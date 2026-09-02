#!/usr/bin/env python3
"""Promote eleven bounded Module 21A MDK, MFGE8, and adhesion packets."""

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
REVIEW_FILES = [RELAY / "module21a_pair_relay_review_batches220_221.tsv", RELAY / "module21a_pair_relay_review_batches222_223.tsv"]
AUDIT = RELAY / "module21a_relay_promotion_batch037.tsv"
SUMMARY = RELAY / "module21a_relay_promotion_batch037_summary.json"

PACKET = {
    "M21A-PAIR-EVID-5420": ("mdk lrp1", "M21A-REUSE-2556", "M20A-EXT-2447", "PMID:12215536;PMCID:PMC134045;PMID:38098484", "MDK endocytosis/nucleolin-assisted nuclear-targeting and survival function support qualified-high promotion only in the LRP/LRP1-containing context; do not claim LRP1 kinase signaling or a terminal TF."),
    "M21A-PAIR-EVID-5421": ("mdk ncl", "M21A-REUSE-2557", "M20A-EXT-2449", "PMID:12215536;PMCID:PMC134045;PMID:12084985", "NCL-dependent MDK nucleocytoplasmic shuttling/nuclear-targeting function supports qualified-high function-only promotion; cell-surface/intracellular nucleolin is multifunctional and not a canonical transmembrane receptor."),
    "M21A-PAIR-EVID-5422": ("mdk notch2", "M21A-REUSE-2558", "M20A-EXT-2450", "PMID:18469519;PMID:21632553;Reactome:R-HSA-2974737", "Context-specific MDK-NOTCH2/NICD2-JAK2/STAT3 EMT and chemoresistance function supports qualified-high promotion; preserve additional MDK-receptor possibilities and STAT3 as a measured, non-exclusive endpoint."),
    "M21A-PAIR-EVID-5423": ("mdk ptprz1", "M21A-REUSE-2559", "M20A-EXT-2451", "PMID:10212223", "Direct glycosaminoglycan-dependent MDK-PTPRZ1 binding and PTPRZ1-dependent neuronal migration support qualified-high function-only promotion; PTPRZ1 is a receptor phosphatase and no unique intracellular relay is claimed."),
    "M21A-PAIR-EVID-5427": ("mfap5 notch1", "M21A-REUSE-2562", "M20A-EXT-2461", "PMID:31190277;PMCID:PMC6882185", "MFAP5-NOTCH1 co-IP, dose/knockdown concordance, and Notch-linked tumor invasion/migration function support qualified-high promotion; preserve tumor context and no purified affinity or direct TF-occupancy claim."),
    "M21A-PAIR-EVID-5428": ("mfge8 itgb3", "M21A-REUSE-2563", "M20A-EXT-2463", "PMCID:PMC4273653;DOI:10.1038/nm.3450", "Exact MFGE8-alphaVbeta3 integrin-linked AKT and fatty-acid-uptake function support qualified-high promotion; preserve the complete heterodimer and do not promote ITGB3 alone."),
    "M21A-PAIR-EVID-5429": ("mfge8 itgb5", "M21A-REUSE-2564", "M20A-EXT-2464", "PMCID:PMC4273653;DOI:10.1038/nm.3450", "Exact MFGE8-alphaVbeta5 integrin-linked AKT and functional output support qualified-high promotion; preserve the complete heterodimer and do not promote ITGB5 alone."),
    "M21A-PAIR-EVID-5430": ("mfge8 pdgfrb", "M21A-REUSE-2565", "M20A-EXT-2465", "PMID:21868707;PMCID:PMC6999705", "Integrin-associated MFGE8-PDGFRB retention/cross-talk and PDGF-BB-dependent pericyte migration support qualified-high promotion only in the alphaV-integrin/PDGF-BB context; no direct purified MFGE8-PDGFRB binding is claimed."),
    "M21A-PAIR-EVID-5432": ("mif egfr", "M21A-REUSE-2567", "M20A-EXT-2473", "PMCID:PMC4785887", "Secreted O-GlcNAcylated MIF antagonism of EGF/EGFR activation with ERK/c-JUN and invasion outputs supports qualified-high promotion; preserve inhibitory ligand direction and mammalian secretion, with c-JUN as a pathway readout."),
    "M21A-PAIR-EVID-5437": ("myl9 cd69", "M21A-REUSE-2570", "M20A-EXT-2504", "PMID:28783682;DOI:10.1126/sciimmunol.aaf9154", "Exact MYL9-CD69 binding and activated CD69-positive lymphocyte recruitment/retention support qualified-high function-only promotion; CD69-specific intracellular relay remains unresolved and no terminal TF is assigned."),
    "M21A-PAIR-EVID-5439": ("ncam1 gfra1", "M21A-REUSE-2571", "M20A-EXT-2515", "PMID:18353777;DOI:10.1016/S0092-8674(03)00435-5", "The exact GDNF-GFRA1-NCAM1 receptor-complex/coreceptor association with NCAM-associated Fyn/FAK and neurite function supports qualified-high promotion; preserve receptor-receptor orientation and do not model NCAM1 as an independent soluble ligand."),
}

FUNCTION_ONLY = {"M21A-PAIR-EVID-5420", "M21A-PAIR-EVID-5421", "M21A-PAIR-EVID-5423", "M21A-PAIR-EVID-5437"}
PROMOTION_NOTE = "Module 21A relay/function promotion batch037 (2026-09-02): evidence tier raised to high for the exact, context-bounded packet; evidence-layer scope, upstream Module 20A LR confidence, terminal-TF status, and SCI transfer remain unchanged."


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
        reuse[packet[1]]["validation_status"] = "promoted_high_batch037"
        reuse[packet[1]]["limitations"] = append_once(reuse[packet[1]]["limitations"], PROMOTION_NOTE)
        coverage = next(item for item in pair_rows if item.get("module21a_evidence_ids") == evidence_id)
        coverage["curator_notes"] = append_once(coverage["curator_notes"], PROMOTION_NOTE)
    write_tsv(DETAIL, detail_fields, detail_rows)
    for path, fields, rows in zip(REVIEW_FILES, review_fields, review_rows_by_file):
        write_tsv(path, fields, rows)
    write_tsv(REUSE, reuse_fields, reuse_rows)
    write_tsv(PAIRS, pair_fields, pair_rows)
    write_tsv(AUDIT, audit_fields, audit_rows)
    SUMMARY.write_text(json.dumps({"promotion_id": "module21a-relay-function-batch037-2026-09-02", "records_promoted": len(audit_rows), "evidence_ids": sorted(PACKET), "promotion_note": PROMOTION_NOTE, "upstream_module20a_lr_confidence_changed": False, "terminal_tf_assignments_created": False, "sql_signaling_edges_created": False, "malformed_legacy_rows_touched": False}, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"validated": len(audit_rows), "applied": len(audit_rows), "evidence_ids": sorted(PACKET)}, indent=2))


if __name__ == "__main__":
    main()
