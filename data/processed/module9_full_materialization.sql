-- Module 9B full first-pass materialization generated from tracker-derived JSON.
-- This script is intended for a fresh database loaded with schema/schema.sql and scripts/seed_controlled_vocab.sql.
BEGIN;

CREATE TEMP TABLE _m9_paper_map (tracker_id TEXT PRIMARY KEY, paper_id INTEGER NOT NULL);
CREATE TEMP TABLE _m9_paradigm_map (tracker_id TEXT PRIMARY KEY, paradigm_id INTEGER NOT NULL);
CREATE TEMP TABLE _m9_experiment_map (tracker_id TEXT PRIMARY KEY, experiment_id INTEGER NOT NULL);
CREATE TEMP TABLE _m9_observation_map (tracker_id TEXT PRIMARY KEY, observation_id INTEGER NOT NULL);
CREATE TEMP TABLE _m9_claim_map (tracker_id TEXT PRIMARY KEY, claim_id INTEGER NOT NULL);
CREATE TEMP TABLE _m9_link_map (tracker_id TEXT PRIMARY KEY, link_id INTEGER NOT NULL);
CREATE TEMP TABLE _m9_consensus_map (tracker_id TEXT PRIMARY KEY, consensus_id INTEGER NOT NULL);

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Engineered thoracic spinal cord organoids for transplantation after spinal cord injury.', 'Zhu Y', 2025,
    NULL, NULL, NULL,
    NULL, NULL, '41136603',
    NULL, '{"curator_notes": "Stem-cell-based neural tissue engineering and spinal cord organoids show promises for spinal cord injury repair.", "module": "Module 9B", "tracker_id": "M9A-P001"}'
  )
  RETURNING paper_id
)
INSERT INTO _m9_paper_map (tracker_id, paper_id) SELECT 'M9A-P001', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Harnessing developmental dynamics of spinal cord extracellular matrix improves regenerative potential of spinal cord organoids.', 'Sun Z', 2024,
    NULL, NULL, NULL,
    NULL, NULL, '38565140',
    NULL, '{"curator_notes": "Neonatal spinal cord tissues exhibit remarkable regenerative capabilities as compared to adult spinal cord tissues", "module": "Module 9B", "tracker_id": "M9A-P002"}'
  )
  RETURNING paper_id
)
INSERT INTO _m9_paper_map (tracker_id, paper_id) SELECT 'M9A-P002', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Progress in spinal cord organoid research: advancing understanding of neural development, disease modelling, and regenerative medicine.', 'Huang R', 2025,
    NULL, NULL, NULL,
    NULL, NULL, '39872925',
    NULL, '{"curator_notes": "Stem cell-derived spinal cord organoids (SCOs) have revolutionised the study of spinal cord development and disease", "module": "Module 9B", "tracker_id": "M9A-P003"}'
  )
  RETURNING paper_id
)
INSERT INTO _m9_paper_map (tracker_id, paper_id) SELECT 'M9A-P003', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Injury and therapy in a human spinal cord organoid.', 'Takata N', 2026,
    NULL, NULL, NULL,
    NULL, NULL, '41673139',
    NULL, '{"curator_notes": "Damage to the spinal cord can lead to irreversible paralysis and loss of sensory function, but translation of", "module": "Module 9B", "tracker_id": "M9A-P004"}'
  )
  RETURNING paper_id
)
INSERT INTO _m9_paper_map (tracker_id, paper_id) SELECT 'M9A-P004', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'GelMA Hydrogel Encapsulating iPSC-Derived Human Spinal Cord Organoids Enhances Neural Regeneration and Restores Motor Function in Rat Spinal Cord Injury.', 'Li Y', 2025,
    NULL, NULL, NULL,
    NULL, NULL, '41051068',
    NULL, '{"curator_notes": "Spinal cord injury (SCI) severely compromises neural regeneration due to limited intrinsic repair capacity. Combining", "module": "Module 9B", "tracker_id": "M9A-P005"}'
  )
  RETURNING paper_id
)
INSERT INTO _m9_paper_map (tracker_id, paper_id) SELECT 'M9A-P005', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Generation of engineered human spinal cord organoid in channel-patterned collagen and transplantation for spinal cord regeneration.', 'Ma L', 2025,
    NULL, NULL, NULL,
    NULL, NULL, '41061610',
    NULL, '{"curator_notes": "The construction of artificially manipulable tissue-engineered human spinal cord organoids (HSCO) in vitro is crucial", "module": "Module 9B", "tracker_id": "M9A-P006"}'
  )
  RETURNING paper_id
)
INSERT INTO _m9_paper_map (tracker_id, paper_id) SELECT 'M9A-P006', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Generation of Neural Organoids and Their Application in Disease Modeling and Regenerative Medicine.', 'Huang R', 2025,
    NULL, NULL, NULL,
    NULL, NULL, '40411400',
    NULL, '{"curator_notes": "The complexity and precision of the human nervous system have posed significant challenges for researchers seeking", "module": "Module 9B", "tracker_id": "M9A-P007"}'
  )
  RETURNING paper_id
)
INSERT INTO _m9_paper_map (tracker_id, paper_id) SELECT 'M9A-P007', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Construction of a niche-specific spinal white matter-like tissue to promote directional axon regeneration and myelination for rat spinal cord injury repair.', 'Lai BQ', 2021,
    NULL, NULL, NULL,
    NULL, NULL, '34938909',
    NULL, '{"curator_notes": "Directional axon regeneration and remyelination are crucial for repair of spinal cord injury (SCI), but existing", "module": "Module 9B", "tracker_id": "M9A-P008"}'
  )
  RETURNING paper_id
)
INSERT INTO _m9_paper_map (tracker_id, paper_id) SELECT 'M9A-P008', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Trichostatin A-primed spinal cord organoids alleviate oxidative stress and improve recovery after spinal cord injury involving the NRF2/HO-1 signaling pathway.', 'Wang Y', 2026,
    NULL, NULL, NULL,
    NULL, NULL, '42250855',
    NULL, '{"curator_notes": "Oxidative stress represents a fundamental pathological driver of the secondary injury cascade following traumatic", "module": "Module 9B", "tracker_id": "M9A-P009"}'
  )
  RETURNING paper_id
)
INSERT INTO _m9_paper_map (tracker_id, paper_id) SELECT 'M9A-P009', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Current status of neural progenitor/stem cells for spinal cord injury: fundamental research and clinical trials.', 'Chen XX', 2026,
    NULL, NULL, NULL,
    NULL, NULL, '42266586',
    NULL, '{"curator_notes": "Spinal cord injury (SCI) causes irreversible neurological deficits and represents a major global health and", "module": "Module 9B", "tracker_id": "M9A-P010"}'
  )
  RETURNING paper_id
)
INSERT INTO _m9_paper_map (tracker_id, paper_id) SELECT 'M9A-P010', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'The Evolving Role of Induced Pluripotent Stem Cells and Cerebral Organoids in Treating and Modeling Neurosurgical Diseases.', 'Jovanovich N', 2021,
    NULL, NULL, NULL,
    NULL, NULL, '34454068',
    NULL, '{"curator_notes": "Over the past decade, the use of induced pluripotent stem cells (IPSCs), as both direct therapeutics and building", "module": "Module 9B", "tracker_id": "M9A-P011"}'
  )
  RETURNING paper_id
)
INSERT INTO _m9_paper_map (tracker_id, paper_id) SELECT 'M9A-P011', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Integrating 3D bioprinting and neural stem cell therapy for central nervous system repair: implications for regenerative neurosurgery.', 'Guo Y', 2026,
    NULL, NULL, NULL,
    NULL, NULL, '41982329',
    NULL, '{"curator_notes": "The limited regenerative capacity of the central nervous system (CNS)poses a major challenge in neurosurgical", "module": "Module 9B", "tracker_id": "M9A-P012"}'
  )
  RETURNING paper_id
)
INSERT INTO _m9_paper_map (tracker_id, paper_id) SELECT 'M9A-P012', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Graphene-collagen cryogel controls neuroinflammation and fosters accelerated axonal regeneration in spinal cord injury.', 'Agarwal G', 2022,
    NULL, NULL, NULL,
    NULL, NULL, '35882128',
    NULL, '{"curator_notes": "Spinal cord injury (SCI) is a devastating condition resulting in loss of motor function. The pathology of SCI is", "module": "Module 9B", "tracker_id": "M9A-P013"}'
  )
  RETURNING paper_id
)
INSERT INTO _m9_paper_map (tracker_id, paper_id) SELECT 'M9A-P013', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Spontaneous regeneration of intrinsic spinal cord axons in a novel spinal cord slice culture model.', 'Bonnici B', 2008,
    NULL, NULL, NULL,
    NULL, NULL, '18513321',
    NULL, '{"curator_notes": "A substantial problem in research concerned with axonal repair is the use of a wide variety of lesion models and the", "module": "Module 9B", "tracker_id": "M9A-P014"}'
  )
  RETURNING paper_id
)
INSERT INTO _m9_paper_map (tracker_id, paper_id) SELECT 'M9A-P014', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Axonal regeneration and neural network reconstruction in mammalian CNS.', 'Nishio T', 2009,
    NULL, NULL, NULL,
    NULL, NULL, '19711121',
    NULL, '{"curator_notes": "Following injury to the white matter of the adult mammalian central nervous system (CNS), severed axons fail to", "module": "Module 9B", "tracker_id": "M9A-P015"}'
  )
  RETURNING paper_id
)
INSERT INTO _m9_paper_map (tracker_id, paper_id) SELECT 'M9A-P015', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Embryonic Cell Grafts in a Culture Model of Spinal Cord Lesion: Neuronal Relay Formation Is Essential for Functional Regeneration.', 'Tscherter A', 2016,
    NULL, NULL, NULL,
    NULL, NULL, '27708562',
    NULL, '{"curator_notes": "Presently there exists no cure for spinal cord injury (SCI). However, transplantation of embryonic tissue into spinal", "module": "Module 9B", "tracker_id": "M9A-P016"}'
  )
  RETURNING paper_id
)
INSERT INTO _m9_paper_map (tracker_id, paper_id) SELECT 'M9A-P016', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Transplantation of mesenchymal stem cells enhances axonal outgrowth and cell survival in an organotypic spinal cord slice culture.', 'Cho JS', 2009,
    NULL, NULL, NULL,
    NULL, NULL, '19429051',
    NULL, '{"curator_notes": "Mesenchymal stem cells (MSCs) have demonstrated a measurable therapeutic effect following transplantation into animal", "module": "Module 9B", "tracker_id": "M9A-P017"}'
  )
  RETURNING paper_id
)
INSERT INTO _m9_paper_map (tracker_id, paper_id) SELECT 'M9A-P017', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 9B curated evidence extraction',
    'First-pass Module 9B in vitro and ex vivo SCI model systems curation for M9A-P001',
    'Tracker-derived materialization from Module_9B_TRACKER.md'
  FROM _m9_paper_map WHERE tracker_id = 'M9A-P001'
  RETURNING paradigm_id
)
INSERT INTO _m9_paradigm_map (tracker_id, paradigm_id) SELECT 'M9A-P001', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 9B curated evidence extraction',
    'First-pass Module 9B in vitro and ex vivo SCI model systems curation for M9A-P002',
    'Tracker-derived materialization from Module_9B_TRACKER.md'
  FROM _m9_paper_map WHERE tracker_id = 'M9A-P002'
  RETURNING paradigm_id
)
INSERT INTO _m9_paradigm_map (tracker_id, paradigm_id) SELECT 'M9A-P002', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 9B curated evidence extraction',
    'First-pass Module 9B in vitro and ex vivo SCI model systems curation for M9A-P003',
    'Tracker-derived materialization from Module_9B_TRACKER.md'
  FROM _m9_paper_map WHERE tracker_id = 'M9A-P003'
  RETURNING paradigm_id
)
INSERT INTO _m9_paradigm_map (tracker_id, paradigm_id) SELECT 'M9A-P003', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 9B curated evidence extraction',
    'First-pass Module 9B in vitro and ex vivo SCI model systems curation for M9A-P004',
    'Tracker-derived materialization from Module_9B_TRACKER.md'
  FROM _m9_paper_map WHERE tracker_id = 'M9A-P004'
  RETURNING paradigm_id
)
INSERT INTO _m9_paradigm_map (tracker_id, paradigm_id) SELECT 'M9A-P004', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 9B curated evidence extraction',
    'First-pass Module 9B in vitro and ex vivo SCI model systems curation for M9A-P005',
    'Tracker-derived materialization from Module_9B_TRACKER.md'
  FROM _m9_paper_map WHERE tracker_id = 'M9A-P005'
  RETURNING paradigm_id
)
INSERT INTO _m9_paradigm_map (tracker_id, paradigm_id) SELECT 'M9A-P005', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 9B curated evidence extraction',
    'First-pass Module 9B in vitro and ex vivo SCI model systems curation for M9A-P006',
    'Tracker-derived materialization from Module_9B_TRACKER.md'
  FROM _m9_paper_map WHERE tracker_id = 'M9A-P006'
  RETURNING paradigm_id
)
INSERT INTO _m9_paradigm_map (tracker_id, paradigm_id) SELECT 'M9A-P006', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 9B curated evidence extraction',
    'First-pass Module 9B in vitro and ex vivo SCI model systems curation for M9A-P007',
    'Tracker-derived materialization from Module_9B_TRACKER.md'
  FROM _m9_paper_map WHERE tracker_id = 'M9A-P007'
  RETURNING paradigm_id
)
INSERT INTO _m9_paradigm_map (tracker_id, paradigm_id) SELECT 'M9A-P007', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 9B curated evidence extraction',
    'First-pass Module 9B in vitro and ex vivo SCI model systems curation for M9A-P008',
    'Tracker-derived materialization from Module_9B_TRACKER.md'
  FROM _m9_paper_map WHERE tracker_id = 'M9A-P008'
  RETURNING paradigm_id
)
INSERT INTO _m9_paradigm_map (tracker_id, paradigm_id) SELECT 'M9A-P008', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 9B curated evidence extraction',
    'First-pass Module 9B in vitro and ex vivo SCI model systems curation for M9A-P009',
    'Tracker-derived materialization from Module_9B_TRACKER.md'
  FROM _m9_paper_map WHERE tracker_id = 'M9A-P009'
  RETURNING paradigm_id
)
INSERT INTO _m9_paradigm_map (tracker_id, paradigm_id) SELECT 'M9A-P009', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 9B curated evidence extraction',
    'First-pass Module 9B in vitro and ex vivo SCI model systems curation for M9A-P010',
    'Tracker-derived materialization from Module_9B_TRACKER.md'
  FROM _m9_paper_map WHERE tracker_id = 'M9A-P010'
  RETURNING paradigm_id
)
INSERT INTO _m9_paradigm_map (tracker_id, paradigm_id) SELECT 'M9A-P010', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 9B curated evidence extraction',
    'First-pass Module 9B in vitro and ex vivo SCI model systems curation for M9A-P011',
    'Tracker-derived materialization from Module_9B_TRACKER.md'
  FROM _m9_paper_map WHERE tracker_id = 'M9A-P011'
  RETURNING paradigm_id
)
INSERT INTO _m9_paradigm_map (tracker_id, paradigm_id) SELECT 'M9A-P011', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 9B curated evidence extraction',
    'First-pass Module 9B in vitro and ex vivo SCI model systems curation for M9A-P012',
    'Tracker-derived materialization from Module_9B_TRACKER.md'
  FROM _m9_paper_map WHERE tracker_id = 'M9A-P012'
  RETURNING paradigm_id
)
INSERT INTO _m9_paradigm_map (tracker_id, paradigm_id) SELECT 'M9A-P012', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 9B curated evidence extraction',
    'First-pass Module 9B in vitro and ex vivo SCI model systems curation for M9A-P013',
    'Tracker-derived materialization from Module_9B_TRACKER.md'
  FROM _m9_paper_map WHERE tracker_id = 'M9A-P013'
  RETURNING paradigm_id
)
INSERT INTO _m9_paradigm_map (tracker_id, paradigm_id) SELECT 'M9A-P013', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 9B curated evidence extraction',
    'First-pass Module 9B in vitro and ex vivo SCI model systems curation for M9A-P014',
    'Tracker-derived materialization from Module_9B_TRACKER.md'
  FROM _m9_paper_map WHERE tracker_id = 'M9A-P014'
  RETURNING paradigm_id
)
INSERT INTO _m9_paradigm_map (tracker_id, paradigm_id) SELECT 'M9A-P014', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 9B curated evidence extraction',
    'First-pass Module 9B in vitro and ex vivo SCI model systems curation for M9A-P015',
    'Tracker-derived materialization from Module_9B_TRACKER.md'
  FROM _m9_paper_map WHERE tracker_id = 'M9A-P015'
  RETURNING paradigm_id
)
INSERT INTO _m9_paradigm_map (tracker_id, paradigm_id) SELECT 'M9A-P015', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 9B curated evidence extraction',
    'First-pass Module 9B in vitro and ex vivo SCI model systems curation for M9A-P016',
    'Tracker-derived materialization from Module_9B_TRACKER.md'
  FROM _m9_paper_map WHERE tracker_id = 'M9A-P016'
  RETURNING paradigm_id
)
INSERT INTO _m9_paradigm_map (tracker_id, paradigm_id) SELECT 'M9A-P016', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 9B curated evidence extraction',
    'First-pass Module 9B in vitro and ex vivo SCI model systems curation for M9A-P017',
    'Tracker-derived materialization from Module_9B_TRACKER.md'
  FROM _m9_paper_map WHERE tracker_id = 'M9A-P017'
  RETURNING paradigm_id
)
INSERT INTO _m9_paradigm_map (tracker_id, paradigm_id) SELECT 'M9A-P017', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / PubMed',
    'Tracker experiment M9A-P001-E001',
    'Module 9B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M9B-O001"], "source_experiment_tracker_id": "M9A-P001-E001", "source_paper_tracker_id": "M9A-P001", "tracker_key": "M9A-P001::M9A-P001-E001"}'
  FROM _m9_paper_map p
  JOIN _m9_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M9A-P001'
  RETURNING experiment_id
)
INSERT INTO _m9_experiment_map (tracker_id, experiment_id) SELECT 'M9A-P001::M9A-P001-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / PubMed',
    'Tracker experiment M9A-P002-E001',
    'Module 9B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M9B-O002"], "source_experiment_tracker_id": "M9A-P002-E001", "source_paper_tracker_id": "M9A-P002", "tracker_key": "M9A-P002::M9A-P002-E001"}'
  FROM _m9_paper_map p
  JOIN _m9_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M9A-P002'
  RETURNING experiment_id
)
INSERT INTO _m9_experiment_map (tracker_id, experiment_id) SELECT 'M9A-P002::M9A-P002-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / PubMed',
    'Tracker experiment M9A-P003-E001',
    'Module 9B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M9B-O003"], "source_experiment_tracker_id": "M9A-P003-E001", "source_paper_tracker_id": "M9A-P003", "tracker_key": "M9A-P003::M9A-P003-E001"}'
  FROM _m9_paper_map p
  JOIN _m9_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M9A-P003'
  RETURNING experiment_id
)
INSERT INTO _m9_experiment_map (tracker_id, experiment_id) SELECT 'M9A-P003::M9A-P003-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / PubMed',
    'Tracker experiment M9A-P004-E001',
    'Module 9B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M9B-O004"], "source_experiment_tracker_id": "M9A-P004-E001", "source_paper_tracker_id": "M9A-P004", "tracker_key": "M9A-P004::M9A-P004-E001"}'
  FROM _m9_paper_map p
  JOIN _m9_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M9A-P004'
  RETURNING experiment_id
)
INSERT INTO _m9_experiment_map (tracker_id, experiment_id) SELECT 'M9A-P004::M9A-P004-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / PubMed',
    'Tracker experiment M9A-P005-E001',
    'Module 9B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M9B-O005"], "source_experiment_tracker_id": "M9A-P005-E001", "source_paper_tracker_id": "M9A-P005", "tracker_key": "M9A-P005::M9A-P005-E001"}'
  FROM _m9_paper_map p
  JOIN _m9_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M9A-P005'
  RETURNING experiment_id
)
INSERT INTO _m9_experiment_map (tracker_id, experiment_id) SELECT 'M9A-P005::M9A-P005-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / PubMed',
    'Tracker experiment M9A-P006-E001',
    'Module 9B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M9B-O006"], "source_experiment_tracker_id": "M9A-P006-E001", "source_paper_tracker_id": "M9A-P006", "tracker_key": "M9A-P006::M9A-P006-E001"}'
  FROM _m9_paper_map p
  JOIN _m9_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M9A-P006'
  RETURNING experiment_id
)
INSERT INTO _m9_experiment_map (tracker_id, experiment_id) SELECT 'M9A-P006::M9A-P006-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / PubMed',
    'Tracker experiment M9A-P007-E001',
    'Module 9B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M9B-O007"], "source_experiment_tracker_id": "M9A-P007-E001", "source_paper_tracker_id": "M9A-P007", "tracker_key": "M9A-P007::M9A-P007-E001"}'
  FROM _m9_paper_map p
  JOIN _m9_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M9A-P007'
  RETURNING experiment_id
)
INSERT INTO _m9_experiment_map (tracker_id, experiment_id) SELECT 'M9A-P007::M9A-P007-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / PubMed',
    'Tracker experiment M9A-P008-E001',
    'Module 9B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M9B-O008"], "source_experiment_tracker_id": "M9A-P008-E001", "source_paper_tracker_id": "M9A-P008", "tracker_key": "M9A-P008::M9A-P008-E001"}'
  FROM _m9_paper_map p
  JOIN _m9_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M9A-P008'
  RETURNING experiment_id
)
INSERT INTO _m9_experiment_map (tracker_id, experiment_id) SELECT 'M9A-P008::M9A-P008-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / PubMed',
    'Tracker experiment M9A-P009-E001',
    'Module 9B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M9B-O009"], "source_experiment_tracker_id": "M9A-P009-E001", "source_paper_tracker_id": "M9A-P009", "tracker_key": "M9A-P009::M9A-P009-E001"}'
  FROM _m9_paper_map p
  JOIN _m9_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M9A-P009'
  RETURNING experiment_id
)
INSERT INTO _m9_experiment_map (tracker_id, experiment_id) SELECT 'M9A-P009::M9A-P009-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / PubMed',
    'Tracker experiment M9A-P010-E001',
    'Module 9B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M9B-O010"], "source_experiment_tracker_id": "M9A-P010-E001", "source_paper_tracker_id": "M9A-P010", "tracker_key": "M9A-P010::M9A-P010-E001"}'
  FROM _m9_paper_map p
  JOIN _m9_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M9A-P010'
  RETURNING experiment_id
)
INSERT INTO _m9_experiment_map (tracker_id, experiment_id) SELECT 'M9A-P010::M9A-P010-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / PubMed',
    'Tracker experiment M9A-P011-E001',
    'Module 9B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M9B-O011"], "source_experiment_tracker_id": "M9A-P011-E001", "source_paper_tracker_id": "M9A-P011", "tracker_key": "M9A-P011::M9A-P011-E001"}'
  FROM _m9_paper_map p
  JOIN _m9_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M9A-P011'
  RETURNING experiment_id
)
INSERT INTO _m9_experiment_map (tracker_id, experiment_id) SELECT 'M9A-P011::M9A-P011-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / PubMed',
    'Tracker experiment M9A-P012-E001',
    'Module 9B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M9B-O012"], "source_experiment_tracker_id": "M9A-P012-E001", "source_paper_tracker_id": "M9A-P012", "tracker_key": "M9A-P012::M9A-P012-E001"}'
  FROM _m9_paper_map p
  JOIN _m9_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M9A-P012'
  RETURNING experiment_id
)
INSERT INTO _m9_experiment_map (tracker_id, experiment_id) SELECT 'M9A-P012::M9A-P012-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / PubMed',
    'Tracker experiment M9A-P013-E001',
    'Module 9B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M9B-O013"], "source_experiment_tracker_id": "M9A-P013-E001", "source_paper_tracker_id": "M9A-P013", "tracker_key": "M9A-P013::M9A-P013-E001"}'
  FROM _m9_paper_map p
  JOIN _m9_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M9A-P013'
  RETURNING experiment_id
)
INSERT INTO _m9_experiment_map (tracker_id, experiment_id) SELECT 'M9A-P013::M9A-P013-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / PubMed',
    'Tracker experiment M9A-P014-E001',
    'Module 9B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M9B-O014"], "source_experiment_tracker_id": "M9A-P014-E001", "source_paper_tracker_id": "M9A-P014", "tracker_key": "M9A-P014::M9A-P014-E001"}'
  FROM _m9_paper_map p
  JOIN _m9_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M9A-P014'
  RETURNING experiment_id
)
INSERT INTO _m9_experiment_map (tracker_id, experiment_id) SELECT 'M9A-P014::M9A-P014-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / PubMed',
    'Tracker experiment M9A-P015-E001',
    'Module 9B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M9B-O015"], "source_experiment_tracker_id": "M9A-P015-E001", "source_paper_tracker_id": "M9A-P015", "tracker_key": "M9A-P015::M9A-P015-E001"}'
  FROM _m9_paper_map p
  JOIN _m9_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M9A-P015'
  RETURNING experiment_id
)
INSERT INTO _m9_experiment_map (tracker_id, experiment_id) SELECT 'M9A-P015::M9A-P015-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / PubMed',
    'Tracker experiment M9A-P016-E001',
    'Module 9B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M9B-O016"], "source_experiment_tracker_id": "M9A-P016-E001", "source_paper_tracker_id": "M9A-P016", "tracker_key": "M9A-P016::M9A-P016-E001"}'
  FROM _m9_paper_map p
  JOIN _m9_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M9A-P016'
  RETURNING experiment_id
)
INSERT INTO _m9_experiment_map (tracker_id, experiment_id) SELECT 'M9A-P016::M9A-P016-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / PubMed',
    'Tracker experiment M9A-P017-E001',
    'Module 9B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M9B-O017"], "source_experiment_tracker_id": "M9A-P017-E001", "source_paper_tracker_id": "M9A-P017", "tracker_key": "M9A-P017::M9A-P017-E001"}'
  FROM _m9_paper_map p
  JOIN _m9_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M9A-P017'
  RETURNING experiment_id
)
INSERT INTO _m9_experiment_map (tracker_id, experiment_id) SELECT 'M9A-P017::M9A-P017-E001', experiment_id FROM inserted;

INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Model-system evidence', 'Module 9B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;

INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('biomaterial culture model', 'Module 9B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('in vitro/ex vivo SCI model taxonomy', 'Module 9B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('slice/explant SCI model', 'Module 9B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('spinal cord organoid injury model', 'Module 9B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Stem-cell-based neural tissue engineering and spinal cord organoids show promises for spinal cord injury repair. However, the native spinal cord presents cell heterogeneity and a stereotypical spatial structure that makes difficult their recapitulation within an organoid architecture, which requires an assembly encompassing cellular composition, segmental organization and dorsoventral features. Here we engineer a thoracic vertebral segment-specific spinal',
    'qualitative',
    'Stem-cell-based neural tissue engineering and spinal cord organoids show promises for spinal cord injury repair. However, the native spinal cord presents cell heterogeneity and a stereotypical spatial structure that makes difficult their recapitulation within an organoid architecture, which requires an assembly encompassing cellular composition, segmental organization and dorsoventral features. Here we engineer a thoracic vertebral segment-specific spinal',
    'spinal cord organoid injury model',
    'PubMed/source metadata',
    'Abstract / PubMed',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M9A-P001-E001", "paper_tracker_id": "M9A-P001", "quantitative": "NO", "statistics_reported": "Source-page first pass; exact statistics not extracted", "topic_id": "M9B-T001", "tracker_id": "M9B-O001"}'
  FROM _m9_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M9A-P001::M9A-P001-E001'
    AND et.evidence_type_name = 'Model-system evidence'
    AND ot.outcome_type_name = 'spinal cord organoid injury model'
  RETURNING observation_id
)
INSERT INTO _m9_observation_map (tracker_id, observation_id) SELECT 'M9B-O001', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Neonatal spinal cord tissues exhibit remarkable regenerative capabilities as compared to adult spinal cord tissues after injury, but the role of extracellular matrix (ECM) in this process has remained elusive. Here, we found that early developmental spinal cord had higher levels of ECM proteins associated with neural development and axon growth, but fewer inhibitory proteoglycans, compared to those of adult spinal cord. Decellularized spinal cord ECM from',
    'qualitative',
    'Neonatal spinal cord tissues exhibit remarkable regenerative capabilities as compared to adult spinal cord tissues after injury, but the role of extracellular matrix (ECM) in this process has remained elusive. Here, we found that early developmental spinal cord had higher levels of ECM proteins associated with neural development and axon growth, but fewer inhibitory proteoglycans, compared to those of adult spinal cord. Decellularized spinal cord ECM from',
    'spinal cord organoid injury model',
    'PubMed/source metadata',
    'Abstract / PubMed',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M9A-P002-E001", "paper_tracker_id": "M9A-P002", "quantitative": "NO", "statistics_reported": "Source-page first pass; exact statistics not extracted", "topic_id": "M9B-T002", "tracker_id": "M9B-O002"}'
  FROM _m9_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M9A-P002::M9A-P002-E001'
    AND et.evidence_type_name = 'Model-system evidence'
    AND ot.outcome_type_name = 'spinal cord organoid injury model'
  RETURNING observation_id
)
INSERT INTO _m9_observation_map (tracker_id, observation_id) SELECT 'M9B-O002', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Stem cell-derived spinal cord organoids (SCOs) have revolutionised the study of spinal cord development and disease mechanisms, offering a three-dimensional model that recapitulates the complexity of native tissue. This review synthesises recent advancements in SCO technology, highlighting their role in modelling spinal cord morphogenesis and their application in neurodegenerative disease research. We discuss the methodological breakthroughs in inducing',
    'qualitative',
    'Stem cell-derived spinal cord organoids (SCOs) have revolutionised the study of spinal cord development and disease mechanisms, offering a three-dimensional model that recapitulates the complexity of native tissue. This review synthesises recent advancements in SCO technology, highlighting their role in modelling spinal cord morphogenesis and their application in neurodegenerative disease research. We discuss the methodological breakthroughs in inducing',
    'spinal cord organoid injury model',
    'PubMed/source metadata',
    'Abstract / PubMed',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M9A-P003-E001", "paper_tracker_id": "M9A-P003", "quantitative": "NO", "statistics_reported": "Source-page first pass; exact statistics not extracted", "topic_id": "M9B-T003", "tracker_id": "M9B-O003"}'
  FROM _m9_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M9A-P003::M9A-P003-E001'
    AND et.evidence_type_name = 'Model-system evidence'
    AND ot.outcome_type_name = 'spinal cord organoid injury model'
  RETURNING observation_id
)
INSERT INTO _m9_observation_map (tracker_id, observation_id) SELECT 'M9B-O003', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Damage to the spinal cord can lead to irreversible paralysis and loss of sensory function, but translation of preclinical therapies remains elusive. We recently showed that bioactive supramolecular assemblies of peptide amphiphiles can reverse paralysis in an acute mouse model following severe spinal cord injury (SCI). Here we report the development of two human spinal cord organoid injury models to simulate SCI in vitro, a laceration of the organoid with',
    'qualitative',
    'Damage to the spinal cord can lead to irreversible paralysis and loss of sensory function, but translation of preclinical therapies remains elusive. We recently showed that bioactive supramolecular assemblies of peptide amphiphiles can reverse paralysis in an acute mouse model following severe spinal cord injury (SCI). Here we report the development of two human spinal cord organoid injury models to simulate SCI in vitro, a laceration of the organoid with',
    'spinal cord organoid injury model',
    'PubMed/source metadata',
    'Abstract / PubMed',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M9A-P004-E001", "paper_tracker_id": "M9A-P004", "quantitative": "NO", "statistics_reported": "Source-page first pass; exact statistics not extracted", "topic_id": "M9B-T004", "tracker_id": "M9B-O004"}'
  FROM _m9_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M9A-P004::M9A-P004-E001'
    AND et.evidence_type_name = 'Model-system evidence'
    AND ot.outcome_type_name = 'spinal cord organoid injury model'
  RETURNING observation_id
)
INSERT INTO _m9_observation_map (tracker_id, observation_id) SELECT 'M9B-O004', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Spinal cord injury (SCI) severely compromises neural regeneration due to limited intrinsic repair capacity. Combining induced pluripotent stem cell (iPSC)-derived organoids with biomaterial scaffolds offers a promising regenerative strategy. This study investigated the therapeutic potential of human spinal cord organoids (hSCOs) encapsulated within gelatin methacryloyl (GelMA) hydrogel for SCI repair. hSCOs were generated from iPSCs via stage-specific',
    'qualitative',
    'Spinal cord injury (SCI) severely compromises neural regeneration due to limited intrinsic repair capacity. Combining induced pluripotent stem cell (iPSC)-derived organoids with biomaterial scaffolds offers a promising regenerative strategy. This study investigated the therapeutic potential of human spinal cord organoids (hSCOs) encapsulated within gelatin methacryloyl (GelMA) hydrogel for SCI repair. hSCOs were generated from iPSCs via stage-specific',
    'spinal cord organoid injury model',
    'PubMed/source metadata',
    'Abstract / PubMed',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M9A-P005-E001", "paper_tracker_id": "M9A-P005", "quantitative": "NO", "statistics_reported": "Source-page first pass; exact statistics not extracted", "topic_id": "M9B-T005", "tracker_id": "M9B-O005"}'
  FROM _m9_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M9A-P005::M9A-P005-E001'
    AND et.evidence_type_name = 'Model-system evidence'
    AND ot.outcome_type_name = 'spinal cord organoid injury model'
  RETURNING observation_id
)
INSERT INTO _m9_observation_map (tracker_id, observation_id) SELECT 'M9B-O005', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'The construction of artificially manipulable tissue-engineered human spinal cord organoids (HSCO) in vitro is crucial for recapitulating spinal cord development and facilitating the transplantation repair of complete spinal cord injury (SCI). Here, we develop a millimeter-scale macroscopic complex scaffold assembled by Matrigel-filled channel-patterned type II collagen (CPCol II-M), in which a spheroid derived from human motor neural progenitors extends',
    'qualitative',
    'The construction of artificially manipulable tissue-engineered human spinal cord organoids (HSCO) in vitro is crucial for recapitulating spinal cord development and facilitating the transplantation repair of complete spinal cord injury (SCI). Here, we develop a millimeter-scale macroscopic complex scaffold assembled by Matrigel-filled channel-patterned type II collagen (CPCol II-M), in which a spheroid derived from human motor neural progenitors extends',
    'spinal cord organoid injury model',
    'PubMed/source metadata',
    'Abstract / PubMed',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M9A-P006-E001", "paper_tracker_id": "M9A-P006", "quantitative": "NO", "statistics_reported": "Source-page first pass; exact statistics not extracted", "topic_id": "M9B-T006", "tracker_id": "M9B-O006"}'
  FROM _m9_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M9A-P006::M9A-P006-E001'
    AND et.evidence_type_name = 'Model-system evidence'
    AND ot.outcome_type_name = 'spinal cord organoid injury model'
  RETURNING observation_id
)
INSERT INTO _m9_observation_map (tracker_id, observation_id) SELECT 'M9B-O006', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'The complexity and precision of the human nervous system have posed significant challenges for researchers seeking suitable models to elucidate refractory neural disorders. Traditional approaches, including monolayer cell cultures and animal models, often fail to replicate the intricacies of human neural tissue. The advent of organoid technology derived from stem cells has addressed many of these limitations, providing highly representative platforms for',
    'qualitative',
    'The complexity and precision of the human nervous system have posed significant challenges for researchers seeking suitable models to elucidate refractory neural disorders. Traditional approaches, including monolayer cell cultures and animal models, often fail to replicate the intricacies of human neural tissue. The advent of organoid technology derived from stem cells has addressed many of these limitations, providing highly representative platforms for',
    'spinal cord organoid injury model',
    'PubMed/source metadata',
    'Abstract / PubMed',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M9A-P007-E001", "paper_tracker_id": "M9A-P007", "quantitative": "NO", "statistics_reported": "Source-page first pass; exact statistics not extracted", "topic_id": "M9B-T007", "tracker_id": "M9B-O007"}'
  FROM _m9_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M9A-P007::M9A-P007-E001'
    AND et.evidence_type_name = 'Model-system evidence'
    AND ot.outcome_type_name = 'spinal cord organoid injury model'
  RETURNING observation_id
)
INSERT INTO _m9_observation_map (tracker_id, observation_id) SELECT 'M9B-O007', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Directional axon regeneration and remyelination are crucial for repair of spinal cord injury (SCI), but existing treatments do not effectively promote those processes. Here, we propose a strategy for construction of niche-specific spinal white matter-like tissue (WMLT) using decellularized optic nerve (DON) loaded with neurotrophin-3 (NT-3)-overexpressing oligodendrocyte precursor cells. A rat model with a white matter defect in the dorsal spinal cord of',
    'qualitative',
    'Directional axon regeneration and remyelination are crucial for repair of spinal cord injury (SCI), but existing treatments do not effectively promote those processes. Here, we propose a strategy for construction of niche-specific spinal white matter-like tissue (WMLT) using decellularized optic nerve (DON) loaded with neurotrophin-3 (NT-3)-overexpressing oligodendrocyte precursor cells. A rat model with a white matter defect in the dorsal spinal cord of',
    'in vitro/ex vivo sci model taxonomy',
    'PubMed/source metadata',
    'Abstract / PubMed',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M9A-P008-E001", "paper_tracker_id": "M9A-P008", "quantitative": "NO", "statistics_reported": "Source-page first pass; exact statistics not extracted", "topic_id": "M9B-T008", "tracker_id": "M9B-O008"}'
  FROM _m9_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M9A-P008::M9A-P008-E001'
    AND et.evidence_type_name = 'Model-system evidence'
    AND ot.outcome_type_name = 'in vitro/ex vivo SCI model taxonomy'
  RETURNING observation_id
)
INSERT INTO _m9_observation_map (tracker_id, observation_id) SELECT 'M9B-O008', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Oxidative stress represents a fundamental pathological driver of the secondary injury cascade following traumatic spinal cord injury (SCI). Although the pan-histone deacetylase inhibitor Trichostatin A (TSA) exhibits neuroprotective properties in various contexts, its capacity to modulate the endogenous NRF2/HO-1 antioxidant defense system within the human spinal cord microenvironment remains to be elucidated. In this study, we utilized human induced',
    'qualitative',
    'Oxidative stress represents a fundamental pathological driver of the secondary injury cascade following traumatic spinal cord injury (SCI). Although the pan-histone deacetylase inhibitor Trichostatin A (TSA) exhibits neuroprotective properties in various contexts, its capacity to modulate the endogenous NRF2/HO-1 antioxidant defense system within the human spinal cord microenvironment remains to be elucidated. In this study, we utilized human induced',
    'spinal cord organoid injury model',
    'PubMed/source metadata',
    'Abstract / PubMed',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M9A-P009-E001", "paper_tracker_id": "M9A-P009", "quantitative": "NO", "statistics_reported": "Source-page first pass; exact statistics not extracted", "topic_id": "M9B-T001", "tracker_id": "M9B-O009"}'
  FROM _m9_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M9A-P009::M9A-P009-E001'
    AND et.evidence_type_name = 'Model-system evidence'
    AND ot.outcome_type_name = 'spinal cord organoid injury model'
  RETURNING observation_id
)
INSERT INTO _m9_observation_map (tracker_id, observation_id) SELECT 'M9B-O009', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Spinal cord injury (SCI) causes irreversible neurological deficits and represents a major global health and socioeconomic burden. Although neural progenitor cell (NPC) transplantation is strongly supported by preclinical evidence through cell replacement, intrinsic neuroregeneration, and broad neurotrophic and immunomodulatory effects, its clinical translation has progressed more slowly than anticipated. In parallel, rapid advances in gene editing,',
    'qualitative',
    'Spinal cord injury (SCI) causes irreversible neurological deficits and represents a major global health and socioeconomic burden. Although neural progenitor cell (NPC) transplantation is strongly supported by preclinical evidence through cell replacement, intrinsic neuroregeneration, and broad neurotrophic and immunomodulatory effects, its clinical translation has progressed more slowly than anticipated. In parallel, rapid advances in gene editing,',
    'spinal cord organoid injury model',
    'PubMed/source metadata',
    'Abstract / PubMed',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M9A-P010-E001", "paper_tracker_id": "M9A-P010", "quantitative": "NO", "statistics_reported": "Source-page first pass; exact statistics not extracted", "topic_id": "M9B-T002", "tracker_id": "M9B-O010"}'
  FROM _m9_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M9A-P010::M9A-P010-E001'
    AND et.evidence_type_name = 'Model-system evidence'
    AND ot.outcome_type_name = 'spinal cord organoid injury model'
  RETURNING observation_id
)
INSERT INTO _m9_observation_map (tracker_id, observation_id) SELECT 'M9B-O010', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Over the past decade, the use of induced pluripotent stem cells (IPSCs), as both direct therapeutics and building blocks for 3D in vitro models, has exhibited exciting potential in both helping to elucidate pathogenic mechanisms and treating diseases relevant to neurosurgery. Transplantation of IPSCs is being studied in neurological injuries and diseases, such as spinal cord injury and Parkinson''s disease, whose clinical manifestations stem from',
    'qualitative',
    'Over the past decade, the use of induced pluripotent stem cells (IPSCs), as both direct therapeutics and building blocks for 3D in vitro models, has exhibited exciting potential in both helping to elucidate pathogenic mechanisms and treating diseases relevant to neurosurgery. Transplantation of IPSCs is being studied in neurological injuries and diseases, such as spinal cord injury and Parkinson''s disease, whose clinical manifestations stem from',
    'spinal cord organoid injury model',
    'PubMed/source metadata',
    'Abstract / PubMed',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M9A-P011-E001", "paper_tracker_id": "M9A-P011", "quantitative": "NO", "statistics_reported": "Source-page first pass; exact statistics not extracted", "topic_id": "M9B-T003", "tracker_id": "M9B-O011"}'
  FROM _m9_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M9A-P011::M9A-P011-E001'
    AND et.evidence_type_name = 'Model-system evidence'
    AND ot.outcome_type_name = 'spinal cord organoid injury model'
  RETURNING observation_id
)
INSERT INTO _m9_observation_map (tracker_id, observation_id) SELECT 'M9B-O011', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'The limited regenerative capacity of the central nervous system (CNS)poses a major challenge in neurosurgical interventions for spinal cord injuries, neurodegenerative diseases,and traumatic brain injuries. Traditional approaches offer structural stabilization but rarely achieve true neural tissue regeneration. Recent advances in regenerative medicine have spotlighted two promising strategies: 3D bioprinting and neural stem cell (NSC) therapy.3D',
    'qualitative',
    'The limited regenerative capacity of the central nervous system (CNS)poses a major challenge in neurosurgical interventions for spinal cord injuries, neurodegenerative diseases,and traumatic brain injuries. Traditional approaches offer structural stabilization but rarely achieve true neural tissue regeneration. Recent advances in regenerative medicine have spotlighted two promising strategies: 3D bioprinting and neural stem cell (NSC) therapy.3D',
    'biomaterial culture model',
    'PubMed/source metadata',
    'Abstract / PubMed',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M9A-P012-E001", "paper_tracker_id": "M9A-P012", "quantitative": "NO", "statistics_reported": "Source-page first pass; exact statistics not extracted", "topic_id": "M9B-T004", "tracker_id": "M9B-O012"}'
  FROM _m9_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M9A-P012::M9A-P012-E001'
    AND et.evidence_type_name = 'Model-system evidence'
    AND ot.outcome_type_name = 'biomaterial culture model'
  RETURNING observation_id
)
INSERT INTO _m9_observation_map (tracker_id, observation_id) SELECT 'M9B-O012', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Spinal cord injury (SCI) is a devastating condition resulting in loss of motor function. The pathology of SCI is multifaceted and involves a cascade of events, including neuroinflammation and neuronal degeneration at the epicenter, limiting repair process. We developed a supermacroporous, mechanically elastic, electro-conductive, graphene crosslinked collagen (Gr-Col) cryogels for the regeneration of the spinal cord post-injury. The effects of graphene in',
    'qualitative',
    'Spinal cord injury (SCI) is a devastating condition resulting in loss of motor function. The pathology of SCI is multifaceted and involves a cascade of events, including neuroinflammation and neuronal degeneration at the epicenter, limiting repair process. We developed a supermacroporous, mechanically elastic, electro-conductive, graphene crosslinked collagen (Gr-Col) cryogels for the regeneration of the spinal cord post-injury. The effects of graphene in',
    'slice/explant sci model',
    'PubMed/source metadata',
    'Abstract / PubMed',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M9A-P013-E001", "paper_tracker_id": "M9A-P013", "quantitative": "NO", "statistics_reported": "Source-page first pass; exact statistics not extracted", "topic_id": "M9B-T005", "tracker_id": "M9B-O013"}'
  FROM _m9_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M9A-P013::M9A-P013-E001'
    AND et.evidence_type_name = 'Model-system evidence'
    AND ot.outcome_type_name = 'slice/explant SCI model'
  RETURNING observation_id
)
INSERT INTO _m9_observation_map (tracker_id, observation_id) SELECT 'M9B-O013', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'A substantial problem in research concerned with axonal repair is the use of a wide variety of lesion models and the complexity associated with the respective in vivo lesion paradigms. Organotypic slice cultures are a potential in vitro alternative because the cytoarchitectonic tissue organization is well preserved and the slices can be maintained in culture for several weeks. Until now no spinal cord slice culture model for the study of axonal growth has',
    'qualitative',
    'A substantial problem in research concerned with axonal repair is the use of a wide variety of lesion models and the complexity associated with the respective in vivo lesion paradigms. Organotypic slice cultures are a potential in vitro alternative because the cytoarchitectonic tissue organization is well preserved and the slices can be maintained in culture for several weeks. Until now no spinal cord slice culture model for the study of axonal growth has',
    'slice/explant sci model',
    'PubMed/source metadata',
    'Abstract / PubMed',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M9A-P014-E001", "paper_tracker_id": "M9A-P014", "quantitative": "NO", "statistics_reported": "Source-page first pass; exact statistics not extracted", "topic_id": "M9B-T006", "tracker_id": "M9B-O014"}'
  FROM _m9_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M9A-P014::M9A-P014-E001'
    AND et.evidence_type_name = 'Model-system evidence'
    AND ot.outcome_type_name = 'slice/explant SCI model'
  RETURNING observation_id
)
INSERT INTO _m9_observation_map (tracker_id, observation_id) SELECT 'M9B-O014', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Following injury to the white matter of the adult mammalian central nervous system (CNS), severed axons fail to regenerate beyond the lesion site. Recent studies have revealed that the CNS white matter contains numerous axon growth inhibitors. These findings can easily lead to the concept that regenerating axons cannot grow in the CNS white matter because of the growth inhibition by these inhibitory molecules. This "misconception" appears to be generally',
    'qualitative',
    'Following injury to the white matter of the adult mammalian central nervous system (CNS), severed axons fail to regenerate beyond the lesion site. Recent studies have revealed that the CNS white matter contains numerous axon growth inhibitors. These findings can easily lead to the concept that regenerating axons cannot grow in the CNS white matter because of the growth inhibition by these inhibitory molecules. This "misconception" appears to be generally',
    'slice/explant sci model',
    'PubMed/source metadata',
    'Abstract / PubMed',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M9A-P015-E001", "paper_tracker_id": "M9A-P015", "quantitative": "NO", "statistics_reported": "Source-page first pass; exact statistics not extracted", "topic_id": "M9B-T007", "tracker_id": "M9B-O015"}'
  FROM _m9_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M9A-P015::M9A-P015-E001'
    AND et.evidence_type_name = 'Model-system evidence'
    AND ot.outcome_type_name = 'slice/explant SCI model'
  RETURNING observation_id
)
INSERT INTO _m9_observation_map (tracker_id, observation_id) SELECT 'M9B-O015', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Presently there exists no cure for spinal cord injury (SCI). However, transplantation of embryonic tissue into spinal cord (SC) lesions resulted in axon outgrowth across the lesion site and some functional recovery, fostering hope for future stem cell therapies. Although in vivo evidence for functional recovery is given, the exact cellular mechanism of the graft support remains elusive: either the grafted cells provide a permissive environment for the',
    'qualitative',
    'Presently there exists no cure for spinal cord injury (SCI). However, transplantation of embryonic tissue into spinal cord (SC) lesions resulted in axon outgrowth across the lesion site and some functional recovery, fostering hope for future stem cell therapies. Although in vivo evidence for functional recovery is given, the exact cellular mechanism of the graft support remains elusive: either the grafted cells provide a permissive environment for the',
    'slice/explant sci model',
    'PubMed/source metadata',
    'Abstract / PubMed',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M9A-P016-E001", "paper_tracker_id": "M9A-P016", "quantitative": "NO", "statistics_reported": "Source-page first pass; exact statistics not extracted", "topic_id": "M9B-T008", "tracker_id": "M9B-O016"}'
  FROM _m9_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M9A-P016::M9A-P016-E001'
    AND et.evidence_type_name = 'Model-system evidence'
    AND ot.outcome_type_name = 'slice/explant SCI model'
  RETURNING observation_id
)
INSERT INTO _m9_observation_map (tracker_id, observation_id) SELECT 'M9B-O016', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Mesenchymal stem cells (MSCs) have demonstrated a measurable therapeutic effect following transplantation into animal models of spinal cord injury. However, the mechanism(s) by which transplanted cells promote nerve regeneration and/or functional recovery remains indeterminate. Several studies have suggested that MSCs promote tissue repair via secretion of trophic factors, but delineating the effect of such factors is difficult due to the complexity of',
    'qualitative',
    'Mesenchymal stem cells (MSCs) have demonstrated a measurable therapeutic effect following transplantation into animal models of spinal cord injury. However, the mechanism(s) by which transplanted cells promote nerve regeneration and/or functional recovery remains indeterminate. Several studies have suggested that MSCs promote tissue repair via secretion of trophic factors, but delineating the effect of such factors is difficult due to the complexity of',
    'slice/explant sci model',
    'PubMed/source metadata',
    'Abstract / PubMed',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M9A-P017-E001", "paper_tracker_id": "M9A-P017", "quantitative": "NO", "statistics_reported": "Source-page first pass; exact statistics not extracted", "topic_id": "M9B-T001", "tracker_id": "M9B-O017"}'
  FROM _m9_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M9A-P017::M9A-P017-E001'
    AND et.evidence_type_name = 'Model-system evidence'
    AND ot.outcome_type_name = 'slice/explant SCI model'
  RETURNING observation_id
)
INSERT INTO _m9_observation_map (tracker_id, observation_id) SELECT 'M9B-O017', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Culture format boundaries requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 9A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M9A-P001", "topic_id": "M9B-T001", "tracker_id": "M9B-C001"}'
  FROM _m9_paper_map p
  WHERE p.tracker_id = 'M9A-P001'
  RETURNING claim_id
)
INSERT INTO _m9_claim_map (tracker_id, claim_id) SELECT 'M9B-C001', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Cell-source and maturity boundaries requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 9A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M9A-P002", "topic_id": "M9B-T002", "tracker_id": "M9B-C002"}'
  FROM _m9_paper_map p
  WHERE p.tracker_id = 'M9A-P002'
  RETURNING claim_id
)
INSERT INTO _m9_claim_map (tracker_id, claim_id) SELECT 'M9B-C002', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Injury stimulus boundaries requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 9A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M9A-P003", "topic_id": "M9B-T003", "tracker_id": "M9B-C003"}'
  FROM _m9_paper_map p
  WHERE p.tracker_id = 'M9A-P003'
  RETURNING claim_id
)
INSERT INTO _m9_claim_map (tracker_id, claim_id) SELECT 'M9B-C003', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Assay/readout boundaries requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 9A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M9A-P004", "topic_id": "M9B-T004", "tracker_id": "M9B-C004"}'
  FROM _m9_paper_map p
  WHERE p.tracker_id = 'M9A-P004'
  RETURNING claim_id
)
INSERT INTO _m9_claim_map (tracker_id, claim_id) SELECT 'M9B-C004', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Matrix/debris model boundaries requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 9A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M9A-P005", "topic_id": "M9B-T005", "tracker_id": "M9B-C005"}'
  FROM _m9_paper_map p
  WHERE p.tracker_id = 'M9A-P005'
  RETURNING claim_id
)
INSERT INTO _m9_claim_map (tracker_id, claim_id) SELECT 'M9B-C005', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Biomaterial compatibility boundaries requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 9A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M9A-P006", "topic_id": "M9B-T006", "tracker_id": "M9B-C006"}'
  FROM _m9_paper_map p
  WHERE p.tracker_id = 'M9A-P006'
  RETURNING claim_id
)
INSERT INTO _m9_claim_map (tracker_id, claim_id) SELECT 'M9B-C006', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Organoid/slice/explant translation boundaries requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 9A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M9A-P007", "topic_id": "M9B-T007", "tracker_id": "M9B-C007"}'
  FROM _m9_paper_map p
  WHERE p.tracker_id = 'M9A-P007'
  RETURNING claim_id
)
INSERT INTO _m9_claim_map (tracker_id, claim_id) SELECT 'M9B-C007', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'In vitro confidence boundaries requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 9A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M9A-P008", "topic_id": "M9B-T008", "tracker_id": "M9B-C008"}'
  FROM _m9_paper_map p
  WHERE p.tracker_id = 'M9A-P008'
  RETURNING claim_id
)
INSERT INTO _m9_claim_map (tracker_id, claim_id) SELECT 'M9B-C008', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Culture format boundaries requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 9A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M9A-P009", "topic_id": "M9B-T001", "tracker_id": "M9B-C009"}'
  FROM _m9_paper_map p
  WHERE p.tracker_id = 'M9A-P009'
  RETURNING claim_id
)
INSERT INTO _m9_claim_map (tracker_id, claim_id) SELECT 'M9B-C009', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Cell-source and maturity boundaries requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 9A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M9A-P010", "topic_id": "M9B-T002", "tracker_id": "M9B-C010"}'
  FROM _m9_paper_map p
  WHERE p.tracker_id = 'M9A-P010'
  RETURNING claim_id
)
INSERT INTO _m9_claim_map (tracker_id, claim_id) SELECT 'M9B-C010', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Injury stimulus boundaries requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 9A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M9A-P011", "topic_id": "M9B-T003", "tracker_id": "M9B-C011"}'
  FROM _m9_paper_map p
  WHERE p.tracker_id = 'M9A-P011'
  RETURNING claim_id
)
INSERT INTO _m9_claim_map (tracker_id, claim_id) SELECT 'M9B-C011', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Assay/readout boundaries requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 9A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M9A-P012", "topic_id": "M9B-T004", "tracker_id": "M9B-C012"}'
  FROM _m9_paper_map p
  WHERE p.tracker_id = 'M9A-P012'
  RETURNING claim_id
)
INSERT INTO _m9_claim_map (tracker_id, claim_id) SELECT 'M9B-C012', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Matrix/debris model boundaries requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 9A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M9A-P013", "topic_id": "M9B-T005", "tracker_id": "M9B-C013"}'
  FROM _m9_paper_map p
  WHERE p.tracker_id = 'M9A-P013'
  RETURNING claim_id
)
INSERT INTO _m9_claim_map (tracker_id, claim_id) SELECT 'M9B-C013', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Biomaterial compatibility boundaries requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 9A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M9A-P014", "topic_id": "M9B-T006", "tracker_id": "M9B-C014"}'
  FROM _m9_paper_map p
  WHERE p.tracker_id = 'M9A-P014'
  RETURNING claim_id
)
INSERT INTO _m9_claim_map (tracker_id, claim_id) SELECT 'M9B-C014', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Organoid/slice/explant translation boundaries requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 9A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M9A-P015", "topic_id": "M9B-T007", "tracker_id": "M9B-C015"}'
  FROM _m9_paper_map p
  WHERE p.tracker_id = 'M9A-P015'
  RETURNING claim_id
)
INSERT INTO _m9_claim_map (tracker_id, claim_id) SELECT 'M9B-C015', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'In vitro confidence boundaries requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 9A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M9A-P016", "topic_id": "M9B-T008", "tracker_id": "M9B-C016"}'
  FROM _m9_paper_map p
  WHERE p.tracker_id = 'M9A-P016'
  RETURNING claim_id
)
INSERT INTO _m9_claim_map (tracker_id, claim_id) SELECT 'M9B-C016', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Culture format boundaries requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 9A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M9A-P017", "topic_id": "M9B-T001", "tracker_id": "M9B-C017"}'
  FROM _m9_paper_map p
  WHERE p.tracker_id = 'M9A-P017'
  RETURNING claim_id
)
INSERT INTO _m9_claim_map (tracker_id, claim_id) SELECT 'M9B-C017', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M9B-L001"}'
  FROM _m9_claim_map c
  JOIN _m9_observation_map o ON o.tracker_id = 'M9B-O001'
  WHERE c.tracker_id = 'M9B-C001'
  RETURNING link_id
)
INSERT INTO _m9_link_map (tracker_id, link_id) SELECT 'M9B-L001', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M9B-L002"}'
  FROM _m9_claim_map c
  JOIN _m9_observation_map o ON o.tracker_id = 'M9B-O002'
  WHERE c.tracker_id = 'M9B-C002'
  RETURNING link_id
)
INSERT INTO _m9_link_map (tracker_id, link_id) SELECT 'M9B-L002', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M9B-L003"}'
  FROM _m9_claim_map c
  JOIN _m9_observation_map o ON o.tracker_id = 'M9B-O003'
  WHERE c.tracker_id = 'M9B-C003'
  RETURNING link_id
)
INSERT INTO _m9_link_map (tracker_id, link_id) SELECT 'M9B-L003', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M9B-L004"}'
  FROM _m9_claim_map c
  JOIN _m9_observation_map o ON o.tracker_id = 'M9B-O004'
  WHERE c.tracker_id = 'M9B-C004'
  RETURNING link_id
)
INSERT INTO _m9_link_map (tracker_id, link_id) SELECT 'M9B-L004', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M9B-L005"}'
  FROM _m9_claim_map c
  JOIN _m9_observation_map o ON o.tracker_id = 'M9B-O005'
  WHERE c.tracker_id = 'M9B-C005'
  RETURNING link_id
)
INSERT INTO _m9_link_map (tracker_id, link_id) SELECT 'M9B-L005', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M9B-L006"}'
  FROM _m9_claim_map c
  JOIN _m9_observation_map o ON o.tracker_id = 'M9B-O006'
  WHERE c.tracker_id = 'M9B-C006'
  RETURNING link_id
)
INSERT INTO _m9_link_map (tracker_id, link_id) SELECT 'M9B-L006', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M9B-L007"}'
  FROM _m9_claim_map c
  JOIN _m9_observation_map o ON o.tracker_id = 'M9B-O007'
  WHERE c.tracker_id = 'M9B-C007'
  RETURNING link_id
)
INSERT INTO _m9_link_map (tracker_id, link_id) SELECT 'M9B-L007', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M9B-L008"}'
  FROM _m9_claim_map c
  JOIN _m9_observation_map o ON o.tracker_id = 'M9B-O008'
  WHERE c.tracker_id = 'M9B-C008'
  RETURNING link_id
)
INSERT INTO _m9_link_map (tracker_id, link_id) SELECT 'M9B-L008', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M9B-L009"}'
  FROM _m9_claim_map c
  JOIN _m9_observation_map o ON o.tracker_id = 'M9B-O009'
  WHERE c.tracker_id = 'M9B-C009'
  RETURNING link_id
)
INSERT INTO _m9_link_map (tracker_id, link_id) SELECT 'M9B-L009', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M9B-L010"}'
  FROM _m9_claim_map c
  JOIN _m9_observation_map o ON o.tracker_id = 'M9B-O010'
  WHERE c.tracker_id = 'M9B-C010'
  RETURNING link_id
)
INSERT INTO _m9_link_map (tracker_id, link_id) SELECT 'M9B-L010', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M9B-L011"}'
  FROM _m9_claim_map c
  JOIN _m9_observation_map o ON o.tracker_id = 'M9B-O011'
  WHERE c.tracker_id = 'M9B-C011'
  RETURNING link_id
)
INSERT INTO _m9_link_map (tracker_id, link_id) SELECT 'M9B-L011', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M9B-L012"}'
  FROM _m9_claim_map c
  JOIN _m9_observation_map o ON o.tracker_id = 'M9B-O012'
  WHERE c.tracker_id = 'M9B-C012'
  RETURNING link_id
)
INSERT INTO _m9_link_map (tracker_id, link_id) SELECT 'M9B-L012', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M9B-L013"}'
  FROM _m9_claim_map c
  JOIN _m9_observation_map o ON o.tracker_id = 'M9B-O013'
  WHERE c.tracker_id = 'M9B-C013'
  RETURNING link_id
)
INSERT INTO _m9_link_map (tracker_id, link_id) SELECT 'M9B-L013', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M9B-L014"}'
  FROM _m9_claim_map c
  JOIN _m9_observation_map o ON o.tracker_id = 'M9B-O014'
  WHERE c.tracker_id = 'M9B-C014'
  RETURNING link_id
)
INSERT INTO _m9_link_map (tracker_id, link_id) SELECT 'M9B-L014', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M9B-L015"}'
  FROM _m9_claim_map c
  JOIN _m9_observation_map o ON o.tracker_id = 'M9B-O015'
  WHERE c.tracker_id = 'M9B-C015'
  RETURNING link_id
)
INSERT INTO _m9_link_map (tracker_id, link_id) SELECT 'M9B-L015', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M9B-L016"}'
  FROM _m9_claim_map c
  JOIN _m9_observation_map o ON o.tracker_id = 'M9B-O016'
  WHERE c.tracker_id = 'M9B-C016'
  RETURNING link_id
)
INSERT INTO _m9_link_map (tracker_id, link_id) SELECT 'M9B-L016', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M9B-L017"}'
  FROM _m9_claim_map c
  JOIN _m9_observation_map o ON o.tracker_id = 'M9B-O017'
  WHERE c.tracker_id = 'M9B-C017'
  RETURNING link_id
)
INSERT INTO _m9_link_map (tracker_id, link_id) SELECT 'M9B-L017', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M9B-L018"}'
  FROM _m9_claim_map c
  JOIN _m9_observation_map o ON o.tracker_id = 'M9B-O001'
  WHERE c.tracker_id = 'M9B-C001'
  RETURNING link_id
)
INSERT INTO _m9_link_map (tracker_id, link_id) SELECT 'M9B-L018', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M9B-L019"}'
  FROM _m9_claim_map c
  JOIN _m9_observation_map o ON o.tracker_id = 'M9B-O002'
  WHERE c.tracker_id = 'M9B-C002'
  RETURNING link_id
)
INSERT INTO _m9_link_map (tracker_id, link_id) SELECT 'M9B-L019', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M9B-L020"}'
  FROM _m9_claim_map c
  JOIN _m9_observation_map o ON o.tracker_id = 'M9B-O003'
  WHERE c.tracker_id = 'M9B-C003'
  RETURNING link_id
)
INSERT INTO _m9_link_map (tracker_id, link_id) SELECT 'M9B-L020', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M9B-L021"}'
  FROM _m9_claim_map c
  JOIN _m9_observation_map o ON o.tracker_id = 'M9B-O004'
  WHERE c.tracker_id = 'M9B-C004'
  RETURNING link_id
)
INSERT INTO _m9_link_map (tracker_id, link_id) SELECT 'M9B-L021', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M9B-L022"}'
  FROM _m9_claim_map c
  JOIN _m9_observation_map o ON o.tracker_id = 'M9B-O005'
  WHERE c.tracker_id = 'M9B-C005'
  RETURNING link_id
)
INSERT INTO _m9_link_map (tracker_id, link_id) SELECT 'M9B-L022', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M9B-L023"}'
  FROM _m9_claim_map c
  JOIN _m9_observation_map o ON o.tracker_id = 'M9B-O006'
  WHERE c.tracker_id = 'M9B-C006'
  RETURNING link_id
)
INSERT INTO _m9_link_map (tracker_id, link_id) SELECT 'M9B-L023', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M9B-L024"}'
  FROM _m9_claim_map c
  JOIN _m9_observation_map o ON o.tracker_id = 'M9B-O007'
  WHERE c.tracker_id = 'M9B-C007'
  RETURNING link_id
)
INSERT INTO _m9_link_map (tracker_id, link_id) SELECT 'M9B-L024', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M9B-L025"}'
  FROM _m9_claim_map c
  JOIN _m9_observation_map o ON o.tracker_id = 'M9B-O008'
  WHERE c.tracker_id = 'M9B-C008'
  RETURNING link_id
)
INSERT INTO _m9_link_map (tracker_id, link_id) SELECT 'M9B-L025', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M9B-L026"}'
  FROM _m9_claim_map c
  JOIN _m9_observation_map o ON o.tracker_id = 'M9B-O009'
  WHERE c.tracker_id = 'M9B-C009'
  RETURNING link_id
)
INSERT INTO _m9_link_map (tracker_id, link_id) SELECT 'M9B-L026', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M9B-L027"}'
  FROM _m9_claim_map c
  JOIN _m9_observation_map o ON o.tracker_id = 'M9B-O010'
  WHERE c.tracker_id = 'M9B-C010'
  RETURNING link_id
)
INSERT INTO _m9_link_map (tracker_id, link_id) SELECT 'M9B-L027', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M9B-L028"}'
  FROM _m9_claim_map c
  JOIN _m9_observation_map o ON o.tracker_id = 'M9B-O011'
  WHERE c.tracker_id = 'M9B-C011'
  RETURNING link_id
)
INSERT INTO _m9_link_map (tracker_id, link_id) SELECT 'M9B-L028', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M9B-L029"}'
  FROM _m9_claim_map c
  JOIN _m9_observation_map o ON o.tracker_id = 'M9B-O012'
  WHERE c.tracker_id = 'M9B-C012'
  RETURNING link_id
)
INSERT INTO _m9_link_map (tracker_id, link_id) SELECT 'M9B-L029', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M9B-L030"}'
  FROM _m9_claim_map c
  JOIN _m9_observation_map o ON o.tracker_id = 'M9B-O013'
  WHERE c.tracker_id = 'M9B-C013'
  RETURNING link_id
)
INSERT INTO _m9_link_map (tracker_id, link_id) SELECT 'M9B-L030', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M9B-L031"}'
  FROM _m9_claim_map c
  JOIN _m9_observation_map o ON o.tracker_id = 'M9B-O014'
  WHERE c.tracker_id = 'M9B-C014'
  RETURNING link_id
)
INSERT INTO _m9_link_map (tracker_id, link_id) SELECT 'M9B-L031', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M9B-L032"}'
  FROM _m9_claim_map c
  JOIN _m9_observation_map o ON o.tracker_id = 'M9B-O015'
  WHERE c.tracker_id = 'M9B-C015'
  RETURNING link_id
)
INSERT INTO _m9_link_map (tracker_id, link_id) SELECT 'M9B-L032', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M9B-L033"}'
  FROM _m9_claim_map c
  JOIN _m9_observation_map o ON o.tracker_id = 'M9B-O016'
  WHERE c.tracker_id = 'M9B-C016'
  RETURNING link_id
)
INSERT INTO _m9_link_map (tracker_id, link_id) SELECT 'M9B-L033', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M9B-L034"}'
  FROM _m9_claim_map c
  JOIN _m9_observation_map o ON o.tracker_id = 'M9B-O017'
  WHERE c.tracker_id = 'M9B-C017'
  RETURNING link_id
)
INSERT INTO _m9_link_map (tracker_id, link_id) SELECT 'M9B-L034', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M9B-L035"}'
  FROM _m9_claim_map c
  JOIN _m9_observation_map o ON o.tracker_id = 'M9B-O001'
  WHERE c.tracker_id = 'M9B-C001'
  RETURNING link_id
)
INSERT INTO _m9_link_map (tracker_id, link_id) SELECT 'M9B-L035', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M9B-L036"}'
  FROM _m9_claim_map c
  JOIN _m9_observation_map o ON o.tracker_id = 'M9B-O002'
  WHERE c.tracker_id = 'M9B-C002'
  RETURNING link_id
)
INSERT INTO _m9_link_map (tracker_id, link_id) SELECT 'M9B-L036', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M9B-L037"}'
  FROM _m9_claim_map c
  JOIN _m9_observation_map o ON o.tracker_id = 'M9B-O003'
  WHERE c.tracker_id = 'M9B-C003'
  RETURNING link_id
)
INSERT INTO _m9_link_map (tracker_id, link_id) SELECT 'M9B-L037', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M9B-L038"}'
  FROM _m9_claim_map c
  JOIN _m9_observation_map o ON o.tracker_id = 'M9B-O004'
  WHERE c.tracker_id = 'M9B-C004'
  RETURNING link_id
)
INSERT INTO _m9_link_map (tracker_id, link_id) SELECT 'M9B-L038', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M9B-L039"}'
  FROM _m9_claim_map c
  JOIN _m9_observation_map o ON o.tracker_id = 'M9B-O005'
  WHERE c.tracker_id = 'M9B-C005'
  RETURNING link_id
)
INSERT INTO _m9_link_map (tracker_id, link_id) SELECT 'M9B-L039', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M9B-L040"}'
  FROM _m9_claim_map c
  JOIN _m9_observation_map o ON o.tracker_id = 'M9B-O006'
  WHERE c.tracker_id = 'M9B-C006'
  RETURNING link_id
)
INSERT INTO _m9_link_map (tracker_id, link_id) SELECT 'M9B-L040', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Culture format boundaries is consensus-ready as a first-pass boundary statement, but requires full-text/results upgrades before quantitative or causal strength claims.',
    'M9B-T001',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M9B-B001", "M9B-B002", "M9B-B003", "M9B-B004", "M9B-B005", "M9B-B006", "M9B-B007", "M9B-B008"], "claim_tracker_ids": ["M9B-C001", "M9B-C002", "M9B-C003"], "consensus_draft_id": "M9B-S001", "observation_tracker_ids": ["M9B-O001", "M9B-O002"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 9 first-pass curation freeze.", "topic_id": "M9B-T001"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m9_consensus_map (tracker_id, consensus_id) SELECT 'M9B-S001', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m9_consensus_map c
JOIN _m9_observation_map o ON o.tracker_id = 'M9B-O001'
WHERE c.tracker_id = 'M9B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m9_consensus_map c
JOIN _m9_observation_map o ON o.tracker_id = 'M9B-O002'
WHERE c.tracker_id = 'M9B-S001';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Cell-source and maturity boundaries is consensus-ready as a first-pass boundary statement, but requires full-text/results upgrades before quantitative or causal strength claims.',
    'M9B-T002',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M9B-B001", "M9B-B002", "M9B-B003", "M9B-B004", "M9B-B005", "M9B-B006", "M9B-B007", "M9B-B008"], "claim_tracker_ids": ["M9B-C004", "M9B-C005", "M9B-C006"], "consensus_draft_id": "M9B-S002", "observation_tracker_ids": ["M9B-O003", "M9B-O004"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 9 first-pass curation freeze.", "topic_id": "M9B-T002"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m9_consensus_map (tracker_id, consensus_id) SELECT 'M9B-S002', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m9_consensus_map c
JOIN _m9_observation_map o ON o.tracker_id = 'M9B-O003'
WHERE c.tracker_id = 'M9B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m9_consensus_map c
JOIN _m9_observation_map o ON o.tracker_id = 'M9B-O004'
WHERE c.tracker_id = 'M9B-S002';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Injury stimulus boundaries is consensus-ready as a first-pass boundary statement, but requires full-text/results upgrades before quantitative or causal strength claims.',
    'M9B-T003',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M9B-B001", "M9B-B002", "M9B-B003", "M9B-B004", "M9B-B005", "M9B-B006", "M9B-B007", "M9B-B008"], "claim_tracker_ids": ["M9B-C007", "M9B-C008", "M9B-C009"], "consensus_draft_id": "M9B-S003", "observation_tracker_ids": ["M9B-O005", "M9B-O006"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 9 first-pass curation freeze.", "topic_id": "M9B-T003"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m9_consensus_map (tracker_id, consensus_id) SELECT 'M9B-S003', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m9_consensus_map c
JOIN _m9_observation_map o ON o.tracker_id = 'M9B-O005'
WHERE c.tracker_id = 'M9B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m9_consensus_map c
JOIN _m9_observation_map o ON o.tracker_id = 'M9B-O006'
WHERE c.tracker_id = 'M9B-S003';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Assay/readout boundaries is consensus-ready as a first-pass boundary statement, but requires full-text/results upgrades before quantitative or causal strength claims.',
    'M9B-T004',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M9B-B001", "M9B-B002", "M9B-B003", "M9B-B004", "M9B-B005", "M9B-B006", "M9B-B007", "M9B-B008"], "claim_tracker_ids": ["M9B-C010", "M9B-C011", "M9B-C012"], "consensus_draft_id": "M9B-S004", "observation_tracker_ids": ["M9B-O007", "M9B-O008"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 9 first-pass curation freeze.", "topic_id": "M9B-T004"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m9_consensus_map (tracker_id, consensus_id) SELECT 'M9B-S004', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m9_consensus_map c
JOIN _m9_observation_map o ON o.tracker_id = 'M9B-O007'
WHERE c.tracker_id = 'M9B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m9_consensus_map c
JOIN _m9_observation_map o ON o.tracker_id = 'M9B-O008'
WHERE c.tracker_id = 'M9B-S004';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Matrix/debris model boundaries is consensus-ready as a first-pass boundary statement, but requires full-text/results upgrades before quantitative or causal strength claims.',
    'M9B-T005',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M9B-B001", "M9B-B002", "M9B-B003", "M9B-B004", "M9B-B005", "M9B-B006", "M9B-B007", "M9B-B008"], "claim_tracker_ids": ["M9B-C013", "M9B-C014", "M9B-C015"], "consensus_draft_id": "M9B-S005", "observation_tracker_ids": ["M9B-O009", "M9B-O010"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 9 first-pass curation freeze.", "topic_id": "M9B-T005"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m9_consensus_map (tracker_id, consensus_id) SELECT 'M9B-S005', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m9_consensus_map c
JOIN _m9_observation_map o ON o.tracker_id = 'M9B-O009'
WHERE c.tracker_id = 'M9B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m9_consensus_map c
JOIN _m9_observation_map o ON o.tracker_id = 'M9B-O010'
WHERE c.tracker_id = 'M9B-S005';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Biomaterial compatibility boundaries is consensus-ready as a first-pass boundary statement, but requires full-text/results upgrades before quantitative or causal strength claims.',
    'M9B-T006',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M9B-B001", "M9B-B002", "M9B-B003", "M9B-B004", "M9B-B005", "M9B-B006", "M9B-B007", "M9B-B008"], "claim_tracker_ids": ["M9B-C016", "M9B-C017"], "consensus_draft_id": "M9B-S006", "observation_tracker_ids": ["M9B-O011", "M9B-O012"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 9 first-pass curation freeze.", "topic_id": "M9B-T006"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m9_consensus_map (tracker_id, consensus_id) SELECT 'M9B-S006', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m9_consensus_map c
JOIN _m9_observation_map o ON o.tracker_id = 'M9B-O011'
WHERE c.tracker_id = 'M9B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m9_consensus_map c
JOIN _m9_observation_map o ON o.tracker_id = 'M9B-O012'
WHERE c.tracker_id = 'M9B-S006';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Organoid/slice/explant translation boundaries is consensus-ready as a first-pass boundary statement, but requires full-text/results upgrades before quantitative or causal strength claims.',
    'M9B-T007',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M9B-B001", "M9B-B002", "M9B-B003", "M9B-B004", "M9B-B005", "M9B-B006", "M9B-B007", "M9B-B008"], "claim_tracker_ids": ["M9B-C017"], "consensus_draft_id": "M9B-S007", "observation_tracker_ids": ["M9B-O013", "M9B-O014"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 9 first-pass curation freeze.", "topic_id": "M9B-T007"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m9_consensus_map (tracker_id, consensus_id) SELECT 'M9B-S007', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m9_consensus_map c
JOIN _m9_observation_map o ON o.tracker_id = 'M9B-O013'
WHERE c.tracker_id = 'M9B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m9_consensus_map c
JOIN _m9_observation_map o ON o.tracker_id = 'M9B-O014'
WHERE c.tracker_id = 'M9B-S007';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'In vitro confidence boundaries is consensus-ready as a first-pass boundary statement, but requires full-text/results upgrades before quantitative or causal strength claims.',
    'M9B-T008',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M9B-B001", "M9B-B002", "M9B-B003", "M9B-B004", "M9B-B005", "M9B-B006", "M9B-B007", "M9B-B008"], "claim_tracker_ids": ["M9B-C017"], "consensus_draft_id": "M9B-S008", "observation_tracker_ids": ["M9B-O015", "M9B-O016"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 9 first-pass curation freeze.", "topic_id": "M9B-T008"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m9_consensus_map (tracker_id, consensus_id) SELECT 'M9B-S008', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m9_consensus_map c
JOIN _m9_observation_map o ON o.tracker_id = 'M9B-O015'
WHERE c.tracker_id = 'M9B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m9_consensus_map c
JOIN _m9_observation_map o ON o.tracker_id = 'M9B-O016'
WHERE c.tracker_id = 'M9B-S008';

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
  SELECT COUNT(*) INTO paper_count FROM _m9_paper_map;
  SELECT COUNT(*) INTO experiment_count FROM _m9_experiment_map;
  SELECT COUNT(*) INTO observation_count FROM _m9_observation_map;
  SELECT COUNT(*) INTO claim_count FROM _m9_claim_map;
  SELECT COUNT(*) INTO link_count FROM _m9_link_map;
  SELECT COUNT(*) INTO consensus_count FROM _m9_consensus_map;
  SELECT COUNT(*) INTO consensus_observation_count
  FROM Consensus_Observation co
  JOIN _m9_consensus_map cm ON cm.consensus_id = co.consensus_id;
  IF paper_count <> 17 THEN RAISE EXCEPTION 'Expected 17 papers, found %', paper_count; END IF;
  IF experiment_count <> 17 THEN RAISE EXCEPTION 'Unexpected experiment count %', experiment_count; END IF;
  IF observation_count <> 17 THEN RAISE EXCEPTION 'Expected 17 observations, found %', observation_count; END IF;
  IF claim_count <> 17 THEN RAISE EXCEPTION 'Expected 17 claims, found %', claim_count; END IF;
  IF link_count <> 40 THEN RAISE EXCEPTION 'Expected 40 evidence links, found %', link_count; END IF;
  IF consensus_count <> 8 THEN RAISE EXCEPTION 'Expected 8 consensus rows, found %', consensus_count; END IF;
  IF consensus_observation_count <> 16 THEN RAISE EXCEPTION 'Unexpected consensus-observation count %', consensus_observation_count; END IF;
END $$;

COMMIT;
