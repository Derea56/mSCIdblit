#!/usr/bin/env python3
"""Validate and merge completed remaining-TF batch lanes."""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BATCH_MANIFEST = ROOT / "data/processed/public_tf_union_v1/module_curation/new_tf_batches/new_tf_batch_manifest.json"
DEFAULT_LANE_DIR = ROOT / "work/public_tf_curation/new_tf_batch_lanes"
DEFAULT_OUTPUT = ROOT / "data/processed/public_tf_union_v1/module_curation/new_tf_batch_merged"
FIELDS = [
    "species", "tf_symbol", "target_symbol", "external_record_keys", "decision",
    "module_assignment", "evidence_status", "support_kind", "effect_polarity",
    "primary_pmids", "corroborating_pmids", "shared_paper_status",
    "cross_module_status", "cell_type_context", "stimulus_context", "limitations", "notes",
]
ALLOWED_DECISIONS = {"promote_to_22B", "hold_exact_pair", "hold_direction_conflict", "database_only_unverified"}
MODULES = {"20A", "20B", "21A", "21B", "22A", "22B", "23A", "23B", "24A", "24B"}
SPECIES = {"human", "mouse"}
NO_CROSS = {
    "", "none", "not_applicable", "no_overlap_with_modules_20_21_23_24",
    "no_modules_20_21_23_24_overlap", "no_verified_cross_module_claim", "not_claimed",
}


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows({field: row.get(field, "") for field in FIELDS} for row in rows)


def actual_cross(value: str) -> bool:
    return (value or "").strip().casefold() not in NO_CROSS


def module_tokens(value: str) -> set[str]:
    return {
        token.strip().removesuffix("_candidate")
        for token in value.replace(",", ";").replace("/", ";").split(";")
        if token.strip()
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch-manifest", type=Path, default=DEFAULT_BATCH_MANIFEST)
    parser.add_argument("--lane-dir", type=Path, default=DEFAULT_LANE_DIR)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--batch-id", action="append", dest="batch_ids")
    args = parser.parse_args()

    batch_manifest = json.loads(args.batch_manifest.read_text(encoding="utf-8"))
    all_batches = {batch["batch_id"]: batch for batch in batch_manifest["batches"]}
    batch_ids = args.batch_ids or sorted(all_batches)
    errors: list[str] = []
    merged: list[dict[str, str]] = []
    seen_pairs: set[tuple[str, str, str]] = set()
    coverage: dict[str, set[str]] = {}
    counts: Counter[str] = Counter()

    for batch_id in batch_ids:
        batch = all_batches.get(batch_id)
        if batch is None:
            errors.append(f"unknown batch id: {batch_id}")
            continue
        path = args.lane_dir / f"{batch_id}.tsv"
        if not path.is_file():
            errors.append(f"missing lane file: {path}")
            continue
        rows = read_tsv(path)
        if not rows:
            errors.append(f"empty lane file: {path}")
            continue
        missing = sorted(set(FIELDS) - set(rows[0]))
        if missing:
            errors.append(f"{path.name} missing fields: {', '.join(missing)}")
            continue
        expected = set(batch["tf_keys"])
        seen_tfs: set[str] = set()
        for line, row in enumerate(rows, start=2):
            species = row["species"].strip().lower()
            tf = row["tf_symbol"].strip().casefold()
            target = row["target_symbol"].strip()
            pair = (species, tf, target.casefold())
            if tf not in expected:
                errors.append(f"{path.name}:{line}: TF {row['tf_symbol']} is outside {batch_id}")
            seen_tfs.add(tf)
            if species not in SPECIES:
                errors.append(f"{path.name}:{line}: invalid species {species}")
            if not target or target in {"\\N", "NA", "null"}:
                errors.append(f"{path.name}:{line}: missing target symbol")
            if row["decision"] not in ALLOWED_DECISIONS:
                errors.append(f"{path.name}:{line}: invalid decision {row['decision']}")
            if pair in seen_pairs:
                errors.append(f"duplicate species/TF/target pair: {pair}")
            seen_pairs.add(pair)
            tokens = module_tokens(row["module_assignment"])
            if not tokens or not tokens.issubset(MODULES):
                errors.append(f"{path.name}:{line}: invalid module assignment {row['module_assignment']}")
            if row["decision"] == "promote_to_22B":
                if "22B" not in tokens:
                    errors.append(f"{path.name}:{line}: promotion/module mismatch")
                if not row["primary_pmids"].strip():
                    errors.append(f"{path.name}:{line}: promotion lacks primary PMID")
            if actual_cross(row["cross_module_status"]) and row["decision"].startswith("promote_") and not row["corroborating_pmids"].strip():
                errors.append(f"{path.name}:{line}: cross-module promotion lacks corroborating PMID")
            merged.append(row)
            counts[row["decision"]] += 1
        missing_tfs = sorted(expected - seen_tfs)
        if missing_tfs:
            errors.append(f"{path.name}: missing rows for TF keys: {', '.join(missing_tfs)}")
        coverage[batch_id] = seen_tfs

    status = "pass" if not errors else "fail"
    args.output_dir.mkdir(parents=True, exist_ok=True)
    if not errors:
        write_tsv(args.output_dir / "new_tf_batch_merged.tsv", merged)
    manifest = {
        "status": status,
        "batch_ids": batch_ids,
        "merged_rows": len(merged),
        "decision_counts": dict(counts),
        "batch_tf_coverage": {batch_id: sorted(keys) for batch_id, keys in sorted(coverage.items())},
        "errors": errors,
        "default_module": "22B",
        "canonical_database_writes": False,
        "frozen_release_modified": False,
    }
    (args.output_dir / "new_tf_batch_merge_manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(manifest, sort_keys=True))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
