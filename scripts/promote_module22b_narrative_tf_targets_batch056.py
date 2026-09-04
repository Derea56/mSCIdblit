#!/usr/bin/env python3
"""Add direct, reusable TF-to-target lanes found in holds 0293-0300."""

from __future__ import annotations

import json
import re
from pathlib import Path

from promote_module22b_narrative_tf_targets_batch001 import EDGE_FIELDS, EVIDENCE_FIELDS, read_tsv, write_tsv

ROOT = Path(__file__).resolve().parents[1]
EDGE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
AUDIT_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch056.tsv"
SUMMARY_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch056_summary.json"
BATCH_ID = "module22b-narrative-tf-targets-batch056-2026-09-04"

UPDATES = [
    {
        "holds": "M22B-HOLD-AUDIT-0294;M22B-HOLD-AUDIT-0295",
        "tf": "CEBPB",
        "target": "Cd200r1",
        "species": "mouse",
        "locator": "PMID:22776069; PMCID:PMC3414764; DOI:10.1186/1742-2094-9-165",
        "context": "Primary mouse microglial and mixed-glial cultures and BV2 cells showed C/EBPbeta binding to the Cd200r1 promoter by qChIP and C/EBPbeta-dependent LPS-associated Cd200r1 repression; reactive-microglia/neuroinflammation comparator, non-SCI.",
        "summary": "C/EBPbeta promoter qChIP, knockout, overexpression, and expression perturbation support a direct repressive CEBPB-to-Cd200r1 target lane in mouse microglia.",
        "limitations": "The study concerns LPS-reactive microglia and Cd200r1 transcription, not CD200-Cd200r1l or CD200-Cd200r3 ligand-receptor signaling and not SCI. The standalone CEBPB-to-Cd200r1 lane is not transferred to either handoff.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0294;M22B-HOLD-AUDIT-0295",
        "tf": "NFKB1",
        "target": "CD200R1",
        "species": "human",
        "locator": "PMID:39294682; PMCID:PMC11409543; DOI:10.1186/s12974-024-03231-3",
        "context": "Human promoter-luciferase, EMSA, ChIP, NFKB1 knockdown/overexpression, and peripheral-blood evidence supported direct NFKB1 regulation of CD200R1; mouse NFKB1 knockout and MPTP neuroinflammation were used as comparator validation, non-SCI.",
        "summary": "NFKB1 promoter binding and loss- and gain-of-function evidence support a direct NFKB1-to-CD200R1 target lane in human microglial-regulatory evidence.",
        "limitations": "The study concerns CD200R1 expression regulation in Parkinson-related neuroinflammation and does not establish CD200 signaling through CD200R1L or CD200R3, nor SCI activity. The standalone NFKB1-to-CD200R1 lane is not transferred to either handoff.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0298",
        "tf": "RELA",
        "target": "Icam1",
        "species": "mouse",
        "locator": "PMID:26843107; PMCID:PMC5310569; DOI:10.1007/s12035-016-9742-4",
        "context": "Mouse Neuro2a neuronal-cell experiments showed CD40L-induced p65/RELA recruitment to the Icam1 promoter by ChIP-qPCR and reduced Icam1 transcription after p65 knockdown; neuronal comparator, non-SCI.",
        "summary": "CD40L stimulation, p65/RELA promoter ChIP, and p65 perturbation support a direct RELA-to-Icam1 target lane in mouse neuronal cells.",
        "limitations": "The source supports a CD40L-induced transcriptional complex and does not establish an SCI injury model or every component of the submitted CD40LG-CD40 handoff in vivo. The standalone RELA-to-Icam1 lane is recorded without changing the upstream hold.",
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
            "source_a_edge_id": f"M22B-TARGET-SEARCH-0293-{index:02d}",
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
            "source_a_evidence_id": f"M22B-TARGET-SEARCH-EVID-0293-{index:02d}",
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
            "consolidation_note": f"{BATCH_ID}: primary-study target-gene evidence; upstream handoffs remain separate and unupgraded.",
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
