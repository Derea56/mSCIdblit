-- Conservative review queue for composite signaling labels.
--
-- Token matches are candidates only. This table intentionally does not create
-- contains_component edges; those require separate evidence-backed curation.

BEGIN;

CREATE TABLE IF NOT EXISTS SignalingEntityComponentCandidate (
  component_candidate_id BIGSERIAL PRIMARY KEY,
  composite_entity_id INTEGER NOT NULL,
  candidate_component_entity_id INTEGER NOT NULL,
  detection_method VARCHAR(100) NOT NULL,
  candidate_status VARCHAR(32) NOT NULL DEFAULT 'candidate',
  export_priority VARCHAR(50) NOT NULL DEFAULT 'exclude',
  source_registry VARCHAR(255) NOT NULL,
  source_version VARCHAR(100) NOT NULL,
  evidence_note TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (composite_entity_id)
    REFERENCES SignalingEntity(entity_id) ON DELETE CASCADE,
  FOREIGN KEY (candidate_component_entity_id)
    REFERENCES SignalingEntity(entity_id) ON DELETE CASCADE,
  UNIQUE (composite_entity_id, candidate_component_entity_id),
  CONSTRAINT component_candidate_status CHECK (
    candidate_status IN ('candidate', 'accepted', 'rejected', 'deferred')
  ),
  CONSTRAINT component_candidate_priority CHECK (
    export_priority IN ('high', 'medium', 'low', 'exclude')
  ),
  CONSTRAINT component_candidate_gate CHECK (
    candidate_status = 'accepted' OR export_priority = 'exclude'
  ),
  CONSTRAINT component_candidate_evidence_nonempty CHECK (btrim(evidence_note) <> '')
);

CREATE INDEX IF NOT EXISTS idx_component_candidate_composite
  ON SignalingEntityComponentCandidate(composite_entity_id);
CREATE INDEX IF NOT EXISTS idx_component_candidate_component
  ON SignalingEntityComponentCandidate(candidate_component_entity_id);
CREATE INDEX IF NOT EXISTS idx_component_candidate_status
  ON SignalingEntityComponentCandidate(candidate_status, export_priority);

INSERT INTO SignalingEntityComponentCandidate (
  composite_entity_id,
  candidate_component_entity_id,
  detection_method,
  candidate_status,
  export_priority,
  source_registry,
  source_version,
  evidence_note
)
SELECT DISTINCT
  composite.entity_id,
  component.entity_id,
  'token_match_to_explicit_tf_role',
  CASE
    WHEN EXISTS (
      SELECT 1
      FROM SignalingEdge AS accepted_edge
      WHERE accepted_edge.relation_type = 'contains_component'
        AND accepted_edge.source_entity_id = composite.entity_id
        AND accepted_edge.target_entity_id = component.entity_id
        AND coalesce(accepted_edge.export_priority, '') <> 'exclude'
    ) THEN 'accepted'
    ELSE 'candidate'
  END,
  CASE
    WHEN EXISTS (
      SELECT 1
      FROM SignalingEdge AS accepted_edge
      WHERE accepted_edge.relation_type = 'contains_component'
        AND accepted_edge.source_entity_id = composite.entity_id
        AND accepted_edge.target_entity_id = component.entity_id
        AND coalesce(accepted_edge.export_priority, '') <> 'exclude'
    ) THEN 'medium'
    ELSE 'exclude'
  END,
  'mSCIdblit_component_review',
  '2026-08-25',
  'Token matched component candidate from composite label '
    || quote_literal(composite.canonical_name)
    || ' to explicit TF role '
    || quote_literal(component.canonical_name)
    || '. Candidate rows require evidence review; no component edge is inferred.'
FROM SignalingEntity AS composite
JOIN LATERAL regexp_split_to_table(
  lower(composite.canonical_name),
  '[^a-z0-9]+'
) AS token(token_text) ON true
JOIN SignalingEntity AS component
  ON lower(coalesce(component.gene_symbol, '')) = token.token_text
JOIN SignalingEntityRole AS component_role
  ON component_role.entity_id = component.entity_id
 AND component_role.role = 'transcription_factor'
 AND component_role.role_status IN ('curated', 'derived')
 AND component_role.export_priority <> 'exclude'
WHERE composite.entity_id <> component.entity_id
  AND composite.canonical_name ~ '[^A-Za-z0-9]'
  AND length(token.token_text) >= 2
ON CONFLICT (composite_entity_id, candidate_component_entity_id)
DO UPDATE SET
  candidate_status = EXCLUDED.candidate_status,
  export_priority = EXCLUDED.export_priority,
  evidence_note = EXCLUDED.evidence_note,
  updated_at = CURRENT_TIMESTAMP;

SELECT candidate_status, export_priority, count(*) AS candidate_count
FROM SignalingEntityComponentCandidate
GROUP BY candidate_status, export_priority
ORDER BY candidate_status, export_priority;

COMMIT;
