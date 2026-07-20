# mSCIdblit
**Mouse Science Database for Spinal Cord Injury Research**

A scientifically rigorous, auditable knowledge base for synthesizing spinal cord injury research.

## 🎯 Core Principles

1. **Experiment is the fundamental evidence unit** — not papers, not observations in isolation
2. **Observations are atomic and immutable** — once recorded, evidence cannot be changed
3. **Author claims are separate from observations** — interpretations are distinguished from data
4. **Consensus is derived from multiple independent papers** — never from single sources
5. **Hypotheses are generated only from consensus** — prevents unfounded speculation
6. **Every observation is traceable to source** — figure, table, or results text reference
7. **Controlled vocabulary ensures standardization** — all terms use approved definitions
8. **Curation status is auditable** — extraction passes and curator notes are tracked explicitly

## 📊 Database Overview

| Component | Purpose |
|-----------|---------|
| **10 ControlledVocabulary tables** | Species, injury models, devices, assays, cell types, biomaterials, etc. |
| **Paper** | Bibliographic metadata |
| **ResearchQuestion** | Research objective |
| **ExperimentalParadigm** | Experimental strategy |
| **Experiment** ⭐ | Fundamental evidence unit (control vs. intervention) |
| **Observation** ⭐ | Atomic, immutable empirical findings |
| **AuthorClaim** | Author interpretations |
| **EvidenceLink** | Claim ↔ Observation traceability |
| **Consensus** | Versioned project-level synthesis |
| **Hypothesis** | Generated ideas (from consensus only) |
| **Lineage** | Scientific traditions |
| **SearchSession** | Reproducible search records |
| **CurationPass / Status tables** | Paper and experiment extraction workflow |
| **CuratorNote** | Ambiguities, blockers, vocabulary requests, quality flags |

## 🚀 Quick Start

### Prerequisites
- PostgreSQL 12+
- `psql` command-line client

### Setup

1. **Create database:**
   ```bash
   createdb mscidbl
   ```

2. **Initialize schema:**
   ```bash
   psql -U <username> -d mscidbl -f schema/schema.sql
   ```

3. **Seed controlled vocabulary:**
   ```bash
   psql -U <username> -d mscidbl -f scripts/seed_controlled_vocab.sql
   ```

4. **Verify:**
   ```bash
   psql -U <username> -d mscidbl -c "SELECT table_name FROM information_schema.tables WHERE table_schema='public';"
   ```

5. **Run smoke test (optional but recommended before curation):**
   ```bash
   psql -v ON_ERROR_STOP=1 -U <username> -d mscidbl -f scripts/smoke_test.sql
   ```

## 📁 Repository Structure

```
mSCIdblit/
├── schema/
│   └── schema.sql                    # Complete schema definition
├── docs/
│   ├── SCHEMA_DOCUMENTATION.md       # Detailed entity documentation
│   ├── IMPLEMENTATION_GUIDE.md       # Data entry examples
│   ├── EXPERIMENT_GRANULARITY.md     # Experiment-splitting rules
│   ├── OLLAMA_CHUNK_EXTRACTION.md    # Local model chunking workflow
│   ├── MODULE_1_2_SYNTHESIS.md       # First cross-module lesion/scaffold synthesis
│   ├── AIMS_EVIDENCE_MAP.md          # Specific aims to module evidence map
│   ├── CONSENSUS_REVIEW_REGISTER.md  # Cross-module consensus review register
│   ├── MATERIALIZED_INTEGRITY_AUDIT.md # Generated bundle/SQL integrity audit
│   └── VALIDATION_QUERIES.md         # Database hygiene checks
├── scripts/
│   ├── export_tracker_evidence_bundle.py # Shared 1B/2B tracker audit + JSON export
│   ├── backfill_observation_per_experiment.py # Ensure exact B observations per A experiment
│   ├── audit_materialized_integrity.py # Bundle/SQL integrity gate
│   ├── export_module1_full_sql.py    # Module 1 SQL materialization
│   ├── export_module1_evidence_bundle.py # Module 1 SQL-oriented evidence JSON
│   ├── export_module2_full_sql.py    # Module 2 SQL materialization
│   ├── export_module_full_sql.py     # Generic B-module SQL materialization
│   ├── export_consensus_review_register.py # Cross-module consensus review export
│   ├── ollama_chunk_extract.py       # Generate small Ollama extraction prompts
│   ├── seed_controlled_vocab.sql     # Populate reference tables
│   └── smoke_test.sql                # Toy workflow validation script
├── templates/
│   ├── paper_extraction_template.md
│   ├── experiment_extraction_template.md
│   ├── observation_extraction_template.md
│   ├── claim_extraction_template.md
│   └── controlled_vocab_request_template.md
├── modules/
│   ├── ROADMAP.md                    # Saturation and consolidation module map
│   ├── Module_1A_TRACKER.md          # Chronic SCI lesion architecture tracker
│   ├── Module_1B_TRACKER.md          # Lesion architecture evidence consolidation
│   ├── Module_2A_TRACKER.md          # Biomaterials and scaffold repair tracker
│   ├── Module_2B_TRACKER.md          # Biomaterials evidence consolidation
│   ├── Module_3A_TRACKER.md          # Immune and myeloid modulation tracker
│   ├── Module_3B_TRACKER.md          # Immune/myeloid evidence consolidation
│   ├── Module_4A_TRACKER.md          # Cell transplantation and graft integration tracker
│   ├── Module_4B_TRACKER.md          # Cell transplantation evidence consolidation
│   ├── Module_5A_TRACKER.md          # Axon regeneration, remyelination, and white matter repair tracker
│   ├── Module_5B_TRACKER.md          # Axon/white matter evidence consolidation
│   ├── Module_6A_TRACKER.md          # Human chronic SCI pathology and translational imaging tracker
│   ├── Module_6B_TRACKER.md          # Human pathology/imaging evidence consolidation
│   ├── Module_7A_TRACKER.md          # Host fibroinflammatory conditioning tracker
│   ├── Module_7B_TRACKER.md          # Host-conditioning evidence consolidation
│   ├── Module_8A_TRACKER.md          # In vivo SCI model systems tracker
│   ├── Module_8B_TRACKER.md          # In vivo SCI model-system evidence consolidation
│   ├── Module_9A_TRACKER.md          # In vitro/ex vivo SCI model systems tracker
│   ├── Module_9B_TRACKER.md          # In vitro/ex vivo SCI model-system evidence consolidation
│   ├── Module_10A_TRACKER.md         # SCI clinical trials tracker
│   ├── Module_10B_TRACKER.md         # SCI clinical trials evidence consolidation
│   ├── Module_11A_TRACKER.md         # Spinal cord ischemic conditioning in cardiac/aortic surgery tracker
│   ├── Module_11B_TRACKER.md         # Spinal cord ischemic conditioning evidence consolidation
│   ├── Module_12A_TRACKER.md         # LPS and innate immune preconditioning tracker
│   └── Module_12B_TRACKER.md         # LPS/innate preconditioning evidence consolidation
├── CONTRIBUTING.md                    # Scientific curation protocol
└── README.md                          # This file
```

## 🔑 Key Features

### 1. Immutable Evidence
```sql
-- Observations are never updated; corrections are new records
INSERT INTO Observation (...) VALUES (...);  -- Original
INSERT INTO Observation (..., notes = 'Correction to previous entry') 
VALUES (...);  -- Correction (old record remains)
-- UPDATE/DELETE are blocked by database triggers
```

### 2. Traceability: Claims → Observations
```sql
-- Every author claim links to supporting observations
SELECT 
  ac.claim_text,
  o.observation_value,
  el.link_type
FROM AuthorClaim ac
JOIN EvidenceLink el ON ac.claim_id = el.claim_id
JOIN Observation o ON el.observation_id = o.observation_id;
```

### 3. Consensus is Versioned
```sql
-- Consensus evolves; version history is preserved
SELECT statement_text, version_number
FROM Consensus_Version 
WHERE consensus_id = 1 
ORDER BY version_number;
```

### 4. Hypotheses Grounded in Consensus
```sql
-- FK constraint ensures hypotheses reference a consensus
INSERT INTO Hypothesis (derived_from_consensus_id = ?, ...) 
VALUES (...);
-- Error if consensus_id doesn't exist
```

### 5. Structured Experiments
```sql
-- One experiment = control + intervention + outcomes
INSERT INTO Experiment (
  control_type = 'sham surgery',
  intervention_type = 'cell transplant',
  ...
);
INSERT INTO Experiment_Species VALUES (experiment_id, species_id);
INSERT INTO Experiment_InjuryModel VALUES (experiment_id, model_id);
INSERT INTO Experiment_Assay VALUES (experiment_id, assay_id);
```

## 📖 Example: Data Entry Workflow

### Paper: "BDNF-expressing macrophages promote recovery after SCI"

**Step 1**: Insert Paper
```sql
INSERT INTO Paper (title, authors, publication_year, journal, doi)
VALUES ('BDNF-expressing macrophages...', 'Smith J, et al', 2023, 'Nature Neuroscience', '10.1038/...');
```

**Step 2**: Record Research Question
```sql
INSERT INTO ResearchQuestion (paper_id, question_text, hypothesis_direction)
VALUES (1, 'Does BDNF in macrophages promote recovery?', 'positive');
```

**Step 3**: Define Experimental Paradigm
```sql
INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description)
VALUES (1, 'Genetic macrophage targeting', 'Using Ccl2-Cre to label macrophages...');
```

**Step 4**: Populate Controlled Vocabulary
```sql
INSERT INTO ControlledVocabulary_Species (species_name, ncbi_taxonomy_id)
VALUES ('Mus musculus', '10090') ON CONFLICT DO NOTHING;

INSERT INTO ControlledVocabulary_InjuryModel (model_name, anatomical_target)
VALUES ('T10 contusion', 'T10') ON CONFLICT DO NOTHING;

INSERT INTO ControlledVocabulary_Assay (assay_name, assay_type)
VALUES ('Basso Mouse Scale', 'behavioral') ON CONFLICT DO NOTHING;
-- ... etc for all reference data
```

**Step 5**: Create Experiment
```sql
INSERT INTO Experiment (
  paper_id, paradigm_id, figure_table_reference, control_type, intervention_type
) VALUES (1, 1, 'Fig 3A', 'WT littermates', 'BDNF knockout macrophages');

INSERT INTO Experiment_Species VALUES (experiment_id, species_id);
INSERT INTO Experiment_InjuryModel VALUES (experiment_id, injury_model_id);
INSERT INTO Experiment_Assay VALUES (experiment_id, assay_id);
```

**Step 6**: Record Observations (Immutable)
```sql
INSERT INTO Observation (
  experiment_id, evidence_type_id, outcome_type_id,
  observation_value, unit, p_value, n_subjects, timepoint_postinjury_days
) VALUES (1, 3, 5, '16.2', 'BMS score', NULL, 12, 28);  -- WT control

INSERT INTO Observation (
  experiment_id, evidence_type_id, outcome_type_id,
  observation_value, unit, p_value, n_subjects, timepoint_postinjury_days
) VALUES (1, 3, 5, '10.5', 'BMS score', 0.012, 12, 28);  -- BDNF KO
```

**Step 7**: Extract Author Claims
```sql
INSERT INTO AuthorClaim (paper_id, claim_text, claim_type, confidence_level)
VALUES 
  (1, 'BDNF in macrophages is necessary for recovery', 'conclusion', 'high'),
  (1, 'BDNF promotes axonal regeneration', 'interpretation', 'medium');
```

**Step 8**: Link Claims to Evidence
```sql
INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
VALUES (1, 2, 'directly_supports', 'KO shows reduced recovery vs WT');
```

**Step 9**: Create Consensus (after multiple papers reviewed)
```sql
INSERT INTO Consensus (
  consensus_statement, topic, version, agreement_level,
  num_supporting_papers, num_contradicting_papers
) VALUES (
  'BDNF from macrophages promotes recovery in acute-subacute SCI',
  'Macrophage BDNF',
  1,
  'moderate',
  8, 1
);
```

**Step 10**: Generate Hypothesis from Consensus
```sql
INSERT INTO Hypothesis (
  hypothesis_text, derived_from_consensus_id,
  hypothesis_type, testability_level, proposed_experiment
) VALUES (
  'IL-10 signaling controls BDNF production in SCI macrophages',
  1,
  'mechanistic',
  'directly_testable',
  'Isolate macrophages from IL-10 KO mice...'
);
```

---

## 📚 Documentation

- **[SCHEMA_DOCUMENTATION.md](docs/SCHEMA_DOCUMENTATION.md)** — Entity definitions, relationships, design rationale
- **[IMPLEMENTATION_GUIDE.md](docs/IMPLEMENTATION_GUIDE.md)** — Step-by-step data entry with examples
- **[EXPERIMENT_GRANULARITY.md](docs/EXPERIMENT_GRANULARITY.md)** — Rules for splitting studies into experiments and observations
- **[VALIDATION_QUERIES.md](docs/VALIDATION_QUERIES.md)** — Quality-control checks after curation batches
- **[CONTRIBUTING.md](CONTRIBUTING.md)** — Scientific curation protocol

## 🔍 Key Queries

### Trace a Claim to All Supporting Observations
```sql
SELECT o.observation_value, o.unit, el.link_type
FROM AuthorClaim ac
JOIN EvidenceLink el ON ac.claim_id = el.claim_id
JOIN Observation o ON el.observation_id = o.observation_id
WHERE ac.claim_id = ?;
```

### Find All Experiments Using a Specific Injury Model
```sql
SELECT DISTINCT p.title, e.experiment_number
FROM Experiment e
JOIN Experiment_InjuryModel eim ON e.experiment_id = eim.experiment_id
JOIN ControlledVocabulary_InjuryModel im ON eim.injury_model_id = im.injury_model_id
JOIN Paper p ON e.paper_id = p.paper_id
WHERE im.model_name = 'T10 contusion';
```

### Show Consensus Supporting Profile
```sql
SELECT 
  c.consensus_statement,
  COUNT(DISTINCT CASE WHEN co.support_type = 'supporting' THEN co.observation_id END) as supporting,
  COUNT(DISTINCT CASE WHEN co.support_type = 'contradicting' THEN co.observation_id END) as contradicting
FROM Consensus c
LEFT JOIN Consensus_Observation co ON c.consensus_id = co.consensus_id
WHERE c.topic = 'Macrophage BDNF'
GROUP BY c.consensus_id;
```

### List Testable Hypotheses
```sql
SELECT h.hypothesis_text, h.proposed_experiment, c.agreement_level
FROM Hypothesis h
JOIN Consensus c ON h.derived_from_consensus_id = c.consensus_id
WHERE h.testability_level = 'directly_testable'
AND c.agreement_level IN ('strong', 'moderate');
```

---

## 🛠️ Design Constraints

| Constraint | Enforcement |
|-----------|--------------|
| Observations are immutable | No `updated_at`; UPDATE/DELETE blocked by trigger |
| Observations are atomic | Single value per Observation record |
| Source provenance is preserved | Source section, quote, page, figure/panel fields on evidence tables |
| Hypotheses require consensus | FK: `hypothesis.derived_from_consensus_id` NOT NULL |
| Claims require evidence | Via `EvidenceLink` (no orphaned claims) |
| Controlled vocabulary standardization | FK constraints on species, injury models, assays, etc. |
| Consensus is versioned | Trigger writes `Consensus_Version` history |
| Curation progress is auditable | `CurationPass`, status tables, and `CuratorNote` |

---

## 🔮 Future Enhancements

- [ ] Full-text search on abstracts and claims
- [ ] Conflict detection (contradictory findings)
- [ ] Data quality scoring
- [ ] Collaborative team curation
- [ ] Knowledge graph export (RDF, Neo4j)
- [ ] Hypothesis tracking (which were tested?)
- [ ] GraphQL API layer
- [ ] Web UI for data entry

---

## 📧 Support

For questions, issues, or contributions, open a GitHub issue or discussion in this repository.

---

**Status**: Active Development  
**Last Updated**: 2026-07-15

**Version**: 2.1 (Curation Workflow + Enforced Immutability)
