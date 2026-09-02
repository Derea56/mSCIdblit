#!/usr/bin/env python3
"""Promote twelve bounded Module 21A SOSTDC1, SPINT1, SPON, SPP1, and SHH packets."""

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
REVIEW_FILES = [RELAY / "module21a_pair_relay_review_batches230.tsv"]
AUDIT = RELAY / "module21a_relay_promotion_batch049.tsv"
SUMMARY = RELAY / "module21a_relay_promotion_batch049_summary.json"

PACKET = {
    "M21A-PAIR-EVID-5660": ("sostdc1 lrp4", "M21A-REUSE-2753", "M20A-EXT-3181", "PMID:19116665; PMID:28694256", "Exact extracellular SOSTDC1-LRP4 anchor/coreceptor to Wnt/BMP integration and developmental function supports qualified-high promotion; preserve unresolved LRP4 cytoplasmic relay and no direct SOSTDC1-Shh claim."),
    "M21A-PAIR-EVID-5661": ("sostdc1 lrp6", "M21A-REUSE-2754", "M20A-EXT-3183", "PMID:30776499; PMCID:PMC6458996; DOI:10.1016/j.bone.2019.02.012", "Exact extracellular SOSTDC1-LRP6 binding and Wnt/BMP attenuation function supports qualified-high promotion; preserve mouse osteoblast/myeloma-contact context and no defined intracellular relay or TF."),
    "M21A-PAIR-EVID-5662": ("spint1 st14", "M21A-REUSE-2755", "M20A-EXT-3187", "PMID:19389929; PMCID:PMC2684167", "Exact extracellular SPINT1-ST14/matriptase inhibitor-protease function supports qualified-high promotion; preserve protease/PAR2-p38 substrate-control topology and do not call it a canonical kinase receptor."),
    "M21A-PAIR-EVID-5663": ("spon1 app", "M21A-REUSE-2756", "M20A-EXT-3189", "PMID:16227578", "Exact full-length F-spondin bridge to APP plus ApoER2/LRP8 receptor-complex trafficking and processing function supports qualified-high promotion; preserve APP/LRP8 context and no generic TF relay."),
    "M21A-PAIR-EVID-5664": ("spon1 lrp8", "M21A-REUSE-2757", "M20A-EXT-3190", "PMID:16227578", "Exact F-spondin-LRP8/ApoER2 contact within the APP receptor complex supports qualified-high promotion; preserve trafficking/APP-processing scope and unresolved unique LRP8 cytoplasmic relay."),
    "M21A-PAIR-EVID-5665": ("spon2 itgam", "M21A-REUSE-2758", "M20A-EXT-3191", "PMID:16105980; PMCID:PMC1895097; DOI:10.1182/blood-2005-04-1658; PMID:19153605; DOI:10.1091/mbc.9.6.1425; PMID:30869196; PMCID:PMC6484411; DOI:10.1111/jcmm.14236", "Exact mindin/Mac-1 alphaM-beta2 complex relay/function supports qualified-high promotion; preserve ITGAM as a subunit, Syk/MAPK macrophage context, and no generic RELA/TF claim."),
    "M21A-PAIR-EVID-5666": ("spon2 itgb2", "M21A-REUSE-2759", "M20A-EXT-3192", "PMID:16105980; PMCID:PMC1895097; DOI:10.1182/blood-2005-04-1658; PMID:19153605; DOI:10.1091/mbc.9.6.1425; PMID:30869196; PMCID:PMC6484411; DOI:10.1111/jcmm.14236", "Exact mindin/Mac-1 alphaM-beta2 complex relay/function supports qualified-high promotion; preserve ITGB2 as a subunit, macrophage Syk/MAPK context, and no generic RELA/TF claim."),
    "M21A-PAIR-EVID-5667": ("spp1 cd44", "M21A-REUSE-2760", "M20A-EXT-3194", "PMID:34070790; PMID:17332338", "Exact OPN-CD44 variant binding plus beta1-integrin cooperation and FAK/integrin motility function supports qualified-high promotion; preserve CD44 isoform and integrin coreceptor context."),
    "M21A-PAIR-EVID-5669": ("spp1 itga5_itgb1", "M21A-REUSE-2762", "M20A-EXT-3196", "PMID:10673366; DOI:10.1006/bbrc.1999.2032", "Exact OPN-alpha5beta1 binding/adhesion function supports qualified-high promotion; preserve the heterodimer and RGD/processed-ligand context and do not infer a kinase or TF branch."),
    "M21A-PAIR-EVID-5670": ("spp1 itga8_itgb1", "M21A-REUSE-2763", "M20A-EXT-3197", "PMID:9614184; PMCID:PMC25364; DOI:10.1091/mbc.9.6.1425", "Exact OPN-alpha8beta1 binding/adhesion and kidney-morphogenesis function supports qualified-high promotion; preserve the heterodimer and developmental context without a unique relay or TF claim."),
    "M21A-PAIR-EVID-5671": ("spp1 itga9_itgb1", "M21A-REUSE-2764", "M20A-EXT-3198", "PMID:19417209; DOI:10.1182/blood-2009-01-197988; PMID:34070790", "Exact thrombin-cleaved OPN-alpha9beta1 binding and hematopoietic migration/retention function supports qualified-high promotion; preserve processed ligand and cell context and do not infer a kinase/TF branch."),
    "M21A-PAIR-EVID-5672": ("spp1 itgav_itgb1", "M21A-REUSE-2765", "M20A-EXT-3199", "PMID:7592829; DOI:10.1074/jbc.270.44.26232; PMID:10861844", "Exact OPN-alphaVbeta1 binding/adhesion and qualified migration function supports qualified-high promotion; preserve integrin-dependent context and no terminal TF claim."),
}

FUNCTION_ONLY = {"M21A-PAIR-EVID-5661", "M21A-PAIR-EVID-5663", "M21A-PAIR-EVID-5669", "M21A-PAIR-EVID-5670", "M21A-PAIR-EVID-5671", "M21A-PAIR-EVID-5672"}
PROMOTION_NOTE = "Module 21A relay/function promotion batch049 (2026-09-02): evidence tier raised to high for the exact, context-bounded packet; evidence-layer scope, upstream Module 20A LR confidence, terminal-TF status, and SCI transfer remain unchanged."


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

    audit_fields = ["evidence_id", "review_id", "pair_key", "pathway_reuse_key", "previous_tier", "new_tier", "source_locators", "decision_basis", "upstream_lr_confidence_unchanged", "terminal_tf_status_unchanged", "sql_materialization"]
    audit_rows = [{"evidence_id": evidence_id, "review_id": packet[2], "pair_key": packet[0], "pathway_reuse_key": packet[1], "previous_tier": detail[evidence_id]["confidence_tier"], "new_tier": "high", "source_locators": detail[evidence_id]["source_locators"], "decision_basis": packet[4], "upstream_lr_confidence_unchanged": "true", "terminal_tf_status_unchanged": "true", "sql_materialization": "false"} for evidence_id, packet in sorted(PACKET.items())]
    if not args.apply:
        print(json.dumps({"validated": len(audit_rows), "apply": False, "evidence_ids": sorted(PACKET)}, indent=2))
        return

    for evidence_id, packet in PACKET.items():
        detail[evidence_id]["confidence_tier"] = "high"
        detail[evidence_id]["limitations"] = append_once(detail[evidence_id]["limitations"], PROMOTION_NOTE)
        review = reviews[packet[2]]
        review["confidence_tier"] = "high"
        review["curator_note"] = append_once(review["curator_note"], PROMOTION_NOTE)
        reuse[packet[1]]["validation_status"] = "promoted_high_batch049"
        reuse[packet[1]]["limitations"] = append_once(reuse[packet[1]]["limitations"], PROMOTION_NOTE)
        coverage = next(item for item in pair_rows if item.get("module21a_evidence_ids") == evidence_id)
        coverage["curator_notes"] = append_once(coverage["curator_notes"], PROMOTION_NOTE)

    write_tsv(DETAIL, detail_fields, detail_rows)
    for path, fields, rows in zip(REVIEW_FILES, review_fields, review_rows_by_file):
        write_tsv(path, fields, rows)
    write_tsv(REUSE, reuse_fields, reuse_rows)
    write_tsv(PAIRS, pair_fields, pair_rows)
    write_tsv(AUDIT, audit_fields, audit_rows)
    SUMMARY.write_text(json.dumps({"promotion_id": "module21a-relay-function-batch049-2026-09-02", "records_promoted": len(audit_rows), "evidence_ids": sorted(PACKET), "promotion_note": PROMOTION_NOTE, "upstream_module20a_lr_confidence_changed": False, "terminal_tf_assignments_created": False, "sql_signaling_edges_created": False, "malformed_legacy_rows_touched": False}, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"validated": len(audit_rows), "applied": len(audit_rows), "evidence_ids": sorted(PACKET)}, indent=2))


if __name__ == "__main__":
    main()
