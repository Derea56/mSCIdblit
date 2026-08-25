-- Explicit mechanism node roles for mSCS and database-side graph queries.
-- Apply after schema/schema.sql.  SignalingEntity.entity_type remains the
-- single legacy type; this table is the many-to-many role authority.

BEGIN;

CREATE TABLE IF NOT EXISTS SignalingEntityRole (
  entity_role_id SERIAL PRIMARY KEY,
  entity_id INTEGER NOT NULL,
  role VARCHAR(64) NOT NULL,
  role_status VARCHAR(32) NOT NULL DEFAULT 'candidate',
  role_source VARCHAR(255) NOT NULL,
  role_evidence TEXT NOT NULL,
  source_registry VARCHAR(255),
  source_version VARCHAR(100),
  export_priority VARCHAR(50) NOT NULL DEFAULT 'exclude',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (entity_id)
    REFERENCES SignalingEntity(entity_id) ON DELETE CASCADE,
  UNIQUE (entity_id, role),
  CONSTRAINT signaling_entity_role_name CHECK (
    role IN ('ligand', 'receptor', 'transcription_factor', 'target_gene', 'signaling_cascade')
  ),
  CONSTRAINT signaling_entity_role_status CHECK (
    role_status IN ('curated', 'derived', 'candidate', 'retired')
  ),
  CONSTRAINT signaling_entity_role_source_nonempty CHECK (btrim(role_source) <> ''),
  CONSTRAINT signaling_entity_role_evidence_nonempty CHECK (btrim(role_evidence) <> ''),
  CONSTRAINT signaling_entity_role_priority CHECK (
    export_priority IN ('high', 'medium', 'low', 'exclude')
  ),
  CONSTRAINT signaling_entity_role_export_gate CHECK (
    export_priority = 'exclude'
    OR role_status IN ('curated', 'derived')
  )
);

CREATE INDEX IF NOT EXISTS idx_signaling_entity_role_entity
  ON SignalingEntityRole(entity_id);
CREATE INDEX IF NOT EXISTS idx_signaling_entity_role_role
  ON SignalingEntityRole(role);
CREATE INDEX IF NOT EXISTS idx_signaling_entity_role_status
  ON SignalingEntityRole(role_status, export_priority);
CREATE INDEX IF NOT EXISTS idx_signaling_entity_role_source
  ON SignalingEntityRole(source_registry, source_version);

COMMENT ON TABLE SignalingEntityRole IS
  'Many-to-many role authority for mechanism nodes; signaling_cascade does not imply activation.';
COMMENT ON COLUMN SignalingEntityRole.role_evidence IS
  'Stable edge/evidence or database provenance supporting this role assignment.';
COMMENT ON COLUMN SignalingEntityRole.export_priority IS
  'Only curated or derived roles can be exported to mSCS; exclude is the safe default.';

COMMIT;
