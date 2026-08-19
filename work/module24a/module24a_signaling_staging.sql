-- Module 24A audit-layer SQL staging materialization
-- Run from the repository root with psql and ON_ERROR_STOP enabled.
-- This script writes only module24a_* staging tables. It does not write the
-- frozen Module 20A LR tables, core SignalingEdge rows, or prior-module data.
-- It preserves pathway/complex/function edges as distinct audit-layer rows and
-- retains explicit no-evidence boundaries rather than dropping them.

\set ON_ERROR_STOP on
BEGIN;

DROP TABLE IF EXISTS module24a_edge_evidence_layer_staging;
DROP TABLE IF EXISTS module24a_saturation_matrix_staging;
DROP TABLE IF EXISTS module24a_perturbation_staging;
DROP TABLE IF EXISTS module24a_evidence_staging;
DROP TABLE IF EXISTS module24a_edge_staging;
DROP TABLE IF EXISTS module24a_batch_plan_staging;
DROP TABLE IF EXISTS module24a_queue_staging;

CREATE TABLE module24a_queue_staging (
  queue_id TEXT PRIMARY KEY,
  batch_id TEXT NOT NULL,
  priority TEXT NOT NULL,
  candidate_class TEXT NOT NULL,
  upstream_signal_or_release_feature TEXT NOT NULL,
  target_or_receptor_system TEXT NOT NULL,
  protease_activation_or_processing_logic TEXT NOT NULL,
  proximal_relay_to_validate TEXT NOT NULL,
  downstream_tf_or_program_target TEXT NOT NULL,
  evidence_layers_to_extract TEXT NOT NULL,
  species_context TEXT NOT NULL,
  cell_type_or_model_context TEXT NOT NULL,
  source_origin TEXT NOT NULL,
  source_record_id TEXT NOT NULL,
  stable_source_locator TEXT NOT NULL,
  search_boundary TEXT NOT NULL,
  status TEXT NOT NULL,
  notes TEXT NOT NULL
);

\copy module24a_queue_staging FROM 'work/module24a/module24a_extraction_queue.tsv' WITH (FORMAT csv, HEADER true, DELIMITER E'\t');

CREATE TABLE module24a_batch_plan_staging (
  batch_id TEXT PRIMARY KEY,
  queue_start TEXT NOT NULL,
  queue_end TEXT NOT NULL,
  candidate_count INTEGER NOT NULL,
  priority_counts TEXT NOT NULL,
  review_status TEXT NOT NULL,
  write_scope TEXT NOT NULL
);

\copy module24a_batch_plan_staging FROM 'work/module24a/module24a_batch_plan.tsv' WITH (FORMAT csv, HEADER true, DELIMITER E'\t');

CREATE TABLE module24a_edge_staging (
  edge_id TEXT PRIMARY KEY,
  source_entity TEXT NOT NULL,
  relation_type TEXT NOT NULL,
  target_entity TEXT NOT NULL,
  pathway_name TEXT NOT NULL,
  effect_polarity TEXT,
  directionality TEXT,
  upstream_signal_context TEXT,
  receptor_or_target_context TEXT,
  cell_type_context TEXT,
  compartment_context TEXT,
  species_context TEXT,
  injury_context TEXT,
  evidence_layer TEXT NOT NULL,
  evidence_status TEXT NOT NULL,
  context_scope TEXT NOT NULL,
  confidence_tier TEXT NOT NULL,
  export_priority TEXT NOT NULL,
  curator_decision TEXT NOT NULL
);

\copy module24a_edge_staging FROM 'work/module24a/module24a_edge_register.tsv' WITH (FORMAT csv, HEADER true, DELIMITER E'\t');

CREATE TABLE module24a_evidence_staging (
  evidence_id TEXT PRIMARY KEY,
  edge_id TEXT,
  source_kind TEXT NOT NULL,
  source_locator TEXT NOT NULL,
  support_kind TEXT NOT NULL,
  species_support TEXT,
  source_species_detail TEXT,
  source_scope TEXT NOT NULL,
  assay_or_perturbation TEXT NOT NULL,
  relation_type TEXT NOT NULL,
  pathway_or_branch TEXT NOT NULL,
  confidence_tier TEXT NOT NULL,
  citation_note TEXT NOT NULL,
  evidence_summary TEXT,
  limitations TEXT
);

\copy module24a_evidence_staging FROM 'work/module24a/module24a_evidence_register.tsv' WITH (FORMAT csv, HEADER true, DELIMITER E'\t');

CREATE TABLE module24a_perturbation_staging (
  perturbation_id TEXT PRIMARY KEY,
  edge_id_or_branch TEXT NOT NULL,
  source_locator TEXT NOT NULL,
  species TEXT NOT NULL,
  cell_or_tissue_context TEXT NOT NULL,
  perturbation_type TEXT NOT NULL,
  perturbation_target TEXT NOT NULL,
  observed_effect TEXT NOT NULL,
  interpretation_boundary TEXT NOT NULL,
  confidence TEXT NOT NULL
);

\copy module24a_perturbation_staging FROM 'work/module24a/module24a_perturbation_register.tsv' WITH (FORMAT csv, HEADER true, DELIMITER E'\t');

CREATE TABLE module24a_saturation_matrix_staging (
  candidate_id TEXT PRIMARY KEY,
  candidate_class TEXT NOT NULL,
  upstream_signal_or_release_feature TEXT NOT NULL,
  target_or_receptor_system TEXT NOT NULL,
  protease_processing_logic TEXT NOT NULL,
  proximal_relay TEXT NOT NULL,
  downstream_tf_or_program TEXT NOT NULL,
  layer1_status TEXT NOT NULL,
  layer2_status TEXT NOT NULL,
  layer3_status TEXT NOT NULL,
  species_posture TEXT NOT NULL,
  sci_context_posture TEXT NOT NULL,
  status TEXT NOT NULL,
  next_gap TEXT NOT NULL
);

\copy module24a_saturation_matrix_staging FROM 'work/module24a/module24a_saturation_matrix.tsv' WITH (FORMAT csv, HEADER true, DELIMITER E'\t');

-- One row per edge/evidence association, including semicolon-delimited
-- evidence-register references. This is derived from the validated audit
-- registers and keeps the edge's explicit evidence-layer classification next
-- to the evidence record's support kind.
CREATE TABLE module24a_edge_evidence_layer_staging (
  edge_id TEXT NOT NULL,
  evidence_id TEXT NOT NULL,
  evidence_layer TEXT NOT NULL,
  support_kind TEXT NOT NULL,
  layer_boundary TEXT NOT NULL,
  PRIMARY KEY (edge_id, evidence_id)
);

INSERT INTO module24a_edge_evidence_layer_staging
  (edge_id, evidence_id, evidence_layer, support_kind, layer_boundary)
SELECT
  trim(ref.edge_id),
  e.evidence_id,
  ed.evidence_layer,
  e.support_kind,
  CASE
    WHEN ed.evidence_layer IN ('ligand_receptor_binding', 'ligand_receptor_activation',
                               'ligand_receptor_pharmacology', 'receptor_or_sensor_engagement')
      THEN 'binding_or_activation'
    WHEN ed.evidence_layer = 'receptor_proximal_relay'
      THEN 'receptor_proximal_relay'
    WHEN ed.evidence_layer = 'downstream_pathway_or_cellular_function'
      THEN 'downstream_pathway_or_cellular_function'
    ELSE 'unresolved_or_legacy_layer_label'
  END
FROM module24a_evidence_staging e
CROSS JOIN LATERAL unnest(string_to_array(e.edge_id, ';')) AS ref(edge_id)
JOIN module24a_edge_staging ed ON ed.edge_id = trim(ref.edge_id)
WHERE trim(e.edge_id) <> '';

-- Integrity assertions. Any failure aborts the transaction.
DO $$
DECLARE
  n INTEGER;
BEGIN
  SELECT COUNT(*) INTO n FROM module24a_queue_staging;
  IF n <> 171 THEN RAISE EXCEPTION 'Expected 171 queue rows, found %', n; END IF;

  SELECT COUNT(*) INTO n FROM module24a_batch_plan_staging;
  IF n <> 4 THEN RAISE EXCEPTION 'Expected 4 batch-plan rows, found %', n; END IF;

  SELECT COUNT(*) INTO n FROM module24a_edge_staging;
  IF n <> 151 THEN RAISE EXCEPTION 'Expected 151 edges, found %', n; END IF;

  SELECT COUNT(*) INTO n FROM module24a_evidence_staging;
  IF n <> 200 THEN RAISE EXCEPTION 'Expected 200 evidence records, found %', n; END IF;

  SELECT COUNT(*) INTO n FROM module24a_saturation_matrix_staging;
  IF n <> 189 THEN RAISE EXCEPTION 'Expected 189 saturation rows, found %', n; END IF;

  SELECT COUNT(*) INTO n FROM module24a_perturbation_staging;
  IF n <> 0 THEN RAISE EXCEPTION 'Expected empty perturbation register, found %', n; END IF;

  SELECT COUNT(*) INTO n
  FROM (
    SELECT source_entity, relation_type, target_entity, pathway_name,
           upstream_signal_context, cell_type_context, species_context
    FROM module24a_edge_staging
    GROUP BY source_entity, relation_type, target_entity, pathway_name,
             upstream_signal_context, cell_type_context, species_context
    HAVING COUNT(*) > 1
  ) duplicate_keys;
  IF n <> 0 THEN RAISE EXCEPTION 'Duplicate edge keys: %', n; END IF;

  SELECT COUNT(*) INTO n
  FROM module24a_edge_staging e
  WHERE NOT EXISTS (
    SELECT 1
    FROM module24a_edge_evidence_layer_staging l
    WHERE l.edge_id = e.edge_id
      AND l.support_kind <> 'no_evidence_boundary'
  );
  IF n <> 0 THEN RAISE EXCEPTION 'Edges without qualifying supporting evidence: %', n; END IF;

  SELECT COUNT(*) INTO n
  FROM module24a_edge_evidence_layer_staging l
  WHERE NOT EXISTS (SELECT 1 FROM module24a_edge_staging e WHERE e.edge_id = l.edge_id)
     OR NOT EXISTS (SELECT 1 FROM module24a_evidence_staging e WHERE e.evidence_id = l.evidence_id);
  IF n <> 0 THEN RAISE EXCEPTION 'Invalid edge/evidence-layer references: %', n; END IF;

  SELECT COUNT(*) INTO n
  FROM module24a_evidence_staging e
  WHERE e.support_kind = 'no_evidence_boundary'
    AND trim(e.edge_id) <> '';
  IF n <> 0 THEN RAISE EXCEPTION 'No-evidence boundaries must not point to edges: %', n; END IF;

  SELECT COUNT(*) INTO n
  FROM module24a_saturation_matrix_staging m
  WHERE m.candidate_id LIKE 'M24A-Q%'
    AND NOT EXISTS (SELECT 1 FROM module24a_queue_staging q WHERE q.queue_id = m.candidate_id);
  IF n <> 0 THEN RAISE EXCEPTION 'Matrix rows missing from queue: %', n; END IF;

  SELECT COUNT(*) INTO n
  FROM module24a_queue_staging q
  WHERE NOT EXISTS (SELECT 1 FROM module24a_saturation_matrix_staging m WHERE m.candidate_id = q.queue_id);
  IF n <> 0 THEN RAISE EXCEPTION 'Queue rows missing from saturation matrix: %', n; END IF;

  SELECT COUNT(*) INTO n
  FROM module24a_edge_evidence_layer_staging
  WHERE evidence_layer NOT IN ('ligand_receptor_binding', 'ligand_receptor_activation',
                               'ligand_receptor_pharmacology', 'receptor_or_sensor_engagement',
                               'receptor_proximal_relay', 'downstream_pathway_or_cellular_function',
                               'reviewed_batch003A', 'reviewed_batch003B');
  IF n <> 0 THEN RAISE EXCEPTION 'Unexpected evidence-layer labels: %', n; END IF;
END $$;

COMMENT ON TABLE module24a_queue_staging IS 'Module 24A candidate queue; source candidates are not evidence by themselves.';
COMMENT ON TABLE module24a_edge_staging IS 'Module 24A audit-layer edges; direct, pathway, complex, and functional edges remain distinct.';
COMMENT ON TABLE module24a_evidence_staging IS 'Module 24A stable evidence records and explicit no-evidence boundaries.';
COMMENT ON TABLE module24a_edge_evidence_layer_staging IS 'Derived edge/evidence layer map retaining binding, proximal relay, and downstream/function boundaries.';
COMMENT ON TABLE module24a_saturation_matrix_staging IS 'Module 24A saturation audit matrix, including legacy reuse anchors and unresolved gaps.';

COMMIT;
