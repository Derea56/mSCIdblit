-- Structured measurement projection for external evidence observations.
--
-- Apply after schema/module_evidence_crosswalk.sql. This table preserves
-- reported/transcribed values and modality-specific fields without making the
-- measurement itself a mechanism edge or a module assignment.

BEGIN;

CREATE TABLE IF NOT EXISTS EvidenceObservationDetail (
  detail_id BIGSERIAL PRIMARY KEY,
  source_record_id BIGINT NOT NULL,
  source_detail_key TEXT NOT NULL,
  local_paper_id INTEGER,
  local_experiment_id INTEGER,
  local_observation_id INTEGER,
  local_claim_id INTEGER,
  reported_entity_name TEXT,
  reported_entity_type VARCHAR(64),
  measurement_kind TEXT NOT NULL,
  assay TEXT,
  protein_form TEXT,
  feature_type VARCHAR(64),
  feature_id TEXT,
  reported_value_numeric DOUBLE PRECISION,
  reported_value_text TEXT,
  reported_value_kind VARCHAR(64) NOT NULL DEFAULT 'unknown',
  native_value_numeric DOUBLE PRECISION,
  transcribed_value_numeric DOUBLE PRECISION,
  transcribed_value_text TEXT,
  transcribed_value_sem DOUBLE PRECISION,
  transcribed_value_sd DOUBLE PRECISION,
  transcribed_value_lower DOUBLE PRECISION,
  transcribed_value_upper DOUBLE PRECISION,
  unit TEXT,
  direction_vs_control TEXT NOT NULL DEFAULT 'not_reported',
  comparator TEXT,
  sample_count INTEGER,
  biological_replicates INTEGER,
  technical_replicates INTEGER,
  timepoint_value DOUBLE PRECISION,
  timepoint_unit TEXT,
  condition TEXT,
  tissue_context TEXT,
  cell_context TEXT,
  sample_scope TEXT,
  normalization TEXT,
  negative_evidence_status TEXT,
  source_evidence_label TEXT,
  evidence_grade VARCHAR(1),
  context_level VARCHAR(2),
  measurement_status VARCHAR(32) NOT NULL DEFAULT 'unknown',
  source_field_locator TEXT,
  raw_observation_text TEXT,
  normalization_notes TEXT,
  native_fields_json TEXT NOT NULL DEFAULT '{}',
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (source_record_id) REFERENCES EvidenceSourceRecord(source_record_id)
    ON DELETE CASCADE,
  FOREIGN KEY (local_paper_id) REFERENCES Paper(paper_id)
    ON DELETE SET NULL,
  FOREIGN KEY (local_experiment_id) REFERENCES Experiment(experiment_id)
    ON DELETE SET NULL,
  FOREIGN KEY (local_observation_id) REFERENCES Observation(observation_id)
    ON DELETE SET NULL,
  FOREIGN KEY (local_claim_id) REFERENCES AuthorClaim(claim_id)
    ON DELETE SET NULL,
  CONSTRAINT evidence_observation_detail_key_nonempty CHECK (btrim(source_detail_key) <> ''),
  CONSTRAINT evidence_observation_detail_measurement_nonempty CHECK (btrim(measurement_kind) <> ''),
  CONSTRAINT evidence_observation_detail_grade CHECK (
    evidence_grade IS NULL OR evidence_grade IN ('A', 'B', 'C', 'D', 'E', 'U')
  ),
  CONSTRAINT evidence_observation_detail_context CHECK (
    context_level IS NULL OR context_level IN ('L0', 'L1', 'L2', 'L3', 'L4')
  ),
  CONSTRAINT evidence_observation_detail_status CHECK (
    measurement_status IN (
      'reported', 'transcribed', 'digitized', 'qualitative',
      'unreported', 'derived_pilot', 'unknown'
    )
  ),
  UNIQUE (source_record_id, source_detail_key)
);

CREATE INDEX IF NOT EXISTS idx_evidence_observation_detail_source
  ON EvidenceObservationDetail(source_record_id);
CREATE INDEX IF NOT EXISTS idx_evidence_observation_detail_entity
  ON EvidenceObservationDetail(reported_entity_name);
CREATE INDEX IF NOT EXISTS idx_evidence_observation_detail_measurement
  ON EvidenceObservationDetail(measurement_kind, measurement_status);
CREATE INDEX IF NOT EXISTS idx_evidence_observation_detail_context
  ON EvidenceObservationDetail(evidence_grade, context_level);
CREATE INDEX IF NOT EXISTS idx_evidence_observation_detail_local_observation
  ON EvidenceObservationDetail(local_observation_id);

COMMENT ON TABLE EvidenceObservationDetail IS
  'Structured projection of an external evidence measurement. mSCS remains authoritative for the native record; this table preserves queryable reported values and provenance without creating graph edges.';
COMMENT ON COLUMN EvidenceObservationDetail.source_detail_key IS
  'Exact source observation key when available, otherwise a documented source-field locator key for a derived artifact row.';
COMMENT ON COLUMN EvidenceObservationDetail.reported_value_numeric IS
  'Primary query value: native source value when present, otherwise explicitly transcribed/digitized value. The separate native/transcribed fields preserve origin.';
COMMENT ON COLUMN EvidenceObservationDetail.native_fields_json IS
  'Lossless imported source-row snapshot and joined context fields; not a substitute for the authoritative mSCS record.';
COMMENT ON COLUMN EvidenceObservationDetail.evidence_grade IS
  'mSCIdblit ABC/Evidence grade only when a documented vocabulary mapping exists; otherwise NULL with source_evidence_label preserved.';
COMMENT ON COLUMN EvidenceObservationDetail.context_level IS
  'mSCIdblit L0-L4 context level only after explicit adjudication; source context remains in the native fields and context columns.';

COMMIT;
