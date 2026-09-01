# mSCIdblit
**Mouse Science Database for Spinal Cord Injury Research**

A scientifically rigorous, auditable knowledge base for synthesizing spinal cord injury research.

## Module Narrative Order

Module numbers are stable identifiers, not the recommended reading order. For presentations and synthesis, use: model systems (Module 8), traumatic SCI-to-chronic-lesion pathobiology (Module 13), chronic lesion architecture (Module 1), human pathology/imaging (Module 6), immune/myeloid modulation (Module 3), TLR signaling cascade architecture (Module 17), non-TLR DAMP sensing (Module 18), histone modification and chromatin-state regulation (Module 19), innate immune conditioning/tolerance (Module 12), ischemic-conditioning comparators (Module 11), host fibroinflammatory conditioning (Module 7), peripheral nerve and DRG priming of CNS repair (Module 15), PNS electrical stimulation preconditioning (Module 16), in vitro/ex vivo validation systems (Module 9), biomaterials/scaffolds (Module 2), cell transplantation (Module 4), axon/remyelination/white matter repair (Module 5), CRISPR epigenome editing for neuroregeneration (Module 14), and clinical trials (Module 10).

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

The additive `EvidenceSourceRecord` and `ModuleEvidenceLink` layer connects
external modality evidence—such as mSCS protein, spatial, and epigenetic
records—to modules, pathways, entities, or existing edges without flattening
source measurements or changing graph semantics. See
[`docs/MODULE_EVIDENCE_CROSSWALK.md`](/Users/derea/Documents/SCI/mSCIdblit/docs/MODULE_EVIDENCE_CROSSWALK.md).
The linked `EvidenceObservationDetail` layer preserves queryable reported and
transcribed values while retaining the native mSCS row snapshot and source
artifact hash.

## mSCS method-resource intake

The frozen LIANA, CellChatDB, and NicheNet resources used by mSCS can be
imported into an additive mSCIdblit method-resource layer. This preserves one
canonical communication identity while retaining exact native fields,
complex components, pathway/cofactor annotations, NicheNet ligand-target
matrix metadata, source checksums, and method-specific projections. Method
resource membership is not biological validation and does not create mechanism
edges. See
[`docs/METHOD_RESOURCE_MIGRATION.md`](/Users/derea/Documents/SCI/mSCIdblit/docs/METHOD_RESOURCE_MIGRATION.md).

Apply the layer after the base schema when loading the generated intake SQL:

```bash
psql -U <username> -d mscidbl -f schema/method_resource_layer.sql
python3 scripts/import_method_resources.py
psql -U <username> -d mscidbl -f data/processed/method_resource_migration_v1/method_resource_materialization.sql
psql -U <username> -d mscidbl -f scripts/validate_method_resource_layer.sql
python3 scripts/benchmark_method_resource_equivalence.py
python3 scripts/build_mscs_release_bundle.py
```

## Public TF/regulon evidence staging

The public TF/regulon expansion is maintained as a separate, additive staging
layer under
`data/processed/public_tf_union_expansion_v1/comprehensive_interaction_promotion_v1/module_integration_staging_v1/`.
It is provenance-aware and review-only: it does not write canonical TF,
regulon, Module 22B, mechanism-edge, or module-tracker records.

The evidence-strength axis is preserved as A/B/C/D/E, independently from the
graded context axis: L0 no context evidence, L1 non-CNS, L2 CNS, L3 spinal-cord
tissue, and L4 spinal-cord-injury context. Component context never upgrades an
exact regulator-target pair. The latest C-tier pass covers 3,004 unique
regulator-target-species relationships: 2,459 module-routed and 545
catalog-only. All retain `C_tflink_source_table_only`; 2,989 are explicitly
resolved as context-unverifiable at L0 for the current evidence packet, while
15 retain source-backed component-context overlays. All 15 exact pairs remain
L0; component context is recorded independently.

Resume from these artifacts:

- [`context_evidence_adjudications.tsv`](/Users/derea/Documents/SCI/mSCIdblit/data/processed/public_tf_union_expansion_v1/comprehensive_interaction_promotion_v1/module_integration_staging_v1/context_evidence_adjudications.tsv) — one context adjudication per promotion record.
- [`c_tier_context_review_queue.tsv`](/Users/derea/Documents/SCI/mSCIdblit/data/processed/public_tf_union_expansion_v1/comprehensive_interaction_promotion_v1/module_integration_staging_v1/c_tier_context_review_queue.tsv) — all C relationships, deduplicated by regulator-target-species.
- [`c_tier_context_search_round_001.tsv`](/Users/derea/Documents/SCI/mSCIdblit/data/processed/public_tf_union_expansion_v1/comprehensive_interaction_promotion_v1/module_integration_staging_v1/c_tier_context_search_round_001.tsv), [`c_tier_context_search_round_002.tsv`](/Users/derea/Documents/SCI/mSCIdblit/data/processed/public_tf_union_expansion_v1/comprehensive_interaction_promotion_v1/module_integration_staging_v1/c_tier_context_search_round_002.tsv), [`c_tier_context_search_round_003.tsv`](/Users/derea/Documents/SCI/mSCIdblit/data/processed/public_tf_union_expansion_v1/comprehensive_interaction_promotion_v1/module_integration_staging_v1/c_tier_context_search_round_003.tsv), and [`c_tier_context_search_round_004.tsv`](/Users/derea/Documents/SCI/mSCIdblit/data/processed/public_tf_union_expansion_v1/comprehensive_interaction_promotion_v1/module_integration_staging_v1/c_tier_context_search_round_004.tsv) — targeted search ledgers with upgrade and no-upgrade decisions.
- [`docs/PUBLIC_TF_EVIDENCE_HANDOFF_2026-08-28.md`](/Users/derea/Documents/SCI/mSCIdblit/docs/PUBLIC_TF_EVIDENCE_HANDOFF_2026-08-28.md) — detailed counts, safeguards, and continuation instructions.

Re-run the public-TF screening and queue builders only after changing the
source or adjudication inputs:

```bash
python3 scripts/build_public_tf_context_adjudications.py
python3 scripts/screen_public_tf_module_integration.py
python3 scripts/build_public_tf_c_context_review_queue.py
```

Do not infer context from a TFLink citation or gene identity, and do not
materialize or commit/push this staging work without an explicit review step.

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
   psql -U <username> -d mscidbl -f schema/module_evidence_crosswalk.sql
   psql -U <username> -d mscidbl -f schema/evidence_observation_detail.sql
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
   psql -v ON_ERROR_STOP=1 -U <username> -d mscidbl -f scripts/validate_module_evidence_crosswalk.sql
   ```

## 📁 Repository Structure

```
mSCIdblit/
├── schema/
│   ├── schema.sql                    # Complete schema definition
│   ├── module_evidence_crosswalk.sql # External evidence ↔ module/edge bridge
│   ├── evidence_observation_detail.sql # Queryable external measurements
│   └── method_resource_layer.sql     # Canonical method-resource intake layer
├── docs/
│   ├── SCHEMA_DOCUMENTATION.md       # Detailed entity documentation
│   ├── IMPLEMENTATION_GUIDE.md       # Data entry examples
│   ├── EXPERIMENT_GRANULARITY.md     # Experiment-splitting rules
│   ├── OLLAMA_CHUNK_EXTRACTION.md    # Local model chunking workflow
│   ├── MODULE_1_2_SYNTHESIS.md       # First cross-module lesion/scaffold synthesis
│   ├── CROSS_MODULE_SYNTHESIS.md     # Aim-aligned synthesis across Modules 1B-16B
│   ├── AIMS_EVIDENCE_MAP.md          # Specific aims to module evidence map
│   ├── CONSENSUS_REVIEW_REGISTER.md  # Cross-module consensus review register
│   ├── MATERIALIZED_INTEGRITY_AUDIT.md # Generated bundle/SQL integrity audit
│   ├── MODULE_17_TLR_SIGNALING.md    # TLR pathway graph queries and interpretation rules
│   ├── MODULE_18_NON_TLR_DAMPS.md    # Non-TLR DAMP pathway graph queries and interpretation rules
│   ├── MODULE_19_HISTONE_MODIFICATION.md # Histone-modification graph queries and interpretation rules
│   ├── MECHANISM_BUNDLE_EXPORT.md    # Export curated signaling graph bundles for mSCS
│   ├── METHOD_RESOURCE_MIGRATION.md  # Frozen method-resource intake and equivalence contract
│   ├── MODULE20_24_MECHANISM_GRAPH_RELEASE.md # Evidence-gated Module 20B–24B graph release
│   ├── MODULE_EVIDENCE_CROSSWALK.md  # Cross-cutting modality evidence bridge
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
│   ├── export_cross_module_synthesis.py # Aim-aligned synthesis export
│   ├── export_mechanism_bundle.py    # Export mSCS-compatible mechanism bundle snapshots
│   ├── import_method_resources.py    # Import frozen LIANA/CellChat/NicheNet resources
│   ├── benchmark_method_resource_equivalence.py # Resource-level equivalence benchmark
│   ├── build_mscs_release_bundle.py  # Combine graph and method-resource release layers
│   ├── validate_mscs_release_bundle.py # Check combined release checksums and contents
│   ├── import_mscs_modality_evidence.py # Build mSCS evidence bridge materialization
│   ├── ollama_chunk_extract.py       # Generate small Ollama extraction prompts
│   ├── seed_controlled_vocab.sql     # Populate reference tables
│   ├── validate_module_evidence_crosswalk.sql # Crosswalk integrity gate
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
│   ├── Module_12A_TRACKER.md         # Innate immune conditioning and tolerance tracker
│   ├── Module_12B_TRACKER.md         # Innate conditioning evidence consolidation
│   ├── Module_13A_TRACKER.md         # Traumatic SCI pathobiology and chronic lesion formation tracker
│   ├── Module_13B_TRACKER.md         # Traumatic SCI pathobiology evidence consolidation
│   ├── Module_14A_TRACKER.md         # CRISPR epigenome editing for neuroregeneration tracker
│   ├── Module_14B_TRACKER.md         # CRISPR epigenome editing evidence consolidation
│   ├── Module_15A_TRACKER.md         # Peripheral nerve and DRG priming of CNS repair tracker
│   ├── Module_15B_TRACKER.md         # Peripheral nerve and DRG priming evidence consolidation
│   ├── Module_16A_TRACKER.md         # PNS electrical stimulation preconditioning tracker
│   ├── Module_16B_TRACKER.md         # PNS electrical stimulation preconditioning evidence consolidation
│   ├── Module_17A_TRACKER.md         # TLR signaling cascade and innate receptor pathway architecture tracker
│   ├── Module_17B_TRACKER.md         # TLR signaling graph evidence consolidation
│   ├── Module_18A_TRACKER.md         # Non-TLR DAMP sensing and downstream danger signaling tracker
│   ├── Module_18B_TRACKER.md         # Non-TLR DAMP evidence consolidation
│   ├── Module_19A_TRACKER.md         # Histone modification and chromatin-state regulation tracker
│   └── Module_19B_TRACKER.md         # Histone modification evidence consolidation
├── CONTRIBUTING.md                    # Scientific curation protocol
└── README.md                          # This file
```

## 🔑 Key Features

### Mechanism Export to `mSCS`

Curated signaling pathway rows should move into the simulator through an explicit bundle export, not through ad hoc SQL in `mSCS`.

```bash
python3 /Users/derea/Documents/SCI/mSCIdblit/scripts/export_mechanism_bundle.py \
  --database-url "$MSCIDBLIT_DATABASE_URL" \
  --output-dir /Users/derea/Documents/SCI/mSCIdblit/data/processed/mechanism_bundle_strict_mouse \
  --species-support mouse \
  --species-support both \
  --cell-type-context astrocytes \
  --min-export-priority medium \
  --require-sources \
  --bundle-name astro_strict_mouse_v1
```

That export produces the exact three-file contract that `mSCS` imports:

- `mechanism_nodes.tsv`
- `mechanism_edges.tsv`
- `mechanism_edge_sources.tsv`

See [`docs/MECHANISM_BUNDLE_EXPORT.md`](/Users/derea/Documents/SCI/mSCIdblit/docs/MECHANISM_BUNDLE_EXPORT.md) for the full filter and provenance rules.

For the register-backed Module 20B–24B release snapshot, see
[`docs/MODULE20_24_MECHANISM_GRAPH_RELEASE.md`](/Users/derea/Documents/SCI/mSCIdblit/docs/MODULE20_24_MECHANISM_GRAPH_RELEASE.md).
It includes evidence-gated graph edges, source provenance, pathway summaries,
boundary summaries, and a deterministic integrity validator.

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
- **[MODULE20A_HANDOFF_2026-08-07.md](docs/MODULE20A_HANDOFF_2026-08-07.md)** — Current Module 20A curation state and resume instructions
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
