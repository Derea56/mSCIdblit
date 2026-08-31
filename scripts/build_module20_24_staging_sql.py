#!/usr/bin/env python3
"""Build isolated PostgreSQL staging SQL for Module 20B-24B synthesis."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "work" / "cross_module_synthesis" / "module20_24_isolated_staging.sql"
LINKAGE = ROOT / "work" / "cross_module_synthesis" / "path_linkage_batches"


def copy_command(table: str, path: Path, columns: str) -> str:
    return (
        f"\\copy module20_24_staging.{table} ({columns}) FROM '{path}' "
        "WITH (FORMAT csv, HEADER true, DELIMITER E'\\t', QUOTE '" + '"' + "', ESCAPE '" + '"' + "', NULL '')"
    )


def main() -> None:
    paper_cols = "canonical_paper_key, canonical_merge_key, paper_ready, metadata_status, title, authors, publication_year, journal, volume, issue, pages, doi, pmid, pmcid, source_metadata_url, evidence_ids, modules, evidence_layers"
    anchor_cols = "evidence_id, module, linkage_edge_ids, b_edge_ids, source_a_evidence_id, evidence_layer, support_kind, source_scope, anchor_type, anchor_locator, canonical_paper_key, anchor_resolution_status, metadata_status, species_support"
    alias_cols = "raw_label, normalized_key, label_type, layer, linkage_edge_ids, source_rows, dedup_status, complex_preservation_note"
    linkage_cols = "path_id, ligand, receptor_complex, relay_or_pathway, terminal_tf_or_output, lr_edge_ids, lr_evidence_ids, relay_edge_ids, relay_evidence_ids, downstream_edge_ids, downstream_evidence_ids, linkage_status, evidence_confidence, species_and_model_context, assay_or_perturbation, context_and_limitations, source_locators"
    lines = [
        "-- Isolated Module 20B-24B source-anchor and linkage staging.",
        "-- This file does not modify canonical Paper, Observation, AuthorClaim, SignalingEdge, or SignalingEdgeSource tables.",
        "BEGIN;",
        "CREATE SCHEMA IF NOT EXISTS module20_24_staging;",
        "DROP TABLE IF EXISTS module20_24_staging.promoted_path_linkage;",
        "DROP TABLE IF EXISTS module20_24_staging.entity_pathway_dedup_audit;",
        "DROP TABLE IF EXISTS module20_24_staging.promoted_source_anchor_resolution;",
        "DROP TABLE IF EXISTS module20_24_staging.canonical_paper_anchor_map;",
        "DROP TABLE IF EXISTS module20_24_staging.canonical_paper_metadata;",
        "CREATE TABLE module20_24_staging.canonical_paper_metadata (canonical_paper_key TEXT PRIMARY KEY, canonical_merge_key TEXT NOT NULL, paper_ready BOOLEAN NOT NULL, metadata_status TEXT NOT NULL, title TEXT, authors TEXT, publication_year INTEGER, journal TEXT, volume TEXT, issue TEXT, pages TEXT, doi TEXT, pmid TEXT, pmcid TEXT, source_metadata_url TEXT, evidence_ids TEXT, modules TEXT, evidence_layers TEXT);",
        "CREATE TABLE module20_24_staging.canonical_paper_anchor_map (canonical_paper_key TEXT PRIMARY KEY, primary_anchor_type TEXT NOT NULL, primary_anchor_locator TEXT NOT NULL, alternate_anchor_types TEXT, evidence_ids TEXT, modules TEXT, evidence_layers TEXT, anchor_resolution_status TEXT NOT NULL, metadata_status TEXT NOT NULL);",
        "CREATE TABLE module20_24_staging.promoted_source_anchor_resolution (evidence_id TEXT NOT NULL, module TEXT NOT NULL, linkage_edge_ids TEXT NOT NULL, b_edge_ids TEXT NOT NULL, source_a_evidence_id TEXT, evidence_layer TEXT NOT NULL, support_kind TEXT NOT NULL, source_scope TEXT, anchor_type TEXT NOT NULL, anchor_locator TEXT NOT NULL, canonical_paper_key TEXT NOT NULL, anchor_resolution_status TEXT NOT NULL, metadata_status TEXT NOT NULL, species_support TEXT, PRIMARY KEY (evidence_id, anchor_type, anchor_locator));",
        "CREATE TABLE module20_24_staging.entity_pathway_dedup_audit (raw_label TEXT NOT NULL, normalized_key TEXT NOT NULL, label_type TEXT NOT NULL, layer TEXT NOT NULL, linkage_edge_ids TEXT NOT NULL, source_rows INTEGER NOT NULL, dedup_status TEXT NOT NULL, complex_preservation_note TEXT NOT NULL);",
        "CREATE TABLE module20_24_staging.promoted_path_linkage (path_id TEXT PRIMARY KEY, ligand TEXT NOT NULL, receptor_complex TEXT NOT NULL, relay_or_pathway TEXT NOT NULL, terminal_tf_or_output TEXT NOT NULL, lr_edge_ids TEXT NOT NULL, lr_evidence_ids TEXT NOT NULL, relay_edge_ids TEXT, relay_evidence_ids TEXT, downstream_edge_ids TEXT, downstream_evidence_ids TEXT, linkage_status TEXT NOT NULL, evidence_confidence TEXT NOT NULL, species_and_model_context TEXT NOT NULL, assay_or_perturbation TEXT NOT NULL, context_and_limitations TEXT NOT NULL, source_locators TEXT NOT NULL);",
        copy_command("canonical_paper_metadata", ROOT / "work/cross_module_synthesis/module20_24_canonical_paper_metadata.tsv", paper_cols) + ";",
        copy_command("canonical_paper_anchor_map", ROOT / "work/cross_module_synthesis/module20_24_canonical_paper_anchor_map.tsv", "canonical_paper_key, primary_anchor_type, primary_anchor_locator, alternate_anchor_types, evidence_ids, modules, evidence_layers, anchor_resolution_status, metadata_status") + ";",
        copy_command("promoted_source_anchor_resolution", ROOT / "work/cross_module_synthesis/module20_24_promoted_source_anchor_resolution.tsv", anchor_cols) + ";",
        copy_command("entity_pathway_dedup_audit", ROOT / "work/cross_module_synthesis/module20_24_entity_pathway_dedup_audit.tsv", alias_cols) + ";",
    ]
    for path in sorted(LINKAGE.glob("module20_24_path_linkage_block*.tsv")):
        lines.append(copy_command("promoted_path_linkage", path, linkage_cols) + ";")
    lines.extend([
        "DO $$",
        "DECLARE duplicate_paths INTEGER; duplicate_papers INTEGER; bad_anchor_rows INTEGER; unresolved_required INTEGER;",
        "BEGIN",
        "  SELECT COUNT(*) INTO duplicate_paths FROM (SELECT path_id FROM module20_24_staging.promoted_path_linkage GROUP BY path_id HAVING COUNT(*) > 1) d;",
        "  SELECT COUNT(*) INTO duplicate_papers FROM (SELECT canonical_paper_key FROM module20_24_staging.canonical_paper_metadata GROUP BY canonical_paper_key HAVING COUNT(*) > 1) d;",
        "  SELECT COUNT(*) INTO bad_anchor_rows FROM module20_24_staging.promoted_source_anchor_resolution WHERE anchor_locator = '' OR canonical_paper_key = '';",
        "  SELECT COUNT(*) INTO unresolved_required FROM module20_24_staging.canonical_paper_metadata WHERE paper_ready AND (title IS NULL OR title = '');",
        "  IF duplicate_paths > 0 OR duplicate_papers > 0 OR bad_anchor_rows > 0 OR unresolved_required > 0 THEN",
        "    RAISE EXCEPTION 'Module 20B-24B staging validation failed: duplicate_paths=%, duplicate_papers=%, bad_anchor_rows=%, unresolved_required=%', duplicate_paths, duplicate_papers, bad_anchor_rows, unresolved_required;",
        "  END IF;",
        "END $$;",
        "COMMIT;",
    ])
    OUT.write_text("\n".join(lines) + "\n")
    print(f"wrote {OUT} with {len(list(LINKAGE.glob('module20_24_path_linkage_block*.tsv')))} linkage COPY inputs")


if __name__ == "__main__":
    main()
