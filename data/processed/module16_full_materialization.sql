-- Module 16B full first-pass materialization generated from tracker-derived JSON.
-- This script is intended for a fresh database loaded with schema/schema.sql and scripts/seed_controlled_vocab.sql.
BEGIN;

CREATE TEMP TABLE _m16_paper_map (tracker_id TEXT PRIMARY KEY, paper_id INTEGER NOT NULL);
CREATE TEMP TABLE _m16_paradigm_map (tracker_id TEXT PRIMARY KEY, paradigm_id INTEGER NOT NULL);
CREATE TEMP TABLE _m16_experiment_map (tracker_id TEXT PRIMARY KEY, experiment_id INTEGER NOT NULL);
CREATE TEMP TABLE _m16_observation_map (tracker_id TEXT PRIMARY KEY, observation_id INTEGER NOT NULL);
CREATE TEMP TABLE _m16_claim_map (tracker_id TEXT PRIMARY KEY, claim_id INTEGER NOT NULL);
CREATE TEMP TABLE _m16_link_map (tracker_id TEXT PRIMARY KEY, link_id INTEGER NOT NULL);
CREATE TEMP TABLE _m16_consensus_map (tracker_id TEXT PRIMARY KEY, consensus_id INTEGER NOT NULL);

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Depolarization and electrical stimulation enhance in vitro and in vivo sensory axon growth after spinal cord injury', 'Udina', 2008,
    'Experimental Neurology', NULL, NULL,
    NULL, '10.1016/j.expneurol.2008.08.029', 'PMC5752127',
    NULL, '{"curator_notes": "Direct sensory axon growth after SCI; depolarization/electrical stimulation increased initiation but did not fully replace conditioning lesion.", "module": "Module 16B", "tracker_id": "M16A-P001"}'
  )
  RETURNING paper_id
)
INSERT INTO _m16_paper_map (tracker_id, paper_id) SELECT 'M16A-P001', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Differential effects of electrical stimulation of sciatic nerve on metabolic activity in spinal cord and dorsal root ganglion in the rat', 'Kadekaro', 1985,
    'Proceedings of the National Academy of Sciences', NULL, NULL,
    NULL, '10.1073/pnas.82.17.6010', 'PMID:3862113',
    NULL, '{"curator_notes": "Sciatic stump stimulation caused frequency-dependent spinal dorsal horn glucose utilization without DRG cell-body metabolic activation.", "module": "Module 16B", "tracker_id": "M16A-P002"}'
  )
  RETURNING paper_id
)
INSERT INTO _m16_paper_map (tracker_id, paper_id) SELECT 'M16A-P002', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Brief Electrical Stimulation Promotes Recovery after Surgical Repair of Injured Peripheral Nerves', 'Gordon', 2023,
    'International Journal of Molecular Sciences', NULL, NULL,
    NULL, '10.3390/ijms242316939', 'PMC10779324',
    NULL, '{"curator_notes": "Review anchor for brief ES and conditioning ES; includes intact sciatic nerve 20 Hz for 1 h enhancing DRG neurite outgrowth.", "module": "Module 16B", "tracker_id": "M16A-P003"}'
  )
  RETURNING paper_id
)
INSERT INTO _m16_paper_map (tracker_id, paper_id) SELECT 'M16A-P003', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Functional Electrical Stimulation and the Modulation of the Axon Regeneration Program', 'Gordon', 2020,
    'Frontiers in Cell and Developmental Biology', NULL, NULL,
    NULL, '10.3389/fcell.2020.00736', 'PMC7425295',
    NULL, '{"curator_notes": "Review anchor stating ES activates overlapping pathways with conditioning lesions but does not fully recapitulate their growth-promoting effects.", "module": "Module 16B", "tracker_id": "M16A-P004"}'
  )
  RETURNING paper_id
)
INSERT INTO _m16_paper_map (tracker_id, paper_id) SELECT 'M16A-P004', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Regeneration of dorsal column fibers into and beyond the lesion site following adult spinal cord injury', 'Neumann', 1999,
    'Neuron', NULL, NULL,
    NULL, '10.1016/S0896-6273(00)80755-2', 'PMID:10402195',
    NULL, '{"curator_notes": "Conditioning lesion comparator; defines benchmark that peripheral axotomy before dorsal column injury enables growth beyond lesion.", "module": "Module 16B", "tracker_id": "M16A-P005"}'
  )
  RETURNING paper_id
)
INSERT INTO _m16_paper_map (tracker_id, paper_id) SELECT 'M16A-P005', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Conditioning lesions before or after spinal cord injury recruit broad genetic mechanisms that sustain axonal regeneration: superiority to cAMP-mediated effects', 'Blesch', 2012,
    'Experimental Neurology', NULL, NULL,
    NULL, '10.1016/j.expneurol.2011.12.037', 'PMID:22227059',
    NULL, '{"curator_notes": "Conditioning lesion/cAMP comparator for judging whether ES only partially mimics lesion-induced growth programs.", "module": "Module 16B", "tracker_id": "M16A-P006"}'
  )
  RETURNING paper_id
)
INSERT INTO _m16_paper_map (tracker_id, paper_id) SELECT 'M16A-P006', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Conditioning Injury-Induced Spinal Axon Regeneration Requires Signal Transducer and Activator of Transcription 3 Activation', 'Qiu', 2005,
    'Journal of Neuroscience', NULL, NULL,
    NULL, '10.1523/JNEUROSCI.4427-04.2005', 'PMID:15716400',
    NULL, '{"curator_notes": "STAT3 conditioning lesion comparator; useful for testing whether ES engages similar DRG pathways.", "module": "Module 16B", "tracker_id": "M16A-P007"}'
  )
  RETURNING paper_id
)
INSERT INTO _m16_paper_map (tracker_id, paper_id) SELECT 'M16A-P007', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Enriched conditioning expands the regenerative ability of sensory neurons after spinal cord injury via neuronal intrinsic redox signaling', 'Pita-Thomas', 2021,
    'Nature Communications', NULL, NULL,
    NULL, '10.1038/s41467-020-20112-4', 'PMID:33349630',
    NULL, '{"curator_notes": "Activity/enrichment plus lesion-conditioning comparator; supports activity-state synergy boundary.", "module": "Module 16B", "tracker_id": "M16A-P008"}'
  )
  RETURNING paper_id
)
INSERT INTO _m16_paper_map (tracker_id, paper_id) SELECT 'M16A-P008', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'A conditioning lesion of the peripheral axons of dorsal root ganglion cells accelerates regeneration of only their peripheral axons', 'Oblinger', 1984,
    'Journal of Neuroscience', NULL, NULL,
    NULL, '10.1523/JNEUROSCI.04-07-01736.1984', 'PMID:6204020',
    NULL, '{"curator_notes": "Branch-specific conditioning boundary; prevents assuming peripheral effects equal central branch repair.", "module": "Module 16B", "tracker_id": "M16A-P009"}'
  )
  RETURNING paper_id
)
INSERT INTO _m16_paper_map (tracker_id, paper_id) SELECT 'M16A-P009', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Mechanisms of enhancement of neurite regeneration in vitro following a conditioning sciatic nerve lesion', 'Smith', 1998,
    'Journal of Comparative Neurology', NULL, NULL,
    NULL, NULL, 'PMID:9527536',
    NULL, '{"curator_notes": "Lesion-conditioning neurite morphology comparator for ES-induced DRG neurite effects.", "module": "Module 16B", "tracker_id": "M16A-P010"}'
  )
  RETURNING paper_id
)
INSERT INTO _m16_paper_map (tracker_id, paper_id) SELECT 'M16A-P010', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'A Conditioning Sciatic Nerve Lesion Triggers a Pro-regenerative State in Primary Sensory Neurons Also of Dorsal Root Ganglia Non-associated With the Damaged Nerve', 'Dubovy', 2019,
    'Frontiers in Cellular Neuroscience', NULL, NULL,
    NULL, '10.3389/fncel.2019.00011', 'PMID:30778286',
    NULL, '{"curator_notes": "Remote DRG lesion-conditioning comparator; helps frame whether ES has local versus systemic/remote priming evidence.", "module": "Module 16B", "tracker_id": "M16A-P011"}'
  )
  RETURNING paper_id
)
INSERT INTO _m16_paper_map (tracker_id, paper_id) SELECT 'M16A-P011', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'CNS regeneration: only on one condition', 'Silver', 2009,
    'Current Biology', NULL, NULL,
    NULL, '10.1016/j.cub.2009.04.026', 'PMID:19515349',
    NULL, '{"curator_notes": "Commentary boundary for conditioning lesion timing and central regeneration claims.", "module": "Module 16B", "tracker_id": "M16A-P012"}'
  )
  RETURNING paper_id
)
INSERT INTO _m16_paper_map (tracker_id, paper_id) SELECT 'M16A-P012', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Conditioning lesions of peripheral nerves change regenerated axon numbers', 'Jenq', 1988,
    'Brain Research', NULL, NULL,
    NULL, '10.1016/0006-8993(88)90057-1', 'PMID:3167569',
    NULL, '{"curator_notes": "Peripheral conditioning lesion timing benchmark for regenerated axon numbers.", "module": "Module 16B", "tracker_id": "M16A-P013"}'
  )
  RETURNING paper_id
)
INSERT INTO _m16_paper_map (tracker_id, paper_id) SELECT 'M16A-P013', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'AMPK controls the axonal regenerative ability of dorsal root ganglia sensory neurons after spinal cord injury', 'Kong', 2020,
    'Nature Metabolism', NULL, NULL,
    NULL, '10.1038/s42255-020-0252-3', 'PMID:32778834',
    NULL, '{"curator_notes": "DRG metabolic growth-state comparator; candidate readout for ES-induced conditioning.", "module": "Module 16B", "tracker_id": "M16A-P014"}'
  )
  RETURNING paper_id
)
INSERT INTO _m16_paper_map (tracker_id, paper_id) SELECT 'M16A-P014', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'The Dorsal Column Lesion Model of Spinal Cord Injury and Its Use in Deciphering the Neuron-Intrinsic Injury Response', 'Bradke', 2018,
    'Methods in Molecular Biology', NULL, NULL,
    NULL, '10.1007/978-1-4939-7649-2_13', 'PMID:29717546',
    NULL, '{"curator_notes": "Model boundary for central branch repair assays.", "module": "Module 16B", "tracker_id": "M16A-P015"}'
  )
  RETURNING paper_id
)
INSERT INTO _m16_paper_map (tracker_id, paper_id) SELECT 'M16A-P015', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Sensory Afferents Regenerated into Dorsal Columns after Spinal Cord Injury Remain in a Chronic Pathophysiological State', 'Houle', 2007,
    'Experimental Neurology', NULL, NULL,
    NULL, '10.1016/j.expneurol.2007.01.026', 'PMC3103885',
    NULL, '{"curator_notes": "Functional/chronic boundary: regenerated sensory afferents after conditioning-plus-repair may remain pathophysiological.", "module": "Module 16B", "tracker_id": "M16A-P016"}'
  )
  RETURNING paper_id
)
INSERT INTO _m16_paper_map (tracker_id, paper_id) SELECT 'M16A-P016', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 16B curated evidence extraction',
    'First-pass Module 16B PNS electrical stimulation preconditioning for CNS repair curation for M16A-P001',
    'Tracker-derived materialization from Module_16B_TRACKER.md'
  FROM _m16_paper_map WHERE tracker_id = 'M16A-P001'
  RETURNING paradigm_id
)
INSERT INTO _m16_paradigm_map (tracker_id, paradigm_id) SELECT 'M16A-P001', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 16B curated evidence extraction',
    'First-pass Module 16B PNS electrical stimulation preconditioning for CNS repair curation for M16A-P002',
    'Tracker-derived materialization from Module_16B_TRACKER.md'
  FROM _m16_paper_map WHERE tracker_id = 'M16A-P002'
  RETURNING paradigm_id
)
INSERT INTO _m16_paradigm_map (tracker_id, paradigm_id) SELECT 'M16A-P002', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 16B curated evidence extraction',
    'First-pass Module 16B PNS electrical stimulation preconditioning for CNS repair curation for M16A-P003',
    'Tracker-derived materialization from Module_16B_TRACKER.md'
  FROM _m16_paper_map WHERE tracker_id = 'M16A-P003'
  RETURNING paradigm_id
)
INSERT INTO _m16_paradigm_map (tracker_id, paradigm_id) SELECT 'M16A-P003', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 16B curated evidence extraction',
    'First-pass Module 16B PNS electrical stimulation preconditioning for CNS repair curation for M16A-P004',
    'Tracker-derived materialization from Module_16B_TRACKER.md'
  FROM _m16_paper_map WHERE tracker_id = 'M16A-P004'
  RETURNING paradigm_id
)
INSERT INTO _m16_paradigm_map (tracker_id, paradigm_id) SELECT 'M16A-P004', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 16B curated evidence extraction',
    'First-pass Module 16B PNS electrical stimulation preconditioning for CNS repair curation for M16A-P005',
    'Tracker-derived materialization from Module_16B_TRACKER.md'
  FROM _m16_paper_map WHERE tracker_id = 'M16A-P005'
  RETURNING paradigm_id
)
INSERT INTO _m16_paradigm_map (tracker_id, paradigm_id) SELECT 'M16A-P005', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 16B curated evidence extraction',
    'First-pass Module 16B PNS electrical stimulation preconditioning for CNS repair curation for M16A-P006',
    'Tracker-derived materialization from Module_16B_TRACKER.md'
  FROM _m16_paper_map WHERE tracker_id = 'M16A-P006'
  RETURNING paradigm_id
)
INSERT INTO _m16_paradigm_map (tracker_id, paradigm_id) SELECT 'M16A-P006', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 16B curated evidence extraction',
    'First-pass Module 16B PNS electrical stimulation preconditioning for CNS repair curation for M16A-P007',
    'Tracker-derived materialization from Module_16B_TRACKER.md'
  FROM _m16_paper_map WHERE tracker_id = 'M16A-P007'
  RETURNING paradigm_id
)
INSERT INTO _m16_paradigm_map (tracker_id, paradigm_id) SELECT 'M16A-P007', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 16B curated evidence extraction',
    'First-pass Module 16B PNS electrical stimulation preconditioning for CNS repair curation for M16A-P008',
    'Tracker-derived materialization from Module_16B_TRACKER.md'
  FROM _m16_paper_map WHERE tracker_id = 'M16A-P008'
  RETURNING paradigm_id
)
INSERT INTO _m16_paradigm_map (tracker_id, paradigm_id) SELECT 'M16A-P008', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 16B curated evidence extraction',
    'First-pass Module 16B PNS electrical stimulation preconditioning for CNS repair curation for M16A-P009',
    'Tracker-derived materialization from Module_16B_TRACKER.md'
  FROM _m16_paper_map WHERE tracker_id = 'M16A-P009'
  RETURNING paradigm_id
)
INSERT INTO _m16_paradigm_map (tracker_id, paradigm_id) SELECT 'M16A-P009', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 16B curated evidence extraction',
    'First-pass Module 16B PNS electrical stimulation preconditioning for CNS repair curation for M16A-P010',
    'Tracker-derived materialization from Module_16B_TRACKER.md'
  FROM _m16_paper_map WHERE tracker_id = 'M16A-P010'
  RETURNING paradigm_id
)
INSERT INTO _m16_paradigm_map (tracker_id, paradigm_id) SELECT 'M16A-P010', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 16B curated evidence extraction',
    'First-pass Module 16B PNS electrical stimulation preconditioning for CNS repair curation for M16A-P011',
    'Tracker-derived materialization from Module_16B_TRACKER.md'
  FROM _m16_paper_map WHERE tracker_id = 'M16A-P011'
  RETURNING paradigm_id
)
INSERT INTO _m16_paradigm_map (tracker_id, paradigm_id) SELECT 'M16A-P011', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 16B curated evidence extraction',
    'First-pass Module 16B PNS electrical stimulation preconditioning for CNS repair curation for M16A-P012',
    'Tracker-derived materialization from Module_16B_TRACKER.md'
  FROM _m16_paper_map WHERE tracker_id = 'M16A-P012'
  RETURNING paradigm_id
)
INSERT INTO _m16_paradigm_map (tracker_id, paradigm_id) SELECT 'M16A-P012', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 16B curated evidence extraction',
    'First-pass Module 16B PNS electrical stimulation preconditioning for CNS repair curation for M16A-P013',
    'Tracker-derived materialization from Module_16B_TRACKER.md'
  FROM _m16_paper_map WHERE tracker_id = 'M16A-P013'
  RETURNING paradigm_id
)
INSERT INTO _m16_paradigm_map (tracker_id, paradigm_id) SELECT 'M16A-P013', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 16B curated evidence extraction',
    'First-pass Module 16B PNS electrical stimulation preconditioning for CNS repair curation for M16A-P014',
    'Tracker-derived materialization from Module_16B_TRACKER.md'
  FROM _m16_paper_map WHERE tracker_id = 'M16A-P014'
  RETURNING paradigm_id
)
INSERT INTO _m16_paradigm_map (tracker_id, paradigm_id) SELECT 'M16A-P014', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 16B curated evidence extraction',
    'First-pass Module 16B PNS electrical stimulation preconditioning for CNS repair curation for M16A-P015',
    'Tracker-derived materialization from Module_16B_TRACKER.md'
  FROM _m16_paper_map WHERE tracker_id = 'M16A-P015'
  RETURNING paradigm_id
)
INSERT INTO _m16_paradigm_map (tracker_id, paradigm_id) SELECT 'M16A-P015', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 16B curated evidence extraction',
    'First-pass Module 16B PNS electrical stimulation preconditioning for CNS repair curation for M16A-P016',
    'Tracker-derived materialization from Module_16B_TRACKER.md'
  FROM _m16_paper_map WHERE tracker_id = 'M16A-P016'
  RETURNING paradigm_id
)
INSERT INTO _m16_paradigm_map (tracker_id, paradigm_id) SELECT 'M16A-P016', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Full text PMC',
    'Tracker experiment M16A-P001-E001',
    'Module 16B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M16B-O001"], "source_experiment_tracker_id": "M16A-P001-E001", "source_paper_tracker_id": "M16A-P001", "tracker_key": "M16A-P001::M16A-P001-E001"}'
  FROM _m16_paper_map p
  JOIN _m16_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M16A-P001'
  RETURNING experiment_id
)
INSERT INTO _m16_experiment_map (tracker_id, experiment_id) SELECT 'M16A-P001::M16A-P001-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Full text PMC',
    'Tracker experiment M16A-P002-E001',
    'Module 16B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M16B-O002"], "source_experiment_tracker_id": "M16A-P002-E001", "source_paper_tracker_id": "M16A-P002", "tracker_key": "M16A-P002::M16A-P002-E001"}'
  FROM _m16_paper_map p
  JOIN _m16_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M16A-P002'
  RETURNING experiment_id
)
INSERT INTO _m16_experiment_map (tracker_id, experiment_id) SELECT 'M16A-P002::M16A-P002-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Full text PMC',
    'Tracker experiment M16A-P003-E001',
    'Module 16B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M16B-O003"], "source_experiment_tracker_id": "M16A-P003-E001", "source_paper_tracker_id": "M16A-P003", "tracker_key": "M16A-P003::M16A-P003-E001"}'
  FROM _m16_paper_map p
  JOIN _m16_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M16A-P003'
  RETURNING experiment_id
)
INSERT INTO _m16_experiment_map (tracker_id, experiment_id) SELECT 'M16A-P003::M16A-P003-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Full text PMC',
    'Tracker experiment M16A-P004-E001',
    'Module 16B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M16B-O004"], "source_experiment_tracker_id": "M16A-P004-E001", "source_paper_tracker_id": "M16A-P004", "tracker_key": "M16A-P004::M16A-P004-E001"}'
  FROM _m16_paper_map p
  JOIN _m16_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M16A-P004'
  RETURNING experiment_id
)
INSERT INTO _m16_experiment_map (tracker_id, experiment_id) SELECT 'M16A-P004::M16A-P004-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M16A-P005-E001',
    'Module 16B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M16B-O005"], "source_experiment_tracker_id": "M16A-P005-E001", "source_paper_tracker_id": "M16A-P005", "tracker_key": "M16A-P005::M16A-P005-E001"}'
  FROM _m16_paper_map p
  JOIN _m16_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M16A-P005'
  RETURNING experiment_id
)
INSERT INTO _m16_experiment_map (tracker_id, experiment_id) SELECT 'M16A-P005::M16A-P005-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Full text PMC',
    'Tracker experiment M16A-P006-E001',
    'Module 16B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M16B-O006"], "source_experiment_tracker_id": "M16A-P006-E001", "source_paper_tracker_id": "M16A-P006", "tracker_key": "M16A-P006::M16A-P006-E001"}'
  FROM _m16_paper_map p
  JOIN _m16_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M16A-P006'
  RETURNING experiment_id
)
INSERT INTO _m16_experiment_map (tracker_id, experiment_id) SELECT 'M16A-P006::M16A-P006-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Full text PMC',
    'Tracker experiment M16A-P007-E001',
    'Module 16B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M16B-O007"], "source_experiment_tracker_id": "M16A-P007-E001", "source_paper_tracker_id": "M16A-P007", "tracker_key": "M16A-P007::M16A-P007-E001"}'
  FROM _m16_paper_map p
  JOIN _m16_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M16A-P007'
  RETURNING experiment_id
)
INSERT INTO _m16_experiment_map (tracker_id, experiment_id) SELECT 'M16A-P007::M16A-P007-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M16A-P008-E001',
    'Module 16B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M16B-O008"], "source_experiment_tracker_id": "M16A-P008-E001", "source_paper_tracker_id": "M16A-P008", "tracker_key": "M16A-P008::M16A-P008-E001"}'
  FROM _m16_paper_map p
  JOIN _m16_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M16A-P008'
  RETURNING experiment_id
)
INSERT INTO _m16_experiment_map (tracker_id, experiment_id) SELECT 'M16A-P008::M16A-P008-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Full text PMC',
    'Tracker experiment M16A-P009-E001',
    'Module 16B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M16B-O009"], "source_experiment_tracker_id": "M16A-P009-E001", "source_paper_tracker_id": "M16A-P009", "tracker_key": "M16A-P009::M16A-P009-E001"}'
  FROM _m16_paper_map p
  JOIN _m16_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M16A-P009'
  RETURNING experiment_id
)
INSERT INTO _m16_experiment_map (tracker_id, experiment_id) SELECT 'M16A-P009::M16A-P009-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M16A-P010-E001',
    'Module 16B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M16B-O010"], "source_experiment_tracker_id": "M16A-P010-E001", "source_paper_tracker_id": "M16A-P010", "tracker_key": "M16A-P010::M16A-P010-E001"}'
  FROM _m16_paper_map p
  JOIN _m16_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M16A-P010'
  RETURNING experiment_id
)
INSERT INTO _m16_experiment_map (tracker_id, experiment_id) SELECT 'M16A-P010::M16A-P010-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Full text PMC',
    'Tracker experiment M16A-P011-E001',
    'Module 16B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M16B-O011"], "source_experiment_tracker_id": "M16A-P011-E001", "source_paper_tracker_id": "M16A-P011", "tracker_key": "M16A-P011::M16A-P011-E001"}'
  FROM _m16_paper_map p
  JOIN _m16_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M16A-P011'
  RETURNING experiment_id
)
INSERT INTO _m16_experiment_map (tracker_id, experiment_id) SELECT 'M16A-P011::M16A-P011-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Full text PMC',
    'Tracker experiment M16A-P012-E001',
    'Module 16B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M16B-O012"], "source_experiment_tracker_id": "M16A-P012-E001", "source_paper_tracker_id": "M16A-P012", "tracker_key": "M16A-P012::M16A-P012-E001"}'
  FROM _m16_paper_map p
  JOIN _m16_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M16A-P012'
  RETURNING experiment_id
)
INSERT INTO _m16_experiment_map (tracker_id, experiment_id) SELECT 'M16A-P012::M16A-P012-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M16A-P013-E001',
    'Module 16B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M16B-O013"], "source_experiment_tracker_id": "M16A-P013-E001", "source_paper_tracker_id": "M16A-P013", "tracker_key": "M16A-P013::M16A-P013-E001"}'
  FROM _m16_paper_map p
  JOIN _m16_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M16A-P013'
  RETURNING experiment_id
)
INSERT INTO _m16_experiment_map (tracker_id, experiment_id) SELECT 'M16A-P013::M16A-P013-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M16A-P014-E001',
    'Module 16B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M16B-O014"], "source_experiment_tracker_id": "M16A-P014-E001", "source_paper_tracker_id": "M16A-P014", "tracker_key": "M16A-P014::M16A-P014-E001"}'
  FROM _m16_paper_map p
  JOIN _m16_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M16A-P014'
  RETURNING experiment_id
)
INSERT INTO _m16_experiment_map (tracker_id, experiment_id) SELECT 'M16A-P014::M16A-P014-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M16A-P015-E001',
    'Module 16B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M16B-O015"], "source_experiment_tracker_id": "M16A-P015-E001", "source_paper_tracker_id": "M16A-P015", "tracker_key": "M16A-P015::M16A-P015-E001"}'
  FROM _m16_paper_map p
  JOIN _m16_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M16A-P015'
  RETURNING experiment_id
)
INSERT INTO _m16_experiment_map (tracker_id, experiment_id) SELECT 'M16A-P015::M16A-P015-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Full text PMC',
    'Tracker experiment M16A-P016-E001',
    'Module 16B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M16B-O016"], "source_experiment_tracker_id": "M16A-P016-E001", "source_paper_tracker_id": "M16A-P016", "tracker_key": "M16A-P016::M16A-P016-E001"}'
  FROM _m16_paper_map p
  JOIN _m16_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M16A-P016'
  RETURNING experiment_id
)
INSERT INTO _m16_experiment_map (tracker_id, experiment_id) SELECT 'M16A-P016::M16A-P016-E001', experiment_id FROM inserted;

INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('DRG metabolic growth-state evidence', 'Module 16B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('ES regeneration-program review evidence', 'Module 16B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('PNS ES plus SCI evidence', 'Module 16B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('STAT3 comparator evidence', 'Module 16B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('activity-state comparator evidence', 'Module 16B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('branch-specific conditioning evidence', 'Module 16B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('brief ES / conditioning ES evidence', 'Module 16B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('chronic functional safety evidence', 'Module 16B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('conditioning lesion benchmark evidence', 'Module 16B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('conditioning versus cAMP comparator evidence', 'Module 16B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('dorsal column model evidence', 'Module 16B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('neurite morphology comparator evidence', 'Module 16B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('peripheral conditioning timing evidence', 'Module 16B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('remote DRG comparator evidence', 'Module 16B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('sciatic nerve stimulation physiology evidence', 'Module 16B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('timing comparator evidence', 'Module 16B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;

INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('AMPK-linked regeneration competence', 'Module 16B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('DRG growth-state benchmark', 'Module 16B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('DRG neurite outgrowth and peripheral nerve repair', 'Module 16B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('central axon growth beyond lesion', 'Module 16B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('central branch assay design', 'Module 16B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('gene-program durability', 'Module 16B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('local versus remote DRG priming', 'Module 16B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('neurite initiation/outgrowth/branching', 'Module 16B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('peripheral versus central branch specificity', 'Module 16B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('redox signaling and SCI regeneration', 'Module 16B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('regenerated axon number', 'Module 16B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('regenerated sensory afferent physiology', 'Module 16B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('regeneration-program activation', 'Module 16B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('sensory axon growth initiation and elongation', 'Module 16B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('sequence-dependent central regeneration', 'Module 16B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('spinal versus DRG metabolic activation', 'Module 16B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Electrical stimulation/depolarization enhanced sensory axon growth initiation after SCI but was less robust than conditioning lesion for elongation through the lesion.',
    'qualitative',
    'Electrical stimulation/depolarization enhanced sensory axon growth initiation after SCI but was less robust than conditioning lesion for elongation through the lesion.',
    'ES enhances initiation more than elongation',
    'Module 16A tracker / source-page, full-text PMC, or review metadata',
    'Full text PMC',
    'high',
    '{"curator_notes": "Direct CNS repair ES boundary.", "experiment_tracker_id": "M16A-P001-E001", "paper_tracker_id": "M16A-P001", "quantitative": "NO", "statistics_reported": "Full-text first pass; exact growth distances not materialized here", "topic_id": "M16B-T001", "tracker_id": "M16B-O001"}'
  FROM _m16_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M16A-P001::M16A-P001-E001'
    AND et.evidence_type_name = 'PNS ES plus SCI evidence'
    AND ot.outcome_type_name = 'sensory axon growth initiation and elongation'
  RETURNING observation_id
)
INSERT INTO _m16_observation_map (tracker_id, observation_id) SELECT 'M16B-O001', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Sciatic nerve stimulation produced frequency-dependent dorsal horn metabolic activation but did not increase DRG cell-body glucose utilization.',
    'qualitative',
    'Sciatic nerve stimulation produced frequency-dependent dorsal horn metabolic activation but did not increase DRG cell-body glucose utilization.',
    'sciatic ES activates spinal terminals not DRG soma metabolism',
    'Module 16A tracker / source-page, full-text PMC, or review metadata',
    'Full text PMC',
    'high',
    '{"curator_notes": "Compartment boundary.", "experiment_tracker_id": "M16A-P002-E001", "paper_tracker_id": "M16A-P002", "quantitative": "YES", "statistics_reported": "Frequency-dependent glucose-utilization effect reported", "topic_id": "M16B-T002", "tracker_id": "M16B-O002"}'
  FROM _m16_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M16A-P002::M16A-P002-E001'
    AND et.evidence_type_name = 'sciatic nerve stimulation physiology evidence'
    AND ot.outcome_type_name = 'spinal versus DRG metabolic activation'
  RETURNING observation_id
)
INSERT INTO _m16_observation_map (tracker_id, observation_id) SELECT 'M16B-O002', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Brief ES can enhance DRG neurite outgrowth and peripheral nerve repair outcomes, but conditioning ES and lesion conditioning are not equivalent across endpoints.',
    'qualitative',
    'Brief ES can enhance DRG neurite outgrowth and peripheral nerve repair outcomes, but conditioning ES and lesion conditioning are not equivalent across endpoints.',
    'brief ES supports PNS repair and DRG neurites',
    'Module 16A tracker / source-page, full-text PMC, or review metadata',
    'Full text PMC',
    'high',
    '{"curator_notes": "Parameter anchor.", "experiment_tracker_id": "M16A-P003-E001", "paper_tracker_id": "M16A-P003", "quantitative": "YES", "statistics_reported": "Review reports 20 Hz for 1 h intact sciatic ES enhanced DRG neurite extension", "topic_id": "M16B-T003", "tracker_id": "M16B-O003"}'
  FROM _m16_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M16A-P003::M16A-P003-E001'
    AND et.evidence_type_name = 'brief ES / conditioning ES evidence'
    AND ot.outcome_type_name = 'DRG neurite outgrowth and peripheral nerve repair'
  RETURNING observation_id
)
INSERT INTO _m16_observation_map (tracker_id, observation_id) SELECT 'M16B-O003', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Review states ES activates overlapping pathways with peripheral conditioning lesions but does not fully recapitulate conditioning lesion effects.',
    'qualitative',
    'Review states ES activates overlapping pathways with peripheral conditioning lesions but does not fully recapitulate conditioning lesion effects.',
    'ES overlaps but does not equal lesion conditioning',
    'Module 16A tracker / source-page, full-text PMC, or review metadata',
    'Full text PMC',
    'high',
    '{"curator_notes": "Key equivalence boundary.", "experiment_tracker_id": "M16A-P004-E001", "paper_tracker_id": "M16A-P004", "quantitative": "NO", "statistics_reported": "Review-level first pass", "topic_id": "M16B-T001", "tracker_id": "M16B-O004"}'
  FROM _m16_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M16A-P004::M16A-P004-E001'
    AND et.evidence_type_name = 'ES regeneration-program review evidence'
    AND ot.outcome_type_name = 'regeneration-program activation'
  RETURNING observation_id
)
INSERT INTO _m16_observation_map (tracker_id, observation_id) SELECT 'M16B-O004', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Peripheral lesion preconditioning is the benchmark for central sensory axon growth beyond dorsal column lesion.',
    'qualitative',
    'Peripheral lesion preconditioning is the benchmark for central sensory axon growth beyond dorsal column lesion.',
    'lesion preconditioning benchmark',
    'Module 16A tracker / source-page, full-text PMC, or review metadata',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Comparator-only row.", "experiment_tracker_id": "M16A-P005-E001", "paper_tracker_id": "M16A-P005", "quantitative": "NO", "statistics_reported": "Source-page first pass", "topic_id": "M16B-T004", "tracker_id": "M16B-O005"}'
  FROM _m16_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M16A-P005::M16A-P005-E001'
    AND et.evidence_type_name = 'conditioning lesion benchmark evidence'
    AND ot.outcome_type_name = 'central axon growth beyond lesion'
  RETURNING observation_id
)
INSERT INTO _m16_observation_map (tracker_id, observation_id) SELECT 'M16B-O005', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Lesion conditioning recruited broader and longer-lasting genetic programs than cAMP, setting a benchmark for ES mimicry.',
    'qualitative',
    'Lesion conditioning recruited broader and longer-lasting genetic programs than cAMP, setting a benchmark for ES mimicry.',
    'lesion conditioning broader than cAMP',
    'Module 16A tracker / source-page, full-text PMC, or review metadata',
    'Full text PMC',
    'high',
    '{"curator_notes": "Comparator-only row.", "experiment_tracker_id": "M16A-P006-E001", "paper_tracker_id": "M16A-P006", "quantitative": "NO", "statistics_reported": "Full-text first pass", "topic_id": "M16B-T004", "tracker_id": "M16B-O006"}'
  FROM _m16_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M16A-P006::M16A-P006-E001'
    AND et.evidence_type_name = 'conditioning versus cAMP comparator evidence'
    AND ot.outcome_type_name = 'gene-program durability'
  RETURNING observation_id
)
INSERT INTO _m16_observation_map (tracker_id, observation_id) SELECT 'M16B-O006', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'STAT3 activation is a required DRG growth-state benchmark for conditioning-like stimulation approaches.',
    'qualitative',
    'STAT3 activation is a required DRG growth-state benchmark for conditioning-like stimulation approaches.',
    'STAT3 benchmark for DRG priming',
    'Module 16A tracker / source-page, full-text PMC, or review metadata',
    'Full text PMC',
    'high',
    '{"curator_notes": "Pathway comparator.", "experiment_tracker_id": "M16A-P007-E001", "paper_tracker_id": "M16A-P007", "quantitative": "NO", "statistics_reported": "Full-text first pass", "topic_id": "M16B-T004", "tracker_id": "M16B-O007"}'
  FROM _m16_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M16A-P007::M16A-P007-E001'
    AND et.evidence_type_name = 'STAT3 comparator evidence'
    AND ot.outcome_type_name = 'DRG growth-state benchmark'
  RETURNING observation_id
)
INSERT INTO _m16_observation_map (tracker_id, observation_id) SELECT 'M16B-O007', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Enriched conditioning shows activity-state synergy with lesion conditioning through PKC-STAT3-NOX2 signaling.',
    'qualitative',
    'Enriched conditioning shows activity-state synergy with lesion conditioning through PKC-STAT3-NOX2 signaling.',
    'activity-state synergy readout',
    'Module 16A tracker / source-page, full-text PMC, or review metadata',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Candidate readout row.", "experiment_tracker_id": "M16A-P008-E001", "paper_tracker_id": "M16A-P008", "quantitative": "NO", "statistics_reported": "Source-page first pass", "topic_id": "M16B-T005", "tracker_id": "M16B-O008"}'
  FROM _m16_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M16A-P008::M16A-P008-E001'
    AND et.evidence_type_name = 'activity-state comparator evidence'
    AND ot.outcome_type_name = 'redox signaling and SCI regeneration'
  RETURNING observation_id
)
INSERT INTO _m16_observation_map (tracker_id, observation_id) SELECT 'M16B-O008', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Peripheral conditioning effects can be branch-specific and cannot be assumed to improve central branch repair in every assay.',
    'qualitative',
    'Peripheral conditioning effects can be branch-specific and cannot be assumed to improve central branch repair in every assay.',
    'branch-specific conditioning boundary',
    'Module 16A tracker / source-page, full-text PMC, or review metadata',
    'Full text PMC',
    'high',
    '{"curator_notes": "Negative/boundary comparator.", "experiment_tracker_id": "M16A-P009-E001", "paper_tracker_id": "M16A-P009", "quantitative": "YES", "statistics_reported": "Peripheral branch increased 4.4 to 5.5 mm/day; central branch not significantly affected", "topic_id": "M16B-T004", "tracker_id": "M16B-O009"}'
  FROM _m16_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M16A-P009::M16A-P009-E001'
    AND et.evidence_type_name = 'branch-specific conditioning evidence'
    AND ot.outcome_type_name = 'peripheral versus central branch specificity'
  RETURNING observation_id
)
INSERT INTO _m16_observation_map (tracker_id, observation_id) SELECT 'M16B-O009', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Conditioning lesions alter neurite initiation, growth rate, and branching, defining phenotype dimensions for ES comparison.',
    'qualitative',
    'Conditioning lesions alter neurite initiation, growth rate, and branching, defining phenotype dimensions for ES comparison.',
    'neurite morphology comparator',
    'Module 16A tracker / source-page, full-text PMC, or review metadata',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Phenotype boundary.", "experiment_tracker_id": "M16A-P010-E001", "paper_tracker_id": "M16A-P010", "quantitative": "NO", "statistics_reported": "Source-page first pass", "topic_id": "M16B-T004", "tracker_id": "M16B-O010"}'
  FROM _m16_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M16A-P010::M16A-P010-E001'
    AND et.evidence_type_name = 'neurite morphology comparator evidence'
    AND ot.outcome_type_name = 'neurite initiation/outgrowth/branching'
  RETURNING observation_id
)
INSERT INTO _m16_observation_map (tracker_id, observation_id) SELECT 'M16B-O010', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Lesion conditioning can produce remote/non-associated DRG priming; ES needs separate evidence before remote effects are inferred.',
    'qualitative',
    'Lesion conditioning can produce remote/non-associated DRG priming; ES needs separate evidence before remote effects are inferred.',
    'remote DRG priming not assumed for ES',
    'Module 16A tracker / source-page, full-text PMC, or review metadata',
    'Full text PMC',
    'high',
    '{"curator_notes": "Remote-effect boundary.", "experiment_tracker_id": "M16A-P011-E001", "paper_tracker_id": "M16A-P011", "quantitative": "NO", "statistics_reported": "Full-text first pass", "topic_id": "M16B-T006", "tracker_id": "M16B-O011"}'
  FROM _m16_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M16A-P011::M16A-P011-E001'
    AND et.evidence_type_name = 'remote DRG comparator evidence'
    AND ot.outcome_type_name = 'local versus remote DRG priming'
  RETURNING observation_id
)
INSERT INTO _m16_observation_map (tracker_id, observation_id) SELECT 'M16B-O011', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Conditioning-like claims must preserve sequence and timing because reversed-order effects differ from preconditioning.',
    'qualitative',
    'Conditioning-like claims must preserve sequence and timing because reversed-order effects differ from preconditioning.',
    'timing and sequence boundary',
    'Module 16A tracker / source-page, full-text PMC, or review metadata',
    'Full text PMC',
    'high',
    '{"curator_notes": "Timing boundary.", "experiment_tracker_id": "M16A-P012-E001", "paper_tracker_id": "M16A-P012", "quantitative": "NO", "statistics_reported": "Review/commentary first pass", "topic_id": "M16B-T004", "tracker_id": "M16B-O012"}'
  FROM _m16_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M16A-P012::M16A-P012-E001'
    AND et.evidence_type_name = 'timing comparator evidence'
    AND ot.outcome_type_name = 'sequence-dependent central regeneration'
  RETURNING observation_id
)
INSERT INTO _m16_observation_map (tracker_id, observation_id) SELECT 'M16B-O012', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Conditioning effects on regenerated axon numbers require sufficient interval between lesions; timing is a stimulation-design boundary.',
    'qualitative',
    'Conditioning effects on regenerated axon numbers require sufficient interval between lesions; timing is a stimulation-design boundary.',
    'interval-dependent conditioning effect',
    'Module 16A tracker / source-page, full-text PMC, or review metadata',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Timing benchmark.", "experiment_tracker_id": "M16A-P013-E001", "paper_tracker_id": "M16A-P013", "quantitative": "NO", "statistics_reported": "Source-page first pass", "topic_id": "M16B-T004", "tracker_id": "M16B-O013"}'
  FROM _m16_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M16A-P013::M16A-P013-E001'
    AND et.evidence_type_name = 'peripheral conditioning timing evidence'
    AND ot.outcome_type_name = 'regenerated axon number'
  RETURNING observation_id
)
INSERT INTO _m16_observation_map (tracker_id, observation_id) SELECT 'M16B-O013', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'AMPK controls DRG sensory-neuron regenerative ability, supporting metabolic readouts for ES preconditioning.',
    'qualitative',
    'AMPK controls DRG sensory-neuron regenerative ability, supporting metabolic readouts for ES preconditioning.',
    'AMPK candidate readout',
    'Module 16A tracker / source-page, full-text PMC, or review metadata',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Mechanistic readout candidate.", "experiment_tracker_id": "M16A-P014-E001", "paper_tracker_id": "M16A-P014", "quantitative": "NO", "statistics_reported": "Source-page first pass", "topic_id": "M16B-T005", "tracker_id": "M16B-O014"}'
  FROM _m16_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M16A-P014::M16A-P014-E001'
    AND et.evidence_type_name = 'DRG metabolic growth-state evidence'
    AND ot.outcome_type_name = 'AMPK-linked regeneration competence'
  RETURNING observation_id
)
INSERT INTO _m16_observation_map (tracker_id, observation_id) SELECT 'M16B-O014', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Dorsal column model defines the assay boundary for testing whether ES improves central branch regeneration.',
    'qualitative',
    'Dorsal column model defines the assay boundary for testing whether ES improves central branch regeneration.',
    'dorsal column assay boundary',
    'Module 16A tracker / source-page, full-text PMC, or review metadata',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Model ontology row.", "experiment_tracker_id": "M16A-P015-E001", "paper_tracker_id": "M16A-P015", "quantitative": "NO", "statistics_reported": "Source-page first pass", "topic_id": "M16B-T008", "tracker_id": "M16B-O015"}'
  FROM _m16_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M16A-P015::M16A-P015-E001'
    AND et.evidence_type_name = 'dorsal column model evidence'
    AND ot.outcome_type_name = 'central branch assay design'
  RETURNING observation_id
)
INSERT INTO _m16_observation_map (tracker_id, observation_id) SELECT 'M16B-O015', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Even regenerated sensory afferents after conditioning-plus-repair can remain chronically pathophysiological, setting functional safety boundaries for ES-enabled repair.',
    'qualitative',
    'Even regenerated sensory afferents after conditioning-plus-repair can remain chronically pathophysiological, setting functional safety boundaries for ES-enabled repair.',
    'chronic pathophysiology safety boundary',
    'Module 16A tracker / source-page, full-text PMC, or review metadata',
    'Full text PMC',
    'high',
    '{"curator_notes": "Safety/function boundary.", "experiment_tracker_id": "M16A-P016-E001", "paper_tracker_id": "M16A-P016", "quantitative": "NO", "statistics_reported": "Full-text first pass", "topic_id": "M16B-T007", "tracker_id": "M16B-O016"}'
  FROM _m16_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M16A-P016::M16A-P016-E001'
    AND et.evidence_type_name = 'chronic functional safety evidence'
    AND ot.outcome_type_name = 'regenerated sensory afferent physiology'
  RETURNING observation_id
)
INSERT INTO _m16_observation_map (tracker_id, observation_id) SELECT 'M16B-O016', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'PNS electrical stimulation can enhance sensory axon growth initiation after SCI, but current evidence suggests it is less robust than conditioning lesion for sustained elongation through CNS lesions.',
    'mechanistic boundary',
    'high',
    'Module 16A tracker / source-page, full-text PMC, or review metadata',
    'high',
    '{"curator_notes": "Direct CNS ES claim.", "source_paper_tracker_id": "M16A-P001", "topic_id": "M16B-T001", "tracker_id": "M16B-C001"}'
  FROM _m16_paper_map p
  WHERE p.tracker_id = 'M16A-P001'
  RETURNING claim_id
)
INSERT INTO _m16_claim_map (tracker_id, claim_id) SELECT 'M16B-C001', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Sciatic nerve stimulation can activate spinal afferent-terminal metabolism without necessarily activating DRG soma metabolism.',
    'mechanistic boundary',
    'high',
    'Module 16A tracker / source-page, full-text PMC, or review metadata',
    'high',
    '{"curator_notes": "Compartment claim.", "source_paper_tracker_id": "M16A-P002", "topic_id": "M16B-T002", "tracker_id": "M16B-C002"}'
  FROM _m16_paper_map p
  WHERE p.tracker_id = 'M16A-P002'
  RETURNING claim_id
)
INSERT INTO _m16_claim_map (tracker_id, claim_id) SELECT 'M16B-C002', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Brief PNS electrical stimulation has strong peripheral nerve repair and DRG neurite evidence, but CNS repair claims need separate central-branch testing.',
    'boundary condition',
    'high',
    'Module 16A tracker / source-page, full-text PMC, or review metadata',
    'high',
    '{"curator_notes": "Translation boundary.", "source_paper_tracker_id": "M16A-P003", "topic_id": "M16B-T003", "tracker_id": "M16B-C003"}'
  FROM _m16_paper_map p
  WHERE p.tracker_id = 'M16A-P003'
  RETURNING claim_id
)
INSERT INTO _m16_claim_map (tracker_id, claim_id) SELECT 'M16B-C003', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Electrical stimulation overlaps with conditioning lesion molecular pathways but should not be treated as fully equivalent to crush or axotomy conditioning.',
    'boundary condition',
    'high',
    'Module 16A tracker / source-page, full-text PMC, or review metadata',
    'high',
    '{"curator_notes": "Review-supported equivalence boundary.", "source_paper_tracker_id": "M16A-P004", "topic_id": "M16B-T001", "tracker_id": "M16B-C004"}'
  FROM _m16_paper_map p
  WHERE p.tracker_id = 'M16A-P004'
  RETURNING claim_id
)
INSERT INTO _m16_claim_map (tracker_id, claim_id) SELECT 'M16B-C004', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Peripheral axotomy preconditioning remains the benchmark for central sensory axon growth beyond dorsal column lesion.',
    'comparator',
    'medium',
    'Module 16A tracker / source-page, full-text PMC, or review metadata',
    'medium',
    '{"curator_notes": "Comparator claim.", "source_paper_tracker_id": "M16A-P005", "topic_id": "M16B-T004", "tracker_id": "M16B-C005"}'
  FROM _m16_paper_map p
  WHERE p.tracker_id = 'M16A-P005'
  RETURNING claim_id
)
INSERT INTO _m16_claim_map (tracker_id, claim_id) SELECT 'M16B-C005', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Conditioning lesion recruits broader gene-expression mechanisms than cAMP, so ES should be evaluated against broad growth-state readouts rather than a single pathway marker.',
    'comparator',
    'high',
    'Module 16A tracker / source-page, full-text PMC, or review metadata',
    'high',
    '{"curator_notes": "Mechanistic benchmark.", "source_paper_tracker_id": "M16A-P006", "topic_id": "M16B-T004", "tracker_id": "M16B-C006"}'
  FROM _m16_paper_map p
  WHERE p.tracker_id = 'M16A-P006'
  RETURNING claim_id
)
INSERT INTO _m16_claim_map (tracker_id, claim_id) SELECT 'M16B-C006', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'STAT3 activation is a useful benchmark readout for DRG conditioning-like effects.',
    'comparator',
    'high',
    'Module 16A tracker / source-page, full-text PMC, or review metadata',
    'high',
    '{"curator_notes": "Pathway benchmark.", "source_paper_tracker_id": "M16A-P007", "topic_id": "M16B-T004", "tracker_id": "M16B-C007"}'
  FROM _m16_paper_map p
  WHERE p.tracker_id = 'M16A-P007'
  RETURNING claim_id
)
INSERT INTO _m16_claim_map (tracker_id, claim_id) SELECT 'M16B-C007', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Activity-state and redox pathways may synergize with conditioning, so ES experiments should assay more than electrical activation alone.',
    'synthesis',
    'medium',
    'Module 16A tracker / source-page, full-text PMC, or review metadata',
    'medium',
    '{"curator_notes": "Activity synergy claim.", "source_paper_tracker_id": "M16A-P008", "topic_id": "M16B-T005", "tracker_id": "M16B-C008"}'
  FROM _m16_paper_map p
  WHERE p.tracker_id = 'M16A-P008'
  RETURNING claim_id
)
INSERT INTO _m16_claim_map (tracker_id, claim_id) SELECT 'M16B-C008', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Branch-specific conditioning evidence warns against assuming peripheral nerve growth effects automatically translate to central branch regeneration.',
    'boundary condition',
    'high',
    'Module 16A tracker / source-page, full-text PMC, or review metadata',
    'high',
    '{"curator_notes": "Negative comparator.", "source_paper_tracker_id": "M16A-P009", "topic_id": "M16B-T004", "tracker_id": "M16B-C009"}'
  FROM _m16_paper_map p
  WHERE p.tracker_id = 'M16A-P009'
  RETURNING claim_id
)
INSERT INTO _m16_claim_map (tracker_id, claim_id) SELECT 'M16B-C009', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'ES studies should distinguish neurite initiation, outgrowth rate, elongation, and branching because conditioning lesions affect these dimensions differently.',
    'evidence standard',
    'medium',
    'Module 16A tracker / source-page, full-text PMC, or review metadata',
    'medium',
    '{"curator_notes": "Endpoint granularity claim.", "source_paper_tracker_id": "M16A-P010", "topic_id": "M16B-T004", "tracker_id": "M16B-C010"}'
  FROM _m16_paper_map p
  WHERE p.tracker_id = 'M16A-P010'
  RETURNING claim_id
)
INSERT INTO _m16_claim_map (tracker_id, claim_id) SELECT 'M16B-C010', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Remote DRG priming after lesion conditioning is real, but electrical stimulation requires direct evidence before remote or contralateral DRG priming is inferred.',
    'boundary condition',
    'high',
    'Module 16A tracker / source-page, full-text PMC, or review metadata',
    'high',
    '{"curator_notes": "Remote-effect boundary.", "source_paper_tracker_id": "M16A-P011", "topic_id": "M16B-T006", "tracker_id": "M16B-C011"}'
  FROM _m16_paper_map p
  WHERE p.tracker_id = 'M16A-P011'
  RETURNING claim_id
)
INSERT INTO _m16_claim_map (tracker_id, claim_id) SELECT 'M16B-C011', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'ES conditioning experiments must preserve sequence and timing because conditioning effects vary when peripheral stimulation or lesioning occurs before versus after CNS injury.',
    'evidence standard',
    'high',
    'Module 16A tracker / source-page, full-text PMC, or review metadata',
    'high',
    '{"curator_notes": "Timing claim.", "source_paper_tracker_id": "M16A-P012", "topic_id": "M16B-T004", "tracker_id": "M16B-C012"}'
  FROM _m16_paper_map p
  WHERE p.tracker_id = 'M16A-P012'
  RETURNING claim_id
)
INSERT INTO _m16_claim_map (tracker_id, claim_id) SELECT 'M16B-C012', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Conditioning biology is interval-dependent, making stimulation schedule a mechanistic variable rather than simple protocol metadata.',
    'evidence standard',
    'medium',
    'Module 16A tracker / source-page, full-text PMC, or review metadata',
    'medium',
    '{"curator_notes": "Schedule claim.", "source_paper_tracker_id": "M16A-P013", "topic_id": "M16B-T004", "tracker_id": "M16B-C013"}'
  FROM _m16_paper_map p
  WHERE p.tracker_id = 'M16A-P013'
  RETURNING claim_id
)
INSERT INTO _m16_claim_map (tracker_id, claim_id) SELECT 'M16B-C013', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'AMPK and metabolic growth-state pathways are candidate readouts for PNS ES preconditioning studies.',
    'target nomination',
    'medium',
    'Module 16A tracker / source-page, full-text PMC, or review metadata',
    'medium',
    '{"curator_notes": "Readout candidate.", "source_paper_tracker_id": "M16A-P014", "topic_id": "M16B-T005", "tracker_id": "M16B-C014"}'
  FROM _m16_paper_map p
  WHERE p.tracker_id = 'M16A-P014'
  RETURNING claim_id
)
INSERT INTO _m16_claim_map (tracker_id, claim_id) SELECT 'M16B-C014', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'The dorsal column model is the appropriate central-branch assay for testing whether PNS ES improves DRG sensory axon regeneration after SCI.',
    'model boundary',
    'medium',
    'Module 16A tracker / source-page, full-text PMC, or review metadata',
    'medium',
    '{"curator_notes": "Model ontology claim.", "source_paper_tracker_id": "M16A-P015", "topic_id": "M16B-T008", "tracker_id": "M16B-C015"}'
  FROM _m16_paper_map p
  WHERE p.tracker_id = 'M16A-P015'
  RETURNING claim_id
)
INSERT INTO _m16_claim_map (tracker_id, claim_id) SELECT 'M16B-C015', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'ES-enabled regeneration strategies must include chronic functional physiology and sensory-pathophysiology safety endpoints.',
    'safety boundary',
    'high',
    'Module 16A tracker / source-page, full-text PMC, or review metadata',
    'high',
    '{"curator_notes": "Chronic endpoint claim.", "source_paper_tracker_id": "M16A-P016", "topic_id": "M16B-T007", "tracker_id": "M16B-C016"}'
  FROM _m16_paper_map p
  WHERE p.tracker_id = 'M16A-P016'
  RETURNING claim_id
)
INSERT INTO _m16_claim_map (tracker_id, claim_id) SELECT 'M16B-C016', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct ES-plus-SCI observation.", "strength": "high", "tracker_id": "M16B-L001"}'
  FROM _m16_claim_map c
  JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O001'
  WHERE c.tracker_id = 'M16B-C001'
  RETURNING link_id
)
INSERT INTO _m16_link_map (tracker_id, link_id) SELECT 'M16B-L001', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct compartment observation.", "strength": "high", "tracker_id": "M16B-L002"}'
  FROM _m16_claim_map c
  JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O002'
  WHERE c.tracker_id = 'M16B-C002'
  RETURNING link_id
)
INSERT INTO _m16_link_map (tracker_id, link_id) SELECT 'M16B-L002', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct brief ES review observation.", "strength": "high", "tracker_id": "M16B-L003"}'
  FROM _m16_claim_map c
  JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O003'
  WHERE c.tracker_id = 'M16B-C003'
  RETURNING link_id
)
INSERT INTO _m16_link_map (tracker_id, link_id) SELECT 'M16B-L003', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct review-supported equivalence boundary.", "strength": "high", "tracker_id": "M16B-L004"}'
  FROM _m16_claim_map c
  JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O004'
  WHERE c.tracker_id = 'M16B-C004'
  RETURNING link_id
)
INSERT INTO _m16_link_map (tracker_id, link_id) SELECT 'M16B-L004', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Comparator observation.", "strength": "medium", "tracker_id": "M16B-L005"}'
  FROM _m16_claim_map c
  JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O005'
  WHERE c.tracker_id = 'M16B-C005'
  RETURNING link_id
)
INSERT INTO _m16_link_map (tracker_id, link_id) SELECT 'M16B-L005', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Comparator observation.", "strength": "high", "tracker_id": "M16B-L006"}'
  FROM _m16_claim_map c
  JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O006'
  WHERE c.tracker_id = 'M16B-C006'
  RETURNING link_id
)
INSERT INTO _m16_link_map (tracker_id, link_id) SELECT 'M16B-L006', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "STAT3 comparator observation.", "strength": "high", "tracker_id": "M16B-L007"}'
  FROM _m16_claim_map c
  JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O007'
  WHERE c.tracker_id = 'M16B-C007'
  RETURNING link_id
)
INSERT INTO _m16_link_map (tracker_id, link_id) SELECT 'M16B-L007', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Activity-state comparator observation.", "strength": "medium", "tracker_id": "M16B-L008"}'
  FROM _m16_claim_map c
  JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O008'
  WHERE c.tracker_id = 'M16B-C008'
  RETURNING link_id
)
INSERT INTO _m16_link_map (tracker_id, link_id) SELECT 'M16B-L008', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Branch-specific boundary observation.", "strength": "high", "tracker_id": "M16B-L009"}'
  FROM _m16_claim_map c
  JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O009'
  WHERE c.tracker_id = 'M16B-C009'
  RETURNING link_id
)
INSERT INTO _m16_link_map (tracker_id, link_id) SELECT 'M16B-L009', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Neurite morphology comparator observation.", "strength": "medium", "tracker_id": "M16B-L010"}'
  FROM _m16_claim_map c
  JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O010'
  WHERE c.tracker_id = 'M16B-C010'
  RETURNING link_id
)
INSERT INTO _m16_link_map (tracker_id, link_id) SELECT 'M16B-L010', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Remote DRG comparator observation.", "strength": "high", "tracker_id": "M16B-L011"}'
  FROM _m16_claim_map c
  JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O011'
  WHERE c.tracker_id = 'M16B-C011'
  RETURNING link_id
)
INSERT INTO _m16_link_map (tracker_id, link_id) SELECT 'M16B-L011', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Timing commentary observation.", "strength": "high", "tracker_id": "M16B-L012"}'
  FROM _m16_claim_map c
  JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O012'
  WHERE c.tracker_id = 'M16B-C012'
  RETURNING link_id
)
INSERT INTO _m16_link_map (tracker_id, link_id) SELECT 'M16B-L012', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Interval timing observation.", "strength": "medium", "tracker_id": "M16B-L013"}'
  FROM _m16_claim_map c
  JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O013'
  WHERE c.tracker_id = 'M16B-C013'
  RETURNING link_id
)
INSERT INTO _m16_link_map (tracker_id, link_id) SELECT 'M16B-L013', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "AMPK readout observation.", "strength": "medium", "tracker_id": "M16B-L014"}'
  FROM _m16_claim_map c
  JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O014'
  WHERE c.tracker_id = 'M16B-C014'
  RETURNING link_id
)
INSERT INTO _m16_link_map (tracker_id, link_id) SELECT 'M16B-L014', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Dorsal column assay observation.", "strength": "medium", "tracker_id": "M16B-L015"}'
  FROM _m16_claim_map c
  JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O015'
  WHERE c.tracker_id = 'M16B-C015'
  RETURNING link_id
)
INSERT INTO _m16_link_map (tracker_id, link_id) SELECT 'M16B-L015', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Chronic physiology safety observation.", "strength": "high", "tracker_id": "M16B-L016"}'
  FROM _m16_claim_map c
  JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O016'
  WHERE c.tracker_id = 'M16B-C016'
  RETURNING link_id
)
INSERT INTO _m16_link_map (tracker_id, link_id) SELECT 'M16B-L016', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Review reinforces partial mimicry boundary.", "strength": "low", "tracker_id": "M16B-L017"}'
  FROM _m16_claim_map c
  JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O004'
  WHERE c.tracker_id = 'M16B-C001'
  RETURNING link_id
)
INSERT INTO _m16_link_map (tracker_id, link_id) SELECT 'M16B-L017', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Lesion benchmark contextualizes ES effect size.", "strength": "low", "tracker_id": "M16B-L018"}'
  FROM _m16_claim_map c
  JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O005'
  WHERE c.tracker_id = 'M16B-C001'
  RETURNING link_id
)
INSERT INTO _m16_link_map (tracker_id, link_id) SELECT 'M16B-L018', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Dorsal column model contextualizes afferent pathway.", "strength": "low", "tracker_id": "M16B-L019"}'
  FROM _m16_claim_map c
  JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O015'
  WHERE c.tracker_id = 'M16B-C002'
  RETURNING link_id
)
INSERT INTO _m16_link_map (tracker_id, link_id) SELECT 'M16B-L019', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Direct CNS ES row limits peripheral repair extrapolation.", "strength": "low", "tracker_id": "M16B-L020"}'
  FROM _m16_claim_map c
  JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O001'
  WHERE c.tracker_id = 'M16B-C003'
  RETURNING link_id
)
INSERT INTO _m16_link_map (tracker_id, link_id) SELECT 'M16B-L020', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Broad gene program comparator supports non-equivalence.", "strength": "low", "tracker_id": "M16B-L021"}'
  FROM _m16_claim_map c
  JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O006'
  WHERE c.tracker_id = 'M16B-C004'
  RETURNING link_id
)
INSERT INTO _m16_link_map (tracker_id, link_id) SELECT 'M16B-L021', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Branch-specific comparator supports non-equivalence.", "strength": "low", "tracker_id": "M16B-L022"}'
  FROM _m16_claim_map c
  JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O009'
  WHERE c.tracker_id = 'M16B-C004'
  RETURNING link_id
)
INSERT INTO _m16_link_map (tracker_id, link_id) SELECT 'M16B-L022', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "ES row compares against lesion benchmark.", "strength": "low", "tracker_id": "M16B-L023"}'
  FROM _m16_claim_map c
  JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O001'
  WHERE c.tracker_id = 'M16B-C005'
  RETURNING link_id
)
INSERT INTO _m16_link_map (tracker_id, link_id) SELECT 'M16B-L023', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "STAT3 row supports broad-growth-state readout.", "strength": "low", "tracker_id": "M16B-L024"}'
  FROM _m16_claim_map c
  JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O007'
  WHERE c.tracker_id = 'M16B-C006'
  RETURNING link_id
)
INSERT INTO _m16_link_map (tracker_id, link_id) SELECT 'M16B-L024', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Neurite phenotype row supports multi-endpoint readout.", "strength": "low", "tracker_id": "M16B-L025"}'
  FROM _m16_claim_map c
  JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O010'
  WHERE c.tracker_id = 'M16B-C006'
  RETURNING link_id
)
INSERT INTO _m16_link_map (tracker_id, link_id) SELECT 'M16B-L025', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Enriched conditioning includes STAT3/redox context.", "strength": "low", "tracker_id": "M16B-L026"}'
  FROM _m16_claim_map c
  JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O008'
  WHERE c.tracker_id = 'M16B-C007'
  RETURNING link_id
)
INSERT INTO _m16_link_map (tracker_id, link_id) SELECT 'M16B-L026', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "AMPK row supports metabolic readout context.", "strength": "low", "tracker_id": "M16B-L027"}'
  FROM _m16_claim_map c
  JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O014'
  WHERE c.tracker_id = 'M16B-C008'
  RETURNING link_id
)
INSERT INTO _m16_link_map (tracker_id, link_id) SELECT 'M16B-L027', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Dorsal column model supports branch-specific assay boundary.", "strength": "low", "tracker_id": "M16B-L028"}'
  FROM _m16_claim_map c
  JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O015'
  WHERE c.tracker_id = 'M16B-C009'
  RETURNING link_id
)
INSERT INTO _m16_link_map (tracker_id, link_id) SELECT 'M16B-L028', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Brief ES DRG neurite row supports endpoint granularity.", "strength": "low", "tracker_id": "M16B-L029"}'
  FROM _m16_claim_map c
  JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O003'
  WHERE c.tracker_id = 'M16B-C010'
  RETURNING link_id
)
INSERT INTO _m16_link_map (tracker_id, link_id) SELECT 'M16B-L029', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Brief ES row lacks remote DRG proof and supports boundary.", "strength": "low", "tracker_id": "M16B-L030"}'
  FROM _m16_claim_map c
  JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O003'
  WHERE c.tracker_id = 'M16B-C011'
  RETURNING link_id
)
INSERT INTO _m16_link_map (tracker_id, link_id) SELECT 'M16B-L030', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Interval row reinforces timing boundary.", "strength": "low", "tracker_id": "M16B-L031"}'
  FROM _m16_claim_map c
  JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O013'
  WHERE c.tracker_id = 'M16B-C012'
  RETURNING link_id
)
INSERT INTO _m16_link_map (tracker_id, link_id) SELECT 'M16B-L031', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Sequence row reinforces schedule boundary.", "strength": "low", "tracker_id": "M16B-L032"}'
  FROM _m16_claim_map c
  JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O012'
  WHERE c.tracker_id = 'M16B-C013'
  RETURNING link_id
)
INSERT INTO _m16_link_map (tracker_id, link_id) SELECT 'M16B-L032', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Metabolic stimulation row supports pathway-readout design.", "strength": "low", "tracker_id": "M16B-L033"}'
  FROM _m16_claim_map c
  JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O002'
  WHERE c.tracker_id = 'M16B-C014'
  RETURNING link_id
)
INSERT INTO _m16_link_map (tracker_id, link_id) SELECT 'M16B-L033', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Lesion benchmark supports dorsal column assay choice.", "strength": "low", "tracker_id": "M16B-L034"}'
  FROM _m16_claim_map c
  JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O005'
  WHERE c.tracker_id = 'M16B-C015'
  RETURNING link_id
)
INSERT INTO _m16_link_map (tracker_id, link_id) SELECT 'M16B-L034', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Direct ES row needs chronic functional follow-up.", "strength": "low", "tracker_id": "M16B-L035"}'
  FROM _m16_claim_map c
  JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O001'
  WHERE c.tracker_id = 'M16B-C016'
  RETURNING link_id
)
INSERT INTO _m16_link_map (tracker_id, link_id) SELECT 'M16B-L035', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Peripheral repair ES row needs CNS safety separation.", "strength": "low", "tracker_id": "M16B-L036"}'
  FROM _m16_claim_map c
  JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O003'
  WHERE c.tracker_id = 'M16B-C016'
  RETURNING link_id
)
INSERT INTO _m16_link_map (tracker_id, link_id) SELECT 'M16B-L036', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "ES-plus-SCI row contextualizes activity-state hypothesis.", "strength": "low", "tracker_id": "M16B-L037"}'
  FROM _m16_claim_map c
  JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O001'
  WHERE c.tracker_id = 'M16B-C008'
  RETURNING link_id
)
INSERT INTO _m16_link_map (tracker_id, link_id) SELECT 'M16B-L037', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Timing row supports avoiding remote inference without direct schedule/side data.", "strength": "low", "tracker_id": "M16B-L038"}'
  FROM _m16_claim_map c
  JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O012'
  WHERE c.tracker_id = 'M16B-C011'
  RETURNING link_id
)
INSERT INTO _m16_link_map (tracker_id, link_id) SELECT 'M16B-L038', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Branch-specific row supports central-branch assay requirement.", "strength": "low", "tracker_id": "M16B-L039"}'
  FROM _m16_claim_map c
  JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O009'
  WHERE c.tracker_id = 'M16B-C015'
  RETURNING link_id
)
INSERT INTO _m16_link_map (tracker_id, link_id) SELECT 'M16B-L039', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Chronic physiology row reinforces safety boundary.", "strength": "low", "tracker_id": "M16B-L040"}'
  FROM _m16_claim_map c
  JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O016'
  WHERE c.tracker_id = 'M16B-C016'
  RETURNING link_id
)
INSERT INTO _m16_link_map (tracker_id, link_id) SELECT 'M16B-L040', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'PNS electrical stimulation is consensus-ready as a non-destructive conditioning-like strategy that can enhance sensory axon growth initiation, but current evidence does not support treating it as fully equivalent to peripheral nerve crush or axotomy conditioning for sustained central regeneration through SCI lesions.',
    'M16B-T001',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M16B-B001", "M16B-B002", "M16B-B003", "M16B-B004", "M16B-B005", "M16B-B006", "M16B-B007", "M16B-B008"], "claim_tracker_ids": ["M16B-C001", "M16B-C002", "M16B-C003", "M16B-C004"], "consensus_draft_id": "M16B-S001", "observation_tracker_ids": ["M16B-O001", "M16B-O002", "M16B-O003", "M16B-O004"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 16 first-pass curation freeze.", "topic_id": "M16B-T001"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m16_consensus_map (tracker_id, consensus_id) SELECT 'M16B-S001', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m16_consensus_map c
JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O001'
WHERE c.tracker_id = 'M16B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m16_consensus_map c
JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O002'
WHERE c.tracker_id = 'M16B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m16_consensus_map c
JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O003'
WHERE c.tracker_id = 'M16B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m16_consensus_map c
JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O004'
WHERE c.tracker_id = 'M16B-S001';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Sciatic nerve stimulation can activate spinal afferent-terminal metabolism without parallel DRG soma metabolic activation, so PNS ES studies must distinguish peripheral axon, spinal terminal, DRG cell body, and central lesion compartments.',
    'M16B-T002',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M16B-B001", "M16B-B002", "M16B-B003", "M16B-B004", "M16B-B005", "M16B-B006", "M16B-B007", "M16B-B008"], "claim_tracker_ids": ["M16B-C002"], "consensus_draft_id": "M16B-S002", "observation_tracker_ids": ["M16B-O002"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 16 first-pass curation freeze.", "topic_id": "M16B-T002"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m16_consensus_map (tracker_id, consensus_id) SELECT 'M16B-S002', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m16_consensus_map c
JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O002'
WHERE c.tracker_id = 'M16B-S002';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Brief electrical stimulation has strong peripheral nerve repair and DRG neurite-outgrowth support, but CNS repair claims require direct central-branch, dorsal-column, lesion-crossing, and chronic functional endpoints.',
    'M16B-T003',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M16B-B001", "M16B-B002", "M16B-B003", "M16B-B004", "M16B-B005", "M16B-B006", "M16B-B007", "M16B-B008"], "claim_tracker_ids": ["M16B-C001", "M16B-C002", "M16B-C003", "M16B-C004"], "consensus_draft_id": "M16B-S003", "observation_tracker_ids": ["M16B-O001", "M16B-O002", "M16B-O003", "M16B-O004"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 16 first-pass curation freeze.", "topic_id": "M16B-T003"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m16_consensus_map (tracker_id, consensus_id) SELECT 'M16B-S003', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m16_consensus_map c
JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O001'
WHERE c.tracker_id = 'M16B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m16_consensus_map c
JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O002'
WHERE c.tracker_id = 'M16B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m16_consensus_map c
JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O003'
WHERE c.tracker_id = 'M16B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m16_consensus_map c
JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O004'
WHERE c.tracker_id = 'M16B-S003';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Conditioning lesion biology should be used as the benchmark for ES preconditioning: cAMP, STAT3, transcriptional programs, timing, interval, and branch-specific outcomes define what must be measured before claiming ES has induced a true DRG growth state.',
    'M16B-T004',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M16B-B001", "M16B-B002", "M16B-B003", "M16B-B004", "M16B-B005", "M16B-B006", "M16B-B007", "M16B-B008"], "claim_tracker_ids": ["M16B-C005", "M16B-C006", "M16B-C007", "M16B-C008", "M16B-C009", "M16B-C010", "M16B-C011", "M16B-C012", "M16B-C013"], "consensus_draft_id": "M16B-S004", "observation_tracker_ids": ["M16B-O005", "M16B-O006", "M16B-O007", "M16B-O008", "M16B-O009", "M16B-O010", "M16B-O011", "M16B-O012", "M16B-O013"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 16 first-pass curation freeze.", "topic_id": "M16B-T004"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m16_consensus_map (tracker_id, consensus_id) SELECT 'M16B-S004', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m16_consensus_map c
JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O005'
WHERE c.tracker_id = 'M16B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m16_consensus_map c
JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O006'
WHERE c.tracker_id = 'M16B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m16_consensus_map c
JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O007'
WHERE c.tracker_id = 'M16B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m16_consensus_map c
JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O008'
WHERE c.tracker_id = 'M16B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m16_consensus_map c
JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O009'
WHERE c.tracker_id = 'M16B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m16_consensus_map c
JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O010'
WHERE c.tracker_id = 'M16B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m16_consensus_map c
JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O011'
WHERE c.tracker_id = 'M16B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m16_consensus_map c
JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O012'
WHERE c.tracker_id = 'M16B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m16_consensus_map c
JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O013'
WHERE c.tracker_id = 'M16B-S004';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Activity-state and metabolic pathways, including PKC-STAT3-NOX2 redox signaling and AMPK-linked regenerative ability, are candidate readouts for PNS ES preconditioning but need direct perturbation in ES-conditioned SCI models.',
    'M16B-T005',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M16B-B001", "M16B-B002", "M16B-B003", "M16B-B004", "M16B-B005", "M16B-B006", "M16B-B007", "M16B-B008"], "claim_tracker_ids": ["M16B-C008", "M16B-C009", "M16B-C010", "M16B-C011", "M16B-C012", "M16B-C013", "M16B-C014"], "consensus_draft_id": "M16B-S005", "observation_tracker_ids": ["M16B-O008", "M16B-O009", "M16B-O010", "M16B-O011", "M16B-O012", "M16B-O013", "M16B-O014"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 16 first-pass curation freeze.", "topic_id": "M16B-T005"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m16_consensus_map (tracker_id, consensus_id) SELECT 'M16B-S005', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m16_consensus_map c
JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O008'
WHERE c.tracker_id = 'M16B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m16_consensus_map c
JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O009'
WHERE c.tracker_id = 'M16B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m16_consensus_map c
JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O010'
WHERE c.tracker_id = 'M16B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m16_consensus_map c
JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O011'
WHERE c.tracker_id = 'M16B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m16_consensus_map c
JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O012'
WHERE c.tracker_id = 'M16B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m16_consensus_map c
JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O013'
WHERE c.tracker_id = 'M16B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m16_consensus_map c
JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O014'
WHERE c.tracker_id = 'M16B-S005';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Remote or contralateral DRG priming is established for unilateral sciatic lesion conditioning, but PNS electrical stimulation should not inherit that claim until experiments directly measure side, segment, associated versus non-associated DRGs, and later CNS repair endpoints.',
    'M16B-T006',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M16B-B001", "M16B-B002", "M16B-B003", "M16B-B004", "M16B-B005", "M16B-B006", "M16B-B007", "M16B-B008"], "claim_tracker_ids": ["M16B-C011"], "consensus_draft_id": "M16B-S006", "observation_tracker_ids": ["M16B-O011"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 16 first-pass curation freeze.", "topic_id": "M16B-T006"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m16_consensus_map (tracker_id, consensus_id) SELECT 'M16B-S006', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m16_consensus_map c
JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O011'
WHERE c.tracker_id = 'M16B-S006';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'ES-enabled regeneration strategies should include chronic sensory physiology and maladaptive plasticity endpoints because regenerating afferents may remain pathophysiological even when anatomical growth is achieved.',
    'M16B-T007',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M16B-B001", "M16B-B002", "M16B-B003", "M16B-B004", "M16B-B005", "M16B-B006", "M16B-B007", "M16B-B008"], "claim_tracker_ids": ["M16B-C016"], "consensus_draft_id": "M16B-S007", "observation_tracker_ids": ["M16B-O016"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 16 first-pass curation freeze.", "topic_id": "M16B-T007"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m16_consensus_map (tracker_id, consensus_id) SELECT 'M16B-S007', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m16_consensus_map c
JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O016'
WHERE c.tracker_id = 'M16B-S007';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Module 16 should function as the PNS electrical-stimulation preconditioning layer: candidate studies should specify nerve target, intact or injured nerve status, stimulation parameters, timing, DRG and spinal readouts, lesion model, and whether the endpoint is peripheral repair, central initiation, lesion traversal, growth beyond lesion, or functional recovery.',
    'M16B-T008',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M16B-B001", "M16B-B002", "M16B-B003", "M16B-B004", "M16B-B005", "M16B-B006", "M16B-B007", "M16B-B008"], "claim_tracker_ids": ["M16B-C001", "M16B-C002", "M16B-C003", "M16B-C004", "M16B-C005", "M16B-C006", "M16B-C007", "M16B-C008", "M16B-C009", "M16B-C010", "M16B-C011", "M16B-C012", "M16B-C013", "M16B-C014", "M16B-C015", "M16B-C016"], "consensus_draft_id": "M16B-S008", "observation_tracker_ids": ["M16B-O001", "M16B-O002", "M16B-O003", "M16B-O004", "M16B-O005", "M16B-O006", "M16B-O007", "M16B-O008", "M16B-O009", "M16B-O010", "M16B-O011", "M16B-O012", "M16B-O013", "M16B-O014", "M16B-O015", "M16B-O016"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 16 first-pass curation freeze.", "topic_id": "M16B-T008"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m16_consensus_map (tracker_id, consensus_id) SELECT 'M16B-S008', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m16_consensus_map c
JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O001'
WHERE c.tracker_id = 'M16B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m16_consensus_map c
JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O002'
WHERE c.tracker_id = 'M16B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m16_consensus_map c
JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O003'
WHERE c.tracker_id = 'M16B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m16_consensus_map c
JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O004'
WHERE c.tracker_id = 'M16B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m16_consensus_map c
JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O005'
WHERE c.tracker_id = 'M16B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m16_consensus_map c
JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O006'
WHERE c.tracker_id = 'M16B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m16_consensus_map c
JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O007'
WHERE c.tracker_id = 'M16B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m16_consensus_map c
JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O008'
WHERE c.tracker_id = 'M16B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m16_consensus_map c
JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O009'
WHERE c.tracker_id = 'M16B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m16_consensus_map c
JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O010'
WHERE c.tracker_id = 'M16B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m16_consensus_map c
JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O011'
WHERE c.tracker_id = 'M16B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m16_consensus_map c
JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O012'
WHERE c.tracker_id = 'M16B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m16_consensus_map c
JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O013'
WHERE c.tracker_id = 'M16B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m16_consensus_map c
JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O014'
WHERE c.tracker_id = 'M16B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m16_consensus_map c
JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O015'
WHERE c.tracker_id = 'M16B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m16_consensus_map c
JOIN _m16_observation_map o ON o.tracker_id = 'M16B-O016'
WHERE c.tracker_id = 'M16B-S008';

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
  SELECT COUNT(*) INTO paper_count FROM _m16_paper_map;
  SELECT COUNT(*) INTO experiment_count FROM _m16_experiment_map;
  SELECT COUNT(*) INTO observation_count FROM _m16_observation_map;
  SELECT COUNT(*) INTO claim_count FROM _m16_claim_map;
  SELECT COUNT(*) INTO link_count FROM _m16_link_map;
  SELECT COUNT(*) INTO consensus_count FROM _m16_consensus_map;
  SELECT COUNT(*) INTO consensus_observation_count
  FROM Consensus_Observation co
  JOIN _m16_consensus_map cm ON cm.consensus_id = co.consensus_id;
  IF paper_count <> 16 THEN RAISE EXCEPTION 'Expected 16 papers, found %', paper_count; END IF;
  IF experiment_count <> 16 THEN RAISE EXCEPTION 'Unexpected experiment count %', experiment_count; END IF;
  IF observation_count <> 16 THEN RAISE EXCEPTION 'Expected 16 observations, found %', observation_count; END IF;
  IF claim_count <> 16 THEN RAISE EXCEPTION 'Expected 16 claims, found %', claim_count; END IF;
  IF link_count <> 40 THEN RAISE EXCEPTION 'Expected 40 evidence links, found %', link_count; END IF;
  IF consensus_count <> 8 THEN RAISE EXCEPTION 'Expected 8 consensus rows, found %', consensus_count; END IF;
  IF consensus_observation_count <> 43 THEN RAISE EXCEPTION 'Unexpected consensus-observation count %', consensus_observation_count; END IF;
END $$;

COMMIT;
