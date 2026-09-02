#!/usr/bin/env python3
"""Promote exact, bounded Module 21A interactions from lanes 5411-5510."""

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
    RELAY / "module21a_pair_relay_review_batches220_221.tsv",
    RELAY / "module21a_pair_relay_review_batches222_223.tsv",
    RELAY / "module21a_pair_relay_review_batches224_225.tsv",
]
AUDIT = RELAY / "module21a_relay_promotion_batch117.tsv"
SUMMARY = RELAY / "module21a_relay_promotion_batch117_summary.json"

PACKET = [
    (5417, "M20A-EXT-2438", "M21A-REUSE-2553"),
    (5424, "M20A-EXT-2452", ""),
    (5425, "M20A-EXT-2455", "M21A-REUSE-2560"),
    (5433, "M20A-EXT-2493", ""),
    (5434, "M20A-EXT-2494", ""),
    (5440, "M20A-EXT-2519", ""),
    (5444, "M20A-EXT-2529", ""),
    (5445, "M20A-EXT-2536", ""),
    (5464, "M20A-EXT-2587", "M21A-REUSE-2593"),
    (5467, "M20A-EXT-2590", "M21A-REUSE-2596"),
    (5470, "M20A-EXT-2606", "M21A-REUSE-2599"),
    (5476, "M20A-EXT-2624", "M21A-REUSE-2605"),
    (5477, "M20A-EXT-2625", "M21A-REUSE-2606"),
    (5492, "M20A-EXT-2649", "M21A-REUSE-2618"),
    (5494, "M20A-EXT-2652", ""),
    (5495, "M20A-EXT-2654", ""),
    (5496, "M20A-EXT-2655", ""),
    (5499, "M20A-EXT-2666", "M21A-REUSE-2621"),
    (5500, "M20A-EXT-2667", ""),
    (5504, "M20A-EXT-2675", "M21A-REUSE-2623"),
    (5505, "M20A-EXT-2676", "M21A-REUSE-2624"),
    (5506, "M20A-EXT-2677", "M21A-REUSE-2625"),
    (5507, "M20A-EXT-2678", "M21A-REUSE-2626"),
    (5508, "M20A-EXT-2680", "M21A-REUSE-2627"),
]

NOTE = (
    "Module 21A qualified-relay promotion batch117 (2026-09-02): exact matrix/"
    "adhesion, proteoglycan, synaptic, neuropeptide-GPCR, sorting/scavenging, "
    "and receptor-trafficking evidence is raised to high only at the recorded "
    "supported layer. Complex, subunit, splice/isoform, ligand-form, antagonist, "
    "species/model, assay, and no-SCI boundaries remain explicit; no terminal-TF "
    "claim or SQL signaling edge is created."
)

BASIS = {
    5417: "MATN1-dependent adhesion through alpha1-beta1 supports high at the exact ITGB1-containing matrix-receptor layer; autonomous ITGB1 and an intracellular pathway are not inferred.",
    5424: "Direct glycosaminoglycan/core-protein-dependent MDK-SDC1 association supports high at the exact proteoglycan-binding layer; no SDC1 cytoplasmic relay is claimed.",
    5425: "Direct MDK-SDC4 binding and SDC4-dependent Ras-linked function support high at the exact proteoglycan/function layer; no universal MDK-to-Ras relay is inferred.",
    5433: "Direct MMRN2-CD248 extracellular receptor-complex association supports high at the exact binding layer; no CD248-specific intracellular relay is inferred.",
    5434: "Direct MMRN2-CD93 extracellular receptor-complex association supports high at the exact binding layer; shared MMRN2-site and no CD93-specific relay boundaries remain explicit.",
    5440: "Direct heterophilic NCAM1-ROBO3 association supports high at the exact adhesion-binding layer; no ROBO3-specific downstream relay or TF is inferred.",
    5444: "Direct NGF/proNGF binding to SORCS3 supports high at the exact Vps10p-domain binding/trafficking layer; p75NTR/TrkA pathways are not transferred.",
    5445: "Direct binding of the laminin-nidogen complex containing NID1 to PTPRF supports high at the exact extracellular matrix-complex layer; purified NID1-alone and PTPRF relay claims are excluded.",
    5464: "NPTX1 association with NPTXR-containing neuronal pentraxin complexes and AMPAR clustering supports high at the exact synaptic-complex/function layer; no unique NPTXR cytosolic relay is inferred.",
    5467: "NPVF activation of NPFFR2 and Gi/o-linked receptor function support high at the exact cross-reactive RFamide GPCR layer; lower selectivity and no TF endpoint remain explicit.",
    5470: "NPY activation of NPY2R with Gi/o-linked neuronal and presynaptic function supports high at the exact Y2R layer; fragment and neighboring-receptor caveats remain explicit.",
    5476: "Direct NLGN3-NRXN1 trans-synaptic adhesion with synapse differentiation supports high at the exact adhesion/function layer; splice dependence and no unique intracellular relay remain explicit.",
    5477: "NLGN1-NRXN2beta complex-resolved adhesion and synaptic function support high at the exact beta-neurexin complex layer; promoter/splice and no NRXN2-only relay boundaries remain explicit.",
    5492: "Direct neurotensin-SORT1 binding with cargo capture and endocytic/scavenging function supports high at the exact sorting-receptor layer; no canonical SORT1 intracellular relay is claimed.",
    5494: "Direct NXPH1 binding to the alpha-NRXN2 LNS2 domain supports high at the exact splice-resolved binding layer; promoter/SS2 and downstream relay are not inferred.",
    5495: "Direct splice-sensitive NXPH3 binding to the alpha-NRXN1 LNS2 domain supports high at the exact binding layer; promoter/splice and intracellular relay boundaries remain explicit.",
    5496: "Direct splice-sensitive NXPH3 binding to the alpha-NRXN2 LNS2 domain supports high at the exact binding layer; promoter/splice and intracellular relay boundaries remain explicit.",
    5499: "Direct OSTN-NPR3 binding with altered natriuretic-peptide clearance supports high at the exact clearance-receptor layer; indirect CNP/NPR2 effects are not an NPR3 intracellular relay.",
    5500: "OXT pharmacological binding/activity at AVPR1A supports high only at the exact cross-reactive GPCR binding layer; species, potency, and lack of OXT-specific downstream isolation remain explicit.",
    5504: "Direct PCSK9-APLP2 interaction with endocytic/lysosomal routing supports high at the exact trafficking layer; APLP2 kinase or TF signaling is not inferred.",
    5505: "Direct PCSK9-CD36 binding with receptor degradation and lipid-uptake effects supports high at the exact receptor-trafficking layer; no CD36-proximal TF relay is claimed.",
    5506: "PCSK9-CD81 interaction with intracellular degradation supports high at the exact tetraspanin-trafficking layer; no CD81 kinase or transcriptional relay is inferred.",
    5507: "Direct PCSK9-LDLR binding with endosomal rerouting and lysosomal degradation supports high at the exact clearance/trafficking layer; no signaling relay is claimed.",
    5508: "Direct PCSK9-LRP8/ApoER2 binding with endocytic/lysosomal degradation supports high at the exact receptor-trafficking layer; tissue-context differences and no LRP8 relay remain explicit.",
}


def read(path):
    with path.open(encoding="utf-8", newline="") as handle:
        r = csv.DictReader(handle, delimiter="\t")
        return list(r.fieldnames or []), list(r)


def write(path, fields, rows):
    with path.open("w", encoding="utf-8", newline="") as handle:
        w = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        w.writeheader(); w.writerows(rows)


def tokens(value):
    return {x.strip() for x in value.split(";") if x.strip()}


def once(value):
    return value if NOTE in value else f"{value} {NOTE}".strip()


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--apply", action="store_true"); args = ap.parse_args()
    df, detail_rows = read(DETAIL); uf, reuse_rows = read(REUSE); pf, pair_rows = read(PAIRS)
    review_tables = [read(path) for path in REVIEW_FILES]
    reviews = {r["review_id"]: r for _, rows in review_tables for r in rows}
    detail = {r["evidence_id"]: r for r in detail_rows}
    reuse = {r["pathway_reuse_key"]: r for r in reuse_rows if r.get("pathway_reuse_key")}
    coverage = {}
    audit = []
    for number, review_id, reuse_key in PACKET:
        evidence_id = f"M21A-PAIR-EVID-{number}"; row = detail.get(evidence_id); review = reviews.get(review_id)
        if row is None or row.get("confidence_tier") not in {"medium", "medium-high"} or row.get("pathway_reuse_key", "") != reuse_key:
            raise SystemExit(f"detail lineage/tier mismatch: {evidence_id}")
        if not tokens(row.get("evidence_layer", "")) & {"binding_activation", "ligand_receptor_binding_or_activation", "receptor_proximal_relay", "downstream_pathway_function"}:
            raise SystemExit(f"detail layer mismatch: {evidence_id}")
        if review is None or review.get("evidence_id") != evidence_id or review.get("pathway_reuse_key", "") != reuse_key or review.get("source_locators") != row.get("source_locators"):
            raise SystemExit(f"review lineage mismatch: {evidence_id}")
        if review.get("review_status") not in {"reviewed_relay_candidate", "reviewed_binding_only", "reviewed_function_only", "reviewed_scavenging_only"}:
            raise SystemExit(f"review status mismatch: {evidence_id}")
        if reuse_key and (reuse.get(reuse_key) is None or reuse[reuse_key].get("evidence_ids") != evidence_id):
            raise SystemExit(f"reuse lineage mismatch: {evidence_id}")
        matching = [p for p in pair_rows if evidence_id in tokens(p.get("module21a_evidence_ids", "")) and p.get("pair_key") == review.get("pair_key")]
        if len(matching) != 1: raise SystemExit(f"coverage mapping mismatch: {evidence_id}")
        pair = matching[0]; coverage[evidence_id] = pair
        if pair.get("module21a_status") != review.get("review_status") or pair.get("module22a_status") != "no_terminal_tf_evidence":
            raise SystemExit(f"coverage/TF-boundary mismatch: {evidence_id}")
        hits = []
        for path in RELAY.glob("module21a_relay_promotion_batch*.tsv"):
            if path == AUDIT: continue
            with path.open(encoding="utf-8", newline="") as handle:
                if any(x.get("evidence_id") == evidence_id or x.get("pair_key") == review["pair_key"] for x in csv.DictReader(handle, delimiter="\t")): hits.append(path.name)
        if hits: raise SystemExit(f"promotion overlap for {evidence_id}: {hits}")
        audit.append({"evidence_id": evidence_id, "review_id": review_id, "pair_key": review["pair_key"], "pathway_reuse_key": reuse_key, "previous_tier": row["confidence_tier"], "new_tier": "high", "source_locators": row["source_locators"], "decision_basis": BASIS[number], "upstream_lr_confidence_unchanged": "true", "terminal_tf_status_unchanged": "true", "sql_materialization": "false"})
    if not args.apply:
        print(json.dumps({"validated": len(audit), "apply": False, "evidence_ids": [x["evidence_id"] for x in audit]}, indent=2)); return
    for number, review_id, reuse_key in PACKET:
        evidence_id = f"M21A-PAIR-EVID-{number}"; detail[evidence_id]["confidence_tier"] = "high"; detail[evidence_id]["limitations"] = once(detail[evidence_id]["limitations"])
        reviews[review_id]["confidence_tier"] = "high"; reviews[review_id]["curator_note"] = once(reviews[review_id]["curator_note"])
        if reuse_key: reuse[reuse_key]["validation_status"] = "promoted_high_batch117"; reuse[reuse_key]["limitations"] = once(reuse[reuse_key]["limitations"])
        coverage[evidence_id]["curator_notes"] = once(coverage[evidence_id]["curator_notes"])
    write(DETAIL, df, detail_rows); write(REUSE, uf, reuse_rows); write(PAIRS, pf, pair_rows)
    for path, (fields, rows) in zip(REVIEW_FILES, review_tables): write(path, fields, rows)
    fields = ["evidence_id", "review_id", "pair_key", "pathway_reuse_key", "previous_tier", "new_tier", "source_locators", "decision_basis", "upstream_lr_confidence_unchanged", "terminal_tf_status_unchanged", "sql_materialization"]
    write(AUDIT, fields, audit)
    SUMMARY.write_text(json.dumps({"promotion_id": "module21a-local-register-exact-pair-batch117-2026-09-02", "records_promoted": len(audit), "evidence_ids": [x["evidence_id"] for x in audit], "promotion_note": NOTE, "upstream_module20a_lr_confidence_changed": False, "terminal_tf_assignments_created": False, "sql_signaling_edges_created": False, "malformed_legacy_rows_touched": False}, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"validated": len(audit), "applied": len(audit), "evidence_ids": [x["evidence_id"] for x in audit]}, indent=2))


if __name__ == "__main__":
    main()
