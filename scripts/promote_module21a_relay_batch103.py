#!/usr/bin/env python3
"""Promote a locally revalidated Module 21A chemokine/Notch/Ephrin packet."""

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
    RELAY / "module21a_pair_relay_review_batches172_173.tsv",
    RELAY / "module21a_pair_relay_review_batches174_175.tsv",
]
PROMOTION_GLOB = "module21a_relay_promotion_batch*.tsv"
AUDIT = RELAY / "module21a_relay_promotion_batch103.tsv"
SUMMARY = RELAY / "module21a_relay_promotion_batch103_summary.json"

PACKET = [
    (4211, "M20A-LIANA-REMAINING-0057", "M21A-REUSE-1981"),
    (4212, "M20A-LIANA-REMAINING-0058", "M21A-REUSE-1982"),
    (4213, "M20A-LIANA-REMAINING-0059", "M21A-REUSE-1983"),
    (4215, "M20A-LIANA-REMAINING-0061", "M21A-REUSE-1984"),
    (4217, "M20A-LIANA-REMAINING-0065", "M21A-REUSE-1985"),
    (4218, "M20A-LIANA-REMAINING-0067", "M21A-REUSE-1986"),
    (4219, "M20A-LIANA-REMAINING-0068", "M21A-REUSE-1987"),
    (4220, "M20A-LIANA-REMAINING-0069", "M21A-REUSE-1988"),
    (4221, "M20A-LIANA-REMAINING-0070", "M21A-REUSE-1989"),
    (4222, "M20A-LIANA-REMAINING-0071", "M21A-REUSE-1990"),
    (4223, "M20A-LIANA-REMAINING-0072", "M21A-REUSE-1991"),
    (4226, "M20A-LIANA-REMAINING-0075", "M21A-REUSE-1993"),
    (4230, "M20A-LIANA-REMAINING-0079", "M21A-REUSE-1996"),
    (4236, "M20A-LIANA-REMAINING-0085", "M21A-REUSE-1997"),
    (4243, "M20A-LIANA-REMAINING-0092", "M21A-REUSE-1998"),
    (4244, "M20A-LIANA-REMAINING-0093", "M21A-REUSE-1999"),
    (4247, "M20A-LIANA-REMAINING-0096", "M21A-REUSE-2000"),
    (4248, "M20A-LIANA-REMAINING-0097", "M21A-REUSE-2001"),
    (4249, "M20A-LIANA-REMAINING-0098", "M21A-REUSE-2002"),
    (4255, "M20A-LIANA-REMAINING-0104", "M21A-REUSE-2004"),
    (4257, "M20A-LIANA-REMAINING-0106", "M21A-REUSE-2005"),
]

PROMOTION_NOTE = (
    "Module 21A qualified-relay promotion batch103 (2026-09-02): exact pair-associated "
    "chemokine GPCR activation, Notch ligand interaction, TLR/co-receptor function, or "
    "Eph/ephrin receptor-complex binding/function is raised to high at the validated layer. "
    "Chemokine species and receptor context, processed domains, membrane presentation, "
    "force/clustering, bidirectional signaling, complex stoichiometry, assay, model, and "
    "no-SCI boundaries remain explicit. Existing Module 22A metadata is preserved unchanged; "
    "no new terminal-TF or SCI claim is created."
)


def read_tsv(path: Path):
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        return list(reader.fieldnames or []), list(reader)


def write_tsv(path: Path, fields, rows):
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


def tokens(value: str) -> set[str]:
    return {item.strip() for item in value.split(";") if item.strip()}


def overlap(evidence_id, pair_key, paths):
    hits = []
    for path in paths:
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
    review_fields = [fields for fields, _ in review_tables]
    review_rows_by_file = [rows for _, rows in review_tables]
    detail = index(detail_rows, "evidence_id")
    reuse = index(reuse_rows, "pathway_reuse_key")
    reviews = index([row for rows in review_rows_by_file for row in rows], "review_id")
    prior = [path for path in RELAY.glob(PROMOTION_GLOB) if path != AUDIT]
    allowed_tiers = {"medium", "medium-high"}
    allowed_layers = {"binding_activation", "ligand_receptor_binding_or_activation",
                      "receptor_proximal_relay", "downstream_pathway_function"}
    allowed_statuses = {"reviewed_relay_candidate", "reviewed_binding_only", "reviewed_function_only"}
    audit_rows = []
    coverage = {}

    for number, review_id, reuse_key in PACKET:
        evidence_id = f"M21A-PAIR-EVID-{number}"
        row = detail.get(evidence_id)
        review = reviews.get(review_id)
        if (row is None or row.get("confidence_tier", "").strip() not in allowed_tiers
                or not (tokens(row.get("evidence_layer", "")) & allowed_layers)
                or row.get("pathway_reuse_key", "") != reuse_key):
            raise SystemExit(f"detail lineage mismatch: {evidence_id}")
        if (review is None or review.get("evidence_id") != evidence_id
                or review.get("pathway_reuse_key", "") != reuse_key
                or review.get("source_locators") != row.get("source_locators")
                or review.get("confidence_tier", "").strip() not in allowed_tiers
                or review.get("review_status") not in allowed_statuses):
            raise SystemExit(f"review lineage mismatch: {evidence_id}")
        if reuse.get(reuse_key) is None or reuse[reuse_key].get("evidence_ids") != evidence_id:
            raise SystemExit(f"reuse lineage mismatch: {evidence_id}")
        matching = [candidate for candidate in pair_rows
                    if evidence_id in tokens(candidate.get("module21a_evidence_ids", ""))
                    and candidate.get("pair_key") == review.get("pair_key")]
        if len(matching) != 1:
            raise SystemExit(f"coverage mapping mismatch: {evidence_id} ({len(matching)} rows)")
        pair = matching[0]
        coverage[evidence_id] = pair
        if (pair.get("module21a_status") != review.get("review_status")
                or pair.get("module22a_status") != "no_terminal_tf_evidence"):
            raise SystemExit(f"coverage or TF-boundary mismatch: {evidence_id}")
        hit = overlap(evidence_id, review["pair_key"], prior)
        if hit:
            raise SystemExit(f"promotion overlap for {evidence_id}: {', '.join(hit)}")
        audit_rows.append({
            "evidence_id": evidence_id, "review_id": review_id, "pair_key": review["pair_key"],
            "pathway_reuse_key": reuse_key, "previous_tier": row["confidence_tier"],
            "new_tier": "high", "source_locators": row["source_locators"],
            "decision_basis": "Local-register revalidation supports exact pair-associated qualified-high function at the recorded layer; topology and TF metadata remain unchanged.",
            "upstream_lr_confidence_unchanged": "true", "terminal_tf_status_unchanged": "true",
            "sql_materialization": "false",
        })

    if not args.apply:
        print(json.dumps({"validated": len(audit_rows), "apply": False,
                          "evidence_ids": [r["evidence_id"] for r in audit_rows]}, indent=2))
        return

    for number, review_id, reuse_key in PACKET:
        evidence_id = f"M21A-PAIR-EVID-{number}"
        detail[evidence_id]["confidence_tier"] = "high"
        detail[evidence_id]["limitations"] = append_once(detail[evidence_id]["limitations"], PROMOTION_NOTE)
        reviews[review_id]["confidence_tier"] = "high"
        reviews[review_id]["curator_note"] = append_once(reviews[review_id]["curator_note"], PROMOTION_NOTE)
        reuse[reuse_key]["validation_status"] = "promoted_high_batch103"
        reuse[reuse_key]["limitations"] = append_once(reuse[reuse_key]["limitations"], PROMOTION_NOTE)
        coverage[evidence_id]["curator_notes"] = append_once(coverage[evidence_id]["curator_notes"], PROMOTION_NOTE)

    write_tsv(DETAIL, detail_fields, detail_rows)
    for path, fields, rows in zip(REVIEW_FILES, review_fields, review_rows_by_file):
        write_tsv(path, fields, rows)
    write_tsv(REUSE, reuse_fields, reuse_rows)
    write_tsv(PAIRS, pair_fields, pair_rows)
    audit_fields = ["evidence_id", "review_id", "pair_key", "pathway_reuse_key", "previous_tier",
                    "new_tier", "source_locators", "decision_basis",
                    "upstream_lr_confidence_unchanged", "terminal_tf_status_unchanged",
                    "sql_materialization"]
    write_tsv(AUDIT, audit_fields, audit_rows)
    SUMMARY.write_text(json.dumps({
        "promotion_id": "module21a-local-revalidated-chemokine-notch-ephrin-batch103-2026-09-02",
        "records_promoted": len(audit_rows),
        "evidence_ids": [r["evidence_id"] for r in audit_rows],
        "promotion_note": PROMOTION_NOTE,
        "upstream_module20a_lr_confidence_changed": False,
        "terminal_tf_assignments_created": False,
        "sql_signaling_edges_created": False,
        "malformed_legacy_rows_touched": False,
    }, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"validated": len(audit_rows), "applied": len(audit_rows),
                      "evidence_ids": [r["evidence_id"] for r in audit_rows]}, indent=2))


if __name__ == "__main__":
    main()
