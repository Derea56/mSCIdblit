#!/usr/bin/env python3
"""Promote three bounded Module 21A FGF/hepassocin packets."""

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
AUDIT = RELAY / "module21a_relay_promotion_batch025.tsv"
SUMMARY = RELAY / "module21a_relay_promotion_batch025_summary.json"

PACKET = {
    "M21A-PAIR-EVID-5183": {
        "pair_key": "fgf22 fgfr1", "reuse_key": "M21A-REUSE-2428", "review_id": "M20A-EXT-1676",
        "review_file": RELAY / "module21a_pair_relay_review_batches212_213.tsv",
        "citations": "PMID:16597617; PMCID:PMC2080618; PMID:27605441; PMID:25926357",
        "required_layers": ("receptor_proximal_relay", "downstream_pathway_function"),
        "basis": "FGF22 receptor-isoform-specific activation and FGFR1b-dependent presynaptic differentiation/vesicle recruitment support qualified-high exact relay/function evidence; FGFR1b and neuronal context remain explicit.",
    },
    "M21A-PAIR-EVID-5185": {
        "pair_key": "fgf23 fgfr2", "reuse_key": "M21A-REUSE-2429", "review_id": "M20A-EXT-1678",
        "review_file": RELAY / "module21a_pair_relay_review_batches212_213.tsv",
        "citations": "PMID:26878171; PMCID:PMC4767336; DOI:10.1172/JCI83470",
        "required_layers": ("receptor_proximal_relay", "downstream_pathway_function"),
        "basis": "FGFR2-dependent PKA/Rap1 inhibition and beta2-integrin/neutrophil recruitment outputs support qualified-high noncanonical relay/function evidence; this is Klotho-independent PMN context and not canonical renal FGF23 signaling.",
    },
    "M21A-PAIR-EVID-5192": {
        "pair_key": "fgl1 egfr", "reuse_key": "M21A-REUSE-2430", "review_id": "M20A-EXT-1697",
        "review_file": RELAY / "module21a_pair_relay_review_batches212_213.tsv",
        "citations": "PMID:41967236; DOI:10.1016/j.abb.2026.110820",
        "required_layers": ("receptor_proximal_relay", "downstream_pathway_function"),
        "basis": "EGFR silencing, NOX1/p38 perturbation, and vascular injury/adhesion outputs support qualified-high EGFR-dependent downstream relay/function evidence in defined HUVEC, hepatocyte, and mouse vascular models; purified FGL1-EGFR binding is not claimed.",
    },
}

PROMOTION_NOTE = "Module 21A relay/function promotion batch025 (2026-09-02): evidence tier raised to high for the exact, context-bounded packet; evidence-layer scope, upstream Module 20A LR confidence, terminal-TF status, and SCI transfer remain unchanged."


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
    review_sets = {}
    for review_file in {expected["review_file"] for expected in PACKET.values()}:
        fields, rows = read_tsv(review_file)
        review_sets[review_file] = (fields, rows, index(rows, "review_id"))
    detail = index(detail_rows, "evidence_id")
    reuse = index(reuse_rows, "pathway_reuse_key")

    for evidence_id, expected in PACKET.items():
        row = detail.get(evidence_id)
        if row is None or row.get("confidence_tier") != "medium-high":
            raise SystemExit(f"{evidence_id} missing or not medium-high")
        if not all(layer in row.get("evidence_layer", "") for layer in expected["required_layers"]):
            raise SystemExit(f"{evidence_id} lacks required evidence layers")
        if row.get("pathway_reuse_key") != expected["reuse_key"] or row.get("source_locators") != expected["citations"]:
            raise SystemExit(f"detail lineage mismatch: {evidence_id}")
        _, _, reviews = review_sets[expected["review_file"]]
        review = reviews.get(expected["review_id"])
        if (review is None or review.get("evidence_id") != evidence_id or review.get("pair_key") != expected["pair_key"]
                or review.get("source_locators") != expected["citations"]
                or review.get("confidence_tier") != "medium-high"
                or review.get("review_status") != "reviewed_relay_candidate"):
            raise SystemExit(f"review lineage mismatch: {evidence_id}")
        reuse_row = reuse.get(expected["reuse_key"])
        if reuse_row is None or reuse_row.get("evidence_ids") != evidence_id:
            raise SystemExit(f"reuse lineage mismatch: {evidence_id}")
        coverage = next((item for item in pair_rows if item.get("module21a_evidence_ids") == evidence_id), None)
        if (coverage is None or coverage.get("pair_key") != expected["pair_key"]
                or coverage.get("module21a_status") != "reviewed_relay_candidate"):
            raise SystemExit(f"coverage lineage mismatch: {evidence_id}")

    audit_fields = ["evidence_id", "review_id", "pair_key", "pathway_reuse_key", "previous_tier", "new_tier", "source_locators", "decision_basis", "upstream_lr_confidence_unchanged", "terminal_tf_status_unchanged", "sql_materialization"]
    audit_rows = [{
        "evidence_id": evidence_id,
        "review_id": expected["review_id"],
        "pair_key": expected["pair_key"],
        "pathway_reuse_key": expected["reuse_key"],
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
        _, _, reviews = review_sets[expected["review_file"]]
        review = reviews[expected["review_id"]]
        review["confidence_tier"] = "high"
        review["curator_note"] = append_once(review["curator_note"], PROMOTION_NOTE)
        reuse_row = reuse[expected["reuse_key"]]
        reuse_row["validation_status"] = "promoted_high_batch025"
        reuse_row["limitations"] = append_once(reuse_row["limitations"], PROMOTION_NOTE)
        coverage = next(item for item in pair_rows if item.get("module21a_evidence_ids") == evidence_id)
        coverage["curator_notes"] = append_once(coverage["curator_notes"], PROMOTION_NOTE)

    write_tsv(DETAIL, detail_fields, detail_rows)
    for review_file, (fields, rows, _) in review_sets.items():
        write_tsv(review_file, fields, rows)
    write_tsv(REUSE, reuse_fields, reuse_rows)
    write_tsv(PAIRS, pair_fields, pair_rows)
    write_tsv(AUDIT, audit_fields, audit_rows)
    SUMMARY.write_text(json.dumps({
        "promotion_id": "module21a-relay-function-batch025-2026-09-02",
        "records_promoted": len(audit_rows),
        "evidence_ids": sorted(PACKET),
        "promotion_note": PROMOTION_NOTE,
        "upstream_module20a_lr_confidence_changed": False,
        "terminal_tf_assignments_created": False,
        "sql_signaling_edges_created": False,
        "malformed_legacy_rows_touched": False,
    }, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"validated": len(audit_rows), "applied": len(audit_rows), "evidence_ids": sorted(PACKET)}, indent=2))


if __name__ == "__main__":
    main()
