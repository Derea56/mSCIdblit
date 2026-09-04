#!/usr/bin/env python3
"""Add direct, reusable TF-to-target lanes found in holds 0349-0356."""

from __future__ import annotations

import json
import re
from pathlib import Path

from promote_module22b_narrative_tf_targets_batch001 import EDGE_FIELDS, EVIDENCE_FIELDS, read_tsv, write_tsv

ROOT = Path(__file__).resolve().parents[1]
EDGE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
AUDIT_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch063.tsv"
SUMMARY_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch063_summary.json"
BATCH_ID = "module22b-narrative-tf-targets-batch063-2026-09-04"

UPDATES = [
    {
        "holds": "M22B-HOLD-AUDIT-0349",
        "tf": "VDR",
        "target": "CLDN2",
        "species": "human",
        "locator": "PMID:26212084; PMCID:PMC4650691; DOI:10.1038/srep10642",
        "context": "Human intestinal epithelial-cell and mouse intestine experiments showed VDR binding at the CLDN2 promoter, a functional vitamin-D response element, promoter activation, and reduced CLDN2 after VDR loss. Non-SCI intestinal-barrier comparator.",
        "summary": "VDR promoter ChIP, functional response-element deletion, reporter activation, and VDR loss-of-function support direct VDR activation of human CLDN2.",
        "limitations": "The study concerns vitamin-D-dependent intestinal barrier regulation and does not establish Cldn2 homophilic signaling to VDR or SCI activity.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0350",
        "tf": "JUN",
        "target": "CLDN3",
        "species": "human",
        "locator": "PMID:28383479; PMCID:PMC5412349; DOI:10.3390/ijms18040765",
        "context": "Human colorectal-cell experiments showed c-Jun/AP-1 binding at multiple CLDN3 promoter sites by ChIP, promoter-reporter activation, and loss of activation after site mutation; c-Kit/JNK signaling increased c-Jun occupancy. Non-SCI epithelial/cancer comparator.",
        "summary": "c-Jun promoter ChIP, binding-site mutagenesis, and reporter activation support direct JUN activation of human CLDN3 in a stimulus-dependent AP-1 circuit.",
        "limitations": "The study concerns SCF/c-Kit/JNK signaling in intestinal epithelium and colorectal cancer and does not establish Cldn3 homophilic signaling to JUN or SCI activity.",
    },
    {
        "holds": "M22B-HOLD-AUDIT-0351;M22B-HOLD-AUDIT-0352;M22B-HOLD-AUDIT-0353;M22B-HOLD-AUDIT-0354;M22B-HOLD-AUDIT-0355;M22B-HOLD-AUDIT-0356",
        "tf": "RARA",
        "target": "KLRB1",
        "species": "human",
        "locator": "PMID:30397350; PMCID:PMC6474659; DOI:10.1038/s41590-018-0230-z",
        "context": "Human CD161-positive regulatory-T-cell studies showed that all-trans retinoic acid induced KLRB1/CD161 and increased RARA occupancy at the KLRB1 locus by ChIP-qPCR. Wound-repair/inflammatory-gut comparator, not SCI.",
        "summary": "ATRA-induced RARA occupancy at the human KLRB1 locus and induction of CD161 support a direct RARA-to-KLRB1 target lane.",
        "limitations": "The evidence is human KLRB1 regulation in retinoic-acid-responsive regulatory T cells and does not establish RARA regulation of the distinct mouse Klrb1a, Klrb1b, Klrb1c, or Klrb1f paralogs, nor CLEC2D/E signaling to RARA or SCI activity.",
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
            "source_a_edge_id": f"M22B-TARGET-SEARCH-0349-{index:02d}",
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
            "source_a_evidence_id": f"M22B-TARGET-SEARCH-EVID-0349-{index:02d}",
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
