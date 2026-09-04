#!/usr/bin/env python3
"""Add target lanes recovered while reviewing Module 22B holds 0085-0092."""

from __future__ import annotations

import json
import re
from pathlib import Path

from promote_module22b_narrative_tf_targets_batch001 import EDGE_FIELDS, EVIDENCE_FIELDS, read_tsv, write_tsv

ROOT = Path(__file__).resolve().parents[1]
EDGE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
AUDIT_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch043.tsv"
SUMMARY_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch043_summary.json"
BATCH_ID = "module22b-narrative-tf-targets-batch043-2026-09-03"

UPDATES = [
    {
        "holds": "M22B-HOLD-AUDIT-0085",
        "tf": "STAT3",
        "target": "SOCS3",
        "species": "rat",
        "locator": "PMID:18571793; PMCID:PMC2621074",
        "status": "reviewed_direct_target",
        "confidence": "high",
        "context": "Primary rat astrocyte experiments with oncostatin-M stimulation, STAT3 ChIP at the Socs3 promoter, STAT3 inhibition, and promoter transcription assays; CNS inflammatory/neuroprotection comparator, not traumatic SCI.",
        "summary": "Oncostatin M induced Socs3 in primary astrocytes, STAT3 was recruited to the Socs3 promoter, and STAT3 inhibition reduced the response, supporting Socs3 as a direct STAT3 target in an OSM cytokine model.",
        "limitations": "This standalone STAT3 target lane does not establish the submitted OSM-IL6ST/LIFR-to-STAT3 handoff in an SCI receiver cell; the astrocyte model supports OSM-linked regulation but not traumatic-SCI specificity.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0086",
        "tf": "STAT4",
        "target": "IFNG",
        "species": "human",
        "locator": "PMID:9558063",
        "status": "reviewed_direct_target",
        "confidence": "high",
        "context": "Primary human CD4-positive T-lymphocyte promoter and transcription assays with IL-12/IL-18 stimulation, in vivo footprinting, STAT4-site mutation, and IFNG promoter reporter analysis; T-helper differentiation comparator, non-SCI.",
        "summary": "IL-12 stimulation produced a STAT4 footprint at the human IFNG promoter, and mutation of the STAT4 site inhibited IL-12-dependent promoter activation, supporting IFNG as a direct STAT4 target.",
        "limitations": "This standalone STAT4 target lane does not establish the submitted IL-23 receptor-specific handoff in SCI; the direct promoter study used IL-12 and costimulation in primary human T cells rather than IL-23 or an SCI receiver cell.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0087",
        "tf": "STAT5",
        "target": "Il4",
        "species": "mouse",
        "locator": "PMCID:PMC6039124; GEO:GSE81384",
        "status": "reviewed_regulatory_support",
        "confidence": "medium-high",
        "context": "Primary mouse CD4-positive T-cell TSLP stimulation and differentiation experiments with STAT5 ChIP-seq, JAK2 inhibition, time-course expression, and TSLP receptor comparison; allergic T-helper-2 comparator, non-SCI.",
        "summary": "TSLP activated STAT5 in mouse CD4-positive T cells, STAT5 occupied regulatory regions associated with the Il4 locus, and TSLP-dependent early Il4 expression was blocked by JAK2 inhibition, supporting a STAT5-linked Il4 response.",
        "limitations": "This standalone STAT5 target lane does not establish the submitted TSLP-CRLF2/IL7R handoff in SCI; T-cell receptor and IL-4/GATA3 cooperativity contribute to the later cytokine program, so this is regulatory support rather than isolated STAT5 sufficiency.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0087",
        "tf": "STAT5",
        "target": "Il5",
        "species": "mouse",
        "locator": "PMCID:PMC6039124; GEO:GSE81384",
        "status": "reviewed_regulatory_support",
        "confidence": "medium-high",
        "context": "Primary mouse CD4-positive T-cell TSLP stimulation and differentiation experiments with STAT5 ChIP-seq, JAK2 inhibition, time-course expression, and TSLP receptor comparison; allergic T-helper-2 comparator, non-SCI.",
        "summary": "TSLP activated STAT5 in mouse CD4-positive T cells, STAT5 occupied regulatory regions associated with the Il5 locus, and TSLP-dependent Il5 induction was blocked by JAK2 inhibition, supporting a STAT5-linked Il5 response.",
        "limitations": "This standalone STAT5 target lane does not establish the submitted TSLP-CRLF2/IL7R handoff in SCI; T-cell receptor and IL-4/GATA3 cooperativity contribute to the later cytokine program, so this is regulatory support rather than isolated STAT5 sufficiency.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0087",
        "tf": "STAT5",
        "target": "Il13",
        "species": "mouse",
        "locator": "PMCID:PMC6039124; GEO:GSE81384",
        "status": "reviewed_regulatory_support",
        "confidence": "medium-high",
        "context": "Primary mouse CD4-positive T-cell TSLP stimulation and differentiation experiments with STAT5 ChIP-seq, JAK2 inhibition, time-course expression, and TSLP receptor comparison; allergic T-helper-2 comparator, non-SCI.",
        "summary": "TSLP activated STAT5 in mouse CD4-positive T cells, STAT5 occupied regulatory regions associated with the Il13 locus, and TSLP-dependent Il13 induction was blocked by JAK2 inhibition, supporting a STAT5-linked Il13 response.",
        "limitations": "This standalone STAT5 target lane does not establish the submitted TSLP-CRLF2/IL7R handoff in SCI; T-cell receptor and IL-4/GATA3 cooperativity contribute to the later cytokine program, so this is regulatory support rather than isolated STAT5 sufficiency.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0087",
        "tf": "STAT5",
        "target": "Il9",
        "species": "mouse",
        "locator": "PMCID:PMC6039124; GEO:GSE81384",
        "status": "reviewed_regulatory_support",
        "confidence": "medium-high",
        "context": "Primary mouse CD4-positive T-cell TSLP stimulation and differentiation experiments with STAT5 ChIP-seq, JAK2 inhibition, time-course expression, and TSLP receptor comparison; allergic T-helper-2 comparator, non-SCI.",
        "summary": "The TSLP CD4-positive T-cell study identified STAT5 binding in regulatory regions associated with the Il9 locus within the TSLP-programmed T-helper-2 cytokine response.",
        "limitations": "This standalone STAT5 target lane does not establish the submitted TSLP-CRLF2/IL7R handoff in SCI; the Il9 assignment is based on locus-associated STAT5 binding in the programmed T-helper-2 model rather than a single-locus STAT5 perturbation.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0088",
        "tf": "TAZ;TEAD",
        "target": "CTGF",
        "species": "human",
        "locator": "PMID:19324877; PMCID:PMC2679435",
        "status": "reviewed_direct_target",
        "confidence": "high",
        "context": "Human mammalian-cell TAZ/TEAD perturbation experiments with CTGF promoter reporter assays, TAZ ChIP, TEAD dominant-negative inhibition, and endogenous expression analysis; epithelial/cancer comparator, non-SCI.",
        "summary": "TAZ bound the human CTGF promoter, activated CTGF transcription, and required TEAD interaction for promoter activity, establishing CTGF as a direct TAZ-TEAD target.",
        "limitations": "This standalone TAZ-TEAD target lane does not establish the submitted LAMA5-alpha6beta1-to-TAZ/TEAD handoff in SCI; the evidence is from mammalian epithelial/cancer models and does not resolve integrin-specific upstream activation.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0088",
        "tf": "TAZ;TEAD",
        "target": "CYR61",
        "species": "human",
        "locator": "PMID:21349946",
        "status": "reviewed_direct_target",
        "confidence": "high",
        "context": "Human mammary-cell TAZ/TEAD perturbation experiments with promoter reporter mutation, TAZ/TEAD interaction disruption, expression profiling, and promoter occupancy evidence; breast-cancer comparator, non-SCI.",
        "summary": "TAZ/TEAD interaction was required for activation of the human CYR61 promoter, and promoter response was lost after mutation of the TEAD response element, supporting CYR61 as a direct TAZ-TEAD target.",
        "limitations": "This standalone TAZ-TEAD target lane does not establish the submitted LAMA5-alpha6beta1-to-TAZ/TEAD handoff in SCI; the evidence is from mammary cancer cells and does not resolve integrin-specific upstream activation.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0090",
        "tf": "TCF/LEF family",
        "target": "Axin2",
        "species": "mouse",
        "locator": "PMID:11809808; PMCID:PMC134648",
        "status": "reviewed_direct_target",
        "confidence": "high",
        "context": "Primary mouse embryonic-tissue and cultured-cell Wnt experiments with Axin2 promoter/first-intron reporters, TCF/LEF-site mutation, beta-catenin induction, and in vitro DNA-binding assays; developmental comparator, non-SCI.",
        "summary": "Wnt activation induced mouse Axin2, and mutation or deletion of conserved TCF/LEF sites in the Axin2 promoter/first intron greatly reduced beta-catenin-dependent transcription, supporting Axin2 as a direct TCF/LEF-family target.",
        "limitations": "This standalone TCF/LEF target lane does not establish the submitted WNT7A-RECK-to-TCF/LEF handoff in SCI; receptor and ligand specificity were not isolated in the Axin2 promoter study.",
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
    for index, update in enumerate(UPDATES, start=206):
        pair = (update["species"].casefold(), update["tf"].casefold(), update["target"].casefold())
        if pair in existing:
            raise SystemExit(f"target pair already exists: {pair}")
        edge_id, evidence_id = f"M22B-E{edge_number:06d}", f"M22B-EVID-{evidence_number:06d}"
        edge_number += 1
        evidence_number += 1
        edges.append({
            "b_edge_id": edge_id,
            "source_entity": update["tf"],
            "relation_type": f"{update['tf']} activates the {update['target']} target gene in primary-study evidence",
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
