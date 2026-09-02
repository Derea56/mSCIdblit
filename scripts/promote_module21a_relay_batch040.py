#!/usr/bin/env python3
"""Promote eleven bounded Module 21A neurotrophin, netrin, and OSM packets."""

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
REVIEW = RELAY / "module21a_pair_relay_review_batches224_225.tsv"
AUDIT = RELAY / "module21a_relay_promotion_batch040.tsv"
SUMMARY = RELAY / "module21a_relay_promotion_batch040_summary.json"

PACKET = {
    "M21A-PAIR-EVID-5480": ("ntf3 ntrk2", "M21A-REUSE-2607", "M20A-EXT-2629", "PMID:1649702;PMCID:PMC2710095;PMID:8752100", "Direct NT-3/TrkB activation, receptor autophosphorylation, Ras-MAPK, and context-dependent neuronal/mitogenic output support qualified-high promotion; preserve weaker NT-3 efficacy at TrkB and isoform/engineered-cell limits."),
    "M21A-PAIR-EVID-5482": ("ntf5 ntrk2", "M21A-REUSE-2609", "M20A-EXT-2632", "PMID:10486198;PMCID:PMC6488875;PMID:1649702", "Direct NT-4/5/TrkB activation with PLCgamma/MAPK and neuronal synaptic/survival outputs support qualified-high promotion; preserve NT-4/5 nomenclature and TrkB isoform/slice context."),
    "M21A-PAIR-EVID-5483": ("ntn1 mcam", "M21A-REUSE-2610", "M20A-EXT-2634", "PMCID:PMC4349246;PMCID:PMC10157725", "Exact netrin-1/MCAM-CD146 binding with G-alpha-i/Gab1-Akt-mTOR/ERK endothelial relay/function supports qualified-high promotion; MCAM is an adhesion/signaling receptor rather than a canonical RTK."),
    "M21A-PAIR-EVID-5484": ("ntn1 neo1", "M21A-REUSE-2611", "M20A-EXT-2635", "PMCID:PMC4369087;PMCID:PMC2172498;https://reactome.org/content/detail/R-HSA-374689", "Exact netrin-1/NEO1 binding and FAK/Src-associated axon-guidance function support qualified-high promotion; preserve NEO1/DCC-family complex and splice architecture."),
    "M21A-PAIR-EVID-5485": ("ntn1 unc5d", "M21A-REUSE-2612", "M20A-EXT-2636", "PMID:23778138;PMCID:PMC3696554;https://www.jci.org/articles/view/65988", "Netrin-1 suppression of UNC5D cleavage and dependence-receptor survival output supports qualified-high promotion; this is a cleavage switch, not a universal kinase relay, and E2F1 remains a downstream fragment-associated readout."),
    "M21A-PAIR-EVID-5488": ("ntng1 lrrc4c", "M21A-REUSE-2614", "M20A-EXT-2641", "PMID:17785411;PMCID:PMC6528442;PMCID:PMC3713730", "Exact NTNG1/LRRC4C-NGL1 trans-synaptic adhesion and excitatory synapse function support qualified-high promotion; preserve neuronal lamina context and no conventional kinase/TF claim."),
    "M21A-PAIR-EVID-5489": ("ntng2 lrrc4", "M21A-REUSE-2615", "M20A-EXT-2642", "PMID:17785411;PMCID:PMC3713730;PMID:19467332", "Exact NTNG2/LRRC4-NGL2 adhesion and pathway-specific excitatory synapse function support qualified-high promotion; do not transfer to LRRC4C/NTNG1 or LRRC4B/PTPR complexes."),
    "M21A-PAIR-EVID-5490": ("nts ntsr1", "M21A-REUSE-2616", "M20A-EXT-2647", "PMID:12360476;PMID:21725197;PMID:31614143", "NTS/NTSR1 Gq/11-PLC/PKC and ERK relay with context-dependent EGFR/HER2 transactivation/function supports qualified-high promotion; preserve SORT1 and cancer-cell context."),
    "M21A-PAIR-EVID-5491": ("nts ntsr2", "M21A-REUSE-2617", "M20A-EXT-2648", "PMID:15361549;PMID:31223654;PMCID:PMC6584543", "Exact NTSR2 internalization-dependent ERK and nociceptive function support qualified-high promotion; preserve low-affinity receptor, analog, species, and sortilin-availability caveats."),
    "M21A-PAIR-EVID-5497": ("osm il6st_lifr", "M21A-REUSE-2619", "M20A-EXT-2664", "PMID:1324910;PMID:29511087;DOI:10.1074/jbc.RA118.001920;PMID:10854424", "Assembled OSM/gp130/LIFR composite JAK/STAT with ancillary ERK/PI3K function supports qualified-high promotion; preserve human OSM/gp130-OSMR alternative and murine OSMR bias, not binary OSM-LIFR binding."),
    "M21A-PAIR-EVID-5498": ("osm il6st_osmr", "M21A-REUSE-2620", "M20A-EXT-2665", "PMID:17148439;PMID:27539849;PMID:17881458", "Exact OSM/gp130/OSMR composite JAK/STAT and Shc1/SHP2-Ras-ERK remodeling/epithelial function support qualified-high promotion; preserve species/cell context and possible gp130/LIFR branch."),
}

FUNCTION_ONLY = {"M21A-PAIR-EVID-5488", "M21A-PAIR-EVID-5489"}

PROMOTION_NOTE = "Module 21A relay/function promotion batch040 (2026-09-02): evidence tier raised to high for the exact, context-bounded packet; evidence-layer scope, upstream Module 20A LR confidence, terminal-TF status, and SCI transfer remain unchanged."


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
    review_fields, review_rows = read_tsv(REVIEW)
    detail, reuse, reviews = index(detail_rows, "evidence_id"), index(reuse_rows, "pathway_reuse_key"), index(review_rows, "review_id")
    for evidence_id, packet in PACKET.items():
        pair_key, reuse_key, review_id, citations, _basis = packet
        row = detail.get(evidence_id)
        if row is None or row.get("confidence_tier") != "medium-high" or row.get("pathway_reuse_key") != reuse_key or row.get("source_locators") != citations:
            raise SystemExit(f"detail lineage mismatch: {evidence_id}")
        required_layers = ("downstream_pathway_function",) if evidence_id in FUNCTION_ONLY else ("receptor_proximal_relay", "downstream_pathway_function")
        if not all(layer in row.get("evidence_layer", "") for layer in required_layers):
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
    audit_rows = [{"evidence_id": eid, "review_id": packet[2], "pair_key": packet[0], "pathway_reuse_key": packet[1], "previous_tier": detail[eid]["confidence_tier"], "new_tier": "high", "source_locators": detail[eid]["source_locators"], "decision_basis": packet[4], "upstream_lr_confidence_unchanged": "true", "terminal_tf_status_unchanged": "true", "sql_materialization": "false"} for eid, packet in sorted(PACKET.items())]
    if not args.apply:
        print(json.dumps({"validated": len(audit_rows), "apply": False, "evidence_ids": sorted(PACKET)}, indent=2))
        return
    for evidence_id, packet in PACKET.items():
        detail[evidence_id]["confidence_tier"] = "high"
        detail[evidence_id]["limitations"] = append_once(detail[evidence_id]["limitations"], PROMOTION_NOTE)
        reviews[packet[2]]["confidence_tier"] = "high"
        reviews[packet[2]]["curator_note"] = append_once(reviews[packet[2]]["curator_note"], PROMOTION_NOTE)
        reuse[packet[1]]["validation_status"] = "promoted_high_batch040"
        reuse[packet[1]]["limitations"] = append_once(reuse[packet[1]]["limitations"], PROMOTION_NOTE)
        coverage = next(item for item in pair_rows if item.get("module21a_evidence_ids") == evidence_id)
        coverage["curator_notes"] = append_once(coverage["curator_notes"], PROMOTION_NOTE)
    write_tsv(DETAIL, detail_fields, detail_rows)
    write_tsv(REVIEW, review_fields, review_rows)
    write_tsv(REUSE, reuse_fields, reuse_rows)
    write_tsv(PAIRS, pair_fields, pair_rows)
    write_tsv(AUDIT, audit_fields, audit_rows)
    SUMMARY.write_text(json.dumps({"promotion_id": "module21a-relay-function-batch040-2026-09-02", "records_promoted": len(audit_rows), "evidence_ids": sorted(PACKET), "promotion_note": PROMOTION_NOTE, "upstream_module20a_lr_confidence_changed": False, "terminal_tf_assignments_created": False, "sql_signaling_edges_created": False, "malformed_legacy_rows_touched": False}, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"validated": len(audit_rows), "applied": len(audit_rows), "evidence_ids": sorted(PACKET)}, indent=2))


if __name__ == "__main__":
    main()
