-- Generalized evidence-backed TF/regulon materialization.
--
-- This migration does not infer ligand -> TF activation and does not split
-- composite labels. It materializes only existing, exportable canonical
-- TF-target SignalingEdge rows and their register provenance.
--
-- Apply after:
--   schema/regulon_layer.sql
--   schema/mechanism_register_layer.sql
--   schema/mechanism_roles_layer.sql
--   scripts/materialize_mechanism_roles.sql
--   schema/nfkb1_core_regulon_layer.sql (when that example is present)

BEGIN;

DO $$
BEGIN
  IF to_regclass('public.Regulon') IS NULL
     OR to_regclass('public.RegulonMember') IS NULL
     OR to_regclass('public.RegulonMemberSource') IS NULL THEN
    RAISE EXCEPTION
      'Generalized regulon materialization requires schema/regulon_layer.sql';
  END IF;
  IF to_regclass('public.SignalingEdgeRegisterSource') IS NULL THEN
    RAISE EXCEPTION
      'Generalized regulon materialization requires schema/mechanism_register_layer.sql';
  END IF;
END $$;

CREATE TEMP TABLE _msc_idblit_tf_target_pair ON COMMIT DROP AS
WITH target_edges AS (
  SELECT edge.*
  FROM SignalingEdge AS edge
  WHERE edge.relation_type IN (
      'regulates_target_gene',
      'induces_target_gene',
      'represses_target_gene'
    )
    AND coalesce(edge.export_priority, '') <> 'exclude'
    AND EXISTS (
      SELECT 1
      FROM SignalingEntityRole AS source_role
      WHERE source_role.entity_id = edge.source_entity_id
        AND source_role.role = 'transcription_factor'
        AND source_role.role_status IN ('curated', 'derived')
        AND source_role.export_priority <> 'exclude'
    )
    AND EXISTS (
      SELECT 1
      FROM SignalingEntityRole AS target_role
      WHERE target_role.entity_id = edge.target_entity_id
        AND target_role.role = 'target_gene'
        AND target_role.role_status IN ('curated', 'derived')
        AND target_role.export_priority <> 'exclude'
    )
),
source_rows AS (
  SELECT
    edge.edge_id,
    edge.source_entity_id AS tf_entity_id,
    edge.target_entity_id,
    edge.pathway_id,
    edge.effect_polarity,
    edge.relation_type,
    register.register_edge_id,
    register.confidence_tier AS register_confidence_tier,
    register.edge_status,
    register_source.register_evidence_id,
    register_source.support_kind,
    register_source.source_scope,
    register_source.confidence_tier AS source_confidence_tier,
    register_source.evidence_exportable
  FROM target_edges AS edge
  JOIN SignalingEdgeRegister AS register
    ON register.edge_id = edge.edge_id
  JOIN SignalingEdgeRegisterSource AS register_source
    ON register_source.edge_id = edge.edge_id
),
pair_rows AS (
  SELECT
    tf_entity_id,
    target_entity_id,
    count(DISTINCT edge_id) AS edge_count,
    string_agg(DISTINCT edge_id::text, ', ' ORDER BY edge_id::text) AS edge_ids,
    string_agg(DISTINCT register_edge_id, ', ' ORDER BY register_edge_id) AS register_edge_ids,
    bool_or(
      evidence_exportable
      AND coalesce(source_scope, '') <> 'negative_evidence'
    ) AS has_nonnegative_exportable_source,
    bool_or(
      evidence_exportable
      AND coalesce(source_scope, '') = 'direct_edge'
    ) AS has_direct_source,
    bool_or(effect_polarity = 'activating') AS has_activating_edge,
    bool_or(effect_polarity = 'inhibitory') AS has_inhibitory_edge,
    bool_or(effect_polarity = 'context_dependent') AS has_context_edge,
    string_agg(
      DISTINCT coalesce(register_edge_id, edge_id::text),
      ', ' ORDER BY coalesce(register_edge_id, edge_id::text)
    ) AS evidence_registers
  FROM source_rows
  GROUP BY tf_entity_id, target_entity_id
)
SELECT
  pair_rows.*,
  CASE
    WHEN pair_rows.has_activating_edge AND pair_rows.has_inhibitory_edge
      THEN 'context_dependent'
    WHEN pair_rows.has_context_edge
      THEN 'context_dependent'
    WHEN pair_rows.has_activating_edge
      THEN 'activating_target'
    WHEN pair_rows.has_inhibitory_edge
      THEN 'repressing_target'
    ELSE 'unknown'
  END AS regulatory_effect,
  CASE
    WHEN pair_rows.has_direct_source
      THEN 'direct_binding'
    ELSE 'inferred_regulatory'
  END AS membership_basis,
  CASE
    WHEN pair_rows.has_nonnegative_exportable_source
      THEN 'supported'
    ELSE 'candidate'
  END AS membership_status,
  CASE
    WHEN pair_rows.has_nonnegative_exportable_source
      THEN 'medium'
    ELSE 'uncertain'
  END AS confidence_tier,
  CASE
    WHEN pair_rows.has_nonnegative_exportable_source
      THEN 'medium'
    ELSE 'exclude'
  END AS export_priority
FROM pair_rows;

-- One release-scoped regulon per explicit TF. This is a complete
-- materialization of the current graph's evidence-backed target edges, not a
-- claim that the resulting set is an exhaustive biological regulon.
INSERT INTO Regulon (
  tf_entity_id,
  regulon_name,
  species_context,
  cell_type_context,
  compartment_context,
  source_registry,
  source_version,
  definition_status,
  membership_semantics,
  notes
)
SELECT DISTINCT
  pair.tf_entity_id,
  left(tf.canonical_name || ' evidence-backed target set', 255),
  'mixed',
  'unspecified',
  'unspecified',
  'mSCIdblit_signaling_edges',
  '2026-08-25',
  'curated',
  'target_gene_membership',
  'Release materialization of exportable canonical TF-target edges and their '
    || 'register provenance. This target set is not exhaustive and does not '
    || 'assert TF activation by an upstream ligand.'
FROM _msc_idblit_tf_target_pair AS pair
JOIN SignalingEntity AS tf
  ON tf.entity_id = pair.tf_entity_id
ON CONFLICT (
  tf_entity_id,
  species_context,
  cell_type_context,
  compartment_context,
  source_registry,
  source_version
)
DO UPDATE SET
  regulon_name = EXCLUDED.regulon_name,
  definition_status = EXCLUDED.definition_status,
  notes = EXCLUDED.notes,
  updated_at = CURRENT_TIMESTAMP;

-- The target_gene pathway is a typed downstream layer in this release. The
-- membership is supported by the same evidence-backed TF-target edges; it is
-- not an upstream signaling activation shortcut. Do not overwrite an existing
-- pathway member with a different curated role.
INSERT INTO SignalingPathwayMember (
  pathway_id,
  entity_id,
  member_role,
  membership_status,
  notes
)
SELECT DISTINCT
  edge.pathway_id,
  edge.source_entity_id,
  'transcription_factor',
  'supported',
  'Derived from exportable TF-target edges; pathway membership marks the '
    || 'downstream target-gene layer and does not assert upstream TF activation.'
FROM SignalingEdge AS edge
JOIN _msc_idblit_tf_target_pair AS pair
  ON pair.tf_entity_id = edge.source_entity_id
 AND pair.target_entity_id = edge.target_entity_id
WHERE edge.pathway_id IS NOT NULL
  AND edge.relation_type IN (
    'regulates_target_gene',
    'induces_target_gene',
    'represses_target_gene'
  )
  AND NOT EXISTS (
    SELECT 1
    FROM SignalingPathwayMember AS existing_member
    WHERE existing_member.pathway_id = edge.pathway_id
      AND existing_member.entity_id = edge.source_entity_id
  )
ON CONFLICT DO NOTHING;

INSERT INTO RegulonMember (
  regulon_id,
  target_entity_id,
  membership_basis,
  regulatory_effect,
  membership_status,
  confidence_tier,
  export_priority,
  notes
)
SELECT
  regulon.regulon_id,
  pair.target_entity_id,
  pair.membership_basis,
  pair.regulatory_effect,
  pair.membership_status,
  pair.confidence_tier,
  pair.export_priority,
  'Materialized from ' || pair.edge_count::text
    || ' canonical target-gene edge(s); registers: '
    || pair.evidence_registers
FROM _msc_idblit_tf_target_pair AS pair
JOIN Regulon AS regulon
  ON regulon.tf_entity_id = pair.tf_entity_id
 AND regulon.source_registry = 'mSCIdblit_signaling_edges'
 AND regulon.source_version = '2026-08-25'
 AND regulon.species_context = 'mixed'
 AND regulon.cell_type_context = 'unspecified'
 AND regulon.compartment_context = 'unspecified'
ON CONFLICT (regulon_id, target_entity_id)
DO UPDATE SET
  membership_basis = EXCLUDED.membership_basis,
  regulatory_effect = EXCLUDED.regulatory_effect,
  membership_status = EXCLUDED.membership_status,
  confidence_tier = EXCLUDED.confidence_tier,
  export_priority = EXCLUDED.export_priority,
  notes = EXCLUDED.notes,
  updated_at = CURRENT_TIMESTAMP;

-- Preserve every register source, including explicit negative evidence. A
-- membership is exportable only when at least one non-negative exportable
-- source exists, as determined above.
INSERT INTO RegulonMemberSource (
  regulon_member_id,
  source_registry,
  source_version,
  external_record_id,
  source_locator,
  support_kind,
  evidence_scope,
  evidence_status,
  species_support,
  confidence_tier,
  citation_note,
  limitations
)
SELECT DISTINCT
  member.regulon_member_id,
  'mSCIdblit_edge_register',
  '2026-08-25',
  register_source.register_evidence_id,
  register_source.source_locator,
  coalesce(register_source.support_kind, 'manual_background'),
  CASE register_source.source_scope
    WHEN 'direct_edge' THEN 'direct_binding'
    WHEN 'negative_evidence' THEN 'negative_evidence'
    WHEN 'contextual_support' THEN 'inferred_regulatory'
    WHEN 'pathway_membership' THEN 'inferred_regulatory'
    ELSE 'inferred_regulatory'
  END,
  CASE
    WHEN register_source.source_scope = 'negative_evidence'
      THEN 'negative'
    WHEN register_source.evidence_exportable
      THEN 'supporting'
    ELSE 'context_limited'
  END,
  coalesce(register_source.species_support, 'mixed'),
  CASE register_source.confidence_tier
    WHEN 'high' THEN 'high'
    WHEN 'low' THEN 'low'
    WHEN 'uncertain' THEN 'uncertain'
    ELSE 'medium'
  END,
  register_source.citation_note,
  'Register evidence was preserved as a regulon-source row. The source '
    || 'supports TF-target membership only and does not establish upstream '
    || 'ligand/receptor activation.'
FROM SignalingEdge AS edge
JOIN _msc_idblit_tf_target_pair AS pair
  ON pair.tf_entity_id = edge.source_entity_id
 AND pair.target_entity_id = edge.target_entity_id
JOIN SignalingEdgeRegisterSource AS register_source
  ON register_source.edge_id = edge.edge_id
JOIN RegulonMember AS member
  ON member.target_entity_id = edge.target_entity_id
JOIN Regulon AS regulon
  ON regulon.regulon_id = member.regulon_id
 AND regulon.tf_entity_id = edge.source_entity_id
 AND regulon.source_registry = 'mSCIdblit_signaling_edges'
 AND regulon.source_version = '2026-08-25'
WHERE edge.relation_type IN (
    'regulates_target_gene',
    'induces_target_gene',
    'represses_target_gene'
  )
  AND member.regulon_id = regulon.regulon_id
ON CONFLICT DO NOTHING;

SELECT 'generic_regulons' AS metric, count(*) AS value
FROM Regulon
WHERE source_registry = 'mSCIdblit_signaling_edges'
  AND source_version = '2026-08-25'
UNION ALL
SELECT 'generic_regulon_members', count(*)
FROM RegulonMember AS member
JOIN Regulon AS regulon ON regulon.regulon_id = member.regulon_id
WHERE regulon.source_registry = 'mSCIdblit_signaling_edges'
  AND regulon.source_version = '2026-08-25'
UNION ALL
SELECT 'generic_regulon_sources', count(*)
FROM RegulonMemberSource AS source
WHERE source.source_registry = 'mSCIdblit_edge_register'
  AND source.source_version = '2026-08-25';

COMMIT;
