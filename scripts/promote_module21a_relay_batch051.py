#!/usr/bin/env python3
"""Promote eight bounded Module 21A UCN, WNT, and chemokine packets."""

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
    RELAY / "module21a_pair_relay_review_batches232.tsv",
    RELAY / "module21a_pair_relay_review_batches234.tsv",
]
AUDIT = RELAY / "module21a_relay_promotion_batch051.tsv"
SUMMARY = RELAY / "module21a_relay_promotion_batch051_summary.json"

PACKET = {
    "M21A-PAIR-EVID-5721": ("ucn crhr2", "M21A-REUSE-2804", "M20A-EXT-3395", "PMID:8612563; DOI:10.1210/endo.137.5.8612563; PMID:12611895; DOI:10.1074/jbc.M210476200; PMID:19008330", "Exact UCN1-CRHR2alpha/beta direct relay/function supports qualified-high promotion; preserve isoform, tissue, and non-exclusive receptor context."),
    "M21A-PAIR-EVID-5723": ("wnt3 ror2", "M21A-REUSE-2806", "M20A-EXT-3485", "PMID:15388793; DOI:10.1210/me.2004-0153", "Exact WNT3-ROR2 association/modulation and osteoblast WNT function supports qualified-high function-only promotion; preserve unresolved FZD/LRP contribution and unchanged ROR2 autophosphorylation."),
    "M21A-PAIR-EVID-5724": ("wnt3 ryk", "M21A-REUSE-2807", "M20A-EXT-3486", "PMID:19000841; DOI:10.1016/j.devcel.2008.10.004", "Exact WNT3-RYK association and gamma-secretase/RYK-ICD transduction supports qualified-high promotion; preserve cell-based association semantics and no added terminal-TF claim."),
    "M21A-PAIR-EVID-5725": ("wnt5a ptk7", "M21A-REUSE-2808", "M20A-EXT-3500", "PMID:26499793; PMCID:PMC4683276; DOI:10.1074/jbc.M115.697615; PMID:21772251; PMCID:PMC3173783", "Exact context-dependent WNT5A-PTK7 JNK/motility relay/function supports qualified-high promotion; preserve ROR2/FZD context and the earlier Xenopus ligand-specific negative boundary."),
    "M21A-PAIR-EVID-5726": ("wnt5a ror1", "M21A-REUSE-2809", "M20A-EXT-3502", "PMID:18287027; DOI:10.1073/pnas.0712148105; PMID:22403610; PMCID:PMC3293865; DOI:10.1371/journal.pone.0031127", "Exact WNT5A-ROR1 association and ROR1/CK1epsilon-to-PI3K-AKT/CREB survival-growth function supports qualified-high promotion; preserve ROR1/ROR2/FZD context and CREB as a measured endpoint."),
    "M21A-PAIR-EVID-5727": ("wnt5b fzd1_lrp6", "M21A-REUSE-2810", "M20A-EXT-3507", "PMID:42256303; DOI:10.1016/j.isci.2026.116129; https://www.sciencedirect.com/science/article/pii/S258900422601504X", "Exact WNT5B-FZD1/LRP6 composite functional branch supports qualified-high function-only promotion; preserve renal exosome/hypoxia disease context and do not claim purified ternary contact or fixed stoichiometry."),
    "M21A-PAIR-EVID-5728": ("wnt7a reck", "M21A-REUSE-2811", "M20A-EXT-3524", "PMID:30304675; PMCID:PMC6338448; DOI:10.1016/j.celrep.2018.09.045", "Exact WNT7A-RECK/GPR124/FZD/LRP signalosome relay/function supports qualified-high promotion; preserve RECK GPI-anchored scaffold topology and TCF/LEF reporter boundaries."),
    "M21A-PAIR-EVID-5732": ("cxcl5 cxcr2", "M21A-REUSE-2815", "M20A-LIANA-REMAINING-0066", "PMID:8702798; PMID:28869519; PMID:20643340; PMCID:PMC3748840; PMID:38627393", "Exact CXCL5/ENA-78-CXCR2 Gi/o-beta-arrestin/internalization relay and neutrophil/sensory function supports qualified-high promotion; preserve processing, GAG, and CXCR2 ligand-promiscuity context."),
}

FUNCTION_ONLY = {"M21A-PAIR-EVID-5723", "M21A-PAIR-EVID-5727"}
PROMOTION_NOTE = "Module 21A relay/function promotion batch051 (2026-09-02): evidence tier raised to high for the exact, context-bounded packet; evidence-layer scope, upstream Module 20A LR confidence, terminal-TF status, and SCI transfer remain unchanged."
LINEAGE_NOTES = {"M21A-PAIR-EVID-5732": "Child audit listed M21A-LIANA-REMAINING-0066; local review and coverage registers both resolve the observed review ID as M20A-LIANA-REMAINING-0066."}


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

    for evidence_id, packet in PACKET.items():
        pair_key, reuse_key, review_id, citations, _basis = packet
        row = detail.get(evidence_id)
        if row is None or row.get("confidence_tier") not in {"medium", "medium-high"} or row.get("pathway_reuse_key") != reuse_key or row.get("source_locators") != citations:
            raise SystemExit(f"detail lineage mismatch: {evidence_id}")
        required_layers = ("downstream_pathway_function",) if evidence_id in FUNCTION_ONLY else ("receptor_proximal_relay", "downstream_pathway_function")
        if not all(layer in row.get("evidence_layer", "") for layer in required_layers):
            raise SystemExit(f"{evidence_id} lacks required evidence layers")
        review = reviews.get(review_id)
        allowed_status = {"reviewed_function_only"} if evidence_id in FUNCTION_ONLY else {"reviewed_relay_candidate"}
        if (review is None or review.get("evidence_id") != evidence_id or review.get("pair_key") != pair_key or review.get("source_locators") != citations or review.get("confidence_tier") not in {"medium", "medium-high"} or review.get("review_status") not in allowed_status):
            raise SystemExit(f"review lineage mismatch: {evidence_id}")
        if reuse.get(reuse_key) is None or reuse[reuse_key].get("evidence_ids") != evidence_id:
            raise SystemExit(f"reuse lineage mismatch: {evidence_id}")
        coverage = next((item for item in pair_rows if item.get("module21a_evidence_ids") == evidence_id), None)
        if coverage is None or coverage.get("pair_key") != pair_key or coverage.get("module21a_status") not in allowed_status:
            raise SystemExit(f"coverage lineage mismatch: {evidence_id}")

    audit_fields = ["evidence_id", "review_id", "pair_key", "pathway_reuse_key", "previous_tier", "new_tier", "source_locators", "decision_basis", "register_lineage_note", "upstream_lr_confidence_unchanged", "terminal_tf_status_unchanged", "sql_materialization"]
    audit_rows = [{"evidence_id": evidence_id, "review_id": packet[2], "pair_key": packet[0], "pathway_reuse_key": packet[1], "previous_tier": detail[evidence_id]["confidence_tier"], "new_tier": "high", "source_locators": detail[evidence_id]["source_locators"], "decision_basis": packet[4], "register_lineage_note": LINEAGE_NOTES.get(evidence_id, "none"), "upstream_lr_confidence_unchanged": "true", "terminal_tf_status_unchanged": "true", "sql_materialization": "false"} for evidence_id, packet in sorted(PACKET.items())]
    if not args.apply:
        print(json.dumps({"validated": len(audit_rows), "apply": False, "evidence_ids": sorted(PACKET)}, indent=2))
        return

    for evidence_id, packet in PACKET.items():
        detail[evidence_id]["confidence_tier"] = "high"
        detail[evidence_id]["limitations"] = append_once(detail[evidence_id]["limitations"], PROMOTION_NOTE)
        if evidence_id in LINEAGE_NOTES:
            detail[evidence_id]["limitations"] = append_once(detail[evidence_id]["limitations"], LINEAGE_NOTES[evidence_id])
        review = reviews[packet[2]]
        review["confidence_tier"] = "high"
        review["curator_note"] = append_once(review["curator_note"], PROMOTION_NOTE)
        if evidence_id in LINEAGE_NOTES:
            review["curator_note"] = append_once(review["curator_note"], LINEAGE_NOTES[evidence_id])
        reuse[packet[1]]["validation_status"] = "promoted_high_batch051"
        reuse[packet[1]]["limitations"] = append_once(reuse[packet[1]]["limitations"], PROMOTION_NOTE)
        coverage = next(item for item in pair_rows if item.get("module21a_evidence_ids") == evidence_id)
        coverage["curator_notes"] = append_once(coverage["curator_notes"], PROMOTION_NOTE)

    write_tsv(DETAIL, detail_fields, detail_rows)
    for path, fields, rows in zip(REVIEW_FILES, review_fields, review_rows_by_file):
        write_tsv(path, fields, rows)
    write_tsv(REUSE, reuse_fields, reuse_rows)
    write_tsv(PAIRS, pair_fields, pair_rows)
    write_tsv(AUDIT, audit_fields, audit_rows)
    SUMMARY.write_text(json.dumps({"promotion_id": "module21a-relay-function-batch051-2026-09-02", "records_promoted": len(audit_rows), "evidence_ids": sorted(PACKET), "promotion_note": PROMOTION_NOTE, "register_lineage_notes": LINEAGE_NOTES, "upstream_module20a_lr_confidence_changed": False, "terminal_tf_assignments_created": False, "sql_signaling_edges_created": False, "malformed_legacy_rows_touched": False}, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"validated": len(audit_rows), "applied": len(audit_rows), "evidence_ids": sorted(PACKET)}, indent=2))


if __name__ == "__main__":
    main()
