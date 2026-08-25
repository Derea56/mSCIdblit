-- Read-only release gate for the explicit NFKB1 component and core regulon.

SELECT 'nfkb1_tf_role' AS check_name, count(*) AS issue_count
FROM SignalingEntity AS entity
LEFT JOIN SignalingEntityRole AS role
  ON role.entity_id = entity.entity_id
 AND role.role = 'transcription_factor'
 AND role.role_status IN ('curated', 'derived')
 AND role.export_priority <> 'exclude'
WHERE entity.canonical_name = 'NFKB1'
  AND role.entity_role_id IS NULL;

SELECT 'nfkb1_core_target_count' AS check_name,
       count(*) AS observed_count,
       17 AS expected_count
FROM SignalingEdge AS edge
JOIN SignalingEntity AS source ON source.entity_id = edge.source_entity_id
WHERE source.canonical_name = 'NFKB1'
  AND edge.relation_type = 'regulates_target_gene'
  AND edge.pathway_id = (
    SELECT pathway_id
    FROM SignalingPathway
    WHERE pathway_name = 'NFKB1-core-regulon'
  );

SELECT 'nfkb1_targets_missing_target_role' AS check_name, count(*) AS issue_count
FROM SignalingEdge AS edge
JOIN SignalingEntity AS source ON source.entity_id = edge.source_entity_id
LEFT JOIN SignalingEntityRole AS role
  ON role.entity_id = edge.target_entity_id
 AND role.role = 'target_gene'
 AND role.role_status IN ('curated', 'derived')
 AND role.export_priority <> 'exclude'
WHERE source.canonical_name = 'NFKB1'
  AND edge.relation_type = 'regulates_target_gene'
  AND role.entity_role_id IS NULL;

SELECT 'nfkb1_target_edges_missing_register_evidence' AS check_name, count(*) AS issue_count
FROM SignalingEdge AS edge
JOIN SignalingEntity AS source ON source.entity_id = edge.source_entity_id
WHERE source.canonical_name = 'NFKB1'
  AND edge.relation_type = 'regulates_target_gene'
  AND NOT EXISTS (
    SELECT 1
    FROM SignalingEdgeRegisterSource AS register_source
    WHERE register_source.edge_id = edge.edge_id
  );

SELECT 'nfkb1_regulon_members_missing_source' AS check_name, count(*) AS issue_count
FROM RegulonMember AS member
JOIN Regulon AS regulon ON regulon.regulon_id = member.regulon_id
JOIN SignalingEntity AS tf ON tf.entity_id = regulon.tf_entity_id
WHERE tf.canonical_name = 'NFKB1'
  AND member.export_priority <> 'exclude'
  AND NOT EXISTS (
    SELECT 1
    FROM RegulonMemberSource AS source
    WHERE source.regulon_member_id = member.regulon_member_id
      AND source.evidence_status = 'supporting'
  );

SELECT 'tnfr_nfkb1_activation_edges' AS check_name, count(*) AS issue_count
FROM SignalingEdge AS edge
JOIN SignalingEntity AS source ON source.entity_id = edge.source_entity_id
JOIN SignalingEntity AS target ON target.entity_id = edge.target_entity_id
WHERE source.canonical_name IN ('TNFR1/p55 receptor', 'TNFR2 receptor complex')
  AND target.canonical_name = 'NFKB1'
  AND edge.relation_type IN ('activates', 'supports_tf_activation');

DO $$
DECLARE
  issue_count INTEGER;
BEGIN
  SELECT count(*) INTO issue_count
  FROM SignalingEntity AS entity
  LEFT JOIN SignalingEntityRole AS role
    ON role.entity_id = entity.entity_id
   AND role.role = 'transcription_factor'
   AND role.role_status IN ('curated', 'derived')
   AND role.export_priority <> 'exclude'
  WHERE entity.canonical_name = 'NFKB1'
    AND role.entity_role_id IS NULL;
  IF issue_count > 0 THEN
    RAISE EXCEPTION 'NFKB1 release gate failed: missing explicit TF role';
  END IF;

  SELECT count(*) INTO issue_count
  FROM SignalingEdge AS edge
  JOIN SignalingEntity AS source ON source.entity_id = edge.source_entity_id
  WHERE source.canonical_name = 'NFKB1'
    AND edge.relation_type = 'regulates_target_gene'
    AND edge.pathway_id = (
      SELECT pathway_id FROM SignalingPathway
      WHERE pathway_name = 'NFKB1-core-regulon'
    );
  IF issue_count <> 17 THEN
    RAISE EXCEPTION 'NFKB1 release gate failed: expected 17 core target edges, observed %', issue_count;
  END IF;

  SELECT count(*) INTO issue_count
  FROM SignalingEdge AS edge
  JOIN SignalingEntity AS source ON source.entity_id = edge.source_entity_id
  LEFT JOIN SignalingEntityRole AS role
    ON role.entity_id = edge.target_entity_id
   AND role.role = 'target_gene'
   AND role.role_status IN ('curated', 'derived')
   AND role.export_priority <> 'exclude'
  WHERE source.canonical_name = 'NFKB1'
    AND edge.relation_type = 'regulates_target_gene'
    AND role.entity_role_id IS NULL;
  IF issue_count > 0 THEN
    RAISE EXCEPTION 'NFKB1 release gate failed: % target edges lack target_gene roles', issue_count;
  END IF;

  SELECT count(*) INTO issue_count
  FROM SignalingEdge AS edge
  JOIN SignalingEntity AS source ON source.entity_id = edge.source_entity_id
  WHERE source.canonical_name = 'NFKB1'
    AND edge.relation_type = 'regulates_target_gene'
    AND NOT EXISTS (
      SELECT 1 FROM SignalingEdgeRegisterSource AS register_source
      WHERE register_source.edge_id = edge.edge_id
    );
  IF issue_count > 0 THEN
    RAISE EXCEPTION 'NFKB1 release gate failed: % target edges lack register evidence', issue_count;
  END IF;

  SELECT count(*) INTO issue_count
  FROM RegulonMember AS member
  JOIN Regulon AS regulon ON regulon.regulon_id = member.regulon_id
  JOIN SignalingEntity AS tf ON tf.entity_id = regulon.tf_entity_id
  WHERE tf.canonical_name = 'NFKB1'
    AND member.export_priority <> 'exclude'
    AND NOT EXISTS (
      SELECT 1 FROM RegulonMemberSource AS source
      WHERE source.regulon_member_id = member.regulon_member_id
        AND source.evidence_status = 'supporting'
    );
  IF issue_count > 0 THEN
    RAISE EXCEPTION 'NFKB1 release gate failed: % regulon members lack supporting sources', issue_count;
  END IF;

  SELECT count(*) INTO issue_count
  FROM SignalingEdge AS edge
  JOIN SignalingEntity AS source ON source.entity_id = edge.source_entity_id
  JOIN SignalingEntity AS target ON target.entity_id = edge.target_entity_id
  WHERE source.canonical_name IN ('TNFR1/p55 receptor', 'TNFR2 receptor complex')
    AND target.canonical_name = 'NFKB1'
    AND edge.relation_type IN ('activates', 'supports_tf_activation');
  IF issue_count > 0 THEN
    RAISE EXCEPTION 'NFKB1 release gate failed: standalone TNFR-to-NFKB1 activation edge detected';
  END IF;
END $$;
