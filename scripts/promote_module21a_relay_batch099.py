#!/usr/bin/env python3
"""Promote seven validated Module 21A ciliary/co-receptor/mucin rows."""

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
REVIEW_FILES = [RELAY / "module21a_pair_relay_review_batches162_163.tsv"]
PROMOTION_GLOB = "module21a_relay_promotion_batch*.tsv"
AUDIT = RELAY / "module21a_relay_promotion_batch099.tsv"
SUMMARY = RELAY / "module21a_relay_promotion_batch099_summary.json"

PACKET = [
    ("M21A-PAIR-EVID-3911", "M20A-EXT-3225", "M21A-REUSE-1874"),
    ("M21A-PAIR-EVID-3912", "M20A-EXT-3226", "M21A-REUSE-1875"),
    ("M21A-PAIR-EVID-3913", "M20A-EXT-3227", "M21A-REUSE-1876"),
    ("M21A-PAIR-EVID-3916", "M20A-EXT-3230", "M21A-REUSE-1877"),
    ("M21A-PAIR-EVID-3918", "M20A-EXT-3232", "M21A-REUSE-1879"),
]

PROMOTION_NOTE = (
    "Module 21A qualified-relay promotion batch099 (2026-09-02): exact pair-associated "
    "ciliary complex association, co-receptor relay, mucin-complex association, or bounded "
    "downstream function is raised to high at the validated layer. TCTN1/TMEM67 transition-"
    "zone association, TDGF1/Cripto-ACVR1B and ACVR1C co-receptor relays, TDGF1/GPC1 "
    "coreceptor function, TFF1/MUC5AC mucin complex, and TFF2/CXCR4 function, "
    "Nodal dependence, glycoform, processing, complex, species/model, assay, pathway, "
    "and no-direct-binding boundaries where recorded remain explicit. Existing Module 22A "
    "terminal-TF metadata is preserved unchanged; no new terminal-TF or SCI claim is created."
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


def tokens(value: str) -> set[str]:
    return {item.strip() for item in value.split(";") if item.strip()}


def layers(value: str) -> set[str]:
    return tokens(value)


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
    promotion_paths = [path for path in RELAY.glob(PROMOTION_GLOB) if path != AUDIT]
    allowed_tiers = {"medium", "medium-high"}
    allowed_layers = {
        "binding_or_complex_association",
        "ligand_receptor_binding_or_activation",
        "receptor_proximal_relay",
        "downstream_pathway_function",
    }
    allowed_statuses = {
        "reviewed_relay_candidate", "reviewed_binding_only", "reviewed_function_only",
    }

    audit_rows = []
    coverage = {}
    for evidence_id, review_id, reuse_key in PACKET:
        row = detail.get(evidence_id)
        review = reviews.get(review_id)
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
        if reuse.get(reuse_key) is None or reuse[reuse_key].get("evidence_ids") != evidence_id:
            raise SystemExit(f"reuse lineage mismatch: {evidence_id}")
        matching = [
            candidate for candidate in pair_rows
            if evidence_id in tokens(candidate.get("module21a_evidence_ids", ""))
            and candidate.get("pair_key") == review.get("pair_key")
        ]
        if len(matching) != 1:
            raise SystemExit(f"coverage mapping mismatch: {evidence_id} ({len(matching)} rows)")
        pair = matching[0]
        coverage[evidence_id] = pair
        if (
            pair.get("module21a_status") != review.get("review_status")
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
                "Exact ciliary or receptor-complex association, co-receptor relay, mucin "
                "complex, or bounded downstream function supports qualified-high promotion; "
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
        reuse[reuse_key]["validation_status"] = "promoted_high_batch099"
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
        "promotion_id": "module21a-ciliary-coreceptor-mucin-batch099-2026-09-02",
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
