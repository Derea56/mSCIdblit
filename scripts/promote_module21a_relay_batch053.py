#!/usr/bin/env python3
"""Promote the bounded Module 21A WNT7B-GPR124/FZD4-LRP5 packet."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RELAY = ROOT / "work" / "module21_relay"
DETAIL = RELAY / "module21a_pair_relay_evidence_detail.tsv"
REUSE = RELAY / "module21a_pathway_reuse_registry.tsv"
PAIRS = RELAY / "module21a_all_pair_relay_coverage.tsv"
REVIEW_FILES = [RELAY / "module21a_pair_relay_review_batches235.tsv"]
AUDIT = RELAY / "module21a_relay_promotion_batch053.tsv"
SUMMARY = RELAY / "module21a_relay_promotion_batch053_summary.json"

EVIDENCE_ID = "M21A-PAIR-EVID-5771"
PAIR_KEY = "wnt7b fzd4_lrp5"
REUSE_KEY = "M21A-REUSE-2822"
REVIEW_ID = "M20A-LIANA-REMAINING-0510"
CITATIONS = "PMID:25373781; PMCID:PMC4223636; DOI:10.1016/j.devcell.2014.08.018; PMID:40914247; PMCID:PMC12514574; DOI:10.1016/j.jbc.2025.110682"
BASIS = "Exact functional WNT7B-GPR124/FZD4-LRP5 context supports qualified-high promotion; preserve RECK/broader WNT7 coreceptor context, the 2025 FZD-independent complex, and TCF/LEF as a reporter endpoint."
PROMOTION_NOTE = "Module 21A relay/function promotion batch053 (2026-09-02): evidence tier raised to high for the exact, context-bounded packet; evidence-layer scope, upstream Module 20A LR confidence, terminal-TF status, and SCI transfer remain unchanged."


def read_tsv(path):
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        return list(reader.fieldnames or []), list(reader)


def write_tsv(path, fields, rows):
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def index(rows, key):
    result = {}
    for row in rows:
        value = row.get(key, "")
        if value and value in result:
            raise SystemExit(f"duplicate {key}: {value}")
        if value:
            result[value] = row
    return result


def append_once(value, note):
    return value if note in value else f"{value} {note}".strip()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    detail_fields, detail_rows = read_tsv(DETAIL)
    reuse_fields, reuse_rows = read_tsv(REUSE)
    pair_fields, pair_rows = read_tsv(PAIRS)
    review_tables = [read_tsv(path) for path in REVIEW_FILES]
    review_fields = [fields for fields, _ in review_tables]
    review_rows_by_file = [rows for _, rows in review_tables]
    detail = index(detail_rows, "evidence_id")
    reuse = index(reuse_rows, "pathway_reuse_key")
    reviews = index([row for rows in review_rows_by_file for row in rows], "review_id")
    coverage = next((row for row in pair_rows if row.get("module21a_evidence_ids") == EVIDENCE_ID), None)
    row = detail.get(EVIDENCE_ID)
    review = reviews.get(REVIEW_ID)
    if row is None or row.get("confidence_tier") not in {"medium", "medium-high"} or row.get("pathway_reuse_key") != REUSE_KEY or row.get("source_locators") != CITATIONS:
        raise SystemExit("detail lineage mismatch")
    if not all(layer in row.get("evidence_layer", "") for layer in ("receptor_proximal_relay", "downstream_pathway_function")):
        raise SystemExit("detail evidence-layer mismatch")
    if review is None or review.get("evidence_id") != EVIDENCE_ID or review.get("pair_key") != PAIR_KEY or review.get("source_locators") != CITATIONS or review.get("confidence_tier") not in {"medium", "medium-high"} or review.get("review_status") != "reviewed_relay_candidate":
        raise SystemExit("review lineage mismatch")
    if reuse.get(REUSE_KEY) is None or reuse[REUSE_KEY].get("evidence_ids") != EVIDENCE_ID:
        raise SystemExit("reuse lineage mismatch")
    if coverage is None or coverage.get("pair_key") != PAIR_KEY or coverage.get("module21a_status") != "reviewed_relay_candidate":
        raise SystemExit("coverage lineage mismatch")

    audit_fields = ["evidence_id", "review_id", "pair_key", "pathway_reuse_key", "previous_tier", "new_tier", "source_locators", "decision_basis", "upstream_lr_confidence_unchanged", "terminal_tf_status_unchanged", "sql_materialization"]
    audit_rows = [{
        "evidence_id": EVIDENCE_ID,
        "review_id": REVIEW_ID,
        "pair_key": PAIR_KEY,
        "pathway_reuse_key": REUSE_KEY,
        "previous_tier": row["confidence_tier"],
        "new_tier": "high",
        "source_locators": row["source_locators"],
        "decision_basis": BASIS,
        "upstream_lr_confidence_unchanged": "true",
        "terminal_tf_status_unchanged": "true",
        "sql_materialization": "false",
    }]
    if not args.apply:
        print(json.dumps({"validated": 1, "apply": False, "evidence_ids": [EVIDENCE_ID]}, indent=2))
        return

    row["confidence_tier"] = "high"
    row["limitations"] = append_once(row["limitations"], PROMOTION_NOTE)
    review["confidence_tier"] = "high"
    review["curator_note"] = append_once(review["curator_note"], PROMOTION_NOTE)
    reuse[REUSE_KEY]["validation_status"] = "promoted_high_batch053"
    reuse[REUSE_KEY]["limitations"] = append_once(reuse[REUSE_KEY]["limitations"], PROMOTION_NOTE)
    coverage["curator_notes"] = append_once(coverage["curator_notes"], PROMOTION_NOTE)

    write_tsv(DETAIL, detail_fields, detail_rows)
    for path, fields, rows in zip(REVIEW_FILES, review_fields, review_rows_by_file):
        write_tsv(path, fields, rows)
    write_tsv(REUSE, reuse_fields, reuse_rows)
    write_tsv(PAIRS, pair_fields, pair_rows)
    write_tsv(AUDIT, audit_fields, audit_rows)
    SUMMARY.write_text(json.dumps({
        "promotion_id": "module21a-relay-function-batch053-2026-09-02",
        "records_promoted": 1,
        "evidence_ids": [EVIDENCE_ID],
        "promotion_note": PROMOTION_NOTE,
        "upstream_module20a_lr_confidence_changed": False,
        "terminal_tf_assignments_created": False,
        "sql_signaling_edges_created": False,
        "malformed_legacy_rows_touched": False,
    }, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"validated": 1, "applied": 1, "evidence_ids": [EVIDENCE_ID]}, indent=2))


if __name__ == "__main__":
    main()
