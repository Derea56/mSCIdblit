-- Validate the cross-cutting module/evidence bridge.
-- Run after schema/module_evidence_crosswalk.sql on the target PostgreSQL DB.

\set ON_ERROR_STOP on

BEGIN;

DO $$
DECLARE
  invalid_included BIGINT;
  invalid_verified BIGINT;
  invalid_external BIGINT;
BEGIN
  SELECT COUNT(*) INTO invalid_included
  FROM ModuleEvidenceLink AS link
  WHERE link.release_status = 'included'
    AND link.local_paper_id IS NULL
    AND link.local_observation_id IS NULL
    AND link.local_claim_id IS NULL;

  IF invalid_included <> 0 THEN
    RAISE EXCEPTION 'Module evidence validation failed: % included links lack a local paper, observation, or claim anchor', invalid_included;
  END IF;

  SELECT COUNT(*) INTO invalid_verified
  FROM ModuleEvidenceLink AS link
  JOIN EvidenceSourceRecord AS source
    ON source.source_record_id = link.source_record_id
  WHERE link.release_status = 'included'
    AND source.source_status <> 'verified';

  IF invalid_verified <> 0 THEN
    RAISE EXCEPTION 'Module evidence validation failed: % included links point to non-verified external source records', invalid_verified;
  END IF;

  SELECT COUNT(*) INTO invalid_external
  FROM ModuleEvidenceLink AS link
  LEFT JOIN EvidenceSourceRecord AS source
    ON source.source_record_id = link.source_record_id
  WHERE source.source_record_id IS NULL;

  IF invalid_external <> 0 THEN
    RAISE EXCEPTION 'Module evidence validation failed: % links have no external source record', invalid_external;
  END IF;
END $$;

SELECT
  'PASS module evidence crosswalk validation' AS status,
  (SELECT COUNT(*) FROM EvidenceSourceRecord) AS source_records,
  (SELECT COUNT(*) FROM ModuleEvidenceLink) AS links,
  (SELECT COUNT(*) FROM ModuleEvidenceLink WHERE release_status = 'included') AS included_links,
  (SELECT COUNT(*) FROM ModuleEvidenceLink WHERE release_status <> 'included') AS non_included_links;

ROLLBACK;
