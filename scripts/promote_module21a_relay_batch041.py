#!/usr/bin/env python3
"""Promote nine bounded Module 21A peptide, immune, and proteolysis packets."""

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
REVIEW = RELAY / "module21a_pair_relay_review_batches224_225.tsv"
AUDIT = RELAY / "module21a_relay_promotion_batch041.tsv"
SUMMARY = RELAY / "module21a_relay_promotion_batch041_summary.json"

PACKET = {
    "M21A-PAIR-EVID-5503": ("oxt oxtr", "M21A-REUSE-2622", "M20A-EXT-2670", "PMID:9512491;PMID:10074787", "Exact OXTR Gq-PLC/IP3-calcium relay and myometrial contractile/reproductive function support qualified-high promotion; preserve tissue-dependent coupling."),
    "M21A-PAIR-EVID-5509": ("pdcd1lg2 pdcd1", "M21A-REUSE-2628", "M20A-EXT-2684", "PMID:11224527;PMID:33990697", "Exact PD-L2/PD-1 inhibitory phosphorylation/SHP2/TCR-proximal relay and reduced T-cell proliferation/cytokines support qualified-high promotion; preserve antigen/TCR context."),
    "M21A-PAIR-EVID-5510": ("pdpn clec1b", "M21A-REUSE-2629", "M20A-EXT-2697", "PMCID:PMC2749330;PMID:20154219;PMID:38561690", "Exact podoplanin/CLEC-2 hemITAM-Src/Syk-PLCgamma2 platelet relay/function supports qualified-high promotion; preserve multimerization and platelet/megakaryocyte context."),
    "M21A-PAIR-EVID-5511": ("pglyrp1 trem1", "M21A-REUSE-2630", "M20A-EXT-2727", "PMID:25595774;PMCID:PMC4319313;DOI:10.1016/j.celrep.2024.113813", "TREM1-DAP12/Syk-ERK relay and myeloid/glial inflammatory function support qualified-high promotion; ligand multimerization or peptidoglycan-complex dependence remains possible."),
    "M21A-PAIR-EVID-5512": ("pigf flt1", "M21A-REUSE-2631", "M20A-EXT-2731", "PMID:26861455;PMID:33599733", "FLT1 tyrosine-kinase PI3K-AKT/ERK/p38 relay and macrophage/RPE inflammatory function support qualified-high promotion; preserve weak, cell-context-dependent signaling and possible VEGFR2 transactivation."),
    "M21A-PAIR-EVID-5514": ("plau plaur", "M21A-REUSE-2633", "M20A-EXT-2746", "PMID:12426305;PMID:16267271;PMID:23709605", "uPA/uPAR-containing integrin/EGFR-FAK/Src/Rac-ERK/PI3K-AKT relay and migration/angiogenesis support qualified-high promotion; preserve scuPA/uPA form, uPAR cleavage, GPI anchoring, and co-receptor context."),
    "M21A-PAIR-EVID-5516": ("plg plgrkt", "M21A-REUSE-2635", "M20A-EXT-2762", "PMID:19897580;PMID:31221672;PMCID:PMC3217361", "Direct membrane binding followed by cell-surface plasmin activation/extracellular proteolysis and macrophage migration support qualified-high function-only promotion; PLGRKT kinase/adaptor relay is not established."),
    "M21A-PAIR-EVID-5518": ("pnoc oprl1", "M21A-REUSE-2637", "M20A-EXT-2772", "PMID:9489755;PMID:9721727;PMID:11413235", "Exact nociceptin/OPRL1 Gi/o/Gbetagamma and PLC/PKC or PI3K-SOS-Ras-ERK relay supports qualified-high promotion; preserve tissue-dependent inhibitory/stimulatory cAMP behavior."),
    "M21A-PAIR-EVID-5519": ("prl prlr", "M21A-REUSE-2638", "M20A-EXT-2808", "PMID:7925093;PMID:9516478;PMID:9314595;PMID:19273609", "Exact prolactin/PRLR JAK2-STAT5 with MAPK/PI3K and mammary differentiation/lactogenesis/proliferation function supports qualified-high promotion; preserve isoform, tissue, and hormonal-state limits."),
}

FUNCTION_ONLY = {"M21A-PAIR-EVID-5516"}
PROMOTION_NOTE = "Module 21A relay/function promotion batch041 (2026-09-02): evidence tier raised to high for the exact, context-bounded packet; evidence-layer scope, upstream Module 20A LR confidence, terminal-TF status, and SCI transfer remain unchanged."


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
    detail, reuse, reviews = index(detail_rows, "evidence_id"), index(reuse_rows, "pathway_reuse_key"), index(review_rows, "review_id")
    for evidence_id, packet in PACKET.items():
        pair_key, reuse_key, review_id, citations, _basis = packet
        row = detail.get(evidence_id)
        if row is None or row.get("confidence_tier") != "medium-high" or row.get("pathway_reuse_key") != reuse_key or row.get("source_locators") != citations:
            raise SystemExit(f"detail lineage mismatch: {evidence_id}")
        required_layers = ("downstream_pathway_function",) if evidence_id in FUNCTION_ONLY else ("receptor_proximal_relay", "downstream_pathway_function")
        if not all(layer in row.get("evidence_layer", "") for layer in required_layers):
            raise SystemExit(f"{evidence_id} lacks required evidence layers")
        review = reviews.get(review_id)
        allowed_status = {"reviewed_function_only"} if evidence_id in FUNCTION_ONLY else {"reviewed_relay_candidate"}
        if (review is None or review.get("evidence_id") != evidence_id or review.get("pair_key") != pair_key or review.get("source_locators") != citations or review.get("confidence_tier") != "medium-high" or review.get("review_status") not in allowed_status):
            raise SystemExit(f"review lineage mismatch: {evidence_id}")
        if reuse.get(reuse_key) is None or reuse[reuse_key].get("evidence_ids") != evidence_id:
            raise SystemExit(f"reuse lineage mismatch: {evidence_id}")
        coverage = next((item for item in pair_rows if item.get("module21a_evidence_ids") == evidence_id), None)
        if coverage is None or coverage.get("pair_key") != pair_key or coverage.get("module21a_status") not in allowed_status:
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
        reuse[packet[1]]["validation_status"] = "promoted_high_batch041"
        reuse[packet[1]]["limitations"] = append_once(reuse[packet[1]]["limitations"], PROMOTION_NOTE)
        coverage = next(item for item in pair_rows if item.get("module21a_evidence_ids") == evidence_id)
        coverage["curator_notes"] = append_once(coverage["curator_notes"], PROMOTION_NOTE)
    write_tsv(DETAIL, detail_fields, detail_rows)
    write_tsv(REVIEW, review_fields, review_rows)
    write_tsv(REUSE, reuse_fields, reuse_rows)
    write_tsv(PAIRS, pair_fields, pair_rows)
    write_tsv(AUDIT, audit_fields, audit_rows)
    SUMMARY.write_text(json.dumps({"promotion_id": "module21a-relay-function-batch041-2026-09-02", "records_promoted": len(audit_rows), "evidence_ids": sorted(PACKET), "promotion_note": PROMOTION_NOTE, "upstream_module20a_lr_confidence_changed": False, "terminal_tf_assignments_created": False, "sql_signaling_edges_created": False, "malformed_legacy_rows_touched": False}, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"validated": len(audit_rows), "applied": len(audit_rows), "evidence_ids": sorted(PACKET)}, indent=2))


if __name__ == "__main__":
    main()
