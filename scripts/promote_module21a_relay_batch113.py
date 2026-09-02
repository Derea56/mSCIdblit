#!/usr/bin/env python3
"""Promote a conservative exact-pair subset from Module 21A lanes 5011-5210."""

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
    RELAY / "module21a_pair_relay_review_batches206_207.tsv",
    RELAY / "module21a_pair_relay_review_batches208_209.tsv",
    RELAY / "module21a_pair_relay_review_batches210_211.tsv",
    RELAY / "module21a_pair_relay_review_batches212_213.tsv",
]
AUDIT = RELAY / "module21a_relay_promotion_batch113.tsv"
SUMMARY = RELAY / "module21a_relay_promotion_batch113_summary.json"
PACKET = [
    (5030, "M20A-EXT-1385", ""),
    (5033, "M20A-EXT-1388", ""),
    (5059, "M20A-EXT-1458", ""),
    (5060, "M20A-EXT-1459", ""),
    (5067, "M20A-EXT-1468", ""),
    (5071, "M20A-EXT-1472", ""),
    (5087, "M20A-EXT-1500", "M21A-REUSE-2386"),
    (5122, "M20A-EXT-1577", "M21A-REUSE-2404"),
    (5152, "M20A-EXT-1607", "M21A-REUSE-2415"),
    (5153, "M20A-EXT-1608", "M21A-REUSE-2416"),
    (5182, "M20A-EXT-1675", "M21A-REUSE-2427"),
    (5193, "M20A-EXT-1698", ""),
    (5194, "M20A-EXT-1699", "M21A-REUSE-2431"),
    (5197, "M20A-EXT-1702", ""),
    (5206, "M20A-EXT-1711", "M21A-REUSE-2434"),
]
NOTE = (
    "Module 21A qualified-relay promotion batch113 (2026-09-02): exact adhesion, "
    "checkpoint, Hedgehog-complex, endothelin, coagulation, apoptotic-complex, FGF, "
    "LAG3, FLT3, and fibronectin-associated evidence is raised to high only at the "
    "recorded supported layer. Binding-only, coreceptor, ligand-form, complex, "
    "species/model, assay, and no-SCI boundaries remain explicit; no terminal-TF claim "
    "or SQL signaling edge is created."
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
    df, dr = read(DETAIL); uf, ur = read(REUSE); pf, pr = read(PAIRS)
    review_tables = [read(path) for path in REVIEW_FILES]
    reviews = index([row for _, rows in review_tables for row in rows], "review_id")
    detail, reuse = index(dr, "evidence_id"), index(ur, "pathway_reuse_key")
    cov, audit = {}, []
    for number, review_id, reuse_key in PACKET:
        eid = f"M21A-PAIR-EVID-{number}"; row = detail.get(eid); review = reviews.get(review_id)
        if row is None or row.get("confidence_tier") not in {"medium", "medium-high"} or not (tokens(row.get("evidence_layer", "")) & {"binding_activation", "ligand_receptor_binding_or_activation", "receptor_proximal_relay", "downstream_pathway_function"}) or row.get("pathway_reuse_key", "") != reuse_key: raise SystemExit(f"detail lineage mismatch: {eid}")
        if review is None or review.get("evidence_id") != eid or review.get("pathway_reuse_key", "") != reuse_key or review.get("source_locators") != row.get("source_locators") or review.get("review_status") not in {"reviewed_relay_candidate", "reviewed_binding_only", "reviewed_function_only"}: raise SystemExit(f"review lineage mismatch: {eid}")
        if reuse_key and (reuse.get(reuse_key) is None or reuse[reuse_key].get("evidence_ids") != eid): raise SystemExit(f"reuse lineage mismatch: {eid}")
        matching = [p for p in pr if eid in tokens(p.get("module21a_evidence_ids", "")) and p.get("pair_key") == review.get("pair_key")]
        if len(matching) != 1: raise SystemExit(f"coverage mapping mismatch: {eid}")
        pair = matching[0]; cov[eid] = pair
        if pair.get("module21a_status") != review.get("review_status") or pair.get("module22a_status") != "no_terminal_tf_evidence": raise SystemExit(f"coverage or TF-boundary mismatch: {eid}")
        hits = []
        for path in RELAY.glob("module21a_relay_promotion_batch*.tsv"):
            if path == AUDIT: continue
            if any(x.get("evidence_id") == eid or x.get("pair_key") == review["pair_key"] for x in read(path)[1]): hits.append(path.name)
        if hits: raise SystemExit(f"promotion overlap for {eid}: {hits}")
        audit.append({"evidence_id": eid, "review_id": review_id, "pair_key": review["pair_key"], "pathway_reuse_key": reuse_key, "previous_tier": row["confidence_tier"], "new_tier": "high", "source_locators": row["source_locators"], "decision_basis": "Local-register lineage supports exact-pair qualified-high evidence at the recorded layer; molecular form, topology, context, and TF boundaries remain unchanged.", "upstream_lr_confidence_unchanged": "true", "terminal_tf_status_unchanged": "true", "sql_materialization": "false"})
    if not args.apply:
        print(json.dumps({"validated": len(audit), "apply": False, "evidence_ids": [x["evidence_id"] for x in audit]}, indent=2)); return
    for number, review_id, reuse_key in PACKET:
        eid = f"M21A-PAIR-EVID-{number}"; detail[eid]["confidence_tier"] = "high"; detail[eid]["limitations"] = once(detail[eid]["limitations"]); reviews[review_id]["confidence_tier"] = "high"; reviews[review_id]["curator_note"] = once(reviews[review_id]["curator_note"])
        if reuse_key: reuse[reuse_key]["validation_status"] = "promoted_high_batch113"; reuse[reuse_key]["limitations"] = once(reuse[reuse_key]["limitations"])
        cov[eid]["curator_notes"] = once(cov[eid]["curator_notes"])
    write(DETAIL, df, dr); write(REUSE, uf, ur); write(PAIRS, pf, pr)
    for path, (fields, rows) in zip(REVIEW_FILES, review_tables): write(path, fields, rows)
    fields = ["evidence_id", "review_id", "pair_key", "pathway_reuse_key", "previous_tier", "new_tier", "source_locators", "decision_basis", "upstream_lr_confidence_unchanged", "terminal_tf_status_unchanged", "sql_materialization"]
    write(AUDIT, fields, audit)
    SUMMARY.write_text(json.dumps({"promotion_id": "module21a-local-register-exact-pair-batch113-2026-09-02", "records_promoted": len(audit), "evidence_ids": [x["evidence_id"] for x in audit], "promotion_note": NOTE, "upstream_module20a_lr_confidence_changed": False, "terminal_tf_assignments_created": False, "sql_signaling_edges_created": False, "malformed_legacy_rows_touched": False}, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"validated": len(audit), "applied": len(audit), "evidence_ids": [x["evidence_id"] for x in audit]}, indent=2))


if __name__ == "__main__": main()
