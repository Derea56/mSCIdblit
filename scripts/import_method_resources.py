#!/usr/bin/env python3
"""Import the frozen mSCS method resources into an mSCIdblit intake layer.

The importer keeps method-resource membership separate from curated biological
evidence.  It copies small source files losslessly, records large binary files
as checksum-pinned references, emits canonical LR records and native
projections, and writes idempotent PostgreSQL materialization SQL.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
import subprocess
from collections import defaultdict
from datetime import date
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE_ROOT = ROOT.parent / "mSCS" / "data" / "external" / "method_resources" / "phase2_external_snapshot_2026-08-05"
DEFAULT_OUTPUT = ROOT / "data" / "processed" / "method_resource_migration_v1"
DEFAULT_RAW_SNAPSHOT = ROOT / "data" / "raw" / "method_resources" / "mscs_phase2_external_snapshot_2026-08-05"
MAX_COPIED_BYTES = 10_000_000

SOURCE_METHODS = {
    "liana_mouseconsensus.tsv": "liana",
    "cellchat_mouse.tsv": "cellchat",
    "CellChatDB.mouse.rda": "cellchat",
    "CellChatDB.mouse.standalone.json": "cellchat",
    "master_lr_registry.tsv": "registry",
    "master_lr_registry.manifest.json": "registry",
    "resource_manifest.json": "registry",
    "ligand_target_matrix_nsga2r_final_mouse.rds": "nichenet",
    "lr_network_mouse_21122021.rds": "nichenet",
    "ligand_target_matrix.f64le.bin": "nichenet",
    "ligands.tsv": "nichenet",
    "target_genes.tsv": "nichenet",
    "lr_network.tsv": "nichenet",
    "neutral_model_manifest.json": "nichenet",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def json_text(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sql(value: Any) -> str:
    if value is None or value == "":
        return "NULL"
    if isinstance(value, bool):
        return "TRUE" if value else "FALSE"
    if isinstance(value, (int, float)):
        return str(value)
    return "'" + str(value).replace("'", "''") + "'"


def write_tsv(path: Path, fields: list[str], rows: Iterable[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: "" if row.get(field) is None else row.get(field, "") for field in fields})


def read_tsv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        rows = list(reader)
        return list(reader.fieldnames or []), rows


def git_head(repo: Path) -> str | None:
    result = subprocess.run(
        ["git", "-C", str(repo), "rev-parse", "HEAD"],
        capture_output=True,
        text=True,
        check=False,
    )
    return result.stdout.strip() if result.returncode == 0 else None


def tracked(repo: Path, relative_path: Path) -> bool:
    result = subprocess.run(
        ["git", "-C", str(repo), "ls-files", "--error-unmatch", str(relative_path)],
        capture_output=True,
        text=True,
        check=False,
    )
    return result.returncode == 0


def format_for(path: Path) -> str:
    suffix = path.suffix.lower()
    return {
        ".tsv": "tsv",
        ".json": "json",
        ".rda": "rda",
        ".rds": "rds",
        ".bin": "binary",
    }.get(suffix, "other")


def row_count_and_columns(path: Path) -> tuple[int | None, int | None, list[str]]:
    if path.suffix.lower() == ".tsv":
        fields, rows = read_tsv(path)
        return len(rows), len(fields), fields
    if path.name == "CellChatDB.mouse.standalone.json":
        payload = json.loads(path.read_text(encoding="utf-8"))
        interactions = payload.get("interactions", []) if isinstance(payload, dict) else []
        columns = sorted({key for row in interactions if isinstance(row, dict) for key in row})
        return len(interactions), len(columns), columns
    return None, None, []


def resource_metadata(relative: Path, source_root: Path, source_manifest: dict[str, Any], neutral_manifest: dict[str, Any], source_repo: Path) -> dict[str, Any]:
    path = source_root / relative
    name = path.name
    rel_text = relative.as_posix()
    method = SOURCE_METHODS.get(name, "other")
    source_version = None
    source_release = None
    source_url = None
    resource_name = name
    role = "source_snapshot"
    usage = "audit and provenance"
    preprocessing = "No transformation was applied to the source artifact before hashing."
    if name == "liana_mouseconsensus.tsv":
        method_meta = source_manifest.get("liana", {})
        source_version = method_meta.get("package_version")
        resource_name = str(method_meta.get("resource", "mouseconsensus"))
        role = "direct_lr_candidates"
        usage = "candidate discovery and method-native LIANA input"
        preprocessing = "mSCS snapshot table; values are retained exactly. Canonical normalization is whitespace trimming only."
    elif name == "cellchat_mouse.tsv":
        meta = source_manifest.get("cellchat", {})
        source_version = meta.get("source_commit")
        source_url = meta.get("source_url")
        resource_name = "CellChatDB.mouse interaction export"
        role = "native_cellchat_projection"
        usage = "candidate discovery and CellChat-compatible input"
        preprocessing = "Exported from the frozen CellChatDB.mouse RDA; source fields are retained exactly."
    elif name in {"CellChatDB.mouse.rda", "CellChatDB.mouse.standalone.json"}:
        meta = source_manifest.get("cellchat", {})
        source_version = meta.get("source_commit")
        source_url = meta.get("source_url")
        resource_name = "CellChatDB.mouse"
        role = "source_database" if name.endswith(".rda") else "native_cellchat_projection"
        usage = "CellChat native input and audit"
        preprocessing = "RDA is the source database; standalone JSON is an explicit mSCS export of the same interaction, complex, and cofactor content."
    elif name == "master_lr_registry.tsv":
        meta = source_manifest.get("master_lr_registry", {})
        resource_name = "master_mouse_lr_union_v1"
        source_version = meta.get("registry_id")
        role = "canonical_union_compatibility_registry"
        usage = "legacy mSCS compatibility and candidate-union input"
        preprocessing = "Derived mSCS union of the frozen LIANA, NicheNet LR, and CellChat resources; validated against the exact source pair union."
    elif name == "master_lr_registry.manifest.json":
        resource_name = "master_mouse_lr_union_v1 manifest"
        role = "source_manifest"
        usage = "registry provenance and checksum audit"
    elif name == "resource_manifest.json":
        resource_name = "phase2_external_resources_2026-08-05 manifest"
        role = "source_manifest"
        usage = "resource provenance and checksum audit"
    elif name in {"ligand_target_matrix_nsga2r_final_mouse.rds", "lr_network_mouse_21122021.rds"}:
        meta = source_manifest.get("nichenet", {})
        source_version = meta.get("model")
        source_release = meta.get("resource_id")
        resource_name = "NicheNet v2 mouse"
        role = "native_nichenet_numeric_prior" if name.endswith("matrix_nsga2r_final_mouse.rds") else "native_nichenet_lr_resource"
        usage = "NicheNet native input"
        preprocessing = "Frozen NicheNet v2 source file; no RDS reserialization or numerical transformation was applied."
    elif name == "ligand_target_matrix.f64le.bin":
        meta = neutral_manifest
        source_version = meta.get("schema_version")
        source_release = meta.get("source_resource_id")
        resource_name = "NicheNet neutral model"
        role = "numeric_prior_matrix"
        usage = "NicheNet ligand-target scoring and downstream target inference"
        preprocessing = "Deterministic neutral snapshot representation of the frozen NicheNet matrix; float64 little-endian column-major layout is preserved."
    elif name in {"ligands.tsv", "target_genes.tsv", "lr_network.tsv", "neutral_model_manifest.json"}:
        meta = neutral_manifest
        source_version = meta.get("schema_version")
        source_release = meta.get("source_resource_id")
        resource_name = "NicheNet neutral model"
        role = "ligand_axis" if name == "ligands.tsv" else "target_axis" if name == "target_genes.tsv" else "direct_lr_candidates" if name == "lr_network.tsv" else "source_manifest"
        usage = "NicheNet native input and audit"
        preprocessing = "Neutral snapshot metadata/axis table; values are retained exactly."
    else:
        role = "unclassified_snapshot_artifact"
        usage = "audit and provenance only"
        preprocessing = "Present in the frozen source directory but not assigned a method-specific semantic role by the importer."
    rows, columns, column_names = row_count_and_columns(path)
    return {
        "resource_key": f"mscs_phase2:{rel_text}",
        "method_name": method,
        "resource_name": resource_name,
        "resource_role": role,
        "species_scope": "mouse" if method in {"liana", "cellchat", "nichenet", "registry"} else None,
        "source_release": source_release,
        "source_version": source_version,
        "source_url": source_url,
        "primary_citation": None,
        "source_repository": "mSCS",
        "source_repository_commit": git_head(source_repo),
        "source_relative_path": f"data/external/method_resources/phase2_external_snapshot_2026-08-05/{rel_text}",
        "source_artifact_sha256": sha256(path),
        "original_format": format_for(path),
        "imported_on": date.today().isoformat(),
        "row_count": rows,
        "column_count": columns,
        "original_columns_json": json_text(column_names),
        "preprocessing_notes": preprocessing,
        "usage_scope": usage,
        "retention_status": "copied_lossless" if path.stat().st_size <= MAX_COPIED_BYTES else "source_reference_only",
        "source_file_tracked": tracked(source_repo, Path("data/external/method_resources/phase2_external_snapshot_2026-08-05") / relative),
        "source_status": "verified",
        "source_bytes": path.stat().st_size,
    }


def canonical_id(species: str, ligand: str, receptor: str) -> str:
    digest = hashlib.sha256(f"{species}\0{ligand}\0{receptor}".encode("utf-8")).hexdigest()[:24]
    return f"MSCICOMM-{digest}"


def normalized_name(value: str) -> str:
    return value.strip()


def parse_source_records(root: Path) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]], dict[str, Any]]:
    records: list[dict[str, Any]] = []
    components: list[dict[str, Any]] = []
    annotations: list[dict[str, Any]] = []
    by_pair: dict[tuple[str, str, str], dict[str, Any]] = {}
    source_counts: dict[str, int] = {}

    def add_record(resource_key: str, method: str, source_record_key: str, key_kind: str, row: dict[str, str], ligand_field: str, receptor_field: str) -> None:
        ligand = str(row.get(ligand_field, "") or "").strip()
        receptor = str(row.get(receptor_field, "") or "").strip()
        if not ligand or not receptor:
            raise ValueError(f"Empty LR field in {resource_key} record {source_record_key}")
        species = "mouse"
        comm_id = canonical_id(species, ligand, receptor)
        pair = (species, ligand, receptor)
        explicit_ligand_components = [part.strip() for part in str(row.get("ligand_components", "") or "").split("|") if part.strip()]
        explicit_receptor_components = [part.strip() for part in str(row.get("receptor_components", "") or "").split("|") if part.strip()]
        complex_row = bool(len(explicit_ligand_components) > 1 or len(explicit_receptor_components) > 1)
        current = by_pair.setdefault(pair, {
            "canonical_communication_id": comm_id,
            "species_scope": species,
            "ligand_name": ligand,
            "receptor_name": receptor,
            "normalized_ligand_name": normalized_name(ligand),
            "normalized_receptor_name": normalized_name(receptor),
            "communication_kind": "complex_lr_candidate" if complex_row else "direct_lr_candidate",
            "evidence_status": "method_resource_only",
            "source_method_count": 0,
            "source_record_count": 0,
            "source_methods": set(),
            "normalization_notes": "Whitespace trimming only; no synonym, orthology, or biological validation inference.",
        })
        if complex_row:
            current["communication_kind"] = "complex_lr_candidate"
        current["source_record_count"] += 1
        current["source_methods"].add(method)
        records.append({
            "resource_key": resource_key,
            "canonical_communication_id": comm_id,
            "source_record_key": source_record_key,
            "source_record_key_kind": key_kind,
            "record_kind": "complex_lr_candidate" if complex_row else "direct_lr_candidate",
            "native_ligand": row.get(ligand_field, ""),
            "native_receptor": row.get(receptor_field, ""),
            "normalized_ligand": normalized_name(ligand),
            "normalized_receptor": normalized_name(receptor),
            "original_values_json": json_text(row),
            "normalized_values_json": json_text({"ligand": normalized_name(ligand), "receptor": normalized_name(receptor), "species": species}),
            "transform_notes": "Whitespace trimming only; source row retained losslessly in original_values_json.",
            "evidence_status": "method_resource_only",
            "method_score_json": "{}",
        })
        if explicit_ligand_components:
            for ordinal, value in enumerate(explicit_ligand_components, start=1):
                components.append({
                    "resource_key": resource_key,
                    "source_record_key": source_record_key,
                    "record_kind": "complex_lr_candidate" if complex_row else "direct_lr_candidate",
                    "canonical_communication_id": comm_id,
                    "side": "ligand",
                    "component_name": value,
                    "component_ordinal": ordinal,
                    "source_field_name": "ligand_components",
                    "original_component_value": value,
                    "notes": "Explicit CellChat component field; components were not inferred from the ligand name.",
                })
        if explicit_receptor_components:
            for ordinal, value in enumerate(explicit_receptor_components, start=1):
                components.append({
                    "resource_key": resource_key,
                    "source_record_key": source_record_key,
                    "record_kind": "complex_lr_candidate" if complex_row else "direct_lr_candidate",
                    "canonical_communication_id": comm_id,
                    "side": "receptor",
                    "component_name": value,
                    "component_ordinal": ordinal,
                    "source_field_name": "receptor_components",
                    "original_component_value": value,
                    "notes": "Explicit CellChat component field; components were not inferred from the receptor name.",
                })
        annotation_fields = {
            "pathway_name": "pathway",
            "annotation": "annotation",
            "evidence": "source_evidence_label",
            "cofactor_annotations": "cofactor",
        }
        for field, kind in annotation_fields.items():
            raw = str(row.get(field, "") or "").strip()
            if not raw:
                continue
            values = [part.strip() for part in raw.split(";") if part.strip()] if field == "cofactor_annotations" else [raw]
            for value in values:
                annotations.append({
                    "resource_key": resource_key,
                    "source_record_key": source_record_key,
                    "record_kind": "complex_lr_candidate" if complex_row else "direct_lr_candidate",
                    "annotation_kind": kind,
                    "source_field_name": field,
                    "annotation_value": value,
                    "annotation_scope": "method_resource",
                    "notes": "Method-native annotation; not independently adjudicated biological evidence.",
                })
        source_counts[resource_key] = source_counts.get(resource_key, 0) + 1

    liana_path = root / "liana_mouseconsensus.tsv"
    if liana_path.is_file():
        _, rows = read_tsv(liana_path)
        for index, row in enumerate(rows, start=1):
            add_record("mscs_phase2:liana_mouseconsensus.tsv", "liana", f"row:{index:06d}", "generated_row_locator", row, "ligand", "receptor")

    cellchat_path = root / "cellchat_mouse.tsv"
    if cellchat_path.is_file():
        _, rows = read_tsv(cellchat_path)
        seen: set[str] = set()
        for index, row in enumerate(rows, start=1):
            source_key = row.get("source_record_id", "").strip() or f"row:{index:06d}"
            key_kind = "source_record_id" if row.get("source_record_id", "").strip() else "generated_row_locator"
            if source_key in seen:
                raise ValueError(f"Duplicate CellChat source_record_id: {source_key}")
            seen.add(source_key)
            add_record("mscs_phase2:cellchat_mouse.tsv", "cellchat", source_key, key_kind, row, "ligand", "receptor")

    nichenet_path = root / "nichenet_neutral_v1" / "lr_network.tsv"
    if nichenet_path.is_file():
        _, rows = read_tsv(nichenet_path)
        for index, row in enumerate(rows, start=1):
            add_record("mscs_phase2:nichenet_neutral_v1/lr_network.tsv", "nichenet", f"row:{index:06d}", "generated_row_locator", row, "from", "to")

    canonical = []
    for row in sorted(by_pair.values(), key=lambda value: (value["ligand_name"], value["receptor_name"])):
        row = dict(row)
        row["source_method_count"] = len(row["source_methods"])
        row["source_methods_json"] = json_text(sorted(row.pop("source_methods")))
        canonical.append(row)
    return records, components, annotations, {"source_counts": source_counts, "canonical": canonical}


def projection_metadata(source_root: Path, output: Path, resources: list[dict[str, Any]]) -> list[dict[str, Any]]:
    native_root = output / "method_native"
    projections: list[dict[str, Any]] = []
    mapping = {
        "liana_mouseconsensus.tsv": ("liana", "native_input", "liana_mouseconsensus.tsv"),
        "cellchat_mouse.tsv": ("cellchat", "native_input", "cellchat_mouse.tsv"),
        "CellChatDB.mouse.rda": ("cellchat", "native_source", "CellChatDB.mouse.rda"),
        "CellChatDB.mouse.standalone.json": ("cellchat", "native_input", "CellChatDB.mouse.standalone.json"),
        "master_lr_registry.tsv": ("registry", "compatibility_union", "master_lr_registry.tsv"),
        "nichenet_neutral_v1/ligands.tsv": ("nichenet", "native_input", "nichenet_neutral_v1/ligands.tsv"),
        "nichenet_neutral_v1/target_genes.tsv": ("nichenet", "native_input", "nichenet_neutral_v1/target_genes.tsv"),
        "nichenet_neutral_v1/lr_network.tsv": ("nichenet", "native_input", "nichenet_neutral_v1/lr_network.tsv"),
        "nichenet_neutral_v1/neutral_model_manifest.json": ("nichenet", "native_manifest", "nichenet_neutral_v1/neutral_model_manifest.json"),
        "resource_manifest.json": ("registry", "source_manifest", "resource_manifest.json"),
        "master_lr_registry.manifest.json": ("registry", "source_manifest", "master_lr_registry.manifest.json"),
    }
    resource_by_path = {row["source_relative_path"].split("phase2_external_snapshot_2026-08-05/", 1)[-1]: row for row in resources}
    for relative, (method, role, native_relative) in mapping.items():
        source = source_root / relative
        if not source.is_file():
            continue
        resource = resource_by_path[relative]
        destination = native_root / native_relative
        if source.stat().st_size <= MAX_COPIED_BYTES:
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)
            if sha256(destination) != resource["source_artifact_sha256"]:
                raise ValueError(f"Projection copy hash mismatch: {source}")
            projection_path = Path("method_native") / native_relative
            status = "lossless"
        else:
            projection_path = Path("mSCS") / resource["source_relative_path"]
            status = "reference_only"
        rows, columns, column_names = row_count_and_columns(source)
        projections.append({
            "projection_key": f"mscs_phase2:{native_relative}",
            "resource_key": resource["resource_key"],
            "method_name": method,
            "projection_role": role,
            "relative_path": projection_path.as_posix(),
            "projection_format": format_for(source),
            "projection_sha256": resource["source_artifact_sha256"],
            "row_count": rows,
            "column_count": columns,
            "columns_json": json_text(column_names),
            "losslessness_status": status,
            "transformation_notes": "Byte-for-byte copy of the frozen mSCS file." if status == "lossless" else "Exact checksum-pinned reference; binary file is not duplicated in this Git release.",
        })
    # The neutral matrix and both original NicheNet RDS files are explicit
    # projections even though they remain source references because of size.
    for relative, role in (
        ("nichenet_neutral_v1/ligand_target_matrix.f64le.bin", "numeric_prior_matrix"),
        ("nichenet_v2_mouse/ligand_target_matrix_nsga2r_final_mouse.rds", "native_numeric_prior"),
        ("nichenet_v2_mouse/lr_network_mouse_21122021.rds", "native_lr_resource"),
    ):
        source = source_root / relative
        if not source.is_file():
            continue
        resource = resource_by_path[relative]
        native_relative = Path("method_native") / relative
        if source.stat().st_size <= MAX_COPIED_BYTES:
            destination = output / native_relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)
            if sha256(destination) != resource["source_artifact_sha256"]:
                raise ValueError(f"Projection copy hash mismatch: {source}")
            projection_path = native_relative
            status = "lossless"
        else:
            projection_path = Path("mSCS") / resource["source_relative_path"]
            status = "reference_only"
        projections.append({
            "projection_key": f"mscs_phase2:{relative}",
            "resource_key": resource["resource_key"],
            "method_name": "nichenet",
            "projection_role": role,
            "relative_path": projection_path.as_posix(),
            "projection_format": format_for(source),
            "projection_sha256": resource["source_artifact_sha256"],
            "row_count": resource["row_count"],
            "column_count": resource["column_count"],
            "columns_json": resource["original_columns_json"],
            "losslessness_status": status,
            "transformation_notes": "Byte-for-byte copy of the frozen mSCS file." if status == "lossless" else "Exact checksum-pinned reference; binary/RDS file is not duplicated in this Git release.",
        })
    return projections


def numeric_artifacts(source_root: Path, resources: list[dict[str, Any]], neutral_manifest: dict[str, Any]) -> list[dict[str, Any]]:
    resource_by_path = {row["source_relative_path"].split("phase2_external_snapshot_2026-08-05/", 1)[-1]: row for row in resources}
    rows: list[dict[str, Any]] = []
    matrix_rel = "nichenet_neutral_v1/ligand_target_matrix.f64le.bin"
    if (source_root / matrix_rel).is_file():
        resource = resource_by_path[matrix_rel]
        rows.append({
            "resource_key": resource["resource_key"],
            "artifact_key": "nichenet_neutral_v1_ligand_target_matrix",
            "artifact_kind": "ligand_target_prior_matrix",
            "storage_path": f"mSCS/{resource['source_relative_path']}",
            "storage_status": "source_reference_only",
            "artifact_sha256": resource["source_artifact_sha256"],
            "byte_size": resource["source_bytes"],
            "dtype": neutral_manifest.get("matrix_dtype"),
            "endianness": neutral_manifest.get("matrix_endianness"),
            "layout": neutral_manifest.get("matrix_layout"),
            "shape_json": json_text(neutral_manifest.get("matrix_shape")),
            "axis_artifacts_json": json_text([neutral_manifest.get("target_axis_file"), neutral_manifest.get("ligand_axis_file")]),
            "source_model_version": neutral_manifest.get("source_model"),
            "notes": "The exact dense numerical prior remains available by checksum-pinned source reference; relational expansion is a documented migration gap.",
        })
    return rows


def emit_sql(output: Path, resources: list[dict[str, Any]], canonical: list[dict[str, Any]], records: list[dict[str, Any]], components: list[dict[str, Any]], annotations: list[dict[str, Any]], projections: list[dict[str, Any]], numeric: list[dict[str, Any]]) -> None:
    lines = [
        "-- Generated by scripts/import_method_resources.py.",
        "-- Apply schema/method_resource_layer.sql first.",
        "BEGIN;",
    ]
    for row in resources:
        fields = [
            "resource_key", "method_name", "resource_name", "resource_role", "species_scope",
            "source_release", "source_version", "source_url", "primary_citation", "source_repository",
            "source_repository_commit", "source_relative_path", "source_artifact_sha256", "original_format",
            "imported_on", "row_count", "column_count", "original_columns_json", "preprocessing_notes",
            "usage_scope", "retention_status", "source_file_tracked", "source_status",
        ]
        values = [row.get(field) for field in fields]
        lines.append(
            "INSERT INTO MethodResource (" + ", ".join(fields) + ") VALUES (" + ", ".join(sql(value) for value in values) + ") "
            "ON CONFLICT (resource_key) DO UPDATE SET " + ", ".join(f"{field}=EXCLUDED.{field}" for field in fields[1:]) + ";"
        )
    for row in canonical:
        fields = ["canonical_communication_id", "species_scope", "ligand_name", "receptor_name", "normalized_ligand_name", "normalized_receptor_name", "communication_kind", "evidence_status", "source_method_count", "source_record_count", "source_methods_json", "normalization_notes"]
        lines.append(
            "INSERT INTO CanonicalCommunicationRecord (" + ", ".join(fields) + ") VALUES (" + ", ".join(sql(row.get(field)) for field in fields) + ") "
            "ON CONFLICT (canonical_communication_id) DO UPDATE SET " + ", ".join(f"{field}=EXCLUDED.{field}" for field in fields[1:]) + ";"
        )
    for row in records:
        fields = ["method_resource_id", "canonical_communication_id", "source_record_key", "source_record_key_kind", "record_kind", "native_ligand", "native_receptor", "normalized_ligand", "normalized_receptor", "original_values_json", "normalized_values_json", "transform_notes", "evidence_status", "method_score_json"]
        values = [f"(SELECT method_resource_id FROM MethodResource WHERE resource_key={sql(row['resource_key'])})"] + [sql(row.get(field)) for field in fields[1:]]
        lines.append(
            "INSERT INTO MethodResourceRecord (" + ", ".join(fields) + ") VALUES (" + ", ".join(values) + ") "
            "ON CONFLICT (method_resource_id, source_record_key, record_kind) DO UPDATE SET " + ", ".join(f"{field}=EXCLUDED.{field}" for field in fields[5:]) + ";"
        )
    record_id_sql = lambda row: f"(SELECT method_resource_record_id FROM MethodResourceRecord WHERE method_resource_id=(SELECT method_resource_id FROM MethodResource WHERE resource_key={sql(row['resource_key'])}) AND source_record_key={sql(row['source_record_key'])} AND record_kind={sql(row['record_kind'])})"
    for row in components:
        fields = ["method_resource_record_id", "canonical_communication_id", "side", "component_name", "component_ordinal", "source_field_name", "original_component_value", "notes"]
        values = [record_id_sql(row), sql(row["canonical_communication_id"]), sql(row["side"]), sql(row["component_name"]), sql(row["component_ordinal"]), sql(row["source_field_name"]), sql(row["original_component_value"]), sql(row["notes"])]
        lines.append(
            "INSERT INTO MethodResourceComplexComponent (" + ", ".join(fields) + ") VALUES (" + ", ".join(values) + ") "
            "ON CONFLICT (method_resource_record_id, side, component_ordinal) DO UPDATE SET component_name=EXCLUDED.component_name, source_field_name=EXCLUDED.source_field_name, original_component_value=EXCLUDED.original_component_value, notes=EXCLUDED.notes;"
        )
    for row in annotations:
        fields = ["method_resource_record_id", "annotation_kind", "source_field_name", "annotation_value", "annotation_scope", "notes"]
        values = [record_id_sql(row), sql(row["annotation_kind"]), sql(row["source_field_name"]), sql(row["annotation_value"]), sql(row["annotation_scope"]), sql(row["notes"])]
        lines.append(
            "INSERT INTO MethodResourceAnnotation (" + ", ".join(fields) + ") VALUES (" + ", ".join(values) + ") "
            "ON CONFLICT (method_resource_record_id, annotation_kind, source_field_name, annotation_value) DO UPDATE SET annotation_scope=EXCLUDED.annotation_scope, notes=EXCLUDED.notes;"
        )
    for row in projections:
        fields = ["projection_key", "method_resource_id", "method_name", "projection_role", "relative_path", "projection_format", "projection_sha256", "row_count", "column_count", "columns_json", "losslessness_status", "transformation_notes"]
        values = [sql(row["projection_key"]), f"(SELECT method_resource_id FROM MethodResource WHERE resource_key={sql(row['resource_key'])})"] + [sql(row.get(field)) for field in fields[2:]]
        lines.append(
            "INSERT INTO MethodResourceProjection (" + ", ".join(fields) + ") VALUES (" + ", ".join(values) + ") "
            "ON CONFLICT (projection_key) DO UPDATE SET " + ", ".join(f"{field}=EXCLUDED.{field}" for field in fields[1:]) + ";"
        )
    for row in numeric:
        fields = ["method_resource_id", "artifact_key", "artifact_kind", "storage_path", "storage_status", "artifact_sha256", "byte_size", "dtype", "endianness", "layout", "shape_json", "axis_artifacts_json", "source_model_version", "notes"]
        values = [f"(SELECT method_resource_id FROM MethodResource WHERE resource_key={sql(row['resource_key'])})"] + [sql(row.get(field)) for field in fields[1:]]
        lines.append(
            "INSERT INTO MethodResourceNumericArtifact (" + ", ".join(fields) + ") VALUES (" + ", ".join(values) + ") "
            "ON CONFLICT (method_resource_id, artifact_key) DO UPDATE SET " + ", ".join(f"{field}=EXCLUDED.{field}" for field in fields[2:]) + ";"
        )
    lines.append("COMMIT;")
    (output / "method_resource_materialization.sql").write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, default=DEFAULT_SOURCE_ROOT)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--raw-snapshot-dir", type=Path, default=DEFAULT_RAW_SNAPSHOT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source_root = args.source_root.resolve()
    output = args.output_dir.resolve()
    raw_snapshot = args.raw_snapshot_dir.resolve()
    if not source_root.is_dir():
        raise SystemExit(f"Source resource directory does not exist: {source_root}")
    source_manifest = json.loads((source_root / "resource_manifest.json").read_text(encoding="utf-8"))
    neutral_manifest = json.loads((source_root / "nichenet_neutral_v1" / "neutral_model_manifest.json").read_text(encoding="utf-8"))
    source_repo = source_root.parents[4]
    files = sorted(path for path in source_root.rglob("*") if path.is_file())
    resources: list[dict[str, Any]] = []
    snapshot_rows: list[dict[str, Any]] = []
    for path in files:
        relative = path.relative_to(source_root)
        resource = resource_metadata(relative, source_root, source_manifest, neutral_manifest, source_repo)
        resources.append(resource)
        copied_path = raw_snapshot / relative
        copied = path.stat().st_size <= MAX_COPIED_BYTES
        if copied:
            copied_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, copied_path)
            if sha256(copied_path) != resource["source_artifact_sha256"]:
                raise SystemExit(f"Source snapshot hash mismatch after copy: {relative}")
        snapshot_rows.append({
            "resource_key": resource["resource_key"],
            "source_relative_path": resource["source_relative_path"],
            "source_bytes": resource["source_bytes"],
            "source_sha256": resource["source_artifact_sha256"],
            "source_format": resource["original_format"],
            "source_repository": resource["source_repository"],
            "source_repository_commit": resource["source_repository_commit"],
            "source_file_tracked": str(resource["source_file_tracked"]).lower(),
            "retention_status": resource["retention_status"],
            "copied_snapshot_path": str(Path("data/raw/method_resources/mscs_phase2_external_snapshot_2026-08-05") / relative) if copied else "",
            "reference_path": resource["source_relative_path"] if not copied else "",
            "notes": "Byte-for-byte local source snapshot." if copied else "Exact local source was hashed but not copied because it exceeds the migration copy limit.",
        })

    records, components, annotations, parsed = parse_source_records(source_root)
    canonical = parsed["canonical"]
    registry_fields, registry_rows = read_tsv(source_root / "master_lr_registry.tsv")
    registry_pairs = {(row["ligand"].strip(), row["receptor"].strip()) for row in registry_rows}
    canonical_pairs = {(row["ligand_name"], row["receptor_name"]) for row in canonical}
    if registry_pairs != canonical_pairs:
        raise SystemExit(f"Master registry mismatch: canonical-only={len(canonical_pairs - registry_pairs)} registry-only={len(registry_pairs - canonical_pairs)}")
    projections = projection_metadata(source_root, output, resources)
    numeric = numeric_artifacts(source_root, resources, neutral_manifest)

    output.mkdir(parents=True, exist_ok=True)
    write_tsv(output / "source_snapshot_manifest.tsv", [
        "resource_key", "source_relative_path", "source_bytes", "source_sha256", "source_format",
        "source_repository", "source_repository_commit", "source_file_tracked", "retention_status",
        "copied_snapshot_path", "reference_path", "notes",
    ], snapshot_rows)
    write_tsv(output / "canonical_communication_records.tsv", [
        "canonical_communication_id", "species_scope", "ligand_name", "receptor_name",
        "normalized_ligand_name", "normalized_receptor_name", "communication_kind", "evidence_status",
        "source_method_count", "source_record_count", "source_methods_json", "normalization_notes",
    ], canonical)
    write_tsv(output / "method_resource_records.tsv", [
        "resource_key", "canonical_communication_id", "source_record_key", "source_record_key_kind",
        "record_kind", "native_ligand", "native_receptor", "normalized_ligand", "normalized_receptor",
        "original_values_json", "normalized_values_json", "transform_notes", "evidence_status", "method_score_json",
    ], records)
    write_tsv(output / "method_resource_complex_components.tsv", [
        "resource_key", "source_record_key", "record_kind", "canonical_communication_id", "side",
        "component_name", "component_ordinal", "source_field_name", "original_component_value", "notes",
    ], components)
    write_tsv(output / "method_resource_annotations.tsv", [
        "resource_key", "source_record_key", "record_kind", "annotation_kind", "source_field_name",
        "annotation_value", "annotation_scope", "notes",
    ], annotations)
    write_tsv(output / "method_resource_projections.tsv", [
        "projection_key", "resource_key", "method_name", "projection_role", "relative_path",
        "projection_format", "projection_sha256", "row_count", "column_count", "columns_json",
        "losslessness_status", "transformation_notes",
    ], projections)
    write_tsv(output / "method_resource_numeric_artifacts.tsv", [
        "resource_key", "artifact_key", "artifact_kind", "storage_path", "storage_status", "artifact_sha256",
        "byte_size", "dtype", "endianness", "layout", "shape_json", "axis_artifacts_json",
        "source_model_version", "notes",
    ], numeric)
    write_tsv(output / "method_resource_manifest.tsv", [
        "resource_key", "method_name", "resource_name", "resource_role", "species_scope", "source_release",
        "source_version", "source_url", "primary_citation", "source_repository", "source_repository_commit",
        "source_relative_path", "source_artifact_sha256", "original_format", "imported_on", "row_count",
        "column_count", "original_columns_json", "preprocessing_notes", "usage_scope", "retention_status",
        "source_file_tracked", "source_status",
    ], resources)
    emit_sql(output, resources, canonical, records, components, annotations, projections, numeric)

    report = {
        "schema_version": "method_resource_migration_v1",
        "source_snapshot_id": "phase2_external_snapshot_2026-08-05",
        "source_root": "mSCS/data/external/method_resources/phase2_external_snapshot_2026-08-05",
        "source_repository": "mSCS",
        "source_repository_commit": git_head(source_repo),
        "source_files": len(resources),
        "copied_source_files": sum(row["retention_status"] == "copied_lossless" for row in resources),
        "reference_only_source_files": sum(row["retention_status"] == "source_reference_only" for row in resources),
        "canonical_communication_count": len(canonical),
        "method_resource_record_count": len(records),
        "complex_component_count": len(components),
        "annotation_count": len(annotations),
        "projection_count": len(projections),
        "numeric_artifact_count": len(numeric),
        "method_resource_record_counts": parsed["source_counts"],
        "master_registry_pair_count": len(registry_pairs),
        "master_registry_matches_canonical_union": True,
        "biological_validation_created": False,
        "mechanism_edges_created": False,
        "migration_gaps": [
            "The large NicheNet v2 ligand-target RDS file and the 221 MiB neutral ligand-target matrix remain checksum-pinned references rather than Git-copied binaries.",
            "No local Paper, Observation, AuthorClaim, or SignalingEdge rows are created by this resource import.",
            "LIANA source URL/citation is not present in the frozen mSCS manifest and remains null.",
            "No frozen Tensor-cell2cell resource was present in the inspected mSCS method-resource directory; no Tensor projection was created.",
        ],
    }
    (output / "method_resource_migration_report.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
