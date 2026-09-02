#!/usr/bin/env python3
"""Promote six bounded Module 21A costimulatory, growth-factor, and cytokine packets."""

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
REVIEW_FILE = RELAY / "module21a_pair_relay_review_batches218_219.tsv"
AUDIT = RELAY / "module21a_relay_promotion_batch033.tsv"
SUMMARY = RELAY / "module21a_relay_promotion_batch033_summary.json"

PACKET = {
    "M21A-PAIR-EVID-5340": ("icosl icos", "M21A-REUSE-2497", "M20A-EXT-2099", "PMID:19915142; PMID:30319662; PMID:19603141", "reviewed_relay_candidate", "Exact forward ICOS costimulation with PI3K/AKT/MAPK and T-cell differentiation/cytokine function supports qualified-high relay/function; reverse ICOSL signaling remains separate and no terminal TF is inferred."),
    "M21A-PAIR-EVID-5341": ("igf1 igf1r", "M21A-REUSE-2498", "M20A-EXT-2101", "PMID:19406949; PMID:18829558; PMID:10669726", "reviewed_relay_candidate", "Exact IGF1R RTK, IRS-PI3K-AKT, and MAPK/ERK relay/function supports qualified-high promotion; heterogeneous epithelial/cancer context remains bounded."),
    "M21A-PAIR-EVID-5343": ("igf2 igf1r", "M21A-REUSE-2500", "M20A-EXT-2107", "PMID:10207053; PMID:19406949; DOI:10.1210/en.2008-1473", "reviewed_relay_candidate", "Exact IGF2-IGF1R relay/function supports qualified-high promotion; preserve possible IR-A contribution and receptor-abundance context."),
    "M21A-PAIR-EVID-5345": ("igf2 insr", "M21A-REUSE-2502", "M20A-EXT-2109", "PMID:10207053; PMID:16239300; PMID:19443570", "reviewed_relay_candidate", "IGF2 binds and activates the insulin receptor predominantly through IR-A with mitogenic/survival outputs; promote only the IR-A isoform, not generic INSR."),
    "M21A-PAIR-EVID-5358": ("il15 il15ra_il2rb_il2rg", "M21A-REUSE-2508", "M20A-EXT-2143", "PMID:23104097;PMID:8530383;PMID:19050240;PMID:24500400", "reviewed_relay_candidate", "Exact IL-15 quaternary receptor/trans-presentation and JAK/STAT5 function support qualified-high promotion; IL15RA presents ligand while IL2RB/IL2RG carry principal signaling and cis/trans geometry remains explicit."),
    "M21A-PAIR-EVID-5359": ("il16 cd4", "M21A-REUSE-2509", "M20A-EXT-2147", "PMID:14607889;PMID:11971026;DOI:10.4049/jimmunol.171.10.4965", "reviewed_function_only", "Exact IL-16-CD4 binding and CD4-dependent chemotaxis support qualified-high binding/function; CCR5 is an enhancing cofactor rather than the IL-16 receptor and no intracellular relay is inferred."),
}

PROMOTION_NOTE = "Module 21A relay/function promotion batch033 (2026-09-02): evidence tier raised to high for the exact, context-bounded packet; evidence-layer scope, upstream Module 20A LR confidence, terminal-TF status, and SCI transfer remain unchanged."


def read_tsv(path):
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        return list(reader.fieldnames or []), list(reader)


def write_tsv(path, fields, rows):
    with path.open("w", encoding="utf-8", newline="") as handle:
        csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n").writerows(rows)


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
    review_fields, review_rows = read_tsv(REVIEW_FILE)
    detail, reuse, reviews = index(detail_rows, "evidence_id"), index(reuse_rows, "pathway_reuse_key"), index(review_rows, "review_id")
    for evidence_id, packet in PACKET.items():
        pair_key, reuse_key, review_id, citations, review_status, _basis = packet
        row = detail.get(evidence_id)
        if row is None or row.get("confidence_tier") != "medium-high" or row.get("pathway_reuse_key", "") != reuse_key or row.get("source_locators") != citations:
            raise SystemExit(f"detail lineage mismatch: {evidence_id}")
        required = ("downstream_pathway_function",) if evidence_id == "M21A-PAIR-EVID-5359" else ("receptor_proximal_relay", "downstream_pathway_function")
        if not all(layer in row.get("evidence_layer", "") for layer in required):
            raise SystemExit(f"{evidence_id} lacks required evidence layers")
        review = reviews.get(review_id)
        if (review is None or review.get("evidence_id") != evidence_id or review.get("pair_key") != pair_key or review.get("source_locators") != citations or review.get("confidence_tier") != "medium-high" or review.get("review_status") != review_status):
            raise SystemExit(f"review lineage mismatch: {evidence_id}")
        if reuse.get(reuse_key) is None or reuse[reuse_key].get("evidence_ids") != evidence_id:
            raise SystemExit(f"reuse lineage mismatch: {evidence_id}")
        coverage = next((item for item in pair_rows if item.get("module21a_evidence_ids") == evidence_id), None)
        if coverage is None or coverage.get("pair_key") != pair_key or coverage.get("module21a_status") != review_status:
            raise SystemExit(f"coverage lineage mismatch: {evidence_id}")
    audit_fields = ["evidence_id", "review_id", "pair_key", "pathway_reuse_key", "previous_tier", "new_tier", "source_locators", "decision_basis", "upstream_lr_confidence_unchanged", "terminal_tf_status_unchanged", "sql_materialization"]
    audit_rows = [{"evidence_id": eid, "review_id": p[2], "pair_key": p[0], "pathway_reuse_key": p[1], "previous_tier": detail[eid]["confidence_tier"], "new_tier": "high", "source_locators": detail[eid]["source_locators"], "decision_basis": p[5], "upstream_lr_confidence_unchanged": "true", "terminal_tf_status_unchanged": "true", "sql_materialization": "false"} for eid, p in sorted(PACKET.items())]
    if not args.apply:
        print(json.dumps({"validated": len(audit_rows), "apply": False, "evidence_ids": sorted(PACKET)}, indent=2))
        return
    for evidence_id, packet in PACKET.items():
        detail[evidence_id]["confidence_tier"] = "high"
        detail[evidence_id]["limitations"] = append_once(detail[evidence_id]["limitations"], PROMOTION_NOTE)
        reviews[packet[2]]["confidence_tier"] = "high"
        reviews[packet[2]]["curator_note"] = append_once(reviews[packet[2]]["curator_note"], PROMOTION_NOTE)
        reuse[packet[1]]["validation_status"] = "promoted_high_batch033"
        reuse[packet[1]]["limitations"] = append_once(reuse[packet[1]]["limitations"], PROMOTION_NOTE)
        coverage = next(item for item in pair_rows if item.get("module21a_evidence_ids") == evidence_id)
        coverage["curator_notes"] = append_once(coverage["curator_notes"], PROMOTION_NOTE)
    write_tsv(DETAIL, detail_fields, detail_rows)
    write_tsv(REVIEW_FILE, review_fields, review_rows)
    write_tsv(REUSE, reuse_fields, reuse_rows)
    write_tsv(PAIRS, pair_fields, pair_rows)
    write_tsv(AUDIT, audit_fields, audit_rows)
    SUMMARY.write_text(json.dumps({"promotion_id": "module21a-relay-function-batch033-2026-09-02", "records_promoted": len(audit_rows), "evidence_ids": sorted(PACKET), "promotion_note": PROMOTION_NOTE, "upstream_module20a_lr_confidence_changed": False, "terminal_tf_assignments_created": False, "sql_signaling_edges_created": False, "malformed_legacy_rows_touched": False}, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"validated": len(audit_rows), "applied": len(audit_rows), "evidence_ids": sorted(PACKET)}, indent=2))


if __name__ == "__main__":
    main()
