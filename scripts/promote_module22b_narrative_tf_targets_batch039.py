#!/usr/bin/env python3
"""Add target lanes recovered while reviewing Module 22B holds 0065-0068."""

from __future__ import annotations

import json
import re
from pathlib import Path

from promote_module22b_narrative_tf_targets_batch001 import EDGE_FIELDS, EVIDENCE_FIELDS, read_tsv, write_tsv

ROOT = Path(__file__).resolve().parents[1]
EDGE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
AUDIT_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch039.tsv"
SUMMARY_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch039_summary.json"
BATCH_ID = "module22b-narrative-tf-targets-batch039-2026-09-03"

UPDATES = [
    (
        "M22B-HOLD-AUDIT-0065",
        "RUNX2",
        "Ibsp",
        "mouse",
        "PMID:16000302",
        "Primary mouse MC3T3-E1 preosteoblast promoter, ChIP, DNA-binding, and site-mutagenesis experiments; osteoblast differentiation comparator, non-SCI.",
        "RUNX2 bound the mouse Ibsp/Bsp promoter in chromatin and in vitro assays, and the RUNX2 sites functioned as osteoblast-specific transcriptional enhancers.",
        "This standalone RUNX2 target lane does not establish the submitted EDIL3-integrin-to-RUNX2 handoff or SCI specificity; DLX5 cooperativity is part of the promoter mechanism.",
    ),
    (
        "M22B-HOLD-AUDIT-0065",
        "RUNX2",
        "Galnt3",
        "mouse",
        "PMCID:PMC10889289",
        "Primary mouse osteoblast expression and perturbation experiments with Runx2 overexpression/knockdown, ChIP-seq, and Galnt3 promoter reporter assays; bone-cell comparator, non-SCI.",
        "Runx2 perturbation changed Galnt3 expression, Runx2 occupied the Galnt3 promoter in primary osteoblast ChIP-seq, and the Galnt3 promoter was directly regulated in reporter assays.",
        "This standalone RUNX2 target lane does not establish the submitted EDIL3-integrin-to-RUNX2 handoff or SCI specificity; the direct promoter evidence is from osteoblast-lineage cells.",
    ),
    (
        "M22B-HOLD-AUDIT-0066",
        "SMAD1/5;SMAD4",
        "ID3",
        "human",
        "PMID:18372118",
        "Primary human ovarian epithelial and ovarian-cancer cell experiments with BMP4 stimulation, Smad1/5 and Smad4 ChIP, enhancer reporter assays, and BMP antagonism; epithelial comparator, non-SCI.",
        "BMP4 stimulation recruited Smads 1/5 and Smad4 to upstream and intronic ID3 enhancers and increased ID3 promoter activity; BMP antagonism reduced endogenous ID3 expression.",
        "This standalone BMP-SMAD target lane does not establish any submitted ligand-receptor-specific handoff or SCI specificity; SMAD1/5 and SMAD4 were tested, not SMAD8 specifically.",
    ),
    (
        "M22B-HOLD-AUDIT-0067",
        "SMAD1;SMAD5;SMAD8",
        "Hey1",
        "mouse",
        "PMID:18986983; PMCID:PMC2610517",
        "Primary mouse mesenchymal progenitor-cell BMP9/GDF2 experiments with early expression profiling and Smad1/5/8 and Smad4 promoter ChIP; osteogenic comparator, non-SCI.",
        "BMP9/GDF2 induced Hey1, and ChIP assays detected BMP9-dependent Smad1/5/8 and Smad4 occupancy at the mouse Hey1 promoter, supporting a direct BMP9-Smad target.",
        "This standalone SMAD target lane does not establish the submitted GDF2-ACVRL1-ACVR2A handoff in SCI; the study is a mesenchymal osteogenic model and reports a BMP9-induced pathway target.",
    ),
    (
        "M22B-HOLD-AUDIT-0068",
        "SMAD1;SMAD5;SMAD8",
        "Hes5",
        "mouse",
        "PMID:24173804; PMCID:PMC3833432",
        "Primary mouse hippocampal-neuron cultures with GDF5 stimulation, SMAD1/5/8-dependent reporter assays, SMAD-binding-site mutation, expression analysis, and Hes5 loss-of-function; neural-development comparator, non-SCI.",
        "GDF5 increased Hes5 expression and intact Hes5-promoter activity through a SMAD-dependent mechanism; mutating the SMAD-binding consensus sequence abolished the promoter response, and Hes5 was necessary for the dendrite-growth phenotype.",
        "This standalone SMAD target lane does not establish the submitted GDF5 receptor-complex handoff in SCI; the evidence is a developmental hippocampal-neuron model and supports a SMAD-dependent target assignment rather than receptor-specific upstream activation.",
    ),
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
    for index, (holds, tf, target, species, locator, context, summary, limitations) in enumerate(UPDATES, start=187):
        pair = (species.casefold(), tf.casefold(), target.casefold())
        if pair in existing:
            raise SystemExit(f"target pair already exists: {pair}")
        edge_id, evidence_id = f"M22B-E{edge_number:06d}", f"M22B-EVID-{evidence_number:06d}"
        edge_number += 1
        evidence_number += 1
        edges.append({
            "b_edge_id": edge_id,
            "source_entity": tf,
            "relation_type": f"{tf} activates the {target} target gene in primary-study evidence",
            "target_entity": target,
            "pathway_name": "target_gene",
            "evidence_layer": "ligand_receptor_or_direct_molecular",
            "source_a_edge_id": f"M22B-TARGET-SEARCH-{index:04d}",
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
            "source_a_evidence_id": f"M22B-TARGET-SEARCH-EVID-{index:04d}",
            "b_edge_ids": edge_id,
            "source_kind": "reviewed_direct_target",
            "source_locator": locator,
            "support_kind": "primary_experiment",
            "species_support": species,
            "source_scope": "direct_edge",
            "confidence_tier": "high",
            "citation_note": f"Primary-study target-gene evidence identified while reviewing hold row {holds}; standalone general TF-regulon claim.",
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
    fields = ["batch_id", "hold_edges_reviewed", "tf", "target", "species", "b_edge_id", "b_evidence_id", "source_locator", "upstream_handoff_upgraded", "standalone_target_gene_edge", "decision_basis"]
    write_tsv(AUDIT_PATH, audit, fields)
    write_tsv(EDGE_PATH, edges, EDGE_FIELDS)
    write_tsv(EVIDENCE_PATH, evidence, EVIDENCE_FIELDS)
    summary = {
        "batch_id": BATCH_ID,
        "standalone_target_gene_edges_added": len(audit),
        "upstream_handoff_edges_upgraded": 0,
        "high_edges_after": sum(r["confidence_tier"] == "high" for r in edges),
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
