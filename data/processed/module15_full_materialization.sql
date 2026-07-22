-- Module 15B full first-pass materialization generated from tracker-derived JSON.
-- This script is intended for a fresh database loaded with schema/schema.sql and scripts/seed_controlled_vocab.sql.
BEGIN;

CREATE TEMP TABLE _m15_paper_map (tracker_id TEXT PRIMARY KEY, paper_id INTEGER NOT NULL);
CREATE TEMP TABLE _m15_paradigm_map (tracker_id TEXT PRIMARY KEY, paradigm_id INTEGER NOT NULL);
CREATE TEMP TABLE _m15_experiment_map (tracker_id TEXT PRIMARY KEY, experiment_id INTEGER NOT NULL);
CREATE TEMP TABLE _m15_observation_map (tracker_id TEXT PRIMARY KEY, observation_id INTEGER NOT NULL);
CREATE TEMP TABLE _m15_claim_map (tracker_id TEXT PRIMARY KEY, claim_id INTEGER NOT NULL);
CREATE TEMP TABLE _m15_link_map (tracker_id TEXT PRIMARY KEY, link_id INTEGER NOT NULL);
CREATE TEMP TABLE _m15_consensus_map (tracker_id TEXT PRIMARY KEY, consensus_id INTEGER NOT NULL);

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Peripheral injury enhances central regeneration of primary sensory neurones', 'Richardson', 1984,
    'Nature', NULL, NULL,
    NULL, '10.1038/309791a0', '6204205',
    NULL, '{"curator_notes": "Foundational evidence that cutting peripheral axons increases spinal sensory axon regeneration into peripheral nerve grafts.", "module": "Module 15B", "tracker_id": "M15A-P001"}'
  )
  RETURNING paper_id
)
INSERT INTO _m15_paper_map (tracker_id, paper_id) SELECT 'M15A-P001', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'A conditioning lesion of the peripheral axons of dorsal root ganglion cells accelerates regeneration of only their peripheral axons', 'Oblinger', 1984,
    'Journal of Neuroscience', NULL, NULL,
    NULL, '10.1523/JNEUROSCI.04-07-01736.1984', '6204020',
    NULL, '{"curator_notes": "Early branch-specific boundary: peripheral conditioning accelerated peripheral but not dorsal-root central-branch regeneration in that assay.", "module": "Module 15B", "tracker_id": "M15A-P002"}'
  )
  RETURNING paper_id
)
INSERT INTO _m15_paper_map (tracker_id, paper_id) SELECT 'M15A-P002', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Regeneration of dorsal column fibers into and beyond the lesion site following adult spinal cord injury', 'Neumann', 1999,
    'Neuron', NULL, NULL,
    NULL, '10.1016/S0896-6273(00)80755-2', '10402195',
    NULL, '{"curator_notes": "Peripheral sciatic preconditioning 1-2 weeks before dorsal column lesion enabled growth into and beyond the SCI lesion.", "module": "Module 15B", "tracker_id": "M15A-P003"}'
  )
  RETURNING paper_id
)
INSERT INTO _m15_paper_map (tracker_id, paper_id) SELECT 'M15A-P003', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Sustaining intrinsic growth capacity of adult neurons promotes spinal cord regeneration', 'Neumann', 2005,
    'Proceedings of the National Academy of Sciences', NULL, NULL,
    NULL, '10.1073/pnas.0508538102', '16275900',
    NULL, '{"curator_notes": "Two priming lesions, at SCI and 1 week after SCI, sustained intrinsic growth capacity and promoted regeneration beyond lesion.", "module": "Module 15B", "tracker_id": "M15A-P004"}'
  )
  RETURNING paper_id
)
INSERT INTO _m15_paper_map (tracker_id, paper_id) SELECT 'M15A-P004', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Conditioning lesions before or after spinal cord injury recruit broad genetic mechanisms that sustain axonal regeneration: superiority to cAMP-mediated effects', 'Blesch', 2012,
    'Experimental Neurology', NULL, NULL,
    NULL, '10.1016/j.expneurol.2011.12.037', '22227059',
    NULL, '{"curator_notes": "Sciatic conditioning before or shortly after SCI outperformed cAMP and recruited broader, longer-lasting genetic mechanisms.", "module": "Module 15B", "tracker_id": "M15A-P005"}'
  )
  RETURNING paper_id
)
INSERT INTO _m15_paper_map (tracker_id, paper_id) SELECT 'M15A-P005', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Conditioning Injury-Induced Spinal Axon Regeneration Requires Signal Transducer and Activator of Transcription 3 Activation', 'Qiu', 2005,
    'Journal of Neuroscience', NULL, NULL,
    NULL, '10.1523/JNEUROSCI.4427-04.2005', '15716400',
    NULL, '{"curator_notes": "Sciatic transection activated STAT3 in DRG neurons; JAK2 inhibitor reduced GAP-43, neurite outgrowth, and dorsal column regeneration.", "module": "Module 15B", "tracker_id": "M15A-P006"}'
  )
  RETURNING paper_id
)
INSERT INTO _m15_paper_map (tracker_id, paper_id) SELECT 'M15A-P006', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Conditioning injury-induced spinal axon regeneration fails in interleukin-6 knock-out mice', 'Cao', 2004,
    'Journal of Neuroscience', NULL, NULL,
    NULL, '10.1523/JNEUROSCI.2245-04.2004', '15128857',
    NULL, '{"curator_notes": "IL-6 required for conditioning-induced GAP-43 upregulation and dorsal column regeneration after sciatic preconditioning.", "module": "Module 15B", "tracker_id": "M15A-P007"}'
  )
  RETURNING paper_id
)
INSERT INTO _m15_paper_map (tracker_id, paper_id) SELECT 'M15A-P007', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'A role for cAMP in regeneration of the adult mammalian CNS', 'Qiu', 2002,
    'Neuron / review-context PMC record', NULL, NULL,
    NULL, NULL, 'PMC1571233',
    NULL, '{"curator_notes": "cAMP elevation in DRG can mimic part of conditioning lesion effect, but later rows show conditioning recruits broader mechanisms.", "module": "Module 15B", "tracker_id": "M15A-P008"}'
  )
  RETURNING paper_id
)
INSERT INTO _m15_paper_map (tracker_id, paper_id) SELECT 'M15A-P008', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'A transcription-dependent switch controls competence of adult neurons for distinct modes of axon growth', 'Smith', 1997,
    'Journal of Neuroscience', NULL, NULL,
    NULL, '10.1523/JNEUROSCI.17-02-00646.1997', '8987787',
    NULL, '{"curator_notes": "Adult DRG growth competence depends on transcriptional state and supports intrinsic-growth switch logic.", "module": "Module 15B", "tracker_id": "M15A-P009"}'
  )
  RETURNING paper_id
)
INSERT INTO _m15_paper_map (tracker_id, paper_id) SELECT 'M15A-P009', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Mechanisms of enhancement of neurite regeneration in vitro following a conditioning sciatic nerve lesion', 'Smith', 1998,
    'Journal of Comparative Neurology', NULL, NULL,
    NULL, NULL, '9527536',
    NULL, '{"curator_notes": "Conditioning lesion changes neurite initiation, outgrowth rate, and branching in cultured adult DRG neurons.", "module": "Module 15B", "tracker_id": "M15A-P010"}'
  )
  RETURNING paper_id
)
INSERT INTO _m15_paper_map (tracker_id, paper_id) SELECT 'M15A-P010', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'A Conditioning Sciatic Nerve Lesion Triggers a Pro-regenerative State in Primary Sensory Neurons Also of Dorsal Root Ganglia Non-associated With the Damaged Nerve', 'Dubovy', 2019,
    'Frontiers in Cellular Neuroscience', NULL, NULL,
    NULL, '10.3389/fncel.2019.00011', '30778286',
    NULL, '{"curator_notes": "Unilateral sciatic nerve injury induced bilateral/remote DRG GAP-43 and SCG10 changes and increased later regeneration capacity in non-associated DRGs.", "module": "Module 15B", "tracker_id": "M15A-P011"}'
  )
  RETURNING paper_id
)
INSERT INTO _m15_paper_map (tracker_id, paper_id) SELECT 'M15A-P011', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Enriched conditioning expands the regenerative ability of sensory neurons after spinal cord injury via neuronal intrinsic redox signaling', 'Pita-Thomas', 2021,
    'Nature Communications', NULL, NULL,
    NULL, '10.1038/s41467-020-20112-4', '33349630',
    NULL, '{"curator_notes": "Environmental enrichment plus sciatic conditioning activates PKC-STAT3-NOX2 redox signaling and drives axons beyond SCI lesion.", "module": "Module 15B", "tracker_id": "M15A-P012"}'
  )
  RETURNING paper_id
)
INSERT INTO _m15_paper_map (tracker_id, paper_id) SELECT 'M15A-P012', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Contribution of macrophages to enhanced regenerative capacity of dorsal root ganglia sensory neurons by conditioning injury', 'Kwon', 2013,
    'Journal of Neuroscience', NULL, NULL,
    NULL, '10.1523/JNEUROSCI.0448-13.2013', '24048840',
    NULL, '{"curator_notes": "DRG macrophages and inflammatory mediators, including oncomodulin, contribute to maintenance of conditioning-induced regeneration capacity.", "module": "Module 15B", "tracker_id": "M15A-P013"}'
  )
  RETURNING paper_id
)
INSERT INTO _m15_paper_map (tracker_id, paper_id) SELECT 'M15A-P013', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Spinal Glia Division Contributes to Conditioning Lesion-Induced Axon Regeneration Into the Injured Spinal Cord', 'Zhao', 2015,
    'Journal of Neuropathology and Experimental Neurology', NULL, NULL,
    NULL, '10.1097/NEN.0000000000000192', '25933310',
    NULL, '{"curator_notes": "Conditioning sciatic nerve crush induced spinal glia division/TIMP-1-related effects contributing to central sensory axon growth.", "module": "Module 15B", "tracker_id": "M15A-P014"}'
  )
  RETURNING paper_id
)
INSERT INTO _m15_paper_map (tracker_id, paper_id) SELECT 'M15A-P014', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'The Dorsal Column Lesion Model of Spinal Cord Injury and Its Use in Deciphering the Neuron-Intrinsic Injury Response', 'Bradke', 2018,
    'Methods in Molecular Biology', NULL, NULL,
    NULL, '10.1007/978-1-4939-7649-2_13', '29717546',
    NULL, '{"curator_notes": "Review/protocol anchor for DRG neurons as a model of peripheral versus central branch intrinsic injury response.", "module": "Module 15B", "tracker_id": "M15A-P015"}'
  )
  RETURNING paper_id
)
INSERT INTO _m15_paper_map (tracker_id, paper_id) SELECT 'M15A-P015', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'CNS regeneration: only on one condition', 'Silver', 2009,
    'Current Biology', NULL, NULL,
    NULL, '10.1016/j.cub.2009.04.026', '19515349',
    NULL, '{"curator_notes": "Commentary/review anchor emphasizing conditioning lesion paradigm and reversed lesion-order evidence boundary.", "module": "Module 15B", "tracker_id": "M15A-P016"}'
  )
  RETURNING paper_id
)
INSERT INTO _m15_paper_map (tracker_id, paper_id) SELECT 'M15A-P016', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 15B curated evidence extraction',
    'First-pass Module 15B peripheral nerve and DRG priming of CNS repair curation for M15A-P001',
    'Tracker-derived materialization from Module_15B_TRACKER.md'
  FROM _m15_paper_map WHERE tracker_id = 'M15A-P001'
  RETURNING paradigm_id
)
INSERT INTO _m15_paradigm_map (tracker_id, paradigm_id) SELECT 'M15A-P001', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 15B curated evidence extraction',
    'First-pass Module 15B peripheral nerve and DRG priming of CNS repair curation for M15A-P002',
    'Tracker-derived materialization from Module_15B_TRACKER.md'
  FROM _m15_paper_map WHERE tracker_id = 'M15A-P002'
  RETURNING paradigm_id
)
INSERT INTO _m15_paradigm_map (tracker_id, paradigm_id) SELECT 'M15A-P002', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 15B curated evidence extraction',
    'First-pass Module 15B peripheral nerve and DRG priming of CNS repair curation for M15A-P003',
    'Tracker-derived materialization from Module_15B_TRACKER.md'
  FROM _m15_paper_map WHERE tracker_id = 'M15A-P003'
  RETURNING paradigm_id
)
INSERT INTO _m15_paradigm_map (tracker_id, paradigm_id) SELECT 'M15A-P003', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 15B curated evidence extraction',
    'First-pass Module 15B peripheral nerve and DRG priming of CNS repair curation for M15A-P004',
    'Tracker-derived materialization from Module_15B_TRACKER.md'
  FROM _m15_paper_map WHERE tracker_id = 'M15A-P004'
  RETURNING paradigm_id
)
INSERT INTO _m15_paradigm_map (tracker_id, paradigm_id) SELECT 'M15A-P004', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 15B curated evidence extraction',
    'First-pass Module 15B peripheral nerve and DRG priming of CNS repair curation for M15A-P005',
    'Tracker-derived materialization from Module_15B_TRACKER.md'
  FROM _m15_paper_map WHERE tracker_id = 'M15A-P005'
  RETURNING paradigm_id
)
INSERT INTO _m15_paradigm_map (tracker_id, paradigm_id) SELECT 'M15A-P005', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 15B curated evidence extraction',
    'First-pass Module 15B peripheral nerve and DRG priming of CNS repair curation for M15A-P006',
    'Tracker-derived materialization from Module_15B_TRACKER.md'
  FROM _m15_paper_map WHERE tracker_id = 'M15A-P006'
  RETURNING paradigm_id
)
INSERT INTO _m15_paradigm_map (tracker_id, paradigm_id) SELECT 'M15A-P006', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 15B curated evidence extraction',
    'First-pass Module 15B peripheral nerve and DRG priming of CNS repair curation for M15A-P007',
    'Tracker-derived materialization from Module_15B_TRACKER.md'
  FROM _m15_paper_map WHERE tracker_id = 'M15A-P007'
  RETURNING paradigm_id
)
INSERT INTO _m15_paradigm_map (tracker_id, paradigm_id) SELECT 'M15A-P007', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 15B curated evidence extraction',
    'First-pass Module 15B peripheral nerve and DRG priming of CNS repair curation for M15A-P008',
    'Tracker-derived materialization from Module_15B_TRACKER.md'
  FROM _m15_paper_map WHERE tracker_id = 'M15A-P008'
  RETURNING paradigm_id
)
INSERT INTO _m15_paradigm_map (tracker_id, paradigm_id) SELECT 'M15A-P008', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 15B curated evidence extraction',
    'First-pass Module 15B peripheral nerve and DRG priming of CNS repair curation for M15A-P009',
    'Tracker-derived materialization from Module_15B_TRACKER.md'
  FROM _m15_paper_map WHERE tracker_id = 'M15A-P009'
  RETURNING paradigm_id
)
INSERT INTO _m15_paradigm_map (tracker_id, paradigm_id) SELECT 'M15A-P009', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 15B curated evidence extraction',
    'First-pass Module 15B peripheral nerve and DRG priming of CNS repair curation for M15A-P010',
    'Tracker-derived materialization from Module_15B_TRACKER.md'
  FROM _m15_paper_map WHERE tracker_id = 'M15A-P010'
  RETURNING paradigm_id
)
INSERT INTO _m15_paradigm_map (tracker_id, paradigm_id) SELECT 'M15A-P010', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 15B curated evidence extraction',
    'First-pass Module 15B peripheral nerve and DRG priming of CNS repair curation for M15A-P011',
    'Tracker-derived materialization from Module_15B_TRACKER.md'
  FROM _m15_paper_map WHERE tracker_id = 'M15A-P011'
  RETURNING paradigm_id
)
INSERT INTO _m15_paradigm_map (tracker_id, paradigm_id) SELECT 'M15A-P011', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 15B curated evidence extraction',
    'First-pass Module 15B peripheral nerve and DRG priming of CNS repair curation for M15A-P012',
    'Tracker-derived materialization from Module_15B_TRACKER.md'
  FROM _m15_paper_map WHERE tracker_id = 'M15A-P012'
  RETURNING paradigm_id
)
INSERT INTO _m15_paradigm_map (tracker_id, paradigm_id) SELECT 'M15A-P012', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 15B curated evidence extraction',
    'First-pass Module 15B peripheral nerve and DRG priming of CNS repair curation for M15A-P013',
    'Tracker-derived materialization from Module_15B_TRACKER.md'
  FROM _m15_paper_map WHERE tracker_id = 'M15A-P013'
  RETURNING paradigm_id
)
INSERT INTO _m15_paradigm_map (tracker_id, paradigm_id) SELECT 'M15A-P013', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 15B curated evidence extraction',
    'First-pass Module 15B peripheral nerve and DRG priming of CNS repair curation for M15A-P014',
    'Tracker-derived materialization from Module_15B_TRACKER.md'
  FROM _m15_paper_map WHERE tracker_id = 'M15A-P014'
  RETURNING paradigm_id
)
INSERT INTO _m15_paradigm_map (tracker_id, paradigm_id) SELECT 'M15A-P014', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 15B curated evidence extraction',
    'First-pass Module 15B peripheral nerve and DRG priming of CNS repair curation for M15A-P015',
    'Tracker-derived materialization from Module_15B_TRACKER.md'
  FROM _m15_paper_map WHERE tracker_id = 'M15A-P015'
  RETURNING paradigm_id
)
INSERT INTO _m15_paradigm_map (tracker_id, paradigm_id) SELECT 'M15A-P015', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 15B curated evidence extraction',
    'First-pass Module 15B peripheral nerve and DRG priming of CNS repair curation for M15A-P016',
    'Tracker-derived materialization from Module_15B_TRACKER.md'
  FROM _m15_paper_map WHERE tracker_id = 'M15A-P016'
  RETURNING paradigm_id
)
INSERT INTO _m15_paradigm_map (tracker_id, paradigm_id) SELECT 'M15A-P016', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M15A-P001-E001',
    'Module 15B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M15B-O001"], "source_experiment_tracker_id": "M15A-P001-E001", "source_paper_tracker_id": "M15A-P001", "tracker_key": "M15A-P001::M15A-P001-E001"}'
  FROM _m15_paper_map p
  JOIN _m15_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M15A-P001'
  RETURNING experiment_id
)
INSERT INTO _m15_experiment_map (tracker_id, experiment_id) SELECT 'M15A-P001::M15A-P001-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Full-text PMC',
    'Tracker experiment M15A-P002-E001',
    'Module 15B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M15B-O002"], "source_experiment_tracker_id": "M15A-P002-E001", "source_paper_tracker_id": "M15A-P002", "tracker_key": "M15A-P002::M15A-P002-E001"}'
  FROM _m15_paper_map p
  JOIN _m15_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M15A-P002'
  RETURNING experiment_id
)
INSERT INTO _m15_experiment_map (tracker_id, experiment_id) SELECT 'M15A-P002::M15A-P002-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M15A-P003-E001',
    'Module 15B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M15B-O003"], "source_experiment_tracker_id": "M15A-P003-E001", "source_paper_tracker_id": "M15A-P003", "tracker_key": "M15A-P003::M15A-P003-E001"}'
  FROM _m15_paper_map p
  JOIN _m15_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M15A-P003'
  RETURNING experiment_id
)
INSERT INTO _m15_experiment_map (tracker_id, experiment_id) SELECT 'M15A-P003::M15A-P003-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Full-text PMC',
    'Tracker experiment M15A-P004-E001',
    'Module 15B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M15B-O004"], "source_experiment_tracker_id": "M15A-P004-E001", "source_paper_tracker_id": "M15A-P004", "tracker_key": "M15A-P004::M15A-P004-E001"}'
  FROM _m15_paper_map p
  JOIN _m15_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M15A-P004'
  RETURNING experiment_id
)
INSERT INTO _m15_experiment_map (tracker_id, experiment_id) SELECT 'M15A-P004::M15A-P004-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Full-text PMC',
    'Tracker experiment M15A-P005-E001',
    'Module 15B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M15B-O005"], "source_experiment_tracker_id": "M15A-P005-E001", "source_paper_tracker_id": "M15A-P005", "tracker_key": "M15A-P005::M15A-P005-E001"}'
  FROM _m15_paper_map p
  JOIN _m15_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M15A-P005'
  RETURNING experiment_id
)
INSERT INTO _m15_experiment_map (tracker_id, experiment_id) SELECT 'M15A-P005::M15A-P005-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Full-text PMC',
    'Tracker experiment M15A-P006-E001',
    'Module 15B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M15B-O006"], "source_experiment_tracker_id": "M15A-P006-E001", "source_paper_tracker_id": "M15A-P006", "tracker_key": "M15A-P006::M15A-P006-E001"}'
  FROM _m15_paper_map p
  JOIN _m15_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M15A-P006'
  RETURNING experiment_id
)
INSERT INTO _m15_experiment_map (tracker_id, experiment_id) SELECT 'M15A-P006::M15A-P006-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M15A-P007-E001',
    'Module 15B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M15B-O007"], "source_experiment_tracker_id": "M15A-P007-E001", "source_paper_tracker_id": "M15A-P007", "tracker_key": "M15A-P007::M15A-P007-E001"}'
  FROM _m15_paper_map p
  JOIN _m15_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M15A-P007'
  RETURNING experiment_id
)
INSERT INTO _m15_experiment_map (tracker_id, experiment_id) SELECT 'M15A-P007::M15A-P007-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Full-text PMC',
    'Tracker experiment M15A-P008-E001',
    'Module 15B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M15B-O008"], "source_experiment_tracker_id": "M15A-P008-E001", "source_paper_tracker_id": "M15A-P008", "tracker_key": "M15A-P008::M15A-P008-E001"}'
  FROM _m15_paper_map p
  JOIN _m15_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M15A-P008'
  RETURNING experiment_id
)
INSERT INTO _m15_experiment_map (tracker_id, experiment_id) SELECT 'M15A-P008::M15A-P008-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Full-text PMC',
    'Tracker experiment M15A-P009-E001',
    'Module 15B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M15B-O009"], "source_experiment_tracker_id": "M15A-P009-E001", "source_paper_tracker_id": "M15A-P009", "tracker_key": "M15A-P009::M15A-P009-E001"}'
  FROM _m15_paper_map p
  JOIN _m15_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M15A-P009'
  RETURNING experiment_id
)
INSERT INTO _m15_experiment_map (tracker_id, experiment_id) SELECT 'M15A-P009::M15A-P009-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M15A-P010-E001',
    'Module 15B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M15B-O010"], "source_experiment_tracker_id": "M15A-P010-E001", "source_paper_tracker_id": "M15A-P010", "tracker_key": "M15A-P010::M15A-P010-E001"}'
  FROM _m15_paper_map p
  JOIN _m15_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M15A-P010'
  RETURNING experiment_id
)
INSERT INTO _m15_experiment_map (tracker_id, experiment_id) SELECT 'M15A-P010::M15A-P010-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Full-text PMC',
    'Tracker experiment M15A-P011-E001',
    'Module 15B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M15B-O011"], "source_experiment_tracker_id": "M15A-P011-E001", "source_paper_tracker_id": "M15A-P011", "tracker_key": "M15A-P011::M15A-P011-E001"}'
  FROM _m15_paper_map p
  JOIN _m15_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M15A-P011'
  RETURNING experiment_id
)
INSERT INTO _m15_experiment_map (tracker_id, experiment_id) SELECT 'M15A-P011::M15A-P011-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M15A-P012-E001',
    'Module 15B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M15B-O012"], "source_experiment_tracker_id": "M15A-P012-E001", "source_paper_tracker_id": "M15A-P012", "tracker_key": "M15A-P012::M15A-P012-E001"}'
  FROM _m15_paper_map p
  JOIN _m15_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M15A-P012'
  RETURNING experiment_id
)
INSERT INTO _m15_experiment_map (tracker_id, experiment_id) SELECT 'M15A-P012::M15A-P012-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M15A-P013-E001',
    'Module 15B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M15B-O013"], "source_experiment_tracker_id": "M15A-P013-E001", "source_paper_tracker_id": "M15A-P013", "tracker_key": "M15A-P013::M15A-P013-E001"}'
  FROM _m15_paper_map p
  JOIN _m15_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M15A-P013'
  RETURNING experiment_id
)
INSERT INTO _m15_experiment_map (tracker_id, experiment_id) SELECT 'M15A-P013::M15A-P013-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M15A-P014-E001',
    'Module 15B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M15B-O014"], "source_experiment_tracker_id": "M15A-P014-E001", "source_paper_tracker_id": "M15A-P014", "tracker_key": "M15A-P014::M15A-P014-E001"}'
  FROM _m15_paper_map p
  JOIN _m15_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M15A-P014'
  RETURNING experiment_id
)
INSERT INTO _m15_experiment_map (tracker_id, experiment_id) SELECT 'M15A-P014::M15A-P014-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M15A-P015-E001',
    'Module 15B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M15B-O015"], "source_experiment_tracker_id": "M15A-P015-E001", "source_paper_tracker_id": "M15A-P015", "tracker_key": "M15A-P015::M15A-P015-E001"}'
  FROM _m15_paper_map p
  JOIN _m15_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M15A-P015'
  RETURNING experiment_id
)
INSERT INTO _m15_experiment_map (tracker_id, experiment_id) SELECT 'M15A-P015::M15A-P015-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Full-text PMC',
    'Tracker experiment M15A-P016-E001',
    'Module 15B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M15B-O016"], "source_experiment_tracker_id": "M15A-P016-E001", "source_paper_tracker_id": "M15A-P016", "tracker_key": "M15A-P016::M15A-P016-E001"}'
  FROM _m15_paper_map p
  JOIN _m15_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M15A-P016'
  RETURNING experiment_id
)
INSERT INTO _m15_experiment_map (tracker_id, experiment_id) SELECT 'M15A-P016::M15A-P016-E001', experiment_id FROM inserted;

INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('DRG culture conditioning evidence', 'Module 15B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('DRG macrophage evidence', 'Module 15B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('IL-6 pathway evidence', 'Module 15B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('STAT3 pathway evidence', 'Module 15B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('branch-specific conditioning evidence', 'Module 15B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('cAMP mimicry evidence', 'Module 15B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('conditioning paradigm review evidence', 'Module 15B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('conditioning versus cAMP evidence', 'Module 15B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('dorsal column model evidence', 'Module 15B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('dorsal column regeneration evidence', 'Module 15B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('enriched conditioning evidence', 'Module 15B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('peripheral conditioning evidence', 'Module 15B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('remote DRG priming evidence', 'Module 15B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('repeated priming evidence', 'Module 15B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('spinal glia support evidence', 'Module 15B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('transcriptional switch evidence', 'Module 15B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;

INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('DRG growth competence and dorsal column regeneration', 'Module 15B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('GAP-43 and dorsal column regeneration', 'Module 15B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('axon growth competence', 'Module 15B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('central axon regeneration', 'Module 15B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('central axon regeneration beyond lesion', 'Module 15B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('central axon regeneration boundary', 'Module 15B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('central sensory axon regeneration', 'Module 15B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('contralateral/remote regenerative state', 'Module 15B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('genetic program duration and central regeneration', 'Module 15B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('intrinsic injury response model', 'Module 15B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('maintenance of regenerative capacity', 'Module 15B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('neurite initiation, outgrowth, and branching', 'Module 15B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('peripheral versus central branch regeneration', 'Module 15B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('redox signaling and regeneration after SCI', 'Module 15B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('sensory axon growth into injured spinal cord', 'Module 15B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('sustained intrinsic growth capacity', 'Module 15B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Peripheral axon injury made long spinal primary sensory axons far more likely to regenerate into peripheral nerve grafts, implicating inducible neuronal events.',
    'qualitative',
    NULL,
    'Peripheral axon injury made long spinal primary sensory axons far more likely to regenerate into peripheral nerve grafts, implicating inducible neuronal events.',
    'peripheral injury enhances central sensory axon regeneration',
    'Module 15A tracker / source-page, full-text PMC, or review metadata',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Foundational conditioning lesion row.", "experiment_tracker_id": "M15A-P001-E001", "measurement_method_inference": null, "paper_tracker_id": "M15A-P001", "quantitative": "YES", "statistics_reported": "Source-page reports approximately 100-fold likelihood increase", "topic_id": "M15B-T001", "tracker_id": "M15B-O001"}'
  FROM _m15_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M15A-P001::M15A-P001-E001'
    AND et.evidence_type_name = 'peripheral conditioning evidence'
    AND ot.outcome_type_name = 'central sensory axon regeneration'
  RETURNING observation_id
)
INSERT INTO _m15_observation_map (tracker_id, observation_id) SELECT 'M15B-O001', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Conditioning accelerated peripheral branch regeneration but did not significantly accelerate dorsal-root central branch regeneration in this assay.',
    'qualitative',
    NULL,
    'Conditioning accelerated peripheral branch regeneration but did not significantly accelerate dorsal-root central branch regeneration in this assay.',
    'branch-specific conditioning effect',
    'Module 15A tracker / source-page, full-text PMC, or review metadata',
    'Full-text PMC',
    'high',
    '{"curator_notes": "Important negative/boundary row.", "experiment_tracker_id": "M15A-P002-E001", "measurement_method_inference": null, "paper_tracker_id": "M15A-P002", "quantitative": "YES", "statistics_reported": "Peripheral branch rate increased from 4.4 to 5.5 mm/day; dorsal-root central branch not significantly affected", "topic_id": "M15B-T007", "tracker_id": "M15B-O002"}'
  FROM _m15_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M15A-P002::M15A-P002-E001'
    AND et.evidence_type_name = 'branch-specific conditioning evidence'
    AND ot.outcome_type_name = 'peripheral versus central branch regeneration'
  RETURNING observation_id
)
INSERT INTO _m15_observation_map (tracker_id, observation_id) SELECT 'M15B-O002', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Preconditioning 1-2 weeks before dorsal column injury increased central axon growth into spinal cord above the lesion.',
    'qualitative',
    NULL,
    'Preconditioning 1-2 weeks before dorsal column injury increased central axon growth into spinal cord above the lesion.',
    'preconditioning enables dorsal column growth beyond lesion',
    'Module 15A tracker / source-page, full-text PMC, or review metadata',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Timing-sensitive positive row.", "experiment_tracker_id": "M15A-P003-E001", "measurement_method_inference": null, "paper_tracker_id": "M15A-P003", "quantitative": "NO", "statistics_reported": "Source-page first pass; exact fiber counts not extracted", "topic_id": "M15B-T001", "tracker_id": "M15B-O003"}'
  FROM _m15_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M15A-P003::M15A-P003-E001'
    AND et.evidence_type_name = 'dorsal column regeneration evidence'
    AND ot.outcome_type_name = 'central axon regeneration beyond lesion'
  RETURNING observation_id
)
INSERT INTO _m15_observation_map (tracker_id, observation_id) SELECT 'M15B-O003', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Two priming lesions sustained intrinsic growth capacity and promoted regeneration within and beyond spinal lesion after SCI.',
    'qualitative',
    NULL,
    'Two priming lesions sustained intrinsic growth capacity and promoted regeneration within and beyond spinal lesion after SCI.',
    'repeated priming sustains regeneration after SCI',
    'Module 15A tracker / source-page, full-text PMC, or review metadata',
    'Full-text PMC',
    'high',
    '{"curator_notes": "Clinically relevant post-SCI timing row.", "experiment_tracker_id": "M15A-P004-E001", "measurement_method_inference": null, "paper_tracker_id": "M15A-P004", "quantitative": "NO", "statistics_reported": "Full-text first pass; exact regeneration distances not materialized here", "topic_id": "M15B-T002", "tracker_id": "M15B-O004"}'
  FROM _m15_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M15A-P004::M15A-P004-E001'
    AND et.evidence_type_name = 'repeated priming evidence'
    AND ot.outcome_type_name = 'sustained intrinsic growth capacity'
  RETURNING observation_id
)
INSERT INTO _m15_observation_map (tracker_id, observation_id) SELECT 'M15B-O004', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Conditioning lesions outperformed cAMP, worked before or shortly after SCI, and recruited broader, longer-lasting genetic mechanisms.',
    'qualitative',
    NULL,
    'Conditioning lesions outperformed cAMP, worked before or shortly after SCI, and recruited broader, longer-lasting genetic mechanisms.',
    'conditioning broader than cAMP mimicry',
    'Module 15A tracker / source-page, full-text PMC, or review metadata',
    'Full-text PMC',
    'high',
    '{"curator_notes": "Broad mechanism comparator.", "experiment_tracker_id": "M15A-P005-E001", "measurement_method_inference": null, "paper_tracker_id": "M15A-P005", "quantitative": "NO", "statistics_reported": "Full-text first pass; microarray details queued", "topic_id": "M15B-T003", "tracker_id": "M15B-O005"}'
  FROM _m15_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M15A-P005::M15A-P005-E001'
    AND et.evidence_type_name = 'conditioning versus cAMP evidence'
    AND ot.outcome_type_name = 'genetic program duration and central regeneration'
  RETURNING observation_id
)
INSERT INTO _m15_observation_map (tracker_id, observation_id) SELECT 'M15B-O005', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'STAT3 activation after sciatic transection was necessary for enhanced DRG growth ability and dorsal column regeneration.',
    'qualitative',
    'pathway activity / phospho-signaling assay',
    'STAT3 activation after sciatic transection was necessary for enhanced DRG growth ability and dorsal column regeneration.',
    'STAT3 required for conditioning effect',
    'Module 15A tracker / source-page, full-text PMC, or review metadata',
    'Full-text PMC',
    'high',
    '{"curator_notes": "JAK/STAT boundary.", "experiment_tracker_id": "M15A-P006-E001", "measurement_method_inference": "pathway activity / phospho-signaling assay", "paper_tracker_id": "M15A-P006", "quantitative": "NO", "statistics_reported": "Full-text first pass; inhibitor results queued for quantitative extraction", "topic_id": "M15B-T004", "tracker_id": "M15B-O006"}'
  FROM _m15_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M15A-P006::M15A-P006-E001'
    AND et.evidence_type_name = 'STAT3 pathway evidence'
    AND ot.outcome_type_name = 'DRG growth competence and dorsal column regeneration'
  RETURNING observation_id
)
INSERT INTO _m15_observation_map (tracker_id, observation_id) SELECT 'M15B-O006', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'IL-6 knockout abolished conditioning-induced GAP-43 upregulation and dorsal column regeneration.',
    'qualitative',
    'ELISA / cytokine protein assay; genetic perturbation / knockdown assay',
    'IL-6 knockout abolished conditioning-induced GAP-43 upregulation and dorsal column regeneration.',
    'IL-6 required for conditioning-induced regeneration',
    'Module 15A tracker / source-page, full-text PMC, or review metadata',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Genetic cytokine boundary.", "experiment_tracker_id": "M15A-P007-E001", "measurement_method_inference": "ELISA / cytokine protein assay; genetic perturbation / knockdown assay", "paper_tracker_id": "M15A-P007", "quantitative": "NO", "statistics_reported": "Source-page first pass", "topic_id": "M15B-T004", "tracker_id": "M15B-O007"}'
  FROM _m15_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M15A-P007::M15A-P007-E001'
    AND et.evidence_type_name = 'IL-6 pathway evidence'
    AND ot.outcome_type_name = 'GAP-43 and dorsal column regeneration'
  RETURNING observation_id
)
INSERT INTO _m15_observation_map (tracker_id, observation_id) SELECT 'M15B-O007', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'cAMP elevation in DRG can mimic part of the conditioning lesion effect on central axon regeneration.',
    'qualitative',
    NULL,
    'cAMP elevation in DRG can mimic part of the conditioning lesion effect on central axon regeneration.',
    'cAMP mimics part of conditioning effect',
    'Module 15A tracker / source-page, full-text PMC, or review metadata',
    'Full-text PMC',
    'high',
    '{"curator_notes": "Mechanistic comparator.", "experiment_tracker_id": "M15A-P008-E001", "measurement_method_inference": null, "paper_tracker_id": "M15A-P008", "quantitative": "NO", "statistics_reported": "Review/full-text context", "topic_id": "M15B-T003", "tracker_id": "M15B-O008"}'
  FROM _m15_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M15A-P008::M15A-P008-E001'
    AND et.evidence_type_name = 'cAMP mimicry evidence'
    AND ot.outcome_type_name = 'central axon regeneration'
  RETURNING observation_id
)
INSERT INTO _m15_observation_map (tracker_id, observation_id) SELECT 'M15B-O008', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Adult sensory neuron axon growth competence depends on transcriptional state, supporting an intrinsic-growth switch after conditioning.',
    'qualitative',
    'qPCR / RT-PCR / mRNA assay',
    'Adult sensory neuron axon growth competence depends on transcriptional state, supporting an intrinsic-growth switch after conditioning.',
    'transcriptional switch controls growth competence',
    'Module 15A tracker / source-page, full-text PMC, or review metadata',
    'Full-text PMC',
    'high',
    '{"curator_notes": "Intrinsic program boundary.", "experiment_tracker_id": "M15A-P009-E001", "measurement_method_inference": "qPCR / RT-PCR / mRNA assay", "paper_tracker_id": "M15A-P009", "quantitative": "NO", "statistics_reported": "Full-text first pass", "topic_id": "M15B-T003", "tracker_id": "M15B-O009"}'
  FROM _m15_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M15A-P009::M15A-P009-E001'
    AND et.evidence_type_name = 'transcriptional switch evidence'
    AND ot.outcome_type_name = 'axon growth competence'
  RETURNING observation_id
)
INSERT INTO _m15_observation_map (tracker_id, observation_id) SELECT 'M15B-O009', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Conditioning altered neurite initiation, outgrowth rate, and branching, showing multiple separable components of enhanced regeneration.',
    'qualitative',
    NULL,
    'Conditioning altered neurite initiation, outgrowth rate, and branching, showing multiple separable components of enhanced regeneration.',
    'conditioning changes neurite initiation/outgrowth/branching',
    'Module 15A tracker / source-page, full-text PMC, or review metadata',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "In vitro DRG phenotype row.", "experiment_tracker_id": "M15A-P010-E001", "measurement_method_inference": null, "paper_tracker_id": "M15A-P010", "quantitative": "NO", "statistics_reported": "Source-page first pass", "topic_id": "M15B-T002", "tracker_id": "M15B-O010"}'
  FROM _m15_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M15A-P010::M15A-P010-E001'
    AND et.evidence_type_name = 'DRG culture conditioning evidence'
    AND ot.outcome_type_name = 'neurite initiation, outgrowth, and branching'
  RETURNING observation_id
)
INSERT INTO _m15_observation_map (tracker_id, observation_id) SELECT 'M15B-O010', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Unilateral sciatic injury induced bilateral and remote DRG pro-regenerative markers and increased regeneration capacity in DRGs not associated with the injured nerve.',
    'qualitative',
    NULL,
    'Unilateral sciatic injury induced bilateral and remote DRG pro-regenerative markers and increased regeneration capacity in DRGs not associated with the injured nerve.',
    'unilateral sciatic injury primes remote DRGs',
    'Module 15A tracker / source-page, full-text PMC, or review metadata',
    'Full-text PMC',
    'high',
    '{"curator_notes": "Direct remote/contralateral-style row.", "experiment_tracker_id": "M15A-P011-E001", "measurement_method_inference": null, "paper_tracker_id": "M15A-P011", "quantitative": "NO", "statistics_reported": "Full-text first pass; exact marker and neurite values queued", "topic_id": "M15B-T006", "tracker_id": "M15B-O011"}'
  FROM _m15_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M15A-P011::M15A-P011-E001'
    AND et.evidence_type_name = 'remote DRG priming evidence'
    AND ot.outcome_type_name = 'contralateral/remote regenerative state'
  RETURNING observation_id
)
INSERT INTO _m15_observation_map (tracker_id, observation_id) SELECT 'M15B-O011', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Enriched conditioning enhanced DRG regeneration after SCI via PKC-STAT3-NOX2 redox signaling and improved functional recovery.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Enriched conditioning enhanced DRG regeneration after SCI via PKC-STAT3-NOX2 redox signaling and improved functional recovery.',
    'enriched conditioning uses PKC-STAT3-NOX2 redox axis',
    'Module 15A tracker / source-page, full-text PMC, or review metadata',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Extended conditioning paradigm.", "experiment_tracker_id": "M15A-P012-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M15A-P012", "quantitative": "NO", "statistics_reported": "Source-page first pass", "topic_id": "M15B-T004", "tracker_id": "M15B-O012"}'
  FROM _m15_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M15A-P012::M15A-P012-E001'
    AND et.evidence_type_name = 'enriched conditioning evidence'
    AND ot.outcome_type_name = 'redox signaling and regeneration after SCI'
  RETURNING observation_id
)
INSERT INTO _m15_observation_map (tracker_id, observation_id) SELECT 'M15B-O012', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'DRG macrophages and inflammatory mediators contributed to maintenance of conditioning-induced regenerative capacity.',
    'qualitative',
    NULL,
    'DRG macrophages and inflammatory mediators contributed to maintenance of conditioning-induced regenerative capacity.',
    'DRG macrophages maintain conditioning effect',
    'Module 15A tracker / source-page, full-text PMC, or review metadata',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Intraganglionic immune support.", "experiment_tracker_id": "M15A-P013-E001", "measurement_method_inference": null, "paper_tracker_id": "M15A-P013", "quantitative": "NO", "statistics_reported": "Source-page first pass", "topic_id": "M15B-T005", "tracker_id": "M15B-O013"}'
  FROM _m15_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M15A-P013::M15A-P013-E001'
    AND et.evidence_type_name = 'DRG macrophage evidence'
    AND ot.outcome_type_name = 'maintenance of regenerative capacity'
  RETURNING observation_id
)
INSERT INTO _m15_observation_map (tracker_id, observation_id) SELECT 'M15B-O013', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Spinal glia division contributed to conditioning lesion-induced sensory axon regeneration into injured spinal cord.',
    'qualitative',
    NULL,
    'Spinal glia division contributed to conditioning lesion-induced sensory axon regeneration into injured spinal cord.',
    'spinal glia division supports conditioning-induced regeneration',
    'Module 15A tracker / source-page, full-text PMC, or review metadata',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Lesion-site support boundary.", "experiment_tracker_id": "M15A-P014-E001", "measurement_method_inference": null, "paper_tracker_id": "M15A-P014", "quantitative": "NO", "statistics_reported": "Source-page first pass", "topic_id": "M15B-T005", "tracker_id": "M15B-O014"}'
  FROM _m15_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M15A-P014::M15A-P014-E001'
    AND et.evidence_type_name = 'spinal glia support evidence'
    AND ot.outcome_type_name = 'sensory axon growth into injured spinal cord'
  RETURNING observation_id
)
INSERT INTO _m15_observation_map (tracker_id, observation_id) SELECT 'M15B-O014', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Dorsal column model review frames DRG neurons as ideal for separating peripheral and central branch injury responses.',
    'qualitative',
    NULL,
    'Dorsal column model review frames DRG neurons as ideal for separating peripheral and central branch injury responses.',
    'DRG model separates peripheral and central branch responses',
    'Module 15A tracker / source-page, full-text PMC, or review metadata',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Model boundary row.", "experiment_tracker_id": "M15A-P015-E001", "measurement_method_inference": null, "paper_tracker_id": "M15A-P015", "quantitative": "NO", "statistics_reported": "Source-page first pass", "topic_id": "M15B-T007", "tracker_id": "M15B-O015"}'
  FROM _m15_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M15A-P015::M15A-P015-E001'
    AND et.evidence_type_name = 'dorsal column model evidence'
    AND ot.outcome_type_name = 'intrinsic injury response model'
  RETURNING observation_id
)
INSERT INTO _m15_observation_map (tracker_id, observation_id) SELECT 'M15B-O015', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Commentary highlights that peripheral DRG conditioning can enable central axon regeneration and that sequence/timing determines effect.',
    'qualitative',
    NULL,
    'Commentary highlights that peripheral DRG conditioning can enable central axon regeneration and that sequence/timing determines effect.',
    'conditioning paradigm timing boundary',
    'Module 15A tracker / source-page, full-text PMC, or review metadata',
    'Full-text PMC',
    'high',
    '{"curator_notes": "Synthesis boundary row.", "experiment_tracker_id": "M15A-P016-E001", "measurement_method_inference": null, "paper_tracker_id": "M15A-P016", "quantitative": "NO", "statistics_reported": "Review/commentary first pass", "topic_id": "M15B-T008", "tracker_id": "M15B-O016"}'
  FROM _m15_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M15A-P016::M15A-P016-E001'
    AND et.evidence_type_name = 'conditioning paradigm review evidence'
    AND ot.outcome_type_name = 'central axon regeneration boundary'
  RETURNING observation_id
)
INSERT INTO _m15_observation_map (tracker_id, observation_id) SELECT 'M15B-O016', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Peripheral axotomy can alter the regenerative behavior of primary sensory neurons and increase central regeneration potential.',
    'mechanistic',
    'medium',
    'Module 15A tracker / source-page, full-text PMC, or review metadata',
    'medium',
    '{"curator_notes": "Foundational source-page claim.", "source_paper_tracker_id": "M15A-P001", "topic_id": "M15B-T001", "tracker_id": "M15B-C001"}'
  FROM _m15_paper_map p
  WHERE p.tracker_id = 'M15A-P001'
  RETURNING claim_id
)
INSERT INTO _m15_claim_map (tracker_id, claim_id) SELECT 'M15B-C001', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Conditioning effects are branch- and assay-specific, so peripheral growth acceleration should not be assumed to equal central branch regeneration.',
    'boundary condition',
    'high',
    'Module 15A tracker / source-page, full-text PMC, or review metadata',
    'high',
    '{"curator_notes": "Important negative boundary.", "source_paper_tracker_id": "M15A-P002", "topic_id": "M15B-T007", "tracker_id": "M15B-C002"}'
  FROM _m15_paper_map p
  WHERE p.tracker_id = 'M15A-P002'
  RETURNING claim_id
)
INSERT INTO _m15_claim_map (tracker_id, claim_id) SELECT 'M15B-C002', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Preconditioning peripheral axotomy can induce a DRG intrinsic growth state sufficient to support dorsal column axon growth beyond a spinal lesion.',
    'mechanistic',
    'medium',
    'Module 15A tracker / source-page, full-text PMC, or review metadata',
    'medium',
    '{"curator_notes": "Dorsal column positive row.", "source_paper_tracker_id": "M15A-P003", "topic_id": "M15B-T001", "tracker_id": "M15B-C003"}'
  FROM _m15_paper_map p
  WHERE p.tracker_id = 'M15A-P003'
  RETURNING claim_id
)
INSERT INTO _m15_claim_map (tracker_id, claim_id) SELECT 'M15B-C003', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Repeated peripheral priming can sustain intrinsic growth capacity after SCI and improve regeneration when single post-injury priming is insufficient.',
    'mechanistic',
    'high',
    'Module 15A tracker / source-page, full-text PMC, or review metadata',
    'high',
    '{"curator_notes": "Post-SCI timing claim.", "source_paper_tracker_id": "M15A-P004", "topic_id": "M15B-T002", "tracker_id": "M15B-C004"}'
  FROM _m15_paper_map p
  WHERE p.tracker_id = 'M15A-P004'
  RETURNING claim_id
)
INSERT INTO _m15_claim_map (tracker_id, claim_id) SELECT 'M15B-C004', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Peripheral conditioning lesions recruit broader and more durable genetic programs than cAMP elevation alone.',
    'mechanistic',
    'high',
    'Module 15A tracker / source-page, full-text PMC, or review metadata',
    'high',
    '{"curator_notes": "Broad mechanism claim.", "source_paper_tracker_id": "M15A-P005", "topic_id": "M15B-T003", "tracker_id": "M15B-C005"}'
  FROM _m15_paper_map p
  WHERE p.tracker_id = 'M15A-P005'
  RETURNING claim_id
)
INSERT INTO _m15_claim_map (tracker_id, claim_id) SELECT 'M15B-C005', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'JAK/STAT3 activation in DRG neurons is necessary for conditioning-induced growth competence and central sensory axon regeneration.',
    'mechanistic',
    'high',
    'Module 15A tracker / source-page, full-text PMC, or review metadata',
    'high',
    '{"curator_notes": "Inhibitor-supported claim.", "source_paper_tracker_id": "M15A-P006", "topic_id": "M15B-T004", "tracker_id": "M15B-C006"}'
  FROM _m15_paper_map p
  WHERE p.tracker_id = 'M15A-P006'
  RETURNING claim_id
)
INSERT INTO _m15_claim_map (tracker_id, claim_id) SELECT 'M15B-C006', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'IL-6 is required for conditioning-induced GAP-43 upregulation and dorsal column regeneration in the tested mouse model.',
    'mechanistic',
    'medium',
    'Module 15A tracker / source-page, full-text PMC, or review metadata',
    'medium',
    '{"curator_notes": "Knockout source-page claim.", "source_paper_tracker_id": "M15A-P007", "topic_id": "M15B-T004", "tracker_id": "M15B-C007"}'
  FROM _m15_paper_map p
  WHERE p.tracker_id = 'M15A-P007'
  RETURNING claim_id
)
INSERT INTO _m15_claim_map (tracker_id, claim_id) SELECT 'M15B-C007', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'cAMP signaling can mimic part of the conditioning lesion effect but should be treated as a partial mechanism.',
    'boundary condition',
    'high',
    'Module 15A tracker / source-page, full-text PMC, or review metadata',
    'high',
    '{"curator_notes": "Mechanistic comparator.", "source_paper_tracker_id": "M15A-P008", "topic_id": "M15B-T003", "tracker_id": "M15B-C008"}'
  FROM _m15_paper_map p
  WHERE p.tracker_id = 'M15A-P008'
  RETURNING claim_id
)
INSERT INTO _m15_claim_map (tracker_id, claim_id) SELECT 'M15B-C008', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Adult sensory neuron regeneration competence depends on transcriptional growth-state switching.',
    'mechanistic',
    'high',
    'Module 15A tracker / source-page, full-text PMC, or review metadata',
    'high',
    '{"curator_notes": "Intrinsic program claim.", "source_paper_tracker_id": "M15A-P009", "topic_id": "M15B-T003", "tracker_id": "M15B-C009"}'
  FROM _m15_paper_map p
  WHERE p.tracker_id = 'M15A-P009'
  RETURNING claim_id
)
INSERT INTO _m15_claim_map (tracker_id, claim_id) SELECT 'M15B-C009', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Conditioning changes multiple neurite-growth parameters, so regeneration capacity should not be represented as one undifferentiated endpoint.',
    'boundary condition',
    'medium',
    'Module 15A tracker / source-page, full-text PMC, or review metadata',
    'medium',
    '{"curator_notes": "In vitro phenotype boundary.", "source_paper_tracker_id": "M15A-P010", "topic_id": "M15B-T002", "tracker_id": "M15B-C010"}'
  FROM _m15_paper_map p
  WHERE p.tracker_id = 'M15A-P010'
  RETURNING claim_id
)
INSERT INTO _m15_claim_map (tracker_id, claim_id) SELECT 'M15B-C010', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Unilateral sciatic nerve injury can trigger a systemic or remote pro-regenerative DRG response outside the directly injured nerve territory.',
    'mechanistic',
    'high',
    'Module 15A tracker / source-page, full-text PMC, or review metadata',
    'high',
    '{"curator_notes": "Remote/contralateral-style claim.", "source_paper_tracker_id": "M15A-P011", "topic_id": "M15B-T006", "tracker_id": "M15B-C011"}'
  FROM _m15_paper_map p
  WHERE p.tracker_id = 'M15A-P011'
  RETURNING claim_id
)
INSERT INTO _m15_claim_map (tracker_id, claim_id) SELECT 'M15B-C011', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Enriched conditioning expands sensory-neuron regenerative ability through a neuronal intrinsic PKC-STAT3-NOX2 redox signaling axis.',
    'mechanistic',
    'medium',
    'Module 15A tracker / source-page, full-text PMC, or review metadata',
    'medium',
    '{"curator_notes": "Enriched-conditioning claim.", "source_paper_tracker_id": "M15A-P012", "topic_id": "M15B-T004", "tracker_id": "M15B-C012"}'
  FROM _m15_paper_map p
  WHERE p.tracker_id = 'M15A-P012'
  RETURNING claim_id
)
INSERT INTO _m15_claim_map (tracker_id, claim_id) SELECT 'M15B-C012', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'DRG macrophages and inflammatory mediators help maintain conditioning-induced regenerative capacity.',
    'mechanistic',
    'medium',
    'Module 15A tracker / source-page, full-text PMC, or review metadata',
    'medium',
    '{"curator_notes": "Intraganglionic immune claim.", "source_paper_tracker_id": "M15A-P013", "topic_id": "M15B-T005", "tracker_id": "M15B-C013"}'
  FROM _m15_paper_map p
  WHERE p.tracker_id = 'M15A-P013'
  RETURNING claim_id
)
INSERT INTO _m15_claim_map (tracker_id, claim_id) SELECT 'M15B-C013', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Spinal glial proliferation can contribute to conditioning lesion-induced sensory axon regeneration into the injured spinal cord.',
    'mechanistic',
    'medium',
    'Module 15A tracker / source-page, full-text PMC, or review metadata',
    'medium',
    '{"curator_notes": "Lesion-site glial claim.", "source_paper_tracker_id": "M15A-P014", "topic_id": "M15B-T005", "tracker_id": "M15B-C014"}'
  FROM _m15_paper_map p
  WHERE p.tracker_id = 'M15A-P014'
  RETURNING claim_id
)
INSERT INTO _m15_claim_map (tracker_id, claim_id) SELECT 'M15B-C014', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'The dorsal column model is a strong system for separating peripheral and central branch injury responses in the same DRG neuron population.',
    'model boundary',
    'medium',
    'Module 15A tracker / source-page, full-text PMC, or review metadata',
    'medium',
    '{"curator_notes": "Model ontology claim.", "source_paper_tracker_id": "M15A-P015", "topic_id": "M15B-T007", "tracker_id": "M15B-C015"}'
  FROM _m15_paper_map p
  WHERE p.tracker_id = 'M15A-P015'
  RETURNING claim_id
)
INSERT INTO _m15_claim_map (tracker_id, claim_id) SELECT 'M15B-C015', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Peripheral nerve/DRG conditioning is a host-priming comparator for SCI repair, but sequence, sensory-pathway specificity, and translation constraints must be retained.',
    'synthesis',
    'high',
    'Module 15A tracker / source-page, full-text PMC, or review metadata',
    'high',
    '{"curator_notes": "Project-level boundary.", "source_paper_tracker_id": "M15A-P016", "topic_id": "M15B-T008", "tracker_id": "M15B-C016"}'
  FROM _m15_paper_map p
  WHERE p.tracker_id = 'M15A-P016'
  RETURNING claim_id
)
INSERT INTO _m15_claim_map (tracker_id, claim_id) SELECT 'M15B-C016', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct first-pass link.", "strength": "medium", "tracker_id": "M15B-L001"}'
  FROM _m15_claim_map c
  JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O001'
  WHERE c.tracker_id = 'M15B-C001'
  RETURNING link_id
)
INSERT INTO _m15_link_map (tracker_id, link_id) SELECT 'M15B-L001', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct first-pass link.", "strength": "high", "tracker_id": "M15B-L002"}'
  FROM _m15_claim_map c
  JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O002'
  WHERE c.tracker_id = 'M15B-C002'
  RETURNING link_id
)
INSERT INTO _m15_link_map (tracker_id, link_id) SELECT 'M15B-L002', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct first-pass link.", "strength": "medium", "tracker_id": "M15B-L003"}'
  FROM _m15_claim_map c
  JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O003'
  WHERE c.tracker_id = 'M15B-C003'
  RETURNING link_id
)
INSERT INTO _m15_link_map (tracker_id, link_id) SELECT 'M15B-L003', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct first-pass link.", "strength": "high", "tracker_id": "M15B-L004"}'
  FROM _m15_claim_map c
  JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O004'
  WHERE c.tracker_id = 'M15B-C004'
  RETURNING link_id
)
INSERT INTO _m15_link_map (tracker_id, link_id) SELECT 'M15B-L004', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct first-pass link.", "strength": "high", "tracker_id": "M15B-L005"}'
  FROM _m15_claim_map c
  JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O005'
  WHERE c.tracker_id = 'M15B-C005'
  RETURNING link_id
)
INSERT INTO _m15_link_map (tracker_id, link_id) SELECT 'M15B-L005', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct first-pass link.", "strength": "high", "tracker_id": "M15B-L006"}'
  FROM _m15_claim_map c
  JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O006'
  WHERE c.tracker_id = 'M15B-C006'
  RETURNING link_id
)
INSERT INTO _m15_link_map (tracker_id, link_id) SELECT 'M15B-L006', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct first-pass link.", "strength": "medium", "tracker_id": "M15B-L007"}'
  FROM _m15_claim_map c
  JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O007'
  WHERE c.tracker_id = 'M15B-C007'
  RETURNING link_id
)
INSERT INTO _m15_link_map (tracker_id, link_id) SELECT 'M15B-L007', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct first-pass link.", "strength": "high", "tracker_id": "M15B-L008"}'
  FROM _m15_claim_map c
  JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O008'
  WHERE c.tracker_id = 'M15B-C008'
  RETURNING link_id
)
INSERT INTO _m15_link_map (tracker_id, link_id) SELECT 'M15B-L008', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct first-pass link.", "strength": "high", "tracker_id": "M15B-L009"}'
  FROM _m15_claim_map c
  JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O009'
  WHERE c.tracker_id = 'M15B-C009'
  RETURNING link_id
)
INSERT INTO _m15_link_map (tracker_id, link_id) SELECT 'M15B-L009', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct first-pass link.", "strength": "medium", "tracker_id": "M15B-L010"}'
  FROM _m15_claim_map c
  JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O010'
  WHERE c.tracker_id = 'M15B-C010'
  RETURNING link_id
)
INSERT INTO _m15_link_map (tracker_id, link_id) SELECT 'M15B-L010', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct first-pass link.", "strength": "high", "tracker_id": "M15B-L011"}'
  FROM _m15_claim_map c
  JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O011'
  WHERE c.tracker_id = 'M15B-C011'
  RETURNING link_id
)
INSERT INTO _m15_link_map (tracker_id, link_id) SELECT 'M15B-L011', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct first-pass link.", "strength": "medium", "tracker_id": "M15B-L012"}'
  FROM _m15_claim_map c
  JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O012'
  WHERE c.tracker_id = 'M15B-C012'
  RETURNING link_id
)
INSERT INTO _m15_link_map (tracker_id, link_id) SELECT 'M15B-L012', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct first-pass link.", "strength": "medium", "tracker_id": "M15B-L013"}'
  FROM _m15_claim_map c
  JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O013'
  WHERE c.tracker_id = 'M15B-C013'
  RETURNING link_id
)
INSERT INTO _m15_link_map (tracker_id, link_id) SELECT 'M15B-L013', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct first-pass link.", "strength": "medium", "tracker_id": "M15B-L014"}'
  FROM _m15_claim_map c
  JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O014'
  WHERE c.tracker_id = 'M15B-C014'
  RETURNING link_id
)
INSERT INTO _m15_link_map (tracker_id, link_id) SELECT 'M15B-L014', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct first-pass link.", "strength": "medium", "tracker_id": "M15B-L015"}'
  FROM _m15_claim_map c
  JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O015'
  WHERE c.tracker_id = 'M15B-C015'
  RETURNING link_id
)
INSERT INTO _m15_link_map (tracker_id, link_id) SELECT 'M15B-L015', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct first-pass link.", "strength": "high", "tracker_id": "M15B-L016"}'
  FROM _m15_claim_map c
  JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O016'
  WHERE c.tracker_id = 'M15B-C016'
  RETURNING link_id
)
INSERT INTO _m15_link_map (tracker_id, link_id) SELECT 'M15B-L016', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Neumann/Woolf contextualizes foundational conditioning effect.", "strength": "low", "tracker_id": "M15B-L017"}'
  FROM _m15_claim_map c
  JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O003'
  WHERE c.tracker_id = 'M15B-C001'
  RETURNING link_id
)
INSERT INTO _m15_link_map (tracker_id, link_id) SELECT 'M15B-L017', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Dorsal column model row supports sensory pathway boundary.", "strength": "low", "tracker_id": "M15B-L018"}'
  FROM _m15_claim_map c
  JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O015'
  WHERE c.tracker_id = 'M15B-C001'
  RETURNING link_id
)
INSERT INTO _m15_link_map (tracker_id, link_id) SELECT 'M15B-L018', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Model row reinforces branch specificity.", "strength": "low", "tracker_id": "M15B-L019"}'
  FROM _m15_claim_map c
  JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O015'
  WHERE c.tracker_id = 'M15B-C002'
  RETURNING link_id
)
INSERT INTO _m15_link_map (tracker_id, link_id) SELECT 'M15B-L019', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Repeated priming contextualizes timing dependence.", "strength": "low", "tracker_id": "M15B-L020"}'
  FROM _m15_claim_map c
  JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O004'
  WHERE c.tracker_id = 'M15B-C003'
  RETURNING link_id
)
INSERT INTO _m15_link_map (tracker_id, link_id) SELECT 'M15B-L020', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Broad genetic programs contextualize sustained effect.", "strength": "low", "tracker_id": "M15B-L021"}'
  FROM _m15_claim_map c
  JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O005'
  WHERE c.tracker_id = 'M15B-C004'
  RETURNING link_id
)
INSERT INTO _m15_link_map (tracker_id, link_id) SELECT 'M15B-L021', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "cAMP row supports partial-mechanism boundary.", "strength": "low", "tracker_id": "M15B-L022"}'
  FROM _m15_claim_map c
  JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O008'
  WHERE c.tracker_id = 'M15B-C005'
  RETURNING link_id
)
INSERT INTO _m15_link_map (tracker_id, link_id) SELECT 'M15B-L022', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Transcriptional switch row supports broad mechanism boundary.", "strength": "low", "tracker_id": "M15B-L023"}'
  FROM _m15_claim_map c
  JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O009'
  WHERE c.tracker_id = 'M15B-C005'
  RETURNING link_id
)
INSERT INTO _m15_link_map (tracker_id, link_id) SELECT 'M15B-L023', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "IL-6 row supports cytokine/STAT boundary.", "strength": "low", "tracker_id": "M15B-L024"}'
  FROM _m15_claim_map c
  JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O007'
  WHERE c.tracker_id = 'M15B-C006'
  RETURNING link_id
)
INSERT INTO _m15_link_map (tracker_id, link_id) SELECT 'M15B-L024', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Enriched conditioning row supports STAT3 redox axis.", "strength": "low", "tracker_id": "M15B-L025"}'
  FROM _m15_claim_map c
  JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O012'
  WHERE c.tracker_id = 'M15B-C006'
  RETURNING link_id
)
INSERT INTO _m15_link_map (tracker_id, link_id) SELECT 'M15B-L025', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "STAT3 row supports IL-6/JAK pathway boundary.", "strength": "low", "tracker_id": "M15B-L026"}'
  FROM _m15_claim_map c
  JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O006'
  WHERE c.tracker_id = 'M15B-C007'
  RETURNING link_id
)
INSERT INTO _m15_link_map (tracker_id, link_id) SELECT 'M15B-L026', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Conditioning versus cAMP row supports partial mimicry boundary.", "strength": "low", "tracker_id": "M15B-L027"}'
  FROM _m15_claim_map c
  JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O005'
  WHERE c.tracker_id = 'M15B-C008'
  RETURNING link_id
)
INSERT INTO _m15_link_map (tracker_id, link_id) SELECT 'M15B-L027', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Broad gene mechanism row supports transcriptional switching.", "strength": "low", "tracker_id": "M15B-L028"}'
  FROM _m15_claim_map c
  JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O005'
  WHERE c.tracker_id = 'M15B-C009'
  RETURNING link_id
)
INSERT INTO _m15_link_map (tracker_id, link_id) SELECT 'M15B-L028', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Branch-specific row supports endpoint separation.", "strength": "low", "tracker_id": "M15B-L029"}'
  FROM _m15_claim_map c
  JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O002'
  WHERE c.tracker_id = 'M15B-C010'
  RETURNING link_id
)
INSERT INTO _m15_link_map (tracker_id, link_id) SELECT 'M15B-L029', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Enriched conditioning contextualizes systemic/expanded priming logic.", "strength": "low", "tracker_id": "M15B-L030"}'
  FROM _m15_claim_map c
  JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O012'
  WHERE c.tracker_id = 'M15B-C011'
  RETURNING link_id
)
INSERT INTO _m15_link_map (tracker_id, link_id) SELECT 'M15B-L030', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "DRG macrophage row contextualizes systemic/inflammatory mediator boundary.", "strength": "low", "tracker_id": "M15B-L031"}'
  FROM _m15_claim_map c
  JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O013'
  WHERE c.tracker_id = 'M15B-C011'
  RETURNING link_id
)
INSERT INTO _m15_link_map (tracker_id, link_id) SELECT 'M15B-L031', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "STAT3 row contextualizes redox-axis claim.", "strength": "low", "tracker_id": "M15B-L032"}'
  FROM _m15_claim_map c
  JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O006'
  WHERE c.tracker_id = 'M15B-C012'
  RETURNING link_id
)
INSERT INTO _m15_link_map (tracker_id, link_id) SELECT 'M15B-L032', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Remote DRG row contextualizes immune-mediated systemic response.", "strength": "low", "tracker_id": "M15B-L033"}'
  FROM _m15_claim_map c
  JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O011'
  WHERE c.tracker_id = 'M15B-C013'
  RETURNING link_id
)
INSERT INTO _m15_link_map (tracker_id, link_id) SELECT 'M15B-L033', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "DRG macrophage row separates ganglion versus spinal glia.", "strength": "low", "tracker_id": "M15B-L034"}'
  FROM _m15_claim_map c
  JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O013'
  WHERE c.tracker_id = 'M15B-C014'
  RETURNING link_id
)
INSERT INTO _m15_link_map (tracker_id, link_id) SELECT 'M15B-L034', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Branch-specific row supports model ontology.", "strength": "low", "tracker_id": "M15B-L035"}'
  FROM _m15_claim_map c
  JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O002'
  WHERE c.tracker_id = 'M15B-C015'
  RETURNING link_id
)
INSERT INTO _m15_link_map (tracker_id, link_id) SELECT 'M15B-L035', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Dorsal column positive row supports host-priming comparator.", "strength": "low", "tracker_id": "M15B-L036"}'
  FROM _m15_claim_map c
  JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O003'
  WHERE c.tracker_id = 'M15B-C016'
  RETURNING link_id
)
INSERT INTO _m15_link_map (tracker_id, link_id) SELECT 'M15B-L036', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Repeated post-SCI priming contextualizes translation timing.", "strength": "low", "tracker_id": "M15B-L037"}'
  FROM _m15_claim_map c
  JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O004'
  WHERE c.tracker_id = 'M15B-C016'
  RETURNING link_id
)
INSERT INTO _m15_link_map (tracker_id, link_id) SELECT 'M15B-L037', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Broad genetic mechanism row supports comparator value.", "strength": "low", "tracker_id": "M15B-L038"}'
  FROM _m15_claim_map c
  JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O005'
  WHERE c.tracker_id = 'M15B-C016'
  RETURNING link_id
)
INSERT INTO _m15_link_map (tracker_id, link_id) SELECT 'M15B-L038', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Remote DRG row supports systemic priming boundary.", "strength": "low", "tracker_id": "M15B-L039"}'
  FROM _m15_claim_map c
  JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O011'
  WHERE c.tracker_id = 'M15B-C016'
  RETURNING link_id
)
INSERT INTO _m15_link_map (tracker_id, link_id) SELECT 'M15B-L039', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Review/commentary row supports project-level boundary.", "strength": "low", "tracker_id": "M15B-L040"}'
  FROM _m15_claim_map c
  JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O016'
  WHERE c.tracker_id = 'M15B-C016'
  RETURNING link_id
)
INSERT INTO _m15_link_map (tracker_id, link_id) SELECT 'M15B-L040', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Peripheral nerve injury can induce a DRG intrinsic growth state that improves central sensory axon regeneration, but the claim is strongest for DRG/dorsal-column sensory systems and must preserve peripheral lesion, central test lesion, species, and endpoint boundaries.',
    'M15B-T001',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M15B-B001", "M15B-B002", "M15B-B003", "M15B-B004", "M15B-B005", "M15B-B006", "M15B-B007", "M15B-B008"], "claim_tracker_ids": ["M15B-C001", "M15B-C002", "M15B-C003"], "consensus_draft_id": "M15B-S001", "observation_tracker_ids": ["M15B-O001", "M15B-O002", "M15B-O003"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 15 first-pass curation freeze.", "topic_id": "M15B-T001"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m15_consensus_map (tracker_id, consensus_id) SELECT 'M15B-S001', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m15_consensus_map c
JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O001'
WHERE c.tracker_id = 'M15B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m15_consensus_map c
JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O002'
WHERE c.tracker_id = 'M15B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m15_consensus_map c
JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O003'
WHERE c.tracker_id = 'M15B-S001';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Timing is a causal variable in conditioning-lesion biology: preconditioning, concurrent priming, post-SCI priming, repeated priming, and enriched conditioning produce different regenerative outcomes and should be analyzed as separate intervention classes.',
    'M15B-T002',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M15B-B001", "M15B-B002", "M15B-B003", "M15B-B004", "M15B-B005", "M15B-B006", "M15B-B007", "M15B-B008"], "claim_tracker_ids": ["M15B-C003", "M15B-C004", "M15B-C005"], "consensus_draft_id": "M15B-S002", "observation_tracker_ids": ["M15B-O003", "M15B-O004", "M15B-O005"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 15 first-pass curation freeze.", "topic_id": "M15B-T002"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m15_consensus_map (tracker_id, consensus_id) SELECT 'M15B-S002', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m15_consensus_map c
JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O003'
WHERE c.tracker_id = 'M15B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m15_consensus_map c
JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O004'
WHERE c.tracker_id = 'M15B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m15_consensus_map c
JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O005'
WHERE c.tracker_id = 'M15B-S002';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'cAMP/PKA signaling can mimic part of the conditioning effect, but peripheral nerve conditioning recruits broader and more durable transcriptional programs, so cAMP should be treated as one mechanism rather than the whole priming state.',
    'M15B-T003',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M15B-B001", "M15B-B002", "M15B-B003", "M15B-B004", "M15B-B005", "M15B-B006", "M15B-B007", "M15B-B008"], "claim_tracker_ids": ["M15B-C005", "M15B-C006", "M15B-C007", "M15B-C008", "M15B-C009"], "consensus_draft_id": "M15B-S003", "observation_tracker_ids": ["M15B-O005", "M15B-O006", "M15B-O007", "M15B-O008", "M15B-O009"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 15 first-pass curation freeze.", "topic_id": "M15B-T003"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m15_consensus_map (tracker_id, consensus_id) SELECT 'M15B-S003', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m15_consensus_map c
JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O005'
WHERE c.tracker_id = 'M15B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m15_consensus_map c
JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O006'
WHERE c.tracker_id = 'M15B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m15_consensus_map c
JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O007'
WHERE c.tracker_id = 'M15B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m15_consensus_map c
JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O008'
WHERE c.tracker_id = 'M15B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m15_consensus_map c
JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O009'
WHERE c.tracker_id = 'M15B-S003';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'IL-6/JAK/STAT3 signaling is a consensus-ready mediator family for conditioning-induced DRG growth competence, with enriched-conditioning evidence extending this axis into PKC-STAT3-NOX2 redox signaling after SCI.',
    'M15B-T004',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M15B-B001", "M15B-B002", "M15B-B003", "M15B-B004", "M15B-B005", "M15B-B006", "M15B-B007", "M15B-B008"], "claim_tracker_ids": ["M15B-C006", "M15B-C007", "M15B-C008", "M15B-C009", "M15B-C010", "M15B-C011", "M15B-C012"], "consensus_draft_id": "M15B-S004", "observation_tracker_ids": ["M15B-O006", "M15B-O007", "M15B-O008", "M15B-O009", "M15B-O010", "M15B-O011", "M15B-O012"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 15 first-pass curation freeze.", "topic_id": "M15B-T004"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m15_consensus_map (tracker_id, consensus_id) SELECT 'M15B-S004', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m15_consensus_map c
JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O006'
WHERE c.tracker_id = 'M15B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m15_consensus_map c
JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O007'
WHERE c.tracker_id = 'M15B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m15_consensus_map c
JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O008'
WHERE c.tracker_id = 'M15B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m15_consensus_map c
JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O009'
WHERE c.tracker_id = 'M15B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m15_consensus_map c
JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O010'
WHERE c.tracker_id = 'M15B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m15_consensus_map c
JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O011'
WHERE c.tracker_id = 'M15B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m15_consensus_map c
JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O012'
WHERE c.tracker_id = 'M15B-S004';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Conditioning lesion effects include non-neuronal support: DRG macrophages and spinal glial division contribute to the maintenance or expression of regenerative capacity and should be separated by compartment and timing.',
    'M15B-T005',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M15B-B001", "M15B-B002", "M15B-B003", "M15B-B004", "M15B-B005", "M15B-B006", "M15B-B007", "M15B-B008"], "claim_tracker_ids": ["M15B-C013", "M15B-C014"], "consensus_draft_id": "M15B-S005", "observation_tracker_ids": ["M15B-O013", "M15B-O014"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 15 first-pass curation freeze.", "topic_id": "M15B-T005"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m15_consensus_map (tracker_id, consensus_id) SELECT 'M15B-S005', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m15_consensus_map c
JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O013'
WHERE c.tracker_id = 'M15B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m15_consensus_map c
JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O014'
WHERE c.tracker_id = 'M15B-S005';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Unilateral sciatic nerve injury can induce pro-regenerative marker expression and enhanced growth capacity in DRGs not directly associated with the damaged nerve, making remote or contralateral DRG priming a real boundary to track separately from ipsilateral conditioning.',
    'M15B-T006',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M15B-B001", "M15B-B002", "M15B-B003", "M15B-B004", "M15B-B005", "M15B-B006", "M15B-B007", "M15B-B008"], "claim_tracker_ids": ["M15B-C011", "M15B-C012"], "consensus_draft_id": "M15B-S006", "observation_tracker_ids": ["M15B-O011", "M15B-O012"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 15 first-pass curation freeze.", "topic_id": "M15B-T006"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m15_consensus_map (tracker_id, consensus_id) SELECT 'M15B-S006', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m15_consensus_map c
JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O011'
WHERE c.tracker_id = 'M15B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m15_consensus_map c
JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O012'
WHERE c.tracker_id = 'M15B-S006';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Peripheral conditioning is not a universal regeneration switch: early branch-specific negative evidence and dorsal-column model boundaries show that peripheral, central, ipsilateral, contralateral, and tract-specific outcomes must remain separated.',
    'M15B-T007',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M15B-B001", "M15B-B002", "M15B-B003", "M15B-B004", "M15B-B005", "M15B-B006", "M15B-B007", "M15B-B008"], "claim_tracker_ids": ["M15B-C002", "M15B-C003", "M15B-C004", "M15B-C005", "M15B-C006", "M15B-C007", "M15B-C008", "M15B-C009", "M15B-C010", "M15B-C011", "M15B-C012", "M15B-C013", "M15B-C014", "M15B-C015"], "consensus_draft_id": "M15B-S007", "observation_tracker_ids": ["M15B-O002", "M15B-O003", "M15B-O004", "M15B-O005", "M15B-O006", "M15B-O007", "M15B-O008", "M15B-O009", "M15B-O010", "M15B-O011", "M15B-O012", "M15B-O013", "M15B-O014", "M15B-O015"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 15 first-pass curation freeze.", "topic_id": "M15B-T007"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m15_consensus_map (tracker_id, consensus_id) SELECT 'M15B-S007', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m15_consensus_map c
JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O002'
WHERE c.tracker_id = 'M15B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m15_consensus_map c
JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O003'
WHERE c.tracker_id = 'M15B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m15_consensus_map c
JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O004'
WHERE c.tracker_id = 'M15B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m15_consensus_map c
JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O005'
WHERE c.tracker_id = 'M15B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m15_consensus_map c
JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O006'
WHERE c.tracker_id = 'M15B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m15_consensus_map c
JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O007'
WHERE c.tracker_id = 'M15B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m15_consensus_map c
JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O008'
WHERE c.tracker_id = 'M15B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m15_consensus_map c
JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O009'
WHERE c.tracker_id = 'M15B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m15_consensus_map c
JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O010'
WHERE c.tracker_id = 'M15B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m15_consensus_map c
JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O011'
WHERE c.tracker_id = 'M15B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m15_consensus_map c
JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O012'
WHERE c.tracker_id = 'M15B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m15_consensus_map c
JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O013'
WHERE c.tracker_id = 'M15B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m15_consensus_map c
JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O014'
WHERE c.tracker_id = 'M15B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m15_consensus_map c
JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O015'
WHERE c.tracker_id = 'M15B-S007';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Module 15 should function as a peripheral-to-CNS host-priming comparator for SCI repair: candidate synthesis should ask whether a treatment mimics DRG growth-state induction, sustains that state after SCI, recruits systemic/remote DRG programs, or changes the lesion environment enough for central axon growth.',
    'M15B-T008',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M15B-B001", "M15B-B002", "M15B-B003", "M15B-B004", "M15B-B005", "M15B-B006", "M15B-B007", "M15B-B008"], "claim_tracker_ids": ["M15B-C004", "M15B-C005", "M15B-C006", "M15B-C007", "M15B-C008", "M15B-C009", "M15B-C010", "M15B-C011", "M15B-C012", "M15B-C013", "M15B-C014", "M15B-C015", "M15B-C016"], "consensus_draft_id": "M15B-S008", "observation_tracker_ids": ["M15B-O004", "M15B-O005", "M15B-O006", "M15B-O007", "M15B-O008", "M15B-O009", "M15B-O010", "M15B-O011", "M15B-O012", "M15B-O013", "M15B-O014", "M15B-O015", "M15B-O016"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 15 first-pass curation freeze.", "topic_id": "M15B-T008"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m15_consensus_map (tracker_id, consensus_id) SELECT 'M15B-S008', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m15_consensus_map c
JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O004'
WHERE c.tracker_id = 'M15B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m15_consensus_map c
JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O005'
WHERE c.tracker_id = 'M15B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m15_consensus_map c
JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O006'
WHERE c.tracker_id = 'M15B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m15_consensus_map c
JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O007'
WHERE c.tracker_id = 'M15B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m15_consensus_map c
JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O008'
WHERE c.tracker_id = 'M15B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m15_consensus_map c
JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O009'
WHERE c.tracker_id = 'M15B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m15_consensus_map c
JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O010'
WHERE c.tracker_id = 'M15B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m15_consensus_map c
JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O011'
WHERE c.tracker_id = 'M15B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m15_consensus_map c
JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O012'
WHERE c.tracker_id = 'M15B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m15_consensus_map c
JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O013'
WHERE c.tracker_id = 'M15B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m15_consensus_map c
JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O014'
WHERE c.tracker_id = 'M15B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m15_consensus_map c
JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O015'
WHERE c.tracker_id = 'M15B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m15_consensus_map c
JOIN _m15_observation_map o ON o.tracker_id = 'M15B-O016'
WHERE c.tracker_id = 'M15B-S008';

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
  SELECT COUNT(*) INTO paper_count FROM _m15_paper_map;
  SELECT COUNT(*) INTO experiment_count FROM _m15_experiment_map;
  SELECT COUNT(*) INTO observation_count FROM _m15_observation_map;
  SELECT COUNT(*) INTO claim_count FROM _m15_claim_map;
  SELECT COUNT(*) INTO link_count FROM _m15_link_map;
  SELECT COUNT(*) INTO consensus_count FROM _m15_consensus_map;
  SELECT COUNT(*) INTO consensus_observation_count
  FROM Consensus_Observation co
  JOIN _m15_consensus_map cm ON cm.consensus_id = co.consensus_id;
  IF paper_count <> 16 THEN RAISE EXCEPTION 'Expected 16 papers, found %', paper_count; END IF;
  IF experiment_count <> 16 THEN RAISE EXCEPTION 'Unexpected experiment count %', experiment_count; END IF;
  IF observation_count <> 16 THEN RAISE EXCEPTION 'Expected 16 observations, found %', observation_count; END IF;
  IF claim_count <> 16 THEN RAISE EXCEPTION 'Expected 16 claims, found %', claim_count; END IF;
  IF link_count <> 40 THEN RAISE EXCEPTION 'Expected 40 evidence links, found %', link_count; END IF;
  IF consensus_count <> 8 THEN RAISE EXCEPTION 'Expected 8 consensus rows, found %', consensus_count; END IF;
  IF consensus_observation_count <> 49 THEN RAISE EXCEPTION 'Unexpected consensus-observation count %', consensus_observation_count; END IF;
END $$;

COMMIT;
