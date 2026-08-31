-- Add independent evidence-grade and context-level axes to Module 20B-24B
-- provenance.  This migration is intentionally additive and idempotent.
-- It does not promote an edge, create Paper/Observation rows, or change the
-- existing register evidence/export gates.

BEGIN;

ALTER TABLE SignalingEdgeRegisterSource
  ADD COLUMN IF NOT EXISTS evidence_grade VARCHAR(1),
  ADD COLUMN IF NOT EXISTS context_level VARCHAR(2),
  ADD COLUMN IF NOT EXISTS grading_basis TEXT,
  ADD COLUMN IF NOT EXISTS grading_status VARCHAR(40);

ALTER TABLE SignalingEdgeSource
  ADD COLUMN IF NOT EXISTS evidence_grade VARCHAR(1),
  ADD COLUMN IF NOT EXISTS context_level VARCHAR(2),
  ADD COLUMN IF NOT EXISTS grading_basis TEXT,
  ADD COLUMN IF NOT EXISTS grading_status VARCHAR(40);

DO $$
BEGIN
  IF NOT EXISTS (
    SELECT 1 FROM pg_constraint
    WHERE conname = 'signaling_edge_register_source_evidence_grade'
  ) THEN
    ALTER TABLE SignalingEdgeRegisterSource
      ADD CONSTRAINT signaling_edge_register_source_evidence_grade
      CHECK (evidence_grade IS NULL OR evidence_grade IN ('A', 'B', 'C', 'D', 'E', 'U'));
  END IF;
  IF NOT EXISTS (
    SELECT 1 FROM pg_constraint
    WHERE conname = 'signaling_edge_register_source_context_level'
  ) THEN
    ALTER TABLE SignalingEdgeRegisterSource
      ADD CONSTRAINT signaling_edge_register_source_context_level
      CHECK (context_level IS NULL OR context_level IN ('L0', 'L1', 'L2', 'L3', 'L4'));
  END IF;
  IF NOT EXISTS (
    SELECT 1 FROM pg_constraint
    WHERE conname = 'signaling_edge_source_evidence_grade'
  ) THEN
    ALTER TABLE SignalingEdgeSource
      ADD CONSTRAINT signaling_edge_source_evidence_grade
      CHECK (evidence_grade IS NULL OR evidence_grade IN ('A', 'B', 'C', 'D', 'E', 'U'));
  END IF;
  IF NOT EXISTS (
    SELECT 1 FROM pg_constraint
    WHERE conname = 'signaling_edge_source_context_level'
  ) THEN
    ALTER TABLE SignalingEdgeSource
      ADD CONSTRAINT signaling_edge_source_context_level
      CHECK (context_level IS NULL OR context_level IN ('L0', 'L1', 'L2', 'L3', 'L4'));
  END IF;
END $$;

CREATE INDEX IF NOT EXISTS idx_signaling_edge_register_source_grade
  ON SignalingEdgeRegisterSource(evidence_grade);
CREATE INDEX IF NOT EXISTS idx_signaling_edge_register_source_context
  ON SignalingEdgeRegisterSource(context_level);
CREATE INDEX IF NOT EXISTS idx_signaling_edge_source_grade
  ON SignalingEdgeSource(evidence_grade);
CREATE INDEX IF NOT EXISTS idx_signaling_edge_source_context
  ON SignalingEdgeSource(context_level);

COMMENT ON COLUMN SignalingEdgeRegisterSource.evidence_grade IS
  'Independent A-E/U evidence axis: A corroborated literature, B single traceable primary source, C source-table evidence, D database/profile-only, E reviewed nonpromotable, U unreviewed.';
COMMENT ON COLUMN SignalingEdgeRegisterSource.context_level IS
  'Independent L0-L4 context axis: L0 none, L1 non-CNS, L2 CNS, L3 spinal-cord tissue, L4 spinal-cord injury.';
COMMENT ON COLUMN SignalingEdgeSource.evidence_grade IS
  'Independent A-E/U evidence axis retained separately from canonical traversal confidence.';
COMMENT ON COLUMN SignalingEdgeSource.context_level IS
  'Independent L0-L4 context axis retained separately from canonical traversal confidence.';

COMMIT;
