#!/usr/bin/env python3
"""Promote twelve bounded Module 21A TGM2, THBS1, SHH, SLIT, SLPI, SLURP1, SNCA, and SOST packets."""

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
    RELAY / "module21a_pair_relay_review_batches230.tsv",
    RELAY / "module21a_pair_relay_review_batches231.tsv",
]
AUDIT = RELAY / "module21a_relay_promotion_batch048.tsv"
SUMMARY = RELAY / "module21a_relay_promotion_batch048_summary.json"

PACKET = {
    "M21A-PAIR-EVID-5643": ("tgm2 sdc4", "M21A-REUSE-2737", "M20A-EXT-3280", "PMID:19398782; PMID:22442151; PMID:20929862; PMCID:PMC3001003", "Exact HS/SDC4 proteoglycan coreceptor plus TG2-FN matrix presentation relay/function supports qualified-high promotion; preserve PKCalpha/beta1 co-signaling and matrix context and do not call SDC4 a kinase receptor."),
    "M21A-PAIR-EVID-5644": ("thbs1 itga2b_itgb3", "M21A-REUSE-2738", "M20A-EXT-3283", "PMID:9169439; DOI:10.1074/jbc.272.23.14740; PMID:8550562; DOI:10.1074/jbc.271.1.21", "Exact TSP1 C-terminal/CD47-IAP/alphaIIbbeta3 platelet activation function supports qualified-high promotion; preserve the CD47 bridge and platelet context and do not claim direct binary THBS1-integrin binding."),
    "M21A-PAIR-EVID-5645": ("thbs1 itga4", "M21A-REUSE-2739", "M20A-EXT-3284", "PMID:11980922; PMCID:PMC2173289; DOI:10.1083/jcb.200109098", "Exact activated THBS1-alpha4beta1 matrix relay/function supports qualified-high promotion; preserve the complete alpha4beta1 complex, activation state, and matrix boundaries."),
    "M21A-PAIR-EVID-5648": ("shh scube2", "M21A-REUSE-2741", "M20A-EXT-3144", "PMID:19480626; PMID:33038332; DOI:10.1042/BJ20090341", "Exact lipidated SHH-SCUBE2 chaperone/release and receptor-proximal handoff supports qualified-high promotion; preserve CDON/BOC/GAS1-PTCH1 topology and treat GLI1 as a measured provisional endpoint."),
    "M21A-PAIR-EVID-5649": ("slit1 robo2", "M21A-REUSE-2742", "M20A-EXT-3149", "PMID:18278043; PMID:19934013; PMID:17715346; DOI:10.1038/nn2051", "Exact SLIT1-ROBO2 receptor-dependent adhesion/axon-guidance function supports qualified-high promotion; preserve N-cadherin/cytoskeletal and developmental context and do not infer a universal ROBO2 adaptor-to-TF branch."),
    "M21A-PAIR-EVID-5650": ("slit3 robo1", "M21A-REUSE-2743", "M20A-EXT-3157", "PMID:23255421", "Exact SLIT3-ROBO1 developmental migration/adhesion/survival function supports qualified-high promotion; preserve mouse cardiac neural-crest/systemic-venous-return context and unresolved intracellular relay."),
    "M21A-PAIR-EVID-5652": ("slit3 robo4", "M21A-REUSE-2745", "M20A-EXT-3159", "PMID:24355925; PMID:24090675; PMID:35288626", "Exact HS-SLIT3-ROBO4 endothelial receptor-complex relay/function supports qualified-high promotion; preserve HS presentation, endothelial context, and unresolved ROBO4 cytoplasmic relay."),
    "M21A-PAIR-EVID-5653": ("slpi plscr1", "M21A-REUSE-2746", "M20A-EXT-3164", "PMID:19333378; PMCID:PMC2659420; DOI:10.1371/journal.pone.0005006", "Exact membrane SLPI-PLSCR1/CD4 complex antiviral function supports qualified-high promotion; preserve human T-cell/monocyte context and do not convert antiviral activity into a generic kinase cascade."),
    "M21A-PAIR-EVID-5654": ("slpi plscr4", "M21A-REUSE-2747", "M20A-EXT-3165", "PMID:19333378; PMCID:PMC2659420; DOI:10.1371/journal.pone.0005006", "Exact membrane SLPI-PLSCR4/CD4 complex antiviral function supports qualified-high promotion; preserve shared-complex semantics and do not infer a distinct PLSCR4 cytosolic branch or TF."),
    "M21A-PAIR-EVID-5655": ("slurp1 chrna7", "M21A-REUSE-2748", "M20A-EXT-3169", "PMID:29545933; PMCID:PMC5837762; DOI:10.18632/oncotarget.24312; PMID:34595181; PMCID:PMC8476798; DOI:10.3389/fcell.2021.739391; PMID:24365495; DOI:10.1016/j.jneuroim.2013.12.003", "Exact modulatory SLURP1-CHRNA7 receptor-complex relay/function supports qualified-high promotion; preserve inhibitory versus modulatory direction and context-specific PDGFR/EGFR/NF-kappaB branches."),
    "M21A-PAIR-EVID-5656": ("snca lag3", "M21A-REUSE-2749", "M20A-EXT-3173", "PMID:27708076; PMID:34172566", "Exact pathogenic alpha-synuclein PFF-LAG3 binding/uptake and neuron-to-neuron toxicity function supports qualified-high promotion; preserve PFF conformers and do not transfer to monomeric SNCA or infer a canonical LAG3 relay."),
    "M21A-PAIR-EVID-5657": ("sost lrp4", "M21A-REUSE-2750", "M20A-EXT-3178", "PMID:35099616; PMID:22696217", "Exact extracellular SOST-LRP4 anchor/coreceptor-to-LRP5/6 WNT inhibition function supports qualified-high promotion; preserve LRP4 organizing topology and treat TCF/LEF as reporter output rather than a pair-specific TF."),
}

FUNCTION_ONLY = {"M21A-PAIR-EVID-5644", "M21A-PAIR-EVID-5653", "M21A-PAIR-EVID-5654", "M21A-PAIR-EVID-5656"}
PROMOTION_NOTE = "Module 21A relay/function promotion batch048 (2026-09-02): evidence tier raised to high for the exact, context-bounded packet; evidence-layer scope, upstream Module 20A LR confidence, terminal-TF status, and SCI transfer remain unchanged."


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
        reuse[packet[1]]["validation_status"] = "promoted_high_batch048"
        reuse[packet[1]]["limitations"] = append_once(reuse[packet[1]]["limitations"], PROMOTION_NOTE)
        coverage = next(item for item in pair_rows if item.get("module21a_evidence_ids") == evidence_id)
        coverage["curator_notes"] = append_once(coverage["curator_notes"], PROMOTION_NOTE)

    write_tsv(DETAIL, detail_fields, detail_rows)
    for path, fields, rows in zip(REVIEW_FILES, review_fields, review_rows_by_file):
        write_tsv(path, fields, rows)
    write_tsv(REUSE, reuse_fields, reuse_rows)
    write_tsv(PAIRS, pair_fields, pair_rows)
    write_tsv(AUDIT, audit_fields, audit_rows)
    SUMMARY.write_text(json.dumps({"promotion_id": "module21a-relay-function-batch048-2026-09-02", "records_promoted": len(audit_rows), "evidence_ids": sorted(PACKET), "promotion_note": PROMOTION_NOTE, "upstream_module20a_lr_confidence_changed": False, "terminal_tf_assignments_created": False, "sql_signaling_edges_created": False, "malformed_legacy_rows_touched": False}, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"validated": len(audit_rows), "applied": len(audit_rows), "evidence_ids": sorted(PACKET)}, indent=2))


if __name__ == "__main__":
    main()
