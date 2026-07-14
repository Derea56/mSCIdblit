# SCI Knowledge Base Schema v2 — Design Documentation

## Design Philosophy

This schema embodies strict scientific principles:

1. **Experiment is the fundamental evidence unit** — Experiments (not papers) are the atomic entities around which all other data organizes
2. **Observations are atomic and immutable** — Once recorded, observations cannot be modified or deleted (only new ones added)
3. **Author claims are separate from observations** — Interpretations and claims are stored distinctly from raw empirical findings
4. **Consensus is derived from multiple independent papers** — Never from single sources
5. **Hypotheses are generated only from consensus** — New ideas emerge from synthesized knowledge, not speculation
6. **Every observation is traceable to a source** — Figure, table, or explicit results text reference
7. **Controlled vocabulary ensures standardization** — Terms like injury models, assays, cell types use standardized definitions

---

## Entity Definitions

### **ControlledVocabulary Tables** (Reference Data)

These tables define standardized terms used across the database:

| Table | Purpose | Examples |
|-------|---------|----------|
| `ControlledVocabulary_Species` | Animal model organisms | Mus musculus, Rattus norvegicus |
| `ControlledVocabulary_InjuryModel` | Spinal cord injury type | T9 contusion, L4 transection, C4 lateral hemisection |
| `ControlledVocabulary_InjuryDevice` | Equipment for inducing injury | NYU impactor, Allen weight drop, surgical transection |
| `ControlledVocabulary_LesionCompartment` | Anatomical location of damage | White matter, gray matter, dorsal horn |
| `ControlledVocabulary_EvidenceType` | Type of empirical evidence | "behavioral measurement", "histological assessment", "electrophysiological recording" |
| `ControlledVocabulary_OutcomeType` | Measured outcome | "locomotor recovery", "neuropathic pain", "tissue sparing" |
| `ControlledVocabulary_CellType` | Normalized cell types | Astrocytes, oligodendrocytes, macrophages |
| `ControlledVocabulary_Biomaterial` | Therapeutic materials | Poly(lactic-co-glycolic acid), collagen scaffold, neural progenitor cells |
| `ControlledVocabulary_SurgicalProcedure` | Surgical interventions | Laminectomy, dura mater opening, cell transplantation |
| `ControlledVocabulary_Assay` | Measurement techniques | BMS (Basso Mouse Scale), immunohistochemistry, electrophysiology |

---

## Core Entities

### **Paper**
Bibliographic metadata only. No interpretation stored here.

```sql
paper_id (PK)
title
authors
publication_year
journal, volume, issue, pages
doi, pmid (unique external identifiers)
abstract
url
created_at, updated_at
```

**Key Principle**: Papers are containers; the real science happens in Experiments → Observations.

---

### **ResearchQuestion**
The biological question investigated by a paper.

```sql
question_id (PK)
paper_id (FK)
question_text — the explicit question posed
hypothesis_direction — 'positive' (confirm), 'negative' (disprove), 'exploratory'
keywords
```

**Example**: "Does oligodendrocyte progenitor cell transplantation promote axonal regeneration after spinal cord contusion?"

---

### **ExperimentalParadigm**
The overall experimental strategy or methodology type.

```sql
paradigm_id (PK)
paper_id (FK)
paradigm_name — e.g., "Cell transplantation with behavioral tracking"
description
methodology — specific techniques
```

**Why separate?** A single paper may use multiple paradigms (e.g., behavioral testing + histology).

---

### **Experiment** ⭐ THE FUNDAMENTAL EVIDENCE UNIT

A single experimental comparison. This is where the science lives.

```sql
experiment_id (PK)
paper_id (FK)
paradigm_id (FK)
experiment_number — sequential (Exp 1, 2, 3...)
figure_table_reference — e.g., "Fig 3A", "Table 2"
figure_panel_reference — e.g., "panel A"
title
description
sample_size — n
control_type — e.g., 'sham surgery', 'vehicle injection'
intervention_type — e.g., 'cell transplant', 'drug treatment'
duration_days — how long was intervention active?
timepoint_postinjury_days — when was this measured relative to injury?
notes
created_at (immutable)
```

**Critical Design**: Each Experiment has:
- One control condition
- One intervention condition
- Multiple Observations (different outcome measures)

**Example**:
- Control: Sham-operated mice
- Intervention: OPC transplantation at 7 days post-T9 contusion
- Observations: BMS score at 1 week, histological lesion size, axon density

---

### **Observation** ⭐ ATOMIC, IMMUTABLE EVIDENCE

The smallest unit of empirical data. Once recorded, never changed.

```sql
observation_id (PK)
experiment_id (FK)
evidence_type_id (FK) — references ControlledVocabulary_EvidenceType
outcome_type_id (FK) — references ControlledVocabulary_OutcomeType
observation_value — THE EXACT VALUE as stated/measured
unit — measurement unit
standard_error
confidence_interval_lower, confidence_interval_upper
p_value
effect_size
n_subjects
measurement_method — HOW was this measured?
timepoint_postinjury_days — if different from experiment
notes — contextual notes (NEVER inferred)
created_at (immutable)
```

**IMMUTABILITY GUARANTEE**:
- `created_at` is set once, never updated
- No `updated_at` column (observations don't change)
- If an observation is wrong, a new (corrected) observation is recorded with notes

**Example Observation**:
- Experiment: OPC transplant at T9 contusion
- Evidence Type: "behavioral measurement"
- Outcome Type: "locomotor recovery"
- Value: "6.5"
- Unit: "BMS score"
- Timepoint: "28 days post-injury"
- n_subjects: 12
- Notes: "Mean of 3 trials per animal"

---

### **AuthorClaim**
Explicit or implicit interpretations proposed by the authors.

```sql
claim_id (PK)
paper_id (FK)
claim_text — the full claim
claim_type — 'interpretation', 'conclusion', 'speculation', 'mechanistic', 'implication'
confidence_level — 'high', 'medium', 'low', 'speculative'
notes
created_at, updated_at
```

**CRITICAL**: This table stores what the authors *say*, not what the data *show*. Authors make claims; the Observation table holds the data. The `EvidenceLink` table connects them.

**Example**:
- Claim Text: "OPC transplantation promotes axonal regeneration and functional recovery in chronic SCI"
- Type: "conclusion"
- Confidence: "high"

---

### **EvidenceLink**
Explicit many-to-many mapping between claims and observations. This is how we ensure traceability.

```sql
link_id (PK)
claim_id (FK)
observation_id (FK)
link_type — 'directly_supports', 'indirectly_supports', 'contradicts', 'partially_supports'
notes — why this link matters
created_at
UNIQUE(claim_id, observation_id) — prevent duplicates
```

**Example**:
- Claim: "OPC transplantation promotes axonal regeneration"
- Link Type: "directly_supports"
- Observation: "6.5 BMS score in transplanted group vs 3.2 in sham (p=0.01)"

---

### **BiologicalEntity**
Normalized registry of genes, proteins, cell types, cytokines, biomaterials, and anatomical structures.

```sql
entity_id (PK)
entity_name — UNIQUE, canonical name
entity_type — 'protein', 'gene', 'cell_type', 'cytokine', 'biomaterial', 'anatomical_structure'
ncbi_gene_id, uniprot_id — external database links
cell_type_id (FK) — link to ControlledVocabulary_CellType if applicable
synonyms
description
```

**Why?** Enables queries like "find all papers studying BDNF" across papers that may use different nomenclature.

---

### **Experiment_BiologicalEntity** (Many-to-Many)
Maps biological entities to experiments.

```sql
experiment_id (FK)
entity_id (FK)
entity_role — 'target', 'intervention', 'measurement', 'confound'
```

---

### **Experiment_[ControlledVocab]** (Many-to-Many)
These junction tables connect experiments to controlled vocabulary terms:

- `Experiment_InjuryModel` — which injury model?
- `Experiment_InjuryDevice` — what device was used?
- `Experiment_Species` — which animal?
- `Experiment_LesionCompartment` — where is the lesion?
- `Experiment_Assay` — which outcome measures?
- `Experiment_Biomaterial` — which therapeutic material (if any)?
- `Experiment_SurgicalProcedure` — which procedures?

This enables structured queries: "Find all experiments using OPC transplantation in rats post-T9 contusion"

---

### **Versioned Interpretation: Consensus**

### **Consensus**
Project-level synthesis derived *only* from multiple independent papers.

```sql
consensus_id (PK)
consensus_statement — the synthesized claim
topic — e.g., "OPC transplantation efficacy"
version — current version number
agreement_level — 'strong', 'moderate', 'weak', 'emerging', or percentage
num_supporting_papers
num_contradicting_papers
synthesis_date
created_at, updated_at
notes
```

**CRITICAL PRINCIPLE**: A consensus can be updated (version incremented) as new evidence arrives, but the version history is preserved.

**Example**:
- Version 1: "Limited evidence suggests OPC transplantation may improve recovery"
- Version 2 (updated): "Moderate consensus that OPC transplantation promotes regeneration in acute-chronic window"

---

### **Consensus_Version**
Immutable record of all consensus versions.

```sql
version_id (PK)
consensus_id (FK)
version_number
statement_text
agreement_level
summary_of_changes — what changed from previous version?
created_at
```

This table ensures every iteration of the consensus is auditable.

---

### **Consensus_Observation**
Maps observations to consensus statements (derived relationship).

```sql
consensus_id (FK)
observation_id (FK)
support_type — 'supporting', 'contradicting'
```

**Note**: This is *derived* data. The primary evidence relationship is `EvidenceLink` (Claim ← Observation). Consensus adds a project-level aggregation layer.

---

### **Hypothesis**

Testable ideas generated *only* from consensus statements.

```sql
hypothesis_id (PK)
hypothesis_text
derived_from_consensus_id (FK) — MUST reference a Consensus
hypothesis_type — 'mechanistic', 'therapeutic', 'predictive'
testability_level — 'directly_testable', 'partially_testable', 'speculative'
biological_entities — JSON array of entity_ids involved
predicted_outcome
proposed_experiment — suggested experimental design
confidence_level
created_at, updated_at
```

**CRITICAL**: Hypotheses are *generated* from consensus, not speculation. The FK ensures this constraint.

**Example**:
- Consensus: "BDNF signaling in macrophages is critical for SCI recovery"
- Hypothesis: "Conditional deletion of BDNF in macrophages will impair recovery in T10 contusion model"
- Proposed Experiment: "Perform T10 SCI in Ccl2-Cre; BDNF^fl/fl mice and wild-type littermates; assess BMS and tissue sparing"

---

### **Lineage**

Scientific traditions linking anchor papers and evolving conceptual frameworks.

```sql
lineage_id (PK)
lineage_name — e.g., "Macrophage polarization in SCI"
lineage_description
anchor_paper_id (FK) — foundational paper
key_concepts
domain — 'regeneration', 'inflammation', 'plasticity', 'neuroprotection'
```

---

### **SearchSession**

Reproducible, auditable literature search record.

```sql
search_id (PK)
search_query
search_strategy — detailed description
database_source — 'PubMed', 'Google Scholar', 'bioRxiv'
search_date
filters — JSON (keywords, date range, inclusion/exclusion)
papers_retrieved
papers_reviewed
papers_included_count
inclusion_criteria
exclusion_criteria
notes
```

**Why?** Enables replication of literature searches and transparent methodology for future reviewers.

---

## Data Integrity Constraints

1. **Observations are immutable**: No `updated_at` column; immutability enforced by application logic.
2. **Hypotheses require consensus**: FK constraint `hypothesis.derived_from_consensus_id` ensures hypotheses cannot exist in isolation.
3. **Consensus is versioned**: New versions are recorded; old versions remain in `Consensus_Version`.
4. **EvidenceLink prevents duplicates**: UNIQUE constraint on `(claim_id, observation_id)`.

---

## Key Query Patterns

### Trace a Claim to Supporting Observations
```sql
SELECT o.observation_id, o.observation_value, o.unit, el.link_type
FROM AuthorClaim ac
JOIN EvidenceLink el ON ac.claim_id = el.claim_id
JOIN Observation o ON el.observation_id = o.observation_id
WHERE ac.claim_id = ?;
```

### Find All Experiments Using a Specific Biomaterial
```sql
SELECT DISTINCT p.title, e.experiment_number, e.intervention_type
FROM Experiment e
JOIN Experiment_Biomaterial eb ON e.experiment_id = eb.experiment_id
JOIN ControlledVocabulary_Biomaterial b ON eb.biomaterial_id = b.biomaterial_id
JOIN Paper p ON e.paper_id = p.paper_id
WHERE b.biomaterial_name = 'Poly(lactic-co-glycolic acid)';
```

### Build a Consensus Supporting Profile
```sql
SELECT 
  c.consensus_statement,
  COUNT(DISTINCT co_sup.observation_id) as supporting_obs,
  COUNT(DISTINCT co_con.observation_id) as contradicting_obs
FROM Consensus c
LEFT JOIN Consensus_Observation co_sup ON c.consensus_id = co_sup.consensus_id AND co_sup.support_type = 'supporting'
LEFT JOIN Consensus_Observation co_con ON c.consensus_id = co_con.consensus_id AND co_con.support_type = 'contradicting'
WHERE c.topic = 'OPC transplantation'
GROUP BY c.consensus_id, c.consensus_statement;
```

### Find Hypotheses Ready for Testing
```sql
SELECT h.hypothesis_text, h.proposed_experiment, c.agreement_level
FROM Hypothesis h
JOIN Consensus c ON h.derived_from_consensus_id = c.consensus_id
WHERE h.testability_level = 'directly_testable'
AND c.agreement_level IN ('strong', 'moderate');
```

---

## Rationale for Design Choices

### Why separate Experiment and Observation?
- **Experiment** = experimental design (control vs intervention)
- **Observation** = measured outcomes
- One experiment typically produces multiple observations (different outcome measures)

### Why immutable Observations?
- Scientific integrity: evidence is never altered
- Audit trail: if data is corrected, new records are added, old ones remain

### Why separate AuthorClaim from Observation?
- **Observation** = what the data show
- **AuthorClaim** = what the authors interpret
- Authors often overstate or understate findings; separating allows critical evaluation

### Why versioned Consensus?
- Science evolves; consensus changes
- But version history is preserved for transparency
- New papers → Consensus updated → Version incremented

### Why Hypotheses from Consensus only?
- Prevents unconstrained speculation
- Ensures new ideas are grounded in synthesized evidence
- Maintains scientific rigor

---

## Database Engine Compatibility

Written for **PostgreSQL**. Adaptations:

- **MySQL**: Replace `SERIAL` with `INT AUTO_INCREMENT`, `STRING_AGG` with `GROUP_CONCAT`
- **SQLite**: Replace `SERIAL` with `INTEGER PRIMARY KEY AUTOINCREMENT`, remove complex aggregates
- **SQL Server**: Replace `SERIAL` with `INT IDENTITY(1,1)`

---

## Future Extensions

- **Full-text search** on abstracts, claims, observation notes
- **Conflict detection** (contradictory findings across papers)
- **Data quality scoring** (evidence confidence ratings)
- **Collaborative annotations** (multiple curators, version control)
- **Knowledge graph export** (RDF, graph database serialization)
- **Hypothesis tracking** (which proposed experiments were actually conducted?)
