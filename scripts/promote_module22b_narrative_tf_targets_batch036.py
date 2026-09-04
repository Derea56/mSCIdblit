#!/usr/bin/env python3
"""Add target lanes recovered while reviewing Module 22B holds 0049-0052."""

from __future__ import annotations

import json
import re
from pathlib import Path

from promote_module22b_narrative_tf_targets_batch001 import EDGE_FIELDS, EVIDENCE_FIELDS, read_tsv, write_tsv

ROOT = Path(__file__).resolve().parents[1]
EDGE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
AUDIT_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch036.tsv"
SUMMARY_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch036_summary.json"
BATCH_ID = "module22b-narrative-tf-targets-batch036-2026-09-03"

UPDATES = [
    (
        "M22B-HOLD-AUDIT-0050",
        "RARB",
        "CYP26A1",
        "human",
        "PMID:18166136; PMCID:PMC2249606",
        "Primary human hepatocellular-carcinoma study with retinoid treatment, RARbeta/RARB promoter ChIP, reporter assays, and RARB knockdown; hepatic retinoid-response, non-SCI comparator.",
        "Retinoid treatment increased RARbeta/RARB occupancy at the human CYP26A1 promoter containing RAREs, supporting direct RARB regulation of CYP26A1.",
        "This standalone RARB target lane does not establish the submitted RARB-CRABP2-to-ALDH1A3 route or SCI specificity; the evidence is hepatocellular-carcinoma and retinoid context dependent.",
    ),
    (
        "M22B-HOLD-AUDIT-0052",
        "RARG",
        "PTGES",
        "human",
        "PMID:41274504; PMCID:PMC12774775",
        "Primary human oral squamous-cell-carcinoma study integrating RARG CUT&RUN, RARG knockout, chromatin marks, transcriptomics, and RARG agonist response; epithelial, non-SCI comparator.",
        "Integrated RARG binding and agonist/knockout transcriptomic evidence classified PTGES as a ligand-bound RARG target induced in human squamous epithelial cancer cells.",
        "This standalone RARG target lane does not establish the submitted RARG-CRABP2-to-ALDH1A3 route or SCI specificity; the target definition is ligand and epithelial-context dependent.",
    ),
    (
        "M22B-HOLD-AUDIT-0052",
        "RARG",
        "CYP26B1",
        "human",
        "PMID:41274504; PMCID:PMC12774775",
        "Primary human oral squamous-cell-carcinoma study integrating RARG CUT&RUN, RARG knockout, chromatin marks, transcriptomics, and RARG agonist response; epithelial, non-SCI comparator.",
        "Integrated RARG binding and agonist/knockout transcriptomic evidence classified CYP26B1 as a ligand-bound RARG target induced in human squamous epithelial cancer cells.",
        "This standalone RARG target lane does not establish the submitted RARG-CRABP2-to-ALDH1A3 route or SCI specificity; the target definition is ligand and epithelial-context dependent.",
    ),
    (
        "M22B-HOLD-AUDIT-0052",
        "RARG",
        "DHRS3",
        "human",
        "PMID:41274504; PMCID:PMC12774775",
        "Primary human oral squamous-cell-carcinoma study integrating RARG CUT&RUN, RARG knockout, chromatin marks, transcriptomics, and RARG agonist response; epithelial, non-SCI comparator.",
        "Integrated RARG binding and agonist/knockout transcriptomic evidence classified DHRS3 as a ligand-bound RARG target induced in human squamous epithelial cancer cells.",
        "This standalone RARG target lane does not establish the submitted RARG-CRABP2-to-ALDH1A3 route or SCI specificity; the target definition is ligand and epithelial-context dependent.",
    ),
]


def next_id(rows: list[dict[str, str]], field: str) -> int:
    return max([int(match.group(1)) for row in rows if (match := re.search(r"(\d+)$", row[field]))] or [0]) + 1


def main() -> int:
    edges, evidence = read_tsv(EDGE_PATH), read_tsv(EVIDENCE_PATH)
    existing = {(r.get("species_context", "").casefold(), r.get("source_entity", "").casefold(), r.get("target_entity", "").casefold()) for r in edges if r.get("pathway_name") == "target_gene"}
    edge_number, evidence_number = next_id(edges, "b_edge_id"), next_id(evidence, "b_evidence_id")
    audit = []
    for index, (holds, tf, target, species, locator, context, summary, limitations) in enumerate(UPDATES, start=173):
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
