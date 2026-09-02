#!/usr/bin/env python3
"""Promote worker-confirmed exact-pair rows from the Module 21A 4711-4760 audit."""

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
REVIEW = RELAY / "module21a_pair_relay_review_batches194_195.tsv"
AUDIT = RELAY / "module21a_relay_promotion_batch112.tsv"
SUMMARY = RELAY / "module21a_relay_promotion_batch112_summary.json"
PACKET = [
    (4727, "M20A-CELLCHAT-REMAINING-0478", "M21A-REUSE-2172"),
    (4733, "M20A-CELLCHAT-REMAINING-0730", "M21A-REUSE-2175"),
    (4744, "M20A-CELLCHAT-REMAINING-1291", "M21A-REUSE-2179"),
]
NOTE = (
    "Module 21A qualified-relay promotion batch112 (2026-09-02): worker-confirmed exact "
    "FLRT3-UNC5B adhesion/guidance, GDF5-BMPR1A/ACVR2B receptor-complex, and IL-17A/F "
    "heterodimer receptor-relay evidence is raised to high at the recorded supported layer. "
    "Subtype, stoichiometry, ligand-form, species/model, assay, and no-SCI boundaries remain "
    "explicit; pending terminal-TF rows remain untouched and no SQL edge is created."
)


def read(path):
    with path.open(encoding="utf-8", newline="") as handle:
        r = csv.DictReader(handle, delimiter="\t")
        return list(r.fieldnames or []), list(r)


def write(path, fields, rows):
    with path.open("w", encoding="utf-8", newline="") as handle:
        w = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        w.writeheader(); w.writerows(rows)


def index(rows, key):
    out = {}
    for row in rows:
        value = row.get(key, "")
        if value and value in out: raise SystemExit(f"duplicate {key}: {value}")
        if value: out[value] = row
    return out


def tokens(value): return {x.strip() for x in value.split(";") if x.strip()}
def once(value): return value if NOTE in value else f"{value} {NOTE}".strip()


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--apply", action="store_true"); args = ap.parse_args()
    df, dr = read(DETAIL); uf, ur = read(REUSE); pf, pr = read(PAIRS); rf, rr = read(REVIEW)
    detail, reuse, reviews = index(dr, "evidence_id"), index(ur, "pathway_reuse_key"), index(rr, "review_id")
    prior = [p for p in RELAY.glob("module21a_relay_promotion_batch*.tsv") if p != AUDIT]
    cov = {}; audit = []
    for number, review_id, reuse_key in PACKET:
        eid = f"M21A-PAIR-EVID-{number}"; row = detail.get(eid); review = reviews.get(review_id)
        if row is None or row.get("confidence_tier") not in {"medium", "medium-high"} or not (tokens(row.get("evidence_layer", "")) & {"binding_activation", "ligand_receptor_binding_or_activation", "receptor_proximal_relay", "downstream_pathway_function"}) or row.get("pathway_reuse_key", "") != reuse_key: raise SystemExit(f"detail lineage mismatch: {eid}")
        if review is None or review.get("evidence_id") != eid or review.get("pathway_reuse_key", "") != reuse_key or review.get("source_locators") != row.get("source_locators") or review.get("review_status") not in {"reviewed_relay_candidate", "reviewed_binding_only", "reviewed_function_only"}: raise SystemExit(f"review lineage mismatch: {eid}")
        if reuse.get(reuse_key) is None or reuse[reuse_key].get("evidence_ids") != eid: raise SystemExit(f"reuse lineage mismatch: {eid}")
        matching = [p for p in pr if eid in tokens(p.get("module21a_evidence_ids", "")) and p.get("pair_key") == review.get("pair_key")]
        if len(matching) != 1: raise SystemExit(f"coverage mapping mismatch: {eid}")
        pair = matching[0]; cov[eid] = pair
        if pair.get("module21a_status") != review.get("review_status") or pair.get("module22a_status") != "no_terminal_tf_evidence": raise SystemExit(f"coverage or TF-boundary mismatch: {eid}")
        hits = [p.name for p in prior if any(x.get("evidence_id") == eid or x.get("pair_key") == review["pair_key"] for x in read(p)[1])]
        if hits: raise SystemExit(f"promotion overlap for {eid}: {hits}")
        audit.append({"evidence_id": eid, "review_id": review_id, "pair_key": review["pair_key"], "pathway_reuse_key": reuse_key, "previous_tier": row["confidence_tier"], "new_tier": "high", "source_locators": row["source_locators"], "decision_basis": "Worker audit and local-register lineage support exact-pair qualified-high evidence at the recorded layer; topology and TF metadata remain unchanged.", "upstream_lr_confidence_unchanged": "true", "terminal_tf_status_unchanged": "true", "sql_materialization": "false"})
    if not args.apply:
        print(json.dumps({"validated": len(audit), "apply": False, "evidence_ids": [x["evidence_id"] for x in audit]}, indent=2)); return
    for number, review_id, reuse_key in PACKET:
        eid = f"M21A-PAIR-EVID-{number}"; detail[eid]["confidence_tier"] = "high"; detail[eid]["limitations"] = once(detail[eid]["limitations"]); reviews[review_id]["confidence_tier"] = "high"; reviews[review_id]["curator_note"] = once(reviews[review_id]["curator_note"]); reuse[reuse_key]["validation_status"] = "promoted_high_batch112"; reuse[reuse_key]["limitations"] = once(reuse[reuse_key]["limitations"]); cov[eid]["curator_notes"] = once(cov[eid]["curator_notes"])
    write(DETAIL, df, dr); write(REUSE, uf, ur); write(PAIRS, pf, pr); write(REVIEW, rf, rr)
    fields = ["evidence_id", "review_id", "pair_key", "pathway_reuse_key", "previous_tier", "new_tier", "source_locators", "decision_basis", "upstream_lr_confidence_unchanged", "terminal_tf_status_unchanged", "sql_materialization"]
    write(AUDIT, fields, audit)
    SUMMARY.write_text(json.dumps({"promotion_id": "module21a-worker-confirmed-exact-pair-batch112-2026-09-02", "records_promoted": len(audit), "evidence_ids": [x["evidence_id"] for x in audit], "promotion_note": NOTE, "upstream_module20a_lr_confidence_changed": False, "terminal_tf_assignments_created": False, "sql_signaling_edges_created": False, "malformed_legacy_rows_touched": False}, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"validated": len(audit), "applied": len(audit), "evidence_ids": [x["evidence_id"] for x in audit]}, indent=2))


if __name__ == "__main__": main()
