#!/usr/bin/env python3
"""Promote seven bounded Module 21A relay/function packets."""

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
REVIEW_FILE = RELAY / "module21a_pair_relay_review_batches208_209.tsv"
AUDIT = RELAY / "module21a_relay_promotion_batch021.tsv"
SUMMARY = RELAY / "module21a_relay_promotion_batch021_summary.json"

PACKET = {
    "M21A-PAIR-EVID-5101": {
        "pair_key": "efna4 epha10", "reuse_key": "M21A-REUSE-2390", "review_id": "M20A-EXT-1531",
        "citations": "PMID:33436772; DOI:10.1038/s41598-020-80060-3",
        "required_layers": ("receptor_proximal_relay", "downstream_pathway_function"),
        "review_status": "reviewed_relay_candidate",
        "coverage_status": "reviewed_relay_candidate",
        "scope": "relay/function",
        "basis": "EFNA4/EPHA10 dependence, ERK inhibition, and NANOG perturbation support qualified-high exact relay/function evidence in defined oral-carcinoma and xenograft models; direct binding is not upgraded beyond the receptor-dependence packet.",
    },
    "M21A-PAIR-EVID-5104": {
        "pair_key": "efna5 ephb2", "reuse_key": "M21A-REUSE-2392", "review_id": "M20A-EXT-1540",
        "citations": "PMID:26839344; DOI:10.1242/dev.129478; PMID:15107857",
        "required_layers": ("receptor_proximal_relay", "downstream_pathway_function"),
        "review_status": "reviewed_relay_candidate",
        "coverage_status": "reviewed_relay_candidate",
        "scope": "relay/function",
        "basis": "Exact ephrin-A5/EphB2 stimulation, receptor phosphorylation, sustained JNK, and optic-cup or growth-cone outputs support qualified-high relay/function evidence; developmental and comparator-model boundaries remain explicit.",
    },
    "M21A-PAIR-EVID-5105": {
        "pair_key": "efnb1 ephb1", "reuse_key": "M21A-REUSE-2393", "review_id": "M20A-EXT-1543",
        "citations": "PMID:39648610; DOI:10.1002/cac2.12637; PMID:25944917",
        "required_layers": ("receptor_proximal_relay", "downstream_pathway_function"),
        "review_status": "reviewed_relay_candidate",
        "coverage_status": "reviewed_relay_candidate",
        "scope": "bidirectional relay/function",
        "basis": "EFNB1/EPHB1 contact, perturbation, AKT output, and tumor-platelet metastatic phenotypes support qualified-high contact/signaling evidence; forward EphB1 and reverse EFNB1 contributions remain inseparable in some assays.",
    },
    "M21A-PAIR-EVID-5108": {
        "pair_key": "egf pld2", "reuse_key": "M21A-REUSE-2394", "review_id": "M20A-EXT-1563",
        "citations": "PMID:12646582; DOI:10.1074/jbc.M208438200; PMID:15896299",
        "required_layers": ("downstream_pathway_function",),
        "review_status": "reviewed_function_only",
        "coverage_status": "reviewed_function_only",
        "scope": "downstream function/metabolic effector",
        "basis": "EGF-to-EGFR signaling through the PLC-gamma1/PLD2 complex and IP3/Ca2+ output supports qualified-high downstream-function evidence; PLD2 is not promoted as a direct EGF receptor or binding partner.",
    },
    "M21A-PAIR-EVID-5113": {
        "pair_key": "entpd1 adora1", "reuse_key": "M21A-REUSE-2397", "review_id": "M20A-EXT-1568",
        "citations": "PMID:32999463; DOI:10.1038/s41586-020-2623-2; DOI:10.1152/ajprenal.00603.2007",
        "required_layers": ("downstream_pathway_function",),
        "review_status": "reviewed_function_only",
        "coverage_status": "reviewed_function_only",
        "scope": "downstream function/metabolic coupling",
        "basis": "ENTPD1/CD39 contribution to AMP/CD73/adenosine availability and ADORA1-dependent neuronal or vascular outputs supports qualified-high metabolic-coupling function evidence; CD73 is an essential intermediate and no enzyme-receptor binding is claimed.",
    },
    "M21A-PAIR-EVID-5115": {
        "pair_key": "entpd1 adora2b", "reuse_key": "M21A-REUSE-2399", "review_id": "M20A-EXT-1570",
        "citations": "DOI:10.1186/s12931-023-02486-3; DOI:10.1016/j.bbrc.2025.153142; PMID:38833181",
        "required_layers": ("downstream_pathway_function",),
        "review_status": "reviewed_function_only",
        "coverage_status": "reviewed_function_only",
        "scope": "downstream function/metabolic coupling",
        "basis": "ENTPD1/CD39 and CD73-generated adenosine with ADORA2B-dependent protection or trophoblast differentiation supports qualified-high metabolic-coupling function evidence; CD73 is obligatory and direct enzyme-receptor binding is excluded.",
    },
    "M21A-PAIR-EVID-5118": {
        "pair_key": "epo ephb4", "reuse_key": "M21A-REUSE-2401", "review_id": "M20A-EXT-1573",
        "citations": "PMCID:PMC4643364; PMID:26481148",
        "required_layers": ("receptor_proximal_relay", "downstream_pathway_function"),
        "review_status": "reviewed_relay_candidate",
        "coverage_status": "reviewed_relay_candidate",
        "scope": "relay/function",
        "basis": "EPO stimulation, EphB4 perturbation, receptor activation, Src/STAT3 output, and tumor-growth effects support qualified-high exact relay/function evidence in defined cancer models; this alternative receptor does not replace canonical EPOR physiology.",
    },
}

PROMOTION_NOTE = "Module 21A relay/function promotion batch021 (2026-09-02): evidence tier raised to high for the exact, context-bounded packet; evidence-layer scope, upstream Module 20A LR confidence, terminal-TF status, and SCI transfer remain unchanged."


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
    review_fields, review_rows = read_tsv(REVIEW_FILE)
    detail = index(detail_rows, "evidence_id")
    reuse = index(reuse_rows, "pathway_reuse_key")
    reviews = index(review_rows, "review_id")

    for evidence_id, expected in PACKET.items():
        row = detail.get(evidence_id)
        if row is None or row.get("confidence_tier") != "medium-high":
            raise SystemExit(f"{evidence_id} missing or not medium-high")
        if not all(layer in row.get("evidence_layer", "") for layer in expected["required_layers"]):
            raise SystemExit(f"{evidence_id} lacks required evidence layers")
        if row.get("pathway_reuse_key") != expected["reuse_key"] or row.get("source_locators") != expected["citations"]:
            raise SystemExit(f"detail lineage mismatch: {evidence_id}")
        review = reviews.get(expected["review_id"])
        if (review is None or review.get("evidence_id") != evidence_id or review.get("pair_key") != expected["pair_key"]
                or review.get("source_locators") != expected["citations"]
                or review.get("confidence_tier") != "medium-high"
                or review.get("review_status") != expected["review_status"]):
            raise SystemExit(f"review lineage mismatch: {evidence_id}")
        reuse_row = reuse.get(expected["reuse_key"])
        if reuse_row is None or reuse_row.get("evidence_ids") != evidence_id:
            raise SystemExit(f"reuse lineage mismatch: {evidence_id}")
        coverage = next((item for item in pair_rows if item.get("module21a_evidence_ids") == evidence_id), None)
        if (coverage is None or coverage.get("pair_key") != expected["pair_key"]
                or coverage.get("module21a_status") != expected["coverage_status"]):
            raise SystemExit(f"coverage lineage mismatch: {evidence_id}")

    audit_fields = ["evidence_id", "review_id", "pair_key", "pathway_reuse_key", "promotion_scope", "previous_tier", "new_tier", "source_locators", "decision_basis", "upstream_lr_confidence_unchanged", "terminal_tf_status_unchanged", "sql_materialization"]
    audit_rows = [{
        "evidence_id": evidence_id,
        "review_id": expected["review_id"],
        "pair_key": expected["pair_key"],
        "pathway_reuse_key": expected["reuse_key"],
        "promotion_scope": expected["scope"],
        "previous_tier": detail[evidence_id]["confidence_tier"],
        "new_tier": "high",
        "source_locators": detail[evidence_id]["source_locators"],
        "decision_basis": expected["basis"],
        "upstream_lr_confidence_unchanged": "true",
        "terminal_tf_status_unchanged": "true",
        "sql_materialization": "false",
    } for evidence_id, expected in sorted(PACKET.items())]

    if not args.apply:
        print(json.dumps({"validated": len(audit_rows), "apply": False, "evidence_ids": sorted(PACKET)}, indent=2))
        return

    for evidence_id, expected in PACKET.items():
        row = detail[evidence_id]
        row["confidence_tier"] = "high"
        row["limitations"] = append_once(row["limitations"], PROMOTION_NOTE)
        review = reviews[expected["review_id"]]
        review["confidence_tier"] = "high"
        review["curator_note"] = append_once(review["curator_note"], PROMOTION_NOTE)
        reuse_row = reuse[expected["reuse_key"]]
        reuse_row["validation_status"] = "promoted_high_batch021"
        reuse_row["limitations"] = append_once(reuse_row["limitations"], PROMOTION_NOTE)
        coverage = next(item for item in pair_rows if item.get("module21a_evidence_ids") == evidence_id)
        coverage["curator_notes"] = append_once(coverage["curator_notes"], PROMOTION_NOTE)

    write_tsv(DETAIL, detail_fields, detail_rows)
    write_tsv(REVIEW_FILE, review_fields, review_rows)
    write_tsv(REUSE, reuse_fields, reuse_rows)
    write_tsv(PAIRS, pair_fields, pair_rows)
    write_tsv(AUDIT, audit_fields, audit_rows)
    SUMMARY.write_text(json.dumps({
        "promotion_id": "module21a-relay-function-batch021-2026-09-02",
        "records_promoted": len(audit_rows),
        "evidence_ids": sorted(PACKET),
        "promotion_note": PROMOTION_NOTE,
        "provenance_correction": "M21A-PAIR-EVID-5118 corrected from PMID:23314808 to PMID:26481148 for PMCID:PMC4643364 before promotion.",
        "upstream_module20a_lr_confidence_changed": False,
        "terminal_tf_assignments_created": False,
        "sql_signaling_edges_created": False,
        "malformed_legacy_rows_touched": False,
    }, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"validated": len(audit_rows), "applied": len(audit_rows), "evidence_ids": sorted(PACKET)}, indent=2))


if __name__ == "__main__":
    main()
