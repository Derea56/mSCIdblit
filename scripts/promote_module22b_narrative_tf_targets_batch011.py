#!/usr/bin/env python3
"""Add additional primary-study TF target lanes from narrative hold review."""

from __future__ import annotations

import json
import re
from pathlib import Path

from promote_module22b_narrative_tf_targets_batch001 import (
    EDGE_FIELDS,
    EVIDENCE_FIELDS,
    read_tsv,
    write_tsv,
)


ROOT = Path(__file__).resolve().parents[1]
EDGE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
AUDIT_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch011.tsv"
SUMMARY_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch011_summary.json"
BATCH_ID = "module22b-narrative-tf-targets-batch011-2026-09-03"

UPDATES = [
    (
        "M22B-HOLD-AUDIT-0038;M22B-HOLD-AUDIT-0039;M22B-HOLD-AUDIT-0040;M22B-HOLD-AUDIT-0041",
        "JUN",
        "CCNA2",
        "rat",
        "PMID:15737994",
        "Rat1a cells with inducible c-Jun expression, cyclin A2 promoter reporter/mutation assays, and c-Jun ChIP.",
        "The primary study showed c-Jun binding directly to the cyclin A2 promoter and c-Jun-dependent cyclin A2 promoter activity and expression.",
        "This is a general rat c-Jun target-gene edge in a transformation model; it does not establish any of the reviewed BDNF, DMP1, MIF, or WNT5A handoffs or SCI activation.",
    ),
    (
        "M22B-HOLD-AUDIT-0038;M22B-HOLD-AUDIT-0039;M22B-HOLD-AUDIT-0040;M22B-HOLD-AUDIT-0041",
        "JUN;CEBPB",
        "TNF",
        "human",
        "PMID:9566900",
        "Human Jurkat and U937 myeloid-cell models with c-Jun/C/EBP-beta perturbation, TNF promoter reporter assays, and DNA-binding assays.",
        "The primary study showed cooperative c-Jun and C/EBP-beta activation of the human TNF promoter through an AP-1 site and increased cellular TNF output in U937 cells.",
        "The evidence supports the c-Jun/C/EBP-beta composite rather than an isolated c-Jun claim; it does not establish the reviewed upstream handoffs or SCI specificity.",
    ),
    (
        "M22B-HOLD-AUDIT-0038;M22B-HOLD-AUDIT-0039;M22B-HOLD-AUDIT-0040;M22B-HOLD-AUDIT-0041",
        "JUN;SP1",
        "CDKN1A",
        "human",
        "PMID:10506225",
        "Human HepG2 promoter-reporter and protein-interaction assays for c-Jun/Sp1-dependent CDKN1A transactivation.",
        "The primary study showed c-Jun-dependent transactivation of the human CDKN1A promoter through functional cooperation with Sp1.",
        "The edge is a c-Jun/Sp1 composite regulatory claim without direct c-Jun DNA binding at the promoter; it does not establish the reviewed upstream handoffs or SCI specificity.",
    ),
    (
        "M22B-HOLD-AUDIT-0087;M22B-HOLD-AUDIT-1711",
        "STAT5",
        "CD40LG",
        "human",
        "PMID:24500400",
        "Primary human CD4 T cells activated with IL-15, with STAT5 promoter ChIP, promoter mutagenesis, and STAT5 gain- and loss-of-function assays.",
        "The primary study showed STAT5 binding to the human CD40LG promoter and STAT5-dependent CD40LG transcription after IL-15-supported T-cell activation.",
        "This is a human T-cell STAT5 target-gene edge; it does not assign the submitted TSLP or IL-15 receptor handoff to a specific upstream branch or establish SCI specificity.",
    ),
    (
        "M22B-HOLD-AUDIT-0087;M22B-HOLD-AUDIT-1711",
        "STAT5",
        "MIR155HG",
        "human",
        "PMID:23676217",
        "Human cutaneous T-cell-lymphoma and primary T-cell models with STAT5 ChIP-seq, cytokine stimulation, and STAT5 knockdown.",
        "The primary study identified the BIC/MIR155HG promoter as a STAT5 target and showed STAT5-dependent expression after IL-2/IL-15 signaling.",
        "This is a human malignant/primary T-cell STAT5 target-gene edge; it does not assign the submitted TSLP or IL-15 receptor handoff to a specific upstream branch or establish SCI specificity.",
    ),
    (
        "M22B-HOLD-AUDIT-0087;M22B-HOLD-AUDIT-1711",
        "STAT5",
        "MIR21",
        "human",
        "PMID:27329723",
        "Human cutaneous T-cell-lymphoma models and patient-derived cells with STAT5 promoter ChIP, cytokine stimulation, and STAT5 depletion.",
        "The primary study showed direct STAT5 binding to the MIR21 promoter and STAT5-dependent MIR21 expression in cytokine-responsive malignant T cells.",
        "This is a human cutaneous T-cell STAT5 target-gene edge; it does not assign the submitted TSLP or IL-15 receptor handoff to a specific upstream branch or establish SCI specificity.",
    ),
    (
        "M22B-HOLD-AUDIT-0087;M22B-HOLD-AUDIT-1711",
        "STAT5",
        "Bcl2l1",
        "mouse",
        "PMID:28732065",
        "Mouse erythroid progenitors with EPO-induced pSTAT5 ChIP-seq, newly transcribed RNA sequencing, and target-gene validation.",
        "The primary study identified Bcl2l1 as a direct pSTAT5 target in mouse erythroid cells using promoter/enhancer occupancy and rapid transcriptional response.",
        "This is a mouse erythroid STAT5 target-gene edge; it does not assign the submitted TSLP or IL-15 receptor handoff to a specific upstream branch or establish SCI specificity.",
    ),
    (
        "M22B-HOLD-AUDIT-0087;M22B-HOLD-AUDIT-1711",
        "STAT5",
        "Pim1",
        "mouse",
        "PMID:28732065",
        "Mouse erythroid progenitors with EPO-induced pSTAT5 ChIP-seq, newly transcribed RNA sequencing, and target-gene validation.",
        "The primary study identified Pim1 as a direct pSTAT5 target in mouse erythroid cells using promoter/enhancer occupancy and rapid transcriptional response.",
        "This is a mouse erythroid STAT5 target-gene edge; it does not assign the submitted TSLP or IL-15 receptor handoff to a specific upstream branch or establish SCI specificity.",
    ),
    (
        "M22B-HOLD-AUDIT-0087;M22B-HOLD-AUDIT-1711",
        "STAT5",
        "Rbm25",
        "mouse",
        "PMID:28732065",
        "Mouse erythroid progenitors with EPO-induced pSTAT5 ChIP-seq, newly transcribed RNA sequencing, and target-gene validation.",
        "The primary study identified Rbm25 as a newly validated direct pSTAT5 target in mouse erythroid differentiation using occupancy and rapid transcriptional response.",
        "This is a mouse erythroid STAT5 target-gene edge; it does not assign the submitted TSLP or IL-15 receptor handoff to a specific upstream branch or establish SCI specificity.",
    ),
]


def next_id(rows: list[dict[str, str]], field: str) -> int:
    return max([int(match.group(1)) for row in rows if (match := re.search(r"(\d+)$", row[field]))] or [0]) + 1


def main() -> int:
    edges, evidence = read_tsv(EDGE_PATH), read_tsv(EVIDENCE_PATH)
    existing = {
        (
            row.get("species_context", "").casefold(),
            row.get("source_entity", "").casefold(),
            row.get("target_entity", "").casefold(),
        )
        for row in edges
        if row.get("pathway_name") == "target_gene"
    }
    edge_number, evidence_number = next_id(edges, "b_edge_id"), next_id(evidence, "b_evidence_id")
    audit: list[dict[str, str]] = []
    for index, (holds, tf, target, species, locator, context, summary, limitations) in enumerate(UPDATES, start=87):
        pair = (species.casefold(), tf.casefold(), target.casefold())
        if pair in existing:
            raise SystemExit(f"target pair already exists: {pair}")
        edge_id = f"M22B-E{edge_number:06d}"
        evidence_id = f"M22B-EVID-{evidence_number:06d}"
        edge_number += 1
        evidence_number += 1
        source_id = f"M22B-TARGET-SEARCH-{index:04d}"
        evidence_source_id = f"M22B-TARGET-SEARCH-EVID-{index:04d}"
        edges.append({
            "b_edge_id": edge_id,
            "source_entity": tf,
            "relation_type": f"{tf} activates the {target} target gene in primary-study evidence",
            "target_entity": target,
            "pathway_name": "target_gene",
            "evidence_layer": "ligand_receptor_or_direct_molecular",
            "source_a_edge_id": source_id,
            "edge_status": "reviewed_direct_target",
            "context_scope": context,
            "cell_type_context": context,
            "compartment_context": "unspecified",
            "species_context": species,
            "injury_context": "not_assessed",
            "confidence_tier": "high",
            "export_priority": "medium",
            "exportable": "true",
            "consolidation_note": f"{BATCH_ID}: standalone target edge found while reviewing {holds}; upstream handoff remains separate and unupgraded.",
        })
        evidence.append({
            "b_evidence_id": evidence_id,
            "source_a_evidence_id": evidence_source_id,
            "b_edge_ids": edge_id,
            "source_kind": "reviewed_direct_target",
            "source_locator": locator,
            "support_kind": "primary_experiment",
            "species_support": species,
            "source_scope": "direct_edge",
            "confidence_tier": "high",
            "citation_note": f"Primary-study target-gene evidence identified while reviewing hold rows {holds}; standalone general TF-regulon claim.",
            "evidence_summary": summary,
            "limitations": limitations,
            "evidence_layer": "ligand_receptor_or_direct_molecular",
            "exportable": "true",
            "consolidation_note": f"{BATCH_ID}: primary-study target-gene evidence; upstream handoff remains separate and unupgraded.",
        })
        audit.append({
            "batch_id": BATCH_ID,
            "hold_edges_reviewed": holds,
            "tf": tf,
            "target": target,
            "species": species,
            "b_edge_id": edge_id,
            "b_evidence_id": evidence_id,
            "source_locator": locator,
            "upstream_handoff_upgraded": "false",
            "standalone_target_gene_edge": "true",
            "decision_basis": summary,
        })
        existing.add(pair)

    audit_fields = [
        "batch_id", "hold_edges_reviewed", "tf", "target", "species", "b_edge_id",
        "b_evidence_id", "source_locator", "upstream_handoff_upgraded",
        "standalone_target_gene_edge", "decision_basis",
    ]
    write_tsv(AUDIT_PATH, audit, audit_fields)
    write_tsv(EDGE_PATH, edges, EDGE_FIELDS)
    write_tsv(EVIDENCE_PATH, evidence, EVIDENCE_FIELDS)
    summary = {
        "batch_id": BATCH_ID,
        "standalone_target_gene_edges_added": len(audit),
        "upstream_handoff_edges_upgraded": 0,
        "high_edges_after": sum(row["confidence_tier"] == "high" for row in edges),
        "exportable_edges_after": sum(row["exportable"] == "true" for row in edges),
        "target_gene_edges_after": sum(row["pathway_name"] == "target_gene" for row in edges),
        "upstream_activation_inferred": False,
        "audit": str(AUDIT_PATH),
    }
    SUMMARY_PATH.parent.mkdir(parents=True, exist_ok=True)
    SUMMARY_PATH.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
