#!/usr/bin/env python3
"""Promote six bounded Module 21A insulin, adhesion, and galectin packets."""

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
REVIEW = RELAY / "module21a_pair_relay_review_batches220_221.tsv"
AUDIT = RELAY / "module21a_relay_promotion_batch035.tsv"
SUMMARY = RELAY / "module21a_relay_promotion_batch035_summary.json"

PACKET = {
    "M21A-PAIR-EVID-5383": ("ins2 igf1r", "M21A-REUSE-2529", "M20A-EXT-2238", "PMID:20844560;PMCID:PMC3141222;PMID:20360006;PMCID:PMC2878077", "Insulin activation of the IGF1R-containing INSR/IGF1R hybrid receptor, receptor/IRS phosphorylation, knockout-reconstitution, and growth/metabolic function support qualified-high promotion; preserve the hybrid-receptor context and do not generalize to standalone IGF1R or canonical INSR."),
    "M21A-PAIR-EVID-5388": ("jag1 cd46", "M21A-REUSE-2533", "M20A-EXT-2272", "PMID:23086448;PMCID:PMC3505834;DOI:10.1038/ni.2454", "Direct JAG1-CD46 binding with CD46-dependent Notch crosstalk and T-cell function supports qualified-high promotion; preserve the receptor-complex/crosstalk scope, with HES1/RBPJ as pathway readouts rather than direct TF occupancy."),
    "M21A-PAIR-EVID-5389": ("kiss1 kiss1r", "M21A-REUSE-2534", "M20A-EXT-2278", "PMID:24295737;PMCID:PMC3890437", "Exact KISS1/KISS1R GPCR activation, sustained receptor-dependent calcium signaling, and trafficking function support qualified-high promotion; Gq/PLC/ERK placement remains bounded pharmacology and no terminal-TF claim is added."),
    "M21A-PAIR-EVID-5391": ("l1cam egfr", "M21A-REUSE-2536", "M20A-EXT-2314", "PMCID:PMC379294;PMID:12631718;DOI:10.1083/jcb.200208081", "L1CAM-dependent EGFR cis/trans association, transactivation, phosphorylation, and neurite/adhesion function support qualified-high promotion; require cis co-organization and do not represent soluble L1CAM or generic direct EGFR binding."),
    "M21A-PAIR-EVID-5398": ("lgals1 cd69", "M21A-REUSE-2538", "M20A-EXT-2351", "PMID:24752896;PMCID:PMC4054309;DOI:10.1128/MCB.00348-14", "Glycan-dependent LGALS1-CD69 binding and CD69-dependent suppression of Th17 differentiation support qualified-high downstream/function promotion; CD69 has no resolved intracellular relay here and Gal-1 has other glycoprotein receptors."),
    "M21A-PAIR-EVID-5399": ("lgals1 itgb1", "M21A-REUSE-2539", "M20A-EXT-2352", "PMID:14550305;DOI:10.1016/j.bbrc.2003.09.112", "LGALS1 binding to an ITGB1-containing integrin, beta1-integrin activation, FAK-associated phosphorylation, and adhesion support qualified-high promotion; the alpha partner is unresolved, so no specific heterodimer or autonomous ITGB1 claim is added."),
}

PROMOTION_NOTE = "Module 21A relay/function promotion batch035 (2026-09-02): evidence tier raised to high for the exact, context-bounded packet; evidence-layer scope, upstream Module 20A LR confidence, terminal-TF status, and SCI transfer remain unchanged."


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
    review_fields, review_rows = read_tsv(REVIEW)
    detail = index(detail_rows, "evidence_id")
    reuse = index(reuse_rows, "pathway_reuse_key")
    reviews = index(review_rows, "review_id")
    for evidence_id, packet in PACKET.items():
        pair_key, reuse_key, review_id, citations, _basis = packet
        row = detail.get(evidence_id)
        if row is None or row.get("confidence_tier") not in {"medium", "medium-high"} or row.get("pathway_reuse_key") != reuse_key or row.get("source_locators") != citations:
            raise SystemExit(f"detail lineage mismatch: {evidence_id}")
        required_layers = ("downstream_pathway_function",) if evidence_id == "M21A-PAIR-EVID-5398" else ("receptor_proximal_relay", "downstream_pathway_function")
        if not all(layer in row.get("evidence_layer", "") for layer in required_layers):
            raise SystemExit(f"{evidence_id} lacks required evidence layers")
        review = reviews.get(review_id)
        allowed_status = {"reviewed_relay_candidate"} if evidence_id != "M21A-PAIR-EVID-5398" else {"reviewed_function_only"}
        if (review is None or review.get("evidence_id") != evidence_id or review.get("pair_key") != pair_key or review.get("source_locators") != citations or review.get("confidence_tier") not in {"medium", "medium-high"} or review.get("review_status") not in allowed_status):
            raise SystemExit(f"review lineage mismatch: {evidence_id}")
        if reuse.get(reuse_key) is None or reuse[reuse_key].get("evidence_ids") != evidence_id:
            raise SystemExit(f"reuse lineage mismatch: {evidence_id}")
        coverage_row = next((item for item in pair_rows if item.get("module21a_evidence_ids") == evidence_id), None)
        allowed_coverage_status = {"reviewed_relay_candidate"} if evidence_id != "M21A-PAIR-EVID-5398" else {"reviewed_function_only"}
        if coverage_row is None or coverage_row.get("pair_key") != pair_key or coverage_row.get("module21a_status") not in allowed_coverage_status:
            raise SystemExit(f"coverage lineage mismatch: {evidence_id}")
    audit_fields = ["evidence_id", "review_id", "pair_key", "pathway_reuse_key", "previous_tier", "new_tier", "source_locators", "decision_basis", "upstream_lr_confidence_unchanged", "terminal_tf_status_unchanged", "sql_materialization"]
    audit_rows = [{"evidence_id": eid, "review_id": packet[2], "pair_key": packet[0], "pathway_reuse_key": packet[1], "previous_tier": detail[eid]["confidence_tier"], "new_tier": "high", "source_locators": detail[eid]["source_locators"], "decision_basis": packet[4], "upstream_lr_confidence_unchanged": "true", "terminal_tf_status_unchanged": "true", "sql_materialization": "false"} for eid, packet in sorted(PACKET.items())]
    if not args.apply:
        print(json.dumps({"validated": len(audit_rows), "apply": False, "evidence_ids": sorted(PACKET)}, indent=2))
        return
    for evidence_id, packet in PACKET.items():
        detail[evidence_id]["confidence_tier"] = "high"
        detail[evidence_id]["limitations"] = append_once(detail[evidence_id]["limitations"], PROMOTION_NOTE)
        reviews[packet[2]]["confidence_tier"] = "high"
        reviews[packet[2]]["curator_note"] = append_once(reviews[packet[2]]["curator_note"], PROMOTION_NOTE)
        reuse[packet[1]]["validation_status"] = "promoted_high_batch035"
        reuse[packet[1]]["limitations"] = append_once(reuse[packet[1]]["limitations"], PROMOTION_NOTE)
        coverage_row = next(item for item in pair_rows if item.get("module21a_evidence_ids") == evidence_id)
        coverage_row["curator_notes"] = append_once(coverage_row["curator_notes"], PROMOTION_NOTE)
    write_tsv(DETAIL, detail_fields, detail_rows)
    write_tsv(REVIEW, review_fields, review_rows)
    write_tsv(REUSE, reuse_fields, reuse_rows)
    write_tsv(PAIRS, pair_fields, pair_rows)
    write_tsv(AUDIT, audit_fields, audit_rows)
    SUMMARY.write_text(json.dumps({"promotion_id": "module21a-relay-function-batch035-2026-09-02", "records_promoted": len(audit_rows), "evidence_ids": sorted(PACKET), "promotion_note": PROMOTION_NOTE, "upstream_module20a_lr_confidence_changed": False, "terminal_tf_assignments_created": False, "sql_signaling_edges_created": False, "malformed_legacy_rows_touched": False}, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"validated": len(audit_rows), "applied": len(audit_rows), "evidence_ids": sorted(PACKET)}, indent=2))


if __name__ == "__main__":
    main()
