#!/usr/bin/env python3
"""Promote fifteen bounded Module 21A prolactin-family and PTH packets."""

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
REVIEW_FILES = [RELAY / "module21a_pair_relay_review_batches224_225.tsv", RELAY / "module21a_pair_relay_review_batches226_227.tsv"]
AUDIT = RELAY / "module21a_relay_promotion_batch042.tsv"
SUMMARY = RELAY / "module21a_relay_promotion_batch042_summary.json"

PACKET = {
    "M21A-PAIR-EVID-5520": ("prlh prlhr", "M21A-REUSE-2639", "M20A-EXT-2809", "PMID:21185342;PMCID:PMC1572376;PMID:23467899", "GPR10/PRLHR Gi/o or Gq/11-PLC-calcium relay with pituitary/neuroendocrine outputs supports qualified-high promotion; preserve recombinant versus endogenous coupling and analog boundaries."),
    "M21A-PAIR-EVID-5521": ("proc procr", "M21A-REUSE-2640", "M20A-EXT-2813", "PMID:14577849;PMID:27561318;PMID:21252088", "Activation-state-dependent protein-C/EPCR cytoprotective relay/function supports qualified-high promotion; preserve zymogen versus activated protein C and EPCR-occupied thrombin semantics."),
    "M21A-PAIR-EVID-5522": ("prok1 prokr1", "M21A-REUSE-2641", "M20A-EXT-2816", "PMID:18339712;PMCID:PMC4382091", "Exact PROK1/PROKR1 Gq-PLC-calcium, c-Src/EGFR transactivation, ERK/Akt, and endometrial/vascular function support qualified-high promotion; preserve engineered and co-expression context."),
    "M21A-PAIR-EVID-5523": ("prok1 prokr2", "M21A-REUSE-2642", "M20A-EXT-2817", "PMID:12054613;DOI:10.1016/j.cellsig.2021.110000", "Direct PROKR2 activation with Gq/11, Gi/o, arrestin, calcium, and ERK branches supports qualified-high promotion; coupling varies by ligand isoform, species, expression system, and cell context."),
    "M21A-PAIR-EVID-5524": ("prok2 prokr1", "M21A-REUSE-2643", "M20A-EXT-2818", "PMID:12054613;DOI:10.1016/j.cellsig.2021.110000", "Direct PROK2/PROKR1 activation with Gq/11-PLC-calcium, Gi/o-ERK, cAMP, and arrestin function supports qualified-high promotion; preserve PROK2 potency and assay-dependent coupling."),
    "M21A-PAIR-EVID-5525": ("prok2 prokr2", "M21A-REUSE-2644", "M20A-EXT-2819", "PMID:12054613;PMID:31132148;DOI:10.1016/j.cellsig.2021.110000", "Exact PROK2/PROKR2 activation and olfactory-interneuron migration function support qualified-high promotion; preserve recombinant versus mutant-mouse context and variable coupling."),
    "M21A-PAIR-EVID-5527": ("pros1 mertk", "M21A-REUSE-2645", "M20A-EXT-2821", "PMCID:PMC4206827;PMID:25074926;PMID:33848267", "MERTK autophosphorylation and efferocytosis/inflammatory-resolution function support qualified-high promotion; require gamma-carboxylated PROS1, calcium, and phosphatidylserine targets."),
    "M21A-PAIR-EVID-5528": ("pros1 tyro3", "M21A-REUSE-2646", "M20A-EXT-2822", "PMCID:PMC4206827;PMCID:PMC6966665;PMID:10627473", "TYRO3 autophosphorylation and ERK/AKT survival, proliferation, or neuronal-protection function support qualified-high promotion; preserve PROS1 gamma-carboxylation and receptor/cell context."),
    "M21A-PAIR-EVID-5529": ("psap gpr37", "M21A-REUSE-2647", "M20A-EXT-2830", "PMID:23690594;PMCID:PMC3677493;PMID:24371137", "GPR37 Gi/o-cAMP inhibition/ERK relay and astrocyte/neuronal stress protection support qualified-high promotion; preserve full-length prosaposin versus prosaptide fragment and overexpression context."),
    "M21A-PAIR-EVID-5532": ("pth lrp6", "M21A-REUSE-2649", "M20A-EXT-2854", "PMID:18981475;PMCID:PMC2577789;PMID:25088803", "PTH1R-recruited LRP6/Axin beta-catenin/osteoblast function supports qualified-high promotion; this is a ternary PTH1R-coreceptor relay, not direct PTH-LRP6 binding."),
    "M21A-PAIR-EVID-5533": ("pth pth1r", "M21A-REUSE-2650", "M20A-EXT-2855", "PMID:9482662;PMID:15611080;PMID:19674967", "Direct PTH/PTH1R Gs-cAMP/PKA and Gq-PLC-calcium relay with trafficking and EGFR-ERK outputs supports qualified-high promotion; preserve ligand conformation and receptor-trafficking dependence."),
    "M21A-PAIR-EVID-5534": ("pth pth2r", "M21A-REUSE-2651", "M20A-EXT-2856", "PMID:8770894;PMID:9482662;PMID:9360953", "PTH/PTH2R receptor-proximal Gs-cAMP/calcium evidence supports qualified-high promotion only at that layer; preserve human/species dependence and TIP39 as preferred physiological ligand."),
    "M21A-PAIR-EVID-5536": ("pth2 pth2r", "M21A-REUSE-2652", "M20A-EXT-2867", "PMID:12098667;PMID:12559132;PMID:19706789", "Direct mature TIP39/PTH2R Gs-cAMP/Gq-calcium activation with neuronal/chondrocyte function supports qualified-high promotion; SOX9 is a reporter endpoint, not receptor-TF binding."),
    "M21A-PAIR-EVID-5537": ("pthlh pth1r", "M21A-REUSE-2653", "M20A-EXT-2878", "PMID:7479750;PMID:19674967;PMID:26090315", "Direct PTHrP/PTH1R cAMP/calcium with context-dependent ERK and neuronal/epithelial/osteogenic function supports qualified-high promotion; preserve PTHrP peptide form and signal duration."),
    "M21A-PAIR-EVID-5539": ("ptn alk", "M21A-REUSE-2654", "M20A-EXT-2884", "PMID:11278720;PMID:15908427;https://www.jci.org/articles/view/76838", "Direct PTN/ALK RTK activation with IRS1/Shc/PLCgamma/PI3K and RAS-MEK-ERK function supports qualified-high promotion; preserve PTN processing, ALK/co-receptor composition, and PTPRZ1-dependent branch."),
}

RECEPTOR_ONLY = {"M21A-PAIR-EVID-5534"}
PROMOTION_NOTE = "Module 21A relay/function promotion batch042 (2026-09-02): evidence tier raised to high for the exact, context-bounded packet; evidence-layer scope, upstream Module 20A LR confidence, terminal-TF status, and SCI transfer remain unchanged."


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
        required_layers = ("receptor_proximal_relay",) if evidence_id in RECEPTOR_ONLY else ("receptor_proximal_relay", "downstream_pathway_function")
        if not all(layer in row.get("evidence_layer", "") for layer in required_layers):
            raise SystemExit(f"{evidence_id} lacks required evidence layers")
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
        reuse[packet[1]]["validation_status"] = "promoted_high_batch042"
        reuse[packet[1]]["limitations"] = append_once(reuse[packet[1]]["limitations"], PROMOTION_NOTE)
        coverage = next(item for item in pair_rows if item.get("module21a_evidence_ids") == evidence_id)
        coverage["curator_notes"] = append_once(coverage["curator_notes"], PROMOTION_NOTE)
    write_tsv(DETAIL, detail_fields, detail_rows)
    for path, fields, rows in zip(REVIEW_FILES, review_fields, review_rows_by_file):
        write_tsv(path, fields, rows)
    write_tsv(REUSE, reuse_fields, reuse_rows)
    write_tsv(PAIRS, pair_fields, pair_rows)
    write_tsv(AUDIT, audit_fields, audit_rows)
    SUMMARY.write_text(json.dumps({"promotion_id": "module21a-relay-function-batch042-2026-09-02", "records_promoted": len(audit_rows), "evidence_ids": sorted(PACKET), "promotion_note": PROMOTION_NOTE, "upstream_module20a_lr_confidence_changed": False, "terminal_tf_assignments_created": False, "sql_signaling_edges_created": False, "malformed_legacy_rows_touched": False}, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"validated": len(audit_rows), "applied": len(audit_rows), "evidence_ids": sorted(PACKET)}, indent=2))


if __name__ == "__main__":
    main()
