#!/usr/bin/env python3
"""Promote eleven bounded Module 21A neuropeptide, natriuretic, and ERBB packets."""

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
REVIEW_FILES = [RELAY / "module21a_pair_relay_review_batches222_223.tsv", RELAY / "module21a_pair_relay_review_batches224_225.tsv"]
AUDIT = RELAY / "module21a_relay_promotion_batch039.tsv"
SUMMARY = RELAY / "module21a_relay_promotion_batch039_summary.json"

PACKET = {
    "M21A-PAIR-EVID-5460": ("npff npffr2", "M21A-REUSE-2589", "M20A-EXT-2569", "PMID:23911743;PMID:28581443;PMID:35691527", "Exact NPFF/NPFFR2 GPCR Gi/o-cAMP relay and neuroimmune/metabolic/stress function support qualified-high promotion; preserve RF-amide cross-reactivity and distributed in-vivo circuit context."),
    "M21A-PAIR-EVID-5461": ("nppa npr1", "M21A-REUSE-2590", "M20A-EXT-2570", "PMCID:PMC3879815;PMID:29934640;PMCID:PMC6298697", "Exact ANP/NPR1 particulate-guanylyl-cyclase cGMP/PKG relay and cardiomyocyte function support qualified-high promotion; preserve spatial compartmentalization and other NP-receptor engagement at high concentration."),
    "M21A-PAIR-EVID-5463": ("nps npsr1", "M21A-REUSE-2592", "M20A-EXT-2581", "PMID:26865629;PMCID:PMC4340626;PMCID:PMC3142248", "Exact NPS/NPSR1 dual Gs/Gq cAMP-calcium/ERK relay and neuronal function support qualified-high promotion; CRE reporter is pathway output, not TF occupancy, and isoform/analog bias remains."),
    "M21A-PAIR-EVID-5466": ("npvf npffr1", "M21A-REUSE-2595", "M20A-EXT-2589", "PMID:23911743;PMID:19682524;PMID:34534716", "Exact NPVF/NPFFR1 Gi/o-cAMP and neuroendocrine/reproductive/nociceptive function support qualified-high promotion; preserve high-affinity RF-amide cross-reactivity and non-exclusive in-vivo phenotypes."),
    "M21A-PAIR-EVID-5468": ("npw npbwr1", "M21A-REUSE-2597", "M20A-EXT-2594", "PMID:12401809;PMCID:PMC156358;PMID:12810535;PMID:15797961", "Exact NPW/NPBWR1 Gi/o-cAMP and context-dependent PLC-calcium/endocrine function support qualified-high promotion; preserve species and NPBWR2-expression boundaries."),
    "M21A-PAIR-EVID-5469": ("npy npy1r", "M21A-REUSE-2598", "M20A-EXT-2605", "PMID:18641693;PMID:15470140;PMID:38882210", "Exact NPY/NPY1R Gi/o, calcium/ERK, and cellular function support qualified-high promotion; preserve model/concentration dependence and engineered-analog limits."),
    "M21A-PAIR-EVID-5471": ("npy npy5r", "M21A-REUSE-2600", "M20A-EXT-2607", "PMID:10660688;PMID:18641693;PMID:30503694", "NPY/NPY5R Gi/o/PKC-MEK-ERK and growth-function evidence supports qualified-high promotion; preserve Y1R/Y2R cross-talk and the alpha-adrenergic potentiation context."),
    "M21A-PAIR-EVID-5472": ("nrg2 erbb2_erbb3", "M21A-REUSE-2601", "M20A-EXT-2610", "PMID:12466964;PMCID:PMC109195;PMCID:PMC2590688;https://reactome.org/content/detail/R-HSA-1227986", "NRG2 ligand binding through ERBB3 with ERBB2 kinase-partner ERK/PI3K-AKT relay and function support qualified-high promotion; preserve NRG2alpha/beta specificity and composite stoichiometry, not direct NRG2-ERBB2 binding."),
    "M21A-PAIR-EVID-5473": ("nrg2 erbb2_erbb4", "M21A-REUSE-2602", "M20A-EXT-2611", "PMID:12466964;PMCID:PMC109195;PMID:16338790;PMID:17945187;https://reactome.org/content/detail/R-HSA-1227986", "NRG2 ligand binding through ERBB4 with ERBB2 kinase-partner ERK/PI3K-AKT relay and function support qualified-high promotion; preserve NRG2alpha/beta boundary and composite-receptor semantics."),
    "M21A-PAIR-EVID-5474": ("nrxn1 nlgn1", "M21A-REUSE-2603", "M20A-EXT-2622", "PMCID:PMC2119998;PMCID:PMC2771087;DOI:10.1016/S0969212611001353", "Exact calcium-/splice-dependent NRXN1/NLGN1 trans-synaptic adhesion and excitatory synapse function support qualified-high function-only promotion; preserve alpha/beta promoter, splice, and multicomponent scaffold context."),
    "M21A-PAIR-EVID-5475": ("nrxn1 nlgn2", "M21A-REUSE-2604", "M20A-EXT-2623", "PMID:18334217;PMID:18084303;PMCID:PMC2922956", "Exact NRXN1beta/NLGN2 calcium-dependent trans-synaptic adhesion and inhibitory synapse function support qualified-high function-only promotion; preserve NRXN1 SS4 and neuroligin isoform context."),
}

FUNCTION_ONLY = {"M21A-PAIR-EVID-5474", "M21A-PAIR-EVID-5475"}
PROMOTION_NOTE = "Module 21A relay/function promotion batch039 (2026-09-02): evidence tier raised to high for the exact, context-bounded packet; evidence-layer scope, upstream Module 20A LR confidence, terminal-TF status, and SCI transfer remain unchanged."


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
        reuse[packet[1]]["validation_status"] = "promoted_high_batch039"
        reuse[packet[1]]["limitations"] = append_once(reuse[packet[1]]["limitations"], PROMOTION_NOTE)
        coverage = next(item for item in pair_rows if item.get("module21a_evidence_ids") == evidence_id)
        coverage["curator_notes"] = append_once(coverage["curator_notes"], PROMOTION_NOTE)
    write_tsv(DETAIL, detail_fields, detail_rows)
    for path, fields, rows in zip(REVIEW_FILES, review_fields, review_rows_by_file):
        write_tsv(path, fields, rows)
    write_tsv(REUSE, reuse_fields, reuse_rows)
    write_tsv(PAIRS, pair_fields, pair_rows)
    write_tsv(AUDIT, audit_fields, audit_rows)
    SUMMARY.write_text(json.dumps({"promotion_id": "module21a-relay-function-batch039-2026-09-02", "records_promoted": len(audit_rows), "evidence_ids": sorted(PACKET), "promotion_note": PROMOTION_NOTE, "upstream_module20a_lr_confidence_changed": False, "terminal_tf_assignments_created": False, "sql_signaling_edges_created": False, "malformed_legacy_rows_touched": False}, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"validated": len(audit_rows), "applied": len(audit_rows), "evidence_ids": sorted(PACKET)}, indent=2))


if __name__ == "__main__":
    main()
