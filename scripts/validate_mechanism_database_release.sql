-- Database-backed mechanism release gate.
-- Run after loading a validated graph bundle and after
-- scripts/validate_mechanism_roles.sql.

SELECT 'edges_missing_register_mapping' AS check_name, count(*) AS issue_count
FROM SignalingEdge AS edge
LEFT JOIN SignalingEdgeRegister AS register ON register.edge_id = edge.edge_id
WHERE register.edge_id IS NULL;

SELECT 'register_edges_missing_evidence' AS check_name, count(*) AS issue_count
FROM SignalingEdgeRegister AS register
WHERE NOT EXISTS (
  SELECT 1
  FROM SignalingEdgeRegisterSource AS source
  WHERE source.edge_id = register.edge_id
);

SELECT 'orphan_register_sources' AS check_name, count(*) AS issue_count
FROM SignalingEdgeRegisterSource AS source
LEFT JOIN SignalingEdgeRegister AS register
  ON register.edge_id = source.edge_id
WHERE register.edge_id IS NULL;

DO $$
DECLARE
  issue_count INTEGER;
BEGIN
  SELECT count(*) INTO issue_count
  FROM SignalingEdge AS edge
  LEFT JOIN SignalingEdgeRegister AS register ON register.edge_id = edge.edge_id
  WHERE register.edge_id IS NULL;
  IF issue_count > 0 THEN
    RAISE EXCEPTION 'Database graph release failed: % edges lack register mappings', issue_count;
  END IF;

  SELECT count(*) INTO issue_count
  FROM SignalingEdgeRegister AS register
  WHERE NOT EXISTS (
    SELECT 1
    FROM SignalingEdgeRegisterSource AS source
    WHERE source.edge_id = register.edge_id
  );
  IF issue_count > 0 THEN
    RAISE EXCEPTION 'Database graph release failed: % register edges lack evidence rows', issue_count;
  END IF;

  SELECT count(*) INTO issue_count
  FROM SignalingEdgeRegisterSource AS source
  LEFT JOIN SignalingEdgeRegister AS register
    ON register.edge_id = source.edge_id
  WHERE register.edge_id IS NULL;
  IF issue_count > 0 THEN
    RAISE EXCEPTION 'Database graph release failed: % register evidence rows are orphaned', issue_count;
  END IF;
END $$;
