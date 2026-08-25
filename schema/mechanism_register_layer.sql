-- Preserve register-backed mechanism provenance when graph rows are loaded into
-- the normalized database. Apply after schema/schema.sql and before loading a
-- Module 20B-24B mechanism bundle.

BEGIN;

-- The evidence registers contain long composite labels and explanatory
-- relation descriptions. Widening these columns preserves the source text;
-- it does not change the role or edge release gates.
ALTER TABLE SignalingEntity
  ALTER COLUMN canonical_name TYPE TEXT;
ALTER TABLE SignalingEdge
  ALTER COLUMN relation_type TYPE TEXT;
ALTER TABLE SignalingEdge
  ALTER COLUMN evidence_status TYPE TEXT;
ALTER TABLE SignalingEdge
  ALTER COLUMN context_scope TYPE TEXT;

CREATE TABLE IF NOT EXISTS SignalingEdgeRegister (
  edge_register_id BIGSERIAL PRIMARY KEY,
  edge_id INTEGER NOT NULL UNIQUE,
  register_edge_id VARCHAR(255) NOT NULL UNIQUE,
  module VARCHAR(32) NOT NULL,
  source_label TEXT NOT NULL,
  target_label TEXT NOT NULL,
  register_relation_type TEXT NOT NULL,
  graph_relation_type TEXT NOT NULL,
  pathway_name TEXT NOT NULL,
  evidence_layer TEXT NOT NULL,
  edge_status TEXT NOT NULL,
  confidence_tier VARCHAR(50),
  evidence_ids TEXT,
  consolidation_note TEXT,
  FOREIGN KEY (edge_id) REFERENCES SignalingEdge(edge_id) ON DELETE CASCADE
);

ALTER TABLE SignalingEdgeRegister
  ALTER COLUMN edge_status TYPE TEXT;

CREATE INDEX IF NOT EXISTS idx_signaling_edge_register_edge
  ON SignalingEdgeRegister(edge_id);
CREATE INDEX IF NOT EXISTS idx_signaling_edge_register_module
  ON SignalingEdgeRegister(module, pathway_name);

CREATE TABLE IF NOT EXISTS SignalingEdgeRegisterSource (
  register_source_id BIGSERIAL PRIMARY KEY,
  edge_id INTEGER NOT NULL,
  register_edge_id VARCHAR(255) NOT NULL,
  register_evidence_id VARCHAR(255) NOT NULL,
  module VARCHAR(32) NOT NULL,
  support_kind VARCHAR(100),
  species_support VARCHAR(50),
  source_scope VARCHAR(100),
  confidence_tier VARCHAR(50),
  citation_note TEXT,
  notes TEXT,
  source_kind TEXT,
  source_locator TEXT,
  source_locator_status VARCHAR(100),
  evidence_summary TEXT,
  limitations TEXT,
  evidence_layer TEXT,
  evidence_exportable BOOLEAN NOT NULL DEFAULT FALSE,
  consolidation_note TEXT,
  FOREIGN KEY (edge_id) REFERENCES SignalingEdge(edge_id) ON DELETE CASCADE,
  UNIQUE (edge_id, register_evidence_id)
);

CREATE INDEX IF NOT EXISTS idx_signaling_edge_register_source_edge
  ON SignalingEdgeRegisterSource(edge_id);
CREATE INDEX IF NOT EXISTS idx_signaling_edge_register_source_species
  ON SignalingEdgeRegisterSource(species_support);
CREATE INDEX IF NOT EXISTS idx_signaling_edge_register_source_locator
  ON SignalingEdgeRegisterSource(source_locator_status);

COMMENT ON TABLE SignalingEdgeRegister IS
  'Raw register identity and relation text for normalized mechanism edges; preserves source labels without heuristic splitting.';
COMMENT ON TABLE SignalingEdgeRegisterSource IS
  'Register evidence provenance that cannot be forced into Paper/Observation foreign keys without a reviewed source mapping.';

COMMIT;
