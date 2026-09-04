#!/usr/bin/env python3
"""Add direct, reusable TF-to-cadherin lanes found in holds 0309-0316."""

from __future__ import annotations

import json
import re
from pathlib import Path

from promote_module22b_narrative_tf_targets_batch001 import EDGE_FIELDS, EVIDENCE_FIELDS, read_tsv, write_tsv

ROOT = Path(__file__).resolve().parents[1]
EDGE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
AUDIT_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch059.tsv"
SUMMARY_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch059_summary.json"
BATCH_ID = "module22b-narrative-tf-targets-batch059-2026-09-04"

UPDATES = [
    {
        "holds": "M22B-HOLD-AUDIT-0315",
        "tf": "SMAD4",
        "target": "CDH2",
        "species": "human",
        "locator": "PMID:25264609; PMCID:PMC4180072; DOI:10.1371/journal.pone.0107948",
        "context": "Human pancreatic ductal epithelium experiments showed TGF-beta-dependent SMAD4 binding at four CDH2 promoter SBEs; reporter mutation and SMAD4 knockdown identified a required SBE for stimulated CDH2 transcription. Non-SCI epithelial/EMT comparator.",
        "summary": "SMAD4 promoter occupancy, SBE reporter analysis, and knockdown support direct SMAD4 activation of CDH2 in human ductal epithelium.",
        "limitations": "The study concerns TGF-beta-driven epithelial motility and does not establish CDH2-CDH2 signaling to SMAD4 or SCI activity. The standalone SMAD4-to-CDH2 lane is not transferred to the CDH2 handoff.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0316",
        "tf": "CEBPB",
        "target": "CDH3",
        "species": "human",
        "locator": "PMID:23405208; PMCID:PMC3566012; DOI:10.1371/journal.pone.0055749",
        "context": "Human breast-cancer-cell experiments showed C/EBPbeta isoform binding at conserved CDH3 promoter regions, promoter activation in luciferase assays, and modulation of P-cadherin after C/EBPbeta perturbation. Non-SCI cancer comparator.",
        "summary": "C/EBPbeta promoter binding, mutational analysis, reporter activation, and perturbation support direct CEBPB regulation of CDH3 in human breast cancer cells.",
        "limitations": "The study concerns P-cadherin regulation in breast cancer and does not establish CDH3-CDH3 signaling to CEBPB or SCI activity. Isoform-specific effects differ between promoter activation and protein output, so the lane is retained as a general CEBPB-to-CDH3 relationship.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0316",
        "tf": "HOXA9",
        "target": "CDH3",
        "species": "human",
        "locator": "PMID:25023983; PMCID:PMC4105245; DOI:10.1186/1476-4598-13-170",
        "context": "Human ovarian-cancer-cell experiments showed HOXA9 occupancy at two CDH3 promoter sites, HOXA9-dependent CDH3/P-cadherin expression, and functional dependence of aggregation and implantation phenotypes on P-cadherin. Non-SCI cancer comparator.",
        "summary": "HOXA9 promoter ChIP, gain/loss perturbation, and CDH3 rescue experiments support direct HOXA9 induction of CDH3 in human ovarian cancer cells.",
        "limitations": "The study concerns ovarian-cancer dissemination and does not establish CDH3-CDH3 signaling to HOXA9 or SCI activity. The standalone HOXA9-to-CDH3 lane is not transferred to the CDH3 handoff.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0314",
        "tf": "PAX3",
        "target": "Cdh15",
        "species": "mouse",
        "locator": "PMID:33869209; PMCID:PMC8047199; DOI:10.3389/fcell.2021.652652",
        "context": "Mouse embryonic myotome studies showed PAX3-dependent Cdh15/M-cadherin expression across Pax3 gain- and loss-of-function alleles and identified a regulatory peak whose PAX3 binding activated transcription. Developmental muscle comparator, not SCI.",
        "summary": "PAX3 occupancy at a Cdh15 regulatory peak and Pax3 gain/loss-of-function expression changes support a direct PAX3-to-Cdh15 target lane in mouse myotome development.",
        "limitations": "The study concerns embryonic myotome patterning and does not establish CDH15-CDH15 signaling to PAX3 or SCI activity. The standalone PAX3-to-Cdh15 lane is not transferred to the CDH15 handoff.",
    },
]


def next_id(rows: list[dict[str, str]], field: str) -> int:
    return max([int(match.group(1)) for row in rows if (match := re.search(r"(\d+)$", row[field]))] or [0]) + 1


def main() -> int:
    edges, evidence = read_tsv(EDGE_PATH), read_tsv(EVIDENCE_PATH)
    existing = {
        (r.get("species_context", "").casefold(), r.get("source_entity", "").casefold(), r.get("target_entity", "").casefold())
        for r in edges
        if r.get("pathway_name") == "target_gene"
    }
    edge_num = next_id(edges, "b_edge_id")
    evidence_num = next_id(evidence, "b_evidence_id")
    audit_rows = []
    for index, update in enumerate(UPDATES, start=1):
        pair = (update["species"].casefold(), update["tf"].casefold(), update["target"].casefold())
        if pair in existing:
            raise SystemExit(f"target pair already exists: {pair}")
        edge_id = f"M22B-E{edge_num:06d}"
        evidence_id = f"M22B-EVID-{evidence_num:06d}"
        edges.append({
            "b_edge_id": edge_id,
            "source_entity": update["tf"],
            "relation_type": f"{update['tf']} regulates the {update['target']} target gene in primary-study evidence",
            "target_entity": update["target"],
            "pathway_name": "target_gene",
            "evidence_layer": "ligand_receptor_or_direct_molecular",
            "source_a_edge_id": f"M22B-TARGET-SEARCH-0309-{index:02d}",
            "edge_status": "reviewed_direct_target",
            "context_scope": update["context"],
            "cell_type_context": update["context"],
            "compartment_context": "unspecified",
            "species_context": update["species"],
            "injury_context": "not_assessed",
            "confidence_tier": "high",
            "export_priority": "medium",
            "exportable": "true",
            "consolidation_note": f"{BATCH_ID}: standalone target edge found while reviewing {update['holds']}; upstream handoffs remain separate and unupgraded.",
        })
        evidence.append({
            "b_evidence_id": evidence_id,
            "source_a_evidence_id": f"M22B-TARGET-SEARCH-EVID-0309-{index:02d}",
            "b_edge_ids": edge_id,
            "source_kind": "reviewed_direct_target",
            "source_locator": update["locator"],
            "support_kind": "primary_experiment",
            "species_support": update["species"],
            "source_scope": "direct_edge",
            "confidence_tier": "high",
            "citation_note": f"Primary-study target-gene evidence identified while reviewing hold row {update['holds']}; standalone general TF-regulon claim.",
            "evidence_summary": update["summary"],
            "limitations": update["limitations"],
            "evidence_layer": "ligand_receptor_or_direct_molecular",
            "exportable": "true",
            "consolidation_note": f"{BATCH_ID}: primary-study target-gene evidence; upstream handoff remains separate and unupgraded.",
        })
        audit_rows.append({
            "batch_id": BATCH_ID,
            "hold_edges_reviewed": update["holds"],
            "tf": update["tf"],
            "target": update["target"],
            "species": update["species"],
            "b_edge_id": edge_id,
            "b_evidence_id": evidence_id,
            "source_locator": update["locator"],
            "upstream_handoff_upgraded": "false",
            "standalone_target_gene_edge": "true",
            "decision_basis": update["summary"],
        })
        existing.add(pair)
        edge_num += 1
        evidence_num += 1
    audit_fields = ["batch_id", "hold_edges_reviewed", "tf", "target", "species", "b_edge_id", "b_evidence_id", "source_locator", "upstream_handoff_upgraded", "standalone_target_gene_edge", "decision_basis"]
    write_tsv(AUDIT_PATH, audit_rows, audit_fields)
    write_tsv(EDGE_PATH, edges, EDGE_FIELDS)
    write_tsv(EVIDENCE_PATH, evidence, EVIDENCE_FIELDS)
    summary = {
        "batch_id": BATCH_ID,
        "standalone_target_gene_edges_added": len(UPDATES),
        "upstream_handoff_edges_upgraded": 0,
        "high_edges_after": sum(r["confidence_tier"] == "high" for r in edges),
        "medium_high_edges_after": sum(r["confidence_tier"] == "medium-high" for r in edges),
        "exportable_edges_after": sum(r["exportable"] == "true" for r in edges),
        "target_gene_edges_after": sum(r["pathway_name"] == "target_gene" for r in edges),
        "upstream_activation_inferred": False,
        "audit": str(AUDIT_PATH),
    }
    SUMMARY_PATH.parent.mkdir(parents=True, exist_ok=True)
    SUMMARY_PATH.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
