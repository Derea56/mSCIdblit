-- Canonical method-resource layer for LIANA, CellChat, NicheNet, and related
-- communication resources.
--
-- This layer is intentionally separate from SignalingEdge and
-- EvidenceSourceRecord. Presence in a method resource is provenance for a
-- tool input, not biological validation or mechanism-edge support.

BEGIN;

CREATE TABLE IF NOT EXISTS MethodResource (
  method_resource_id BIGSERIAL PRIMARY KEY,
  resource_key VARCHAR(160) NOT NULL UNIQUE,
  method_name VARCHAR(64) NOT NULL,
  resource_name VARCHAR(255) NOT NULL,
  resource_role VARCHAR(80) NOT NULL,
  species_scope VARCHAR(64),
  source_release VARCHAR(255),
  source_version VARCHAR(255),
  source_url TEXT,
  primary_citation TEXT,
  source_repository VARCHAR(255) NOT NULL,
  source_repository_commit CHAR(40),
  source_relative_path TEXT NOT NULL,
  source_artifact_sha256 CHAR(64) NOT NULL,
  original_format VARCHAR(32) NOT NULL,
  imported_on DATE NOT NULL,
  row_count BIGINT,
  column_count INTEGER,
  original_columns_json TEXT NOT NULL DEFAULT '[]',
  preprocessing_notes TEXT NOT NULL,
  usage_scope TEXT NOT NULL,
  retention_status VARCHAR(40) NOT NULL DEFAULT 'source_reference_only',
  source_file_tracked BOOLEAN NOT NULL DEFAULT FALSE,
  source_status VARCHAR(32) NOT NULL DEFAULT 'verified',
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT method_resource_format CHECK (
    original_format IN ('tsv', 'json', 'rda', 'rds', 'binary', 'manifest', 'other')
  ),
  CONSTRAINT method_resource_retention CHECK (
    retention_status IN ('copied_lossless', 'source_reference_only', 'migration_gap')
  ),
  CONSTRAINT method_resource_status CHECK (
    source_status IN ('verified', 'candidate', 'unresolved', 'retired')
  ),
  CONSTRAINT method_resource_sha256 CHECK (
    source_artifact_sha256 ~ '^[0-9a-fA-F]{64}$'
  ),
  CONSTRAINT method_resource_nonempty CHECK (
    btrim(resource_key) <> ''
    AND btrim(method_name) <> ''
    AND btrim(resource_name) <> ''
    AND btrim(resource_role) <> ''
    AND btrim(source_repository) <> ''
    AND btrim(source_relative_path) <> ''
    AND btrim(original_format) <> ''
    AND btrim(preprocessing_notes) <> ''
    AND btrim(usage_scope) <> ''
  )
);

CREATE INDEX IF NOT EXISTS idx_method_resource_method
  ON MethodResource(method_name, resource_name);
CREATE INDEX IF NOT EXISTS idx_method_resource_retention
  ON MethodResource(retention_status, source_status);

CREATE TABLE IF NOT EXISTS CanonicalCommunicationRecord (
  canonical_communication_id VARCHAR(64) PRIMARY KEY,
  species_scope VARCHAR(64) NOT NULL,
  ligand_name TEXT NOT NULL,
  receptor_name TEXT NOT NULL,
  normalized_ligand_name TEXT NOT NULL,
  normalized_receptor_name TEXT NOT NULL,
  communication_kind VARCHAR(40) NOT NULL DEFAULT 'direct_lr_candidate',
  evidence_status VARCHAR(40) NOT NULL DEFAULT 'method_resource_only',
  source_method_count INTEGER NOT NULL DEFAULT 0,
  source_record_count INTEGER NOT NULL DEFAULT 0,
  source_methods_json TEXT NOT NULL DEFAULT '[]',
  normalization_notes TEXT NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT canonical_communication_kind CHECK (
    communication_kind IN ('direct_lr_candidate', 'complex_lr_candidate')
  ),
  CONSTRAINT canonical_communication_evidence CHECK (
    evidence_status IN ('method_resource_only', 'curated_evidence_linked', 'excluded')
  ),
  CONSTRAINT canonical_communication_nonempty CHECK (
    btrim(canonical_communication_id) <> ''
    AND btrim(species_scope) <> ''
    AND btrim(ligand_name) <> ''
    AND btrim(receptor_name) <> ''
    AND btrim(normalized_ligand_name) <> ''
    AND btrim(normalized_receptor_name) <> ''
    AND btrim(normalization_notes) <> ''
  )
);

CREATE INDEX IF NOT EXISTS idx_canonical_communication_pair
  ON CanonicalCommunicationRecord(species_scope, normalized_ligand_name, normalized_receptor_name);

CREATE TABLE IF NOT EXISTS MethodResourceRecord (
  method_resource_record_id BIGSERIAL PRIMARY KEY,
  method_resource_id BIGINT NOT NULL,
  canonical_communication_id VARCHAR(64) NOT NULL,
  source_record_key TEXT NOT NULL,
  source_record_key_kind VARCHAR(40) NOT NULL,
  record_kind VARCHAR(48) NOT NULL,
  native_ligand TEXT,
  native_receptor TEXT,
  normalized_ligand TEXT,
  normalized_receptor TEXT,
  original_values_json TEXT NOT NULL DEFAULT '{}',
  normalized_values_json TEXT NOT NULL DEFAULT '{}',
  transform_notes TEXT NOT NULL,
  evidence_status VARCHAR(40) NOT NULL DEFAULT 'method_resource_only',
  method_score_json TEXT NOT NULL DEFAULT '{}',
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (method_resource_id) REFERENCES MethodResource(method_resource_id)
    ON DELETE CASCADE,
  FOREIGN KEY (canonical_communication_id) REFERENCES CanonicalCommunicationRecord(canonical_communication_id)
    ON DELETE CASCADE,
  CONSTRAINT method_resource_record_kind CHECK (
    record_kind IN ('direct_lr_candidate', 'complex_lr_candidate', 'method_registry_union')
  ),
  CONSTRAINT method_resource_record_status CHECK (
    evidence_status IN ('method_resource_only', 'curated_evidence_linked', 'excluded')
  ),
  CONSTRAINT method_resource_record_nonempty CHECK (
    btrim(source_record_key) <> ''
    AND btrim(source_record_key_kind) <> ''
    AND btrim(record_kind) <> ''
    AND btrim(transform_notes) <> ''
  ),
  UNIQUE (method_resource_id, source_record_key, record_kind)
);

CREATE INDEX IF NOT EXISTS idx_method_resource_record_communication
  ON MethodResourceRecord(canonical_communication_id);
CREATE INDEX IF NOT EXISTS idx_method_resource_record_source
  ON MethodResourceRecord(method_resource_id, source_record_key);

CREATE TABLE IF NOT EXISTS MethodResourceComplexComponent (
  method_resource_component_id BIGSERIAL PRIMARY KEY,
  method_resource_record_id BIGINT NOT NULL,
  canonical_communication_id VARCHAR(64) NOT NULL,
  side VARCHAR(16) NOT NULL,
  component_name TEXT NOT NULL,
  component_ordinal INTEGER NOT NULL,
  source_field_name VARCHAR(80) NOT NULL,
  original_component_value TEXT NOT NULL,
  notes TEXT NOT NULL,
  FOREIGN KEY (method_resource_record_id) REFERENCES MethodResourceRecord(method_resource_record_id)
    ON DELETE CASCADE,
  FOREIGN KEY (canonical_communication_id) REFERENCES CanonicalCommunicationRecord(canonical_communication_id)
    ON DELETE CASCADE,
  CONSTRAINT method_resource_component_side CHECK (side IN ('ligand', 'receptor')),
  CONSTRAINT method_resource_component_ordinal CHECK (component_ordinal > 0),
  CONSTRAINT method_resource_component_nonempty CHECK (
    btrim(component_name) <> ''
    AND btrim(source_field_name) <> ''
    AND btrim(original_component_value) <> ''
    AND btrim(notes) <> ''
  ),
  UNIQUE (method_resource_record_id, side, component_ordinal)
);

CREATE TABLE IF NOT EXISTS MethodResourceAnnotation (
  method_resource_annotation_id BIGSERIAL PRIMARY KEY,
  method_resource_record_id BIGINT NOT NULL,
  annotation_kind VARCHAR(48) NOT NULL,
  source_field_name VARCHAR(80) NOT NULL,
  annotation_value TEXT NOT NULL,
  annotation_scope VARCHAR(40) NOT NULL DEFAULT 'method_resource',
  notes TEXT NOT NULL,
  FOREIGN KEY (method_resource_record_id) REFERENCES MethodResourceRecord(method_resource_record_id)
    ON DELETE CASCADE,
  CONSTRAINT method_resource_annotation_kind CHECK (
    annotation_kind IN ('pathway', 'annotation', 'source_evidence_label', 'cofactor', 'other')
  ),
  CONSTRAINT method_resource_annotation_scope CHECK (
    annotation_scope IN ('method_resource', 'curated_evidence')
  ),
  CONSTRAINT method_resource_annotation_nonempty CHECK (
    btrim(source_field_name) <> ''
    AND btrim(annotation_value) <> ''
    AND btrim(notes) <> ''
  ),
  UNIQUE (method_resource_record_id, annotation_kind, source_field_name, annotation_value)
);

CREATE INDEX IF NOT EXISTS idx_method_resource_annotation_value
  ON MethodResourceAnnotation(annotation_kind, annotation_value);

CREATE TABLE IF NOT EXISTS MethodResourceProjection (
  method_resource_projection_id BIGSERIAL PRIMARY KEY,
  projection_key VARCHAR(160) NOT NULL UNIQUE,
  method_resource_id BIGINT,
  method_name VARCHAR(64) NOT NULL,
  projection_role VARCHAR(64) NOT NULL,
  relative_path TEXT NOT NULL,
  projection_format VARCHAR(32) NOT NULL,
  projection_sha256 CHAR(64) NOT NULL,
  row_count BIGINT,
  column_count INTEGER,
  columns_json TEXT NOT NULL DEFAULT '[]',
  losslessness_status VARCHAR(32) NOT NULL,
  transformation_notes TEXT NOT NULL,
  FOREIGN KEY (method_resource_id) REFERENCES MethodResource(method_resource_id)
    ON DELETE SET NULL,
  CONSTRAINT method_resource_projection_format CHECK (
    projection_format IN ('tsv', 'json', 'rda', 'rds', 'binary', 'manifest', 'other')
  ),
  CONSTRAINT method_resource_projection_losslessness CHECK (
    losslessness_status IN ('lossless', 'deterministic_transform', 'reference_only', 'migration_gap')
  ),
  CONSTRAINT method_resource_projection_sha256 CHECK (
    projection_sha256 ~ '^[0-9a-fA-F]{64}$'
  ),
  CONSTRAINT method_resource_projection_nonempty CHECK (
    btrim(projection_key) <> ''
    AND btrim(method_name) <> ''
    AND btrim(projection_role) <> ''
    AND btrim(relative_path) <> ''
    AND btrim(projection_format) <> ''
    AND btrim(transformation_notes) <> ''
  )
);

CREATE INDEX IF NOT EXISTS idx_method_resource_projection_method
  ON MethodResourceProjection(method_name, projection_role);

CREATE TABLE IF NOT EXISTS MethodResourceNumericArtifact (
  method_resource_numeric_artifact_id BIGSERIAL PRIMARY KEY,
  method_resource_id BIGINT NOT NULL,
  artifact_key VARCHAR(160) NOT NULL,
  artifact_kind VARCHAR(64) NOT NULL,
  storage_path TEXT NOT NULL,
  storage_status VARCHAR(32) NOT NULL,
  artifact_sha256 CHAR(64) NOT NULL,
  byte_size BIGINT,
  dtype VARCHAR(32),
  endianness VARCHAR(16),
  layout VARCHAR(32),
  shape_json TEXT,
  axis_artifacts_json TEXT NOT NULL DEFAULT '[]',
  source_model_version TEXT,
  notes TEXT NOT NULL,
  FOREIGN KEY (method_resource_id) REFERENCES MethodResource(method_resource_id)
    ON DELETE CASCADE,
  CONSTRAINT method_resource_numeric_storage CHECK (
    storage_status IN ('copied_lossless', 'source_reference_only', 'migration_gap')
  ),
  CONSTRAINT method_resource_numeric_sha256 CHECK (
    artifact_sha256 ~ '^[0-9a-fA-F]{64}$'
  ),
  CONSTRAINT method_resource_numeric_nonempty CHECK (
    btrim(artifact_key) <> ''
    AND btrim(artifact_kind) <> ''
    AND btrim(storage_path) <> ''
    AND btrim(notes) <> ''
  ),
  UNIQUE (method_resource_id, artifact_key)
);

COMMENT ON TABLE MethodResource IS
  'Immutable method-resource provenance and source snapshot metadata. Resource membership is not biological validation.';
COMMENT ON TABLE CanonicalCommunicationRecord IS
  'Deduplicated communication pair identity derived from exact method records; no synonym or biological validation inference is performed.';
COMMENT ON TABLE MethodResourceRecord IS
  'One exact source-resource record linked to a canonical communication pair. Native values remain losslessly available in JSON.';
COMMENT ON TABLE MethodResourceComplexComponent IS
  'Explicit complex component structure from a method resource; components are not inferred from punctuation in names.';
COMMENT ON TABLE MethodResourceAnnotation IS
  'Method-native pathway, cofactor, annotation, and source labels kept separate from curated evidence.';
COMMENT ON TABLE MethodResourceProjection IS
  'Versioned native-input or compatibility projection emitted for a downstream tool.';
COMMENT ON TABLE MethodResourceNumericArtifact IS
  'Storage metadata for numeric priors such as the dense NicheNet ligand-target matrix; axis and source hashes are retained for exact lookup.';

COMMIT;
