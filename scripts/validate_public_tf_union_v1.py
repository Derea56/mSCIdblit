#!/usr/bin/env python3
"""Validate public TF union artifacts and the frozen-release boundary."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import subprocess
from pathlib import Path


REQUIRED_FILES = (
    "integration_manifest.json",
    "source_registry.tsv",
    "identity_mapping.tsv",
    "frozen_entity_mapping.tsv",
    "unresolved_identity_queue.tsv",
    "source_records.tsv",
    "source_references.tsv",
    "source_regulons.tsv",
    "source_regulon_members.tsv",
    "priority_tf_evidence.tsv",
    "load_public_tf_union.sql",
    "public_tf_union_gap_report.json",
    "PUBLIC_TF_UNION_GAP_AUDIT_V1.md",
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_tsv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        return reader.fieldnames or [], list(reader)


def git_unchanged(root: Path, commit: str, path: str) -> bool:
    result = subprocess.run(
        ["git", "diff", "--quiet", commit, "--", path],
        cwd=root,
        check=False,
    )
    return result.returncode == 0


def git_blob_sha256(root: Path, commit: str, path: str) -> str:
    content = subprocess.check_output(["git", "show", f"{commit}:{path}"], cwd=root)
    return hashlib.sha256(content).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--repo-root", type=Path, default=Path("."))
    parser.add_argument("--frozen-commit", default="eeb9960")
    parser.add_argument("--report", type=Path, default=None)
    args = parser.parse_args()
    root = args.repo_root.resolve()
    output_dir = (root / args.output_dir).resolve() if not args.output_dir.is_absolute() else args.output_dir
    report_path = args.report or (output_dir / "public_tf_union_validation.json")
    errors: list[str] = []
    checks: dict[str, object] = {}

    missing = [name for name in REQUIRED_FILES if not (output_dir / name).is_file()]
    if missing:
        errors.extend(f"missing artifact: {name}" for name in missing)
        report = {"status": "fail", "errors": errors, "checks": checks}
        report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(report, sort_keys=True))
        return 1

    manifest = json.loads((output_dir / "integration_manifest.json").read_text(encoding="utf-8"))
    audit = json.loads((output_dir / "public_tf_union_gap_report.json").read_text(encoding="utf-8"))
    counts = manifest["counts"]
    checks["audit_acceptance_checks"] = audit["acceptance_checks"]
    for name, value in audit["acceptance_checks"].items():
        if value is not True:
            errors.append(f"audit acceptance check failed: {name}")

    table_files = {
        "source_registry_rows": "source_registry.tsv",
        "identity_mapping_rows": "identity_mapping.tsv",
        "source_records": "source_records.tsv",
        "source_references": "source_references.tsv",
        "source_regulons": "source_regulons.tsv",
        "materialized_source_regulon_members": "source_regulon_members.tsv",
        "priority_tf_verification_rows": "priority_tf_evidence.tsv",
    }
    table_row_counts = {}
    for count_key, filename in table_files.items():
        fields, rows = read_tsv(output_dir / filename)
        table_row_counts[count_key] = len(rows)
        if len(rows) != counts[count_key]:
            errors.append(f"{filename} row count {len(rows)} != manifest {counts[count_key]}")
        if not fields:
            errors.append(f"{filename} has no header")
    checks["artifact_row_counts"] = table_row_counts
    frozen_mapping_fields, frozen_mapping_rows = read_tsv(output_dir / "frozen_entity_mapping.tsv")
    table_row_counts["frozen_entity_mapping_rows"] = len(frozen_mapping_rows)
    if len(frozen_mapping_rows) != counts["identity_mapping_rows"]:
        errors.append(
            f"frozen_entity_mapping.tsv row count {len(frozen_mapping_rows)} != identity mapping rows {counts['identity_mapping_rows']}"
        )
    checks["frozen_mapping_rows_have_resolution_status"] = all(
        bool(row.get("frozen_entity_match_status")) for row in frozen_mapping_rows
    )
    if not checks["frozen_mapping_rows_have_resolution_status"]:
        errors.append("frozen_entity_mapping.tsv contains rows without a resolution status")

    records_fields, records = read_tsv(output_dir / "source_records.tsv")
    members_fields, members = read_tsv(output_dir / "source_regulon_members.tsv")
    checks["external_record_keys_unique"] = len({row["external_record_key"] for row in records}) == len(records)
    checks["all_record_rows_export_gated"] = all(row["export_priority"] == "exclude" for row in records)
    checks["all_member_rows_export_gated"] = all(row["export_priority"] == "exclude" for row in members)
    if not checks["external_record_keys_unique"]:
        errors.append("duplicate external_record_key in source_records.tsv")
    if not checks["all_record_rows_export_gated"]:
        errors.append("source record outside exclude export gate")
    if not checks["all_member_rows_export_gated"]:
        errors.append("source member outside exclude export gate")

    registry_fields, registry_rows = read_tsv(output_dir / "source_registry.tsv")
    snapshot_hash_checks = {}
    for row in registry_rows:
        snapshot = Path(row["snapshot_path"])
        observed = sha256(snapshot) if snapshot.is_file() else None
        snapshot_hash_checks[f"{row['source_registry']}:{row['species_context']}"] = observed == row["snapshot_sha256"]
        if observed != row["snapshot_sha256"]:
            errors.append(f"snapshot digest mismatch or missing: {snapshot}")
    checks["snapshot_hashes_match_registry"] = snapshot_hash_checks

    frozen_paths = (
        "data/processed/mechanism_bundle_module20_24_db_v1_0_0",
        "VERSION",
        "docs/RELEASE_v1.0.0.md",
    )
    frozen_checks = {path: git_unchanged(root, args.frozen_commit, path) for path in frozen_paths}
    checks["frozen_release_paths_unchanged"] = frozen_checks
    for path, unchanged in frozen_checks.items():
        if not unchanged:
            errors.append(f"frozen release path changed relative to {args.frozen_commit}: {path}")

    bundle_prefix = "data/processed/mechanism_bundle_module20_24_db_v1_0_0"
    tagged_bundle_files = subprocess.check_output(
        ["git", "ls-tree", "-r", "--name-only", args.frozen_commit, "--", bundle_prefix],
        cwd=root,
        text=True,
    ).splitlines()
    bundle_hashes = {}
    for relative_path in tagged_bundle_files:
        current_path = root / relative_path
        current_hash = sha256(current_path) if current_path.is_file() else None
        tagged_hash = git_blob_sha256(root, args.frozen_commit, relative_path)
        bundle_hashes[relative_path] = {
            "current_sha256": current_hash,
            "tagged_sha256": tagged_hash,
            "match": current_hash == tagged_hash,
        }
        if current_hash != tagged_hash:
            errors.append(f"frozen bundle hash mismatch: {relative_path}")
    checks["frozen_bundle_sha256_matches_tag"] = bundle_hashes

    checks["frozen_release_metadata"] = {
        "graph_version": manifest.get("frozen_graph_version", "1.0.0"),
        "frozen_commit": args.frozen_commit,
        "integration_status": manifest.get("integration_status"),
    }
    status = "pass" if not errors else "fail"
    report = {"status": status, "errors": errors, "checks": checks}
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"status": status, "errors": errors, "report": str(report_path)}, sort_keys=True))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
