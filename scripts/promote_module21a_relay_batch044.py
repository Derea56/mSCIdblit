#!/usr/bin/env python3
"""Promote thirteen bounded Module 21A R-spondin and semaphorin packets."""

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
REVIEW_FILES = [RELAY / "module21a_pair_relay_review_batches226_227.tsv", RELAY / "module21a_pair_relay_review_batches229.tsv"]
AUDIT = RELAY / "module21a_relay_promotion_batch044.tsv"
SUMMARY = RELAY / "module21a_relay_promotion_batch044_summary.json"

PACKET = {
    "M21A-PAIR-EVID-5560": ("rspo1 lrp6", "M21A-REUSE-2675", "M20A-EXT-2956", "PMID:18400942;PMCID:PMC2397303;DOI:10.1091/mbc.e08-02-0187;PMID:21693646;https://pubmed.ncbi.nlm.nih.gov/18400942/", "RSPO1-LRP6 receptor-proximal WNT-complex relay/function supports qualified-high promotion; preserve HSPG/LGR dependence and do not imply LRP6 is the sole RSPO1 receptor."),
    "M21A-PAIR-EVID-5561": ("rspo1 rnf43", "M21A-REUSE-2676", "M20A-EXT-2957", "PMID:24225776;PMCID:PMC3905715;PMID:24532711;https://pubmed.ncbi.nlm.nih.gov/24225776/", "Exact RSPO1-RNF43/LGR-FZD-LRP E3-ligase complex relay/function supports qualified-high promotion; preserve variable LGR/FZD/LRP composition and non-kinase topology."),
    "M21A-PAIR-EVID-5562": ("rspo1 znrf3", "M21A-REUSE-2677", "M20A-EXT-2958", "PMID:24349440;PMID:24225776;PMCID:PMC3905715;PMID:24532711;https://pubmed.ncbi.nlm.nih.gov/24349440/", "Exact RSPO1-ZNRF3/LGR-FZD-LRP receptor-complex relay/function supports qualified-high promotion; preserve ZNRF3 ectodomain structural and stoichiometric limits."),
    "M21A-PAIR-EVID-5563": ("rspo2 lgr4", "M21A-REUSE-2678", "M20A-EXT-2959", "PMID:21909076;PMID:21693646;PMID:24225776;PMID:29405118;https://pubmed.ncbi.nlm.nih.gov/21909076/", "Exact RSPO2-LGR4 WNT-complex relay/function supports qualified-high promotion; preserve HSPG/LGR-independent branches and reporter-as-pathway-output semantics."),
    "M21A-PAIR-EVID-5564": ("rspo2 lgr5", "M21A-REUSE-2679", "M20A-EXT-2960", "PMID:21693646;PMID:21909076;PMID:24225776;PMID:29405118;https://pubmed.ncbi.nlm.nih.gov/21693646/", "Exact RSPO2-LGR5/RNF43-ZNRF3/FZD-LRP relay/function supports qualified-high promotion; preserve engineered-system strength and LGR-independent HSPG signaling."),
    "M21A-PAIR-EVID-5566": ("rspo2 rnf43", "M21A-REUSE-2680", "M20A-EXT-2962", "PMID:24225776;PMID:29405118;PMCID:PMC5800842;https://pubmed.ncbi.nlm.nih.gov/24225776/", "Exact RSPO2-RNF43 E3-ligase neutralization and WNT receptor-preservation relay/function support qualified-high promotion; preserve species/cell and LGR-independent HSPG differences."),
    "M21A-PAIR-EVID-5567": ("rspo2 znrf3", "M21A-REUSE-2681", "M20A-EXT-2963", "PMID:24225776;PMID:29405118;PMID:39753551;https://pubmed.ncbi.nlm.nih.gov/24225776/", "Exact RSPO2-ZNRF3 receptor-complex relay/function supports qualified-high promotion; preserve membrane E3-regulator and HSPG/LGR-independent branch boundaries."),
    "M21A-PAIR-EVID-5568": ("rspo3 lgr4", "M21A-REUSE-2682", "M20A-EXT-2964", "PMID:21909076;PMID:21727895;PMID:29405118;PMID:32926477;https://pubmed.ncbi.nlm.nih.gov/21909076/", "Exact RSPO3-LGR4 WNT-complex relay/function supports qualified-high promotion; preserve HSPG-independent and SDC4/PCP branches and reporter limits."),
    "M21A-PAIR-EVID-5569": ("rspo3 lgr5", "M21A-REUSE-2683", "M20A-EXT-2965", "PMID:21909076;PMID:21727895;PMID:29405118;PMID:31235935;DOI:10.1038/s41556-019-0339-9;https://pubmed.ncbi.nlm.nih.gov/21909076/", "Exact RSPO3-LGR5/RNF43-ZNRF3/FZD-LRP relay/function supports qualified-high promotion; preserve tissue versus engineered evidence and LGR-independent branches."),
    "M21A-PAIR-EVID-5571": ("rspo3 rnf43", "M21A-REUSE-2684", "M20A-EXT-2968", "PMID:29405118;PMCID:PMC5800842;PMID:24225776;https://pubmed.ncbi.nlm.nih.gov/29405118/", "RSPO3 FU1/RNF43-module-dependent WNT function supports qualified-high function-only promotion; do not upgrade to direct purified binary RSPO3-RNF43 binding."),
    "M21A-PAIR-EVID-5572": ("rspo3 sdc4", "M21A-REUSE-2685", "M20A-EXT-2969", "PMID:21397842;PMID:24275095;DOI:10.1016/j.devcel.2011.01.006;https://pubmed.ncbi.nlm.nih.gov/21397842/", "Exact noncanonical RSPO3-SDC4 PCP receptor-complex relay/function supports qualified-high promotion; preserve SDC4 proteoglycan identity and separation from canonical LGR/RNF43/ZNRF3 WNT."),
    "M21A-PAIR-EVID-5573": ("sema3f nrp2_plxna3", "M21A-REUSE-2686", "M20A-EXT-3074", "PMID:20010807; PMID:29154130; PMID:37010951", "Exact NRP2/PLXNA3 holoreceptor-dependent SEMA3F neuronal downstream function supports qualified-high function-only promotion; no purified binary PLXNA3 binding or unique kinase relay is claimed."),
    "M21A-PAIR-EVID-5574": ("sema3g nrp2_plxna1", "M21A-REUSE-2687", "M20A-EXT-3078", "PMID:36720439; PMID:40533501", "Exact NRP2/PLXNA1 SEMA3G receptor-complex relay/function supports qualified-high promotion; preserve vascular and tumor contexts and YAP/MYC as context-specific outputs."),
}

FUNCTION_ONLY = {"M21A-PAIR-EVID-5571", "M21A-PAIR-EVID-5573"}
PROMOTION_NOTE = "Module 21A relay/function promotion batch044 (2026-09-02): evidence tier raised to high for the exact, context-bounded packet; evidence-layer scope, upstream Module 20A LR confidence, terminal-TF status, and SCI transfer remain unchanged."


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
        reuse[packet[1]]["validation_status"] = "promoted_high_batch044"
        reuse[packet[1]]["limitations"] = append_once(reuse[packet[1]]["limitations"], PROMOTION_NOTE)
        coverage = next(item for item in pair_rows if item.get("module21a_evidence_ids") == evidence_id)
        coverage["curator_notes"] = append_once(coverage["curator_notes"], PROMOTION_NOTE)
    write_tsv(DETAIL, detail_fields, detail_rows)
    for path, fields, rows in zip(REVIEW_FILES, review_fields, review_rows_by_file):
        write_tsv(path, fields, rows)
    write_tsv(REUSE, reuse_fields, reuse_rows)
    write_tsv(PAIRS, pair_fields, pair_rows)
    write_tsv(AUDIT, audit_fields, audit_rows)
    SUMMARY.write_text(json.dumps({"promotion_id": "module21a-relay-function-batch044-2026-09-02", "records_promoted": len(audit_rows), "evidence_ids": sorted(PACKET), "promotion_note": PROMOTION_NOTE, "upstream_module20a_lr_confidence_changed": False, "terminal_tf_assignments_created": False, "sql_signaling_edges_created": False, "malformed_legacy_rows_touched": False}, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"validated": len(audit_rows), "applied": len(audit_rows), "evidence_ids": sorted(PACKET)}, indent=2))


if __name__ == "__main__":
    main()
