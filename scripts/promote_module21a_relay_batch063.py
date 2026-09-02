#!/usr/bin/env python3
"""Promote independently verified receptor/channel/function packets."""

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
    RELAY / "module21a_pair_relay_review_batches050_051.tsv",
    RELAY / "module21a_pair_relay_review_batches052_053.tsv",
    RELAY / "module21a_pair_relay_review_batches054_055.tsv",
]
AUDIT = RELAY / "module21a_relay_promotion_batch063.tsv"
SUMMARY = RELAY / "module21a_relay_promotion_batch063_summary.json"

# Exact safe set from the independent 1161–1210 audit. Existing-high 1197 and
# all unresolved, binding-only, and malformed 1202–1207 rows are excluded.
PACKET = [
    ("M21A-PAIR-EVID-1162", "M20A-CELLCHAT-REMAINING-0704", "M21A-REUSE-0725"),
    ("M21A-PAIR-EVID-1163", "M20A-CELLCHAT-REMAINING-0705", "M21A-REUSE-0726"),
    ("M21A-PAIR-EVID-1164", "M20A-CELLCHAT-REMAINING-0706", "M21A-REUSE-0727"),
    ("M21A-PAIR-EVID-1165", "M20A-CELLCHAT-REMAINING-0707", "M21A-REUSE-0728"),
    ("M21A-PAIR-EVID-1166", "M20A-CELLCHAT-REMAINING-0708", "M21A-REUSE-0729"),
    ("M21A-PAIR-EVID-1167", "M20A-CELLCHAT-REMAINING-0709", "M21A-REUSE-0730"),
    ("M21A-PAIR-EVID-1168", "M20A-CELLCHAT-REMAINING-0710", "M21A-REUSE-0731"),
    ("M21A-PAIR-EVID-1169", "M20A-CELLCHAT-REMAINING-0711", "M21A-REUSE-0732"),
    ("M21A-PAIR-EVID-1170", "M20A-CELLCHAT-REMAINING-0712", "M21A-REUSE-0733"),
    ("M21A-PAIR-EVID-1171", "M20A-CELLCHAT-REMAINING-0713", "M21A-REUSE-0734"),
    ("M21A-PAIR-EVID-1172", "M20A-CELLCHAT-REMAINING-0714", "M21A-REUSE-0735"),
    ("M21A-PAIR-EVID-1173", "M20A-CELLCHAT-REMAINING-0715", "M21A-REUSE-0736"),
    ("M21A-PAIR-EVID-1174", "M20A-CELLCHAT-REMAINING-0716", "M21A-REUSE-0737"),
    ("M21A-PAIR-EVID-1175", "M20A-CELLCHAT-REMAINING-0717", "M21A-REUSE-0738"),
    ("M21A-PAIR-EVID-1176", "M20A-CELLCHAT-REMAINING-0718", "M21A-REUSE-0739"),
    ("M21A-PAIR-EVID-1178", "M20A-CELLCHAT-REMAINING-0720", "M21A-REUSE-0740"),
    ("M21A-PAIR-EVID-1180", "M20A-CELLCHAT-REMAINING-0722", "M21A-REUSE-0741"),
    ("M21A-PAIR-EVID-1182", "M20A-CELLCHAT-REMAINING-0741", "M21A-REUSE-0742"),
    ("M21A-PAIR-EVID-1183", "M20A-CELLCHAT-REMAINING-0742", "M21A-REUSE-0743"),
    ("M21A-PAIR-EVID-1185", "M20A-CELLCHAT-REMAINING-0744", "M21A-REUSE-0744"),
    ("M21A-PAIR-EVID-1186", "M20A-CELLCHAT-REMAINING-0745", "M21A-REUSE-0745"),
    ("M21A-PAIR-EVID-1190", "M20A-CELLCHAT-REMAINING-0749", "M21A-REUSE-0746"),
    ("M21A-PAIR-EVID-1193", "M20A-CELLCHAT-REMAINING-0752", "M21A-REUSE-0747"),
    ("M21A-PAIR-EVID-1194", "M20A-CELLCHAT-REMAINING-0753", "M21A-REUSE-0748"),
    ("M21A-PAIR-EVID-1196", "M20A-CELLCHAT-REMAINING-0755", "M21A-REUSE-0749"),
    ("M21A-PAIR-EVID-1198", "M20A-CELLCHAT-REMAINING-0757", "M21A-REUSE-0751"),
    ("M21A-PAIR-EVID-1199", "M20A-CELLCHAT-REMAINING-0758", "M21A-REUSE-0752"),
    ("M21A-PAIR-EVID-1200", "M20A-CELLCHAT-REMAINING-0759", "M21A-REUSE-0753"),
    ("M21A-PAIR-EVID-1201", "M20A-CELLCHAT-REMAINING-0760", "M21A-REUSE-0754"),
    ("M21A-PAIR-EVID-1208", "M20A-CELLCHAT-REMAINING-0767", "M21A-REUSE-0761"),
]

PROMOTION_NOTE = (
    "Module 21A receptor/channel promotion batch063 (2026-09-02): exact mature-ligand activation "
    "of the specified receptor complex or connexin function is raised to high at the supported "
    "receptor-proximal or downstream-function layer. Biosynthetic, vesicular-transport, and source "
    "labels remain separate context; complex composition, native assembly, localization, and model "
    "boundaries remain explicit, with no terminal-TF or SCI claim."
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
            or not row.get("evidence_layer")
        ):
            raise SystemExit(f"detail lineage mismatch: {evidence_id}")
        review = reviews.get(review_id)
        if (
            review is None
            or review.get("evidence_id") != evidence_id
            or review.get("pathway_reuse_key") != reuse_key
            or review.get("source_locators") != row.get("source_locators")
            or review.get("confidence_tier") not in {"medium", "medium-high"}
            or review.get("review_status") not in {"reviewed_relay_candidate", "reviewed_function_only"}
        ):
            raise SystemExit(f"review lineage mismatch: {evidence_id}")
        if reuse.get(reuse_key) is None or reuse[reuse_key].get("evidence_ids") != evidence_id:
            raise SystemExit(f"reuse lineage mismatch: {evidence_id}")
        if (
            coverage[evidence_id] is None
            or coverage[evidence_id].get("pair_key") != review.get("pair_key")
            or coverage[evidence_id].get("module21a_status") != review.get("review_status")
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
                "Exact mature-ligand receptor-complex or connexin function supports qualified-high "
                "promotion at the supported receptor-proximal/downstream-function layer; source "
                "processing and native assembly boundaries are unchanged."
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
        reuse[reuse_key]["validation_status"] = "promoted_high_batch063"
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
            "promotion_id": "module21a-receptor-channel-batch063-2026-09-02",
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
