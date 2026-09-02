#!/usr/bin/env python3
"""Promote fifteen bounded Module 21A semaphorin, SHH, and RSPO packets."""

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
    RELAY / "module21a_pair_relay_review_batches228.tsv",
    RELAY / "module21a_pair_relay_review_batches229.tsv",
]
AUDIT = RELAY / "module21a_relay_promotion_batch045.tsv"
SUMMARY = RELAY / "module21a_relay_promotion_batch045_summary.json"

PACKET = {
    "M21A-PAIR-EVID-5580": ("sema4d plxnb2", "M21A-REUSE-2692", "M20A-EXT-3092", "PMID:28416516; PMID:26275342; DOI:10.1136/annrheumdis-2016-210706", "Exact membrane SEMA4D-PLXNB2 contact/reverse-signaling function supports qualified-high promotion; preserve membrane-versus-soluble geometry and do not infer a canonical PLXNB2 adaptor, kinase, or terminal TF."),
    "M21A-PAIR-EVID-5582": ("sema5b plxna1", "M21A-REUSE-2694", "M20A-EXT-3097", "PMID:31209173; PMCID:PMC6697390; DOI:10.1523/JNEUROSCI.0113-19.2019", "Exact PLXNA1-dependent SEMA5B auditory branch-refinement function supports qualified-high promotion; preserve PLXNA3 co-expression and do not infer purified binary binding or a defined cytosolic relay."),
    "M21A-PAIR-EVID-5584": ("sema7a itga1_itgb1", "M21A-REUSE-2695", "M20A-EXT-3102", "PMID:17377534; PMID:12879062; PMCID:PMC5353663; DOI:10.1038/nature01790", "Exact SEMA7A-ITGA1/ITGB1 heterodimer relay/function supports qualified-high promotion; preserve the complete alpha1beta1 complex, membrane anchoring, and neural/immune context."),
    "M21A-PAIR-EVID-5585": ("sema7a plxnc1", "M21A-REUSE-2696", "M20A-EXT-3103", "PMID:17727705; PMID:20727575; PMID:31292439; PMCID:PMC6610950; DOI:10.1038/ncomms8835; DOI:10.1038/s41467-019-11055-6", "Exact SEMA7A-PLXNC1 cell-recognition and activity-dependent olfactory synapse function supports qualified-high promotion; retain the author-correction lineage and do not infer a PLXNC1 adaptor, kinase, or terminal TF."),
    "M21A-PAIR-EVID-5587": ("serpinf1 plxdc1", "M21A-REUSE-2697", "M20A-EXT-3117", "PMID:25535841; PMCID:PMC4303762; DOI:10.7554/eLife.05401", "Exact SERPINF1/PEDF-PLXDC1 receptor-oligomer and cytoplasmic-tail function supports qualified-high promotion; preserve atypical single-pass topology and cell-type-specific outputs."),
    "M21A-PAIR-EVID-5588": ("serpinf1 plxdc2", "M21A-REUSE-2698", "M20A-EXT-3118", "PMID:25535841; PMCID:PMC4303762; DOI:10.7554/eLife.05401", "Exact SERPINF1/PEDF-PLXDC2 binding, oligomer, and cytoplasmic-tail function supports qualified-high promotion; preserve PLXDC2-versus-PLXDC1 distinction and cell-type-specific outputs."),
    "M21A-PAIR-EVID-5589": ("sfrp2 fzd5", "M21A-REUSE-2699", "M20A-EXT-3124", "PMID:28840375; DOI:10.1016/j.cellsig.2017.06.004", "Exact endothelial SFRP2-FZD5 calcium/calcineurin/NFATC3 function supports qualified-high promotion; preserve endothelial and engineered-system boundaries and treat NFATC3 as a measured downstream endpoint."),
    "M21A-PAIR-EVID-5591": ("sftpd sirpa", "M21A-REUSE-2700", "M20A-EXT-3128", "PMID:18420961; DOI:10.1165/rcmb.2007-0452OC", "Exact SFTPD-SIRPA inhibitory receptor-proximal function supports qualified-high promotion; preserve collectin oligomerization/collagen-domain presentation and macrophage context."),
    "M21A-PAIR-EVID-5592": ("sftpd tlr4", "M21A-REUSE-2701", "M20A-EXT-3129", "PMID:16834340; PMID:35865531; PMCID:PMC9294227; DOI:10.1021/bi060176z; DOI:10.3389/fimmu.2022.913901", "Exact antagonistic SFTPD-TLR4/MD-2 complex modulation supports qualified-high promotion; preserve LPS/MD-2, oligomerization, and species/tissue context and do not call it productive TLR4 activation."),
    "M21A-PAIR-EVID-5593": ("shh boc", "M21A-REUSE-2702", "M20A-EXT-3135", "PMID:21115611; PMID:21664576; PMID:33038332; PMID:34057474; PMCID:PMC6514406", "Exact SHH-BOC coreceptor-dependent Hedgehog function supports qualified-high promotion; preserve positive/decoy context and combined GAS1/CDON/BOC boundaries."),
    "M21A-PAIR-EVID-5594": ("shh cdon", "M21A-REUSE-2703", "M20A-EXT-3136", "PMID:21802063; PMID:21664576; PMID:33038332; DOI:10.1016/j.ajhg.2011.07.001", "Exact SHH-CDON coreceptor/ligand-presenting pathway-competence function supports qualified-high promotion; preserve PTCH1-associated topology and do not infer a universal CDON-specific adaptor."),
    "M21A-PAIR-EVID-5595": ("shh gas1", "M21A-REUSE-2704", "M20A-EXT-3137", "PMID:11572986; PMID:21664576; PMID:33038332; DOI:10.1126/science.1064505", "Exact SHH-GAS1 availability/coreceptor modulation supports qualified-high promotion; preserve lipid/presentation/tissue-dependent antagonistic or promotive direction and do not infer a GAS1 intracellular relay."),
    "M21A-PAIR-EVID-5596": ("shh gpc1", "M21A-REUSE-2705", "M20A-EXT-3138", "PMID:23931997; DOI:10.1016/j.neuron.2013.05.025", "Exact SHH-GPC1 heparan-sulfate presentation and post-crossing guidance function supports qualified-high function-only promotion; preserve transcription-dependent versus independent branches and do not infer a cytosolic relay."),
    "M21A-PAIR-EVID-5597": ("shh hhip", "M21A-REUSE-2706", "M20A-EXT-3140", "PMID:34887403; PMID:40333979; DOI:10.1016/j.celrep.2021.109842", "Exact inhibitory SHH-HHIP sequestration/function supports qualified-high function-only promotion; preserve HHIP secreted-antagonist topology and separate direct binding/Gli1 inhibition from broader stromal effects."),
    "M21A-PAIR-EVID-5598": ("rspo3 znrf3", "M21A-REUSE-2707", "M20A-EXT-2970", "PMID:24225776; PMCID:PMC3905715; DOI:10.1038/ncomms3787; PMID:28467820", "Exact RSPO3-ZNRF3 E3-ligase receptor-complex relay/function supports qualified-high promotion; preserve ZNRF3 membrane-regulator topology and do not transfer RNF43 evidence or infer a kinase/TF edge."),
}

FUNCTION_ONLY = {
    "M21A-PAIR-EVID-5582",
    "M21A-PAIR-EVID-5585",
    "M21A-PAIR-EVID-5596",
    "M21A-PAIR-EVID-5597",
}

FUNCTION_ONLY_STATUS = {
    "M21A-PAIR-EVID-5582": {"reviewed_relay_candidate"},
    "M21A-PAIR-EVID-5585": {"reviewed_function_only"},
    "M21A-PAIR-EVID-5596": {"reviewed_function_only"},
    "M21A-PAIR-EVID-5597": {"reviewed_function_only"},
}

SOURCE_CORRECTIONS = {
    "M21A-PAIR-EVID-5580": (
        "DOI:10.1136/annrheumdis-2016-209676",
        "DOI:10.1136/annrheumdis-2016-210706",
    ),
    "M21A-PAIR-EVID-5594": (
        "DOI:10.1016/j.ajhg.2011.06.009",
        "DOI:10.1016/j.ajhg.2011.07.001",
    ),
}

PROMOTION_NOTE = "Module 21A relay/function promotion batch045 (2026-09-02): evidence tier raised to high for the exact, context-bounded packet; evidence-layer scope, upstream Module 20A LR confidence, terminal-TF status, and SCI transfer remain unchanged."
CORRECTION_NOTE = "Source DOI normalized to the PMID-resolved record before batch045 materialization; PMID remains the canonical locator."


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


def normalize_source(row):
    evidence_id = row.get("evidence_id", "")
    correction = SOURCE_CORRECTIONS.get(evidence_id)
    if correction is None:
        return
    old, new = correction
    value = row.get("source_locators", "")
    if old in value:
        row["source_locators"] = value.replace(old, new)
    elif new not in value:
        raise SystemExit(f"unresolved source DOI for {evidence_id}")


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

    for row in detail_rows:
        normalize_source(row)
    for row in review_rows:
        normalize_source(row)

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
        allowed_status = FUNCTION_ONLY_STATUS[evidence_id] if evidence_id in FUNCTION_ONLY else {"reviewed_relay_candidate"}
        if (review is None or review.get("evidence_id") != evidence_id or review.get("pair_key") != pair_key or review.get("source_locators") != citations or review.get("confidence_tier") not in {"medium", "medium-high"} or review.get("review_status") not in allowed_status):
            raise SystemExit(f"review lineage mismatch: {evidence_id}")
        if reuse.get(reuse_key) is None or reuse[reuse_key].get("evidence_ids") != evidence_id:
            raise SystemExit(f"reuse lineage mismatch: {evidence_id}")
        coverage = next((item for item in pair_rows if item.get("module21a_evidence_ids") == evidence_id), None)
        if coverage is None or coverage.get("pair_key") != pair_key or coverage.get("module21a_status") not in allowed_status:
            raise SystemExit(f"coverage lineage mismatch: {evidence_id}")

    audit_fields = ["evidence_id", "review_id", "pair_key", "pathway_reuse_key", "previous_tier", "new_tier", "source_locators", "decision_basis", "source_metadata_correction", "upstream_lr_confidence_unchanged", "terminal_tf_status_unchanged", "sql_materialization"]
    audit_rows = []
    for evidence_id, packet in sorted(PACKET.items()):
        audit_rows.append({
            "evidence_id": evidence_id,
            "review_id": packet[2],
            "pair_key": packet[0],
            "pathway_reuse_key": packet[1],
            "previous_tier": detail[evidence_id]["confidence_tier"],
            "new_tier": "high",
            "source_locators": detail[evidence_id]["source_locators"],
            "decision_basis": packet[4],
            "source_metadata_correction": CORRECTION_NOTE if evidence_id in SOURCE_CORRECTIONS else "none",
            "upstream_lr_confidence_unchanged": "true",
            "terminal_tf_status_unchanged": "true",
            "sql_materialization": "false",
        })

    if not args.apply:
        print(json.dumps({"validated": len(audit_rows), "apply": False, "source_corrections": sorted(SOURCE_CORRECTIONS), "evidence_ids": sorted(PACKET)}, indent=2))
        return

    for evidence_id, packet in PACKET.items():
        detail[evidence_id]["confidence_tier"] = "high"
        detail[evidence_id]["limitations"] = append_once(detail[evidence_id]["limitations"], PROMOTION_NOTE)
        if evidence_id in SOURCE_CORRECTIONS:
            detail[evidence_id]["limitations"] = append_once(detail[evidence_id]["limitations"], CORRECTION_NOTE)
        review = reviews[packet[2]]
        review["confidence_tier"] = "high"
        review["curator_note"] = append_once(review["curator_note"], PROMOTION_NOTE)
        if evidence_id in SOURCE_CORRECTIONS:
            review["curator_note"] = append_once(review["curator_note"], CORRECTION_NOTE)
        reuse[packet[1]]["validation_status"] = "promoted_high_batch045"
        reuse[packet[1]]["limitations"] = append_once(reuse[packet[1]]["limitations"], PROMOTION_NOTE)
        coverage = next(item for item in pair_rows if item.get("module21a_evidence_ids") == evidence_id)
        coverage["curator_notes"] = append_once(coverage["curator_notes"], PROMOTION_NOTE)

    write_tsv(DETAIL, detail_fields, detail_rows)
    for path, fields, rows in zip(REVIEW_FILES, review_fields, review_rows_by_file):
        write_tsv(path, fields, rows)
    write_tsv(REUSE, reuse_fields, reuse_rows)
    write_tsv(PAIRS, pair_fields, pair_rows)
    write_tsv(AUDIT, audit_fields, audit_rows)
    SUMMARY.write_text(json.dumps({
        "promotion_id": "module21a-relay-function-batch045-2026-09-02",
        "records_promoted": len(audit_rows),
        "evidence_ids": sorted(PACKET),
        "promotion_note": PROMOTION_NOTE,
        "source_metadata_corrections": sorted(SOURCE_CORRECTIONS),
        "upstream_module20a_lr_confidence_changed": False,
        "terminal_tf_assignments_created": False,
        "sql_signaling_edges_created": False,
        "malformed_legacy_rows_touched": False,
    }, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"validated": len(audit_rows), "applied": len(audit_rows), "source_corrections": sorted(SOURCE_CORRECTIONS), "evidence_ids": sorted(PACKET)}, indent=2))


if __name__ == "__main__":
    main()
