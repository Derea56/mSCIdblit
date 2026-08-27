-- Additive public TF/regulon union layer.
--
-- This migration deliberately does not insert into, update, or replace the
-- frozen mSCIdblit mechanism tables.  The external layer is discovery-only:
-- public assertions retain source, species, raw identifiers, references,
-- normalization decisions, verification status, and limitations.  All
-- external rows are excluded from release export by default.

BEGIN;

CREATE TABLE IF NOT EXISTS external_tf_source_registry (
  source_registry TEXT NOT NULL,
  source_version TEXT NOT NULL,
  species_context TEXT NOT NULL,
  retrieval_date DATE NOT NULL,
  source_url TEXT NOT NULL,
  snapshot_path TEXT NOT NULL,
  snapshot_sha256 CHAR(64) NOT NULL,
  resource_class TEXT NOT NULL,
  upstream_version TEXT,
  notes TEXT,
  PRIMARY KEY (source_registry, source_version, species_context),
  CONSTRAINT external_tf_registry_species CHECK (
    species_context IN ('human', 'mouse')
  ),
  CONSTRAINT external_tf_registry_resource CHECK (
    resource_class IN ('tf_regulon', 'causal_signaling')
  ),
  CONSTRAINT external_tf_registry_url_nonempty CHECK (btrim(source_url) <> ''),
  CONSTRAINT external_tf_registry_sha256 CHECK (
    snapshot_sha256 ~ '^[0-9a-f]{64}$'
  )
);

CREATE TABLE IF NOT EXISTS external_tf_identity_mapping (
  mapping_id BIGSERIAL PRIMARY KEY,
  source_registry TEXT NOT NULL,
  source_version TEXT NOT NULL,
  species_context TEXT NOT NULL,
  identity_role TEXT NOT NULL,
  source_symbol TEXT NOT NULL,
  normalized_symbol TEXT,
  normalized_symbol_key TEXT,
  identity_decision TEXT NOT NULL,
  identity_reason TEXT NOT NULL,
  mscidblit_entity_id INTEGER,
  frozen_entity_match_status TEXT NOT NULL DEFAULT 'not_evaluated',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (source_registry, source_version, species_context)
    REFERENCES external_tf_source_registry(
      source_registry, source_version, species_context
    ) ON DELETE CASCADE,
  FOREIGN KEY (mscidblit_entity_id)
    REFERENCES SignalingEntity(entity_id) ON DELETE SET NULL,
  UNIQUE (
    source_registry, source_version, species_context,
    identity_role, source_symbol
  ),
  CONSTRAINT external_tf_mapping_role CHECK (
    identity_role IN ('tf', 'target')
  ),
  CONSTRAINT external_tf_mapping_decision CHECK (
    identity_decision IN (
      'normalized_exact',
      'composite_unresolved',
      'empty_unresolved',
      'non_symbol_identifier_unresolved'
    )
  ),
  CONSTRAINT external_tf_mapping_frozen_status CHECK (
    frozen_entity_match_status IN (
      'not_evaluated', 'mapped_unique', 'absent_from_frozen_graph',
      'ambiguous_frozen_entity'
    )
  ),
  CONSTRAINT external_tf_mapping_source_nonempty CHECK (btrim(source_symbol) <> ''),
  CONSTRAINT external_tf_mapping_normalized_pair CHECK (
    (normalized_symbol IS NULL AND normalized_symbol_key IS NULL)
    OR (normalized_symbol IS NOT NULL AND normalized_symbol_key IS NOT NULL)
  )
);

CREATE INDEX IF NOT EXISTS idx_external_tf_mapping_symbol
  ON external_tf_identity_mapping(normalized_symbol_key, identity_role, species_context);
CREATE INDEX IF NOT EXISTS idx_external_tf_mapping_frozen_entity
  ON external_tf_identity_mapping(mscidblit_entity_id);

CREATE TABLE IF NOT EXISTS external_tf_regulon_record (
  external_record_key TEXT PRIMARY KEY,
  source_registry TEXT NOT NULL,
  source_version TEXT NOT NULL,
  species_context TEXT NOT NULL,
  external_record_id TEXT NOT NULL,
  raw_record_id TEXT NOT NULL,
  raw_record_sha256 CHAR(64) NOT NULL,
  raw_payload JSONB NOT NULL,
  source_tf_symbol TEXT NOT NULL,
  source_target_symbol TEXT NOT NULL,
  tf_normalized_symbol TEXT,
  tf_normalized_symbol_key TEXT,
  target_normalized_symbol TEXT,
  target_normalized_symbol_key TEXT,
  raw_relationship_effect TEXT NOT NULL,
  effect_polarity TEXT NOT NULL DEFAULT 'unknown',
  relationship_class TEXT NOT NULL DEFAULT 'unresolved',
  evidence_basis TEXT NOT NULL,
  confidence_tier TEXT NOT NULL DEFAULT 'uncertain',
  dorothea_level TEXT,
  curation_effort INTEGER,
  external_sources TEXT,
  reference_text TEXT,
  reference_pmids TEXT,
  source_locator TEXT NOT NULL,
  verification_status TEXT NOT NULL DEFAULT 'unverified_public_record',
  limitations TEXT NOT NULL,
  export_priority TEXT NOT NULL DEFAULT 'exclude',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (source_registry, source_version, species_context)
    REFERENCES external_tf_source_registry(
      source_registry, source_version, species_context
    ) ON DELETE CASCADE,
  UNIQUE (
    source_registry, source_version, species_context, external_record_id
  ),
  CONSTRAINT external_tf_record_effect CHECK (
    effect_polarity IN (
      'activating_target', 'repressing_target', 'context_dependent', 'unknown'
    )
  ),
  CONSTRAINT external_tf_record_class CHECK (
    relationship_class IN (
      'direct_binding', 'perturbation_response', 'expression_association',
      'inferred_regulatory', 'unresolved'
    )
  ),
  CONSTRAINT external_tf_record_basis CHECK (
    evidence_basis IN (
      'database_curated', 'literature_lead', 'inferred_from_source_consensus',
      'unresolved'
    )
  ),
  CONSTRAINT external_tf_record_confidence CHECK (
    confidence_tier IN ('high', 'medium', 'low', 'uncertain')
  ),
  CONSTRAINT external_tf_record_verification CHECK (
    verification_status IN (
      'primary_reference_verified', 'context_limited_reference',
      'reference_lead_only', 'unverified_public_record', 'unresolved_reference'
    )
  ),
  CONSTRAINT external_tf_record_export_gate CHECK (export_priority = 'exclude'),
  CONSTRAINT external_tf_record_sha256 CHECK (raw_record_sha256 ~ '^[0-9a-f]{64}$'),
  CONSTRAINT external_tf_record_nonempty CHECK (
    btrim(external_record_id) <> ''
    AND btrim(raw_record_id) <> ''
    AND btrim(source_locator) <> ''
    AND btrim(limitations) <> ''
  )
);

CREATE INDEX IF NOT EXISTS idx_external_tf_record_tf
  ON external_tf_regulon_record(source_registry, species_context, tf_normalized_symbol_key);
CREATE INDEX IF NOT EXISTS idx_external_tf_record_target
  ON external_tf_regulon_record(species_context, target_normalized_symbol_key);
CREATE INDEX IF NOT EXISTS idx_external_tf_record_verification
  ON external_tf_regulon_record(verification_status, confidence_tier);
CREATE INDEX IF NOT EXISTS idx_external_tf_record_effect
  ON external_tf_regulon_record(species_context, effect_polarity);

CREATE TABLE IF NOT EXISTS external_tf_reference (
  external_reference_id BIGSERIAL PRIMARY KEY,
  external_record_key TEXT NOT NULL,
  reference_namespace TEXT NOT NULL,
  reference_id TEXT NOT NULL,
  reference_locator TEXT NOT NULL,
  reference_status TEXT NOT NULL DEFAULT 'database_reference_lead',
  FOREIGN KEY (external_record_key)
    REFERENCES external_tf_regulon_record(external_record_key) ON DELETE CASCADE,
  UNIQUE (external_record_key, reference_namespace, reference_id),
  CONSTRAINT external_tf_reference_namespace CHECK (
    reference_namespace IN ('PMID', 'PMCID', 'DOI', 'source_reference', 'unresolved')
  ),
  CONSTRAINT external_tf_reference_status CHECK (
    reference_status IN (
      'database_reference_lead', 'primary_reference_verified',
      'context_limited_reference', 'unresolved_reference'
    )
  ),
  CONSTRAINT external_tf_reference_nonempty CHECK (
    btrim(reference_id) <> '' AND btrim(reference_locator) <> ''
  )
);

CREATE INDEX IF NOT EXISTS idx_external_tf_reference_pmid
  ON external_tf_reference(reference_namespace, reference_id);

CREATE TABLE IF NOT EXISTS external_tf_regulon (
  external_regulon_id TEXT PRIMARY KEY,
  source_registry TEXT NOT NULL,
  source_version TEXT NOT NULL,
  species_context TEXT NOT NULL,
  tf_normalized_symbol TEXT NOT NULL,
  tf_normalized_symbol_key TEXT NOT NULL,
  regulon_name TEXT NOT NULL,
  definition_status TEXT NOT NULL DEFAULT 'candidate',
  membership_semantics TEXT NOT NULL DEFAULT 'public_source_membership',
  source_record_count INTEGER NOT NULL DEFAULT 0,
  materialized_member_count INTEGER NOT NULL DEFAULT 0,
  export_priority TEXT NOT NULL DEFAULT 'exclude',
  limitations TEXT NOT NULL,
  FOREIGN KEY (source_registry, source_version, species_context)
    REFERENCES external_tf_source_registry(
      source_registry, source_version, species_context
    ) ON DELETE CASCADE,
  UNIQUE (
    source_registry, source_version, species_context, tf_normalized_symbol_key
  ),
  CONSTRAINT external_tf_regulon_status CHECK (
    definition_status IN ('candidate', 'curated', 'deprecated')
  ),
  CONSTRAINT external_tf_regulon_semantics CHECK (
    membership_semantics = 'public_source_membership'
  ),
  CONSTRAINT external_tf_regulon_export_gate CHECK (export_priority = 'exclude'),
  CONSTRAINT external_tf_regulon_nonempty CHECK (
    btrim(tf_normalized_symbol) <> ''
    AND btrim(tf_normalized_symbol_key) <> ''
    AND btrim(regulon_name) <> ''
    AND btrim(limitations) <> ''
  )
);

-- Compatibility repair for an earlier draft that used BIGSERIAL before
-- deterministic source-scoped regulon keys were finalized. No-op on a fresh
-- install.
DO $$
BEGIN
  IF EXISTS (
    SELECT 1 FROM information_schema.columns
    WHERE table_schema = 'public'
      AND table_name = 'external_tf_regulon'
      AND column_name = 'external_regulon_id'
      AND data_type = 'bigint'
  ) THEN
    IF to_regclass('public.external_tf_regulon_member') IS NOT NULL THEN
      ALTER TABLE external_tf_regulon_member
        DROP CONSTRAINT IF EXISTS external_tf_regulon_member_external_regulon_id_fkey;
      ALTER TABLE external_tf_regulon_member
        ALTER COLUMN external_regulon_id TYPE TEXT
        USING external_regulon_id::TEXT;
    END IF;
    ALTER TABLE external_tf_regulon
      ALTER COLUMN external_regulon_id TYPE TEXT
      USING external_regulon_id::TEXT;
    ALTER TABLE external_tf_regulon
      ALTER COLUMN external_regulon_id DROP DEFAULT;
  END IF;
END $$;

CREATE TABLE IF NOT EXISTS external_tf_regulon_member (
  external_regulon_member_id BIGSERIAL PRIMARY KEY,
  external_regulon_id TEXT NOT NULL,
  external_record_key TEXT NOT NULL,
  target_normalized_symbol TEXT,
  target_normalized_symbol_key TEXT,
  membership_basis TEXT NOT NULL,
  regulatory_effect TEXT NOT NULL,
  membership_status TEXT NOT NULL DEFAULT 'candidate',
  confidence_tier TEXT NOT NULL DEFAULT 'uncertain',
  export_priority TEXT NOT NULL DEFAULT 'exclude',
  FOREIGN KEY (external_regulon_id)
    REFERENCES external_tf_regulon(external_regulon_id) ON DELETE CASCADE,
  FOREIGN KEY (external_record_key)
    REFERENCES external_tf_regulon_record(external_record_key) ON DELETE CASCADE,
  UNIQUE (external_regulon_id, external_record_key),
  CONSTRAINT external_tf_member_basis CHECK (
    membership_basis IN (
      'direct_binding', 'perturbation_response', 'expression_association',
      'inferred_regulatory', 'unresolved'
    )
  ),
  CONSTRAINT external_tf_member_effect CHECK (
    regulatory_effect IN (
      'activating_target', 'repressing_target', 'context_dependent', 'unknown'
    )
  ),
  CONSTRAINT external_tf_member_status CHECK (
    membership_status IN ('candidate', 'supported', 'excluded')
  ),
  CONSTRAINT external_tf_member_confidence CHECK (
    confidence_tier IN ('high', 'medium', 'low', 'uncertain')
  ),
  CONSTRAINT external_tf_member_export_gate CHECK (export_priority = 'exclude')
);

DO $$
BEGIN
  IF NOT EXISTS (
    SELECT 1 FROM pg_constraint
    WHERE conname = 'external_tf_regulon_member_external_regulon_id_fkey'
  ) THEN
    ALTER TABLE external_tf_regulon_member
      ADD CONSTRAINT external_tf_regulon_member_external_regulon_id_fkey
      FOREIGN KEY (external_regulon_id)
      REFERENCES external_tf_regulon(external_regulon_id) ON DELETE CASCADE;
  END IF;
END $$;

CREATE INDEX IF NOT EXISTS idx_external_tf_member_target
  ON external_tf_regulon_member(target_normalized_symbol_key);

CREATE TABLE IF NOT EXISTS external_tf_evidence_verification (
  verification_id TEXT PRIMARY KEY,
  external_record_key TEXT,
  priority_tf_symbol TEXT NOT NULL,
  species_context TEXT NOT NULL,
  target_normalized_symbol TEXT,
  verification_scope TEXT NOT NULL,
  reference_pmid TEXT,
  reference_locator TEXT,
  reference_title TEXT,
  verification_status TEXT NOT NULL,
  evidence_class TEXT NOT NULL,
  verified_effect TEXT NOT NULL,
  cell_type_context TEXT NOT NULL,
  compartment_context TEXT NOT NULL,
  stimulus_context TEXT NOT NULL,
  confidence_tier TEXT NOT NULL,
  limitations TEXT NOT NULL,
  notes TEXT NOT NULL,
  FOREIGN KEY (external_record_key)
    REFERENCES external_tf_regulon_record(external_record_key) ON DELETE SET NULL,
  CONSTRAINT external_tf_verification_species CHECK (
    species_context IN ('human', 'mouse')
  ),
  CONSTRAINT external_tf_verification_scope CHECK (
    verification_scope IN ('tf_identity', 'tf_target_record')
  ),
  CONSTRAINT external_tf_verification_status CHECK (
    verification_status IN (
      'primary_reference_verified', 'context_limited_reference',
      'database_curated_unverified', 'unresolved_reason_recorded'
    )
  ),
  CONSTRAINT external_tf_verification_class CHECK (
    evidence_class IN (
      'direct_binding', 'perturbation_response', 'expression_association',
      'inferred_regulatory', 'unresolved'
    )
  ),
  CONSTRAINT external_tf_verification_effect CHECK (
    verified_effect IN (
      'activating_target', 'repressing_target', 'context_dependent', 'unknown'
    )
  ),
  CONSTRAINT external_tf_verification_confidence CHECK (
    confidence_tier IN ('high', 'medium', 'low', 'uncertain')
  ),
  CONSTRAINT external_tf_verification_required_context CHECK (
    btrim(cell_type_context) <> ''
    AND btrim(compartment_context) <> ''
    AND btrim(stimulus_context) <> ''
    AND btrim(limitations) <> ''
    AND btrim(notes) <> ''
  )
);

CREATE INDEX IF NOT EXISTS idx_external_tf_verification_priority
  ON external_tf_evidence_verification(priority_tf_symbol, species_context);
CREATE INDEX IF NOT EXISTS idx_external_tf_verification_record
  ON external_tf_evidence_verification(external_record_key);

-- Downstream view: every source-specific assertion remains visible, while
-- frozen-node and explicit-role coverage are exposed as separate flags.
CREATE OR REPLACE VIEW external_tf_downstream_union AS
SELECT
  record.external_record_key,
  record.source_registry,
  record.source_version,
  record.species_context,
  record.external_record_id,
  record.source_tf_symbol,
  record.source_target_symbol,
  record.tf_normalized_symbol,
  record.target_normalized_symbol,
  record.raw_relationship_effect,
  record.effect_polarity,
  record.relationship_class,
  record.evidence_basis,
  record.confidence_tier,
  record.dorothea_level,
  record.reference_pmids,
  record.verification_status,
  record.limitations,
  tf_map.mscidblit_entity_id AS tf_entity_id,
  target_map.mscidblit_entity_id AS target_entity_id,
  (tf_map.mscidblit_entity_id IS NOT NULL) AS tf_node_present,
  (target_map.mscidblit_entity_id IS NOT NULL) AS target_node_present,
  EXISTS (
    SELECT 1 FROM SignalingEntityRole role
    WHERE role.entity_id = tf_map.mscidblit_entity_id
      AND role.role = 'transcription_factor'
      AND role.role_status IN ('curated', 'derived')
      AND role.export_priority <> 'exclude'
  ) AS tf_role_present,
  EXISTS (
    SELECT 1 FROM SignalingEntityRole role
    WHERE role.entity_id = target_map.mscidblit_entity_id
      AND role.role = 'target_gene'
      AND role.role_status IN ('curated', 'derived')
      AND role.export_priority <> 'exclude'
  ) AS target_role_present,
  record.tf_normalized_symbol_key,
  record.target_normalized_symbol_key
FROM external_tf_regulon_record record
LEFT JOIN external_tf_identity_mapping tf_map
  ON tf_map.source_registry = record.source_registry
 AND tf_map.source_version = record.source_version
 AND tf_map.species_context = record.species_context
 AND tf_map.identity_role = 'tf'
 AND tf_map.source_symbol = record.source_tf_symbol
LEFT JOIN external_tf_identity_mapping target_map
  ON target_map.source_registry = record.source_registry
 AND target_map.source_version = record.source_version
 AND target_map.species_context = record.species_context
 AND target_map.identity_role = 'target'
 AND target_map.source_symbol = record.source_target_symbol;

-- Entity mapping view exported after database materialization.  It keeps the
-- source-level normalization table separate from the optional exact-symbol
-- match into the frozen, mouse-scoped graph.
CREATE OR REPLACE VIEW external_tf_entity_mapping AS
SELECT
  mapping.mapping_id,
  mapping.source_registry,
  mapping.source_version,
  mapping.species_context,
  mapping.identity_role,
  mapping.source_symbol,
  mapping.normalized_symbol,
  mapping.normalized_symbol_key,
  mapping.identity_decision,
  mapping.identity_reason,
  mapping.mscidblit_entity_id,
  mapping.frozen_entity_match_status,
  entity.canonical_name AS frozen_canonical_name,
  entity.gene_symbol AS frozen_gene_symbol,
  entity.organism_scope AS frozen_organism_scope,
  EXISTS (
    SELECT 1 FROM SignalingEntityRole role
    WHERE role.entity_id = mapping.mscidblit_entity_id
      AND role.role = 'transcription_factor'
      AND role.role_status IN ('curated', 'derived')
      AND role.export_priority <> 'exclude'
  ) AS frozen_tf_role_present,
  EXISTS (
    SELECT 1 FROM SignalingEntityRole role
    WHERE role.entity_id = mapping.mscidblit_entity_id
      AND role.role = 'target_gene'
      AND role.role_status IN ('curated', 'derived')
      AND role.export_priority <> 'exclude'
  ) AS frozen_target_role_present
FROM external_tf_identity_mapping mapping
LEFT JOIN SignalingEntity entity ON entity.entity_id = mapping.mscidblit_entity_id;

-- Upstream path view: exact frozen-entity symbol matches only.  No ligand ->
-- TF activation is inferred from a regulon membership.  Complex TF labels and
-- unresolved aliases remain upstream gaps until explicitly mapped.
CREATE OR REPLACE VIEW external_tf_upstream_paths AS
SELECT DISTINCT
  record.source_registry,
  record.source_version,
  record.species_context,
  record.tf_normalized_symbol,
  record.tf_normalized_symbol_key,
  tf_map.mscidblit_entity_id AS tf_entity_id,
  edge.edge_id,
  source_entity.canonical_name AS upstream_entity_name,
  target_entity.canonical_name AS tf_entity_name,
  pathway.pathway_name,
  edge.relation_type,
  edge.effect_polarity,
  edge.species_context AS edge_species_context,
  edge.evidence_status,
  edge.export_priority,
  edge_source.support_kind,
  edge_source.source_scope,
  edge_source.confidence_tier
FROM external_tf_regulon_record record
JOIN external_tf_identity_mapping tf_map
  ON tf_map.source_registry = record.source_registry
 AND tf_map.source_version = record.source_version
 AND tf_map.species_context = record.species_context
 AND tf_map.identity_role = 'tf'
 AND tf_map.source_symbol = record.source_tf_symbol
 AND tf_map.mscidblit_entity_id IS NOT NULL
JOIN SignalingEdge edge ON edge.target_entity_id = tf_map.mscidblit_entity_id
 AND edge.export_priority <> 'exclude'
JOIN SignalingEntity source_entity ON source_entity.entity_id = edge.source_entity_id
JOIN SignalingEntity target_entity ON target_entity.entity_id = edge.target_entity_id
LEFT JOIN SignalingPathway pathway ON pathway.pathway_id = edge.pathway_id
LEFT JOIN SignalingEdgeSource edge_source ON edge_source.edge_id = edge.edge_id;

CREATE OR REPLACE VIEW external_tf_upstream_gaps AS
SELECT
  regulon.source_registry,
  regulon.source_version,
  regulon.species_context,
  regulon.tf_normalized_symbol,
  regulon.tf_normalized_symbol_key,
  tf_map.mscidblit_entity_id AS tf_entity_id,
  tf_map.frozen_entity_match_status,
  count(DISTINCT edge.edge_id) AS supported_upstream_edge_count,
  CASE WHEN count(DISTINCT edge.edge_id) = 0 THEN TRUE ELSE FALSE END
    AS upstream_path_absent,
  CASE
    WHEN tf_map.mscidblit_entity_id IS NULL THEN 'tf_node_unmapped'
    WHEN count(DISTINCT edge.edge_id) = 0 THEN 'upstream_path_absent'
    ELSE 'upstream_path_present'
  END AS upstream_gap_class
FROM external_tf_regulon regulon
LEFT JOIN external_tf_identity_mapping tf_map
  ON tf_map.source_registry = regulon.source_registry
 AND tf_map.source_version = regulon.source_version
 AND tf_map.species_context = regulon.species_context
 AND tf_map.identity_role = 'tf'
 AND tf_map.normalized_symbol_key = regulon.tf_normalized_symbol_key
LEFT JOIN SignalingEdge edge
  ON edge.target_entity_id = tf_map.mscidblit_entity_id
 AND edge.export_priority <> 'exclude'
GROUP BY
  regulon.source_registry,
  regulon.source_version,
  regulon.species_context,
  regulon.tf_normalized_symbol,
  regulon.tf_normalized_symbol_key,
  tf_map.mscidblit_entity_id,
  tf_map.frozen_entity_match_status;

COMMENT ON TABLE external_tf_source_registry IS
  'Public TF/regulon snapshot registry; additive to frozen mSCIdblit release.';
COMMENT ON TABLE external_tf_identity_mapping IS
  'Conservative source-symbol identity decisions, including unresolved/composite queue rows.';
COMMENT ON TABLE external_tf_regulon_record IS
  'One provenance-preserving public source assertion per raw source record.';
COMMENT ON TABLE external_tf_regulon IS
  'Source- and species-specific public regulon grouping; never part of frozen export.';
COMMENT ON TABLE external_tf_regulon_member IS
  'Materialized public membership rows linked one-to-one to external source records.';
COMMENT ON TABLE external_tf_evidence_verification IS
  'Manual/primary-literature verification decisions for prioritized TFs and selected records.';
COMMENT ON VIEW external_tf_entity_mapping IS
  'Source identity mapping plus optional exact-symbol match and explicit frozen role flags.';
COMMENT ON VIEW external_tf_upstream_paths IS
  'Exact frozen SignalingEdge paths terminating at mapped TF entities; no inferred ligand-to-TF activation.';
COMMENT ON VIEW external_tf_upstream_gaps IS
  'Explicit upstream coverage report for each materialized public TF regulon.';

COMMIT;
