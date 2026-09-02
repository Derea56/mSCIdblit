#!/usr/bin/env python3
"""Promote a narrowly validated Module 21A relay/function evidence packet.

This is an audit-layer update.  It raises only the evidence tier for exact
receptor-complex relay/function records whose existing primary-source packet
was independently checked.  It does not raise the upstream Module 20A LR
confidence, create SQL SignalingEdge rows, assign terminal TFs, or alter
malformed legacy rows outside the selected packet.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RELAY = ROOT / "work" / "module21_relay"
DETAIL = RELAY / "module21a_pair_relay_evidence_detail.tsv"
REVIEW = RELAY / "module21a_pair_relay_review_batches194_195.tsv"
REUSE = RELAY / "module21a_pathway_reuse_registry.tsv"
PAIRS = RELAY / "module21a_all_pair_relay_coverage.tsv"
AUDIT = RELAY / "module21a_relay_promotion_batch001.tsv"
SUMMARY = RELAY / "module21a_relay_promotion_batch001_summary.json"

PACKET = {
    "M21A-PAIR-EVID-4743": {
        "pair_key": "il17a il17ra_il17rc",
        "reuse_key": "M21A-REUSE-2178",
        "review_id": "M20A-CELLCHAT-REMAINING-1290",
        "citations": "PMID:17911633; PMID:20554964; PMID:18097068; PMCID:PMC2821718",
        "basis": "IL-17A/IL17RA/IL17RC receptor-complex and receptor-dependent signaling are supported by binding, receptor reconstitution or blockade, Act1/SEFIR proximal evidence, and inflammatory response readouts.",
    },
    "M21A-PAIR-EVID-4751": {
        "pair_key": "il33 il1rl1_il1rap",
        "reuse_key": "M21A-REUSE-2185",
        "review_id": "M20A-CELLCHAT-REMAINING-1302",
        "citations": "PMID:19836339; PMID:23980170; PMID:27031441; DOI:10.1016/j.molcel.2009.08.025; DOI:10.1016/j.cyto.2016.03.013",
        "basis": "IL-33/ST2/IL1RAP complex assembly is supported by structural studies, and ST2 reconstitution with receptor blockade supports receptor-proximal inflammatory signaling.",
    },
}

PROMOTION_NOTE = "Module 21A relay/function promotion batch001 (2026-09-02): evidence tier raised from medium-high to high for the exact receptor-complex relay/function packet; upstream Module 20A LR confidence, terminal-TF status, and SCI transfer remain unchanged."


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


def validate(detail: dict[str, dict[str, str]], review: dict[str, dict[str, str]], reuse: dict[str, dict[str, str]], pairs: dict[str, dict[str, str]]) -> None:
    for evidence_id, expected in PACKET.items():
        d = detail.get(evidence_id)
        if d is None:
            raise SystemExit(f"missing detail record: {evidence_id}")
        if d["confidence_tier"] != "medium-high":
            raise SystemExit(f"{evidence_id} expected medium-high detail tier, found {d['confidence_tier']!r}")
        if expected["pair_key"] not in {d.get("pathway_branch", "")} and expected["pair_key"] != "":
            pass
        if "receptor_proximal_relay" not in d.get("evidence_layer", ""):
            raise SystemExit(f"{evidence_id} lacks receptor_proximal_relay layer")
        if "downstream_pathway_function" not in d.get("evidence_layer", ""):
            raise SystemExit(f"{evidence_id} lacks downstream_pathway_function layer")
        if expected["reuse_key"] != d.get("pathway_reuse_key"):
            raise SystemExit(f"{evidence_id} reuse-key mismatch")
        if expected["citations"] != d.get("source_locators"):
            raise SystemExit(f"{evidence_id} source-locator mismatch")

        rv = review.get(expected["review_id"])
        if rv is None or rv.get("evidence_id") != evidence_id:
            raise SystemExit(f"review/detail lineage mismatch: {evidence_id}")
        if rv.get("pair_key") != expected["pair_key"] or rv.get("confidence_tier") != "medium-high":
            raise SystemExit(f"review record not an exact medium-high match: {evidence_id}")

        ru = reuse.get(expected["reuse_key"])
        if ru is None or ru.get("evidence_ids") != evidence_id:
            raise SystemExit(f"reuse/detail lineage mismatch: {evidence_id}")

        pair = next((row for row in pairs.values() if row.get("module21a_evidence_ids") == evidence_id), None)
        if pair is None or pair.get("pair_key") != expected["pair_key"]:
            raise SystemExit(f"coverage/detail lineage mismatch: {evidence_id}")
        if pair.get("module21a_status") != "reviewed_relay_candidate":
            raise SystemExit(f"coverage row is not a relay candidate: {evidence_id}")


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
    pairs = {row.get("coverage_id", ""): row for row in pair_rows}
    validate(detail, review, reuse, pairs)

    audit_fields = [
        "evidence_id", "review_id", "pair_key", "pathway_reuse_key", "previous_tier",
        "new_tier", "source_locators", "decision_basis", "upstream_lr_confidence_unchanged",
        "terminal_tf_status_unchanged", "sql_materialization",
    ]
    audit_rows = []
    for evidence_id, expected in sorted(PACKET.items()):
        d = detail[evidence_id]
        audit_rows.append({
            "evidence_id": evidence_id,
            "review_id": expected["review_id"],
            "pair_key": expected["pair_key"],
            "pathway_reuse_key": expected["reuse_key"],
            "previous_tier": d["confidence_tier"],
            "new_tier": "high",
            "source_locators": d["source_locators"],
            "decision_basis": expected["basis"],
            "upstream_lr_confidence_unchanged": "true",
            "terminal_tf_status_unchanged": "true",
            "sql_materialization": "false",
        })

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
        ru["validation_status"] = "promoted_relay_function_high_batch001"
        ru["limitations"] = append_once(ru["limitations"], PROMOTION_NOTE)
        pair = next(row for row in pairs.values() if row.get("module21a_evidence_ids") == evidence_id)
        pair["curator_notes"] = append_once(pair["curator_notes"], PROMOTION_NOTE)

    write_tsv(DETAIL, detail_fields, detail_rows)
    write_tsv(REVIEW, review_fields, review_rows)
    write_tsv(REUSE, reuse_fields, reuse_rows)
    write_tsv(PAIRS, pair_fields, pair_rows)
    write_tsv(AUDIT, audit_fields, audit_rows)
    SUMMARY.write_text(json.dumps({
        "promotion_id": "module21a-relay-function-batch001-2026-09-02",
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
