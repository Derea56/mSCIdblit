#!/usr/bin/env python3
"""Add reusable TF-target lanes found while reviewing holds 0245-0252."""

from __future__ import annotations

import json
import re
from pathlib import Path

from promote_module22b_narrative_tf_targets_batch001 import EDGE_FIELDS, EVIDENCE_FIELDS, read_tsv, write_tsv

ROOT = Path(__file__).resolve().parents[1]
EDGE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
AUDIT_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch050.tsv"
SUMMARY_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch050_summary.json"
BATCH_ID = "module22b-narrative-tf-targets-batch050-2026-09-04"

UPDATES = [
    {
        "holds": "M22B-HOLD-AUDIT-0245",
        "tf": "RelB",
        "target": "Ccl21a",
        "species": "mouse",
        "status": "reviewed_regulatory_support",
        "confidence": "medium-high",
        "locator": "PMID:20126461; PMCID:PMC2813291; DOI:10.1371/journal.pone.0008955",
        "context": "Murine renal tubular-cell experiments showed TWEAK-induced noncanonical NF-kB activation with nuclear RelB/p52 DNA binding; RelB siRNA prevented Ccl21a induction, and the pathway was associated with Ccl21a expression during experimental acute kidney injury; non-SCI injury comparator.",
        "summary": "TWEAK-induced Ccl21a expression in murine renal tubular cells required RelB, with nuclear RelB/p52 DNA-binding complexes and RelB-siRNA sensitivity supporting a RelB-linked Ccl21a regulatory lane.",
        "limitations": "The study supports pathway perturbation and DNA-binding-complex evidence rather than RelB occupancy at the endogenous Ccl21a locus. The stimulus is TWEAK and the injury model is renal AKI, not an SCI receiver-cell experiment; this standalone lane does not upgrade the Ccl21a-Ackr4 or Ccl21a-Ccr7 handoffs.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0245;M22B-HOLD-AUDIT-0247;M22B-HOLD-AUDIT-0250;M22B-HOLD-AUDIT-0252",
        "tf": "SP1",
        "target": "CCR7",
        "species": "human",
        "status": "reviewed_direct_target",
        "confidence": "high",
        "locator": "PMID:25797200; DOI:10.1016/j.humimm.2015.03.010",
        "context": "Human mature dendritic-cell experiments showed SP1 binding at the CCR7 promoter by ChIP and stimulation of CCR7 promoter activity in transfection assays; immune-trafficking comparator, non-SCI.",
        "summary": "SP1 bound the human CCR7 promoter and stimulated CCR7 promoter activity in mature dendritic-cell regulatory experiments, supporting a direct SP1-to-CCR7 target lane.",
        "limitations": "The study concerns CCR7 receptor expression in mature human dendritic cells, not downstream signaling from any CCL21 paralog–CCR7 handoff and not an SCI receiver-cell experiment. Promoter assays do not establish that a submitted Ccl21 paralog activates SP1.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0245;M22B-HOLD-AUDIT-0247;M22B-HOLD-AUDIT-0250;M22B-HOLD-AUDIT-0252",
        "tf": "SP3",
        "target": "CCR7",
        "species": "human",
        "status": "reviewed_direct_target",
        "confidence": "high",
        "locator": "PMID:25797200; DOI:10.1016/j.humimm.2015.03.010",
        "context": "Human mature dendritic-cell experiments showed SP3 binding at the CCR7 promoter by ChIP and stimulation of CCR7 promoter activity in transfection assays; immune-trafficking comparator, non-SCI.",
        "summary": "SP3 bound the human CCR7 promoter and stimulated CCR7 promoter activity in mature dendritic-cell regulatory experiments, supporting a direct SP3-to-CCR7 target lane.",
        "limitations": "The study concerns CCR7 receptor expression in mature human dendritic cells, not downstream signaling from any CCL21 paralog–CCR7 handoff and not an SCI receiver-cell experiment. Promoter assays do not establish that a submitted Ccl21 paralog activates SP3.",
    },
]


def next_id(rows: list[dict[str, str]], field: str) -> int:
    return max([int(match.group(1)) for row in rows if (match := re.search(r"(\d+)$", row[field]))] or [0]) + 1


def main() -> int:
    edges, evidence = read_tsv(EDGE_PATH), read_tsv(EVIDENCE_PATH)
    existing = {
        (r.get("species_context", "").casefold(), r.get("source_entity", "").casefold(), r.get("target_entity", "").casefold())
        for r in edges if r.get("pathway_name") == "target_gene"
    }
    edge_number, evidence_number = next_id(edges, "b_edge_id"), next_id(evidence, "b_evidence_id")
    audit = []
    for index, update in enumerate(UPDATES, start=250):
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
            "consolidation_note": f"{BATCH_ID}: standalone target edge found while reviewing {update['holds']}; upstream handoffs remain separate and unupgraded.",
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
            "citation_note": f"Primary-study target-gene evidence identified while reviewing hold rows {update['holds']}; standalone general TF-regulon claim.",
            "evidence_summary": update["summary"],
            "limitations": update["limitations"],
            "evidence_layer": "ligand_receptor_or_direct_molecular",
            "exportable": "true",
            "consolidation_note": f"{BATCH_ID}: primary-study target-gene evidence; upstream handoffs remain separate and unupgraded.",
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
