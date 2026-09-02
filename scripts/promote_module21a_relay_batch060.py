#!/usr/bin/env python3
"""Promote independently verified mature-GABA/GABAA receptor-complex packets."""

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
    RELAY / "module21a_pair_relay_review_batches042_043_044_045.tsv",
    RELAY / "module21a_pair_relay_review_batches046_047.tsv",
]
AUDIT = RELAY / "module21a_relay_promotion_batch060.tsv"
SUMMARY = RELAY / "module21a_relay_promotion_batch060_summary.json"

# (evidence_id, review_id, reuse_key), from the independent 961–1010 audit.
PACKET = [
    (f"M21A-PAIR-EVID-{evid}", f"M20A-CELLCHAT-REMAINING-{review:04d}", f"M21A-REUSE-{reuse:04d}")
    for evid, review, reuse in [
        (961, 503, 554), (962, 504, 555), (963, 505, 556), (964, 506, 557),
        (965, 507, 558), (966, 508, 559), (967, 509, 560), (968, 510, 561),
        (969, 511, 562), (970, 512, 563), (971, 513, 564), (972, 514, 565),
        (975, 517, 566), (976, 518, 567), (977, 519, 568), (978, 520, 569),
        (979, 521, 570), (980, 522, 571), (981, 523, 572), (982, 524, 573),
        (983, 525, 574), (984, 526, 575), (985, 527, 576), (986, 528, 577),
        (987, 529, 578), (988, 530, 579), (989, 531, 580), (992, 534, 581),
        (993, 535, 582), (994, 536, 583), (995, 537, 584), (996, 538, 585),
        (997, 539, 586), (998, 540, 587), (999, 541, 588), (1000, 542, 589),
        (1001, 543, 590), (1002, 544, 591), (1003, 545, 592), (1004, 546, 593),
        (1005, 547, 594), (1006, 548, 595), (1009, 551, 596), (1010, 552, 597),
    ]
]

PROMOTION_NOTE = (
    "Module 21A receptor-complex promotion batch060 (2026-09-02): mature GABA activation "
    "of the exact recombinant GABAA subunit complex is raised to high at the receptor-proximal "
    "channel/function layer. GAD1/SLC6A synthesis and transport remain separate source context; "
    "native abundance, stoichiometry, localization, ionic conditions, and model-specific outputs "
    "remain bounded, with no terminal-TF or SCI claim."
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

    for evidence_id, review_id, reuse_key in PACKET:
        row = detail.get(evidence_id)
        if (
            row is None
            or row.get("confidence_tier") not in {"medium", "medium-high"}
            or row.get("pathway_reuse_key") != reuse_key
            or "receptor_proximal_relay" not in row.get("evidence_layer", "")
            or "GABAA" not in row.get("pathway_branch", "")
        ):
            raise SystemExit(f"detail lineage mismatch: {evidence_id}")
        review = reviews.get(review_id)
        if (
            review is None
            or review.get("evidence_id") != evidence_id
            or not review.get("pair_key", "").startswith("gaba-gad1_slc6a")
            or "gabr_a" not in review.get("pair_key", "")
            or review.get("pathway_reuse_key") != reuse_key
            or review.get("source_locators") != row.get("source_locators")
            or review.get("confidence_tier") not in {"medium", "medium-high"}
            or review.get("review_status") != "reviewed_relay_candidate"
        ):
            raise SystemExit(f"review lineage mismatch: {evidence_id}")
        if reuse.get(reuse_key) is None or reuse[reuse_key].get("evidence_ids") != evidence_id:
            raise SystemExit(f"reuse lineage mismatch: {evidence_id}")
        if (
            coverage[evidence_id] is None
            or coverage[evidence_id].get("pair_key") != review.get("pair_key")
            or coverage[evidence_id].get("module21a_status") != "reviewed_relay_candidate"
        ):
            raise SystemExit(f"coverage lineage mismatch: {evidence_id}")

    audit_fields = [
        "evidence_id", "review_id", "pair_key", "pathway_reuse_key", "previous_tier",
        "new_tier", "source_locators", "decision_basis", "upstream_lr_confidence_unchanged",
        "terminal_tf_status_unchanged", "sql_materialization",
    ]
    audit_rows = []
    for evidence_id, review_id, reuse_key in PACKET:
        row = detail[evidence_id]
        audit_rows.append({
            "evidence_id": evidence_id,
            "review_id": review_id,
            "pair_key": reviews[review_id]["pair_key"],
            "pathway_reuse_key": reuse_key,
            "previous_tier": row["confidence_tier"],
            "new_tier": "high",
            "source_locators": row["source_locators"],
            "decision_basis": (
                "Exact mature-GABA activation of the specified GABAA receptor complex and "
                "receptor-proximal channel/function support qualified-high promotion; source "
                "synthesis/transport context and native assembly boundaries are unchanged."
            ),
            "upstream_lr_confidence_unchanged": "true",
            "terminal_tf_status_unchanged": "true",
            "sql_materialization": "false",
        })

    if not args.apply:
        print(json.dumps({"validated": len(audit_rows), "apply": False, "evidence_ids": [r["evidence_id"] for r in audit_rows]}, indent=2))
        return

    for evidence_id, review_id, reuse_key in PACKET:
        detail[evidence_id]["confidence_tier"] = "high"
        detail[evidence_id]["limitations"] = append_once(detail[evidence_id]["limitations"], PROMOTION_NOTE)
        review = reviews[review_id]
        review["confidence_tier"] = "high"
        review["curator_note"] = append_once(review["curator_note"], PROMOTION_NOTE)
        reuse[reuse_key]["validation_status"] = "promoted_high_batch060"
        reuse[reuse_key]["limitations"] = append_once(reuse[reuse_key]["limitations"], PROMOTION_NOTE)
        coverage[evidence_id]["curator_notes"] = append_once(coverage[evidence_id]["curator_notes"], PROMOTION_NOTE)

    write_tsv(DETAIL, detail_fields, detail_rows)
    for path, fields, rows in zip(REVIEW_FILES, review_fields, review_rows_by_file):
        write_tsv(path, fields, rows)
    write_tsv(REUSE, reuse_fields, reuse_rows)
    write_tsv(PAIRS, pair_fields, pair_rows)
    write_tsv(AUDIT, audit_fields, audit_rows)
    SUMMARY.write_text(
        json.dumps({
            "promotion_id": "module21a-receptor-complex-batch060-2026-09-02",
            "records_promoted": len(audit_rows),
            "evidence_ids": [r["evidence_id"] for r in audit_rows],
            "promotion_note": PROMOTION_NOTE,
            "upstream_module20a_lr_confidence_changed": False,
            "terminal_tf_assignments_created": False,
            "sql_signaling_edges_created": False,
            "malformed_legacy_rows_touched": False,
        }, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({"validated": len(audit_rows), "applied": len(audit_rows), "evidence_ids": [r["evidence_id"] for r in audit_rows]}, indent=2))


if __name__ == "__main__":
    main()
