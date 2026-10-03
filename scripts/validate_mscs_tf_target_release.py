#!/usr/bin/env python3
"""Fail-closed validation for the additive mSCS TF-target prior release."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path

try:
    from nichenet_release_contract import CONTRACT_RELATIVE, validate_contract
    from tf_target_prior_contract import PRIOR_MANIFEST, validate_prior_manifest
except ModuleNotFoundError:  # Imported as scripts.validate_mscs_tf_target_release in tests.
    from scripts.nichenet_release_contract import CONTRACT_RELATIVE, validate_contract
    from scripts.tf_target_prior_contract import PRIOR_MANIFEST, validate_prior_manifest


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BUNDLE = ROOT / "data/processed/mscs_release_bundle_v1_8_0_nichenet_tf_prior_candidate_components_v1"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_tsv(path: Path) -> list[dict[str, str]]:
    if not path.is_file():
        raise SystemExit(f"Missing TSV: {path}")
    csv.field_size_limit(max(csv.field_size_limit(), 10_000_000))
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def validate_component_crosswalk(bundle: Path, manifest: dict[str, object]) -> dict[str, int]:
    candidate_relative = manifest.get("candidate_universe_path")
    crosswalk_relative = manifest.get("candidate_universe_component_crosswalk_path")
    if not isinstance(candidate_relative, str) or not isinstance(crosswalk_relative, str):
        raise SystemExit("Release manifest lacks candidate component-crosswalk paths")
    candidates = read_tsv(bundle / candidate_relative)
    crosswalk = read_tsv(bundle / crosswalk_relative)
    candidate_ids = {row.get("candidate_pair_id", "") for row in candidates}
    crosswalk_ids = {row.get("candidate_pair_id", "") for row in crosswalk}
    if len(candidate_ids) != len(candidates) or len(crosswalk_ids) != len(crosswalk):
        raise SystemExit("Candidate or component crosswalk contains duplicate IDs")
    if candidate_ids != crosswalk_ids:
        raise SystemExit("Candidate and component crosswalk ID sets differ")
    required_candidate = {"component_mapping_id", "component_mapping_status", "ligand_components", "receptor_components"}
    required_crosswalk = {"component_mapping_id", "candidate_pair_id", "component_mapping_status", "ligand_components", "receptor_components", "source_registry_sha256"}
    if not candidates or not required_candidate.issubset(candidates[0]) or not crosswalk or not required_crosswalk.issubset(crosswalk[0]):
        raise SystemExit("Candidate component crosswalk columns are incomplete")
    cross_by_id = {row["candidate_pair_id"]: row for row in crosswalk}
    allowed = {
        "explicit_source_complex", "single_gene_identity",
        "source_registry_and_explicit_resource_agree",
        "unresolved_no_exact_source_registry_pair",
        "unresolved_source_component_disagreement",
        "unresolved_missing_or_invalid_source_components",
        "unresolved_duplicate_source_components",
        "unresolved_entity_type_component_mismatch",
    }
    for row in candidates:
        cross = cross_by_id[row["candidate_pair_id"]]
        if row["component_mapping_id"] != cross["component_mapping_id"] or row["component_mapping_status"] != cross["component_mapping_status"]:
            raise SystemExit("Candidate and component crosswalk mapping identity mismatch")
        if row["component_mapping_status"] not in allowed:
            raise SystemExit("Unknown component mapping status")
        if not row["component_mapping_status"].startswith("unresolved_"):
            if row["ligand_components"] != cross["ligand_components"] or row["receptor_components"] != cross["receptor_components"]:
                raise SystemExit("Resolved candidate component fields disagree with crosswalk")
    source_path = bundle / "method_resources/method_native/master_lr_registry.tsv"
    source_hash = sha256(source_path)
    if any(row["source_registry_sha256"] != source_hash for row in crosswalk):
        raise SystemExit("Component crosswalk source-registry checksum does not match release resource")
    return {
        "candidate_count": len(candidates),
        "crosswalk_count": len(crosswalk),
        "resolved_count": sum(not row["component_mapping_status"].startswith("unresolved_") for row in crosswalk),
        "unresolved_count": sum(row["component_mapping_status"].startswith("unresolved_") for row in crosswalk),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle-dir", type=Path, default=DEFAULT_BUNDLE)
    parser.add_argument("--nichenet-artifact-root", type=Path, required=True)
    return parser.parse_args()


def validate_release_identity(manifest: dict[str, object]) -> None:
    """Validate the additive-release pointers before checking nested artifacts."""
    if manifest.get("schema_version") != "mscs_release_bundle_v1":
        raise SystemExit("Unsupported mSCS release bundle schema")
    if manifest.get("nichenet_ligand_target_prior_manifest") != CONTRACT_RELATIVE.as_posix():
        raise SystemExit("Release manifest does not point to the NicheNet prior contract")
    if manifest.get("tf_target_prior_manifest") != PRIOR_MANIFEST.as_posix():
        raise SystemExit("Release manifest does not point to the TF-target prior contract")
    if not manifest.get("candidate_universe_component_crosswalk_path"):
        raise SystemExit("Release manifest does not point to the candidate component crosswalk")
    if not manifest.get("candidate_component_handoff_path"):
        raise SystemExit("Release manifest does not point to the candidate component handoff")
    if not manifest.get("parent_release_id") or manifest.get("parent_release_id") == manifest.get("release_id"):
        raise SystemExit("TF-target release does not identify a distinct parent release")
    if manifest.get("original_mscs_resources_preserved") is not True:
        raise SystemExit("Original mSCS resources are not explicitly preserved")


def main() -> int:
    args = parse_args()
    bundle = args.bundle_dir.resolve()
    companion_root = args.nichenet_artifact_root.resolve()
    manifest_path = bundle / "release_manifest.json"
    if not manifest_path.is_file():
        raise SystemExit(f"Missing release manifest: {manifest_path}")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    validate_release_identity(manifest)

    mismatches: list[str] = []
    for relative, expected in manifest.get("files", {}).items():
        path = bundle / relative
        if not path.is_file():
            mismatches.append(f"missing manifest file: {relative}")
            continue
        if sha256(path) != expected.get("sha256") or path.stat().st_size != expected.get("bytes"):
            mismatches.append(f"checksum/size mismatch: {relative}")
    if mismatches:
        raise SystemExit("Release bundle validation failed: " + "; ".join(mismatches))

    candidate_relative = manifest.get("candidate_universe_path")
    if candidate_relative:
        candidate_path = bundle / str(candidate_relative)
        candidate_rows = read_tsv(candidate_path)
        expected_count = manifest.get("counts", {}).get("candidate_universe_records")
        if expected_count is not None and len(candidate_rows) != expected_count:
            raise SystemExit(f"Candidate universe row count mismatch: {len(candidate_rows)} != {expected_count}")

    try:
        nichenet_summary = validate_contract(bundle=bundle, companion_artifact_root=companion_root)
        prior_summary = validate_prior_manifest(bundle)
    except ValueError as exc:
        raise SystemExit(f"Nested release contract validation failed: {exc}") from exc

    prior_manifest = json.loads((bundle / PRIOR_MANIFEST).read_text(encoding="utf-8"))
    if manifest.get("tf_target_prior") != prior_manifest:
        raise SystemExit("Top-level TF-target prior summary does not match its release contract")
    expected_pairs = manifest.get("counts", {}).get("tf_target_prior_pairs")
    if expected_pairs != prior_summary["pair_count"]:
        raise SystemExit("Top-level TF-target pair count does not match the prior contract")
    component_summary = validate_component_crosswalk(bundle, manifest)
    print(json.dumps({
        "status": "PASS additive mSCS TF-target prior release validation",
        "release_id": manifest.get("release_id"),
        "parent_release_id": manifest.get("parent_release_id"),
        "manifest_files_checked": len(manifest.get("files", {})),
        "nichenet": nichenet_summary,
        "tf_target_prior": prior_summary,
        "candidate_components": component_summary,
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
