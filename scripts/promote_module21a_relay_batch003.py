#!/usr/bin/env python3
"""Promote a narrowly validated third Module 21A relay/function packet."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RELAY = ROOT / "work" / "module21_relay"
DETAIL = RELAY / "module21a_pair_relay_evidence_detail.tsv"
REVIEW = RELAY / "module21a_pair_relay_review_batches196_197.tsv"
REUSE = RELAY / "module21a_pathway_reuse_registry.tsv"
PAIRS = RELAY / "module21a_all_pair_relay_coverage.tsv"
AUDIT = RELAY / "module21a_relay_promotion_batch003.tsv"
SUMMARY = RELAY / "module21a_relay_promotion_batch003_summary.json"

PACKET = {
    "M21A-PAIR-EVID-4775": {
        "pair_key": "pdgfb pdgfra",
        "reuse_key": "M21A-REUSE-2204",
        "review_id": "M20A-CELLCHAT-REMAINING-1568",
        "citations": "PMID:7679113; PMID:11331881; PMID:27856617; PMID:1318305; PMID:7923614; PMID:7486687",
        "basis": "Purified or heterologous receptor binding, PDGF-BB-dependent PDGFRA activation, and downstream ERK/Akt/PLC-gamma and cell-response assays support the exact PDGF-BB-PDGFRA relay/function record.",
    },
    "M21A-PAIR-EVID-4780": {
        "pair_key": "pgf flt1",
        "reuse_key": "M21A-REUSE-2207",
        "review_id": "M20A-CELLCHAT-REMAINING-1590",
        "citations": "PMID:7929268; PMID:12796773; DOI:10.1074/jbc.273.35.22272; DOI:10.1074/jbc.271.6.3154",
        "basis": "PlGF-FLT1 binding, FLT1 phosphorylation, receptor cross-talk, and endothelial/vascular functional assays support the exact receptor-proximal relay/function record.",
    },
    "M21A-PAIR-EVID-4786": {
        "pair_key": "tgfa egfr",
        "reuse_key": "M21A-REUSE-2212",
        "review_id": "M20A-CELLCHAT-REMAINING-1736",
        "citations": "PMID:1524218; PMID:2302227; PMID:1572907; PMID:26091170; DOI:10.1016/0006-291X(90)90853-F",
        "basis": "TGF-alpha-EGFR binding, EGFR tyrosine-phosphorylation/trafficking, kinase dependence, and growth-factor response assays support the exact receptor-proximal relay/function record.",
    },
}

PROMOTION_NOTE = "Module 21A relay/function promotion batch003 (2026-09-02): evidence tier raised from medium-high to high for the exact receptor-complex relay/function packet; upstream Module 20A LR confidence, terminal-TF status, and SCI transfer remain unchanged."


def read_tsv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        return list(reader.fieldnames or []), list(reader)


def write_tsv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def append_once(value: str, note: str) -> str:
    return value if note in value else f"{value} {note}".strip()


def index_unique(rows: list[dict[str, str]], key: str, label: str) -> dict[str, dict[str, str]]:
    result: dict[str, dict[str, str]] = {}
    for row in rows:
        value = row.get(key, "")
        if value in result and value:
            raise SystemExit(f"duplicate {label}: {value}")
        if value:
            result[value] = row
    return result


def validate(detail, review, reuse, pairs) -> None:
    for evidence_id, expected in PACKET.items():
        d = detail.get(evidence_id)
        if d is None:
            raise SystemExit(f"missing detail record: {evidence_id}")
        if d.get("confidence_tier") != "medium-high":
            raise SystemExit(f"{evidence_id} expected medium-high detail tier, found {d.get('confidence_tier')!r}")
        for layer in ("receptor_proximal_relay", "downstream_pathway_function"):
            if layer not in d.get("evidence_layer", ""):
                raise SystemExit(f"{evidence_id} lacks {layer} layer")
        if d.get("pathway_reuse_key") != expected["reuse_key"] or d.get("source_locators") != expected["citations"]:
            raise SystemExit(f"detail lineage mismatch: {evidence_id}")
        rv = review.get(expected["review_id"])
        if rv is None or rv.get("evidence_id") != evidence_id or rv.get("pair_key") != expected["pair_key"]:
            raise SystemExit(f"review/detail lineage mismatch: {evidence_id}")
        if rv.get("confidence_tier") != "medium-high" or rv.get("review_status") != "reviewed_relay_candidate":
            raise SystemExit(f"review record is not an exact medium-high relay candidate: {evidence_id}")
        ru = reuse.get(expected["reuse_key"])
        if ru is None or ru.get("evidence_ids") != evidence_id:
            raise SystemExit(f"reuse/detail lineage mismatch: {evidence_id}")
        pair = next((row for row in pairs if row.get("module21a_evidence_ids") == evidence_id), None)
        if pair is None or pair.get("pair_key") != expected["pair_key"] or pair.get("module21a_status") != "reviewed_relay_candidate":
            raise SystemExit(f"coverage/detail lineage mismatch: {evidence_id}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="write the validated promotion")
    args = parser.parse_args()
    detail_fields, detail_rows = read_tsv(DETAIL)
    review_fields, review_rows = read_tsv(REVIEW)
    reuse_fields, reuse_rows = read_tsv(REUSE)
    pair_fields, pair_rows = read_tsv(PAIRS)
    detail = index_unique(detail_rows, "evidence_id", "evidence ID")
    review = index_unique(review_rows, "review_id", "review ID")
    reuse = index_unique(reuse_rows, "pathway_reuse_key", "reuse key")
    validate(detail, review, reuse, pair_rows)

    audit_fields = [
        "evidence_id", "review_id", "pair_key", "pathway_reuse_key", "previous_tier",
        "new_tier", "source_locators", "decision_basis", "upstream_lr_confidence_unchanged",
        "terminal_tf_status_unchanged", "sql_materialization",
    ]
    audit_rows = [{
        "evidence_id": evidence_id,
        "review_id": expected["review_id"],
        "pair_key": expected["pair_key"],
        "pathway_reuse_key": expected["reuse_key"],
        "previous_tier": detail[evidence_id]["confidence_tier"],
        "new_tier": "high",
        "source_locators": detail[evidence_id]["source_locators"],
        "decision_basis": expected["basis"],
        "upstream_lr_confidence_unchanged": "true",
        "terminal_tf_status_unchanged": "true",
        "sql_materialization": "false",
    } for evidence_id, expected in sorted(PACKET.items())]

    if not args.apply:
        print(json.dumps({"validated": len(audit_rows), "apply": False, "evidence_ids": sorted(PACKET)}, indent=2))
        return

    for evidence_id, expected in PACKET.items():
        d = detail[evidence_id]
        d["confidence_tier"] = "high"
        d["limitations"] = append_once(d["limitations"], PROMOTION_NOTE)
        rv = review[expected["review_id"]]
        rv["confidence_tier"] = "high"
        rv["curator_note"] = append_once(rv["curator_note"], PROMOTION_NOTE)
        ru = reuse[expected["reuse_key"]]
        ru["validation_status"] = "promoted_relay_function_high_batch003"
        ru["limitations"] = append_once(ru["limitations"], PROMOTION_NOTE)
        pair = next(row for row in pair_rows if row.get("module21a_evidence_ids") == evidence_id)
        pair["curator_notes"] = append_once(pair["curator_notes"], PROMOTION_NOTE)

    write_tsv(DETAIL, detail_fields, detail_rows)
    write_tsv(REVIEW, review_fields, review_rows)
    write_tsv(REUSE, reuse_fields, reuse_rows)
    write_tsv(PAIRS, pair_fields, pair_rows)
    write_tsv(AUDIT, audit_fields, audit_rows)
    SUMMARY.write_text(json.dumps({
        "promotion_id": "module21a-relay-function-batch003-2026-09-02",
        "records_promoted": len(audit_rows),
        "evidence_ids": sorted(PACKET),
        "promotion_note": PROMOTION_NOTE,
        "upstream_module20a_lr_confidence_changed": False,
        "terminal_tf_assignments_created": False,
        "sql_signaling_edges_created": False,
        "malformed_legacy_rows_touched": False,
    }, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"validated": len(audit_rows), "applied": len(audit_rows), "evidence_ids": sorted(PACKET)}, indent=2))


if __name__ == "__main__":
    main()
