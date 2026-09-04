#!/usr/bin/env python3
"""Add target lanes recovered while reviewing Module 22B holds 0025-0028."""

from __future__ import annotations

import json
import re
from pathlib import Path

from promote_module22b_narrative_tf_targets_batch001 import EDGE_FIELDS, EVIDENCE_FIELDS, read_tsv, write_tsv

ROOT = Path(__file__).resolve().parents[1]
EDGE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
AUDIT_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch030.tsv"
SUMMARY_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch030_summary.json"
BATCH_ID = "module22b-narrative-tf-targets-batch030-2026-09-03"

UPDATES = [
    ("M22B-HOLD-AUDIT-0025", "EGR1", "GRM2", "mouse", "PMID:23508685; PMCID:PMC3657099", "Primary mouse frontal-cortex and neuronal-cell experiments examining 5-HT2A-dependent EGR1 occupancy and Grm2 promoter activity; neural non-SCI comparator.", "EGR1 binding at the mouse Grm2 promoter was reduced in 5-HT2A-knockout cortex, and EGR1 overexpression increased Grm2 expression and promoter activity.", "This is a standalone EGR1 target-gene edge from a serotonin/neural model; it does not establish the submitted 5-HT2A/2B/2C-to-EGR1/FOS handoff or SCI specificity."),
    ("M22B-HOLD-AUDIT-0027", "ELK1", "TBP", "human", "PMID:17074809; PMCID:PMC1800663", "Primary human hepatoma-cell and mouse fibroblast experiments with EGF/JNK perturbation, ELK1 promoter occupancy, and TBP transcriptional assays; non-SCI comparator.", "EGF-dependent ELK1 occupancy at the human TBP promoter was linked to TBP transcriptional regulation, with JNK1/2 perturbation altering ELK1 phosphorylation and TBP expression.", "This is a standalone ELK1 target-gene edge from growth-factor and hepatoma/fibroblast models; it does not establish the submitted DSPP-DPP-integrin-to-ELK1 handoff or SCI specificity."),
    ("M22B-HOLD-AUDIT-0027", "ELK1", "DUSP16", "mouse", "PMID:39434411; PMCID:PMC11822628", "Primary mouse neural-progenitor and Alzheimer-model experiments with ELK1 perturbation, Dusp16 promoter ChIP-qPCR, and promoter-reporter assays; non-SCI comparator.", "ELK1 was associated with the Dusp16 promoter, and ELK1 perturbation altered Dusp16 transcription in neural progenitor-cell and Alzheimer-model experiments.", "This is a standalone ELK1 target-gene edge from neural-differentiation and Alzheimer models; it does not establish the submitted DSPP-DPP-integrin-to-ELK1 handoff or SCI specificity."),
    ("M22B-HOLD-AUDIT-0028", "ELK1", "LRG1", "human", "PMID:31602408; PMCID:PMC6778114", "Primary human dermal-fibroblast mechanical-loading study with ELK1 ChIP-seq/ChIP-qPCR, ELK1 perturbation, promoter reporter, and mouse scar validation; injury/fibrosis non-SCI comparator.", "Mechanical loading activated ERK/ELK1, ELK1 bound the LRG1 promoter, and ELK1 perturbation plus promoter-reporter assays supported LRG1 transcriptional activation.", "This is a standalone ELK1 target-gene edge from skin fibrosis and mechanical-loading models; it does not establish the submitted ARTN-GFRA3_RET-to-ELK1/AP-1 handoff or SCI specificity."),
    ("M22B-HOLD-AUDIT-0028", "ELK1", "CLDND1", "human", "PMID:35892692; PMCID:PMC9329870", "Primary human brain-endothelial-cell study with ELK1 overexpression/deletion, promoter/enhancer reporter, ChIP, EGF stimulation, and EGFR inhibition; non-SCI comparator.", "ELK1 activated the human CLDND1 promoter/enhancer, bound the regulatory region, and increased CLDND1 expression; EGF-dependent induction was attenuated by EGFR inhibition.", "This is a standalone ELK1 target-gene edge from a brain-endothelial barrier model; it does not establish the submitted ARTN-GFRA3_RET-to-ELK1/AP-1 handoff or SCI specificity."),
]


def next_id(rows: list[dict[str, str]], field: str) -> int:
    return max([int(match.group(1)) for row in rows if (match := re.search(r"(\d+)$", row[field]))] or [0]) + 1


def main() -> int:
    edges, evidence = read_tsv(EDGE_PATH), read_tsv(EVIDENCE_PATH)
    existing = {(r.get("species_context", "").casefold(), r.get("source_entity", "").casefold(), r.get("target_entity", "").casefold()) for r in edges if r.get("pathway_name") == "target_gene"}
    edge_number, evidence_number = next_id(edges, "b_edge_id"), next_id(evidence, "b_evidence_id")
    audit = []
    for index, (holds, tf, target, species, locator, context, summary, limitations) in enumerate(UPDATES, start=136):
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
