#!/usr/bin/env python3
"""Materialize the active public ligand--receptor review batches.

The triage stage assigns stable batch identifiers.  This script turns those
rows into batch packets plus a manifest and curator contract.  It does not
promote edges, adjudicate evidence, or assign confidence.
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_QUEUE = ROOT / "data/processed/public_database_comparison_v2/candidate_triage_v1/candidate_review_queue.tsv"
DEFAULT_OUTPUT = ROOT / "data/processed/public_database_comparison_v2/candidate_triage_v1/review_batches"


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--queue", type=Path, default=DEFAULT_QUEUE)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    rows = read_tsv(args.queue)
    if not rows:
        raise SystemExit("review queue is empty")
    if any(not row.get("review_batch") for row in rows):
        raise SystemExit("every queue row must have a review_batch")

    fields = list(rows[0])
    batches: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        batches.setdefault(row["review_batch"], []).append(row)
    batch_ids = sorted(batches)
    manifest: list[dict[str, str]] = []
    for batch_id in batch_ids:
        batch_rows = batches[batch_id]
        path = args.output_dir / f"{batch_id}.tsv"
        write_tsv(path, batch_rows, fields)
        lanes = Counter(row["review_lane"] for row in batch_rows)
        manifest.append(
            {
                "batch_id": batch_id,
                "row_count": str(len(batch_rows)),
                "primary_locator_rows": str(
                    sum(int(row.get("primary_locator_count", "0") or 0) > 0 for row in batch_rows)
                ),
                "alias_adjudication_rows": str(lanes.get("alias_adjudication", 0)),
                "primary_evidence_rows": str(lanes.get("primary_evidence_review", 0)),
                "discovery_rows": str(lanes.get("discovery_review", 0)),
                "first_candidate_unit_id": batch_rows[0]["candidate_unit_id"],
                "last_candidate_unit_id": batch_rows[-1]["candidate_unit_id"],
                "packet_path": str(path.relative_to(ROOT)),
                "status": "assigned",
            }
        )
    write_tsv(args.output_dir / "manifest.tsv", manifest, list(manifest[0]))

    contract = """# Public ligand--receptor evidence-review contract

Review one packet at a time. First decide whether the public row is already
represented by the matched mSCIdblit graph edge under an alias, processed form,
species-specific form, receptor complex, or reverse orientation. If it is not
represented, open the cited primary paper or perform a documented discovery
search.

Return one disposition per candidate unit. Allowed dispositions are:

- `already_present_exact_or_alias`
- `already_present_reverse_orientation`
- `new_primary_supported_edge_candidate`
- `hold_contextual_or_complex_boundary`
- `reject_precursor_or_non_edge_form`
- `no_primary_evidence_found`
- `needs_manual_adjudication`

Record exact source locators, species, assay or functional readout, and a short
evidence note. Do not promote graph edges in the packet. Do not assign route
confidence; mSCS evaluates plausibility after evidence is curated.
"""
    (args.output_dir / "review_contract.md").write_text(contract, encoding="utf-8")

    summary = {
        "queue_path": str(args.queue),
        "queue_rows": len(rows),
        "batch_count": len(batch_ids),
        "batch_size_max": max(len(batches[batch_id]) for batch_id in batch_ids),
        "batch_rows": sum(len(batch) for batch in batches.values()),
        "lane_counts": dict(sorted(Counter(row["review_lane"] for row in rows).items())),
        "policy": "Packets are evidence-review inputs only; they do not create graph edges or confidence scores.",
    }
    (args.output_dir / "manifest.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"prepared_batches={len(batch_ids)} queue_rows={len(rows)} output={args.output_dir}")


if __name__ == "__main__":
    main()
