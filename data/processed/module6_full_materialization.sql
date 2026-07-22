-- Module 6B full first-pass materialization generated from tracker-derived JSON.
-- This script is intended for a fresh database loaded with schema/schema.sql and scripts/seed_controlled_vocab.sql.
BEGIN;

CREATE TEMP TABLE _m6_paper_map (tracker_id TEXT PRIMARY KEY, paper_id INTEGER NOT NULL);
CREATE TEMP TABLE _m6_paradigm_map (tracker_id TEXT PRIMARY KEY, paradigm_id INTEGER NOT NULL);
CREATE TEMP TABLE _m6_experiment_map (tracker_id TEXT PRIMARY KEY, experiment_id INTEGER NOT NULL);
CREATE TEMP TABLE _m6_observation_map (tracker_id TEXT PRIMARY KEY, observation_id INTEGER NOT NULL);
CREATE TEMP TABLE _m6_claim_map (tracker_id TEXT PRIMARY KEY, claim_id INTEGER NOT NULL);
CREATE TEMP TABLE _m6_link_map (tracker_id TEXT PRIMARY KEY, link_id INTEGER NOT NULL);
CREATE TEMP TABLE _m6_consensus_map (tracker_id TEXT PRIMARY KEY, consensus_id INTEGER NOT NULL);

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Human spinal cord retains substantial structural mass in chronic stages after injury', 'Tuszynski MH', 1999,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Chronic structural preservation and focal cystic atrophy anchor", "module": "Module 6B", "tracker_id": "M6A-P001"}'
  )
  RETURNING paper_id
)
INSERT INTO _m6_paper_map (tracker_id, paper_id) SELECT 'M6A-P001', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Motoneuron death after human spinal cord injury', 'Grumbles RM', 2017,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Motoneuron loss and thin-myelin/remyelination pathology", "module": "Module 6B", "tracker_id": "M6A-P002"}'
  )
  RETURNING paper_id
)
INSERT INTO _m6_paper_map (tracker_id, paper_id) SELECT 'M6A-P002', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'One-year clinical study of NeuroRegen scaffold implantation following scar resection in complete chronic spinal cord injury patients', 'Xiao Z', 2016,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Chronic scar-resection and scaffold implantation anatomy", "module": "Module 6B", "tracker_id": "M6A-P003"}'
  )
  RETURNING paper_id
)
INSERT INTO _m6_paper_map (tracker_id, paper_id) SELECT 'M6A-P003', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'DTI of chronic spinal cord injury in children without MRI abnormalities and with pathology on MRI and comparison to severity of motor impairment', 'Faro SH', 2022,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "MRI-normal appearing cord can have DTI abnormalities", "module": "Module 6B", "tracker_id": "M6A-P004"}'
  )
  RETURNING paper_id
)
INSERT INTO _m6_paper_map (tracker_id, paper_id) SELECT 'M6A-P004', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Longitudinal motor system changes from acute to chronic spinal cord injury', 'Emmenegger TM', 2024,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Five-year tissue bridge and remote motor-system degeneration anchor", "module": "Module 6B", "tracker_id": "M6A-P005"}'
  )
  RETURNING paper_id
)
INSERT INTO _m6_paper_map (tracker_id, paper_id) SELECT 'M6A-P005', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Diffusion Tensor MR Imaging in Chronic Spinal Cord Injury', 'Ellingson BM', 2008,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Entire neuraxis DTI changes after chronic SCI", "module": "Module 6B", "tracker_id": "M6A-P006"}'
  )
  RETURNING paper_id
)
INSERT INTO _m6_paper_map (tracker_id, paper_id) SELECT 'M6A-P006', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Subject-specific regional measures of water diffusion are associated with impairment in chronic spinal cord injury', 'Smith AC', 2017,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Injury-region-specific DTI metrics associated with ISNCSCI impairment", "module": "Module 6B", "tracker_id": "M6A-P007"}'
  )
  RETURNING paper_id
)
INSERT INTO _m6_paper_map (tracker_id, paper_id) SELECT 'M6A-P007', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Tissue bridges predict recovery after traumatic and ischemic thoracic spinal cord injury', 'Pfyffer D', 2019,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Thoracic traumatic/ischemic tissue bridges predict recovery", "module": "Module 6B", "tracker_id": "M6A-P008"}'
  )
  RETURNING paper_id
)
INSERT INTO _m6_paper_map (tracker_id, paper_id) SELECT 'M6A-P008', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Prognostic value of tissue bridges in cervical spinal cord injury: a longitudinal multicentre cohort study', 'Pfyffer D', 2024,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Tissue bridges as trial-stratification biomarker", "module": "Module 6B", "tracker_id": "M6A-P009"}'
  )
  RETURNING paper_id
)
INSERT INTO _m6_paper_map (tracker_id, paper_id) SELECT 'M6A-P009', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'MR Spectroscopy of the Cervical Spinal Cord in Chronic Spinal Cord Injury', 'Wyss PO', 2019,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Supralesional metabolic alterations linked to atrophy and impairment", "module": "Module 6B", "tracker_id": "M6A-P010"}'
  )
  RETURNING paper_id
)
INSERT INTO _m6_paper_map (tracker_id, paper_id) SELECT 'M6A-P010', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'MRI investigation of the sensorimotor cortex and the corticospinal tract after acute spinal cord injury: a prospective longitudinal study', 'Freund P', 2013,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Degeneration above lesion and clinical outcome linkage", "module": "Module 6B", "tracker_id": "M6A-P011"}'
  )
  RETURNING paper_id
)
INSERT INTO _m6_paper_map (tracker_id, paper_id) SELECT 'M6A-P011', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Quantitative MRI of rostral spinal cord and brain regions is predictive of functional recovery in acute spinal cord injury', 'Seif M', 2018,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Early qMRI volume/microstructure predicts functional recovery", "module": "Module 6B", "tracker_id": "M6A-P012"}'
  )
  RETURNING paper_id
)
INSERT INTO _m6_paper_map (tracker_id, paper_id) SELECT 'M6A-P012', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Axonal integrity predicts cortical reorganisation following cervical injury', 'Freund P', 2012,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "CST integrity linked to cortical reorganization", "module": "Module 6B", "tracker_id": "M6A-P013"}'
  )
  RETURNING paper_id
)
INSERT INTO _m6_paper_map (tracker_id, paper_id) SELECT 'M6A-P013', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Disability, atrophy and cortical reorganization following spinal cord injury', 'Wrigley PJ', 2009,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Cord/cortical atrophy and reorganization linked to disability", "module": "Module 6B", "tracker_id": "M6A-P014"}'
  )
  RETURNING paper_id
)
INSERT INTO _m6_paper_map (tracker_id, paper_id) SELECT 'M6A-P014', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Changes of non-affected upper limb cortical representation in paraplegic patients as assessed by fMRI', 'Curt A', 2002,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Non-affected upper-limb representation changes after SCI", "module": "Module 6B", "tracker_id": "M6A-P015"}'
  )
  RETURNING paper_id
)
INSERT INTO _m6_paper_map (tracker_id, paper_id) SELECT 'M6A-P015', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Dynamics of progressive degeneration of major spinal pathways following spinal cord injury: a longitudinal study', 'Freund/Seif group', 2023,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Cervical CST/dorsal column degeneration gradients over two years", "module": "Module 6B", "tracker_id": "M6A-P016"}'
  )
  RETURNING paper_id
)
INSERT INTO _m6_paper_map (tracker_id, paper_id) SELECT 'M6A-P016', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Vascular mechanisms in the pathophysiology of human spinal cord injury', 'Tator CH', 1997,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Acute-to-subacute vascular pathology up to 9 months", "module": "Module 6B", "tracker_id": "M6A-P017"}'
  )
  RETURNING paper_id
)
INSERT INTO _m6_paper_map (tracker_id, paper_id) SELECT 'M6A-P017', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'A case of post-traumatic syringomyelia: neuropathological findings after 1 year of cystic drainage', 'Foo D', 1989,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Syrinx drainage did not restore satisfactory function; autopsy mapped residual damage", "module": "Module 6B", "tracker_id": "M6A-P018"}'
  )
  RETURNING paper_id
)
INSERT INTO _m6_paper_map (tracker_id, paper_id) SELECT 'M6A-P018', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Progressive late post-traumatic syringomyelia', 'Rossier AB', 1981,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Late cyst/syrinx complication anchor", "module": "Module 6B", "tracker_id": "M6A-P019"}'
  )
  RETURNING paper_id
)
INSERT INTO _m6_paper_map (tracker_id, paper_id) SELECT 'M6A-P019', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Magnetic resonance imaging evaluation of spinal cord injury in clinical trials', 'Burns AS', 2012,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Trial screening and outcome-measure framing", "module": "Module 6B", "tracker_id": "M6A-P020"}'
  )
  RETURNING paper_id
)
INSERT INTO _m6_paper_map (tracker_id, paper_id) SELECT 'M6A-P020', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Independent spinal cord atrophy measures correlate to motor and sensory deficits in individuals with spinal cord injury', 'Lundell H', 2011,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Cord atrophy metric linked to motor/sensory deficits", "module": "Module 6B", "tracker_id": "M6A-P021"}'
  )
  RETURNING paper_id
)
INSERT INTO _m6_paper_map (tracker_id, paper_id) SELECT 'M6A-P021', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Lateral corticospinal tract damage correlates with motor output in incomplete spinal cord injury', 'Smith AC', 2018,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Lateral CST damage and motor output linkage; complements subject-specific DTI and tissue bridge papers", "module": "Module 6B", "tracker_id": "M6A-P022"}'
  )
  RETURNING paper_id
)
INSERT INTO _m6_paper_map (tracker_id, paper_id) SELECT 'M6A-P022', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Atrophy of specific brain regions in cervical spinal cord injury', 'Freund P', 2011,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Supraspinal atrophy context; keep secondary to spinal anatomy", "module": "Module 6B", "tracker_id": "M6A-P023"}'
  )
  RETURNING paper_id
)
INSERT INTO _m6_paper_map (tracker_id, paper_id) SELECT 'M6A-P023', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Sensorimotor cortical plasticity during recovery following spinal cord injury: a longitudinal fMRI study', 'Jurkiewicz MT', 2006,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Cortical plasticity during recovery", "module": "Module 6B", "tracker_id": "M6A-P024"}'
  )
  RETURNING paper_id
)
INSERT INTO _m6_paper_map (tracker_id, paper_id) SELECT 'M6A-P024', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Plasticity of the human motor cortex following cervical spinal cord injury', 'Mikulis DJ', 2002,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Tongue/motor cortex reorganization anchor", "module": "Module 6B", "tracker_id": "M6A-P025"}'
  )
  RETURNING paper_id
)
INSERT INTO _m6_paper_map (tracker_id, paper_id) SELECT 'M6A-P025', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Motor cortex activation is related to force of squeezing after spinal cord injury', 'Cramer SC', 2005,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Brain activation/function boundary", "module": "Module 6B", "tracker_id": "M6A-P026"}'
  )
  RETURNING paper_id
)
INSERT INTO _m6_paper_map (tracker_id, paper_id) SELECT 'M6A-P026', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Tracking sensory system atrophy and outcome prediction in spinal cord injury', 'Grabher P', 2015,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Sensory tract degeneration and clinical outcome", "module": "Module 6B", "tracker_id": "M6A-P027"}'
  )
  RETURNING paper_id
)
INSERT INTO _m6_paper_map (tracker_id, paper_id) SELECT 'M6A-P027', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Tracking trauma-induced neurodegeneration above the level of spinal cord injury', 'Huber E', 2017,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Supralesional spinal/brain degeneration trajectory", "module": "Module 6B", "tracker_id": "M6A-P028"}'
  )
  RETURNING paper_id
)
INSERT INTO _m6_paper_map (tracker_id, paper_id) SELECT 'M6A-P028', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Traumatic and nontraumatic spinal cord injury: pathological insights from neuroimaging', 'David G', 2019,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Supports traumatic/nontraumatic boundary", "module": "Module 6B", "tracker_id": "M6A-P029"}'
  )
  RETURNING paper_id
)
INSERT INTO _m6_paper_map (tracker_id, paper_id) SELECT 'M6A-P029', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Quantitative MRI and histology-informed markers of myelin, iron, and tissue microstructure', 'Weiskopf N', 2015,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "qMRI interpretation boundary", "module": "Module 6B", "tracker_id": "M6A-P030"}'
  )
  RETURNING paper_id
)
INSERT INTO _m6_paper_map (tracker_id, paper_id) SELECT 'M6A-P030', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'In chronic complete spinal cord injury supraspinal changes detected by quantitative MRI are confined to volume reduction in the caudal brainstem', 'Seif M', 2021,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Brainstem/dorsal column Wallerian degeneration boundary", "module": "Module 6B", "tracker_id": "M6A-P031"}'
  )
  RETURNING paper_id
)
INSERT INTO _m6_paper_map (tracker_id, paper_id) SELECT 'M6A-P031', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Metabolic profile of complete spinal cord injury in pons and cerebellum: a 3T 1H MRS study', 'Wyss PO', 2023,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Pons/cerebellum metabolic changes in complete SCI", "module": "Module 6B", "tracker_id": "M6A-P032"}'
  )
  RETURNING paper_id
)
INSERT INTO _m6_paper_map (tracker_id, paper_id) SELECT 'M6A-P032', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Improving diagnostic workup following traumatic spinal cord injury: advances in biomarkers', 'Hupp M', 2021,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Imaging and fluid biomarker map", "module": "Module 6B", "tracker_id": "M6A-P033"}'
  )
  RETURNING paper_id
)
INSERT INTO _m6_paper_map (tracker_id, paper_id) SELECT 'M6A-P033', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Tracking changes following spinal cord injury: insights from neuroimaging', 'Freund P', 2019,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Review-map for qMRI/fMRI/DTI categories", "module": "Module 6B", "tracker_id": "M6A-P034"}'
  )
  RETURNING paper_id
)
INSERT INTO _m6_paper_map (tracker_id, paper_id) SELECT 'M6A-P034', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Midsagittal tissue bridges are associated with walking ability in incomplete spinal cord injury: a magnetic resonance imaging case series', 'Pfyffer D', 2017,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Tissue bridge ratio associated with 6-minute walk distance", "module": "Module 6B", "tracker_id": "M6A-P035"}'
  )
  RETURNING paper_id
)
INSERT INTO _m6_paper_map (tracker_id, paper_id) SELECT 'M6A-P035', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Clinical trial readiness and imaging in spinal cord injury', 'Stucki G / EMSCI group', 2012,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Retained for screening anatomy context", "module": "Module 6B", "tracker_id": "M6A-P036"}'
  )
  RETURNING paper_id
)
INSERT INTO _m6_paper_map (tracker_id, paper_id) SELECT 'M6A-P036', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 6B curated evidence extraction',
    'First-pass Module 6B human chronic SCI pathology and translational imaging curation for M6A-P001',
    'Tracker-derived materialization from Module_6B_TRACKER.md'
  FROM _m6_paper_map WHERE tracker_id = 'M6A-P001'
  RETURNING paradigm_id
)
INSERT INTO _m6_paradigm_map (tracker_id, paradigm_id) SELECT 'M6A-P001', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 6B curated evidence extraction',
    'First-pass Module 6B human chronic SCI pathology and translational imaging curation for M6A-P002',
    'Tracker-derived materialization from Module_6B_TRACKER.md'
  FROM _m6_paper_map WHERE tracker_id = 'M6A-P002'
  RETURNING paradigm_id
)
INSERT INTO _m6_paradigm_map (tracker_id, paradigm_id) SELECT 'M6A-P002', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 6B curated evidence extraction',
    'First-pass Module 6B human chronic SCI pathology and translational imaging curation for M6A-P003',
    'Tracker-derived materialization from Module_6B_TRACKER.md'
  FROM _m6_paper_map WHERE tracker_id = 'M6A-P003'
  RETURNING paradigm_id
)
INSERT INTO _m6_paradigm_map (tracker_id, paradigm_id) SELECT 'M6A-P003', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 6B curated evidence extraction',
    'First-pass Module 6B human chronic SCI pathology and translational imaging curation for M6A-P004',
    'Tracker-derived materialization from Module_6B_TRACKER.md'
  FROM _m6_paper_map WHERE tracker_id = 'M6A-P004'
  RETURNING paradigm_id
)
INSERT INTO _m6_paradigm_map (tracker_id, paradigm_id) SELECT 'M6A-P004', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 6B curated evidence extraction',
    'First-pass Module 6B human chronic SCI pathology and translational imaging curation for M6A-P005',
    'Tracker-derived materialization from Module_6B_TRACKER.md'
  FROM _m6_paper_map WHERE tracker_id = 'M6A-P005'
  RETURNING paradigm_id
)
INSERT INTO _m6_paradigm_map (tracker_id, paradigm_id) SELECT 'M6A-P005', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 6B curated evidence extraction',
    'First-pass Module 6B human chronic SCI pathology and translational imaging curation for M6A-P006',
    'Tracker-derived materialization from Module_6B_TRACKER.md'
  FROM _m6_paper_map WHERE tracker_id = 'M6A-P006'
  RETURNING paradigm_id
)
INSERT INTO _m6_paradigm_map (tracker_id, paradigm_id) SELECT 'M6A-P006', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 6B curated evidence extraction',
    'First-pass Module 6B human chronic SCI pathology and translational imaging curation for M6A-P007',
    'Tracker-derived materialization from Module_6B_TRACKER.md'
  FROM _m6_paper_map WHERE tracker_id = 'M6A-P007'
  RETURNING paradigm_id
)
INSERT INTO _m6_paradigm_map (tracker_id, paradigm_id) SELECT 'M6A-P007', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 6B curated evidence extraction',
    'First-pass Module 6B human chronic SCI pathology and translational imaging curation for M6A-P008',
    'Tracker-derived materialization from Module_6B_TRACKER.md'
  FROM _m6_paper_map WHERE tracker_id = 'M6A-P008'
  RETURNING paradigm_id
)
INSERT INTO _m6_paradigm_map (tracker_id, paradigm_id) SELECT 'M6A-P008', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 6B curated evidence extraction',
    'First-pass Module 6B human chronic SCI pathology and translational imaging curation for M6A-P009',
    'Tracker-derived materialization from Module_6B_TRACKER.md'
  FROM _m6_paper_map WHERE tracker_id = 'M6A-P009'
  RETURNING paradigm_id
)
INSERT INTO _m6_paradigm_map (tracker_id, paradigm_id) SELECT 'M6A-P009', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 6B curated evidence extraction',
    'First-pass Module 6B human chronic SCI pathology and translational imaging curation for M6A-P010',
    'Tracker-derived materialization from Module_6B_TRACKER.md'
  FROM _m6_paper_map WHERE tracker_id = 'M6A-P010'
  RETURNING paradigm_id
)
INSERT INTO _m6_paradigm_map (tracker_id, paradigm_id) SELECT 'M6A-P010', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 6B curated evidence extraction',
    'First-pass Module 6B human chronic SCI pathology and translational imaging curation for M6A-P011',
    'Tracker-derived materialization from Module_6B_TRACKER.md'
  FROM _m6_paper_map WHERE tracker_id = 'M6A-P011'
  RETURNING paradigm_id
)
INSERT INTO _m6_paradigm_map (tracker_id, paradigm_id) SELECT 'M6A-P011', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 6B curated evidence extraction',
    'First-pass Module 6B human chronic SCI pathology and translational imaging curation for M6A-P012',
    'Tracker-derived materialization from Module_6B_TRACKER.md'
  FROM _m6_paper_map WHERE tracker_id = 'M6A-P012'
  RETURNING paradigm_id
)
INSERT INTO _m6_paradigm_map (tracker_id, paradigm_id) SELECT 'M6A-P012', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 6B curated evidence extraction',
    'First-pass Module 6B human chronic SCI pathology and translational imaging curation for M6A-P013',
    'Tracker-derived materialization from Module_6B_TRACKER.md'
  FROM _m6_paper_map WHERE tracker_id = 'M6A-P013'
  RETURNING paradigm_id
)
INSERT INTO _m6_paradigm_map (tracker_id, paradigm_id) SELECT 'M6A-P013', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 6B curated evidence extraction',
    'First-pass Module 6B human chronic SCI pathology and translational imaging curation for M6A-P014',
    'Tracker-derived materialization from Module_6B_TRACKER.md'
  FROM _m6_paper_map WHERE tracker_id = 'M6A-P014'
  RETURNING paradigm_id
)
INSERT INTO _m6_paradigm_map (tracker_id, paradigm_id) SELECT 'M6A-P014', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 6B curated evidence extraction',
    'First-pass Module 6B human chronic SCI pathology and translational imaging curation for M6A-P015',
    'Tracker-derived materialization from Module_6B_TRACKER.md'
  FROM _m6_paper_map WHERE tracker_id = 'M6A-P015'
  RETURNING paradigm_id
)
INSERT INTO _m6_paradigm_map (tracker_id, paradigm_id) SELECT 'M6A-P015', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 6B curated evidence extraction',
    'First-pass Module 6B human chronic SCI pathology and translational imaging curation for M6A-P016',
    'Tracker-derived materialization from Module_6B_TRACKER.md'
  FROM _m6_paper_map WHERE tracker_id = 'M6A-P016'
  RETURNING paradigm_id
)
INSERT INTO _m6_paradigm_map (tracker_id, paradigm_id) SELECT 'M6A-P016', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 6B curated evidence extraction',
    'First-pass Module 6B human chronic SCI pathology and translational imaging curation for M6A-P017',
    'Tracker-derived materialization from Module_6B_TRACKER.md'
  FROM _m6_paper_map WHERE tracker_id = 'M6A-P017'
  RETURNING paradigm_id
)
INSERT INTO _m6_paradigm_map (tracker_id, paradigm_id) SELECT 'M6A-P017', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 6B curated evidence extraction',
    'First-pass Module 6B human chronic SCI pathology and translational imaging curation for M6A-P018',
    'Tracker-derived materialization from Module_6B_TRACKER.md'
  FROM _m6_paper_map WHERE tracker_id = 'M6A-P018'
  RETURNING paradigm_id
)
INSERT INTO _m6_paradigm_map (tracker_id, paradigm_id) SELECT 'M6A-P018', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 6B curated evidence extraction',
    'First-pass Module 6B human chronic SCI pathology and translational imaging curation for M6A-P019',
    'Tracker-derived materialization from Module_6B_TRACKER.md'
  FROM _m6_paper_map WHERE tracker_id = 'M6A-P019'
  RETURNING paradigm_id
)
INSERT INTO _m6_paradigm_map (tracker_id, paradigm_id) SELECT 'M6A-P019', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 6B curated evidence extraction',
    'First-pass Module 6B human chronic SCI pathology and translational imaging curation for M6A-P020',
    'Tracker-derived materialization from Module_6B_TRACKER.md'
  FROM _m6_paper_map WHERE tracker_id = 'M6A-P020'
  RETURNING paradigm_id
)
INSERT INTO _m6_paradigm_map (tracker_id, paradigm_id) SELECT 'M6A-P020', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 6B curated evidence extraction',
    'First-pass Module 6B human chronic SCI pathology and translational imaging curation for M6A-P021',
    'Tracker-derived materialization from Module_6B_TRACKER.md'
  FROM _m6_paper_map WHERE tracker_id = 'M6A-P021'
  RETURNING paradigm_id
)
INSERT INTO _m6_paradigm_map (tracker_id, paradigm_id) SELECT 'M6A-P021', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 6B curated evidence extraction',
    'First-pass Module 6B human chronic SCI pathology and translational imaging curation for M6A-P022',
    'Tracker-derived materialization from Module_6B_TRACKER.md'
  FROM _m6_paper_map WHERE tracker_id = 'M6A-P022'
  RETURNING paradigm_id
)
INSERT INTO _m6_paradigm_map (tracker_id, paradigm_id) SELECT 'M6A-P022', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 6B curated evidence extraction',
    'First-pass Module 6B human chronic SCI pathology and translational imaging curation for M6A-P023',
    'Tracker-derived materialization from Module_6B_TRACKER.md'
  FROM _m6_paper_map WHERE tracker_id = 'M6A-P023'
  RETURNING paradigm_id
)
INSERT INTO _m6_paradigm_map (tracker_id, paradigm_id) SELECT 'M6A-P023', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 6B curated evidence extraction',
    'First-pass Module 6B human chronic SCI pathology and translational imaging curation for M6A-P024',
    'Tracker-derived materialization from Module_6B_TRACKER.md'
  FROM _m6_paper_map WHERE tracker_id = 'M6A-P024'
  RETURNING paradigm_id
)
INSERT INTO _m6_paradigm_map (tracker_id, paradigm_id) SELECT 'M6A-P024', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 6B curated evidence extraction',
    'First-pass Module 6B human chronic SCI pathology and translational imaging curation for M6A-P025',
    'Tracker-derived materialization from Module_6B_TRACKER.md'
  FROM _m6_paper_map WHERE tracker_id = 'M6A-P025'
  RETURNING paradigm_id
)
INSERT INTO _m6_paradigm_map (tracker_id, paradigm_id) SELECT 'M6A-P025', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 6B curated evidence extraction',
    'First-pass Module 6B human chronic SCI pathology and translational imaging curation for M6A-P026',
    'Tracker-derived materialization from Module_6B_TRACKER.md'
  FROM _m6_paper_map WHERE tracker_id = 'M6A-P026'
  RETURNING paradigm_id
)
INSERT INTO _m6_paradigm_map (tracker_id, paradigm_id) SELECT 'M6A-P026', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 6B curated evidence extraction',
    'First-pass Module 6B human chronic SCI pathology and translational imaging curation for M6A-P027',
    'Tracker-derived materialization from Module_6B_TRACKER.md'
  FROM _m6_paper_map WHERE tracker_id = 'M6A-P027'
  RETURNING paradigm_id
)
INSERT INTO _m6_paradigm_map (tracker_id, paradigm_id) SELECT 'M6A-P027', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 6B curated evidence extraction',
    'First-pass Module 6B human chronic SCI pathology and translational imaging curation for M6A-P028',
    'Tracker-derived materialization from Module_6B_TRACKER.md'
  FROM _m6_paper_map WHERE tracker_id = 'M6A-P028'
  RETURNING paradigm_id
)
INSERT INTO _m6_paradigm_map (tracker_id, paradigm_id) SELECT 'M6A-P028', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 6B curated evidence extraction',
    'First-pass Module 6B human chronic SCI pathology and translational imaging curation for M6A-P029',
    'Tracker-derived materialization from Module_6B_TRACKER.md'
  FROM _m6_paper_map WHERE tracker_id = 'M6A-P029'
  RETURNING paradigm_id
)
INSERT INTO _m6_paradigm_map (tracker_id, paradigm_id) SELECT 'M6A-P029', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 6B curated evidence extraction',
    'First-pass Module 6B human chronic SCI pathology and translational imaging curation for M6A-P030',
    'Tracker-derived materialization from Module_6B_TRACKER.md'
  FROM _m6_paper_map WHERE tracker_id = 'M6A-P030'
  RETURNING paradigm_id
)
INSERT INTO _m6_paradigm_map (tracker_id, paradigm_id) SELECT 'M6A-P030', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 6B curated evidence extraction',
    'First-pass Module 6B human chronic SCI pathology and translational imaging curation for M6A-P031',
    'Tracker-derived materialization from Module_6B_TRACKER.md'
  FROM _m6_paper_map WHERE tracker_id = 'M6A-P031'
  RETURNING paradigm_id
)
INSERT INTO _m6_paradigm_map (tracker_id, paradigm_id) SELECT 'M6A-P031', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 6B curated evidence extraction',
    'First-pass Module 6B human chronic SCI pathology and translational imaging curation for M6A-P032',
    'Tracker-derived materialization from Module_6B_TRACKER.md'
  FROM _m6_paper_map WHERE tracker_id = 'M6A-P032'
  RETURNING paradigm_id
)
INSERT INTO _m6_paradigm_map (tracker_id, paradigm_id) SELECT 'M6A-P032', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 6B curated evidence extraction',
    'First-pass Module 6B human chronic SCI pathology and translational imaging curation for M6A-P033',
    'Tracker-derived materialization from Module_6B_TRACKER.md'
  FROM _m6_paper_map WHERE tracker_id = 'M6A-P033'
  RETURNING paradigm_id
)
INSERT INTO _m6_paradigm_map (tracker_id, paradigm_id) SELECT 'M6A-P033', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 6B curated evidence extraction',
    'First-pass Module 6B human chronic SCI pathology and translational imaging curation for M6A-P034',
    'Tracker-derived materialization from Module_6B_TRACKER.md'
  FROM _m6_paper_map WHERE tracker_id = 'M6A-P034'
  RETURNING paradigm_id
)
INSERT INTO _m6_paradigm_map (tracker_id, paradigm_id) SELECT 'M6A-P034', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 6B curated evidence extraction',
    'First-pass Module 6B human chronic SCI pathology and translational imaging curation for M6A-P035',
    'Tracker-derived materialization from Module_6B_TRACKER.md'
  FROM _m6_paper_map WHERE tracker_id = 'M6A-P035'
  RETURNING paradigm_id
)
INSERT INTO _m6_paradigm_map (tracker_id, paradigm_id) SELECT 'M6A-P035', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 6B curated evidence extraction',
    'First-pass Module 6B human chronic SCI pathology and translational imaging curation for M6A-P036',
    'Tracker-derived materialization from Module_6B_TRACKER.md'
  FROM _m6_paper_map WHERE tracker_id = 'M6A-P036'
  RETURNING paradigm_id
)
INSERT INTO _m6_paradigm_map (tracker_id, paradigm_id) SELECT 'M6A-P036', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Fig 1; Table 1',
    'Tracker experiment M6A-P001-E001',
    'Module 6B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M6B-O001"], "source_experiment_tracker_id": "M6A-P001-E001", "source_paper_tracker_id": "M6A-P001", "tracker_key": "M6A-P001::M6A-P001-E001"}'
  FROM _m6_paper_map p
  JOIN _m6_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M6A-P001'
  RETURNING experiment_id
)
INSERT INTO _m6_experiment_map (tracker_id, experiment_id) SELECT 'M6A-P001::M6A-P001-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Fig 1-Fig 5',
    'Tracker experiment M6A-P002-E001',
    'Module 6B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M6B-O002"], "source_experiment_tracker_id": "M6A-P002-E001", "source_paper_tracker_id": "M6A-P002", "tracker_key": "M6A-P002::M6A-P002-E001"}'
  FROM _m6_paper_map p
  JOIN _m6_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M6A-P002'
  RETURNING experiment_id
)
INSERT INTO _m6_experiment_map (tracker_id, experiment_id) SELECT 'M6A-P002::M6A-P002-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Clinical source',
    'Tracker experiment M6A-P003-E001',
    'Module 6B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M6B-O003"], "source_experiment_tracker_id": "M6A-P003-E001", "source_paper_tracker_id": "M6A-P003", "tracker_key": "M6A-P003::M6A-P003-E001"}'
  FROM _m6_paper_map p
  JOIN _m6_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M6A-P003'
  RETURNING experiment_id
)
INSERT INTO _m6_experiment_map (tracker_id, experiment_id) SELECT 'M6A-P003::M6A-P003-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source',
    'Tracker experiment M6A-P004-E001',
    'Module 6B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M6B-O004"], "source_experiment_tracker_id": "M6A-P004-E001", "source_paper_tracker_id": "M6A-P004", "tracker_key": "M6A-P004::M6A-P004-E001"}'
  FROM _m6_paper_map p
  JOIN _m6_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M6A-P004'
  RETURNING experiment_id
)
INSERT INTO _m6_experiment_map (tracker_id, experiment_id) SELECT 'M6A-P004::M6A-P004-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source',
    'Tracker experiment M6A-P005-E001',
    'Module 6B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M6B-O005"], "source_experiment_tracker_id": "M6A-P005-E001", "source_paper_tracker_id": "M6A-P005", "tracker_key": "M6A-P005::M6A-P005-E001"}'
  FROM _m6_paper_map p
  JOIN _m6_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M6A-P005'
  RETURNING experiment_id
)
INSERT INTO _m6_experiment_map (tracker_id, experiment_id) SELECT 'M6A-P005::M6A-P005-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/PMC',
    'Tracker experiment M6A-P006-E001',
    'Module 6B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M6B-O006"], "source_experiment_tracker_id": "M6A-P006-E001", "source_paper_tracker_id": "M6A-P006", "tracker_key": "M6A-P006::M6A-P006-E001"}'
  FROM _m6_paper_map p
  JOIN _m6_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M6A-P006'
  RETURNING experiment_id
)
INSERT INTO _m6_experiment_map (tracker_id, experiment_id) SELECT 'M6A-P006::M6A-P006-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/PMC',
    'Tracker experiment M6A-P007-E001',
    'Module 6B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M6B-O007"], "source_experiment_tracker_id": "M6A-P007-E001", "source_paper_tracker_id": "M6A-P007", "tracker_key": "M6A-P007::M6A-P007-E001"}'
  FROM _m6_paper_map p
  JOIN _m6_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M6A-P007'
  RETURNING experiment_id
)
INSERT INTO _m6_experiment_map (tracker_id, experiment_id) SELECT 'M6A-P007::M6A-P007-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/PMC',
    'Tracker experiment M6A-P008-E001',
    'Module 6B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M6B-O008"], "source_experiment_tracker_id": "M6A-P008-E001", "source_paper_tracker_id": "M6A-P008", "tracker_key": "M6A-P008::M6A-P008-E001"}'
  FROM _m6_paper_map p
  JOIN _m6_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M6A-P008'
  RETURNING experiment_id
)
INSERT INTO _m6_experiment_map (tracker_id, experiment_id) SELECT 'M6A-P008::M6A-P008-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/PMC',
    'Tracker experiment M6A-P009-E001',
    'Module 6B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M6B-O009"], "source_experiment_tracker_id": "M6A-P009-E001", "source_paper_tracker_id": "M6A-P009", "tracker_key": "M6A-P009::M6A-P009-E001"}'
  FROM _m6_paper_map p
  JOIN _m6_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M6A-P009'
  RETURNING experiment_id
)
INSERT INTO _m6_experiment_map (tracker_id, experiment_id) SELECT 'M6A-P009::M6A-P009-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source',
    'Tracker experiment M6A-P010-E001',
    'Module 6B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M6B-O010"], "source_experiment_tracker_id": "M6A-P010-E001", "source_paper_tracker_id": "M6A-P010", "tracker_key": "M6A-P010::M6A-P010-E001"}'
  FROM _m6_paper_map p
  JOIN _m6_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M6A-P010'
  RETURNING experiment_id
)
INSERT INTO _m6_experiment_map (tracker_id, experiment_id) SELECT 'M6A-P010::M6A-P010-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/PubMed',
    'Tracker experiment M6A-P011-E001',
    'Module 6B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M6B-O011"], "source_experiment_tracker_id": "M6A-P011-E001", "source_paper_tracker_id": "M6A-P011", "tracker_key": "M6A-P011::M6A-P011-E001"}'
  FROM _m6_paper_map p
  JOIN _m6_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M6A-P011'
  RETURNING experiment_id
)
INSERT INTO _m6_experiment_map (tracker_id, experiment_id) SELECT 'M6A-P011::M6A-P011-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/PubMed',
    'Tracker experiment M6A-P012-E001',
    'Module 6B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M6B-O012"], "source_experiment_tracker_id": "M6A-P012-E001", "source_paper_tracker_id": "M6A-P012", "tracker_key": "M6A-P012::M6A-P012-E001"}'
  FROM _m6_paper_map p
  JOIN _m6_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M6A-P012'
  RETURNING experiment_id
)
INSERT INTO _m6_experiment_map (tracker_id, experiment_id) SELECT 'M6A-P012::M6A-P012-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/PubMed',
    'Tracker experiment M6A-P013-E001',
    'Module 6B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M6B-O013"], "source_experiment_tracker_id": "M6A-P013-E001", "source_paper_tracker_id": "M6A-P013", "tracker_key": "M6A-P013::M6A-P013-E001"}'
  FROM _m6_paper_map p
  JOIN _m6_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M6A-P013'
  RETURNING experiment_id
)
INSERT INTO _m6_experiment_map (tracker_id, experiment_id) SELECT 'M6A-P013::M6A-P013-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/PMC',
    'Tracker experiment M6A-P014-E001',
    'Module 6B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M6B-O014"], "source_experiment_tracker_id": "M6A-P014-E001", "source_paper_tracker_id": "M6A-P014", "tracker_key": "M6A-P014::M6A-P014-E001"}'
  FROM _m6_paper_map p
  JOIN _m6_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M6A-P014'
  RETURNING experiment_id
)
INSERT INTO _m6_experiment_map (tracker_id, experiment_id) SELECT 'M6A-P014::M6A-P014-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/PubMed',
    'Tracker experiment M6A-P015-E001',
    'Module 6B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M6B-O015"], "source_experiment_tracker_id": "M6A-P015-E001", "source_paper_tracker_id": "M6A-P015", "tracker_key": "M6A-P015::M6A-P015-E001"}'
  FROM _m6_paper_map p
  JOIN _m6_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M6A-P015'
  RETURNING experiment_id
)
INSERT INTO _m6_experiment_map (tracker_id, experiment_id) SELECT 'M6A-P015::M6A-P015-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/PMC',
    'Tracker experiment M6A-P016-E001',
    'Module 6B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M6B-O016"], "source_experiment_tracker_id": "M6A-P016-E001", "source_paper_tracker_id": "M6A-P016", "tracker_key": "M6A-P016::M6A-P016-E001"}'
  FROM _m6_paper_map p
  JOIN _m6_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M6A-P016'
  RETURNING experiment_id
)
INSERT INTO _m6_experiment_map (tracker_id, experiment_id) SELECT 'M6A-P016::M6A-P016-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'M1A carried',
    'Tracker experiment M6A-P017-E001',
    'Module 6B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M6B-O017"], "source_experiment_tracker_id": "M6A-P017-E001", "source_paper_tracker_id": "M6A-P017", "tracker_key": "M6A-P017::M6A-P017-E001"}'
  FROM _m6_paper_map p
  JOIN _m6_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M6A-P017'
  RETURNING experiment_id
)
INSERT INTO _m6_experiment_map (tracker_id, experiment_id) SELECT 'M6A-P017::M6A-P017-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source',
    'Tracker experiment M6A-P018-E001',
    'Module 6B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M6B-O018"], "source_experiment_tracker_id": "M6A-P018-E001", "source_paper_tracker_id": "M6A-P018", "tracker_key": "M6A-P018::M6A-P018-E001"}'
  FROM _m6_paper_map p
  JOIN _m6_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M6A-P018'
  RETURNING experiment_id
)
INSERT INTO _m6_experiment_map (tracker_id, experiment_id) SELECT 'M6A-P018::M6A-P018-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source',
    'Tracker experiment M6A-P019-E001',
    'Module 6B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M6B-O019"], "source_experiment_tracker_id": "M6A-P019-E001", "source_paper_tracker_id": "M6A-P019", "tracker_key": "M6A-P019::M6A-P019-E001"}'
  FROM _m6_paper_map p
  JOIN _m6_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M6A-P019'
  RETURNING experiment_id
)
INSERT INTO _m6_experiment_map (tracker_id, experiment_id) SELECT 'M6A-P019::M6A-P019-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Review/source',
    'Tracker experiment M6A-P020-E001',
    'Module 6B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M6B-O020"], "source_experiment_tracker_id": "M6A-P020-E001", "source_paper_tracker_id": "M6A-P020", "tracker_key": "M6A-P020::M6A-P020-E001"}'
  FROM _m6_paper_map p
  JOIN _m6_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M6A-P020'
  RETURNING experiment_id
)
INSERT INTO _m6_experiment_map (tracker_id, experiment_id) SELECT 'M6A-P020::M6A-P020-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract',
    'Tracker experiment M6A-P021-E001',
    'Module 6B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M6B-O021"], "source_experiment_tracker_id": "M6A-P021-E001", "source_paper_tracker_id": "M6A-P021", "tracker_key": "M6A-P021::M6A-P021-E001"}'
  FROM _m6_paper_map p
  JOIN _m6_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M6A-P021'
  RETURNING experiment_id
)
INSERT INTO _m6_experiment_map (tracker_id, experiment_id) SELECT 'M6A-P021::M6A-P021-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/PMC ref',
    'Tracker experiment M6A-P022-E001',
    'Module 6B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M6B-O022"], "source_experiment_tracker_id": "M6A-P022-E001", "source_paper_tracker_id": "M6A-P022", "tracker_key": "M6A-P022::M6A-P022-E001"}'
  FROM _m6_paper_map p
  JOIN _m6_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M6A-P022'
  RETURNING experiment_id
)
INSERT INTO _m6_experiment_map (tracker_id, experiment_id) SELECT 'M6A-P022::M6A-P022-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract',
    'Tracker experiment M6A-P023-E001',
    'Module 6B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M6B-O023"], "source_experiment_tracker_id": "M6A-P023-E001", "source_paper_tracker_id": "M6A-P023", "tracker_key": "M6A-P023::M6A-P023-E001"}'
  FROM _m6_paper_map p
  JOIN _m6_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M6A-P023'
  RETURNING experiment_id
)
INSERT INTO _m6_experiment_map (tracker_id, experiment_id) SELECT 'M6A-P023::M6A-P023-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract',
    'Tracker experiment M6A-P024-E001',
    'Module 6B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M6B-O024"], "source_experiment_tracker_id": "M6A-P024-E001", "source_paper_tracker_id": "M6A-P024", "tracker_key": "M6A-P024::M6A-P024-E001"}'
  FROM _m6_paper_map p
  JOIN _m6_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M6A-P024'
  RETURNING experiment_id
)
INSERT INTO _m6_experiment_map (tracker_id, experiment_id) SELECT 'M6A-P024::M6A-P024-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract',
    'Tracker experiment M6A-P025-E001',
    'Module 6B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M6B-O025"], "source_experiment_tracker_id": "M6A-P025-E001", "source_paper_tracker_id": "M6A-P025", "tracker_key": "M6A-P025::M6A-P025-E001"}'
  FROM _m6_paper_map p
  JOIN _m6_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M6A-P025'
  RETURNING experiment_id
)
INSERT INTO _m6_experiment_map (tracker_id, experiment_id) SELECT 'M6A-P025::M6A-P025-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract',
    'Tracker experiment M6A-P026-E001',
    'Module 6B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M6B-O026"], "source_experiment_tracker_id": "M6A-P026-E001", "source_paper_tracker_id": "M6A-P026", "tracker_key": "M6A-P026::M6A-P026-E001"}'
  FROM _m6_paper_map p
  JOIN _m6_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M6A-P026'
  RETURNING experiment_id
)
INSERT INTO _m6_experiment_map (tracker_id, experiment_id) SELECT 'M6A-P026::M6A-P026-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract',
    'Tracker experiment M6A-P027-E001',
    'Module 6B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M6B-O027"], "source_experiment_tracker_id": "M6A-P027-E001", "source_paper_tracker_id": "M6A-P027", "tracker_key": "M6A-P027::M6A-P027-E001"}'
  FROM _m6_paper_map p
  JOIN _m6_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M6A-P027'
  RETURNING experiment_id
)
INSERT INTO _m6_experiment_map (tracker_id, experiment_id) SELECT 'M6A-P027::M6A-P027-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract',
    'Tracker experiment M6A-P028-E001',
    'Module 6B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M6B-O028"], "source_experiment_tracker_id": "M6A-P028-E001", "source_paper_tracker_id": "M6A-P028", "tracker_key": "M6A-P028::M6A-P028-E001"}'
  FROM _m6_paper_map p
  JOIN _m6_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M6A-P028'
  RETURNING experiment_id
)
INSERT INTO _m6_experiment_map (tracker_id, experiment_id) SELECT 'M6A-P028::M6A-P028-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Review/map',
    'Tracker experiment M6A-P029-E001',
    'Module 6B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M6B-O029"], "source_experiment_tracker_id": "M6A-P029-E001", "source_paper_tracker_id": "M6A-P029", "tracker_key": "M6A-P029::M6A-P029-E001"}'
  FROM _m6_paper_map p
  JOIN _m6_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M6A-P029'
  RETURNING experiment_id
)
INSERT INTO _m6_experiment_map (tracker_id, experiment_id) SELECT 'M6A-P029::M6A-P029-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Methods/map',
    'Tracker experiment M6A-P030-E001',
    'Module 6B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M6B-O030"], "source_experiment_tracker_id": "M6A-P030-E001", "source_paper_tracker_id": "M6A-P030", "tracker_key": "M6A-P030::M6A-P030-E001"}'
  FROM _m6_paper_map p
  JOIN _m6_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M6A-P030'
  RETURNING experiment_id
)
INSERT INTO _m6_experiment_map (tracker_id, experiment_id) SELECT 'M6A-P030::M6A-P030-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source',
    'Tracker experiment M6A-P031-E001',
    'Module 6B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M6B-O031"], "source_experiment_tracker_id": "M6A-P031-E001", "source_paper_tracker_id": "M6A-P031", "tracker_key": "M6A-P031::M6A-P031-E001"}'
  FROM _m6_paper_map p
  JOIN _m6_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M6A-P031'
  RETURNING experiment_id
)
INSERT INTO _m6_experiment_map (tracker_id, experiment_id) SELECT 'M6A-P031::M6A-P031-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source',
    'Tracker experiment M6A-P032-E001',
    'Module 6B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M6B-O032"], "source_experiment_tracker_id": "M6A-P032-E001", "source_paper_tracker_id": "M6A-P032", "tracker_key": "M6A-P032::M6A-P032-E001"}'
  FROM _m6_paper_map p
  JOIN _m6_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M6A-P032'
  RETURNING experiment_id
)
INSERT INTO _m6_experiment_map (tracker_id, experiment_id) SELECT 'M6A-P032::M6A-P032-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Review/map',
    'Tracker experiment M6A-P033-E001',
    'Module 6B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M6B-O033"], "source_experiment_tracker_id": "M6A-P033-E001", "source_paper_tracker_id": "M6A-P033", "tracker_key": "M6A-P033::M6A-P033-E001"}'
  FROM _m6_paper_map p
  JOIN _m6_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M6A-P033'
  RETURNING experiment_id
)
INSERT INTO _m6_experiment_map (tracker_id, experiment_id) SELECT 'M6A-P033::M6A-P033-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Review/map',
    'Tracker experiment M6A-P034-E001',
    'Module 6B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M6B-O034"], "source_experiment_tracker_id": "M6A-P034-E001", "source_paper_tracker_id": "M6A-P034", "tracker_key": "M6A-P034::M6A-P034-E001"}'
  FROM _m6_paper_map p
  JOIN _m6_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M6A-P034'
  RETURNING experiment_id
)
INSERT INTO _m6_experiment_map (tracker_id, experiment_id) SELECT 'M6A-P034::M6A-P034-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/PMC',
    'Tracker experiment M6A-P035-E001',
    'Module 6B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M6B-O035"], "source_experiment_tracker_id": "M6A-P035-E001", "source_paper_tracker_id": "M6A-P035", "tracker_key": "M6A-P035::M6A-P035-E001"}'
  FROM _m6_paper_map p
  JOIN _m6_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M6A-P035'
  RETURNING experiment_id
)
INSERT INTO _m6_experiment_map (tracker_id, experiment_id) SELECT 'M6A-P035::M6A-P035-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Review/map',
    'Tracker experiment M6A-P036-E001',
    'Module 6B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M6B-O036"], "source_experiment_tracker_id": "M6A-P036-E001", "source_paper_tracker_id": "M6A-P036", "tracker_key": "M6A-P036::M6A-P036-E001"}'
  FROM _m6_paper_map p
  JOIN _m6_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M6A-P036'
  RETURNING experiment_id
)
INSERT INTO _m6_experiment_map (tracker_id, experiment_id) SELECT 'M6A-P036::M6A-P036-E001', experiment_id FROM inserted;

INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Autopsy vascular pathology', 'Module 6B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Biomarker readiness', 'Module 6B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Brain morphometry', 'Module 6B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Cervical cord MRS', 'Module 6B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Cervical tissue bridge MRI', 'Module 6B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Chronic DTI', 'Module 6B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Chronic MRI stereology', 'Module 6B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Chronic complete qMRI', 'Module 6B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Cord atrophy MRI', 'Module 6B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Late syrinx precedent', 'Module 6B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Longitudinal brain/CST MRI', 'Module 6B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Longitudinal fMRI', 'Module 6B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Longitudinal qMRI', 'Module 6B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Multimodal MRI/fMRI', 'Module 6B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Neurodegeneration imaging', 'Module 6B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Neuroimaging synthesis', 'Module 6B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Pediatric DTI', 'Module 6B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Sensory pathway MRI', 'Module 6B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Structural MRI/fMRI', 'Module 6B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Subject-specific DTI', 'Module 6B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Supraspinal MRS', 'Module 6B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Surgical anatomy/trial', 'Module 6B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Syrinx autopsy pathology', 'Module 6B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Thoracic tissue bridge MRI', 'Module 6B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Tissue bridge MRI', 'Module 6B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Tract-specific diffusion MRI', 'Module 6B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Traumatic/nontraumatic synthesis', 'Module 6B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Trial imaging framework', 'Module 6B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Trial readiness', 'Module 6B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Ventral-root pathology', 'Module 6B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('fMRI', 'Module 6B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('fMRI activation', 'Module 6B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('fMRI cortical plasticity', 'Module 6B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('qMRI interpretation', 'Module 6B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('qMRI prediction', 'Module 6B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('qMRI tract degeneration', 'Module 6B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;

INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Above-lesion degeneration', 'Module 6B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Atrophy and disability', 'Module 6B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Axon and myelin pathology', 'Module 6B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Brainstem/dorsal column change', 'Module 6B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Chronic complication', 'Module 6B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Chronic cyst complication', 'Module 6B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Cortical reorganization', 'Module 6B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Cortical representation', 'Module 6B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Diagnostic workup', 'Module 6B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Force association', 'Module 6B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Functional recovery', 'Module 6B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Imaging category map', 'Module 6B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Impairment association', 'Module 6B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Lesion and motor-system change', 'Module 6B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Lesion architecture', 'Module 6B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('MRI-normal cord abnormality', 'Module 6B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Metabolic alteration', 'Module 6B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Metabolic change', 'Module 6B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Modality boundary', 'Module 6B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Motor cortex reorganization', 'Module 6B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Motor output', 'Module 6B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Motor/sensory deficits', 'Module 6B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Pathology boundary', 'Module 6B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Prognosis/stratification', 'Module 6B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Progressive remote degeneration', 'Module 6B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Recovery plasticity', 'Module 6B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Recovery prediction', 'Module 6B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Remote degeneration', 'Module 6B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Scar resection and implantation', 'Module 6B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Screening/outcome framework', 'Module 6B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Screening/stratification', 'Module 6B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Sensory atrophy/outcome', 'Module 6B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Supraspinal atrophy', 'Module 6B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Vascular and secondary tissue damage', 'Module 6B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Walking ability', 'Module 6B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Whole-cord diffusion', 'Module 6B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Focal cystic atrophy was largely restricted to the impact site, with substantial adjacent rostral/caudal cord mass preserved except in late syrinx cases.',
    'cord area/anatomy',
    'MRI / imaging assay',
    'Focal cystic atrophy was largely restricted to the impact site, with substantial adjacent rostral/caudal cord mass preserved except in late syrinx cases.',
    'chronic SCI can preserve adjacent cord mass despite focal cystic loss',
    'M1A carried',
    'Fig 1; Table 1',
    'high',
    '{"curator_notes": "Human structural preservation anchor.", "experiment_tracker_id": "M6A-P001-E001", "measurement_method_inference": "MRI / imaging assay", "paper_tracker_id": "M6A-P001", "quantitative": "YES", "statistics_reported": "source/full-text carried", "topic_id": "M6B-T001", "tracker_id": "M6B-O001"}'
  FROM _m6_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M6A-P001::M6A-P001-E001'
    AND et.evidence_type_name = 'Chronic MRI stereology'
    AND ot.outcome_type_name = 'Lesion architecture'
  RETURNING observation_id
)
INSERT INTO _m6_observation_map (tracker_id, observation_id) SELECT 'M6B-O001', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Human SCI caused large-diameter ventral-root axon loss at/near lesion levels and thin myelin in surviving large fibers.',
    'axon count/myelin',
    'immunostaining / histology / pathology; MRI / imaging assay',
    'Human SCI caused large-diameter ventral-root axon loss at/near lesion levels and thin myelin in surviving large fibers.',
    'chronic SCI includes ventral-root axon loss and thin-myelin pathology',
    'M1A carried',
    'Fig 1-Fig 5',
    'high',
    '{"curator_notes": "Tissue pathology not captured by MRI alone.", "experiment_tracker_id": "M6A-P002-E001", "measurement_method_inference": "immunostaining / histology / pathology; MRI / imaging assay", "paper_tracker_id": "M6A-P002", "quantitative": "YES", "statistics_reported": "source/full-text carried", "topic_id": "M6B-T002", "tracker_id": "M6B-O002"}'
  FROM _m6_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M6A-P002::M6A-P002-E001'
    AND et.evidence_type_name = 'Ventral-root pathology'
    AND ot.outcome_type_name = 'Axon and myelin pathology'
  RETURNING observation_id
)
INSERT INTO _m6_observation_map (tracker_id, observation_id) SELECT 'M6B-O002', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Five patients underwent MRI/electrophysiology-guided chronic scar resection and scaffold-cell implantation.',
    'feasibility/anatomy',
    'MRI / imaging assay',
    'Five patients underwent MRI/electrophysiology-guided chronic scar resection and scaffold-cell implantation.',
    'chronic scar-resection anatomy can be mapped for human scaffold implantation',
    'Source page',
    'Clinical source',
    'high',
    '{"curator_notes": "Human reconstructive anatomy precedent.", "experiment_tracker_id": "M6A-P003-E001", "measurement_method_inference": "MRI / imaging assay", "paper_tracker_id": "M6A-P003", "quantitative": "YES", "statistics_reported": "source-page level", "topic_id": "M6B-T001", "tracker_id": "M6B-O003"}'
  FROM _m6_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M6A-P003::M6A-P003-E001'
    AND et.evidence_type_name = 'Surgical anatomy/trial'
    AND ot.outcome_type_name = 'Scar resection and implantation'
  RETURNING observation_id
)
INSERT INTO _m6_observation_map (tracker_id, observation_id) SELECT 'M6B-O003', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Pediatric SCI groups showed abnormal FA/RD in adjacent MRI-normal-appearing cord segments, with FA patterns related to AIS severity.',
    'FA/RD/AIS',
    'MRI / imaging assay',
    'Pediatric SCI groups showed abnormal FA/RD in adjacent MRI-normal-appearing cord segments, with FA patterns related to AIS severity.',
    'DTI detects pediatric SCI abnormalities beyond conventional MRI',
    'Abstract/source page',
    'Abstract/source',
    'medium',
    '{"curator_notes": "Pediatric and MRI-normal boundary.", "experiment_tracker_id": "M6A-P004-E001", "measurement_method_inference": "MRI / imaging assay", "paper_tracker_id": "M6A-P004", "quantitative": "YES", "statistics_reported": "abstract-level", "topic_id": "M6B-T003", "tracker_id": "M6B-O004"}'
  FROM _m6_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M6A-P004::M6A-P004-E001'
    AND et.evidence_type_name = 'Pediatric DTI'
    AND ot.outcome_type_name = 'MRI-normal cord abnormality'
  RETURNING observation_id
)
INSERT INTO _m6_observation_map (tracker_id, observation_id) SELECT 'M6B-O004', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Lesion size contracted early, tissue bridges emerged, remote cord/CST degeneration progressed, and lesion/myelin metrics predicted long-term motor and SCIM recovery.',
    'lesion/qMRI/recovery',
    'MRI / imaging assay; behavioral / functional recovery assay',
    'Lesion size contracted early, tissue bridges emerged, remote cord/CST degeneration progressed, and lesion/myelin metrics predicted long-term motor and SCIM recovery.',
    'acute-to-chronic MRI tracks lesion contraction, bridges, degeneration, and recovery prediction',
    'Abstract/source page',
    'Abstract/source',
    'high',
    '{"curator_notes": "Strong longitudinal imaging anchor.", "experiment_tracker_id": "M6A-P005-E001", "measurement_method_inference": "MRI / imaging assay; behavioral / functional recovery assay", "paper_tracker_id": "M6A-P005", "quantitative": "YES", "statistics_reported": "source-page level", "topic_id": "M6B-T004", "tracker_id": "M6B-O005"}'
  FROM _m6_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M6A-P005::M6A-P005-E001'
    AND et.evidence_type_name = 'Longitudinal qMRI'
    AND ot.outcome_type_name = 'Lesion and motor-system change'
  RETURNING observation_id
)
INSERT INTO _m6_observation_map (tracker_id, observation_id) SELECT 'M6B-O005', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Chronic SCI showed elevated lesion diffusion, lower FA at lesion, completeness-dependent FA, and altered upper-cervical diffusion.',
    'FA/diffusion',
    NULL,
    'Chronic SCI showed elevated lesion diffusion, lower FA at lesion, completeness-dependent FA, and altered upper-cervical diffusion.',
    'chronic SCI alters lesion and remote DTI metrics',
    'Abstract/PMC',
    'Abstract/PMC',
    'medium',
    '{"curator_notes": "Whole-cord DTI anchor.", "experiment_tracker_id": "M6A-P006-E001", "measurement_method_inference": null, "paper_tracker_id": "M6A-P006", "quantitative": "YES", "statistics_reported": "abstract-level", "topic_id": "M6B-T003", "tracker_id": "M6B-O006"}'
  FROM _m6_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M6A-P006::M6A-P006-E001'
    AND et.evidence_type_name = 'Chronic DTI'
    AND ot.outcome_type_name = 'Whole-cord diffusion'
  RETURNING observation_id
)
INSERT INTO _m6_observation_map (tracker_id, observation_id) SELECT 'M6B-O006', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Subject-specific injury-region DTI metrics were associated with residual motor and sensory impairment.',
    'DTI/ISNCSCI',
    NULL,
    'Subject-specific injury-region DTI metrics were associated with residual motor and sensory impairment.',
    'subject-specific DTI metrics relate to motor/sensory impairment',
    'Abstract/PMC',
    'Abstract/PMC',
    'medium',
    '{"curator_notes": "Tractography-region boundary.", "experiment_tracker_id": "M6A-P007-E001", "measurement_method_inference": null, "paper_tracker_id": "M6A-P007", "quantitative": "YES", "statistics_reported": "abstract-level", "topic_id": "M6B-T003", "tracker_id": "M6B-O007"}'
  FROM _m6_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M6A-P007::M6A-P007-E001'
    AND et.evidence_type_name = 'Subject-specific DTI'
    AND ot.outcome_type_name = 'Impairment association'
  RETURNING observation_id
)
INSERT INTO _m6_observation_map (tracker_id, observation_id) SELECT 'M6B-O007', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Wider midsagittal tissue bridges at 1 month were associated with better lower-extremity motor and pinprick recovery at 1 year.',
    'bridge width/recovery',
    'MRI / imaging assay; behavioral / functional recovery assay',
    'Wider midsagittal tissue bridges at 1 month were associated with better lower-extremity motor and pinprick recovery at 1 year.',
    'thoracic tissue bridges predict lower-extremity motor and pinprick recovery',
    'Abstract/PMC',
    'Abstract/PMC',
    'medium',
    '{"curator_notes": "Thoracic traumatic/ischemic boundary.", "experiment_tracker_id": "M6A-P008-E001", "measurement_method_inference": "MRI / imaging assay; behavioral / functional recovery assay", "paper_tracker_id": "M6A-P008", "quantitative": "YES", "statistics_reported": "abstract-level", "topic_id": "M6B-T004", "tracker_id": "M6B-O008"}'
  FROM _m6_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M6A-P008::M6A-P008-E001'
    AND et.evidence_type_name = 'Thoracic tissue bridge MRI'
    AND ot.outcome_type_name = 'Recovery prediction'
  RETURNING observation_id
)
INSERT INTO _m6_observation_map (tracker_id, observation_id) SELECT 'M6B-O008', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Cervical tissue bridge measures supported recovery-specific stratification and trial prognostication.',
    'bridge metrics/recovery',
    'MRI / imaging assay; behavioral / functional recovery assay',
    'Cervical tissue bridge measures supported recovery-specific stratification and trial prognostication.',
    'cervical tissue bridges support recovery prognostication',
    'Abstract/PMC',
    'Abstract/PMC',
    'medium',
    '{"curator_notes": "Multicentre cervical anchor.", "experiment_tracker_id": "M6A-P009-E001", "measurement_method_inference": "MRI / imaging assay; behavioral / functional recovery assay", "paper_tracker_id": "M6A-P009", "quantitative": "YES", "statistics_reported": "abstract-level", "topic_id": "M6B-T004", "tracker_id": "M6B-O009"}'
  FROM _m6_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M6A-P009::M6A-P009-E001'
    AND et.evidence_type_name = 'Cervical tissue bridge MRI'
    AND ot.outcome_type_name = 'Prognosis/stratification'
  RETURNING observation_id
)
INSERT INTO _m6_observation_map (tracker_id, observation_id) SELECT 'M6B-O009', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Chronic SCI showed lower tNAA/mI and tCho/mI ratios at C2, associated with atrophy, tissue bridge severity, and worse sensory/motor outcomes.',
    'metabolite ratios',
    NULL,
    'Chronic SCI showed lower tNAA/mI and tCho/mI ratios at C2, associated with atrophy, tissue bridge severity, and worse sensory/motor outcomes.',
    'cervical MRS detects supralesional metabolic change linked to impairment',
    'Abstract/source page',
    'Abstract/source',
    'medium',
    '{"curator_notes": "Metabolic spinal cord biomarker.", "experiment_tracker_id": "M6A-P010-E001", "measurement_method_inference": null, "paper_tracker_id": "M6A-P010", "quantitative": "YES", "statistics_reported": "abstract-level", "topic_id": "M6B-T005", "tracker_id": "M6B-O010"}'
  FROM _m6_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M6A-P010::M6A-P010-E001'
    AND et.evidence_type_name = 'Cervical cord MRS'
    AND ot.outcome_type_name = 'Metabolic alteration'
  RETURNING observation_id
)
INSERT INTO _m6_observation_map (tracker_id, observation_id) SELECT 'M6B-O010', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Longitudinal MRI detected degeneration above lesion in cranial CST and sensorimotor cortices with clinical outcome relevance.',
    'volume/morphometry',
    'MRI / imaging assay',
    'Longitudinal MRI detected degeneration above lesion in cranial CST and sensorimotor cortices with clinical outcome relevance.',
    'SCI causes remote CST and sensorimotor cortical degeneration',
    'PubMed',
    'Abstract/PubMed',
    'low',
    '{"curator_notes": "Full text upgrade needed.", "experiment_tracker_id": "M6A-P011-E001", "measurement_method_inference": "MRI / imaging assay", "paper_tracker_id": "M6A-P011", "quantitative": "YES", "statistics_reported": "abstract-level", "topic_id": "M6B-T005", "tracker_id": "M6B-O011"}'
  FROM _m6_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M6A-P011::M6A-P011-E001'
    AND et.evidence_type_name = 'Longitudinal brain/CST MRI'
    AND ot.outcome_type_name = 'Remote degeneration'
  RETURNING observation_id
)
INSERT INTO _m6_observation_map (tracker_id, observation_id) SELECT 'M6B-O011', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Early rostral cord and brain volume/microstructural changes predicted functional recovery.',
    'qMRI/recovery',
    'behavioral / functional recovery assay',
    'Early rostral cord and brain volume/microstructural changes predicted functional recovery.',
    'early qMRI rostral cord/brain metrics predict recovery',
    'PubMed',
    'Abstract/PubMed',
    'medium',
    '{"curator_notes": "Prediction anchor.", "experiment_tracker_id": "M6A-P012-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M6A-P012", "quantitative": "YES", "statistics_reported": "abstract-level", "topic_id": "M6B-T005", "tracker_id": "M6B-O012"}'
  FROM _m6_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M6A-P012::M6A-P012-E001'
    AND et.evidence_type_name = 'qMRI prediction'
    AND ot.outcome_type_name = 'Functional recovery'
  RETURNING observation_id
)
INSERT INTO _m6_observation_map (tracker_id, observation_id) SELECT 'M6B-O012', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'CST microstructural integrity related to spinal cord area and sensorimotor cortical reorganization.',
    'CST/cortex',
    'MRI / imaging assay',
    'CST microstructural integrity related to spinal cord area and sensorimotor cortical reorganization.',
    'axonal integrity links spinal structure to cortical reorganization',
    'PubMed',
    'Abstract/PubMed',
    'medium',
    '{"curator_notes": "Tract-plasticity linkage.", "experiment_tracker_id": "M6A-P013-E001", "measurement_method_inference": "MRI / imaging assay", "paper_tracker_id": "M6A-P013", "quantitative": "YES", "statistics_reported": "abstract-level", "topic_id": "M6B-T006", "tracker_id": "M6B-O013"}'
  FROM _m6_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M6A-P013::M6A-P013-E001'
    AND et.evidence_type_name = 'Multimodal MRI/fMRI'
    AND ot.outcome_type_name = 'Cortical reorganization'
  RETURNING observation_id
)
INSERT INTO _m6_observation_map (tracker_id, observation_id) SELECT 'M6B-O013', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Cord and cortical atrophy were associated with sensorimotor cortical reorganization and disability.',
    'atrophy/fMRI',
    'MRI / imaging assay',
    'Cord and cortical atrophy were associated with sensorimotor cortical reorganization and disability.',
    'cord/cortical atrophy associates with reorganization and disability',
    'Abstract/PMC',
    'Abstract/PMC',
    'medium',
    '{"curator_notes": "Brain-spine linkage.", "experiment_tracker_id": "M6A-P014-E001", "measurement_method_inference": "MRI / imaging assay", "paper_tracker_id": "M6A-P014", "quantitative": "YES", "statistics_reported": "abstract-level", "topic_id": "M6B-T006", "tracker_id": "M6B-O014"}'
  FROM _m6_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M6A-P014::M6A-P014-E001'
    AND et.evidence_type_name = 'Structural MRI/fMRI'
    AND ot.outcome_type_name = 'Atrophy and disability'
  RETURNING observation_id
)
INSERT INTO _m6_observation_map (tracker_id, observation_id) SELECT 'M6B-O014', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Paraplegic patients showed altered cortical representation of non-affected upper limb movements.',
    'fMRI activation',
    NULL,
    'Paraplegic patients showed altered cortical representation of non-affected upper limb movements.',
    'chronic SCI alters motor cortical representation',
    'PubMed',
    'Abstract/PubMed',
    'low',
    '{"curator_notes": "Indirect for lesion anatomy.", "experiment_tracker_id": "M6A-P015-E001", "measurement_method_inference": null, "paper_tracker_id": "M6A-P015", "quantitative": "YES", "statistics_reported": "abstract-level", "topic_id": "M6B-T006", "tracker_id": "M6B-O015"}'
  FROM _m6_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M6A-P015::M6A-P015-E001'
    AND et.evidence_type_name = 'fMRI'
    AND ot.outcome_type_name = 'Cortical representation'
  RETURNING observation_id
)
INSERT INTO _m6_observation_map (tracker_id, observation_id) SELECT 'M6B-O015', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Remote CST and dorsal column degeneration formed progressive spatial gradients after SCI.',
    'tract qMRI',
    'spatial transcriptomics / spatial atlas',
    'Remote CST and dorsal column degeneration formed progressive spatial gradients after SCI.',
    'major spinal pathways degenerate progressively after SCI',
    'Abstract/PMC',
    'Abstract/PMC',
    'medium',
    '{"curator_notes": "Tract-gradient anchor.", "experiment_tracker_id": "M6A-P016-E001", "measurement_method_inference": "spatial transcriptomics / spatial atlas", "paper_tracker_id": "M6A-P016", "quantitative": "YES", "statistics_reported": "abstract-level", "topic_id": "M6B-T005", "tracker_id": "M6B-O016"}'
  FROM _m6_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M6A-P016::M6A-P016-E001'
    AND et.evidence_type_name = 'qMRI tract degeneration'
    AND ot.outcome_type_name = 'Progressive remote degeneration'
  RETURNING observation_id
)
INSERT INTO _m6_observation_map (tracker_id, observation_id) SELECT 'M6B-O016', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Human SCI vascular pathology included hemorrhage, white-matter degeneration, venous occlusion, cavitation, and remote infarct-like lesions.',
    'histology/microangiography',
    'immunostaining / histology / pathology',
    'Human SCI vascular pathology included hemorrhage, white-matter degeneration, venous occlusion, cavitation, and remote infarct-like lesions.',
    'human SCI includes vascular pathology and remote infarct-like lesions',
    'M1A carried',
    'M1A carried',
    'high',
    '{"curator_notes": "Vascular compartment anchor.", "experiment_tracker_id": "M6A-P017-E001", "measurement_method_inference": "immunostaining / histology / pathology", "paper_tracker_id": "M6A-P017", "quantitative": "YES", "statistics_reported": "source/full-text carried", "topic_id": "M6B-T002", "tracker_id": "M6B-O017"}'
  FROM _m6_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M6A-P017::M6A-P017-E001'
    AND et.evidence_type_name = 'Autopsy vascular pathology'
    AND ot.outcome_type_name = 'Vascular and secondary tissue damage'
  RETURNING observation_id
)
INSERT INTO _m6_observation_map (tracker_id, observation_id) SELECT 'M6B-O017', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Syrinx occurred in partially damaged segments and drainage did not yield satisfactory symptom relief despite radiographic drainage.',
    'syrinx/function',
    'immunostaining / histology / pathology',
    'Syrinx occurred in partially damaged segments and drainage did not yield satisfactory symptom relief despite radiographic drainage.',
    'post-traumatic syrinx can persist as chronic structural pathology',
    'Abstract/source page',
    'Abstract/source',
    'medium',
    '{"curator_notes": "Cyst/syrinx boundary.", "experiment_tracker_id": "M6A-P018-E001", "measurement_method_inference": "immunostaining / histology / pathology", "paper_tracker_id": "M6A-P018", "quantitative": "YES", "statistics_reported": "abstract-level", "topic_id": "M6B-T001", "tracker_id": "M6B-O018"}'
  FROM _m6_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M6A-P018::M6A-P018-E001'
    AND et.evidence_type_name = 'Syrinx autopsy pathology'
    AND ot.outcome_type_name = 'Chronic cyst complication'
  RETURNING observation_id
)
INSERT INTO _m6_observation_map (tracker_id, observation_id) SELECT 'M6B-O018', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Progressive late post-traumatic syringomyelia was identified as a chronic structural complication after SCI.',
    'syrinx',
    NULL,
    'Progressive late post-traumatic syringomyelia was identified as a chronic structural complication after SCI.',
    'late post-traumatic syringomyelia is a chronic SCI complication',
    'Abstract/source page',
    'Abstract/source',
    'low',
    '{"curator_notes": "Legacy row.", "experiment_tracker_id": "M6A-P019-E001", "measurement_method_inference": null, "paper_tracker_id": "M6A-P019", "quantitative": "NO", "statistics_reported": "abstract-level", "topic_id": "M6B-T001", "tracker_id": "M6B-O019"}'
  FROM _m6_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M6A-P019::M6A-P019-E001'
    AND et.evidence_type_name = 'Late syrinx precedent'
    AND ot.outcome_type_name = 'Chronic complication'
  RETURNING observation_id
)
INSERT INTO _m6_observation_map (tracker_id, observation_id) SELECT 'M6B-O019', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'MRI anatomy is positioned as a clinical trial screening and outcome-measure tool.',
    'trial framework',
    'MRI / imaging assay',
    'MRI anatomy is positioned as a clinical trial screening and outcome-measure tool.',
    'MRI supports SCI trial screening and endpoint selection',
    'Review/source',
    'Review/source',
    'medium',
    '{"curator_notes": "Map anchor, not primary cohort.", "experiment_tracker_id": "M6A-P020-E001", "measurement_method_inference": "MRI / imaging assay", "paper_tracker_id": "M6A-P020", "quantitative": "NO", "statistics_reported": "review-level", "topic_id": "M6B-T007", "tracker_id": "M6B-O020"}'
  FROM _m6_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M6A-P020::M6A-P020-E001'
    AND et.evidence_type_name = 'Trial imaging framework'
    AND ot.outcome_type_name = 'Screening/outcome framework'
  RETURNING observation_id
)
INSERT INTO _m6_observation_map (tracker_id, observation_id) SELECT 'M6B-O020', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Independent spinal cord atrophy measures correlated with motor and sensory deficits.',
    'atrophy/deficits',
    'MRI / imaging assay',
    'Independent spinal cord atrophy measures correlated with motor and sensory deficits.',
    'cord atrophy metrics correlate with impairment',
    'Abstract',
    'Abstract',
    'low',
    '{"curator_notes": "Full text upgrade needed.", "experiment_tracker_id": "M6A-P021-E001", "measurement_method_inference": "MRI / imaging assay", "paper_tracker_id": "M6A-P021", "quantitative": "YES", "statistics_reported": "abstract-level", "topic_id": "M6B-T005", "tracker_id": "M6B-O021"}'
  FROM _m6_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M6A-P021::M6A-P021-E001'
    AND et.evidence_type_name = 'Cord atrophy MRI'
    AND ot.outcome_type_name = 'Motor/sensory deficits'
  RETURNING observation_id
)
INSERT INTO _m6_observation_map (tracker_id, observation_id) SELECT 'M6B-O021', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Lateral corticospinal tract damage correlated with motor output in incomplete SCI.',
    'CST diffusion/motor',
    'MRI / imaging assay',
    'Lateral corticospinal tract damage correlated with motor output in incomplete SCI.',
    'lateral CST damage correlates with motor output',
    'Abstract/PMC reference',
    'Abstract/PMC ref',
    'medium',
    '{"curator_notes": "Tract-specific motor anchor.", "experiment_tracker_id": "M6A-P022-E001", "measurement_method_inference": "MRI / imaging assay", "paper_tracker_id": "M6A-P022", "quantitative": "YES", "statistics_reported": "abstract-level", "topic_id": "M6B-T003", "tracker_id": "M6B-O022"}'
  FROM _m6_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M6A-P022::M6A-P022-E001'
    AND et.evidence_type_name = 'Tract-specific diffusion MRI'
    AND ot.outcome_type_name = 'Motor output'
  RETURNING observation_id
)
INSERT INTO _m6_observation_map (tracker_id, observation_id) SELECT 'M6B-O022', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Specific brain regions showed atrophy after cervical SCI.',
    'brain volume',
    NULL,
    'Specific brain regions showed atrophy after cervical SCI.',
    'cervical SCI is associated with brain-region atrophy',
    'Abstract',
    'Abstract',
    'low',
    '{"curator_notes": "Secondary to spinal anatomy.", "experiment_tracker_id": "M6A-P023-E001", "measurement_method_inference": null, "paper_tracker_id": "M6A-P023", "quantitative": "YES", "statistics_reported": "abstract-level", "topic_id": "M6B-T006", "tracker_id": "M6B-O023"}'
  FROM _m6_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M6A-P023::M6A-P023-E001'
    AND et.evidence_type_name = 'Brain morphometry'
    AND ot.outcome_type_name = 'Supraspinal atrophy'
  RETURNING observation_id
)
INSERT INTO _m6_observation_map (tracker_id, observation_id) SELECT 'M6B-O023', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Sensorimotor cortical plasticity changed during recovery following SCI.',
    'fMRI/recovery',
    'behavioral / functional recovery assay',
    'Sensorimotor cortical plasticity changed during recovery following SCI.',
    'sensorimotor cortical plasticity changes during recovery',
    'Abstract',
    'Abstract',
    'low',
    '{"curator_notes": "Full text upgrade needed.", "experiment_tracker_id": "M6A-P024-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M6A-P024", "quantitative": "YES", "statistics_reported": "abstract-level", "topic_id": "M6B-T006", "tracker_id": "M6B-O024"}'
  FROM _m6_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M6A-P024::M6A-P024-E001'
    AND et.evidence_type_name = 'Longitudinal fMRI'
    AND ot.outcome_type_name = 'Recovery plasticity'
  RETURNING observation_id
)
INSERT INTO _m6_observation_map (tracker_id, observation_id) SELECT 'M6B-O024', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Human motor cortex plasticity was observed after cervical SCI.',
    'fMRI',
    NULL,
    'Human motor cortex plasticity was observed after cervical SCI.',
    'cervical SCI is associated with motor cortex plasticity',
    'Abstract',
    'Abstract',
    'low',
    '{"curator_notes": "Early fMRI anchor.", "experiment_tracker_id": "M6A-P025-E001", "measurement_method_inference": null, "paper_tracker_id": "M6A-P025", "quantitative": "YES", "statistics_reported": "abstract-level", "topic_id": "M6B-T006", "tracker_id": "M6B-O025"}'
  FROM _m6_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M6A-P025::M6A-P025-E001'
    AND et.evidence_type_name = 'fMRI cortical plasticity'
    AND ot.outcome_type_name = 'Motor cortex reorganization'
  RETURNING observation_id
)
INSERT INTO _m6_observation_map (tracker_id, observation_id) SELECT 'M6B-O025', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Motor cortex activation related to squeezing force after SCI.',
    'fMRI/force',
    NULL,
    'Motor cortex activation related to squeezing force after SCI.',
    'motor cortex activation relates to residual force',
    'Abstract',
    'Abstract',
    'low',
    '{"curator_notes": "Functional endpoint boundary.", "experiment_tracker_id": "M6A-P026-E001", "measurement_method_inference": null, "paper_tracker_id": "M6A-P026", "quantitative": "YES", "statistics_reported": "abstract-level", "topic_id": "M6B-T006", "tracker_id": "M6B-O026"}'
  FROM _m6_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M6A-P026::M6A-P026-E001'
    AND et.evidence_type_name = 'fMRI activation'
    AND ot.outcome_type_name = 'Force association'
  RETURNING observation_id
)
INSERT INTO _m6_observation_map (tracker_id, observation_id) SELECT 'M6B-O026', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Sensory system atrophy was tracked and linked to outcome prediction.',
    'sensory MRI/outcome',
    'MRI / imaging assay',
    'Sensory system atrophy was tracked and linked to outcome prediction.',
    'sensory pathway atrophy can support outcome prediction',
    'Abstract',
    'Abstract',
    'low',
    '{"curator_notes": "Full text upgrade needed.", "experiment_tracker_id": "M6A-P027-E001", "measurement_method_inference": "MRI / imaging assay", "paper_tracker_id": "M6A-P027", "quantitative": "YES", "statistics_reported": "abstract-level", "topic_id": "M6B-T005", "tracker_id": "M6B-O027"}'
  FROM _m6_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M6A-P027::M6A-P027-E001'
    AND et.evidence_type_name = 'Sensory pathway MRI'
    AND ot.outcome_type_name = 'Sensory atrophy/outcome'
  RETURNING observation_id
)
INSERT INTO _m6_observation_map (tracker_id, observation_id) SELECT 'M6B-O027', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Neurodegeneration above the level of SCI was tracked longitudinally.',
    'neuroimaging',
    'MRI / imaging assay',
    'Neurodegeneration above the level of SCI was tracked longitudinally.',
    'above-lesion neurodegeneration progresses after SCI',
    'Abstract',
    'Abstract',
    'low',
    '{"curator_notes": "Remote degeneration context.", "experiment_tracker_id": "M6A-P028-E001", "measurement_method_inference": "MRI / imaging assay", "paper_tracker_id": "M6A-P028", "quantitative": "YES", "statistics_reported": "abstract-level", "topic_id": "M6B-T005", "tracker_id": "M6B-O028"}'
  FROM _m6_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M6A-P028::M6A-P028-E001'
    AND et.evidence_type_name = 'Neurodegeneration imaging'
    AND ot.outcome_type_name = 'Above-lesion degeneration'
  RETURNING observation_id
)
INSERT INTO _m6_observation_map (tracker_id, observation_id) SELECT 'M6B-O028', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Neuroimaging can reveal pathological similarities and boundaries across traumatic and nontraumatic SCI.',
    'synthesis',
    'immunostaining / histology / pathology; MRI / imaging assay',
    'Neuroimaging can reveal pathological similarities and boundaries across traumatic and nontraumatic SCI.',
    'traumatic and nontraumatic SCI need separate imaging-pathology boundaries',
    'Review/map',
    'Review/map',
    'medium',
    '{"curator_notes": "Etiology boundary.", "experiment_tracker_id": "M6A-P029-E001", "measurement_method_inference": "immunostaining / histology / pathology; MRI / imaging assay", "paper_tracker_id": "M6A-P029", "quantitative": "NO", "statistics_reported": "review-level", "topic_id": "M6B-T007", "tracker_id": "M6B-O029"}'
  FROM _m6_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M6A-P029::M6A-P029-E001'
    AND et.evidence_type_name = 'Traumatic/nontraumatic synthesis'
    AND ot.outcome_type_name = 'Pathology boundary'
  RETURNING observation_id
)
INSERT INTO _m6_observation_map (tracker_id, observation_id) SELECT 'M6B-O029', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'qMRI metrics require cautious interpretation as indirect markers of myelin, iron, and tissue structure.',
    'methods boundary',
    'immunostaining / histology / pathology',
    'qMRI metrics require cautious interpretation as indirect markers of myelin, iron, and tissue structure.',
    'qMRI markers are indirect and histology-informed',
    'Methods/map',
    'Methods/map',
    'medium',
    '{"curator_notes": "Prevents overinterpretation.", "experiment_tracker_id": "M6A-P030-E001", "measurement_method_inference": "immunostaining / histology / pathology", "paper_tracker_id": "M6A-P030", "quantitative": "NO", "statistics_reported": "methods-level", "topic_id": "M6B-T008", "tracker_id": "M6B-O030"}'
  FROM _m6_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M6A-P030::M6A-P030-E001'
    AND et.evidence_type_name = 'qMRI interpretation'
    AND ot.outcome_type_name = 'Modality boundary'
  RETURNING observation_id
)
INSERT INTO _m6_observation_map (tracker_id, observation_id) SELECT 'M6B-O030', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Chronic complete SCI showed supraspinal qMRI changes mainly as caudal brainstem volume reduction consistent with dorsal column Wallerian degeneration.',
    'qMRI volume',
    NULL,
    'Chronic complete SCI showed supraspinal qMRI changes mainly as caudal brainstem volume reduction consistent with dorsal column Wallerian degeneration.',
    'complete SCI qMRI changes localize mainly to caudal brainstem volume reduction',
    'Abstract/source page',
    'Abstract/source',
    'medium',
    '{"curator_notes": "Complete-SCI boundary.", "experiment_tracker_id": "M6A-P031-E001", "measurement_method_inference": null, "paper_tracker_id": "M6A-P031", "quantitative": "YES", "statistics_reported": "abstract-level", "topic_id": "M6B-T005", "tracker_id": "M6B-O031"}'
  FROM _m6_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M6A-P031::M6A-P031-E001'
    AND et.evidence_type_name = 'Chronic complete qMRI'
    AND ot.outcome_type_name = 'Brainstem/dorsal column change'
  RETURNING observation_id
)
INSERT INTO _m6_observation_map (tracker_id, observation_id) SELECT 'M6B-O031', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Complete SCI showed altered metabolites in pons/cerebellum with correlations to clinical scores.',
    'MRS/metabolites',
    NULL,
    'Complete SCI showed altered metabolites in pons/cerebellum with correlations to clinical scores.',
    'supraspinal MRS detects metabolic changes linked to clinical scores',
    'Abstract/source page',
    'Abstract/source',
    'medium',
    '{"curator_notes": "Supraspinal metabolic anchor.", "experiment_tracker_id": "M6A-P032-E001", "measurement_method_inference": null, "paper_tracker_id": "M6A-P032", "quantitative": "YES", "statistics_reported": "abstract-level", "topic_id": "M6B-T005", "tracker_id": "M6B-O032"}'
  FROM _m6_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M6A-P032::M6A-P032-E001'
    AND et.evidence_type_name = 'Supraspinal MRS'
    AND ot.outcome_type_name = 'Metabolic change'
  RETURNING observation_id
)
INSERT INTO _m6_observation_map (tracker_id, observation_id) SELECT 'M6B-O032', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Imaging biomarkers are part of a broader diagnostic workup after traumatic SCI.',
    'biomarker framework',
    'MRI / imaging assay',
    'Imaging biomarkers are part of a broader diagnostic workup after traumatic SCI.',
    'imaging is one component of SCI biomarker workup',
    'Review/map',
    'Review/map',
    'medium',
    '{"curator_notes": "Review-map only.", "experiment_tracker_id": "M6A-P033-E001", "measurement_method_inference": "MRI / imaging assay", "paper_tracker_id": "M6A-P033", "quantitative": "NO", "statistics_reported": "review-level", "topic_id": "M6B-T007", "tracker_id": "M6B-O033"}'
  FROM _m6_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M6A-P033::M6A-P033-E001'
    AND et.evidence_type_name = 'Biomarker readiness'
    AND ot.outcome_type_name = 'Diagnostic workup'
  RETURNING observation_id
)
INSERT INTO _m6_observation_map (tracker_id, observation_id) SELECT 'M6B-O033', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Neuroimaging tracks structural, microstructural, metabolic, and functional consequences of SCI.',
    'synthesis',
    'MRI / imaging assay',
    'Neuroimaging tracks structural, microstructural, metabolic, and functional consequences of SCI.',
    'SCI neuroimaging spans structural, microstructural, metabolic, and functional domains',
    'Review/map',
    'Review/map',
    'medium',
    '{"curator_notes": "Modality map.", "experiment_tracker_id": "M6A-P034-E001", "measurement_method_inference": "MRI / imaging assay", "paper_tracker_id": "M6A-P034", "quantitative": "NO", "statistics_reported": "review-level", "topic_id": "M6B-T007", "tracker_id": "M6B-O034"}'
  FROM _m6_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M6A-P034::M6A-P034-E001'
    AND et.evidence_type_name = 'Neuroimaging synthesis'
    AND ot.outcome_type_name = 'Imaging category map'
  RETURNING observation_id
)
INSERT INTO _m6_observation_map (tracker_id, observation_id) SELECT 'M6B-O034', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Tissue bridge ratio was associated with 6-minute walk distance in incomplete SCI.',
    'bridge ratio/6MWD',
    'MRI / imaging assay',
    'Tissue bridge ratio was associated with 6-minute walk distance in incomplete SCI.',
    'midsagittal tissue bridge ratio associates with walking ability',
    'Abstract/PMC',
    'Abstract/PMC',
    'medium',
    '{"curator_notes": "Incomplete SCI case-series anchor.", "experiment_tracker_id": "M6A-P035-E001", "measurement_method_inference": "MRI / imaging assay", "paper_tracker_id": "M6A-P035", "quantitative": "YES", "statistics_reported": "abstract-level", "topic_id": "M6B-T004", "tracker_id": "M6B-O035"}'
  FROM _m6_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M6A-P035::M6A-P035-E001'
    AND et.evidence_type_name = 'Tissue bridge MRI'
    AND ot.outcome_type_name = 'Walking ability'
  RETURNING observation_id
)
INSERT INTO _m6_observation_map (tracker_id, observation_id) SELECT 'M6B-O035', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Trial-readiness literature frames imaging as screening and stratification rather than direct repair evidence.',
    'trial framework',
    'MRI / imaging assay',
    'Trial-readiness literature frames imaging as screening and stratification rather than direct repair evidence.',
    'imaging trial readiness is screening/stratification evidence',
    'Review/map',
    'Review/map',
    'low',
    '{"curator_notes": "Review-map boundary.", "experiment_tracker_id": "M6A-P036-E001", "measurement_method_inference": "MRI / imaging assay", "paper_tracker_id": "M6A-P036", "quantitative": "NO", "statistics_reported": "review-level", "topic_id": "M6B-T007", "tracker_id": "M6B-O036"}'
  FROM _m6_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M6A-P036::M6A-P036-E001'
    AND et.evidence_type_name = 'Trial readiness'
    AND ot.outcome_type_name = 'Screening/stratification'
  RETURNING observation_id
)
INSERT INTO _m6_observation_map (tracker_id, observation_id) SELECT 'M6B-O036', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Chronic human SCI lesion architecture can preserve adjacent cord tissue while focal cystic loss and syrinx/cyst pathology remain important compartments.',
    'synthesis',
    'high',
    'Tracker/source rows',
    'medium',
    '{"curator_notes": "Architecture claim.", "source_paper_tracker_id": "M6A-P001, P018-P019", "topic_id": "M6B-T001", "tracker_id": "M6B-C001"}'
  FROM _m6_paper_map p
  WHERE p.tracker_id = 'M6A-P001'
  RETURNING claim_id
)
INSERT INTO _m6_claim_map (tracker_id, claim_id) SELECT 'M6B-C001', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Ventral-root axon loss and thin-myelin pathology are human chronic SCI compartments relevant to motor output and remyelination boundaries.',
    'conclusion',
    'high',
    'M1A carried',
    'high',
    '{"curator_notes": "Tissue pathology.", "source_paper_tracker_id": "M6A-P002", "topic_id": "M6B-T002", "tracker_id": "M6B-C002"}'
  FROM _m6_paper_map p
  WHERE p.tracker_id = 'M6A-P002'
  RETURNING claim_id
)
INSERT INTO _m6_claim_map (tracker_id, claim_id) SELECT 'M6B-C002', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Chronic scar resection and scaffold-cell implantation can be anatomically planned with MRI and electrophysiologic boundary mapping in humans.',
    'conclusion',
    'high',
    'Source page',
    'high',
    '{"curator_notes": "Feasibility, not efficacy.", "source_paper_tracker_id": "M6A-P003", "topic_id": "M6B-T001", "tracker_id": "M6B-C003"}'
  FROM _m6_paper_map p
  WHERE p.tracker_id = 'M6A-P003'
  RETURNING claim_id
)
INSERT INTO _m6_claim_map (tracker_id, claim_id) SELECT 'M6B-C003', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Vascular pathology is part of human SCI lesion evolution and can include hemorrhage, venous occlusion, cavitation, and remote infarct-like lesions.',
    'conclusion',
    'high',
    'M1A carried',
    'high',
    '{"curator_notes": "Autopsy anchor.", "source_paper_tracker_id": "M6A-P017", "topic_id": "M6B-T002", "tracker_id": "M6B-C004"}'
  FROM _m6_paper_map p
  WHERE p.tracker_id = 'M6A-P017'
  RETURNING claim_id
)
INSERT INTO _m6_claim_map (tracker_id, claim_id) SELECT 'M6B-C004', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Post-traumatic syrinx and cystic complications should be preserved as distinct chronic structural complications.',
    'conclusion',
    'medium',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Legacy/full-text upgrade boundary.", "source_paper_tracker_id": "M6A-P018-P019", "topic_id": "M6B-T001", "tracker_id": "M6B-C005"}'
  FROM _m6_paper_map p
  WHERE p.tracker_id = 'M6A-P018'
  RETURNING claim_id
)
INSERT INTO _m6_claim_map (tracker_id, claim_id) SELECT 'M6B-C005', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'DTI can detect abnormalities beyond conventional MRI-visible lesion morphology.',
    'synthesis',
    'medium',
    'Abstract/PMC',
    'medium',
    '{"curator_notes": "Modality-specific.", "source_paper_tracker_id": "M6A-P004, P006-P007", "topic_id": "M6B-T003", "tracker_id": "M6B-C006"}'
  FROM _m6_paper_map p
  WHERE p.tracker_id = 'M6A-P004'
  RETURNING claim_id
)
INSERT INTO _m6_claim_map (tracker_id, claim_id) SELECT 'M6B-C006', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Subject-specific or tract-specific diffusion metrics relate to motor and sensory impairment after SCI.',
    'synthesis',
    'medium',
    'Abstract/PMC',
    'medium',
    '{"curator_notes": "Tract metric claim.", "source_paper_tracker_id": "M6A-P007, P022", "topic_id": "M6B-T003", "tracker_id": "M6B-C007"}'
  FROM _m6_paper_map p
  WHERE p.tracker_id = 'M6A-P007'
  RETURNING claim_id
)
INSERT INTO _m6_claim_map (tracker_id, claim_id) SELECT 'M6B-C007', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Tissue bridge and lesion-geometry metrics are clinically meaningful prognostic MRI biomarkers.',
    'synthesis',
    'high',
    'Abstract/PMC/source',
    'medium',
    '{"curator_notes": "Prognostic biomarker.", "source_paper_tracker_id": "M6A-P005, P008-P009, P035", "topic_id": "M6B-T004", "tracker_id": "M6B-C008"}'
  FROM _m6_paper_map p
  WHERE p.tracker_id = 'M6A-P005'
  RETURNING claim_id
)
INSERT INTO _m6_claim_map (tracker_id, claim_id) SELECT 'M6B-C008', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Tissue bridge interpretation should preserve level, timing, etiology, completeness, and endpoint boundaries.',
    'boundary condition',
    'high',
    'Module 6A tracker',
    'high',
    '{"curator_notes": "Prevents overgeneralization.", "source_paper_tracker_id": "M6A-P008-P009, P035", "topic_id": "M6B-T004", "tracker_id": "M6B-C009"}'
  FROM _m6_paper_map p
  WHERE p.tracker_id = 'M6A-P008'
  RETURNING claim_id
)
INSERT INTO _m6_claim_map (tracker_id, claim_id) SELECT 'M6B-C009', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'MRS can capture spinal or supraspinal metabolic changes related to impairment or clinical scores.',
    'synthesis',
    'medium',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Metabolic biomarkers.", "source_paper_tracker_id": "M6A-P010, P032", "topic_id": "M6B-T005", "tracker_id": "M6B-C010"}'
  FROM _m6_paper_map p
  WHERE p.tracker_id = 'M6A-P010'
  RETURNING claim_id
)
INSERT INTO _m6_claim_map (tracker_id, claim_id) SELECT 'M6B-C010', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'qMRI and longitudinal neuroimaging track remote degeneration and recovery predictors after SCI.',
    'synthesis',
    'medium',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Remote degeneration.", "source_paper_tracker_id": "M6A-P005, P011-P012, P016, P027-P031", "topic_id": "M6B-T005", "tracker_id": "M6B-C011"}'
  FROM _m6_paper_map p
  WHERE p.tracker_id = 'M6A-P005'
  RETURNING claim_id
)
INSERT INTO _m6_claim_map (tracker_id, claim_id) SELECT 'M6B-C011', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'CST and dorsal column degeneration can occur above the lesion over time.',
    'synthesis',
    'medium',
    'Abstract/PMC/source',
    'medium',
    '{"curator_notes": "Tract degeneration.", "source_paper_tracker_id": "M6A-P011, P016, P028, P031", "topic_id": "M6B-T005", "tracker_id": "M6B-C012"}'
  FROM _m6_paper_map p
  WHERE p.tracker_id = 'M6A-P011'
  RETURNING claim_id
)
INSERT INTO _m6_claim_map (tracker_id, claim_id) SELECT 'M6B-C012', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'fMRI and cortical reorganization studies indicate remote plasticity after SCI.',
    'synthesis',
    'medium',
    'Abstract/source page',
    'low',
    '{"curator_notes": "Indirect evidence.", "source_paper_tracker_id": "M6A-P013-P015, P024-P026", "topic_id": "M6B-T006", "tracker_id": "M6B-C013"}'
  FROM _m6_paper_map p
  WHERE p.tracker_id = 'M6A-P013'
  RETURNING claim_id
)
INSERT INTO _m6_claim_map (tracker_id, claim_id) SELECT 'M6B-C013', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Cortical reorganization claims should be linked to spinal lesion severity, tract integrity, or clinical impairment before consensus use.',
    'boundary condition',
    'high',
    'Module 6A tracker',
    'high',
    '{"curator_notes": "Brain-only caution.", "source_paper_tracker_id": "M6A-P013-P014, P023-P026", "topic_id": "M6B-T006", "tracker_id": "M6B-C014"}'
  FROM _m6_paper_map p
  WHERE p.tracker_id = 'M6A-P013'
  RETURNING claim_id
)
INSERT INTO _m6_claim_map (tracker_id, claim_id) SELECT 'M6B-C014', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Cord, sensory-system, and brain atrophy metrics are clinically relevant but indirect.',
    'synthesis',
    'medium',
    'Abstract/source page',
    'low',
    '{"curator_notes": "Full-text upgrade queue.", "source_paper_tracker_id": "M6A-P021, P023, P027-P028", "topic_id": "M6B-T005", "tracker_id": "M6B-C015"}'
  FROM _m6_paper_map p
  WHERE p.tracker_id = 'M6A-P021'
  RETURNING claim_id
)
INSERT INTO _m6_claim_map (tracker_id, claim_id) SELECT 'M6B-C015', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Imaging supports trial screening, endpoint selection, and stratification.',
    'synthesis',
    'medium',
    'Review/source',
    'medium',
    '{"curator_notes": "Trial readiness.", "source_paper_tracker_id": "M6A-P020, P036", "topic_id": "M6B-T007", "tracker_id": "M6B-C016"}'
  FROM _m6_paper_map p
  WHERE p.tracker_id = 'M6A-P020'
  RETURNING claim_id
)
INSERT INTO _m6_claim_map (tracker_id, claim_id) SELECT 'M6B-C016', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Pediatric, traumatic, ischemic, nontraumatic, complete, and incomplete SCI should not be collapsed without preserving cohort boundaries.',
    'boundary condition',
    'high',
    'Module 6A tracker',
    'high',
    '{"curator_notes": "Cohort ontology.", "source_paper_tracker_id": "M6A-P004, P008-P009, P029, P031-P035", "topic_id": "M6B-T008", "tracker_id": "M6B-C017"}'
  FROM _m6_paper_map p
  WHERE p.tracker_id = 'M6A-P004'
  RETURNING claim_id
)
INSERT INTO _m6_claim_map (tracker_id, claim_id) SELECT 'M6B-C017', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'MRI evidence and autopsy pathology are complementary but not interchangeable.',
    'boundary condition',
    'high',
    'Module 6A tracker',
    'high',
    '{"curator_notes": "Modality boundary.", "source_paper_tracker_id": "M6A-P001-P010, P017-P019", "topic_id": "M6B-T008", "tracker_id": "M6B-C018"}'
  FROM _m6_paper_map p
  WHERE p.tracker_id = 'M6A-P001'
  RETURNING claim_id
)
INSERT INTO _m6_claim_map (tracker_id, claim_id) SELECT 'M6B-C018', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'DTI, qMRI, MRS, and fMRI are indirect biomarkers that require modality-specific confidence labels.',
    'boundary condition',
    'high',
    'Module 6A tracker',
    'high',
    '{"curator_notes": "Interpretation boundary.", "source_paper_tracker_id": "M6A-P004, P006-P016, P021-P032", "topic_id": "M6B-T008", "tracker_id": "M6B-C019"}'
  FROM _m6_paper_map p
  WHERE p.tracker_id = 'M6A-P004'
  RETURNING claim_id
)
INSERT INTO _m6_claim_map (tracker_id, claim_id) SELECT 'M6B-C019', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Surgical reconstruction and trial screening anatomy are feasibility or stratification evidence unless linked to repair outcomes.',
    'boundary condition',
    'high',
    'Module 6A tracker',
    'high',
    '{"curator_notes": "Surgical/trial boundary.", "source_paper_tracker_id": "M6A-P003, P020, P036", "topic_id": "M6B-T007", "tracker_id": "M6B-C020"}'
  FROM _m6_paper_map p
  WHERE p.tracker_id = 'M6A-P003'
  RETURNING claim_id
)
INSERT INTO _m6_claim_map (tracker_id, claim_id) SELECT 'M6B-C020', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Review and method rows should guide interpretation but should not replace primary cohort extraction.',
    'boundary condition',
    'high',
    'Module 6A tracker',
    'high',
    '{"curator_notes": "Review-map boundary.", "source_paper_tracker_id": "M6A-P020, P029-P034, P036", "topic_id": "M6B-T007", "tracker_id": "M6B-C021"}'
  FROM _m6_paper_map p
  WHERE p.tracker_id = 'M6A-P020'
  RETURNING claim_id
)
INSERT INTO _m6_claim_map (tracker_id, claim_id) SELECT 'M6B-C021', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Human pathology and imaging evidence define translation constraints for animal and biomaterial modules.',
    'synthesis',
    'high',
    'Module 6A tracker',
    'high',
    '{"curator_notes": "Cross-module role.", "source_paper_tracker_id": "M6A-P001-P036", "topic_id": "M6B-T008", "tracker_id": "M6B-C022"}'
  FROM _m6_paper_map p
  WHERE p.tracker_id = 'M6A-P001'
  RETURNING claim_id
)
INSERT INTO _m6_claim_map (tracker_id, claim_id) SELECT 'M6B-C022', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Preserved human tissue and surgical scar-resection anatomy may support reconstruction feasibility but do not prove regenerative permissiveness.',
    'boundary condition',
    'high',
    'Module 6A tracker',
    'high',
    '{"curator_notes": "Feasibility versus mechanism.", "source_paper_tracker_id": "M6A-P001, P003", "topic_id": "M6B-T001", "tracker_id": "M6B-C023"}'
  FROM _m6_paper_map p
  WHERE p.tracker_id = 'M6A-P001'
  RETURNING claim_id
)
INSERT INTO _m6_claim_map (tracker_id, claim_id) SELECT 'M6B-C023', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Ventral-root and myelin pathology links Module 6 to remyelination/white-matter repair, but remains human pathology evidence rather than intervention evidence.',
    'boundary condition',
    'high',
    'Module 6A tracker',
    'high',
    '{"curator_notes": "Cross-module boundary.", "source_paper_tracker_id": "M6A-P002", "topic_id": "M6B-T002", "tracker_id": "M6B-C024"}'
  FROM _m6_paper_map p
  WHERE p.tracker_id = 'M6A-P002'
  RETURNING claim_id
)
INSERT INTO _m6_claim_map (tracker_id, claim_id) SELECT 'M6B-C024', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Vascular and syrinx pathology link lesion architecture to chronic secondary structural damage.',
    'synthesis',
    'medium',
    'M1A/abstract rows',
    'medium',
    '{"curator_notes": "Pathology architecture.", "source_paper_tracker_id": "M6A-P017-P019", "topic_id": "M6B-T002", "tracker_id": "M6B-C025"}'
  FROM _m6_paper_map p
  WHERE p.tracker_id = 'M6A-P017'
  RETURNING claim_id
)
INSERT INTO _m6_claim_map (tracker_id, claim_id) SELECT 'M6B-C025', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Remote motor-system and sensory-system degeneration should be treated as active chronic pathology rather than only downstream disability.',
    'synthesis',
    'medium',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Systems pathology.", "source_paper_tracker_id": "M6A-P005, P011-P012, P016, P027-P032", "topic_id": "M6B-T005", "tracker_id": "M6B-C026"}'
  FROM _m6_paper_map p
  WHERE p.tracker_id = 'M6A-P005'
  RETURNING claim_id
)
INSERT INTO _m6_claim_map (tracker_id, claim_id) SELECT 'M6B-C026', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Pediatric SCIWOMR highlights the limitation of conventional MRI for detecting clinically relevant cord pathology.',
    'conclusion',
    'medium',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Pediatric boundary.", "source_paper_tracker_id": "M6A-P004", "topic_id": "M6B-T003", "tracker_id": "M6B-C027"}'
  FROM _m6_paper_map p
  WHERE p.tracker_id = 'M6A-P004'
  RETURNING claim_id
)
INSERT INTO _m6_claim_map (tracker_id, claim_id) SELECT 'M6B-C027', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Lateral CST and tissue bridge metrics can support motor recovery stratification.',
    'synthesis',
    'medium',
    'Abstract/PMC/source',
    'medium',
    '{"curator_notes": "Tract plus lesion geometry.", "source_paper_tracker_id": "M6A-P008-P009, P022, P035", "topic_id": "M6B-T003", "tracker_id": "M6B-C028"}'
  FROM _m6_paper_map p
  WHERE p.tracker_id = 'M6A-P008'
  RETURNING claim_id
)
INSERT INTO _m6_claim_map (tracker_id, claim_id) SELECT 'M6B-C028', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Metabolic imaging adds nonstructural clinical readouts to human SCI pathology assessment.',
    'synthesis',
    'medium',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "MRS claim.", "source_paper_tracker_id": "M6A-P010, P032", "topic_id": "M6B-T005", "tracker_id": "M6B-C029"}'
  FROM _m6_paper_map p
  WHERE p.tracker_id = 'M6A-P010'
  RETURNING claim_id
)
INSERT INTO _m6_claim_map (tracker_id, claim_id) SELECT 'M6B-C029', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'fMRI activation findings are lower-directness evidence for lesion anatomy unless tied to spinal metrics or outcomes.',
    'boundary condition',
    'high',
    'Module 6A tracker',
    'high',
    '{"curator_notes": "Directness boundary.", "source_paper_tracker_id": "M6A-P015, P024-P026", "topic_id": "M6B-T006", "tracker_id": "M6B-C030"}'
  FROM _m6_paper_map p
  WHERE p.tracker_id = 'M6A-P015'
  RETURNING claim_id
)
INSERT INTO _m6_claim_map (tracker_id, claim_id) SELECT 'M6B-C030', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Clinical trial imaging should be used as screening and stratification evidence before being treated as mechanistic repair evidence.',
    'boundary condition',
    'high',
    'Review/map',
    'medium',
    '{"curator_notes": "Trial interpretation.", "source_paper_tracker_id": "M6A-P020, P033-P036", "topic_id": "M6B-T007", "tracker_id": "M6B-C031"}'
  FROM _m6_paper_map p
  WHERE p.tracker_id = 'M6A-P020'
  RETURNING claim_id
)
INSERT INTO _m6_claim_map (tracker_id, claim_id) SELECT 'M6B-C031', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Module 6 consensus should stratify by modality, timing, injury level, etiology, completeness, and confidence.',
    'synthesis',
    'high',
    'Module 6A tracker',
    'high',
    '{"curator_notes": "Ontology claim.", "source_paper_tracker_id": "M6A-P001-P036", "topic_id": "M6B-T008", "tracker_id": "M6B-C032"}'
  FROM _m6_paper_map p
  WHERE p.tracker_id = 'M6A-P001'
  RETURNING claim_id
)
INSERT INTO _m6_claim_map (tracker_id, claim_id) SELECT 'M6B-C032', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Low-confidence abstract/source-page rows require full-text upgrade before strong numeric or mechanistic claims.',
    'boundary condition',
    'high',
    'Module 6A tracker',
    'high',
    '{"curator_notes": "Evidence quality.", "source_paper_tracker_id": "M6A-P006-P036", "topic_id": "M6B-T008", "tracker_id": "M6B-C033"}'
  FROM _m6_paper_map p
  WHERE p.tracker_id = 'M6A-P006'
  RETURNING claim_id
)
INSERT INTO _m6_claim_map (tracker_id, claim_id) SELECT 'M6B-C033', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Chronic SCI imaging is not equivalent to histologic cell-state evidence.',
    'boundary condition',
    'high',
    'Module 6A tracker',
    'high',
    '{"curator_notes": "Imaging-to-cell-state caution.", "source_paper_tracker_id": "M6A-P004, P006-P016, P021-P032", "topic_id": "M6B-T008", "tracker_id": "M6B-C034"}'
  FROM _m6_paper_map p
  WHERE p.tracker_id = 'M6A-P004'
  RETURNING claim_id
)
INSERT INTO _m6_claim_map (tracker_id, claim_id) SELECT 'M6B-C034', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Human evidence can set translational boundaries for implant, graft, and reconstruction planning.',
    'synthesis',
    'high',
    'Module 6A tracker',
    'high',
    '{"curator_notes": "Cross-module translation.", "source_paper_tracker_id": "M6A-P001-P036", "topic_id": "M6B-T008", "tracker_id": "M6B-C035"}'
  FROM _m6_paper_map p
  WHERE p.tracker_id = 'M6A-P001'
  RETURNING claim_id
)
INSERT INTO _m6_claim_map (tracker_id, claim_id) SELECT 'M6B-C035', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Module 6B should preserve human evidence type and not mix animal imaging into human pathology consensus statements.',
    'boundary condition',
    'high',
    'Module 6A tracker',
    'high',
    '{"curator_notes": "Species boundary.", "source_paper_tracker_id": "M6A-P001-P036", "topic_id": "M6B-T008", "tracker_id": "M6B-C036"}'
  FROM _m6_paper_map p
  WHERE p.tracker_id = 'M6A-P001'
  RETURNING claim_id
)
INSERT INTO _m6_claim_map (tracker_id, claim_id) SELECT 'M6B-C036', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "MRI stereology preservation", "strength": "high", "tracker_id": "M6B-L001"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O001'
  WHERE c.tracker_id = 'M6B-C001'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L001', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Syrinx pathology", "strength": "medium", "tracker_id": "M6B-L002"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O018'
  WHERE c.tracker_id = 'M6B-C001'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L002', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Late syrinx precedent", "strength": "low", "tracker_id": "M6B-L003"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O019'
  WHERE c.tracker_id = 'M6B-C001'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L003', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Ventral-root pathology", "strength": "high", "tracker_id": "M6B-L004"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O002'
  WHERE c.tracker_id = 'M6B-C002'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L004', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Scar-resection anatomy", "strength": "high", "tracker_id": "M6B-L005"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O003'
  WHERE c.tracker_id = 'M6B-C003'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L005', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Vascular autopsy pathology", "strength": "high", "tracker_id": "M6B-L006"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O017'
  WHERE c.tracker_id = 'M6B-C004'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L006', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Syrinx autopsy row", "strength": "medium", "tracker_id": "M6B-L007"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O018'
  WHERE c.tracker_id = 'M6B-C005'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L007', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Late syrinx row", "strength": "low", "tracker_id": "M6B-L008"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O019'
  WHERE c.tracker_id = 'M6B-C005'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L008', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Pediatric DTI", "strength": "medium", "tracker_id": "M6B-L009"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O004'
  WHERE c.tracker_id = 'M6B-C006'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L009', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Chronic whole-cord DTI", "strength": "medium", "tracker_id": "M6B-L010"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O006'
  WHERE c.tracker_id = 'M6B-C006'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L010', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Subject-specific DTI", "strength": "medium", "tracker_id": "M6B-L011"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O007'
  WHERE c.tracker_id = 'M6B-C006'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L011', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Impairment association", "strength": "medium", "tracker_id": "M6B-L012"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O007'
  WHERE c.tracker_id = 'M6B-C007'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L012', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "CST motor output", "strength": "medium", "tracker_id": "M6B-L013"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O022'
  WHERE c.tracker_id = 'M6B-C007'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L013', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Longitudinal lesion/tissue bridge", "strength": "high", "tracker_id": "M6B-L014"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O005'
  WHERE c.tracker_id = 'M6B-C008'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L014', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Thoracic tissue bridge", "strength": "medium", "tracker_id": "M6B-L015"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O008'
  WHERE c.tracker_id = 'M6B-C008'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L015', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Cervical multicentre bridge", "strength": "medium", "tracker_id": "M6B-L016"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O009'
  WHERE c.tracker_id = 'M6B-C008'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L016', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Walking association", "strength": "medium", "tracker_id": "M6B-L017"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O035'
  WHERE c.tracker_id = 'M6B-C008'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L017', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Thoracic traumatic/ischemic", "strength": "medium", "tracker_id": "M6B-L018"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O008'
  WHERE c.tracker_id = 'M6B-C009'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L018', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cervical cohort", "strength": "medium", "tracker_id": "M6B-L019"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O009'
  WHERE c.tracker_id = 'M6B-C009'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L019', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Incomplete SCI walking", "strength": "medium", "tracker_id": "M6B-L020"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O035'
  WHERE c.tracker_id = 'M6B-C009'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L020', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Cervical cord MRS", "strength": "medium", "tracker_id": "M6B-L021"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O010'
  WHERE c.tracker_id = 'M6B-C010'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L021', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Supraspinal MRS", "strength": "medium", "tracker_id": "M6B-L022"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O032'
  WHERE c.tracker_id = 'M6B-C010'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L022', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Longitudinal qMRI", "strength": "high", "tracker_id": "M6B-L023"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O005'
  WHERE c.tracker_id = 'M6B-C011'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L023', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "CST/cortex degeneration", "strength": "low", "tracker_id": "M6B-L024"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O011'
  WHERE c.tracker_id = 'M6B-C011'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L024', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "qMRI recovery prediction", "strength": "medium", "tracker_id": "M6B-L025"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O012'
  WHERE c.tracker_id = 'M6B-C011'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L025', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Tract degeneration gradients", "strength": "medium", "tracker_id": "M6B-L026"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O016'
  WHERE c.tracker_id = 'M6B-C011'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L026', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Sensory atrophy", "strength": "low", "tracker_id": "M6B-L027"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O027'
  WHERE c.tracker_id = 'M6B-C011'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L027', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Above-lesion degeneration", "strength": "low", "tracker_id": "M6B-L028"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O028'
  WHERE c.tracker_id = 'M6B-C011'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L028', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Cranial CST degeneration", "strength": "low", "tracker_id": "M6B-L029"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O011'
  WHERE c.tracker_id = 'M6B-C012'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L029', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "CST/dorsal column gradients", "strength": "medium", "tracker_id": "M6B-L030"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O016'
  WHERE c.tracker_id = 'M6B-C012'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L030', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Dorsal column Wallerian degeneration", "strength": "medium", "tracker_id": "M6B-L031"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O031'
  WHERE c.tracker_id = 'M6B-C012'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L031', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Axonal integrity/cortical reorganization", "strength": "medium", "tracker_id": "M6B-L032"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O013'
  WHERE c.tracker_id = 'M6B-C013'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L032', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Atrophy and cortical reorganization", "strength": "medium", "tracker_id": "M6B-L033"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O014'
  WHERE c.tracker_id = 'M6B-C013'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L033', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Upper-limb representation", "strength": "low", "tracker_id": "M6B-L034"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O015'
  WHERE c.tracker_id = 'M6B-C013'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L034', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Recovery plasticity", "strength": "low", "tracker_id": "M6B-L035"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O024'
  WHERE c.tracker_id = 'M6B-C013'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L035', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Motor cortex plasticity", "strength": "low", "tracker_id": "M6B-L036"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O025'
  WHERE c.tracker_id = 'M6B-C013'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L036', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Motor activation/force", "strength": "low", "tracker_id": "M6B-L037"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O026'
  WHERE c.tracker_id = 'M6B-C013'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L037', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Has tract linkage", "strength": "medium", "tracker_id": "M6B-L038"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O013'
  WHERE c.tracker_id = 'M6B-C014'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L038', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Has disability linkage", "strength": "medium", "tracker_id": "M6B-L039"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O014'
  WHERE c.tracker_id = 'M6B-C014'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L039', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Brain-only atrophy caution", "strength": "low", "tracker_id": "M6B-L040"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O023'
  WHERE c.tracker_id = 'M6B-C014'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L040', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Cord atrophy deficits", "strength": "low", "tracker_id": "M6B-L041"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O021'
  WHERE c.tracker_id = 'M6B-C015'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L041', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Brain atrophy", "strength": "low", "tracker_id": "M6B-L042"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O023'
  WHERE c.tracker_id = 'M6B-C015'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L042', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Sensory atrophy", "strength": "low", "tracker_id": "M6B-L043"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O027'
  WHERE c.tracker_id = 'M6B-C015'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L043', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Neurodegeneration above lesion", "strength": "low", "tracker_id": "M6B-L044"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O028'
  WHERE c.tracker_id = 'M6B-C015'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L044', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "MRI trial framework", "strength": "medium", "tracker_id": "M6B-L045"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O020'
  WHERE c.tracker_id = 'M6B-C016'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L045', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Trial-readiness review", "strength": "low", "tracker_id": "M6B-L046"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O036'
  WHERE c.tracker_id = 'M6B-C016'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L046', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Pediatric SCIWOMR", "strength": "medium", "tracker_id": "M6B-L047"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O004'
  WHERE c.tracker_id = 'M6B-C017'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L047', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Traumatic/ischemic thoracic", "strength": "medium", "tracker_id": "M6B-L048"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O008'
  WHERE c.tracker_id = 'M6B-C017'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L048', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Complete SCI", "strength": "medium", "tracker_id": "M6B-L049"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O031'
  WHERE c.tracker_id = 'M6B-C017'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L049', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Incomplete SCI", "strength": "medium", "tracker_id": "M6B-L050"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O035'
  WHERE c.tracker_id = 'M6B-C017'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L050', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "MRI anatomy", "strength": "high", "tracker_id": "M6B-L051"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O001'
  WHERE c.tracker_id = 'M6B-C018'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L051', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Autopsy/ventral-root pathology", "strength": "high", "tracker_id": "M6B-L052"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O002'
  WHERE c.tracker_id = 'M6B-C018'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L052', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Autopsy vascular pathology", "strength": "high", "tracker_id": "M6B-L053"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O017'
  WHERE c.tracker_id = 'M6B-C018'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L053', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Syrinx autopsy pathology", "strength": "medium", "tracker_id": "M6B-L054"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O018'
  WHERE c.tracker_id = 'M6B-C018'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L054', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "DTI", "strength": "medium", "tracker_id": "M6B-L055"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O004'
  WHERE c.tracker_id = 'M6B-C019'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L055', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "MRS", "strength": "medium", "tracker_id": "M6B-L056"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O010'
  WHERE c.tracker_id = 'M6B-C019'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L056', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "qMRI", "strength": "medium", "tracker_id": "M6B-L057"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O012'
  WHERE c.tracker_id = 'M6B-C019'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L057', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "multimodal/fMRI", "strength": "medium", "tracker_id": "M6B-L058"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O013'
  WHERE c.tracker_id = 'M6B-C019'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L058', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Surgery feasibility", "strength": "high", "tracker_id": "M6B-L059"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O003'
  WHERE c.tracker_id = 'M6B-C020'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L059', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Trial framework", "strength": "medium", "tracker_id": "M6B-L060"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O020'
  WHERE c.tracker_id = 'M6B-C020'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L060', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Trial readiness", "strength": "low", "tracker_id": "M6B-L061"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O036'
  WHERE c.tracker_id = 'M6B-C020'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L061', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Review/map", "strength": "medium", "tracker_id": "M6B-L062"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O029'
  WHERE c.tracker_id = 'M6B-C021'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L062', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Methods/map", "strength": "medium", "tracker_id": "M6B-L063"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O030'
  WHERE c.tracker_id = 'M6B-C021'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L063', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Biomarker review", "strength": "medium", "tracker_id": "M6B-L064"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O033'
  WHERE c.tracker_id = 'M6B-C021'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L064', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Neuroimaging review", "strength": "medium", "tracker_id": "M6B-L065"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O034'
  WHERE c.tracker_id = 'M6B-C021'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L065', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Human preserved tissue", "strength": "high", "tracker_id": "M6B-L066"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O001'
  WHERE c.tracker_id = 'M6B-C022'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L066', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Human vascular pathology", "strength": "high", "tracker_id": "M6B-L067"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O017'
  WHERE c.tracker_id = 'M6B-C022'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L067', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Preserved tissue", "strength": "high", "tracker_id": "M6B-L068"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O001'
  WHERE c.tracker_id = 'M6B-C023'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L068', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Scar resection", "strength": "high", "tracker_id": "M6B-L069"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O003'
  WHERE c.tracker_id = 'M6B-C023'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L069', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Ventral root/myelin", "strength": "high", "tracker_id": "M6B-L070"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O002'
  WHERE c.tracker_id = 'M6B-C024'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L070', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Vascular pathology", "strength": "high", "tracker_id": "M6B-L071"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O017'
  WHERE c.tracker_id = 'M6B-C025'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L071', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Syrinx pathology", "strength": "medium", "tracker_id": "M6B-L072"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O018'
  WHERE c.tracker_id = 'M6B-C025'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L072', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Motor-system longitudinal", "strength": "high", "tracker_id": "M6B-L073"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O005'
  WHERE c.tracker_id = 'M6B-C026'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L073', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Major pathway degeneration", "strength": "medium", "tracker_id": "M6B-L074"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O016'
  WHERE c.tracker_id = 'M6B-C026'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L074', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Sensory system atrophy", "strength": "low", "tracker_id": "M6B-L075"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O027'
  WHERE c.tracker_id = 'M6B-C026'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L075', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Supraspinal metabolism", "strength": "medium", "tracker_id": "M6B-L076"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O032'
  WHERE c.tracker_id = 'M6B-C026'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L076', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Pediatric MRI-normal DTI abnormality", "strength": "medium", "tracker_id": "M6B-L077"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O004'
  WHERE c.tracker_id = 'M6B-C027'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L077', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Tissue bridge recovery", "strength": "medium", "tracker_id": "M6B-L078"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O008'
  WHERE c.tracker_id = 'M6B-C028'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L078', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Lateral CST motor output", "strength": "medium", "tracker_id": "M6B-L079"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O022'
  WHERE c.tracker_id = 'M6B-C028'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L079', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Walking bridge ratio", "strength": "medium", "tracker_id": "M6B-L080"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O035'
  WHERE c.tracker_id = 'M6B-C028'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L080', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Spinal MRS", "strength": "medium", "tracker_id": "M6B-L081"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O010'
  WHERE c.tracker_id = 'M6B-C029'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L081', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Supraspinal MRS", "strength": "medium", "tracker_id": "M6B-L082"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O032'
  WHERE c.tracker_id = 'M6B-C029'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L082', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "fMRI indirectness", "strength": "low", "tracker_id": "M6B-L083"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O015'
  WHERE c.tracker_id = 'M6B-C030'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L083', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Cortical plasticity", "strength": "low", "tracker_id": "M6B-L084"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O024'
  WHERE c.tracker_id = 'M6B-C030'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L084', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Activation/force", "strength": "low", "tracker_id": "M6B-L085"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O026'
  WHERE c.tracker_id = 'M6B-C030'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L085', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Clinical trial MRI", "strength": "medium", "tracker_id": "M6B-L086"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O020'
  WHERE c.tracker_id = 'M6B-C031'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L086', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Biomarker workup", "strength": "medium", "tracker_id": "M6B-L087"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O033'
  WHERE c.tracker_id = 'M6B-C031'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L087', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Trial readiness", "strength": "low", "tracker_id": "M6B-L088"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O036'
  WHERE c.tracker_id = 'M6B-C031'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L088', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "pediatric and DTI", "strength": "medium", "tracker_id": "M6B-L089"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O004'
  WHERE c.tracker_id = 'M6B-C032'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L089', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "level/etiology/timing", "strength": "medium", "tracker_id": "M6B-L090"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O008'
  WHERE c.tracker_id = 'M6B-C032'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L090', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "completeness", "strength": "medium", "tracker_id": "M6B-L091"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O031'
  WHERE c.tracker_id = 'M6B-C032'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L091', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "endpoint/incomplete SCI", "strength": "medium", "tracker_id": "M6B-L092"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O035'
  WHERE c.tracker_id = 'M6B-C032'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L092', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "abstract-level row", "strength": "low", "tracker_id": "M6B-L093"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O011'
  WHERE c.tracker_id = 'M6B-C033'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L093', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "abstract-level row", "strength": "low", "tracker_id": "M6B-L094"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O021'
  WHERE c.tracker_id = 'M6B-C033'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L094', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "abstract-level row", "strength": "low", "tracker_id": "M6B-L095"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O024'
  WHERE c.tracker_id = 'M6B-C033'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L095', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "abstract-level row", "strength": "low", "tracker_id": "M6B-L096"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O026'
  WHERE c.tracker_id = 'M6B-C033'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L096', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "diffusion metric caution", "strength": "medium", "tracker_id": "M6B-L097"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O006'
  WHERE c.tracker_id = 'M6B-C034'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L097', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "metabolite caution", "strength": "medium", "tracker_id": "M6B-L098"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O010'
  WHERE c.tracker_id = 'M6B-C034'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L098', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "qMRI methods boundary", "strength": "medium", "tracker_id": "M6B-L099"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O030'
  WHERE c.tracker_id = 'M6B-C034'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L099', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "human lesion architecture", "strength": "high", "tracker_id": "M6B-L100"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O001'
  WHERE c.tracker_id = 'M6B-C035'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L100', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "reconstructive anatomy", "strength": "high", "tracker_id": "M6B-L101"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O003'
  WHERE c.tracker_id = 'M6B-C035'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L101', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "prognostic stratification", "strength": "medium", "tracker_id": "M6B-L102"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O008'
  WHERE c.tracker_id = 'M6B-C035'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L102', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "human-only evidence", "strength": "high", "tracker_id": "M6B-L103"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O001'
  WHERE c.tracker_id = 'M6B-C036'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L103', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "human autopsy evidence", "strength": "high", "tracker_id": "M6B-L104"}'
  FROM _m6_claim_map c
  JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O017'
  WHERE c.tracker_id = 'M6B-C036'
  RETURNING link_id
)
INSERT INTO _m6_link_map (tracker_id, link_id) SELECT 'M6B-L104', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Human chronic SCI lesion architecture should be represented as separable compartments, including focal cystic loss, retained adjacent cord, scar-resection anatomy, syrinx or cyst complications, and potential tissue bridges, because each carries different surgical and translational implications.',
    'M6B-T001',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M6B-B001", "M6B-B005", "M6B-B008"], "claim_tracker_ids": ["M6B-C001", "M6B-C003", "M6B-C005", "M6B-C023"], "consensus_draft_id": "M6B-S001", "observation_tracker_ids": ["M6B-O001", "M6B-O003", "M6B-O018", "M6B-O019"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Architecture statement.", "topic_id": "M6B-T001"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m6_consensus_map (tracker_id, consensus_id) SELECT 'M6B-S001', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O001'
WHERE c.tracker_id = 'M6B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O003'
WHERE c.tracker_id = 'M6B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O018'
WHERE c.tracker_id = 'M6B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O019'
WHERE c.tracker_id = 'M6B-S001';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Human pathology adds tissue-level constraints that imaging alone cannot resolve: ventral-root and motoneuron loss, axon/myelin abnormalities, vascular injury patterns, cystic cavitation, and scar composition should remain separately queryable.',
    'M6B-T002',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M6B-B001", "M6B-B002"], "claim_tracker_ids": ["M6B-C002", "M6B-C004", "M6B-C018", "M6B-C024", "M6B-C025"], "consensus_draft_id": "M6B-S002", "observation_tracker_ids": ["M6B-O002", "M6B-O017", "M6B-O018"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Autopsy/pathology statement.", "topic_id": "M6B-T002"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m6_consensus_map (tracker_id, consensus_id) SELECT 'M6B-S002', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O002'
WHERE c.tracker_id = 'M6B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O017'
WHERE c.tracker_id = 'M6B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O018'
WHERE c.tracker_id = 'M6B-S002';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Diffusion MRI and tract-specific measures can reveal clinically relevant cord injury beyond conventional MRI, but consensus use requires tract, spinal level, directionality, clinical endpoint, acquisition method, and confidence labels.',
    'M6B-T003',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M6B-B002", "M6B-B003", "M6B-B006"], "claim_tracker_ids": ["M6B-C006", "M6B-C007", "M6B-C027", "M6B-C028"], "consensus_draft_id": "M6B-S003", "observation_tracker_ids": ["M6B-O004", "M6B-O006", "M6B-O007", "M6B-O022"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Diffusion/tract statement.", "topic_id": "M6B-T003"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m6_consensus_map (tracker_id, consensus_id) SELECT 'M6B-S003', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O004'
WHERE c.tracker_id = 'M6B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O006'
WHERE c.tracker_id = 'M6B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O007'
WHERE c.tracker_id = 'M6B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O022'
WHERE c.tracker_id = 'M6B-S003';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Tissue bridges and lesion-geometry measures are among the strongest human imaging candidates for prognosis and stratification, but their meaning depends on injury level, etiology, completeness, timing, scan modality, and the specific recovery endpoint.',
    'M6B-T004',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M6B-B001", "M6B-B006"], "claim_tracker_ids": ["M6B-C008", "M6B-C009", "M6B-C028", "M6B-C032"], "consensus_draft_id": "M6B-S004", "observation_tracker_ids": ["M6B-O005", "M6B-O008", "M6B-O009", "M6B-O035"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Tissue bridge statement.", "topic_id": "M6B-T004"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m6_consensus_map (tracker_id, consensus_id) SELECT 'M6B-S004', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O005'
WHERE c.tracker_id = 'M6B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O008'
WHERE c.tracker_id = 'M6B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O009'
WHERE c.tracker_id = 'M6B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O035'
WHERE c.tracker_id = 'M6B-S004';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'qMRI, MRS, atrophy, and longitudinal neuroimaging support chronic SCI as a system-level condition with remote spinal, sensory, motor, brainstem, cortical, and metabolic changes; these should be modeled as linked but distinct from local lesion-bed anatomy.',
    'M6B-T005',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M6B-B003", "M6B-B004", "M6B-B007"], "claim_tracker_ids": ["M6B-C010", "M6B-C011", "M6B-C012", "M6B-C015", "M6B-C026", "M6B-C029"], "consensus_draft_id": "M6B-S005", "observation_tracker_ids": ["M6B-O010", "M6B-O011", "M6B-O012", "M6B-O016", "M6B-O021", "M6B-O027", "M6B-O028", "M6B-O029", "M6B-O030", "M6B-O031", "M6B-O032"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Remote degeneration statement.", "topic_id": "M6B-T005"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m6_consensus_map (tracker_id, consensus_id) SELECT 'M6B-S005', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O010'
WHERE c.tracker_id = 'M6B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O011'
WHERE c.tracker_id = 'M6B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O012'
WHERE c.tracker_id = 'M6B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O016'
WHERE c.tracker_id = 'M6B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O021'
WHERE c.tracker_id = 'M6B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O027'
WHERE c.tracker_id = 'M6B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O028'
WHERE c.tracker_id = 'M6B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O029'
WHERE c.tracker_id = 'M6B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O030'
WHERE c.tracker_id = 'M6B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O031'
WHERE c.tracker_id = 'M6B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O032'
WHERE c.tracker_id = 'M6B-S005';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'fMRI and cortical reorganization evidence supports remote neural plasticity after SCI, but it should remain indirect lesion-bed evidence unless paired with spinal lesion metrics, tract integrity, or clinical impairment measures.',
    'M6B-T006',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M6B-B003", "M6B-B004"], "claim_tracker_ids": ["M6B-C013", "M6B-C014", "M6B-C030"], "consensus_draft_id": "M6B-S006", "observation_tracker_ids": ["M6B-O013", "M6B-O014", "M6B-O015", "M6B-O023", "M6B-O024", "M6B-O025", "M6B-O026"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Cortical plasticity statement.", "topic_id": "M6B-T006"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m6_consensus_map (tracker_id, consensus_id) SELECT 'M6B-S006', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O013'
WHERE c.tracker_id = 'M6B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O014'
WHERE c.tracker_id = 'M6B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O015'
WHERE c.tracker_id = 'M6B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O023'
WHERE c.tracker_id = 'M6B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O024'
WHERE c.tracker_id = 'M6B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O025'
WHERE c.tracker_id = 'M6B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O026'
WHERE c.tracker_id = 'M6B-S006';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Human imaging is ready to support surgical planning, trial screening, stratification, and endpoint selection, but registry, review, and trial-readiness rows should not be promoted to repair-efficacy evidence without intervention-linked outcomes.',
    'M6B-T007',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M6B-B005", "M6B-B007", "M6B-B008"], "claim_tracker_ids": ["M6B-C016", "M6B-C020", "M6B-C021", "M6B-C031"], "consensus_draft_id": "M6B-S007", "observation_tracker_ids": ["M6B-O003", "M6B-O020", "M6B-O029", "M6B-O033", "M6B-O034", "M6B-O035", "M6B-O036"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Translation/trial statement.", "topic_id": "M6B-T007"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m6_consensus_map (tracker_id, consensus_id) SELECT 'M6B-S007', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O003'
WHERE c.tracker_id = 'M6B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O020'
WHERE c.tracker_id = 'M6B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O029'
WHERE c.tracker_id = 'M6B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O033'
WHERE c.tracker_id = 'M6B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O034'
WHERE c.tracker_id = 'M6B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O035'
WHERE c.tracker_id = 'M6B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O036'
WHERE c.tracker_id = 'M6B-S007';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Module 6 should function as the human translation boundary layer: every consensus statement must preserve modality, confidence, timing, injury level, etiology, completeness, endpoint directness, and whether the evidence is pathology, imaging, planning, or efficacy.',
    'M6B-T008',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["all boundary records"], "claim_tracker_ids": ["M6B-C017", "M6B-C018", "M6B-C019", "M6B-C022", "M6B-C032", "M6B-C033", "M6B-C034", "M6B-C035", "M6B-C036"], "consensus_draft_id": "M6B-S008", "observation_tracker_ids": ["M6B-O001", "M6B-O002", "M6B-O003", "M6B-O004", "M6B-O005", "M6B-O006", "M6B-O007", "M6B-O008", "M6B-O009", "M6B-O010", "M6B-O011", "M6B-O012", "M6B-O013", "M6B-O014", "M6B-O015", "M6B-O016", "M6B-O017", "M6B-O018", "M6B-O019", "M6B-O020", "M6B-O021", "M6B-O022", "M6B-O023", "M6B-O024", "M6B-O025", "M6B-O026", "M6B-O027", "M6B-O028", "M6B-O029", "M6B-O030", "M6B-O031", "M6B-O032", "M6B-O033", "M6B-O034", "M6B-O035", "M6B-O036"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Cross-module guardrail.", "topic_id": "M6B-T008"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m6_consensus_map (tracker_id, consensus_id) SELECT 'M6B-S008', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O001'
WHERE c.tracker_id = 'M6B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O002'
WHERE c.tracker_id = 'M6B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O003'
WHERE c.tracker_id = 'M6B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O004'
WHERE c.tracker_id = 'M6B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O005'
WHERE c.tracker_id = 'M6B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O006'
WHERE c.tracker_id = 'M6B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O007'
WHERE c.tracker_id = 'M6B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O008'
WHERE c.tracker_id = 'M6B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O009'
WHERE c.tracker_id = 'M6B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O010'
WHERE c.tracker_id = 'M6B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O011'
WHERE c.tracker_id = 'M6B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O012'
WHERE c.tracker_id = 'M6B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O013'
WHERE c.tracker_id = 'M6B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O014'
WHERE c.tracker_id = 'M6B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O015'
WHERE c.tracker_id = 'M6B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O016'
WHERE c.tracker_id = 'M6B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O017'
WHERE c.tracker_id = 'M6B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O018'
WHERE c.tracker_id = 'M6B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O019'
WHERE c.tracker_id = 'M6B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O020'
WHERE c.tracker_id = 'M6B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O021'
WHERE c.tracker_id = 'M6B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O022'
WHERE c.tracker_id = 'M6B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O023'
WHERE c.tracker_id = 'M6B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O024'
WHERE c.tracker_id = 'M6B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O025'
WHERE c.tracker_id = 'M6B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O026'
WHERE c.tracker_id = 'M6B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O027'
WHERE c.tracker_id = 'M6B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O028'
WHERE c.tracker_id = 'M6B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O029'
WHERE c.tracker_id = 'M6B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O030'
WHERE c.tracker_id = 'M6B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O031'
WHERE c.tracker_id = 'M6B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O032'
WHERE c.tracker_id = 'M6B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O033'
WHERE c.tracker_id = 'M6B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O034'
WHERE c.tracker_id = 'M6B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O035'
WHERE c.tracker_id = 'M6B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m6_consensus_map c
JOIN _m6_observation_map o ON o.tracker_id = 'M6B-O036'
WHERE c.tracker_id = 'M6B-S008';

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
  SELECT COUNT(*) INTO paper_count FROM _m6_paper_map;
  SELECT COUNT(*) INTO experiment_count FROM _m6_experiment_map;
  SELECT COUNT(*) INTO observation_count FROM _m6_observation_map;
  SELECT COUNT(*) INTO claim_count FROM _m6_claim_map;
  SELECT COUNT(*) INTO link_count FROM _m6_link_map;
  SELECT COUNT(*) INTO consensus_count FROM _m6_consensus_map;
  SELECT COUNT(*) INTO consensus_observation_count
  FROM Consensus_Observation co
  JOIN _m6_consensus_map cm ON cm.consensus_id = co.consensus_id;
  IF paper_count <> 36 THEN RAISE EXCEPTION 'Expected 36 papers, found %', paper_count; END IF;
  IF experiment_count <> 36 THEN RAISE EXCEPTION 'Unexpected experiment count %', experiment_count; END IF;
  IF observation_count <> 36 THEN RAISE EXCEPTION 'Expected 36 observations, found %', observation_count; END IF;
  IF claim_count <> 36 THEN RAISE EXCEPTION 'Expected 36 claims, found %', claim_count; END IF;
  IF link_count <> 104 THEN RAISE EXCEPTION 'Expected 104 evidence links, found %', link_count; END IF;
  IF consensus_count <> 8 THEN RAISE EXCEPTION 'Expected 8 consensus rows, found %', consensus_count; END IF;
  IF consensus_observation_count <> 76 THEN RAISE EXCEPTION 'Unexpected consensus-observation count %', consensus_observation_count; END IF;
END $$;

COMMIT;
