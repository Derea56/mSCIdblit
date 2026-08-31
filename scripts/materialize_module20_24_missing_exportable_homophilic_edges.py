#!/usr/bin/env python3
"""Generate SQL for the five exportable homophilic edges missing from the DB.

The B-layer registers encode these as self-interactions.  The canonical
database deliberately rejects self-loop ``SignalingEdge`` rows, so each is
represented as ``protein -> homophilic complex``.  This is a graph
representation of the tested homophilic assembly, not an inferred distinct
receptor or intracellular mechanism.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path

from materialize_module20_24_paper_provenance import sql


ROOT = Path(__file__).resolve().parents[1]
OUT_SQL = ROOT / "work" / "cross_module_synthesis" / "canonical_evidence_review" / "module20_24_missing_exportable_homophilic_edges.sql"

ITEMS = {
    "M20B-EVID-001498": {
        "module": "20B",
        "b_edge_id": "M20B-E001498",
        "source_name": "Pcdha4b",
        "target_name": "Pcdha4b homophilic complex",
        "source_entity_type": "ligand",
        "source_gene_symbol": "Pcdha4b",
        "source_organism_scope": "mouse",
        "source_aliases": "PCDHA4B; Pcdha4b; Pcdh-alpha4",
        "target_organism_scope": "mouse",
        "pathway_name": "PCDHA4B homophilic adhesion",
        "pathway_description": "PCDHA4B homophilic trans-adhesion supported by direct primary assays in mouse neurons and transfected cells.",
    },
    "M20B-EVID-002375": {
        "module": "20B",
        "b_edge_id": "M20B-E002375",
        "source_name": "Ncam1",
        "target_name": "NCAM1 homophilic complex",
        "source_entity_type": "ligand",
        "source_gene_symbol": "Ncam1",
        "source_organism_scope": "mouse; rat; chick; human comparator",
        "source_aliases": "NCAM1; Ncam1",
        "target_organism_scope": "mouse; rat; chick; human comparator",
        "pathway_name": "NCAM1 homophilic adhesion Module 20B",
        "pathway_description": "NCAM1 homophilic adhesion and associated neurite relay supported by direct domain, cell, and perturbation assays.",
    },
    "M24B-EVID-000124": {
        "module": "24B",
        "b_edge_id": "M24B-E000087",
        "source_name": "Flrt3",
        "target_name": "FLRT3 homophilic complex",
        "source_entity_type": "ligand",
        "source_gene_symbol": "Flrt3",
        "source_organism_scope": "mouse; human comparator",
        "source_aliases": "FLRT3; Flrt3",
        "target_organism_scope": "mouse; human comparator",
        "pathway_name": "FLRT3 homophilic adhesion/migration branch",
        "pathway_description": "FLRT3 homophilic adhesion and cortical-neuron distribution comparator supported by structural and cell-aggregation assays.",
    },
    "M24B-EVID-000161": {
        "module": "24B",
        "b_edge_id": "M24B-E000119",
        "source_name": "PCDHGC5",
        "target_name": "PCDHGC5 homophilic complex",
        "source_entity_type": "ligand",
        "source_gene_symbol": "PCDHGC5",
        "source_organism_scope": "mouse; rat comparator",
        "source_aliases": "PCDHGC5; Pcdhgc5; gammaC5",
        "target_organism_scope": "mouse; rat comparator",
        "pathway_name": "PCDHGC5 homophilic synaptic adhesion",
        "pathway_description": "PCDHGC5 homophilic trans-adhesion supported by direct SPR and interface-mutagenesis assays.",
    },
    "M23B-EVID-000670": {
        "module": "23B",
        "b_edge_id": "M23B-E000490",
        "source_name": "CADM3",
        "target_name": "CADM3 homophilic complex",
        "source_entity_type": "ligand",
        "source_gene_symbol": "CADM3",
        "source_organism_scope": "zebrafish",
        "source_aliases": "CADM3; Cadm3",
        "target_organism_scope": "zebrafish",
        "pathway_name": "CADM3 homophilic adhesion",
        "pathway_description": "CADM3 homophilic adhesion and retinal-neuroepithelial proliferation control supported by ectodomain-dependent primary assays.",
    },
}


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def json_sql(payload: dict[str, object]) -> str:
    return sql(json.dumps(payload, sort_keys=True))


def bool_sql(value: bool) -> str:
    return "TRUE" if value else "FALSE"


def main() -> None:
    edges: dict[str, dict[str, str]] = {}
    evidence: dict[str, dict[str, str]] = {}
    ledger = {
        row["b_evidence_id"]: row
        for row in read_tsv(ROOT / "work" / "cross_module_synthesis" / "canonical_evidence_review" / "module20_24_evidence_grade_ledger.tsv")
    }
    for module in ("20b", "21b", "22b", "23b", "24b"):
        edge_path = ROOT / "work" / "module_b_consolidation" / f"module{module}" / f"module{module}_edge_register.tsv"
        evidence_path = ROOT / "work" / "module_b_consolidation" / f"module{module}" / f"module{module}_evidence_register.tsv"
        edges.update({row["b_edge_id"]: row for row in read_tsv(edge_path)})
        evidence.update({row["b_evidence_id"]: row for row in read_tsv(evidence_path)})

    phase2 = {
        row["b_evidence_id"]: row
        for row in read_tsv(ROOT / "work" / "cross_module_synthesis" / "canonical_evidence_review" / "module20_24_integrated_phase2_extractions.tsv")
        if row["b_evidence_id"] in ITEMS
    }
    missing = sorted(set(ITEMS) - set(phase2))
    if missing:
        raise SystemExit("Missing exact Phase-2 rows: " + ", ".join(missing))

    lines = [
        "-- Exact integration of four exportable Module 20B-24B homophilic edges.",
        "-- Self-interactions are represented as protein -> homophilic complex",
        "-- because SignalingEdge enforces distinct source and target nodes.",
        "BEGIN;",
        "CREATE TEMP TABLE m2024_homophilic_edge_map (b_edge_id TEXT PRIMARY KEY, edge_id INTEGER NOT NULL);",
        "",
    ]

    for evidence_id in sorted(ITEMS):
        item = ITEMS[evidence_id]
        edge = edges[item["b_edge_id"]]
        ev = evidence[evidence_id]
        row = phase2[evidence_id]
        grade = ledger.get(evidence_id, {}).get("evidence_grade") or "U"
        context = ledger.get(evidence_id, {}).get("context_level") or "L0"
        boundary_note = (
            f"Exact B-layer self-interaction {item['b_edge_id']} represented as "
            f"{item['source_name']} -> {item['target_name']} because the canonical database "
            "rejects self-loop edges; this does not infer a distinct receptor or intracellular mechanism."
        )
        source_notes = {
            "canonicalization_batch": "module20_24_homophilic_exportable_2026_08_31",
            "b_edge_id": item["b_edge_id"],
            "b_evidence_id": evidence_id,
            "source_register_relation": edge["relation_type"],
            "source_register_target": edge["target_entity"],
            "homophilic_self_interaction_representation": f"{item['source_name']} -> {item['target_name']}",
            "phase2_extraction_id": row["extraction_id"],
            "source_locator": ev["source_locator"],
        }
        lines.extend([
            "INSERT INTO SignalingPathway (pathway_name, description, source_registry, notes)",
            f"VALUES ({sql(item['pathway_name'])}, {sql(item['pathway_description'])}, {sql('module20_24_B_layer')}, {sql(boundary_note)})",
            "ON CONFLICT (pathway_name) DO NOTHING;",
            "",
            "INSERT INTO SignalingEntity (canonical_name, entity_type, gene_symbol, organism_scope, aliases, notes)",
            f"VALUES ({sql(item['source_name'])}, {sql(item['source_entity_type'])}, {sql(item['source_gene_symbol'])}, {sql(item['source_organism_scope'])}, {sql(item['source_aliases'])}, {sql('Exact B-layer homophilic-edge endpoint; source entity.')})",
            "ON CONFLICT (canonical_name) DO NOTHING;",
            "INSERT INTO SignalingEntity (canonical_name, entity_type, organism_scope, aliases, notes)",
            f"VALUES ({sql(item['target_name'])}, 'receptor', {sql(item['target_organism_scope'])}, {sql(item['source_name'] + ' homophilic assembly')}, {sql(boundary_note)})",
            "ON CONFLICT (canonical_name) DO NOTHING;",
            "",
            "INSERT INTO SignalingEntityRole (entity_id, role, role_status, export_priority, role_source, role_evidence)",
            f"SELECT entity_id, 'ligand', 'derived', 'low', {sql('Module 20-24 canonical homophilic-edge integration 2026-08-31')}, {sql('Exact B-layer evidence ' + evidence_id + '; Phase-2 extraction ' + row['extraction_id'] + '.')} FROM SignalingEntity WHERE canonical_name={sql(item['source_name'])}",
            "ON CONFLICT (entity_id, role) DO NOTHING;",
            "INSERT INTO SignalingEntityRole (entity_id, role, role_status, export_priority, role_source, role_evidence)",
            f"SELECT entity_id, 'signaling_cascade', 'derived', 'low', {sql('Module 20-24 canonical homophilic-edge integration 2026-08-31')}, {sql('Exact B-layer evidence ' + evidence_id + '; homophilic assembly is represented as a graph node.')} FROM SignalingEntity WHERE canonical_name={sql(item['source_name'])}",
            "ON CONFLICT (entity_id, role) DO NOTHING;",
            "INSERT INTO SignalingEntityRole (entity_id, role, role_status, export_priority, role_source, role_evidence)",
            f"SELECT entity_id, 'receptor', 'derived', 'low', {sql('Module 20-24 canonical homophilic-edge integration 2026-08-31')}, {sql('Exact B-layer evidence ' + evidence_id + '; target is a representation of the tested homophilic assembly.')} FROM SignalingEntity WHERE canonical_name={sql(item['target_name'])}",
            "ON CONFLICT (entity_id, role) DO NOTHING;",
            "INSERT INTO SignalingEntityRole (entity_id, role, role_status, export_priority, role_source, role_evidence)",
            f"SELECT entity_id, 'signaling_cascade', 'derived', 'low', {sql('Module 20-24 canonical homophilic-edge integration 2026-08-31')}, {sql('Exact B-layer evidence ' + evidence_id + '; homophilic assembly is represented as a graph node.')} FROM SignalingEntity WHERE canonical_name={sql(item['target_name'])}",
            "ON CONFLICT (entity_id, role) DO NOTHING;",
            "",
            "INSERT INTO SignalingEdge (source_entity_id, target_entity_id, pathway_id, relation_type, effect_polarity, directionality, compartment_context, species_context, evidence_status, context_scope, export_priority, notes)",
            f"SELECT source.entity_id, target.entity_id, pathway.pathway_id, 'binds_receptor', 'unknown', 'directed', 'cell surface/adhesion', {sql(edge['species_context'])}, 'evidence_backed_homophilic_adhesion', {sql(edge['context_scope'])}, 'medium', {sql(boundary_note)}",
            f"FROM SignalingEntity source JOIN SignalingEntity target ON target.canonical_name={sql(item['target_name'])} JOIN SignalingPathway pathway ON pathway.pathway_name={sql(item['pathway_name'])}",
            f"WHERE source.canonical_name={sql(item['source_name'])}",
            "  AND NOT EXISTS (SELECT 1 FROM SignalingEdge existing WHERE existing.source_entity_id=source.entity_id AND existing.target_entity_id=target.entity_id AND existing.pathway_id=pathway.pathway_id AND existing.relation_type='binds_receptor');",
            "INSERT INTO m2024_homophilic_edge_map (b_edge_id, edge_id)",
            f"SELECT {sql(item['b_edge_id'])}, edge.edge_id FROM SignalingEdge edge JOIN SignalingEntity source ON source.entity_id=edge.source_entity_id JOIN SignalingEntity target ON target.entity_id=edge.target_entity_id JOIN SignalingPathway pathway ON pathway.pathway_name={sql(item['pathway_name'])} WHERE source.canonical_name={sql(item['source_name'])} AND target.canonical_name={sql(item['target_name'])} AND edge.pathway_id=pathway.pathway_id AND edge.relation_type='binds_receptor' ON CONFLICT (b_edge_id) DO NOTHING;",
            "",
            "INSERT INTO SignalingEdgeRegister (edge_id, register_edge_id, module, source_label, target_label, register_relation_type, graph_relation_type, pathway_name, evidence_layer, edge_status, confidence_tier, evidence_ids, consolidation_note)",
            f"SELECT map.edge_id, {sql(item['b_edge_id'])}, {sql(item['module'])}, {sql(item['source_name'])}, {sql(item['target_name'])}, {sql(edge['relation_type'])}, 'binds_receptor', {sql(item['pathway_name'])}, {sql(edge['evidence_layer'])}, {sql(edge['edge_status'])}, {sql(edge['confidence_tier'])}, {sql(evidence_id)}, {sql(boundary_note)} FROM m2024_homophilic_edge_map map WHERE map.b_edge_id={sql(item['b_edge_id'])} ON CONFLICT (register_edge_id) DO NOTHING;",
            "",
            "INSERT INTO SignalingEdgeRegisterSource (edge_id, register_edge_id, register_evidence_id, module, support_kind, species_support, source_scope, confidence_tier, citation_note, notes, source_kind, source_locator, source_locator_status, evidence_summary, limitations, evidence_layer, evidence_exportable, consolidation_note, evidence_grade, context_level, grading_basis, grading_status)",
            f"SELECT map.edge_id, {sql(item['b_edge_id'])}, {sql(evidence_id)}, {sql(item['module'])}, {sql(ev['support_kind'])}, {sql(ev['species_support'])}, {sql(ev['source_scope'])}, {sql(ev['confidence_tier'])}, {sql(ev['citation_note'])}, {json_sql(source_notes)}, {sql(ev['source_kind'])}, {sql(ev['source_locator'])}, {sql('stable_plus_local' if 'PMID:' in ev['source_locator'] else 'local_only_or_unresolved')}, {sql(ev['evidence_summary'])}, {sql(ev['limitations'])}, {sql(ev['evidence_layer'])}, {bool_sql(ev['exportable'] == 'true')}, {sql(ev['consolidation_note'])}, {sql(grade)}, {sql(context)}, {sql('Preserved exact B-layer grade/context from the evidence-grade ledger; homophilic graph representation is documented in notes.')}, {sql('homophilic_exportable_register_source')} FROM m2024_homophilic_edge_map map WHERE map.b_edge_id={sql(item['b_edge_id'])} ON CONFLICT (edge_id, register_evidence_id) DO NOTHING;",
            "",
        ])

    lines.extend(["COMMIT;", ""])
    OUT_SQL.write_text("\n".join(lines))
    print(f"integrated_items={len(ITEMS)} sql={OUT_SQL}")


if __name__ == "__main__":
    main()
