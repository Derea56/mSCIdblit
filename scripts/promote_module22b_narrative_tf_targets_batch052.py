#!/usr/bin/env python3
"""Add a reusable CEBPB-to-CCL3 lane found while reviewing holds 0261-0268."""

from __future__ import annotations

import json
import re
from pathlib import Path

from promote_module22b_narrative_tf_targets_batch001 import EDGE_FIELDS, EVIDENCE_FIELDS, read_tsv, write_tsv

ROOT = Path(__file__).resolve().parents[1]
EDGE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
AUDIT_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch052.tsv"
SUMMARY_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch052_summary.json"
BATCH_ID = "module22b-narrative-tf-targets-batch052-2026-09-04"

UPDATE = {
    "holds": "M22B-HOLD-AUDIT-0267;M22B-HOLD-AUDIT-0268",
    "tf": "CEBPB",
    "target": "CCL3",
    "species": "human",
    "status": "reviewed_direct_target",
    "confidence": "high",
    "locator": "PMID:20702408; PMCID:PMC2963416; DOI:10.1074/jbc.M110.130377",
    "context": "Human articular-chondrocyte experiments showed C/EBPbeta binding to an IL-1-responsive CCL3 promoter element by EMSA and ChIP, with promoter mutation, C/EBPbeta overexpression, and siRNA perturbation changing CCL3 induction; cartilage-inflammation comparator, non-SCI.",
    "summary": "C/EBPbeta directly bound the human CCL3 promoter, and promoter mutation, C/EBPbeta overexpression, and C/EBPbeta siRNA altered IL-1beta-responsive CCL3 expression, supporting a direct CEBPB-to-CCL3 target lane.",
    "limitations": "The study concerns IL-1beta-responsive human chondrocytes and does not establish downstream signaling from Ccl3-Ackr2, Ccl3-Ccr1, or Ccl3-Ccr1l1. It is not an SCI receiver-cell experiment and does not establish that any submitted receptor branch activates CEBPB.",
}


def next_id(rows: list[dict[str, str]], field: str) -> int:
    return max([int(match.group(1)) for row in rows if (match := re.search(r"(\d+)$", row[field]))] or [0]) + 1


def main() -> int:
    edges, evidence = read_tsv(EDGE_PATH), read_tsv(EVIDENCE_PATH)
    pair = (UPDATE["species"].casefold(), UPDATE["tf"].casefold(), UPDATE["target"].casefold())
    existing = {
        (r.get("species_context", "").casefold(), r.get("source_entity", "").casefold(), r.get("target_entity", "").casefold())
        for r in edges if r.get("pathway_name") == "target_gene"
    }
    if pair in existing:
        raise SystemExit(f"target pair already exists: {pair}")
    edge_id = f"M22B-E{next_id(edges, 'b_edge_id'):06d}"
    evidence_id = f"M22B-EVID-{next_id(evidence, 'b_evidence_id'):06d}"
    edges.append({
        "b_edge_id": edge_id,
        "source_entity": UPDATE["tf"],
        "relation_type": "CEBPB regulates the CCL3 target gene in primary-study evidence",
        "target_entity": UPDATE["target"],
        "pathway_name": "target_gene",
        "evidence_layer": "ligand_receptor_or_direct_molecular",
        "source_a_edge_id": "M22B-TARGET-SEARCH-0267",
        "edge_status": UPDATE["status"],
        "context_scope": UPDATE["context"],
        "cell_type_context": UPDATE["context"],
        "compartment_context": "unspecified",
        "species_context": UPDATE["species"],
        "injury_context": "not_assessed",
        "confidence_tier": UPDATE["confidence"],
        "export_priority": "medium",
        "exportable": "true",
        "consolidation_note": f"{BATCH_ID}: standalone target edge found while reviewing {UPDATE['holds']}; upstream handoffs remain separate and unupgraded.",
    })
    evidence.append({
        "b_evidence_id": evidence_id,
        "source_a_evidence_id": "M22B-TARGET-SEARCH-EVID-0267",
        "b_edge_ids": edge_id,
        "source_kind": UPDATE["status"],
        "source_locator": UPDATE["locator"],
        "support_kind": "primary_experiment",
        "species_support": UPDATE["species"],
        "source_scope": "direct_edge",
        "confidence_tier": UPDATE["confidence"],
        "citation_note": f"Primary-study target-gene evidence identified while reviewing hold rows {UPDATE['holds']}; standalone general TF-regulon claim.",
        "evidence_summary": UPDATE["summary"],
        "limitations": UPDATE["limitations"],
        "evidence_layer": "ligand_receptor_or_direct_molecular",
        "exportable": "true",
        "consolidation_note": f"{BATCH_ID}: primary-study target-gene evidence; upstream handoffs remain separate and unupgraded.",
    })
    fields = ["batch_id", "hold_edges_reviewed", "tf", "target", "species", "b_edge_id", "b_evidence_id", "source_locator", "upstream_handoff_upgraded", "standalone_target_gene_edge", "decision_basis"]
    write_tsv(AUDIT_PATH, [{
        "batch_id": BATCH_ID,
        "hold_edges_reviewed": UPDATE["holds"],
        "tf": UPDATE["tf"],
        "target": UPDATE["target"],
        "species": UPDATE["species"],
        "b_edge_id": edge_id,
        "b_evidence_id": evidence_id,
        "source_locator": UPDATE["locator"],
        "upstream_handoff_upgraded": "false",
        "standalone_target_gene_edge": "true",
        "decision_basis": UPDATE["summary"],
    }], fields)
    write_tsv(EDGE_PATH, edges, EDGE_FIELDS)
    write_tsv(EVIDENCE_PATH, evidence, EVIDENCE_FIELDS)
    summary = {
        "batch_id": BATCH_ID,
        "standalone_target_gene_edges_added": 1,
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
