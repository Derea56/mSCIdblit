#!/usr/bin/env python3
"""Promote six bounded Module 21A cadherin/FGFR/coreceptor packets."""

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
AUDIT = RELAY / "module21a_relay_promotion_batch024.tsv"
SUMMARY = RELAY / "module21a_relay_promotion_batch024_summary.json"

PACKET = {
    "M21A-PAIR-EVID-5166": {
        "pair_key": "fat4 dchs1", "reuse_key": "M21A-REUSE-2419", "review_id": "M20A-EXT-1621",
        "review_file": RELAY / "module21a_pair_relay_review_batches210_211.tsv",
        "citations": "PMID:25355906; PMID:26116666; PMID:28826487",
        "basis": "FAT4-DCHS1 heterophilic adhesion-complex evidence and mouse developmental perturbation support qualified-high atypical cadherin receptor-complex and tissue-polarity function; YAP1 remains an effector/coactivator rather than a finalized TF.",
    },
    "M21A-PAIR-EVID-5173": {
        "pair_key": "fgf11 fgfr1", "reuse_key": "M21A-REUSE-2421", "review_id": "M20A-EXT-1651",
        "review_file": RELAY / "module21a_pair_relay_review_batches212_213.tsv",
        "citations": "PMID:37342898; DOI:10.1096/fj.202300324R",
        "basis": "Recombinant FGF11/FHF11 binding to FGFR1, receptor activation/internalization, and anti-apoptotic output support qualified-high exact receptor binding/activation; unconventional secretion and recombinant/cell context remain explicit.",
    },
    "M21A-PAIR-EVID-5174": {
        "pair_key": "fgf12 fgfr1", "reuse_key": "M21A-REUSE-2422", "review_id": "M20A-EXT-1653",
        "review_file": RELAY / "module21a_pair_relay_review_batches212_213.tsv",
        "citations": "PMID:37342898; DOI:10.1096/fj.202300324R",
        "basis": "Recombinant FGF12/FHF12 binding to FGFR1, receptor activation/internalization, and anti-apoptotic output support qualified-high exact receptor binding/activation; no unique intracellular adaptor or TF is inferred.",
    },
    "M21A-PAIR-EVID-5175": {
        "pair_key": "fgf13 fgfr1", "reuse_key": "M21A-REUSE-2423", "review_id": "M20A-EXT-1656",
        "review_file": RELAY / "module21a_pair_relay_review_batches212_213.tsv",
        "citations": "PMID:37342898; DOI:10.1096/fj.202300324R",
        "basis": "Recombinant FGF13/FHF13 binding to FGFR1, receptor activation/internalization, and anti-apoptotic output support qualified-high receptor-proximal activation; endogenous secretion and tissue relevance remain limited.",
    },
    "M21A-PAIR-EVID-5176": {
        "pair_key": "fgf14 fgfr1", "reuse_key": "M21A-REUSE-2424", "review_id": "M20A-EXT-1662",
        "review_file": RELAY / "module21a_pair_relay_review_batches212_213.tsv",
        "citations": "PMID:37342898; DOI:10.1096/fj.202300324R",
        "basis": "Recombinant FGF14/FHF14 binding to FGFR1, receptor activation/internalization, and anti-apoptotic output support qualified-high exact receptor activation; extracellular activity is not generalized to the predominantly intracellular neuronal FHF context.",
    },
    "M21A-PAIR-EVID-5179": {
        "pair_key": "fgf2 nrp1", "reuse_key": "M21A-REUSE-2425", "review_id": "M20A-EXT-1669",
        "review_file": RELAY / "module21a_pair_relay_review_batches212_213.tsv",
        "citations": "PMID:39704408; PMCID:PMC11858877; DOI:10.1021/acschembio.4c00475",
        "basis": "FGF2 proximity labeling, GAG/heparin dependence, NRP1 depletion, and FGFR-associated signaling support qualified-high coreceptor-supported function in A549 cells; autonomous FGF2-NRP1 binary binding is not claimed.",
    },
}

PROMOTION_NOTE = "Module 21A relay/function promotion batch024 (2026-09-02): evidence tier raised to high for the exact, context-bounded packet; evidence-layer scope, upstream Module 20A LR confidence, terminal-TF status, and SCI transfer remain unchanged."


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
    review_sets = {}
    for review_file in {expected["review_file"] for expected in PACKET.values()}:
        fields, rows = read_tsv(review_file)
        review_sets[review_file] = (fields, rows, index(rows, "review_id"))
    detail = index(detail_rows, "evidence_id")
    reuse = index(reuse_rows, "pathway_reuse_key")

    for evidence_id, expected in PACKET.items():
        row = detail.get(evidence_id)
        if row is None or row.get("confidence_tier") != "medium-high":
            raise SystemExit(f"{evidence_id} missing or not medium-high")
        if not all(layer in row.get("evidence_layer", "") for layer in ("receptor_proximal_relay", "downstream_pathway_function")):
            raise SystemExit(f"{evidence_id} lacks relay/function layers")
        if row.get("pathway_reuse_key") != expected["reuse_key"] or row.get("source_locators") != expected["citations"]:
            raise SystemExit(f"detail lineage mismatch: {evidence_id}")
        _, _, reviews = review_sets[expected["review_file"]]
        review = reviews.get(expected["review_id"])
        if (review is None or review.get("evidence_id") != evidence_id or review.get("pair_key") != expected["pair_key"]
                or review.get("source_locators") != expected["citations"]
                or review.get("confidence_tier") != "medium-high"
                or review.get("review_status") != "reviewed_relay_candidate"):
            raise SystemExit(f"review lineage mismatch: {evidence_id}")
        reuse_row = reuse.get(expected["reuse_key"])
        if reuse_row is None or reuse_row.get("evidence_ids") != evidence_id:
            raise SystemExit(f"reuse lineage mismatch: {evidence_id}")
        coverage = next((item for item in pair_rows if item.get("module21a_evidence_ids") == evidence_id), None)
        if (coverage is None or coverage.get("pair_key") != expected["pair_key"]
                or coverage.get("module21a_status") != "reviewed_relay_candidate"):
            raise SystemExit(f"coverage lineage mismatch: {evidence_id}")

    audit_fields = ["evidence_id", "review_id", "pair_key", "pathway_reuse_key", "previous_tier", "new_tier", "source_locators", "decision_basis", "upstream_lr_confidence_unchanged", "terminal_tf_status_unchanged", "sql_materialization"]
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
        row = detail[evidence_id]
        row["confidence_tier"] = "high"
        row["limitations"] = append_once(row["limitations"], PROMOTION_NOTE)
        _, _, reviews = review_sets[expected["review_file"]]
        review = reviews[expected["review_id"]]
        review["confidence_tier"] = "high"
        review["curator_note"] = append_once(review["curator_note"], PROMOTION_NOTE)
        reuse_row = reuse[expected["reuse_key"]]
        reuse_row["validation_status"] = "promoted_high_batch024"
        reuse_row["limitations"] = append_once(reuse_row["limitations"], PROMOTION_NOTE)
        coverage = next(item for item in pair_rows if item.get("module21a_evidence_ids") == evidence_id)
        coverage["curator_notes"] = append_once(coverage["curator_notes"], PROMOTION_NOTE)

    write_tsv(DETAIL, detail_fields, detail_rows)
    for review_file, (fields, rows, _) in review_sets.items():
        write_tsv(review_file, fields, rows)
    write_tsv(REUSE, reuse_fields, reuse_rows)
    write_tsv(PAIRS, pair_fields, pair_rows)
    write_tsv(AUDIT, audit_fields, audit_rows)
    SUMMARY.write_text(json.dumps({
        "promotion_id": "module21a-relay-function-batch024-2026-09-02",
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
