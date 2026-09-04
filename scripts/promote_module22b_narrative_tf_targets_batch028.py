#!/usr/bin/env python3
"""Add CREB/ATF4 target lanes recovered while reviewing Module 22B holds 0017-0020."""

from __future__ import annotations

import json
import re
from pathlib import Path

from promote_module22b_narrative_tf_targets_batch001 import EDGE_FIELDS, EVIDENCE_FIELDS, read_tsv, write_tsv

ROOT = Path(__file__).resolve().parents[1]
EDGE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
AUDIT_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch028.tsv"
SUMMARY_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_narrative_tf_targets_batch028_summary.json"
BATCH_ID = "module22b-narrative-tf-targets-batch028-2026-09-03"

UPDATES = [
    (
        "M22B-HOLD-AUDIT-0017",
        "CREB",
        "GADD45B",
        "rat",
        "PMID:32927466",
        "Primary rat striatal-neuron dopamine/DRD1 model; neural non-SCI comparator.",
        "Dopamine-induced Gadd45b mRNA in primary striatal neurons required DRD1, MEK, and CREB signaling; CREB inhibition blocked baseline and dopamine-induced Gadd45b expression.",
        "This is a standalone CREB target-gene edge from a rat neural model; it does not establish the submitted dopamine-DRD1-to-CREB handoff or SCI specificity.",
    ),
    (
        "M22B-HOLD-AUDIT-0018",
        "CREB1;ATF1;CREM1",
        "FOS",
        "mouse",
        "PMID:17962702; PMCID:PMC2905627",
        "Primary mouse spermatogonial stem-cell model; non-SCI comparator.",
        "GDNF/GFRα1/RET stimulation phosphorylated CREB1, ATF1, and CREM1 and induced c-fos transcription; the study mapped the pathway as GDNF/GFRα1/RET/Ras/ERK/CREB-family/c-fos.",
        "This is a composite CREB-family target lane because the study did not isolate one family member as sufficient; it does not establish the submitted GDNF-GFRA1_RET-to-TF handoff or SCI specificity.",
    ),
    (
        "M22B-HOLD-AUDIT-0019; M22B-HOLD-AUDIT-0020",
        "ATF4",
        "DDIT3",
        "human",
        "PMID:14630918; PMID:17267404",
        "Primary human CHOP/DDIT3 promoter and cultured-cell experiments with mouse ATF2-deficient validation; non-SCI comparator.",
        "ATF4 bound the human CHOP/DDIT3 amino-acid response element and was required, together with ATF2 phosphorylation, for starvation-induced CHOP transcription.",
        "This is a standalone ATF4 target-gene edge from amino-acid-response models; it does not establish the submitted GABA-receptor-to-ATF4 handoff or SCI specificity.",
    ),
    (
        "M22B-HOLD-AUDIT-0019; M22B-HOLD-AUDIT-0020",
        "ATF4",
        "GABBR1",
        "human",
        "PMID:15240803",
        "Primary human GABBR1 promoter analysis in hippocampal neuronal contexts; neural non-SCI comparator.",
        "ATF4 cotransfection increased GABBR1a promoter activity in hippocampal neurons, demonstrating that ATF4/CREB-family proteins can regulate the human GABBR1 promoter.",
        "This is a standalone ATF4 target-gene edge from a promoter study; it does not establish the submitted GABA-GAD2/SLC6A1/SLC6A11 or GABA-GAD2/SLC6A12-GABBR1 upstream handoffs or SCI specificity.",
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
    for index, (holds, tf, target, species, locator, context, summary, limitations) in enumerate(UPDATES, start=132):
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
