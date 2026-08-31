-- Add an artifact-to-adjudication bridge for Module 20B-24B evidence.
-- This table records how each retained source artifact was used or evaluated;
-- it does not itself promote a mechanism edge.

BEGIN;

CREATE TABLE IF NOT EXISTS EvidenceArtifactAdjudication (
  adjudication_id BIGSERIAL PRIMARY KEY,
  artifact_id BIGINT NOT NULL,
  module VARCHAR(16) NOT NULL,
  register_edge_id VARCHAR(255) NOT NULL DEFAULT '',
  register_evidence_id VARCHAR(255) NOT NULL DEFAULT '',
  extraction_id VARCHAR(255) NOT NULL DEFAULT '',
  canonical_paper_key TEXT NOT NULL DEFAULT '',
  resolved_pmid VARCHAR(50),
  artifact_role VARCHAR(64) NOT NULL,
  paper_match_status TEXT NOT NULL,
  artifact_support_status VARCHAR(64) NOT NULL,
  evidence_grade VARCHAR(1),
  context_level VARCHAR(2),
  observation_status VARCHAR(128),
  claim_status VARCHAR(128),
  source_locator TEXT,
  candidate_observation_snippet TEXT,
  candidate_claim_snippet TEXT,
  adjudication_basis TEXT NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (artifact_id) REFERENCES EvidenceArtifact(artifact_id)
    ON DELETE CASCADE,
  CONSTRAINT evidence_artifact_adjudication_grade
    CHECK (evidence_grade IS NULL OR evidence_grade IN ('A', 'B', 'C', 'D', 'E', 'U')),
  CONSTRAINT evidence_artifact_adjudication_context
    CHECK (context_level IS NULL OR context_level IN ('L0', 'L1', 'L2', 'L3', 'L4')),
  UNIQUE (artifact_id, module, register_evidence_id, extraction_id)
);

-- Keep reruns safe if the table was created by an earlier version of this
-- migration with a bounded paper-match column.
ALTER TABLE EvidenceArtifactAdjudication
  ALTER COLUMN paper_match_status TYPE TEXT;

CREATE INDEX IF NOT EXISTS idx_evidence_artifact_adjudication_artifact
  ON EvidenceArtifactAdjudication(artifact_id);
CREATE INDEX IF NOT EXISTS idx_evidence_artifact_adjudication_evidence
  ON EvidenceArtifactAdjudication(module, register_evidence_id);
CREATE INDEX IF NOT EXISTS idx_evidence_artifact_adjudication_status
  ON EvidenceArtifactAdjudication(artifact_support_status);

COMMENT ON TABLE EvidenceArtifactAdjudication IS
  'Per-artifact extraction/adjudication bridge. Statuses preserve provenance and review state; they do not independently promote mechanism edges.';
COMMENT ON COLUMN EvidenceArtifactAdjudication.artifact_support_status IS
  'How the retained artifact relates to the reviewed evidence ledger: supporting_validated_claim, negative_or_boundary_evaluated, candidate_requires_review, linked_unresolved, metadata_or_search_only, or unmapped_source_artifact.';

COMMIT;
