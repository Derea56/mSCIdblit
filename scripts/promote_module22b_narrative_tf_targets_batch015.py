#!/usr/bin/env python3
"""Add five primary-study TF target lanes recovered from remaining holds."""

from __future__ import annotations

import json
import re
from pathlib import Path

from promote_module22b_narrative_tf_targets_batch001 import EDGE_FIELDS, EVIDENCE_FIELDS, read_tsv, write_tsv

ROOT = Path(__file__).resolve().parents[1]
EDGE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
AUDIT_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch015.tsv"
SUMMARY_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch015_summary.json"
BATCH_ID = "module22b-narrative-tf-targets-batch015-2026-09-03"

UPDATES = [
    (
        "M22B-HOLD-AUDIT-0054;M22B-HOLD-AUDIT-0055;M22B-HOLD-AUDIT-0056;M22B-HOLD-AUDIT-0057;M22B-HOLD-AUDIT-0058;M22B-HOLD-AUDIT-0059;M22B-HOLD-AUDIT-0060;M22B-HOLD-AUDIT-0081",
        "RELA",
        "BIRC2",
        "human",
        "PMID:22249179",
        "Human HepG2 cells stimulated with TNF-alpha, with RelA/p65 promoter occupancy and transcriptional activation assays at NF-kB target loci; non-SCI comparator.",
        "The primary study detected RelA/p65 recruitment at the BIRC2 (c-IAP1) promoter and analyzed RelA-dependent NF-kB transcriptional activation in the stimulated cells.",
        "This is a general RELA target-gene edge from an inflammatory liver-cell model and does not establish any submitted ligand-specific RELA handoff or SCI specificity.",
    ),
    (
        "M22B-HOLD-AUDIT-0054;M22B-HOLD-AUDIT-0055;M22B-HOLD-AUDIT-0056;M22B-HOLD-AUDIT-0057;M22B-HOLD-AUDIT-0058;M22B-HOLD-AUDIT-0059;M22B-HOLD-AUDIT-0060;M22B-HOLD-AUDIT-0081",
        "RELA",
        "XIAP",
        "human",
        "PMID:22249179",
        "Human HepG2 cells stimulated with TNF-alpha, with RelA/p65 promoter occupancy and transcriptional activation assays at NF-kB target loci; non-SCI comparator.",
        "The primary study detected RelA/p65 recruitment at the XIAP promoter and analyzed RelA-dependent NF-kB transcriptional activation in the stimulated cells.",
        "This is a general RELA target-gene edge from an inflammatory liver-cell model and does not establish any submitted ligand-specific RELA handoff or SCI specificity.",
    ),
    (
        "M22B-HOLD-AUDIT-0083;M22B-HOLD-AUDIT-0084;M22B-HOLD-AUDIT-0085",
        "STAT3",
        "MYC",
        "human",
        "PMID:34525179",
        "Primary human acute-myeloid-leukemia stem-cell model with STAT3 perturbation, MYC promoter ChIP-PCR, and MYC expression analyses; non-SCI comparator.",
        "The primary study showed STAT3 binding at the MYC promoter and STAT3-dependent MYC expression in leukemia stem cells.",
        "This is a general human STAT3 target-gene edge from a leukemia model and does not establish the submitted PGLYRP1, RBP4, or OSM receptor handoffs or SCI specificity.",
    ),
    (
        "M22B-HOLD-AUDIT-0083;M22B-HOLD-AUDIT-0084;M22B-HOLD-AUDIT-0085",
        "STAT3",
        "LCN2",
        "human",
        "PMID:22851691",
        "Primary human macrophage inflammatory-response model with IL-10 stimulation, STAT3 promoter ChIP, and LCN2/NGAL expression analyses; non-SCI comparator.",
        "The primary study detected STAT3 occupancy at the LCN2 (NGAL) promoter and measured IL-10-associated LCN2 induction in macrophages.",
        "This is a general human STAT3 target-gene edge from an IL-10 macrophage model and does not establish the submitted PGLYRP1, RBP4, or OSM receptor handoffs or SCI specificity.",
    ),
    (
        "M22B-HOLD-AUDIT-0088",
        "TAZ;TEAD1",
        "ZEB1",
        "mouse",
        "PMID:20207963",
        "Primary mouse retinal pigment epithelial-cell model with TAZ/YAP promoter ChIP and TAZ knockdown during dedifferentiation; non-SCI comparator.",
        "The primary study showed TAZ–TEAD1-associated binding at the Zeb1 promoter and loss of Zeb1 induction after TAZ knockdown.",
        "This is a TAZ–TEAD1 complex target-gene edge from a retinal epithelial model and does not establish the submitted LAMA5-alpha6beta1 handoff or SCI specificity.",
    ),
]


def next_id(rows: list[dict[str, str]], field: str) -> int:
    return max([int(match.group(1)) for row in rows if (match := re.search(r"(\d+)$", row[field]))] or [0]) + 1


def main() -> int:
    edges, evidence = read_tsv(EDGE_PATH), read_tsv(EVIDENCE_PATH)
    existing = {(r.get("species_context", "").casefold(), r.get("source_entity", "").casefold(), r.get("target_entity", "").casefold()) for r in edges if r.get("pathway_name") == "target_gene"}
    edge_number, evidence_number = next_id(edges, "b_edge_id"), next_id(evidence, "b_evidence_id")
    audit = []
    for index, (holds, tf, target, species, locator, context, summary, limitations) in enumerate(UPDATES, start=105):
        pair = (species.casefold(), tf.casefold(), target.casefold())
        if pair in existing:
            raise SystemExit(f"target pair already exists: {pair}")
        edge_id, evidence_id = f"M22B-E{edge_number:06d}", f"M22B-EVID-{evidence_number:06d}"
        edge_number += 1
        evidence_number += 1
        edges.append({"b_edge_id": edge_id, "source_entity": tf, "relation_type": f"{tf} activates the {target} target gene in primary-study evidence", "target_entity": target, "pathway_name": "target_gene", "evidence_layer": "ligand_receptor_or_direct_molecular", "source_a_edge_id": f"M22B-TARGET-SEARCH-{index:04d}", "edge_status": "reviewed_direct_target", "context_scope": context, "cell_type_context": context, "compartment_context": "unspecified", "species_context": species, "injury_context": "not_assessed", "confidence_tier": "high", "export_priority": "medium", "exportable": "true", "consolidation_note": f"{BATCH_ID}: standalone target edge found while reviewing {holds}; upstream handoff remains separate and unupgraded."})
        evidence.append({"b_evidence_id": evidence_id, "source_a_evidence_id": f"M22B-TARGET-SEARCH-EVID-{index:04d}", "b_edge_ids": edge_id, "source_kind": "reviewed_direct_target", "source_locator": locator, "support_kind": "primary_experiment", "species_support": species, "source_scope": "direct_edge", "confidence_tier": "high", "citation_note": f"Primary-study target-gene evidence identified while reviewing hold rows {holds}; standalone general TF-regulon claim.", "evidence_summary": summary, "limitations": limitations, "evidence_layer": "ligand_receptor_or_direct_molecular", "exportable": "true", "consolidation_note": f"{BATCH_ID}: primary-study target-gene evidence; upstream handoff remains separate and unupgraded."})
        audit.append({"batch_id": BATCH_ID, "hold_edges_reviewed": holds, "tf": tf, "target": target, "species": species, "b_edge_id": edge_id, "b_evidence_id": evidence_id, "source_locator": locator, "upstream_handoff_upgraded": "false", "standalone_target_gene_edge": "true", "decision_basis": summary})
        existing.add(pair)
    fields = ["batch_id", "hold_edges_reviewed", "tf", "target", "species", "b_edge_id", "b_evidence_id", "source_locator", "upstream_handoff_upgraded", "standalone_target_gene_edge", "decision_basis"]
    write_tsv(AUDIT_PATH, audit, fields)
    write_tsv(EDGE_PATH, edges, EDGE_FIELDS)
    write_tsv(EVIDENCE_PATH, evidence, EVIDENCE_FIELDS)
    summary = {"batch_id": BATCH_ID, "standalone_target_gene_edges_added": len(audit), "upstream_handoff_edges_upgraded": 0, "high_edges_after": sum(r["confidence_tier"] == "high" for r in edges), "exportable_edges_after": sum(r["exportable"] == "true" for r in edges), "target_gene_edges_after": sum(r["pathway_name"] == "target_gene" for r in edges), "upstream_activation_inferred": False, "audit": str(AUDIT_PATH)}
    SUMMARY_PATH.parent.mkdir(parents=True, exist_ok=True)
    SUMMARY_PATH.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
