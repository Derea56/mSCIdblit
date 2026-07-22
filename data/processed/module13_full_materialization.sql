-- Module 13B full first-pass materialization generated from tracker-derived JSON.
-- This script is intended for a fresh database loaded with schema/schema.sql and scripts/seed_controlled_vocab.sql.
BEGIN;

CREATE TEMP TABLE _m13_paper_map (tracker_id TEXT PRIMARY KEY, paper_id INTEGER NOT NULL);
CREATE TEMP TABLE _m13_paradigm_map (tracker_id TEXT PRIMARY KEY, paradigm_id INTEGER NOT NULL);
CREATE TEMP TABLE _m13_experiment_map (tracker_id TEXT PRIMARY KEY, experiment_id INTEGER NOT NULL);
CREATE TEMP TABLE _m13_observation_map (tracker_id TEXT PRIMARY KEY, observation_id INTEGER NOT NULL);
CREATE TEMP TABLE _m13_claim_map (tracker_id TEXT PRIMARY KEY, claim_id INTEGER NOT NULL);
CREATE TEMP TABLE _m13_link_map (tracker_id TEXT PRIMARY KEY, link_id INTEGER NOT NULL);
CREATE TEMP TABLE _m13_consensus_map (tracker_id TEXT PRIMARY KEY, consensus_id INTEGER NOT NULL);

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Correlative analyses of lesion development and functional status after graded spinal cord contusive injuries in the rat', 'Noble', 1989,
    'Experimental Neurology', NULL, NULL,
    NULL, '10.1016/0014-4886(89)90182-9', '2912748',
    NULL, '{"curator_notes": "Graded contusion time course from 15 min to 8 weeks linking hemorrhage, lesion expansion, gray/white matter loss, residual white matter, and function.", "module": "Module 13B", "tracker_id": "M13A-P001"}'
  )
  RETURNING paper_id
)
INSERT INTO _m13_paper_map (tracker_id, paper_id) SELECT 'M13A-P001', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Spatio-temporal progression of grey and white matter damage following contusion injury in rat spinal cord', 'Williams', 2010,
    'PLoS ONE', NULL, NULL,
    NULL, '10.1371/journal.pone.0012042', '20711496',
    NULL, '{"curator_notes": "Controlled contusion time course from 15 min to 10 weeks; gray matter loss rapid by 24 h and white matter loss extends to 1 week.", "module": "Module 13B", "tracker_id": "M13A-P002"}'
  )
  RETURNING paper_id
)
INSERT INTO _m13_paper_map (tracker_id, paper_id) SELECT 'M13A-P002', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'MR-pathologic comparisons of Wallerian degeneration in spinal cord injury', 'Marcillo', 1994,
    'AJNR American Journal of Neuroradiology', NULL, NULL,
    NULL, NULL, '7900580',
    NULL, '{"curator_notes": "Human postmortem MRI-pathology series from 8 days to 23 years after SCI defining ascending/descending Wallerian degeneration.", "module": "Module 13B", "tracker_id": "M13A-P003"}'
  )
  RETURNING paper_id
)
INSERT INTO _m13_paper_map (tracker_id, paper_id) SELECT 'M13A-P003', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Axonal degeneration and demyelination following traumatic spinal cord injury: A systematic review and meta-analysis', 'Hassannejad', 2019,
    'Journal of Chemical Neuroanatomy', NULL, NULL,
    NULL, '10.1016/j.jchemneu.2019.01.009', '30726717',
    NULL, '{"curator_notes": "Systematic review/meta-analysis of animal axonal degeneration and demyelination across SCI phase, model, severity, and level.", "module": "Module 13B", "tracker_id": "M13A-P004"}'
  )
  RETURNING paper_id
)
INSERT INTO _m13_paper_map (tracker_id, paper_id) SELECT 'M13A-P004', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Blood-spinal cord barrier after spinal cord injury: relation to revascularization and wound healing', 'Whetstone', 2003,
    'Journal of Neuroscience Research', NULL, NULL,
    NULL, NULL, '23887829',
    NULL, '{"curator_notes": "Barrier disruption and vascular remodeling time-course anchor.", "module": "Module 13B", "tracker_id": "M13A-P005"}'
  )
  RETURNING paper_id
)
INSERT INTO _m13_paper_map (tracker_id, paper_id) SELECT 'M13A-P005', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'MRI evidence that glibenclamide reduces acute lesion expansion in a rat model of spinal cord injury', 'Simard', 2012,
    'Spinal Cord', NULL, NULL,
    NULL, '10.1038/sc.2012.81', 'PMC4076111',
    NULL, '{"curator_notes": "MRI/histology evidence that hemorrhagic lesion expansion occurs over first 24 h and is modifiable by Sur1-Trpm4 blockade.", "module": "Module 13B", "tracker_id": "M13A-P006"}'
  )
  RETURNING paper_id
)
INSERT INTO _m13_paper_map (tracker_id, paper_id) SELECT 'M13A-P006', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Glial scar borders are formed by newly proliferated, elongated astrocytes that interact to corral inflammatory and fibrotic cells via STAT3-dependent mechanisms after spinal cord injury', 'Wanner', 2013,
    'Journal of Neuroscience', NULL, NULL,
    NULL, '10.1523/JNEUROSCI.2121-13.2013', '23904622',
    NULL, '{"curator_notes": "Astrocytic scar-border formation from 5-14 days corrals inflammatory and fibrotic cells through STAT3-dependent mechanisms.", "module": "Module 13B", "tracker_id": "M13A-P007"}'
  )
  RETURNING paper_id
)
INSERT INTO _m13_paper_map (tracker_id, paper_id) SELECT 'M13A-P007', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Spatiotemporal dynamics of the molecular expression pattern and intercellular interactions in the glial scar response to spinal cord injury', 'Gong', 2023,
    'Cell Death & Disease', NULL, NULL,
    NULL, '10.1038/s41419-022-05069-6', '35788904',
    NULL, '{"curator_notes": "Spatial transcriptomic scar atlas with phases from macrophage infiltration to scar stationary state.", "module": "Module 13B", "tracker_id": "M13A-P008"}'
  )
  RETURNING paper_id
)
INSERT INTO _m13_paper_map (tracker_id, paper_id) SELECT 'M13A-P008', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Astrocytic Ryk signaling coordinates scarring and wound healing after spinal cord injury', 'Shen', 2025,
    'Nature Neuroscience', NULL, NULL,
    NULL, NULL, '40208942',
    NULL, '{"curator_notes": "Astrocyte Ryk signaling regulates astrocyte morphology, border formation, scar size, and multicellular injury responses.", "module": "Module 13B", "tracker_id": "M13A-P009"}'
  )
  RETURNING paper_id
)
INSERT INTO _m13_paper_map (tracker_id, paper_id) SELECT 'M13A-P009', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Derivation and transcriptional reprogramming of border-forming wound repair astrocytes after spinal cord injury or stroke in mice', 'O''Shea', 2024,
    'Nature Neuroscience', NULL, NULL,
    NULL, NULL, '38907165',
    NULL, '{"curator_notes": "Border-forming wound repair astrocytes derive mainly from local mature astrocytes and acquire persistent wound-healing states.", "module": "Module 13B", "tracker_id": "M13A-P010"}'
  )
  RETURNING paper_id
)
INSERT INTO _m13_paper_map (tracker_id, paper_id) SELECT 'M13A-P010', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Heterogeneous fibroblasts contribute to fibrotic scar formation after spinal cord injury in mice and monkeys', 'Xue', 2024,
    'Nature Communications', NULL, NULL,
    NULL, '10.1038/s41467-024-50158-1', '39060269',
    NULL, '{"curator_notes": "Mouse/monkey fibroblast heterogeneity; perivascular and meningeal fibroblast compartments contribute spatially distinct scar domains.", "module": "Module 13B", "tracker_id": "M13A-P011"}'
  )
  RETURNING paper_id
)
INSERT INTO _m13_paper_map (tracker_id, paper_id) SELECT 'M13A-P011', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'TLR4 Deficiency Impairs Oligodendrocyte Formation in the Injured Spinal Cord', 'Church', 2016,
    'Journal of Neuroscience', NULL, NULL,
    NULL, '10.1523/JNEUROSCI.0065-16.2016', '27277810',
    NULL, '{"curator_notes": "Innate signaling boundary: post-SCI inflammation can support debris clearance, oligodendrocyte replacement, remyelination, and recovery.", "module": "Module 13B", "tracker_id": "M13A-P012"}'
  )
  RETURNING paper_id
)
INSERT INTO _m13_paper_map (tracker_id, paper_id) SELECT 'M13A-P012', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Delayed microglial depletion after spinal cord injury reduces chronic inflammation and neurodegeneration in the brain and improves neurological recovery in male mice', 'Li', 2020,
    'Theranostics', NULL, NULL,
    NULL, '10.7150/thno.49199', '33052221',
    NULL, '{"curator_notes": "Microglia/macrophage modulation changes chronic inflammatory and neurodegenerative outcomes.", "module": "Module 13B", "tracker_id": "M13A-P013"}'
  )
  RETURNING paper_id
)
INSERT INTO _m13_paper_map (tracker_id, paper_id) SELECT 'M13A-P013', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Delayed microglial depletion after spinal cord injury reduces chronic inflammation and neurodegeneration in the brain and improves neurological recovery in male mice', 'Li', 2020,
    'Theranostics', NULL, NULL,
    NULL, '10.7150/thno.49199', 'PMC7545988',
    NULL, '{"curator_notes": "Duplicate full-text anchor retained for chronic remote degeneration and behavior boundary.", "module": "Module 13B", "tracker_id": "M13A-P014"}'
  )
  RETURNING paper_id
)
INSERT INTO _m13_paper_map (tracker_id, paper_id) SELECT 'M13A-P014', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Microglia and macrophages promote corralling, wound compaction and recovery after spinal cord injury via Plexin-B2', 'Zhou', 2020,
    'Nature Neuroscience', NULL, NULL,
    NULL, NULL, '33147453',
    NULL, '{"curator_notes": "Microglia/macrophages promote wound corralling and compaction, supporting protective organization rather than simple suppression.", "module": "Module 13B", "tracker_id": "M13A-P015"}'
  )
  RETURNING paper_id
)
INSERT INTO _m13_paper_map (tracker_id, paper_id) SELECT 'M13A-P015', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Testing Pathological Variation of White Matter Tract in Adult Rats after Severe Spinal Cord Injury with MRI', 'Song', 2018,
    'BioMed Research International', NULL, NULL,
    NULL, '10.1155/2018/4068156', 'PMC6252222',
    NULL, '{"curator_notes": "MRI tracks white matter tract pathology after severe thoracic contusion and relates spared white matter to locomotor recovery.", "module": "Module 13B", "tracker_id": "M13A-P016"}'
  )
  RETURNING paper_id
)
INSERT INTO _m13_paper_map (tracker_id, paper_id) SELECT 'M13A-P016', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Histological repair of damaged spinal cord tissue from chronic contusion injury of rat: a LM observation', 'Zhang', 2011,
    'Histology and Histopathology', NULL, NULL,
    NULL, '10.14670/HH-26.45', '21117026',
    NULL, '{"curator_notes": "Chronic contusion lesion histology describing fibrotic, cellular, Schwann-cell, axonal, and cavity zones.", "module": "Module 13B", "tracker_id": "M13A-P017"}'
  )
  RETURNING paper_id
)
INSERT INTO _m13_paper_map (tracker_id, paper_id) SELECT 'M13A-P017', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Reawakening inflammation in the chronically injured spinal cord using lipopolysaccharide induces diverse microglial states', 'Cucarian', 2025,
    'Nature Communications', NULL, NULL,
    NULL, NULL, '40022205',
    NULL, '{"curator_notes": "Chronic SCI microglial plasticity boundary; chronic lesion remains inducible rather than inert.", "module": "Module 13B", "tracker_id": "M13A-P018"}'
  )
  RETURNING paper_id
)
INSERT INTO _m13_paper_map (tracker_id, paper_id) SELECT 'M13A-P018', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Astrocytic Ryk signaling coordinates scarring and wound healing after spinal cord injury', 'Shen', 2025,
    'Nature Neuroscience', NULL, NULL,
    NULL, NULL, '40208942',
    NULL, '{"curator_notes": "Human/rodent astrocytic wound-healing signal bridge.", "module": "Module 13B", "tracker_id": "M13A-P019"}'
  )
  RETURNING paper_id
)
INSERT INTO _m13_paper_map (tracker_id, paper_id) SELECT 'M13A-P019', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Heterogeneous fibroblasts contribute to fibrotic scar formation after spinal cord injury in mice and monkeys', 'Xue', 2024,
    'Nature Communications', NULL, NULL,
    NULL, '10.1038/s41467-024-50158-1', '39060269',
    NULL, '{"curator_notes": "Cross-species fibrotic scar conservation boundary.", "module": "Module 13B", "tracker_id": "M13A-P020"}'
  )
  RETURNING paper_id
)
INSERT INTO _m13_paper_map (tracker_id, paper_id) SELECT 'M13A-P020', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Spatiotemporal dynamics of the molecular expression pattern and intercellular interactions in the glial scar response to spinal cord injury', 'Gong', 2023,
    'Cell Death & Disease', NULL, NULL,
    NULL, '10.1038/s41419-022-05069-6', '35788904',
    NULL, '{"curator_notes": "Ligand-receptor and spatial boundary evidence for multicellular scar architecture.", "module": "Module 13B", "tracker_id": "M13A-P021"}'
  )
  RETURNING paper_id
)
INSERT INTO _m13_paper_map (tracker_id, paper_id) SELECT 'M13A-P021', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Heterogeneity analysis of astrocytes following spinal cord injury at single-cell resolution', 'GEO', 2021,
    'GEO DataSet', NULL, NULL,
    NULL, NULL, 'GSE189070',
    NULL, '{"curator_notes": "Single-cell astrocyte time course at 0.5, 1, 3, 7, 14, 60, and 90 days after mouse hemisection SCI.", "module": "Module 13B", "tracker_id": "M13A-P022"}'
  )
  RETURNING paper_id
)
INSERT INTO _m13_paper_map (tracker_id, paper_id) SELECT 'M13A-P022', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'MR-pathologic comparisons of wallerian degeneration in spinal cord injury', 'Marcillo', 1994,
    'AJNR American Journal of Neuroradiology', NULL, NULL,
    NULL, NULL, 'PMC8337709',
    NULL, '{"curator_notes": "Human cord postmortem MRI-pathology evidence of Wallerian degeneration across days to decades.", "module": "Module 13B", "tracker_id": "M13A-P023"}'
  )
  RETURNING paper_id
)
INSERT INTO _m13_paper_map (tracker_id, paper_id) SELECT 'M13A-P023', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'MRI evidence that glibenclamide reduces acute lesion expansion in a rat model of spinal cord injury', 'Simard', 2012,
    'Spinal Cord', NULL, NULL,
    NULL, '10.1038/sc.2012.81', 'PMC4076111',
    NULL, '{"curator_notes": "Progressive hemorrhagic necrosis intervention anchor showing acute lesion expansion can be reduced.", "module": "Module 13B", "tracker_id": "M13A-P024"}'
  )
  RETURNING paper_id
)
INSERT INTO _m13_paper_map (tracker_id, paper_id) SELECT 'M13A-P024', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 13B curated evidence extraction',
    'First-pass Module 13B traumatic SCI pathobiology and chronic lesion formation curation for M13A-P001',
    'Tracker-derived materialization from Module_13B_TRACKER.md'
  FROM _m13_paper_map WHERE tracker_id = 'M13A-P001'
  RETURNING paradigm_id
)
INSERT INTO _m13_paradigm_map (tracker_id, paradigm_id) SELECT 'M13A-P001', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 13B curated evidence extraction',
    'First-pass Module 13B traumatic SCI pathobiology and chronic lesion formation curation for M13A-P002',
    'Tracker-derived materialization from Module_13B_TRACKER.md'
  FROM _m13_paper_map WHERE tracker_id = 'M13A-P002'
  RETURNING paradigm_id
)
INSERT INTO _m13_paradigm_map (tracker_id, paradigm_id) SELECT 'M13A-P002', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 13B curated evidence extraction',
    'First-pass Module 13B traumatic SCI pathobiology and chronic lesion formation curation for M13A-P003',
    'Tracker-derived materialization from Module_13B_TRACKER.md'
  FROM _m13_paper_map WHERE tracker_id = 'M13A-P003'
  RETURNING paradigm_id
)
INSERT INTO _m13_paradigm_map (tracker_id, paradigm_id) SELECT 'M13A-P003', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 13B curated evidence extraction',
    'First-pass Module 13B traumatic SCI pathobiology and chronic lesion formation curation for M13A-P004',
    'Tracker-derived materialization from Module_13B_TRACKER.md'
  FROM _m13_paper_map WHERE tracker_id = 'M13A-P004'
  RETURNING paradigm_id
)
INSERT INTO _m13_paradigm_map (tracker_id, paradigm_id) SELECT 'M13A-P004', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 13B curated evidence extraction',
    'First-pass Module 13B traumatic SCI pathobiology and chronic lesion formation curation for M13A-P005',
    'Tracker-derived materialization from Module_13B_TRACKER.md'
  FROM _m13_paper_map WHERE tracker_id = 'M13A-P005'
  RETURNING paradigm_id
)
INSERT INTO _m13_paradigm_map (tracker_id, paradigm_id) SELECT 'M13A-P005', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 13B curated evidence extraction',
    'First-pass Module 13B traumatic SCI pathobiology and chronic lesion formation curation for M13A-P006',
    'Tracker-derived materialization from Module_13B_TRACKER.md'
  FROM _m13_paper_map WHERE tracker_id = 'M13A-P006'
  RETURNING paradigm_id
)
INSERT INTO _m13_paradigm_map (tracker_id, paradigm_id) SELECT 'M13A-P006', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 13B curated evidence extraction',
    'First-pass Module 13B traumatic SCI pathobiology and chronic lesion formation curation for M13A-P007',
    'Tracker-derived materialization from Module_13B_TRACKER.md'
  FROM _m13_paper_map WHERE tracker_id = 'M13A-P007'
  RETURNING paradigm_id
)
INSERT INTO _m13_paradigm_map (tracker_id, paradigm_id) SELECT 'M13A-P007', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 13B curated evidence extraction',
    'First-pass Module 13B traumatic SCI pathobiology and chronic lesion formation curation for M13A-P008',
    'Tracker-derived materialization from Module_13B_TRACKER.md'
  FROM _m13_paper_map WHERE tracker_id = 'M13A-P008'
  RETURNING paradigm_id
)
INSERT INTO _m13_paradigm_map (tracker_id, paradigm_id) SELECT 'M13A-P008', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 13B curated evidence extraction',
    'First-pass Module 13B traumatic SCI pathobiology and chronic lesion formation curation for M13A-P009',
    'Tracker-derived materialization from Module_13B_TRACKER.md'
  FROM _m13_paper_map WHERE tracker_id = 'M13A-P009'
  RETURNING paradigm_id
)
INSERT INTO _m13_paradigm_map (tracker_id, paradigm_id) SELECT 'M13A-P009', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 13B curated evidence extraction',
    'First-pass Module 13B traumatic SCI pathobiology and chronic lesion formation curation for M13A-P010',
    'Tracker-derived materialization from Module_13B_TRACKER.md'
  FROM _m13_paper_map WHERE tracker_id = 'M13A-P010'
  RETURNING paradigm_id
)
INSERT INTO _m13_paradigm_map (tracker_id, paradigm_id) SELECT 'M13A-P010', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 13B curated evidence extraction',
    'First-pass Module 13B traumatic SCI pathobiology and chronic lesion formation curation for M13A-P011',
    'Tracker-derived materialization from Module_13B_TRACKER.md'
  FROM _m13_paper_map WHERE tracker_id = 'M13A-P011'
  RETURNING paradigm_id
)
INSERT INTO _m13_paradigm_map (tracker_id, paradigm_id) SELECT 'M13A-P011', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 13B curated evidence extraction',
    'First-pass Module 13B traumatic SCI pathobiology and chronic lesion formation curation for M13A-P012',
    'Tracker-derived materialization from Module_13B_TRACKER.md'
  FROM _m13_paper_map WHERE tracker_id = 'M13A-P012'
  RETURNING paradigm_id
)
INSERT INTO _m13_paradigm_map (tracker_id, paradigm_id) SELECT 'M13A-P012', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 13B curated evidence extraction',
    'First-pass Module 13B traumatic SCI pathobiology and chronic lesion formation curation for M13A-P013',
    'Tracker-derived materialization from Module_13B_TRACKER.md'
  FROM _m13_paper_map WHERE tracker_id = 'M13A-P013'
  RETURNING paradigm_id
)
INSERT INTO _m13_paradigm_map (tracker_id, paradigm_id) SELECT 'M13A-P013', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 13B curated evidence extraction',
    'First-pass Module 13B traumatic SCI pathobiology and chronic lesion formation curation for M13A-P014',
    'Tracker-derived materialization from Module_13B_TRACKER.md'
  FROM _m13_paper_map WHERE tracker_id = 'M13A-P014'
  RETURNING paradigm_id
)
INSERT INTO _m13_paradigm_map (tracker_id, paradigm_id) SELECT 'M13A-P014', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 13B curated evidence extraction',
    'First-pass Module 13B traumatic SCI pathobiology and chronic lesion formation curation for M13A-P015',
    'Tracker-derived materialization from Module_13B_TRACKER.md'
  FROM _m13_paper_map WHERE tracker_id = 'M13A-P015'
  RETURNING paradigm_id
)
INSERT INTO _m13_paradigm_map (tracker_id, paradigm_id) SELECT 'M13A-P015', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 13B curated evidence extraction',
    'First-pass Module 13B traumatic SCI pathobiology and chronic lesion formation curation for M13A-P016',
    'Tracker-derived materialization from Module_13B_TRACKER.md'
  FROM _m13_paper_map WHERE tracker_id = 'M13A-P016'
  RETURNING paradigm_id
)
INSERT INTO _m13_paradigm_map (tracker_id, paradigm_id) SELECT 'M13A-P016', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 13B curated evidence extraction',
    'First-pass Module 13B traumatic SCI pathobiology and chronic lesion formation curation for M13A-P017',
    'Tracker-derived materialization from Module_13B_TRACKER.md'
  FROM _m13_paper_map WHERE tracker_id = 'M13A-P017'
  RETURNING paradigm_id
)
INSERT INTO _m13_paradigm_map (tracker_id, paradigm_id) SELECT 'M13A-P017', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 13B curated evidence extraction',
    'First-pass Module 13B traumatic SCI pathobiology and chronic lesion formation curation for M13A-P018',
    'Tracker-derived materialization from Module_13B_TRACKER.md'
  FROM _m13_paper_map WHERE tracker_id = 'M13A-P018'
  RETURNING paradigm_id
)
INSERT INTO _m13_paradigm_map (tracker_id, paradigm_id) SELECT 'M13A-P018', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 13B curated evidence extraction',
    'First-pass Module 13B traumatic SCI pathobiology and chronic lesion formation curation for M13A-P019',
    'Tracker-derived materialization from Module_13B_TRACKER.md'
  FROM _m13_paper_map WHERE tracker_id = 'M13A-P019'
  RETURNING paradigm_id
)
INSERT INTO _m13_paradigm_map (tracker_id, paradigm_id) SELECT 'M13A-P019', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 13B curated evidence extraction',
    'First-pass Module 13B traumatic SCI pathobiology and chronic lesion formation curation for M13A-P020',
    'Tracker-derived materialization from Module_13B_TRACKER.md'
  FROM _m13_paper_map WHERE tracker_id = 'M13A-P020'
  RETURNING paradigm_id
)
INSERT INTO _m13_paradigm_map (tracker_id, paradigm_id) SELECT 'M13A-P020', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 13B curated evidence extraction',
    'First-pass Module 13B traumatic SCI pathobiology and chronic lesion formation curation for M13A-P021',
    'Tracker-derived materialization from Module_13B_TRACKER.md'
  FROM _m13_paper_map WHERE tracker_id = 'M13A-P021'
  RETURNING paradigm_id
)
INSERT INTO _m13_paradigm_map (tracker_id, paradigm_id) SELECT 'M13A-P021', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 13B curated evidence extraction',
    'First-pass Module 13B traumatic SCI pathobiology and chronic lesion formation curation for M13A-P022',
    'Tracker-derived materialization from Module_13B_TRACKER.md'
  FROM _m13_paper_map WHERE tracker_id = 'M13A-P022'
  RETURNING paradigm_id
)
INSERT INTO _m13_paradigm_map (tracker_id, paradigm_id) SELECT 'M13A-P022', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 13B curated evidence extraction',
    'First-pass Module 13B traumatic SCI pathobiology and chronic lesion formation curation for M13A-P023',
    'Tracker-derived materialization from Module_13B_TRACKER.md'
  FROM _m13_paper_map WHERE tracker_id = 'M13A-P023'
  RETURNING paradigm_id
)
INSERT INTO _m13_paradigm_map (tracker_id, paradigm_id) SELECT 'M13A-P023', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 13B curated evidence extraction',
    'First-pass Module 13B traumatic SCI pathobiology and chronic lesion formation curation for M13A-P024',
    'Tracker-derived materialization from Module_13B_TRACKER.md'
  FROM _m13_paper_map WHERE tracker_id = 'M13A-P024'
  RETURNING paradigm_id
)
INSERT INTO _m13_paradigm_map (tracker_id, paradigm_id) SELECT 'M13A-P024', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page or PMC',
    'Tracker experiment M13A-P001-E001',
    'Module 13B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M13B-O001"], "source_experiment_tracker_id": "M13A-P001-E001", "source_paper_tracker_id": "M13A-P001", "tracker_key": "M13A-P001::M13A-P001-E001"}'
  FROM _m13_paper_map p
  JOIN _m13_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M13A-P001'
  RETURNING experiment_id
)
INSERT INTO _m13_experiment_map (tracker_id, experiment_id) SELECT 'M13A-P001::M13A-P001-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page or PMC',
    'Tracker experiment M13A-P002-E001',
    'Module 13B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M13B-O002"], "source_experiment_tracker_id": "M13A-P002-E001", "source_paper_tracker_id": "M13A-P002", "tracker_key": "M13A-P002::M13A-P002-E001"}'
  FROM _m13_paper_map p
  JOIN _m13_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M13A-P002'
  RETURNING experiment_id
)
INSERT INTO _m13_experiment_map (tracker_id, experiment_id) SELECT 'M13A-P002::M13A-P002-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page or PMC',
    'Tracker experiment M13A-P003-E001',
    'Module 13B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M13B-O003"], "source_experiment_tracker_id": "M13A-P003-E001", "source_paper_tracker_id": "M13A-P003", "tracker_key": "M13A-P003::M13A-P003-E001"}'
  FROM _m13_paper_map p
  JOIN _m13_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M13A-P003'
  RETURNING experiment_id
)
INSERT INTO _m13_experiment_map (tracker_id, experiment_id) SELECT 'M13A-P003::M13A-P003-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page or PMC',
    'Tracker experiment M13A-P004-E001',
    'Module 13B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M13B-O004"], "source_experiment_tracker_id": "M13A-P004-E001", "source_paper_tracker_id": "M13A-P004", "tracker_key": "M13A-P004::M13A-P004-E001"}'
  FROM _m13_paper_map p
  JOIN _m13_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M13A-P004'
  RETURNING experiment_id
)
INSERT INTO _m13_experiment_map (tracker_id, experiment_id) SELECT 'M13A-P004::M13A-P004-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page or PMC',
    'Tracker experiment M13A-P005-E001',
    'Module 13B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M13B-O005"], "source_experiment_tracker_id": "M13A-P005-E001", "source_paper_tracker_id": "M13A-P005", "tracker_key": "M13A-P005::M13A-P005-E001"}'
  FROM _m13_paper_map p
  JOIN _m13_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M13A-P005'
  RETURNING experiment_id
)
INSERT INTO _m13_experiment_map (tracker_id, experiment_id) SELECT 'M13A-P005::M13A-P005-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page or PMC',
    'Tracker experiment M13A-P006-E001',
    'Module 13B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M13B-O006"], "source_experiment_tracker_id": "M13A-P006-E001", "source_paper_tracker_id": "M13A-P006", "tracker_key": "M13A-P006::M13A-P006-E001"}'
  FROM _m13_paper_map p
  JOIN _m13_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M13A-P006'
  RETURNING experiment_id
)
INSERT INTO _m13_experiment_map (tracker_id, experiment_id) SELECT 'M13A-P006::M13A-P006-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page or PMC',
    'Tracker experiment M13A-P007-E001',
    'Module 13B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M13B-O007"], "source_experiment_tracker_id": "M13A-P007-E001", "source_paper_tracker_id": "M13A-P007", "tracker_key": "M13A-P007::M13A-P007-E001"}'
  FROM _m13_paper_map p
  JOIN _m13_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M13A-P007'
  RETURNING experiment_id
)
INSERT INTO _m13_experiment_map (tracker_id, experiment_id) SELECT 'M13A-P007::M13A-P007-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page or PMC',
    'Tracker experiment M13A-P008-E001',
    'Module 13B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M13B-O008"], "source_experiment_tracker_id": "M13A-P008-E001", "source_paper_tracker_id": "M13A-P008", "tracker_key": "M13A-P008::M13A-P008-E001"}'
  FROM _m13_paper_map p
  JOIN _m13_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M13A-P008'
  RETURNING experiment_id
)
INSERT INTO _m13_experiment_map (tracker_id, experiment_id) SELECT 'M13A-P008::M13A-P008-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page or PMC',
    'Tracker experiment M13A-P009-E001',
    'Module 13B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M13B-O009"], "source_experiment_tracker_id": "M13A-P009-E001", "source_paper_tracker_id": "M13A-P009", "tracker_key": "M13A-P009::M13A-P009-E001"}'
  FROM _m13_paper_map p
  JOIN _m13_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M13A-P009'
  RETURNING experiment_id
)
INSERT INTO _m13_experiment_map (tracker_id, experiment_id) SELECT 'M13A-P009::M13A-P009-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page or PMC',
    'Tracker experiment M13A-P010-E001',
    'Module 13B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M13B-O010"], "source_experiment_tracker_id": "M13A-P010-E001", "source_paper_tracker_id": "M13A-P010", "tracker_key": "M13A-P010::M13A-P010-E001"}'
  FROM _m13_paper_map p
  JOIN _m13_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M13A-P010'
  RETURNING experiment_id
)
INSERT INTO _m13_experiment_map (tracker_id, experiment_id) SELECT 'M13A-P010::M13A-P010-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page or PMC',
    'Tracker experiment M13A-P011-E001',
    'Module 13B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M13B-O011"], "source_experiment_tracker_id": "M13A-P011-E001", "source_paper_tracker_id": "M13A-P011", "tracker_key": "M13A-P011::M13A-P011-E001"}'
  FROM _m13_paper_map p
  JOIN _m13_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M13A-P011'
  RETURNING experiment_id
)
INSERT INTO _m13_experiment_map (tracker_id, experiment_id) SELECT 'M13A-P011::M13A-P011-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page or PMC',
    'Tracker experiment M13A-P012-E001',
    'Module 13B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M13B-O012"], "source_experiment_tracker_id": "M13A-P012-E001", "source_paper_tracker_id": "M13A-P012", "tracker_key": "M13A-P012::M13A-P012-E001"}'
  FROM _m13_paper_map p
  JOIN _m13_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M13A-P012'
  RETURNING experiment_id
)
INSERT INTO _m13_experiment_map (tracker_id, experiment_id) SELECT 'M13A-P012::M13A-P012-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page or PMC',
    'Tracker experiment M13A-P013-E001',
    'Module 13B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M13B-O013"], "source_experiment_tracker_id": "M13A-P013-E001", "source_paper_tracker_id": "M13A-P013", "tracker_key": "M13A-P013::M13A-P013-E001"}'
  FROM _m13_paper_map p
  JOIN _m13_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M13A-P013'
  RETURNING experiment_id
)
INSERT INTO _m13_experiment_map (tracker_id, experiment_id) SELECT 'M13A-P013::M13A-P013-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page or PMC',
    'Tracker experiment M13A-P014-E001',
    'Module 13B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M13B-O014"], "source_experiment_tracker_id": "M13A-P014-E001", "source_paper_tracker_id": "M13A-P014", "tracker_key": "M13A-P014::M13A-P014-E001"}'
  FROM _m13_paper_map p
  JOIN _m13_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M13A-P014'
  RETURNING experiment_id
)
INSERT INTO _m13_experiment_map (tracker_id, experiment_id) SELECT 'M13A-P014::M13A-P014-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page or PMC',
    'Tracker experiment M13A-P015-E001',
    'Module 13B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M13B-O015"], "source_experiment_tracker_id": "M13A-P015-E001", "source_paper_tracker_id": "M13A-P015", "tracker_key": "M13A-P015::M13A-P015-E001"}'
  FROM _m13_paper_map p
  JOIN _m13_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M13A-P015'
  RETURNING experiment_id
)
INSERT INTO _m13_experiment_map (tracker_id, experiment_id) SELECT 'M13A-P015::M13A-P015-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page or PMC',
    'Tracker experiment M13A-P016-E001',
    'Module 13B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M13B-O016"], "source_experiment_tracker_id": "M13A-P016-E001", "source_paper_tracker_id": "M13A-P016", "tracker_key": "M13A-P016::M13A-P016-E001"}'
  FROM _m13_paper_map p
  JOIN _m13_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M13A-P016'
  RETURNING experiment_id
)
INSERT INTO _m13_experiment_map (tracker_id, experiment_id) SELECT 'M13A-P016::M13A-P016-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page or PMC',
    'Tracker experiment M13A-P017-E001',
    'Module 13B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M13B-O017"], "source_experiment_tracker_id": "M13A-P017-E001", "source_paper_tracker_id": "M13A-P017", "tracker_key": "M13A-P017::M13A-P017-E001"}'
  FROM _m13_paper_map p
  JOIN _m13_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M13A-P017'
  RETURNING experiment_id
)
INSERT INTO _m13_experiment_map (tracker_id, experiment_id) SELECT 'M13A-P017::M13A-P017-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page or PMC',
    'Tracker experiment M13A-P018-E001',
    'Module 13B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M13B-O018"], "source_experiment_tracker_id": "M13A-P018-E001", "source_paper_tracker_id": "M13A-P018", "tracker_key": "M13A-P018::M13A-P018-E001"}'
  FROM _m13_paper_map p
  JOIN _m13_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M13A-P018'
  RETURNING experiment_id
)
INSERT INTO _m13_experiment_map (tracker_id, experiment_id) SELECT 'M13A-P018::M13A-P018-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page or PMC',
    'Tracker experiment M13A-P019-E001',
    'Module 13B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M13B-O019"], "source_experiment_tracker_id": "M13A-P019-E001", "source_paper_tracker_id": "M13A-P019", "tracker_key": "M13A-P019::M13A-P019-E001"}'
  FROM _m13_paper_map p
  JOIN _m13_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M13A-P019'
  RETURNING experiment_id
)
INSERT INTO _m13_experiment_map (tracker_id, experiment_id) SELECT 'M13A-P019::M13A-P019-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page or PMC',
    'Tracker experiment M13A-P020-E001',
    'Module 13B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M13B-O020"], "source_experiment_tracker_id": "M13A-P020-E001", "source_paper_tracker_id": "M13A-P020", "tracker_key": "M13A-P020::M13A-P020-E001"}'
  FROM _m13_paper_map p
  JOIN _m13_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M13A-P020'
  RETURNING experiment_id
)
INSERT INTO _m13_experiment_map (tracker_id, experiment_id) SELECT 'M13A-P020::M13A-P020-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page or PMC',
    'Tracker experiment M13A-P021-E001',
    'Module 13B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M13B-O021"], "source_experiment_tracker_id": "M13A-P021-E001", "source_paper_tracker_id": "M13A-P021", "tracker_key": "M13A-P021::M13A-P021-E001"}'
  FROM _m13_paper_map p
  JOIN _m13_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M13A-P021'
  RETURNING experiment_id
)
INSERT INTO _m13_experiment_map (tracker_id, experiment_id) SELECT 'M13A-P021::M13A-P021-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page or PMC',
    'Tracker experiment M13A-P022-E001',
    'Module 13B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M13B-O022"], "source_experiment_tracker_id": "M13A-P022-E001", "source_paper_tracker_id": "M13A-P022", "tracker_key": "M13A-P022::M13A-P022-E001"}'
  FROM _m13_paper_map p
  JOIN _m13_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M13A-P022'
  RETURNING experiment_id
)
INSERT INTO _m13_experiment_map (tracker_id, experiment_id) SELECT 'M13A-P022::M13A-P022-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page or PMC',
    'Tracker experiment M13A-P023-E001',
    'Module 13B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M13B-O023"], "source_experiment_tracker_id": "M13A-P023-E001", "source_paper_tracker_id": "M13A-P023", "tracker_key": "M13A-P023::M13A-P023-E001"}'
  FROM _m13_paper_map p
  JOIN _m13_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M13A-P023'
  RETURNING experiment_id
)
INSERT INTO _m13_experiment_map (tracker_id, experiment_id) SELECT 'M13A-P023::M13A-P023-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page or PMC',
    'Tracker experiment M13A-P024-E001',
    'Module 13B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M13B-O024"], "source_experiment_tracker_id": "M13A-P024-E001", "source_paper_tracker_id": "M13A-P024", "tracker_key": "M13A-P024::M13A-P024-E001"}'
  FROM _m13_paper_map p
  JOIN _m13_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M13A-P024'
  RETURNING experiment_id
)
INSERT INTO _m13_experiment_map (tracker_id, experiment_id) SELECT 'M13A-P024::M13A-P024-E001', experiment_id FROM inserted;

INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('time-course pathobiology evidence', 'Module 13B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;

INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('astrocytic border formation', 'Module 13B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('axon myelin degeneration', 'Module 13B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('cell death/tissue loss', 'Module 13B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('chronic lesion stabilization', 'Module 13B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('fibrotic scar formation', 'Module 13B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('immune wound response', 'Module 13B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('lesion geometry', 'Module 13B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('vascular/barrier injury', 'Module 13B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Graded contusion time course from 15 min to 8 weeks linking hemorrhage, lesion expansion, gray/white matter loss, residual white matter, and function.',
    'qualitative',
    NULL,
    'Graded contusion time course from 15 min to 8 weeks linking hemorrhage, lesion expansion, gray/white matter loss, residual white matter, and function.',
    'graded contusion lesion development',
    'Module 13A tracker / source-page, full-text PMC, database, or abstract metadata',
    'Abstract/source page or PMC',
    'medium',
    '{"curator_notes": "First-pass extraction preserving temporal pathobiology boundary.", "experiment_tracker_id": "M13A-P001-E001", "measurement_method_inference": null, "paper_tracker_id": "M13A-P001", "quantitative": "NO", "statistics_reported": "Source-page/full-text first pass; exact statistics retained only when directly available", "topic_id": "M13B-T001", "tracker_id": "M13B-O001"}'
  FROM _m13_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M13A-P001::M13A-P001-E001'
    AND et.evidence_type_name = 'time-course pathobiology evidence'
    AND ot.outcome_type_name = 'lesion geometry'
  RETURNING observation_id
)
INSERT INTO _m13_observation_map (tracker_id, observation_id) SELECT 'M13B-O001', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Controlled contusion time course from 15 min to 10 weeks; gray matter loss rapid by 24 h and white matter loss extends to 1 week.',
    'qualitative',
    NULL,
    'Controlled contusion time course from 15 min to 10 weeks; gray matter loss rapid by 24 h and white matter loss extends to 1 week.',
    'gray/white matter progression',
    'Module 13A tracker / source-page, full-text PMC, database, or abstract metadata',
    'Abstract/source page or PMC',
    'high',
    '{"curator_notes": "First-pass extraction preserving temporal pathobiology boundary.", "experiment_tracker_id": "M13A-P002-E001", "measurement_method_inference": null, "paper_tracker_id": "M13A-P002", "quantitative": "NO", "statistics_reported": "Source-page/full-text first pass; exact statistics retained only when directly available", "topic_id": "M13B-T001", "tracker_id": "M13B-O002"}'
  FROM _m13_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M13A-P002::M13A-P002-E001'
    AND et.evidence_type_name = 'time-course pathobiology evidence'
    AND ot.outcome_type_name = 'lesion geometry'
  RETURNING observation_id
)
INSERT INTO _m13_observation_map (tracker_id, observation_id) SELECT 'M13B-O002', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Human postmortem MRI-pathology series from 8 days to 23 years after SCI defining ascending/descending Wallerian degeneration.',
    'qualitative',
    'immunostaining / histology / pathology; MRI / imaging assay',
    'Human postmortem MRI-pathology series from 8 days to 23 years after SCI defining ascending/descending Wallerian degeneration.',
    'human Wallerian degeneration',
    'Module 13A tracker / source-page, full-text PMC, database, or abstract metadata',
    'Abstract/source page or PMC',
    'high',
    '{"curator_notes": "First-pass extraction preserving temporal pathobiology boundary.", "experiment_tracker_id": "M13A-P003-E001", "measurement_method_inference": "immunostaining / histology / pathology; MRI / imaging assay", "paper_tracker_id": "M13A-P003", "quantitative": "NO", "statistics_reported": "Source-page/full-text first pass; exact statistics retained only when directly available", "topic_id": "M13B-T007", "tracker_id": "M13B-O003"}'
  FROM _m13_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M13A-P003::M13A-P003-E001'
    AND et.evidence_type_name = 'time-course pathobiology evidence'
    AND ot.outcome_type_name = 'axon myelin degeneration'
  RETURNING observation_id
)
INSERT INTO _m13_observation_map (tracker_id, observation_id) SELECT 'M13B-O003', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Systematic review/meta-analysis of animal axonal degeneration and demyelination across SCI phase, model, severity, and level.',
    'qualitative',
    NULL,
    'Systematic review/meta-analysis of animal axonal degeneration and demyelination across SCI phase, model, severity, and level.',
    'axon/myelin degeneration meta-analysis',
    'Module 13A tracker / source-page, full-text PMC, database, or abstract metadata',
    'Abstract/source page or PMC',
    'medium',
    '{"curator_notes": "First-pass extraction preserving temporal pathobiology boundary.", "experiment_tracker_id": "M13A-P004-E001", "measurement_method_inference": null, "paper_tracker_id": "M13A-P004", "quantitative": "NO", "statistics_reported": "Source-page/full-text first pass; exact statistics retained only when directly available", "topic_id": "M13B-T007", "tracker_id": "M13B-O004"}'
  FROM _m13_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M13A-P004::M13A-P004-E001'
    AND et.evidence_type_name = 'time-course pathobiology evidence'
    AND ot.outcome_type_name = 'axon myelin degeneration'
  RETURNING observation_id
)
INSERT INTO _m13_observation_map (tracker_id, observation_id) SELECT 'M13B-O004', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Barrier disruption and vascular remodeling time-course anchor.',
    'qualitative',
    'barrier / permeability / endothelial assay',
    'Barrier disruption and vascular remodeling time-course anchor.',
    'barrier and vascular remodeling',
    'Module 13A tracker / source-page, full-text PMC, database, or abstract metadata',
    'Abstract/source page or PMC',
    'medium',
    '{"curator_notes": "First-pass extraction preserving temporal pathobiology boundary.", "experiment_tracker_id": "M13A-P005-E001", "measurement_method_inference": "barrier / permeability / endothelial assay", "paper_tracker_id": "M13A-P005", "quantitative": "NO", "statistics_reported": "Source-page/full-text first pass; exact statistics retained only when directly available", "topic_id": "M13B-T002", "tracker_id": "M13B-O005"}'
  FROM _m13_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M13A-P005::M13A-P005-E001'
    AND et.evidence_type_name = 'time-course pathobiology evidence'
    AND ot.outcome_type_name = 'vascular/barrier injury'
  RETURNING observation_id
)
INSERT INTO _m13_observation_map (tracker_id, observation_id) SELECT 'M13B-O005', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'MRI/histology evidence that hemorrhagic lesion expansion occurs over first 24 h and is modifiable by Sur1-Trpm4 blockade.',
    'qualitative',
    'immunostaining / histology / pathology; barrier / permeability / endothelial assay; MRI / imaging assay',
    'MRI/histology evidence that hemorrhagic lesion expansion occurs over first 24 h and is modifiable by Sur1-Trpm4 blockade.',
    'progressive hemorrhagic necrosis',
    'Module 13A tracker / source-page, full-text PMC, database, or abstract metadata',
    'Abstract/source page or PMC',
    'high',
    '{"curator_notes": "First-pass extraction preserving temporal pathobiology boundary.", "experiment_tracker_id": "M13A-P006-E001", "measurement_method_inference": "immunostaining / histology / pathology; barrier / permeability / endothelial assay; MRI / imaging assay", "paper_tracker_id": "M13A-P006", "quantitative": "NO", "statistics_reported": "Source-page/full-text first pass; exact statistics retained only when directly available", "topic_id": "M13B-T002", "tracker_id": "M13B-O006"}'
  FROM _m13_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M13A-P006::M13A-P006-E001'
    AND et.evidence_type_name = 'time-course pathobiology evidence'
    AND ot.outcome_type_name = 'vascular/barrier injury'
  RETURNING observation_id
)
INSERT INTO _m13_observation_map (tracker_id, observation_id) SELECT 'M13B-O006', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Astrocytic scar-border formation from 5-14 days corrals inflammatory and fibrotic cells through STAT3-dependent mechanisms.',
    'qualitative',
    NULL,
    'Astrocytic scar-border formation from 5-14 days corrals inflammatory and fibrotic cells through STAT3-dependent mechanisms.',
    'STAT3 astrocytic border formation',
    'Module 13A tracker / source-page, full-text PMC, database, or abstract metadata',
    'Abstract/source page or PMC',
    'medium',
    '{"curator_notes": "First-pass extraction preserving temporal pathobiology boundary.", "experiment_tracker_id": "M13A-P007-E001", "measurement_method_inference": null, "paper_tracker_id": "M13A-P007", "quantitative": "NO", "statistics_reported": "Source-page/full-text first pass; exact statistics retained only when directly available", "topic_id": "M13B-T005", "tracker_id": "M13B-O007"}'
  FROM _m13_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M13A-P007::M13A-P007-E001'
    AND et.evidence_type_name = 'time-course pathobiology evidence'
    AND ot.outcome_type_name = 'astrocytic border formation'
  RETURNING observation_id
)
INSERT INTO _m13_observation_map (tracker_id, observation_id) SELECT 'M13B-O007', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Spatial transcriptomic scar atlas with phases from macrophage infiltration to scar stationary state.',
    'qualitative',
    'spatial transcriptomics / spatial atlas; bulk transcriptomics / GEO dataset',
    'Spatial transcriptomic scar atlas with phases from macrophage infiltration to scar stationary state.',
    'spatial scar phase progression',
    'Module 13A tracker / source-page, full-text PMC, database, or abstract metadata',
    'Abstract/source page or PMC',
    'medium',
    '{"curator_notes": "First-pass extraction preserving temporal pathobiology boundary.", "experiment_tracker_id": "M13A-P008-E001", "measurement_method_inference": "spatial transcriptomics / spatial atlas; bulk transcriptomics / GEO dataset", "paper_tracker_id": "M13A-P008", "quantitative": "NO", "statistics_reported": "Source-page/full-text first pass; exact statistics retained only when directly available", "topic_id": "M13B-T005", "tracker_id": "M13B-O008"}'
  FROM _m13_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M13A-P008::M13A-P008-E001'
    AND et.evidence_type_name = 'time-course pathobiology evidence'
    AND ot.outcome_type_name = 'astrocytic border formation'
  RETURNING observation_id
)
INSERT INTO _m13_observation_map (tracker_id, observation_id) SELECT 'M13B-O008', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Astrocyte Ryk signaling regulates astrocyte morphology, border formation, scar size, and multicellular injury responses.',
    'qualitative',
    NULL,
    'Astrocyte Ryk signaling regulates astrocyte morphology, border formation, scar size, and multicellular injury responses.',
    'astrocytic Ryk wound signaling',
    'Module 13A tracker / source-page, full-text PMC, database, or abstract metadata',
    'Abstract/source page or PMC',
    'medium',
    '{"curator_notes": "First-pass extraction preserving temporal pathobiology boundary.", "experiment_tracker_id": "M13A-P009-E001", "measurement_method_inference": null, "paper_tracker_id": "M13A-P009", "quantitative": "NO", "statistics_reported": "Source-page/full-text first pass; exact statistics retained only when directly available", "topic_id": "M13B-T005", "tracker_id": "M13B-O009"}'
  FROM _m13_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M13A-P009::M13A-P009-E001'
    AND et.evidence_type_name = 'time-course pathobiology evidence'
    AND ot.outcome_type_name = 'astrocytic border formation'
  RETURNING observation_id
)
INSERT INTO _m13_observation_map (tracker_id, observation_id) SELECT 'M13B-O009', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Border-forming wound repair astrocytes derive mainly from local mature astrocytes and acquire persistent wound-healing states.',
    'qualitative',
    NULL,
    'Border-forming wound repair astrocytes derive mainly from local mature astrocytes and acquire persistent wound-healing states.',
    'wound repair astrocyte derivation',
    'Module 13A tracker / source-page, full-text PMC, database, or abstract metadata',
    'Abstract/source page or PMC',
    'medium',
    '{"curator_notes": "First-pass extraction preserving temporal pathobiology boundary.", "experiment_tracker_id": "M13A-P010-E001", "measurement_method_inference": null, "paper_tracker_id": "M13A-P010", "quantitative": "NO", "statistics_reported": "Source-page/full-text first pass; exact statistics retained only when directly available", "topic_id": "M13B-T005", "tracker_id": "M13B-O010"}'
  FROM _m13_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M13A-P010::M13A-P010-E001'
    AND et.evidence_type_name = 'time-course pathobiology evidence'
    AND ot.outcome_type_name = 'astrocytic border formation'
  RETURNING observation_id
)
INSERT INTO _m13_observation_map (tracker_id, observation_id) SELECT 'M13B-O010', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Mouse/monkey fibroblast heterogeneity; perivascular and meningeal fibroblast compartments contribute spatially distinct scar domains.',
    'qualitative',
    NULL,
    'Mouse/monkey fibroblast heterogeneity; perivascular and meningeal fibroblast compartments contribute spatially distinct scar domains.',
    'fibroblast scar heterogeneity',
    'Module 13A tracker / source-page, full-text PMC, database, or abstract metadata',
    'Abstract/source page or PMC',
    'medium',
    '{"curator_notes": "First-pass extraction preserving temporal pathobiology boundary.", "experiment_tracker_id": "M13A-P011-E001", "measurement_method_inference": null, "paper_tracker_id": "M13A-P011", "quantitative": "NO", "statistics_reported": "Source-page/full-text first pass; exact statistics retained only when directly available", "topic_id": "M13B-T006", "tracker_id": "M13B-O011"}'
  FROM _m13_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M13A-P011::M13A-P011-E001'
    AND et.evidence_type_name = 'time-course pathobiology evidence'
    AND ot.outcome_type_name = 'fibrotic scar formation'
  RETURNING observation_id
)
INSERT INTO _m13_observation_map (tracker_id, observation_id) SELECT 'M13B-O011', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Innate signaling boundary: post-SCI inflammation can support debris clearance, oligodendrocyte replacement, remyelination, and recovery.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Innate signaling boundary: post-SCI inflammation can support debris clearance, oligodendrocyte replacement, remyelination, and recovery.',
    'TLR4-linked oligodendrocyte replacement',
    'Module 13A tracker / source-page, full-text PMC, database, or abstract metadata',
    'Abstract/source page or PMC',
    'medium',
    '{"curator_notes": "First-pass extraction preserving temporal pathobiology boundary.", "experiment_tracker_id": "M13A-P012-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M13A-P012", "quantitative": "NO", "statistics_reported": "Source-page/full-text first pass; exact statistics retained only when directly available", "topic_id": "M13B-T003", "tracker_id": "M13B-O012"}'
  FROM _m13_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M13A-P012::M13A-P012-E001'
    AND et.evidence_type_name = 'time-course pathobiology evidence'
    AND ot.outcome_type_name = 'cell death/tissue loss'
  RETURNING observation_id
)
INSERT INTO _m13_observation_map (tracker_id, observation_id) SELECT 'M13B-O012', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Microglia/macrophage modulation changes chronic inflammatory and neurodegenerative outcomes.',
    'qualitative',
    NULL,
    'Microglia/macrophage modulation changes chronic inflammatory and neurodegenerative outcomes.',
    'microglial depletion and chronic inflammation',
    'Module 13A tracker / source-page, full-text PMC, database, or abstract metadata',
    'Abstract/source page or PMC',
    'high',
    '{"curator_notes": "First-pass extraction preserving temporal pathobiology boundary.", "experiment_tracker_id": "M13A-P013-E001", "measurement_method_inference": null, "paper_tracker_id": "M13A-P013", "quantitative": "NO", "statistics_reported": "Source-page/full-text first pass; exact statistics retained only when directly available", "topic_id": "M13B-T004", "tracker_id": "M13B-O013"}'
  FROM _m13_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M13A-P013::M13A-P013-E001'
    AND et.evidence_type_name = 'time-course pathobiology evidence'
    AND ot.outcome_type_name = 'immune wound response'
  RETURNING observation_id
)
INSERT INTO _m13_observation_map (tracker_id, observation_id) SELECT 'M13B-O013', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Duplicate full-text anchor retained for chronic remote degeneration and behavior boundary.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Duplicate full-text anchor retained for chronic remote degeneration and behavior boundary.',
    'remote neurodegeneration after SCI',
    'Module 13A tracker / source-page, full-text PMC, database, or abstract metadata',
    'Abstract/source page or PMC',
    'high',
    '{"curator_notes": "First-pass extraction preserving temporal pathobiology boundary.", "experiment_tracker_id": "M13A-P014-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M13A-P014", "quantitative": "NO", "statistics_reported": "Source-page/full-text first pass; exact statistics retained only when directly available", "topic_id": "M13B-T004", "tracker_id": "M13B-O014"}'
  FROM _m13_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M13A-P014::M13A-P014-E001'
    AND et.evidence_type_name = 'time-course pathobiology evidence'
    AND ot.outcome_type_name = 'immune wound response'
  RETURNING observation_id
)
INSERT INTO _m13_observation_map (tracker_id, observation_id) SELECT 'M13B-O014', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Microglia/macrophages promote wound corralling and compaction, supporting protective organization rather than simple suppression.',
    'qualitative',
    NULL,
    'Microglia/macrophages promote wound corralling and compaction, supporting protective organization rather than simple suppression.',
    'microglia/macrophage wound corralling',
    'Module 13A tracker / source-page, full-text PMC, database, or abstract metadata',
    'Abstract/source page or PMC',
    'medium',
    '{"curator_notes": "First-pass extraction preserving temporal pathobiology boundary.", "experiment_tracker_id": "M13A-P015-E001", "measurement_method_inference": null, "paper_tracker_id": "M13A-P015", "quantitative": "NO", "statistics_reported": "Source-page/full-text first pass; exact statistics retained only when directly available", "topic_id": "M13B-T004", "tracker_id": "M13B-O015"}'
  FROM _m13_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M13A-P015::M13A-P015-E001'
    AND et.evidence_type_name = 'time-course pathobiology evidence'
    AND ot.outcome_type_name = 'immune wound response'
  RETURNING observation_id
)
INSERT INTO _m13_observation_map (tracker_id, observation_id) SELECT 'M13B-O015', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'MRI tracks white matter tract pathology after severe thoracic contusion and relates spared white matter to locomotor recovery.',
    'qualitative',
    'immunostaining / histology / pathology; MRI / imaging assay; behavioral / functional recovery assay',
    'MRI tracks white matter tract pathology after severe thoracic contusion and relates spared white matter to locomotor recovery.',
    'white matter tract MRI pathology',
    'Module 13A tracker / source-page, full-text PMC, database, or abstract metadata',
    'Abstract/source page or PMC',
    'high',
    '{"curator_notes": "First-pass extraction preserving temporal pathobiology boundary.", "experiment_tracker_id": "M13A-P016-E001", "measurement_method_inference": "immunostaining / histology / pathology; MRI / imaging assay; behavioral / functional recovery assay", "paper_tracker_id": "M13A-P016", "quantitative": "NO", "statistics_reported": "Source-page/full-text first pass; exact statistics retained only when directly available", "topic_id": "M13B-T007", "tracker_id": "M13B-O016"}'
  FROM _m13_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M13A-P016::M13A-P016-E001'
    AND et.evidence_type_name = 'time-course pathobiology evidence'
    AND ot.outcome_type_name = 'axon myelin degeneration'
  RETURNING observation_id
)
INSERT INTO _m13_observation_map (tracker_id, observation_id) SELECT 'M13B-O016', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Chronic contusion lesion histology describing fibrotic, cellular, Schwann-cell, axonal, and cavity zones.',
    'qualitative',
    'immunostaining / histology / pathology',
    'Chronic contusion lesion histology describing fibrotic, cellular, Schwann-cell, axonal, and cavity zones.',
    'chronic cavity-zone histology',
    'Module 13A tracker / source-page, full-text PMC, database, or abstract metadata',
    'Abstract/source page or PMC',
    'low',
    '{"curator_notes": "First-pass extraction preserving temporal pathobiology boundary.", "experiment_tracker_id": "M13A-P017-E001", "measurement_method_inference": "immunostaining / histology / pathology", "paper_tracker_id": "M13A-P017", "quantitative": "NO", "statistics_reported": "Source-page/full-text first pass; exact statistics retained only when directly available", "topic_id": "M13B-T008", "tracker_id": "M13B-O017"}'
  FROM _m13_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M13A-P017::M13A-P017-E001'
    AND et.evidence_type_name = 'time-course pathobiology evidence'
    AND ot.outcome_type_name = 'chronic lesion stabilization'
  RETURNING observation_id
)
INSERT INTO _m13_observation_map (tracker_id, observation_id) SELECT 'M13B-O017', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Chronic SCI microglial plasticity boundary; chronic lesion remains inducible rather than inert.',
    'qualitative',
    NULL,
    'Chronic SCI microglial plasticity boundary; chronic lesion remains inducible rather than inert.',
    'chronic microglial plasticity',
    'Module 13A tracker / source-page, full-text PMC, database, or abstract metadata',
    'Abstract/source page or PMC',
    'medium',
    '{"curator_notes": "First-pass extraction preserving temporal pathobiology boundary.", "experiment_tracker_id": "M13A-P018-E001", "measurement_method_inference": null, "paper_tracker_id": "M13A-P018", "quantitative": "NO", "statistics_reported": "Source-page/full-text first pass; exact statistics retained only when directly available", "topic_id": "M13B-T008", "tracker_id": "M13B-O018"}'
  FROM _m13_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M13A-P018::M13A-P018-E001'
    AND et.evidence_type_name = 'time-course pathobiology evidence'
    AND ot.outcome_type_name = 'chronic lesion stabilization'
  RETURNING observation_id
)
INSERT INTO _m13_observation_map (tracker_id, observation_id) SELECT 'M13B-O018', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Human/rodent astrocytic wound-healing signal bridge.',
    'qualitative',
    NULL,
    'Human/rodent astrocytic wound-healing signal bridge.',
    'human/rodent astrocyte scar signaling',
    'Module 13A tracker / source-page, full-text PMC, database, or abstract metadata',
    'Abstract/source page or PMC',
    'medium',
    '{"curator_notes": "First-pass extraction preserving temporal pathobiology boundary.", "experiment_tracker_id": "M13A-P019-E001", "measurement_method_inference": null, "paper_tracker_id": "M13A-P019", "quantitative": "NO", "statistics_reported": "Source-page/full-text first pass; exact statistics retained only when directly available", "topic_id": "M13B-T005", "tracker_id": "M13B-O019"}'
  FROM _m13_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M13A-P019::M13A-P019-E001'
    AND et.evidence_type_name = 'time-course pathobiology evidence'
    AND ot.outcome_type_name = 'astrocytic border formation'
  RETURNING observation_id
)
INSERT INTO _m13_observation_map (tracker_id, observation_id) SELECT 'M13B-O019', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Cross-species fibrotic scar conservation boundary.',
    'qualitative',
    NULL,
    'Cross-species fibrotic scar conservation boundary.',
    'cross-species fibrotic scar conservation',
    'Module 13A tracker / source-page, full-text PMC, database, or abstract metadata',
    'Abstract/source page or PMC',
    'medium',
    '{"curator_notes": "First-pass extraction preserving temporal pathobiology boundary.", "experiment_tracker_id": "M13A-P020-E001", "measurement_method_inference": null, "paper_tracker_id": "M13A-P020", "quantitative": "NO", "statistics_reported": "Source-page/full-text first pass; exact statistics retained only when directly available", "topic_id": "M13B-T006", "tracker_id": "M13B-O020"}'
  FROM _m13_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M13A-P020::M13A-P020-E001'
    AND et.evidence_type_name = 'time-course pathobiology evidence'
    AND ot.outcome_type_name = 'fibrotic scar formation'
  RETURNING observation_id
)
INSERT INTO _m13_observation_map (tracker_id, observation_id) SELECT 'M13B-O020', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Ligand-receptor and spatial boundary evidence for multicellular scar architecture.',
    'qualitative',
    'spatial transcriptomics / spatial atlas',
    'Ligand-receptor and spatial boundary evidence for multicellular scar architecture.',
    'ligand-receptor scar interactions',
    'Module 13A tracker / source-page, full-text PMC, database, or abstract metadata',
    'Abstract/source page or PMC',
    'medium',
    '{"curator_notes": "First-pass extraction preserving temporal pathobiology boundary.", "experiment_tracker_id": "M13A-P021-E001", "measurement_method_inference": "spatial transcriptomics / spatial atlas", "paper_tracker_id": "M13A-P021", "quantitative": "NO", "statistics_reported": "Source-page/full-text first pass; exact statistics retained only when directly available", "topic_id": "M13B-T006", "tracker_id": "M13B-O021"}'
  FROM _m13_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M13A-P021::M13A-P021-E001'
    AND et.evidence_type_name = 'time-course pathobiology evidence'
    AND ot.outcome_type_name = 'fibrotic scar formation'
  RETURNING observation_id
)
INSERT INTO _m13_observation_map (tracker_id, observation_id) SELECT 'M13B-O021', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Single-cell astrocyte time course at 0.5, 1, 3, 7, 14, 60, and 90 days after mouse hemisection SCI.',
    'qualitative',
    'single-cell RNA-seq / cell-state atlas',
    'Single-cell astrocyte time course at 0.5, 1, 3, 7, 14, 60, and 90 days after mouse hemisection SCI.',
    'single-cell astrocyte time course',
    'Module 13A tracker / source-page, full-text PMC, database, or abstract metadata',
    'Abstract/source page or PMC',
    'medium',
    '{"curator_notes": "First-pass extraction preserving temporal pathobiology boundary.", "experiment_tracker_id": "M13A-P022-E001", "measurement_method_inference": "single-cell RNA-seq / cell-state atlas", "paper_tracker_id": "M13A-P022", "quantitative": "NO", "statistics_reported": "Source-page/full-text first pass; exact statistics retained only when directly available", "topic_id": "M13B-T005", "tracker_id": "M13B-O022"}'
  FROM _m13_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M13A-P022::M13A-P022-E001'
    AND et.evidence_type_name = 'time-course pathobiology evidence'
    AND ot.outcome_type_name = 'astrocytic border formation'
  RETURNING observation_id
)
INSERT INTO _m13_observation_map (tracker_id, observation_id) SELECT 'M13B-O022', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Human cord postmortem MRI-pathology evidence of Wallerian degeneration across days to decades.',
    'qualitative',
    'immunostaining / histology / pathology; MRI / imaging assay',
    'Human cord postmortem MRI-pathology evidence of Wallerian degeneration across days to decades.',
    'MRI-pathology Wallerian course',
    'Module 13A tracker / source-page, full-text PMC, database, or abstract metadata',
    'Abstract/source page or PMC',
    'high',
    '{"curator_notes": "First-pass extraction preserving temporal pathobiology boundary.", "experiment_tracker_id": "M13A-P023-E001", "measurement_method_inference": "immunostaining / histology / pathology; MRI / imaging assay", "paper_tracker_id": "M13A-P023", "quantitative": "NO", "statistics_reported": "Source-page/full-text first pass; exact statistics retained only when directly available", "topic_id": "M13B-T007", "tracker_id": "M13B-O023"}'
  FROM _m13_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M13A-P023::M13A-P023-E001'
    AND et.evidence_type_name = 'time-course pathobiology evidence'
    AND ot.outcome_type_name = 'axon myelin degeneration'
  RETURNING observation_id
)
INSERT INTO _m13_observation_map (tracker_id, observation_id) SELECT 'M13B-O023', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Progressive hemorrhagic necrosis intervention anchor showing acute lesion expansion can be reduced.',
    'qualitative',
    'barrier / permeability / endothelial assay',
    'Progressive hemorrhagic necrosis intervention anchor showing acute lesion expansion can be reduced.',
    'modifiable acute hemorrhagic expansion',
    'Module 13A tracker / source-page, full-text PMC, database, or abstract metadata',
    'Abstract/source page or PMC',
    'high',
    '{"curator_notes": "First-pass extraction preserving temporal pathobiology boundary.", "experiment_tracker_id": "M13A-P024-E001", "measurement_method_inference": "barrier / permeability / endothelial assay", "paper_tracker_id": "M13A-P024", "quantitative": "NO", "statistics_reported": "Source-page/full-text first pass; exact statistics retained only when directly available", "topic_id": "M13B-T002", "tracker_id": "M13B-O024"}'
  FROM _m13_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M13A-P024::M13A-P024-E001'
    AND et.evidence_type_name = 'time-course pathobiology evidence'
    AND ot.outcome_type_name = 'vascular/barrier injury'
  RETURNING observation_id
)
INSERT INTO _m13_observation_map (tracker_id, observation_id) SELECT 'M13B-O024', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Mechanical severity and early lesion geometry condition later tissue loss and functional deficits.',
    'mechanistic synthesis',
    'medium',
    'Module 13A tracker / source-page, full-text PMC, database, or abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text and dataset extraction queued where needed.", "source_paper_tracker_id": "M13A-P001", "topic_id": "M13B-T001", "tracker_id": "M13B-C001"}'
  FROM _m13_paper_map p
  WHERE p.tracker_id = 'M13A-P001'
  RETURNING claim_id
)
INSERT INTO _m13_claim_map (tracker_id, claim_id) SELECT 'M13B-C001', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Mechanical severity and early lesion geometry condition later tissue loss and functional deficits.',
    'mechanistic synthesis',
    'high',
    'Module 13A tracker / source-page, full-text PMC, database, or abstract metadata',
    'high',
    '{"curator_notes": "First-pass claim abstraction; full text and dataset extraction queued where needed.", "source_paper_tracker_id": "M13A-P002", "topic_id": "M13B-T001", "tracker_id": "M13B-C002"}'
  FROM _m13_paper_map p
  WHERE p.tracker_id = 'M13A-P002'
  RETURNING claim_id
)
INSERT INTO _m13_claim_map (tracker_id, claim_id) SELECT 'M13B-C002', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Modern spatial/single-cell datasets define trajectories and cell-cell interactions during scar and lesion formation.',
    'boundary condition',
    'high',
    'Module 13A tracker / source-page, full-text PMC, database, or abstract metadata',
    'high',
    '{"curator_notes": "First-pass claim abstraction; full text and dataset extraction queued where needed.", "source_paper_tracker_id": "M13A-P003", "topic_id": "M13B-T007", "tracker_id": "M13B-C003"}'
  FROM _m13_paper_map p
  WHERE p.tracker_id = 'M13A-P003'
  RETURNING claim_id
)
INSERT INTO _m13_claim_map (tracker_id, claim_id) SELECT 'M13B-C003', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Modern spatial/single-cell datasets define trajectories and cell-cell interactions during scar and lesion formation.',
    'boundary condition',
    'medium',
    'Module 13A tracker / source-page, full-text PMC, database, or abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text and dataset extraction queued where needed.", "source_paper_tracker_id": "M13A-P004", "topic_id": "M13B-T007", "tracker_id": "M13B-C004"}'
  FROM _m13_paper_map p
  WHERE p.tracker_id = 'M13A-P004'
  RETURNING claim_id
)
INSERT INTO _m13_claim_map (tracker_id, claim_id) SELECT 'M13B-C004', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Vascular/barrier failure and hemorrhagic expansion are core secondary-injury mechanisms.',
    'mechanistic synthesis',
    'medium',
    'Module 13A tracker / source-page, full-text PMC, database, or abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text and dataset extraction queued where needed.", "source_paper_tracker_id": "M13A-P005", "topic_id": "M13B-T002", "tracker_id": "M13B-C005"}'
  FROM _m13_paper_map p
  WHERE p.tracker_id = 'M13A-P005'
  RETURNING claim_id
)
INSERT INTO _m13_claim_map (tracker_id, claim_id) SELECT 'M13B-C005', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Vascular/barrier failure and hemorrhagic expansion are core secondary-injury mechanisms.',
    'mechanistic synthesis',
    'high',
    'Module 13A tracker / source-page, full-text PMC, database, or abstract metadata',
    'high',
    '{"curator_notes": "First-pass claim abstraction; full text and dataset extraction queued where needed.", "source_paper_tracker_id": "M13A-P006", "topic_id": "M13B-T002", "tracker_id": "M13B-C006"}'
  FROM _m13_paper_map p
  WHERE p.tracker_id = 'M13A-P006'
  RETURNING claim_id
)
INSERT INTO _m13_claim_map (tracker_id, claim_id) SELECT 'M13B-C006', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Astrocytic border formation is a coordinated wound-containment process that shapes chronic lesion interfaces.',
    'mechanistic synthesis',
    'medium',
    'Module 13A tracker / source-page, full-text PMC, database, or abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text and dataset extraction queued where needed.", "source_paper_tracker_id": "M13A-P007", "topic_id": "M13B-T005", "tracker_id": "M13B-C007"}'
  FROM _m13_paper_map p
  WHERE p.tracker_id = 'M13A-P007'
  RETURNING claim_id
)
INSERT INTO _m13_claim_map (tracker_id, claim_id) SELECT 'M13B-C007', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Astrocytic border formation is a coordinated wound-containment process that shapes chronic lesion interfaces.',
    'mechanistic synthesis',
    'medium',
    'Module 13A tracker / source-page, full-text PMC, database, or abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text and dataset extraction queued where needed.", "source_paper_tracker_id": "M13A-P008", "topic_id": "M13B-T005", "tracker_id": "M13B-C008"}'
  FROM _m13_paper_map p
  WHERE p.tracker_id = 'M13A-P008'
  RETURNING claim_id
)
INSERT INTO _m13_claim_map (tracker_id, claim_id) SELECT 'M13B-C008', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Astrocytic border formation is a coordinated wound-containment process that shapes chronic lesion interfaces.',
    'mechanistic synthesis',
    'medium',
    'Module 13A tracker / source-page, full-text PMC, database, or abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text and dataset extraction queued where needed.", "source_paper_tracker_id": "M13A-P009", "topic_id": "M13B-T005", "tracker_id": "M13B-C009"}'
  FROM _m13_paper_map p
  WHERE p.tracker_id = 'M13A-P009'
  RETURNING claim_id
)
INSERT INTO _m13_claim_map (tracker_id, claim_id) SELECT 'M13B-C009', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Astrocytic border formation is a coordinated wound-containment process that shapes chronic lesion interfaces.',
    'mechanistic synthesis',
    'medium',
    'Module 13A tracker / source-page, full-text PMC, database, or abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text and dataset extraction queued where needed.", "source_paper_tracker_id": "M13A-P010", "topic_id": "M13B-T005", "tracker_id": "M13B-C010"}'
  FROM _m13_paper_map p
  WHERE p.tracker_id = 'M13A-P010'
  RETURNING claim_id
)
INSERT INTO _m13_claim_map (tracker_id, claim_id) SELECT 'M13B-C010', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Fibrotic/stromal scarring is heterogeneous, spatially organized, and cross-species relevant.',
    'mechanistic synthesis',
    'medium',
    'Module 13A tracker / source-page, full-text PMC, database, or abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text and dataset extraction queued where needed.", "source_paper_tracker_id": "M13A-P011", "topic_id": "M13B-T006", "tracker_id": "M13B-C011"}'
  FROM _m13_paper_map p
  WHERE p.tracker_id = 'M13A-P011'
  RETURNING claim_id
)
INSERT INTO _m13_claim_map (tracker_id, claim_id) SELECT 'M13B-C011', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Axon/myelin loss and Wallerian degeneration evolve over time and depend on model, level, severity, and distance from lesion.',
    'mechanistic synthesis',
    'medium',
    'Module 13A tracker / source-page, full-text PMC, database, or abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text and dataset extraction queued where needed.", "source_paper_tracker_id": "M13A-P012", "topic_id": "M13B-T003", "tracker_id": "M13B-C012"}'
  FROM _m13_paper_map p
  WHERE p.tracker_id = 'M13A-P012'
  RETURNING claim_id
)
INSERT INTO _m13_claim_map (tracker_id, claim_id) SELECT 'M13B-C012', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Inflammatory cells must be interpreted by timing and repair function, not only as global damage mediators.',
    'mechanistic synthesis',
    'high',
    'Module 13A tracker / source-page, full-text PMC, database, or abstract metadata',
    'high',
    '{"curator_notes": "First-pass claim abstraction; full text and dataset extraction queued where needed.", "source_paper_tracker_id": "M13A-P013", "topic_id": "M13B-T004", "tracker_id": "M13B-C013"}'
  FROM _m13_paper_map p
  WHERE p.tracker_id = 'M13A-P013'
  RETURNING claim_id
)
INSERT INTO _m13_claim_map (tracker_id, claim_id) SELECT 'M13B-C013', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Inflammatory cells must be interpreted by timing and repair function, not only as global damage mediators.',
    'mechanistic synthesis',
    'high',
    'Module 13A tracker / source-page, full-text PMC, database, or abstract metadata',
    'high',
    '{"curator_notes": "First-pass claim abstraction; full text and dataset extraction queued where needed.", "source_paper_tracker_id": "M13A-P014", "topic_id": "M13B-T004", "tracker_id": "M13B-C014"}'
  FROM _m13_paper_map p
  WHERE p.tracker_id = 'M13A-P014'
  RETURNING claim_id
)
INSERT INTO _m13_claim_map (tracker_id, claim_id) SELECT 'M13B-C014', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Inflammatory cells must be interpreted by timing and repair function, not only as global damage mediators.',
    'mechanistic synthesis',
    'medium',
    'Module 13A tracker / source-page, full-text PMC, database, or abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text and dataset extraction queued where needed.", "source_paper_tracker_id": "M13A-P015", "topic_id": "M13B-T004", "tracker_id": "M13B-C015"}'
  FROM _m13_paper_map p
  WHERE p.tracker_id = 'M13A-P015'
  RETURNING claim_id
)
INSERT INTO _m13_claim_map (tracker_id, claim_id) SELECT 'M13B-C015', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Modern spatial/single-cell datasets define trajectories and cell-cell interactions during scar and lesion formation.',
    'boundary condition',
    'high',
    'Module 13A tracker / source-page, full-text PMC, database, or abstract metadata',
    'high',
    '{"curator_notes": "First-pass claim abstraction; full text and dataset extraction queued where needed.", "source_paper_tracker_id": "M13A-P016", "topic_id": "M13B-T007", "tracker_id": "M13B-C016"}'
  FROM _m13_paper_map p
  WHERE p.tracker_id = 'M13A-P016'
  RETURNING claim_id
)
INSERT INTO _m13_claim_map (tracker_id, claim_id) SELECT 'M13B-C016', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Chronic lesion anatomy is a stabilized output of interacting traumatic, vascular, immune, glial, stromal, and degenerative processes.',
    'boundary condition',
    'low',
    'Module 13A tracker / source-page, full-text PMC, database, or abstract metadata',
    'low',
    '{"curator_notes": "First-pass claim abstraction; full text and dataset extraction queued where needed.", "source_paper_tracker_id": "M13A-P017", "topic_id": "M13B-T008", "tracker_id": "M13B-C017"}'
  FROM _m13_paper_map p
  WHERE p.tracker_id = 'M13A-P017'
  RETURNING claim_id
)
INSERT INTO _m13_claim_map (tracker_id, claim_id) SELECT 'M13B-C017', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Chronic lesion anatomy is a stabilized output of interacting traumatic, vascular, immune, glial, stromal, and degenerative processes.',
    'boundary condition',
    'medium',
    'Module 13A tracker / source-page, full-text PMC, database, or abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text and dataset extraction queued where needed.", "source_paper_tracker_id": "M13A-P018", "topic_id": "M13B-T008", "tracker_id": "M13B-C018"}'
  FROM _m13_paper_map p
  WHERE p.tracker_id = 'M13A-P018'
  RETURNING claim_id
)
INSERT INTO _m13_claim_map (tracker_id, claim_id) SELECT 'M13B-C018', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Astrocytic border formation is a coordinated wound-containment process that shapes chronic lesion interfaces.',
    'mechanistic synthesis',
    'medium',
    'Module 13A tracker / source-page, full-text PMC, database, or abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text and dataset extraction queued where needed.", "source_paper_tracker_id": "M13A-P019", "topic_id": "M13B-T005", "tracker_id": "M13B-C019"}'
  FROM _m13_paper_map p
  WHERE p.tracker_id = 'M13A-P019'
  RETURNING claim_id
)
INSERT INTO _m13_claim_map (tracker_id, claim_id) SELECT 'M13B-C019', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Fibrotic/stromal scarring is heterogeneous, spatially organized, and cross-species relevant.',
    'mechanistic synthesis',
    'medium',
    'Module 13A tracker / source-page, full-text PMC, database, or abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text and dataset extraction queued where needed.", "source_paper_tracker_id": "M13A-P020", "topic_id": "M13B-T006", "tracker_id": "M13B-C020"}'
  FROM _m13_paper_map p
  WHERE p.tracker_id = 'M13A-P020'
  RETURNING claim_id
)
INSERT INTO _m13_claim_map (tracker_id, claim_id) SELECT 'M13B-C020', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Fibrotic/stromal scarring is heterogeneous, spatially organized, and cross-species relevant.',
    'mechanistic synthesis',
    'medium',
    'Module 13A tracker / source-page, full-text PMC, database, or abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text and dataset extraction queued where needed.", "source_paper_tracker_id": "M13A-P021", "topic_id": "M13B-T006", "tracker_id": "M13B-C021"}'
  FROM _m13_paper_map p
  WHERE p.tracker_id = 'M13A-P021'
  RETURNING claim_id
)
INSERT INTO _m13_claim_map (tracker_id, claim_id) SELECT 'M13B-C021', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Astrocytic border formation is a coordinated wound-containment process that shapes chronic lesion interfaces.',
    'mechanistic synthesis',
    'medium',
    'Module 13A tracker / source-page, full-text PMC, database, or abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text and dataset extraction queued where needed.", "source_paper_tracker_id": "M13A-P022", "topic_id": "M13B-T005", "tracker_id": "M13B-C022"}'
  FROM _m13_paper_map p
  WHERE p.tracker_id = 'M13A-P022'
  RETURNING claim_id
)
INSERT INTO _m13_claim_map (tracker_id, claim_id) SELECT 'M13B-C022', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Modern spatial/single-cell datasets define trajectories and cell-cell interactions during scar and lesion formation.',
    'boundary condition',
    'high',
    'Module 13A tracker / source-page, full-text PMC, database, or abstract metadata',
    'high',
    '{"curator_notes": "First-pass claim abstraction; full text and dataset extraction queued where needed.", "source_paper_tracker_id": "M13A-P023", "topic_id": "M13B-T007", "tracker_id": "M13B-C023"}'
  FROM _m13_paper_map p
  WHERE p.tracker_id = 'M13A-P023'
  RETURNING claim_id
)
INSERT INTO _m13_claim_map (tracker_id, claim_id) SELECT 'M13B-C023', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Vascular/barrier failure and hemorrhagic expansion are core secondary-injury mechanisms.',
    'mechanistic synthesis',
    'high',
    'Module 13A tracker / source-page, full-text PMC, database, or abstract metadata',
    'high',
    '{"curator_notes": "First-pass claim abstraction; full text and dataset extraction queued where needed.", "source_paper_tracker_id": "M13A-P024", "topic_id": "M13B-T002", "tracker_id": "M13B-C024"}'
  FROM _m13_paper_map p
  WHERE p.tracker_id = 'M13A-P024'
  RETURNING claim_id
)
INSERT INTO _m13_claim_map (tracker_id, claim_id) SELECT 'M13B-C024', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct first-pass link from claim to same-source observation.", "strength": "medium", "tracker_id": "M13B-L001"}'
  FROM _m13_claim_map c
  JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O001'
  WHERE c.tracker_id = 'M13B-C001'
  RETURNING link_id
)
INSERT INTO _m13_link_map (tracker_id, link_id) SELECT 'M13B-L001', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct first-pass link from claim to same-source observation.", "strength": "high", "tracker_id": "M13B-L002"}'
  FROM _m13_claim_map c
  JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O002'
  WHERE c.tracker_id = 'M13B-C002'
  RETURNING link_id
)
INSERT INTO _m13_link_map (tracker_id, link_id) SELECT 'M13B-L002', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct first-pass link from claim to same-source observation.", "strength": "high", "tracker_id": "M13B-L003"}'
  FROM _m13_claim_map c
  JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O003'
  WHERE c.tracker_id = 'M13B-C003'
  RETURNING link_id
)
INSERT INTO _m13_link_map (tracker_id, link_id) SELECT 'M13B-L003', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct first-pass link from claim to same-source observation.", "strength": "medium", "tracker_id": "M13B-L004"}'
  FROM _m13_claim_map c
  JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O004'
  WHERE c.tracker_id = 'M13B-C004'
  RETURNING link_id
)
INSERT INTO _m13_link_map (tracker_id, link_id) SELECT 'M13B-L004', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct first-pass link from claim to same-source observation.", "strength": "medium", "tracker_id": "M13B-L005"}'
  FROM _m13_claim_map c
  JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O005'
  WHERE c.tracker_id = 'M13B-C005'
  RETURNING link_id
)
INSERT INTO _m13_link_map (tracker_id, link_id) SELECT 'M13B-L005', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct first-pass link from claim to same-source observation.", "strength": "high", "tracker_id": "M13B-L006"}'
  FROM _m13_claim_map c
  JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O006'
  WHERE c.tracker_id = 'M13B-C006'
  RETURNING link_id
)
INSERT INTO _m13_link_map (tracker_id, link_id) SELECT 'M13B-L006', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct first-pass link from claim to same-source observation.", "strength": "medium", "tracker_id": "M13B-L007"}'
  FROM _m13_claim_map c
  JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O007'
  WHERE c.tracker_id = 'M13B-C007'
  RETURNING link_id
)
INSERT INTO _m13_link_map (tracker_id, link_id) SELECT 'M13B-L007', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct first-pass link from claim to same-source observation.", "strength": "medium", "tracker_id": "M13B-L008"}'
  FROM _m13_claim_map c
  JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O008'
  WHERE c.tracker_id = 'M13B-C008'
  RETURNING link_id
)
INSERT INTO _m13_link_map (tracker_id, link_id) SELECT 'M13B-L008', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct first-pass link from claim to same-source observation.", "strength": "medium", "tracker_id": "M13B-L009"}'
  FROM _m13_claim_map c
  JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O009'
  WHERE c.tracker_id = 'M13B-C009'
  RETURNING link_id
)
INSERT INTO _m13_link_map (tracker_id, link_id) SELECT 'M13B-L009', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct first-pass link from claim to same-source observation.", "strength": "medium", "tracker_id": "M13B-L010"}'
  FROM _m13_claim_map c
  JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O010'
  WHERE c.tracker_id = 'M13B-C010'
  RETURNING link_id
)
INSERT INTO _m13_link_map (tracker_id, link_id) SELECT 'M13B-L010', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct first-pass link from claim to same-source observation.", "strength": "medium", "tracker_id": "M13B-L011"}'
  FROM _m13_claim_map c
  JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O011'
  WHERE c.tracker_id = 'M13B-C011'
  RETURNING link_id
)
INSERT INTO _m13_link_map (tracker_id, link_id) SELECT 'M13B-L011', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct first-pass link from claim to same-source observation.", "strength": "medium", "tracker_id": "M13B-L012"}'
  FROM _m13_claim_map c
  JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O012'
  WHERE c.tracker_id = 'M13B-C012'
  RETURNING link_id
)
INSERT INTO _m13_link_map (tracker_id, link_id) SELECT 'M13B-L012', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct first-pass link from claim to same-source observation.", "strength": "high", "tracker_id": "M13B-L013"}'
  FROM _m13_claim_map c
  JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O013'
  WHERE c.tracker_id = 'M13B-C013'
  RETURNING link_id
)
INSERT INTO _m13_link_map (tracker_id, link_id) SELECT 'M13B-L013', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct first-pass link from claim to same-source observation.", "strength": "high", "tracker_id": "M13B-L014"}'
  FROM _m13_claim_map c
  JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O014'
  WHERE c.tracker_id = 'M13B-C014'
  RETURNING link_id
)
INSERT INTO _m13_link_map (tracker_id, link_id) SELECT 'M13B-L014', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct first-pass link from claim to same-source observation.", "strength": "medium", "tracker_id": "M13B-L015"}'
  FROM _m13_claim_map c
  JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O015'
  WHERE c.tracker_id = 'M13B-C015'
  RETURNING link_id
)
INSERT INTO _m13_link_map (tracker_id, link_id) SELECT 'M13B-L015', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct first-pass link from claim to same-source observation.", "strength": "high", "tracker_id": "M13B-L016"}'
  FROM _m13_claim_map c
  JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O016'
  WHERE c.tracker_id = 'M13B-C016'
  RETURNING link_id
)
INSERT INTO _m13_link_map (tracker_id, link_id) SELECT 'M13B-L016', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct first-pass link from claim to same-source observation.", "strength": "medium", "tracker_id": "M13B-L017"}'
  FROM _m13_claim_map c
  JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O017'
  WHERE c.tracker_id = 'M13B-C017'
  RETURNING link_id
)
INSERT INTO _m13_link_map (tracker_id, link_id) SELECT 'M13B-L017', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct first-pass link from claim to same-source observation.", "strength": "medium", "tracker_id": "M13B-L018"}'
  FROM _m13_claim_map c
  JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O018'
  WHERE c.tracker_id = 'M13B-C018'
  RETURNING link_id
)
INSERT INTO _m13_link_map (tracker_id, link_id) SELECT 'M13B-L018', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct first-pass link from claim to same-source observation.", "strength": "medium", "tracker_id": "M13B-L019"}'
  FROM _m13_claim_map c
  JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O019'
  WHERE c.tracker_id = 'M13B-C019'
  RETURNING link_id
)
INSERT INTO _m13_link_map (tracker_id, link_id) SELECT 'M13B-L019', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct first-pass link from claim to same-source observation.", "strength": "medium", "tracker_id": "M13B-L020"}'
  FROM _m13_claim_map c
  JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O020'
  WHERE c.tracker_id = 'M13B-C020'
  RETURNING link_id
)
INSERT INTO _m13_link_map (tracker_id, link_id) SELECT 'M13B-L020', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct first-pass link from claim to same-source observation.", "strength": "medium", "tracker_id": "M13B-L021"}'
  FROM _m13_claim_map c
  JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O021'
  WHERE c.tracker_id = 'M13B-C021'
  RETURNING link_id
)
INSERT INTO _m13_link_map (tracker_id, link_id) SELECT 'M13B-L021', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct first-pass link from claim to same-source observation.", "strength": "medium", "tracker_id": "M13B-L022"}'
  FROM _m13_claim_map c
  JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O022'
  WHERE c.tracker_id = 'M13B-C022'
  RETURNING link_id
)
INSERT INTO _m13_link_map (tracker_id, link_id) SELECT 'M13B-L022', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct first-pass link from claim to same-source observation.", "strength": "high", "tracker_id": "M13B-L023"}'
  FROM _m13_claim_map c
  JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O023'
  WHERE c.tracker_id = 'M13B-C023'
  RETURNING link_id
)
INSERT INTO _m13_link_map (tracker_id, link_id) SELECT 'M13B-L023', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct first-pass link from claim to same-source observation.", "strength": "high", "tracker_id": "M13B-L024"}'
  FROM _m13_claim_map c
  JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O024'
  WHERE c.tracker_id = 'M13B-C024'
  RETURNING link_id
)
INSERT INTO _m13_link_map (tracker_id, link_id) SELECT 'M13B-L024', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cross-source contextual link preserving model/timing boundaries.", "strength": "low", "tracker_id": "M13B-L025"}'
  FROM _m13_claim_map c
  JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O008'
  WHERE c.tracker_id = 'M13B-C001'
  RETURNING link_id
)
INSERT INTO _m13_link_map (tracker_id, link_id) SELECT 'M13B-L025', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cross-source contextual link preserving model/timing boundaries.", "strength": "low", "tracker_id": "M13B-L026"}'
  FROM _m13_claim_map c
  JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O009'
  WHERE c.tracker_id = 'M13B-C002'
  RETURNING link_id
)
INSERT INTO _m13_link_map (tracker_id, link_id) SELECT 'M13B-L026', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cross-source contextual link preserving model/timing boundaries.", "strength": "low", "tracker_id": "M13B-L027"}'
  FROM _m13_claim_map c
  JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O010'
  WHERE c.tracker_id = 'M13B-C003'
  RETURNING link_id
)
INSERT INTO _m13_link_map (tracker_id, link_id) SELECT 'M13B-L027', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cross-source contextual link preserving model/timing boundaries.", "strength": "low", "tracker_id": "M13B-L028"}'
  FROM _m13_claim_map c
  JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O011'
  WHERE c.tracker_id = 'M13B-C004'
  RETURNING link_id
)
INSERT INTO _m13_link_map (tracker_id, link_id) SELECT 'M13B-L028', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cross-source contextual link preserving model/timing boundaries.", "strength": "low", "tracker_id": "M13B-L029"}'
  FROM _m13_claim_map c
  JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O012'
  WHERE c.tracker_id = 'M13B-C005'
  RETURNING link_id
)
INSERT INTO _m13_link_map (tracker_id, link_id) SELECT 'M13B-L029', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cross-source contextual link preserving model/timing boundaries.", "strength": "low", "tracker_id": "M13B-L030"}'
  FROM _m13_claim_map c
  JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O013'
  WHERE c.tracker_id = 'M13B-C006'
  RETURNING link_id
)
INSERT INTO _m13_link_map (tracker_id, link_id) SELECT 'M13B-L030', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cross-source contextual link preserving model/timing boundaries.", "strength": "low", "tracker_id": "M13B-L031"}'
  FROM _m13_claim_map c
  JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O014'
  WHERE c.tracker_id = 'M13B-C007'
  RETURNING link_id
)
INSERT INTO _m13_link_map (tracker_id, link_id) SELECT 'M13B-L031', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cross-source contextual link preserving model/timing boundaries.", "strength": "low", "tracker_id": "M13B-L032"}'
  FROM _m13_claim_map c
  JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O015'
  WHERE c.tracker_id = 'M13B-C008'
  RETURNING link_id
)
INSERT INTO _m13_link_map (tracker_id, link_id) SELECT 'M13B-L032', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cross-source contextual link preserving model/timing boundaries.", "strength": "low", "tracker_id": "M13B-L033"}'
  FROM _m13_claim_map c
  JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O016'
  WHERE c.tracker_id = 'M13B-C009'
  RETURNING link_id
)
INSERT INTO _m13_link_map (tracker_id, link_id) SELECT 'M13B-L033', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cross-source contextual link preserving model/timing boundaries.", "strength": "low", "tracker_id": "M13B-L034"}'
  FROM _m13_claim_map c
  JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O017'
  WHERE c.tracker_id = 'M13B-C010'
  RETURNING link_id
)
INSERT INTO _m13_link_map (tracker_id, link_id) SELECT 'M13B-L034', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cross-source contextual link preserving model/timing boundaries.", "strength": "low", "tracker_id": "M13B-L035"}'
  FROM _m13_claim_map c
  JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O018'
  WHERE c.tracker_id = 'M13B-C011'
  RETURNING link_id
)
INSERT INTO _m13_link_map (tracker_id, link_id) SELECT 'M13B-L035', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cross-source contextual link preserving model/timing boundaries.", "strength": "low", "tracker_id": "M13B-L036"}'
  FROM _m13_claim_map c
  JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O019'
  WHERE c.tracker_id = 'M13B-C012'
  RETURNING link_id
)
INSERT INTO _m13_link_map (tracker_id, link_id) SELECT 'M13B-L036', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cross-source contextual link preserving model/timing boundaries.", "strength": "low", "tracker_id": "M13B-L037"}'
  FROM _m13_claim_map c
  JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O020'
  WHERE c.tracker_id = 'M13B-C013'
  RETURNING link_id
)
INSERT INTO _m13_link_map (tracker_id, link_id) SELECT 'M13B-L037', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cross-source contextual link preserving model/timing boundaries.", "strength": "low", "tracker_id": "M13B-L038"}'
  FROM _m13_claim_map c
  JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O021'
  WHERE c.tracker_id = 'M13B-C014'
  RETURNING link_id
)
INSERT INTO _m13_link_map (tracker_id, link_id) SELECT 'M13B-L038', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cross-source contextual link preserving model/timing boundaries.", "strength": "low", "tracker_id": "M13B-L039"}'
  FROM _m13_claim_map c
  JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O022'
  WHERE c.tracker_id = 'M13B-C015'
  RETURNING link_id
)
INSERT INTO _m13_link_map (tracker_id, link_id) SELECT 'M13B-L039', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cross-source contextual link preserving model/timing boundaries.", "strength": "low", "tracker_id": "M13B-L040"}'
  FROM _m13_claim_map c
  JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O023'
  WHERE c.tracker_id = 'M13B-C016'
  RETURNING link_id
)
INSERT INTO _m13_link_map (tracker_id, link_id) SELECT 'M13B-L040', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cross-source contextual link preserving model/timing boundaries.", "strength": "low", "tracker_id": "M13B-L041"}'
  FROM _m13_claim_map c
  JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O024'
  WHERE c.tracker_id = 'M13B-C017'
  RETURNING link_id
)
INSERT INTO _m13_link_map (tracker_id, link_id) SELECT 'M13B-L041', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cross-source contextual link preserving model/timing boundaries.", "strength": "low", "tracker_id": "M13B-L042"}'
  FROM _m13_claim_map c
  JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O001'
  WHERE c.tracker_id = 'M13B-C018'
  RETURNING link_id
)
INSERT INTO _m13_link_map (tracker_id, link_id) SELECT 'M13B-L042', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cross-source contextual link preserving model/timing boundaries.", "strength": "low", "tracker_id": "M13B-L043"}'
  FROM _m13_claim_map c
  JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O002'
  WHERE c.tracker_id = 'M13B-C019'
  RETURNING link_id
)
INSERT INTO _m13_link_map (tracker_id, link_id) SELECT 'M13B-L043', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cross-source contextual link preserving model/timing boundaries.", "strength": "low", "tracker_id": "M13B-L044"}'
  FROM _m13_claim_map c
  JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O003'
  WHERE c.tracker_id = 'M13B-C020'
  RETURNING link_id
)
INSERT INTO _m13_link_map (tracker_id, link_id) SELECT 'M13B-L044', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cross-source contextual link preserving model/timing boundaries.", "strength": "low", "tracker_id": "M13B-L045"}'
  FROM _m13_claim_map c
  JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O004'
  WHERE c.tracker_id = 'M13B-C021'
  RETURNING link_id
)
INSERT INTO _m13_link_map (tracker_id, link_id) SELECT 'M13B-L045', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cross-source contextual link preserving model/timing boundaries.", "strength": "low", "tracker_id": "M13B-L046"}'
  FROM _m13_claim_map c
  JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O005'
  WHERE c.tracker_id = 'M13B-C022'
  RETURNING link_id
)
INSERT INTO _m13_link_map (tracker_id, link_id) SELECT 'M13B-L046', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cross-source contextual link preserving model/timing boundaries.", "strength": "low", "tracker_id": "M13B-L047"}'
  FROM _m13_claim_map c
  JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O006'
  WHERE c.tracker_id = 'M13B-C023'
  RETURNING link_id
)
INSERT INTO _m13_link_map (tracker_id, link_id) SELECT 'M13B-L047', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cross-source contextual link preserving model/timing boundaries.", "strength": "low", "tracker_id": "M13B-L048"}'
  FROM _m13_claim_map c
  JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O007'
  WHERE c.tracker_id = 'M13B-C024'
  RETURNING link_id
)
INSERT INTO _m13_link_map (tracker_id, link_id) SELECT 'M13B-L048', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cross-source contextual link preserving model/timing boundaries.", "strength": "low", "tracker_id": "M13B-L049"}'
  FROM _m13_claim_map c
  JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O008'
  WHERE c.tracker_id = 'M13B-C001'
  RETURNING link_id
)
INSERT INTO _m13_link_map (tracker_id, link_id) SELECT 'M13B-L049', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cross-source contextual link preserving model/timing boundaries.", "strength": "low", "tracker_id": "M13B-L050"}'
  FROM _m13_claim_map c
  JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O009'
  WHERE c.tracker_id = 'M13B-C002'
  RETURNING link_id
)
INSERT INTO _m13_link_map (tracker_id, link_id) SELECT 'M13B-L050', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cross-source contextual link preserving model/timing boundaries.", "strength": "low", "tracker_id": "M13B-L051"}'
  FROM _m13_claim_map c
  JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O010'
  WHERE c.tracker_id = 'M13B-C003'
  RETURNING link_id
)
INSERT INTO _m13_link_map (tracker_id, link_id) SELECT 'M13B-L051', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cross-source contextual link preserving model/timing boundaries.", "strength": "low", "tracker_id": "M13B-L052"}'
  FROM _m13_claim_map c
  JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O011'
  WHERE c.tracker_id = 'M13B-C004'
  RETURNING link_id
)
INSERT INTO _m13_link_map (tracker_id, link_id) SELECT 'M13B-L052', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cross-source contextual link preserving model/timing boundaries.", "strength": "low", "tracker_id": "M13B-L053"}'
  FROM _m13_claim_map c
  JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O012'
  WHERE c.tracker_id = 'M13B-C005'
  RETURNING link_id
)
INSERT INTO _m13_link_map (tracker_id, link_id) SELECT 'M13B-L053', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cross-source contextual link preserving model/timing boundaries.", "strength": "low", "tracker_id": "M13B-L054"}'
  FROM _m13_claim_map c
  JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O013'
  WHERE c.tracker_id = 'M13B-C006'
  RETURNING link_id
)
INSERT INTO _m13_link_map (tracker_id, link_id) SELECT 'M13B-L054', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cross-source contextual link preserving model/timing boundaries.", "strength": "low", "tracker_id": "M13B-L055"}'
  FROM _m13_claim_map c
  JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O014'
  WHERE c.tracker_id = 'M13B-C007'
  RETURNING link_id
)
INSERT INTO _m13_link_map (tracker_id, link_id) SELECT 'M13B-L055', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cross-source contextual link preserving model/timing boundaries.", "strength": "low", "tracker_id": "M13B-L056"}'
  FROM _m13_claim_map c
  JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O015'
  WHERE c.tracker_id = 'M13B-C008'
  RETURNING link_id
)
INSERT INTO _m13_link_map (tracker_id, link_id) SELECT 'M13B-L056', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Primary traumatic SCI sets an initial lesion geometry, but the chronic lesion is produced by a time-dependent cascade rather than by the mechanical insult alone; injury model, severity, spinal level, and early hemorrhage must be retained as causal boundaries.',
    'M13B-T001',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M13B-B001", "M13B-B002", "M13B-B003", "M13B-B004", "M13B-B005", "M13B-B006", "M13B-B007", "M13B-B008"], "claim_tracker_ids": ["M13B-C001", "M13B-C002", "M13B-C003"], "consensus_draft_id": "M13B-S001", "observation_tracker_ids": ["M13B-O001", "M13B-O002", "M13B-O003"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 13 first-pass curation freeze.", "topic_id": "M13B-T001"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m13_consensus_map (tracker_id, consensus_id) SELECT 'M13B-S001', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m13_consensus_map c
JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O001'
WHERE c.tracker_id = 'M13B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m13_consensus_map c
JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O002'
WHERE c.tracker_id = 'M13B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m13_consensus_map c
JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O003'
WHERE c.tracker_id = 'M13B-S001';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Vascular failure, blood-spinal cord barrier disruption, edema, and progressive hemorrhagic necrosis are early drivers of lesion expansion and are experimentally modifiable, making vascular integrity a core injury-to-lesion mechanism.',
    'M13B-T002',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M13B-B001", "M13B-B002", "M13B-B003", "M13B-B004", "M13B-B005", "M13B-B006", "M13B-B007", "M13B-B008"], "claim_tracker_ids": ["M13B-C004", "M13B-C005", "M13B-C006"], "consensus_draft_id": "M13B-S002", "observation_tracker_ids": ["M13B-O004", "M13B-O005", "M13B-O006"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 13 first-pass curation freeze.", "topic_id": "M13B-T002"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m13_consensus_map (tracker_id, consensus_id) SELECT 'M13B-S002', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m13_consensus_map c
JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O004'
WHERE c.tracker_id = 'M13B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m13_consensus_map c
JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O005'
WHERE c.tracker_id = 'M13B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m13_consensus_map c
JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O006'
WHERE c.tracker_id = 'M13B-S002';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Gray matter loss can occur rapidly while white matter loss, axon degeneration, demyelination, and Wallerian degeneration evolve over longer windows, so chronic spared-tissue anatomy must be interpreted through time-resolved tract and cell-population boundaries.',
    'M13B-T003',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M13B-B001", "M13B-B002", "M13B-B003", "M13B-B004", "M13B-B005", "M13B-B006", "M13B-B007", "M13B-B008"], "claim_tracker_ids": ["M13B-C007", "M13B-C008", "M13B-C009"], "consensus_draft_id": "M13B-S003", "observation_tracker_ids": ["M13B-O007", "M13B-O008", "M13B-O009"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 13 first-pass curation freeze.", "topic_id": "M13B-T003"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m13_consensus_map (tracker_id, consensus_id) SELECT 'M13B-S003', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m13_consensus_map c
JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O007'
WHERE c.tracker_id = 'M13B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m13_consensus_map c
JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O008'
WHERE c.tracker_id = 'M13B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m13_consensus_map c
JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O009'
WHERE c.tracker_id = 'M13B-S003';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Innate immune responses after traumatic SCI are not only damaging inflammation: microglia and macrophages can expand injury, clear debris, compact wounds, corral lesion cores, and alter chronic neurodegeneration depending on timing and state.',
    'M13B-T004',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M13B-B001", "M13B-B002", "M13B-B003", "M13B-B004", "M13B-B005", "M13B-B006", "M13B-B007", "M13B-B008"], "claim_tracker_ids": ["M13B-C010", "M13B-C011", "M13B-C012"], "consensus_draft_id": "M13B-S004", "observation_tracker_ids": ["M13B-O010", "M13B-O011", "M13B-O012"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 13 first-pass curation freeze.", "topic_id": "M13B-T004"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m13_consensus_map (tracker_id, consensus_id) SELECT 'M13B-S004', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m13_consensus_map c
JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O010'
WHERE c.tracker_id = 'M13B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m13_consensus_map c
JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O011'
WHERE c.tracker_id = 'M13B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m13_consensus_map c
JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O012'
WHERE c.tracker_id = 'M13B-S004';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Astrocytic border formation is an active wound-repair process that contains non-neural lesion cores and coordinates multicellular scar responses; it should not be summarized only as a regeneration-inhibitory barrier.',
    'M13B-T005',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M13B-B001", "M13B-B002", "M13B-B003", "M13B-B004", "M13B-B005", "M13B-B006", "M13B-B007", "M13B-B008"], "claim_tracker_ids": ["M13B-C013", "M13B-C014", "M13B-C015"], "consensus_draft_id": "M13B-S005", "observation_tracker_ids": ["M13B-O013", "M13B-O014", "M13B-O015"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 13 first-pass curation freeze.", "topic_id": "M13B-T005"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m13_consensus_map (tracker_id, consensus_id) SELECT 'M13B-S005', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m13_consensus_map c
JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O013'
WHERE c.tracker_id = 'M13B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m13_consensus_map c
JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O014'
WHERE c.tracker_id = 'M13B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m13_consensus_map c
JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O015'
WHERE c.tracker_id = 'M13B-S005';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Fibrotic scar formation is a spatially organized stromal response involving heterogeneous fibroblast/perivascular/meningeal compartments and extracellular matrix programs that help define the chronic lesion core and interface.',
    'M13B-T006',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M13B-B001", "M13B-B002", "M13B-B003", "M13B-B004", "M13B-B005", "M13B-B006", "M13B-B007", "M13B-B008"], "claim_tracker_ids": ["M13B-C016", "M13B-C017", "M13B-C018"], "consensus_draft_id": "M13B-S006", "observation_tracker_ids": ["M13B-O016", "M13B-O017", "M13B-O018"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 13 first-pass curation freeze.", "topic_id": "M13B-T006"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m13_consensus_map (tracker_id, consensus_id) SELECT 'M13B-S006', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m13_consensus_map c
JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O016'
WHERE c.tracker_id = 'M13B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m13_consensus_map c
JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O017'
WHERE c.tracker_id = 'M13B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m13_consensus_map c
JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O018'
WHERE c.tracker_id = 'M13B-S006';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Cavitation and chronic lesion stabilization emerge from interacting vascular, immune, glial, stromal, axon/myelin, and tissue-clearance processes; static chronic lesion anatomy should be linked back to the temporal mechanisms that formed it.',
    'M13B-T007',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M13B-B001", "M13B-B002", "M13B-B003", "M13B-B004", "M13B-B005", "M13B-B006", "M13B-B007", "M13B-B008"], "claim_tracker_ids": ["M13B-C019", "M13B-C020", "M13B-C021"], "consensus_draft_id": "M13B-S007", "observation_tracker_ids": ["M13B-O019", "M13B-O020", "M13B-O021"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 13 first-pass curation freeze.", "topic_id": "M13B-T007"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m13_consensus_map (tracker_id, consensus_id) SELECT 'M13B-S007', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m13_consensus_map c
JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O019'
WHERE c.tracker_id = 'M13B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m13_consensus_map c
JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O020'
WHERE c.tracker_id = 'M13B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m13_consensus_map c
JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O021'
WHERE c.tracker_id = 'M13B-S007';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Module 13 should serve as the causal bridge between model-system selection and chronic lesion architecture: every downstream conditioning, biomaterial, cell, or axon-repair claim should specify which injury-to-lesion process it is expected to modify.',
    'M13B-T008',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M13B-B001", "M13B-B002", "M13B-B003", "M13B-B004", "M13B-B005", "M13B-B006", "M13B-B007", "M13B-B008"], "claim_tracker_ids": ["M13B-C022", "M13B-C023", "M13B-C024"], "consensus_draft_id": "M13B-S008", "observation_tracker_ids": ["M13B-O022", "M13B-O023", "M13B-O024"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 13 first-pass curation freeze.", "topic_id": "M13B-T008"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m13_consensus_map (tracker_id, consensus_id) SELECT 'M13B-S008', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m13_consensus_map c
JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O022'
WHERE c.tracker_id = 'M13B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m13_consensus_map c
JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O023'
WHERE c.tracker_id = 'M13B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m13_consensus_map c
JOIN _m13_observation_map o ON o.tracker_id = 'M13B-O024'
WHERE c.tracker_id = 'M13B-S008';

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
  SELECT COUNT(*) INTO paper_count FROM _m13_paper_map;
  SELECT COUNT(*) INTO experiment_count FROM _m13_experiment_map;
  SELECT COUNT(*) INTO observation_count FROM _m13_observation_map;
  SELECT COUNT(*) INTO claim_count FROM _m13_claim_map;
  SELECT COUNT(*) INTO link_count FROM _m13_link_map;
  SELECT COUNT(*) INTO consensus_count FROM _m13_consensus_map;
  SELECT COUNT(*) INTO consensus_observation_count
  FROM Consensus_Observation co
  JOIN _m13_consensus_map cm ON cm.consensus_id = co.consensus_id;
  IF paper_count <> 24 THEN RAISE EXCEPTION 'Expected 24 papers, found %', paper_count; END IF;
  IF experiment_count <> 24 THEN RAISE EXCEPTION 'Unexpected experiment count %', experiment_count; END IF;
  IF observation_count <> 24 THEN RAISE EXCEPTION 'Expected 24 observations, found %', observation_count; END IF;
  IF claim_count <> 24 THEN RAISE EXCEPTION 'Expected 24 claims, found %', claim_count; END IF;
  IF link_count <> 56 THEN RAISE EXCEPTION 'Expected 56 evidence links, found %', link_count; END IF;
  IF consensus_count <> 8 THEN RAISE EXCEPTION 'Expected 8 consensus rows, found %', consensus_count; END IF;
  IF consensus_observation_count <> 24 THEN RAISE EXCEPTION 'Unexpected consensus-observation count %', consensus_observation_count; END IF;
END $$;

COMMIT;
