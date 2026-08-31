#!/usr/bin/env python3
"""Validate batch 008 reports without mutating canonical Module 20A data."""

from __future__ import annotations

import csv
import json
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / "work" / "module20_db_seed"
BATCH = WORK / "evidence_search_agents" / "agent_batch_008"
QUEUE = WORK / "evidence_escalation_router" / "module20a_external_review_queue.tsv"

FIELDS = [
    "review_id", "pair_key", "verdict", "source_locators", "species_support",
    "support_kind", "evidence_summary", "limitations", "search_notes",
]
ALLOWED = {"promote_candidate", "needs_manual_review", "hold_low", "reject_pair", "no_evidence"}


def read(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    queue = {row["review_id"]: row for row in read(QUEUE)}
    manifest = read(BATCH / "manifest.tsv")
    reports: list[dict[str, str]] = []
    errors: list[str] = []
    for item in manifest:
        path = ROOT / item["report_path"]
        if not path.exists():
            errors.append(f"missing report: {path}")
            continue
        rows = read(path)
        if list(rows[0]) != FIELDS if rows else True:
            errors.append(f"bad header or empty report: {path}")
        if len(rows) != int(item["row_count"]):
            errors.append(f"row count mismatch: {path} expected {item['row_count']} got {len(rows)}")
        seen: set[str] = set()
        for row in rows:
            rid = row.get("review_id", "")
            if rid in seen:
                errors.append(f"duplicate review_id {rid} in {path}")
            seen.add(rid)
            if rid not in queue:
                errors.append(f"unknown review_id {rid} in {path}")
            if row.get("verdict") not in ALLOWED:
                errors.append(f"invalid verdict {row.get('verdict')} for {rid}")
        reports.extend(rows)

    ids = [row["review_id"] for row in reports]
    counts = Counter(row["verdict"] for row in reports)
    expected = sum(int(item["row_count"]) for item in manifest)
    if len(reports) != expected:
        errors.append(f"total report rows expected {expected} got {len(reports)}")
    if len(set(ids)) != len(ids):
        errors.append("reports contain duplicate review_ids across packets")

    fields = FIELDS
    write(BATCH / "validated_reports.tsv", fields, sorted(reports, key=lambda row: row["review_id"]))
    summary = {
        "generated_utc": datetime.now(UTC).isoformat(timespec="seconds"),
        "batch_id": "agent_batch_008",
        "packet_count": len(manifest),
        "rows_expected": expected,
        "rows_reported": len(reports),
        "unique_review_ids": len(set(ids)),
        "verdict_counts": dict(sorted(counts.items())),
        "validation_errors": errors,
        "canonical_queue_mutated": False,
        "signaling_edges_created": False,
    }
    (BATCH / "validation_summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
