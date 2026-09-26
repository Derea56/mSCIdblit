-- Context-specific evidence overlay for the neutral mechanism graph.
--
-- Apply after schema/module_evidence_crosswalk.sql and
-- schema/evidence_observation_detail.sql. These tables add structured context
-- and external mechanism links without creating or modifying SignalingEdge
-- rows. mSCS remains responsible for route evaluation and calibration.

BEGIN;

CREATE TABLE IF NOT EXISTS EvidenceContextProfile (
  context_id TEXT PRIMARY KEY,
  context_name TEXT NOT NULL,
  context_kind VARCHAR(32) NOT NULL,
  disease_context TEXT,
  anatomical_context TEXT,
  species TEXT,
  injury_model TEXT,
  injury_level TEXT,
  timepoint_value DOUBLE PRECISION,
  timepoint_unit TEXT,
  perturbation TEXT,
  treatment TEXT,
  cell_type TEXT,
  sample_id TEXT,
  context_status VARCHAR(32) NOT NULL DEFAULT 'defined',
  provenance_note TEXT NOT NULL,
  metadata_json TEXT NOT NULL DEFAULT '{}',
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT evidence_context_profile_id_nonempty CHECK (btrim(context_id) <> ''),
  CONSTRAINT evidence_context_profile_name_nonempty CHECK (btrim(context_name) <> ''),
  CONSTRAINT evidence_context_profile_kind CHECK (
    context_kind IN ('ontology_scope', 'study_context', 'sample_context')
  ),
  CONSTRAINT evidence_context_profile_status CHECK (
    context_status IN ('defined', 'candidate', 'verified', 'retired')
  ),
  CONSTRAINT evidence_context_profile_provenance_nonempty CHECK (
    btrim(provenance_note) <> ''
  )
);

CREATE TABLE IF NOT EXISTS ContextEvidenceObservation (
  context_observation_id TEXT PRIMARY KEY,
  context_id TEXT NOT NULL REFERENCES EvidenceContextProfile(context_id)
    ON DELETE CASCADE,
  source_record_id BIGINT REFERENCES EvidenceSourceRecord(source_record_id)
    ON DELETE SET NULL,
  modality VARCHAR(64) NOT NULL,
  assay TEXT,
  measurement_kind TEXT NOT NULL,
  measured_entity_name TEXT,
  measured_entity_type VARCHAR(64),
  feature_id TEXT,
  value_numeric DOUBLE PRECISION,
  value_text TEXT,
  value_kind VARCHAR(32) NOT NULL DEFAULT 'unknown',
  unit TEXT,
  direction_vs_control TEXT NOT NULL DEFAULT 'not_reported',
  comparator TEXT,
  biological_replicates INTEGER,
  timepoint_value DOUBLE PRECISION,
  timepoint_unit TEXT,
  perturbation TEXT,
  cell_type TEXT,
  sample_id TEXT,
  observation_status VARCHAR(32) NOT NULL DEFAULT 'unknown',
  evidence_role VARCHAR(40) NOT NULL DEFAULT 'dataset_observation',
  dependency_group TEXT NOT NULL,
  source_artifact_path TEXT,
  source_artifact_sha256 CHAR(64),
  source_locator TEXT,
  provenance_note TEXT NOT NULL,
  native_fields_json TEXT NOT NULL DEFAULT '{}',
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT context_observation_id_nonempty CHECK (btrim(context_observation_id) <> ''),
  CONSTRAINT context_observation_modality CHECK (
    modality IN (
      'protein', 'proteomics', 'transcriptomics', 'spatial',
      'spatial_transcriptomics', 'epigenomics', 'chromatin_accessibility',
      'imaging', 'perturbation', 'functional', 'histology', 'other'
    )
  ),
  CONSTRAINT context_observation_measurement_nonempty CHECK (btrim(measurement_kind) <> ''),
  CONSTRAINT context_observation_value_kind CHECK (
    value_kind IN ('numeric', 'qualitative', 'categorical', 'unreported', 'unknown')
  ),
  CONSTRAINT context_observation_status CHECK (
    observation_status IN (
      'observed', 'reported', 'transcribed', 'digitized', 'derived',
      'inferred', 'negative', 'not_measured', 'unknown'
    )
  ),
  CONSTRAINT context_observation_role CHECK (
    evidence_role IN (
      'dataset_observation', 'context_matched_external_observation',
      'inferred_bridge', 'contextual_annotation'
    )
  ),
  CONSTRAINT context_observation_dependency_nonempty CHECK (btrim(dependency_group) <> ''),
  CONSTRAINT context_observation_provenance_nonempty CHECK (btrim(provenance_note) <> ''),
  CONSTRAINT context_observation_sha256 CHECK (
    source_artifact_sha256 IS NULL
    OR source_artifact_sha256 ~ '^[0-9a-fA-F]{64}$'
  )
);

CREATE TABLE IF NOT EXISTS ContextMechanismLink (
  context_mechanism_link_id TEXT PRIMARY KEY,
  context_observation_id TEXT NOT NULL
    REFERENCES ContextEvidenceObservation(context_observation_id)
    ON DELETE CASCADE,
  mechanism_release_id TEXT NOT NULL,
  mechanism_target_kind VARCHAR(32) NOT NULL,
  mechanism_target_key TEXT NOT NULL,
  mechanism_route_id TEXT,
  route_stage VARCHAR(32) NOT NULL,
  link_role VARCHAR(40) NOT NULL,
  context_match VARCHAR(32) NOT NULL DEFAULT 'unknown',
  support_status VARCHAR(32) NOT NULL DEFAULT 'unresolved',
  release_status VARCHAR(32) NOT NULL DEFAULT 'staging',
  link_basis TEXT NOT NULL,
  source_field_locator TEXT,
  notes TEXT,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT context_mechanism_link_id_nonempty CHECK (btrim(context_mechanism_link_id) <> ''),
  CONSTRAINT context_mechanism_release_nonempty CHECK (btrim(mechanism_release_id) <> ''),
  CONSTRAINT context_mechanism_target_kind CHECK (
    mechanism_target_kind IN ('route', 'node', 'edge', 'pathway', 'module')
  ),
  CONSTRAINT context_mechanism_target_key_nonempty CHECK (btrim(mechanism_target_key) <> ''),
  CONSTRAINT context_mechanism_route_stage CHECK (
    route_stage IN ('ligand', 'receptor', 'intracellular', 'tf', 'output', 'route', 'context')
  ),
  CONSTRAINT context_mechanism_link_role CHECK (
    link_role IN (
      'input_support', 'receptor_support', 'intracellular_support',
      'tf_support', 'output_support', 'spatial_context',
      'regulatory_context', 'contradictory_or_negative', 'unresolved'
    )
  ),
  CONSTRAINT context_mechanism_context_match CHECK (
    context_match IN ('exact', 'related', 'generic', 'unknown')
  ),
  CONSTRAINT context_mechanism_support_status CHECK (
    support_status IN ('supporting', 'contextual', 'contradictory', 'unresolved', 'excluded')
  ),
  CONSTRAINT context_mechanism_release_status CHECK (
    release_status IN ('staging', 'included', 'held', 'screened_out', 'retired')
  ),
  CONSTRAINT context_mechanism_basis_nonempty CHECK (btrim(link_basis) <> '')
);

CREATE INDEX IF NOT EXISTS idx_evidence_context_profile_scope
  ON EvidenceContextProfile(disease_context, anatomical_context, context_status);
CREATE INDEX IF NOT EXISTS idx_context_observation_context_modality
  ON ContextEvidenceObservation(context_id, modality, observation_status);
CREATE INDEX IF NOT EXISTS idx_context_observation_source
  ON ContextEvidenceObservation(source_record_id);
CREATE INDEX IF NOT EXISTS idx_context_observation_dependency
  ON ContextEvidenceObservation(dependency_group);
CREATE INDEX IF NOT EXISTS idx_context_mechanism_target
  ON ContextMechanismLink(mechanism_release_id, mechanism_target_kind, mechanism_target_key);
CREATE INDEX IF NOT EXISTS idx_context_mechanism_route_stage
  ON ContextMechanismLink(mechanism_route_id, route_stage, release_status);

COMMENT ON TABLE EvidenceContextProfile IS
  'Structured disease, injury, tissue, study, or sample context for an evidence overlay; it does not alter generic mechanism edges.';
COMMENT ON TABLE ContextEvidenceObservation IS
  'Context-specific observation with source provenance and dependency grouping; not a route score and not a graph edge.';
COMMENT ON TABLE ContextMechanismLink IS
  'Reviewed link from a context observation to a stable identifier in a pinned mechanism release; it does not promote graph traversal.';
COMMENT ON COLUMN ContextEvidenceObservation.evidence_role IS
  'Separates measured dataset evidence from context-matched external observations and inferred bridges.';
COMMENT ON COLUMN ContextEvidenceObservation.dependency_group IS
  'Source/experiment dependency key used by downstream evaluation to avoid double counting correlated claims.';
COMMENT ON COLUMN ContextMechanismLink.context_match IS
  'Match between the observation context and the mechanism claim; it is not a confidence score.';

COMMIT;
