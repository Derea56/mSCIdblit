#!/usr/bin/env python3
"""Promote fifteen validated Module 21A POMC/protease/function rows."""

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
    RELAY / "module21a_pair_relay_review_batches146_147_148_149_150_151.tsv",
    RELAY / "module21a_pair_relay_review_batches152_153_154_155.tsv",
]
PROMOTION_GLOB = "module21a_relay_promotion_batch*.tsv"
AUDIT = RELAY / "module21a_relay_promotion_batch095.tsv"
SUMMARY = RELAY / "module21a_relay_promotion_batch095_summary.json"

PACKET = [
    ("M21A-PAIR-EVID-3616", "M20A-EXT-2791", "M21A-REUSE-1785"),
    ("M21A-PAIR-EVID-3622", "M20A-EXT-2797", "M21A-REUSE-1786"),
    ("M21A-PAIR-EVID-3623", "M20A-EXT-2798", "M21A-REUSE-1787"),
    ("M21A-PAIR-EVID-3632", "M20A-EXT-2807", "M21A-REUSE-1788"),
    ("M21A-PAIR-EVID-3633", "M20A-EXT-2810", ""),
    ("M21A-PAIR-EVID-3634", "M20A-EXT-2811", ""),
    ("M21A-PAIR-EVID-3637", "M20A-EXT-2815", ""),
    ("M21A-PAIR-EVID-3638", "M20A-EXT-2823", "M21A-REUSE-1789"),
    ("M21A-PAIR-EVID-3639", "M20A-EXT-2824", "M21A-REUSE-1790"),
    ("M21A-PAIR-EVID-3643", "M20A-EXT-2828", "M21A-REUSE-1792"),
    ("M21A-PAIR-EVID-3645", "M20A-EXT-2832", ""),
    ("M21A-PAIR-EVID-3646", "M20A-EXT-2834", "M21A-REUSE-1793"),
    ("M21A-PAIR-EVID-3647", "M20A-EXT-2835", ""),
    ("M21A-PAIR-EVID-3658", "M20A-EXT-2846", "M21A-REUSE-1799"),
    ("M21A-PAIR-EVID-3659", "M20A-EXT-2847", ""),
]

PROMOTION_NOTE = (
    "Module 21A qualified-relay promotion batch095 (2026-09-02): exact pair-associated "
    "receptor-complex binding, receptor-proximal relay, enzyme/substrate processing, or "
    "bounded downstream function is raised to high at the validated layer. Processed POMC "
    "beta-endorphin, POSTN integrin complexes, PRL/PRLR-ERBB2 transactivation, PrP/Doppel-"
    "RPSA physical association, thrombin-THBD-PROC cofactor activation, PRSS2/PAR cleavage, "
    "PSAP uptake/function, PSEN1 gamma-secretase processing/assembly, PTGS2/ALOX5 pathway "
    "cross-talk, PTGS2/CAV1 association, precursor-versus-processed ligand, complex, "
    "isoform, species/model, assay, pathway, and no-direct-binding boundaries where recorded "
    "remain explicit. Existing Module 22A terminal-TF metadata is preserved unchanged; no "
    "new terminal-TF or SCI claim is created."
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


def layers(value: str) -> set[str]:
    return {item.strip() for item in value.split(";") if item.strip()}


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
    allowed_layers = {
        "ligand_receptor_binding_or_activation",
        "receptor_proximal_relay",
        "downstream_pathway_function",
    }
    allowed_statuses = {
        "reviewed_relay_candidate", "reviewed_binding_only", "reviewed_function_only",
    }

    audit_rows = []
    for evidence_id, review_id, reuse_key in PACKET:
        row = detail.get(evidence_id)
        review = reviews.get(review_id)
        pair = coverage[evidence_id]
        if (
            row is None
            or row.get("confidence_tier", "").strip() not in allowed_tiers
            or not layers(row.get("evidence_layer", "")) & allowed_layers
            or row.get("pathway_reuse_key", "") != reuse_key
        ):
            raise SystemExit(f"detail lineage mismatch: {evidence_id}")
        if (
            review is None
            or review.get("evidence_id") != evidence_id
            or review.get("pathway_reuse_key", "") != reuse_key
            or review.get("source_locators") != row.get("source_locators")
            or review.get("confidence_tier", "").strip() not in allowed_tiers
            or review.get("review_status") not in allowed_statuses
        ):
            raise SystemExit(f"review lineage mismatch: {evidence_id}")
        if reuse_key and (
            reuse.get(reuse_key) is None or reuse[reuse_key].get("evidence_ids") != evidence_id
        ):
            raise SystemExit(f"reuse lineage mismatch: {evidence_id}")
        if (
            pair is None
            or pair.get("pair_key") != review.get("pair_key")
            or pair.get("module21a_status") != review.get("review_status")
            or pair.get("module21a_evidence_ids") != evidence_id
            or pair.get("module22a_status") != "no_terminal_tf_evidence"
        ):
            raise SystemExit(f"coverage lineage or TF-boundary mismatch: {evidence_id}")
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
                "Exact receptor-complex binding, receptor-proximal relay, enzyme/substrate "
                "processing, or bounded downstream function supports qualified-high promotion; "
                "recorded topology and Module 22A TF metadata remain unchanged."
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
        if reuse_key:
            reuse[reuse_key]["validation_status"] = "promoted_high_batch095"
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
        "promotion_id": "module21a-pomc-protease-function-batch095-2026-09-02",
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
