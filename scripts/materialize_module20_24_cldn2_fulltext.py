#!/usr/bin/env python3
"""Generate SQL for the two CLDN2 rows resolved from local primary full text.

The original Phase-2 rows were held because only a PMCID locator and no
validated atomic extraction had been retained.  The repository contains the
NCBI full-text record for PMID 22645303/PMCID PMC3434516.  This materializer
uses the paper's reported CLDN2--CLDN2 trans-homotypic interaction and the
separate liver-metastasis functional result, preserving the B/L1 grades from
the evidence ledger.  It does not transfer the comparator evidence to CNS or
SCI context and does not merge the two evidence layers.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path

from materialize_module20_24_paper_provenance import sql


ROOT = Path(__file__).resolve().parents[1]
REVIEW_ROOT = ROOT / "work" / "cross_module_synthesis" / "canonical_evidence_review"
PHASE2 = REVIEW_ROOT / "module20_24_integrated_phase2_extractions.tsv"
OUT_SQL = REVIEW_ROOT / "module20_24_cldn2_fulltext_materialization.sql"

SOURCE_HTML = "data/raw/evidence/module20_24_supervised_cli_phase2/retry_C23B096_PMC3434516_ncbi.html"
PAPER = {
    "title": "Claudin-2 Promotes Breast Cancer Liver Metastasis by Facilitating Tumor Cell Interactions with Hepatocytes",
    "authors": (
        "Sébastien Tabariès; Fanny Dupuy; Zhifeng Dong; Anie Monast; "
        "Matthew G Annis; Jonathan Spicer; Lorenzo E Ferri; Atilla Omeroglu; "
        "Mark Basik; Eitan Amir; Mark Clemons; Peter M Siegel"
    ),
    "publication_year": 2012,
    "journal": "Molecular and Cellular Biology",
    "volume": "32",
    "issue": "15",
    "pages": "2979",
    "doi": "10.1128/MCB.00299-12",
    "pmid": "PMID:22645303",
    "abstract": (
        "We previously identified claudin-2 as a functional mediator of breast cancer liver metastasis. "
        "We now confirm that claudin-2 levels are elevated in liver metastases, but not in skin metastases, "
        "compared to levels in their matched primary tumors in patients with breast cancer. Moreover, claudin-2 "
        "is specifically expressed in liver-metastatic breast cancer cells compared to populations derived from "
        "bone or lung metastases. The increased liver tropism exhibited by claudin-2-expressing breast cancer "
        "cells requires claudin-2-mediated interactions between breast cancer cells and primary hepatocytes. "
        "Furthermore, the reduction of the claudin-2 expression level, either in cancer cells or in primary "
        "hepatocytes, diminishes these heterotypic cell-cell interactions. Finally, we demonstrate that the first "
        "claudin-2 extracellular loop is essential for mediating tumor cell-hepatocyte interactions and the ability "
        "of breast cancer cells to form liver metastases in vivo. Thus, during breast cancer liver metastasis, "
        "claudin-2 shifts from acting within tight-junctional complexes to functioning as an adhesion molecule "
        "between breast cancer cells and hepatocytes."
    ),
    "url": "https://pubmed.ncbi.nlm.nih.gov/22645303/",
}

ITEMS = {
    "M23B-EVID-000501": {
        "edge_id": "M23B-E000343",
        "extraction_id": "M23B-P2-R-000462",
        "evidence_layer": "ligand_receptor_or_direct_molecular",
        "outcome_type": "molecular_signaling_output",
        "pathway_name": "Claudin-2 homophilic adhesion and metastatic cell-hepatocyte interaction",
        "pathway_description": "CLDN2 trans-homotypic adhesion between liver-metastatic breast-cancer cells and primary hepatocytes, resolved from the primary full text.",
        "register_relation_type": "binds/activates",
        "graph_relation_type": "binds_receptor",
        "source_scope": "direct_edge",
        "figure_reference": "Fig. 8B; Fig. 9A-C",
        "source_section": "RESULTS: Claudin-2 promotes breast cancer cell adhesion to hepatocytes; RESULTS: Claudin-2 expression is required for primary hepatocytes to promote breast cancer cell adhesion",
        "assay": "cell attachment assay; claudin-2 siRNA knockdown; claudin-4 extracellular-loop chimera rescue",
        "cell_model": "mouse primary hepatocytes and liver-aggressive 4T1-derived breast-cancer populations",
        "perturbation": "two independent mouse claudin-2 siRNAs in hepatocytes; claudin-2 knockdown and claudin-4/claudin-2 loop chimeras in cancer cells",
        "observation": "Two independent claudin-2 siRNAs reduced claudin-2 in primary mouse hepatocytes by 25-50% over four independent experiments and attenuated adhesion of two liver-aggressive breast-cancer populations; the first extracellular-loop claudin-2 chimera rescued adhesion after cancer-cell claudin-2 knockdown.",
        "claim": "The authors conclude that liver-metastatic breast-cancer cells interact with resident hepatocytes in part through trans-homotypic claudin-2-claudin-2 interactions, with the first extracellular loop as a major determinant.",
        "quote": "trans-homotypic interactions between claudin-2 molecules expressed in both cell types",
        "evidence_summary": "Primary full text reports trans-homotypic CLDN2-CLDN2 interactions between CLDN2-expressing breast-cancer cells and primary mouse hepatocytes, including first extracellular-loop chimera rescue and hepatocyte CLDN2 knockdown.",
        "limitations": "The comparator is breast-cancer liver metastasis rather than CNS or spinal-cord injury; the evidence is cell adhesion and loop-dependent functional interaction, not a purified affinity measurement.",
    },
    "M23B-EVID-000503": {
        "edge_id": "M23B-E000344",
        "extraction_id": "M23B-P2-R-000464",
        "evidence_layer": "downstream_or_functional",
        "outcome_type": "cellular_functional_output",
        "pathway_name": "Claudin-2 homophilic adhesion metastatic function",
        "pathway_description": "CLDN2-dependent hepatocyte adhesion and liver-metastatic burden, resolved as a downstream functional layer from the primary full text.",
        "register_relation_type": "promotes/modulates",
        "graph_relation_type": "promotes",
        "source_scope": "contextual_support",
        "figure_reference": "Fig. 10",
        "source_section": "RESULTS: The first extracellular loop of claudin-2 is sufficient for its pro-liver-metastatic functions",
        "assay": "splenic injection experimental metastasis assay; liver metastatic burden quantification",
        "cell_model": "liver-aggressive 4T1-derived breast-cancer cells in mouse experimental metastasis",
        "perturbation": "claudin-2 knockdown with claudin-4 or extracellular-loop chimeric rescue constructs",
        "observation": "Reduced claudin-2 decreased liver-metastatic burden after splenic injection; C4(C2/C2) and C4(C2/C4) chimeras rescued the phenotype, whereas wild-type claudin-4 and C4(C4/C2) did not.",
        "claim": "The authors conclude that claudin-2 promotes breast-cancer liver metastasis in part by promoting cell-cell interactions with hepatocytes through trans-homotypic claudin-2 complexes that require the first extracellular loop.",
        "quote": "These interactions are driven by trans-homotypic complexes between claudin-2 expressed by the cancer cell and claudin-2 expressed by the hepatocytes",
        "evidence_summary": "Primary full text reports CLDN2-dependent liver-metastatic burden and first extracellular-loop chimera rescue after splenic injection.",
        "limitations": "This is a non-CNS breast-cancer liver-metastasis comparator; it does not establish spinal-cord or SCI context and does not assert a transcription-factor or terminal target mechanism.",
    },
}


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def json_sql(payload: dict[str, object]) -> str:
    return sql(json.dumps(payload, sort_keys=True))


def db_text(value: str, limit: int) -> str:
    encoded = value.encode("utf-8")
    if len(encoded) <= limit:
        return value
    return encoded[: max(0, limit - 3)].decode("utf-8", errors="ignore") + "..."


def marker(column: str, extraction_id: str) -> str:
    return (
        f"{column} LIKE {sql('%\"canonicalization_batch\": \"module20_24_cldn2_fulltext_2026_08_31\"%')}"
        f" AND {column} LIKE {sql('%\"extraction_id\": \"' + extraction_id + '\"%')}"
    )


def main() -> None:
    phase2 = {row["b_evidence_id"]: row for row in read_tsv(PHASE2)}
    missing = sorted(set(ITEMS) - set(phase2))
    if missing:
        raise SystemExit("Missing exact Phase-2 rows: " + ", ".join(missing))

    lines = [
        "-- Exact local full-text materialization for the two CLDN2 Module 23B rows.",
        "-- Direct homophilic interaction and downstream metastasis function remain separate.",
        "-- Evidence grades/context levels are preserved as B/L1 from the ledger.",
        "BEGIN;",
        "",
        "CREATE TEMP TABLE m2024_cldn2_edges (b_edge_id TEXT PRIMARY KEY, edge_id INTEGER NOT NULL);",
        "CREATE TEMP TABLE m2024_cldn2_experiments (extraction_id TEXT PRIMARY KEY, experiment_id INTEGER NOT NULL);",
        "CREATE TEMP TABLE m2024_cldn2_observations (extraction_id TEXT PRIMARY KEY, observation_id INTEGER NOT NULL);",
        "CREATE TEMP TABLE m2024_cldn2_claims (extraction_id TEXT PRIMARY KEY, claim_id INTEGER NOT NULL);",
        "",
        "INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, abstract, url)",
        f"VALUES ({sql(PAPER['title'])}, {sql(PAPER['authors'])}, {PAPER['publication_year']}, {sql(PAPER['journal'])}, {sql(PAPER['volume'])}, {sql(PAPER['issue'])}, {sql(PAPER['pages'])}, {sql(PAPER['doi'])}, {sql(PAPER['pmid'])}, {sql(PAPER['abstract'])}, {sql(PAPER['url'])})",
        "ON CONFLICT (pmid) DO NOTHING;",
        "",
        "INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)",
        f"SELECT paper_id, {sql('Module 23B CLDN2 primary-full-text evidence extraction')}, {sql('Source-defined extraction of the exact CLDN2 homophilic adhesion and liver-metastasis results from PMID 22645303; not a claim about the publication experiment numbering.')}, {sql('Primary-paper full-text Results and figure-legend verification with separate molecular and downstream functional evidence units.')}",
        f"FROM Paper WHERE pmid={sql(PAPER['pmid'])} AND NOT EXISTS (SELECT 1 FROM ExperimentalParadigm WHERE paper_id=Paper.paper_id AND paradigm_name={sql('Module 23B CLDN2 primary-full-text evidence extraction')});",
        "",
    ]

    for evidence_id, item in ITEMS.items():
        phase = phase2[evidence_id]
        notes = {
            "canonicalization_batch": "module20_24_cldn2_fulltext_2026_08_31",
            "extraction_id": item["extraction_id"],
            "b_edge_id": item["edge_id"],
            "b_evidence_id": evidence_id,
            "canonical_paper_key": PAPER["pmid"],
            "source_locator": f"PMID:22645303; PMCID:PMC3434516; DOI:10.1128/MCB.00299-12; local={SOURCE_HTML}",
            "source_defined_evidence_unit": True,
            "previous_phase2_observation_status": phase.get("observation_status", ""),
            "previous_phase2_claim_status": phase.get("claim_status", ""),
            "evidence_grade": "B",
            "context_level": "L1",
            "context_basis": "Non-CNS breast-cancer liver-metastasis comparator; no CNS, spinal-cord, or SCI context is asserted.",
            "source_section": item["source_section"],
            "figure_or_table": item["figure_reference"],
            "cell_or_model": item["cell_model"],
            "assay": item["assay"],
            "perturbation": item["perturbation"],
        }
        lines.extend([
            "INSERT INTO SignalingPathway (pathway_name, description, source_registry, notes)",
            f"VALUES ({sql(item['pathway_name'])}, {sql(item['pathway_description'])}, {sql('module20_24_B_layer')}, {sql('Exact full-text CLDN2 route; direct and functional evidence layers remain separate.')})",
            "ON CONFLICT (pathway_name) DO NOTHING;",
            "",
            "INSERT INTO SignalingEntity (canonical_name, entity_type, gene_symbol, organism_scope, aliases, notes)",
            f"VALUES ('CLDN2', 'ligand', 'CLDN2', {sql('mouse; human comparator')}, {sql('CLDN2; claudin-2')}, {sql('Exact primary full-text source entity; comparator protein involved in trans-homotypic adhesion.')})",
            "ON CONFLICT (canonical_name) DO NOTHING;",
            "INSERT INTO SignalingEntity (canonical_name, entity_type, organism_scope, aliases, notes)",
            f"VALUES ('CLDN2 homophilic complex', 'receptor', {sql('mouse; human comparator')}, {sql('CLDN2; claudin-2 trans-homotypic complex')}, {sql('Non-self-loop representation of the tested CLDN2-CLDN2 assembly; not a distinct receptor inference.')})",
            "ON CONFLICT (canonical_name) DO NOTHING;",
            "",
            "INSERT INTO SignalingEntityRole (entity_id, role, role_status, export_priority, role_source, role_evidence)",
            f"SELECT entity_id, 'ligand', 'derived', 'medium', {sql('Module 23B CLDN2 full-text verification 2026-08-31')}, {sql('Exact primary-paper PMID 22645303; B-layer evidence ' + evidence_id)} FROM SignalingEntity WHERE canonical_name='CLDN2' ON CONFLICT (entity_id, role) DO NOTHING;",
            "INSERT INTO SignalingEntityRole (entity_id, role, role_status, export_priority, role_source, role_evidence)",
            f"SELECT entity_id, 'signaling_cascade', 'derived', 'medium', {sql('Module 23B CLDN2 full-text verification 2026-08-31')}, {sql('CLDN2 trans-homotypic adhesion assembly; evidence ' + evidence_id)} FROM SignalingEntity WHERE canonical_name='CLDN2' ON CONFLICT (entity_id, role) DO NOTHING;",
            "INSERT INTO SignalingEntityRole (entity_id, role, role_status, export_priority, role_source, role_evidence)",
            f"SELECT entity_id, 'receptor', 'derived', 'medium', {sql('Module 23B CLDN2 full-text verification 2026-08-31')}, {sql('Homophilic complex representation; evidence ' + evidence_id)} FROM SignalingEntity WHERE canonical_name='CLDN2 homophilic complex' ON CONFLICT (entity_id, role) DO NOTHING;",
            "INSERT INTO SignalingEntityRole (entity_id, role, role_status, export_priority, role_source, role_evidence)",
            f"SELECT entity_id, 'signaling_cascade', 'derived', 'medium', {sql('Module 23B CLDN2 full-text verification 2026-08-31')}, {sql('Homophilic complex is a graph representation; evidence ' + evidence_id)} FROM SignalingEntity WHERE canonical_name='CLDN2 homophilic complex' ON CONFLICT (entity_id, role) DO NOTHING;",
            "",
            "INSERT INTO SignalingEdge (source_entity_id, target_entity_id, pathway_id, relation_type, effect_polarity, directionality, ligand_context, cell_type_context, compartment_context, species_context, injury_context, evidence_status, context_scope, export_priority, notes)",
            f"SELECT source.entity_id, target.entity_id, pathway.pathway_id, {sql(item['graph_relation_type'])}, {sql('activating' if item['graph_relation_type'] == 'promotes' else 'unknown')}, 'directed', {sql('CLDN2 trans-homotypic adhesion')}, {sql(item['cell_model'])}, 'cell surface/adhesion', {sql('mouse; human comparator')}, 'non-SCI comparator unless otherwise stated', {sql('fulltext_verified_evidence_backed')}, {sql('bounded primary comparator; no SCI transfer')}, 'medium', {sql('Exact full-text CLDN2 route; graph target is a homophilic-complex representation and direct/functional layers remain separate.')}",
            f"FROM SignalingEntity source JOIN SignalingEntity target ON target.canonical_name='CLDN2 homophilic complex' JOIN SignalingPathway pathway ON pathway.pathway_name={sql(item['pathway_name'])} WHERE source.canonical_name='CLDN2' AND NOT EXISTS (SELECT 1 FROM SignalingEdge e WHERE e.source_entity_id=source.entity_id AND e.target_entity_id=target.entity_id AND e.pathway_id=pathway.pathway_id AND e.relation_type={sql(item['graph_relation_type'])});",
            "INSERT INTO m2024_cldn2_edges (b_edge_id, edge_id)",
            f"SELECT {sql(item['edge_id'])}, e.edge_id FROM SignalingEdge e JOIN SignalingEntity source ON source.entity_id=e.source_entity_id JOIN SignalingEntity target ON target.entity_id=e.target_entity_id JOIN SignalingPathway pathway ON pathway.pathway_id=e.pathway_id WHERE source.canonical_name='CLDN2' AND target.canonical_name='CLDN2 homophilic complex' AND pathway.pathway_name={sql(item['pathway_name'])} AND e.relation_type={sql(item['graph_relation_type'])} ON CONFLICT (b_edge_id) DO NOTHING;",
            "INSERT INTO SignalingEdgeRegister (edge_id, register_edge_id, module, source_label, target_label, register_relation_type, graph_relation_type, pathway_name, evidence_layer, edge_status, confidence_tier, evidence_ids, consolidation_note)",
            f"SELECT map.edge_id, {sql(item['edge_id'])}, '23B', 'CLDN2', 'CLDN2 homophilic complex', {sql(item['register_relation_type'])}, {sql(item['graph_relation_type'])}, {sql(item['pathway_name'])}, {sql(item['evidence_layer'])}, 'staged_primary_review', 'medium', {sql(evidence_id)}, {sql('Full-text verified from PMID 22645303; exact direct/functional layer retained; no CNS or SCI transfer.')} FROM m2024_cldn2_edges map WHERE map.b_edge_id={sql(item['edge_id'])} ON CONFLICT (register_edge_id) DO NOTHING;",
            "",
            "INSERT INTO SignalingEdgeRegisterSource (edge_id, register_edge_id, register_evidence_id, module, support_kind, species_support, source_scope, confidence_tier, citation_note, notes, source_kind, source_locator, source_locator_status, evidence_summary, limitations, evidence_layer, evidence_exportable, consolidation_note, evidence_grade, context_level, grading_basis, grading_status)",
            f"SELECT map.edge_id, {sql(item['edge_id'])}, {sql(evidence_id)}, '23B', 'primary_experiment', 'mouse; human comparator', {sql(item['source_scope'])}, 'medium', {sql('PMID:22645303; PMCID:PMC3434516; DOI:10.1128/MCB.00299-12')}, {json_sql(dict(notes, record_type='canonical_register_source', source_locator_status='stable_plus_local'))}, 'primary_research_paper', {sql('PMID:22645303; PMCID:PMC3434516; DOI:10.1128/MCB.00299-12; local=' + SOURCE_HTML)}, 'stable_plus_local', {sql(item['evidence_summary'])}, {sql(item['limitations'])}, {sql(item['evidence_layer'])}, TRUE, {sql('Full-text verification resolves the source-unit blocker; direct and functional layers remain separate.')}, 'B', 'L1', {sql('Single primary full-text source verified; B/L1 ledger grade preserved. ' + notes['context_basis'])}, 'fulltext_verified_bounded' FROM m2024_cldn2_edges map WHERE map.b_edge_id={sql(item['edge_id'])} ON CONFLICT (edge_id, register_evidence_id) DO NOTHING;",
            "",
            "INSERT INTO Experiment (paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes)",
            f"SELECT p.paper_id, ep.paradigm_id, NULL, {sql(item['figure_reference'])}, {sql('Source-defined CLDN2 evidence unit ' + item['extraction_id'])}, {sql('Primary full-text result: ' + item['observation'])}, {json_sql(notes)} FROM Paper p JOIN ExperimentalParadigm ep ON ep.paper_id=p.paper_id AND ep.paradigm_name={sql('Module 23B CLDN2 primary-full-text evidence extraction')} WHERE p.pmid={sql(PAPER['pmid'])} AND NOT EXISTS (SELECT 1 FROM Experiment e WHERE {marker('e.notes', item['extraction_id'])});",
            "INSERT INTO m2024_cldn2_experiments (extraction_id, experiment_id)",
            f"SELECT {sql(item['extraction_id'])}, experiment_id FROM Experiment WHERE {marker('notes', item['extraction_id'])} ON CONFLICT (extraction_id) DO NOTHING;",
            "INSERT INTO Observation (experiment_id, evidence_type_id, outcome_type_id, observation_value, measurement_method, raw_observation_text, normalized_observation_value, source_section, figure_panel_reference, extraction_confidence, notes)",
            f"SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id, {sql(db_text(item['observation'], 500))}, {sql(db_text(item['assay'], 255))}, {sql(item['observation'])}, {sql(db_text(item['observation'], 500))}, {sql(db_text(item['source_section'], 100))}, {sql(db_text(item['figure_reference'], 100))}, 'medium', {json_sql(dict(notes, record_type='canonical_observation', full_observation_value=item['observation']))} FROM m2024_cldn2_experiments e JOIN ControlledVocabulary_EvidenceType et ON et.evidence_type_name={sql(item['evidence_layer'])} JOIN ControlledVocabulary_OutcomeType ot ON ot.outcome_type_name={sql(item['outcome_type'])} WHERE e.extraction_id={sql(item['extraction_id'])} AND NOT EXISTS (SELECT 1 FROM Observation existing WHERE {marker('existing.notes', item['extraction_id'])});",
            "INSERT INTO m2024_cldn2_observations (extraction_id, observation_id)",
            f"SELECT {sql(item['extraction_id'])}, observation_id FROM Observation WHERE {marker('notes', item['extraction_id'])} ON CONFLICT (extraction_id) DO NOTHING;",
            "INSERT INTO AuthorClaim (paper_id, claim_text, claim_type, confidence_level, source_section, source_quote, extraction_confidence, notes)",
            f"SELECT p.paper_id, {sql(item['claim'])}, 'curated_evidence_claim', 'medium', {sql(db_text(item['source_section'], 100))}, {sql(item['quote'])}, 'medium', {json_sql(dict(notes, record_type='canonical_claim', claim_origin='primary_fulltext_author_interpretation'))} FROM Paper p WHERE p.pmid={sql(PAPER['pmid'])} AND NOT EXISTS (SELECT 1 FROM AuthorClaim ac WHERE {marker('ac.notes', item['extraction_id'])});",
            "INSERT INTO m2024_cldn2_claims (extraction_id, claim_id)",
            f"SELECT {sql(item['extraction_id'])}, claim_id FROM AuthorClaim WHERE {marker('notes', item['extraction_id'])} ON CONFLICT (extraction_id) DO NOTHING;",
            "INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)",
            f"SELECT c.claim_id, o.observation_id, 'supports', {json_sql(dict(notes, record_type='canonical_evidence_link'))} FROM m2024_cldn2_claims c JOIN m2024_cldn2_observations o ON o.extraction_id=c.extraction_id WHERE c.extraction_id={sql(item['extraction_id'])} ON CONFLICT (claim_id, observation_id) DO NOTHING;",
            "",
            "INSERT INTO SignalingEdgeSource (edge_id, paper_id, observation_id, claim_id, support_kind, species_support, source_scope, confidence_tier, citation_note, notes, evidence_grade, context_level, grading_basis, grading_status)",
            f"SELECT map.edge_id, p.paper_id, o.observation_id, c.claim_id, 'primary_experiment', 'mixed', {sql(item['source_scope'])}, 'medium', {sql('PMID:22645303; PMCID:PMC3434516; DOI:10.1128/MCB.00299-12')}, {json_sql(dict(notes, record_type='canonical_edge_source', edge_support_status='supports_requested_edge', register_source_locator=SOURCE_HTML))}, 'B', 'L1', {sql('Single primary full-text source verified; B/L1 ledger grade preserved. ' + notes['context_basis'])}, 'fulltext_verified_bounded' FROM m2024_cldn2_edges map JOIN Paper p ON p.pmid={sql(PAPER['pmid'])} JOIN m2024_cldn2_observations o ON o.extraction_id={sql(item['extraction_id'])} JOIN m2024_cldn2_claims c ON c.extraction_id={sql(item['extraction_id'])} WHERE map.b_edge_id={sql(item['edge_id'])} AND NOT EXISTS (SELECT 1 FROM SignalingEdgeSource existing WHERE {marker('existing.notes', item['extraction_id'])});",
            "",
        ])

    lines.extend(["COMMIT;", ""])
    OUT_SQL.write_text("\n".join(lines), encoding="utf-8")
    print(f"integrated_items={len(ITEMS)} sql={OUT_SQL}")


if __name__ == "__main__":
    main()
