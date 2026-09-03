#!/usr/bin/env python3
"""Apply the second bounded upgrade to a Module 22B low-confidence edge."""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EDGE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
AUDIT_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_low_confidence_upgrade_batch002.tsv"
SUMMARY_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_low_confidence_upgrade_batch002_summary.json"

EDGE_ID = "M22B-E000782"
EVIDENCE_ID = "M22B-EVID-005759"
BATCH_ID = "module22b-low-confidence-upgrade-batch002-2026-09-02"
SOURCE_LOCATOR = "PMID:33200805; PMCID:PMC7705994; DOI:10.3892/mmr.2020.11690"
BASIS = (
    "Primary human pancreatic-cancer study shows recombinant WNT5A increases ABCG2 "
    "and gemcitabine resistance, while FZD7 silencing or inhibition blocks the "
    "response; this supports a bounded receptor-dependent functional edge, not a "
    "direct binding or terminal TF-target claim."
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
        raise SystemExit("batch002 edge/evidence row is missing")
    if edge["confidence_tier"] not in {"low", "medium"}:
        raise SystemExit(f"{EDGE_ID}: expected low or already-upgraded edge, found {edge['confidence_tier']!r}")
    if edge["exportable"] != "true":
        raise SystemExit(f"{EDGE_ID}: expected exportable=true")
    if EDGE_ID not in (ev.get("b_edge_ids") or "").split(";"):
        raise SystemExit(f"{EVIDENCE_ID}: not linked to {EDGE_ID}")

    old_target = edge["target_entity"]
    old_status = edge["edge_status"]
    edge["confidence_tier"] = "medium"
    edge["consolidation_note"] = append_once(
        edge["consolidation_note"],
        "Low-confidence upgrade batch002: medium after exact primary-source re-review.",
    )
    ev["confidence_tier"] = "high"
    ev["source_locator"] = SOURCE_LOCATOR
    ev["evidence_summary"] = BASIS
    edge["context_scope"] = append_once(
        edge["context_scope"],
        "Primary human pancreatic-cancer perturbation supports a bounded WNT5A-FZD7 functional relay; purified binding, generalizability beyond Capan-2 cells, and terminal TF output remain unresolved.",
    )
    ev["limitations"] = edge["context_scope"]
    ev["consolidation_note"] = append_once(
        ev["consolidation_note"],
        "Low-confidence upgrade batch002: high-quality primary functional source; edge remains medium because receptor assignment is perturbational and context-specific.",
    )

    audit = [{
        "batch_id": BATCH_ID,
        "b_edge_id": EDGE_ID,
        "b_evidence_id": EVIDENCE_ID,
        "old_edge_confidence": "low",
        "new_edge_confidence": "medium",
        "old_evidence_confidence": "",
        "new_evidence_confidence": "high",
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
        "medium_edges_after": sum(row["confidence_tier"] == "medium" for row in edges),
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
