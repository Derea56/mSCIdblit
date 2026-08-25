-- Read-only database-side role and label release gate.
-- Run after schema/schema.sql and schema/mechanism_roles_layer.sql:
--   psql "$MSCIDBLIT_DATABASE_URL" -v ON_ERROR_STOP=1 \
--     -f scripts/validate_mechanism_roles.sql

SELECT 'signaling_entities_missing_cascade_role' AS check_name, count(*) AS issue_count
FROM SignalingEntity AS entity
WHERE EXISTS (
    SELECT 1
    FROM SignalingEdge AS edge
    WHERE edge.source_entity_id = entity.entity_id
       OR edge.target_entity_id = entity.entity_id
  )
  AND NOT EXISTS (
    SELECT 1
    FROM SignalingEntityRole AS role
    WHERE role.entity_id = entity.entity_id
      AND role.role = 'signaling_cascade'
      AND role.role_status IN ('curated', 'derived')
      AND role.export_priority <> 'exclude'
  );

SELECT 'binds_receptor_edges_missing_endpoint_roles' AS check_name, count(*) AS issue_count
FROM SignalingEdge AS edge
WHERE edge.relation_type = 'binds_receptor'
  AND (
    NOT EXISTS (
      SELECT 1 FROM SignalingEntityRole AS source_role
      WHERE source_role.entity_id = edge.source_entity_id
        AND source_role.role = 'ligand'
        AND source_role.role_status IN ('curated', 'derived')
        AND source_role.export_priority <> 'exclude'
    )
    OR NOT EXISTS (
      SELECT 1 FROM SignalingEntityRole AS target_role
      WHERE target_role.entity_id = edge.target_entity_id
        AND target_role.role = 'receptor'
        AND target_role.role_status IN ('curated', 'derived')
        AND target_role.export_priority <> 'exclude'
    )
  );

SELECT 'regulatory_edges_missing_endpoint_roles' AS check_name, count(*) AS issue_count
FROM SignalingEdge AS edge
WHERE edge.relation_type IN ('regulates_target_gene', 'induces_target_gene', 'represses_target_gene')
  AND (
    NOT EXISTS (
      SELECT 1 FROM SignalingEntityRole AS source_role
      WHERE source_role.entity_id = edge.source_entity_id
        AND source_role.role = 'transcription_factor'
        AND source_role.role_status IN ('curated', 'derived')
        AND source_role.export_priority <> 'exclude'
    )
    OR NOT EXISTS (
      SELECT 1 FROM SignalingEntityRole AS target_role
      WHERE target_role.entity_id = edge.target_entity_id
        AND target_role.role = 'target_gene'
        AND target_role.role_status IN ('curated', 'derived')
        AND target_role.export_priority <> 'exclude'
    )
  );

SELECT 'roles_missing_provenance' AS check_name, count(*) AS issue_count
FROM SignalingEntityRole
WHERE btrim(role_source) = '' OR btrim(role_evidence) = '';

DO $$
DECLARE
  issue_count INTEGER;
BEGIN
  SELECT count(*) INTO issue_count
  FROM SignalingEntity AS entity
  WHERE EXISTS (
      SELECT 1 FROM SignalingEdge AS edge
      WHERE edge.source_entity_id = entity.entity_id
         OR edge.target_entity_id = entity.entity_id
    )
    AND NOT EXISTS (
      SELECT 1 FROM SignalingEntityRole AS role
      WHERE role.entity_id = entity.entity_id
        AND role.role = 'signaling_cascade'
        AND role.role_status IN ('curated', 'derived')
        AND role.export_priority <> 'exclude'
    );
  IF issue_count > 0 THEN
    RAISE EXCEPTION 'Mechanism role gate failed: % graph entities lack signaling_cascade role', issue_count;
  END IF;

  SELECT count(*) INTO issue_count
  FROM SignalingEdge AS edge
  WHERE edge.relation_type = 'binds_receptor'
    AND (
      NOT EXISTS (
        SELECT 1 FROM SignalingEntityRole AS source_role
        WHERE source_role.entity_id = edge.source_entity_id
          AND source_role.role = 'ligand'
          AND source_role.role_status IN ('curated', 'derived')
          AND source_role.export_priority <> 'exclude'
      )
      OR NOT EXISTS (
        SELECT 1 FROM SignalingEntityRole AS target_role
        WHERE target_role.entity_id = edge.target_entity_id
          AND target_role.role = 'receptor'
          AND target_role.role_status IN ('curated', 'derived')
          AND target_role.export_priority <> 'exclude'
      )
    );
  IF issue_count > 0 THEN
    RAISE EXCEPTION 'Mechanism role gate failed: % binds_receptor edges lack endpoint roles', issue_count;
  END IF;

  SELECT count(*) INTO issue_count
  FROM SignalingEdge AS edge
  WHERE edge.relation_type IN ('regulates_target_gene', 'induces_target_gene', 'represses_target_gene')
    AND (
      NOT EXISTS (
        SELECT 1 FROM SignalingEntityRole AS source_role
        WHERE source_role.entity_id = edge.source_entity_id
          AND source_role.role = 'transcription_factor'
          AND source_role.role_status IN ('curated', 'derived')
          AND source_role.export_priority <> 'exclude'
      )
      OR NOT EXISTS (
        SELECT 1 FROM SignalingEntityRole AS target_role
        WHERE target_role.entity_id = edge.target_entity_id
          AND target_role.role = 'target_gene'
          AND target_role.role_status IN ('curated', 'derived')
          AND target_role.export_priority <> 'exclude'
      )
    );
  IF issue_count > 0 THEN
    RAISE EXCEPTION 'Mechanism role gate failed: % regulatory edges lack endpoint roles', issue_count;
  END IF;
END $$;
