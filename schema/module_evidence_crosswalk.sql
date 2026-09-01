-- Cross-cutting evidence bridge for module, pathway, entity, and edge review.
--
-- Apply after schema/schema.sql. This layer is intentionally additive: it
-- does not replace Observation, copy modality-native measurements, or create
-- SignalingEdge rows. An external source record points to the authoritative
-- mSCS record; ModuleEvidenceLink records only its reviewed relationship to
-- mSCIdblit's biological organization.

BEGIN;

CREATE TABLE IF NOT EXISTS EvidenceSourceRecord (
  source_record_id BIGSERIAL PRIMARY KEY,
  source_system VARCHAR(64) NOT NULL,
  source_database VARCHAR(128) NOT NULL,
  source_record_type VARCHAR(64) NOT NULL,
  source_record_key TEXT NOT NULL,
  source_version VARCHAR(128) NOT NULL DEFAULT '',
  modality VARCHAR(64) NOT NULL,
  assay VARCHAR(255),
  source_artifact_path TEXT,
  source_artifact_sha256 CHAR(64),
  source_locator TEXT,
  source_url TEXT,
  source_status VARCHAR(32) NOT NULL DEFAULT 'candidate',
  provenance_note TEXT NOT NULL,
  source_metadata_json TEXT NOT NULL DEFAULT '{}',
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT evidence_source_record_nonempty CHECK (
    btrim(source_system) <> ''
    AND btrim(source_database) <> ''
    AND btrim(source_record_type) <> ''
    AND btrim(source_record_key) <> ''
    AND btrim(modality) <> ''
    AND btrim(provenance_note) <> ''
  ),
  CONSTRAINT evidence_source_record_modality CHECK (
    modality IN (
      'protein', 'proteomics', 'spatial', 'spatial_transcriptomics',
      'epigenetic', 'epigenomics', 'chromatin_accessibility', 'other'
    )
  ),
  CONSTRAINT evidence_source_record_status CHECK (
    source_status IN ('verified', 'candidate', 'unresolved', 'retired')
  ),
  CONSTRAINT evidence_source_record_sha256 CHECK (
    source_artifact_sha256 IS NULL
    OR source_artifact_sha256 ~ '^[0-9a-fA-F]{64}$'
  ),
  UNIQUE (
    source_system,
    source_database,
    source_record_type,
    source_record_key,
    source_version
  )
);

CREATE INDEX IF NOT EXISTS idx_evidence_source_record_lookup
  ON EvidenceSourceRecord(source_system, source_database, source_record_type, source_record_key);
CREATE INDEX IF NOT EXISTS idx_evidence_source_record_modality
  ON EvidenceSourceRecord(modality, source_status);

CREATE TABLE IF NOT EXISTS ModuleEvidenceLink (
  module_evidence_link_id BIGSERIAL PRIMARY KEY,
  source_record_id BIGINT NOT NULL,
  module VARCHAR(32),
  link_role VARCHAR(64) NOT NULL,
  target_kind VARCHAR(32) NOT NULL,
  pathway_id INTEGER,
  entity_id INTEGER,
  edge_id INTEGER,
  local_paper_id INTEGER,
  local_experiment_id INTEGER,
  local_observation_id INTEGER,
  local_claim_id INTEGER,
  support_status VARCHAR(32) NOT NULL DEFAULT 'contextual',
  evidence_grade VARCHAR(1),
  context_level VARCHAR(2),
  inference_role VARCHAR(32) NOT NULL DEFAULT 'descriptive',
  release_status VARCHAR(32) NOT NULL DEFAULT 'staging',
  link_basis TEXT NOT NULL,
  source_field_locator TEXT,
  notes TEXT,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (source_record_id) REFERENCES EvidenceSourceRecord(source_record_id)
    ON DELETE CASCADE,
  FOREIGN KEY (pathway_id) REFERENCES SignalingPathway(pathway_id)
    ON DELETE CASCADE,
  FOREIGN KEY (entity_id) REFERENCES SignalingEntity(entity_id)
    ON DELETE CASCADE,
  FOREIGN KEY (pathway_id, entity_id)
    REFERENCES SignalingPathwayMember(pathway_id, entity_id)
    ON DELETE CASCADE,
  FOREIGN KEY (edge_id) REFERENCES SignalingEdge(edge_id)
    ON DELETE CASCADE,
  FOREIGN KEY (local_paper_id) REFERENCES Paper(paper_id)
    ON DELETE SET NULL,
  FOREIGN KEY (local_experiment_id) REFERENCES Experiment(experiment_id)
    ON DELETE SET NULL,
  FOREIGN KEY (local_observation_id) REFERENCES Observation(observation_id)
    ON DELETE SET NULL,
  FOREIGN KEY (local_claim_id) REFERENCES AuthorClaim(claim_id)
    ON DELETE SET NULL,
  CONSTRAINT module_evidence_link_role CHECK (
    link_role IN (
      'member_support', 'edge_support', 'pathway_state',
      'spatial_context', 'regulatory_context',
      'contradictory_or_negative', 'unresolved'
    )
  ),
  CONSTRAINT module_evidence_link_target_kind CHECK (
    target_kind IN ('module', 'pathway', 'pathway_member', 'entity', 'edge')
  ),
  CONSTRAINT module_evidence_link_target_shape CHECK (
    (target_kind = 'module'
      AND pathway_id IS NULL AND entity_id IS NULL AND edge_id IS NULL)
    OR (target_kind = 'pathway'
      AND pathway_id IS NOT NULL AND entity_id IS NULL AND edge_id IS NULL)
    OR (target_kind = 'pathway_member'
      AND pathway_id IS NOT NULL AND entity_id IS NOT NULL AND edge_id IS NULL)
    OR (target_kind = 'entity'
      AND pathway_id IS NULL AND entity_id IS NOT NULL AND edge_id IS NULL)
    OR (target_kind = 'edge'
      AND pathway_id IS NULL AND entity_id IS NULL AND edge_id IS NOT NULL)
  ),
  CONSTRAINT module_evidence_link_module_name CHECK (
    target_kind <> 'module' OR (module IS NOT NULL AND btrim(module) <> '')
  ),
  CONSTRAINT module_evidence_link_status CHECK (
    support_status IN ('supporting', 'contextual', 'contradictory', 'unresolved', 'excluded')
  ),
  CONSTRAINT module_evidence_link_grade CHECK (
    evidence_grade IS NULL OR evidence_grade IN ('A', 'B', 'C', 'D', 'E', 'U')
  ),
  CONSTRAINT module_evidence_link_context CHECK (
    context_level IS NULL OR context_level IN ('L0', 'L1', 'L2', 'L3', 'L4')
  ),
  CONSTRAINT module_evidence_link_inference_role CHECK (
    inference_role IN ('descriptive', 'predictive', 'causal_supporting', 'unknown')
  ),
  CONSTRAINT module_evidence_link_release_status CHECK (
    release_status IN ('staging', 'included', 'held', 'screened_out', 'retired')
  ),
  CONSTRAINT module_evidence_link_basis_nonempty CHECK (btrim(link_basis) <> ''),
  CONSTRAINT module_evidence_link_included_anchor CHECK (
    release_status <> 'included'
    OR local_paper_id IS NOT NULL
    OR local_observation_id IS NOT NULL
    OR local_claim_id IS NOT NULL
  )
);

CREATE INDEX IF NOT EXISTS idx_module_evidence_link_source
  ON ModuleEvidenceLink(source_record_id);
CREATE INDEX IF NOT EXISTS idx_module_evidence_link_module_role
  ON ModuleEvidenceLink(module, link_role, release_status);
CREATE INDEX IF NOT EXISTS idx_module_evidence_link_edge
  ON ModuleEvidenceLink(edge_id);
CREATE INDEX IF NOT EXISTS idx_module_evidence_link_entity
  ON ModuleEvidenceLink(entity_id);
CREATE INDEX IF NOT EXISTS idx_module_evidence_link_observation
  ON ModuleEvidenceLink(local_observation_id);
CREATE INDEX IF NOT EXISTS idx_module_evidence_link_grade_context
  ON ModuleEvidenceLink(evidence_grade, context_level);

CREATE UNIQUE INDEX IF NOT EXISTS uq_module_evidence_link_projection
  ON ModuleEvidenceLink (
    source_record_id,
    COALESCE(module, ''),
    link_role,
    target_kind,
    COALESCE(pathway_id, 0),
    COALESCE(entity_id, 0),
    COALESCE(edge_id, 0),
    COALESCE(local_paper_id, 0),
    COALESCE(local_observation_id, 0),
    COALESCE(local_claim_id, 0)
  );

COMMENT ON TABLE EvidenceSourceRecord IS
  'Exact external evidence pointer, such as an mSCS study, dataset, assay, observation, or claim. Detailed modality-native values remain in the source repository.';
COMMENT ON COLUMN EvidenceSourceRecord.source_record_key IS
  'Exact source-system key; never infer or synthesize an identifier.';
COMMENT ON COLUMN EvidenceSourceRecord.source_metadata_json IS
  'Small provenance/identity metadata only. Do not use this column as a lossy replacement for the source record.';
COMMENT ON TABLE ModuleEvidenceLink IS
  'Cross-cutting relationship between an external evidence record and a module, pathway, entity, or edge. It does not create or promote a mechanism edge.';
COMMENT ON COLUMN ModuleEvidenceLink.link_role IS
  'What the evidence bears on: membership, edge, pathway state, spatial context, regulatory context, contradiction, or unresolved review.';
COMMENT ON COLUMN ModuleEvidenceLink.evidence_grade IS
  'Independent A-E/U evidence-strength axis; retained separately from context_level and graph traversal status.';
COMMENT ON COLUMN ModuleEvidenceLink.context_level IS
  'Independent L0-L4 biological-context axis; retained separately from evidence_grade and graph traversal status.';
COMMENT ON COLUMN ModuleEvidenceLink.release_status IS
  'Projection release state. Included links require a local Paper, Observation, or AuthorClaim anchor.';

COMMIT;
