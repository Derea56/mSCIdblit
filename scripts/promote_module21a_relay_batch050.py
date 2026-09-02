#!/usr/bin/env python3
"""Promote seven bounded Module 21A THY1, TIMP, TNC, and transferrin packets."""

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
REVIEW_FILES = [RELAY / "module21a_pair_relay_review_batches232.tsv"]
AUDIT = RELAY / "module21a_relay_promotion_batch050.tsv"
SUMMARY = RELAY / "module21a_relay_promotion_batch050_summary.json"

PACKET = {
    "M21A-PAIR-EVID-5702": ("thy1 itgam_itgb2", "M21A-REUSE-2789", "M20A-EXT-3296", "PMID:15004192; DOI:10.4049/jimmunol.172.6.3850", "Exact endothelial THY1-alphaMbeta2/Mac-1 adhesion and transendothelial-migration function supports qualified-high promotion; preserve the complete Mac-1 heterodimer and no cytosolic relay or TF claim."),
    "M21A-PAIR-EVID-5705": ("timp1 cd63", "M21A-REUSE-2791", "M20A-EXT-3299", "PMID:32034211; PMID:23522389", "Exact TIMP1-CD63/beta1-integrin tetraspanin-complex relay/function supports qualified-high promotion; preserve beta1-integrin, cancer-state, and domain context and do not call CD63 a kinase receptor."),
    "M21A-PAIR-EVID-5706": ("timp2 itga3", "M21A-REUSE-2792", "M20A-EXT-3302", "PMID:16326706; PMID:18721821; PMCID:PMC2574962; DOI:10.1016/j.mvr.2008.07.003; PMID:21871510; PMCID:PMC3177407; DOI:10.1016/j.peptides.2011.08.010", "Exact TIMP2-alpha3beta1/SHP-1-Csk/cAMP-Rap1-MAPK inhibitory relay/function supports qualified-high promotion; preserve the complete alpha3beta1 complex and distinguish integrin outputs from FGF2/VEGF antagonism."),
    "M21A-PAIR-EVID-5707": ("timp2 itgb1", "M21A-REUSE-2793", "M20A-EXT-3303", "PMID:16326706; PMID:18721821; PMCID:PMC2574962; DOI:10.1016/j.mvr.2008.07.003; PMID:21871510; PMCID:PMC3177407; DOI:10.1016/j.peptides.2011.08.010", "Exact TIMP2-alpha3beta1/ITGB1 complex function supports qualified-high promotion; preserve ITGB1 as the beta1 subunit, not an isolated receptor, and retain the SHP-1/Csk/cAMP-Rap1/MAPK context."),
    "M21A-PAIR-EVID-5710": ("tnc cntn1", "M21A-REUSE-2795", "M20A-EXT-3311", "PMID:1382076; PMCID:PMC2289633; DOI:10.1083/jcb.119.1.203; PMID:12151539", "Exact TNC FNIII-domain-CNTN1/contactin binding and neuronal adhesion/neurite function supports qualified-high promotion; preserve TNC splice/domain architecture and no CNTN1 cytosolic relay or TF claim."),
    "M21A-PAIR-EVID-5712": ("tnc itga7", "M21A-REUSE-2797", "M20A-EXT-3315", "PMID:14715956", "Exact TNC FNIII-D alpha7beta1 binding and neuronal process-extension function supports qualified-high promotion; preserve the complete alpha7beta1 heterodimer and no isolated ITGA7 relay or TF claim."),
    "M21A-PAIR-EVID-5716": ("trf tfr2", "M21A-REUSE-2799", "M20A-EXT-3360", "PMID:20096706; PMID:12393650; DOI:10.1182/blood-2002-01-0076", "Exact transferrin-TFR2alpha binding, uptake/recycling, and iron-sensing function supports qualified-high promotion; preserve lower affinity versus TFR1, TFR2 isoform/tissue context, and scavenging-only topology."),
}

FUNCTION_ONLY = {"M21A-PAIR-EVID-5702", "M21A-PAIR-EVID-5710", "M21A-PAIR-EVID-5712", "M21A-PAIR-EVID-5716"}
STATUS_BY_ID = {
    "M21A-PAIR-EVID-5702": {"reviewed_function_only"},
    "M21A-PAIR-EVID-5710": {"reviewed_function_only"},
    "M21A-PAIR-EVID-5712": {"reviewed_function_only"},
    "M21A-PAIR-EVID-5716": {"reviewed_scavenging_only"},
}
PROMOTION_NOTE = "Module 21A relay/function promotion batch050 (2026-09-02): evidence tier raised to high for the exact, context-bounded packet; evidence-layer scope, upstream Module 20A LR confidence, terminal-TF status, and SCI transfer remain unchanged."


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
        allowed_status = STATUS_BY_ID[evidence_id] if evidence_id in FUNCTION_ONLY else {"reviewed_relay_candidate"}
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
        reuse[packet[1]]["validation_status"] = "promoted_high_batch050"
        reuse[packet[1]]["limitations"] = append_once(reuse[packet[1]]["limitations"], PROMOTION_NOTE)
        coverage = next(item for item in pair_rows if item.get("module21a_evidence_ids") == evidence_id)
        coverage["curator_notes"] = append_once(coverage["curator_notes"], PROMOTION_NOTE)

    write_tsv(DETAIL, detail_fields, detail_rows)
    for path, fields, rows in zip(REVIEW_FILES, review_fields, review_rows_by_file):
        write_tsv(path, fields, rows)
    write_tsv(REUSE, reuse_fields, reuse_rows)
    write_tsv(PAIRS, pair_fields, pair_rows)
    write_tsv(AUDIT, audit_fields, audit_rows)
    SUMMARY.write_text(json.dumps({"promotion_id": "module21a-relay-function-batch050-2026-09-02", "records_promoted": len(audit_rows), "evidence_ids": sorted(PACKET), "promotion_note": PROMOTION_NOTE, "upstream_module20a_lr_confidence_changed": False, "terminal_tf_assignments_created": False, "sql_signaling_edges_created": False, "malformed_legacy_rows_touched": False}, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"validated": len(audit_rows), "applied": len(audit_rows), "evidence_ids": sorted(PACKET)}, indent=2))


if __name__ == "__main__":
    main()
