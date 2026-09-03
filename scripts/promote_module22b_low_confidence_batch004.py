#!/usr/bin/env python3
"""Re-anchor two TNFSF/TNFRSF rows to exact primary pair evidence."""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EDGE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
AUDIT_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_low_confidence_upgrade_batch004.tsv"
SUMMARY_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_low_confidence_upgrade_batch004_summary.json"
BATCH_ID = "module22b-low-confidence-upgrade-batch004-2026-09-02"
SOURCE_LOCATOR = "PMID:16547002; DOI:10.1074/jbc.M601553200"

PACKET = {
    "M22B-E000518": {
        "evidence_id": "M22B-EVID-005133",
        "basis": "Primary TNFSF/TNFRSF flow-cytometry survey directly detects the CD30L/TNFSF8-CD30/TNFRSF8 pair in human and mouse reagent panels. The receptor-binding result supports the re-anchored CD30 costimulatory branch, but does not by itself prove the full TRAF2/NF-kB relay or a terminal TF target.",
        "relation": "CD30L/TNFSF8 binds CD30/TNFRSF8; receptor-clustering costimulatory and NF-kB branch remains bounded; TWEAK/Fn14 is a separate ligand-receptor branch",
        "scope": "The original TWEAK-TNFRSF8 mismatch is not promoted; this row is re-anchored to the separately supported CD30L/TNFRSF8 pair. The flow-cytometry survey establishes binding, not the complete downstream TRAF2/NF-kB relay or a terminal TF target.",
    },
    "M22B-E000619": {
        "evidence_id": "M22B-EVID-005141",
        "basis": "Primary TNFSF/TNFRSF flow-cytometry survey directly detects the OX40L/TNFSF4-OX40/TNFRSF4 pair in human and mouse reagent panels. The receptor-binding result supports the re-anchored OX40 costimulatory branch, but does not by itself prove the full TRAF2/RIP/IKK/NF-kB relay or a terminal TF target.",
        "relation": "OX40L/TNFSF4 binds OX40/TNFRSF4; receptor-clustering costimulatory and NF-kB branch remains bounded",
        "scope": "The original TNFSF4-to-TRAF2 mismatch is not treated as a direct interaction; this row is re-anchored to the separately supported OX40L/TNFSF4 receptor pair. The flow-cytometry survey establishes binding, not the complete downstream TRAF2/RIP/IKK/NF-kB relay or a terminal TF target.",
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
    ev_by_id = {row["b_evidence_id"]: row for row in evidence}
    audit = []
    for edge_id, spec in PACKET.items():
        edge = edge_by_id.get(edge_id)
        ev = ev_by_id.get(spec["evidence_id"])
        if edge is None or ev is None:
            raise SystemExit(f"missing packet row: {edge_id} / {spec['evidence_id']}")
        if edge["confidence_tier"] not in {"low", "medium"}:
            raise SystemExit(f"{edge_id}: expected low or already-upgraded row, found {edge['confidence_tier']!r}")
        if edge["exportable"] != "true":
            raise SystemExit(f"{edge_id}: expected exportable=true")
        old_target = edge["target_entity"]
        old_status = edge["edge_status"]
        edge["confidence_tier"] = "medium"
        edge["relation_type"] = spec["relation"]
        edge["context_scope"] = spec["scope"]
        edge["consolidation_note"] = append_once(edge["consolidation_note"], "Low-confidence upgrade batch004: medium after exact TNFSF/TNFRSF pair re-review.")
        ev["confidence_tier"] = "high"
        ev["source_locator"] = SOURCE_LOCATOR
        ev["evidence_summary"] = spec["basis"]
        ev["limitations"] = edge["context_scope"]
        ev["consolidation_note"] = append_once(ev["consolidation_note"], "Low-confidence upgrade batch004: exact primary pair-binding re-adjudication; downstream branch remains bounded.")
        audit.append({
            "batch_id": BATCH_ID,
            "b_edge_id": edge_id,
            "b_evidence_id": spec["evidence_id"],
            "old_edge_confidence": "low",
            "new_edge_confidence": "medium",
            "old_evidence_confidence": "",
            "new_evidence_confidence": "high",
            "old_target": old_target,
            "new_target": edge["target_entity"],
            "old_edge_status": old_status,
            "new_edge_status": edge["edge_status"],
            "decision_basis": spec["basis"],
            "source_locator": SOURCE_LOCATOR,
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
        "low_edges_after": sum(row["confidence_tier"] == "low" for row in edges),
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
