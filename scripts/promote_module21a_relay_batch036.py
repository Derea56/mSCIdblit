#!/usr/bin/env python3
"""Promote twelve bounded Module 21A galectin, LGI, cytokine, and matrix packets."""

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
REVIEW = RELAY / "module21a_pair_relay_review_batches220_221.tsv"
AUDIT = RELAY / "module21a_relay_promotion_batch036.tsv"
SUMMARY = RELAY / "module21a_relay_promotion_batch036_summary.json"

PACKET = {
    "M21A-PAIR-EVID-5401": ("lgals3 mcam", "M21A-REUSE-2540", "M20A-EXT-2356", "PMID:28364041;DOI:10.1074/jbc.M117.783431;PMID:29741757;DOI:10.1002/1873-3468.13083", "Glycan-dependent LGALS3-MCAM/CD146 binding, receptor dimerization, AKT signaling, and endothelial migration/cytokine function support qualified-high promotion; preserve endothelial glycoprotein and cell-context boundaries."),
    "M21A-PAIR-EVID-5403": ("lgi1 adam22", "M21A-REUSE-2542", "M20A-EXT-2359", "PMCID:PMC2575350;PMID:20133599", "Direct LGI1-ADAM22 binding and ADAM22-linked synaptic-complex function support qualified-high promotion; ADAM22 is non-catalytic and associated ADAM23, MAGUK, and ion-channel components remain required context."),
    "M21A-PAIR-EVID-5405": ("lgi1 rtn4r", "M21A-REUSE-2543", "M20A-EXT-2361", "PMID:20463223;PMID:27468420;DOI:10.1002/mgg3.215", "LGI1 binding to RTN4R/NgR1 in an ADAM22-associated complex and receptor-dependent growth-cone/myelin-inhibition function support qualified-high promotion; preserve GPI-anchored RTN4R and coreceptor context."),
    "M21A-PAIR-EVID-5407": ("lgi3 adam23", "M21A-REUSE-2545", "M20A-EXT-2365", "PMID:38194969;PMCID:PMC10828548;DOI:10.1083/jcb.202211031", "LGI3 secretion, ADAM23-dependent juxtaparanodal organization, genetics, and axonal electrical function support qualified-high promotion; preserve LGI2 redundancy, myelinated-axon context, and the non-kinase receptor-complex scope."),
    "M21A-PAIR-EVID-5410": ("lhb lhcgr", "M21A-REUSE-2547", "M20A-EXT-2375", "https://academic.oup.com/endo/article/165/6/bqae052/7659435;PMID:12456794;DOI:10.1210/me.2002-0208", "The LHB subunit contributes to intact alpha/beta LH or LHB-CGA fusion binding and LHCGR Gs/cAMP and calcium function; promote only in the intact glycoprotein-ligand context, not isolated LHB agonism."),
    "M21A-PAIR-EVID-5411": ("lif il6st_lifr", "M21A-REUSE-2548", "M20A-EXT-2381", "PMID:8921810;DOI:10.1161/01.CIR.94.10.2626;PMID:9712900;DOI:10.1074/jbc.273.35.22701;PMID:9242667", "Exact LIFR-IL6ST/gp130 complex activation with JAK/STAT3, MAPK, differentiation, and cardiac function supports qualified-high promotion; preserve composite-receptor stoichiometry and tissue-specific branch use."),
    "M21A-PAIR-EVID-5413": ("lrrc4b ptprf", "M21A-REUSE-2549", "M20A-EXT-2415", "PMID:19252495;PMID:20139422;Reactome:R-HSA-6798258", "Direct LRRC4B/NGL3-PTPRF/LAR ectodomain binding and trans-synaptic synaptogenesis function support qualified-high promotion; preserve splice and synaptic context, with adhesion/PTP organization rather than a defined kinase cascade."),
    "M21A-PAIR-EVID-5414": ("lta_ltb ltbr", "M21A-REUSE-2550", "M20A-EXT-2418", "PMID:8171323;DOI:10.1126/science.8171323;PMID:24248355;PMCID:PMC3856818;DOI:10.1073/pnas.1310838110;PMID:12556537", "Membrane LTalpha1beta2 binding and LTBR dimerization with TRAF/NIK/IKK and NF-kappaB function support qualified-high promotion; preserve the heterotrimeric ligand and canonical/noncanonical branch context."),
    "M21A-PAIR-EVID-5415": ("ltf lrp1", "M21A-REUSE-2551", "M20A-EXT-2427", "PMID:15178744;DOI:10.1016/j.bone.2004.03.006;PMID:12215536", "LTF binding to an LRP1-containing context, RAP-sensitive/LRP1-null comparisons, ERK1/2, and osteoblast mitogenic function support qualified-high promotion; preserve multiligand LRP1 and endocytic/mitogenic scope."),
    "M21A-PAIR-EVID-5416": ("matn1 itga1", "M21A-REUSE-2552", "M20A-EXT-2437", "PMID:10196235;DOI:10.1074/jbc.274.16.11417", "MATN1/CMP association with alpha1beta1 and adhesion/spreading function support qualified-high promotion at exact extracellular binding/function scope; no purified affinity or intracellular relay is claimed."),
    "M21A-PAIR-EVID-5418": ("mdk alk", "M21A-REUSE-2554", "M20A-EXT-2443", "PMID:12122009;DOI:10.1074/jbc.M205749200", "Cell-based MDK-ALK binding, ALK phosphorylation, PI3K/MAPK signaling, and growth/angiogenic function support qualified-high promotion; preserve debated receptor-composition and model-context boundaries."),
    "M21A-PAIR-EVID-5419": ("mdk gpc2", "M21A-REUSE-2555", "M20A-EXT-2444", "PMID:12084985;DOI:10.1023/A:1016042303253", "Heparan-sulfate-dependent MDK-GPC2 binding, GPC2 clustering, neuronal adhesion, and neurite outgrowth support qualified-high extracellular binding/function promotion; GPC2 has no defined cytosolic relay and no TF claim is added."),
}

PROMOTION_NOTE = "Module 21A relay/function promotion batch036 (2026-09-02): evidence tier raised to high for the exact, context-bounded packet; evidence-layer scope, upstream Module 20A LR confidence, terminal-TF status, and SCI transfer remain unchanged."


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
        required_layers = ("downstream_pathway_function",) if evidence_id in {"M21A-PAIR-EVID-5416", "M21A-PAIR-EVID-5419"} else ("receptor_proximal_relay", "downstream_pathway_function")
        if not all(layer in row.get("evidence_layer", "") for layer in required_layers):
            raise SystemExit(f"{evidence_id} lacks required evidence layers")
        review = reviews.get(review_id)
        allowed_status = {"reviewed_function_only"} if evidence_id in {"M21A-PAIR-EVID-5416", "M21A-PAIR-EVID-5419"} else {"reviewed_relay_candidate"}
        if (review is None or review.get("evidence_id") != evidence_id or review.get("pair_key") != pair_key or review.get("source_locators") != citations or review.get("confidence_tier") != "medium-high" or review.get("review_status") not in allowed_status):
            raise SystemExit(f"review lineage mismatch: {evidence_id}")
        if reuse.get(reuse_key) is None or reuse[reuse_key].get("evidence_ids") != evidence_id:
            raise SystemExit(f"reuse lineage mismatch: {evidence_id}")
        coverage = next((item for item in pair_rows if item.get("module21a_evidence_ids") == evidence_id), None)
        if coverage is None or coverage.get("pair_key") != pair_key or coverage.get("module21a_status") not in allowed_status:
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
        reuse[packet[1]]["validation_status"] = "promoted_high_batch036"
        reuse[packet[1]]["limitations"] = append_once(reuse[packet[1]]["limitations"], PROMOTION_NOTE)
        coverage = next(item for item in pair_rows if item.get("module21a_evidence_ids") == evidence_id)
        coverage["curator_notes"] = append_once(coverage["curator_notes"], PROMOTION_NOTE)
    write_tsv(DETAIL, detail_fields, detail_rows)
    write_tsv(REVIEW, review_fields, review_rows)
    write_tsv(REUSE, reuse_fields, reuse_rows)
    write_tsv(PAIRS, pair_fields, pair_rows)
    write_tsv(AUDIT, audit_fields, audit_rows)
    SUMMARY.write_text(json.dumps({"promotion_id": "module21a-relay-function-batch036-2026-09-02", "records_promoted": len(audit_rows), "evidence_ids": sorted(PACKET), "promotion_note": PROMOTION_NOTE, "upstream_module20a_lr_confidence_changed": False, "terminal_tf_assignments_created": False, "sql_signaling_edges_created": False, "malformed_legacy_rows_touched": False}, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"validated": len(audit_rows), "applied": len(audit_rows), "evidence_ids": sorted(PACKET)}, indent=2))


if __name__ == "__main__":
    main()
