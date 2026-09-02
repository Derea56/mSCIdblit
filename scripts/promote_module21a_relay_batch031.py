#!/usr/bin/env python3
"""Promote seven bounded Module 21A receptor and coreceptor packets."""

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
AUDIT = RELAY / "module21a_relay_promotion_batch031.tsv"
SUMMARY = RELAY / "module21a_relay_promotion_batch031_summary.json"

PACKET = {
    "M21A-PAIR-EVID-5301": {
        "pair_key": "gpi1 amfr", "reuse_key": "M21A-REUSE-2476", "review_id": "M20A-EXT-1944",
        "citations": "PMID:10456327; PMID:21252914; PMID:17690101; PMID:24576828", "review_status": "reviewed_relay_candidate",
        "basis": "AMF/PGI engages AMFR/gp78 with receptor-dependent uptake, AKT/ERK signaling, and motility/survival outputs, supporting qualified-high relay/function for this unusual seven-TM RING-E3 receptor context.",
    },
    "M21A-PAIR-EVID-5304": {
        "pair_key": "grp grpr", "reuse_key": "M21A-REUSE-2478", "review_id": "M20A-EXT-1953",
        "citations": "PMID:10446156; PMID:7946967; DOI:10.1074/jbc.274.34.23901; DOI:10.1016/0898-6568(94)90089-2", "review_status": "reviewed_relay_candidate",
        "basis": "Exact GRPR calcium/PLC/PKC/MEK-MAPK relay with secretion and motility function supports qualified-high receptor relay/function; bombesin comparator and EGFR crosstalk remain bounded.",
    },
    "M21A-PAIR-EVID-5309": {
        "pair_key": "h2-ab1 cd4", "reuse_key": "M21A-REUSE-2482", "review_id": "M20A-EXT-1971",
        "citations": "PMID:29386113; PMCID:PMC5813697; PMID:26831112; PMID:8816805", "review_status": "reviewed_relay_candidate",
        "basis": "H2-Ab1-containing peptide-MHC-II/TCR-CD3/CD4 engagement with Lck signaling and T-cell function supports qualified-high composite coreceptor relay/function; the isolated H2-Ab1 chain is not promoted.",
    },
    "M21A-PAIR-EVID-5311": {
        "pair_key": "h2-k1 cd8a", "reuse_key": "M21A-REUSE-2483", "review_id": "M20A-EXT-1983",
        "citations": "PMID:8955273; PMID:9806633; PMID:8920857; DOI:10.1038/384577a0", "review_status": "reviewed_relay_candidate",
        "basis": "H2-K1-containing peptide-MHC-I/CD8alpha engagement with TCR-proximal Lck signaling and CTL function supports qualified-high bounded composite relay/function; peptide, allele, TCR, and CD8 dimer context remain mandatory.",
    },
    "M21A-PAIR-EVID-5315": {
        "pair_key": "h2-t23 cd8a", "reuse_key": "", "review_id": "M20A-EXT-1992",
        "citations": "PMID:31992596; PMCID:PMC7062157; PMID:15749886; PMID:12594948", "review_status": "reviewed_binding_only",
        "required_layers": ("downstream_pathway_function",),
        "basis": "SPR/recombinant binding and functional coreceptor modulation support qualified-high exact Qa-1b/H2-T23-CD8alpha-alpha binding/function; no canonical kinase relay or isolated CD8alpha edge is inferred.",
    },
    "M21A-PAIR-EVID-5317": {
        "pair_key": "hcrt hcrtr1", "reuse_key": "M21A-REUSE-2485", "review_id": "M20A-EXT-2010",
        "citations": "PMID:25656479; PMID:41256182; https://pubmed.ncbi.nlm.nih.gov/?term=orexin-A+OX1R+PLC+calcium", "review_status": "reviewed_relay_candidate",
        "basis": "Receptor-selective orexin-A pharmacology/conditional deletion with calcium/PLC/PKC and neuronal excitability supports qualified-high HCRTR1 GPCR relay/function; coupling remains cell-type and ligand dependent.",
    },
    "M21A-PAIR-EVID-5319": {
        "pair_key": "hgf cd44", "reuse_key": "M21A-REUSE-2487", "review_id": "M20A-EXT-2020",
        "citations": "PMID:12464636; PMID:26181364; PMID:20357818; PMID:11034601", "review_status": "reviewed_relay_candidate",
        "basis": "HGF binding, CD44v6/CD44-HS manipulation, Met/Gab1/AKT signaling, and motility support qualified-high isoform-specific HGF coreceptor relay/function; HGF can signal CD44-independently and downstream effectors remain context-specific.",
    },
}

PROMOTION_NOTE = "Module 21A relay/function promotion batch031 (2026-09-02): evidence tier raised to high for the exact, context-bounded packet; evidence-layer scope, upstream Module 20A LR confidence, terminal-TF status, and SCI transfer remain unchanged."


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
            reuse_row["validation_status"] = "promoted_high_batch031"
            reuse_row["limitations"] = append_once(reuse_row["limitations"], PROMOTION_NOTE)
        coverage = next(item for item in pair_rows if item.get("module21a_evidence_ids") == evidence_id)
        coverage["curator_notes"] = append_once(coverage["curator_notes"], PROMOTION_NOTE)

    write_tsv(DETAIL, detail_fields, detail_rows)
    write_tsv(REVIEW_FILE, review_fields, review_rows)
    write_tsv(REUSE, reuse_fields, reuse_rows)
    write_tsv(PAIRS, pair_fields, pair_rows)
    write_tsv(AUDIT, audit_fields, audit_rows)
    SUMMARY.write_text(json.dumps({
        "promotion_id": "module21a-relay-function-batch031-2026-09-02",
        "records_promoted": len(audit_rows), "evidence_ids": sorted(PACKET),
        "promotion_note": PROMOTION_NOTE, "upstream_module20a_lr_confidence_changed": False,
        "terminal_tf_assignments_created": False, "sql_signaling_edges_created": False,
        "malformed_legacy_rows_touched": False,
    }, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"validated": len(audit_rows), "applied": len(audit_rows), "evidence_ids": sorted(PACKET)}, indent=2))


if __name__ == "__main__":
    main()
