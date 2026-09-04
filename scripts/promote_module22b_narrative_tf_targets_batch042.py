#!/usr/bin/env python3
"""Add target lanes recovered while reviewing Module 22B holds 0077-0084."""

from __future__ import annotations

import json
import re
from pathlib import Path

from promote_module22b_narrative_tf_targets_batch001 import EDGE_FIELDS, EVIDENCE_FIELDS, read_tsv, write_tsv

ROOT = Path(__file__).resolve().parents[1]
EDGE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
AUDIT_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch042.tsv"
SUMMARY_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch042_summary.json"
BATCH_ID = "module22b-narrative-tf-targets-batch042-2026-09-03"

UPDATES = [
    {
        "holds": "M22B-HOLD-AUDIT-0077",
        "tf": "SOX2",
        "target": "Sox6",
        "species": "chicken",
        "locator": "PMID:24501124; PMCID:PMC3932859",
        "status": "reviewed_direct_target",
        "confidence": "high",
        "context": "Primary developing chicken neural-tube experiments with Sox2 ChIP-on-chip, in ovo Sox2 gain/repression, Sox6 expression analysis, and neural-progenitor differentiation assays; developmental CNS/spinal-cord comparator, not traumatic SCI.",
        "summary": "Sox2 ChIP-on-chip identified Sox6 as a candidate target, and in ovo chicken neural-tube gain- and loss-of-function experiments showed that Sox2 promotes Sox6 expression as a direct regulatory target.",
        "limitations": "This standalone SOX2 target lane does not establish the submitted ECM1-ITGB4-to-SOX2 handoff in SCI; the evidence is developmental chicken CNS and does not resolve the upstream integrin route.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0077",
        "tf": "SOX2",
        "target": "Socs3",
        "species": "mouse",
        "locator": "PMID:30849367; PMCID:PMC6506828",
        "status": "reviewed_regulatory_support",
        "confidence": "medium-high",
        "context": "Primary mouse brain-derived neural-stem-cell experiments with SOX2 ChIP, Pol II ChIA-PET, SOX2 deletion, transcript profiling, and Socs3 rescue; neural-stem-cell comparator, not traumatic SCI.",
        "summary": "SOX2-bound distal enhancer-promoter interactions were associated with Socs3 expression in mouse neural stem cells, Sox2 ablation reduced the connected gene program, and Socs3 overexpression rescued the self-renewal defect, supporting a functional SOX2-Socs3 regulatory lane.",
        "limitations": "This standalone SOX2 lane does not establish the submitted ECM1-ITGB4-to-SOX2 handoff in SCI; enhancer-to-gene regulation is supported by chromatin connectivity and rescue rather than a single promoter-occupancy assay.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0078",
        "tf": "STAT1",
        "target": "Jmjd3",
        "species": "rat",
        "locator": "PMID:24097101; PMCID:PMC3940857",
        "status": "reviewed_direct_target",
        "confidence": "high",
        "context": "Primary rat microglial cultures stimulated with LPS, phospho-STAT1 ChIP-chip and ChIP-PCR, transcript profiling, STAT1 knockdown, and constitutively active STAT1 experiments; CNS inflammatory comparator with ischemic-brain comparison, not traumatic SCI.",
        "summary": "Phospho-STAT1 occupied the rat Jmjd3 promoter in LPS-stimulated microglia, ChIP-PCR confirmed binding, and STAT1 perturbation altered Jmjd3 induction, supporting Jmjd3 as a direct STAT1 target.",
        "limitations": "This standalone STAT1 target lane does not establish the submitted IL-9-receptor-specific STAT1 handoff in SCI; Jmjd3 regulation also involves STAT3 and NF-kappaB in the microglial inflammatory model.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0083",
        "tf": "STAT3",
        "target": "Jmjd3",
        "species": "rat",
        "locator": "PMID:24097101; PMCID:PMC3940857",
        "status": "reviewed_direct_target",
        "confidence": "high",
        "context": "Primary rat microglial cultures stimulated with LPS, phospho-STAT3 ChIP-chip and ChIP-PCR, transcript profiling, STAT3 knockdown, and constitutively active STAT3 experiments; CNS inflammatory comparator with ischemic-brain comparison, not traumatic SCI.",
        "summary": "Phospho-STAT3 occupied the rat Jmjd3 promoter in LPS-stimulated microglia, ChIP-PCR confirmed binding, and STAT3 perturbation altered Jmjd3 induction, supporting Jmjd3 as a direct STAT3 target.",
        "limitations": "This standalone STAT3 target lane does not establish the submitted PGLYRP1-Trem1 handoff in SCI; Jmjd3 regulation also involves STAT1 and NF-kappaB in the microglial inflammatory model.",
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
    for index, update in enumerate(UPDATES, start=202):
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
