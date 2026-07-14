-- ============================================================================
-- mSCIdblit: SCI Knowledge Base Schema v2
-- Design: Evidence immutability + versioned interpretation
-- Focus: Spinal cord injury reconstruction research synthesis
-- ============================================================================

-- ============================================================================
-- CONTROLLED VOCABULARY REFERENCE TABLES
-- ============================================================================

CREATE TABLE IF NOT EXISTS ControlledVocabulary_Species (
  species_id SERIAL PRIMARY KEY,
  species_name VARCHAR(255) NOT NULL UNIQUE,
  ncbi_taxonomy_id VARCHAR(50),
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS ControlledVocabulary_InjuryModel (
  injury_model_id SERIAL PRIMARY KEY,
  model_name VARCHAR(255) NOT NULL UNIQUE,
  description TEXT,
  anatomical_target VARCHAR(255),  -- e.g., "T9 contusion", "L4 transection"
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS ControlledVocabulary_InjuryDevice (
  injury_device_id SERIAL PRIMARY KEY,
  device_name VARCHAR(255) NOT NULL UNIQUE,
  manufacturer VARCHAR(255),
  parameters VARCHAR(500),  -- e.g., force, duration, weight
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS ControlledVocabulary_LesionCompartment (
  compartment_id SERIAL PRIMARY KEY,
  compartment_name VARCHAR(255) NOT NULL UNIQUE,
  anatomical_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS ControlledVocabulary_EvidenceType (
  evidence_type_id SERIAL PRIMARY KEY,
  evidence_type_name VARCHAR(255) NOT NULL UNIQUE,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS ControlledVocabulary_OutcomeType (
  outcome_type_id SERIAL PRIMARY KEY,
  outcome_type_name VARCHAR(255) NOT NULL UNIQUE,
  description TEXT,
  measurement_unit VARCHAR(100),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS ControlledVocabulary_CellType (
  cell_type_id SERIAL PRIMARY KEY,
  cell_type_name VARCHAR(255) NOT NULL UNIQUE,
  synonyms TEXT,  -- comma-separated
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS ControlledVocabulary_Biomaterial (
  biomaterial_id SERIAL PRIMARY KEY,
  biomaterial_name VARCHAR(255) NOT NULL UNIQUE,
  material_category VARCHAR(100),  -- e.g., 'ECM', 'synthetic polymer', 'cell therapy'
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS ControlledVocabulary_SurgicalProcedure (
  procedure_id SERIAL PRIMARY KEY,
  procedure_name VARCHAR(255) NOT NULL UNIQUE,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS ControlledVocabulary_Assay (
  assay_id SERIAL PRIMARY KEY,
  assay_name VARCHAR(255) NOT NULL UNIQUE,
  assay_type VARCHAR(100),  -- e.g., 'behavioral', 'histological', 'molecular', 'electrophysiological'
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================================
-- CORE BIBLIOGRAPHIC ENTITY
-- ============================================================================

CREATE TABLE IF NOT EXISTS Paper (
  paper_id SERIAL PRIMARY KEY,
  title VARCHAR(500) NOT NULL,
  authors TEXT,
  publication_year INTEGER,
  journal VARCHAR(255),
  volume VARCHAR(50),
  issue VARCHAR(50),
  pages VARCHAR(100),
  doi VARCHAR(255) UNIQUE,
  pmid VARCHAR(50) UNIQUE,
  abstract TEXT,
  url VARCHAR(500),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT valid_year CHECK (publication_year > 1800 AND publication_year <= EXTRACT(YEAR FROM CURRENT_DATE))
);

CREATE INDEX idx_paper_doi ON Paper(doi);
CREATE INDEX idx_paper_pmid ON Paper(pmid);
CREATE INDEX idx_paper_year ON Paper(publication_year);

-- ============================================================================
-- RESEARCH FRAMEWORK
-- ============================================================================

CREATE TABLE IF NOT EXISTS ResearchQuestion (
  question_id SERIAL PRIMARY KEY,
  paper_id INTEGER NOT NULL,
  question_text TEXT NOT NULL,
  hypothesis_direction VARCHAR(50),  -- 'positive', 'negative', 'exploratory'
  keywords TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (paper_id) REFERENCES Paper(paper_id) ON DELETE CASCADE
);

CREATE INDEX idx_question_paper ON ResearchQuestion(paper_id);

CREATE TABLE IF NOT EXISTS ExperimentalParadigm (
  paradigm_id SERIAL PRIMARY KEY,
  paper_id INTEGER NOT NULL,
  paradigm_name VARCHAR(255) NOT NULL,
  description TEXT,
  methodology TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (paper_id) REFERENCES Paper(paper_id) ON DELETE CASCADE
);

CREATE INDEX idx_paradigm_paper ON ExperimentalParadigm(paper_id);

-- ============================================================================
-- IMMUTABLE EVIDENCE HIERARCHY
-- ============================================================================

CREATE TABLE IF NOT EXISTS Experiment (
  experiment_id SERIAL PRIMARY KEY,
  paper_id INTEGER NOT NULL,
  paradigm_id INTEGER NOT NULL,
  experiment_number INTEGER,
  figure_table_reference VARCHAR(100),  -- e.g., "Fig 3A", "Table 2"
  figure_panel_reference VARCHAR(100),  -- e.g., "panel A"
  title VARCHAR(500),
  description TEXT,
  sample_size INTEGER,
  control_type VARCHAR(100),  -- e.g., 'sham surgery', 'vehicle injection', 'wild-type'
  intervention_type VARCHAR(100),  -- e.g., 'cell transplant', 'drug treatment', 'genetic modification'
  duration_days FLOAT,
  timepoint_postinjury_days FLOAT,
  notes TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (paper_id) REFERENCES Paper(paper_id) ON DELETE CASCADE,
  FOREIGN KEY (paradigm_id) REFERENCES ExperimentalParadigm(paradigm_id) ON DELETE CASCADE
);

CREATE INDEX idx_experiment_paper ON Experiment(paper_id);
CREATE INDEX idx_experiment_paradigm ON Experiment(paradigm_id);

-- ============================================================================
-- ATOMIC OBSERVATIONS (IMMUTABLE EVIDENCE)
-- ============================================================================

CREATE TABLE IF NOT EXISTS Observation (
  observation_id SERIAL PRIMARY KEY,
  experiment_id INTEGER NOT NULL,
  evidence_type_id INTEGER NOT NULL,
  outcome_type_id INTEGER NOT NULL,
  observation_value VARCHAR(500) NOT NULL,  -- exact measured/stated value
  unit VARCHAR(100),
  standard_error FLOAT,
  confidence_interval_lower FLOAT,
  confidence_interval_upper FLOAT,
  p_value FLOAT,
  effect_size FLOAT,
  n_subjects INTEGER,
  measurement_method VARCHAR(255),  -- how was this measured?
  timepoint_postinjury_days FLOAT,  -- if different from experiment
  notes TEXT,  -- contextual notes only; never inferred
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  -- Immutability: observations are never deleted (only new ones added)
  FOREIGN KEY (experiment_id) REFERENCES Experiment(experiment_id) ON DELETE CASCADE,
  FOREIGN KEY (evidence_type_id) REFERENCES ControlledVocabulary_EvidenceType(evidence_type_id),
  FOREIGN KEY (outcome_type_id) REFERENCES ControlledVocabulary_OutcomeType(outcome_type_id),
  CONSTRAINT valid_p_value CHECK (p_value >= 0 AND p_value <= 1 OR p_value IS NULL)
);

CREATE INDEX idx_observation_experiment ON Observation(experiment_id);
CREATE INDEX idx_observation_evidence_type ON Observation(evidence_type_id);

-- ============================================================================
-- AUTHOR CLAIMS (INTERPRETATIONS)
-- ============================================================================

CREATE TABLE IF NOT EXISTS AuthorClaim (
  claim_id SERIAL PRIMARY KEY,
  paper_id INTEGER NOT NULL,
  claim_text TEXT NOT NULL,
  claim_type VARCHAR(100),  -- 'interpretation', 'conclusion', 'speculation', 'mechanistic', 'implication'
  confidence_level VARCHAR(50),  -- 'high', 'medium', 'low', 'speculative'
  notes TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (paper_id) REFERENCES Paper(paper_id) ON DELETE CASCADE
);

CREATE INDEX idx_claim_paper ON AuthorClaim(paper_id);
CREATE INDEX idx_claim_type ON AuthorClaim(claim_type);

-- ============================================================================
-- EVIDENCE LINK (TRACEABILITY: CLAIMS ← OBSERVATIONS)
-- ============================================================================

CREATE TABLE IF NOT EXISTS EvidenceLink (
  link_id SERIAL PRIMARY KEY,
  claim_id INTEGER NOT NULL,
  observation_id INTEGER NOT NULL,
  link_type VARCHAR(100),  -- 'directly_supports', 'indirectly_supports', 'contradicts', 'partially_supports'
  notes TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (claim_id) REFERENCES AuthorClaim(claim_id) ON DELETE CASCADE,
  FOREIGN KEY (observation_id) REFERENCES Observation(observation_id) ON DELETE CASCADE,
  UNIQUE(claim_id, observation_id)  -- prevent duplicate evidence links
);

CREATE INDEX idx_link_claim ON EvidenceLink(claim_id);
CREATE INDEX idx_link_observation ON EvidenceLink(observation_id);

-- ============================================================================
-- BIOLOGICAL ENTITIES (NORMALIZED ONTOLOGY)
-- ============================================================================

CREATE TABLE IF NOT EXISTS BiologicalEntity (
  entity_id SERIAL PRIMARY KEY,
  entity_name VARCHAR(255) NOT NULL UNIQUE,
  entity_type VARCHAR(100),  -- 'protein', 'gene', 'cell_type', 'cytokine', 'biomaterial', 'anatomical_structure'
  ncbi_gene_id VARCHAR(50),
  uniprot_id VARCHAR(50),
  cell_type_id INTEGER,
  synonyms TEXT,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (cell_type_id) REFERENCES ControlledVocabulary_CellType(cell_type_id)
);

CREATE INDEX idx_entity_name ON BiologicalEntity(entity_name);
CREATE INDEX idx_entity_type ON BiologicalEntity(entity_type);
CREATE INDEX idx_entity_gene_id ON BiologicalEntity(ncbi_gene_id);

-- ============================================================================
-- EXPERIMENT-LEVEL BIOLOGICAL CONTEXT
-- ============================================================================

CREATE TABLE IF NOT EXISTS Experiment_BiologicalEntity (
  experiment_id INTEGER NOT NULL,
  entity_id INTEGER NOT NULL,
  entity_role VARCHAR(100),  -- 'target', 'intervention', 'measurement', 'confound'
  PRIMARY KEY (experiment_id, entity_id),
  FOREIGN KEY (experiment_id) REFERENCES Experiment(experiment_id) ON DELETE CASCADE,
  FOREIGN KEY (entity_id) REFERENCES BiologicalEntity(entity_id) ON DELETE CASCADE
);

CREATE INDEX idx_exp_entity ON Experiment_BiologicalEntity(entity_id);

-- ============================================================================
-- EXPERIMENT-LEVEL PARAMETERS (CONTROLLED VOCABULARY MAPPING)
-- ============================================================================

CREATE TABLE IF NOT EXISTS Experiment_InjuryModel (
  experiment_id INTEGER NOT NULL,
  injury_model_id INTEGER NOT NULL,
  PRIMARY KEY (experiment_id, injury_model_id),
  FOREIGN KEY (experiment_id) REFERENCES Experiment(experiment_id) ON DELETE CASCADE,
  FOREIGN KEY (injury_model_id) REFERENCES ControlledVocabulary_InjuryModel(injury_model_id)
);

CREATE TABLE IF NOT EXISTS Experiment_InjuryDevice (
  experiment_id INTEGER NOT NULL,
  injury_device_id INTEGER NOT NULL,
  PRIMARY KEY (experiment_id, injury_device_id),
  FOREIGN KEY (experiment_id) REFERENCES Experiment(experiment_id) ON DELETE CASCADE,
  FOREIGN KEY (injury_device_id) REFERENCES ControlledVocabulary_InjuryDevice(injury_device_id)
);

CREATE TABLE IF NOT EXISTS Experiment_Species (
  experiment_id INTEGER NOT NULL,
  species_id INTEGER NOT NULL,
  PRIMARY KEY (experiment_id, species_id),
  FOREIGN KEY (experiment_id) REFERENCES Experiment(experiment_id) ON DELETE CASCADE,
  FOREIGN KEY (species_id) REFERENCES ControlledVocabulary_Species(species_id)
);

CREATE TABLE IF NOT EXISTS Experiment_LesionCompartment (
  experiment_id INTEGER NOT NULL,
  compartment_id INTEGER NOT NULL,
  PRIMARY KEY (experiment_id, compartment_id),
  FOREIGN KEY (experiment_id) REFERENCES Experiment(experiment_id) ON DELETE CASCADE,
  FOREIGN KEY (compartment_id) REFERENCES ControlledVocabulary_LesionCompartment(compartment_id)
);

CREATE TABLE IF NOT EXISTS Experiment_Assay (
  experiment_id INTEGER NOT NULL,
  assay_id INTEGER NOT NULL,
  PRIMARY KEY (experiment_id, assay_id),
  FOREIGN KEY (experiment_id) REFERENCES Experiment(experiment_id) ON DELETE CASCADE,
  FOREIGN KEY (assay_id) REFERENCES ControlledVocabulary_Assay(assay_id)
);

CREATE TABLE IF NOT EXISTS Experiment_Biomaterial (
  experiment_id INTEGER NOT NULL,
  biomaterial_id INTEGER NOT NULL,
  role VARCHAR(100),  -- 'intervention', 'scaffold', 'vehicle'
  PRIMARY KEY (experiment_id, biomaterial_id),
  FOREIGN KEY (experiment_id) REFERENCES Experiment(experiment_id) ON DELETE CASCADE,
  FOREIGN KEY (biomaterial_id) REFERENCES ControlledVocabulary_Biomaterial(biomaterial_id)
);

CREATE TABLE IF NOT EXISTS Experiment_SurgicalProcedure (
  experiment_id INTEGER NOT NULL,
  procedure_id INTEGER NOT NULL,
  sequence_order INTEGER,  -- order of procedures if multiple
  PRIMARY KEY (experiment_id, procedure_id),
  FOREIGN KEY (experiment_id) REFERENCES Experiment(experiment_id) ON DELETE CASCADE,
  FOREIGN KEY (procedure_id) REFERENCES ControlledVocabulary_SurgicalProcedure(procedure_id)
);

-- ============================================================================
-- VERSIONED INTERPRETATION: CONSENSUS
-- ============================================================================

CREATE TABLE IF NOT EXISTS Consensus (
  consensus_id SERIAL PRIMARY KEY,
  consensus_statement TEXT NOT NULL,
  topic VARCHAR(255),
  version INTEGER NOT NULL DEFAULT 1,  -- versioning for evolving assessments
  agreement_level VARCHAR(100),  -- 'strong', 'moderate', 'weak', 'emerging', or percentage
  num_supporting_papers INTEGER,
  num_contradicting_papers INTEGER,
  synthesis_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  notes TEXT
);

CREATE INDEX idx_consensus_topic ON Consensus(topic);
CREATE INDEX idx_consensus_version ON Consensus(consensus_id, version);

-- ============================================================================
-- CONSENSUS VERSION HISTORY
-- ============================================================================

CREATE TABLE IF NOT EXISTS Consensus_Version (
  version_id SERIAL PRIMARY KEY,
  consensus_id INTEGER NOT NULL,
  version_number INTEGER NOT NULL,
  statement_text TEXT NOT NULL,
  agreement_level VARCHAR(100),
  summary_of_changes TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (consensus_id) REFERENCES Consensus(consensus_id) ON DELETE CASCADE
);

CREATE INDEX idx_consensus_version_history ON Consensus_Version(consensus_id, version_number);

-- ============================================================================
-- CONSENSUS TO OBSERVATIONS MAPPING (DERIVED, NOT PRIMARY EVIDENCE)
-- ============================================================================

CREATE TABLE IF NOT EXISTS Consensus_Observation (
  consensus_id INTEGER NOT NULL,
  observation_id INTEGER NOT NULL,
  support_type VARCHAR(100),  -- 'supporting', 'contradicting'
  PRIMARY KEY (consensus_id, observation_id),
  FOREIGN KEY (consensus_id) REFERENCES Consensus(consensus_id) ON DELETE CASCADE,
  FOREIGN KEY (observation_id) REFERENCES Observation(observation_id) ON DELETE CASCADE
);

-- ============================================================================
-- HYPOTHESES (GENERATED ONLY FROM CONSENSUS)
-- ============================================================================

CREATE TABLE IF NOT EXISTS Hypothesis (
  hypothesis_id SERIAL PRIMARY KEY,
  hypothesis_text TEXT NOT NULL,
  derived_from_consensus_id INTEGER NOT NULL,
  hypothesis_type VARCHAR(100),  -- 'mechanistic', 'therapeutic', 'predictive'
  testability_level VARCHAR(50),  -- 'directly_testable', 'partially_testable', 'speculative'
  biological_entities TEXT,  -- JSON array of entity_ids involved
  predicted_outcome TEXT,
  proposed_experiment TEXT,  -- suggested experimental design to test
  confidence_level VARCHAR(50),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (derived_from_consensus_id) REFERENCES Consensus(consensus_id) ON DELETE CASCADE
);

CREATE INDEX idx_hypothesis_consensus ON Hypothesis(derived_from_consensus_id);

-- ============================================================================
-- SCIENTIFIC LINEAGE
-- ============================================================================

CREATE TABLE IF NOT EXISTS Lineage (
  lineage_id SERIAL PRIMARY KEY,
  lineage_name VARCHAR(255) NOT NULL UNIQUE,
  lineage_description TEXT,
  anchor_paper_id INTEGER,
  key_concepts TEXT,  -- comma-separated or JSON
  domain VARCHAR(100),  -- e.g., 'regeneration', 'inflammation', 'plasticity', 'neuroprotection'
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (anchor_paper_id) REFERENCES Paper(paper_id) ON DELETE SET NULL
);

CREATE INDEX idx_lineage_domain ON Lineage(domain);

CREATE TABLE IF NOT EXISTS Paper_Lineage (
  paper_id INTEGER NOT NULL,
  lineage_id INTEGER NOT NULL,
  contribution_type VARCHAR(100),  -- 'foundational', 'supporting', 'contradictory', 'novel_finding'
  PRIMARY KEY (paper_id, lineage_id),
  FOREIGN KEY (paper_id) REFERENCES Paper(paper_id) ON DELETE CASCADE,
  FOREIGN KEY (lineage_id) REFERENCES Lineage(lineage_id) ON DELETE CASCADE
);

CREATE INDEX idx_lineage_paper ON Paper_Lineage(lineage_id);

-- ============================================================================
-- SEARCH SESSIONS (REPRODUCIBLE LITERATURE SEARCH RECORD)
-- ============================================================================

CREATE TABLE IF NOT EXISTS SearchSession (
  search_id SERIAL PRIMARY KEY,
  search_query TEXT NOT NULL,
  search_strategy TEXT,  -- detailed description of search methodology
  database_source VARCHAR(255),  -- 'PubMed', 'Google Scholar', 'bioRxiv', etc.
  search_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  filters TEXT,  -- JSON: keywords, date range, inclusion/exclusion criteria
  papers_retrieved INTEGER,
  papers_reviewed INTEGER,
  papers_included_count INTEGER,
  inclusion_criteria TEXT,
  exclusion_criteria TEXT,
  notes TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_search_date ON SearchSession(search_date);
CREATE INDEX idx_search_source ON SearchSession(database_source);

CREATE TABLE IF NOT EXISTS SearchSession_Paper (
  search_id INTEGER NOT NULL,
  paper_id INTEGER NOT NULL,
  inclusion_status VARCHAR(100),  -- 'included', 'excluded', 'under_review'
  reason_for_exclusion TEXT,
  PRIMARY KEY (search_id, paper_id),
  FOREIGN KEY (search_id) REFERENCES SearchSession(search_id) ON DELETE CASCADE,
  FOREIGN KEY (paper_id) REFERENCES Paper(paper_id) ON DELETE CASCADE
);

-- ============================================================================
-- AUDIT & PROVENANCE TABLES
-- ============================================================================

CREATE TABLE IF NOT EXISTS DataSource (
  source_id SERIAL PRIMARY KEY,
  source_type VARCHAR(100),  -- 'PubMed', 'bioRxiv', 'search_session', 'manual_entry'
  source_identifier VARCHAR(500),  -- e.g., search query, entry date
  access_date TIMESTAMP,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS ChangeLog (
  change_id SERIAL PRIMARY KEY,
  table_name VARCHAR(255),
  record_id INTEGER,
  change_type VARCHAR(50),  -- 'insert', 'update', 'delete'
  old_values TEXT,  -- JSON
  new_values TEXT,  -- JSON
  changed_by VARCHAR(255),
  changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_changelog_table ON ChangeLog(table_name, record_id, changed_at);

-- ============================================================================
-- CRITICAL CONSTRAINTS FOR DATA INTEGRITY
-- ============================================================================

-- Constraint: Observations are never inferred (ensured by application logic)
-- Constraint: Hypotheses can only be derived from Consensus (FK enforced)
-- Constraint: Consensus statements are versioned, never deleted
-- Constraint: Evidence remains immutable once recorded

-- ============================================================================
-- VIEWS FOR COMMON QUERIES
-- ============================================================================

CREATE VIEW v_paper_with_experiments AS
SELECT 
  p.paper_id,
  p.title,
  p.publication_year,
  COUNT(DISTINCT e.experiment_id) as experiment_count,
  COUNT(DISTINCT o.observation_id) as observation_count
FROM Paper p
LEFT JOIN Experiment e ON p.paper_id = e.paper_id
LEFT JOIN Observation o ON e.experiment_id = o.experiment_id
GROUP BY p.paper_id, p.title, p.publication_year;

CREATE VIEW v_claim_evidence_chain AS
SELECT 
  ac.claim_id,
  ac.claim_text,
  ac.claim_type,
  COUNT(DISTINCT el.observation_id) as supporting_observations,
  STRING_AGG(DISTINCT CAST(el.observation_id AS TEXT), ', ') as observation_ids
FROM AuthorClaim ac
LEFT JOIN EvidenceLink el ON ac.claim_id = el.claim_id
GROUP BY ac.claim_id, ac.claim_text, ac.claim_type;

CREATE VIEW v_consensus_supporting_papers AS
SELECT 
  c.consensus_id,
  c.consensus_statement,
  COUNT(DISTINCT CASE WHEN co.support_type = 'supporting' THEN co.observation_id END) as supporting_obs,
  COUNT(DISTINCT CASE WHEN co.support_type = 'contradicting' THEN co.observation_id END) as contradicting_obs
FROM Consensus c
LEFT JOIN Consensus_Observation co ON c.consensus_id = co.consensus_id
GROUP BY c.consensus_id, c.consensus_statement;
