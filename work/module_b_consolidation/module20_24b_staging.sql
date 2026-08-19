-- Module 20B-24B audit-layer staging materialization.
-- Writes only module20b_* through module24b_* tables in the staging database.
\set ON_ERROR_STOP on
BEGIN;

DROP TABLE IF EXISTS module20b_complex_staging;

DO $$
DECLARE m TEXT;
BEGIN
  FOREACH m IN ARRAY ARRAY['20','21','22','23','24'] LOOP
    EXECUTE format('DROP TABLE IF EXISTS module%sb_boundary_staging', m);
    EXECUTE format('DROP TABLE IF EXISTS module%sb_consolidation_matrix_staging', m);
    EXECUTE format('DROP TABLE IF EXISTS module%sb_evidence_staging', m);
    EXECUTE format('DROP TABLE IF EXISTS module%sb_edge_staging', m);
  END LOOP;
END $$;

CREATE TABLE module20b_edge_staging (
  b_edge_id TEXT PRIMARY KEY, source_entity TEXT, relation_type TEXT,
  target_entity TEXT, pathway_name TEXT, evidence_layer TEXT,
  source_a_edge_id TEXT, edge_status TEXT, context_scope TEXT,
  cell_type_context TEXT, compartment_context TEXT, species_context TEXT,
  injury_context TEXT, confidence_tier TEXT, export_priority TEXT,
  exportable BOOLEAN, consolidation_note TEXT
);

CREATE TABLE module20b_evidence_staging (
  b_evidence_id TEXT PRIMARY KEY, source_a_evidence_id TEXT, b_edge_ids TEXT,
  source_kind TEXT, source_locator TEXT, support_kind TEXT,
  species_support TEXT, source_scope TEXT, confidence_tier TEXT,
  citation_note TEXT, evidence_summary TEXT, limitations TEXT,
  evidence_layer TEXT, exportable BOOLEAN, consolidation_note TEXT
);

CREATE TABLE module20b_boundary_staging (
  boundary_id TEXT PRIMARY KEY, source_a_evidence_id TEXT, source_a_edge_ids TEXT,
  boundary_type TEXT, source_locator TEXT, species_support TEXT,
  source_scope TEXT, summary TEXT, limitations TEXT
);

CREATE TABLE module20b_consolidation_matrix_staging (
  candidate_id TEXT PRIMARY KEY, source_a_status TEXT, b_status TEXT,
  layer1_status TEXT, layer2_status TEXT, layer3_status TEXT,
  species_posture TEXT, injury_context_posture TEXT, next_gap TEXT
);

CREATE TABLE module20b_complex_staging (
  complex_id TEXT PRIMARY KEY, source_review_id TEXT, complex_coverage TEXT,
  pair_label TEXT, note TEXT
);

\copy module20b_edge_staging FROM 'work/module_b_consolidation/module20b/module20b_edge_register.tsv' WITH (FORMAT csv, HEADER true, DELIMITER E'\t');
\copy module20b_evidence_staging FROM 'work/module_b_consolidation/module20b/module20b_evidence_register.tsv' WITH (FORMAT csv, HEADER true, DELIMITER E'\t');
\copy module20b_boundary_staging FROM 'work/module_b_consolidation/module20b/module20b_boundary_register.tsv' WITH (FORMAT csv, HEADER true, DELIMITER E'\t');
\copy module20b_consolidation_matrix_staging FROM 'work/module_b_consolidation/module20b/module20b_consolidation_matrix.tsv' WITH (FORMAT csv, HEADER true, DELIMITER E'\t');
\copy module20b_complex_staging FROM 'work/module_b_consolidation/module20b/module20b_complex_register.tsv' WITH (FORMAT csv, HEADER true, DELIMITER E'\t');

DO $$
DECLARE m TEXT; n INTEGER;
BEGIN
  FOREACH m IN ARRAY ARRAY['21','22','23','24'] LOOP
    EXECUTE format('CREATE TABLE module%sb_edge_staging (LIKE module20b_edge_staging INCLUDING ALL)', m);
    EXECUTE format('CREATE TABLE module%sb_evidence_staging (LIKE module20b_evidence_staging INCLUDING ALL)', m);
    EXECUTE format('CREATE TABLE module%sb_boundary_staging (LIKE module20b_boundary_staging INCLUDING ALL)', m);
    EXECUTE format('CREATE TABLE module%sb_consolidation_matrix_staging (LIKE module20b_consolidation_matrix_staging INCLUDING ALL)', m);
  END LOOP;
END $$;

\copy module21b_edge_staging FROM 'work/module_b_consolidation/module21b/module21b_edge_register.tsv' WITH (FORMAT csv, HEADER true, DELIMITER E'\t');
\copy module21b_evidence_staging FROM 'work/module_b_consolidation/module21b/module21b_evidence_register.tsv' WITH (FORMAT csv, HEADER true, DELIMITER E'\t');
\copy module21b_boundary_staging FROM 'work/module_b_consolidation/module21b/module21b_boundary_register.tsv' WITH (FORMAT csv, HEADER true, DELIMITER E'\t');
\copy module21b_consolidation_matrix_staging FROM 'work/module_b_consolidation/module21b/module21b_consolidation_matrix.tsv' WITH (FORMAT csv, HEADER true, DELIMITER E'\t');
\copy module22b_edge_staging FROM 'work/module_b_consolidation/module22b/module22b_edge_register.tsv' WITH (FORMAT csv, HEADER true, DELIMITER E'\t');
\copy module22b_evidence_staging FROM 'work/module_b_consolidation/module22b/module22b_evidence_register.tsv' WITH (FORMAT csv, HEADER true, DELIMITER E'\t');
\copy module22b_boundary_staging FROM 'work/module_b_consolidation/module22b/module22b_boundary_register.tsv' WITH (FORMAT csv, HEADER true, DELIMITER E'\t');
\copy module22b_consolidation_matrix_staging FROM 'work/module_b_consolidation/module22b/module22b_consolidation_matrix.tsv' WITH (FORMAT csv, HEADER true, DELIMITER E'\t');
\copy module23b_edge_staging FROM 'work/module_b_consolidation/module23b/module23b_edge_register.tsv' WITH (FORMAT csv, HEADER true, DELIMITER E'\t');
\copy module23b_evidence_staging FROM 'work/module_b_consolidation/module23b/module23b_evidence_register.tsv' WITH (FORMAT csv, HEADER true, DELIMITER E'\t');
\copy module23b_boundary_staging FROM 'work/module_b_consolidation/module23b/module23b_boundary_register.tsv' WITH (FORMAT csv, HEADER true, DELIMITER E'\t');
\copy module23b_consolidation_matrix_staging FROM 'work/module_b_consolidation/module23b/module23b_consolidation_matrix.tsv' WITH (FORMAT csv, HEADER true, DELIMITER E'\t');
\copy module24b_edge_staging FROM 'work/module_b_consolidation/module24b/module24b_edge_register.tsv' WITH (FORMAT csv, HEADER true, DELIMITER E'\t');
\copy module24b_evidence_staging FROM 'work/module_b_consolidation/module24b/module24b_evidence_register.tsv' WITH (FORMAT csv, HEADER true, DELIMITER E'\t');
\copy module24b_boundary_staging FROM 'work/module_b_consolidation/module24b/module24b_boundary_register.tsv' WITH (FORMAT csv, HEADER true, DELIMITER E'\t');
\copy module24b_consolidation_matrix_staging FROM 'work/module_b_consolidation/module24b/module24b_consolidation_matrix.tsv' WITH (FORMAT csv, HEADER true, DELIMITER E'\t');

DO $$
DECLARE m TEXT; n INTEGER;
BEGIN
  FOREACH m IN ARRAY ARRAY['20','21','22','23','24'] LOOP
    EXECUTE format('SELECT count(*) FROM module%sb_edge_staging WHERE exportable AND NOT EXISTS (SELECT 1 FROM module%sb_evidence_staging e WHERE e.exportable AND position('';'' || module%sb_edge_staging.b_edge_id || '';'' in '';'' || e.b_edge_ids || '';'' ) > 0)', m, m, m) INTO n;
    IF n <> 0 THEN RAISE EXCEPTION 'Module %B exportable edges without exportable evidence: %', m, n; END IF;
    EXECUTE format('SELECT count(*) FROM module%sb_edge_staging WHERE b_edge_id IN (SELECT b_edge_id FROM module%sb_edge_staging GROUP BY b_edge_id HAVING count(*) > 1)', m, m) INTO n;
    IF n <> 0 THEN RAISE EXCEPTION 'Module %B duplicate edge IDs: %', m, n; END IF;
  END LOOP;
END $$;

COMMIT;
