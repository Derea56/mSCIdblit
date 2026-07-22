-- Module 14B full first-pass materialization generated from tracker-derived JSON.
-- This script is intended for a fresh database loaded with schema/schema.sql and scripts/seed_controlled_vocab.sql.
BEGIN;

CREATE TEMP TABLE _m14_paper_map (tracker_id TEXT PRIMARY KEY, paper_id INTEGER NOT NULL);
CREATE TEMP TABLE _m14_paradigm_map (tracker_id TEXT PRIMARY KEY, paradigm_id INTEGER NOT NULL);
CREATE TEMP TABLE _m14_experiment_map (tracker_id TEXT PRIMARY KEY, experiment_id INTEGER NOT NULL);
CREATE TEMP TABLE _m14_observation_map (tracker_id TEXT PRIMARY KEY, observation_id INTEGER NOT NULL);
CREATE TEMP TABLE _m14_claim_map (tracker_id TEXT PRIMARY KEY, claim_id INTEGER NOT NULL);
CREATE TEMP TABLE _m14_link_map (tracker_id TEXT PRIMARY KEY, link_id INTEGER NOT NULL);
CREATE TEMP TABLE _m14_consensus_map (tracker_id TEXT PRIMARY KEY, consensus_id INTEGER NOT NULL);

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Transcriptional repression of PTEN in neural cells using CRISPR/dCas9 epigenetic editing', 'Moses', 2020,
    'Scientific Reports', NULL, NULL,
    NULL, '10.1038/s41598-020-68235-0', '32647121',
    NULL, '{"curator_notes": "Direct dCas9-KRAB PTEN repression in human neural/iPSC-derived cells and rat PC-12 cells; histone methylation/deacetylation and neurite outgrowth anchor.", "module": "Module 14B", "tracker_id": "M14A-P001"}'
  )
  RETURNING paper_id
)
INSERT INTO _m14_paper_map (tracker_id, paper_id) SELECT 'M14A-P001', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'A Neuron-Optimized CRISPR/dCas9 Activation System for Robust and Specific Gene Regulation', 'Savell', 2019,
    'eNeuro', NULL, NULL,
    NULL, '10.1523/ENEURO.0495-18.2019', 'PMC6412672',
    NULL, '{"curator_notes": "Neuronal CRISPRa platform; robust/tunable/multiplexed gene activation including Bdnf promoter specificity and in vivo CNS expression.", "module": "Module 14B", "tracker_id": "M14A-P002"}'
  )
  RETURNING paper_id
)
INSERT INTO _m14_paper_map (tracker_id, paper_id) SELECT 'M14A-P002', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'In vivo locus-specific editing of the neuroepigenome', 'Savell', 2020,
    'Nature Reviews Neuroscience', NULL, NULL,
    NULL, '10.1038/s41583-020-0334-4', '32704051',
    NULL, '{"curator_notes": "Review anchor for CRISPRa/i, dCas9-DNMT/TET1, histone acetylation/methylation, and in vivo neuroepigenome editing boundaries.", "module": "Module 14B", "tracker_id": "M14A-P003"}'
  )
  RETURNING paper_id
)
INSERT INTO _m14_paper_map (tracker_id, paper_id) SELECT 'M14A-P003', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Applications of CRISPR/Cas9 in the Mammalian Central Nervous System', 'Savell', 2017,
    'Yale Journal of Biology and Medicine', NULL, NULL,
    NULL, NULL, '29259522',
    NULL, '{"curator_notes": "CNS CRISPR review; dCas9 expands tools for local chromatin modification and gene regulation in neurons.", "module": "Module 14B", "tracker_id": "M14A-P004"}'
  )
  RETURNING paper_id
)
INSERT INTO _m14_paper_map (tracker_id, paper_id) SELECT 'M14A-P004', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Editing the Neuronal Genome: a CRISPR View of Chromatin Regulation in Neuronal Development, Function, and Plasticity', 'Yang', 2016,
    'Yale Journal of Biology and Medicine', NULL, NULL,
    NULL, NULL, '28018138',
    NULL, '{"curator_notes": "Review anchor for enhancer activation/repression and epigenome manipulation in neurobiology.", "module": "Module 14B", "tracker_id": "M14A-P005"}'
  )
  RETURNING paper_id
)
INSERT INTO _m14_paper_map (tracker_id, paper_id) SELECT 'M14A-P005', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Decoding epigenetic codes: new frontiers in exploring recovery from spinal cord injury', 'Zhang', 2020,
    'Neural Regeneration Research', NULL, NULL,
    NULL, '10.4103/1673-5374.276323', '32209760',
    NULL, '{"curator_notes": "SCI epigenetic-regulation review; links epigenetic landmarks to axon regeneration, glial activation, neurogenesis, and secondary injury.", "module": "Module 14B", "tracker_id": "M14A-P006"}'
  )
  RETURNING paper_id
)
INSERT INTO _m14_paper_map (tracker_id, paper_id) SELECT 'M14A-P006', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Epigenetic Regulation of WNT3A Enhancer during Regeneration of Injured Cortical Neurons', 'Chang', 2020,
    'International Journal of Molecular Sciences', NULL, NULL,
    NULL, '10.3390/ijms21051891', '32164275',
    NULL, '{"curator_notes": "Injury-responsive enhancer/chromatin state anchor for regeneration-associated gene regulation.", "module": "Module 14B", "tracker_id": "M14A-P007"}'
  )
  RETURNING paper_id
)
INSERT INTO _m14_paper_map (tracker_id, paper_id) SELECT 'M14A-P007', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'The regulatory code of injury-responsive enhancers enables precision cell-state targeting in the CNS', 'Zamboni', 2026,
    'Nature Neuroscience', NULL, NULL,
    NULL, '10.1038/s41593-025-02131-w', '41331142',
    NULL, '{"curator_notes": "Mouse spinal cord contusion snRNA/chromatin accessibility; injury-responsive enhancers selectively target reactive astrocytes across CNS.", "module": "Module 14B", "tracker_id": "M14A-P008"}'
  )
  RETURNING paper_id
)
INSERT INTO _m14_paper_map (tracker_id, paper_id) SELECT 'M14A-P008', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Optic nerve regeneration screen identifies multiple genes restricting adult neural repair', 'Weng', 2021,
    'Neuron', NULL, NULL,
    NULL, '10.1016/j.neuron.2021.02.024', '33657370',
    NULL, '{"curator_notes": "Large-scale in vivo optic nerve regeneration screen; shRNA hits validated by CRISPR-Cas9 editing define candidate repression targets.", "module": "Module 14B", "tracker_id": "M14A-P009"}'
  )
  RETURNING paper_id
)
INSERT INTO _m14_paper_map (tracker_id, paper_id) SELECT 'M14A-P009', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'An Image-Based miRNA Screen Identifies miRNA-135s As Regulators of CNS Axon Growth and Regeneration by Targeting Kruppel-like Factor 4', 'Gaub', 2019,
    'Journal of Neuroscience', NULL, NULL,
    NULL, '10.1523/JNEUROSCI.0888-18.2018', 'PMC6596187',
    NULL, '{"curator_notes": "KLF4 target-discovery comparator for regeneration-associated transcriptional repression.", "module": "Module 14B", "tracker_id": "M14A-P010"}'
  )
  RETURNING paper_id
)
INSERT INTO _m14_paper_map (tracker_id, paper_id) SELECT 'M14A-P010', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Epigenome editing by a CRISPR-Cas9-based acetyltransferase activates genes from promoters and enhancers', 'Hilton', 2015,
    'Nature Biotechnology', NULL, NULL,
    NULL, '10.1038/nbt.3199', '29236675',
    NULL, '{"curator_notes": "dCas9-p300 acetyltransferase tool anchor for promoter/enhancer activation.", "module": "Module 14B", "tracker_id": "M14A-P011"}'
  )
  RETURNING paper_id
)
INSERT INTO _m14_paper_map (tracker_id, paper_id) SELECT 'M14A-P011', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'CRISPR-mediated modular RNA-guided regulation of transcription in eukaryotes', 'Gilbert', 2013,
    'Cell', NULL, NULL,
    NULL, '10.1016/j.cell.2013.06.044', '23849981',
    NULL, '{"curator_notes": "Foundational CRISPRi/a modular regulation platform; boundary for transcriptional control without cutting.", "module": "Module 14B", "tracker_id": "M14A-P012"}'
  )
  RETURNING paper_id
)
INSERT INTO _m14_paper_map (tracker_id, paper_id) SELECT 'M14A-P012', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Genome-scale transcriptional activation by an engineered CRISPR-Cas9 complex', 'Konermann', 2015,
    'Nature', NULL, NULL,
    NULL, '10.1038/nature14136', '25849900',
    NULL, '{"curator_notes": "SAM/CRISPRa platform anchor for multiplexed gene activation and target discovery.", "module": "Module 14B", "tracker_id": "M14A-P013"}'
  )
  RETURNING paper_id
)
INSERT INTO _m14_paper_map (tracker_id, paper_id) SELECT 'M14A-P013', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'In vivo CRISPRa decreases seizures and rescues cognitive deficits in a rodent model of fragile X syndrome', 'Colasante', 2020,
    'Molecular Therapy', NULL, NULL,
    NULL, '10.1016/j.ymthe.2019.01.001', '30643228',
    NULL, '{"curator_notes": "In vivo CNS CRISPRa therapeutic-style proof-of-concept; delivery and durability comparator for neuroregeneration translation.", "module": "Module 14B", "tracker_id": "M14A-P014"}'
  )
  RETURNING paper_id
)
INSERT INTO _m14_paper_map (tracker_id, paper_id) SELECT 'M14A-P014', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'CRISPR/Cas: a potential gene-editing tool in the nervous system', 'Gao', 2020,
    'Cell Regeneration', NULL, NULL,
    NULL, '10.1186/s13619-020-00044-6', '32761306',
    NULL, '{"curator_notes": "Nervous-system CRISPR review covering engineered Cas proteins and CNS application boundaries.", "module": "Module 14B", "tracker_id": "M14A-P015"}'
  )
  RETURNING paper_id
)
INSERT INTO _m14_paper_map (tracker_id, paper_id) SELECT 'M14A-P015', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'CRISPR and Artificial Intelligence in Neuroregeneration: Closed-Loop Strategies for Precision Medicine, Spinal Cord Repair, and Adaptive Neuro-Oncology', 'Farooq', 2025,
    'International Journal of Molecular Sciences', NULL, NULL,
    NULL, '10.3390/ijms262010080', 'PMC12524701',
    NULL, '{"curator_notes": "Recent neuroregeneration review explicitly framing epigenetic CRISPR editing as reversible/flexible growth-program regulation.", "module": "Module 14B", "tracker_id": "M14A-P016"}'
  )
  RETURNING paper_id
)
INSERT INTO _m14_paper_map (tracker_id, paper_id) SELECT 'M14A-P016', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 14B curated evidence extraction',
    'First-pass Module 14B CRISPR-based epigenome editing for neuroregeneration curation for M14A-P001',
    'Tracker-derived materialization from Module_14B_TRACKER.md'
  FROM _m14_paper_map WHERE tracker_id = 'M14A-P001'
  RETURNING paradigm_id
)
INSERT INTO _m14_paradigm_map (tracker_id, paradigm_id) SELECT 'M14A-P001', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 14B curated evidence extraction',
    'First-pass Module 14B CRISPR-based epigenome editing for neuroregeneration curation for M14A-P002',
    'Tracker-derived materialization from Module_14B_TRACKER.md'
  FROM _m14_paper_map WHERE tracker_id = 'M14A-P002'
  RETURNING paradigm_id
)
INSERT INTO _m14_paradigm_map (tracker_id, paradigm_id) SELECT 'M14A-P002', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 14B curated evidence extraction',
    'First-pass Module 14B CRISPR-based epigenome editing for neuroregeneration curation for M14A-P003',
    'Tracker-derived materialization from Module_14B_TRACKER.md'
  FROM _m14_paper_map WHERE tracker_id = 'M14A-P003'
  RETURNING paradigm_id
)
INSERT INTO _m14_paradigm_map (tracker_id, paradigm_id) SELECT 'M14A-P003', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 14B curated evidence extraction',
    'First-pass Module 14B CRISPR-based epigenome editing for neuroregeneration curation for M14A-P004',
    'Tracker-derived materialization from Module_14B_TRACKER.md'
  FROM _m14_paper_map WHERE tracker_id = 'M14A-P004'
  RETURNING paradigm_id
)
INSERT INTO _m14_paradigm_map (tracker_id, paradigm_id) SELECT 'M14A-P004', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 14B curated evidence extraction',
    'First-pass Module 14B CRISPR-based epigenome editing for neuroregeneration curation for M14A-P005',
    'Tracker-derived materialization from Module_14B_TRACKER.md'
  FROM _m14_paper_map WHERE tracker_id = 'M14A-P005'
  RETURNING paradigm_id
)
INSERT INTO _m14_paradigm_map (tracker_id, paradigm_id) SELECT 'M14A-P005', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 14B curated evidence extraction',
    'First-pass Module 14B CRISPR-based epigenome editing for neuroregeneration curation for M14A-P006',
    'Tracker-derived materialization from Module_14B_TRACKER.md'
  FROM _m14_paper_map WHERE tracker_id = 'M14A-P006'
  RETURNING paradigm_id
)
INSERT INTO _m14_paradigm_map (tracker_id, paradigm_id) SELECT 'M14A-P006', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 14B curated evidence extraction',
    'First-pass Module 14B CRISPR-based epigenome editing for neuroregeneration curation for M14A-P007',
    'Tracker-derived materialization from Module_14B_TRACKER.md'
  FROM _m14_paper_map WHERE tracker_id = 'M14A-P007'
  RETURNING paradigm_id
)
INSERT INTO _m14_paradigm_map (tracker_id, paradigm_id) SELECT 'M14A-P007', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 14B curated evidence extraction',
    'First-pass Module 14B CRISPR-based epigenome editing for neuroregeneration curation for M14A-P008',
    'Tracker-derived materialization from Module_14B_TRACKER.md'
  FROM _m14_paper_map WHERE tracker_id = 'M14A-P008'
  RETURNING paradigm_id
)
INSERT INTO _m14_paradigm_map (tracker_id, paradigm_id) SELECT 'M14A-P008', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 14B curated evidence extraction',
    'First-pass Module 14B CRISPR-based epigenome editing for neuroregeneration curation for M14A-P009',
    'Tracker-derived materialization from Module_14B_TRACKER.md'
  FROM _m14_paper_map WHERE tracker_id = 'M14A-P009'
  RETURNING paradigm_id
)
INSERT INTO _m14_paradigm_map (tracker_id, paradigm_id) SELECT 'M14A-P009', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 14B curated evidence extraction',
    'First-pass Module 14B CRISPR-based epigenome editing for neuroregeneration curation for M14A-P010',
    'Tracker-derived materialization from Module_14B_TRACKER.md'
  FROM _m14_paper_map WHERE tracker_id = 'M14A-P010'
  RETURNING paradigm_id
)
INSERT INTO _m14_paradigm_map (tracker_id, paradigm_id) SELECT 'M14A-P010', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 14B curated evidence extraction',
    'First-pass Module 14B CRISPR-based epigenome editing for neuroregeneration curation for M14A-P011',
    'Tracker-derived materialization from Module_14B_TRACKER.md'
  FROM _m14_paper_map WHERE tracker_id = 'M14A-P011'
  RETURNING paradigm_id
)
INSERT INTO _m14_paradigm_map (tracker_id, paradigm_id) SELECT 'M14A-P011', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 14B curated evidence extraction',
    'First-pass Module 14B CRISPR-based epigenome editing for neuroregeneration curation for M14A-P012',
    'Tracker-derived materialization from Module_14B_TRACKER.md'
  FROM _m14_paper_map WHERE tracker_id = 'M14A-P012'
  RETURNING paradigm_id
)
INSERT INTO _m14_paradigm_map (tracker_id, paradigm_id) SELECT 'M14A-P012', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 14B curated evidence extraction',
    'First-pass Module 14B CRISPR-based epigenome editing for neuroregeneration curation for M14A-P013',
    'Tracker-derived materialization from Module_14B_TRACKER.md'
  FROM _m14_paper_map WHERE tracker_id = 'M14A-P013'
  RETURNING paradigm_id
)
INSERT INTO _m14_paradigm_map (tracker_id, paradigm_id) SELECT 'M14A-P013', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 14B curated evidence extraction',
    'First-pass Module 14B CRISPR-based epigenome editing for neuroregeneration curation for M14A-P014',
    'Tracker-derived materialization from Module_14B_TRACKER.md'
  FROM _m14_paper_map WHERE tracker_id = 'M14A-P014'
  RETURNING paradigm_id
)
INSERT INTO _m14_paradigm_map (tracker_id, paradigm_id) SELECT 'M14A-P014', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 14B curated evidence extraction',
    'First-pass Module 14B CRISPR-based epigenome editing for neuroregeneration curation for M14A-P015',
    'Tracker-derived materialization from Module_14B_TRACKER.md'
  FROM _m14_paper_map WHERE tracker_id = 'M14A-P015'
  RETURNING paradigm_id
)
INSERT INTO _m14_paradigm_map (tracker_id, paradigm_id) SELECT 'M14A-P015', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 14B curated evidence extraction',
    'First-pass Module 14B CRISPR-based epigenome editing for neuroregeneration curation for M14A-P016',
    'Tracker-derived materialization from Module_14B_TRACKER.md'
  FROM _m14_paper_map WHERE tracker_id = 'M14A-P016'
  RETURNING paradigm_id
)
INSERT INTO _m14_paradigm_map (tracker_id, paradigm_id) SELECT 'M14A-P016', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M14A-P001-E001',
    'Module 14B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M14B-O001"], "source_experiment_tracker_id": "M14A-P001-E001", "source_paper_tracker_id": "M14A-P001", "tracker_key": "M14A-P001::M14A-P001-E001"}'
  FROM _m14_paper_map p
  JOIN _m14_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M14A-P001'
  RETURNING experiment_id
)
INSERT INTO _m14_experiment_map (tracker_id, experiment_id) SELECT 'M14A-P001::M14A-P001-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Full-text PMC',
    'Tracker experiment M14A-P002-E001',
    'Module 14B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M14B-O002"], "source_experiment_tracker_id": "M14A-P002-E001", "source_paper_tracker_id": "M14A-P002", "tracker_key": "M14A-P002::M14A-P002-E001"}'
  FROM _m14_paper_map p
  JOIN _m14_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M14A-P002'
  RETURNING experiment_id
)
INSERT INTO _m14_experiment_map (tracker_id, experiment_id) SELECT 'M14A-P002::M14A-P002-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M14A-P003-E001',
    'Module 14B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M14B-O003"], "source_experiment_tracker_id": "M14A-P003-E001", "source_paper_tracker_id": "M14A-P003", "tracker_key": "M14A-P003::M14A-P003-E001"}'
  FROM _m14_paper_map p
  JOIN _m14_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M14A-P003'
  RETURNING experiment_id
)
INSERT INTO _m14_experiment_map (tracker_id, experiment_id) SELECT 'M14A-P003::M14A-P003-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Full-text PMC',
    'Tracker experiment M14A-P004-E001',
    'Module 14B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M14B-O004"], "source_experiment_tracker_id": "M14A-P004-E001", "source_paper_tracker_id": "M14A-P004", "tracker_key": "M14A-P004::M14A-P004-E001"}'
  FROM _m14_paper_map p
  JOIN _m14_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M14A-P004'
  RETURNING experiment_id
)
INSERT INTO _m14_experiment_map (tracker_id, experiment_id) SELECT 'M14A-P004::M14A-P004-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Full-text PMC',
    'Tracker experiment M14A-P005-E001',
    'Module 14B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M14B-O005"], "source_experiment_tracker_id": "M14A-P005-E001", "source_paper_tracker_id": "M14A-P005", "tracker_key": "M14A-P005::M14A-P005-E001"}'
  FROM _m14_paper_map p
  JOIN _m14_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M14A-P005'
  RETURNING experiment_id
)
INSERT INTO _m14_experiment_map (tracker_id, experiment_id) SELECT 'M14A-P005::M14A-P005-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Full-text PMC',
    'Tracker experiment M14A-P006-E001',
    'Module 14B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M14B-O006"], "source_experiment_tracker_id": "M14A-P006-E001", "source_paper_tracker_id": "M14A-P006", "tracker_key": "M14A-P006::M14A-P006-E001"}'
  FROM _m14_paper_map p
  JOIN _m14_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M14A-P006'
  RETURNING experiment_id
)
INSERT INTO _m14_experiment_map (tracker_id, experiment_id) SELECT 'M14A-P006::M14A-P006-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Full-text PMC',
    'Tracker experiment M14A-P007-E001',
    'Module 14B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M14B-O007"], "source_experiment_tracker_id": "M14A-P007-E001", "source_paper_tracker_id": "M14A-P007", "tracker_key": "M14A-P007::M14A-P007-E001"}'
  FROM _m14_paper_map p
  JOIN _m14_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M14A-P007'
  RETURNING experiment_id
)
INSERT INTO _m14_experiment_map (tracker_id, experiment_id) SELECT 'M14A-P007::M14A-P007-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M14A-P008-E001',
    'Module 14B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M14B-O008"], "source_experiment_tracker_id": "M14A-P008-E001", "source_paper_tracker_id": "M14A-P008", "tracker_key": "M14A-P008::M14A-P008-E001"}'
  FROM _m14_paper_map p
  JOIN _m14_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M14A-P008'
  RETURNING experiment_id
)
INSERT INTO _m14_experiment_map (tracker_id, experiment_id) SELECT 'M14A-P008::M14A-P008-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M14A-P009-E001',
    'Module 14B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M14B-O009"], "source_experiment_tracker_id": "M14A-P009-E001", "source_paper_tracker_id": "M14A-P009", "tracker_key": "M14A-P009::M14A-P009-E001"}'
  FROM _m14_paper_map p
  JOIN _m14_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M14A-P009'
  RETURNING experiment_id
)
INSERT INTO _m14_experiment_map (tracker_id, experiment_id) SELECT 'M14A-P009::M14A-P009-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Full-text PMC',
    'Tracker experiment M14A-P010-E001',
    'Module 14B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M14B-O010"], "source_experiment_tracker_id": "M14A-P010-E001", "source_paper_tracker_id": "M14A-P010", "tracker_key": "M14A-P010::M14A-P010-E001"}'
  FROM _m14_paper_map p
  JOIN _m14_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M14A-P010'
  RETURNING experiment_id
)
INSERT INTO _m14_experiment_map (tracker_id, experiment_id) SELECT 'M14A-P010::M14A-P010-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M14A-P011-E001',
    'Module 14B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M14B-O011"], "source_experiment_tracker_id": "M14A-P011-E001", "source_paper_tracker_id": "M14A-P011", "tracker_key": "M14A-P011::M14A-P011-E001"}'
  FROM _m14_paper_map p
  JOIN _m14_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M14A-P011'
  RETURNING experiment_id
)
INSERT INTO _m14_experiment_map (tracker_id, experiment_id) SELECT 'M14A-P011::M14A-P011-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M14A-P012-E001',
    'Module 14B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M14B-O012"], "source_experiment_tracker_id": "M14A-P012-E001", "source_paper_tracker_id": "M14A-P012", "tracker_key": "M14A-P012::M14A-P012-E001"}'
  FROM _m14_paper_map p
  JOIN _m14_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M14A-P012'
  RETURNING experiment_id
)
INSERT INTO _m14_experiment_map (tracker_id, experiment_id) SELECT 'M14A-P012::M14A-P012-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M14A-P013-E001',
    'Module 14B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M14B-O013"], "source_experiment_tracker_id": "M14A-P013-E001", "source_paper_tracker_id": "M14A-P013", "tracker_key": "M14A-P013::M14A-P013-E001"}'
  FROM _m14_paper_map p
  JOIN _m14_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M14A-P013'
  RETURNING experiment_id
)
INSERT INTO _m14_experiment_map (tracker_id, experiment_id) SELECT 'M14A-P013::M14A-P013-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M14A-P014-E001',
    'Module 14B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M14B-O014"], "source_experiment_tracker_id": "M14A-P014-E001", "source_paper_tracker_id": "M14A-P014", "tracker_key": "M14A-P014::M14A-P014-E001"}'
  FROM _m14_paper_map p
  JOIN _m14_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M14A-P014'
  RETURNING experiment_id
)
INSERT INTO _m14_experiment_map (tracker_id, experiment_id) SELECT 'M14A-P014::M14A-P014-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Full-text PMC',
    'Tracker experiment M14A-P015-E001',
    'Module 14B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M14B-O015"], "source_experiment_tracker_id": "M14A-P015-E001", "source_paper_tracker_id": "M14A-P015", "tracker_key": "M14A-P015::M14A-P015-E001"}'
  FROM _m14_paper_map p
  JOIN _m14_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M14A-P015'
  RETURNING experiment_id
)
INSERT INTO _m14_experiment_map (tracker_id, experiment_id) SELECT 'M14A-P015::M14A-P015-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Full-text PMC',
    'Tracker experiment M14A-P016-E001',
    'Module 14B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M14B-O016"], "source_experiment_tracker_id": "M14A-P016-E001", "source_paper_tracker_id": "M14A-P016", "tracker_key": "M14A-P016::M14A-P016-E001"}'
  FROM _m14_paper_map p
  JOIN _m14_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M14A-P016'
  RETURNING experiment_id
)
INSERT INTO _m14_experiment_map (tracker_id, experiment_id) SELECT 'M14A-P016::M14A-P016-E001', experiment_id FROM inserted;

INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('CNS CRISPR review evidence', 'Module 14B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('CNS injury enhancer evidence', 'Module 14B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('CRISPR epigenome editing evidence', 'Module 14B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('CRISPR transcriptional regulation evidence', 'Module 14B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('CRISPRa platform evidence', 'Module 14B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('SCI epigenetic context evidence', 'Module 14B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('epigenome editing tool evidence', 'Module 14B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('in vivo CNS CRISPRa evidence', 'Module 14B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('injury enhancer evidence', 'Module 14B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('nervous-system CRISPR review evidence', 'Module 14B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('neurobiology CRISPR/chromatin evidence', 'Module 14B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('neuroepigenome editing evidence', 'Module 14B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('neuronal CRISPRa platform evidence', 'Module 14B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('neuroregeneration review evidence', 'Module 14B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('regeneration target-discovery evidence', 'Module 14B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;

INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('KLF4-linked axon growth regulation', 'Module 14B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('PTEN repression and neurite outgrowth', 'Module 14B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('activation/repression without DNA cleavage', 'Module 14B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('axon regeneration target nomination', 'Module 14B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('cell-state-specific targeting', 'Module 14B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('chromatin-effector toolkit', 'Module 14B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('delivery and safety boundary', 'Module 14B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('endogenous gene activation', 'Module 14B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('enhancer and epigenome manipulation', 'Module 14B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('local chromatin regulation', 'Module 14B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('multiplexed activation and screening', 'Module 14B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('promoter/enhancer acetylation', 'Module 14B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('regeneration and secondary injury', 'Module 14B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('regeneration-associated enhancer regulation', 'Module 14B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('reversible growth-program regulation', 'Module 14B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('therapeutic-style endogenous activation', 'Module 14B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'dCas9-KRAB repressed PTEN, induced promoter histone methylation/deacetylation, outperformed shRNA, and enhanced PC-12 neurite outgrowth.',
    'qualitative',
    'genetic perturbation / knockdown assay',
    'dCas9-KRAB repressed PTEN, induced promoter histone methylation/deacetylation, outperformed shRNA, and enhanced PC-12 neurite outgrowth.',
    'dCas9-KRAB PTEN repression enhances neurite outgrowth',
    'Module 14A tracker / source-page, full-text PMC, or review metadata',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Direct regeneration-relevant CRISPRi anchor.", "experiment_tracker_id": "M14A-P001-E001", "measurement_method_inference": "genetic perturbation / knockdown assay", "paper_tracker_id": "M14A-P001", "quantitative": "NO", "statistics_reported": "Source-page first pass; exact statistics not extracted", "topic_id": "M14B-T001", "tracker_id": "M14B-O001"}'
  FROM _m14_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M14A-P001::M14A-P001-E001'
    AND et.evidence_type_name = 'CRISPR epigenome editing evidence'
    AND ot.outcome_type_name = 'PTEN repression and neurite outgrowth'
  RETURNING observation_id
)
INSERT INTO _m14_observation_map (tracker_id, observation_id) SELECT 'M14B-O001', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Neuron-optimized CRISPRa produced robust, tunable, multiplexed, and promoter-selective gene activation in neurons and in vivo CNS structures.',
    'qualitative',
    NULL,
    'Neuron-optimized CRISPRa produced robust, tunable, multiplexed, and promoter-selective gene activation in neurons and in vivo CNS structures.',
    'neuronal CRISPRa enables tunable endogenous activation',
    'Module 14A tracker / source-page, full-text PMC, or review metadata',
    'Full-text PMC',
    'high',
    '{"curator_notes": "Tool-platform anchor for neuronal gene activation.", "experiment_tracker_id": "M14A-P002-E001", "measurement_method_inference": null, "paper_tracker_id": "M14A-P002", "quantitative": "NO", "statistics_reported": "Full-text first pass; exact effect sizes not materialized here", "topic_id": "M14B-T002", "tracker_id": "M14B-O002"}'
  FROM _m14_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M14A-P002::M14A-P002-E001'
    AND et.evidence_type_name = 'neuronal CRISPRa platform evidence'
    AND ot.outcome_type_name = 'endogenous gene activation'
  RETURNING observation_id
)
INSERT INTO _m14_observation_map (tracker_id, observation_id) SELECT 'M14B-O002', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Review maps locus-specific neuroepigenome editing tools and emphasizes chromatin-effector boundaries in vivo.',
    'qualitative',
    NULL,
    'Review maps locus-specific neuroepigenome editing tools and emphasizes chromatin-effector boundaries in vivo.',
    'neuroepigenome editing toolkit boundary',
    'Module 14A tracker / source-page, full-text PMC, or review metadata',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Tool-class boundary row.", "experiment_tracker_id": "M14A-P003-E001", "measurement_method_inference": null, "paper_tracker_id": "M14A-P003", "quantitative": "NO", "statistics_reported": "Review/source-page first pass", "topic_id": "M14B-T003", "tracker_id": "M14B-O003"}'
  FROM _m14_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M14A-P003::M14A-P003-E001'
    AND et.evidence_type_name = 'neuroepigenome editing evidence'
    AND ot.outcome_type_name = 'chromatin-effector toolkit'
  RETURNING observation_id
)
INSERT INTO _m14_observation_map (tracker_id, observation_id) SELECT 'M14B-O003', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'CNS CRISPR review identifies dCas9-based chromatin modification as a modular way to interrogate neuronal gene regulation.',
    'qualitative',
    'genetic perturbation / knockdown assay',
    'CNS CRISPR review identifies dCas9-based chromatin modification as a modular way to interrogate neuronal gene regulation.',
    'dCas9 enables local chromatin regulation in CNS',
    'Module 14A tracker / source-page, full-text PMC, or review metadata',
    'Full-text PMC',
    'high',
    '{"curator_notes": "CNS tool context.", "experiment_tracker_id": "M14A-P004-E001", "measurement_method_inference": "genetic perturbation / knockdown assay", "paper_tracker_id": "M14A-P004", "quantitative": "NO", "statistics_reported": "Review-level evidence", "topic_id": "M14B-T002", "tracker_id": "M14B-O004"}'
  FROM _m14_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M14A-P004::M14A-P004-E001'
    AND et.evidence_type_name = 'CNS CRISPR review evidence'
    AND ot.outcome_type_name = 'local chromatin regulation'
  RETURNING observation_id
)
INSERT INTO _m14_observation_map (tracker_id, observation_id) SELECT 'M14B-O004', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Review separates enhancer editing, CRISPRa/i, and epigenome manipulation as distinct neurobiology applications.',
    'qualitative',
    'genetic perturbation / knockdown assay',
    'Review separates enhancer editing, CRISPRa/i, and epigenome manipulation as distinct neurobiology applications.',
    'enhancer editing and epigenome manipulation are distinct tool uses',
    'Module 14A tracker / source-page, full-text PMC, or review metadata',
    'Full-text PMC',
    'high',
    '{"curator_notes": "Prevents tool-class collapse.", "experiment_tracker_id": "M14A-P005-E001", "measurement_method_inference": "genetic perturbation / knockdown assay", "paper_tracker_id": "M14A-P005", "quantitative": "NO", "statistics_reported": "Review-level evidence", "topic_id": "M14B-T003", "tracker_id": "M14B-O005"}'
  FROM _m14_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M14A-P005::M14A-P005-E001'
    AND et.evidence_type_name = 'neurobiology CRISPR/chromatin evidence'
    AND ot.outcome_type_name = 'enhancer and epigenome manipulation'
  RETURNING observation_id
)
INSERT INTO _m14_observation_map (tracker_id, observation_id) SELECT 'M14B-O005', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'SCI review links post-injury epigenetic landmarks to regeneration and secondary injury, supporting target selection for epigenome editing.',
    'qualitative',
    NULL,
    'SCI review links post-injury epigenetic landmarks to regeneration and secondary injury, supporting target selection for epigenome editing.',
    'SCI epigenetic landmarks inform target selection',
    'Module 14A tracker / source-page, full-text PMC, or review metadata',
    'Full-text PMC',
    'high',
    '{"curator_notes": "SCI context anchor.", "experiment_tracker_id": "M14A-P006-E001", "measurement_method_inference": null, "paper_tracker_id": "M14A-P006", "quantitative": "NO", "statistics_reported": "Review-level evidence", "topic_id": "M14B-T004", "tracker_id": "M14B-O006"}'
  FROM _m14_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M14A-P006::M14A-P006-E001'
    AND et.evidence_type_name = 'SCI epigenetic context evidence'
    AND ot.outcome_type_name = 'regeneration and secondary injury'
  RETURNING observation_id
)
INSERT INTO _m14_observation_map (tracker_id, observation_id) SELECT 'M14B-O006', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Injured cortical neuron study identifies enhancer-level epigenetic regulation of WNT3A during regeneration.',
    'qualitative',
    NULL,
    'Injured cortical neuron study identifies enhancer-level epigenetic regulation of WNT3A during regeneration.',
    'WNT3A enhancer regulation in injured neurons',
    'Module 14A tracker / source-page, full-text PMC, or review metadata',
    'Full-text PMC',
    'high',
    '{"curator_notes": "Enhancer target candidate row.", "experiment_tracker_id": "M14A-P007-E001", "measurement_method_inference": null, "paper_tracker_id": "M14A-P007", "quantitative": "NO", "statistics_reported": "Full-text first pass", "topic_id": "M14B-T004", "tracker_id": "M14B-O007"}'
  FROM _m14_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M14A-P007::M14A-P007-E001'
    AND et.evidence_type_name = 'injury enhancer evidence'
    AND ot.outcome_type_name = 'regeneration-associated enhancer regulation'
  RETURNING observation_id
)
INSERT INTO _m14_observation_map (tracker_id, observation_id) SELECT 'M14B-O007', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Injury-responsive enhancers in mouse spinal cord injury retain cell-type specificity and can target reactive astrocytes across CNS using gene-delivery vectors.',
    'qualitative',
    'single-cell RNA-seq / cell-state atlas',
    'Injury-responsive enhancers in mouse spinal cord injury retain cell-type specificity and can target reactive astrocytes across CNS using gene-delivery vectors.',
    'injury enhancers target reactive astrocyte states',
    'Module 14A tracker / source-page, full-text PMC, or review metadata',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "SCI enhancer targeting boundary.", "experiment_tracker_id": "M14A-P008-E001", "measurement_method_inference": "single-cell RNA-seq / cell-state atlas", "paper_tracker_id": "M14A-P008", "quantitative": "NO", "statistics_reported": "Source-page first pass", "topic_id": "M14B-T005", "tracker_id": "M14B-O008"}'
  FROM _m14_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M14A-P008::M14A-P008-E001'
    AND et.evidence_type_name = 'CNS injury enhancer evidence'
    AND ot.outcome_type_name = 'cell-state-specific targeting'
  RETURNING observation_id
)
INSERT INTO _m14_observation_map (tracker_id, observation_id) SELECT 'M14B-O008', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Optic nerve screen identified multiple regeneration-restricting genes and used CRISPR validation to define target candidates for regulatory repression.',
    'qualitative',
    'genetic perturbation / knockdown assay',
    'Optic nerve screen identified multiple regeneration-restricting genes and used CRISPR validation to define target candidates for regulatory repression.',
    'CRISPR-validated regeneration suppressor targets',
    'Module 14A tracker / source-page, full-text PMC, or review metadata',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Comparator; not epigenome editing efficacy.", "experiment_tracker_id": "M14A-P009-E001", "measurement_method_inference": "genetic perturbation / knockdown assay", "paper_tracker_id": "M14A-P009", "quantitative": "NO", "statistics_reported": "Source-page first pass", "topic_id": "M14B-T006", "tracker_id": "M14B-O009"}'
  FROM _m14_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M14A-P009::M14A-P009-E001'
    AND et.evidence_type_name = 'regeneration target-discovery evidence'
    AND ot.outcome_type_name = 'axon regeneration target nomination'
  RETURNING observation_id
)
INSERT INTO _m14_observation_map (tracker_id, observation_id) SELECT 'M14B-O009', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'miRNA-135/KLF4 work supports KLF4-family repression as an intrinsic-growth target logic relevant to CRISPRi.',
    'qualitative',
    NULL,
    'miRNA-135/KLF4 work supports KLF4-family repression as an intrinsic-growth target logic relevant to CRISPRi.',
    'KLF4 repression target logic',
    'Module 14A tracker / source-page, full-text PMC, or review metadata',
    'Full-text PMC',
    'high',
    '{"curator_notes": "Target-discovery comparator.", "experiment_tracker_id": "M14A-P010-E001", "measurement_method_inference": null, "paper_tracker_id": "M14A-P010", "quantitative": "NO", "statistics_reported": "Full-text first pass", "topic_id": "M14B-T006", "tracker_id": "M14B-O010"}'
  FROM _m14_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M14A-P010::M14A-P010-E001'
    AND et.evidence_type_name = 'regeneration target-discovery evidence'
    AND ot.outcome_type_name = 'KLF4-linked axon growth regulation'
  RETURNING observation_id
)
INSERT INTO _m14_observation_map (tracker_id, observation_id) SELECT 'M14B-O010', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'dCas9-p300 provides a programmable enhancer/promoter acetylation strategy relevant to activating regeneration-associated loci.',
    'qualitative',
    NULL,
    'dCas9-p300 provides a programmable enhancer/promoter acetylation strategy relevant to activating regeneration-associated loci.',
    'dCas9-p300 acetylation activation tool',
    'Module 14A tracker / source-page, full-text PMC, or review metadata',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Activation effector boundary.", "experiment_tracker_id": "M14A-P011-E001", "measurement_method_inference": null, "paper_tracker_id": "M14A-P011", "quantitative": "NO", "statistics_reported": "Source-page first pass", "topic_id": "M14B-T003", "tracker_id": "M14B-O011"}'
  FROM _m14_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M14A-P011::M14A-P011-E001'
    AND et.evidence_type_name = 'epigenome editing tool evidence'
    AND ot.outcome_type_name = 'promoter/enhancer acetylation'
  RETURNING observation_id
)
INSERT INTO _m14_observation_map (tracker_id, observation_id) SELECT 'M14B-O011', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Foundational CRISPRi/a work establishes guide-programmable transcriptional regulation without DNA cleavage.',
    'qualitative',
    'qPCR / RT-PCR / mRNA assay; genetic perturbation / knockdown assay',
    'Foundational CRISPRi/a work establishes guide-programmable transcriptional regulation without DNA cleavage.',
    'guide-programmable transcriptional regulation',
    'Module 14A tracker / source-page, full-text PMC, or review metadata',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Foundational tool boundary.", "experiment_tracker_id": "M14A-P012-E001", "measurement_method_inference": "qPCR / RT-PCR / mRNA assay; genetic perturbation / knockdown assay", "paper_tracker_id": "M14A-P012", "quantitative": "NO", "statistics_reported": "Source-page first pass", "topic_id": "M14B-T003", "tracker_id": "M14B-O012"}'
  FROM _m14_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M14A-P012::M14A-P012-E001'
    AND et.evidence_type_name = 'CRISPR transcriptional regulation evidence'
    AND ot.outcome_type_name = 'activation/repression without DNA cleavage'
  RETURNING observation_id
)
INSERT INTO _m14_observation_map (tracker_id, observation_id) SELECT 'M14B-O012', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'SAM CRISPRa establishes multiplexed activation logic for discovering growth-promoting regulatory programs.',
    'qualitative',
    NULL,
    'SAM CRISPRa establishes multiplexed activation logic for discovering growth-promoting regulatory programs.',
    'multiplexed CRISPRa target discovery',
    'Module 14A tracker / source-page, full-text PMC, or review metadata',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "CRISPRa discovery boundary.", "experiment_tracker_id": "M14A-P013-E001", "measurement_method_inference": null, "paper_tracker_id": "M14A-P013", "quantitative": "NO", "statistics_reported": "Source-page first pass", "topic_id": "M14B-T003", "tracker_id": "M14B-O013"}'
  FROM _m14_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M14A-P013::M14A-P013-E001'
    AND et.evidence_type_name = 'CRISPRa platform evidence'
    AND ot.outcome_type_name = 'multiplexed activation and screening'
  RETURNING observation_id
)
INSERT INTO _m14_observation_map (tracker_id, observation_id) SELECT 'M14B-O013', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'In vivo CNS CRISPRa proof-of-concept supports therapeutic feasibility boundaries for gene activation in neural tissue.',
    'qualitative',
    NULL,
    'In vivo CNS CRISPRa proof-of-concept supports therapeutic feasibility boundaries for gene activation in neural tissue.',
    'in vivo CNS CRISPRa feasibility',
    'Module 14A tracker / source-page, full-text PMC, or review metadata',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Translation comparator.", "experiment_tracker_id": "M14A-P014-E001", "measurement_method_inference": null, "paper_tracker_id": "M14A-P014", "quantitative": "NO", "statistics_reported": "Source-page first pass", "topic_id": "M14B-T007", "tracker_id": "M14B-O014"}'
  FROM _m14_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M14A-P014::M14A-P014-E001'
    AND et.evidence_type_name = 'in vivo CNS CRISPRa evidence'
    AND ot.outcome_type_name = 'therapeutic-style endogenous activation'
  RETURNING observation_id
)
INSERT INTO _m14_observation_map (tracker_id, observation_id) SELECT 'M14B-O014', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Nervous-system CRISPR review provides delivery, specificity, and tool-class boundaries for CNS translation.',
    'qualitative',
    'genetic perturbation / knockdown assay',
    'Nervous-system CRISPR review provides delivery, specificity, and tool-class boundaries for CNS translation.',
    'CNS CRISPR delivery and safety boundaries',
    'Module 14A tracker / source-page, full-text PMC, or review metadata',
    'Full-text PMC',
    'high',
    '{"curator_notes": "Safety/tool-class boundary.", "experiment_tracker_id": "M14A-P015-E001", "measurement_method_inference": "genetic perturbation / knockdown assay", "paper_tracker_id": "M14A-P015", "quantitative": "NO", "statistics_reported": "Review-level evidence", "topic_id": "M14B-T007", "tracker_id": "M14B-O015"}'
  FROM _m14_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M14A-P015::M14A-P015-E001'
    AND et.evidence_type_name = 'nervous-system CRISPR review evidence'
    AND ot.outcome_type_name = 'delivery and safety boundary'
  RETURNING observation_id
)
INSERT INTO _m14_observation_map (tracker_id, observation_id) SELECT 'M14B-O015', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Recent review frames epigenetic CRISPR editing as reversible/flexible gene-program control for neuroregeneration, while requiring validation before clinical claims.',
    'qualitative',
    'genetic perturbation / knockdown assay',
    'Recent review frames epigenetic CRISPR editing as reversible/flexible gene-program control for neuroregeneration, while requiring validation before clinical claims.',
    'epigenetic CRISPR as flexible neuroregeneration platform',
    'Module 14A tracker / source-page, full-text PMC, or review metadata',
    'Full-text PMC',
    'high',
    '{"curator_notes": "Project-level translation boundary.", "experiment_tracker_id": "M14A-P016-E001", "measurement_method_inference": "genetic perturbation / knockdown assay", "paper_tracker_id": "M14A-P016", "quantitative": "NO", "statistics_reported": "Review-level evidence", "topic_id": "M14B-T008", "tracker_id": "M14B-O016"}'
  FROM _m14_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M14A-P016::M14A-P016-E001'
    AND et.evidence_type_name = 'neuroregeneration review evidence'
    AND ot.outcome_type_name = 'reversible growth-program regulation'
  RETURNING observation_id
)
INSERT INTO _m14_observation_map (tracker_id, observation_id) SELECT 'M14B-O016', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'CRISPR/dCas9-KRAB repression of PTEN is a direct regeneration-relevant epigenome-editing strategy because it modifies promoter chromatin and improves neurite outgrowth in neural cells.',
    'mechanistic',
    'medium',
    'Module 14A tracker / source-page, full-text PMC, or review metadata',
    'medium',
    '{"curator_notes": "Full-text quantitative upgrade queued.", "source_paper_tracker_id": "M14A-P001", "topic_id": "M14B-T001", "tracker_id": "M14B-C001"}'
  FROM _m14_paper_map p
  WHERE p.tracker_id = 'M14A-P001'
  RETURNING claim_id
)
INSERT INTO _m14_claim_map (tracker_id, claim_id) SELECT 'M14B-C001', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Neuron-optimized CRISPRa can activate endogenous neuronal genes in a tunable, multiplexed, promoter-selective manner in vitro and in vivo.',
    'tool validation',
    'high',
    'Module 14A tracker / source-page, full-text PMC, or review metadata',
    'high',
    '{"curator_notes": "Tool-platform claim.", "source_paper_tracker_id": "M14A-P002", "topic_id": "M14B-T002", "tracker_id": "M14B-C002"}'
  FROM _m14_paper_map p
  WHERE p.tracker_id = 'M14A-P002'
  RETURNING claim_id
)
INSERT INTO _m14_claim_map (tracker_id, claim_id) SELECT 'M14B-C002', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Neuroepigenome editing requires effector-specific interpretation because CRISPRa, CRISPRi, DNMT, TET1, p300, and histone-modifying systems produce different regulatory states.',
    'boundary condition',
    'medium',
    'Module 14A tracker / source-page, full-text PMC, or review metadata',
    'medium',
    '{"curator_notes": "Review-level claim.", "source_paper_tracker_id": "M14A-P003", "topic_id": "M14B-T003", "tracker_id": "M14B-C003"}'
  FROM _m14_paper_map p
  WHERE p.tracker_id = 'M14A-P003'
  RETURNING claim_id
)
INSERT INTO _m14_claim_map (tracker_id, claim_id) SELECT 'M14B-C003', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'dCas9 expands CNS CRISPR from permanent editing into modular local chromatin and gene-regulatory perturbation.',
    'tool validation',
    'high',
    'Module 14A tracker / source-page, full-text PMC, or review metadata',
    'high',
    '{"curator_notes": "CNS tool claim.", "source_paper_tracker_id": "M14A-P004", "topic_id": "M14B-T002", "tracker_id": "M14B-C004"}'
  FROM _m14_paper_map p
  WHERE p.tracker_id = 'M14A-P004'
  RETURNING claim_id
)
INSERT INTO _m14_claim_map (tracker_id, claim_id) SELECT 'M14B-C004', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Enhancer activation/repression and epigenome manipulation should be separated from nuclease-based genome editing in neurobiology.',
    'boundary condition',
    'high',
    'Module 14A tracker / source-page, full-text PMC, or review metadata',
    'high',
    '{"curator_notes": "Tool-class boundary.", "source_paper_tracker_id": "M14A-P005", "topic_id": "M14B-T003", "tracker_id": "M14B-C005"}'
  FROM _m14_paper_map p
  WHERE p.tracker_id = 'M14A-P005'
  RETURNING claim_id
)
INSERT INTO _m14_claim_map (tracker_id, claim_id) SELECT 'M14B-C005', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'SCI epigenetic landmarks are relevant target-selection evidence for axon regeneration, glial activation, neurogenesis, and secondary injury.',
    'synthesis',
    'high',
    'Module 14A tracker / source-page, full-text PMC, or review metadata',
    'high',
    '{"curator_notes": "SCI context claim.", "source_paper_tracker_id": "M14A-P006", "topic_id": "M14B-T004", "tracker_id": "M14B-C006"}'
  FROM _m14_paper_map p
  WHERE p.tracker_id = 'M14A-P006'
  RETURNING claim_id
)
INSERT INTO _m14_claim_map (tracker_id, claim_id) SELECT 'M14B-C006', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Injury-responsive enhancer regulation can nominate regeneration-associated loci that may later be tested with CRISPR epigenome editing.',
    'target nomination',
    'high',
    'Module 14A tracker / source-page, full-text PMC, or review metadata',
    'high',
    '{"curator_notes": "Enhancer target claim.", "source_paper_tracker_id": "M14A-P007", "topic_id": "M14B-T004", "tracker_id": "M14B-C007"}'
  FROM _m14_paper_map p
  WHERE p.tracker_id = 'M14A-P007'
  RETURNING claim_id
)
INSERT INTO _m14_claim_map (tracker_id, claim_id) SELECT 'M14B-C007', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Injury-responsive enhancers provide a route to cell-state-specific targeting in injured CNS tissue, including reactive astrocyte states after spinal cord injury.',
    'tool validation',
    'medium',
    'Module 14A tracker / source-page, full-text PMC, or review metadata',
    'medium',
    '{"curator_notes": "Source-page confidence retained.", "source_paper_tracker_id": "M14A-P008", "topic_id": "M14B-T005", "tracker_id": "M14B-C008"}'
  FROM _m14_paper_map p
  WHERE p.tracker_id = 'M14A-P008'
  RETURNING claim_id
)
INSERT INTO _m14_claim_map (tracker_id, claim_id) SELECT 'M14B-C008', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'CRISPR-validated regeneration screens nominate target genes for regulatory repression but do not prove dCas9 epigenome-editing efficacy by themselves.',
    'boundary condition',
    'medium',
    'Module 14A tracker / source-page, full-text PMC, or review metadata',
    'medium',
    '{"curator_notes": "Comparator boundary.", "source_paper_tracker_id": "M14A-P009", "topic_id": "M14B-T006", "tracker_id": "M14B-C009"}'
  FROM _m14_paper_map p
  WHERE p.tracker_id = 'M14A-P009'
  RETURNING claim_id
)
INSERT INTO _m14_claim_map (tracker_id, claim_id) SELECT 'M14B-C009', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'KLF-family repression is a credible intrinsic-growth target logic for CRISPRi-style neuroregeneration experiments.',
    'target nomination',
    'high',
    'Module 14A tracker / source-page, full-text PMC, or review metadata',
    'high',
    '{"curator_notes": "Comparator target evidence.", "source_paper_tracker_id": "M14A-P010", "topic_id": "M14B-T006", "tracker_id": "M14B-C010"}'
  FROM _m14_paper_map p
  WHERE p.tracker_id = 'M14A-P010'
  RETURNING claim_id
)
INSERT INTO _m14_claim_map (tracker_id, claim_id) SELECT 'M14B-C010', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'dCas9-p300 supports a promoter/enhancer acetylation strategy for activating silent or insufficiently active growth-associated loci.',
    'tool validation',
    'medium',
    'Module 14A tracker / source-page, full-text PMC, or review metadata',
    'medium',
    '{"curator_notes": "Activation effector claim.", "source_paper_tracker_id": "M14A-P011", "topic_id": "M14B-T003", "tracker_id": "M14B-C011"}'
  FROM _m14_paper_map p
  WHERE p.tracker_id = 'M14A-P011'
  RETURNING claim_id
)
INSERT INTO _m14_claim_map (tracker_id, claim_id) SELECT 'M14B-C011', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'CRISPRi/a establishes programmable transcriptional control without DNA cleavage, which is the core distinction from permanent genome editing.',
    'tool validation',
    'medium',
    'Module 14A tracker / source-page, full-text PMC, or review metadata',
    'medium',
    '{"curator_notes": "Foundational tool claim.", "source_paper_tracker_id": "M14A-P012", "topic_id": "M14B-T003", "tracker_id": "M14B-C012"}'
  FROM _m14_paper_map p
  WHERE p.tracker_id = 'M14A-P012'
  RETURNING claim_id
)
INSERT INTO _m14_claim_map (tracker_id, claim_id) SELECT 'M14B-C012', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Multiplexed CRISPRa can be used as a discovery strategy for coordinated pro-regenerative gene programs.',
    'tool validation',
    'medium',
    'Module 14A tracker / source-page, full-text PMC, or review metadata',
    'medium',
    '{"curator_notes": "Platform claim.", "source_paper_tracker_id": "M14A-P013", "topic_id": "M14B-T003", "tracker_id": "M14B-C013"}'
  FROM _m14_paper_map p
  WHERE p.tracker_id = 'M14A-P013'
  RETURNING claim_id
)
INSERT INTO _m14_claim_map (tracker_id, claim_id) SELECT 'M14B-C013', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'In vivo CNS CRISPRa examples support feasibility of endogenous gene activation in neural tissue but remain disease/model-specific.',
    'boundary condition',
    'medium',
    'Module 14A tracker / source-page, full-text PMC, or review metadata',
    'medium',
    '{"curator_notes": "Translation comparator.", "source_paper_tracker_id": "M14A-P014", "topic_id": "M14B-T007", "tracker_id": "M14B-C014"}'
  FROM _m14_paper_map p
  WHERE p.tracker_id = 'M14A-P014'
  RETURNING claim_id
)
INSERT INTO _m14_claim_map (tracker_id, claim_id) SELECT 'M14B-C014', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'CNS CRISPR translation requires delivery, specificity, immune/off-target, durability, and tool-class safety boundaries.',
    'boundary condition',
    'high',
    'Module 14A tracker / source-page, full-text PMC, or review metadata',
    'high',
    '{"curator_notes": "Safety boundary.", "source_paper_tracker_id": "M14A-P015", "topic_id": "M14B-T007", "tracker_id": "M14B-C015"}'
  FROM _m14_paper_map p
  WHERE p.tracker_id = 'M14A-P015'
  RETURNING claim_id
)
INSERT INTO _m14_claim_map (tracker_id, claim_id) SELECT 'M14B-C015', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'CRISPR epigenome editing is best framed as a reversible/flexible neuroregeneration platform until direct in vivo SCI efficacy and safety are shown.',
    'synthesis',
    'high',
    'Module 14A tracker / source-page, full-text PMC, or review metadata',
    'high',
    '{"curator_notes": "Project-level boundary.", "source_paper_tracker_id": "M14A-P016", "topic_id": "M14B-T008", "tracker_id": "M14B-C016"}'
  FROM _m14_paper_map p
  WHERE p.tracker_id = 'M14A-P016'
  RETURNING claim_id
)
INSERT INTO _m14_claim_map (tracker_id, claim_id) SELECT 'M14B-C016', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct first-pass link from PTEN dCas9-KRAB claim to observation.", "strength": "medium", "tracker_id": "M14B-L001"}'
  FROM _m14_claim_map c
  JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O001'
  WHERE c.tracker_id = 'M14B-C001'
  RETURNING link_id
)
INSERT INTO _m14_link_map (tracker_id, link_id) SELECT 'M14B-L001', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct first-pass link from neuronal CRISPRa claim to observation.", "strength": "high", "tracker_id": "M14B-L002"}'
  FROM _m14_claim_map c
  JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O002'
  WHERE c.tracker_id = 'M14B-C002'
  RETURNING link_id
)
INSERT INTO _m14_link_map (tracker_id, link_id) SELECT 'M14B-L002', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct first-pass link preserving review-level confidence.", "strength": "medium", "tracker_id": "M14B-L003"}'
  FROM _m14_claim_map c
  JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O003'
  WHERE c.tracker_id = 'M14B-C003'
  RETURNING link_id
)
INSERT INTO _m14_link_map (tracker_id, link_id) SELECT 'M14B-L003', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct first-pass link preserving full-text review confidence.", "strength": "high", "tracker_id": "M14B-L004"}'
  FROM _m14_claim_map c
  JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O004'
  WHERE c.tracker_id = 'M14B-C004'
  RETURNING link_id
)
INSERT INTO _m14_link_map (tracker_id, link_id) SELECT 'M14B-L004', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct first-pass link preserving full-text review confidence.", "strength": "high", "tracker_id": "M14B-L005"}'
  FROM _m14_claim_map c
  JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O005'
  WHERE c.tracker_id = 'M14B-C005'
  RETURNING link_id
)
INSERT INTO _m14_link_map (tracker_id, link_id) SELECT 'M14B-L005', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct first-pass link preserving SCI epigenetic context.", "strength": "high", "tracker_id": "M14B-L006"}'
  FROM _m14_claim_map c
  JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O006'
  WHERE c.tracker_id = 'M14B-C006'
  RETURNING link_id
)
INSERT INTO _m14_link_map (tracker_id, link_id) SELECT 'M14B-L006', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct first-pass link from enhancer claim to observation.", "strength": "high", "tracker_id": "M14B-L007"}'
  FROM _m14_claim_map c
  JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O007'
  WHERE c.tracker_id = 'M14B-C007'
  RETURNING link_id
)
INSERT INTO _m14_link_map (tracker_id, link_id) SELECT 'M14B-L007', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct first-pass link preserving source-page confidence.", "strength": "medium", "tracker_id": "M14B-L008"}'
  FROM _m14_claim_map c
  JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O008'
  WHERE c.tracker_id = 'M14B-C008'
  RETURNING link_id
)
INSERT INTO _m14_link_map (tracker_id, link_id) SELECT 'M14B-L008', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct first-pass comparator link.", "strength": "medium", "tracker_id": "M14B-L009"}'
  FROM _m14_claim_map c
  JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O009'
  WHERE c.tracker_id = 'M14B-C009'
  RETURNING link_id
)
INSERT INTO _m14_link_map (tracker_id, link_id) SELECT 'M14B-L009', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct first-pass KLF4 target link.", "strength": "high", "tracker_id": "M14B-L010"}'
  FROM _m14_claim_map c
  JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O010'
  WHERE c.tracker_id = 'M14B-C010'
  RETURNING link_id
)
INSERT INTO _m14_link_map (tracker_id, link_id) SELECT 'M14B-L010', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct first-pass p300 tool link.", "strength": "medium", "tracker_id": "M14B-L011"}'
  FROM _m14_claim_map c
  JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O011'
  WHERE c.tracker_id = 'M14B-C011'
  RETURNING link_id
)
INSERT INTO _m14_link_map (tracker_id, link_id) SELECT 'M14B-L011', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct first-pass CRISPRi/a platform link.", "strength": "medium", "tracker_id": "M14B-L012"}'
  FROM _m14_claim_map c
  JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O012'
  WHERE c.tracker_id = 'M14B-C012'
  RETURNING link_id
)
INSERT INTO _m14_link_map (tracker_id, link_id) SELECT 'M14B-L012', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct first-pass SAM CRISPRa link.", "strength": "medium", "tracker_id": "M14B-L013"}'
  FROM _m14_claim_map c
  JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O013'
  WHERE c.tracker_id = 'M14B-C013'
  RETURNING link_id
)
INSERT INTO _m14_link_map (tracker_id, link_id) SELECT 'M14B-L013', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct first-pass in vivo CNS CRISPRa comparator link.", "strength": "medium", "tracker_id": "M14B-L014"}'
  FROM _m14_claim_map c
  JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O014'
  WHERE c.tracker_id = 'M14B-C014'
  RETURNING link_id
)
INSERT INTO _m14_link_map (tracker_id, link_id) SELECT 'M14B-L014', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct first-pass CNS safety boundary link.", "strength": "high", "tracker_id": "M14B-L015"}'
  FROM _m14_claim_map c
  JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O015'
  WHERE c.tracker_id = 'M14B-C015'
  RETURNING link_id
)
INSERT INTO _m14_link_map (tracker_id, link_id) SELECT 'M14B-L015', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct first-pass neuroregeneration synthesis link.", "strength": "high", "tracker_id": "M14B-L016"}'
  FROM _m14_claim_map c
  JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O016'
  WHERE c.tracker_id = 'M14B-C016'
  RETURNING link_id
)
INSERT INTO _m14_link_map (tracker_id, link_id) SELECT 'M14B-L016', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Target-discovery comparator supports repression-target logic but not dCas9 efficacy.", "strength": "low", "tracker_id": "M14B-L017"}'
  FROM _m14_claim_map c
  JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O009'
  WHERE c.tracker_id = 'M14B-C001'
  RETURNING link_id
)
INSERT INTO _m14_link_map (tracker_id, link_id) SELECT 'M14B-L017', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "KLF4 repression comparator supports intrinsic-growth target boundary.", "strength": "low", "tracker_id": "M14B-L018"}'
  FROM _m14_claim_map c
  JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O010'
  WHERE c.tracker_id = 'M14B-C001'
  RETURNING link_id
)
INSERT INTO _m14_link_map (tracker_id, link_id) SELECT 'M14B-L018', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "CNS CRISPR review supports neuronal tool context.", "strength": "low", "tracker_id": "M14B-L019"}'
  FROM _m14_claim_map c
  JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O004'
  WHERE c.tracker_id = 'M14B-C002'
  RETURNING link_id
)
INSERT INTO _m14_link_map (tracker_id, link_id) SELECT 'M14B-L019', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "In vivo CNS CRISPRa comparator supports translation boundary.", "strength": "low", "tracker_id": "M14B-L020"}'
  FROM _m14_claim_map c
  JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O014'
  WHERE c.tracker_id = 'M14B-C002'
  RETURNING link_id
)
INSERT INTO _m14_link_map (tracker_id, link_id) SELECT 'M14B-L020', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "p300 tool row supports effector-specific activation boundary.", "strength": "low", "tracker_id": "M14B-L021"}'
  FROM _m14_claim_map c
  JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O011'
  WHERE c.tracker_id = 'M14B-C003'
  RETURNING link_id
)
INSERT INTO _m14_link_map (tracker_id, link_id) SELECT 'M14B-L021', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Foundational CRISPRi/a row supports activation/repression distinction.", "strength": "low", "tracker_id": "M14B-L022"}'
  FROM _m14_claim_map c
  JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O012'
  WHERE c.tracker_id = 'M14B-C003'
  RETURNING link_id
)
INSERT INTO _m14_link_map (tracker_id, link_id) SELECT 'M14B-L022', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "SAM platform supports multiplexed activation boundary.", "strength": "low", "tracker_id": "M14B-L023"}'
  FROM _m14_claim_map c
  JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O013'
  WHERE c.tracker_id = 'M14B-C003'
  RETURNING link_id
)
INSERT INTO _m14_link_map (tracker_id, link_id) SELECT 'M14B-L023', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Neuron-optimized CRISPRa row supports CNS dCas9 platform claim.", "strength": "low", "tracker_id": "M14B-L024"}'
  FROM _m14_claim_map c
  JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O002'
  WHERE c.tracker_id = 'M14B-C004'
  RETURNING link_id
)
INSERT INTO _m14_link_map (tracker_id, link_id) SELECT 'M14B-L024', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Neuroepigenome review supports tool-class distinction.", "strength": "low", "tracker_id": "M14B-L025"}'
  FROM _m14_claim_map c
  JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O003'
  WHERE c.tracker_id = 'M14B-C005'
  RETURNING link_id
)
INSERT INTO _m14_link_map (tracker_id, link_id) SELECT 'M14B-L025', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "WNT3A enhancer row supports SCI epigenetic target logic.", "strength": "low", "tracker_id": "M14B-L026"}'
  FROM _m14_claim_map c
  JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O007'
  WHERE c.tracker_id = 'M14B-C006'
  RETURNING link_id
)
INSERT INTO _m14_link_map (tracker_id, link_id) SELECT 'M14B-L026', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "SCI injury enhancer row supports cell-state target logic.", "strength": "low", "tracker_id": "M14B-L027"}'
  FROM _m14_claim_map c
  JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O008'
  WHERE c.tracker_id = 'M14B-C006'
  RETURNING link_id
)
INSERT INTO _m14_link_map (tracker_id, link_id) SELECT 'M14B-L027', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "dCas9-p300 row supports possible enhancer activation strategy.", "strength": "low", "tracker_id": "M14B-L028"}'
  FROM _m14_claim_map c
  JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O011'
  WHERE c.tracker_id = 'M14B-C007'
  RETURNING link_id
)
INSERT INTO _m14_link_map (tracker_id, link_id) SELECT 'M14B-L028', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "CNS CRISPR safety review contextualizes delivery boundary.", "strength": "low", "tracker_id": "M14B-L029"}'
  FROM _m14_claim_map c
  JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O015'
  WHERE c.tracker_id = 'M14B-C008'
  RETURNING link_id
)
INSERT INTO _m14_link_map (tracker_id, link_id) SELECT 'M14B-L029', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "PTEN dCas9 row distinguishes direct epigenome editing from target discovery.", "strength": "low", "tracker_id": "M14B-L030"}'
  FROM _m14_claim_map c
  JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O001'
  WHERE c.tracker_id = 'M14B-C009'
  RETURNING link_id
)
INSERT INTO _m14_link_map (tracker_id, link_id) SELECT 'M14B-L030', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Optic nerve screen supports target-discovery comparator logic.", "strength": "low", "tracker_id": "M14B-L031"}'
  FROM _m14_claim_map c
  JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O009'
  WHERE c.tracker_id = 'M14B-C010'
  RETURNING link_id
)
INSERT INTO _m14_link_map (tracker_id, link_id) SELECT 'M14B-L031', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "WNT3A enhancer row contextualizes acetylation target logic.", "strength": "low", "tracker_id": "M14B-L032"}'
  FROM _m14_claim_map c
  JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O007'
  WHERE c.tracker_id = 'M14B-C011'
  RETURNING link_id
)
INSERT INTO _m14_link_map (tracker_id, link_id) SELECT 'M14B-L032', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Neuroepigenome review supports non-cleaving regulatory edit boundary.", "strength": "low", "tracker_id": "M14B-L033"}'
  FROM _m14_claim_map c
  JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O003'
  WHERE c.tracker_id = 'M14B-C012'
  RETURNING link_id
)
INSERT INTO _m14_link_map (tracker_id, link_id) SELECT 'M14B-L033', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Neuronal CRISPRa row contextualizes multiplexed neuronal activation.", "strength": "low", "tracker_id": "M14B-L034"}'
  FROM _m14_claim_map c
  JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O002'
  WHERE c.tracker_id = 'M14B-C013'
  RETURNING link_id
)
INSERT INTO _m14_link_map (tracker_id, link_id) SELECT 'M14B-L034', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Neuronal CRISPRa platform supports in vivo CNS feasibility logic.", "strength": "low", "tracker_id": "M14B-L035"}'
  FROM _m14_claim_map c
  JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O002'
  WHERE c.tracker_id = 'M14B-C014'
  RETURNING link_id
)
INSERT INTO _m14_link_map (tracker_id, link_id) SELECT 'M14B-L035', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Neuroepigenome editing review contextualizes safety/durability concerns.", "strength": "low", "tracker_id": "M14B-L036"}'
  FROM _m14_claim_map c
  JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O003'
  WHERE c.tracker_id = 'M14B-C015'
  RETURNING link_id
)
INSERT INTO _m14_link_map (tracker_id, link_id) SELECT 'M14B-L036', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "In vivo CNS CRISPRa example contextualizes delivery boundary.", "strength": "low", "tracker_id": "M14B-L037"}'
  FROM _m14_claim_map c
  JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O014'
  WHERE c.tracker_id = 'M14B-C015'
  RETURNING link_id
)
INSERT INTO _m14_link_map (tracker_id, link_id) SELECT 'M14B-L037', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Direct PTEN row supports platform but remains in vitro.", "strength": "low", "tracker_id": "M14B-L038"}'
  FROM _m14_claim_map c
  JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O001'
  WHERE c.tracker_id = 'M14B-C016'
  RETURNING link_id
)
INSERT INTO _m14_link_map (tracker_id, link_id) SELECT 'M14B-L038', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Injury enhancer row supports cell-state-targeted platform logic.", "strength": "low", "tracker_id": "M14B-L039"}'
  FROM _m14_claim_map c
  JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O008'
  WHERE c.tracker_id = 'M14B-C016'
  RETURNING link_id
)
INSERT INTO _m14_link_map (tracker_id, link_id) SELECT 'M14B-L039', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "CNS CRISPR review supports safety boundary for project-level claim.", "strength": "low", "tracker_id": "M14B-L040"}'
  FROM _m14_claim_map c
  JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O015'
  WHERE c.tracker_id = 'M14B-C016'
  RETURNING link_id
)
INSERT INTO _m14_link_map (tracker_id, link_id) SELECT 'M14B-L040', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'CRISPR/dCas9 epigenome editing is consensus-ready as a regeneration-relevant regulatory strategy because dCas9-KRAB can repress PTEN in neural cells, induce local repressive chromatin marks, and improve neurite outgrowth; however, this direct evidence is still primarily in vitro and should not be overstated as in vivo SCI efficacy.',
    'M14B-T001',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M14B-B001", "M14B-B002", "M14B-B003", "M14B-B004", "M14B-B005", "M14B-B006", "M14B-B007", "M14B-B008"], "claim_tracker_ids": ["M14B-C001", "M14B-C002", "M14B-C003"], "consensus_draft_id": "M14B-S001", "observation_tracker_ids": ["M14B-O001", "M14B-O002", "M14B-O003"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 14 first-pass curation freeze.", "topic_id": "M14B-T001"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m14_consensus_map (tracker_id, consensus_id) SELECT 'M14B-S001', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m14_consensus_map c
JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O001'
WHERE c.tracker_id = 'M14B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m14_consensus_map c
JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O002'
WHERE c.tracker_id = 'M14B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m14_consensus_map c
JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O003'
WHERE c.tracker_id = 'M14B-S001';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Neuron-optimized CRISPRa/i systems provide a practical platform for tunable endogenous gene regulation in post-mitotic neural cells, including promoter-selective and multiplexed activation, but each claim must preserve vector, cell type, guide, expression, and in vivo/in vitro boundaries.',
    'M14B-T002',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M14B-B001", "M14B-B002", "M14B-B003", "M14B-B004", "M14B-B005", "M14B-B006", "M14B-B007", "M14B-B008"], "claim_tracker_ids": ["M14B-C002", "M14B-C003", "M14B-C004"], "consensus_draft_id": "M14B-S002", "observation_tracker_ids": ["M14B-O002", "M14B-O003", "M14B-O004"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 14 first-pass curation freeze.", "topic_id": "M14B-T002"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m14_consensus_map (tracker_id, consensus_id) SELECT 'M14B-S002', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m14_consensus_map c
JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O002'
WHERE c.tracker_id = 'M14B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m14_consensus_map c
JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O003'
WHERE c.tracker_id = 'M14B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m14_consensus_map c
JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O004'
WHERE c.tracker_id = 'M14B-S002';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'CRISPR epigenome editing should be organized by effector mechanism rather than by the word CRISPR alone: repression, activation, acetylation, methylation, demethylation, and scaffolded activator systems produce different chromatin states, durations, and safety questions.',
    'M14B-T003',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M14B-B001", "M14B-B002", "M14B-B003", "M14B-B004", "M14B-B005", "M14B-B006", "M14B-B007", "M14B-B008"], "claim_tracker_ids": ["M14B-C003", "M14B-C004", "M14B-C005"], "consensus_draft_id": "M14B-S003", "observation_tracker_ids": ["M14B-O003", "M14B-O004", "M14B-O005"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 14 first-pass curation freeze.", "topic_id": "M14B-T003"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m14_consensus_map (tracker_id, consensus_id) SELECT 'M14B-S003', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m14_consensus_map c
JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O003'
WHERE c.tracker_id = 'M14B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m14_consensus_map c
JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O004'
WHERE c.tracker_id = 'M14B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m14_consensus_map c
JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O005'
WHERE c.tracker_id = 'M14B-S003';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'SCI and CNS injury epigenetic maps are useful for nominating regulatory targets because injury changes chromatin, enhancer activity, glial activation, neurogenesis, and axon-growth programs, but map evidence must be followed by perturbation before causal repair claims.',
    'M14B-T004',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M14B-B001", "M14B-B002", "M14B-B003", "M14B-B004", "M14B-B005", "M14B-B006", "M14B-B007", "M14B-B008"], "claim_tracker_ids": ["M14B-C006", "M14B-C007", "M14B-C008"], "consensus_draft_id": "M14B-S004", "observation_tracker_ids": ["M14B-O006", "M14B-O007", "M14B-O008"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 14 first-pass curation freeze.", "topic_id": "M14B-T004"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m14_consensus_map (tracker_id, consensus_id) SELECT 'M14B-S004', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m14_consensus_map c
JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O006'
WHERE c.tracker_id = 'M14B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m14_consensus_map c
JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O007'
WHERE c.tracker_id = 'M14B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m14_consensus_map c
JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O008'
WHERE c.tracker_id = 'M14B-S004';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Injury-responsive enhancers create an important bridge between epigenome editing and cell-state specificity: they may help target reactive CNS states such as astrocytes after SCI, but enhancer targeting is a delivery/regulatory specificity claim until linked to repair endpoints.',
    'M14B-T005',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M14B-B001", "M14B-B002", "M14B-B003", "M14B-B004", "M14B-B005", "M14B-B006", "M14B-B007", "M14B-B008"], "claim_tracker_ids": ["M14B-C007", "M14B-C008"], "consensus_draft_id": "M14B-S005", "observation_tracker_ids": ["M14B-O007", "M14B-O008"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 14 first-pass curation freeze.", "topic_id": "M14B-T005"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m14_consensus_map (tracker_id, consensus_id) SELECT 'M14B-S005', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m14_consensus_map c
JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O007'
WHERE c.tracker_id = 'M14B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m14_consensus_map c
JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O008'
WHERE c.tracker_id = 'M14B-S005';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Neuroregeneration screens and intrinsic-growth target studies identify candidate loci for CRISPRi/a, including PTEN/KLF-style repression and regeneration-associated gene activation, but target discovery is not equivalent to dCas9 epigenome-editing efficacy.',
    'M14B-T006',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M14B-B001", "M14B-B002", "M14B-B003", "M14B-B004", "M14B-B005", "M14B-B006", "M14B-B007", "M14B-B008"], "claim_tracker_ids": ["M14B-C009", "M14B-C010"], "consensus_draft_id": "M14B-S006", "observation_tracker_ids": ["M14B-O009", "M14B-O010"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 14 first-pass curation freeze.", "topic_id": "M14B-T006"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m14_consensus_map (tracker_id, consensus_id) SELECT 'M14B-S006', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m14_consensus_map c
JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O009'
WHERE c.tracker_id = 'M14B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m14_consensus_map c
JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O010'
WHERE c.tracker_id = 'M14B-S006';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'CNS delivery and safety are central boundaries for CRISPR epigenome editing: vector capacity, cell specificity, immune response, off-target regulation, expression duration, reversibility, and durability must be recorded before translational neuroregeneration claims.',
    'M14B-T007',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M14B-B001", "M14B-B002", "M14B-B003", "M14B-B004", "M14B-B005", "M14B-B006", "M14B-B007", "M14B-B008"], "claim_tracker_ids": ["M14B-C011", "M14B-C012", "M14B-C013", "M14B-C014", "M14B-C015"], "consensus_draft_id": "M14B-S007", "observation_tracker_ids": ["M14B-O011", "M14B-O012", "M14B-O013", "M14B-O014", "M14B-O015"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 14 first-pass curation freeze.", "topic_id": "M14B-T007"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m14_consensus_map (tracker_id, consensus_id) SELECT 'M14B-S007', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m14_consensus_map c
JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O011'
WHERE c.tracker_id = 'M14B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m14_consensus_map c
JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O012'
WHERE c.tracker_id = 'M14B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m14_consensus_map c
JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O013'
WHERE c.tracker_id = 'M14B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m14_consensus_map c
JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O014'
WHERE c.tracker_id = 'M14B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m14_consensus_map c
JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O015'
WHERE c.tracker_id = 'M14B-S007';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Module 14 should be used as a programmable regulatory-editing layer for neuroregeneration: candidate experiments should specify target locus, effector, guide design, delivery vehicle, target cell, chromatin state, model, and endpoint before linking CRISPR epigenome editing to SCI reconstruction, conditioning, graft integration, or axon repair.',
    'M14B-T008',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M14B-B001", "M14B-B002", "M14B-B003", "M14B-B004", "M14B-B005", "M14B-B006", "M14B-B007", "M14B-B008"], "claim_tracker_ids": ["M14B-C014", "M14B-C015", "M14B-C016"], "consensus_draft_id": "M14B-S008", "observation_tracker_ids": ["M14B-O014", "M14B-O015", "M14B-O016"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 14 first-pass curation freeze.", "topic_id": "M14B-T008"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m14_consensus_map (tracker_id, consensus_id) SELECT 'M14B-S008', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m14_consensus_map c
JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O014'
WHERE c.tracker_id = 'M14B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m14_consensus_map c
JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O015'
WHERE c.tracker_id = 'M14B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m14_consensus_map c
JOIN _m14_observation_map o ON o.tracker_id = 'M14B-O016'
WHERE c.tracker_id = 'M14B-S008';

DO $$
DECLARE
  paper_count INTEGER;
  experiment_count INTEGER;
  observation_count INTEGER;
  claim_count INTEGER;
  link_count INTEGER;
  consensus_count INTEGER;
  consensus_observation_count INTEGER;
BEGIN
  SELECT COUNT(*) INTO paper_count FROM _m14_paper_map;
  SELECT COUNT(*) INTO experiment_count FROM _m14_experiment_map;
  SELECT COUNT(*) INTO observation_count FROM _m14_observation_map;
  SELECT COUNT(*) INTO claim_count FROM _m14_claim_map;
  SELECT COUNT(*) INTO link_count FROM _m14_link_map;
  SELECT COUNT(*) INTO consensus_count FROM _m14_consensus_map;
  SELECT COUNT(*) INTO consensus_observation_count
  FROM Consensus_Observation co
  JOIN _m14_consensus_map cm ON cm.consensus_id = co.consensus_id;
  IF paper_count <> 16 THEN RAISE EXCEPTION 'Expected 16 papers, found %', paper_count; END IF;
  IF experiment_count <> 16 THEN RAISE EXCEPTION 'Unexpected experiment count %', experiment_count; END IF;
  IF observation_count <> 16 THEN RAISE EXCEPTION 'Expected 16 observations, found %', observation_count; END IF;
  IF claim_count <> 16 THEN RAISE EXCEPTION 'Expected 16 claims, found %', claim_count; END IF;
  IF link_count <> 40 THEN RAISE EXCEPTION 'Expected 40 evidence links, found %', link_count; END IF;
  IF consensus_count <> 8 THEN RAISE EXCEPTION 'Expected 8 consensus rows, found %', consensus_count; END IF;
  IF consensus_observation_count <> 24 THEN RAISE EXCEPTION 'Unexpected consensus-observation count %', consensus_observation_count; END IF;
END $$;

COMMIT;
