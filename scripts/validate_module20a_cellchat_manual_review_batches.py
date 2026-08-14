#!/usr/bin/env python3
"""Validate CellChat manual/uncertain re-review reports."""

from __future__ import annotations

import csv
import json
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BATCH = ROOT / "work" / "module20_db_seed" / "evidence_search_agents" / "cellchat_manual_review_batch_001"
FIELDS = ["review_id", "pair_key", "pair_label_canonical", "final_class", "source_locators", "species_support", "support_kind", "evidence_summary", "limitations", "review_notes"]
ALLOWED = {"promote_medium", "promote_low", "retain_manual", "no_evidence", "non_ligand_receptor"}


def read(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def main() -> None:
    manifest = read(BATCH / "manifest.tsv")
    errors: list[str] = []
    expected: list[str] = []
    reports: list[dict[str, str]] = []
    for item in manifest:
        packet = read(ROOT / item["packet_path"])
        expected.extend(row["pair_key"] for row in packet)
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
            if row["final_class"] not in ALLOWED:
                errors.append(f"invalid final_class {row['final_class']}")
            if not row["review_notes"].strip():
                errors.append(f"missing review notes {row['pair_key']}")
            if row["final_class"] in {"promote_low", "promote_medium"} and not row["source_locators"].strip():
                errors.append(f"promotion without source locator {row['pair_key']}")
        reports.extend(rows)
    if len(reports) != len(expected):
        errors.append(f"expected {len(expected)} reports, got {len(reports)}")
    if len({row["pair_key"] for row in reports}) != len(reports):
        errors.append("duplicate report pair keys")
    if set(expected) != {row["pair_key"] for row in reports}:
        errors.append("report pair keys do not match packets")
    summary = {"generated_utc": datetime.now(UTC).isoformat(timespec="seconds"), "expected_rows": len(expected), "reported_rows": len(reports), "final_class_counts": dict(sorted(Counter(row["final_class"] for row in reports).items())), "validation_errors": errors, "canonical_ledgers_mutated": False}
    (BATCH / "validation_summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
