-- Add a lossless provenance layer for the retained Module 20B-24B evidence
-- artifacts. This is intentionally separate from canonical biological claims.
-- It records files, checksums, explicit filename identifiers, and conservative
-- register crosswalk candidates without changing graph or evidence semantics.

BEGIN;

CREATE TABLE IF NOT EXISTS EvidenceArtifact (
  artifact_id BIGSERIAL PRIMARY KEY,
  repository_root TEXT NOT NULL,
  relative_path TEXT NOT NULL,
  sha256 CHAR(64) NOT NULL,
  byte_size BIGINT NOT NULL CHECK (byte_size >= 0),
  file_extension VARCHAR(32),
  artifact_role VARCHAR(64) NOT NULL,
  scan_version VARCHAR(32) NOT NULL,
  scanned_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  UNIQUE (repository_root, relative_path)
);

CREATE INDEX IF NOT EXISTS idx_evidence_artifact_sha256
  ON EvidenceArtifact(sha256);
CREATE INDEX IF NOT EXISTS idx_evidence_artifact_role
  ON EvidenceArtifact(artifact_role);

CREATE TABLE IF NOT EXISTS EvidenceArtifactIdentifier (
  artifact_identifier_id BIGSERIAL PRIMARY KEY,
  artifact_id BIGINT NOT NULL,
  identifier_type VARCHAR(32) NOT NULL,
  identifier_value TEXT NOT NULL,
  match_scope VARCHAR(16) NOT NULL,
  FOREIGN KEY (artifact_id) REFERENCES EvidenceArtifact(artifact_id)
    ON DELETE CASCADE,
  CONSTRAINT evidence_artifact_identifier_scope
    CHECK (match_scope IN ('filename')),
  UNIQUE (artifact_id, identifier_type, identifier_value, match_scope)
);

CREATE INDEX IF NOT EXISTS idx_evidence_artifact_identifier_value
  ON EvidenceArtifactIdentifier(identifier_type, identifier_value);

CREATE TABLE IF NOT EXISTS EvidenceArtifactRegisterCrosswalk (
  crosswalk_id BIGSERIAL PRIMARY KEY,
  artifact_id BIGINT NOT NULL,
  register_source_id BIGINT NOT NULL,
  module VARCHAR(32) NOT NULL,
  register_edge_id VARCHAR(255) NOT NULL,
  register_evidence_id VARCHAR(255) NOT NULL,
  matched_identifier_type VARCHAR(32) NOT NULL,
  matched_identifier_value TEXT NOT NULL,
  match_method VARCHAR(64) NOT NULL,
  crosswalk_status VARCHAR(32) NOT NULL,
  notes TEXT,
  FOREIGN KEY (artifact_id) REFERENCES EvidenceArtifact(artifact_id)
    ON DELETE CASCADE,
  FOREIGN KEY (register_source_id)
    REFERENCES SignalingEdgeRegisterSource(register_source_id)
    ON DELETE CASCADE,
  CONSTRAINT evidence_artifact_crosswalk_status
    CHECK (crosswalk_status IN ('filename_token_candidate')),
  UNIQUE (
    artifact_id,
    register_source_id,
    matched_identifier_type,
    matched_identifier_value,
    match_method
  )
);

CREATE INDEX IF NOT EXISTS idx_evidence_artifact_crosswalk_register
  ON EvidenceArtifactRegisterCrosswalk(register_source_id);
CREATE INDEX IF NOT EXISTS idx_evidence_artifact_crosswalk_evidence
  ON EvidenceArtifactRegisterCrosswalk(module, register_evidence_id);

COMMENT ON TABLE EvidenceArtifact IS
  'Checksummed retained source artifacts; presence here is provenance, not biological evidence.';
COMMENT ON TABLE EvidenceArtifactIdentifier IS
  'Explicit identifiers found in artifact filenames only; content citations are intentionally not promoted to source assignments.';
COMMENT ON TABLE EvidenceArtifactRegisterCrosswalk IS
  'Conservative filename-token candidates linking retained artifacts to register sources; not canonical evidence assignment.';

COMMIT;
