#!/usr/bin/env python3
"""Attach the exact-pair TFLink source-chain audit to each C-tier ledger row."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_STAGING = (
    ROOT
    / "data/processed/public_tf_union_expansion_v1/"
    "comprehensive_interaction_promotion_v1/module_integration_staging_v1"
)
MARKER = "round_241_tflink_gtrd_source_chain"


def append_field(row: dict[str, str], field: str, value: str) -> None:
    current = row.get(field, "")
    if MARKER in current:
        return
    row[field] = f"{current};{value}" if current else value


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--staging", type=Path, default=DEFAULT_STAGING)
    args = parser.parse_args()
    audit_path = args.staging / "c_tier_exact_pair_source_chain_audit.tsv"

    with audit_path.open(newline="", encoding="utf-8") as handle:
        audits = {
            row["promotion_id"]: row
            for row in csv.DictReader(handle, delimiter="\t")
        }

    changed = 0
    seen: set[str] = set()
    for ledger_path in sorted(args.staging.glob("c_tier_context_search_round_*.tsv")):
        with ledger_path.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle, delimiter="\t")
            fieldnames = reader.fieldnames or []
            rows = list(reader)
        file_changed = False
        for row in rows:
            promotion_id = row.get("promotion_id", "")
            audit = audits.get(promotion_id)
            if audit is None:
                continue
            seen.add(promotion_id)
            if MARKER in row.get("search_scope", ""):
                continue
            append_field(row, "search_scope", MARKER)
            append_field(
                row,
                "search_queries",
                "TFLink raw snapshot exact-pair checksum organism and source-metadata audit",
            )
            append_field(
                row,
                "search_outcome",
                audit["source_chain_status"],
            )
            append_field(
                row,
                "grade_action",
                "retain_exact_pair_L0_source_chain_verified",
            )
            append_field(
                row,
                "context_evidence_basis",
                "Round 241 verified the exact source-table pair in its species-specific TFLink raw snapshot, including checksum and GTRD/source metadata; this is provenance verification only and does not upgrade context or establish causality.",
            )
            append_field(row, "review_status", MARKER)
            file_changed = True
        if not file_changed:
            continue
        with ledger_path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="\t")
            writer.writeheader()
            writer.writerows(rows)
        changed += len(rows)

    missing = sorted(set(audits) - seen)
    print(f"updated {changed} ledger rows across C-tier search ledgers")
    print(f"audited IDs attached: {len(seen)}")
    if missing:
        print(f"audit IDs without ledger row: {len(missing)}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
