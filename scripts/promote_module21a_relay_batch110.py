#!/usr/bin/env python3
"""Promote the conservative exact-pair subset from Module 21A lanes 4711-4810."""

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
    RELAY / "module21a_pair_relay_review_batches194_195.tsv",
    RELAY / "module21a_pair_relay_review_batches196_197.tsv",
]
AUDIT = RELAY / "module21a_relay_promotion_batch110.tsv"
SUMMARY = RELAY / "module21a_relay_promotion_batch110_summary.json"

PACKET = [
    (4724, "M20A-CELLCHAT-REMAINING-0453", "M21A-REUSE-2169"),
    (4725, "M20A-CELLCHAT-REMAINING-0472", "M21A-REUSE-2170"),
    (4726, "M20A-CELLCHAT-REMAINING-0475", "M21A-REUSE-2171"),
    (4730, "M20A-CELLCHAT-REMAINING-0727", "M21A-REUSE-2173"),
    (4766, "M20A-CELLCHAT-REMAINING-1340", "M21A-REUSE-2198"),
    (4767, "M20A-CELLCHAT-REMAINING-1341", "M21A-REUSE-2199"),
    (4768, "M20A-CELLCHAT-REMAINING-1356", ""),
    (4771, "M20A-CELLCHAT-REMAINING-1461", "M21A-REUSE-2202"),
    (4772, "M20A-CELLCHAT-REMAINING-1470", "M21A-REUSE-2203"),
    (4781, "M20A-CELLCHAT-REMAINING-1594", "M21A-REUSE-2208"),
    (4782, "M20A-CELLCHAT-REMAINING-1670", ""),
    (4785, "M20A-CELLCHAT-REMAINING-1724", "M21A-REUSE-2211"),
    (4796, "M20A-CELLCHAT-REMAINING-1759", ""),
    (4798, "M20A-CELLCHAT-REMAINING-1761", "M21A-REUSE-2220"),
    (4803, "M20A-CELLCHAT-REMAINING-1767", "M21A-REUSE-2223"),
    (4805, "M20A-CELLCHAT-REMAINING-1769", "M21A-REUSE-2224"),
    (4809, "M20A-CELLCHAT-REMAINING-1773", "M21A-REUSE-2228"),
]

PROMOTION_NOTE = (
    "Module 21A qualified-relay promotion batch110 (2026-09-02): exact ErbB, BMP/activin, "
    "neurotrophin, checkpoint/adhesion, chemokine, VEGF, and WNT5B receptor or adhesion "
    "evidence is raised to high only at the recorded supported layer. Ligand processing, "
    "receptor-complex, co-receptor, isoform, partial-agonist, glycoform/GAG, membrane "
    "geometry, heterologous-model, species, assay, and no-SCI boundaries remain explicit; "
    "no terminal-TF claim or SQL signaling edge is created."
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
    return {item.strip() for item in value.split(";") if item.strip()}


def append_once(value, note):
    return value if note in value else f"{value} {note}".strip()


def prior_hits(evidence_id, pair_key):
    hits = []
    for path in RELAY.glob("module21a_relay_promotion_batch*.tsv"):
        if path == AUDIT:
            continue
        _, rows = read_tsv(path)
        if any(row.get("evidence_id") == evidence_id or row.get("pair_key") == pair_key for row in rows):
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
    reviews = index([row for _, rows in review_tables for row in rows], "review_id")
    detail = index(detail_rows, "evidence_id")
    reuse = index(reuse_rows, "pathway_reuse_key")
    coverage = {}
    audit_rows = []
    allowed_tiers = {"medium", "medium-high"}
    allowed_statuses = {"reviewed_relay_candidate", "reviewed_binding_only", "reviewed_function_only"}
    allowed_layers = {"binding_activation", "ligand_receptor_binding_or_activation", "receptor_proximal_relay", "downstream_pathway_function"}

    for number, review_id, reuse_key in PACKET:
        evidence_id = f"M21A-PAIR-EVID-{number}"
        row, review = detail.get(evidence_id), reviews.get(review_id)
        if row is None or row.get("confidence_tier") not in allowed_tiers or not (tokens(row.get("evidence_layer", "")) & allowed_layers) or row.get("pathway_reuse_key", "") != reuse_key:
            raise SystemExit(f"detail lineage mismatch: {evidence_id}")
        if review is None or review.get("evidence_id") != evidence_id or review.get("pathway_reuse_key", "") != reuse_key or review.get("source_locators") != row.get("source_locators") or review.get("review_status") not in allowed_statuses:
            raise SystemExit(f"review lineage mismatch: {evidence_id}")
        if reuse_key and (reuse.get(reuse_key) is None or reuse[reuse_key].get("evidence_ids") != evidence_id):
            raise SystemExit(f"reuse lineage mismatch: {evidence_id}")
        matching = [pair for pair in pair_rows if evidence_id in tokens(pair.get("module21a_evidence_ids", "")) and pair.get("pair_key") == review.get("pair_key")]
        if len(matching) != 1:
            raise SystemExit(f"coverage mapping mismatch: {evidence_id}")
        pair = matching[0]
        coverage[evidence_id] = pair
        if pair.get("module21a_status") != review.get("review_status") or pair.get("module22a_status") != "no_terminal_tf_evidence":
            raise SystemExit(f"coverage or TF-boundary mismatch: {evidence_id}")
        hits = prior_hits(evidence_id, review["pair_key"])
        if hits:
            raise SystemExit(f"promotion overlap for {evidence_id}: {hits}")
        audit_rows.append({
            "evidence_id": evidence_id,
            "review_id": review_id,
            "pair_key": review["pair_key"],
            "pathway_reuse_key": reuse_key,
            "previous_tier": row["confidence_tier"],
            "new_tier": "high",
            "source_locators": row["source_locators"],
            "decision_basis": "Local-register lineage supports exact-pair qualified-high evidence at the recorded layer; molecular form, topology, context, and TF boundaries remain unchanged.",
            "upstream_lr_confidence_unchanged": "true",
            "terminal_tf_status_unchanged": "true",
            "sql_materialization": "false",
        })

    if not args.apply:
        print(json.dumps({"validated": len(audit_rows), "apply": False, "evidence_ids": [row["evidence_id"] for row in audit_rows]}, indent=2))
        return

    for number, review_id, reuse_key in PACKET:
        evidence_id = f"M21A-PAIR-EVID-{number}"
        detail[evidence_id]["confidence_tier"] = "high"
        detail[evidence_id]["limitations"] = append_once(detail[evidence_id]["limitations"], PROMOTION_NOTE)
        reviews[review_id]["confidence_tier"] = "high"
        reviews[review_id]["curator_note"] = append_once(reviews[review_id]["curator_note"], PROMOTION_NOTE)
        if reuse_key:
            reuse[reuse_key]["validation_status"] = "promoted_high_batch110"
            reuse[reuse_key]["limitations"] = append_once(reuse[reuse_key]["limitations"], PROMOTION_NOTE)
        coverage[evidence_id]["curator_notes"] = append_once(coverage[evidence_id]["curator_notes"], PROMOTION_NOTE)

    write_tsv(DETAIL, detail_fields, detail_rows)
    for path, (fields, rows) in zip(REVIEW_FILES, review_tables):
        write_tsv(path, fields, rows)
    write_tsv(REUSE, reuse_fields, reuse_rows)
    write_tsv(PAIRS, pair_fields, pair_rows)
    audit_fields = ["evidence_id", "review_id", "pair_key", "pathway_reuse_key", "previous_tier", "new_tier", "source_locators", "decision_basis", "upstream_lr_confidence_unchanged", "terminal_tf_status_unchanged", "sql_materialization"]
    write_tsv(AUDIT, audit_fields, audit_rows)
    SUMMARY.write_text(json.dumps({
        "promotion_id": "module21a-local-register-exact-pair-batch110-2026-09-02",
        "records_promoted": len(audit_rows),
        "evidence_ids": [row["evidence_id"] for row in audit_rows],
        "promotion_note": PROMOTION_NOTE,
        "upstream_module20a_lr_confidence_changed": False,
        "terminal_tf_assignments_created": False,
        "sql_signaling_edges_created": False,
        "malformed_legacy_rows_touched": False,
    }, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"validated": len(audit_rows), "applied": len(audit_rows), "evidence_ids": [row["evidence_id"] for row in audit_rows]}, indent=2))


if __name__ == "__main__":
    main()
