-- Module 21A audit-layer SQL staging materialization
-- Run from the repository root with psql and ON_ERROR_STOP enabled.
-- This script intentionally does not write Module 20A tables or core
-- simulator-facing SignalingEdge rows. It preserves stable Module 21A IDs,
-- source locators, evidence layers, and unresolved-case qualifiers.

\set ON_ERROR_STOP on
BEGIN;

DROP TABLE IF EXISTS module21a_unresolved_staging;
DROP TABLE IF EXISTS module21a_evidence_layer_staging;
DROP TABLE IF EXISTS module21a_perturbation_staging;
DROP TABLE IF EXISTS module21a_evidence_staging;
DROP TABLE IF EXISTS module21a_edge_staging;

CREATE TABLE module21a_edge_staging (
  batch_source TEXT NOT NULL,
  edge_id TEXT PRIMARY KEY,
  source_entity TEXT NOT NULL,
  relation_type TEXT NOT NULL,
  target_entity TEXT NOT NULL,
  pathway_name TEXT NOT NULL,
  effect_polarity TEXT,
  directionality TEXT,
  ligand_context TEXT,
  cell_type_context TEXT,
  compartment_context TEXT,
  species_context TEXT,
  injury_context TEXT,
  evidence_status TEXT,
  context_scope TEXT,
  confidence_tier TEXT,
  export_priority TEXT,
  curator_decision TEXT
);

CREATE TEMP TABLE _module21a_edges_main (LIKE module21a_edge_staging INCLUDING DEFAULTS);
CREATE TEMP TABLE _module21a_edges_seed (LIKE module21a_edge_staging INCLUDING DEFAULTS);
ALTER TABLE _module21a_edges_main ALTER COLUMN batch_source DROP NOT NULL;
ALTER TABLE _module21a_edges_seed ALTER COLUMN batch_source DROP NOT NULL;

\copy _module21a_edges_main (edge_id, source_entity, relation_type, target_entity, pathway_name, effect_polarity, directionality, ligand_context, cell_type_context, compartment_context, species_context, injury_context, evidence_status, context_scope, confidence_tier, export_priority, curator_decision) FROM 'work/module21_relay/module21a_saturation_edge_register.tsv' WITH (FORMAT csv, HEADER true, DELIMITER E'\t');
\copy _module21a_edges_seed (edge_id, source_entity, relation_type, target_entity, pathway_name, effect_polarity, directionality, ligand_context, cell_type_context, compartment_context, species_context, injury_context, evidence_status, context_scope, confidence_tier, export_priority, curator_decision) FROM 'work/module21_relay/module21a_il6_family_batch1_edge_register.tsv' WITH (FORMAT csv, HEADER true, DELIMITER E'\t');

INSERT INTO module21a_edge_staging
SELECT 'main_register', edge_id, source_entity, relation_type, target_entity, pathway_name,
       effect_polarity, directionality, ligand_context, cell_type_context,
       compartment_context, species_context, injury_context, evidence_status,
       context_scope, confidence_tier, export_priority, curator_decision
FROM _module21a_edges_main;

INSERT INTO module21a_edge_staging
SELECT 'q001_seed_register', edge_id, source_entity, relation_type, target_entity, pathway_name,
       effect_polarity, directionality, ligand_context, cell_type_context,
       compartment_context, species_context, injury_context, evidence_status,
       context_scope, confidence_tier, export_priority, curator_decision
FROM _module21a_edges_seed;

CREATE TABLE module21a_evidence_staging (
  batch_source TEXT NOT NULL,
  evidence_id TEXT PRIMARY KEY,
  edge_id TEXT NOT NULL,
  source_kind TEXT NOT NULL,
  source_locator TEXT NOT NULL,
  support_kind TEXT NOT NULL,
  species_support TEXT,
  source_species_detail TEXT,
  source_scope TEXT,
  confidence_tier TEXT,
  citation_note TEXT,
  evidence_summary TEXT,
  limitations TEXT
);

CREATE TEMP TABLE _module21a_evidence_main (LIKE module21a_evidence_staging INCLUDING DEFAULTS);
CREATE TEMP TABLE _module21a_evidence_seed (LIKE module21a_evidence_staging INCLUDING DEFAULTS);
ALTER TABLE _module21a_evidence_main ALTER COLUMN batch_source DROP NOT NULL;
ALTER TABLE _module21a_evidence_seed ALTER COLUMN batch_source DROP NOT NULL;

\copy _module21a_evidence_main (evidence_id, edge_id, source_kind, source_locator, support_kind, species_support, source_species_detail, source_scope, confidence_tier, citation_note, evidence_summary, limitations) FROM 'work/module21_relay/module21a_saturation_evidence_register.tsv' WITH (FORMAT csv, HEADER true, DELIMITER E'\t');
\copy _module21a_evidence_seed (evidence_id, edge_id, source_kind, source_locator, support_kind, species_support, source_species_detail, source_scope, confidence_tier, citation_note, evidence_summary, limitations) FROM 'work/module21_relay/module21a_il6_family_batch1_evidence_register.tsv' WITH (FORMAT csv, HEADER true, DELIMITER E'\t');

INSERT INTO module21a_evidence_staging
SELECT 'main_register', evidence_id, edge_id, source_kind, source_locator, support_kind,
       species_support, source_species_detail, source_scope, confidence_tier,
       citation_note, evidence_summary, limitations
FROM _module21a_evidence_main;

INSERT INTO module21a_evidence_staging
SELECT 'q001_seed_register', evidence_id, edge_id, source_kind, source_locator, support_kind,
       species_support, source_species_detail, source_scope, confidence_tier,
       citation_note, evidence_summary, limitations
FROM _module21a_evidence_seed;

CREATE TABLE module21a_perturbation_staging (
  batch_source TEXT NOT NULL,
  perturbation_id TEXT PRIMARY KEY,
  edge_id_or_branch TEXT NOT NULL,
  source_locator TEXT NOT NULL,
  species TEXT,
  cell_or_tissue_context TEXT,
  perturbation_type TEXT,
  perturbation_target TEXT,
  observed_effect TEXT,
  interpretation_boundary TEXT,
  confidence TEXT
);

CREATE TEMP TABLE _module21a_perturbations_main (LIKE module21a_perturbation_staging INCLUDING DEFAULTS);
CREATE TEMP TABLE _module21a_perturbations_seed (LIKE module21a_perturbation_staging INCLUDING DEFAULTS);
ALTER TABLE _module21a_perturbations_main ALTER COLUMN batch_source DROP NOT NULL;
ALTER TABLE _module21a_perturbations_seed ALTER COLUMN batch_source DROP NOT NULL;

\copy _module21a_perturbations_main (perturbation_id, edge_id_or_branch, source_locator, species, cell_or_tissue_context, perturbation_type, perturbation_target, observed_effect, interpretation_boundary, confidence) FROM 'work/module21_relay/module21a_saturation_perturbation_register.tsv' WITH (FORMAT csv, HEADER true, DELIMITER E'\t');
\copy _module21a_perturbations_seed (perturbation_id, edge_id_or_branch, source_locator, species, cell_or_tissue_context, perturbation_type, perturbation_target, observed_effect, interpretation_boundary, confidence) FROM 'work/module21_relay/module21a_il6_family_batch1_perturbation_register.tsv' WITH (FORMAT csv, HEADER true, DELIMITER E'\t');

INSERT INTO module21a_perturbation_staging
SELECT 'main_register', perturbation_id, edge_id_or_branch, source_locator, species,
       cell_or_tissue_context, perturbation_type, perturbation_target, observed_effect,
       interpretation_boundary, confidence
FROM _module21a_perturbations_main;

INSERT INTO module21a_perturbation_staging
SELECT 'q001_seed_register', perturbation_id, edge_id_or_branch, source_locator, species,
       cell_or_tissue_context, perturbation_type, perturbation_target, observed_effect,
       interpretation_boundary, confidence
FROM _module21a_perturbations_seed;

CREATE TABLE module21a_evidence_layer_staging (
  edge_id TEXT PRIMARY KEY,
  queue_id TEXT NOT NULL,
  evidence_id TEXT NOT NULL,
  evidence_layer TEXT NOT NULL,
  edge_class TEXT NOT NULL,
  layer_boundary TEXT NOT NULL
);

\copy module21a_evidence_layer_staging (edge_id, queue_id, evidence_id, evidence_layer, edge_class, layer_boundary) FROM 'work/module21_relay/module21a_evidence_layer_register.tsv' WITH (FORMAT csv, HEADER true, DELIMITER E'\t');

CREATE TABLE module21a_unresolved_staging (
  case_id TEXT PRIMARY KEY,
  queue_id TEXT NOT NULL,
  family_name TEXT NOT NULL,
  target_scope TEXT NOT NULL,
  evidence_layer TEXT NOT NULL,
  resolution_status TEXT NOT NULL,
  search_boundary TEXT NOT NULL,
  stable_sources TEXT,
  context_and_limitation TEXT NOT NULL,
  follow_up TEXT NOT NULL
);

\copy module21a_unresolved_staging FROM 'work/module21_relay/module21a_unresolved_register.tsv' WITH (FORMAT csv, HEADER true, DELIMITER E'\t');

-- Integrity assertions. Any failure aborts the transaction.
DO $$
DECLARE
  n INTEGER;
BEGIN
  SELECT COUNT(*) INTO n FROM module21a_edge_staging;
  IF n <> 110 THEN RAISE EXCEPTION 'Expected 110 combined edges, found %', n; END IF;

  SELECT COUNT(*) INTO n FROM module21a_evidence_staging;
  IF n <> 50 THEN RAISE EXCEPTION 'Expected 50 combined evidence records, found %', n; END IF;

  SELECT COUNT(*) INTO n FROM module21a_perturbation_staging;
  IF n <> 54 THEN RAISE EXCEPTION 'Expected 54 combined perturbation records, found %', n; END IF;

  SELECT COUNT(*) INTO n
  FROM module21a_edge_staging e
  WHERE NOT EXISTS (
    SELECT 1 FROM module21a_evidence_staging s
    WHERE e.edge_id = ANY(string_to_array(s.edge_id, ';'))
  );
  IF n <> 0 THEN RAISE EXCEPTION 'Edges without supporting evidence: %', n; END IF;

  SELECT COUNT(*) INTO n
  FROM (
    SELECT source_entity, relation_type, target_entity, pathway_name,
           ligand_context, cell_type_context, species_context
    FROM module21a_edge_staging
    GROUP BY source_entity, relation_type, target_entity, pathway_name,
             ligand_context, cell_type_context, species_context
    HAVING COUNT(*) > 1
  ) duplicate_keys;
  IF n <> 0 THEN RAISE EXCEPTION 'Duplicate edge keys: %', n; END IF;

  SELECT COUNT(*) INTO n
  FROM module21a_evidence_layer_staging l
  WHERE NOT EXISTS (SELECT 1 FROM module21a_edge_staging e WHERE e.edge_id = l.edge_id)
     OR NOT EXISTS (SELECT 1 FROM module21a_evidence_staging s WHERE s.evidence_id = l.evidence_id);
  IF n <> 0 THEN RAISE EXCEPTION 'Evidence-layer rows with invalid references: %', n; END IF;

  SELECT COUNT(*) INTO n
  FROM module21a_edge_staging e
  WHERE e.batch_source = 'main_register'
    AND NOT EXISTS (SELECT 1 FROM module21a_evidence_layer_staging l WHERE l.edge_id = e.edge_id);
  IF n <> 57 THEN RAISE EXCEPTION 'Expected 57 main edges without layer rows (seed excluded), found %', n; END IF;
END $$;

-- Review queries retained in the generated database for handoff.
COMMENT ON TABLE module21a_edge_staging IS 'Module 21A audit-layer edges; not yet mapped to core SignalingEdge IDs.';
COMMENT ON TABLE module21a_evidence_staging IS 'Module 21A stable evidence IDs and source locators.';
COMMENT ON TABLE module21a_evidence_layer_staging IS 'Explicit ligand/receptor, receptor-proximal, and downstream/function evidence-layer assignments.';
COMMENT ON TABLE module21a_unresolved_staging IS 'Explicit unresolved and bounded-search cases; do not silently drop.';

COMMIT;
