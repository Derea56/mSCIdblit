#!/usr/bin/env python3
"""Add target lanes recovered while reviewing Module 22B holds 0045-0048."""

from __future__ import annotations

import json
import re
from pathlib import Path

from promote_module22b_narrative_tf_targets_batch001 import EDGE_FIELDS, EVIDENCE_FIELDS, read_tsv, write_tsv

ROOT = Path(__file__).resolve().parents[1]
EDGE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
AUDIT_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch035.tsv"
SUMMARY_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch035_summary.json"
BATCH_ID = "module22b-narrative-tf-targets-batch035-2026-09-03"

UPDATES = [
    (
        "M22B-HOLD-AUDIT-0045",
        "NFATC1",
        "Ltbp3",
        "mouse",
        "PMID:19576893",
        "Primary mouse RANKL-induced osteoclast activation study with NFATC1 promoter-binding and expression assays; bone-resorption, non-SCI comparator.",
        "NFATc1 directly bound the mouse Ltbp3 promoter and induced Ltbp3 expression in the RANKL osteoclast model.",
        "This standalone NFATC1 target lane does not establish the submitted SEMA6A-PLXNA2-to-NFATC1 handoff or SCI specificity.",
    ),
    (
        "M22B-HOLD-AUDIT-0045",
        "NFATC1",
        "Clcn7",
        "mouse",
        "PMID:19576893",
        "Primary mouse RANKL-induced osteoclast activation study with NFATC1 promoter-binding and expression assays; bone-resorption, non-SCI comparator.",
        "NFATc1 directly bound the mouse Clcn7 (ClC7) promoter and induced Clcn7 expression in the RANKL osteoclast model.",
        "This standalone NFATC1 target lane does not establish the submitted SEMA6A-PLXNA2-to-NFATC1 handoff or SCI specificity.",
    ),
    (
        "M22B-HOLD-AUDIT-0045",
        "NFATC1",
        "Ctsk",
        "mouse",
        "PMID:19576893",
        "Primary mouse RANKL-induced osteoclast activation study with NFATC1 promoter-binding and expression assays; bone-resorption, non-SCI comparator.",
        "NFATc1 directly bound the mouse Ctsk promoter and induced cathepsin K/Ctsk expression in the RANKL osteoclast model.",
        "This standalone NFATC1 target lane does not establish the submitted SEMA6A-PLXNA2-to-NFATC1 handoff or SCI specificity.",
    ),
    (
        "M22B-HOLD-AUDIT-0045",
        "NFATC1",
        "Mmp9",
        "mouse",
        "PMID:19576893",
        "Primary mouse RANKL-induced osteoclast activation study with NFATC1 promoter-binding and expression assays; bone-resorption, non-SCI comparator.",
        "NFATc1 directly bound the mouse Mmp9 promoter and induced Mmp9 expression in the RANKL osteoclast model.",
        "This standalone NFATC1 target lane does not establish the submitted SEMA6A-PLXNA2-to-NFATC1 handoff or SCI specificity.",
    ),
    (
        "M22B-HOLD-AUDIT-0045",
        "NFATC1",
        "Src",
        "mouse",
        "PMID:19576893",
        "Primary mouse RANKL-induced osteoclast activation study with NFATC1 promoter-binding and expression assays; bone-resorption, non-SCI comparator.",
        "NFATc1 directly bound the mouse Src promoter and induced c-Src/Src expression in the RANKL osteoclast model.",
        "This standalone NFATC1 target lane does not establish the submitted SEMA6A-PLXNA2-to-NFATC1 handoff or SCI specificity.",
    ),
    (
        "M22B-HOLD-AUDIT-0047",
        "NR1I2",
        "UGT1A1",
        "human",
        "PMCID:PMC2651806",
        "Primary human hepatocyte study with rifampicin-treated PXR/NR1I2 ChIP, RNA polymerase II occupancy, expression, and PXR-silencing assays; hepatic xenobiotic-response, non-SCI comparator.",
        "PXR/NR1I2 binding and PXR-dependent expression were demonstrated for the human UGT1A1 locus in primary hepatocytes.",
        "This standalone NR1I2 target lane does not establish the submitted PXR-to-CYP11A1 route or SCI specificity; the induction is xenobiotic and hepatocyte context dependent.",
    ),
    (
        "M22B-HOLD-AUDIT-0047",
        "NR1I2",
        "ABCB1",
        "human",
        "PMCID:PMC2651806",
        "Primary human hepatocyte study with rifampicin-treated PXR/NR1I2 ChIP, RNA polymerase II occupancy, expression, and PXR-silencing assays; hepatic xenobiotic-response, non-SCI comparator.",
        "PXR/NR1I2 binding and PXR-dependent expression were demonstrated for the human ABCB1/MDR1 locus in primary hepatocytes.",
        "This standalone NR1I2 target lane does not establish the submitted PXR-to-CYP11A1 route or SCI specificity; the induction is xenobiotic and hepatocyte context dependent.",
    ),
    (
        "M22B-HOLD-AUDIT-0048",
        "NR3C2",
        "Sgk1",
        "mouse",
        "PMID:24491541; PMCID:PMC5488251",
        "Primary murine distal-convoluted-tubule study with aldosterone treatment, MR/NR3C2 ChIP-seq, microarray, RT-qPCR, and ChIP-qPCR; renal epithelial, non-SCI comparator.",
        "Aldosterone-responsive MR/NR3C2 binding and expression were validated at the mouse Sgk1 locus.",
        "This standalone NR3C2 target lane does not establish the submitted MR-to-CYP11B1 route or SCI specificity; the evidence is renal epithelial and aldosterone dependent.",
    ),
    (
        "M22B-HOLD-AUDIT-0048",
        "NR3C2",
        "Fkbp5",
        "mouse",
        "PMID:24491541; PMCID:PMC5488251",
        "Primary murine distal-convoluted-tubule study with aldosterone treatment, MR/NR3C2 ChIP-seq, microarray, RT-qPCR, and ChIP-qPCR; renal epithelial, non-SCI comparator.",
        "Aldosterone-responsive MR/NR3C2 binding and expression were validated at the mouse Fkbp5 locus.",
        "This standalone NR3C2 target lane does not establish the submitted MR-to-CYP11B1 route or SCI specificity; the evidence is renal epithelial and aldosterone dependent.",
    ),
    (
        "M22B-HOLD-AUDIT-0048",
        "NR3C2",
        "Rasl12",
        "mouse",
        "PMID:24491541; PMCID:PMC5488251",
        "Primary murine distal-convoluted-tubule study with aldosterone treatment, MR/NR3C2 ChIP-seq, microarray, RT-qPCR, and ChIP-qPCR; renal epithelial, non-SCI comparator.",
        "Aldosterone-responsive MR/NR3C2 binding and expression were validated at the mouse Rasl12 locus.",
        "This standalone NR3C2 target lane does not establish the submitted MR-to-CYP11B1 route or SCI specificity; the evidence is renal epithelial and aldosterone dependent.",
    ),
    (
        "M22B-HOLD-AUDIT-0048",
        "NR3C2",
        "Tns1",
        "mouse",
        "PMID:24491541; PMCID:PMC5488251",
        "Primary murine distal-convoluted-tubule study with aldosterone treatment, MR/NR3C2 ChIP-seq, microarray, RT-qPCR, and ChIP-qPCR; renal epithelial, non-SCI comparator.",
        "Aldosterone-responsive MR/NR3C2 binding and expression were validated at the mouse Tns1 locus.",
        "This standalone NR3C2 target lane does not establish the submitted MR-to-CYP11B1 route or SCI specificity; the evidence is renal epithelial and aldosterone dependent.",
    ),
    (
        "M22B-HOLD-AUDIT-0048",
        "NR3C2",
        "Tsc22d3",
        "mouse",
        "PMID:24491541; PMCID:PMC5488251",
        "Primary murine distal-convoluted-tubule study with aldosterone treatment, MR/NR3C2 ChIP-seq, microarray, RT-qPCR, and ChIP-qPCR; renal epithelial, non-SCI comparator.",
        "Aldosterone-responsive MR/NR3C2 binding and expression were validated at the mouse Tsc22d3/Gilz locus.",
        "This standalone NR3C2 target lane does not establish the submitted MR-to-CYP11B1 route or SCI specificity; the evidence is renal epithelial and aldosterone dependent.",
    ),
    (
        "M22B-HOLD-AUDIT-0048",
        "NR3C2",
        "EGFR",
        "human",
        "PMID:17311890; DOI:10.1152/ajpendo.00708.2006",
        "Primary human mineralocorticoid-receptor study using hMR-transfected HEK cells with human EGFR promoter reporter and ChIP assays; epithelial, non-SCI comparator.",
        "Aldosterone-activated human MR/NR3C2 interacted with the human EGFR promoter and stimulated EGFR expression in promoter-reporter and ChIP experiments.",
        "This standalone NR3C2 target lane does not establish the submitted MR-to-CYP11B1 route or SCI specificity; the evidence uses transfected epithelial cells and aldosterone stimulation.",
    ),
]


def next_id(rows: list[dict[str, str]], field: str) -> int:
    return max([int(match.group(1)) for row in rows if (match := re.search(r"(\d+)$", row[field]))] or [0]) + 1


def main() -> int:
    edges, evidence = read_tsv(EDGE_PATH), read_tsv(EVIDENCE_PATH)
    existing = {(r.get("species_context", "").casefold(), r.get("source_entity", "").casefold(), r.get("target_entity", "").casefold()) for r in edges if r.get("pathway_name") == "target_gene"}
    edge_number, evidence_number = next_id(edges, "b_edge_id"), next_id(evidence, "b_evidence_id")
    audit = []
    for index, (holds, tf, target, species, locator, context, summary, limitations) in enumerate(UPDATES, start=160):
        pair = (species.casefold(), tf.casefold(), target.casefold())
        if pair in existing:
            raise SystemExit(f"target pair already exists: {pair}")
        edge_id, evidence_id = f"M22B-E{edge_number:06d}", f"M22B-EVID-{evidence_number:06d}"
        edge_number += 1
        evidence_number += 1
        edges.append({"b_edge_id": edge_id, "source_entity": tf, "relation_type": f"{tf} activates the {target} target gene in primary-study evidence", "target_entity": target, "pathway_name": "target_gene", "evidence_layer": "ligand_receptor_or_direct_molecular", "source_a_edge_id": f"M22B-TARGET-SEARCH-{index:04d}", "edge_status": "reviewed_direct_target", "context_scope": context, "cell_type_context": context, "compartment_context": "unspecified", "species_context": species, "injury_context": "not_assessed", "confidence_tier": "high", "export_priority": "medium", "exportable": "true", "consolidation_note": f"{BATCH_ID}: standalone target edge found while reviewing {holds}; upstream handoff remains separate and unupgraded."})
        evidence.append({"b_evidence_id": evidence_id, "source_a_evidence_id": f"M22B-TARGET-SEARCH-EVID-{index:04d}", "b_edge_ids": edge_id, "source_kind": "reviewed_direct_target", "source_locator": locator, "support_kind": "primary_experiment", "species_support": species, "source_scope": "direct_edge", "confidence_tier": "high", "citation_note": f"Primary-study target-gene evidence identified while reviewing hold row {holds}; standalone general TF-regulon claim.", "evidence_summary": summary, "limitations": limitations, "evidence_layer": "ligand_receptor_or_direct_molecular", "exportable": "true", "consolidation_note": f"{BATCH_ID}: primary-study target-gene evidence; upstream handoff remains separate and unupgraded."})
        audit.append({"batch_id": BATCH_ID, "hold_edges_reviewed": holds, "tf": tf, "target": target, "species": species, "b_edge_id": edge_id, "b_evidence_id": evidence_id, "source_locator": locator, "upstream_handoff_upgraded": "false", "standalone_target_gene_edge": "true", "decision_basis": summary})
        existing.add(pair)
    fields = ["batch_id", "hold_edges_reviewed", "tf", "target", "species", "b_edge_id", "b_evidence_id", "source_locator", "upstream_handoff_upgraded", "standalone_target_gene_edge", "decision_basis"]
    write_tsv(AUDIT_PATH, audit, fields)
    write_tsv(EDGE_PATH, edges, EDGE_FIELDS)
    write_tsv(EVIDENCE_PATH, evidence, EVIDENCE_FIELDS)
    summary = {"batch_id": BATCH_ID, "standalone_target_gene_edges_added": len(audit), "upstream_handoff_edges_upgraded": 0, "high_edges_after": sum(r["confidence_tier"] == "high" for r in edges), "exportable_edges_after": sum(r["exportable"] == "true" for r in edges), "target_gene_edges_after": sum(r["pathway_name"] == "target_gene" for r in edges), "upstream_activation_inferred": False, "audit": str(AUDIT_PATH)}
    SUMMARY_PATH.parent.mkdir(parents=True, exist_ok=True)
    SUMMARY_PATH.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
