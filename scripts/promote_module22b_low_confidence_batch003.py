#!/usr/bin/env python3
"""Apply the third bounded upgrade batch to Module 22B low-tier rows."""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EDGE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
AUDIT_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_low_confidence_upgrade_batch003.tsv"
SUMMARY_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_low_confidence_upgrade_batch003_summary.json"
BATCH_ID = "module22b-low-confidence-upgrade-batch003-2026-09-02"

PACKET = {
    "M22B-E000360": {
        "evidence_id": "M22B-EVID-000958",
        "new_edge_tier": "medium",
        "basis": "Primary GDF7 receptor-panel and reconstitution work supports a GDF7-dependent BMP-SMAD1/5/8 response with ID1-linked output in mouse/recombinant systems; exact native SCI receptor stoichiometry and terminal TF regulation remain unresolved.",
        "source_locator": "PMID:16049014; DOI:10.1074/jbc.M504629200",
        "scope_suffix": "Primary GDF7 receptor-panel/reconstitution evidence supports the bounded BMP-SMAD1/5/8-ID1 program; native SCI receptor stoichiometry and terminal TF output remain unresolved.",
    },
    "M22B-E000384": {
        "evidence_id": "M22B-EVID-000948",
        "new_edge_tier": "medium",
        "basis": "Primary GDF1/Nodal receptor-complex studies support Cripto/EGF-CFC-dependent SMAD2/3 developmental transcription in embryonic and recombinant systems; receptor stoichiometry, ligand form, and SCI transfer remain bounded.",
        "source_locator": "PMID:12514096; PMCID:PMC195969; PMCID:PMC4067217",
        "scope_suffix": "Primary GDF1/Nodal receptor-complex evidence supports the bounded developmental SMAD2/3 program; co-receptor dependence, complex stoichiometry, embryonic context, and SCI transfer remain unresolved.",
    },
    "M22B-E000566": {
        "evidence_id": "M22B-EVID-005461",
        "new_edge_tier": "medium",
        "basis": "Primary GDF6 receptor-panel/reconstitution work supports BMPR1B-containing BMP receptor usage and SMAD1/5/8 signaling in mouse/recombinant systems; full-length native complex stoichiometry and SCI transfer remain unresolved.",
        "source_locator": "PMID:16049014; DOI:10.1074/jbc.M504629200",
        "scope_suffix": "Primary GDF6 receptor-panel/reconstitution evidence supports the bounded BMPR1B-containing BMP branch; receptor abundance, ligand form, full-length complex stoichiometry, and SCI transfer remain unresolved.",
    },
    "M22B-E000567": {
        "evidence_id": "M22B-EVID-005462",
        "new_edge_tier": "medium",
        "basis": "Primary GDF7 receptor-panel/reconstitution work supports BMPR1A plus BMPR2-compatible BMP signaling and SMAD1/5/8 output in mouse/recombinant systems; receptor stoichiometry and SCI transfer remain unresolved.",
        "source_locator": "PMID:16049014; DOI:10.1074/jbc.M504629200",
        "scope_suffix": "Primary GDF7 receptor-panel/reconstitution evidence supports the bounded BMPR1A-BMPR2-compatible BMP branch; receptor abundance, ligand form, complex stoichiometry, and SCI transfer remain unresolved.",
    },
    "M22B-E000568": {
        "evidence_id": "M22B-EVID-005463",
        "new_edge_tier": "medium",
        "basis": "Primary GDF7 receptor-panel/reconstitution work supports BMPR1B plus BMPR2-compatible BMP signaling and SMAD1/5/8 output in mouse/recombinant systems; receptor stoichiometry and SCI transfer remain unresolved.",
        "source_locator": "PMID:16049014; DOI:10.1074/jbc.M504629200",
        "scope_suffix": "Primary GDF7 receptor-panel/reconstitution evidence supports the bounded BMPR1B-BMPR2-compatible BMP branch; receptor abundance, ligand form, complex stoichiometry, and SCI transfer remain unresolved.",
    },
    "M22B-E000779": {
        "evidence_id": "M22B-EVID-005731",
        "new_edge_tier": "medium-high",
        "basis": "Primary purified-protein study reconstitutes a WNT3A-mediated FZD8 CRD-LRP6 extracellular ternary complex, measures direct WNT3A-LRP6 binding, and shows receptor-fragment inhibition of beta-catenin signaling; soluble-fragment and no-terminal-TF limits remain.",
        "source_locator": "PMID:20093360; PMCID:PMC2838336; DOI:10.1074/jbc.M109.092130",
        "scope_suffix": "Primary purified-protein evidence resolves a WNT3A-FZD8-LRP6 extracellular ternary complex; soluble receptor fragments do not establish every full-length cellular stoichiometry or SCI context, and no terminal TF edge is added.",
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
        csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n").writeheader()
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writerows(rows)


def append_once(value: str, addition: str) -> str:
    return value if addition in value else (f"{value}; {addition}" if value else addition)


def main() -> int:
    edges = read_tsv(EDGE_PATH)
    evidence = read_tsv(EVIDENCE_PATH)
    edge_by_id = {row["b_edge_id"]: row for row in edges}
    ev_by_id = {row["b_evidence_id"]: row for row in evidence}
    audit = []
    for edge_id, spec in PACKET.items():
        edge = edge_by_id.get(edge_id)
        ev = ev_by_id.get(spec["evidence_id"])
        if edge is None or ev is None:
            raise SystemExit(f"missing packet row: {edge_id} / {spec['evidence_id']}")
        if edge["confidence_tier"] not in {"low-medium", spec["new_edge_tier"]}:
            raise SystemExit(f"{edge_id}: expected low-medium or already-upgraded row, found {edge['confidence_tier']!r}")
        if edge["exportable"] != "true":
            raise SystemExit(f"{edge_id}: expected exportable=true")
        if edge_id not in (ev.get("b_edge_ids") or "").split(";"):
            raise SystemExit(f"{spec['evidence_id']}: not linked to {edge_id}")
        edge["confidence_tier"] = spec["new_edge_tier"]
        edge["context_scope"] = append_once(edge["context_scope"], spec["scope_suffix"])
        edge["consolidation_note"] = append_once(edge["consolidation_note"], f"Low-confidence upgrade batch003: {spec['new_edge_tier']} after exact primary-source re-review.")
        ev["confidence_tier"] = "high"
        ev["source_locator"] = spec["source_locator"]
        ev["evidence_summary"] = spec["basis"]
        ev["limitations"] = edge["context_scope"]
        ev["consolidation_note"] = append_once(ev["consolidation_note"], "Low-confidence upgrade batch003: high-quality primary-source re-adjudication; edge tier remains bounded by layer and exactness.")
        audit.append({
            "batch_id": BATCH_ID,
            "b_edge_id": edge_id,
            "b_evidence_id": spec["evidence_id"],
            "old_edge_confidence": "low-medium",
            "new_edge_confidence": spec["new_edge_tier"],
            "old_evidence_confidence": "",
            "new_evidence_confidence": "high",
            "old_target": edge["target_entity"],
            "new_target": edge["target_entity"],
            "old_edge_status": edge["edge_status"],
            "new_edge_status": edge["edge_status"],
            "decision_basis": spec["basis"],
            "source_locator": spec["source_locator"],
            "module22b_register_changed": "true",
            "canonical_sql_materialization": "false",
        })
    write_tsv(EDGE_PATH, edges, EDGE_FIELDS)
    write_tsv(EVIDENCE_PATH, evidence, EVIDENCE_FIELDS)
    write_tsv(AUDIT_PATH, audit, AUDIT_FIELDS)
    counts = {
        "batch_id": BATCH_ID,
        "records_upgraded": len(audit),
        "medium_edge_upgrades": sum(r["new_edge_confidence"] == "medium" for r in audit),
        "medium_high_edge_upgrades": sum(r["new_edge_confidence"] == "medium-high" for r in audit),
        "low_medium_edges_after": sum(r["confidence_tier"] == "low-medium" for r in edges),
        "medium_edges_after": sum(r["confidence_tier"] == "medium" for r in edges),
        "medium_high_edges_after": sum(r["confidence_tier"] == "medium-high" for r in edges),
        "high_edges_after": sum(r["confidence_tier"] == "high" for r in edges),
        "exportable_edges_after": sum(r["exportable"] == "true" for r in edges),
        "canonical_sql_materialization": False,
        "audit": str(AUDIT_PATH),
    }
    SUMMARY_PATH.parent.mkdir(parents=True, exist_ok=True)
    SUMMARY_PATH.write_text(json.dumps(counts, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(counts, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
