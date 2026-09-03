#!/usr/bin/env python3
"""Recover exact ligand-receptor function programs from terminal-TF boundaries."""

from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EDGE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
AUDIT_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_low_confidence_upgrade_batch016.tsv"
SUMMARY_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_low_confidence_upgrade_batch016_summary.json"
BATCH_ID = "module22b-low-confidence-upgrade-batch016-2026-09-03"

UPGRADES = {
    "M22B-E005601": {"evidence_id": "M22B-EVID-005356", "source_entity": "CCL28", "relation_type": "CCL28 activates CCR3 in a receptor-dependent inflammatory program; no terminal TF-target regulation is assigned", "target_entity": "CCL28-CCR3 -> chemokine receptor inflammatory-cell program", "source_locator": "PMID:40975172; PMID:39193987; PMID:40502012; PMCID:PMC12556802", "species_support": "mouse; human", "basis": "Primary receptor and infection studies support CCL28 engagement of CCR3 and CCR3-dependent inflammatory function. This recovers an exact chemokine-receptor program, but does not assign a terminal TF or SCI receiver mechanism.", "scope": "Engineered receptor assays, chemokine variants, and infection context constrain transfer; no terminal TF occupancy or SCI receiver program was measured."},
    "M22B-E005602": {"evidence_id": "M22B-EVID-005365", "source_entity": "CD40LG", "relation_type": "CD40L binds alpha5beta1 integrin and supports integrin-dependent signaling/function; no terminal TF-target regulation is assigned", "target_entity": "CD40LG-alpha5beta1 -> integrin adhesion/signaling program", "source_locator": "DOI:10.1074/jbc.M608342200; PMID:25403978; PMCID:PMC7960543", "species_support": "human", "basis": "Primary binding and functional studies support CD40L interaction with alpha5beta1 and integrin-dependent cellular responses. This recovers an exact receptor-complex function program, but not a universal intracellular TF edge.", "scope": "The receptor is the alpha5beta1 heterodimer and binding depends on integrin conformation and cell context; ERK/IL-8 outputs are functional readouts, not terminal TF occupancy, and SCI transfer remains unresolved."},
    "M22B-E005603": {"evidence_id": "M22B-EVID-005364", "source_entity": "CD40LG", "relation_type": "CD40L binds alphaIIbbeta3 integrin and supports integrin activation; no terminal TF-target regulation is assigned", "target_entity": "CD40LG-alphaIIbbeta3 -> platelet integrin activation program", "source_locator": "PMCID:PMC10416995; PMID:25403978", "species_support": "human recombinant integrin and platelet-context assays", "basis": "Primary molecular and platelet-context studies support CD40L binding to alphaIIbbeta3 and integrin activation. This recovers an exact receptor-complex function program, but not a terminal TF or general tissue mechanism.", "scope": "Soluble CD40L, activated integrin conformation, cations, and platelet context are required; no terminal TF occupancy or SCI receiver result was measured."},
    "M22B-E005604": {"evidence_id": "M22B-EVID-005366", "source_entity": "CD40LG", "relation_type": "CD40L binds alphaMbeta2 integrin and supports receptor-dependent signaling; no terminal TF-target regulation is assigned", "target_entity": "CD40LG-alphaMbeta2 -> myeloid integrin signaling/adhesion program", "source_locator": "PMID:25403978; DOI:10.1002/eji.201444941", "species_support": "human", "basis": "Primary interaction and cellular studies map CD40L residues involved in alphaMbeta2 binding and report receptor-dependent MAPK responses. This supports an exact receptor-complex function program, but not a complete adaptor-to-TF chain.", "scope": "CD40L is trimeric, receptor usage is multivalent, and the cellular output is activation/context dependent; no terminal TF occupancy or SCI receiver mechanism was established."},
    "M22B-E005615": {"evidence_id": "M22B-EVID-005437", "source_entity": "FGF21", "relation_type": "FGF21 engages betaKlotho as a specificity co-receptor within an FGFR signaling complex; no terminal TF-target regulation is assigned", "target_entity": "FGF21-betaKlotho-FGFR -> endocrine metabolic signaling program", "source_locator": "PMID:17452648; PMID:18064602; PMID:18187602; DOI:10.1002/jcp.21357", "species_support": "mouse; human recombinant and metabolic-cell systems", "basis": "Primary receptor and metabolic studies support betaKlotho as an essential FGF21 specificity co-receptor in an FGFR signaling complex. This recovers an exact ligand/co-receptor program while preserving that KLB is not the signaling kinase and the FGFR subtype varies by assay.", "scope": "FGFR subtype, complex stoichiometry, endocrine dose, and adipocyte/metabolic model constrain transfer; no terminal TF occupancy or SCI receiver result was measured."},
    "M22B-E005619": {"evidence_id": "M22B-EVID-004848", "source_entity": "GLG1", "relation_type": "GLG1/ESL-1 binds E-selectin and supports selectin-dependent leukocyte tethering and rolling; no terminal TF-target regulation is assigned", "target_entity": "GLG1-E-selectin -> leukocyte adhesion/recruitment program", "source_locator": "PMID:9099943; DOI:10.1242/jcs.110.6.687; PMID:17442598; DOI:10.1016/j.immuni.2007.03.011; PMCID:PMC3659783", "species_support": "mouse; human", "basis": "Primary adhesion and immune studies support GLG1/ESL-1 as a cell-surface E-selectin ligand that mediates tethering, slow rolling, and inflammatory recruitment. This recovers an exact adhesion function program, but not a terminal TF.", "scope": "Glycosylation, membrane presentation, and leukocyte/endothelial context determine binding and output; GLG1 also has non-selectin functions and no SCI-specific TF endpoint was measured."},
    "M22B-E005623": {"evidence_id": "M22B-EVID-005491", "source_entity": "JAG1", "relation_type": "JAG1 engages NOTCH4 in a receptor-dependent canonical Notch endothelial program; no terminal TF-target regulation is assigned", "target_entity": "JAG1-NOTCH4 -> endothelial canonical Notch signaling program", "source_locator": "PMID:36044575; DOI:10.1126/sciadv.abo7958; PMID:36376768; PMCID:PMC10119233; DOI:10.1007/s10456-022-09861-6", "species_support": "mouse; human comparator", "basis": "Primary receptor-fragment binding and endothelial functional studies support JAG1 engagement of NOTCH4-associated canonical Notch signaling. This recovers a bounded receptor program, but does not assign a specific CSL/RBPJ target locus.", "scope": "The binding assay uses a NOTCH4 EGF10-14 fragment and vascular studies are context specific; ligand presentation, receptor processing, and SCI transfer remain unresolved."},
    "M22B-E005631": {"evidence_id": "M22B-EVID-005338", "source_entity": "C3d/C3dg", "relation_type": "Processed C3d/C3dg binds CR2/CD21 and participates in a B-cell coreceptor relay; no terminal TF-target regulation is assigned", "target_entity": "processed C3d/C3dg-CR2 -> B-cell coreceptor activation program", "source_locator": "PMID:1718035; PMID:15749857; PMID:19164292; DOI:10.4049/jimmunol.174.6.3264", "species_support": "mouse; human", "basis": "Primary binding and immunologic studies support processed C3d/C3dg engagement of CR2/CD21 and CR2-dependent B-cell coreceptor function. This recovers an exact processed-ligand receptor program, while excluding unprocessed C3 and terminal TF claims.", "scope": "The active ligands are processed complement fragments and CR2 functions in a multicomponent B-cell coreceptor; no terminal TF occupancy or SCI receiver program was measured."},
}

EDGE_FIELDS = ["b_edge_id", "source_entity", "relation_type", "target_entity", "pathway_name", "evidence_layer", "source_a_edge_id", "edge_status", "context_scope", "cell_type_context", "compartment_context", "species_context", "injury_context", "confidence_tier", "export_priority", "exportable", "consolidation_note"]
EVIDENCE_FIELDS = ["b_evidence_id", "source_a_evidence_id", "b_edge_ids", "source_kind", "source_locator", "support_kind", "species_support", "source_scope", "confidence_tier", "citation_note", "evidence_summary", "limitations", "evidence_layer", "exportable", "consolidation_note"]
AUDIT_FIELDS = ["batch_id", "b_edge_id", "b_evidence_id", "old_edge_confidence", "new_edge_confidence", "old_evidence_confidence", "new_evidence_confidence", "old_target", "new_target", "old_edge_status", "new_edge_status", "decision_basis", "source_locator", "module22b_register_changed", "canonical_sql_materialization"]


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle: return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n"); writer.writeheader(); writer.writerows(rows)


def append_once(value: str, addition: str) -> str:
    return value if addition in value else (f"{value}; {addition}" if value else addition)


def main() -> int:
    edges, evidence = read_tsv(EDGE_PATH), read_tsv(EVIDENCE_PATH)
    edge_by_id, evidence_by_id = {r["b_edge_id"]: r for r in edges}, {r["b_evidence_id"]: r for r in evidence}
    audit = []
    for edge_id, change in UPGRADES.items():
        edge, ev = edge_by_id.get(edge_id), evidence_by_id.get(change["evidence_id"])
        if edge is None or ev is None: raise SystemExit(f"missing batch016 row for {edge_id}")
        if edge["confidence_tier"] != "low" or edge["edge_status"] != "no_evidence_boundary": raise SystemExit(f"{edge_id}: expected low no-evidence boundary")
        if ev["source_kind"] != "no_evidence_boundary" or ev["support_kind"] != "negative_evidence": raise SystemExit(f"{edge_id}: expected no-evidence source row")
        old_target, old_status = edge["target_entity"], edge["edge_status"]; old_edge_confidence, old_evidence_confidence = edge["confidence_tier"], ev["confidence_tier"]
        edge.update({"source_entity": change["source_entity"], "relation_type": change["relation_type"], "target_entity": change["target_entity"], "pathway_name": "cell_state_program", "edge_status": "reviewed_program_association", "context_scope": change["scope"], "confidence_tier": "medium", "exportable": "true"})
        edge["consolidation_note"] = append_once(edge["consolidation_note"], f"Low-confidence recovery batch016: medium after exact primary receptor/function re-review for {change['source_entity']}.")
        ev.update({"source_kind": "reviewed_program_association", "source_locator": change["source_locator"], "support_kind": "primary_experiment", "species_support": change["species_support"], "source_scope": "contextual_support", "confidence_tier": "high", "evidence_summary": change["basis"], "limitations": change["scope"], "evidence_layer": "downstream_or_functional", "exportable": "true"})
        ev["consolidation_note"] = append_once(ev["consolidation_note"], "Low-confidence recovery batch016: exact primary receptor-binding/function evidence recovered; terminal TF claim remains excluded.")
        audit.append({"batch_id": BATCH_ID, "b_edge_id": edge_id, "b_evidence_id": change["evidence_id"], "old_edge_confidence": old_edge_confidence, "new_edge_confidence": edge["confidence_tier"], "old_evidence_confidence": old_evidence_confidence, "new_evidence_confidence": ev["confidence_tier"], "old_target": old_target, "new_target": edge["target_entity"], "old_edge_status": old_status, "new_edge_status": edge["edge_status"], "decision_basis": change["basis"], "source_locator": change["source_locator"], "module22b_register_changed": "true", "canonical_sql_materialization": "false"})
    write_tsv(EDGE_PATH, edges, EDGE_FIELDS); write_tsv(EVIDENCE_PATH, evidence, EVIDENCE_FIELDS); write_tsv(AUDIT_PATH, audit, AUDIT_FIELDS)
    counts = {"batch_id": BATCH_ID, "records_upgraded": len(audit), "medium_edge_upgrades": len(audit), "recovered_boundary_edges": len(audit), "low_edges_after": sum(r["confidence_tier"] == "low" for r in edges), "low_medium_edges_after": sum(r["confidence_tier"] == "low-medium" for r in edges), "medium_edges_after": sum(r["confidence_tier"] == "medium" for r in edges), "medium_high_edges_after": sum(r["confidence_tier"] == "medium-high" for r in edges), "high_edges_after": sum(r["confidence_tier"] == "high" for r in edges), "exportable_edges_after": sum(r["exportable"] == "true" for r in edges), "canonical_sql_materialization": False, "audit": str(AUDIT_PATH)}
    SUMMARY_PATH.parent.mkdir(parents=True, exist_ok=True); SUMMARY_PATH.write_text(json.dumps(counts, indent=2) + "\n", encoding="utf-8"); print(json.dumps(counts, indent=2)); return 0


if __name__ == "__main__": raise SystemExit(main())
