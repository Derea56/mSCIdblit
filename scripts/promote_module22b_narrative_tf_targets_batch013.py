#!/usr/bin/env python3
"""Add three primary-study TF target lanes recovered from remaining holds."""

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
AUDIT_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch013.tsv"
SUMMARY_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch013_summary.json"
BATCH_ID = "module22b-narrative-tf-targets-batch013-2026-09-03"

UPDATES = [
    (
        "M22B-HOLD-AUDIT-0067;M22B-HOLD-AUDIT-0068;M22B-HOLD-AUDIT-0069;M22B-HOLD-AUDIT-0070;M22B-HOLD-AUDIT-0071;M22B-HOLD-AUDIT-0072;M22B-HOLD-AUDIT-0073",
        "SMAD1",
        "HOXD3",
        "human",
        "PMID:32061928",
        "Human endothelial/vascular BMP9-ALK1 model with pSMAD1 promoter occupancy and HOXD3 induction assays; non-SCI comparator.",
        "The primary study showed BMP9/ALK1-associated pSMAD1 binding at the HOXD3 promoter and induction of HOXD3 transcription.",
        "This is a SMAD1-member-specific target-gene edge and does not resolve the submitted SMAD1/5/8 family composites, establish the GDF/BMP upstream handoffs, or imply SCI-specific activation.",
    ),
    (
        "M22B-HOLD-AUDIT-0063;M22B-HOLD-AUDIT-2920;M22B-HOLD-AUDIT-2930",
        "RORB",
        "HBP1",
        "human",
        "DOI:10.1186/s12943-017-0590-2",
        "Human colorectal-cancer initiating-cell model with RORbeta chromatin immunoprecipitation, HRE EMSA, HBP1 promoter reporter, and perturbation assays; non-SCI comparator.",
        "Primary experiments showed RORbeta binding upstream of HBP1, identified a RORbeta response element, and demonstrated RORbeta-dependent HBP1 promoter activity and expression.",
        "This is a general RORB target-gene edge from a colorectal-cancer model; it does not establish the reviewed retinoid-to-RORB handoff, the ALDH1A3-specific target, or SCI specificity.",
    ),
    (
        "M22B-HOLD-AUDIT-0063;M22B-HOLD-AUDIT-2920;M22B-HOLD-AUDIT-2930",
        "RORB",
        "Ptf1a",
        "mouse",
        "PMID:23652001; DOI:10.1038/ncomms2793",
        "Mouse retinal developmental model with RORbeta1-responsive Ptf1a enhancer analysis and reporter assays; non-SCI comparator.",
        "Primary experiments identified a RORbeta1-responsive enhancer in the Ptf1a locus and showed enhancer-dependent reporter activation with RORbeta1 in the tested system.",
        "This is a developmental mouse RORB target-gene edge; it does not establish the reviewed retinoid-to-RORB handoff, the ALDH1A3-specific target, or SCI specificity.",
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
    for index, (holds, tf, target, species, locator, context, summary, limitations) in enumerate(UPDATES, start=100):
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
            "citation_note": f"Primary-study target-gene evidence identified while reviewing hold rows {holds}; standalone general TF-regulon claim." + (f" external_record_keys={locator}" if not re.search(r"PMID:\\d+", locator) else ""),
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
