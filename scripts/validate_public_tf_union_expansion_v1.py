#!/usr/bin/env python3
"""Validate the provenance-preserving public TF union expansion artifact."""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DIR = ROOT / "data/processed/public_tf_union_expansion_v1"
DEFAULT_EXISTING = ROOT / "data/processed/public_tf_union_v1"


def read_tsv(path: Path) -> list[dict[str, str]]:
    if not path.is_file() and path.suffix == ".tsv":
        compressed = path.with_suffix(path.suffix + ".gz")
        if compressed.is_file():
            path = compressed
    opener = gzip.open if path.suffix == ".gz" else Path.open
    mode = "rt" if path.suffix == ".gz" else "r"
    with opener(path, mode, newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def issue(checks: dict[str, int], name: str, count: int) -> None:
    checks[name] = int(count)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", type=Path, default=DEFAULT_DIR)
    parser.add_argument("--existing-dir", type=Path, default=DEFAULT_EXISTING)
    args = parser.parse_args()

    checks: dict[str, int] = {}
    required = [
        "source_registry.tsv", "reported_contributor_registry.tsv",
        "reported_contributor_links.tsv", "tf_identity_records.tsv",
        "tflink_tf_summary.tsv", "tf_pair_records.tsv", "tf_candidate_union.tsv",
        "expansion_manifest.json",
    ]
    missing = [
        name for name in required
        if not (args.input_dir / name).is_file()
        and not (args.input_dir / f"{name}.gz").is_file()
    ]
    issue(checks, "missing_required_files", len(missing))
    if missing:
        result = {"status": "fail", "checks": checks, "missing": missing}
        (args.input_dir / "expansion_validation.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        raise SystemExit(json.dumps(result, sort_keys=True))

    registry = read_tsv(args.input_dir / "source_registry.tsv")
    contributors = read_tsv(args.input_dir / "reported_contributor_registry.tsv")
    links = read_tsv(args.input_dir / "reported_contributor_links.tsv")
    identities = read_tsv(args.input_dir / "tf_identity_records.tsv")
    tflink = read_tsv(args.input_dir / "tflink_tf_summary.tsv")
    pairs = read_tsv(args.input_dir / "tf_pair_records.tsv")
    candidates = read_tsv(args.input_dir / "tf_candidate_union.tsv")
    manifest = json.loads((args.input_dir / "expansion_manifest.json").read_text(encoding="utf-8"))

    registry_keys = [(row["source_registry"], row["source_version"], row["species_scope"]) for row in registry]
    issue(checks, "duplicate_registry_keys", len(registry_keys) - len(set(registry_keys)))
    registry_key_set = set(registry_keys)
    issue(checks, "registry_empty_hashes", sum(not row["snapshot_sha256"] for row in registry))

    contributor_keys = [row["contributor_key"] for row in contributors]
    issue(checks, "duplicate_contributor_keys", len(contributor_keys) - len(set(contributor_keys)))
    contributor_key_set = set(contributor_keys)
    pair_record_key_set = {row["pair_record_key"] for row in pairs}
    issue(checks, "contributor_links_without_registry", sum(row["contributor_key"] not in contributor_key_set for row in links))
    issue(checks, "contributor_links_without_pair", sum(row["external_record_key"] not in pair_record_key_set for row in links))
    issue(checks, "contributor_links_marked_independent", sum(row["independent_snapshot"].casefold() != "false" for row in links))
    issue(checks, "duplicate_contributor_record_labels", len(links) - len({(row["external_record_key"], row["raw_source_label"]) for row in links}))

    identity_keys = [row["identity_record_key"] for row in identities]
    issue(checks, "duplicate_identity_record_keys", len(identity_keys) - len(set(identity_keys)))
    issue(checks, "identity_rows_without_registry", sum((row["source_registry"], row["source_version"], row["species_scope"]) not in registry_key_set for row in identities))
    issue(checks, "identity_rows_without_source_id", sum(not row["source_record_id"] for row in identities))

    pair_keys = [row["pair_record_key"] for row in pairs]
    issue(checks, "duplicate_pair_record_keys", len(pair_keys) - len(set(pair_keys)))
    issue(checks, "pair_rows_without_registry", sum((row["source_registry"], row["source_version"], row["species_scope"]) not in registry_key_set for row in pairs))
    issue(checks, "pair_rows_without_source_locator", sum(not row["source_locator"] for row in pairs))
    issue(checks, "pair_rows_without_raw_hash", sum(not row["raw_record_sha256"] for row in pairs))
    issue(checks, "pair_rows_marked_primary_without_scope", sum(row["independence_status"] not in {"repository_snapshot", "integrated_aggregator_snapshot"} for row in pairs))

    candidate_keys = [row["candidate_key"] for row in candidates]
    issue(checks, "duplicate_candidate_keys", len(candidate_keys) - len(set(candidate_keys)))
    issue(checks, "candidate_rows_without_tf_key", sum(not row["tf_key"] for row in candidates))
    issue(checks, "candidate_rows_without_source_registry", sum(not row["source_registries"] for row in candidates))
    issue(checks, "candidate_rows_promoted", sum(row["review_status"] not in {"new_candidate", ""} for row in candidates))
    identity_candidate_keys = {
        (row["species_scope"], row["normalized_symbol_key"])
        for row in identities
        if row["normalized_symbol_key"]
    }
    issue(checks, "candidate_rows_without_identity_trace", sum(
        (row["species_scope"], row["tf_key"]) not in identity_candidate_keys
        for row in candidates
    ))

    issue(checks, "tflink_rows_without_locator", sum(not row["source_locator"] for row in tflink))
    issue(checks, "tflink_rows_with_negative_target_count", sum(int(row["target_count"]) < 0 for row in tflink))

    # The expansion must not lose or rewrite any existing public-union pair.
    existing = read_tsv(args.existing_dir / "source_records.tsv")
    expanded_by_key = {row["pair_record_key"]: row for row in pairs}
    issue(checks, "existing_pair_records_missing", sum(row["external_record_key"] not in expanded_by_key for row in existing))
    issue(checks, "existing_pair_hash_mismatches", sum(
        expanded_by_key.get(row["external_record_key"], {}).get("raw_record_sha256") != row["raw_record_sha256"]
        for row in existing if row["external_record_key"] in expanded_by_key
    ))

    manifest_counts = manifest.get("counts", {})
    actual_counts = {
        "source_registry_rows": len(registry),
        "reported_contributor_registry_rows": len(contributors),
        "reported_contributor_links": len(links),
        "tf_identity_records": len(identities),
        "tf_pair_records": len(pairs),
        "tf_candidate_union_rows": len(candidates),
        "tflink_human_tf_summary_rows": sum(row["species_scope"] == "human" for row in tflink),
        "tflink_mouse_tf_summary_rows": sum(row["species_scope"] == "mouse" for row in tflink),
    }
    issue(checks, "manifest_count_mismatches", sum(manifest_counts.get(key) != value for key, value in actual_counts.items()))

    # Verify the six newly acquired raw snapshots against the manifest.
    raw_hash_issues = 0
    for raw in manifest.get("raw_snapshots", []):
        path = Path(raw["path"])
        if not path.is_file() or sha256_file(path) != raw["sha256"]:
            raw_hash_issues += 1
    issue(checks, "raw_snapshot_hash_mismatches", raw_hash_issues)

    result = {
        "status": "pass" if all(value == 0 for value in checks.values()) else "fail",
        "checks": checks,
        "counts": actual_counts,
        "source_registries": sorted({row["source_registry"] for row in registry}),
        "candidate_species_counts": dict(Counter(row["species_scope"] for row in candidates)),
    }
    (args.input_dir / "expansion_validation.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))
    if result["status"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
