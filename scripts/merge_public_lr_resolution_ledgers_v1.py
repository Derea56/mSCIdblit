#!/usr/bin/env python3
"""Merge batch-specific public LR resolution ledgers without dropping audit rows."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIELDS = [
    "candidate_unit_id", "review_batch", "normalized_ligand_key", "normalized_receptor_key",
    "disposition", "matched_graph_edge_ids", "supporting_primary_locators", "reviewed_source_locators",
    "evidence_layer", "species_support", "evidence_summary", "limitations", "review_status",
]


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("ledgers", nargs="+", type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    merged: dict[str, dict[str, str]] = {}
    for path in args.ledgers:
        for row in read_rows(path):
            candidate_id = row.get("candidate_unit_id", "")
            if not candidate_id:
                raise SystemExit(f"missing candidate_unit_id in {path}")
            if candidate_id in merged:
                raise SystemExit(f"duplicate candidate_unit_id across ledgers: {candidate_id}")
            merged[candidate_id] = {field: row.get(field, "") for field in FIELDS}
    rows = [merged[key] for key in sorted(merged)]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print(f"merged_ledgers={len(args.ledgers)} rows={len(rows)} output={args.output}")


if __name__ == "__main__":
    main()
