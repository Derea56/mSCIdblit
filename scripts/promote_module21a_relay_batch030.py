#!/usr/bin/env python3
"""Promote eight bounded Module 21A GDF/GH/GPC3 packets."""

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
REVIEW_FILE = RELAY / "module21a_pair_relay_review_batches216_217.tsv"
AUDIT = RELAY / "module21a_relay_promotion_batch030.tsv"
SUMMARY = RELAY / "module21a_relay_promotion_batch030_summary.json"

PACKET = {
    "M21A-PAIR-EVID-5286": {
        "pair_key": "gdf9 bmpr2_tgfbr1", "reuse_key": "M21A-REUSE-2466", "review_id": "M20A-EXT-1800",
        "citations": "PMID:16603567", "review_status": "reviewed_relay_candidate",
        "basis": "BMPR2 blockade/gain-of-function and ALK5 knockdown support a GDF9-BMPR2/TGFBR1 receptor-complex relay and ovarian granulosa-cell function; receptor dependence rather than purified ternary structure is retained.",
    },
    "M21A-PAIR-EVID-5287": {
        "pair_key": "gdnf gfra2_ret", "reuse_key": "M21A-REUSE-2467", "review_id": "M20A-EXT-1804",
        "citations": "PMID:9608533; DOI:10.1006/mcne.1998.0667; PMID:31535977", "review_status": "reviewed_relay_candidate",
        "basis": "Chemical crosslinking, GFRalpha2/RET complex reconstitution, and ligand-dependent RET phosphorylation support qualified-high multicomponent GDNF-GFRalpha2-RET relay/function; GFRalpha2 is less efficient than GFRalpha1 and is not a direct GDNF-RET binary edge.",
    },
    "M21A-PAIR-EVID-5288": {
        "pair_key": "gh ghr", "reuse_key": "M21A-REUSE-2468", "review_id": "M20A-EXT-1806",
        "citations": "PMID:18096690", "review_status": "reviewed_relay_candidate",
        "basis": "Exact ligand-induced GHR dimer geometry with JAK2/STAT5 activation supports qualified-high GHR relay/function; preserve engineered dimer/antagonist and non-SCI model context.",
    },
    "M21A-PAIR-EVID-5290": {
        "pair_key": "ghrh ghrhr", "reuse_key": "M21A-REUSE-2470", "review_id": "M20A-EXT-1812",
        "citations": "PMID:12446584; DOI:10.1210/en.2002-220670", "review_status": "reviewed_relay_candidate",
        "basis": "Exact cloned-GHRHR stimulation and cAMP support qualified-high receptor-proximal Gs relay/function; heterologous receptor, pituitary, and GHSR-crosstalk context remains bounded.",
    },
    "M21A-PAIR-EVID-5291": {
        "pair_key": "ghrl ghsr", "reuse_key": "M21A-REUSE-2471", "review_id": "M20A-EXT-1823",
        "citations": "PMID:11087562; DOI:10.1021/jm0001727; PMID:14755130; DOI:10.1159/000076042; PMID:30149681", "review_status": "reviewed_relay_candidate",
        "basis": "Exact ghrelin-GHSR1A binding/activation with G-protein, calcium, ERK, and cellular outputs supports qualified-high GPCR relay/function; constitutive activity and coupling remain endocrine/neuronal/endothelial context dependent.",
    },
    "M21A-PAIR-EVID-5292": {
        "pair_key": "gip gipr", "reuse_key": "M21A-REUSE-2472", "review_id": "M20A-EXT-1833",
        "citations": "PMID:20693566; PMCID:PMC2952555; PMID:35192688; PMCID:PMC7612781", "review_status": "reviewed_relay_candidate",
        "basis": "Exact GIPR activation with cAMP/PI3K-AKT-AMPK signaling and human-adipocyte CREB/TORC2 function supports qualified-high relay/function; CREB requires insulin co-treatment and remains a context-specific downstream endpoint.",
    },
    "M21A-PAIR-EVID-5294": {
        "pair_key": "gnrh1 gnrhr", "reuse_key": "M21A-REUSE-2473", "review_id": "M20A-EXT-1929",
        "citations": "PMID:10766863; DOI:10.1074/jbc.275.16.12251; PMID:11750725; PMID:27569529", "review_status": "reviewed_relay_candidate",
        "basis": "Exact GNRHR stimulation with Gq/11-PLC/Ca2+/PKC relay and EGFR/Src/Ras-ERK transactivation supports qualified-high relay/function; pulse/dose/cell context and crosstalk boundaries remain explicit.",
    },
    "M21A-PAIR-EVID-5298": {
        "pair_key": "gpc3 unc5d", "reuse_key": "", "review_id": "M20A-EXT-1939",
        "citations": "PMID:36240740; DOI:10.1016/j.cell.2022.09.025", "review_status": "reviewed_binding_only",
        "required_layers": ("downstream_pathway_function",),
        "basis": "Structure/SPR/interface mutants and neuronal stripe/migration assays support qualified-high exact GPC3-UNC5D extracellular guidance-complex binding/function; no cytosolic adaptor or kinase relay is promoted.",
    },
}

PROMOTION_NOTE = "Module 21A relay/function promotion batch030 (2026-09-02): evidence tier raised to high for the exact, context-bounded packet; evidence-layer scope, upstream Module 20A LR confidence, terminal-TF status, and SCI transfer remain unchanged."


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
    review_fields, review_rows = read_tsv(REVIEW_FILE)
    detail = index(detail_rows, "evidence_id")
    reuse = index(reuse_rows, "pathway_reuse_key")
    reviews = index(review_rows, "review_id")

    for evidence_id, expected in PACKET.items():
        row = detail.get(evidence_id)
        if row is None or row.get("confidence_tier") != "medium-high":
            raise SystemExit(f"{evidence_id} missing or not medium-high")
        required_layers = expected.get("required_layers", ("receptor_proximal_relay", "downstream_pathway_function"))
        if not all(layer in row.get("evidence_layer", "") for layer in required_layers):
            raise SystemExit(f"{evidence_id} lacks required evidence layers")
        if row.get("pathway_reuse_key", "") != expected["reuse_key"] or row.get("source_locators") != expected["citations"]:
            raise SystemExit(f"detail lineage mismatch: {evidence_id}")
        review = reviews.get(expected["review_id"])
        if (review is None or review.get("evidence_id") != evidence_id or review.get("pair_key") != expected["pair_key"]
                or review.get("source_locators") != expected["citations"]
                or review.get("confidence_tier") != "medium-high"
                or review.get("review_status") != expected["review_status"]):
            raise SystemExit(f"review lineage mismatch: {evidence_id}")
        if expected["reuse_key"]:
            reuse_row = reuse.get(expected["reuse_key"])
            if reuse_row is None or reuse_row.get("evidence_ids") != evidence_id:
                raise SystemExit(f"reuse lineage mismatch: {evidence_id}")
        coverage = next((item for item in pair_rows if item.get("module21a_evidence_ids") == evidence_id), None)
        if (coverage is None or coverage.get("pair_key") != expected["pair_key"]
                or coverage.get("module21a_status") != expected["review_status"]):
            raise SystemExit(f"coverage lineage mismatch: {evidence_id}")

    audit_fields = ["evidence_id", "review_id", "pair_key", "pathway_reuse_key", "previous_tier", "new_tier", "source_locators", "decision_basis", "upstream_lr_confidence_unchanged", "terminal_tf_status_unchanged", "sql_materialization"]
    audit_rows = [{
        "evidence_id": evidence_id, "review_id": expected["review_id"], "pair_key": expected["pair_key"],
        "pathway_reuse_key": expected["reuse_key"], "previous_tier": detail[evidence_id]["confidence_tier"],
        "new_tier": "high", "source_locators": detail[evidence_id]["source_locators"],
        "decision_basis": expected["basis"], "upstream_lr_confidence_unchanged": "true",
        "terminal_tf_status_unchanged": "true", "sql_materialization": "false",
    } for evidence_id, expected in sorted(PACKET.items())]

    if not args.apply:
        print(json.dumps({"validated": len(audit_rows), "apply": False, "evidence_ids": sorted(PACKET)}, indent=2))
        return

    for evidence_id, expected in PACKET.items():
        row = detail[evidence_id]
        row["confidence_tier"] = "high"
        row["limitations"] = append_once(row["limitations"], PROMOTION_NOTE)
        review = reviews[expected["review_id"]]
        review["confidence_tier"] = "high"
        review["curator_note"] = append_once(review["curator_note"], PROMOTION_NOTE)
        if expected["reuse_key"]:
            reuse_row = reuse[expected["reuse_key"]]
            reuse_row["validation_status"] = "promoted_high_batch030"
            reuse_row["limitations"] = append_once(reuse_row["limitations"], PROMOTION_NOTE)
        coverage = next(item for item in pair_rows if item.get("module21a_evidence_ids") == evidence_id)
        coverage["curator_notes"] = append_once(coverage["curator_notes"], PROMOTION_NOTE)

    write_tsv(DETAIL, detail_fields, detail_rows)
    write_tsv(REVIEW_FILE, review_fields, review_rows)
    write_tsv(REUSE, reuse_fields, reuse_rows)
    write_tsv(PAIRS, pair_fields, pair_rows)
    write_tsv(AUDIT, audit_fields, audit_rows)
    SUMMARY.write_text(json.dumps({
        "promotion_id": "module21a-relay-function-batch030-2026-09-02",
        "records_promoted": len(audit_rows), "evidence_ids": sorted(PACKET),
        "promotion_note": PROMOTION_NOTE, "upstream_module20a_lr_confidence_changed": False,
        "terminal_tf_assignments_created": False, "sql_signaling_edges_created": False,
        "malformed_legacy_rows_touched": False,
    }, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"validated": len(audit_rows), "applied": len(audit_rows), "evidence_ids": sorted(PACKET)}, indent=2))


if __name__ == "__main__":
    main()
