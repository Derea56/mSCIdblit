#!/usr/bin/env python3
"""Promote the worker-validated WNT1 receptor-complex subset of Module 21A."""

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
REVIEW_FILES = [RELAY / "module21a_pair_relay_review_batches180_181.tsv", RELAY / "module21a_pair_relay_review_batches182_183.tsv"]
AUDIT = RELAY / "module21a_relay_promotion_batch107.tsv"
SUMMARY = RELAY / "module21a_relay_promotion_batch107_summary.json"
PROMOTION_GLOB = "module21a_relay_promotion_batch*.tsv"
PACKET = [
    (4418, "M20A-LIANA-REMAINING-0268", "M21A-REUSE-2105"),
    (4420, "M20A-LIANA-REMAINING-0270", "M21A-REUSE-2106"),
    (4426, "M20A-LIANA-REMAINING-0276", "M21A-REUSE-2107"),
    (4429, "M20A-LIANA-REMAINING-0279", "M21A-REUSE-2108"),
]
NOTE = (
    "Module 21A qualified-relay promotion batch107 (2026-09-02): worker-validated WNT1 "
    "FZD/LRP or RYK receptor-complex activation/function is raised to high at the exact "
    "recorded layer. Cell-based cotransfection, ectodomain/construct, Frizzled-coupling, "
    "stoichiometry, cross-species, developmental, and no-SCI boundaries remain explicit; "
    "no purified full-complex or terminal-TF claim is created."
)


def read(path):
    with path.open(encoding="utf-8", newline="") as h:
        r = csv.DictReader(h, delimiter="\t")
        return list(r.fieldnames or []), list(r)


def write(path, fields, rows):
    with path.open("w", encoding="utf-8", newline="") as h:
        w = csv.DictWriter(h, fieldnames=fields, delimiter="\t", lineterminator="\n")
        w.writeheader(); w.writerows(rows)


def idx(rows, key):
    out = {}
    for row in rows:
        value = row.get(key, "")
        if value and value in out: raise SystemExit(f"duplicate {key}: {value}")
        if value: out[value] = row
    return out


def toks(value): return {x.strip() for x in value.split(";") if x.strip()}
def once(value): return value if NOTE in value else f"{value} {NOTE}".strip()


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--apply", action="store_true"); args = ap.parse_args()
    df, dr = read(DETAIL); uf, ur = read(REUSE); pf, pr = read(PAIRS)
    tables = [read(x) for x in REVIEW_FILES]
    reviews = idx([r for _, rows in tables for r in rows], "review_id")
    detail, reuse = idx(dr, "evidence_id"), idx(ur, "pathway_reuse_key")
    prior = [x for x in RELAY.glob(PROMOTION_GLOB) if x != AUDIT]
    coverage, audit = {}, []
    for number, review_id, reuse_key in PACKET:
        eid = f"M21A-PAIR-EVID-{number}"; row = detail.get(eid); rev = reviews.get(review_id)
        if row is None or row.get("confidence_tier") not in {"medium", "medium-high"} or row.get("pathway_reuse_key") != reuse_key:
            raise SystemExit(f"detail lineage mismatch: {eid}")
        if rev is None or rev.get("evidence_id") != eid or rev.get("pathway_reuse_key") != reuse_key or rev.get("source_locators") != row.get("source_locators") or rev.get("review_status") != "reviewed_relay_candidate":
            raise SystemExit(f"review lineage mismatch: {eid}")
        if reuse.get(reuse_key) is None or reuse[reuse_key].get("evidence_ids") != eid:
            raise SystemExit(f"reuse lineage mismatch: {eid}")
        matches = [x for x in pr if eid in toks(x.get("module21a_evidence_ids", "")) and x.get("pair_key") == rev.get("pair_key")]
        if len(matches) != 1: raise SystemExit(f"coverage mapping mismatch: {eid}")
        coverage[eid] = matches[0]
        if coverage[eid].get("module21a_status") != rev.get("review_status") or coverage[eid].get("module22a_status") != "no_terminal_tf_evidence":
            raise SystemExit(f"coverage or TF-boundary mismatch: {eid}")
        hits = []
        for path in prior:
            _, rows = read(path)
            if any(x.get("evidence_id") == eid or x.get("pair_key") == rev.get("pair_key") for x in rows): hits.append(path.name)
        if hits: raise SystemExit(f"promotion overlap for {eid}: {hits}")
        audit.append({"evidence_id": eid, "review_id": review_id, "pair_key": rev["pair_key"], "pathway_reuse_key": reuse_key, "previous_tier": row["confidence_tier"], "new_tier": "high", "source_locators": row["source_locators"], "decision_basis": "Worker audit and local-register lineage support exact WNT1 receptor-complex qualified-high function at the recorded layer; topology and TF metadata remain unchanged.", "upstream_lr_confidence_unchanged": "true", "terminal_tf_status_unchanged": "true", "sql_materialization": "false"})
    if not args.apply:
        print(json.dumps({"validated": len(audit), "apply": False, "evidence_ids": [x["evidence_id"] for x in audit]}, indent=2)); return
    for number, review_id, reuse_key in PACKET:
        eid = f"M21A-PAIR-EVID-{number}"; detail[eid]["confidence_tier"] = "high"; detail[eid]["limitations"] = once(detail[eid]["limitations"])
        reviews[review_id]["confidence_tier"] = "high"; reviews[review_id]["curator_note"] = once(reviews[review_id]["curator_note"])
        reuse[reuse_key]["validation_status"] = "promoted_high_batch107"; reuse[reuse_key]["limitations"] = once(reuse[reuse_key]["limitations"])
        coverage[eid]["curator_notes"] = once(coverage[eid]["curator_notes"])
    write(DETAIL, df, dr)
    for path, (fields, rows) in zip(REVIEW_FILES, tables): write(path, fields, rows)
    write(REUSE, uf, ur); write(PAIRS, pf, pr)
    af = ["evidence_id", "review_id", "pair_key", "pathway_reuse_key", "previous_tier", "new_tier", "source_locators", "decision_basis", "upstream_lr_confidence_unchanged", "terminal_tf_status_unchanged", "sql_materialization"]
    write(AUDIT, af, audit)
    SUMMARY.write_text(json.dumps({"promotion_id": "module21a-worker-validated-wnt1-receptor-complex-batch107-2026-09-02", "records_promoted": len(audit), "evidence_ids": [x["evidence_id"] for x in audit], "promotion_note": NOTE, "upstream_module20a_lr_confidence_changed": False, "terminal_tf_assignments_created": False, "sql_signaling_edges_created": False, "malformed_legacy_rows_touched": False}, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"validated": len(audit), "applied": len(audit), "evidence_ids": [x["evidence_id"] for x in audit]}, indent=2))


if __name__ == "__main__": main()
