#!/usr/bin/env python3
"""Add target lanes recovered while reviewing Module 22B holds 0041-0044."""

from __future__ import annotations

import json
import re
from pathlib import Path

from promote_module22b_narrative_tf_targets_batch001 import EDGE_FIELDS, EVIDENCE_FIELDS, read_tsv, write_tsv

ROOT = Path(__file__).resolve().parents[1]
EDGE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
AUDIT_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch034.tsv"
SUMMARY_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch034_summary.json"
BATCH_ID = "module22b-narrative-tf-targets-batch034-2026-09-03"

UPDATES = [
    (
        "M22B-HOLD-AUDIT-0042",
        "MYOD",
        "TEAD2",
        "mouse",
        "PMID:16267055; PMCID:PMC1892582",
        "Primary mouse skeletal-muscle myoblast/myotube and regeneration study with MyoD ChIP at the Tead2 first intron and E-box reporter/mutation assays; muscle regeneration, non-SCI comparator.",
        "MyoD directly bound and activated a regulatory region in the mouse Tead2 locus during myogenic differentiation and regeneration.",
        "This standalone MYOD target lane does not establish the submitted FGF6-FGFR4-to-MYOD/MYOG handoff or SCI specificity.",
    ),
    (
        "M22B-HOLD-AUDIT-0043",
        "NANOG",
        "FOXM1",
        "mouse",
        "PMID:29476172; PMCID:PMC5824884",
        "Primary mouse cerebellar neural-stem-cell study with Nanog ChIP-qPCR, Foxm1 promoter reporter/mutation assays, and Nanog perturbation; neural-stem-cell, non-SCI comparator.",
        "Nanog occupied and activated the mouse Foxm1 promoter in neural stem cells, linking Nanog to Foxm1 transcription.",
        "This standalone NANOG target lane does not establish the submitted EFNA4-EPHA10-to-NANOG handoff or SCI specificity.",
    ),
    (
        "M22B-HOLD-AUDIT-0044",
        "NFATC3",
        "SFTPB",
        "mouse",
        "PMID:16998587; PMCID:PMC1570374",
        "Primary mouse lung-epithelial/perinatal-lung study with NFATC3 promoter binding by ChIP and Sftpb promoter reporter and pathway perturbation assays; non-SCI comparator.",
        "NFATC3 directly bound and activated the mouse Sftpb promoter as part of calcineurin/NFAT control of lung surfactant genes.",
        "This standalone NFATC3 target lane represents a specific NFAT-family member and does not establish the submitted FGF23-FGFR4-to-NFAT handoff or SCI specificity.",
    ),
    (
        "M22B-HOLD-AUDIT-0044",
        "NFATC3",
        "ABCA3",
        "mouse",
        "PMID:16998587; PMCID:PMC1570374",
        "Primary mouse lung-epithelial/perinatal-lung study with NFATC3-dependent Abca3 promoter activation and calcineurin/NFAT pathway perturbation; non-SCI comparator.",
        "NFATC3 activated the mouse Abca3 promoter in the calcineurin/NFAT lung-maturation model.",
        "This standalone NFATC3 target lane represents a specific NFAT-family member and does not establish the submitted FGF23-FGFR4-to-NFAT handoff or SCI specificity.",
    ),
]


def next_id(rows: list[dict[str, str]], field: str) -> int:
    return max([int(match.group(1)) for row in rows if (match := re.search(r"(\d+)$", row[field]))] or [0]) + 1


def main() -> int:
    edges, evidence = read_tsv(EDGE_PATH), read_tsv(EVIDENCE_PATH)
    existing = {(r.get("species_context", "").casefold(), r.get("source_entity", "").casefold(), r.get("target_entity", "").casefold()) for r in edges if r.get("pathway_name") == "target_gene"}
    edge_number, evidence_number = next_id(edges, "b_edge_id"), next_id(evidence, "b_evidence_id")
    audit = []
    for index, (holds, tf, target, species, locator, context, summary, limitations) in enumerate(UPDATES, start=156):
        pair = (species.casefold(), tf.casefold(), target.casefold())
        if pair in existing:
            raise SystemExit(f"target pair already exists: {pair}")
        edge_id, evidence_id = f"M22B-E{edge_number:06d}", f"M22B-EVID-{evidence_number:06d}"
        edge_number += 1
        evidence_number += 1
        edges.append({"b_edge_id": edge_id, "source_entity": tf, "relation_type": f"{tf} activates the {target} target gene in primary-study evidence", "target_entity": target, "pathway_name": "target_gene", "evidence_layer": "ligand_receptor_or_direct_molecular", "source_a_edge_id": f"M22B-TARGET-SEARCH-{index:04d}", "edge_status": "reviewed_direct_target", "context_scope": context, "cell_type_context": context, "compartment_context": "unspecified", "species_context": species, "injury_context": "not_assessed", "confidence_tier": "high", "export_priority": "medium", "exportable": "true", "consolidation_note": f"{BATCH_ID}: standalone target edge found while reviewing {holds}; upstream handoff remains separate and unupgraded."})
        evidence.append({"b_evidence_id": evidence_id, "source_a_evidence_id": f"M22B-TARGET-SEARCH-EVID-{index:04d}", "b_edge_ids": edge_id, "source_kind": "reviewed_direct_target", "source_locator": locator, "support_kind": "primary_experiment", "species_support": species, "source_scope": "direct_edge", "confidence_tier": "high", "citation_note": f"Primary-study target-gene evidence identified while reviewing hold row {holds}; standalone general TF-regulon claim.", "evidence_summary": summary, "limitations": limitations, "evidence_layer": "ligand_receptor_or_direct_molecular", "exportable": "true", "consolidation_note": f"{BATCH_ID}: primary-study target-gene evidence; upstream handoff remains separate and unupgraded."})
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
