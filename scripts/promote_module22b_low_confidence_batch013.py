#!/usr/bin/env python3
"""Recover AREG and BTC receptor-signaling programs from AP-1 boundaries."""

from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EDGE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
AUDIT_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_low_confidence_upgrade_batch013.tsv"
SUMMARY_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_low_confidence_upgrade_batch013_summary.json"
BATCH_ID = "module22b-low-confidence-upgrade-batch013-2026-09-03"

UPGRADES = {
    "M22B-E000007": {
        "evidence_id": "M22B-EVID-000122",
        "source_entity": "AREG",
        "relation_type": "AREG activates EGFR-family signaling with ERK/AKT output; no direct AP-1 target-locus regulation is assigned",
        "target_entity": "AREG -> EGFR-family ERK/AKT signaling -> immediate-early growth program",
        "source_locator": "PMID:20726858; PMID:22593802",
        "species_support": "human",
        "basis": (
            "The primary AREG study supports AREG-dependent EGFR-family signaling, including EGFR-linked ERK and EGFR/HER3-linked AKT output, with inhibition by anti-AREG treatment. "
            "This recovers an exact AREG receptor-signaling program, but does not establish the submitted EGFR-ERBB2 composite as the operative receptor or direct AP-1 occupancy at a target locus."
        ),
        "scope": (
            "Human pancreatic-cancer cell models support AREG-associated EGFR/ERK and EGFR/HER3/AKT signaling. "
            "The evidence is receptor/pathway function rather than AP-1 DNA binding; HER3 versus ERBB2 usage, cell-state dependence, and SCI transfer remain unresolved."
        ),
        "note": "Low-confidence recovery batch013: medium after exact primary AREG/EGFR-family signaling re-review.",
        "evidence_note": "Low-confidence recovery batch013: recovered from no-evidence boundary using exact primary AREG receptor/pathway function; AP-1 target-locus claim remains excluded.",
    },
    "M22B-E000008": {
        "evidence_id": "M22B-EVID-000124",
        "source_entity": "BTC",
        "relation_type": "BTC activates EGFR and ERBB4 in a receptor-pattern-specific signaling program; no direct AP-1 target-locus regulation is assigned",
        "target_entity": "BTC -> EGFR/ERBB4 receptor activation -> distinct EGF-family growth-signaling program",
        "source_locator": "PMID:8570211; PMID:35494243",
        "species_support": "mouse; human",
        "basis": (
            "The primary receptor-panel study shows that BTC stimulates EGFR tyrosine phosphorylation and activates ERBB4, with distinct receptor-phosphorylation and cellular-response patterns in recombinant Ba/F3 cells. "
            "A later tumor study supports BTC dependence of EGFR signaling and cell survival. This establishes a bounded BTC receptor-signaling program, but not direct AP-1 occupancy or an exact BTC-EGFR-ERBB2 ternary assignment."
        ),
        "scope": (
            "Mouse Ba/F3 receptor-panel assays support BTC activation of EGFR and ERBB4; human tumor models provide complementary BTC/EGFR pathway dependence. "
            "The evidence is receptor/pathway function rather than AP-1 DNA binding; receptor-complex stoichiometry, ERBB2-specific contribution, and SCI transfer remain unresolved."
        ),
        "note": "Low-confidence recovery batch013: medium after exact primary BTC/EGFR-ERBB4 signaling re-review.",
        "evidence_note": "Low-confidence recovery batch013: recovered from no-evidence boundary using exact primary BTC receptor activation and pathway function; AP-1 target-locus claim remains excluded.",
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
            raise SystemExit(f"missing batch013 row for {edge_id}")
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
