-- mSCIdblit regulon modeling layer
--
-- Apply after schema/schema.sql.  Regulon membership is a separate evidence
-- layer from SignalingEdge: a TF-target membership does not assert that the
-- TF is activated by any ligand or pathway.

BEGIN;

CREATE TABLE IF NOT EXISTS Regulon (
  regulon_id SERIAL PRIMARY KEY,
  tf_entity_id INTEGER NOT NULL,
  regulon_name VARCHAR(255) NOT NULL,
  species_context VARCHAR(100) NOT NULL,
  cell_type_context VARCHAR(255) NOT NULL DEFAULT 'unspecified',
  compartment_context VARCHAR(255) NOT NULL DEFAULT 'unspecified',
  source_registry VARCHAR(255) NOT NULL,
  source_version VARCHAR(100) NOT NULL,
  definition_status VARCHAR(50) NOT NULL DEFAULT 'candidate',
  membership_semantics VARCHAR(50) NOT NULL DEFAULT 'target_gene_membership',
  notes TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (tf_entity_id)
    REFERENCES SignalingEntity(entity_id) ON DELETE RESTRICT,
  UNIQUE (
    tf_entity_id,
    species_context,
    cell_type_context,
    compartment_context,
    source_registry,
    source_version
  ),
  CONSTRAINT regulon_name_nonempty CHECK (btrim(regulon_name) <> ''),
  CONSTRAINT regulon_species_nonempty CHECK (btrim(species_context) <> ''),
  CONSTRAINT regulon_definition_status CHECK (
    definition_status IN ('candidate', 'curated', 'deprecated', 'superseded')
  ),
  CONSTRAINT regulon_membership_semantics CHECK (
    membership_semantics = 'target_gene_membership'
  )
);

CREATE INDEX IF NOT EXISTS idx_regulon_tf ON Regulon(tf_entity_id);
CREATE INDEX IF NOT EXISTS idx_regulon_context
  ON Regulon(species_context, cell_type_context, compartment_context);
CREATE INDEX IF NOT EXISTS idx_regulon_status ON Regulon(definition_status);
CREATE INDEX IF NOT EXISTS idx_regulon_source
  ON Regulon(source_registry, source_version);

CREATE TABLE IF NOT EXISTS RegulonMember (
  regulon_member_id SERIAL PRIMARY KEY,
  regulon_id INTEGER NOT NULL,
  target_entity_id INTEGER NOT NULL,
  membership_basis VARCHAR(50) NOT NULL,
  regulatory_effect VARCHAR(50) NOT NULL DEFAULT 'unknown',
  membership_status VARCHAR(50) NOT NULL DEFAULT 'candidate',
  confidence_tier VARCHAR(50) NOT NULL DEFAULT 'uncertain',
  export_priority VARCHAR(50) NOT NULL DEFAULT 'exclude',
  notes TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (regulon_id)
    REFERENCES Regulon(regulon_id) ON DELETE CASCADE,
  FOREIGN KEY (target_entity_id)
    REFERENCES SignalingEntity(entity_id) ON DELETE RESTRICT,
  UNIQUE (regulon_id, target_entity_id),
  CONSTRAINT regulon_member_basis CHECK (
    membership_basis IN (
      'direct_binding',
      'perturbation_response',
      'expression_association',
      'inferred_regulatory',
      'candidate'
    )
  ),
  CONSTRAINT regulon_member_effect CHECK (
    regulatory_effect IN (
      'activating_target',
      'repressing_target',
      'context_dependent',
      'unknown'
    )
  ),
  CONSTRAINT regulon_member_status CHECK (
    membership_status IN ('candidate', 'supported', 'excluded', 'superseded')
  ),
  CONSTRAINT regulon_member_confidence CHECK (
    confidence_tier IN ('high', 'medium', 'low', 'uncertain')
  ),
  CONSTRAINT regulon_member_export_priority CHECK (
    export_priority IN ('high', 'medium', 'low', 'exclude')
  ),
  CONSTRAINT regulon_member_candidate_not_exportable CHECK (
    membership_status <> 'candidate' OR export_priority = 'exclude'
  ),
  CONSTRAINT regulon_member_non_supported_not_exportable CHECK (
    membership_status NOT IN ('excluded', 'superseded')
    OR export_priority = 'exclude'
  ),
  CONSTRAINT regulon_member_export_requires_supported CHECK (
    export_priority = 'exclude' OR membership_status = 'supported'
  )
);

CREATE INDEX IF NOT EXISTS idx_regulon_member_regulon
  ON RegulonMember(regulon_id);
CREATE INDEX IF NOT EXISTS idx_regulon_member_target
  ON RegulonMember(target_entity_id);
CREATE INDEX IF NOT EXISTS idx_regulon_member_status
  ON RegulonMember(membership_status, export_priority);
CREATE INDEX IF NOT EXISTS idx_regulon_member_basis
  ON RegulonMember(membership_basis);

CREATE TABLE IF NOT EXISTS RegulonMemberSource (
  regulon_member_source_id SERIAL PRIMARY KEY,
  regulon_member_id INTEGER NOT NULL,
  paper_id INTEGER,
  observation_id INTEGER,
  claim_id INTEGER,
  source_registry VARCHAR(255) NOT NULL,
  source_version VARCHAR(100) NOT NULL,
  external_record_id VARCHAR(255) NOT NULL,
  source_locator VARCHAR(500),
  support_kind VARCHAR(100) NOT NULL,
  evidence_scope VARCHAR(100) NOT NULL,
  evidence_status VARCHAR(50) NOT NULL DEFAULT 'supporting',
  species_support VARCHAR(50),
  confidence_tier VARCHAR(50),
  citation_note TEXT,
  limitations TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (regulon_member_id)
    REFERENCES RegulonMember(regulon_member_id) ON DELETE CASCADE,
  FOREIGN KEY (paper_id)
    REFERENCES Paper(paper_id) ON DELETE SET NULL,
  FOREIGN KEY (observation_id)
    REFERENCES Observation(observation_id) ON DELETE SET NULL,
  FOREIGN KEY (claim_id)
    REFERENCES AuthorClaim(claim_id) ON DELETE SET NULL,
  UNIQUE (
    regulon_member_id,
    source_registry,
    source_version,
    external_record_id,
    support_kind
  ),
  CONSTRAINT regulon_source_record_nonempty CHECK (btrim(external_record_id) <> ''),
  CONSTRAINT regulon_source_locator_nonempty CHECK (
    source_locator IS NULL OR btrim(source_locator) <> ''
  ),
  CONSTRAINT regulon_source_support_kind CHECK (
    support_kind IN (
      'primary_experiment',
      'review_statement',
      'database_curated',
      'consensus_summary',
      'manual_background'
    )
  ),
  CONSTRAINT regulon_source_scope CHECK (
    evidence_scope IN (
      'direct_binding',
      'perturbation_response',
      'expression_association',
      'inferred_regulatory',
      'negative_evidence'
    )
  ),
  CONSTRAINT regulon_source_status CHECK (
    evidence_status IN ('supporting', 'contradicting', 'context_limited', 'negative')
  ),
  CONSTRAINT regulon_source_species CHECK (
    species_support IS NULL
    OR species_support IN ('mouse', 'human', 'both', 'mixed', 'not_applicable')
  ),
  CONSTRAINT regulon_source_confidence CHECK (
    confidence_tier IS NULL
    OR confidence_tier IN ('high', 'medium', 'low', 'uncertain')
  ),
  CONSTRAINT regulon_source_anchor CHECK (
    paper_id IS NOT NULL OR observation_id IS NOT NULL OR claim_id IS NOT NULL
    OR source_locator IS NOT NULL
  )
);

CREATE INDEX IF NOT EXISTS idx_regulon_source_member
  ON RegulonMemberSource(regulon_member_id);
CREATE INDEX IF NOT EXISTS idx_regulon_source_paper
  ON RegulonMemberSource(paper_id);
CREATE INDEX IF NOT EXISTS idx_regulon_source_observation
  ON RegulonMemberSource(observation_id);
CREATE INDEX IF NOT EXISTS idx_regulon_source_claim
  ON RegulonMemberSource(claim_id);
CREATE INDEX IF NOT EXISTS idx_regulon_source_registry
  ON RegulonMemberSource(source_registry, source_version);
CREATE INDEX IF NOT EXISTS idx_regulon_source_status
  ON RegulonMemberSource(evidence_status, confidence_tier);

COMMENT ON TABLE Regulon IS
  'Versioned TF target-set definition; not a signaling activation state.';
COMMENT ON TABLE RegulonMember IS
  'Evidence-gated TF-to-target membership assertion; does not imply TF activation.';
COMMENT ON TABLE RegulonMemberSource IS
  'Paper, observation, claim, or stable external-record provenance for one regulon membership.';
COMMENT ON COLUMN RegulonMember.regulatory_effect IS
  'Effect on the target gene; not the activity state of the TF.';
COMMENT ON COLUMN RegulonMember.export_priority IS
  'Only supported memberships can be exported; exclude is the safe default.';

COMMIT;
