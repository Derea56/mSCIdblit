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
DEFAULT_BUNDLE = ROOT / "data/processed/mscs_release_bundle_v1_7_0_nichenet_tf_prior_v1"


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
    print(json.dumps({
        "status": "PASS additive mSCS TF-target prior release validation",
        "release_id": manifest.get("release_id"),
        "parent_release_id": manifest.get("parent_release_id"),
        "manifest_files_checked": len(manifest.get("files", {})),
        "nichenet": nichenet_summary,
        "tf_target_prior": prior_summary,
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
