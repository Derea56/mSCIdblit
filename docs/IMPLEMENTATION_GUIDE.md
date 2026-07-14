# SCI Knowledge Base Schema v2 — Implementation Guide

## Quick Reference: Entity Hierarchy

```
Paper (bibliography)
  ├─ ResearchQuestion (what was studied?)
  ├─ ExperimentalParadigm (how was it studied?)
  │   └─ Experiment (atomic experimental comparison)
  │       ├─ Experiment_Species (controlled vocab: which animal?)
  │       ├─ Experiment_InjuryModel (controlled vocab: which injury?)
  │       ├─ Experiment_InjuryDevice (controlled vocab: which device?)
  │       ├─ Experiment_LesionCompartment (controlled vocab: where?)
  │       ├─ Experiment_Assay (controlled vocab: which outcome measure?)
  │       ├─ Experiment_Biomaterial (controlled vocab: which material?)
  │       ├─ Experiment_SurgicalProcedure (controlled vocab: which surgery?)
  │       ├─ Experiment_BiologicalEntity (which genes/proteins?)
  │       └─ Observation (atomic evidence: immutable)
  │           ├─ evidence_type_id (e.g., "behavioral measurement")
  │           └─ outcome_type_id (e.g., "locomotor recovery")
  ├─ AuthorClaim (author interpretation)
  │   └─ EvidenceLink (traceability to Observation)
  └─ Paper_Lineage (scientific tradition)

Consensus (versioned project-level synthesis)
  ├─ Consensus_Version (immutable history)
  ├─ Consensus_Observation (derived mapping to evidence)
  └─ Hypothesis (generated ideas, never from speculation)

SearchSession (reproducible search record)
```

---

## Step-by-Step Data Entry Example

### Scenario
You're extracting data from a paper: *"BDNF-expressing macrophages promote recovery after spinal cord injury"*

---

### Step 1: Create Paper Record

```sql
INSERT INTO Paper (
  title, authors, publication_year, journal, doi, abstract
) VALUES (
  'BDNF-expressing macrophages promote recovery after spinal cord injury',
  'Smith J, Johnson A, Williams B',
  2023,
  'Nature Neuroscience',
  '10.1038/s41593-023-00001',
  'Macrophages in the injured spinal cord show heterogeneous BDNF expression. We demonstrate that...'
);
-- Returns: paper_id = 1
```

---

### Step 2: Create Research Question

```sql
INSERT INTO ResearchQuestion (
  paper_id, question_text, hypothesis_direction
) VALUES (
  1,
  'Does BDNF expression in macrophages promote functional recovery after spinal cord contusion?',
  'positive'
);
-- Returns: question_id = 1
```

---

### Step 3: Create Experimental Paradigm

```sql
INSERT INTO ExperimentalParadigm (
  paper_id, paradigm_name, description
) VALUES (
  1,
  'Genetic labeling and conditional deletion in macrophages',
  'Using Ccl2-Cre transgenic mice to label and conditionally delete BDNF in macrophages'
);
-- Returns: paradigm_id = 1
```

---

### Step 4: Populate Controlled Vocabulary (if not already present)

```sql
-- Species
INSERT INTO ControlledVocabulary_Species (species_name, ncbi_taxonomy_id)
VALUES ('Mus musculus', '10090') ON CONFLICT DO NOTHING;

-- Injury Model
INSERT INTO ControlledVocabulary_InjuryModel (model_name, anatomical_target)
VALUES ('Thoracic contusion', 'T10') ON CONFLICT DO NOTHING;

-- Injury Device
INSERT INTO ControlledVocabulary_InjuryDevice (device_name, parameters)
VALUES ('NYU impactor', 'Force: 50 kilodynes') ON CONFLICT DO NOTHING;

-- Lesion Compartment
INSERT INTO ControlledVocabulary_LesionCompartment (compartment_name)
VALUES ('Gray matter and white matter') ON CONFLICT DO NOTHING;

-- Evidence Type
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name)
VALUES ('Behavioral measurement') ON CONFLICT DO NOTHING;

-- Outcome Type
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, measurement_unit)
VALUES ('Locomotor recovery', 'BMS score') ON CONFLICT DO NOTHING;

-- Assay
INSERT INTO ControlledVocabulary_Assay (assay_name, assay_type)
VALUES ('Basso Mouse Scale (BMS)', 'behavioral') ON CONFLICT DO NOTHING;

-- Cell Type
INSERT INTO ControlledVocabulary_CellType (cell_type_name)
VALUES ('Macrophages') ON CONFLICT DO NOTHING;
```

---

### Step 5: Create Experiment

```sql
INSERT INTO Experiment (
  paper_id, paradigm_id, experiment_number, title, figure_table_reference,
  sample_size, control_type, intervention_type, duration_days, timepoint_postinjury_days
) VALUES (
  1,
  1,
  1,
  'BMS recovery in Ccl2-Cre; BDNF^fl/fl vs wild-type after T10 contusion',
  'Fig 3A',
  12,  -- 12 mice per group
  'Ccl2-Cre; BDNF^+/+ littermates (wild-type)',
  'Ccl2-Cre; BDNF^fl/fl (conditional knockout)',
  28,  -- experiment duration
  7    -- measured from 7 days post-injury onward
);
-- Returns: experiment_id = 1
```

---

### Step 6: Link Experiment to Controlled Vocabulary

```sql
INSERT INTO Experiment_Species VALUES (1, 1);  -- Mus musculus
INSERT INTO Experiment_InjuryModel VALUES (1, 1);  -- T10 contusion
INSERT INTO Experiment_InjuryDevice VALUES (1, 1);  -- NYU impactor
INSERT INTO Experiment_LesionCompartment VALUES (1, 1);  -- Gray/white matter
INSERT INTO Experiment_Assay VALUES (1, 1);  -- BMS

-- Link biological entity (BDNF)
INSERT INTO BiologicalEntity (entity_name, entity_type, ncbi_gene_id)
VALUES ('BDNF', 'gene', '12064') ON CONFLICT DO NOTHING;

INSERT INTO Experiment_BiologicalEntity VALUES (
  1,
  (SELECT entity_id FROM BiologicalEntity WHERE entity_name = 'BDNF'),
  'target'  -- this is what we're studying
);
```

---

### Step 7: Record Observations (IMMUTABLE EVIDENCE)

From **Fig 3A** showing BMS scores at 28 days:

```sql
-- Observation 1: Wild-type performance
INSERT INTO Observation (
  experiment_id,
  evidence_type_id,
  outcome_type_id,
  observation_value,
  unit,
  p_value,
  n_subjects,
  measurement_method,
  timepoint_postinjury_days,
  notes
) VALUES (
  1,
  (SELECT evidence_type_id FROM ControlledVocabulary_EvidenceType WHERE evidence_type_name = 'Behavioral measurement'),
  (SELECT outcome_type_id FROM ControlledVocabulary_OutcomeType WHERE outcome_type_name = 'Locomotor recovery'),
  '16.2',  -- mean BMS score
  'BMS score (0-21)',
  NULL,  -- p-value is in the contrast, not for a single group
  12,
  'Open field locomotion assessment',
  28,
  'Mean of 3 trials per animal; SEM = 0.8'
);
-- Returns: observation_id = 1

-- Observation 2: Knockout performance
INSERT INTO Observation (
  experiment_id,
  evidence_type_id,
  outcome_type_id,
  observation_value,
  unit,
  p_value,
  n_subjects,
  measurement_method,
  timepoint_postinjury_days,
  notes
) VALUES (
  1,
  (SELECT evidence_type_id FROM ControlledVocabulary_EvidenceType WHERE evidence_type_name = 'Behavioral measurement'),
  (SELECT outcome_type_id FROM ControlledVocabulary_OutcomeType WHERE outcome_type_name = 'Locomotor recovery'),
  '10.5',  -- mean BMS score
  'BMS score (0-21)',
  0.012,  -- p-value for this contrast: WT vs KO
  12,
  'Open field locomotion assessment',
  28,
  'Mean of 3 trials per animal; SEM = 1.2'
);
-- Returns: observation_id = 2
```

---

### Step 8: Extract Author Claims

From the paper's discussion and conclusion:

```sql
INSERT INTO AuthorClaim (
  paper_id, claim_text, claim_type, confidence_level
) VALUES
  (1, 'BDNF expression in macrophages is necessary for functional recovery after SCI',
      'conclusion', 'high'),
  (1, 'BDNF-expressing macrophages promote axonal regeneration and neural sprouting',
      'interpretation', 'medium'),
  (1, 'Therapeutic targeting of macrophage BDNF could enhance recovery in chronic SCI',
      'implication', 'speculative');
-- Returns: claim_id = 1, 2, 3
```

---

### Step 9: Link Claims to Observations (Traceability)

```sql
INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
VALUES
  (1, 2, 'directly_supports', 'Knockout mice show reduced recovery, directly supporting role for BDNF'),
  (1, 1, 'indirectly_supports', 'Wild-type controls show robust recovery baseline'),
  (2, 2, 'partially_supports', 'Behavioral recovery difference suggests but does not prove regeneration mechanism');
```

Now you can query: "Show me all observations supporting claim_id = 1"

```sql
SELECT o.observation_value, o.unit, el.link_type, el.notes
FROM EvidenceLink el
JOIN Observation o ON el.observation_id = o.observation_id
WHERE el.claim_id = 1;
```

---

### Step 10: Create Project-Level Consensus

After reviewing multiple papers on macrophage BDNF:

```sql
INSERT INTO Consensus (
  consensus_statement,
  topic,
  version,
  agreement_level,
  num_supporting_papers,
  num_contradicting_papers,
  synthesis_date
) VALUES (
  'BDNF signaling from macrophages promotes functional recovery after spinal cord injury, particularly in the acute-subacute phase',
  'Macrophage BDNF and SCI recovery',
  1,
  'moderate',
  8,  -- 8 supporting papers
  2,  -- 2 papers with contradictory findings
  CURRENT_TIMESTAMP
);
-- Returns: consensus_id = 1
```

---

### Step 11: Generate Hypothesis from Consensus

```sql
INSERT INTO Hypothesis (
  hypothesis_text,
  derived_from_consensus_id,
  hypothesis_type,
  testability_level,
  predicted_outcome,
  proposed_experiment,
  confidence_level
) VALUES (
  'Blocking IL-10 production by macrophages will impair their BDNF secretion and reduce recovery',
  1,  -- derived from consensus about BDNF
  'mechanistic',
  'directly_testable',
  'IL-10-deficient macrophages will show reduced BDNF expression; transplantation of IL-10-deficient macrophages will reduce recovery compared to WT',
  'Isolate macrophages from IL-10 KO and WT mice, culture with pro-inflammatory stimulus, measure BDNF secretion via ELISA. Transplant into T10 contusion injury and assess BMS recovery.'
);
```

This hypothesis is **automatically grounded in consensus**—not free-floating speculation.

---

## Key Principles in Action

### ✅ Immutable Observations
```sql
-- Original observation recorded
INSERT INTO Observation (...) VALUES (...);  -- observation_id = 1, created_at = 2024-01-15

-- Mistake discovered! But we DON'T UPDATE; instead we INSERT a correction:
INSERT INTO Observation (..., notes = 'Correction: previous entry had transposed values')
VALUES (...);  -- observation_id = 2, created_at = 2024-01-16

-- Old observation remains in database; audit trail is preserved
SELECT * FROM Observation WHERE experiment_id = 1;  -- shows both records
```

### ✅ Claim-Evidence Traceability
```sql
-- Find the chain: Paper → Claim → Evidence
SELECT 
  p.title,
  ac.claim_text,
  o.observation_value,
  el.link_type
FROM Paper p
JOIN AuthorClaim ac ON p.paper_id = ac.paper_id
JOIN EvidenceLink el ON ac.claim_id = el.claim_id
JOIN Observation o ON el.observation_id = o.observation_id
WHERE p.paper_id = 1;
```

### ✅ Hypothesis Grounded in Consensus
```sql
-- Hypothesis MUST reference a Consensus (enforced by FK)
INSERT INTO Hypothesis (
  hypothesis_text,
  derived_from_consensus_id,  -- FK ensures this references a real Consensus
  ...
) VALUES (...);

-- This will fail:
INSERT INTO Hypothesis (..., derived_from_consensus_id = 999, ...)
-- Error: foreign key constraint violated (no Consensus with id=999)
```

### ✅ Versioned Consensus
```sql
-- Original consensus
INSERT INTO Consensus (..., version = 1) VALUES (...);
-- Creates Consensus_Version entry automatically (via trigger or application logic)

-- New evidence arrives; update consensus
UPDATE Consensus SET version = 2, consensus_statement = 'NEW STATEMENT' WHERE consensus_id = 1;
-- Old version preserved in Consensus_Version; new version in Consensus_Version too

-- Query history
SELECT * FROM Consensus_Version WHERE consensus_id = 1 ORDER BY version;
```

---

## Validation Queries

### Ensure no Hypotheses exist without Consensus
```sql
SELECT h.hypothesis_id, h.hypothesis_text
FROM Hypothesis h
LEFT JOIN Consensus c ON h.derived_from_consensus_id = c.consensus_id
WHERE c.consensus_id IS NULL;
-- Should return: 0 rows
```

### Find Observations with no supporting Claims
```sql
SELECT o.observation_id, o.observation_value
FROM Observation o
LEFT JOIN EvidenceLink el ON o.observation_id = el.observation_id
WHERE el.link_id IS NULL;
-- These observations exist but aren't cited by any claim (might be supporting evidence)
```

### Audit: Show all papers in a SearchSession
```sql
SELECT p.title, sp.inclusion_status, sp.reason_for_exclusion
FROM SearchSession s
JOIN SearchSession_Paper sp ON s.search_id = sp.search_id
JOIN Paper p ON sp.paper_id = p.paper_id
WHERE s.search_id = 1;
```

---

## Design Guarantees

| Principle | How Enforced |
|-----------|---------------|
| Observations are atomic | Only one value per Observation record |
| Observations are immutable | No `updated_at`; new records added, never modified |
| Evidence is traceable | `EvidenceLink` explicitly connects Claims to Observations |
| Hypotheses are grounded | FK constraint: `Hypothesis.derived_from_consensus_id` cannot be NULL |
| Consensus is versioned | `Consensus_Version` table preserves all historical versions |
| Controlled vocabulary used | FK constraints enforce valid species, injury models, assays, etc. |
