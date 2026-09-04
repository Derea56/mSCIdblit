#!/usr/bin/env python3
"""Add direct, reusable TF-to-target lanes found in holds 0333-0340."""

from __future__ import annotations

import json
import re
from pathlib import Path

from promote_module22b_narrative_tf_targets_batch001 import EDGE_FIELDS, EVIDENCE_FIELDS, read_tsv, write_tsv

ROOT = Path(__file__).resolve().parents[1]
EDGE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
AUDIT_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch061.tsv"
SUMMARY_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch061_summary.json"
BATCH_ID = "module22b-narrative-tf-targets-batch061-2026-09-04"

UPDATES = [
    {
        "holds": "M22B-HOLD-AUDIT-0337",
        "tf": "RUNX3",
        "target": "Cd8a",
        "species": "mouse",
        "locator": "PMID:22025728; PMCID:PMC3215065; DOI:10.1073/pnas.1105835108",
        "context": "Mouse activated CD8-positive T-cell studies showed that Runx3/CBFbeta complexes bound the Cd8ab locus; E8I-, Runx3-, or CBFbeta-deficient activated CD8-positive T cells down-regulated Cd8a, supporting Runx3-dependent establishment of the Cd8a regulatory circuit. Non-SCI immune comparator.",
        "summary": "Runx3/CBFbeta locus binding and Runx3 loss-of-function down-regulation support direct RUNX3 regulation of Cd8a during mouse CD8-positive T-cell activation.",
        "limitations": "The study concerns enhancer-dependent Cd8a programming during activated T-cell differentiation and reports factor-independent maintenance after activation; it does not establish Ceacam2 signaling to RUNX3 or SCI activity.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0340",
        "tf": "RELA",
        "target": "SELE",
        "species": "human",
        "locator": "PMID:7523851; PMCID:PMC359176; DOI:10.1128/mcb.14.10.6464-6475.1994",
        "context": "Human endothelial-cell promoter experiments identified multiple NF-kappaB sites in the E-selectin/SELE promoter; mutations that reduced NF-kappaB binding abolished cytokine-induced SELE expression, with HMG-I(Y) supporting NF-kappaB promoter binding. Non-SCI inflammatory endothelial comparator.",
        "summary": "NF-kappaB-site mutagenesis and promoter DNA-binding experiments support RELA/NF-kappaB-dependent activation of human SELE in cytokine-stimulated endothelial cells.",
        "limitations": "The paper tests NF-kappaB complexes rather than isolating RELA as the sole subunit and uses cytokine-stimulated endothelial cells; it does not establish Ceacam2 signaling to RELA or SCI activity.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0333;M22B-HOLD-AUDIT-0334;M22B-HOLD-AUDIT-0335;M22B-HOLD-AUDIT-0336",
        "tf": "ETS1",
        "target": "CD209",
        "species": "human",
        "locator": "PMID:22675249; PMCID:PMC3363004; DOI:10.1155/2012/357060",
        "context": "Human THP-1 monocyte/macrophage-model experiments showed IL-4-induced CD209/DC-SIGN expression and loss of CD209 promoter activity after deletion of the Ets-1 binding site. Non-SCI myeloid inflammatory comparator; the target is human CD209, not the distinct mouse Cd209b-e paralogs.",
        "summary": "Ets-1-site deletion in a human CD209 promoter reporter strongly reduced IL-4-induced promoter activity, supporting a reusable ETS1-to-CD209 target lane.",
        "limitations": "This is human CD209/DC-SIGN promoter evidence in a THP-1 model and does not establish ETS1 regulation of the distinct mouse Cd209b, Cd209c, Cd209d, or Cd209e paralogs, nor Ceacam2 signaling to ETS1 or SCI activity.",
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
            "source_a_edge_id": f"M22B-TARGET-SEARCH-0333-{index:02d}",
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
            "source_a_evidence_id": f"M22B-TARGET-SEARCH-EVID-0333-{index:02d}",
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
