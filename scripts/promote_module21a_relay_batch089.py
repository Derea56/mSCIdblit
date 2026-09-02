#!/usr/bin/env python3
"""Promote thirteen validated Module 21A integrin/processing relay rows."""

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
REVIEW_FILES = [RELAY / "module21a_pair_relay_review_batches134_135.tsv"]
PROMOTION_GLOB = "module21a_relay_promotion_batch*.tsv"
AUDIT = RELAY / "module21a_relay_promotion_batch089.tsv"
SUMMARY = RELAY / "module21a_relay_promotion_batch089_summary.json"

PACKET = [
    ("M21A-PAIR-EVID-3221", "M20A-EXT-2265", "M21A-REUSE-1650"),
    ("M21A-PAIR-EVID-3223", "M20A-EXT-2267", "M21A-REUSE-1651"),
    ("M21A-PAIR-EVID-3224", "M20A-EXT-2268", "M21A-REUSE-1652"),
    ("M21A-PAIR-EVID-3225", "M20A-EXT-2269", "M21A-REUSE-1653"),
    ("M21A-PAIR-EVID-3227", "M20A-EXT-2271", "M21A-REUSE-1654"),
    ("M21A-PAIR-EVID-3229", "M20A-EXT-2274", "M21A-REUSE-1655"),
    ("M21A-PAIR-EVID-3231", "M20A-EXT-2276", "M21A-REUSE-1656"),
    ("M21A-PAIR-EVID-3233", "M20A-EXT-2279", "M21A-REUSE-1657"),
    ("M21A-PAIR-EVID-3236", "M20A-EXT-2283", "M21A-REUSE-1659"),
    ("M21A-PAIR-EVID-3240", "M20A-EXT-2287", "M21A-REUSE-1660"),
    ("M21A-PAIR-EVID-3241", "M20A-EXT-2288", "M21A-REUSE-1661"),
    ("M21A-PAIR-EVID-3246", "M20A-EXT-2293", "M21A-REUSE-1662"),
    ("M21A-PAIR-EVID-3247", "M20A-EXT-2294", "M21A-REUSE-1663"),
]

PROMOTION_NOTE = (
    "Module 21A qualified-relay promotion batch089 (2026-09-02): exact pair-associated "
    "receptor-complex relay or bounded processing/function is raised to high at the "
    "validated layer. Integrin heterodimer, adhesion/cofactor, intracellular-adaptor, "
    "JUNO/IZUMO1, protease-processing, Klotho/FGFR1/FGF23, processed-kinin, HKa/Mac-1, "
    "ligand/material form, species/model, assay, pathway, and no-terminal-TF/SCI "
    "boundaries remain explicit; no unsupported isolated-subunit or universal "
    "ligand-receptor claim is made."
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


def promotion_overlap(evidence_id: str, pair_key: str, paths: list[Path]) -> list[str]:
    hits = []
    for path in paths:
        _, rows = read_tsv(path)
        if any(
            row.get("evidence_id") == evidence_id or row.get("pair_key") == pair_key
            for row in rows
        ):
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
    coverage = {
        evidence_id: next(
            (row for row in pair_rows if row.get("module21a_evidence_ids") == evidence_id), None
        )
        for evidence_id, _review_id, _reuse_key in PACKET
    }
    promotion_paths = [path for path in RELAY.glob(PROMOTION_GLOB) if path != AUDIT]
    allowed_tiers = {"medium", "medium-high"}
    allowed_layers = {"receptor_proximal_relay", "downstream_pathway_function"}
    allowed_statuses = {"reviewed_relay_candidate", "reviewed_function_only"}

    audit_rows = []
    for evidence_id, review_id, reuse_key in PACKET:
        row = detail.get(evidence_id)
        review = reviews.get(review_id)
        pair = coverage[evidence_id]
        if (
            row is None
            or row.get("confidence_tier") not in allowed_tiers
            or row.get("evidence_layer") not in allowed_layers
            or row.get("pathway_reuse_key") != reuse_key
        ):
            raise SystemExit(f"detail lineage mismatch: {evidence_id}")
        if (
            review is None
            or review.get("evidence_id") != evidence_id
            or review.get("pathway_reuse_key") != reuse_key
            or review.get("source_locators") != row.get("source_locators")
            or review.get("confidence_tier") not in allowed_tiers
            or review.get("review_status") not in allowed_statuses
        ):
            raise SystemExit(f"review lineage mismatch: {evidence_id}")
        if reuse.get(reuse_key) is None or reuse[reuse_key].get("evidence_ids") != evidence_id:
            raise SystemExit(f"reuse lineage mismatch: {evidence_id}")
        if (
            pair is None
            or pair.get("pair_key") != review.get("pair_key")
            or pair.get("module21a_status") != review.get("review_status")
            or pair.get("module21a_evidence_ids") != evidence_id
        ):
            raise SystemExit(f"coverage lineage mismatch: {evidence_id}")
        overlap = promotion_overlap(evidence_id, review["pair_key"], promotion_paths)
        if overlap:
            raise SystemExit(f"promotion overlap for {evidence_id}: {', '.join(overlap)}")
        audit_rows.append({
            "evidence_id": evidence_id,
            "review_id": review_id,
            "pair_key": review["pair_key"],
            "pathway_reuse_key": reuse_key,
            "previous_tier": row["confidence_tier"],
            "new_tier": "high",
            "source_locators": row["source_locators"],
            "decision_basis": (
                "Exact pair-associated receptor-complex relay or bounded processing/function "
                "supports qualified-high promotion; recorded topology and context boundaries "
                "remain unchanged."
            ),
            "upstream_lr_confidence_unchanged": "true",
            "terminal_tf_status_unchanged": "true",
            "sql_materialization": "false",
        })

    if not args.apply:
        print(json.dumps({
            "validated": len(audit_rows),
            "apply": False,
            "evidence_ids": [row["evidence_id"] for row in audit_rows],
        }, indent=2))
        return

    for evidence_id, review_id, reuse_key in PACKET:
        detail[evidence_id]["confidence_tier"] = "high"
        detail[evidence_id]["limitations"] = append_once(
            detail[evidence_id]["limitations"], PROMOTION_NOTE
        )
        reviews[review_id]["confidence_tier"] = "high"
        reviews[review_id]["curator_note"] = append_once(
            reviews[review_id]["curator_note"], PROMOTION_NOTE
        )
        reuse[reuse_key]["validation_status"] = "promoted_high_batch089"
        reuse[reuse_key]["limitations"] = append_once(
            reuse[reuse_key]["limitations"], PROMOTION_NOTE
        )
        coverage[evidence_id]["curator_notes"] = append_once(
            coverage[evidence_id]["curator_notes"], PROMOTION_NOTE
        )

    write_tsv(DETAIL, detail_fields, detail_rows)
    for path, fields, rows in zip(REVIEW_FILES, review_fields, review_rows_by_file):
        write_tsv(path, fields, rows)
    write_tsv(REUSE, reuse_fields, reuse_rows)
    write_tsv(PAIRS, pair_fields, pair_rows)
    audit_fields = [
        "evidence_id", "review_id", "pair_key", "pathway_reuse_key", "previous_tier",
        "new_tier", "source_locators", "decision_basis", "upstream_lr_confidence_unchanged",
        "terminal_tf_status_unchanged", "sql_materialization",
    ]
    write_tsv(AUDIT, audit_fields, audit_rows)
    SUMMARY.write_text(json.dumps({
        "promotion_id": "module21a-integrin-processing-relay-batch089-2026-09-02",
        "records_promoted": len(audit_rows),
        "evidence_ids": [row["evidence_id"] for row in audit_rows],
        "promotion_note": PROMOTION_NOTE,
        "upstream_module20a_lr_confidence_changed": False,
        "terminal_tf_assignments_created": False,
        "sql_signaling_edges_created": False,
        "malformed_legacy_rows_touched": False,
    }, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "validated": len(audit_rows),
        "applied": len(audit_rows),
        "evidence_ids": [row["evidence_id"] for row in audit_rows],
    }, indent=2))


if __name__ == "__main__":
    main()
