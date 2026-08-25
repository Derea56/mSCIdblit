-- Read-only release gate for generalized TF, pathway, target, and regulon
-- materialization. Run after the generalized migration.

SELECT
  'exportable_target_edges_have_tf_and_target_roles' AS check_name,
  count(*) AS issue_count
FROM SignalingEdge AS edge
WHERE edge.relation_type IN (
    'regulates_target_gene',
    'induces_target_gene',
    'represses_target_gene'
  )
  AND coalesce(edge.export_priority, '') <> 'exclude'
  AND (
    NOT EXISTS (
      SELECT 1
      FROM SignalingEntityRole AS role
      WHERE role.entity_id = edge.source_entity_id
        AND role.role = 'transcription_factor'
        AND role.role_status IN ('curated', 'derived')
        AND role.export_priority <> 'exclude'
    )
    OR NOT EXISTS (
      SELECT 1
      FROM SignalingEntityRole AS role
      WHERE role.entity_id = edge.target_entity_id
        AND role.role = 'target_gene'
        AND role.role_status IN ('curated', 'derived')
        AND role.export_priority <> 'exclude'
    )
  );

SELECT
  'target_pairs_have_generic_regulon_membership' AS check_name,
  count(*) AS issue_count
FROM (
  SELECT DISTINCT edge.source_entity_id, edge.target_entity_id
  FROM SignalingEdge AS edge
  WHERE edge.relation_type IN (
      'regulates_target_gene',
      'induces_target_gene',
      'represses_target_gene'
    )
    AND coalesce(edge.export_priority, '') <> 'exclude'
) AS pair
WHERE NOT EXISTS (
  SELECT 1
  FROM Regulon AS regulon
  JOIN RegulonMember AS member ON member.regulon_id = regulon.regulon_id
  WHERE regulon.tf_entity_id = pair.source_entity_id
    AND regulon.source_registry = 'mSCIdblit_signaling_edges'
    AND regulon.source_version = '2026-08-25'
    AND member.target_entity_id = pair.target_entity_id
);

SELECT
  'exportable_target_pairs_with_nonnegative_evidence_are_supported' AS check_name,
  count(*) AS issue_count
FROM (
  SELECT
    edge.source_entity_id,
    edge.target_entity_id,
    bool_or(
      register_source.evidence_exportable
      AND coalesce(register_source.source_scope, '') <> 'negative_evidence'
    ) AS has_nonnegative_exportable_source
  FROM SignalingEdge AS edge
  JOIN SignalingEdgeRegisterSource AS register_source
    ON register_source.edge_id = edge.edge_id
  WHERE edge.relation_type IN (
      'regulates_target_gene',
      'induces_target_gene',
      'represses_target_gene'
    )
    AND coalesce(edge.export_priority, '') <> 'exclude'
  GROUP BY edge.source_entity_id, edge.target_entity_id
) AS pair
JOIN Regulon AS regulon
  ON regulon.tf_entity_id = pair.source_entity_id
 AND regulon.source_registry = 'mSCIdblit_signaling_edges'
 AND regulon.source_version = '2026-08-25'
JOIN RegulonMember AS member
  ON member.regulon_id = regulon.regulon_id
 AND member.target_entity_id = pair.target_entity_id
WHERE pair.has_nonnegative_exportable_source
  AND (
    member.membership_status <> 'supported'
    OR member.export_priority = 'exclude'
    OR NOT EXISTS (
      SELECT 1
      FROM RegulonMemberSource AS source
      WHERE source.regulon_member_id = member.regulon_member_id
        AND source.evidence_status = 'supporting'
        AND source.evidence_scope <> 'negative_evidence'
    )
  );

SELECT
  'target_edge_pathways_have_tf_membership' AS check_name,
  count(*) AS issue_count
FROM (
  SELECT DISTINCT edge.pathway_id, edge.source_entity_id
  FROM SignalingEdge AS edge
  WHERE edge.pathway_id IS NOT NULL
    AND edge.relation_type IN (
      'regulates_target_gene',
      'induces_target_gene',
      'represses_target_gene'
    )
    AND coalesce(edge.export_priority, '') <> 'exclude'
) AS pathway_tf
WHERE NOT EXISTS (
  SELECT 1
  FROM SignalingPathwayMember AS member
  WHERE member.pathway_id = pathway_tf.pathway_id
    AND member.entity_id = pathway_tf.source_entity_id
    AND member.member_role = 'transcription_factor'
);

SELECT
  'unresolved_component_candidates_are_not_exportable' AS check_name,
  count(*) AS issue_count
FROM SignalingEntityComponentCandidate
WHERE candidate_status <> 'accepted'
  AND export_priority <> 'exclude';

DO $$
DECLARE
  issue_count INTEGER;
BEGIN
  SELECT count(*) INTO issue_count
  FROM SignalingEdge AS edge
  WHERE edge.relation_type IN (
      'regulates_target_gene',
      'induces_target_gene',
      'represses_target_gene'
    )
    AND coalesce(edge.export_priority, '') <> 'exclude'
    AND (
      NOT EXISTS (
        SELECT 1 FROM SignalingEntityRole AS role
        WHERE role.entity_id = edge.source_entity_id
          AND role.role = 'transcription_factor'
          AND role.role_status IN ('curated', 'derived')
          AND role.export_priority <> 'exclude'
      )
      OR NOT EXISTS (
        SELECT 1 FROM SignalingEntityRole AS role
        WHERE role.entity_id = edge.target_entity_id
          AND role.role = 'target_gene'
          AND role.role_status IN ('curated', 'derived')
          AND role.export_priority <> 'exclude'
      )
    );
  IF issue_count > 0 THEN
    RAISE EXCEPTION 'Generalized TF release gate failed: % target edges lack roles', issue_count;
  END IF;

  SELECT count(*) INTO issue_count
  FROM (
    SELECT DISTINCT edge.source_entity_id, edge.target_entity_id
    FROM SignalingEdge AS edge
    WHERE edge.relation_type IN (
        'regulates_target_gene',
        'induces_target_gene',
        'represses_target_gene'
      )
      AND coalesce(edge.export_priority, '') <> 'exclude'
  ) AS pair
  WHERE NOT EXISTS (
    SELECT 1
    FROM Regulon AS regulon
    JOIN RegulonMember AS member ON member.regulon_id = regulon.regulon_id
    WHERE regulon.tf_entity_id = pair.source_entity_id
      AND regulon.source_registry = 'mSCIdblit_signaling_edges'
      AND regulon.source_version = '2026-08-25'
      AND member.target_entity_id = pair.target_entity_id
  );
  IF issue_count > 0 THEN
    RAISE EXCEPTION 'Generalized TF release gate failed: % target pairs lack regulon membership', issue_count;
  END IF;

  SELECT count(*) INTO issue_count
  FROM (
    SELECT DISTINCT edge.pathway_id, edge.source_entity_id
    FROM SignalingEdge AS edge
    WHERE edge.pathway_id IS NOT NULL
      AND edge.relation_type IN (
        'regulates_target_gene',
        'induces_target_gene',
        'represses_target_gene'
      )
      AND coalesce(edge.export_priority, '') <> 'exclude'
  ) AS pathway_tf
  WHERE NOT EXISTS (
    SELECT 1
    FROM SignalingPathwayMember AS member
    WHERE member.pathway_id = pathway_tf.pathway_id
      AND member.entity_id = pathway_tf.source_entity_id
      AND member.member_role = 'transcription_factor'
  );
  IF issue_count > 0 THEN
    RAISE EXCEPTION 'Generalized TF release gate failed: % target-edge pathways lack TF membership', issue_count;
  END IF;

  SELECT count(*) INTO issue_count
  FROM SignalingEntityComponentCandidate
  WHERE candidate_status <> 'accepted'
    AND export_priority <> 'exclude';
  IF issue_count > 0 THEN
    RAISE EXCEPTION 'Generalized TF release gate failed: % unresolved component candidates are exportable', issue_count;
  END IF;
END $$;
