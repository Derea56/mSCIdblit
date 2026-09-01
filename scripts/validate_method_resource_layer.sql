-- Validate the additive method-resource intake layer.
-- Apply schema/method_resource_layer.sql and the generated
-- method_resource_materialization.sql first.

\set ON_ERROR_STOP on

BEGIN;

DO $$
DECLARE
  issue_count BIGINT;
BEGIN
  SELECT COUNT(*) INTO issue_count
  FROM MethodResource
  WHERE source_status = 'verified'
    AND (source_artifact_sha256 IS NULL OR source_artifact_sha256 !~ '^[0-9a-fA-F]{64}$');
  IF issue_count > 0 THEN
    RAISE EXCEPTION 'Method-resource validation failed: % verified resources lack a valid SHA-256', issue_count;
  END IF;

  SELECT COUNT(*) INTO issue_count
  FROM MethodResourceRecord AS record
  LEFT JOIN MethodResource AS resource ON resource.method_resource_id = record.method_resource_id
  LEFT JOIN CanonicalCommunicationRecord AS communication
    ON communication.canonical_communication_id = record.canonical_communication_id
  WHERE resource.method_resource_id IS NULL
     OR communication.canonical_communication_id IS NULL;
  IF issue_count > 0 THEN
    RAISE EXCEPTION 'Method-resource validation failed: % source records have missing parent rows', issue_count;
  END IF;

  SELECT COUNT(*) INTO issue_count
  FROM MethodResourceComplexComponent AS component
  JOIN MethodResourceRecord AS record
    ON record.method_resource_record_id = component.method_resource_record_id
  WHERE record.canonical_communication_id <> component.canonical_communication_id;
  IF issue_count > 0 THEN
    RAISE EXCEPTION 'Method-resource validation failed: % complex components disagree with their source record communication ID', issue_count;
  END IF;

  SELECT COUNT(*) INTO issue_count
  FROM MethodResourceProjection AS projection
  WHERE projection.projection_sha256 IS NULL
     OR projection.projection_sha256 !~ '^[0-9a-fA-F]{64}$';
  IF issue_count > 0 THEN
    RAISE EXCEPTION 'Method-resource validation failed: % projections lack a valid SHA-256', issue_count;
  END IF;

  SELECT COUNT(*) INTO issue_count
  FROM MethodResourceNumericArtifact AS artifact
  LEFT JOIN MethodResource AS resource ON resource.method_resource_id = artifact.method_resource_id
  WHERE resource.method_resource_id IS NULL;
  IF issue_count > 0 THEN
    RAISE EXCEPTION 'Method-resource validation failed: % numeric artifacts have no parent resource', issue_count;
  END IF;

  SELECT COUNT(*) INTO issue_count
  FROM CanonicalCommunicationRecord AS communication
  WHERE NOT EXISTS (
    SELECT 1
    FROM MethodResourceRecord AS record
    WHERE record.canonical_communication_id = communication.canonical_communication_id
  );
  IF issue_count > 0 THEN
    RAISE EXCEPTION 'Method-resource validation failed: % canonical communications have no source-resource membership', issue_count;
  END IF;
END $$;

SELECT
  'PASS method-resource layer validation' AS status,
  (SELECT COUNT(*) FROM MethodResource) AS resources,
  (SELECT COUNT(*) FROM CanonicalCommunicationRecord) AS canonical_communications,
  (SELECT COUNT(*) FROM MethodResourceRecord) AS source_records,
  (SELECT COUNT(*) FROM MethodResourceComplexComponent) AS complex_components,
  (SELECT COUNT(*) FROM MethodResourceAnnotation) AS annotations,
  (SELECT COUNT(*) FROM MethodResourceProjection) AS projections,
  (SELECT COUNT(*) FROM MethodResourceNumericArtifact) AS numeric_artifacts;

ROLLBACK;
