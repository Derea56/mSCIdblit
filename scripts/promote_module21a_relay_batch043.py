#!/usr/bin/env python3
"""Promote fourteen bounded Module 21A PTN, PYY, relaxin, and R-spondin packets."""

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
REVIEW = RELAY / "module21a_pair_relay_review_batches226_227.tsv"
AUDIT = RELAY / "module21a_relay_promotion_batch043.tsv"
SUMMARY = RELAY / "module21a_relay_promotion_batch043_summary.json"

PACKET = {
    "M21A-PAIR-EVID-5540": ("ptn itgav_itgb3", "M21A-REUSE-2655", "M20A-EXT-2886", "PMID:19141530;DOI:10.1096/fj.08-117564", "PTN-alphaVbeta3/PTPRZ1 composite binding/capture, beta3 phosphorylation, Src modulation, and endothelial migration support qualified-high promotion; preserve the complete composite and do not claim standalone integrin signaling."),
    "M21A-PAIR-EVID-5541": ("ptn ptprz1", "M21A-REUSE-2656", "M20A-EXT-2891", "PMID:27445335;PMID:28569747;https://www.jci.org/articles/view/76838", "Exact PTPRZ1-dependent PTN phosphatase/function layer supports qualified-high promotion; preserve PTPRZ1 isoform and chondroitin-sulfate state, with ERF phosphorylation restricted to HSPC context."),
    "M21A-PAIR-EVID-5542": ("pyy npy1r", "M21A-REUSE-2657", "M20A-EXT-2905", "PMID:1317848;PMID:10970776", "PYY/NPY1R Gi/o, Gbetagamma/Src/EGFR/PKC, ERK, and intestinal epithelial function support qualified-high promotion; preserve PYY processing and engineered-receptor IEC context."),
    "M21A-PAIR-EVID-5543": ("pyy npy2r", "M21A-REUSE-2658", "M20A-EXT-2906", "PMID:7592910;PMID:19837904", "PYY/NPY2R receptor-proximal Gi/o-cAMP inhibition and calcium support qualified-high promotion only at that layer; preserve PYY1-36 versus PYY3-36 and heterologous context."),
    "M21A-PAIR-EVID-5545": ("qrfp qrfpr", "M21A-REUSE-2660", "M20A-EXT-2910", "PMID:12714592;PMID:21623631;PMID:33655503", "Exact QRFPR/GPR103 Gq/Gi calcium-cAMP relay and neuroendocrine/feeding function support qualified-high promotion; preserve QRFP peptide length and receptor glycosylation."),
    "M21A-PAIR-EVID-5546": ("rarres2 cmklr1", "M21A-REUSE-2661", "M20A-EXT-2912", "PMID:27716822;PMID:18809717;PMID:19720798", "Exact chemerin/CMKLR1 Gi/o-arrestin, calcium/ERK, chemotaxis, and metabolic-cell function support qualified-high promotion; preserve ligand processing and distinguish GPR1/CCRL2."),
    "M21A-PAIR-EVID-5547": ("rbp4 stra6", "M21A-REUSE-2662", "M20A-EXT-2914", "PMID:21368206;PMCID:PMC3434520;PMID:25237067;PMID:22826435", "Holo-RBP4/retinol plus CRBP1/LRAT-dependent STRA6/JAK2-STAT3/5 function supports qualified-high promotion; preserve retinol and interdependence requirements, with STAT outputs context-specific."),
    "M21A-PAIR-EVID-5549": ("retn cap1", "M21A-REUSE-2664", "M20A-EXT-2916", "PMID:24606903;PMCID:PMC3969988;DOI:10.1016/j.molmet.2014.01.005;https://pubmed.ncbi.nlm.nih.gov/24606903/;PMID:31294061", "CAP1/cAMP-PKA inflammatory function supports qualified-high promotion; CAP1 is not a canonical transmembrane receptor, human and mouse resistin are not interchangeable, and TLR4 remains a separate proposed receptor."),
    "M21A-PAIR-EVID-5550": ("rgma neo1", "M21A-REUSE-2665", "M20A-EXT-2921", "PMID:16836993;PMID:19273616;PMID:20643353;PMID:23744777;PMID:33748906;https://pubmed.ncbi.nlm.nih.gov/16836993/", "Exact RGMA/NEO1 co-receptor branch supports qualified-high promotion; preserve Unc5B/LARG/FAK/RhoA versus NEO1/BMP-receptor ternary contexts and do not transfer BMP2 as an RGMA ligand."),
    "M21A-PAIR-EVID-5552": ("rln1 rxfp1", "M21A-REUSE-2667", "M20A-EXT-2931", "PMID:12506116;PMID:25389293;PMID:37081311;PMCID:PMC2814924;DOI:10.1038/s41589-023-01321-6;https://pubmed.ncbi.nlm.nih.gov/25389293/", "Exact relaxin-1/RXFP1 cAMP/PKA/p38 signalosome and tissue function support qualified-high promotion; preserve concentration, conformation, cell context, and multiple G-protein branches."),
    "M21A-PAIR-EVID-5554": ("rln3 rxfp3", "M21A-REUSE-2669", "M20A-EXT-2948", "PMID:16411781;PMID:18434306;PMID:15367576;PMID:24802387;PMID:40410443;DOI:10.1074/jbc.M801911200;https://pubmed.ncbi.nlm.nih.gov/18434306/", "Exact H3 relaxin/RXFP3 Gi/o-cAMP inhibition/ERK and neuroendocrine function support qualified-high promotion; preserve ligand bias and heterologous versus neuronal context."),
    "M21A-PAIR-EVID-5556": ("rps19 c5ar1", "M21A-REUSE-2671", "M20A-EXT-2952", "PMID:9881961;PMID:11107061;PMID:11733378;PMID:20473571;PMID:20869475;DOI:10.1007/s10495-010-0511-y;https://pubmed.ncbi.nlm.nih.gov/20473571/", "Cross-linked extracellular RPS19 dimer/polymer/C5AR1 Gi-calcium/PI3K/PLC-ERK/p38 and chemotaxis support qualified-high promotion; do not claim monomeric RPS19 and preserve agonist/antagonist cell differences."),
    "M21A-PAIR-EVID-5557": ("rspo1 lgr4", "M21A-REUSE-2672", "M20A-EXT-2953", "PMID:21693646;PMID:21727895;PMID:23891289;PMID:24639526;PMCID:PMC3777832;DOI:10.1016/j.str.2013.07.001;https://pubmed.ncbi.nlm.nih.gov/21693646/", "Exact RSPO1/LGR4/FZD-LRP6/RNF43-ZNRF3 Wnt-complex relay and function support qualified-high promotion; preserve facultative complex stoichiometry and reporter-as-pathway-output semantics."),
    "M21A-PAIR-EVID-5558": ("rspo1 lgr5", "M21A-REUSE-2673", "M20A-EXT-2954", "PMID:21693646;PMID:21727895;PMID:23891289;PMID:22473993;PMID:24532711;https://pubmed.ncbi.nlm.nih.gov/21727895/", "Exact RSPO1/LGR5/RNF43-ZNRF3/FZD-LRP6 receptor-surface regulation and intestinal stem-cell function support qualified-high promotion; preserve LGR5 versus LGR4 stoichiometry/endocytosis and reporter boundaries."),
}

RECEPTOR_ONLY = {"M21A-PAIR-EVID-5543"}
PROMOTION_NOTE = "Module 21A relay/function promotion batch043 (2026-09-02): evidence tier raised to high for the exact, context-bounded packet; evidence-layer scope, upstream Module 20A LR confidence, terminal-TF status, and SCI transfer remain unchanged."


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
        required_layers = ("receptor_proximal_relay",) if evidence_id in RECEPTOR_ONLY else ("receptor_proximal_relay", "downstream_pathway_function")
        if not all(layer in row.get("evidence_layer", "") for layer in required_layers):
            raise SystemExit(f"{evidence_id} lacks required evidence layers")
        review = reviews.get(review_id)
        if (review is None or review.get("evidence_id") != evidence_id or review.get("pair_key") != pair_key or review.get("source_locators") != citations or review.get("confidence_tier") != "medium-high" or review.get("review_status") != "reviewed_relay_candidate"):
            raise SystemExit(f"review lineage mismatch: {evidence_id}")
        if reuse.get(reuse_key) is None or reuse[reuse_key].get("evidence_ids") != evidence_id:
            raise SystemExit(f"reuse lineage mismatch: {evidence_id}")
        coverage = next((item for item in pair_rows if item.get("module21a_evidence_ids") == evidence_id), None)
        if coverage is None or coverage.get("pair_key") != pair_key or coverage.get("module21a_status") != "reviewed_relay_candidate":
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
        reuse[packet[1]]["validation_status"] = "promoted_high_batch043"
        reuse[packet[1]]["limitations"] = append_once(reuse[packet[1]]["limitations"], PROMOTION_NOTE)
        coverage = next(item for item in pair_rows if item.get("module21a_evidence_ids") == evidence_id)
        coverage["curator_notes"] = append_once(coverage["curator_notes"], PROMOTION_NOTE)
    write_tsv(DETAIL, detail_fields, detail_rows)
    write_tsv(REVIEW, review_fields, review_rows)
    write_tsv(REUSE, reuse_fields, reuse_rows)
    write_tsv(PAIRS, pair_fields, pair_rows)
    write_tsv(AUDIT, audit_fields, audit_rows)
    SUMMARY.write_text(json.dumps({"promotion_id": "module21a-relay-function-batch043-2026-09-02", "records_promoted": len(audit_rows), "evidence_ids": sorted(PACKET), "promotion_note": PROMOTION_NOTE, "upstream_module20a_lr_confidence_changed": False, "terminal_tf_assignments_created": False, "sql_signaling_edges_created": False, "malformed_legacy_rows_touched": False}, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"validated": len(audit_rows), "applied": len(audit_rows), "evidence_ids": sorted(PACKET)}, indent=2))


if __name__ == "__main__":
    main()
