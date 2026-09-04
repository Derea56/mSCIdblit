#!/usr/bin/env python3
"""Promote two bounded Module 22B receptor-dependent functional edges."""

from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EDGE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
AUDIT_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_low_confidence_upgrade_batch007.tsv"
SUMMARY_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_low_confidence_upgrade_batch007_summary.json"
BATCH_ID = "module22b-low-confidence-upgrade-batch007-2026-09-03"

UPGRADES = {
    "M22B-E000641": {
        "evidence_id": "M22B-EVID-005515",
        "source_locator": "PMID:26920052; DOI:10.1016/j.bbrc.2016.02.098",
        "relation_type": "Exogenous S100A8 inhibits PDGF-induced airway-smooth-muscle migration through RAGE; no direct TF-target regulation is assigned",
        "context_scope": (
            "Recombinant S100A8 and RAGE neutralization in rat airway-smooth-muscle cells support RAGE-dependent modulation of PDGF-induced migration. "
            "This is a cell-based receptor-dependence result, not purified ligand-receptor binding or a terminal transcriptional output; the exact intracellular relay and SCI transfer remain unresolved."
        ),
        "basis": (
            "Primary rat airway-smooth-muscle study reports that exogenous S100A8 inhibits PDGF-induced migration and that a RAGE-neutralizing antibody blocks the effect. "
            "This supports a bounded S100A8-RAGE functional edge, but not purified binding or a terminal TF target."
        ),
        "citation_note": "M22A-HANDOFF-005515",
        "note": "Low-confidence upgrade batch007: medium after exact primary RAGE-dependence re-review.",
        "evidence_note": "Low-confidence upgrade batch007: exact primary RAGE-dependence re-adjudication; edge remains medium because evidence is cell-based functional dependence.",
    },
    "M22B-E000706": {
        "evidence_id": "M22B-EVID-005211",
        "source_locator": "PMID:24036928; PMCID:PMC3895427; DOI:10.4161/cc.26388",
        "relation_type": "TGF-beta induces integrin-alphaV-beta5-dependent ventral-stress-fiber and focal-adhesion organization; no direct TF-target regulation is assigned",
        "context_scope": (
            "TGF-beta treatment and integrin-beta5 depletion/rescue experiments in mouse and human epithelial cells support an alphaV-beta5-dependent ventral-stress-fiber and focal-adhesion response. "
            "The evidence is receptor-associated functional dependence rather than direct TGF-beta-alphaV-beta5 binding; the intracellular adhesome and SCI transfer remain unresolved."
        ),
        "basis": (
            "Primary mouse and human epithelial-cell study shows that TGF-beta induces ventral stress fibers, integrin-beta5 suppression reduces the response, and integrin-beta5 constructs restore defined cytoskeletal/focal-adhesion features. "
            "This supports a bounded TGF-beta-integrin-beta5 functional edge, not direct ligand-receptor binding or a terminal TF target."
        ),
        "citation_note": "M22A-HANDOFF-005211",
        "note": "Low-confidence upgrade batch007: medium after exact primary integrin-beta5 dependence re-review.",
        "evidence_note": "Low-confidence upgrade batch007: exact primary integrin-beta5 dependence re-adjudication; edge remains medium because evidence is pathway/functional and does not establish direct ligand binding.",
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
            raise SystemExit(f"missing batch007 row for {edge_id}")
        if edge["confidence_tier"] not in {"low", "low-medium", "medium"}:
            raise SystemExit(f"{edge_id}: unexpected confidence tier {edge['confidence_tier']!r}")
        if edge["exportable"] != "true" or edge_id not in (ev.get("b_edge_ids") or "").split(";"):
            raise SystemExit(f"{edge_id}: row is not an exportable linked edge")
        old_target = edge["target_entity"]
        old_edge_confidence = edge["confidence_tier"]
        old_evidence_confidence = ev["confidence_tier"]
        old_status = edge["edge_status"]
        edge["confidence_tier"] = "medium"
        edge["relation_type"] = change["relation_type"]
        edge["context_scope"] = change["context_scope"]
        edge["consolidation_note"] = append_once(edge["consolidation_note"], change["note"])
        ev["confidence_tier"] = "high"
        ev["source_locator"] = change["source_locator"]
        ev["evidence_summary"] = change["basis"]
        ev["limitations"] = change["context_scope"]
        ev["citation_note"] = change["citation_note"]
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
        "medium_edge_upgrades": sum(row["new_edge_confidence"] == "medium" for row in audit),
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
