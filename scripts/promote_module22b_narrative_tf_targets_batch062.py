#!/usr/bin/env python3
"""Add direct, reusable TF-to-target lanes found in holds 0341-0348."""

from __future__ import annotations

import json
import re
from pathlib import Path

from promote_module22b_narrative_tf_targets_batch001 import EDGE_FIELDS, EVIDENCE_FIELDS, read_tsv, write_tsv

ROOT = Path(__file__).resolve().parents[1]
EDGE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
AUDIT_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch062.tsv"
SUMMARY_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch062_summary.json"
BATCH_ID = "module22b-narrative-tf-targets-batch062-2026-09-04"

UPDATES = [
    {
        "holds": "M22B-HOLD-AUDIT-0341",
        "tf": "RUNX1",
        "target": "ITGA2",
        "species": "human",
        "locator": "PMID:30545930; PMCID:PMC6545826; DOI:10.3324/haematol.2018.188904",
        "context": "Human megakaryocyte studies identified ITGA2 as a RUNX1-regulated gene; RUNX1 bound the ITGA2 regulatory region in primary megakaryocytes and functional regulatory-region assays showed positive RUNX1 control. Non-SCI platelet comparator.",
        "summary": "Primary megakaryocyte RUNX1 occupancy and functional ITGA2 regulatory-region assays support direct RUNX1 activation of human ITGA2.",
        "limitations": "The study concerns familial platelet disorder and megakaryocyte differentiation and does not establish Chad-integrin signaling to RUNX1 or SCI activity.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0347",
        "tf": "CDX2",
        "target": "CLDN1",
        "species": "human",
        "locator": "PMID:22719836; PMCID:PMC3376107; DOI:10.1371/journal.pone.0037174",
        "context": "Human colon-cancer-cell experiments showed CDX2-dependent CLDN1 mRNA and promoter-reporter activation; ChIP confirmed CDX2 binding at the CLDN1 promoter and a CDX2 deletion analysis mapped a required activation domain. Non-SCI epithelial/cancer comparator.",
        "summary": "CDX2 promoter ChIP, gain-of-function expression, reporter activation, and domain analysis support direct CDX2 activation of human CLDN1.",
        "limitations": "The study concerns Wnt-linked colon epithelial regulation and does not establish claudin-1 homophilic signaling to CDX2 or SCI activity.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0347",
        "tf": "Trp63",
        "target": "Cldn1",
        "species": "mouse",
        "locator": "PMID:18648642; PMCID:PMC2453228; DOI:10.1371/journal.pone.0002715",
        "context": "Mouse primary keratinocyte and embryo studies showed p63 binding at the Cldn1 promoter, p63-dependent endogenous Cldn1 expression, and activation of a Cldn1 promoter reporter. Developmental epidermis comparator, not SCI.",
        "summary": "p63 promoter binding, loss-of-function expression data, and Cldn1 reporter activation support direct Trp63 activation of mouse Cldn1.",
        "limitations": "The study concerns epidermal development and uses an activation-stage epithelial model; it does not establish claudin-1 homophilic signaling to Trp63 or SCI activity.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0348",
        "tf": "GATA1",
        "target": "Cldn11",
        "species": "mouse",
        "locator": "PMID:17226765; DOI:10.1002/jcp.20970",
        "context": "Mouse claudin-11 promoter studies identified an overlapping GATA/NF-Y motif; GATA complexes bound the promoter in EMSA/ChIP experiments and GATA-dependent activation was reduced by TF-specific perturbation. Non-SCI seminiferous-epithelium comparator.",
        "summary": "Promoter binding and perturbation experiments support a GATA1-containing activating complex at the mouse Cldn11 promoter.",
        "limitations": "The source describes GATA-family activity in a cooperative GATA/NF-Y/CREB complex rather than isolating every GATA isoform in each assay; it does not establish claudin-11 homophilic signaling to GATA1 or SCI activity.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0348",
        "tf": "CREB1",
        "target": "Cldn11",
        "species": "mouse",
        "locator": "PMID:17226765; DOI:10.1002/jcp.20970",
        "context": "Mouse claudin-11 promoter studies identified CREB in an activating GATA/NF-Y/CREB complex; CREB bound the promoter in EMSA/ChIP experiments and TF-specific perturbation reduced activation. Non-SCI seminiferous-epithelium comparator.",
        "summary": "CREB promoter binding and TF-specific perturbation support direct CREB1-associated activation of mouse Cldn11 in a cooperative promoter complex.",
        "limitations": "The source reports CREB as part of a cooperative complex and does not isolate CREB1 from other CREB-family contributions; it does not establish claudin-11 homophilic signaling to CREB1 or SCI activity.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0348",
        "tf": "GATA2",
        "target": "CLDN11",
        "species": "human",
        "locator": "PMID:29747653; PMCID:PMC5946489; DOI:10.1186/s13046-018-0754-y",
        "context": "Human nasopharyngeal-carcinoma-cell promoter experiments identified GATA2 binding at a CLDN11 promoter motif; GATA2 expression increased promoter activity and mutation of the motif reduced activity. Non-SCI epithelial/cancer comparator.",
        "summary": "GATA2 promoter binding, site mutation, and reporter activation support direct GATA2 activation of human CLDN11.",
        "limitations": "The study concerns methylation-sensitive CLDN11 regulation in nasopharyngeal carcinoma and does not establish claudin-11 homophilic signaling to GATA2 or SCI activity.",
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
            "source_a_edge_id": f"M22B-TARGET-SEARCH-0341-{index:02d}",
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
            "source_a_evidence_id": f"M22B-TARGET-SEARCH-EVID-0341-{index:02d}",
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
