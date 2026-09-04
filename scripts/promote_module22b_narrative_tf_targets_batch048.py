#!/usr/bin/env python3
"""Add target lanes recovered while reviewing Module 22B holds 0181 through 0188."""

from __future__ import annotations

import json
import re
from pathlib import Path

from promote_module22b_narrative_tf_targets_batch001 import EDGE_FIELDS, EVIDENCE_FIELDS, read_tsv, write_tsv

ROOT = Path(__file__).resolve().parents[1]
EDGE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
AUDIT_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch048.tsv"
SUMMARY_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch048_summary.json"
BATCH_ID = "module22b-narrative-tf-targets-batch048-2026-09-03"

UPDATES = [
    {
        "holds": "M22B-HOLD-AUDIT-0183",
        "tf": "IRF1",
        "target": "BST2",
        "species": "human",
        "locator": "PMID:22301143; PMCID:PMC3302510; DOI:10.1128/JVI.06971-11",
        "status": "reviewed_regulatory_support",
        "confidence": "medium-high",
        "context": "Human BST2 promoter-reporter experiments in HEK293T and HeLa cells showed IRF1-dependent promoter activation, including under type-I-IFN-neutralized conditions; antiviral comparator, non-SCI.",
        "summary": "IRF1 expression activated the human BST2 promoter in reporter experiments, including when extracellular type-I-IFN signaling was neutralized, supporting an IRF1-linked BST2 regulatory lane.",
        "limitations": "The study provides promoter-reporter and perturbation support rather than endogenous IRF1 occupancy at the BST2 locus. It is upstream IRF regulation of BST2, not downstream signaling from the submitted BST2-PIRA2 handoff, and is not an SCI receiver-cell study.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0183",
        "tf": "IRF3",
        "target": "BST2",
        "species": "human",
        "locator": "PMID:22301143; PMCID:PMC3302510; DOI:10.1128/JVI.06971-11",
        "status": "reviewed_regulatory_support",
        "confidence": "medium-high",
        "context": "Human BST2 promoter-reporter experiments in HEK293T and HeLa cells showed activation by virus-activated IRF3, including under type-I-IFN-neutralized conditions; antiviral comparator, non-SCI.",
        "summary": "Virus-activated IRF3 stimulated the human BST2 promoter in reporter experiments under conditions that blocked extracellular type-I-IFN signaling, supporting an IRF3-linked BST2 regulatory lane.",
        "limitations": "The study provides promoter-reporter support rather than endogenous IRF3 occupancy at the BST2 locus. It is upstream IRF regulation of BST2, not downstream signaling from the submitted BST2-PIRA2 handoff, and is not an SCI receiver-cell study.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0183",
        "tf": "IRF7",
        "target": "BST2",
        "species": "human",
        "locator": "PMID:22301143; PMCID:PMC3302510; DOI:10.1128/JVI.06971-11",
        "status": "reviewed_regulatory_support",
        "confidence": "medium-high",
        "context": "Human BST2 promoter-reporter experiments in HEK293T and HeLa cells showed activation by virus-activated IRF7; complementary mouse embryonic-fibroblast infection experiments required IRF7 for BST2 induction; antiviral comparator, non-SCI.",
        "summary": "Virus-activated IRF7 stimulated the human BST2 promoter, and IRF7 was required for infection-induced Bst2 upregulation in mouse embryonic fibroblasts, supporting an IRF7-linked BST2 regulatory lane.",
        "limitations": "The human result is promoter-reporter support and the mouse result is pathway perturbation, not endogenous IRF7 occupancy at BST2. This is upstream IRF regulation of BST2, not downstream signaling from the submitted BST2-PIRA2 handoff, and is not an SCI receiver-cell study.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0186",
        "tf": "SMAD1",
        "target": "Id1",
        "species": "mouse",
        "locator": "PMID:19889495; DOI:10.1016/j.diff.2009.10.003",
        "status": "reviewed_regulatory_support",
        "confidence": "medium-high",
        "context": "Mouse Neuro2a neuroblastoma experiments showed BMP2-induced Smad1/5/8 phosphorylation and early Id1 induction, with Smad1 siRNA reducing the response; neural-differentiation comparator, non-SCI.",
        "summary": "BMP2-induced Id1 expression in mouse Neuro2a cells followed Smad1/5/8 activation and was reduced by Smad1 siRNA, supporting a Smad1-linked Id1 regulatory lane.",
        "limitations": "The study does not establish endogenous SMAD1 occupancy at the Id1 locus and uses pathway perturbation in a neuroblastoma model. It does not prove the submitted BMP2 receptor composite or an SCI receiver-cell endpoint.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0187",
        "tf": "SMAD1",
        "target": "Id2",
        "species": "mouse",
        "locator": "PMID:19889495; DOI:10.1016/j.diff.2009.10.003",
        "status": "reviewed_regulatory_support",
        "confidence": "medium-high",
        "context": "Mouse Neuro2a neuroblastoma experiments showed BMP2-induced Smad1/5/8 phosphorylation and early Id2 induction, with Smad1 siRNA reducing the response; neural-differentiation comparator, non-SCI.",
        "summary": "BMP2-induced Id2 expression in mouse Neuro2a cells followed Smad1/5/8 activation and was reduced by Smad1 siRNA, supporting a Smad1-linked Id2 regulatory lane.",
        "limitations": "The study does not establish endogenous SMAD1 occupancy at the Id2 locus and uses pathway perturbation in a neuroblastoma model. It does not prove the submitted BMP2 receptor composite or an SCI receiver-cell endpoint.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0188",
        "tf": "SMAD1",
        "target": "Id3",
        "species": "mouse",
        "locator": "PMID:19889495; DOI:10.1016/j.diff.2009.10.003",
        "status": "reviewed_regulatory_support",
        "confidence": "medium-high",
        "context": "Mouse Neuro2a neuroblastoma experiments showed BMP2-induced Smad1/5/8 phosphorylation and early Id3 induction, with Smad1 siRNA reducing the response; neural-differentiation comparator, non-SCI.",
        "summary": "BMP2-induced Id3 expression in mouse Neuro2a cells followed Smad1/5/8 activation and was reduced by Smad1 siRNA, supporting a Smad1-linked Id3 regulatory lane.",
        "limitations": "The study does not establish endogenous SMAD1 occupancy at the Id3 locus and uses pathway perturbation in a neuroblastoma model. It does not prove the submitted BMP2 receptor composite or an SCI receiver-cell endpoint.",
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
    edge_number, evidence_number = next_id(edges, "b_edge_id"), next_id(evidence, "b_evidence_id")
    audit = []
    for index, update in enumerate(UPDATES, start=221):
        pair = (update["species"].casefold(), update["tf"].casefold(), update["target"].casefold())
        if pair in existing:
            raise SystemExit(f"target pair already exists: {pair}")
        edge_id, evidence_id = f"M22B-E{edge_number:06d}", f"M22B-EVID-{evidence_number:06d}"
        edge_number += 1
        evidence_number += 1
        edges.append({
            "b_edge_id": edge_id,
            "source_entity": update["tf"],
            "relation_type": f"{update['tf']} regulates the {update['target']} target gene in primary-study evidence",
            "target_entity": update["target"],
            "pathway_name": "target_gene",
            "evidence_layer": "ligand_receptor_or_direct_molecular",
            "source_a_edge_id": f"M22B-TARGET-SEARCH-{index:04d}",
            "edge_status": update["status"],
            "context_scope": update["context"],
            "cell_type_context": update["context"],
            "compartment_context": "unspecified",
            "species_context": update["species"],
            "injury_context": "not_assessed",
            "confidence_tier": update["confidence"],
            "export_priority": "medium",
            "exportable": "true",
            "consolidation_note": f"{BATCH_ID}: standalone target edge found while reviewing {update['holds']}; upstream handoff remains separate and unupgraded.",
        })
        evidence.append({
            "b_evidence_id": evidence_id,
            "source_a_evidence_id": f"M22B-TARGET-SEARCH-EVID-{index:04d}",
            "b_edge_ids": edge_id,
            "source_kind": update["status"],
            "source_locator": update["locator"],
            "support_kind": "primary_experiment",
            "species_support": update["species"],
            "source_scope": "direct_edge",
            "confidence_tier": update["confidence"],
            "citation_note": f"Primary-study target-gene evidence identified while reviewing hold row {update['holds']}; standalone general TF-regulon claim.",
            "evidence_summary": update["summary"],
            "limitations": update["limitations"],
            "evidence_layer": "ligand_receptor_or_direct_molecular",
            "exportable": "true",
            "consolidation_note": f"{BATCH_ID}: primary-study target-gene evidence; upstream handoff remains separate and unupgraded.",
        })
        audit.append({
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
    fields = ["batch_id", "hold_edges_reviewed", "tf", "target", "species", "b_edge_id", "b_evidence_id", "source_locator", "upstream_handoff_upgraded", "standalone_target_gene_edge", "decision_basis"]
    write_tsv(AUDIT_PATH, audit, fields)
    write_tsv(EDGE_PATH, edges, EDGE_FIELDS)
    write_tsv(EVIDENCE_PATH, evidence, EVIDENCE_FIELDS)
    summary = {
        "batch_id": BATCH_ID,
        "standalone_target_gene_edges_added": len(audit),
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
