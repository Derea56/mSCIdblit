-- Module 8B full first-pass materialization generated from tracker-derived JSON.
-- This script is intended for a fresh database loaded with schema/schema.sql and scripts/seed_controlled_vocab.sql.
BEGIN;

CREATE TEMP TABLE _m8_paper_map (tracker_id TEXT PRIMARY KEY, paper_id INTEGER NOT NULL);
CREATE TEMP TABLE _m8_paradigm_map (tracker_id TEXT PRIMARY KEY, paradigm_id INTEGER NOT NULL);
CREATE TEMP TABLE _m8_experiment_map (tracker_id TEXT PRIMARY KEY, experiment_id INTEGER NOT NULL);
CREATE TEMP TABLE _m8_observation_map (tracker_id TEXT PRIMARY KEY, observation_id INTEGER NOT NULL);
CREATE TEMP TABLE _m8_claim_map (tracker_id TEXT PRIMARY KEY, claim_id INTEGER NOT NULL);
CREATE TEMP TABLE _m8_link_map (tracker_id TEXT PRIMARY KEY, link_id INTEGER NOT NULL);
CREATE TEMP TABLE _m8_consensus_map (tracker_id TEXT PRIMARY KEY, consensus_id INTEGER NOT NULL);

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Animal models of spinal cord injury: a systematic review.', 'Sharif-Alhoseini M', 2017,
    NULL, NULL, NULL,
    NULL, NULL, '28117332',
    NULL, '{"curator_notes": "PRISMA-guided systematic review. To provide a comprehensive framework of the current animal models for investigating", "module": "Module 8B", "tracker_id": "M8A-P001"}'
  )
  RETURNING paper_id
)
INSERT INTO _m8_paper_map (tracker_id, paper_id) SELECT 'M8A-P001', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Animal Models of Spinal Cord Injury.', 'Sobolev VE', 2025,
    NULL, NULL, NULL,
    NULL, NULL, '40564146',
    NULL, '{"curator_notes": "Spinal cord injury (SCI) is one of the most frequent causes of disability, accompanied by motor and postural", "module": "Module 8B", "tracker_id": "M8A-P002"}'
  )
  RETURNING paper_id
)
INSERT INTO _m8_paper_map (tracker_id, paper_id) SELECT 'M8A-P002', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Biomaterial-based interventions for neuronal regeneration and functional recovery in rodent model of spinal cord injury: a systematic review.', 'Krishna V', 2013,
    NULL, NULL, NULL,
    NULL, NULL, '23809587',
    NULL, '{"curator_notes": "There is considerable interest in translating laboratory advances in neuronal regeneration following spinal cord injury", "module": "Module 8B", "tracker_id": "M8A-P003"}'
  )
  RETURNING paper_id
)
INSERT INTO _m8_paper_map (tracker_id, paper_id) SELECT 'M8A-P003', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Spinal cord injury models: a review.', 'Cheriyan T', 2014,
    NULL, NULL, NULL,
    NULL, NULL, '24912546',
    NULL, '{"curator_notes": "Animal spinal cord injury (SCI) models have proved invaluable in better understanding the mechanisms involved in", "module": "Module 8B", "tracker_id": "M8A-P004"}'
  )
  RETURNING paper_id
)
INSERT INTO _m8_paper_map (tracker_id, paper_id) SELECT 'M8A-P004', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'A valuable animal model of spinal cord injury to study motor dysfunctions, comorbid conditions, and aging associated diseases.', 'Rouleau P', 2013,
    NULL, NULL, NULL,
    NULL, NULL, '23360275',
    NULL, '{"curator_notes": "Most animal models of contused, compressed or transected spinal cord injury (SCI) require a laminectomy to be", "module": "Module 8B", "tracker_id": "M8A-P005"}'
  )
  RETURNING paper_id
)
INSERT INTO _m8_paper_map (tracker_id, paper_id) SELECT 'M8A-P005', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Time-dependent microglia and macrophages response after traumatic spinal cord injury in rat: a systematic review.', 'Rezvan M', 2020,
    NULL, NULL, NULL,
    NULL, NULL, '32665068',
    NULL, '{"curator_notes": "To acquire evidence-based knowledge in temporal and spatial patterns of microglia/macrophages changes to facilitate", "module": "Module 8B", "tracker_id": "M8A-P006"}'
  )
  RETURNING paper_id
)
INSERT INTO _m8_paper_map (tracker_id, paper_id) SELECT 'M8A-P006', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Neuromethods and assessment tools for traumatic spinal cord injury in rodents: A mini review.', 'Kalotra S', 2025,
    NULL, NULL, NULL,
    NULL, NULL, '40398195',
    NULL, '{"curator_notes": "Spinal cord injury (SCI) is one of the most devastating neurological disorders associated with severe locomotor", "module": "Module 8B", "tracker_id": "M8A-P007"}'
  )
  RETURNING paper_id
)
INSERT INTO _m8_paper_map (tracker_id, paper_id) SELECT 'M8A-P007', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Animal models used in spinal cord regeneration research.', 'Kwon BK', 2002,
    NULL, NULL, NULL,
    NULL, NULL, '12131708',
    NULL, '{"curator_notes": "A literature review was conducted. To review animal models and injury paradigms used in the neurobiologic study of", "module": "Module 8B", "tracker_id": "M8A-P008"}'
  )
  RETURNING paper_id
)
INSERT INTO _m8_paper_map (tracker_id, paper_id) SELECT 'M8A-P008', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Rodent models for treatment of spinal cord injury: research trends and progress toward useful repair.', 'Rosenzweig ES', 2004,
    NULL, NULL, NULL,
    NULL, NULL, '15021237',
    NULL, '{"curator_notes": "In this review, we have documented some current research trends in rodent models of spinal cord injury. We have also", "module": "Module 8B", "tracker_id": "M8A-P009"}'
  )
  RETURNING paper_id
)
INSERT INTO _m8_paper_map (tracker_id, paper_id) SELECT 'M8A-P009', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Brain-derived neurotrophic factor (BDNF) as biomarker in stem cell-based therapies of preclinical spinal cord injury models: A systematic review.', 'Abbaszadeh ME', 2025,
    NULL, NULL, NULL,
    NULL, NULL, '40147167',
    NULL, '{"curator_notes": "Stem cell-based therapies offer promising treatment for spinal cord injury (SCI) by reducing inflammation, restoring", "module": "Module 8B", "tracker_id": "M8A-P010"}'
  )
  RETURNING paper_id
)
INSERT INTO _m8_paper_map (tracker_id, paper_id) SELECT 'M8A-P010', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Tissue displacement and impact force are important contributors to outcome after spinal cord contusion injury.', 'Ghasemlou N', 2005,
    NULL, NULL, NULL,
    NULL, NULL, '16023101',
    NULL, '{"curator_notes": "Spinal cord contusion injury in rodents is widely used as a model for spinal cord trauma in humans. Several", "module": "Module 8B", "tracker_id": "M8A-P011"}'
  )
  RETURNING paper_id
)
INSERT INTO _m8_paper_map (tracker_id, paper_id) SELECT 'M8A-P011', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'An electromechanical spinal injury technique with dynamic sensitivity.', 'Stokes BT', 1992,
    NULL, NULL, NULL,
    NULL, NULL, '1474607',
    NULL, '{"curator_notes": "Over the past decade, our laboratory has attempted to create a simple, accurate device that could be used to produce", "module": "Module 8B", "tracker_id": "M8A-P012"}'
  )
  RETURNING paper_id
)
INSERT INTO _m8_paper_map (tracker_id, paper_id) SELECT 'M8A-P012', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'CRISPR gRNA phenotypic screening in zebrafish reveals pro-regenerative genes in spinal cord injury.', 'Keatinge M', 2021,
    NULL, NULL, NULL,
    NULL, NULL, '33914736',
    NULL, '{"curator_notes": "Zebrafish exhibit robust regeneration following spinal cord injury, promoted by macrophages that control post-injury", "module": "Module 8B", "tracker_id": "M8A-P013"}'
  )
  RETURNING paper_id
)
INSERT INTO _m8_paper_map (tracker_id, paper_id) SELECT 'M8A-P013', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Understanding the pathophysiology of acute critical illness: translational lessons from zebrafish models.', 'Fujii K', 2024,
    NULL, NULL, NULL,
    NULL, NULL, '38291192',
    NULL, '{"curator_notes": "The models used to investigate the pathophysiological mechanisms of acute critical illness are not limited to mammalian", "module": "Module 8B", "tracker_id": "M8A-P014"}'
  )
  RETURNING paper_id
)
INSERT INTO _m8_paper_map (tracker_id, paper_id) SELECT 'M8A-P014', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Locomotor, sensorimotor, and pain outcomes after graded mid-thoracic contusion in female Sprague Dawley rats.', 'ODC-SCI dataset', 2026,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "ODC-SCI:1597; DOI 10.34945/F5C31D; promoted as graded T8 contusion severity and endpoint calibration evidence.", "module": "Module 8B", "tracker_id": "M8A-P015"}'
  )
  RETURNING paper_id
)
INSERT INTO _m8_paper_map (tracker_id, paper_id) SELECT 'M8A-P015', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Hemodynamics, weight, and overground locomotion from 1125 rats with thoracic contusion severities from MASCIS.', 'ODC-SCI dataset', 2026,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "ODC-SCI:595; DOI 10.34945/F5QG66; promoted as model-standardization raw-data anchor.", "module": "Module 8B", "tracker_id": "M8A-P016"}'
  )
  RETURNING paper_id
)
INSERT INTO _m8_paper_map (tracker_id, paper_id) SELECT 'M8A-P016', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'CLIMBER meta-analysis Part II: individual animal data from contusive injuries.', 'ODC-SCI dataset', 2026,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "ODC-SCI:1081; DOI 10.34945/F5J59P; promoted as cross-study species, injury-level, severity, and endpoint harmonization evidence.", "module": "Module 8B", "tracker_id": "M8A-P017"}'
  )
  RETURNING paper_id
)
INSERT INTO _m8_paper_map (tracker_id, paper_id) SELECT 'M8A-P017', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'CLIMBER meta-analysis Part I: literature-extracted data from contusive injuries.', 'ODC-SCI dataset', 2026,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "ODC-SCI:1082; DOI 10.34945/F5DG6D; promoted as complementary group-level model-system meta-analysis anchor.", "module": "Module 8B", "tracker_id": "M8A-P018"}'
  )
  RETURNING paper_id
)
INSERT INTO _m8_paper_map (tracker_id, paper_id) SELECT 'M8A-P018', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Cervical C5 unilateral SCI with diverse injury modalities, behavioral outcomes, and histopathology.', 'ODC-SCI dataset', 2026,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "ODC-SCI:26; DOI 10.7295/W9T72FMZ; promoted as cervical model-system and tract/endpoints boundary evidence.", "module": "Module 8B", "tracker_id": "M8A-P019"}'
  )
  RETURNING paper_id
)
INSERT INTO _m8_paper_map (tracker_id, paper_id) SELECT 'M8A-P019', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 8B curated evidence extraction',
    'First-pass Module 8B in vivo SCI model systems curation for M8A-P001',
    'Tracker-derived materialization from Module_8B_TRACKER.md'
  FROM _m8_paper_map WHERE tracker_id = 'M8A-P001'
  RETURNING paradigm_id
)
INSERT INTO _m8_paradigm_map (tracker_id, paradigm_id) SELECT 'M8A-P001', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 8B curated evidence extraction',
    'First-pass Module 8B in vivo SCI model systems curation for M8A-P002',
    'Tracker-derived materialization from Module_8B_TRACKER.md'
  FROM _m8_paper_map WHERE tracker_id = 'M8A-P002'
  RETURNING paradigm_id
)
INSERT INTO _m8_paradigm_map (tracker_id, paradigm_id) SELECT 'M8A-P002', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 8B curated evidence extraction',
    'First-pass Module 8B in vivo SCI model systems curation for M8A-P003',
    'Tracker-derived materialization from Module_8B_TRACKER.md'
  FROM _m8_paper_map WHERE tracker_id = 'M8A-P003'
  RETURNING paradigm_id
)
INSERT INTO _m8_paradigm_map (tracker_id, paradigm_id) SELECT 'M8A-P003', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 8B curated evidence extraction',
    'First-pass Module 8B in vivo SCI model systems curation for M8A-P004',
    'Tracker-derived materialization from Module_8B_TRACKER.md'
  FROM _m8_paper_map WHERE tracker_id = 'M8A-P004'
  RETURNING paradigm_id
)
INSERT INTO _m8_paradigm_map (tracker_id, paradigm_id) SELECT 'M8A-P004', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 8B curated evidence extraction',
    'First-pass Module 8B in vivo SCI model systems curation for M8A-P005',
    'Tracker-derived materialization from Module_8B_TRACKER.md'
  FROM _m8_paper_map WHERE tracker_id = 'M8A-P005'
  RETURNING paradigm_id
)
INSERT INTO _m8_paradigm_map (tracker_id, paradigm_id) SELECT 'M8A-P005', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 8B curated evidence extraction',
    'First-pass Module 8B in vivo SCI model systems curation for M8A-P006',
    'Tracker-derived materialization from Module_8B_TRACKER.md'
  FROM _m8_paper_map WHERE tracker_id = 'M8A-P006'
  RETURNING paradigm_id
)
INSERT INTO _m8_paradigm_map (tracker_id, paradigm_id) SELECT 'M8A-P006', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 8B curated evidence extraction',
    'First-pass Module 8B in vivo SCI model systems curation for M8A-P007',
    'Tracker-derived materialization from Module_8B_TRACKER.md'
  FROM _m8_paper_map WHERE tracker_id = 'M8A-P007'
  RETURNING paradigm_id
)
INSERT INTO _m8_paradigm_map (tracker_id, paradigm_id) SELECT 'M8A-P007', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 8B curated evidence extraction',
    'First-pass Module 8B in vivo SCI model systems curation for M8A-P008',
    'Tracker-derived materialization from Module_8B_TRACKER.md'
  FROM _m8_paper_map WHERE tracker_id = 'M8A-P008'
  RETURNING paradigm_id
)
INSERT INTO _m8_paradigm_map (tracker_id, paradigm_id) SELECT 'M8A-P008', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 8B curated evidence extraction',
    'First-pass Module 8B in vivo SCI model systems curation for M8A-P009',
    'Tracker-derived materialization from Module_8B_TRACKER.md'
  FROM _m8_paper_map WHERE tracker_id = 'M8A-P009'
  RETURNING paradigm_id
)
INSERT INTO _m8_paradigm_map (tracker_id, paradigm_id) SELECT 'M8A-P009', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 8B curated evidence extraction',
    'First-pass Module 8B in vivo SCI model systems curation for M8A-P010',
    'Tracker-derived materialization from Module_8B_TRACKER.md'
  FROM _m8_paper_map WHERE tracker_id = 'M8A-P010'
  RETURNING paradigm_id
)
INSERT INTO _m8_paradigm_map (tracker_id, paradigm_id) SELECT 'M8A-P010', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 8B curated evidence extraction',
    'First-pass Module 8B in vivo SCI model systems curation for M8A-P011',
    'Tracker-derived materialization from Module_8B_TRACKER.md'
  FROM _m8_paper_map WHERE tracker_id = 'M8A-P011'
  RETURNING paradigm_id
)
INSERT INTO _m8_paradigm_map (tracker_id, paradigm_id) SELECT 'M8A-P011', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 8B curated evidence extraction',
    'First-pass Module 8B in vivo SCI model systems curation for M8A-P012',
    'Tracker-derived materialization from Module_8B_TRACKER.md'
  FROM _m8_paper_map WHERE tracker_id = 'M8A-P012'
  RETURNING paradigm_id
)
INSERT INTO _m8_paradigm_map (tracker_id, paradigm_id) SELECT 'M8A-P012', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 8B curated evidence extraction',
    'First-pass Module 8B in vivo SCI model systems curation for M8A-P013',
    'Tracker-derived materialization from Module_8B_TRACKER.md'
  FROM _m8_paper_map WHERE tracker_id = 'M8A-P013'
  RETURNING paradigm_id
)
INSERT INTO _m8_paradigm_map (tracker_id, paradigm_id) SELECT 'M8A-P013', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 8B curated evidence extraction',
    'First-pass Module 8B in vivo SCI model systems curation for M8A-P014',
    'Tracker-derived materialization from Module_8B_TRACKER.md'
  FROM _m8_paper_map WHERE tracker_id = 'M8A-P014'
  RETURNING paradigm_id
)
INSERT INTO _m8_paradigm_map (tracker_id, paradigm_id) SELECT 'M8A-P014', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 8B curated evidence extraction',
    'First-pass Module 8B in vivo SCI model systems curation for M8A-P015',
    'Tracker-derived materialization from Module_8B_TRACKER.md'
  FROM _m8_paper_map WHERE tracker_id = 'M8A-P015'
  RETURNING paradigm_id
)
INSERT INTO _m8_paradigm_map (tracker_id, paradigm_id) SELECT 'M8A-P015', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 8B curated evidence extraction',
    'First-pass Module 8B in vivo SCI model systems curation for M8A-P016',
    'Tracker-derived materialization from Module_8B_TRACKER.md'
  FROM _m8_paper_map WHERE tracker_id = 'M8A-P016'
  RETURNING paradigm_id
)
INSERT INTO _m8_paradigm_map (tracker_id, paradigm_id) SELECT 'M8A-P016', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 8B curated evidence extraction',
    'First-pass Module 8B in vivo SCI model systems curation for M8A-P017',
    'Tracker-derived materialization from Module_8B_TRACKER.md'
  FROM _m8_paper_map WHERE tracker_id = 'M8A-P017'
  RETURNING paradigm_id
)
INSERT INTO _m8_paradigm_map (tracker_id, paradigm_id) SELECT 'M8A-P017', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 8B curated evidence extraction',
    'First-pass Module 8B in vivo SCI model systems curation for M8A-P018',
    'Tracker-derived materialization from Module_8B_TRACKER.md'
  FROM _m8_paper_map WHERE tracker_id = 'M8A-P018'
  RETURNING paradigm_id
)
INSERT INTO _m8_paradigm_map (tracker_id, paradigm_id) SELECT 'M8A-P018', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 8B curated evidence extraction',
    'First-pass Module 8B in vivo SCI model systems curation for M8A-P019',
    'Tracker-derived materialization from Module_8B_TRACKER.md'
  FROM _m8_paper_map WHERE tracker_id = 'M8A-P019'
  RETURNING paradigm_id
)
INSERT INTO _m8_paradigm_map (tracker_id, paradigm_id) SELECT 'M8A-P019', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / PubMed',
    'Tracker experiment M8A-P001-E001',
    'Module 8B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M8B-O001"], "source_experiment_tracker_id": "M8A-P001-E001", "source_paper_tracker_id": "M8A-P001", "tracker_key": "M8A-P001::M8A-P001-E001"}'
  FROM _m8_paper_map p
  JOIN _m8_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M8A-P001'
  RETURNING experiment_id
)
INSERT INTO _m8_experiment_map (tracker_id, experiment_id) SELECT 'M8A-P001::M8A-P001-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / PubMed',
    'Tracker experiment M8A-P002-E001',
    'Module 8B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M8B-O002"], "source_experiment_tracker_id": "M8A-P002-E001", "source_paper_tracker_id": "M8A-P002", "tracker_key": "M8A-P002::M8A-P002-E001"}'
  FROM _m8_paper_map p
  JOIN _m8_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M8A-P002'
  RETURNING experiment_id
)
INSERT INTO _m8_experiment_map (tracker_id, experiment_id) SELECT 'M8A-P002::M8A-P002-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / PubMed',
    'Tracker experiment M8A-P003-E001',
    'Module 8B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M8B-O003"], "source_experiment_tracker_id": "M8A-P003-E001", "source_paper_tracker_id": "M8A-P003", "tracker_key": "M8A-P003::M8A-P003-E001"}'
  FROM _m8_paper_map p
  JOIN _m8_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M8A-P003'
  RETURNING experiment_id
)
INSERT INTO _m8_experiment_map (tracker_id, experiment_id) SELECT 'M8A-P003::M8A-P003-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / PubMed',
    'Tracker experiment M8A-P004-E001',
    'Module 8B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M8B-O004"], "source_experiment_tracker_id": "M8A-P004-E001", "source_paper_tracker_id": "M8A-P004", "tracker_key": "M8A-P004::M8A-P004-E001"}'
  FROM _m8_paper_map p
  JOIN _m8_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M8A-P004'
  RETURNING experiment_id
)
INSERT INTO _m8_experiment_map (tracker_id, experiment_id) SELECT 'M8A-P004::M8A-P004-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / PubMed',
    'Tracker experiment M8A-P005-E001',
    'Module 8B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M8B-O005"], "source_experiment_tracker_id": "M8A-P005-E001", "source_paper_tracker_id": "M8A-P005", "tracker_key": "M8A-P005::M8A-P005-E001"}'
  FROM _m8_paper_map p
  JOIN _m8_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M8A-P005'
  RETURNING experiment_id
)
INSERT INTO _m8_experiment_map (tracker_id, experiment_id) SELECT 'M8A-P005::M8A-P005-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / PubMed',
    'Tracker experiment M8A-P006-E001',
    'Module 8B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M8B-O006"], "source_experiment_tracker_id": "M8A-P006-E001", "source_paper_tracker_id": "M8A-P006", "tracker_key": "M8A-P006::M8A-P006-E001"}'
  FROM _m8_paper_map p
  JOIN _m8_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M8A-P006'
  RETURNING experiment_id
)
INSERT INTO _m8_experiment_map (tracker_id, experiment_id) SELECT 'M8A-P006::M8A-P006-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / PubMed',
    'Tracker experiment M8A-P007-E001',
    'Module 8B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M8B-O007"], "source_experiment_tracker_id": "M8A-P007-E001", "source_paper_tracker_id": "M8A-P007", "tracker_key": "M8A-P007::M8A-P007-E001"}'
  FROM _m8_paper_map p
  JOIN _m8_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M8A-P007'
  RETURNING experiment_id
)
INSERT INTO _m8_experiment_map (tracker_id, experiment_id) SELECT 'M8A-P007::M8A-P007-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / PubMed',
    'Tracker experiment M8A-P008-E001',
    'Module 8B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M8B-O008"], "source_experiment_tracker_id": "M8A-P008-E001", "source_paper_tracker_id": "M8A-P008", "tracker_key": "M8A-P008::M8A-P008-E001"}'
  FROM _m8_paper_map p
  JOIN _m8_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M8A-P008'
  RETURNING experiment_id
)
INSERT INTO _m8_experiment_map (tracker_id, experiment_id) SELECT 'M8A-P008::M8A-P008-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / PubMed',
    'Tracker experiment M8A-P009-E001',
    'Module 8B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M8B-O009"], "source_experiment_tracker_id": "M8A-P009-E001", "source_paper_tracker_id": "M8A-P009", "tracker_key": "M8A-P009::M8A-P009-E001"}'
  FROM _m8_paper_map p
  JOIN _m8_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M8A-P009'
  RETURNING experiment_id
)
INSERT INTO _m8_experiment_map (tracker_id, experiment_id) SELECT 'M8A-P009::M8A-P009-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / PubMed',
    'Tracker experiment M8A-P010-E001',
    'Module 8B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M8B-O010"], "source_experiment_tracker_id": "M8A-P010-E001", "source_paper_tracker_id": "M8A-P010", "tracker_key": "M8A-P010::M8A-P010-E001"}'
  FROM _m8_paper_map p
  JOIN _m8_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M8A-P010'
  RETURNING experiment_id
)
INSERT INTO _m8_experiment_map (tracker_id, experiment_id) SELECT 'M8A-P010::M8A-P010-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / PubMed',
    'Tracker experiment M8A-P011-E001',
    'Module 8B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M8B-O011"], "source_experiment_tracker_id": "M8A-P011-E001", "source_paper_tracker_id": "M8A-P011", "tracker_key": "M8A-P011::M8A-P011-E001"}'
  FROM _m8_paper_map p
  JOIN _m8_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M8A-P011'
  RETURNING experiment_id
)
INSERT INTO _m8_experiment_map (tracker_id, experiment_id) SELECT 'M8A-P011::M8A-P011-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / PubMed',
    'Tracker experiment M8A-P012-E001',
    'Module 8B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M8B-O012"], "source_experiment_tracker_id": "M8A-P012-E001", "source_paper_tracker_id": "M8A-P012", "tracker_key": "M8A-P012::M8A-P012-E001"}'
  FROM _m8_paper_map p
  JOIN _m8_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M8A-P012'
  RETURNING experiment_id
)
INSERT INTO _m8_experiment_map (tracker_id, experiment_id) SELECT 'M8A-P012::M8A-P012-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / PubMed',
    'Tracker experiment M8A-P013-E001',
    'Module 8B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M8B-O013"], "source_experiment_tracker_id": "M8A-P013-E001", "source_paper_tracker_id": "M8A-P013", "tracker_key": "M8A-P013::M8A-P013-E001"}'
  FROM _m8_paper_map p
  JOIN _m8_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M8A-P013'
  RETURNING experiment_id
)
INSERT INTO _m8_experiment_map (tracker_id, experiment_id) SELECT 'M8A-P013::M8A-P013-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / PubMed',
    'Tracker experiment M8A-P014-E001',
    'Module 8B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M8B-O014"], "source_experiment_tracker_id": "M8A-P014-E001", "source_paper_tracker_id": "M8A-P014", "tracker_key": "M8A-P014::M8A-P014-E001"}'
  FROM _m8_paper_map p
  JOIN _m8_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M8A-P014'
  RETURNING experiment_id
)
INSERT INTO _m8_experiment_map (tracker_id, experiment_id) SELECT 'M8A-P014::M8A-P014-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ODC-SCI dataset page',
    'Tracker experiment M8A-P015-E001',
    'Module 8B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M8B-O015"], "source_experiment_tracker_id": "M8A-P015-E001", "source_paper_tracker_id": "M8A-P015", "tracker_key": "M8A-P015::M8A-P015-E001"}'
  FROM _m8_paper_map p
  JOIN _m8_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M8A-P015'
  RETURNING experiment_id
)
INSERT INTO _m8_experiment_map (tracker_id, experiment_id) SELECT 'M8A-P015::M8A-P015-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ODC-SCI dataset page',
    'Tracker experiment M8A-P016-E001',
    'Module 8B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M8B-O016"], "source_experiment_tracker_id": "M8A-P016-E001", "source_paper_tracker_id": "M8A-P016", "tracker_key": "M8A-P016::M8A-P016-E001"}'
  FROM _m8_paper_map p
  JOIN _m8_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M8A-P016'
  RETURNING experiment_id
)
INSERT INTO _m8_experiment_map (tracker_id, experiment_id) SELECT 'M8A-P016::M8A-P016-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ODC-SCI dataset page',
    'Tracker experiment M8A-P017-E001',
    'Module 8B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M8B-O017"], "source_experiment_tracker_id": "M8A-P017-E001", "source_paper_tracker_id": "M8A-P017", "tracker_key": "M8A-P017::M8A-P017-E001"}'
  FROM _m8_paper_map p
  JOIN _m8_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M8A-P017'
  RETURNING experiment_id
)
INSERT INTO _m8_experiment_map (tracker_id, experiment_id) SELECT 'M8A-P017::M8A-P017-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ODC-SCI dataset page',
    'Tracker experiment M8A-P018-E001',
    'Module 8B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M8B-O018"], "source_experiment_tracker_id": "M8A-P018-E001", "source_paper_tracker_id": "M8A-P018", "tracker_key": "M8A-P018::M8A-P018-E001"}'
  FROM _m8_paper_map p
  JOIN _m8_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M8A-P018'
  RETURNING experiment_id
)
INSERT INTO _m8_experiment_map (tracker_id, experiment_id) SELECT 'M8A-P018::M8A-P018-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ODC-SCI dataset page',
    'Tracker experiment M8A-P019-E001',
    'Module 8B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M8B-O019"], "source_experiment_tracker_id": "M8A-P019-E001", "source_paper_tracker_id": "M8A-P019", "tracker_key": "M8A-P019::M8A-P019-E001"}'
  FROM _m8_paper_map p
  JOIN _m8_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M8A-P019'
  RETURNING experiment_id
)
INSERT INTO _m8_experiment_map (tracker_id, experiment_id) SELECT 'M8A-P019::M8A-P019-E001', experiment_id FROM inserted;

INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Dataset/harmonization evidence', 'Module 8B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Dataset/model boundary evidence', 'Module 8B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Dataset/model calibration evidence', 'Module 8B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Model-system evidence', 'Module 8B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;

INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('cervical unilateral multimodal injury dataset', 'Module 8B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('compression/clip injury model', 'Module 8B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('contusion injury model', 'Module 8B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('graded thoracic contusion calibration dataset', 'Module 8B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('in vivo SCI model taxonomy', 'Module 8B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('individual-animal contusion harmonization dataset', 'Module 8B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('large-scale MASCIS contusion severity dataset', 'Module 8B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('literature-extracted contusion harmonization dataset', 'Module 8B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('regenerative zebrafish SCI model', 'Module 8B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('transection/hemisection model', 'Module 8B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'PRISMA-guided systematic review. To provide a comprehensive framework of the current animal models for investigating spinal cord injury (SCI) and categorize them based on the aims, patterns and levels of injury, and outcome measurements as well as animal species. Sina Trauma and Surgery Research Center, Tehran University of Medical Sciences, Tehran, Iran. An electronic search of the Medline database for literature describing animal models of SCI was',
    'qualitative',
    NULL,
    'PRISMA-guided systematic review. To provide a comprehensive framework of the current animal models for investigating spinal cord injury (SCI) and categorize them based on the aims, patterns and levels of injury, and outcome measurements as well as animal species. Sina Trauma and Surgery Research Center, Tehran University of Medical Sciences, Tehran, Iran. An electronic search of the Medline database for literature describing animal models of SCI was',
    'in vivo sci model taxonomy',
    'PubMed/source metadata',
    'Abstract / PubMed',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M8A-P001-E001", "measurement_method_inference": null, "paper_tracker_id": "M8A-P001", "quantitative": "NO", "statistics_reported": "Source-page first pass; exact statistics not extracted", "topic_id": "M8B-T001", "tracker_id": "M8B-O001"}'
  FROM _m8_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M8A-P001::M8A-P001-E001'
    AND et.evidence_type_name = 'Model-system evidence'
    AND ot.outcome_type_name = 'in vivo SCI model taxonomy'
  RETURNING observation_id
)
INSERT INTO _m8_observation_map (tracker_id, observation_id) SELECT 'M8B-O001', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Spinal cord injury (SCI) is one of the most frequent causes of disability, accompanied by motor and postural impairments, as well as autonomic and behavioural disorders. Since the beginning of the last century, researchers have been developing and refining experimental models of SCI to study pathogenesis and find therapies. Since the beginning of the 20th century, quite a wide range of methods have been developed for contusion and compression injury,',
    'qualitative',
    NULL,
    'Spinal cord injury (SCI) is one of the most frequent causes of disability, accompanied by motor and postural impairments, as well as autonomic and behavioural disorders. Since the beginning of the last century, researchers have been developing and refining experimental models of SCI to study pathogenesis and find therapies. Since the beginning of the 20th century, quite a wide range of methods have been developed for contusion and compression injury,',
    'compression/clip injury model',
    'PubMed/source metadata',
    'Abstract / PubMed',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M8A-P002-E001", "measurement_method_inference": null, "paper_tracker_id": "M8A-P002", "quantitative": "NO", "statistics_reported": "Source-page first pass; exact statistics not extracted", "topic_id": "M8B-T002", "tracker_id": "M8B-O002"}'
  FROM _m8_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M8A-P002::M8A-P002-E001'
    AND et.evidence_type_name = 'Model-system evidence'
    AND ot.outcome_type_name = 'compression/clip injury model'
  RETURNING observation_id
)
INSERT INTO _m8_observation_map (tracker_id, observation_id) SELECT 'M8B-O002', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'There is considerable interest in translating laboratory advances in neuronal regeneration following spinal cord injury (SCI). A multimodality approach has been advocated for successful functional neuronal regeneration. With this goal in mind several biomaterials have been employed as neuronal bridges either to support cellular transplants, to release neurotrophic factors, or to do both. A systematic review of this literature is lacking. Such a review may',
    'qualitative',
    NULL,
    'There is considerable interest in translating laboratory advances in neuronal regeneration following spinal cord injury (SCI). A multimodality approach has been advocated for successful functional neuronal regeneration. With this goal in mind several biomaterials have been employed as neuronal bridges either to support cellular transplants, to release neurotrophic factors, or to do both. A systematic review of this literature is lacking. Such a review may',
    'in vivo sci model taxonomy',
    'PubMed/source metadata',
    'Abstract / PubMed',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M8A-P003-E001", "measurement_method_inference": null, "paper_tracker_id": "M8A-P003", "quantitative": "NO", "statistics_reported": "Source-page first pass; exact statistics not extracted", "topic_id": "M8B-T003", "tracker_id": "M8B-O003"}'
  FROM _m8_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M8A-P003::M8A-P003-E001'
    AND et.evidence_type_name = 'Model-system evidence'
    AND ot.outcome_type_name = 'in vivo SCI model taxonomy'
  RETURNING observation_id
)
INSERT INTO _m8_observation_map (tracker_id, observation_id) SELECT 'M8B-O003', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Animal spinal cord injury (SCI) models have proved invaluable in better understanding the mechanisms involved in traumatic SCI and evaluating the effectiveness of experimental therapeutic interventions. Over the past 25 years, substantial gains have been made in developing consistent, reproducible and reliable animal SCI models. Review. The objective of this review was to consolidate current knowledge on SCI models and introduce newer paradigms that are',
    'qualitative',
    NULL,
    'Animal spinal cord injury (SCI) models have proved invaluable in better understanding the mechanisms involved in traumatic SCI and evaluating the effectiveness of experimental therapeutic interventions. Over the past 25 years, substantial gains have been made in developing consistent, reproducible and reliable animal SCI models. Review. The objective of this review was to consolidate current knowledge on SCI models and introduce newer paradigms that are',
    'compression/clip injury model',
    'PubMed/source metadata',
    'Abstract / PubMed',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M8A-P004-E001", "measurement_method_inference": null, "paper_tracker_id": "M8A-P004", "quantitative": "NO", "statistics_reported": "Source-page first pass; exact statistics not extracted", "topic_id": "M8B-T004", "tracker_id": "M8B-O004"}'
  FROM _m8_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M8A-P004::M8A-P004-E001'
    AND et.evidence_type_name = 'Model-system evidence'
    AND ot.outcome_type_name = 'compression/clip injury model'
  RETURNING observation_id
)
INSERT INTO _m8_observation_map (tracker_id, observation_id) SELECT 'M8B-O004', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Most animal models of contused, compressed or transected spinal cord injury (SCI) require a laminectomy to be performed. However, despite advantages and disadvantages associated with each of these models, the laminectomy itself is generally associated with significant problems including longer surgery and anaesthesia (related post-operative complications), neuropathic pain, spinal instabilities, deformities, lordosis, and biomechanical problems, etc. This',
    'qualitative',
    NULL,
    'Most animal models of contused, compressed or transected spinal cord injury (SCI) require a laminectomy to be performed. However, despite advantages and disadvantages associated with each of these models, the laminectomy itself is generally associated with significant problems including longer surgery and anaesthesia (related post-operative complications), neuropathic pain, spinal instabilities, deformities, lordosis, and biomechanical problems, etc. This',
    'transection/hemisection model',
    'PubMed/source metadata',
    'Abstract / PubMed',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M8A-P005-E001", "measurement_method_inference": null, "paper_tracker_id": "M8A-P005", "quantitative": "NO", "statistics_reported": "Source-page first pass; exact statistics not extracted", "topic_id": "M8B-T005", "tracker_id": "M8B-O005"}'
  FROM _m8_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M8A-P005::M8A-P005-E001'
    AND et.evidence_type_name = 'Model-system evidence'
    AND ot.outcome_type_name = 'transection/hemisection model'
  RETURNING observation_id
)
INSERT INTO _m8_observation_map (tracker_id, observation_id) SELECT 'M8B-O005', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'To acquire evidence-based knowledge in temporal and spatial patterns of microglia/macrophages changes to facilitate finding proper intervention time for functional restoration after traumatic spinal cord injury (TSCI). Sina Trauma and Surgery Research Center, Tehran University of Medical Sciences, Tehran, Iran. We searched PubMed and EMBASE via Ovid SP with no temporal and linguistic restrictions. Besides, hand-search was performed in the bibliographies',
    'qualitative',
    'spatial transcriptomics / spatial atlas',
    'To acquire evidence-based knowledge in temporal and spatial patterns of microglia/macrophages changes to facilitate finding proper intervention time for functional restoration after traumatic spinal cord injury (TSCI). Sina Trauma and Surgery Research Center, Tehran University of Medical Sciences, Tehran, Iran. We searched PubMed and EMBASE via Ovid SP with no temporal and linguistic restrictions. Besides, hand-search was performed in the bibliographies',
    'in vivo sci model taxonomy',
    'PubMed/source metadata',
    'Abstract / PubMed',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M8A-P006-E001", "measurement_method_inference": "spatial transcriptomics / spatial atlas", "paper_tracker_id": "M8A-P006", "quantitative": "NO", "statistics_reported": "Source-page first pass; exact statistics not extracted", "topic_id": "M8B-T006", "tracker_id": "M8B-O006"}'
  FROM _m8_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M8A-P006::M8A-P006-E001'
    AND et.evidence_type_name = 'Model-system evidence'
    AND ot.outcome_type_name = 'in vivo SCI model taxonomy'
  RETURNING observation_id
)
INSERT INTO _m8_observation_map (tracker_id, observation_id) SELECT 'M8B-O006', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Spinal cord injury (SCI) is one of the most devastating neurological disorders associated with severe locomotor disability and a high rate of morbidity. Over the last 20-30 years, animal SCI models have proven to be extremely useful in better understanding the underlying molecular mechanism(s) involved in human traumatic SCI and in assessing the efficacy of available therapeutic agents. Thus, the current review article aims to provide readers with an',
    'qualitative',
    'behavioral / functional recovery assay',
    'Spinal cord injury (SCI) is one of the most devastating neurological disorders associated with severe locomotor disability and a high rate of morbidity. Over the last 20-30 years, animal SCI models have proven to be extremely useful in better understanding the underlying molecular mechanism(s) involved in human traumatic SCI and in assessing the efficacy of available therapeutic agents. Thus, the current review article aims to provide readers with an',
    'compression/clip injury model',
    'PubMed/source metadata',
    'Abstract / PubMed',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M8A-P007-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M8A-P007", "quantitative": "NO", "statistics_reported": "Source-page first pass; exact statistics not extracted", "topic_id": "M8B-T007", "tracker_id": "M8B-O007"}'
  FROM _m8_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M8A-P007::M8A-P007-E001'
    AND et.evidence_type_name = 'Model-system evidence'
    AND ot.outcome_type_name = 'compression/clip injury model'
  RETURNING observation_id
)
INSERT INTO _m8_observation_map (tracker_id, observation_id) SELECT 'M8B-O007', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'A literature review was conducted. To review animal models and injury paradigms used in the neurobiologic study of spinal cord regeneration, and to assist the spinal clinician in interpreting the many encouraging reports of potential therapies emerging from basic science laboratories. An enormous amount of interest in spinal cord regeneration research has been generated within the past 20 years with the hope that experimental therapies will become',
    'qualitative',
    NULL,
    'A literature review was conducted. To review animal models and injury paradigms used in the neurobiologic study of spinal cord regeneration, and to assist the spinal clinician in interpreting the many encouraging reports of potential therapies emerging from basic science laboratories. An enormous amount of interest in spinal cord regeneration research has been generated within the past 20 years with the hope that experimental therapies will become',
    'in vivo sci model taxonomy',
    'PubMed/source metadata',
    'Abstract / PubMed',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M8A-P008-E001", "measurement_method_inference": null, "paper_tracker_id": "M8A-P008", "quantitative": "NO", "statistics_reported": "Source-page first pass; exact statistics not extracted", "topic_id": "M8B-T008", "tracker_id": "M8B-O008"}'
  FROM _m8_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M8A-P008::M8A-P008-E001'
    AND et.evidence_type_name = 'Model-system evidence'
    AND ot.outcome_type_name = 'in vivo SCI model taxonomy'
  RETURNING observation_id
)
INSERT INTO _m8_observation_map (tracker_id, observation_id) SELECT 'M8B-O008', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'In this review, we have documented some current research trends in rodent models of spinal cord injury. We have also catalogued the treatments used in studies published between October 2002 and November 2003, with special attention given to studies in which treatments were delayed for at least 4 days after injury. Most spinal cord injury studies are performed with one of three general injury models: transection, compression, or contusion. Although most',
    'qualitative',
    NULL,
    'In this review, we have documented some current research trends in rodent models of spinal cord injury. We have also catalogued the treatments used in studies published between October 2002 and November 2003, with special attention given to studies in which treatments were delayed for at least 4 days after injury. Most spinal cord injury studies are performed with one of three general injury models: transection, compression, or contusion. Although most',
    'compression/clip injury model',
    'PubMed/source metadata',
    'Abstract / PubMed',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M8A-P009-E001", "measurement_method_inference": null, "paper_tracker_id": "M8A-P009", "quantitative": "NO", "statistics_reported": "Source-page first pass; exact statistics not extracted", "topic_id": "M8B-T001", "tracker_id": "M8B-O009"}'
  FROM _m8_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M8A-P009::M8A-P009-E001'
    AND et.evidence_type_name = 'Model-system evidence'
    AND ot.outcome_type_name = 'compression/clip injury model'
  RETURNING observation_id
)
INSERT INTO _m8_observation_map (tracker_id, observation_id) SELECT 'M8B-O009', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Stem cell-based therapies offer promising treatment for spinal cord injury (SCI) by reducing inflammation, restoring plasticity, and supporting neuroprotection and nerve regeneration. Brain-derived neurotrophic factor (BDNF) is crucial in SCI pathophysiology. This study reviews the impact of stem cells on BDNF expression in preclinical SCI models. A thorough search was performed in PubMed, Scopus, and Web of Science until June 2023, identifying studies on',
    'qualitative',
    NULL,
    'Stem cell-based therapies offer promising treatment for spinal cord injury (SCI) by reducing inflammation, restoring plasticity, and supporting neuroprotection and nerve regeneration. Brain-derived neurotrophic factor (BDNF) is crucial in SCI pathophysiology. This study reviews the impact of stem cells on BDNF expression in preclinical SCI models. A thorough search was performed in PubMed, Scopus, and Web of Science until June 2023, identifying studies on',
    'compression/clip injury model',
    'PubMed/source metadata',
    'Abstract / PubMed',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M8A-P010-E001", "measurement_method_inference": null, "paper_tracker_id": "M8A-P010", "quantitative": "NO", "statistics_reported": "Source-page first pass; exact statistics not extracted", "topic_id": "M8B-T002", "tracker_id": "M8B-O010"}'
  FROM _m8_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M8A-P010::M8A-P010-E001'
    AND et.evidence_type_name = 'Model-system evidence'
    AND ot.outcome_type_name = 'compression/clip injury model'
  RETURNING observation_id
)
INSERT INTO _m8_observation_map (tracker_id, observation_id) SELECT 'M8B-O010', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Spinal cord contusion injury in rodents is widely used as a model for spinal cord trauma in humans. Several biomechanical variables can influence injury outcome. In this work, we have assessed the influence of impact force and displacement of the spinal cord at the time of contusion injury on the severity of locomotor deficits and histopathological changes. Our work indicates that there is a linear relationship between force and tissue displacement, and',
    'qualitative',
    'behavioral / functional recovery assay',
    'Spinal cord contusion injury in rodents is widely used as a model for spinal cord trauma in humans. Several biomechanical variables can influence injury outcome. In this work, we have assessed the influence of impact force and displacement of the spinal cord at the time of contusion injury on the severity of locomotor deficits and histopathological changes. Our work indicates that there is a linear relationship between force and tissue displacement, and',
    'contusion injury model',
    'PubMed/source metadata',
    'Abstract / PubMed',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M8A-P011-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M8A-P011", "quantitative": "NO", "statistics_reported": "Source-page first pass; exact statistics not extracted", "topic_id": "M8B-T003", "tracker_id": "M8B-O011"}'
  FROM _m8_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M8A-P011::M8A-P011-E001'
    AND et.evidence_type_name = 'Model-system evidence'
    AND ot.outcome_type_name = 'contusion injury model'
  RETURNING observation_id
)
INSERT INTO _m8_observation_map (tracker_id, observation_id) SELECT 'M8B-O011', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Over the past decade, our laboratory has attempted to create a simple, accurate device that could be used to produce reliable and quantifiable spinal cord injuries in the rodent. We report here on our latest of several modifications of a spinal cord impactor that has allowed us to meet these design criteria. The impactor uses the dynamic capacity of an electromagnetic driver (Ling shaker) and a unique pattern generator to briefly compress the dorsal',
    'qualitative',
    NULL,
    'Over the past decade, our laboratory has attempted to create a simple, accurate device that could be used to produce reliable and quantifiable spinal cord injuries in the rodent. We report here on our latest of several modifications of a spinal cord impactor that has allowed us to meet these design criteria. The impactor uses the dynamic capacity of an electromagnetic driver (Ling shaker) and a unique pattern generator to briefly compress the dorsal',
    'compression/clip injury model',
    'PubMed/source metadata',
    'Abstract / PubMed',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M8A-P012-E001", "measurement_method_inference": null, "paper_tracker_id": "M8A-P012", "quantitative": "NO", "statistics_reported": "Source-page first pass; exact statistics not extracted", "topic_id": "M8B-T004", "tracker_id": "M8B-O012"}'
  FROM _m8_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M8A-P012::M8A-P012-E001'
    AND et.evidence_type_name = 'Model-system evidence'
    AND ot.outcome_type_name = 'compression/clip injury model'
  RETURNING observation_id
)
INSERT INTO _m8_observation_map (tracker_id, observation_id) SELECT 'M8B-O012', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Zebrafish exhibit robust regeneration following spinal cord injury, promoted by macrophages that control post-injury inflammation. However, the mechanistic basis of how macrophages regulate regeneration is poorly understood. To address this gap in understanding, we conducted a rapid in vivo phenotypic screen for macrophage-related genes that promote regeneration after spinal injury. We used acute injection of synthetic RNA Oligo CRISPR guide RNAs',
    'qualitative',
    'genetic perturbation / knockdown assay',
    'Zebrafish exhibit robust regeneration following spinal cord injury, promoted by macrophages that control post-injury inflammation. However, the mechanistic basis of how macrophages regulate regeneration is poorly understood. To address this gap in understanding, we conducted a rapid in vivo phenotypic screen for macrophage-related genes that promote regeneration after spinal injury. We used acute injection of synthetic RNA Oligo CRISPR guide RNAs',
    'regenerative zebrafish sci model',
    'PubMed/source metadata',
    'Abstract / PubMed',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M8A-P013-E001", "measurement_method_inference": "genetic perturbation / knockdown assay", "paper_tracker_id": "M8A-P013", "quantitative": "NO", "statistics_reported": "Source-page first pass; exact statistics not extracted", "topic_id": "M8B-T005", "tracker_id": "M8B-O013"}'
  FROM _m8_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M8A-P013::M8A-P013-E001'
    AND et.evidence_type_name = 'Model-system evidence'
    AND ot.outcome_type_name = 'regenerative zebrafish SCI model'
  RETURNING observation_id
)
INSERT INTO _m8_observation_map (tracker_id, observation_id) SELECT 'M8B-O013', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'The models used to investigate the pathophysiological mechanisms of acute critical illness are not limited to mammalian species. The zebrafish (Danio rerio) is a popular model organism for studying diseases due to its transparency and rapid development. The genes and signaling pathways involved in acute critical illness appear highly conserved among zebrafish and humans. Forward genetics such as random mutagenesis by a chemical mutagen or reverse genetics',
    'qualitative',
    NULL,
    'The models used to investigate the pathophysiological mechanisms of acute critical illness are not limited to mammalian species. The zebrafish (Danio rerio) is a popular model organism for studying diseases due to its transparency and rapid development. The genes and signaling pathways involved in acute critical illness appear highly conserved among zebrafish and humans. Forward genetics such as random mutagenesis by a chemical mutagen or reverse genetics',
    'regenerative zebrafish sci model',
    'PubMed/source metadata',
    'Abstract / PubMed',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M8A-P014-E001", "measurement_method_inference": null, "paper_tracker_id": "M8A-P014", "quantitative": "NO", "statistics_reported": "Source-page first pass; exact statistics not extracted", "topic_id": "M8B-T006", "tracker_id": "M8B-O014"}'
  FROM _m8_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M8A-P014::M8A-P014-E001'
    AND et.evidence_type_name = 'Model-system evidence'
    AND ot.outcome_type_name = 'regenerative zebrafish SCI model'
  RETURNING observation_id
)
INSERT INTO _m8_observation_map (tracker_id, observation_id) SELECT 'M8B-O014', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'ODC-SCI graded T8 contusion dataset links severity variables to locomotor, sensorimotor, pain, and histologic endpoints.',
    'qualitative/dataset',
    'immunostaining / histology / pathology; behavioral / functional recovery assay',
    'ODC-SCI graded T8 contusion dataset links severity variables to locomotor, sensorimotor, pain, and histologic endpoints.',
    'severity-calibrated thoracic contusion model',
    'ODC-SCI dataset metadata',
    'ODC-SCI dataset page',
    'medium',
    '{"curator_notes": "Promoted ODC-SCI candidate; dataset-page confidence retained.", "experiment_tracker_id": "M8A-P015-E001", "measurement_method_inference": "immunostaining / histology / pathology; behavioral / functional recovery assay", "paper_tracker_id": "M8A-P015", "quantitative": "NO", "statistics_reported": "Dataset-page first pass; raw data not reanalyzed", "topic_id": "M8B-T004", "tracker_id": "M8B-O015"}'
  FROM _m8_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M8A-P015::M8A-P015-E001'
    AND et.evidence_type_name = 'Dataset/model calibration evidence'
    AND ot.outcome_type_name = 'graded thoracic contusion calibration dataset'
  RETURNING observation_id
)
INSERT INTO _m8_observation_map (tracker_id, observation_id) SELECT 'M8B-O015', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Large MASCIS dataset records physiologic covariates and overground locomotion across thoracic contusion severities in 1125 rats.',
    'qualitative/dataset',
    'behavioral / functional recovery assay',
    'Large MASCIS dataset records physiologic covariates and overground locomotion across thoracic contusion severities in 1125 rats.',
    'large-scale contusion severity standardization',
    'ODC-SCI dataset metadata',
    'ODC-SCI dataset page',
    'medium',
    '{"curator_notes": "Promoted ODC-SCI candidate; dataset-page confidence retained.", "experiment_tracker_id": "M8A-P016-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M8A-P016", "quantitative": "YES", "statistics_reported": "Dataset size reported in source title/metadata", "topic_id": "M8B-T004", "tracker_id": "M8B-O016"}'
  FROM _m8_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M8A-P016::M8A-P016-E001'
    AND et.evidence_type_name = 'Dataset/model calibration evidence'
    AND ot.outcome_type_name = 'large-scale MASCIS contusion severity dataset'
  RETURNING observation_id
)
INSERT INTO _m8_observation_map (tracker_id, observation_id) SELECT 'M8B-O016', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'CLIMBER individual-animal data support cross-study harmonization of species, injury level, severity, and outcome scales for contusive SCI.',
    'qualitative/dataset',
    NULL,
    'CLIMBER individual-animal data support cross-study harmonization of species, injury level, severity, and outcome scales for contusive SCI.',
    'individual-animal model harmonization',
    'ODC-SCI dataset metadata',
    'ODC-SCI dataset page',
    'medium',
    '{"curator_notes": "Promoted ODC-SCI candidate; dataset-page confidence retained.", "experiment_tracker_id": "M8A-P017-E001", "measurement_method_inference": null, "paper_tracker_id": "M8A-P017", "quantitative": "NO", "statistics_reported": "Dataset-page first pass; meta-analysis estimates not re-extracted", "topic_id": "M8B-T008", "tracker_id": "M8B-O017"}'
  FROM _m8_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M8A-P017::M8A-P017-E001'
    AND et.evidence_type_name = 'Dataset/harmonization evidence'
    AND ot.outcome_type_name = 'individual-animal contusion harmonization dataset'
  RETURNING observation_id
)
INSERT INTO _m8_observation_map (tracker_id, observation_id) SELECT 'M8B-O017', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'CLIMBER group-level literature-extracted data provide complementary model-reporting and endpoint-comparability structure for contusive SCI.',
    'qualitative/dataset',
    NULL,
    'CLIMBER group-level literature-extracted data provide complementary model-reporting and endpoint-comparability structure for contusive SCI.',
    'group-level model harmonization',
    'ODC-SCI dataset metadata',
    'ODC-SCI dataset page',
    'medium',
    '{"curator_notes": "Promoted ODC-SCI candidate; dataset-page confidence retained.", "experiment_tracker_id": "M8A-P018-E001", "measurement_method_inference": null, "paper_tracker_id": "M8A-P018", "quantitative": "NO", "statistics_reported": "Dataset-page first pass; meta-analysis estimates not re-extracted", "topic_id": "M8B-T008", "tracker_id": "M8B-O018"}'
  FROM _m8_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M8A-P018::M8A-P018-E001'
    AND et.evidence_type_name = 'Dataset/harmonization evidence'
    AND ot.outcome_type_name = 'literature-extracted contusion harmonization dataset'
  RETURNING observation_id
)
INSERT INTO _m8_observation_map (tracker_id, observation_id) SELECT 'M8B-O018', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Cervical C5 unilateral SCI dataset adds level, laterality, modality, forelimb/sensorimotor, and histopathologic boundaries absent from thoracic-only models.',
    'qualitative/dataset',
    NULL,
    'Cervical C5 unilateral SCI dataset adds level, laterality, modality, forelimb/sensorimotor, and histopathologic boundaries absent from thoracic-only models.',
    'cervical-level multimodal model boundary',
    'ODC-SCI dataset metadata',
    'ODC-SCI dataset page',
    'medium',
    '{"curator_notes": "Promoted ODC-SCI candidate; dataset-page confidence retained.", "experiment_tracker_id": "M8A-P019-E001", "measurement_method_inference": null, "paper_tracker_id": "M8A-P019", "quantitative": "NO", "statistics_reported": "Dataset-page first pass; raw data not reanalyzed", "topic_id": "M8B-T003", "tracker_id": "M8B-O019"}'
  FROM _m8_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M8A-P019::M8A-P019-E001'
    AND et.evidence_type_name = 'Dataset/model boundary evidence'
    AND ot.outcome_type_name = 'cervical unilateral multimodal injury dataset'
  RETURNING observation_id
)
INSERT INTO _m8_observation_map (tracker_id, observation_id) SELECT 'M8B-O019', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Species/strain model boundaries requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 8A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M8A-P001", "topic_id": "M8B-T001", "tracker_id": "M8B-C001"}'
  FROM _m8_paper_map p
  WHERE p.tracker_id = 'M8A-P001'
  RETURNING claim_id
)
INSERT INTO _m8_claim_map (tracker_id, claim_id) SELECT 'M8B-C001', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Injury mechanism boundaries requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 8A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M8A-P002", "topic_id": "M8B-T002", "tracker_id": "M8B-C002"}'
  FROM _m8_paper_map p
  WHERE p.tracker_id = 'M8A-P002'
  RETURNING claim_id
)
INSERT INTO _m8_claim_map (tracker_id, claim_id) SELECT 'M8B-C002', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Spinal level and tract boundaries requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 8A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M8A-P003", "topic_id": "M8B-T003", "tracker_id": "M8B-C003"}'
  FROM _m8_paper_map p
  WHERE p.tracker_id = 'M8A-P003'
  RETURNING claim_id
)
INSERT INTO _m8_claim_map (tracker_id, claim_id) SELECT 'M8B-C003', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Severity/chronicity boundaries requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 8A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M8A-P004", "topic_id": "M8B-T004", "tracker_id": "M8B-C004"}'
  FROM _m8_paper_map p
  WHERE p.tracker_id = 'M8A-P004'
  RETURNING claim_id
)
INSERT INTO _m8_claim_map (tracker_id, claim_id) SELECT 'M8B-C004', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Lesion architecture boundaries requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 8A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M8A-P005", "topic_id": "M8B-T005", "tracker_id": "M8B-C005"}'
  FROM _m8_paper_map p
  WHERE p.tracker_id = 'M8A-P005'
  RETURNING claim_id
)
INSERT INTO _m8_claim_map (tracker_id, claim_id) SELECT 'M8B-C005', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Behavioral endpoint boundaries requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 8A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M8A-P006", "topic_id": "M8B-T006", "tracker_id": "M8B-C006"}'
  FROM _m8_paper_map p
  WHERE p.tracker_id = 'M8A-P006'
  RETURNING claim_id
)
INSERT INTO _m8_claim_map (tracker_id, claim_id) SELECT 'M8B-C006', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Large-animal/translational boundaries requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 8A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M8A-P007", "topic_id": "M8B-T007", "tracker_id": "M8B-C007"}'
  FROM _m8_paper_map p
  WHERE p.tracker_id = 'M8A-P007'
  RETURNING claim_id
)
INSERT INTO _m8_claim_map (tracker_id, claim_id) SELECT 'M8B-C007', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Model ontology confidence boundaries requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 8A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M8A-P008", "topic_id": "M8B-T008", "tracker_id": "M8B-C008"}'
  FROM _m8_paper_map p
  WHERE p.tracker_id = 'M8A-P008'
  RETURNING claim_id
)
INSERT INTO _m8_claim_map (tracker_id, claim_id) SELECT 'M8B-C008', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Species/strain model boundaries requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 8A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M8A-P009", "topic_id": "M8B-T001", "tracker_id": "M8B-C009"}'
  FROM _m8_paper_map p
  WHERE p.tracker_id = 'M8A-P009'
  RETURNING claim_id
)
INSERT INTO _m8_claim_map (tracker_id, claim_id) SELECT 'M8B-C009', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Injury mechanism boundaries requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 8A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M8A-P010", "topic_id": "M8B-T002", "tracker_id": "M8B-C010"}'
  FROM _m8_paper_map p
  WHERE p.tracker_id = 'M8A-P010'
  RETURNING claim_id
)
INSERT INTO _m8_claim_map (tracker_id, claim_id) SELECT 'M8B-C010', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Spinal level and tract boundaries requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 8A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M8A-P011", "topic_id": "M8B-T003", "tracker_id": "M8B-C011"}'
  FROM _m8_paper_map p
  WHERE p.tracker_id = 'M8A-P011'
  RETURNING claim_id
)
INSERT INTO _m8_claim_map (tracker_id, claim_id) SELECT 'M8B-C011', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Severity/chronicity boundaries requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 8A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M8A-P012", "topic_id": "M8B-T004", "tracker_id": "M8B-C012"}'
  FROM _m8_paper_map p
  WHERE p.tracker_id = 'M8A-P012'
  RETURNING claim_id
)
INSERT INTO _m8_claim_map (tracker_id, claim_id) SELECT 'M8B-C012', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Lesion architecture boundaries requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 8A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M8A-P013", "topic_id": "M8B-T005", "tracker_id": "M8B-C013"}'
  FROM _m8_paper_map p
  WHERE p.tracker_id = 'M8A-P013'
  RETURNING claim_id
)
INSERT INTO _m8_claim_map (tracker_id, claim_id) SELECT 'M8B-C013', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Behavioral endpoint boundaries requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 8A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M8A-P014", "topic_id": "M8B-T006", "tracker_id": "M8B-C014"}'
  FROM _m8_paper_map p
  WHERE p.tracker_id = 'M8A-P014'
  RETURNING claim_id
)
INSERT INTO _m8_claim_map (tracker_id, claim_id) SELECT 'M8B-C014', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Large-animal/translational boundaries requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 8A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M8A-P001", "topic_id": "M8B-T007", "tracker_id": "M8B-C015"}'
  FROM _m8_paper_map p
  WHERE p.tracker_id = 'M8A-P001'
  RETURNING claim_id
)
INSERT INTO _m8_claim_map (tracker_id, claim_id) SELECT 'M8B-C015', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Model ontology confidence boundaries requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 8A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M8A-P002", "topic_id": "M8B-T008", "tracker_id": "M8B-C016"}'
  FROM _m8_paper_map p
  WHERE p.tracker_id = 'M8A-P002'
  RETURNING claim_id
)
INSERT INTO _m8_claim_map (tracker_id, claim_id) SELECT 'M8B-C016', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Graded contusion datasets should be used to calibrate severity and endpoint selection rather than treated as interchangeable therapy evidence.',
    'boundary condition',
    'medium',
    'Module 8A tracker / ODC-SCI metadata',
    'medium',
    '{"curator_notes": "Dataset-page first pass; raw data reanalysis queued.", "source_paper_tracker_id": "M8A-P015", "topic_id": "M8B-T004", "tracker_id": "M8B-C017"}'
  FROM _m8_paper_map p
  WHERE p.tracker_id = 'M8A-P015'
  RETURNING claim_id
)
INSERT INTO _m8_claim_map (tracker_id, claim_id) SELECT 'M8B-C017', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Large-scale contusion datasets can strengthen model standardization by linking injury severity, physiologic covariates, and locomotor outcomes.',
    'synthesis',
    'medium',
    'Module 8A tracker / ODC-SCI metadata',
    'medium',
    '{"curator_notes": "Dataset-page first pass; raw data reanalysis queued.", "source_paper_tracker_id": "M8A-P016", "topic_id": "M8B-T004", "tracker_id": "M8B-C018"}'
  FROM _m8_paper_map p
  WHERE p.tracker_id = 'M8A-P016'
  RETURNING claim_id
)
INSERT INTO _m8_claim_map (tracker_id, claim_id) SELECT 'M8B-C018', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Individual-animal-data harmonization should be preserved as ontology evidence for species, level, severity, and outcome comparability.',
    'synthesis',
    'medium',
    'Module 8A tracker / ODC-SCI metadata',
    'medium',
    '{"curator_notes": "Dataset-page first pass; raw data reanalysis queued.", "source_paper_tracker_id": "M8A-P017", "topic_id": "M8B-T008", "tracker_id": "M8B-C019"}'
  FROM _m8_paper_map p
  WHERE p.tracker_id = 'M8A-P017'
  RETURNING claim_id
)
INSERT INTO _m8_claim_map (tracker_id, claim_id) SELECT 'M8B-C019', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Literature-extracted group-level harmonization is complementary to individual-animal data and should not be overread as experiment-level causal evidence.',
    'boundary condition',
    'medium',
    'Module 8A tracker / ODC-SCI metadata',
    'medium',
    '{"curator_notes": "Dataset-page first pass; raw data reanalysis queued.", "source_paper_tracker_id": "M8A-P018", "topic_id": "M8B-T008", "tracker_id": "M8B-C020"}'
  FROM _m8_paper_map p
  WHERE p.tracker_id = 'M8A-P018'
  RETURNING claim_id
)
INSERT INTO _m8_claim_map (tracker_id, claim_id) SELECT 'M8B-C020', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Cervical unilateral SCI datasets are necessary boundary anchors for forelimb, tract, laterality, and histopathology endpoints that thoracic models do not capture.',
    'synthesis',
    'medium',
    'Module 8A tracker / ODC-SCI metadata',
    'medium',
    '{"curator_notes": "Dataset-page first pass; raw data reanalysis queued.", "source_paper_tracker_id": "M8A-P019", "topic_id": "M8B-T003", "tracker_id": "M8B-C021"}'
  FROM _m8_paper_map p
  WHERE p.tracker_id = 'M8A-P019'
  RETURNING claim_id
)
INSERT INTO _m8_claim_map (tracker_id, claim_id) SELECT 'M8B-C021', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M8B-L001"}'
  FROM _m8_claim_map c
  JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O001'
  WHERE c.tracker_id = 'M8B-C001'
  RETURNING link_id
)
INSERT INTO _m8_link_map (tracker_id, link_id) SELECT 'M8B-L001', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M8B-L002"}'
  FROM _m8_claim_map c
  JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O002'
  WHERE c.tracker_id = 'M8B-C002'
  RETURNING link_id
)
INSERT INTO _m8_link_map (tracker_id, link_id) SELECT 'M8B-L002', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M8B-L003"}'
  FROM _m8_claim_map c
  JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O003'
  WHERE c.tracker_id = 'M8B-C003'
  RETURNING link_id
)
INSERT INTO _m8_link_map (tracker_id, link_id) SELECT 'M8B-L003', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M8B-L004"}'
  FROM _m8_claim_map c
  JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O004'
  WHERE c.tracker_id = 'M8B-C004'
  RETURNING link_id
)
INSERT INTO _m8_link_map (tracker_id, link_id) SELECT 'M8B-L004', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M8B-L005"}'
  FROM _m8_claim_map c
  JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O005'
  WHERE c.tracker_id = 'M8B-C005'
  RETURNING link_id
)
INSERT INTO _m8_link_map (tracker_id, link_id) SELECT 'M8B-L005', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M8B-L006"}'
  FROM _m8_claim_map c
  JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O006'
  WHERE c.tracker_id = 'M8B-C006'
  RETURNING link_id
)
INSERT INTO _m8_link_map (tracker_id, link_id) SELECT 'M8B-L006', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M8B-L007"}'
  FROM _m8_claim_map c
  JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O007'
  WHERE c.tracker_id = 'M8B-C007'
  RETURNING link_id
)
INSERT INTO _m8_link_map (tracker_id, link_id) SELECT 'M8B-L007', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M8B-L008"}'
  FROM _m8_claim_map c
  JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O008'
  WHERE c.tracker_id = 'M8B-C008'
  RETURNING link_id
)
INSERT INTO _m8_link_map (tracker_id, link_id) SELECT 'M8B-L008', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M8B-L009"}'
  FROM _m8_claim_map c
  JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O009'
  WHERE c.tracker_id = 'M8B-C009'
  RETURNING link_id
)
INSERT INTO _m8_link_map (tracker_id, link_id) SELECT 'M8B-L009', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M8B-L010"}'
  FROM _m8_claim_map c
  JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O010'
  WHERE c.tracker_id = 'M8B-C010'
  RETURNING link_id
)
INSERT INTO _m8_link_map (tracker_id, link_id) SELECT 'M8B-L010', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M8B-L011"}'
  FROM _m8_claim_map c
  JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O011'
  WHERE c.tracker_id = 'M8B-C011'
  RETURNING link_id
)
INSERT INTO _m8_link_map (tracker_id, link_id) SELECT 'M8B-L011', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M8B-L012"}'
  FROM _m8_claim_map c
  JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O012'
  WHERE c.tracker_id = 'M8B-C012'
  RETURNING link_id
)
INSERT INTO _m8_link_map (tracker_id, link_id) SELECT 'M8B-L012', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M8B-L013"}'
  FROM _m8_claim_map c
  JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O013'
  WHERE c.tracker_id = 'M8B-C013'
  RETURNING link_id
)
INSERT INTO _m8_link_map (tracker_id, link_id) SELECT 'M8B-L013', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M8B-L014"}'
  FROM _m8_claim_map c
  JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O014'
  WHERE c.tracker_id = 'M8B-C014'
  RETURNING link_id
)
INSERT INTO _m8_link_map (tracker_id, link_id) SELECT 'M8B-L014', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M8B-L015"}'
  FROM _m8_claim_map c
  JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O001'
  WHERE c.tracker_id = 'M8B-C015'
  RETURNING link_id
)
INSERT INTO _m8_link_map (tracker_id, link_id) SELECT 'M8B-L015', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M8B-L016"}'
  FROM _m8_claim_map c
  JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O002'
  WHERE c.tracker_id = 'M8B-C016'
  RETURNING link_id
)
INSERT INTO _m8_link_map (tracker_id, link_id) SELECT 'M8B-L016', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M8B-L017"}'
  FROM _m8_claim_map c
  JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O003'
  WHERE c.tracker_id = 'M8B-C001'
  RETURNING link_id
)
INSERT INTO _m8_link_map (tracker_id, link_id) SELECT 'M8B-L017', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M8B-L018"}'
  FROM _m8_claim_map c
  JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O004'
  WHERE c.tracker_id = 'M8B-C002'
  RETURNING link_id
)
INSERT INTO _m8_link_map (tracker_id, link_id) SELECT 'M8B-L018', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M8B-L019"}'
  FROM _m8_claim_map c
  JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O005'
  WHERE c.tracker_id = 'M8B-C003'
  RETURNING link_id
)
INSERT INTO _m8_link_map (tracker_id, link_id) SELECT 'M8B-L019', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M8B-L020"}'
  FROM _m8_claim_map c
  JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O006'
  WHERE c.tracker_id = 'M8B-C004'
  RETURNING link_id
)
INSERT INTO _m8_link_map (tracker_id, link_id) SELECT 'M8B-L020', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M8B-L021"}'
  FROM _m8_claim_map c
  JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O007'
  WHERE c.tracker_id = 'M8B-C005'
  RETURNING link_id
)
INSERT INTO _m8_link_map (tracker_id, link_id) SELECT 'M8B-L021', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M8B-L022"}'
  FROM _m8_claim_map c
  JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O008'
  WHERE c.tracker_id = 'M8B-C006'
  RETURNING link_id
)
INSERT INTO _m8_link_map (tracker_id, link_id) SELECT 'M8B-L022', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M8B-L023"}'
  FROM _m8_claim_map c
  JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O009'
  WHERE c.tracker_id = 'M8B-C007'
  RETURNING link_id
)
INSERT INTO _m8_link_map (tracker_id, link_id) SELECT 'M8B-L023', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M8B-L024"}'
  FROM _m8_claim_map c
  JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O010'
  WHERE c.tracker_id = 'M8B-C008'
  RETURNING link_id
)
INSERT INTO _m8_link_map (tracker_id, link_id) SELECT 'M8B-L024', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M8B-L025"}'
  FROM _m8_claim_map c
  JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O011'
  WHERE c.tracker_id = 'M8B-C009'
  RETURNING link_id
)
INSERT INTO _m8_link_map (tracker_id, link_id) SELECT 'M8B-L025', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M8B-L026"}'
  FROM _m8_claim_map c
  JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O012'
  WHERE c.tracker_id = 'M8B-C010'
  RETURNING link_id
)
INSERT INTO _m8_link_map (tracker_id, link_id) SELECT 'M8B-L026', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M8B-L027"}'
  FROM _m8_claim_map c
  JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O013'
  WHERE c.tracker_id = 'M8B-C011'
  RETURNING link_id
)
INSERT INTO _m8_link_map (tracker_id, link_id) SELECT 'M8B-L027', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M8B-L028"}'
  FROM _m8_claim_map c
  JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O014'
  WHERE c.tracker_id = 'M8B-C012'
  RETURNING link_id
)
INSERT INTO _m8_link_map (tracker_id, link_id) SELECT 'M8B-L028', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M8B-L029"}'
  FROM _m8_claim_map c
  JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O001'
  WHERE c.tracker_id = 'M8B-C013'
  RETURNING link_id
)
INSERT INTO _m8_link_map (tracker_id, link_id) SELECT 'M8B-L029', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M8B-L030"}'
  FROM _m8_claim_map c
  JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O002'
  WHERE c.tracker_id = 'M8B-C014'
  RETURNING link_id
)
INSERT INTO _m8_link_map (tracker_id, link_id) SELECT 'M8B-L030', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M8B-L031"}'
  FROM _m8_claim_map c
  JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O003'
  WHERE c.tracker_id = 'M8B-C015'
  RETURNING link_id
)
INSERT INTO _m8_link_map (tracker_id, link_id) SELECT 'M8B-L031', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M8B-L032"}'
  FROM _m8_claim_map c
  JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O004'
  WHERE c.tracker_id = 'M8B-C016'
  RETURNING link_id
)
INSERT INTO _m8_link_map (tracker_id, link_id) SELECT 'M8B-L032', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M8B-L033"}'
  FROM _m8_claim_map c
  JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O005'
  WHERE c.tracker_id = 'M8B-C001'
  RETURNING link_id
)
INSERT INTO _m8_link_map (tracker_id, link_id) SELECT 'M8B-L033', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M8B-L034"}'
  FROM _m8_claim_map c
  JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O006'
  WHERE c.tracker_id = 'M8B-C002'
  RETURNING link_id
)
INSERT INTO _m8_link_map (tracker_id, link_id) SELECT 'M8B-L034', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M8B-L035"}'
  FROM _m8_claim_map c
  JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O007'
  WHERE c.tracker_id = 'M8B-C003'
  RETURNING link_id
)
INSERT INTO _m8_link_map (tracker_id, link_id) SELECT 'M8B-L035', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M8B-L036"}'
  FROM _m8_claim_map c
  JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O008'
  WHERE c.tracker_id = 'M8B-C004'
  RETURNING link_id
)
INSERT INTO _m8_link_map (tracker_id, link_id) SELECT 'M8B-L036', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M8B-L037"}'
  FROM _m8_claim_map c
  JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O009'
  WHERE c.tracker_id = 'M8B-C005'
  RETURNING link_id
)
INSERT INTO _m8_link_map (tracker_id, link_id) SELECT 'M8B-L037', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M8B-L038"}'
  FROM _m8_claim_map c
  JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O010'
  WHERE c.tracker_id = 'M8B-C006'
  RETURNING link_id
)
INSERT INTO _m8_link_map (tracker_id, link_id) SELECT 'M8B-L038', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M8B-L039"}'
  FROM _m8_claim_map c
  JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O011'
  WHERE c.tracker_id = 'M8B-C007'
  RETURNING link_id
)
INSERT INTO _m8_link_map (tracker_id, link_id) SELECT 'M8B-L039', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M8B-L040"}'
  FROM _m8_claim_map c
  JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O012'
  WHERE c.tracker_id = 'M8B-C008'
  RETURNING link_id
)
INSERT INTO _m8_link_map (tracker_id, link_id) SELECT 'M8B-L040', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Dataset-page evidence supports graded severity calibration boundary.", "strength": "medium", "tracker_id": "M8B-L041"}'
  FROM _m8_claim_map c
  JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O015'
  WHERE c.tracker_id = 'M8B-C017'
  RETURNING link_id
)
INSERT INTO _m8_link_map (tracker_id, link_id) SELECT 'M8B-L041', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Dataset-page evidence supports large-scale contusion standardization claim.", "strength": "medium", "tracker_id": "M8B-L042"}'
  FROM _m8_claim_map c
  JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O016'
  WHERE c.tracker_id = 'M8B-C018'
  RETURNING link_id
)
INSERT INTO _m8_link_map (tracker_id, link_id) SELECT 'M8B-L042', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Dataset-page evidence supports individual-animal harmonization claim.", "strength": "medium", "tracker_id": "M8B-L043"}'
  FROM _m8_claim_map c
  JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O017'
  WHERE c.tracker_id = 'M8B-C019'
  RETURNING link_id
)
INSERT INTO _m8_link_map (tracker_id, link_id) SELECT 'M8B-L043', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Dataset-page evidence supports group-level harmonization boundary.", "strength": "medium", "tracker_id": "M8B-L044"}'
  FROM _m8_claim_map c
  JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O018'
  WHERE c.tracker_id = 'M8B-C020'
  RETURNING link_id
)
INSERT INTO _m8_link_map (tracker_id, link_id) SELECT 'M8B-L044', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Dataset-page evidence supports cervical-level boundary claim.", "strength": "medium", "tracker_id": "M8B-L045"}'
  FROM _m8_claim_map c
  JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O019'
  WHERE c.tracker_id = 'M8B-C021'
  RETURNING link_id
)
INSERT INTO _m8_link_map (tracker_id, link_id) SELECT 'M8B-L045', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Graded contusion data strengthen severity/chronicity consensus.", "strength": "medium", "tracker_id": "M8B-L046"}'
  FROM _m8_claim_map c
  JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O015'
  WHERE c.tracker_id = 'M8B-C004'
  RETURNING link_id
)
INSERT INTO _m8_link_map (tracker_id, link_id) SELECT 'M8B-L046', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "MASCIS severity data strengthen severity/chronicity consensus.", "strength": "medium", "tracker_id": "M8B-L047"}'
  FROM _m8_claim_map c
  JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O016'
  WHERE c.tracker_id = 'M8B-C012'
  RETURNING link_id
)
INSERT INTO _m8_link_map (tracker_id, link_id) SELECT 'M8B-L047', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "CLIMBER individual-animal data strengthen ontology confidence consensus.", "strength": "medium", "tracker_id": "M8B-L048"}'
  FROM _m8_claim_map c
  JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O017'
  WHERE c.tracker_id = 'M8B-C016'
  RETURNING link_id
)
INSERT INTO _m8_link_map (tracker_id, link_id) SELECT 'M8B-L048', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "CLIMBER group-level data strengthen ontology confidence consensus.", "strength": "medium", "tracker_id": "M8B-L049"}'
  FROM _m8_claim_map c
  JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O018'
  WHERE c.tracker_id = 'M8B-C016'
  RETURNING link_id
)
INSERT INTO _m8_link_map (tracker_id, link_id) SELECT 'M8B-L049', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cervical dataset strengthens spinal-level and tract boundary consensus.", "strength": "medium", "tracker_id": "M8B-L050"}'
  FROM _m8_claim_map c
  JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O019'
  WHERE c.tracker_id = 'M8B-C007'
  RETURNING link_id
)
INSERT INTO _m8_link_map (tracker_id, link_id) SELECT 'M8B-L050', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Both ODC contusion datasets support severity standardization boundaries.", "strength": "low", "tracker_id": "M8B-L051"}'
  FROM _m8_claim_map c
  JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O016'
  WHERE c.tracker_id = 'M8B-C017'
  RETURNING link_id
)
INSERT INTO _m8_link_map (tracker_id, link_id) SELECT 'M8B-L051', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Both ODC contusion datasets support severity standardization boundaries.", "strength": "low", "tracker_id": "M8B-L052"}'
  FROM _m8_claim_map c
  JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O015'
  WHERE c.tracker_id = 'M8B-C018'
  RETURNING link_id
)
INSERT INTO _m8_link_map (tracker_id, link_id) SELECT 'M8B-L052', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "CLIMBER data types are complementary harmonization anchors.", "strength": "low", "tracker_id": "M8B-L053"}'
  FROM _m8_claim_map c
  JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O018'
  WHERE c.tracker_id = 'M8B-C019'
  RETURNING link_id
)
INSERT INTO _m8_link_map (tracker_id, link_id) SELECT 'M8B-L053', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "CLIMBER data types are complementary harmonization anchors.", "strength": "low", "tracker_id": "M8B-L054"}'
  FROM _m8_claim_map c
  JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O017'
  WHERE c.tracker_id = 'M8B-C020'
  RETURNING link_id
)
INSERT INTO _m8_link_map (tracker_id, link_id) SELECT 'M8B-L054', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cervical and thoracic contusion rows define level-dependent boundaries.", "strength": "low", "tracker_id": "M8B-L055"}'
  FROM _m8_claim_map c
  JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O011'
  WHERE c.tracker_id = 'M8B-C021'
  RETURNING link_id
)
INSERT INTO _m8_link_map (tracker_id, link_id) SELECT 'M8B-L055', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'In vivo SCI evidence must retain species, strain, age, sex, and genetic background because model choice changes lesion biology, immune response, spontaneous recovery, surgical feasibility, and translatability.',
    'M8B-T001',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M8B-B001", "M8B-B002", "M8B-B003", "M8B-B004", "M8B-B005", "M8B-B006", "M8B-B007", "M8B-B008"], "claim_tracker_ids": ["M8B-C001", "M8B-C002", "M8B-C003"], "consensus_draft_id": "M8B-S001", "observation_tracker_ids": ["M8B-O001", "M8B-O002"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 8 first-pass curation freeze; ODC-SCI saturation update incorporated.", "topic_id": "M8B-T001"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m8_consensus_map (tracker_id, consensus_id) SELECT 'M8B-S001', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m8_consensus_map c
JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O001'
WHERE c.tracker_id = 'M8B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m8_consensus_map c
JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O002'
WHERE c.tracker_id = 'M8B-S001';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Injury mechanism is a primary evidence boundary: contusion, compression, transection, hemisection, crush, ischemia, and chemical or demyelinating models answer different questions and should not be pooled as interchangeable SCI models.',
    'M8B-T002',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M8B-B001", "M8B-B002", "M8B-B003", "M8B-B004", "M8B-B005", "M8B-B006", "M8B-B007", "M8B-B008"], "claim_tracker_ids": ["M8B-C004", "M8B-C005", "M8B-C006"], "consensus_draft_id": "M8B-S002", "observation_tracker_ids": ["M8B-O002", "M8B-O003", "M8B-O004"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 8 first-pass curation freeze; ODC-SCI saturation update incorporated.", "topic_id": "M8B-T002"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m8_consensus_map (tracker_id, consensus_id) SELECT 'M8B-S002', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m8_consensus_map c
JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O002'
WHERE c.tracker_id = 'M8B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m8_consensus_map c
JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O003'
WHERE c.tracker_id = 'M8B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m8_consensus_map c
JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O004'
WHERE c.tracker_id = 'M8B-S002';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Spinal level and tract involvement define what a model can test; cervical, thoracic, lumbar, dorsal-column, lateral-column, complete, and incomplete injuries should be mapped to the relevant motor, sensory, autonomic, and respiratory endpoints.',
    'M8B-T003',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M8B-B001", "M8B-B002", "M8B-B003", "M8B-B004", "M8B-B005", "M8B-B006", "M8B-B007", "M8B-B008"], "claim_tracker_ids": ["M8B-C007", "M8B-C008", "M8B-C009", "M8B-C021"], "consensus_draft_id": "M8B-S003", "observation_tracker_ids": ["M8B-O003", "M8B-O019"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 8 first-pass curation freeze; ODC-SCI saturation update incorporated.", "topic_id": "M8B-T003"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m8_consensus_map (tracker_id, consensus_id) SELECT 'M8B-S003', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m8_consensus_map c
JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O003'
WHERE c.tracker_id = 'M8B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m8_consensus_map c
JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O019'
WHERE c.tracker_id = 'M8B-S003';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Severity and chronicity are not metadata: force, displacement, duration, lesion completeness, time post-injury, and spontaneous recovery determine whether a model is appropriate for acute neuroprotection, chronic reconstruction, biomaterial testing, or rehabilitation studies.',
    'M8B-T004',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M8B-B001", "M8B-B002", "M8B-B003", "M8B-B004", "M8B-B005", "M8B-B006", "M8B-B007", "M8B-B008"], "claim_tracker_ids": ["M8B-C010", "M8B-C011", "M8B-C012", "M8B-C017", "M8B-C018"], "consensus_draft_id": "M8B-S004", "observation_tracker_ids": ["M8B-O004", "M8B-O015", "M8B-O016"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 8 first-pass curation freeze; ODC-SCI saturation update incorporated.", "topic_id": "M8B-T004"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m8_consensus_map (tracker_id, consensus_id) SELECT 'M8B-S004', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m8_consensus_map c
JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O004'
WHERE c.tracker_id = 'M8B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m8_consensus_map c
JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O015'
WHERE c.tracker_id = 'M8B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m8_consensus_map c
JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O016'
WHERE c.tracker_id = 'M8B-S004';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'In vivo model selection should be tied to lesion architecture. Models that create cystic cavities, spared tissue bridges, fibrotic cores, astrocytic borders, demyelination, or transection gaps support different reconstruction and repair claims.',
    'M8B-T005',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M8B-B001", "M8B-B002", "M8B-B003", "M8B-B004", "M8B-B005", "M8B-B006", "M8B-B007", "M8B-B008"], "claim_tracker_ids": ["M8B-C013", "M8B-C014", "M8B-C015", "M8B-C021"], "consensus_draft_id": "M8B-S005", "observation_tracker_ids": ["M8B-O005", "M8B-O013", "M8B-O019"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 8 first-pass curation freeze; ODC-SCI saturation update incorporated.", "topic_id": "M8B-T005"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m8_consensus_map (tracker_id, consensus_id) SELECT 'M8B-S005', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m8_consensus_map c
JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O005'
WHERE c.tracker_id = 'M8B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m8_consensus_map c
JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O013'
WHERE c.tracker_id = 'M8B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m8_consensus_map c
JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O019'
WHERE c.tracker_id = 'M8B-S005';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Behavioral endpoints must be interpreted as model-specific functional readouts rather than generic recovery measures; locomotor, skilled forelimb, sensory, autonomic, respiratory, pain, and electrophysiologic assays require separate endpoint fields.',
    'M8B-T006',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M8B-B001", "M8B-B002", "M8B-B003", "M8B-B004", "M8B-B005", "M8B-B006", "M8B-B007", "M8B-B008"], "claim_tracker_ids": ["M8B-C014", "M8B-C016", "M8B-C017", "M8B-C018", "M8B-C021"], "consensus_draft_id": "M8B-S006", "observation_tracker_ids": ["M8B-O006", "M8B-O014", "M8B-O015", "M8B-O016", "M8B-O019"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 8 first-pass curation freeze; ODC-SCI saturation update incorporated.", "topic_id": "M8B-T006"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m8_consensus_map (tracker_id, consensus_id) SELECT 'M8B-S006', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m8_consensus_map c
JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O006'
WHERE c.tracker_id = 'M8B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m8_consensus_map c
JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O014'
WHERE c.tracker_id = 'M8B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m8_consensus_map c
JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O015'
WHERE c.tracker_id = 'M8B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m8_consensus_map c
JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O016'
WHERE c.tracker_id = 'M8B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m8_consensus_map c
JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O019'
WHERE c.tracker_id = 'M8B-S006';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Large-animal and translational in vivo models add value for scale, surgical handling, device placement, imaging, and safety, but they do not automatically validate efficacy unless matched endpoints and controls are present.',
    'M8B-T007',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M8B-B001", "M8B-B002", "M8B-B003", "M8B-B004", "M8B-B005", "M8B-B006", "M8B-B007", "M8B-B008"], "claim_tracker_ids": ["M8B-C015", "M8B-C016", "M8B-C019", "M8B-C020"], "consensus_draft_id": "M8B-S007", "observation_tracker_ids": ["M8B-O007", "M8B-O008", "M8B-O009", "M8B-O017", "M8B-O018"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 8 first-pass curation freeze; ODC-SCI saturation update incorporated.", "topic_id": "M8B-T007"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m8_consensus_map (tracker_id, consensus_id) SELECT 'M8B-S007', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m8_consensus_map c
JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O007'
WHERE c.tracker_id = 'M8B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m8_consensus_map c
JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O008'
WHERE c.tracker_id = 'M8B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m8_consensus_map c
JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O009'
WHERE c.tracker_id = 'M8B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m8_consensus_map c
JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O017'
WHERE c.tracker_id = 'M8B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m8_consensus_map c
JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O018'
WHERE c.tracker_id = 'M8B-S007';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Module 8 should function as the in vivo model ontology layer: every downstream consensus claim should preserve species, injury mechanism, level, severity, chronicity, lesion architecture, endpoint family, and extraction confidence.',
    'M8B-T008',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M8B-B001", "M8B-B002", "M8B-B003", "M8B-B004", "M8B-B005", "M8B-B006", "M8B-B007", "M8B-B008"], "claim_tracker_ids": ["M8B-C016", "M8B-C017", "M8B-C018", "M8B-C019", "M8B-C020", "M8B-C021"], "consensus_draft_id": "M8B-S008", "observation_tracker_ids": ["M8B-O008", "M8B-O015", "M8B-O016", "M8B-O017", "M8B-O018", "M8B-O019"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 8 first-pass curation freeze; ODC-SCI saturation update incorporated.", "topic_id": "M8B-T008"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m8_consensus_map (tracker_id, consensus_id) SELECT 'M8B-S008', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m8_consensus_map c
JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O008'
WHERE c.tracker_id = 'M8B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m8_consensus_map c
JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O015'
WHERE c.tracker_id = 'M8B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m8_consensus_map c
JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O016'
WHERE c.tracker_id = 'M8B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m8_consensus_map c
JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O017'
WHERE c.tracker_id = 'M8B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m8_consensus_map c
JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O018'
WHERE c.tracker_id = 'M8B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m8_consensus_map c
JOIN _m8_observation_map o ON o.tracker_id = 'M8B-O019'
WHERE c.tracker_id = 'M8B-S008';

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
  SELECT COUNT(*) INTO paper_count FROM _m8_paper_map;
  SELECT COUNT(*) INTO experiment_count FROM _m8_experiment_map;
  SELECT COUNT(*) INTO observation_count FROM _m8_observation_map;
  SELECT COUNT(*) INTO claim_count FROM _m8_claim_map;
  SELECT COUNT(*) INTO link_count FROM _m8_link_map;
  SELECT COUNT(*) INTO consensus_count FROM _m8_consensus_map;
  SELECT COUNT(*) INTO consensus_observation_count
  FROM Consensus_Observation co
  JOIN _m8_consensus_map cm ON cm.consensus_id = co.consensus_id;
  IF paper_count <> 19 THEN RAISE EXCEPTION 'Expected 19 papers, found %', paper_count; END IF;
  IF experiment_count <> 19 THEN RAISE EXCEPTION 'Unexpected experiment count %', experiment_count; END IF;
  IF observation_count <> 19 THEN RAISE EXCEPTION 'Expected 19 observations, found %', observation_count; END IF;
  IF claim_count <> 21 THEN RAISE EXCEPTION 'Expected 21 claims, found %', claim_count; END IF;
  IF link_count <> 55 THEN RAISE EXCEPTION 'Expected 55 evidence links, found %', link_count; END IF;
  IF consensus_count <> 8 THEN RAISE EXCEPTION 'Expected 8 consensus rows, found %', consensus_count; END IF;
  IF consensus_observation_count <> 29 THEN RAISE EXCEPTION 'Unexpected consensus-observation count %', consensus_observation_count; END IF;
END $$;

COMMIT;
