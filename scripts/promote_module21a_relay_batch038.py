#!/usr/bin/env python3
"""Promote fourteen bounded Module 21A synaptic, peptide, and Nodal packets."""

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
REVIEW = RELAY / "module21a_pair_relay_review_batches222_223.tsv"
AUDIT = RELAY / "module21a_relay_promotion_batch038.tsv"
SUMMARY = RELAY / "module21a_relay_promotion_batch038_summary.json"

PACKET = {
    "M21A-PAIR-EVID-5441": ("ncan sdc3", "M21A-REUSE-2572", "M20A-EXT-2521", "PMID:15198637;PMCID:PMC1134051", "HSPG-dependent NCAN/SDC3 binding and cerebellar neurite-outgrowth function support qualified-high function-only promotion; preserve neurocan fragment and HS/CS chain context, with no defined SDC3 cytosolic relay."),
    "M21A-PAIR-EVID-5442": ("ndp lgr4", "M21A-REUSE-2573", "M20A-EXT-2522", "PMCID:PMC3666258;PMID:23891289", "Direct Norrin/LGR4 binding and activation with FZD/LRP5/6 cooperation and Wnt reporter output support qualified-high promotion; TOPFLASH is pathway output, not direct TF occupancy."),
    "M21A-PAIR-EVID-5446": ("nlgn1 nrxn1", "M21A-REUSE-2575", "M20A-EXT-2537", "PMCID:PMC2119998;PMCID:PMC2771087;DOI:10.1016/S0969212611001353", "Direct NLGN1/NRXN1 trans-synaptic adhesion with synapse and electrophysiology function supports qualified-high function-only promotion; preserve splice, calcium, and multicomponent scaffold context."),
    "M21A-PAIR-EVID-5447": ("nlgn1 nrxn2", "M21A-REUSE-2576", "M20A-EXT-2538", "PMCID:PMC3243752;PMCID:PMC2771087", "NLGN1/NRXN2beta complex-resolved adhesion and GABAergic synapse organization support qualified-high function-only promotion; preserve NRXN2beta and tripartite receptor context."),
    "M21A-PAIR-EVID-5448": ("nlgn2 nrxn1", "M21A-REUSE-2577", "M20A-EXT-2539", "PMID:18334217;PMID:18084303;PMCID:PMC2922956", "Calcium-dependent NLGN2/NRXN1beta trans-synaptic adhesion and inhibitory synapse organization support qualified-high function-only promotion; preserve NRXN1 splice-site-4 and NLGN2 isoform specificity."),
    "M21A-PAIR-EVID-5449": ("nlgn3 nrxn1", "M21A-REUSE-2578", "M20A-EXT-2541", "PMID:18084303;PMID:18334217;PMID:33758193", "Exact NLGN3/NRXN1beta adhesion and synapse differentiation function support qualified-high function-only promotion; preserve splice/isoform dependence and competing PTPdelta-NLGN3 interaction."),
    "M21A-PAIR-EVID-5450": ("nmb nmbr", "M21A-REUSE-2579", "M20A-EXT-2545", "PMID:9555086;PMCID:PMC8490515;PMID:41257985", "Exact NMB/NMBR GPCR activation with Gq/PLC-calcium and context-dependent neuronal/secretory outputs support qualified-high promotion; preserve PLC/PLD and Gbeta-gamma branch distinctions."),
    "M21A-PAIR-EVID-5452": ("nms nmur2", "M21A-REUSE-2581", "M20A-EXT-2550", "PMID:18214396;PMID:27512149;PMID:15331768", "NMS stimulation, NMUR2 knockdown, calcium/Akt/ERK, and myometrial contractile function support qualified-high promotion; preserve pregnancy-associated/inflammatory myometrium context."),
    "M21A-PAIR-EVID-5453": ("nmu nmur1", "M21A-REUSE-2582", "M20A-EXT-2554", "PMID:10894543;PMID:15331768;PMID:20599609;PMID:28869974", "Exact NMU/NMUR1 GPCR activation and Gq/11/Gi, PI3K/PKCepsilon/ERK/calcium functions support qualified-high promotion; preserve neuronal, ILC2, and smooth-muscle branch boundaries."),
    "M21A-PAIR-EVID-5454": ("nmu nmur2", "M21A-REUSE-2583", "M20A-EXT-2555", "PMID:10894543;PMID:11010960;PMID:15331768;PMID:27512149", "Exact NMU/NMUR2 coupling and contractile/neuroendocrine function support qualified-high promotion; preserve recombinant-receptor versus tissue-model differences."),
    "M21A-PAIR-EVID-5455": ("nodal acvr1b_acvr2a", "M21A-REUSE-2584", "M20A-EXT-2556", "PMID:11389842;PMID:18089557;PMCID:PMC154321;https://doi.org/10.1046/j.1365-2443.2002.00528.x", "Nodal/Cripto-dependent ACVR1B/ACVR2A assembly, rescue, and SMAD2/3 developmental function support qualified-high promotion; preserve composite coreceptor and ACVR2A/B redundancy."),
    "M21A-PAIR-EVID-5456": ("nodal acvr1b_acvr2b", "M21A-REUSE-2585", "M20A-EXT-2558", "PMID:11389842;PMID:18089557;PMID:25603319;PMCID:PMC4300205", "Nodal/Cripto-dependent ACVR1B/ACVR2B binding/reconstitution and SMAD2/3 assays support qualified-high promotion; preserve BMPRII/weaker ACTRIIB and ACVR2A/B redundancy, not ACVR2B exclusivity."),
    "M21A-PAIR-EVID-5458": ("npb npbwr1", "M21A-REUSE-2587", "M20A-EXT-2567", "PMID:12401809;PMCID:PMC156358;PMID:15797961", "Exact NPB/NPBWR1 GPCR binding/activation with Gi/o-cAMP, PLC/calcium, and secretory outputs support qualified-high promotion; NPBWR2 is an alternative where expressed."),
    "M21A-PAIR-EVID-5459": ("npff npffr1", "M21A-REUSE-2588", "M20A-EXT-2568", "PMID:23911743;PMCID:PMC4018085;PMID:19682524", "Exact NPFF/NPFFR1 binding/activation, Gi/o-cAMP, calcium, and nociceptive modulation support qualified-high promotion; preserve RF-amide cross-reactivity and heterologous/in-vivo circuit limits."),
}

FUNCTION_ONLY = {f"M21A-PAIR-EVID-{x}" for x in (5441, 5446, 5447, 5448, 5449)}
PROMOTION_NOTE = "Module 21A relay/function promotion batch038 (2026-09-02): evidence tier raised to high for the exact, context-bounded packet; evidence-layer scope, upstream Module 20A LR confidence, terminal-TF status, and SCI transfer remain unchanged."


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
    audit_rows = [{"evidence_id": eid, "review_id": packet[2], "pair_key": packet[0], "pathway_reuse_key": packet[1], "previous_tier": detail[eid]["confidence_tier"], "new_tier": "high", "source_locators": detail[eid]["source_locators"], "decision_basis": packet[4], "upstream_lr_confidence_unchanged": "true", "terminal_tf_status_unchanged": "true", "sql_materialization": "false"} for eid, packet in sorted(PACKET.items())]
    if not args.apply:
        print(json.dumps({"validated": len(audit_rows), "apply": False, "evidence_ids": sorted(PACKET)}, indent=2))
        return
    for evidence_id, packet in PACKET.items():
        detail[evidence_id]["confidence_tier"] = "high"
        detail[evidence_id]["limitations"] = append_once(detail[evidence_id]["limitations"], PROMOTION_NOTE)
        reviews[packet[2]]["confidence_tier"] = "high"
        reviews[packet[2]]["curator_note"] = append_once(reviews[packet[2]]["curator_note"], PROMOTION_NOTE)
        reuse[packet[1]]["validation_status"] = "promoted_high_batch038"
        reuse[packet[1]]["limitations"] = append_once(reuse[packet[1]]["limitations"], PROMOTION_NOTE)
        coverage = next(item for item in pair_rows if item.get("module21a_evidence_ids") == evidence_id)
        coverage["curator_notes"] = append_once(coverage["curator_notes"], PROMOTION_NOTE)
    write_tsv(DETAIL, detail_fields, detail_rows)
    write_tsv(REVIEW, review_fields, review_rows)
    write_tsv(REUSE, reuse_fields, reuse_rows)
    write_tsv(PAIRS, pair_fields, pair_rows)
    write_tsv(AUDIT, audit_fields, audit_rows)
    SUMMARY.write_text(json.dumps({"promotion_id": "module21a-relay-function-batch038-2026-09-02", "records_promoted": len(audit_rows), "evidence_ids": sorted(PACKET), "promotion_note": PROMOTION_NOTE, "upstream_module20a_lr_confidence_changed": False, "terminal_tf_assignments_created": False, "sql_signaling_edges_created": False, "malformed_legacy_rows_touched": False}, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"validated": len(audit_rows), "applied": len(audit_rows), "evidence_ids": sorted(PACKET)}, indent=2))


if __name__ == "__main__":
    main()
