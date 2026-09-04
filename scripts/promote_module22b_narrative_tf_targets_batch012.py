#!/usr/bin/env python3
"""Add four primary-study TF target lanes recovered from remaining holds."""

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
AUDIT_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch012.tsv"
SUMMARY_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch012_summary.json"
BATCH_ID = "module22b-narrative-tf-targets-batch012-2026-09-03"

UPDATES = [
    (
        "M22B-HOLD-AUDIT-0019;M22B-HOLD-AUDIT-0020;M22B-HOLD-AUDIT-0021",
        "ATF4",
        "ASNS",
        "human",
        "PMID:19509279",
        "Human 293 cells with inducible ATF4, amino-acid-response stimulation, ASNS promoter occupancy, and transcriptional activation assays.",
        "The primary study showed ATF4 recruitment to the ASNS proximal promoter and ATF4-dependent activation of the amino-acid-response ASNS transcriptional program.",
        "This is a general human ATF4 target-gene edge from a metabolic-stress model; it does not resolve the CREB/ATF4/ATFx composite or establish any GABA receptor handoff or SCI specificity.",
    ),
    (
        "M22B-HOLD-AUDIT-0019;M22B-HOLD-AUDIT-0020;M22B-HOLD-AUDIT-0021",
        "ATF4",
        "DDIT4",
        "human",
        "PMID:34373753",
        "Human tumor-cell model with ATF4 perturbation, DDIT4 promoter ChIP, promoter reporter assays, and expression analyses.",
        "The primary study used ATF4 promoter occupancy and reporter assays to confirm ATF4 regulation of DDIT4 transcription.",
        "This is a general human ATF4 target-gene edge from a tumor-metabolism model; it does not resolve the CREB/ATF4/ATFx composite or establish any GABA receptor handoff or SCI specificity.",
    ),
    (
        "M22B-HOLD-AUDIT-0018",
        "CREB1;ATF1",
        "CEBPB",
        "human",
        "PMID:14593102",
        "Human adipocyte differentiation model with CREB/ATF1 promoter-element analysis and constitutively active CREB promoter-reporter assays.",
        "The primary study showed that CREB/ATF1-responsive elements in the CEBPB promoter mediate CREB-dependent promoter activation and endogenous CEBPB induction.",
        "The edge is resolved to CREB1/ATF1 and does not assign CREM1, validate the exact GDNF handoff, or establish SCI specificity.",
    ),
    (
        "M22B-HOLD-AUDIT-0030",
        "ESR2",
        "NQO1",
        "human",
        "PMID:9738013",
        "Human breast/endometrial cell promoter-reporter and DNA-binding assays for antiestrogen-liganded estrogen-receptor beta.",
        "The primary study showed ER-beta-associated activation of the human quinone reductase/NQO1 promoter through the EpRE-containing region, with stronger activation through ER-beta than ER-alpha in the tested system.",
        "This is a ligand- and response-element-specific ESR2 regulatory-support edge without an endogenous SCI context; it does not validate the HSD17B1 handoff.",
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
    for index, (holds, tf, target, species, locator, context, summary, limitations) in enumerate(UPDATES, start=96):
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
