#!/usr/bin/env python3
"""Promote six bounded Module 21A semaphorin and TGF-beta packets."""

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
    RELAY / "module21a_pair_relay_review_batches231.tsv",
]
AUDIT = RELAY / "module21a_relay_promotion_batch047.tsv"
SUMMARY = RELAY / "module21a_relay_promotion_batch047_summary.json"

PACKET = {
    "M21A-PAIR-EVID-5621": ("sema3f nrp2_plxna1", "M21A-REUSE-2726", "M20A-EXT-3072", "PMID:18660502; PMID:26319580; PMCID:PMC4582121", "Exact Sema3F-NRP2/PLXNA1 complex relay/function supports qualified-high promotion; preserve NRP2 ligand binding, PLXNA1 transduction, heterologous stoichiometry, and PlexinA3 boundaries."),
    "M21A-PAIR-EVID-5626": ("tgfb1 itgb5", "M21A-REUSE-2727", "M20A-EXT-3254", "PMID:18086923; PMCID:PMC4030512; PMCID:PMC2140013", "Exact latent TGFB1-LAP/alphaVbeta5 traction-to-active-TGFB1 function supports qualified-high promotion; preserve the alphaVbeta5 heterodimer, latent ligand, mechanical matrix context, and no beta5-only relay or TF claim."),
    "M21A-PAIR-EVID-5628": ("tgfb1 sdc2", "M21A-REUSE-2729", "M20A-EXT-3257", "PMID:14976204; DOI:10.1074/jbc.C300430200; PMID:23924348; PMCID:PMC3826270", "Exact TGFB1-SDC2 accessory proteoglycan binding/uptake-to-TGFBR trafficking relay/function supports qualified-high promotion; preserve ectodomain/heparan-sulfate and cell-type context and do not call SDC2 a kinase receptor."),
    "M21A-PAIR-EVID-5631": ("tgfb1 vasn", "M21A-REUSE-2731", "M20A-EXT-3260", "PMID:15247411; PMID:30252131", "Exact inhibitory TGFB1-VASN decoy/sequestration function supports qualified-high promotion; preserve VASN non-signaling topology, vascular context, and limited mouse pair evidence."),
    "M21A-PAIR-EVID-5635": ("tgfb3 acvrl1", "M21A-REUSE-2733", "M20A-EXT-3268", "PMID:10187774; DOI:10.1074/jbc.274.15.9984; PMID:14580334; DOI:10.1016/S1097-2765(03)00386-1", "Exact endothelial TGFB3-ACVRL1/ALK1-containing complex relay/function supports qualified-high promotion; preserve TGFBR2, ALK5/TGFBR1, and endoglin context and do not promote ACVRL1 standalone."),
    "M21A-PAIR-EVID-5637": ("tgfb3 itgb6", "M21A-REUSE-2734", "M20A-EXT-3273", "PMID:11821050; DOI:10.1016/S0014-5793(01)03280-X; PMID:12358597", "Exact latent TGFB3-LAP/alphaVbeta6 activation-to-released-TGFB3 function supports qualified-high promotion; preserve the alphaVbeta6 heterodimer, latent ligand, and no beta6-only or TF claim."),
}

FUNCTION_ONLY = {"M21A-PAIR-EVID-5626", "M21A-PAIR-EVID-5631", "M21A-PAIR-EVID-5637"}
PROMOTION_NOTE = "Module 21A relay/function promotion batch047 (2026-09-02): evidence tier raised to high for the exact, context-bounded packet; evidence-layer scope, upstream Module 20A LR confidence, terminal-TF status, and SCI transfer remain unchanged."


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
        reuse[packet[1]]["validation_status"] = "promoted_high_batch047"
        reuse[packet[1]]["limitations"] = append_once(reuse[packet[1]]["limitations"], PROMOTION_NOTE)
        coverage = next(item for item in pair_rows if item.get("module21a_evidence_ids") == evidence_id)
        coverage["curator_notes"] = append_once(coverage["curator_notes"], PROMOTION_NOTE)

    write_tsv(DETAIL, detail_fields, detail_rows)
    for path, fields, rows in zip(REVIEW_FILES, review_fields, review_rows_by_file):
        write_tsv(path, fields, rows)
    write_tsv(REUSE, reuse_fields, reuse_rows)
    write_tsv(PAIRS, pair_fields, pair_rows)
    write_tsv(AUDIT, audit_fields, audit_rows)
    SUMMARY.write_text(json.dumps({"promotion_id": "module21a-relay-function-batch047-2026-09-02", "records_promoted": len(audit_rows), "evidence_ids": sorted(PACKET), "promotion_note": PROMOTION_NOTE, "upstream_module20a_lr_confidence_changed": False, "terminal_tf_assignments_created": False, "sql_signaling_edges_created": False, "malformed_legacy_rows_touched": False}, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"validated": len(audit_rows), "applied": len(audit_rows), "evidence_ids": sorted(PACKET)}, indent=2))


if __name__ == "__main__":
    main()
