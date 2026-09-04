#!/usr/bin/env python3
"""Recover exact ligand-receptor function programs from terminal-TF boundaries."""

from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EDGE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
AUDIT_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_low_confidence_upgrade_batch015.tsv"
SUMMARY_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_low_confidence_upgrade_batch015_summary.json"
BATCH_ID = "module22b-low-confidence-upgrade-batch015-2026-09-03"

UPGRADES = {
    "M22B-E005606": {
        "evidence_id": "M22B-EVID-005374", "source_entity": "CXCL12",
        "relation_type": "CXCL12 binds ACKR3 and supports atypical beta-arrestin/scavenging function; no terminal TF-target regulation is assigned",
        "target_entity": "CXCL12-ACKR3 -> atypical beta-arrestin/scavenging receptor program",
        "source_locator": "PMID:31506383; PMID:19794961; PMCID:PMC2745668",
        "species_support": "human; mouse xenograft comparator",
        "basis": "Primary binding and functional studies support CXCL12 engagement of ACKR3 and ACKR3-dependent beta-arrestin/scavenging behavior. This recovers an exact atypical-receptor functional program, but does not equate ACKR3 with CXCR4-like chemotaxis or assign a terminal TF.",
        "scope": "ACKR3 is an atypical receptor with context-dependent beta-arrestin and scavenging behavior; no SCI receiver or terminal TF occupancy was measured.",
    },
    "M22B-E005607": {
        "evidence_id": "M22B-EVID-005417", "source_entity": "EFNB2",
        "relation_type": "EFNB2 engages EPHB4 in bidirectional vascular signaling and supports angiogenic morphogenesis; no terminal TF-target regulation is assigned",
        "target_entity": "EFNB2-EPHB4 -> bidirectional vascular morphogenesis program",
        "source_locator": "PMID:9630219; PMID:10518221; PMID:38570531; DOI:10.1016/S1097-2765(00)80342-1",
        "species_support": "mouse; human endothelial comparator",
        "basis": "Primary developmental and genetic studies identify EFNB2 as an arterial ligand and EPHB4 as its venous receptor, with reciprocal signaling required for vascular morphogenesis. This supports an exact receptor-ligand function program, but not a single linear kinase-to-TF relay.",
        "scope": "The axis is membrane/contact and vascular-context dependent; downstream contributions are multicomponent and no terminal TF occupancy or SCI receiver program was measured.",
    },
    "M22B-E005613": {
        "evidence_id": "M22B-EVID-005432", "source_entity": "FGF17",
        "relation_type": "FGF17b activates FGFR1c in a splice-form-specific receptor program; no terminal TF-target regulation is assigned",
        "target_entity": "FGF17b-FGFR1c -> receptor-proximal developmental signaling program",
        "source_locator": "PMID:10381577; PMID:16384934",
        "species_support": "mouse; human recombinant; chick developmental comparator",
        "basis": "Primary receptor-activity and comparative FGF studies support FGF17b activation of the c splice form of FGFR1. This recovers a bounded exact receptor program, but does not generalize across FGF17 isoforms or assign a terminal TF.",
        "scope": "FGF17b and FGFR1c splice specificity, engineered-cell/developmental models, and lack of an SCI receiver constrain transfer; no terminal TF occupancy was measured.",
    },
    "M22B-E005614": {
        "evidence_id": "M22B-EVID-005433", "source_entity": "FGF17",
        "relation_type": "FGF17b activates FGFR2c in a splice-form-specific receptor program; no terminal TF-target regulation is assigned",
        "target_entity": "FGF17b-FGFR2c -> receptor-proximal developmental signaling program",
        "source_locator": "PMID:10381577; PMID:16384934",
        "species_support": "mouse; human recombinant; chick developmental comparator",
        "basis": "Primary receptor-activity and comparative FGF studies support FGF17b activation of the c splice form of FGFR2. This recovers a bounded exact receptor program, but does not generalize across FGF17 isoforms or assign a terminal TF.",
        "scope": "FGF17b and FGFR2c splice specificity, engineered-cell/developmental models, and lack of an SCI receiver constrain transfer; no terminal TF occupancy was measured.",
    },
    "M22B-E005618": {
        "evidence_id": "M22B-EVID-005454", "source_entity": "GDF2",
        "relation_type": "GDF2/BMP9 activates ACVRL1/ALK1 in a BMPR2-containing endothelial receptor context; no terminal TF-target regulation is assigned",
        "target_entity": "GDF2-ACVRL1/ALK1 -> endothelial BMP receptor signaling program",
        "source_locator": "PMID:22622516; PMCID:PMC3409742; PMID:17311849",
        "species_support": "mouse; human; primate comparator",
        "basis": "Primary endothelial receptor studies support GDF2/BMP9 activation of ACVRL1/ALK1 and a BMPR2-containing receptor context. This recovers the ligand-to-ALK1 pathway function while avoiding a unique type-II stoichiometry or terminal TF assignment.",
        "scope": "BMPR2 versus other ActRII-family contributions and endoglin-assisted complexes vary by endothelial context; SMAD/output observations are not terminal-TF evidence and SCI transfer remains unresolved.",
    },
    "M22B-E005624": {
        "evidence_id": "M22B-EVID-005495", "source_entity": "LEAP2",
        "relation_type": "LEAP2 binds and antagonizes GHSR through a receptor-proximal conformational mechanism; no terminal TF-target regulation is assigned",
        "target_entity": "LEAP2-GHSR -> ghrelin-receptor antagonism and metabolic signaling program",
        "source_locator": "PMID:29233536; DOI:10.1016/j.cmet.2017.10.016; PMID:30543423; DOI:10.1021/acs.jmedchem.8b01644; PMID:34447311",
        "species_support": "mouse; human; recombinant receptor systems",
        "basis": "Primary biochemical, structural, and physiological studies support LEAP2 binding and antagonism of GHSR, including receptor-proximal conformational effects. This recovers an exact receptor function program, but not a terminal TF or universal endocrine response.",
        "scope": "LEAP2 processing, constitutive GHSR activity, species, and ghrelin-independent effects constrain transfer; no SCI receiver or terminal TF occupancy was measured.",
    },
    "M22B-E005630": {
        "evidence_id": "M22B-EVID-004952", "source_entity": "SHH",
        "relation_type": "SHH engages PTCH2 and can participate with Smoothened in a ligand-responsive developmental relay; no terminal TF-target regulation is assigned",
        "target_entity": "SHH-PTCH2-SMO -> Hedgehog developmental signaling program",
        "source_locator": "PMID:9811851; PMCID:PMC24870; PMID:25085974",
        "species_support": "mouse; human comparator",
        "basis": "Primary receptor and developmental studies support Hedgehog binding to PTCH2 and PTCH2 participation in a Smoothened-linked ligand-responsive relay. This recovers a bounded PTCH2 pathway program, but does not infer direct SHH-SMO binding or a terminal TF.",
        "scope": "PTCH2 paralog potency, trafficking, PTCH1 compensation, and developmental context affect the relay; no terminal TF occupancy or SCI receiver-cell result was measured.",
    },
    "M22B-E005632": {
        "evidence_id": "M22B-EVID-005234", "source_entity": "VEGFC",
        "relation_type": "Proteolytically processed VEGF-C binds NRP2 and supports an NRP2/VEGFR3 lymphatic sprouting relay; no terminal TF-target regulation is assigned",
        "target_entity": "processed VEGF-C-NRP2/VEGFR3 -> lymphatic sprouting program",
        "source_locator": "PMID:25752543; PMID:20065093; DOI:10.1016/j.str.2015.01.018",
        "species_support": "mouse; human recombinant systems",
        "basis": "Primary structural and functional studies support binding of processed VEGF-C to NRP2 and NRP2/VEGFR3-dependent lymphatic sprouting. This recovers an exact processed-ligand receptor program, while retaining co-receptor and maturation limits and excluding a terminal TF.",
        "scope": "VEGF-C proteolytic maturation, NRP2 co-receptor function, VEGFR3 context, and lymphatic models constrain transfer; no terminal TF occupancy or SCI receiver program was measured.",
    },
}

EDGE_FIELDS = ["b_edge_id", "source_entity", "relation_type", "target_entity", "pathway_name", "evidence_layer", "source_a_edge_id", "edge_status", "context_scope", "cell_type_context", "compartment_context", "species_context", "injury_context", "confidence_tier", "export_priority", "exportable", "consolidation_note"]
EVIDENCE_FIELDS = ["b_evidence_id", "source_a_evidence_id", "b_edge_ids", "source_kind", "source_locator", "support_kind", "species_support", "source_scope", "confidence_tier", "citation_note", "evidence_summary", "limitations", "evidence_layer", "exportable", "consolidation_note"]
AUDIT_FIELDS = ["batch_id", "b_edge_id", "b_evidence_id", "old_edge_confidence", "new_edge_confidence", "old_evidence_confidence", "new_evidence_confidence", "old_target", "new_target", "old_edge_status", "new_edge_status", "decision_basis", "source_locator", "module22b_register_changed", "canonical_sql_materialization"]


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
    edges, evidence = read_tsv(EDGE_PATH), read_tsv(EVIDENCE_PATH)
    edge_by_id, evidence_by_id = {r["b_edge_id"]: r for r in edges}, {r["b_evidence_id"]: r for r in evidence}
    audit = []
    for edge_id, change in UPGRADES.items():
        edge, ev = edge_by_id.get(edge_id), evidence_by_id.get(change["evidence_id"])
        if edge is None or ev is None: raise SystemExit(f"missing batch015 row for {edge_id}")
        if edge["confidence_tier"] != "low" or edge["edge_status"] != "no_evidence_boundary": raise SystemExit(f"{edge_id}: expected low no-evidence boundary")
        if ev["source_kind"] != "no_evidence_boundary" or ev["support_kind"] != "negative_evidence": raise SystemExit(f"{edge_id}: expected no-evidence source row")
        old_target, old_status = edge["target_entity"], edge["edge_status"]
        old_edge_confidence, old_evidence_confidence = edge["confidence_tier"], ev["confidence_tier"]
        edge.update({"source_entity": change["source_entity"], "relation_type": change["relation_type"], "target_entity": change["target_entity"], "pathway_name": "cell_state_program", "edge_status": "reviewed_program_association", "context_scope": change["scope"], "confidence_tier": "medium", "exportable": "true"})
        edge["consolidation_note"] = append_once(edge["consolidation_note"], f"Low-confidence recovery batch015: medium after exact primary receptor/function re-review for {change['source_entity']}.")
        ev.update({"source_kind": "reviewed_program_association", "source_locator": change["source_locator"], "support_kind": "primary_experiment", "species_support": change["species_support"], "source_scope": "contextual_support", "confidence_tier": "high", "evidence_summary": change["basis"], "limitations": change["scope"], "evidence_layer": "downstream_or_functional", "exportable": "true"})
        ev["consolidation_note"] = append_once(ev["consolidation_note"], "Low-confidence recovery batch015: exact primary receptor-binding/function evidence recovered; terminal TF claim remains excluded.")
        audit.append({"batch_id": BATCH_ID, "b_edge_id": edge_id, "b_evidence_id": change["evidence_id"], "old_edge_confidence": old_edge_confidence, "new_edge_confidence": edge["confidence_tier"], "old_evidence_confidence": old_evidence_confidence, "new_evidence_confidence": ev["confidence_tier"], "old_target": old_target, "new_target": edge["target_entity"], "old_edge_status": old_status, "new_edge_status": edge["edge_status"], "decision_basis": change["basis"], "source_locator": change["source_locator"], "module22b_register_changed": "true", "canonical_sql_materialization": "false"})
    write_tsv(EDGE_PATH, edges, EDGE_FIELDS); write_tsv(EVIDENCE_PATH, evidence, EVIDENCE_FIELDS); write_tsv(AUDIT_PATH, audit, AUDIT_FIELDS)
    counts = {"batch_id": BATCH_ID, "records_upgraded": len(audit), "medium_edge_upgrades": len(audit), "recovered_boundary_edges": len(audit), "low_edges_after": sum(r["confidence_tier"] == "low" for r in edges), "low_medium_edges_after": sum(r["confidence_tier"] == "low-medium" for r in edges), "medium_edges_after": sum(r["confidence_tier"] == "medium" for r in edges), "medium_high_edges_after": sum(r["confidence_tier"] == "medium-high" for r in edges), "high_edges_after": sum(r["confidence_tier"] == "high" for r in edges), "exportable_edges_after": sum(r["exportable"] == "true" for r in edges), "canonical_sql_materialization": False, "audit": str(AUDIT_PATH)}
    SUMMARY_PATH.parent.mkdir(parents=True, exist_ok=True); SUMMARY_PATH.write_text(json.dumps(counts, indent=2) + "\n", encoding="utf-8"); print(json.dumps(counts, indent=2)); return 0


if __name__ == "__main__": raise SystemExit(main())
