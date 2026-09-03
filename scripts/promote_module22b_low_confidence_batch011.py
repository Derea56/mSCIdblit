#!/usr/bin/env python3
"""Promote the bounded GABA-A/BDNF/TrkB/CREB functional association."""

from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EDGE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
AUDIT_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_low_confidence_upgrade_batch011.tsv"
SUMMARY_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_low_confidence_upgrade_batch011_summary.json"
BATCH_ID = "module22b-low-confidence-upgrade-batch011-2026-09-03"
EDGE_ID = "M22B-E000051"
EVIDENCE_ID = "M22B-EVID-000695"
SOURCE_LOCATOR = "PMID:21474450; PMCID:PMC3122223; DOI:10.1074/jbc.M110.201582; PMID:12163549; DOI:10.1152/jn.2002.88.2.1005"
BASIS = (
    "Primary developing-neuron studies show that GABA-A receptor agonism activates MAPK/CREB signaling and increases BDNF expression, while TrkB blockade suppresses GABA-A receptor-induced CREB phosphorylation. "
    "This supports a bounded GABA-A-to-BDNF/TrkB/CREB functional association, but not a subtype-specific receptor assignment or direct CREB target-locus claim."
)
RELATION = "GABA-A receptor activation promotes BDNF/TrkB-dependent CREB phosphorylation and activity-dependent neuronal signaling; no receptor-subtype-specific TF-target regulation is assigned"
TARGET = "GABA-A -> Ca2+/MAPK -> BDNF release -> TrkB-dependent CREB phosphorylation and activity-dependent neuronal program"
SCOPE = (
    "Developing cortical-neuron assays support GABA-A receptor agonist/antagonist-sensitive MAPK and CREB activation, BDNF induction, and TrkB-dependent CREB phosphorylation. "
    "The evidence does not resolve a specific GABA-A subunit assembly, a universal mature-neuron response, a direct CREB target locus, or SCI transfer."
)

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
    edge = next((row for row in edges if row["b_edge_id"] == EDGE_ID), None)
    ev = next((row for row in evidence if row["b_evidence_id"] == EVIDENCE_ID), None)
    if edge is None or ev is None:
        raise SystemExit("batch011 edge/evidence row is missing")
    if edge["confidence_tier"] not in {"low", "low-medium", "medium"}:
        raise SystemExit(f"{EDGE_ID}: unexpected confidence tier {edge['confidence_tier']!r}")
    if edge["exportable"] != "true" or EDGE_ID not in (ev.get("b_edge_ids") or "").split(";"):
        raise SystemExit("batch011 row is not an exportable linked edge")
    old_target = edge["target_entity"]
    old_status = edge["edge_status"]
    old_edge_confidence = edge["confidence_tier"]
    old_evidence_confidence = ev["confidence_tier"]
    edge["confidence_tier"] = "medium"
    edge["relation_type"] = RELATION
    edge["target_entity"] = TARGET
    edge["context_scope"] = SCOPE
    edge["consolidation_note"] = append_once(edge["consolidation_note"], "Low-confidence upgrade batch011: medium after exact primary GABA-A/BDNF/TrkB/CREB functional re-review.")
    ev["confidence_tier"] = "high"
    ev["source_locator"] = SOURCE_LOCATOR
    ev["evidence_summary"] = BASIS
    ev["limitations"] = SCOPE
    ev["consolidation_note"] = append_once(ev["consolidation_note"], "Low-confidence upgrade batch011: exact primary GABA-A/BDNF/TrkB/CREB functional re-adjudication; edge remains medium because subtype and target-locus specificity are unresolved.")
    audit = [{
        "batch_id": BATCH_ID,
        "b_edge_id": EDGE_ID,
        "b_evidence_id": EVIDENCE_ID,
        "old_edge_confidence": old_edge_confidence,
        "new_edge_confidence": edge["confidence_tier"],
        "old_evidence_confidence": old_evidence_confidence,
        "new_evidence_confidence": ev["confidence_tier"],
        "old_target": old_target,
        "new_target": edge["target_entity"],
        "old_edge_status": old_status,
        "new_edge_status": edge["edge_status"],
        "decision_basis": BASIS,
        "source_locator": SOURCE_LOCATOR,
        "module22b_register_changed": "true",
        "canonical_sql_materialization": "false",
    }]
    write_tsv(EDGE_PATH, edges, EDGE_FIELDS)
    write_tsv(EVIDENCE_PATH, evidence, EVIDENCE_FIELDS)
    write_tsv(AUDIT_PATH, audit, AUDIT_FIELDS)
    counts = {
        "batch_id": BATCH_ID,
        "records_upgraded": 1,
        "medium_edge_upgrades": 1,
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
