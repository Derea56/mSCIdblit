#!/usr/bin/env python3
"""Promote the exact purified WNT3A-FZD8-LRP6 case in Module 21A."""

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
REVIEW = RELAY / "module21a_pair_relay_review_batches188_189.tsv"
AUDIT = RELAY / "module21a_relay_promotion_batch108.tsv"
SUMMARY = RELAY / "module21a_relay_promotion_batch108_summary.json"
EID = "M21A-PAIR-EVID-4577"
RID = "M20A-LIANA-REMAINING-0427"
RKEY = "M21A-REUSE-2114"
NOTE = (
    "Module 21A qualified-relay promotion batch108 (2026-09-02): direct purified WNT3A-FZD8 "
    "CRD-LRP6 E1E4 ternary-complex formation and receptor-proximal canonical signaling context "
    "is raised to high at the exact supported layer. Soluble-fragment, construct, full-length "
    "stoichiometry, ligand-presentation, species/model, and no-SCI boundaries remain explicit; "
    "no terminal-TF claim is created."
)


def read(path):
    with path.open(encoding="utf-8", newline="") as h:
        r = csv.DictReader(h, delimiter="\t")
        return list(r.fieldnames or []), list(r)


def write(path, fields, rows):
    with path.open("w", encoding="utf-8", newline="") as h:
        w = csv.DictWriter(h, fieldnames=fields, delimiter="\t", lineterminator="\n")
        w.writeheader(); w.writerows(rows)


def index(rows, key):
    out = {}
    for r in rows:
        v = r.get(key, "")
        if v and v in out: raise SystemExit(f"duplicate {key}: {v}")
        if v: out[v] = r
    return out


def tokens(v): return {x.strip() for x in v.split(";") if x.strip()}
def once(v): return v if NOTE in v else f"{v} {NOTE}".strip()


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--apply", action="store_true"); args = ap.parse_args()
    df, dr = read(DETAIL); uf, ur = read(REUSE); pf, pr = read(PAIRS); rf, rr = read(REVIEW)
    detail, reuse, reviews = index(dr, "evidence_id"), index(ur, "pathway_reuse_key"), index(rr, "review_id")
    row, review = detail.get(EID), reviews.get(RID)
    if row is None or row.get("confidence_tier") != "low-medium" or row.get("pathway_reuse_key") != RKEY:
        raise SystemExit("detail lineage mismatch")
    if review is None or review.get("evidence_id") != EID or review.get("pathway_reuse_key") != RKEY or review.get("review_status") != "reviewed_relay_candidate" or review.get("source_locators") != row.get("source_locators"):
        raise SystemExit("review lineage mismatch")
    if reuse.get(RKEY) is None or reuse[RKEY].get("evidence_ids") != EID: raise SystemExit("reuse lineage mismatch")
    matches = [x for x in pr if EID in tokens(x.get("module21a_evidence_ids", "")) and x.get("pair_key") == review.get("pair_key")]
    if len(matches) != 1: raise SystemExit("coverage mapping mismatch")
    pair = matches[0]
    if pair.get("module21a_status") != review.get("review_status") or pair.get("module22a_status") != "no_terminal_tf_evidence": raise SystemExit("coverage or TF-boundary mismatch")
    for path in RELAY.glob("module21a_relay_promotion_batch*.tsv"):
        _, rows = read(path)
        if any(x.get("evidence_id") == EID or x.get("pair_key") == review.get("pair_key") for x in rows): raise SystemExit(f"promotion overlap: {path.name}")
    audit = [{"evidence_id": EID, "review_id": RID, "pair_key": review["pair_key"], "pathway_reuse_key": RKEY, "previous_tier": row["confidence_tier"], "new_tier": "high", "source_locators": row["source_locators"], "decision_basis": "Local-register revalidation supports direct purified ternary-complex formation and exact receptor-proximal function at the recorded layer; topology and TF metadata remain unchanged.", "upstream_lr_confidence_unchanged": "true", "terminal_tf_status_unchanged": "true", "sql_materialization": "false"}]
    if not args.apply: print(json.dumps({"validated": 1, "apply": False, "evidence_ids": [EID]}, indent=2)); return
    row["confidence_tier"] = "high"; row["limitations"] = once(row["limitations"])
    review["confidence_tier"] = "high"; review["curator_note"] = once(review["curator_note"])
    reuse[RKEY]["validation_status"] = "promoted_high_batch108"; reuse[RKEY]["limitations"] = once(reuse[RKEY]["limitations"])
    pair["curator_notes"] = once(pair["curator_notes"])
    write(DETAIL, df, dr); write(REVIEW, rf, rr); write(REUSE, uf, ur); write(PAIRS, pf, pr)
    af = ["evidence_id", "review_id", "pair_key", "pathway_reuse_key", "previous_tier", "new_tier", "source_locators", "decision_basis", "upstream_lr_confidence_unchanged", "terminal_tf_status_unchanged", "sql_materialization"]
    write(AUDIT, af, audit)
    SUMMARY.write_text(json.dumps({"promotion_id": "module21a-local-register-purified-wnt3a-fzd8-lrp6-batch108-2026-09-02", "records_promoted": 1, "evidence_ids": [EID], "promotion_note": NOTE, "upstream_module20a_lr_confidence_changed": False, "terminal_tf_assignments_created": False, "sql_signaling_edges_created": False, "malformed_legacy_rows_touched": False}, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"validated": 1, "applied": 1, "evidence_ids": [EID]}, indent=2))


if __name__ == "__main__": main()
