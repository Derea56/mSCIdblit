#!/usr/bin/env python3
"""Promote nine bounded Module 21A coreceptor and adhesion packets."""

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
REVIEW_FILES = [RELAY / "module21a_pair_relay_review_batches216_217.tsv", RELAY / "module21a_pair_relay_review_batches218_219.tsv"]
AUDIT = RELAY / "module21a_relay_promotion_batch032.tsv"
SUMMARY = RELAY / "module21a_relay_promotion_batch032_summary.json"

PACKET = {
    "M21A-PAIR-EVID-5320": ("hgf nrp1", "M21A-REUSE-2488", "M20A-EXT-2022", "PMID:18065694; PMID:17369861; PMID:21245381; DOI:10.1038/sj.onc.1210348", "reviewed_relay_candidate", "HGF binding to NRP1, NRP1 perturbation, and MET-associated signaling/function support a qualified-high coreceptor relay; NRP1 remains accessory to canonical MET and VEGF/tumor-endothelial context is preserved."),
    "M21A-PAIR-EVID-5326": ("hspa1a tlr4", "M21A-REUSE-2491", "M20A-EXT-2051", "PMID:23043959; PMID:31576776; PMID:28928431", "reviewed_relay_candidate", "Extracellular Hsp70 receptor dependence through TLR4-associated Akt/ERK/JNK and MyD88-p38-NF-kappaB outputs supports qualified-high relay/function; purified direct binding and endotoxin/co-receptor controls remain bounded."),
    "M21A-PAIR-EVID-5328": ("iapp calcr", "M21A-REUSE-2492", "M20A-EXT-2066", "PMID:32219220", "reviewed_relay_candidate", "Engineered CALCR-RAMP3 AMY3 receptor mutagenesis with IAPP cAMP/ERK signaling supports qualified-high exact complex relay/function; no CALCR-only or terminal-TF claim."),
    "M21A-PAIR-EVID-5329": ("iapp ramp3", "M21A-REUSE-2493", "M20A-EXT-2073", "PMID:32219220", "reviewed_relay_candidate", "RAMP3-dependent AMY3 receptor signal modulation supports qualified-high complex-layer promotion; isolated RAMP3 binding is not inferred."),
    "M21A-PAIR-EVID-5330": ("icam1 itgal_itgb2", "M21A-REUSE-2494", "M20A-EXT-2080", "PMID:9539703; PMCID:PMC276084; PMID:19050286; PMID:10688643", "reviewed_relay_candidate", "Complete LFA-1 alphaL-beta2 binding with outside-in cytoskeletal signaling and leukocyte adhesion/migration supports qualified-high relay/function; preserve valency, cations, force, and activation state."),
    "M21A-PAIR-EVID-5332": ("icam2 itgal_itgb2", "M21A-REUSE-2496", "M20A-EXT-2084", "PMID:9153399; PMID:8975879; PMCID:PMC6014170", "reviewed_relay_candidate", "Complete LFA-1 binding with integrin avidity, actin remodeling, and leukocyte crawling/transmigration supports qualified-high relay/function; no isolated subunit claim."),
    "M21A-PAIR-EVID-5333": ("icam4 itga2b", "", "M20A-EXT-2086", "PMID:15355350; DOI:10.1111/j.1432-1033.2004.04313.x; PMID:12477717", "reviewed_binding_only", "Dose-dependent binding of ICAM4 to activated alphaIIb-beta3 supports qualified-high exact binding/adhesion scope; the queued ITGA2B subunit and no receptor-proximal relay are preserved as boundaries.", ("downstream_pathway_function",)),
    "M21A-PAIR-EVID-5335": ("icam4 itgal", "", "M20A-EXT-2088", "PMID:15355350; DOI:10.1111/j.1432-1033.2004.04313.x", "reviewed_binding_only", "Exact ICAM4 binding to alphaL-beta2 transfectants supports qualified-high binding/adhesion scope; ITGAL alone and an intracellular relay are not inferred.", ("downstream_pathway_function",)),
    "M21A-PAIR-EVID-5338": ("icam5 itgal", "", "M20A-EXT-2095", "PMID:8993013; PMID:10741396; PMCID:PMC2603608", "reviewed_binding_only", "Exact ICAM5 binding to complete CD11a/CD18 LFA-1 with T-cell-neuron adhesion supports qualified-high binding/function scope; no autonomous alpha-chain relay is inferred.", ("downstream_pathway_function",)),
}

PROMOTION_NOTE = "Module 21A relay/function promotion batch032 (2026-09-02): evidence tier raised to high for the exact, context-bounded packet; evidence-layer scope, upstream Module 20A LR confidence, terminal-TF status, and SCI transfer remain unchanged."


def read_tsv(path):
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        return list(reader.fieldnames or []), list(reader)


def write_tsv(path, fields, rows):
    with path.open("w", encoding="utf-8", newline="") as handle:
        csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n").writerows(rows)


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
    review_rows_by_file = [rows for _, rows in review_tables]
    review_fields = [fields for fields, _ in review_tables]
    review_rows = [row for rows in review_rows_by_file for row in rows]
    detail, reuse, reviews = index(detail_rows, "evidence_id"), index(reuse_rows, "pathway_reuse_key"), index(review_rows, "review_id")

    for evidence_id, packet in PACKET.items():
        pair_key, reuse_key, review_id, citations, review_status, _basis, *rest = packet
        required_layers = rest[0] if rest else ("receptor_proximal_relay", "downstream_pathway_function")
        row = detail.get(evidence_id)
        if row is None or row.get("confidence_tier") != "medium-high" or row.get("pathway_reuse_key", "") != reuse_key or row.get("source_locators") != citations:
            raise SystemExit(f"detail lineage mismatch: {evidence_id}")
        if not all(layer in row.get("evidence_layer", "") for layer in required_layers):
            raise SystemExit(f"{evidence_id} lacks required evidence layers")
        review = reviews.get(review_id)
        if (review is None or review.get("evidence_id") != evidence_id or review.get("pair_key") != pair_key
                or review.get("source_locators") != citations or review.get("confidence_tier") != "medium-high"
                or review.get("review_status") != review_status):
            raise SystemExit(f"review lineage mismatch: {evidence_id}")
        if reuse_key and (reuse.get(reuse_key) is None or reuse[reuse_key].get("evidence_ids") != evidence_id):
            raise SystemExit(f"reuse lineage mismatch: {evidence_id}")
        coverage = next((item for item in pair_rows if item.get("module21a_evidence_ids") == evidence_id), None)
        if coverage is None or coverage.get("pair_key") != pair_key or coverage.get("module21a_status") != review_status:
            raise SystemExit(f"coverage lineage mismatch: {evidence_id}")

    audit_fields = ["evidence_id", "review_id", "pair_key", "pathway_reuse_key", "previous_tier", "new_tier", "source_locators", "decision_basis", "upstream_lr_confidence_unchanged", "terminal_tf_status_unchanged", "sql_materialization"]
    audit_rows = [{"evidence_id": evidence_id, "review_id": packet[2], "pair_key": packet[0], "pathway_reuse_key": packet[1], "previous_tier": detail[evidence_id]["confidence_tier"], "new_tier": "high", "source_locators": detail[evidence_id]["source_locators"], "decision_basis": packet[5], "upstream_lr_confidence_unchanged": "true", "terminal_tf_status_unchanged": "true", "sql_materialization": "false"} for evidence_id, packet in sorted(PACKET.items())]
    if not args.apply:
        print(json.dumps({"validated": len(audit_rows), "apply": False, "evidence_ids": sorted(PACKET)}, indent=2))
        return
    for evidence_id, packet in PACKET.items():
        row = detail[evidence_id]
        row["confidence_tier"] = "high"
        row["limitations"] = append_once(row["limitations"], PROMOTION_NOTE)
        review = reviews[packet[2]]
        review["confidence_tier"] = "high"
        review["curator_note"] = append_once(review["curator_note"], PROMOTION_NOTE)
        if packet[1]:
            reuse[packet[1]]["validation_status"] = "promoted_high_batch032"
            reuse[packet[1]]["limitations"] = append_once(reuse[packet[1]]["limitations"], PROMOTION_NOTE)
        next(item for item in pair_rows if item.get("module21a_evidence_ids") == evidence_id)["curator_notes"] = append_once(next(item for item in pair_rows if item.get("module21a_evidence_ids") == evidence_id)["curator_notes"], PROMOTION_NOTE)
    write_tsv(DETAIL, detail_fields, detail_rows)
    for path, fields, rows in zip(REVIEW_FILES, review_fields, review_rows_by_file):
        write_tsv(path, fields, rows)
    write_tsv(REUSE, reuse_fields, reuse_rows)
    write_tsv(PAIRS, pair_fields, pair_rows)
    write_tsv(AUDIT, audit_fields, audit_rows)
    SUMMARY.write_text(json.dumps({"promotion_id": "module21a-relay-function-batch032-2026-09-02", "records_promoted": len(audit_rows), "evidence_ids": sorted(PACKET), "promotion_note": PROMOTION_NOTE, "upstream_module20a_lr_confidence_changed": False, "terminal_tf_assignments_created": False, "sql_signaling_edges_created": False, "malformed_legacy_rows_touched": False}, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"validated": len(audit_rows), "applied": len(audit_rows), "evidence_ids": sorted(PACKET)}, indent=2))


if __name__ == "__main__":
    main()
