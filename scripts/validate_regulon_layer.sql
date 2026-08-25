-- Read-only release gate for the regulon modeling layer.
-- Run after schema/regulon_layer.sql, for example:
--   psql "$MSCIDBLIT_DATABASE_URL" -v ON_ERROR_STOP=1 \
--     -f scripts/validate_regulon_layer.sql

SELECT
  'exportable_members_require_curated_regulon' AS check_name,
  count(*) AS issue_count
FROM RegulonMember AS member
JOIN Regulon AS regulon ON regulon.regulon_id = member.regulon_id
WHERE member.export_priority <> 'exclude'
  AND regulon.definition_status <> 'curated';

SELECT
  'exportable_members_require_supporting_evidence' AS check_name,
  count(*) AS issue_count
FROM RegulonMember AS member
WHERE member.export_priority <> 'exclude'
  AND NOT EXISTS (
    SELECT 1
    FROM RegulonMemberSource AS source
    WHERE source.regulon_member_id = member.regulon_member_id
      AND source.evidence_status = 'supporting'
      AND source.evidence_scope <> 'negative_evidence'
  );

SELECT
  'regulon_tf_requires_curated_tf_role' AS check_name,
  count(*) AS issue_count
FROM Regulon AS regulon
JOIN SignalingEntity AS entity ON entity.entity_id = regulon.tf_entity_id
WHERE NOT (
  lower(coalesce(entity.entity_type, '')) IN ('tf', 'transcription_factor', 'tf_complex')
  OR lower(coalesce(entity.entity_subtype, '')) IN ('tf', 'transcription_factor', 'tf_complex')
  OR EXISTS (
    SELECT 1
    FROM SignalingPathwayMember AS pathway_member
    WHERE pathway_member.entity_id = entity.entity_id
      AND lower(pathway_member.member_role) = 'transcription_factor'
  )
);

SELECT
  'external_only_sources_require_stable_locator' AS check_name,
  count(*) AS issue_count
FROM RegulonMemberSource AS source
WHERE source.paper_id IS NULL
  AND source.observation_id IS NULL
  AND source.claim_id IS NULL
  AND (
    source.source_locator IS NULL
    OR source.source_locator !~ '^(PMID:|PMCID:|DOI:|https?://)'
  );

DO $$
DECLARE
  issue_count INTEGER;
BEGIN
  SELECT count(*) INTO issue_count
  FROM RegulonMember AS member
  JOIN Regulon AS regulon ON regulon.regulon_id = member.regulon_id
  WHERE member.export_priority <> 'exclude'
    AND regulon.definition_status <> 'curated';
  IF issue_count > 0 THEN
    RAISE EXCEPTION 'Regulon release gate failed: % exportable members have non-curated parent regulons', issue_count;
  END IF;

  SELECT count(*) INTO issue_count
  FROM RegulonMember AS member
  WHERE member.export_priority <> 'exclude'
    AND NOT EXISTS (
      SELECT 1
      FROM RegulonMemberSource AS source
      WHERE source.regulon_member_id = member.regulon_member_id
        AND source.evidence_status = 'supporting'
        AND source.evidence_scope <> 'negative_evidence'
    );
  IF issue_count > 0 THEN
    RAISE EXCEPTION 'Regulon release gate failed: % exportable members lack supporting evidence', issue_count;
  END IF;

  SELECT count(*) INTO issue_count
  FROM Regulon AS regulon
  JOIN SignalingEntity AS entity ON entity.entity_id = regulon.tf_entity_id
  WHERE NOT (
    lower(coalesce(entity.entity_type, '')) IN ('tf', 'transcription_factor', 'tf_complex')
    OR lower(coalesce(entity.entity_subtype, '')) IN ('tf', 'transcription_factor', 'tf_complex')
    OR EXISTS (
      SELECT 1
      FROM SignalingPathwayMember AS pathway_member
      WHERE pathway_member.entity_id = entity.entity_id
        AND lower(pathway_member.member_role) = 'transcription_factor'
    )
  );
  IF issue_count > 0 THEN
    RAISE EXCEPTION 'Regulon release gate failed: % regulons have no curated TF role', issue_count;
  END IF;
END $$;
