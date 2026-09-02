#!/usr/bin/env python3
"""Promote eleven bounded Module 21A RSPO, SAA, SCUBE2, and Sema3A packets."""

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
    RELAY / "module21a_pair_relay_review_batches228.tsv",
    RELAY / "module21a_pair_relay_review_batches229.tsv",
]
AUDIT = RELAY / "module21a_relay_promotion_batch046.tsv"
SUMMARY = RELAY / "module21a_relay_promotion_batch046_summary.json"

PACKET = {
    "M21A-PAIR-EVID-5600": ("rspo4 rnf43", "M21A-REUSE-2708", "M20A-EXT-2976", "PMID:28467820; PMID:24225776; PMCID:PMC3905715; DOI:10.1038/ncomms3787; PMID:25504990; DOI:10.1124/mol.114.095133", "Exact RSPO4-RNF43 E3-ligase/WNT-complex relay/function supports qualified-high promotion; preserve weaker construct-dependent potency and use RSPO2 structural information only as mechanism context."),
    "M21A-PAIR-EVID-5601": ("rspo4 znrf3", "M21A-REUSE-2709", "M20A-EXT-2977", "PMID:28467820; PMID:24225776; PMCID:PMC3905715; DOI:10.1038/ncomms3787; PMID:25504990; DOI:10.1124/mol.114.095133", "Exact RSPO4-ZNRF3 receptor-complex relay/function supports qualified-high promotion; preserve weak construct-dependent binding, do not transfer RNF43 evidence, and treat reporter/organoid outputs as pathway-level."),
    "M21A-PAIR-EVID-5605": ("s100a1 tlr4", "M21A-REUSE-2713", "M20A-EXT-2989", "PMID:24833748; PMCID:PMC4203355; DOI:10.15252/emmm.201303498; PMID:25880347", "Exact TLR4/MyD88-dependent S100A1 DAMP relay/function supports qualified-high promotion; preserve ischemia/cardiac context and do not infer purified affinity or a broad terminal-TF claim."),
    "M21A-PAIR-EVID-5607": ("saa1 cd36", "M21A-REUSE-2714", "M20A-EXT-3006", "PMID:20075072; PMCID:PMC2832998; DOI:10.1074/jbc.M109.007526; PMID:39244902", "Exact SAA1-CD36 scavenger-receptor signaling/function supports qualified-high promotion; preserve SAA preparation, receptor-complex, and internalization/stoichiometry caveats."),
    "M21A-PAIR-EVID-5608": ("saa1 fpr2", "M21A-REUSE-2715", "M20A-EXT-3008", "PMID:25154907; PMCID:PMC4252704; DOI:10.1016/j.imbio.2014.08.002; PMID:32477346; PMCID:PMC7240019; DOI:10.3389/fimmu.2020.00843", "Exact SAA1-FPR2 GPCR-proximal function supports qualified-high promotion; preserve SAA1 isoform and preparation-purity boundaries and do not infer one structural binding mode."),
    "M21A-PAIR-EVID-5609": ("saa2 fpr2", "M21A-REUSE-2716", "M20A-EXT-3015", "PMID:25154907; PMCID:PMC4252704; DOI:10.1016/j.imbio.2014.08.002; PMID:41654488", "Exact SAA2.2-FPR2 activation/function supports qualified-high promotion; preserve SAA2 form, tumor-conditioned model scope, and EGR1 as a specified-model endpoint only."),
    "M21A-PAIR-EVID-5611": ("scube2 kdr", "M21A-REUSE-2717", "M20A-EXT-3026", "PMID:27834687; DOI:10.1161/ATVBAHA.116.308546", "Exact SCUBE2-VEGF-KDR/VEGFR2 coreceptor-complex relay/function supports qualified-high promotion; preserve VEGF-containing ternary topology and endothelial context."),
    "M21A-PAIR-EVID-5615": ("sema3a nrp1_plxna1", "M21A-REUSE-2720", "M20A-EXT-3038", "PMID:10520994; DOI:10.1016/S0092-8674(00)80062-8; PMID:22723296", "Exact Sema3A-NRP1/PLXNA1 tripartite relay/function supports qualified-high promotion; preserve NRP1 ligand-binding and PLXNA1 signal-transducer roles and do not infer free PLXNA1 binding."),
    "M21A-PAIR-EVID-5616": ("sema3a nrp1_plxna2", "M21A-REUSE-2721", "M20A-EXT-3039", "PMID:11239433; DOI:10.1016/S0896-6273(01)00216-1; PMID:23104057; PMCID:PMC3590443; DOI:10.1038/nsmb.2416", "Exact Sema3A-NRP1/PLXNA2 ternary relay/function supports qualified-high promotion; preserve NRP1 binding versus PLXNA2 transduction and do not claim free PLXNA2 binding."),
    "M21A-PAIR-EVID-5617": ("sema3a nrp1_plxna3", "M21A-REUSE-2722", "M20A-EXT-3040", "PMID:11239433; DOI:10.1016/S0896-6273(01)00216-1; PMID:15721238; DOI:10.1016/j.neuron.2005.01.013; PMID:23991118; PMCID:PMC3753268; PMID:32068081; DOI:10.1016/j.neuroscience.2020.02.008", "Exact context-specific Sema3A-NRP1/PLXNA3 complex/function supports qualified-high promotion; preserve mixed plexin stoichiometry and do not infer binary Sema3A-PLXNA3 binding."),
    "M21A-PAIR-EVID-5618": ("sema3a nrp1_plxna4", "M21A-REUSE-2723", "M20A-EXT-3041", "PMID:34039996; PMCID:PMC8155012; DOI:10.1038/s41467-021-23541-x; PMID:15721238; DOI:10.1016/j.neuron.2005.01.013", "Exact Sema3A-NRP1/PLXNA4 2:2:2 tripartite relay/function supports qualified-high promotion; preserve the purified near-intact complex topology and do not infer free PLXNA4 binding."),
}

PROMOTION_NOTE = "Module 21A relay/function promotion batch046 (2026-09-02): evidence tier raised to high for the exact, context-bounded packet; evidence-layer scope, upstream Module 20A LR confidence, terminal-TF status, and SCI transfer remain unchanged."


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
    detail = index(detail_rows, "evidence_id")
    reuse = index(reuse_rows, "pathway_reuse_key")
    reviews = index(review_rows, "review_id")

    for evidence_id, packet in PACKET.items():
        pair_key, reuse_key, review_id, citations, _basis = packet
        row = detail.get(evidence_id)
        if row is None or row.get("confidence_tier") not in {"medium", "medium-high"} or row.get("pathway_reuse_key") != reuse_key or row.get("source_locators") != citations:
            raise SystemExit(f"detail lineage mismatch: {evidence_id}")
        if not all(layer in row.get("evidence_layer", "") for layer in ("receptor_proximal_relay", "downstream_pathway_function")):
            raise SystemExit(f"{evidence_id} lacks required evidence layers")
        review = reviews.get(review_id)
        if (review is None or review.get("evidence_id") != evidence_id or review.get("pair_key") != pair_key or review.get("source_locators") != citations or review.get("confidence_tier") not in {"medium", "medium-high"} or review.get("review_status") != "reviewed_relay_candidate"):
            raise SystemExit(f"review lineage mismatch: {evidence_id}")
        if reuse.get(reuse_key) is None or reuse[reuse_key].get("evidence_ids") != evidence_id:
            raise SystemExit(f"reuse lineage mismatch: {evidence_id}")
        coverage = next((item for item in pair_rows if item.get("module21a_evidence_ids") == evidence_id), None)
        if coverage is None or coverage.get("pair_key") != pair_key or coverage.get("module21a_status") != "reviewed_relay_candidate":
            raise SystemExit(f"coverage lineage mismatch: {evidence_id}")

    audit_fields = ["evidence_id", "review_id", "pair_key", "pathway_reuse_key", "previous_tier", "new_tier", "source_locators", "decision_basis", "upstream_lr_confidence_unchanged", "terminal_tf_status_unchanged", "sql_materialization"]
    audit_rows = [{
        "evidence_id": evidence_id,
        "review_id": packet[2],
        "pair_key": packet[0],
        "pathway_reuse_key": packet[1],
        "previous_tier": detail[evidence_id]["confidence_tier"],
        "new_tier": "high",
        "source_locators": detail[evidence_id]["source_locators"],
        "decision_basis": packet[4],
        "upstream_lr_confidence_unchanged": "true",
        "terminal_tf_status_unchanged": "true",
        "sql_materialization": "false",
    } for evidence_id, packet in sorted(PACKET.items())]

    if not args.apply:
        print(json.dumps({"validated": len(audit_rows), "apply": False, "evidence_ids": sorted(PACKET)}, indent=2))
        return

    for evidence_id, packet in PACKET.items():
        detail[evidence_id]["confidence_tier"] = "high"
        detail[evidence_id]["limitations"] = append_once(detail[evidence_id]["limitations"], PROMOTION_NOTE)
        reviews[packet[2]]["confidence_tier"] = "high"
        reviews[packet[2]]["curator_note"] = append_once(reviews[packet[2]]["curator_note"], PROMOTION_NOTE)
        reuse[packet[1]]["validation_status"] = "promoted_high_batch046"
        reuse[packet[1]]["limitations"] = append_once(reuse[packet[1]]["limitations"], PROMOTION_NOTE)
        coverage = next(item for item in pair_rows if item.get("module21a_evidence_ids") == evidence_id)
        coverage["curator_notes"] = append_once(coverage["curator_notes"], PROMOTION_NOTE)

    write_tsv(DETAIL, detail_fields, detail_rows)
    for path, fields, rows in zip(REVIEW_FILES, review_fields, review_rows_by_file):
        write_tsv(path, fields, rows)
    write_tsv(REUSE, reuse_fields, reuse_rows)
    write_tsv(PAIRS, pair_fields, pair_rows)
    write_tsv(AUDIT, audit_fields, audit_rows)
    SUMMARY.write_text(json.dumps({
        "promotion_id": "module21a-relay-function-batch046-2026-09-02",
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
