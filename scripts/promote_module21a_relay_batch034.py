#!/usr/bin/env python3
"""Promote nine bounded Module 21A interleukin receptor packets."""

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
REVIEW_FILES = [RELAY / "module21a_pair_relay_review_batches218_219.tsv", RELAY / "module21a_pair_relay_review_batches220_221.tsv"]
AUDIT = RELAY / "module21a_relay_promotion_batch034.tsv"
SUMMARY = RELAY / "module21a_relay_promotion_batch034_summary.json"

PACKET = {
    "M21A-PAIR-EVID-5360": ("il17a_il17f il17ra_il17rc", "M21A-REUSE-2510", "M20A-EXT-2159", "PMID:17911633;PMID:20554964;DOI:10.1038/s41586-022-05116-y", "IL-17A/F heterodimer, IL17RA/IL17RC complex, ACT1/SEFIR relay, and inflammatory function support qualified-high promotion; retain homodimer and stoichiometry caveats."),
    "M21A-PAIR-EVID-5361": ("il18 il18_il18r1_il18rap", "M21A-REUSE-2511", "M20A-EXT-2160", "PMID:24842757;PMID:25589075;PMID:19657352", "Exact IL-18/IL18R1/IL18RAP MyD88-dependent complex with MAPK/NF-kB/PI3K and NK function supports qualified-high promotion; preserve MDM and infection-context boundaries."),
    "M21A-PAIR-EVID-5362": ("il18 il18r1_il18rap", "M21A-REUSE-2512", "M20A-EXT-2162", "PMID:24842757;PMID:25589075;PMID:19657352", "The uppercase submitted label maps to the same exact IL18R1/IL18RAP complex and supports qualified-high relay/function; IL18RAP is accessory, not autonomous."),
    "M21A-PAIR-EVID-5366": ("il1f6 il1rap_il1rl2", "M21A-REUSE-2513", "M20A-EXT-2175", "PMID:29180446;PMCID:PMC3234937;PMID:28726542", "Processed IL-36alpha/IL1F6 binding, IL1RL2/IL1RAP recruitment, MyD88/MAPK/NF-kB, and epithelial function support qualified-high promotion; preserve N-terminal processing."),
    "M21A-PAIR-EVID-5367": ("il1f8 il1rap_il1rl2", "M21A-REUSE-2514", "M20A-EXT-2176", "PMID:29180446;PMCID:PMC3234937;PMID:33326792", "IL-36gamma/IL1F8 productive IL1RL2/IL1RAP complex and epithelial inflammatory function support qualified-high promotion; recombinant binding and infection-context limits remain."),
    "M21A-PAIR-EVID-5368": ("il1f9 il1rap_il1rl2", "M21A-REUSE-2515", "M20A-EXT-2179", "PMID:29180446;PMCID:PMC3234937;PMID:28726542", "IL-36beta/IL1F9 productive IL1RL2/IL1RAP complex and inflammatory function support qualified-high promotion; preserve processing and receptor-presentation context."),
    "M21A-PAIR-EVID-5371": ("il20 il20rb_il22ra1", "M21A-REUSE-2518", "M20A-EXT-2188", "PMID:31205408;PMID:23793061;PMCID:PMC6545341", "Exact IL-20 type-II IL22RA1/IL20RB proximity/perturbation and JAK/STAT epithelial function support qualified-high promotion; IL20RA/IL20RB is an alternative complex."),
    "M21A-PAIR-EVID-5372": ("il21 il21r_il2rg", "M21A-REUSE-2519", "M20A-EXT-2189", "PMID:17884812;PMCID:PMC2323680;PMCID:PMC3338166;PMID:22118527", "Exact IL-21/IL21R/IL2RG common-gamma complex with JAK1/JAK3 and lymphocyte function supports qualified-high promotion; STAT usage remains state-dependent."),
    "M21A-PAIR-EVID-5375": ("il34 ptprz1", "M21A-REUSE-2522", "M20A-EXT-2201", "PMID:23744080;PMCID:PMC3724651;DOI:10.1074/jbc.M112.442731;PMID:35288653", "Direct IL-34/PTPRZ1 binding with chondroitin-sulfate-dependent FAK/paxillin and cellular function supports qualified-high promotion; preserve glioblastoma/macrophage context and distinguish CSF1R."),
}

PROMOTION_NOTE = "Module 21A relay/function promotion batch034 (2026-09-02): evidence tier raised to high for the exact, context-bounded packet; evidence-layer scope, upstream Module 20A LR confidence, terminal-TF status, and SCI transfer remain unchanged."


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
    review_tables = [read_tsv(path) for path in REVIEW_FILES]
    review_fields = [fields for fields, _ in review_tables]
    review_rows_by_file = [rows for _, rows in review_tables]
    review_rows = [row for rows in review_rows_by_file for row in rows]
    detail, reuse, reviews = index(detail_rows, "evidence_id"), index(reuse_rows, "pathway_reuse_key"), index(review_rows, "review_id")
    for evidence_id, packet in PACKET.items():
        pair_key, reuse_key, review_id, citations, _basis = packet
        row = detail.get(evidence_id)
        if row is None or row.get("confidence_tier") != "medium-high" or row.get("pathway_reuse_key") != reuse_key or row.get("source_locators") != citations:
            raise SystemExit(f"detail lineage mismatch: {evidence_id}")
        if not all(layer in row.get("evidence_layer", "") for layer in ("receptor_proximal_relay", "downstream_pathway_function")):
            raise SystemExit(f"{evidence_id} lacks relay/function layers")
        review = reviews.get(review_id)
        if (review is None or review.get("evidence_id") != evidence_id or review.get("pair_key") != pair_key or review.get("source_locators") != citations or review.get("confidence_tier") != "medium-high" or review.get("review_status") != "reviewed_relay_candidate"):
            raise SystemExit(f"review lineage mismatch: {evidence_id}")
        if reuse.get(reuse_key) is None or reuse[reuse_key].get("evidence_ids") != evidence_id:
            raise SystemExit(f"reuse lineage mismatch: {evidence_id}")
        coverage = next((item for item in pair_rows if item.get("module21a_evidence_ids") == evidence_id), None)
        if coverage is None or coverage.get("pair_key") != pair_key or coverage.get("module21a_status") != "reviewed_relay_candidate":
            raise SystemExit(f"coverage lineage mismatch: {evidence_id}")
    audit_fields = ["evidence_id", "review_id", "pair_key", "pathway_reuse_key", "previous_tier", "new_tier", "source_locators", "decision_basis", "upstream_lr_confidence_unchanged", "terminal_tf_status_unchanged", "sql_materialization"]
    audit_rows = [{"evidence_id": eid, "review_id": p[2], "pair_key": p[0], "pathway_reuse_key": p[1], "previous_tier": detail[eid]["confidence_tier"], "new_tier": "high", "source_locators": detail[eid]["source_locators"], "decision_basis": p[4], "upstream_lr_confidence_unchanged": "true", "terminal_tf_status_unchanged": "true", "sql_materialization": "false"} for eid, p in sorted(PACKET.items())]
    if not args.apply:
        print(json.dumps({"validated": len(audit_rows), "apply": False, "evidence_ids": sorted(PACKET)}, indent=2))
        return
    for evidence_id, packet in PACKET.items():
        detail[evidence_id]["confidence_tier"] = "high"
        detail[evidence_id]["limitations"] = append_once(detail[evidence_id]["limitations"], PROMOTION_NOTE)
        reviews[packet[2]]["confidence_tier"] = "high"
        reviews[packet[2]]["curator_note"] = append_once(reviews[packet[2]]["curator_note"], PROMOTION_NOTE)
        reuse[packet[1]]["validation_status"] = "promoted_high_batch034"
        reuse[packet[1]]["limitations"] = append_once(reuse[packet[1]]["limitations"], PROMOTION_NOTE)
        coverage = next(item for item in pair_rows if item.get("module21a_evidence_ids") == evidence_id)
        coverage["curator_notes"] = append_once(coverage["curator_notes"], PROMOTION_NOTE)
    write_tsv(DETAIL, detail_fields, detail_rows)
    for path, fields, rows in zip(REVIEW_FILES, review_fields, review_rows_by_file):
        write_tsv(path, fields, rows)
    write_tsv(REUSE, reuse_fields, reuse_rows)
    write_tsv(PAIRS, pair_fields, pair_rows)
    write_tsv(AUDIT, audit_fields, audit_rows)
    SUMMARY.write_text(json.dumps({"promotion_id": "module21a-relay-function-batch034-2026-09-02", "records_promoted": len(audit_rows), "evidence_ids": sorted(PACKET), "promotion_note": PROMOTION_NOTE, "upstream_module20a_lr_confidence_changed": False, "terminal_tf_assignments_created": False, "sql_signaling_edges_created": False, "malformed_legacy_rows_touched": False}, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"validated": len(audit_rows), "applied": len(audit_rows), "evidence_ids": sorted(PACKET)}, indent=2))


if __name__ == "__main__":
    main()
