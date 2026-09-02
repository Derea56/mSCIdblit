#!/usr/bin/env python3
"""Promote the isoform-resolved IGF1-INSR edge from Module 21A."""

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
REVIEWS = RELAY / "module21a_pair_relay_review_batches218_219.tsv"
AUDIT = RELAY / "module21a_relay_promotion_batch116.tsv"
SUMMARY = RELAY / "module21a_relay_promotion_batch116_summary.json"
EVIDENCE_ID = "M21A-PAIR-EVID-5342"
REVIEW_ID = "M20A-EXT-2103"
REUSE_KEY = "M21A-REUSE-2499"
NOTE = (
    "Module 21A qualified-relay promotion batch116 (2026-09-02): IGF1-INSR "
    "evidence is raised to high only for the low-affinity IR-A isoform branch. "
    "IR-B/generic INSR, species/model, assay, and no-SCI boundaries remain "
    "explicit; no terminal-TF claim or SQL signaling edge is created."
)
BASIS = (
    "Low-affinity IGF-I activation of insulin receptor is supported primarily for IR-A with IRS-1/Akt/ERK outputs; promote only the IR-A receptor-isoform branch, not generic INSR or IR-B."
)


def read(path):
    with path.open(encoding="utf-8", newline="") as handle:
        r = csv.DictReader(handle, delimiter="\t")
        return list(r.fieldnames or []), list(r)


def write(path, fields, rows):
    with path.open("w", encoding="utf-8", newline="") as handle:
        w = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        w.writeheader(); w.writerows(rows)


def tokens(value):
    return {x.strip() for x in value.split(";") if x.strip()}


def once(value):
    return value if NOTE in value else f"{value} {NOTE}".strip()


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--apply", action="store_true"); args = ap.parse_args()
    df, detail_rows = read(DETAIL); uf, reuse_rows = read(REUSE); pf, pair_rows = read(PAIRS); rf, review_rows = read(REVIEWS)
    detail = {r["evidence_id"]: r for r in detail_rows}; reuse = {r["pathway_reuse_key"]: r for r in reuse_rows if r.get("pathway_reuse_key")}
    reviews = {r["review_id"]: r for r in review_rows}; pairs = {r["pair_key"]: r for r in pair_rows}
    row = detail.get(EVIDENCE_ID); review = reviews.get(REVIEW_ID)
    if row is None or row.get("confidence_tier") != "low-medium" or row.get("pathway_reuse_key") != REUSE_KEY:
        raise SystemExit("detail lineage/tier mismatch")
    if review is None or review.get("evidence_id") != EVIDENCE_ID or review.get("pathway_reuse_key") != REUSE_KEY or review.get("review_status") != "reviewed_relay_candidate" or review.get("source_locators") != row.get("source_locators"):
        raise SystemExit("review lineage mismatch")
    if REUSE_KEY not in reuse or reuse[REUSE_KEY].get("evidence_ids") != EVIDENCE_ID:
        raise SystemExit("reuse lineage mismatch")
    pair = pairs.get(review.get("pair_key"))
    if pair is None or EVIDENCE_ID not in tokens(pair.get("module21a_evidence_ids", "")) or pair.get("module21a_status") != review.get("review_status") or pair.get("module22a_status") != "no_terminal_tf_evidence":
        raise SystemExit("coverage/TF-boundary mismatch")
    hits = []
    for path in RELAY.glob("module21a_relay_promotion_batch*.tsv"):
        if path == AUDIT: continue
        with path.open(encoding="utf-8", newline="") as handle:
            if any(x.get("evidence_id") == EVIDENCE_ID or x.get("pair_key") == review.get("pair_key") for x in csv.DictReader(handle, delimiter="\t")): hits.append(path.name)
    if hits: raise SystemExit(f"promotion overlap: {hits}")
    audit = [{"evidence_id": EVIDENCE_ID, "review_id": REVIEW_ID, "pair_key": review["pair_key"], "pathway_reuse_key": REUSE_KEY, "previous_tier": row["confidence_tier"], "new_tier": "high", "source_locators": row["source_locators"], "decision_basis": BASIS, "upstream_lr_confidence_unchanged": "true", "terminal_tf_status_unchanged": "true", "sql_materialization": "false"}]
    if not args.apply:
        print(json.dumps({"validated": 1, "apply": False, "evidence_ids": [EVIDENCE_ID]}, indent=2)); return
    row["confidence_tier"] = "high"; row["limitations"] = once(row["limitations"])
    review["confidence_tier"] = "high"; review["curator_note"] = once(review["curator_note"])
    reuse[REUSE_KEY]["validation_status"] = "promoted_high_batch116"; reuse[REUSE_KEY]["limitations"] = once(reuse[REUSE_KEY]["limitations"])
    pair["curator_notes"] = once(pair["curator_notes"])
    write(DETAIL, df, detail_rows); write(REUSE, uf, reuse_rows); write(PAIRS, pf, pair_rows); write(REVIEWS, rf, review_rows)
    fields = ["evidence_id", "review_id", "pair_key", "pathway_reuse_key", "previous_tier", "new_tier", "source_locators", "decision_basis", "upstream_lr_confidence_unchanged", "terminal_tf_status_unchanged", "sql_materialization"]
    write(AUDIT, fields, audit)
    SUMMARY.write_text(json.dumps({"promotion_id": "module21a-local-register-exact-pair-batch116-2026-09-02", "records_promoted": 1, "evidence_ids": [EVIDENCE_ID], "promotion_note": NOTE, "upstream_module20a_lr_confidence_changed": False, "terminal_tf_assignments_created": False, "sql_signaling_edges_created": False, "malformed_legacy_rows_touched": False}, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"validated": 1, "applied": 1, "evidence_ids": [EVIDENCE_ID]}, indent=2))


if __name__ == "__main__":
    main()
