-- ============================================================================
-- mSCIdblit smoke test
--
-- Usage from a fresh PostgreSQL database:
--   psql -v ON_ERROR_STOP=1 -d mscidbl -f schema/schema.sql
--   psql -v ON_ERROR_STOP=1 -d mscidbl -f scripts/seed_controlled_vocab.sql
--   psql -v ON_ERROR_STOP=1 -d mscidbl -f scripts/smoke_test.sql
--
-- This script inserts one toy paper workflow and verifies the key guarantees:
-- source provenance, evidence linking, consensus versioning, grounded
-- hypotheses, and immutable observations.
-- ============================================================================

BEGIN;

INSERT INTO Paper (title, authors, publication_year, journal, doi, abstract)
VALUES (
  'Smoke test paper for mSCIdblit',
  'Curator A',
  2026,
  'Smoke Test Journal',
  '10.0000/mscidblit-smoke-test',
  'A synthetic record used only to validate schema behavior.'
)
ON CONFLICT (doi) DO UPDATE
SET title = EXCLUDED.title
RETURNING paper_id \gset

INSERT INTO ResearchQuestion (paper_id, question_text, hypothesis_direction, keywords)
VALUES (
  :paper_id,
  'Does the smoke-test intervention alter lesion architecture?',
  'exploratory',
  'smoke-test, lesion architecture'
)
RETURNING question_id \gset

INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
VALUES (
  :paper_id,
  'Synthetic lesion architecture extraction',
  'Toy paradigm for database smoke testing',
  'Manual curation of synthetic values'
)
RETURNING paradigm_id \gset

INSERT INTO Experiment (
  paper_id,
  paradigm_id,
  experiment_number,
  figure_table_reference,
  figure_panel_reference,
  title,
  sample_size,
  control_type,
  intervention_type,
  duration_days,
  timepoint_postinjury_days,
  notes
)
VALUES (
  :paper_id,
  :paradigm_id,
  1,
  'Fig S1',
  'panel A',
  'Smoke-test control versus intervention comparison',
  12,
  'vehicle control',
  'synthetic intervention',
  28,
  28,
  'Synthetic experiment used only for validation'
)
RETURNING experiment_id \gset

INSERT INTO Experiment_Species (experiment_id, species_id)
SELECT :experiment_id, species_id
FROM ControlledVocabulary_Species
WHERE species_name = 'Mus musculus'
ON CONFLICT DO NOTHING;

INSERT INTO Experiment_InjuryModel (experiment_id, injury_model_id)
SELECT :experiment_id, injury_model_id
FROM ControlledVocabulary_InjuryModel
WHERE model_name = 'Thoracic contusion'
ON CONFLICT DO NOTHING;

INSERT INTO Experiment_LesionCompartment (experiment_id, compartment_id)
SELECT :experiment_id, compartment_id
FROM ControlledVocabulary_LesionCompartment
WHERE compartment_name = 'Lesion core'
ON CONFLICT DO NOTHING;

INSERT INTO Experiment_Assay (experiment_id, assay_id)
SELECT :experiment_id, assay_id
FROM ControlledVocabulary_Assay
WHERE assay_name = 'Lesion area measurement'
ON CONFLICT DO NOTHING;

INSERT INTO Observation (
  experiment_id,
  evidence_type_id,
  outcome_type_id,
  observation_value,
  normalized_observation_value,
  unit,
  standard_error,
  n_subjects,
  measurement_method,
  timepoint_postinjury_days,
  raw_observation_text,
  source_section,
  source_quote,
  figure_panel_reference,
  extraction_confidence,
  notes
)
SELECT
  :experiment_id,
  et.evidence_type_id,
  ot.outcome_type_id,
  '1.20',
  '1.20',
  'mm2',
  0.10,
  12,
  'Synthetic histological measurement',
  28,
  'Lesion area was 1.20 mm2 at 28 days post-injury.',
  'figure legend',
  'Lesion area was 1.20 mm2 at 28 days post-injury.',
  'Fig S1A',
  'high',
  'Synthetic observation'
FROM ControlledVocabulary_EvidenceType et
CROSS JOIN ControlledVocabulary_OutcomeType ot
WHERE et.evidence_type_name = 'Histological measurement'
  AND ot.outcome_type_name = 'Lesion area'
RETURNING observation_id \gset

INSERT INTO AuthorClaim (
  paper_id,
  claim_text,
  claim_type,
  confidence_level,
  source_section,
  source_quote,
  extraction_confidence,
  notes
)
VALUES (
  :paper_id,
  'The synthetic intervention altered lesion area in the smoke-test comparison.',
  'conclusion',
  'high',
  'discussion',
  'The synthetic intervention altered lesion area in the smoke-test comparison.',
  'high',
  'Synthetic claim'
)
RETURNING claim_id \gset

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
VALUES (
  :claim_id,
  :observation_id,
  'directly_supports',
  'Smoke-test observation directly supports the toy claim'
);

INSERT INTO Consensus (
  consensus_statement,
  topic,
  version,
  agreement_level,
  num_supporting_papers,
  num_contradicting_papers,
  notes
)
VALUES (
  'Smoke-test consensus statement generated from synthetic evidence.',
  'Smoke test',
  1,
  'emerging',
  2,
  0,
  'Synthetic consensus used only to test version trigger'
)
RETURNING consensus_id \gset

UPDATE Consensus
SET
  version = 2,
  consensus_statement = 'Updated smoke-test consensus statement generated from synthetic evidence.'
WHERE consensus_id = :consensus_id;

INSERT INTO Hypothesis (
  hypothesis_text,
  derived_from_consensus_id,
  hypothesis_type,
  testability_level,
  predicted_outcome,
  proposed_experiment,
  confidence_level
)
VALUES (
  'A second synthetic intervention would also alter lesion area.',
  :consensus_id,
  'predictive',
  'directly_testable',
  'Lesion area changes relative to vehicle control',
  'Repeat the synthetic comparison with an independent toy cohort.',
  'low'
);

CREATE TEMP TABLE smoke_context AS
SELECT
  :observation_id::INTEGER AS observation_id,
  :consensus_id::INTEGER AS consensus_id;

DO $$
DECLARE
  target_observation_id INTEGER;
BEGIN
  SELECT observation_id INTO target_observation_id FROM smoke_context;

  BEGIN
    UPDATE Observation
    SET observation_value = 'should fail'
    WHERE observation_id = target_observation_id;
    RAISE EXCEPTION 'Observation immutability trigger did not fire';
  EXCEPTION
    WHEN OTHERS THEN
      IF SQLERRM NOT LIKE 'Observation records are immutable%' THEN
        RAISE;
      END IF;
  END;
END $$;

DO $$
DECLARE
  target_consensus_id INTEGER;
  version_count INTEGER;
BEGIN
  SELECT consensus_id INTO target_consensus_id FROM smoke_context;

  SELECT COUNT(*)
  INTO version_count
  FROM Consensus_Version
  WHERE consensus_id = target_consensus_id;

  IF version_count < 2 THEN
    RAISE EXCEPTION 'Consensus version trigger produced % version rows, expected at least 2', version_count;
  END IF;
END $$;

SELECT
  'smoke_test_passed' AS status,
  :paper_id AS paper_id,
  :experiment_id AS experiment_id,
  :observation_id AS observation_id,
  :claim_id AS claim_id,
  :consensus_id AS consensus_id;

ROLLBACK;
