-- Idempotently derive exportable mechanism roles from canonical SignalingEdge rows.
-- Run after schema/mechanism_roles_layer.sql and after SignalingEntity/SignalingEdge
-- materialization. Existing curated or candidate role rows are not overwritten.

BEGIN;

INSERT INTO SignalingEntityRole (
  entity_id, role, role_status, role_source, role_evidence,
  source_registry, source_version, export_priority
)
SELECT
  endpoint.entity_id,
  'signaling_cascade',
  'derived',
  'derived_from_signaling_edge',
  'Entity is an endpoint of SignalingEdge rows: '
    || string_agg(endpoint.edge_id::text, ', ' ORDER BY endpoint.edge_id),
  'SignalingEdge',
  'current',
  'low'
FROM (
  SELECT source_entity_id AS entity_id, edge_id FROM SignalingEdge
  UNION
  SELECT target_entity_id AS entity_id, edge_id FROM SignalingEdge
) AS endpoint
GROUP BY endpoint.entity_id
ON CONFLICT (entity_id, role) DO NOTHING;

INSERT INTO SignalingEntityRole (
  entity_id, role, role_status, role_source, role_evidence,
  source_registry, source_version, export_priority
)
SELECT
  edge.source_entity_id,
  'ligand',
  'derived',
  'derived_from_canonical_relation',
  'Source endpoint of binds_receptor edges: '
    || string_agg(edge.edge_id::text, ', ' ORDER BY edge.edge_id),
  'SignalingEdge',
  'current',
  'low'
FROM SignalingEdge AS edge
WHERE edge.relation_type = 'binds_receptor'
GROUP BY edge.source_entity_id
ON CONFLICT (entity_id, role) DO NOTHING;

INSERT INTO SignalingEntityRole (
  entity_id, role, role_status, role_source, role_evidence,
  source_registry, source_version, export_priority
)
SELECT
  edge.target_entity_id,
  'receptor',
  'derived',
  'derived_from_canonical_relation',
  'Target endpoint of binds_receptor edges: '
    || string_agg(edge.edge_id::text, ', ' ORDER BY edge.edge_id),
  'SignalingEdge',
  'current',
  'low'
FROM SignalingEdge AS edge
WHERE edge.relation_type = 'binds_receptor'
GROUP BY edge.target_entity_id
ON CONFLICT (entity_id, role) DO NOTHING;

INSERT INTO SignalingEntityRole (
  entity_id, role, role_status, role_source, role_evidence,
  source_registry, source_version, export_priority
)
SELECT
  edge.source_entity_id,
  'transcription_factor',
  'derived',
  'derived_from_canonical_relation',
  'Source endpoint of canonical target-gene edges: '
    || string_agg(edge.edge_id::text, ', ' ORDER BY edge.edge_id),
  'SignalingEdge',
  'current',
  'low'
FROM SignalingEdge AS edge
WHERE edge.relation_type IN (
  'regulates_target_gene', 'induces_target_gene', 'represses_target_gene'
)
GROUP BY edge.source_entity_id
ON CONFLICT (entity_id, role) DO NOTHING;

INSERT INTO SignalingEntityRole (
  entity_id, role, role_status, role_source, role_evidence,
  source_registry, source_version, export_priority
)
SELECT
  edge.target_entity_id,
  'target_gene',
  'derived',
  'derived_from_canonical_relation',
  'Target endpoint of canonical target-gene edges: '
    || string_agg(edge.edge_id::text, ', ' ORDER BY edge.edge_id),
  'SignalingEdge',
  'current',
  'low'
FROM SignalingEdge AS edge
WHERE edge.relation_type IN (
  'regulates_target_gene', 'induces_target_gene', 'represses_target_gene'
)
GROUP BY edge.target_entity_id
ON CONFLICT (entity_id, role) DO NOTHING;

SELECT role, count(*) AS role_count
FROM SignalingEntityRole
WHERE role_status IN ('curated', 'derived')
  AND export_priority <> 'exclude'
GROUP BY role
ORDER BY role;

COMMIT;
