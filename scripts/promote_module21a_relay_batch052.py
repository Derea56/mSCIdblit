#!/usr/bin/env python3
"""Promote the two bounded Module 21A WNT7A receptor-complex packets."""

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
AUDIT = RELAY / "module21a_relay_promotion_batch052.tsv"
SUMMARY = RELAY / "module21a_relay_promotion_batch052_summary.json"

PACKET = {
    "M21A-PAIR-EVID-5751": (
        "wnt7a fzd4_lrp5",
        "M21A-REUSE-2817",
        "M20A-LIANA-REMAINING-0490",
        "PMID:25373781; PMCID:PMC4223636; DOI:10.1016/j.devcel.2014.08.018; PMID:40914247; PMCID:PMC12514574; DOI:10.1016/j.jbc.2025.110682",
        "Exact functional WNT7A-GPR124/FZD4-LRP5 context supports qualified-high promotion; preserve RECK/broader WNT7 coreceptor context, the 2025 FZD-independent complex, and TCF/LEF as a reporter endpoint.",
    ),
    "M21A-PAIR-EVID-5754": (
        "wnt7a fzd5_lrp6",
        "M21A-REUSE-2819",
        "M20A-LIANA-REMAINING-0493",
        "PMID:12857724; DOI:10.1074/jbc.M300191200; PMID:40914247; PMCID:PMC12514574; DOI:10.1016/j.jbc.2025.110682",
        "Exact functional rat-PC12 WNT7A-FZD5-LRP6 context supports qualified-high promotion; preserve inferred ternary contact, DKK1/DKK3 antagonism, alternative GPR124-RECK-LRP5/6 context, and TCF/LEF as a reporter endpoint.",
    ),
}

SOURCE_CORRECTIONS = {
    "M21A-PAIR-EVID-5754": (
        "DOI:10.1074/jbc.M300191200; PMID:40914247; PMCID:PMC12514574; DOI:10.1016/j.jbc.2025.110682",
        "PMID:12857724; DOI:10.1074/jbc.M300191200; PMID:40914247; PMCID:PMC12514574; DOI:10.1016/j.jbc.2025.110682",
    )
}
CORRECTION_NOTE = "Source PMID 12857724 added to the DOI-resolved record before batch052 materialization; the related EVID-5753 hold remains untouched."
PROMOTION_NOTE = "Module 21A relay/function promotion batch052 (2026-09-02): evidence tier raised to high for the exact, context-bounded packet; evidence-layer scope, upstream Module 20A LR confidence, terminal-TF status, and SCI transfer remain unchanged."


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


def correct_sources(rows, key):
    old, new = SOURCE_CORRECTIONS.get(key, (None, None))
    if old is None:
        return
    for row in rows:
        if row.get(key) == old:
            row[key] = new


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
    review_rows = [row for rows in review_rows_by_file for row in rows]

    # Normalize only the exact promoted review/detail lineage. EVID-5753 is not touched.
    detail = index(detail_rows, "evidence_id")
    reviews = index(review_rows, "review_id")
    for evidence_id, (_pair, _reuse, review_id, _citations, _basis) in PACKET.items():
        old, new = SOURCE_CORRECTIONS.get(evidence_id, (None, None))
        if old and detail[evidence_id].get("source_locators") == old:
            detail[evidence_id]["source_locators"] = new
        if old and reviews[review_id].get("source_locators") == old:
            reviews[review_id]["source_locators"] = new

    reuse = index(reuse_rows, "pathway_reuse_key")
    coverage_by_evidence = {
        evidence_id: next((row for row in pair_rows if row.get("module21a_evidence_ids") == evidence_id), None)
        for evidence_id in PACKET
    }
    review_by_id = reviews

    for evidence_id, (pair_key, reuse_key, review_id, citations, _basis) in PACKET.items():
        row = detail.get(evidence_id)
        if row is None or row.get("confidence_tier") not in {"medium", "medium-high"} or row.get("pathway_reuse_key") != reuse_key or row.get("source_locators") != citations:
            raise SystemExit(f"detail lineage mismatch: {evidence_id}")
        if not all(layer in row.get("evidence_layer", "") for layer in ("receptor_proximal_relay", "downstream_pathway_function")):
            raise SystemExit(f"{evidence_id} lacks required evidence layers")
        review = review_by_id.get(review_id)
        if review is None or review.get("evidence_id") != evidence_id or review.get("pair_key") != pair_key or review.get("source_locators") != citations or review.get("confidence_tier") not in {"medium", "medium-high"} or review.get("review_status") != "reviewed_relay_candidate":
            raise SystemExit(f"review lineage mismatch: {evidence_id}")
        if reuse.get(reuse_key) is None or reuse[reuse_key].get("evidence_ids") != evidence_id:
            raise SystemExit(f"reuse lineage mismatch: {evidence_id}")
        coverage = coverage_by_evidence.get(evidence_id)
        if coverage is None or coverage.get("pair_key") != pair_key or coverage.get("module21a_status") != "reviewed_relay_candidate":
            raise SystemExit(f"coverage lineage mismatch: {evidence_id}")

    audit_fields = ["evidence_id", "review_id", "pair_key", "pathway_reuse_key", "previous_tier", "new_tier", "source_locators", "decision_basis", "source_metadata_correction", "upstream_lr_confidence_unchanged", "terminal_tf_status_unchanged", "sql_materialization"]
    audit_rows = []
    for evidence_id, packet in sorted(PACKET.items()):
        audit_rows.append({
            "evidence_id": evidence_id,
            "review_id": packet[2],
            "pair_key": packet[0],
            "pathway_reuse_key": packet[1],
            "previous_tier": detail[evidence_id]["confidence_tier"],
            "new_tier": "high",
            "source_locators": detail[evidence_id]["source_locators"],
            "decision_basis": packet[4],
            "source_metadata_correction": CORRECTION_NOTE if evidence_id in SOURCE_CORRECTIONS else "none",
            "upstream_lr_confidence_unchanged": "true",
            "terminal_tf_status_unchanged": "true",
            "sql_materialization": "false",
        })

    if not args.apply:
        print(json.dumps({"validated": len(audit_rows), "apply": False, "evidence_ids": sorted(PACKET)}, indent=2))
        return

    for evidence_id, packet in PACKET.items():
        detail[evidence_id]["confidence_tier"] = "high"
        detail[evidence_id]["limitations"] = append_once(detail[evidence_id]["limitations"], PROMOTION_NOTE)
        if evidence_id in SOURCE_CORRECTIONS:
            detail[evidence_id]["limitations"] = append_once(detail[evidence_id]["limitations"], CORRECTION_NOTE)
        review = review_by_id[packet[2]]
        review["confidence_tier"] = "high"
        review["curator_note"] = append_once(review["curator_note"], PROMOTION_NOTE)
        if evidence_id in SOURCE_CORRECTIONS:
            review["curator_note"] = append_once(review["curator_note"], CORRECTION_NOTE)
        reuse[packet[1]]["validation_status"] = "promoted_high_batch052"
        reuse[packet[1]]["limitations"] = append_once(reuse[packet[1]]["limitations"], PROMOTION_NOTE)
        coverage_by_evidence[evidence_id]["curator_notes"] = append_once(coverage_by_evidence[evidence_id]["curator_notes"], PROMOTION_NOTE)

    write_tsv(DETAIL, detail_fields, detail_rows)
    for path, fields, rows in zip(REVIEW_FILES, review_fields, review_rows_by_file):
        write_tsv(path, fields, rows)
    write_tsv(REUSE, reuse_fields, reuse_rows)
    write_tsv(PAIRS, pair_fields, pair_rows)
    write_tsv(AUDIT, audit_fields, audit_rows)
    SUMMARY.write_text(json.dumps({
        "promotion_id": "module21a-relay-function-batch052-2026-09-02",
        "records_promoted": len(audit_rows),
        "evidence_ids": sorted(PACKET),
        "source_metadata_corrections": ["M21A-PAIR-EVID-5754"],
        "promotion_note": PROMOTION_NOTE,
        "correction_note": CORRECTION_NOTE,
        "upstream_module20a_lr_confidence_changed": False,
        "terminal_tf_assignments_created": False,
        "sql_signaling_edges_created": False,
        "malformed_legacy_rows_touched": False,
    }, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"validated": len(audit_rows), "applied": len(audit_rows), "evidence_ids": sorted(PACKET)}, indent=2))


if __name__ == "__main__":
    main()
