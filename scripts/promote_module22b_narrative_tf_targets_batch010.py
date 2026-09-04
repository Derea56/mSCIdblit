#!/usr/bin/env python3
"""Add primary-study TF target lanes recovered from the remaining hold review."""

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
AUDIT_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch010.tsv"
SUMMARY_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch010_summary.json"
BATCH_ID = "module22b-narrative-tf-targets-batch010-2026-09-03"

UPDATES = [
    (
        "M22B-HOLD-AUDIT-0090;M22B-HOLD-AUDIT-0091;M22B-HOLD-AUDIT-0092",
        "TCF4",
        "CD36",
        "human",
        "PMID:25721714; DOI:10.1159/000373951",
        "Human primary macrophages differentiated from monocytes; Wnt1 stimulation, TCF4 perturbation/overexpression, CD36 expression, and TCF4 ChIP at the CD36 promoter.",
        "The primary study showed Wnt1-dependent recruitment of TCF4 to a CD36 promoter binding site, TCF4-dependent CD36 expression, and increased CD36 after TCF4 overexpression.",
        "This is a member-resolved TCF4 edge in a human macrophage model; it does not establish the broad TCF/LEF-family handoffs or SCI activation.",
    ),
    (
        "M22B-HOLD-AUDIT-0037",
        "HOXD3",
        "TGFB1",
        "human",
        "PMID:32061928",
        "Human endothelial-cell and vascular-tissue BMP9/ALK1 model with HOXD3 perturbation and promoter analyses.",
        "The primary study reported that HOXD3 directly targets the TGFB1 promoter as part of a BMP9/ALK1-HOXD3-TGF-beta signaling cascade.",
        "The edge is a general HOXD3 target-gene finding from an endothelial/vascular model, not evidence that the EDIL3-integrin handoff activates HOXD3 or that the edge is SCI-specific.",
    ),
    (
        "M22B-HOLD-AUDIT-0086",
        "STAT4",
        "GZMB",
        "human",
        "PMID:28877912",
        "Human CD8 T-cell cytotoxicity model stimulated with type-I interferon, including STAT4 promoter ChIP-qPCR and GZMB expression assays.",
        "The primary study showed STAT4 binding at the GZMB promoter after interferon stimulation and linked STAT4 activity to GZMB-dependent cytotoxicity.",
        "This is a general human STAT4 target-gene lane in CD8 T cells; it does not assign the IL-23 handoff or establish SCI receiver-cell activation.",
    ),
    (
        "M22B-HOLD-AUDIT-0045",
        "NFATC1",
        "NADK",
        "human",
        "PMID:41203626",
        "Human colorectal-cancer cell model with NFATC1 perturbation, NADK promoter reporter analysis, and NFATC1 ChIP-qPCR.",
        "The primary study showed NFATC1 occupancy at the NADK promoter and NFATC1-dependent NADK expression.",
        "The finding is a general human NFATC1 target-gene edge in a cancer-cell model; it does not establish the SEMA6A-PLXNA2 handoff or SCI specificity.",
    ),
    (
        "M22B-HOLD-AUDIT-0045",
        "NFATC1",
        "MDM2",
        "human",
        "PMID:41203626",
        "Human colorectal-cancer cell model with NFATC1 perturbation and promoter-binding analysis.",
        "The primary study reported NFATC1 binding at the MDM2 p1 and p2 promoters and sustained MDM2 expression in the NFATC1 axis.",
        "The finding is a general human NFATC1 target-gene edge in a cancer-cell model; it does not establish the SEMA6A-PLXNA2 handoff or SCI specificity.",
    ),
    (
        "M22B-HOLD-AUDIT-0061;M22B-HOLD-AUDIT-0062",
        "RORA",
        "SOX4",
        "human",
        "PMID:22509368",
        "Human HEK293 and HepG2 models with ROR-alpha ChIP/chip, promoter occupancy, reporter mutation, and expression assays.",
        "The primary study showed ROR-alpha occupancy at the SOX4 promoter and ROR-alpha-dependent activation of a SOX4 promoter reporter and SOX4 expression.",
        "This is a general human RORA target-gene edge from a non-SCI model; it does not validate the CEL or DHCR7 handoffs.",
    ),
    (
        "M22B-HOLD-AUDIT-0061;M22B-HOLD-AUDIT-0062",
        "RORA",
        "Pcp4",
        "mouse",
        "PMID:14687547",
        "Mouse cerebellar granule-cell precursor model with in vivo ROR-alpha promoter occupancy and coactivator-binding analyses.",
        "The primary study detected ROR-alpha binding and coactivator-associated activation at the Pcp4 promoter in freshly dissected mouse cerebella.",
        "This is a mouse cerebellar RORA target-gene edge, not evidence for the CEL or DHCR7 handoffs and not an SCI receiver-cell claim.",
    ),
    (
        "M22B-HOLD-AUDIT-0061;M22B-HOLD-AUDIT-0062",
        "RORA",
        "Pcp2",
        "mouse",
        "PMID:14687547",
        "Mouse cerebellar granule-cell precursor model with in vivo ROR-alpha promoter occupancy and coactivator-binding analyses.",
        "The primary study detected ROR-alpha binding and coactivator-associated activation at the Pcp2 promoter in freshly dissected mouse cerebella.",
        "This is a mouse cerebellar RORA target-gene edge, not evidence for the CEL or DHCR7 handoffs and not an SCI receiver-cell claim.",
    ),
    (
        "M22B-HOLD-AUDIT-0061;M22B-HOLD-AUDIT-0062",
        "RORA",
        "Slc1a6",
        "mouse",
        "PMID:14687547",
        "Mouse cerebellar granule-cell precursor model with in vivo ROR-alpha promoter occupancy and coactivator-binding analyses.",
        "The primary study detected ROR-alpha binding at the Slc1a6 promoter in freshly dissected mouse cerebella.",
        "The source supports promoter occupancy within a cerebellar RORA target program, but does not validate the CEL or DHCR7 handoffs or establish SCI specificity.",
    ),
    (
        "M22B-HOLD-AUDIT-0061;M22B-HOLD-AUDIT-0062",
        "RORA",
        "Shh",
        "mouse",
        "PMID:14687547",
        "Mouse cerebellar granule-cell precursor model with in vivo ROR-alpha promoter occupancy and coactivator-binding analyses.",
        "The primary study detected ROR-alpha binding at two Shh promoter sites and linked the ROR-alpha target program to Sonic hedgehog signaling in mouse cerebellum.",
        "This is a mouse cerebellar RORA target-gene edge, not evidence for the CEL or DHCR7 handoffs and not an SCI receiver-cell claim.",
    ),
    (
        "M22B-HOLD-AUDIT-0061;M22B-HOLD-AUDIT-0062",
        "RORA",
        "Itpr1",
        "mouse",
        "PMID:14687547",
        "Mouse cerebellar granule-cell precursor model with in vivo ROR-alpha promoter occupancy and coactivator-binding analyses.",
        "The primary study detected ROR-alpha binding at the Itpr1 promoter in freshly dissected mouse cerebella.",
        "The source supports promoter occupancy within a cerebellar RORA target program, but does not validate the CEL or DHCR7 handoffs or establish SCI specificity.",
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
    for index, (holds, tf, target, species, locator, context, summary, limitations) in enumerate(UPDATES, start=75):
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
