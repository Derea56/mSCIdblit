#!/usr/bin/env python3
"""Promote the conservative, no-terminal-TF subset of Module 21A lane 4311-4360."""

from __future__ import annotations

import argparse
import csv
import glob
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RELAY = ROOT / "work" / "module21_relay"
DETAIL = RELAY / "module21a_pair_relay_evidence_detail.tsv"
REUSE = RELAY / "module21a_pathway_reuse_registry.tsv"
PAIRS = RELAY / "module21a_all_pair_relay_coverage.tsv"
REVIEW_FILES = [
    RELAY / "module21a_pair_relay_review_batches176_177.tsv",
    RELAY / "module21a_pair_relay_review_batches178_179.tsv",
]
PROMOTION_GLOB = "module21a_relay_promotion_batch*.tsv"
AUDIT = RELAY / "module21a_relay_promotion_batch105.tsv"
SUMMARY = RELAY / "module21a_relay_promotion_batch105_summary.json"

PACKET = [
    (4311, "M20A-LIANA-REMAINING-0161", "M21A-REUSE-2039"),
    (4313, "M20A-LIANA-REMAINING-0163", "M21A-REUSE-2041"),
    (4316, "M20A-LIANA-REMAINING-0166", "M21A-REUSE-2044"),
    (4317, "M20A-LIANA-REMAINING-0167", "M21A-REUSE-2045"),
    (4327, "M20A-LIANA-REMAINING-0177", "M21A-REUSE-2047"),
    (4329, "M20A-LIANA-REMAINING-0179", "M21A-REUSE-2049"),
    (4330, "M20A-LIANA-REMAINING-0180", "M21A-REUSE-2050"),
    (4331, "M20A-LIANA-REMAINING-0181", "M21A-REUSE-2051"),
    (4332, "M20A-LIANA-REMAINING-0182", "M21A-REUSE-2052"),
    (4333, "M20A-LIANA-REMAINING-0183", "M21A-REUSE-2053"),
    (4334, "M20A-LIANA-REMAINING-0184", "M21A-REUSE-2054"),
    (4336, "M20A-LIANA-REMAINING-0186", "M21A-REUSE-2055"),
    (4337, "M20A-LIANA-REMAINING-0187", "M21A-REUSE-2056"),
    (4338, "M20A-LIANA-REMAINING-0188", "M21A-REUSE-2057"),
    (4339, "M20A-LIANA-REMAINING-0189", "M21A-REUSE-2058"),
    (4341, "M20A-LIANA-REMAINING-0191", "M21A-REUSE-2060"),
    (4346, "M20A-LIANA-REMAINING-0196", "M21A-REUSE-2063"),
    (4348, "M20A-LIANA-REMAINING-0198", "M21A-REUSE-2064"),
    (4352, "M20A-LIANA-REMAINING-0202", "M21A-REUSE-2066"),
    (4353, "M20A-LIANA-REMAINING-0203", "M21A-REUSE-2067"),
]

PROMOTION_NOTE = (
    "Module 21A qualified-relay promotion batch105 (2026-09-02): exact cytokine, Notch, "
    "GPCR, TNFR, neurotrophin, PDGF, and Reelin receptor-complex/function evidence is raised "
    "to high at the validated layer. Receptor stoichiometry, ligand presentation, processing, "
    "co-receptor, isoform, oligomerization, species/model, assay, developmental, and no-SCI "
    "boundaries remain explicit. Existing Module 22A metadata is preserved unchanged; no new "
    "terminal-TF or SCI claim is created."
)


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
    out = {}
    for row in rows:
        value = row.get(key, "")
        if value and value in out:
            raise SystemExit(f"duplicate {key}: {value}")
        if value:
            out[value] = row
    return out


def tokens(value):
    return {x.strip() for x in value.split(";") if x.strip()}


def append_once(value, note):
    return value if note in value else f"{value} {note}".strip()


def prior_hits(evidence_id, pair_key, paths):
    hits = []
    for path in paths:
        _, rows = read_tsv(path)
        if any(r.get("evidence_id") == evidence_id or r.get("pair_key") == pair_key for r in rows):
            hits.append(path.name)
    return hits


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    detail_fields, detail_rows = read_tsv(DETAIL)
    reuse_fields, reuse_rows = read_tsv(REUSE)
    pair_fields, pair_rows = read_tsv(PAIRS)
    review_tables = [read_tsv(path) for path in REVIEW_FILES]
    reviews = index([r for _, rows in review_tables for r in rows], "review_id")
    detail = index(detail_rows, "evidence_id")
    reuse = index(reuse_rows, "pathway_reuse_key")
    prior = [p for p in RELAY.glob(PROMOTION_GLOB) if p != AUDIT]
    coverage, audit_rows = {}, []
    allowed_tiers = {"medium", "medium-high"}
    allowed_statuses = {"reviewed_relay_candidate", "reviewed_binding_only", "reviewed_function_only"}
    allowed_layers = {"binding_activation", "ligand_receptor_binding_or_activation", "receptor_proximal_relay", "downstream_pathway_function"}
    for number, review_id, reuse_key in PACKET:
        evidence_id = f"M21A-PAIR-EVID-{number}"
        row, review = detail.get(evidence_id), reviews.get(review_id)
        if row is None or row.get("confidence_tier") not in allowed_tiers or not (tokens(row.get("evidence_layer", "")) & allowed_layers) or row.get("pathway_reuse_key") != reuse_key:
            raise SystemExit(f"detail lineage mismatch: {evidence_id}")
        if review is None or review.get("evidence_id") != evidence_id or review.get("pathway_reuse_key") != reuse_key or review.get("source_locators") != row.get("source_locators") or review.get("review_status") not in allowed_statuses:
            raise SystemExit(f"review lineage mismatch: {evidence_id}")
        if reuse.get(reuse_key) is None or reuse[reuse_key].get("evidence_ids") != evidence_id:
            raise SystemExit(f"reuse lineage mismatch: {evidence_id}")
        matching = [p for p in pair_rows if evidence_id in tokens(p.get("module21a_evidence_ids", "")) and p.get("pair_key") == review.get("pair_key")]
        if len(matching) != 1:
            raise SystemExit(f"coverage mapping mismatch: {evidence_id}")
        pair = matching[0]
        coverage[evidence_id] = pair
        if pair.get("module21a_status") != review.get("review_status") or pair.get("module22a_status") != "no_terminal_tf_evidence":
            raise SystemExit(f"coverage or TF-boundary mismatch: {evidence_id}")
        hits = prior_hits(evidence_id, review["pair_key"], prior)
        if hits:
            raise SystemExit(f"promotion overlap for {evidence_id}: {hits}")
        audit_rows.append({"evidence_id": evidence_id, "review_id": review_id, "pair_key": review["pair_key"], "pathway_reuse_key": reuse_key, "previous_tier": row["confidence_tier"], "new_tier": "high", "source_locators": row["source_locators"], "decision_basis": "Worker audit and local-register lineage support exact pair-associated qualified-high function at the recorded layer; topology and TF metadata remain unchanged.", "upstream_lr_confidence_unchanged": "true", "terminal_tf_status_unchanged": "true", "sql_materialization": "false"})
    if not args.apply:
        print(json.dumps({"validated": len(audit_rows), "apply": False, "evidence_ids": [r["evidence_id"] for r in audit_rows]}, indent=2))
        return
    for number, review_id, reuse_key in PACKET:
        eid = f"M21A-PAIR-EVID-{number}"
        detail[eid]["confidence_tier"] = "high"
        detail[eid]["limitations"] = append_once(detail[eid]["limitations"], PROMOTION_NOTE)
        reviews[review_id]["confidence_tier"] = "high"
        reviews[review_id]["curator_note"] = append_once(reviews[review_id]["curator_note"], PROMOTION_NOTE)
        reuse[reuse_key]["validation_status"] = "promoted_high_batch105"
        reuse[reuse_key]["limitations"] = append_once(reuse[reuse_key]["limitations"], PROMOTION_NOTE)
        coverage[eid]["curator_notes"] = append_once(coverage[eid]["curator_notes"], PROMOTION_NOTE)
    write_tsv(DETAIL, detail_fields, detail_rows)
    for path, (fields, rows) in zip(REVIEW_FILES, review_tables): write_tsv(path, fields, rows)
    write_tsv(REUSE, reuse_fields, reuse_rows)
    write_tsv(PAIRS, pair_fields, pair_rows)
    audit_fields = ["evidence_id", "review_id", "pair_key", "pathway_reuse_key", "previous_tier", "new_tier", "source_locators", "decision_basis", "upstream_lr_confidence_unchanged", "terminal_tf_status_unchanged", "sql_materialization"]
    write_tsv(AUDIT, audit_fields, audit_rows)
    SUMMARY.write_text(json.dumps({"promotion_id": "module21a-worker-validated-cytokine-notch-gpcr-pdgf-reelin-batch105-2026-09-02", "records_promoted": len(audit_rows), "evidence_ids": [r["evidence_id"] for r in audit_rows], "promotion_note": PROMOTION_NOTE, "upstream_module20a_lr_confidence_changed": False, "terminal_tf_assignments_created": False, "sql_signaling_edges_created": False, "malformed_legacy_rows_touched": False}, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"validated": len(audit_rows), "applied": len(audit_rows), "evidence_ids": [r["evidence_id"] for r in audit_rows]}, indent=2))


if __name__ == "__main__":
    main()
