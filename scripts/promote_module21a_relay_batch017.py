#!/usr/bin/env python3
"""Promote two exact Module 21A evidence packets with explicit layer bounds."""

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
AUDIT = RELAY / "module21a_relay_promotion_batch017.tsv"
SUMMARY = RELAY / "module21a_relay_promotion_batch017_summary.json"
REVIEW_FILE = RELAY / "module21a_pair_relay_review_batches206_207.tsv"

PACKET = {
    "M21A-PAIR-EVID-5032": {
        "pair_key": "crp olr1", "reuse_key": "M21A-REUSE-2355", "review_id": "M20A-EXT-1387",
        "citations": "PMID:19074514; PMID:21821723; DOI:10.1373/clinchem.2008.119750; PMCID:PMC3204104",
        "required_layers": ("ligand_receptor_binding_or_activation", "downstream_pathway_function"),
        "basis": "CRP/OLR1 direct binding or receptor-dependence together with ROS/complement and endothelial or macrophage inflammatory outputs support qualified-high exact binding/function evidence; no canonical kinase relay is inferred.",
    },
    "M21A-PAIR-EVID-5044": {
        "pair_key": "csf2 sdc2", "reuse_key": "M21A-REUSE-2357", "review_id": "M20A-EXT-1399",
        "citations": "PMID:10734053; DOI:10.1074/jbc.275.13.9178",
        "required_layers": ("receptor_proximal_relay", "downstream_pathway_function"),
        "basis": "GM-CSF/SDC2-CSF2RA co-receptor evidence with SDC2 phosphorylation, ERK1 signaling, and human osteoblast mitogenic output supports qualified-high co-receptor relay/function evidence; SDC2 is not treated as a standalone cytokine receptor.",
    },
}
PROMOTION_NOTE = "Module 21A relay/function promotion batch017 (2026-09-02): evidence tier raised to high for the exact, layer-bounded packet; upstream Module 20A LR confidence, terminal-TF status, and SCI transfer remain unchanged."


def read_tsv(path):
    with path.open(encoding="utf-8", newline="") as h:
        r = csv.DictReader(h, delimiter="\t")
        return list(r.fieldnames or []), list(r)


def write_tsv(path, fields, rows):
    with path.open("w", encoding="utf-8", newline="") as h:
        w = csv.DictWriter(h, fieldnames=fields, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


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
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    detail_fields, detail_rows = read_tsv(DETAIL)
    reuse_fields, reuse_rows = read_tsv(REUSE)
    pair_fields, pair_rows = read_tsv(PAIRS)
    review_fields, review_rows = read_tsv(REVIEW_FILE)
    detail, reuse, reviews = index(detail_rows, "evidence_id"), index(reuse_rows, "pathway_reuse_key"), index(review_rows, "review_id")
    for evidence_id, expected in PACKET.items():
        d = detail.get(evidence_id)
        if d is None or d.get("confidence_tier") != "medium-high":
            raise SystemExit(f"{evidence_id} missing or not medium-high")
        if not all(x in d.get("evidence_layer", "") for x in expected["required_layers"]):
            raise SystemExit(f"{evidence_id} lacks required evidence layers")
        if d.get("pathway_reuse_key") != expected["reuse_key"] or d.get("source_locators") != expected["citations"]:
            raise SystemExit(f"detail lineage mismatch: {evidence_id}")
        rv = reviews.get(expected["review_id"])
        if rv is None or rv.get("evidence_id") != evidence_id or rv.get("pair_key") != expected["pair_key"] or rv.get("source_locators") != expected["citations"] or rv.get("confidence_tier") != "medium-high" or rv.get("review_status") != "reviewed_relay_candidate":
            raise SystemExit(f"review lineage mismatch: {evidence_id}")
        ru = reuse.get(expected["reuse_key"])
        if ru is None or ru.get("evidence_ids") != evidence_id:
            raise SystemExit(f"reuse lineage mismatch: {evidence_id}")
        pair = next((p for p in pair_rows if p.get("module21a_evidence_ids") == evidence_id), None)
        if pair is None or pair.get("pair_key") != expected["pair_key"] or pair.get("module21a_status") != "reviewed_relay_candidate":
            raise SystemExit(f"coverage lineage mismatch: {evidence_id}")
    audit_fields = ["evidence_id", "review_id", "pair_key", "pathway_reuse_key", "previous_tier", "new_tier", "source_locators", "decision_basis", "upstream_lr_confidence_unchanged", "terminal_tf_status_unchanged", "sql_materialization"]
    audit_rows = [{"evidence_id": e, "review_id": v["review_id"], "pair_key": v["pair_key"], "pathway_reuse_key": v["reuse_key"], "previous_tier": detail[e]["confidence_tier"], "new_tier": "high", "source_locators": detail[e]["source_locators"], "decision_basis": v["basis"], "upstream_lr_confidence_unchanged": "true", "terminal_tf_status_unchanged": "true", "sql_materialization": "false"} for e, v in sorted(PACKET.items())]
    if not args.apply:
        print(json.dumps({"validated": len(audit_rows), "apply": False, "evidence_ids": sorted(PACKET)}, indent=2))
        return
    for e, v in PACKET.items():
        detail[e]["confidence_tier"] = "high"
        detail[e]["limitations"] = append_once(detail[e]["limitations"], PROMOTION_NOTE)
        rv = reviews[v["review_id"]]
        rv["confidence_tier"] = "high"
        rv["curator_note"] = append_once(rv["curator_note"], PROMOTION_NOTE)
        reuse[v["reuse_key"]]["validation_status"] = "promoted_relay_function_high_batch017"
        reuse[v["reuse_key"]]["limitations"] = append_once(reuse[v["reuse_key"]]["limitations"], PROMOTION_NOTE)
        pair = next(p for p in pair_rows if p.get("module21a_evidence_ids") == e)
        pair["curator_notes"] = append_once(pair["curator_notes"], PROMOTION_NOTE)
    write_tsv(DETAIL, detail_fields, detail_rows)
    write_tsv(REVIEW_FILE, review_fields, review_rows)
    write_tsv(REUSE, reuse_fields, reuse_rows)
    write_tsv(PAIRS, pair_fields, pair_rows)
    write_tsv(AUDIT, audit_fields, audit_rows)
    SUMMARY.write_text(json.dumps({"promotion_id": "module21a-relay-function-batch017-2026-09-02", "records_promoted": len(audit_rows), "evidence_ids": sorted(PACKET), "promotion_note": PROMOTION_NOTE, "upstream_module20a_lr_confidence_changed": False, "terminal_tf_assignments_created": False, "sql_signaling_edges_created": False, "malformed_legacy_rows_touched": False}, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"validated": len(audit_rows), "applied": len(audit_rows), "evidence_ids": sorted(PACKET)}, indent=2))


if __name__ == "__main__":
    main()
