#!/usr/bin/env python3
"""Promote the validated glutamate-receptor rows from the 1311–1360 audit."""

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
    RELAY / "module21a_pair_relay_review_batches058_059.tsv",
    RELAY / "module21a_pair_relay_review_batches060_061.tsv",
]
AUDIT = RELAY / "module21a_relay_promotion_batch064.tsv"
SUMMARY = RELAY / "module21a_relay_promotion_batch064_summary.json"

SAFE_IDS = [
    *range(1311, 1327),
    *range(1336, 1359),
]
PACKET = [(
    f"M21A-PAIR-EVID-{evidence_number}",
    f"M20A-CELLCHAT-REMAINING-{review_number}",
    f"M21A-REUSE-{reuse_number}",
) for evidence_number, review_number, reuse_number in [
    (1311, "0870", "0854"), (1312, "0871", "0855"), (1313, "0872", "0856"),
    (1314, "0873", "0857"), (1315, "0874", "0858"), (1316, "0875", "0859"),
    (1317, "0876", "0860"), (1318, "0877", "0861"), (1319, "0878", "0862"),
    (1320, "0879", "0863"), (1321, "0880", "0864"), (1322, "0881", "0865"),
    (1323, "0882", "0866"), (1324, "0883", "0867"), (1325, "0884", "0868"),
    (1326, "0885", "0869"), (1336, "0895", "0877"), (1337, "0896", "0878"),
    (1338, "0897", "0879"), (1339, "0898", "0880"), (1340, "0899", "0881"),
    (1341, "0900", "0882"), (1342, "0901", "0883"), (1343, "0902", "0884"),
    (1344, "0903", "0885"), (1345, "0904", "0886"), (1346, "0905", "0887"),
    (1347, "0906", "0888"), (1348, "0907", "0889"), (1349, "0908", "0890"),
    (1350, "0909", "0891"), (1351, "0910", "0892"), (1352, "0911", "0893"),
    (1353, "0912", "0894"), (1354, "0913", "0895"), (1355, "0914", "0896"),
    (1356, "0915", "0897"), (1357, "0916", "0898"), (1358, "0917", "0899"),
]]
assert len(PACKET) == len(SAFE_IDS) == 39

PROMOTION_NOTE = (
    "Module 21A glutamate-receptor promotion batch064 (2026-09-02): exact mature glutamate "
    "activation of the specified NMDA, metabotropic, AMPA, or kainate receptor row is raised "
    "to high at the validated receptor-proximal relay layer. Source-processing labels remain "
    "context only; exact receptor composition, model, species, assembly, and electrophysiology "
    "boundaries remain explicit, with no terminal-TF or SCI claim."
)


def read_tsv(path: Path):
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        return list(reader.fieldnames or []), list(reader)


def write_tsv(path: Path, fields, rows):
    with path.open("w", encoding="utf-8", newline="") as handle:
        csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n").writeheader()
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
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
        ) for evidence_id, _review_id, _reuse_key in PACKET
    }

    for evidence_id, review_id, reuse_key in PACKET:
        row = detail.get(evidence_id)
        if (
            row is None
            or row.get("confidence_tier") not in {"medium", "medium-high"}
            or row.get("pathway_reuse_key") != reuse_key
            or row.get("evidence_layer") != "receptor_proximal_relay"
        ):
            raise SystemExit(f"detail lineage mismatch: {evidence_id}")
        review = reviews.get(review_id)
        if (
            review is None
            or review.get("evidence_id") != evidence_id
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
                "Exact mature-glutamate receptor activation supports qualified-high promotion at "
                "the validated receptor-proximal layer; source-processing and native assembly "
                "boundaries are unchanged."
            ),
            "upstream_lr_confidence_unchanged": "true",
            "terminal_tf_status_unchanged": "true",
            "sql_materialization": "false",
        })

    if not args.apply:
        print(json.dumps({"validated": len(audit_rows), "apply": False,
                          "evidence_ids": [r["evidence_id"] for r in audit_rows]}, indent=2))
        return

    for evidence_id, review_id, reuse_key in PACKET:
        detail[evidence_id]["confidence_tier"] = "high"
        detail[evidence_id]["limitations"] = append_once(detail[evidence_id]["limitations"], PROMOTION_NOTE)
        review = reviews[review_id]
        review["confidence_tier"] = "high"
        review["curator_note"] = append_once(review["curator_note"], PROMOTION_NOTE)
        reuse[reuse_key]["validation_status"] = "promoted_high_batch064"
        reuse[reuse_key]["limitations"] = append_once(reuse[reuse_key]["limitations"], PROMOTION_NOTE)
        coverage[evidence_id]["curator_notes"] = append_once(coverage[evidence_id]["curator_notes"], PROMOTION_NOTE)

    write_tsv(DETAIL, detail_fields, detail_rows)
    for path, fields, rows in zip(REVIEW_FILES, review_fields, review_rows_by_file):
        write_tsv(path, fields, rows)
    write_tsv(REUSE, reuse_fields, reuse_rows)
    write_tsv(PAIRS, pair_fields, pair_rows)
    write_tsv(AUDIT, audit_fields, audit_rows)
    SUMMARY.write_text(json.dumps({
        "promotion_id": "module21a-glutamate-receptor-batch064-2026-09-02",
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
