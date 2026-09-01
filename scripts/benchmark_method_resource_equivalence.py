#!/usr/bin/env python3
"""Benchmark frozen mSCS resources against the mSCIdblit projections."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE_ROOT = ROOT.parent / "mSCS" / "data" / "external" / "method_resources" / "phase2_external_snapshot_2026-08-05"
DEFAULT_MIGRATION = ROOT / "data" / "processed" / "method_resource_migration_v1"
DEFAULT_OUTPUT = DEFAULT_MIGRATION / "method_resource_equivalence_report.json"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_tsv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        return list(reader.fieldnames or []), list(reader)


def row_signature(row: dict[str, str], fields: list[str]) -> tuple[str, ...]:
    return tuple(row.get(field, "") for field in fields)


def compare_file(
    source: Path,
    projection: Path,
    fields: list[str] | None = None,
    *,
    source_label: str | None = None,
    projection_label: str | None = None,
) -> dict[str, Any]:
    source_hash = sha256(source)
    result: dict[str, Any] = {
        "source_path": source_label or str(source),
        "projection_path": projection_label or str(projection),
        "source_sha256": source_hash,
        "projection_exists": projection.is_file(),
        "projection_sha256": sha256(projection) if projection.is_file() else None,
        "checksum_match": projection.is_file() and source_hash == sha256(projection),
        "status": "lossless" if projection.is_file() and source_hash == sha256(projection) else "reference_only",
    }
    if not projection.is_file() or source.suffix.lower() != ".tsv":
        return result
    source_fields, source_rows = read_tsv(source)
    projection_fields, projection_rows = read_tsv(projection)
    compare_fields = fields or source_fields
    source_sigs = Counter(row_signature(row, compare_fields) for row in source_rows)
    projection_sigs = Counter(row_signature(row, compare_fields) for row in projection_rows)
    result.update({
        "source_row_count": len(source_rows),
        "projection_row_count": len(projection_rows),
        "source_columns": source_fields,
        "projection_columns": projection_fields,
        "column_correspondence": source_fields == projection_fields,
        "records_present_in_both": sum((source_sigs & projection_sigs).values()),
        "records_only_in_source": sum((source_sigs - projection_sigs).values()),
        "records_only_in_projection": sum((projection_sigs - source_sigs).values()),
        "duplicate_source_records": sum(count - 1 for count in source_sigs.values() if count > 1),
        "duplicate_projection_records": sum(count - 1 for count in projection_sigs.values() if count > 1),
    })
    return result


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, default=DEFAULT_SOURCE_ROOT)
    parser.add_argument("--migration-dir", type=Path, default=DEFAULT_MIGRATION)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source = args.source_root.resolve()
    migration = args.migration_dir.resolve()
    comparisons = []
    for relative in (
        "liana_mouseconsensus.tsv",
        "cellchat_mouse.tsv",
        "CellChatDB.mouse.rda",
        "CellChatDB.mouse.standalone.json",
        "master_lr_registry.tsv",
        "nichenet_neutral_v1/ligands.tsv",
        "nichenet_neutral_v1/target_genes.tsv",
        "nichenet_neutral_v1/lr_network.tsv",
        "nichenet_neutral_v1/neutral_model_manifest.json",
        "nichenet_v2_mouse/ligand_target_matrix_nsga2r_final_mouse.rds",
        "nichenet_v2_mouse/lr_network_mouse_21122021.rds",
        "nichenet_neutral_v1/ligand_target_matrix.f64le.bin",
    ):
        source_path = source / relative
        if not source_path.is_file():
            continue
        if relative.endswith(".tsv") or relative.endswith(".json"):
            native_relative = Path("method_native") / relative
        elif relative == "CellChatDB.mouse.rda":
            native_relative = Path("method_native") / relative
        else:
            native_relative = Path("method_native") / relative
        projected_path = migration / native_relative
        projection_label = (
            (Path("data/processed/method_resource_migration_v1") / native_relative).as_posix()
            if projected_path.is_file()
            else (Path("mSCS") / "data/external/method_resources/phase2_external_snapshot_2026-08-05" / relative).as_posix()
        )
        comparisons.append(compare_file(
            source_path,
            projected_path,
            source_label=(Path("mSCS") / "data/external/method_resources/phase2_external_snapshot_2026-08-05" / relative).as_posix(),
            projection_label=projection_label,
        ))

    records_fields, records = read_tsv(migration / "method_resource_records.tsv")
    normalization_changed = sum(
        row.get("native_ligand", "") != row.get("normalized_ligand", "")
        or row.get("native_receptor", "") != row.get("normalized_receptor", "")
        for row in records
    )
    components_fields, components = read_tsv(migration / "method_resource_complex_components.tsv")
    annotations_fields, annotations = read_tsv(migration / "method_resource_annotations.tsv")
    projections_fields, projections = read_tsv(migration / "method_resource_projections.tsv")
    report = {
        "schema_version": "method_resource_equivalence_benchmark_v1",
        "source_root": "mSCS/data/external/method_resources/phase2_external_snapshot_2026-08-05",
        "migration_dir": "data/processed/method_resource_migration_v1",
        "comparisons": comparisons,
        "summary": {
            "comparison_count": len(comparisons),
            "lossless_checksum_matches": sum(row["status"] == "lossless" for row in comparisons),
            "reference_only_comparisons": sum(row["status"] == "reference_only" for row in comparisons),
            "source_only_record_total": sum(row.get("records_only_in_source", 0) for row in comparisons),
            "projection_only_record_total": sum(row.get("records_only_in_projection", 0) for row in comparisons),
            "normalization_changed_record_count": normalization_changed,
            "complex_component_row_count": len(components),
            "annotation_row_count": len(annotations),
            "projection_manifest_row_count": len(projections),
            "all_lossless_projection_comparisons_exact": all(
                row["status"] != "lossless"
                or (
                    row.get("checksum_match")
                    and row.get("records_only_in_source", 0) == 0
                    and row.get("records_only_in_projection", 0) == 0
                    and row.get("column_correspondence", True)
                )
                for row in comparisons
            ),
        },
        "interpretation": {
            "resource_membership_is_not_biological_validation": True,
            "complex_representation": "Explicit CellChat component fields are preserved in method_resource_complex_components.tsv; no complexes are inferred from punctuation in names.",
            "numeric_prior": "The dense NicheNet matrix is checked by exact source checksum and represented by axis/layout metadata; it is not expanded into 28.9 million relational rows.",
            "analytical_equivalence": "Not claimed. Method-output parity requires matching software, resource, parameters, and input data and is outside this resource-level benchmark.",
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report["summary"], indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
