#!/usr/bin/env python3
"""Promote seven bounded Module 21A GDF receptor-complex packets."""

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
REVIEW_FILES = [
    RELAY / "module21a_pair_relay_review_batches214_215.tsv",
    RELAY / "module21a_pair_relay_review_batches216_217.tsv",
]
AUDIT = RELAY / "module21a_relay_promotion_batch029.tsv"
SUMMARY = RELAY / "module21a_relay_promotion_batch029_summary.json"

PACKET = {
    "M21A-PAIR-EVID-5265": {
        "pair_key": "gdf11 acvr2b_tgfbr1", "reuse_key": "M21A-REUSE-2456", "review_id": "M20A-EXT-1770",
        "citations": "PMCID:PMC1525155; DOI:10.1038/nature03873; PMID:16845371; PMCID:PMC6681762",
        "basis": "The structural GDF11-ActRIIB/ACVR2B-ALK5/TGFBR1 ternary complex plus Acvr2b/Alk5 developmental genetics supports qualified-high exact receptor-complex relay/function; preserve the composite topology and context-specific developmental scope.",
    },
    "M21A-PAIR-EVID-5267": {
        "pair_key": "gdf2 acvr2a_acvrl1", "reuse_key": "M21A-REUSE-2457", "review_id": "M20A-EXT-1777",
        "citations": "PMID:17068149; PMID:22622516; DOI:10.1021/bi300942x",
        "basis": "Exact GDF2/BMP9-ACVRL1/ALK1 endothelial response with ACVR2A/ActRIIA support, SMAD1/5/8-ID1/3 outputs, and migration/growth function supports qualified-high composite relay/function; preserve variable type-II usage and endothelial context.",
    },
    "M21A-PAIR-EVID-5269": {
        "pair_key": "gdf2 eng", "reuse_key": "M21A-REUSE-2458", "review_id": "M20A-EXT-1779",
        "citations": "PMID:17068149; PMID:22622516; PMID:24896812; PMID:41476036; DOI:10.1038/s41467-025-67531-9",
        "basis": "GDF2/BMP9 engages an ENG plus ACVRL1/ALK1 endothelial co-receptor context with receptor perturbation and SMAD/vascular function outputs, supporting qualified-high co-receptor relay/function; ENG is not promoted as a standalone principal kinase receptor.",
    },
    "M21A-PAIR-EVID-5274": {
        "pair_key": "gdf5 acvr2a_bmpr1a", "reuse_key": "M21A-REUSE-2461", "review_id": "M20A-EXT-1785",
        "citations": "PMID:8702914; DOI:10.1074/jbc.271.35.21345; PMID:15890363; DOI:10.1016/j.jmb.2005.04.015",
        "basis": "Exact GDF5 binding/reconstitution and BMP-SMAD/osteoprogenitor function support qualified-high ACVR2A plus BMPR1A receptor-complex relay/function; BMPR1A is weaker than BMPR1B and recombinant/transfected context remains explicit.",
    },
    "M21A-PAIR-EVID-5275": {
        "pair_key": "gdf5 acvr2a_bmpr1b", "reuse_key": "M21A-REUSE-2462", "review_id": "M20A-EXT-1786",
        "citations": "PMID:8702914; DOI:10.1074/jbc.271.35.21345; PMID:15890363; DOI:10.1016/j.jmb.2005.04.015; PMID:26878848",
        "basis": "Exact preferred BMPR1B receptor binding/reconstitution with ACVR2A support and ACVR2A-dependent neuronal function supports qualified-high composite relay/function; receptor stoichiometry and model-specific type-II usage remain bounded.",
    },
    "M21A-PAIR-EVID-5277": {
        "pair_key": "gdf5 acvr2b_bmpr1b", "reuse_key": "M21A-REUSE-2464", "review_id": "M20A-EXT-1788",
        "citations": "PMID:8702914; DOI:10.1074/jbc.271.35.21345; PMID:15890363; DOI:10.1016/j.jmb.2005.04.015",
        "basis": "Exact preferred BMPR1B/type-II ACVR2B receptor-complex binding and BMP functional readouts support qualified-high relay/function; recombinant/transfected stoichiometry and relative type-II usage remain explicit.",
    },
    "M21A-PAIR-EVID-5278": {
        "pair_key": "gdf6 acvr2a_bmpr1a", "reuse_key": "M21A-REUSE-2465", "review_id": "M20A-EXT-1789",
        "citations": "PMID:23527555; DOI:10.1111/febs.12256; PMID:16049014; DOI:10.1074/jbc.M504629200",
        "basis": "Exact Bmpr1a/Acvr2a perturbation with GDF6-induced SMAD1/5/8, p38, and mesenchymal commitment supports qualified-high receptor-proximal relay/function; key functional evidence is not purified ternary binding and remains mouse-mesenchymal-context limited.",
    },
}

PROMOTION_NOTE = "Module 21A relay/function promotion batch029 (2026-09-02): evidence tier raised to high for the exact, context-bounded packet; evidence-layer scope, upstream Module 20A LR confidence, terminal-TF status, and SCI transfer remain unchanged."


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
    review_rows = [row for rows in review_rows_by_file for row in rows]
    detail = index(detail_rows, "evidence_id")
    reuse = index(reuse_rows, "pathway_reuse_key")
    reviews = index(review_rows, "review_id")

    for evidence_id, expected in PACKET.items():
        row = detail.get(evidence_id)
        if row is None or row.get("confidence_tier") != "medium-high":
            raise SystemExit(f"{evidence_id} missing or not medium-high")
        if not all(layer in row.get("evidence_layer", "") for layer in ("receptor_proximal_relay", "downstream_pathway_function")):
            raise SystemExit(f"{evidence_id} lacks relay/function layers")
        if row.get("pathway_reuse_key") != expected["reuse_key"] or row.get("source_locators") != expected["citations"]:
            raise SystemExit(f"detail lineage mismatch: {evidence_id}")
        review = reviews.get(expected["review_id"])
        if (review is None or review.get("evidence_id") != evidence_id or review.get("pair_key") != expected["pair_key"]
                or review.get("source_locators") != expected["citations"]
                or review.get("confidence_tier") != "medium-high"
                or review.get("review_status") != "reviewed_relay_candidate"):
            raise SystemExit(f"review lineage mismatch: {evidence_id}")
        reuse_row = reuse.get(expected["reuse_key"])
        if reuse_row is None or reuse_row.get("evidence_ids") != evidence_id:
            raise SystemExit(f"reuse lineage mismatch: {evidence_id}")
        coverage = next((item for item in pair_rows if item.get("module21a_evidence_ids") == evidence_id), None)
        if (coverage is None or coverage.get("pair_key") != expected["pair_key"]
                or coverage.get("module21a_status") != "reviewed_relay_candidate"):
            raise SystemExit(f"coverage lineage mismatch: {evidence_id}")

    audit_fields = ["evidence_id", "review_id", "pair_key", "pathway_reuse_key", "previous_tier", "new_tier", "source_locators", "decision_basis", "upstream_lr_confidence_unchanged", "terminal_tf_status_unchanged", "sql_materialization"]
    audit_rows = [{
        "evidence_id": evidence_id,
        "review_id": expected["review_id"],
        "pair_key": expected["pair_key"],
        "pathway_reuse_key": expected["reuse_key"],
        "previous_tier": detail[evidence_id]["confidence_tier"],
        "new_tier": "high",
        "source_locators": detail[evidence_id]["source_locators"],
        "decision_basis": expected["basis"],
        "upstream_lr_confidence_unchanged": "true",
        "terminal_tf_status_unchanged": "true",
        "sql_materialization": "false",
    } for evidence_id, expected in sorted(PACKET.items())]

    if not args.apply:
        print(json.dumps({"validated": len(audit_rows), "apply": False, "evidence_ids": sorted(PACKET)}, indent=2))
        return

    for evidence_id, expected in PACKET.items():
        row = detail[evidence_id]
        row["confidence_tier"] = "high"
        row["limitations"] = append_once(row["limitations"], PROMOTION_NOTE)
        review = reviews[expected["review_id"]]
        review["confidence_tier"] = "high"
        review["curator_note"] = append_once(review["curator_note"], PROMOTION_NOTE)
        reuse_row = reuse[expected["reuse_key"]]
        reuse_row["validation_status"] = "promoted_high_batch029"
        reuse_row["limitations"] = append_once(reuse_row["limitations"], PROMOTION_NOTE)
        coverage = next(item for item in pair_rows if item.get("module21a_evidence_ids") == evidence_id)
        coverage["curator_notes"] = append_once(coverage["curator_notes"], PROMOTION_NOTE)

    write_tsv(DETAIL, detail_fields, detail_rows)
    for path, fields, rows in zip(REVIEW_FILES, review_fields, review_rows_by_file):
        write_tsv(path, fields, rows)
    write_tsv(REUSE, reuse_fields, reuse_rows)
    write_tsv(PAIRS, pair_fields, pair_rows)
    write_tsv(AUDIT, audit_fields, audit_rows)
    SUMMARY.write_text(json.dumps({
        "promotion_id": "module21a-relay-function-batch029-2026-09-02",
        "records_promoted": len(audit_rows),
        "evidence_ids": sorted(PACKET),
        "promotion_note": PROMOTION_NOTE,
        "upstream_module20a_lr_confidence_changed": False,
        "terminal_tf_assignments_created": False,
        "sql_signaling_edges_created": False,
        "malformed_legacy_rows_touched": False,
    }, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"validated": len(audit_rows), "applied": len(audit_rows), "evidence_ids": sorted(PACKET)}, indent=2))


if __name__ == "__main__":
    main()
