#!/usr/bin/env python3
"""Add direct, reusable TF-to-cadherin/CEACAM lanes found in holds 0317-0324."""

from __future__ import annotations

import json
import re
from pathlib import Path

from promote_module22b_narrative_tf_targets_batch001 import EDGE_FIELDS, EVIDENCE_FIELDS, read_tsv, write_tsv

ROOT = Path(__file__).resolve().parents[1]
EDGE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
AUDIT_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch060.tsv"
SUMMARY_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch060_summary.json"
BATCH_ID = "module22b-narrative-tf-targets-batch060-2026-09-04"

UPDATES = [
    {
        "holds": "M22B-HOLD-AUDIT-0318",
        "tf": "ERG",
        "target": "CDH5",
        "species": "human",
        "locator": "PMID:18195090; PMCID:PMC2275018; DOI:10.1182/blood-2007-08-105346",
        "context": "Human umbilical-vein endothelial-cell experiments showed ERG binding to the VE-cadherin promoter by ChIP, ERG-dependent promoter transactivation, and reduced CDH5 expression after ERG inhibition. Non-SCI endothelial comparator.",
        "summary": "ERG promoter ChIP, transactivation, and knockdown evidence support direct ERG activation of CDH5 in human endothelial cells.",
        "limitations": "The study concerns endothelial homeostasis and angiogenesis and does not establish CDH5-CDH5 signaling to ERG or SCI activity. The standalone ERG-to-CDH5 lane is not transferred to the CDH5 handoff.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0319;M22B-HOLD-AUDIT-0320;M22B-HOLD-AUDIT-0321;M22B-HOLD-AUDIT-0322;M22B-HOLD-AUDIT-0323;M22B-HOLD-AUDIT-0324",
        "tf": "SOX9",
        "target": "CEACAM1",
        "species": "human",
        "locator": "PMID:18794798; DOI:10.1038/onc.2008.331",
        "context": "Human colonic-cell studies showed SOX9 upregulation of CEACAM1, SOX9-binding sequences in the CEACAM1 promoter, and promoter binding by EMSA and ChIP; mouse intestinal SOX9 deletion reduced Ceacam1 expression. Non-SCI epithelial comparator.",
        "summary": "SOX9 promoter binding, expression perturbation, and coactivator-supported activation support direct SOX9 regulation of CEACAM1.",
        "limitations": "The study concerns colon epithelium and does not establish CEACAM1 interaction signaling to SOX9 or SCI activity. This standalone SOX9-to-CEACAM1 lane is reusable across the CEACAM1 interaction holds without assigning it to any upstream handoff.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0319;M22B-HOLD-AUDIT-0320;M22B-HOLD-AUDIT-0321;M22B-HOLD-AUDIT-0322;M22B-HOLD-AUDIT-0323;M22B-HOLD-AUDIT-0324",
        "tf": "ETS1",
        "target": "CEACAM1",
        "species": "human",
        "locator": "PMID:29558679; PMCID:PMC5909674; DOI:10.1016/j.neo.2018.01.012",
        "context": "Human melanoma-cell studies showed ETS1-dependent CEACAM1 promoter activity, loss of response after ETS1-site deletion or ETS1 phosphorylation mutation, and ETS1 overexpression-induced CEACAM1 mRNA and protein. Non-SCI melanoma comparator.",
        "summary": "ETS1 promoter-site dependence, reporter activation, and overexpression evidence support direct ETS1 regulation of CEACAM1 in human melanoma cells.",
        "limitations": "The study concerns BRAF-mutant melanoma and does not establish CEACAM1 interaction signaling to ETS1 or SCI activity. The standalone ETS1-to-CEACAM1 lane is not transferred to the CEACAM1 handoffs.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0319;M22B-HOLD-AUDIT-0320;M22B-HOLD-AUDIT-0321;M22B-HOLD-AUDIT-0322;M22B-HOLD-AUDIT-0323;M22B-HOLD-AUDIT-0324",
        "tf": "SOX10",
        "target": "Ceacam1",
        "species": "mouse",
        "locator": "PMID:36437876; PMCID:PMC9682343; DOI:10.1016/j.isci.2022.105524",
        "context": "Mouse melanoma-cell studies showed SOX10 knockdown reduced Ceacam1, SOX10 re-expression increased Ceacam1, a distal Ceacam1 promoter fragment was activated by SOX10, and SOX10 occupancy was detected by ChIP. Non-SCI melanoma comparator.",
        "summary": "SOX10 perturbation, distal promoter reporter activity, and ChIP occupancy support direct SOX10 activation of Ceacam1 in mouse melanoma cells.",
        "limitations": "The study concerns melanoma immune infiltration and stemness and does not establish CEACAM1 interaction signaling to SOX10 or SCI activity. The standalone SOX10-to-Ceacam1 lane is not transferred to the CEACAM1 handoffs.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0319;M22B-HOLD-AUDIT-0320;M22B-HOLD-AUDIT-0321;M22B-HOLD-AUDIT-0322;M22B-HOLD-AUDIT-0323;M22B-HOLD-AUDIT-0324",
        "tf": "USF1",
        "target": "CEACAM1",
        "species": "human",
        "locator": "PMID:21050451; PMCID:PMC2991322; DOI:10.1186/1471-2199-11-79",
        "context": "Human breast epithelial-cell studies identified USF1 binding at the active CEACAM1 promoter and showed that IFN-gamma increased USF1 promoter binding; USF1 RNAi reduced CEACAM1 protein. Non-SCI epithelial/inflammation comparator.",
        "summary": "USF1 promoter occupancy, IFN-gamma-linked promoter recruitment, and RNAi perturbation support direct USF1 regulation of CEACAM1 in human breast epithelial cells.",
        "limitations": "The study concerns breast epithelial CEACAM1 expression and context-dependent IFN-gamma induction; it does not establish CEACAM1 interaction signaling to USF1 or SCI activity. The standalone USF1-to-CEACAM1 lane is not transferred to the CEACAM1 handoffs.",
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
            "source_a_edge_id": f"M22B-TARGET-SEARCH-0317-{index:02d}",
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
            "source_a_evidence_id": f"M22B-TARGET-SEARCH-EVID-0317-{index:02d}",
            "b_edge_ids": edge_id,
            "source_kind": "reviewed_direct_target",
            "source_locator": update["locator"],
            "support_kind": "primary_experiment",
            "species_support": update["species"],
            "source_scope": "direct_edge",
            "confidence_tier": "high",
            "citation_note": f"Primary-study target-gene evidence identified while reviewing hold rows {update['holds']}; standalone general TF-regulon claim.",
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
