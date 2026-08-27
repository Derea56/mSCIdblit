#!/usr/bin/env python3
"""Split the remaining non-priority TF inventory into deterministic batches."""

from __future__ import annotations

import argparse
import csv
import json
import math
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INVENTORY = ROOT / "data/processed/public_tf_union_v1/module_curation/new_tf_inventory.tsv"
DEFAULT_REVIEWED = ROOT / "data/processed/public_tf_union_v1/module_curation/new_tf_materialized/priority_tf_agent_decisions.tsv"
DEFAULT_OUTPUT = ROOT / "data/processed/public_tf_union_v1/module_curation/new_tf_batches"


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows({field: row.get(field, "") for field in fields} for row in rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--inventory", type=Path, default=DEFAULT_INVENTORY)
    parser.add_argument("--reviewed", type=Path, default=DEFAULT_REVIEWED)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--batch-size", type=int, default=20)
    args = parser.parse_args()
    if args.batch_size < 1:
        raise SystemExit("--batch-size must be positive")

    inventory = read_tsv(args.inventory)
    reviewed_keys = set()
    if args.reviewed.is_file():
        for row in read_tsv(args.reviewed):
            reviewed_keys.add(row["tf_symbol"].strip().casefold())

    by_key: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in inventory:
        key = row["tf_key"].strip().casefold()
        if key not in reviewed_keys:
            by_key[key].append(row)

    key_rows = []
    for key, rows in by_key.items():
        key_rows.append({
            "tf_key": key,
            "tf_symbols": ";".join(sorted({row["tf_symbol"] for row in rows})),
            "species": ";".join(sorted({row["species"] for row in rows})),
            "max_priority_rank": max(int(row["priority_rank"]) for row in rows),
            "species_rows": len(rows),
        })
    key_rows.sort(key=lambda row: (-row["max_priority_rank"], row["tf_key"]))

    fields = list(inventory[0]) if inventory else []
    batches = []
    for start in range(0, len(key_rows), args.batch_size):
        batch_keys = key_rows[start:start + args.batch_size]
        batch_number = start // args.batch_size + 1
        batch_key_set = {row["tf_key"] for row in batch_keys}
        batch_rows = [row for row in inventory if row["tf_key"].casefold() in batch_key_set]
        batch_rows.sort(key=lambda row: (-int(row["priority_rank"]), row["tf_key"], row["species"]))
        filename = f"new_tf_batch_{batch_number:03d}.tsv"
        write_tsv(args.output_dir / filename, fields, batch_rows)
        batches.append({
            "batch_id": f"NEW-TF-{batch_number:03d}",
            "batch_number": batch_number,
            "filename": filename,
            "tf_key_count": len(batch_keys),
            "species_row_count": len(batch_rows),
            "tf_keys": [row["tf_key"] for row in batch_keys],
            "tf_symbols": [row["tf_symbols"] for row in batch_keys],
            "module_policy": "22B default; existing 20B/21B/23B/24B flags require exact module evidence and independent corroboration",
            "status": "queued",
        })

    manifest = {
        "inventory_rows": len(inventory),
        "reviewed_tf_keys_excluded": sorted(reviewed_keys),
        "remaining_tf_keys": len(key_rows),
        "remaining_species_rows": sum(len(rows) for rows in by_key.values()),
        "batch_size_tf_keys": args.batch_size,
        "batch_count": len(batches),
        "batches": batches,
        "default_module": "22B",
        "canonical_database_writes": False,
        "frozen_release_modified": False,
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "new_tf_batch_manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "remaining_tf_keys": manifest["remaining_tf_keys"],
        "remaining_species_rows": manifest["remaining_species_rows"],
        "batch_count": manifest["batch_count"],
        "batch_size_tf_keys": manifest["batch_size_tf_keys"],
        "output_dir": str(args.output_dir),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
