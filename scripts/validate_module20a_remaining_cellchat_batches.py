#!/usr/bin/env python3
"""Validate remaining CellChat search reports without mutating canonical data."""

from __future__ import annotations

import csv
import json
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BATCH = ROOT / "work" / "module20_db_seed" / "evidence_search_agents" / "cellchat_remaining_batch_001"
FIELDS = ["pair_key", "pair_label_canonical", "verdict", "source_locators", "species_support", "support_kind", "evidence_summary", "limitations", "search_notes"]
ALLOWED = {"promote_candidate", "needs_manual_review", "hold_low", "no_evidence", "reject_pair"}


def read(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def main() -> None:
    manifest = read(BATCH / "manifest.tsv")
    errors: list[str] = []
    reports: list[dict[str, str]] = []
    expected_ids: list[str] = []
    for item in manifest:
        packet = read(ROOT / item["packet_path"])
        expected_ids.extend(row["pair_key"] for row in packet)
        path = ROOT / item["report_path"]
        if not path.exists():
            errors.append(f"missing report {path}")
            continue
        rows = read(path)
        if not rows or list(rows[0]) != FIELDS:
            errors.append(f"bad header {path}")
        if len(rows) != int(item["row_count"]):
            errors.append(f"row count mismatch {path}: {len(rows)}")
        for row in rows:
            if row["verdict"] not in ALLOWED:
                errors.append(f"invalid verdict {row['verdict']}")
            if not row["search_notes"].strip():
                errors.append(f"missing search notes {row['pair_key']}")
        reports.extend(rows)
    if len(reports) != len(expected_ids):
        errors.append(f"expected {len(expected_ids)} reports, got {len(reports)}")
    if len({row["pair_key"] for row in reports}) != len(reports):
        errors.append("duplicate report pair keys")
    if set(expected_ids) != {row["pair_key"] for row in reports}:
        errors.append("report pair keys do not match packets")
    summary = {
        "generated_utc": datetime.now(UTC).isoformat(timespec="seconds"),
        "expected_rows": len(expected_ids),
        "reported_rows": len(reports),
        "verdict_counts": dict(sorted(Counter(row["verdict"] for row in reports).items())),
        "validation_errors": errors,
        "canonical_ledgers_mutated": False,
    }
    (BATCH / "validation_summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
