#!/usr/bin/env python3
"""Fail-closed validation for the additive species-aware gene crosswalk release."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path
from typing import Any

try:
    from nichenet_release_contract import CONTRACT_RELATIVE, validate_contract
    from tf_target_prior_contract import PRIOR_MANIFEST, validate_prior_manifest
except ModuleNotFoundError:  # Imported as scripts.validate_mscs_gene_identifier_release in tests.
    from scripts.nichenet_release_contract import CONTRACT_RELATIVE, validate_contract
    from scripts.tf_target_prior_contract import PRIOR_MANIFEST, validate_prior_manifest


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BUNDLE = ROOT / "data/processed/mscs_release_bundle_v1_8_0_nichenet_tf_prior_gene_identifiers_v2"
DEFAULT_PARENT = ROOT / "data/processed/mscs_release_bundle_v1_7_0_nichenet_tf_prior_v1"
GENE_DIR = Path("gene_identifier_crosswalk")
GENE_MANIFEST = GENE_DIR / "gene_identifier_crosswalk_manifest.json"
ALLOWED_MAPPING_STATUSES = {
    "resolved_source_canonical",
    "resolved_source_alias",
    "ambiguous_source_alias",
    "unresolved_source_symbol",
    "explicit_orthology_one_to_one",
    "explicit_orthology_one_to_many",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_tsv(path: Path) -> list[dict[str, str]]:
    if not path.is_file():
        raise ValueError(f"missing TSV: {path}")
    csv.field_size_limit(max(csv.field_size_limit(), 10_000_000))
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def _check_files(root: Path, files: dict[str, Any]) -> None:
    for relative, expected in files.items():
        path = root / relative
        if not path.is_file():
            raise ValueError(f"missing manifest file: {relative}")
        if sha256(path) != expected.get("sha256") or path.stat().st_size != int(expected.get("bytes", -1)):
            raise ValueError(f"checksum/size mismatch: {relative}")


def validate_gene_crosswalk_artifact(crosswalk_dir: Path) -> dict[str, int]:
    """Validate one standalone crosswalk artifact and return its counts."""
    manifest_path = crosswalk_dir / "gene_identifier_crosswalk_manifest.json"
    if not manifest_path.is_file():
        raise ValueError(f"missing gene crosswalk manifest: {manifest_path}")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("schema_version") != "gene_identifier_crosswalk_v1":
        raise ValueError("unsupported gene crosswalk schema")
    species = manifest.get("species")
    if species != {"human": {"tax_id": "9606"}, "mouse": {"tax_id": "10090"}}:
        raise ValueError("gene crosswalk species/taxonomy block is not explicit")
    if "casefold" not in str(manifest.get("lookup_normalization", "")):
        raise ValueError("gene crosswalk does not declare case-normalized lookup")
    _check_files(crosswalk_dir, manifest.get("files", {}))

    catalogs = read_tsv(crosswalk_dir / "gene_catalog.tsv")
    crosswalk = read_tsv(crosswalk_dir / "gene_crosswalk.tsv")
    orthology = read_tsv(crosswalk_dir / "gene_orthology.tsv")
    audit_path = crosswalk_dir / "gene_label_coverage_audit.tsv"
    catalog_required = {"species", "tax_id", "entrez_gene_id", "canonical_symbol", "source_record_id", "source_sha256"}
    crosswalk_required = {"crosswalk_id", "query_symbol", "lookup_key", "query_species_scope", "species", "mapping_status", "entrez_gene_id", "source_record_id", "source_registry_sha256"}
    orthology_required = {"orthology_record_id", "mouse_entrez_gene_id", "human_entrez_gene_id", "mapping_cardinality", "source_sha256"}
    if not catalogs or not catalog_required.issubset(catalogs[0]):
        raise ValueError("gene catalog columns are incomplete")
    if not crosswalk or not crosswalk_required.issubset(crosswalk[0]):
        raise ValueError("gene crosswalk columns are incomplete")
    if not orthology or not orthology_required.issubset(orthology[0]):
        raise ValueError("gene orthology columns are incomplete")

    catalog_keys = {(row["species"], row["entrez_gene_id"]) for row in catalogs}
    if len(catalog_keys) != len(catalogs) or any(row["species"] not in species or not row["canonical_symbol"] for row in catalogs):
        raise ValueError("gene catalog contains duplicate or incomplete source records")
    crosswalk_ids = [row["crosswalk_id"] for row in crosswalk]
    if len(set(crosswalk_ids)) != len(crosswalk_ids):
        raise ValueError("gene crosswalk contains duplicate crosswalk IDs")
    source_hashes = {item.get("sha256") for item in manifest.get("source_inputs", [])}
    if not source_hashes or any(row["source_registry_sha256"] and row["source_registry_sha256"] not in source_hashes for row in crosswalk):
        raise ValueError("gene crosswalk contains an unpinned source checksum")
    for row in crosswalk:
        if row["lookup_key"] != row["query_symbol"].casefold():
            raise ValueError("gene crosswalk lookup key is not the casefold of the query symbol")
        if row["species"] not in species or row["mapping_status"] not in ALLOWED_MAPPING_STATUSES:
            raise ValueError("gene crosswalk contains an unknown species or mapping status")
        if row["mapping_status"].startswith("unresolved_"):
            if row["entrez_gene_id"] or row["source_record_id"]:
                raise ValueError("unresolved mapping selected a source record")
        elif (row["species"], row["entrez_gene_id"]) not in catalog_keys:
            raise ValueError("resolved mapping points outside the source catalog")
    orthology_ids = [row["orthology_record_id"] for row in orthology]
    if len(set(orthology_ids)) != len(orthology_ids):
        raise ValueError("gene orthology contains duplicate record IDs")
    for row in orthology:
        if ("mouse", row["mouse_entrez_gene_id"]) not in catalog_keys or ("human", row["human_entrez_gene_id"]) not in catalog_keys:
            raise ValueError("orthology row points outside the source catalogs")
        if row["mapping_cardinality"] not in {"one_to_one", "one_to_many"}:
            raise ValueError("orthology row has unknown cardinality")

    if audit_path.is_file():
        audit = read_tsv(audit_path)
        required_audit = {
            "label_audit_id", "label", "label_kind", "query_species_scope", "source_records_json",
            "mouse_mapping_status", "mouse_entrez_gene_ids", "human_mapping_status",
            "human_entrez_gene_ids", "unresolved_mapping_reason",
        }
        if not audit or not required_audit.issubset(audit[0]):
            raise ValueError("gene label audit columns are incomplete")
        audit_ids = [row["label_audit_id"] for row in audit]
        if len(set(audit_ids)) != len(audit_ids):
            raise ValueError("gene label audit contains duplicate IDs")
        allowed_audit_statuses = {"uniquely_mapped_source_gene", "multiple_source_mappings", "ambiguous_source_alias", "unresolved_source_symbol"}
        for row in audit:
            if row["label_kind"] not in {"candidate_universe_label", "candidate_component_label", "validated_output_product_label"}:
                raise ValueError("gene label audit contains an unknown label kind")
            if row["mouse_mapping_status"] not in allowed_audit_statuses or row["human_mapping_status"] not in allowed_audit_statuses:
                raise ValueError("gene label audit contains an unknown mapping status")
            for field, species in (("mouse_entrez_gene_ids", "mouse"), ("human_entrez_gene_ids", "human")):
                for entrez_id in filter(None, row[field].split("|")):
                    if (species, entrez_id) not in catalog_keys:
                        raise ValueError("gene label audit points outside the source catalog")
        if counts := manifest.get("counts", {}):
            expected_audit_counts = {
                "active_release_label_audit_rows": len(audit),
                "active_release_output_product_labels_total": sum(row["label_kind"] == "validated_output_product_label" for row in audit),
                "active_release_output_product_labels_mouse_unique": sum(row["label_kind"] == "validated_output_product_label" and row["mouse_mapping_status"] == "uniquely_mapped_source_gene" for row in audit),
                "active_release_output_product_labels_mouse_ambiguous": sum(row["label_kind"] == "validated_output_product_label" and row["mouse_mapping_status"] in {"ambiguous_source_alias", "multiple_source_mappings"} for row in audit),
                "active_release_output_product_labels_mouse_unresolved": sum(row["label_kind"] == "validated_output_product_label" and row["mouse_mapping_status"] == "unresolved_source_symbol" for row in audit),
                "active_release_candidate_labels_total": sum(row["label_kind"] == "candidate_universe_label" for row in audit),
                "active_release_candidate_components_total": sum(row["label_kind"] == "candidate_component_label" for row in audit),
            }
            for key, value in expected_audit_counts.items():
                if counts.get(key) != value:
                    raise ValueError(f"gene label audit count mismatch for {key}: {counts.get(key)} != {value}")

    if "nichenet_target_ids_total" in counts:
        target_keys: dict[tuple[str, str], set[str]] = {}
        target_ambiguous: set[tuple[str, str]] = set()
        for row in crosswalk:
            if row.get("species") != "mouse" or row.get("query_species_scope") != "mouse" or row.get("mapping_status") not in {"resolved_source_canonical", "resolved_source_alias", "ambiguous_source_alias"}:
                continue
            sources = json.loads(row.get("query_sources_json", "[]"))
            if not any(source.get("source") == "nichenet_target_axis" for source in sources):
                continue
            key = (row["query_symbol"], row["query_species_scope"])
            target_keys.setdefault(key, set()).add(row.get("entrez_gene_id", ""))
            if row.get("mapping_status") == "ambiguous_source_alias":
                target_ambiguous.add(key)
        target_total = len(target_keys)
        target_unique = sum(len(ids) == 1 and key not in target_ambiguous for key, ids in target_keys.items())
        target_ambiguous_count = len(target_ambiguous)
        target_unresolved = int(counts["nichenet_target_ids_total"]) - target_total
        expected_target_counts = {
            "nichenet_target_ids_total": target_total + target_unresolved,
            "nichenet_target_ids_mouse_unique": target_unique,
            "nichenet_target_ids_mouse_ambiguous": target_ambiguous_count,
            "nichenet_target_ids_mouse_unresolved": target_unresolved,
        }
        for key, value in expected_target_counts.items():
            if counts.get(key) != value:
                raise ValueError(f"NicheNet target count mismatch for {key}: {counts.get(key)} != {value}")

    counts = manifest.get("counts", {})
    expected = {
        "mouse_catalog_records": sum(row["species"] == "mouse" for row in catalogs),
        "human_catalog_records": sum(row["species"] == "human" for row in catalogs),
        "crosswalk_rows": len(crosswalk),
        "crosswalk_resolved_rows": sum(row["mapping_status"].startswith("resolved_") for row in crosswalk),
        "crosswalk_ambiguous_rows": sum(row["mapping_status"].startswith("ambiguous_") for row in crosswalk),
        "crosswalk_unresolved_rows": sum(row["mapping_status"].startswith("unresolved_") for row in crosswalk),
        "crosswalk_orthology_rows": sum(row["mapping_status"].startswith("explicit_orthology_") for row in crosswalk),
        "orthology_rows": len(orthology),
    }
    for key, value in expected.items():
        if counts.get(key) != value:
            raise ValueError(f"gene crosswalk count mismatch for {key}: {counts.get(key)} != {value}")
    status_counts = {}
    for row in crosswalk:
        status_counts[row["mapping_status"]] = status_counts.get(row["mapping_status"], 0) + 1
    if counts.get("crosswalk_by_mapping_status") != dict(sorted(status_counts.items())):
        raise ValueError("gene crosswalk mapping-status counts do not match")
    return expected


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle-dir", type=Path, default=DEFAULT_BUNDLE)
    parser.add_argument("--parent-release-dir", type=Path, default=DEFAULT_PARENT)
    parser.add_argument("--nichenet-artifact-root", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    bundle = args.bundle_dir.resolve()
    parent = args.parent_release_dir.resolve()
    manifest_path = bundle / "release_manifest.json"
    if not manifest_path.is_file():
        raise SystemExit(f"missing release manifest: {manifest_path}")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("schema_version") != "mscs_release_bundle_v1":
        raise SystemExit("unsupported mSCS release bundle schema")
    parent_manifest_path = parent / "release_manifest.json"
    if not parent_manifest_path.is_file() or manifest.get("parent_release_id") != json.loads(parent_manifest_path.read_text(encoding="utf-8")).get("release_id"):
        raise SystemExit("gene-identifier release does not identify the expected parent release")
    if manifest.get("gene_identifier_crosswalk_manifest") != GENE_MANIFEST.as_posix():
        raise SystemExit("release manifest does not point to the gene crosswalk manifest")
    if manifest.get("gene_label_coverage_audit") != (GENE_DIR / "gene_label_coverage_audit.tsv").as_posix():
        raise SystemExit("release manifest does not point to the active-label audit")
    if manifest.get("gene_identifier_contract", {}).get("orthology_inference") is not False:
        raise SystemExit("gene release does not explicitly disable inferred orthology")
    _check_files(bundle, manifest.get("files", {}))
    try:
        nichenet_summary = validate_contract(bundle=bundle, companion_artifact_root=args.nichenet_artifact_root.resolve())
        prior_summary = validate_prior_manifest(bundle)
        gene_summary = validate_gene_crosswalk_artifact(bundle / GENE_DIR)
    except ValueError as exc:
        raise SystemExit(f"nested release validation failed: {exc}") from exc
    except (SystemExit, json.JSONDecodeError) as exc:
        raise SystemExit(f"nested release validation failed: {exc}") from exc
    print(json.dumps({
        "status": "PASS additive mSCS gene-identifier release validation",
        "release_id": manifest.get("release_id"),
        "parent_release_id": manifest.get("parent_release_id"),
        "manifest_files_checked": len(manifest.get("files", {})),
        "gene_crosswalk": gene_summary,
        "nichenet": nichenet_summary,
        "tf_target_prior": prior_summary,
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
