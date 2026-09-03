#!/usr/bin/env python3
"""Recover exact receptor-binding/function programs from terminal-TF boundaries."""

from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EDGE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_edge_register.tsv"
EVIDENCE_PATH = ROOT / "work/module_b_consolidation/module22b/module22b_evidence_register.tsv"
AUDIT_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_low_confidence_upgrade_batch014.tsv"
SUMMARY_PATH = ROOT / "work/module22b_low_confidence_upgrade_audit/module22b_low_confidence_upgrade_batch014_summary.json"
BATCH_ID = "module22b-low-confidence-upgrade-batch014-2026-09-03"

UPGRADES = {
    "M22B-E005598": {
        "evidence_id": "M22B-EVID-005336",
        "source_entity": "BTLA",
        "relation_type": "BTLA engages HVEM/TNFRSF14 in trans and supports receptor-dependent inhibitory immune function; no terminal TF-target regulation is assigned",
        "target_entity": "BTLA-HVEM/TNFRSF14 trans-engagement -> inhibitory immune-cell activation program",
        "source_locator": "PMID:38831106; PMID:38676311; PMCID:PMC3381650",
        "species_support": "mouse; human",
        "basis": (
            "The cited primary studies support BTLA-HVEM/TNFRSF14 trans-cellular engagement and receptor-dependent inhibitory immune function. "
            "This recovers an exact ligand-receptor functional program, but does not establish a terminal TF, purified affinity in every context, or an SCI receiver-cell mechanism."
        ),
        "scope": "Trans-cellular geometry, cis/trans competition, and lymphocyte context constrain the result; no direct TF occupancy or SCI-specific receiver program was measured.",
    },
    "M22B-E005605": {
        "evidence_id": "M22B-EVID-005367",
        "source_entity": "CD70",
        "relation_type": "CD70 binds CD27 and supports CD27-dependent lymphocyte costimulation; no terminal TF-target regulation is assigned",
        "target_entity": "CD70-CD27 engagement -> T-cell costimulatory activation program",
        "source_locator": "PMID:8120384; PMID:34419446; PMCID:PMC8484739",
        "species_support": "human; mammalian expression systems",
        "basis": (
            "Primary cloning and functional studies identify CD70 as the CD27 ligand and show CD70-dependent proliferation/costimulation in lymphocyte assays. "
            "This supports an exact CD70-CD27 receptor/costimulatory program, but not a defined intracellular TF or target-gene edge."
        ),
        "scope": "The direct ligand assignment and costimulation are supported in recombinant/heterologous and lymphocyte models; presentation, activation state, and SCI transfer remain unresolved.",
    },
    "M22B-E005611": {
        "evidence_id": "M22B-EVID-005431",
        "source_entity": "FGF1",
        "relation_type": "FGF1 forms a heparan-sulfate-dependent FGFR4 receptor complex and activates receptor signaling; no terminal TF-target regulation is assigned",
        "target_entity": "FGF1-FGFR4 -> heparan-sulfate-dependent receptor tyrosine-kinase signaling program",
        "source_locator": "PMID:7680645; PMID:20547770; PMCID:PMC2924102; DOI:10.1074/jbc.M109.095109",
        "species_support": "mouse; human recombinant systems",
        "basis": (
            "The primary receptor and biochemical studies support FGF1-FGFR4 complex formation and heparan-sulfate/heparin-dependent receptor activation. "
            "This recovers an exact receptor-proximal FGF1-FGFR4 signaling program, but no terminal TF or universal downstream kinase sequence is assigned."
        ),
        "scope": "FGFR splice form, heparan-sulfate chemistry, receptor presentation, and engineered-cell or recombinant assay context constrain generalization; SCI transfer and TF occupancy remain unresolved.",
    },
    "M22B-E005616": {
        "evidence_id": "M22B-EVID-005441",
        "source_entity": "FGF8",
        "relation_type": "FGF8b binds and activates FGFR1c in a splice-form-specific developmental receptor program; no terminal TF-target regulation is assigned",
        "target_entity": "FGF8b-FGFR1c -> receptor-proximal mid-hindbrain developmental signaling program",
        "source_locator": "PMID:16384934; PMCID:PMC2582917; DOI:10.1210/en.2007-1634",
        "species_support": "mouse; human recombinant; chick developmental comparator",
        "basis": (
            "The primary biochemical and developmental work provides direct evidence for an FGF8b-FGFR1c interaction and shows splice-form-dependent developmental signaling. "
            "This supports a bounded exact receptor program, but does not assign all FGF8 isoforms, a terminal TF, or an SCI response."
        ),
        "scope": "FGF8b versus FGF8a, FGFR1c splice specificity, heparan-sulfate/receptor context, and embryonic developmental models limit transfer; no terminal TF occupancy was measured.",
    },
    "M22B-E005617": {
        "evidence_id": "M22B-EVID-005453",
        "source_entity": "GDF15",
        "relation_type": "GDF15 binds GFRAL and activates a GFRAL-RET receptor complex; no terminal TF-target regulation is assigned",
        "target_entity": "GDF15-GFRAL-RET -> caudal-hindbrain neuronal metabolic-response program",
        "source_locator": "PMID:28846097; PMID:28953886; PMID:31535977; DOI:10.1038/nm.4392",
        "species_support": "mouse; human; nonhuman primate recombinant systems",
        "basis": (
            "Primary structural, biochemical, and in vivo studies identify GFRAL as the GDF15 receptor and establish RET as a required signaling coreceptor for the receptor complex. "
            "This supports an exact GDF15-GFRAL receptor program, while preserving that GDF15 is not assigned as a direct RET ligand and no terminal TF is established."
        ),
        "scope": "GFRAL is restricted to specific hindbrain neurons in the cited models; RET is a signaling coreceptor, species and endocrine context matter, and no terminal TF occupancy or SCI receiver-cell result was measured.",
    },
    "M22B-E005622": {
        "evidence_id": "M22B-EVID-005488",
        "source_entity": "JAG1",
        "relation_type": "JAG1 engages NOTCH1 and supports canonical Notch receptor signaling; no terminal TF-target regulation is assigned",
        "target_entity": "JAG1-NOTCH1 -> canonical Notch cell-state signaling program",
        "source_locator": "PMID:10551863; DOI:10.1074/jbc.274.46.32961; PMID:10329626",
        "species_support": "mouse; human comparator",
        "basis": (
            "Primary receptor-binding and co-culture studies support JAG1 engagement of Notch receptors, including NOTCH1, with receptor-dependent canonical Notch signaling. "
            "This recovers an exact JAG1-NOTCH1 program, but does not claim a specific CSL/RBPJ target locus or SCI receiver-cell mechanism."
        ),
        "scope": "Ligand presentation, Fringe modification, receptor fragment versus full-length receptor context, and lymphocyte/endothelial model differences constrain transfer; no terminal TF occupancy was measured.",
    },
    "M22B-E005629": {
        "evidence_id": "M22B-EVID-005509",
        "source_entity": "PDGFC",
        "relation_type": "Proteolytically activated PDGF-C binds preferentially to PDGFRA and supports PDGFRA-dependent receptor-tyrosine-kinase signaling; no terminal TF-target regulation is assigned",
        "target_entity": "processed PDGF-C-PDGFRA -> receptor tyrosine-kinase growth signaling program",
        "source_locator": "PMID:12598536; PMID:15061151; PMID:15207812",
        "species_support": "mouse; human comparator",
        "basis": (
            "Primary ligand-processing, binding, and receptor-function studies support proteolytically activated PDGF-C engagement of PDGFRA and PDGFRA-dependent signaling. "
            "This recovers a bounded PDGF-C-PDGFRA receptor program, but does not assign an unprocessed-ligand mechanism, terminal TF, or SCI-specific response."
        ),
        "scope": "PDGF-C activation processing and receptor selectivity are context dependent; cited models are broader than a clean SCI receiver assay and no terminal TF occupancy was measured.",
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
            raise SystemExit(f"missing batch014 row for {edge_id}")
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
        edge["consolidation_note"] = append_once(edge["consolidation_note"], f"Low-confidence recovery batch014: medium after exact primary receptor/function re-review for {change['source_entity']}.")
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
        ev["consolidation_note"] = append_once(ev["consolidation_note"], "Low-confidence recovery batch014: exact primary receptor-binding/function evidence recovered; terminal TF claim remains excluded.")
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
