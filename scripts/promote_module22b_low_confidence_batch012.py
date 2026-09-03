#!/usr/bin/env python3
"""Recover three serotonin-receptor/CREB functional edges from boundaries."""

from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EDGE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
AUDIT_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_low_confidence_upgrade_batch012.tsv"
SUMMARY_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_low_confidence_upgrade_batch012_summary.json"
BATCH_ID = "module22b-low-confidence-upgrade-batch012-2026-09-03"

UPGRADES = {
    "M22B-E000111": {
        "evidence_id": "M22B-EVID-000318",
        "source_entity": "HTR1A",
        "relation_type": "5-HT1A receptor activation promotes PKA/CREB-dependent hippocampal neuronal signaling; no direct TF-target regulation is assigned",
        "target_entity": "5-HT1A -> PKA/CREB activity -> hippocampal neuronal adaptation and anxiety-associated program",
        "source_locator": "PMID:20164327; PMCID:PMC6634557; DOI:10.1523/JNEUROSCI.5880-09.2010",
        "species_support": "mouse",
        "basis": (
            "Primary mouse study shows that 5-HT1A-selective agonism changes hippocampal CREB phosphorylation and that CREB blockade alters the associated behavioral response. "
            "This supports a bounded 5-HT1A-to-CREB functional association, but not a direct CREB target-locus claim or a universal SCI program."
        ),
        "scope": (
            "Mouse hippocampal assays support 5-HT1A agonist/antagonist-sensitive CREB phosphorylation linked to nNOS-dependent anxiety-related behavior. "
            "The evidence is pathway/functional rather than direct promoter occupancy; dosing, hippocampal subregion, cell state, and SCI transfer remain unresolved."
        ),
        "note": "Low-confidence recovery batch012: medium after exact primary 5-HT1A-CREB functional re-review.",
        "evidence_note": "Low-confidence recovery batch012: recovered from no-evidence boundary using exact primary receptor/CREB function; edge remains medium because no target locus is assigned.",
    },
    "M22B-E000112": {
        "evidence_id": "M22B-EVID-000324",
        "source_entity": "HTR4",
        "relation_type": "5-HT4 receptor activation promotes PKA-dependent CREB activation and enteric neuronal survival/neurogenesis; no direct TF-target regulation is assigned",
        "target_entity": "5-HT4 -> PKA/CREB activity -> enteric neuronal survival and neurogenesis program",
        "source_locator": "PMID:19657021; PMCID:PMC2749879; DOI:10.1523/JNEUROSCI.1145-09.2009",
        "species_support": "mouse",
        "basis": (
            "Primary mouse enteric-neuron study shows that 5-HT4 agonists activate CREB, increase neuronal survival/development, and induce adult enteric neurogenesis; receptor antagonism or knockout blocks the responses. "
            "This supports a bounded 5-HT4-to-CREB functional association, but not a direct CREB target-locus claim or SCI transfer."
        ),
        "scope": (
            "Mouse fetal and adult enteric-neuron assays support 5-HT4 agonist-sensitive CREB activation, reduced apoptosis, and neurogenesis, with PKA dependence in the CREB response. "
            "The evidence is receptor-dependent function rather than direct CREB promoter occupancy; enteric-tissue specificity, downstream target identity, and SCI transfer remain unresolved."
        ),
        "note": "Low-confidence recovery batch012: medium after exact primary 5-HT4-CREB functional re-review.",
        "evidence_note": "Low-confidence recovery batch012: recovered from no-evidence boundary using exact primary receptor/CREB function; edge remains medium because no target locus is assigned.",
    },
    "M22B-E000113": {
        "evidence_id": "M22B-EVID-000328",
        "source_entity": "HTR7",
        "relation_type": "5-HT7 receptor activation promotes PKA-sensitive CREB reporter activity and G12-linked neuronal transcriptional signaling; no direct TF-target regulation is assigned",
        "target_entity": "5-HT7 -> G12/PKA signaling -> CREB activity and neuronal morphology/transcription program",
        "source_locator": "PMID:16120784; PMCID:PMC6725246; DOI:10.1523/JNEUROSCI.1790-05.2005; PMID:26773257",
        "species_support": "mouse; rat; human",
        "basis": (
            "Primary receptor-expression and neuronal studies show 5-HT7-dependent CREB reporter activation with PKA sensitivity, G12-linked transcriptional signaling, and neurite effects in neuronal models. "
            "This supports a bounded 5-HT7-to-CREB functional association, but not direct CREB occupancy at a target locus or a universal receptor-isoform mechanism."
        ),
        "scope": (
            "5-HT7-transfected NIH3T3 assays and mouse hippocampal-neuron assays support receptor-dependent CREB reporter activity and G12-associated neuronal signaling. "
            "The evidence is reporter/pathway function rather than direct endogenous target-gene occupancy; G-protein coupling, splice isoform, neuronal subregion, and SCI transfer remain unresolved."
        ),
        "note": "Low-confidence recovery batch012: medium after exact primary 5-HT7-CREB functional re-review.",
        "evidence_note": "Low-confidence recovery batch012: recovered from no-evidence boundary using exact primary receptor/CREB function; edge remains medium because no target locus is assigned.",
    },
}

EDGE_FIELDS = [
    "b_edge_id", "source_entity", "relation_type", "target_entity", "pathway_name",
    "evidence_layer", "source_a_edge_id", "edge_status", "context_scope",
    "cell_type_context", "compartment_context", "species_context", "injury_context",
    "confidence_tier", "export_priority", "exportable", "consolidation_note",
]
EVIDENCE_FIELDS = [
    "b_evidence_id", "source_a_evidence_id", "b_edge_ids", "source_kind",
    "source_locator", "support_kind", "species_support", "source_scope",
    "confidence_tier", "citation_note", "evidence_summary", "limitations",
    "evidence_layer", "exportable", "consolidation_note",
]
AUDIT_FIELDS = [
    "batch_id", "b_edge_id", "b_evidence_id", "old_edge_confidence", "new_edge_confidence",
    "old_evidence_confidence", "new_evidence_confidence", "old_target", "new_target",
    "old_edge_status", "new_edge_status", "decision_basis", "source_locator",
    "module22b_register_changed", "canonical_sql_materialization",
]


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def append_once(value: str, addition: str) -> str:
    return value if addition in value else (f"{value}; {addition}" if value else addition)


def main() -> int:
    edges = read_tsv(EDGE_PATH)
    evidence = read_tsv(EVIDENCE_PATH)
    edge_by_id = {row["b_edge_id"]: row for row in edges}
    evidence_by_id = {row["b_evidence_id"]: row for row in evidence}
    audit = []
    for edge_id, change in UPGRADES.items():
        edge = edge_by_id.get(edge_id)
        ev = evidence_by_id.get(change["evidence_id"])
        if edge is None or ev is None:
            raise SystemExit(f"missing batch012 row for {edge_id}")
        if edge["confidence_tier"] != "low" or edge["edge_status"] != "no_evidence_boundary":
            raise SystemExit(f"{edge_id}: expected low no-evidence boundary, found {edge['confidence_tier']}/{edge['edge_status']}")
        if ev["source_kind"] != "no_evidence_boundary" or ev["support_kind"] != "negative_evidence":
            raise SystemExit(f"{edge_id}: expected no-evidence source row")
        old_target = edge["target_entity"]
        old_status = edge["edge_status"]
        old_edge_confidence = edge["confidence_tier"]
        old_evidence_confidence = ev["confidence_tier"]
        edge["source_entity"] = change["source_entity"]
        edge["relation_type"] = change["relation_type"]
        edge["target_entity"] = change["target_entity"]
        edge["pathway_name"] = "cell_state_program"
        edge["edge_status"] = "reviewed_program_association"
        edge["context_scope"] = change["scope"]
        edge["confidence_tier"] = "medium"
        edge["exportable"] = "true"
        edge["consolidation_note"] = append_once(edge["consolidation_note"], change["note"])
        ev["source_kind"] = "reviewed_program_association"
        ev["source_locator"] = change["source_locator"]
        ev["support_kind"] = "primary_experiment"
        ev["species_support"] = change["species_support"]
        ev["source_scope"] = "contextual_support"
        ev["confidence_tier"] = "high"
        ev["evidence_summary"] = change["basis"]
        ev["limitations"] = change["scope"]
        ev["evidence_layer"] = "downstream_or_functional"
        ev["exportable"] = "true"
        ev["consolidation_note"] = append_once(ev["consolidation_note"], change["evidence_note"])
        audit.append({
            "batch_id": BATCH_ID,
            "b_edge_id": edge_id,
            "b_evidence_id": change["evidence_id"],
            "old_edge_confidence": old_edge_confidence,
            "new_edge_confidence": edge["confidence_tier"],
            "old_evidence_confidence": old_evidence_confidence,
            "new_evidence_confidence": ev["confidence_tier"],
            "old_target": old_target,
            "new_target": edge["target_entity"],
            "old_edge_status": old_status,
            "new_edge_status": edge["edge_status"],
            "decision_basis": change["basis"],
            "source_locator": change["source_locator"],
            "module22b_register_changed": "true",
            "canonical_sql_materialization": "false",
        })
    write_tsv(EDGE_PATH, edges, EDGE_FIELDS)
    write_tsv(EVIDENCE_PATH, evidence, EVIDENCE_FIELDS)
    write_tsv(AUDIT_PATH, audit, AUDIT_FIELDS)
    counts = {
        "batch_id": BATCH_ID,
        "records_upgraded": len(audit),
        "medium_edge_upgrades": len(audit),
        "recovered_boundary_edges": len(audit),
        "low_edges_after": sum(row["confidence_tier"] == "low" for row in edges),
        "low_medium_edges_after": sum(row["confidence_tier"] == "low-medium" for row in edges),
        "medium_edges_after": sum(row["confidence_tier"] == "medium" for row in edges),
        "medium_high_edges_after": sum(row["confidence_tier"] == "medium-high" for row in edges),
        "high_edges_after": sum(row["confidence_tier"] == "high" for row in edges),
        "exportable_edges_after": sum(row["exportable"] == "true" for row in edges),
        "canonical_sql_materialization": False,
        "audit": str(AUDIT_PATH),
    }
    SUMMARY_PATH.parent.mkdir(parents=True, exist_ok=True)
    SUMMARY_PATH.write_text(json.dumps(counts, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(counts, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
