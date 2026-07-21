-- Module 12B full first-pass materialization generated from tracker-derived JSON.
-- This script is intended for a fresh database loaded with schema/schema.sql and scripts/seed_controlled_vocab.sql.
BEGIN;

CREATE TEMP TABLE _m12_paper_map (tracker_id TEXT PRIMARY KEY, paper_id INTEGER NOT NULL);
CREATE TEMP TABLE _m12_paradigm_map (tracker_id TEXT PRIMARY KEY, paradigm_id INTEGER NOT NULL);
CREATE TEMP TABLE _m12_experiment_map (tracker_id TEXT PRIMARY KEY, experiment_id INTEGER NOT NULL);
CREATE TEMP TABLE _m12_observation_map (tracker_id TEXT PRIMARY KEY, observation_id INTEGER NOT NULL);
CREATE TEMP TABLE _m12_claim_map (tracker_id TEXT PRIMARY KEY, claim_id INTEGER NOT NULL);
CREATE TEMP TABLE _m12_link_map (tracker_id TEXT PRIMARY KEY, link_id INTEGER NOT NULL);
CREATE TEMP TABLE _m12_consensus_map (tracker_id TEXT PRIMARY KEY, consensus_id INTEGER NOT NULL);

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Lipopolysaccharide preconditioning facilitates M2 activation of resident microglia after spinal cord injury', 'Hayakawa', 2014,
    'Journal of Neuroinflammation', NULL, NULL,
    NULL, NULL, '25044014',
    NULL, '{"curator_notes": "Mouse thoracic contusion; systemic low-dose LPS 48 h before SCI; resident microglia M2/IL-10/IRF3 and functional/tissue repair signal.", "module": "Module 12B", "tracker_id": "M12A-P001"}'
  )
  RETURNING paper_id
)
INSERT INTO _m12_paper_map (tracker_id, paper_id) SELECT 'M12A-P001', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Serial Systemic Injections of Endotoxin (LPS) Elicit Neuroprotective Spinal Cord Microglia through IL-1-Dependent Cross Talk with Endothelial Cells', 'Freria', 2020,
    'Journal of Neuroscience', NULL, NULL,
    NULL, NULL, 'PMC7672996',
    NULL, '{"curator_notes": "Repeated systemic LPS primes spinal cord microglia/endothelium and protects in ischemic SCI; IL-1-dependent cross-talk boundary.", "module": "Module 12B", "tracker_id": "M12A-P002"}'
  )
  RETURNING paper_id
)
INSERT INTO _m12_paper_map (tracker_id, paper_id) SELECT 'M12A-P002', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Dynamic Interleukin-1 Receptor Type 1 Signaling Mediates Microglia-Vasculature Interactions Following Repeated Systemic LPS', 'Nemeth', 2022,
    'Journal of Neuroscience', NULL, NULL,
    NULL, NULL, 'PMC8906862',
    NULL, '{"curator_notes": "Repeated LPS programs spinal microglia-vascular interactions through IL-1R1 signaling; mechanistic follow-up to Freria.", "module": "Module 12B", "tracker_id": "M12A-P003"}'
  )
  RETURNING paper_id
)
INSERT INTO _m12_paper_map (tracker_id, paper_id) SELECT 'M12A-P003', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'LPS Preconditioning Attenuates Apoptosis Mechanism by Inhibiting NF-kB and Caspase-3 Activity: TLR4 Pre-activation in the Signaling Pathway of LPS-Induced Neuroprotection', 'Sangaran', 2021,
    'Molecular Neurobiology', NULL, NULL,
    NULL, NULL, '33421016',
    NULL, '{"curator_notes": "Review anchor for LPS/TLR4 preconditioning mechanisms and apoptosis/NF-kB/caspase-3 boundaries.", "module": "Module 12B", "tracker_id": "M12A-P004"}'
  )
  RETURNING paper_id
)
INSERT INTO _m12_paper_map (tracker_id, paper_id) SELECT 'M12A-P004', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'LPS preconditioning redirects TLR signaling following stroke: TRIF-IRF3 plays a seminal role in mediating tolerance to ischemic injury', 'Vartanian', 2011,
    'Journal of Neuroinflammation', NULL, NULL,
    NULL, NULL, 'PMC3217906',
    NULL, '{"curator_notes": "Brain ischemia comparator; TRIF-IRF3 and NF-kB redirection provide mechanistic boundary for innate conditioning.", "module": "Module 12B", "tracker_id": "M12A-P005"}'
  )
  RETURNING paper_id
)
INSERT INTO _m12_paper_map (tracker_id, paper_id) SELECT 'M12A-P005', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Endogenous Protection from Ischemic Brain Injury by Preconditioned Monocytes', 'Garcia-Bonilla', 2018,
    'Journal of Neuroscience', NULL, NULL,
    NULL, NULL, '29946039',
    NULL, '{"curator_notes": "Peripheral monocyte preconditioning comparator; IL-10/iNOS/CCR2 and adoptive-transfer logic for systemic conditioning.", "module": "Module 12B", "tracker_id": "M12A-P006"}'
  )
  RETURNING paper_id
)
INSERT INTO _m12_paper_map (tracker_id, paper_id) SELECT 'M12A-P006', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Neuroprotection by Preconditioning in Mice is Dependent on MyD88-Mediated CXCL10 Expression in Endothelial Cells', 'Zhang', 2023,
    'Journal of Neuroscience', NULL, NULL,
    NULL, NULL, '36591943',
    NULL, '{"curator_notes": "Peripheral LPS preconditioning brain ischemia model; endothelial MyD88/CXCL10 upstream regulatory-node comparator.", "module": "Module 12B", "tracker_id": "M12A-P007"}'
  )
  RETURNING paper_id
)
INSERT INTO _m12_paper_map (tracker_id, paper_id) SELECT 'M12A-P007', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'TLR4 Deficiency Impairs Oligodendrocyte Formation in the Injured Spinal Cord', 'Church', 2016,
    'Journal of Neuroscience', NULL, NULL,
    NULL, NULL, '27277810',
    NULL, '{"curator_notes": "SCI TLR4 boundary; innate inflammatory signaling can support myelin debris clearance, oligodendrocyte replacement, and recovery.", "module": "Module 12B", "tracker_id": "M12A-P008"}'
  )
  RETURNING paper_id
)
INSERT INTO _m12_paper_map (tracker_id, paper_id) SELECT 'M12A-P008', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Spinal cord injury in the rat: treatment with bacterial lipopolysaccharide and indomethacin enhances cellular repair and locomotor function', 'Guth', 1994,
    'Experimental Neurology', NULL, NULL,
    NULL, NULL, '8157128',
    NULL, '{"curator_notes": "Older traumatic SCI treatment row; LPS plus indomethacin after SCI improves repair/locomotion but not preconditioning.", "module": "Module 12B", "tracker_id": "M12A-P009"}'
  )
  RETURNING paper_id
)
INSERT INTO _m12_paper_map (tracker_id, paper_id) SELECT 'M12A-P009', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Reawakening inflammation in the chronically injured spinal cord using lipopolysaccharide induces diverse microglial states', 'Cucarian', 2025,
    'Nature Communications', NULL, NULL,
    NULL, NULL, '40022205',
    NULL, '{"curator_notes": "Chronic SCI scRNA-seq/plasticity row; LPS reawakens inflammatory/microglial states after chronic injury.", "module": "Module 12B", "tracker_id": "M12A-P010"}'
  )
  RETURNING paper_id
)
INSERT INTO _m12_paper_map (tracker_id, paper_id) SELECT 'M12A-P010', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Different TLR4 expression and microglia/macrophage activation induced by hemorrhage in the rat spinal cord after compressive injury', 'Zhang', 2013,
    'Journal of Neuroinflammation', NULL, NULL,
    NULL, NULL, '24015844',
    NULL, '{"curator_notes": "Traumatic SCI hemorrhage boundary; TLR4/microglia activation varies with lesion context.", "module": "Module 12B", "tracker_id": "M12A-P011"}'
  )
  RETURNING paper_id
)
INSERT INTO _m12_paper_map (tracker_id, paper_id) SELECT 'M12A-P011', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Redefining macrophage phenotypes after spinal cord injury: An open data approach', 'Bradbury', 2025,
    'Nature Communications', NULL, NULL,
    NULL, NULL, '40113007',
    NULL, '{"curator_notes": "Open-data macrophage phenotype boundary; limits simple M1/M2 interpretation in SCI.", "module": "Module 12B", "tracker_id": "M12A-P012"}'
  )
  RETURNING paper_id
)
INSERT INTO _m12_paper_map (tracker_id, paper_id) SELECT 'M12A-P012', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Single low-dose lipopolysaccharide preconditioning: neuroprotective against axonal injury and modulates glial cells', 'Bastien', 2017,
    'PLoS ONE', NULL, NULL,
    NULL, NULL, 'PMC5289820',
    NULL, '{"curator_notes": "TBI comparator; single low-dose LPS preconditioning reduces axonal injury and changes glial responses.", "module": "Module 12B", "tracker_id": "M12A-P013"}'
  )
  RETURNING paper_id
)
INSERT INTO _m12_paper_map (tracker_id, paper_id) SELECT 'M12A-P013', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Sevoflurane preconditioning ameliorates spinal cord ischemia/reperfusion injury by modulating microglia/macrophage polarization via GSK-3b/Nrf2', 'Cai', 2021,
    'Journal of Neuroinflammation', NULL, NULL,
    NULL, NULL, '34370899',
    NULL, '{"curator_notes": "Non-LPS comparator preserving polarization endpoint and regulatory-node logic in spinal cord ischemia.", "module": "Module 12B", "tracker_id": "M12A-P014"}'
  )
  RETURNING paper_id
)
INSERT INTO _m12_paper_map (tracker_id, paper_id) SELECT 'M12A-P014', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Ischemic preconditioning protects against spinal cord ischemia-reperfusion injury in rabbits by attenuating blood spinal cord barrier disruption', 'Fang', 2013,
    'Molecular Neurobiology', NULL, NULL,
    NULL, NULL, '23685868',
    NULL, '{"curator_notes": "Non-LPS spinal ischemia comparator; barrier, ZO-1, MMP-9, TNF-alpha boundaries.", "module": "Module 12B", "tracker_id": "M12A-P015"}'
  )
  RETURNING paper_id
)
INSERT INTO _m12_paper_map (tracker_id, paper_id) SELECT 'M12A-P015', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Co-application of ischemic preconditioning and postconditioning provides additive neuroprotection against spinal cord ischemia in rabbits', 'Jiang', 2008,
    'Anesthesiology', NULL, NULL,
    NULL, NULL, '18275975',
    NULL, '{"curator_notes": "Non-LPS spinal ischemia conditioning comparator; timing/additivity boundary.", "module": "Module 12B", "tracker_id": "M12A-P016"}'
  )
  RETURNING paper_id
)
INSERT INTO _m12_paper_map (tracker_id, paper_id) SELECT 'M12A-P016', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'TLR2 agonist Pam3CSK4 dose-response testing after SCI', 'ODC-SCI', 2026,
    'ODC-SCI dataset', NULL, NULL,
    NULL, NULL, 'ODC-SCI:1389',
    NULL, '{"curator_notes": "ODC dataset row from prior audit; TLR agonist/dose-response comparator for innate immune conditioning.", "module": "Module 12B", "tracker_id": "M12A-P017"}'
  )
  RETURNING paper_id
)
INSERT INTO _m12_paper_map (tracker_id, paper_id) SELECT 'M12A-P017', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'TLR2 and TLR4 agonist testing in SCI', 'ODC-SCI', 2026,
    'ODC-SCI dataset', NULL, NULL,
    NULL, NULL, 'ODC-SCI:1387',
    NULL, '{"curator_notes": "ODC dataset row from prior audit; innate agonist boundary requiring source extraction.", "module": "Module 12B", "tracker_id": "M12A-P018"}'
  )
  RETURNING paper_id
)
INSERT INTO _m12_paper_map (tracker_id, paper_id) SELECT 'M12A-P018', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Systemic LPS drives microglia-mediated perineuronal net degradation after cervical SCI', 'ODC-SCI', 2026,
    'ODC-SCI dataset', NULL, NULL,
    NULL, NULL, 'ODC-SCI:1536',
    NULL, '{"curator_notes": "ODC dataset row from prior audit; systemic LPS after cervical SCI and PNN/plasticity endpoint.", "module": "Module 12B", "tracker_id": "M12A-P019"}'
  )
  RETURNING paper_id
)
INSERT INTO _m12_paper_map (tracker_id, paper_id) SELECT 'M12A-P019', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Cultured macrophage with spinal cord homogenate and PI3K inhibition', 'ODC-SCI', 2026,
    'ODC-SCI dataset', NULL, NULL,
    NULL, NULL, 'ODC-SCI:930',
    NULL, '{"curator_notes": "In vitro bridge for macrophage activation/regulatory-node validation after SCI homogenate exposure.", "module": "Module 12B", "tracker_id": "M12A-P020"}'
  )
  RETURNING paper_id
)
INSERT INTO _m12_paper_map (tracker_id, paper_id) SELECT 'M12A-P020', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Pleiotrophin in vitro and dose-response in vivo SCI dataset', 'ODC-SCI', 2026,
    'ODC-SCI dataset', NULL, NULL,
    NULL, NULL, 'ODC-SCI:1235',
    NULL, '{"curator_notes": "In vitro/in vivo validation structure comparator for conditioning-derived candidate testing.", "module": "Module 12B", "tracker_id": "M12A-P021"}'
  )
  RETURNING paper_id
)
INSERT INTO _m12_paper_map (tracker_id, paper_id) SELECT 'M12A-P021', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Probiotic treatment after C5 contusion', 'ODC-SCI', 2026,
    'ODC-SCI dataset', NULL, NULL,
    NULL, NULL, 'ODC-SCI:688',
    NULL, '{"curator_notes": "Microbiome/systemic inflammation safer host-conditioning comparator.", "module": "Module 12B", "tracker_id": "M12A-P022"}'
  )
  RETURNING paper_id
)
INSERT INTO _m12_paper_map (tracker_id, paper_id) SELECT 'M12A-P022', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Fecal transplant after unilateral cervical contusion', 'ODC-SCI', 2026,
    'ODC-SCI dataset', NULL, NULL,
    NULL, NULL, 'ODC-SCI:578',
    NULL, '{"curator_notes": "Microbiota-transfer host-conditioning comparator; separates LPS mechanism from translational alternatives.", "module": "Module 12B", "tracker_id": "M12A-P023"}'
  )
  RETURNING paper_id
)
INSERT INTO _m12_paper_map (tracker_id, paper_id) SELECT 'M12A-P023', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Revised Specific Aims Preconditioning Logic', 'mSCIdblit project', 2026,
    'Project aims', NULL, NULL,
    NULL, NULL, 'Project aims document',
    NULL, '{"curator_notes": "Project logic anchor: innate immune conditioning is broader than LPS; endotoxin/LPS is one discovery platform, not a clinical therapeutic.", "module": "Module 12B", "tracker_id": "M12A-P024"}'
  )
  RETURNING paper_id
)
INSERT INTO _m12_paper_map (tracker_id, paper_id) SELECT 'M12A-P024', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 12B curated evidence extraction',
    'First-pass Module 12B innate immune conditioning and tolerance biology curation for M12A-P001',
    'Tracker-derived materialization from Module_12B_TRACKER.md'
  FROM _m12_paper_map WHERE tracker_id = 'M12A-P001'
  RETURNING paradigm_id
)
INSERT INTO _m12_paradigm_map (tracker_id, paradigm_id) SELECT 'M12A-P001', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 12B curated evidence extraction',
    'First-pass Module 12B innate immune conditioning and tolerance biology curation for M12A-P002',
    'Tracker-derived materialization from Module_12B_TRACKER.md'
  FROM _m12_paper_map WHERE tracker_id = 'M12A-P002'
  RETURNING paradigm_id
)
INSERT INTO _m12_paradigm_map (tracker_id, paradigm_id) SELECT 'M12A-P002', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 12B curated evidence extraction',
    'First-pass Module 12B innate immune conditioning and tolerance biology curation for M12A-P003',
    'Tracker-derived materialization from Module_12B_TRACKER.md'
  FROM _m12_paper_map WHERE tracker_id = 'M12A-P003'
  RETURNING paradigm_id
)
INSERT INTO _m12_paradigm_map (tracker_id, paradigm_id) SELECT 'M12A-P003', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 12B curated evidence extraction',
    'First-pass Module 12B innate immune conditioning and tolerance biology curation for M12A-P004',
    'Tracker-derived materialization from Module_12B_TRACKER.md'
  FROM _m12_paper_map WHERE tracker_id = 'M12A-P004'
  RETURNING paradigm_id
)
INSERT INTO _m12_paradigm_map (tracker_id, paradigm_id) SELECT 'M12A-P004', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 12B curated evidence extraction',
    'First-pass Module 12B innate immune conditioning and tolerance biology curation for M12A-P005',
    'Tracker-derived materialization from Module_12B_TRACKER.md'
  FROM _m12_paper_map WHERE tracker_id = 'M12A-P005'
  RETURNING paradigm_id
)
INSERT INTO _m12_paradigm_map (tracker_id, paradigm_id) SELECT 'M12A-P005', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 12B curated evidence extraction',
    'First-pass Module 12B innate immune conditioning and tolerance biology curation for M12A-P006',
    'Tracker-derived materialization from Module_12B_TRACKER.md'
  FROM _m12_paper_map WHERE tracker_id = 'M12A-P006'
  RETURNING paradigm_id
)
INSERT INTO _m12_paradigm_map (tracker_id, paradigm_id) SELECT 'M12A-P006', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 12B curated evidence extraction',
    'First-pass Module 12B innate immune conditioning and tolerance biology curation for M12A-P007',
    'Tracker-derived materialization from Module_12B_TRACKER.md'
  FROM _m12_paper_map WHERE tracker_id = 'M12A-P007'
  RETURNING paradigm_id
)
INSERT INTO _m12_paradigm_map (tracker_id, paradigm_id) SELECT 'M12A-P007', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 12B curated evidence extraction',
    'First-pass Module 12B innate immune conditioning and tolerance biology curation for M12A-P008',
    'Tracker-derived materialization from Module_12B_TRACKER.md'
  FROM _m12_paper_map WHERE tracker_id = 'M12A-P008'
  RETURNING paradigm_id
)
INSERT INTO _m12_paradigm_map (tracker_id, paradigm_id) SELECT 'M12A-P008', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 12B curated evidence extraction',
    'First-pass Module 12B innate immune conditioning and tolerance biology curation for M12A-P009',
    'Tracker-derived materialization from Module_12B_TRACKER.md'
  FROM _m12_paper_map WHERE tracker_id = 'M12A-P009'
  RETURNING paradigm_id
)
INSERT INTO _m12_paradigm_map (tracker_id, paradigm_id) SELECT 'M12A-P009', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 12B curated evidence extraction',
    'First-pass Module 12B innate immune conditioning and tolerance biology curation for M12A-P010',
    'Tracker-derived materialization from Module_12B_TRACKER.md'
  FROM _m12_paper_map WHERE tracker_id = 'M12A-P010'
  RETURNING paradigm_id
)
INSERT INTO _m12_paradigm_map (tracker_id, paradigm_id) SELECT 'M12A-P010', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 12B curated evidence extraction',
    'First-pass Module 12B innate immune conditioning and tolerance biology curation for M12A-P011',
    'Tracker-derived materialization from Module_12B_TRACKER.md'
  FROM _m12_paper_map WHERE tracker_id = 'M12A-P011'
  RETURNING paradigm_id
)
INSERT INTO _m12_paradigm_map (tracker_id, paradigm_id) SELECT 'M12A-P011', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 12B curated evidence extraction',
    'First-pass Module 12B innate immune conditioning and tolerance biology curation for M12A-P012',
    'Tracker-derived materialization from Module_12B_TRACKER.md'
  FROM _m12_paper_map WHERE tracker_id = 'M12A-P012'
  RETURNING paradigm_id
)
INSERT INTO _m12_paradigm_map (tracker_id, paradigm_id) SELECT 'M12A-P012', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 12B curated evidence extraction',
    'First-pass Module 12B innate immune conditioning and tolerance biology curation for M12A-P013',
    'Tracker-derived materialization from Module_12B_TRACKER.md'
  FROM _m12_paper_map WHERE tracker_id = 'M12A-P013'
  RETURNING paradigm_id
)
INSERT INTO _m12_paradigm_map (tracker_id, paradigm_id) SELECT 'M12A-P013', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 12B curated evidence extraction',
    'First-pass Module 12B innate immune conditioning and tolerance biology curation for M12A-P014',
    'Tracker-derived materialization from Module_12B_TRACKER.md'
  FROM _m12_paper_map WHERE tracker_id = 'M12A-P014'
  RETURNING paradigm_id
)
INSERT INTO _m12_paradigm_map (tracker_id, paradigm_id) SELECT 'M12A-P014', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 12B curated evidence extraction',
    'First-pass Module 12B innate immune conditioning and tolerance biology curation for M12A-P015',
    'Tracker-derived materialization from Module_12B_TRACKER.md'
  FROM _m12_paper_map WHERE tracker_id = 'M12A-P015'
  RETURNING paradigm_id
)
INSERT INTO _m12_paradigm_map (tracker_id, paradigm_id) SELECT 'M12A-P015', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 12B curated evidence extraction',
    'First-pass Module 12B innate immune conditioning and tolerance biology curation for M12A-P016',
    'Tracker-derived materialization from Module_12B_TRACKER.md'
  FROM _m12_paper_map WHERE tracker_id = 'M12A-P016'
  RETURNING paradigm_id
)
INSERT INTO _m12_paradigm_map (tracker_id, paradigm_id) SELECT 'M12A-P016', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 12B curated evidence extraction',
    'First-pass Module 12B innate immune conditioning and tolerance biology curation for M12A-P017',
    'Tracker-derived materialization from Module_12B_TRACKER.md'
  FROM _m12_paper_map WHERE tracker_id = 'M12A-P017'
  RETURNING paradigm_id
)
INSERT INTO _m12_paradigm_map (tracker_id, paradigm_id) SELECT 'M12A-P017', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 12B curated evidence extraction',
    'First-pass Module 12B innate immune conditioning and tolerance biology curation for M12A-P018',
    'Tracker-derived materialization from Module_12B_TRACKER.md'
  FROM _m12_paper_map WHERE tracker_id = 'M12A-P018'
  RETURNING paradigm_id
)
INSERT INTO _m12_paradigm_map (tracker_id, paradigm_id) SELECT 'M12A-P018', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 12B curated evidence extraction',
    'First-pass Module 12B innate immune conditioning and tolerance biology curation for M12A-P019',
    'Tracker-derived materialization from Module_12B_TRACKER.md'
  FROM _m12_paper_map WHERE tracker_id = 'M12A-P019'
  RETURNING paradigm_id
)
INSERT INTO _m12_paradigm_map (tracker_id, paradigm_id) SELECT 'M12A-P019', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 12B curated evidence extraction',
    'First-pass Module 12B innate immune conditioning and tolerance biology curation for M12A-P020',
    'Tracker-derived materialization from Module_12B_TRACKER.md'
  FROM _m12_paper_map WHERE tracker_id = 'M12A-P020'
  RETURNING paradigm_id
)
INSERT INTO _m12_paradigm_map (tracker_id, paradigm_id) SELECT 'M12A-P020', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 12B curated evidence extraction',
    'First-pass Module 12B innate immune conditioning and tolerance biology curation for M12A-P021',
    'Tracker-derived materialization from Module_12B_TRACKER.md'
  FROM _m12_paper_map WHERE tracker_id = 'M12A-P021'
  RETURNING paradigm_id
)
INSERT INTO _m12_paradigm_map (tracker_id, paradigm_id) SELECT 'M12A-P021', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 12B curated evidence extraction',
    'First-pass Module 12B innate immune conditioning and tolerance biology curation for M12A-P022',
    'Tracker-derived materialization from Module_12B_TRACKER.md'
  FROM _m12_paper_map WHERE tracker_id = 'M12A-P022'
  RETURNING paradigm_id
)
INSERT INTO _m12_paradigm_map (tracker_id, paradigm_id) SELECT 'M12A-P022', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 12B curated evidence extraction',
    'First-pass Module 12B innate immune conditioning and tolerance biology curation for M12A-P023',
    'Tracker-derived materialization from Module_12B_TRACKER.md'
  FROM _m12_paper_map WHERE tracker_id = 'M12A-P023'
  RETURNING paradigm_id
)
INSERT INTO _m12_paradigm_map (tracker_id, paradigm_id) SELECT 'M12A-P023', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 12B curated evidence extraction',
    'First-pass Module 12B innate immune conditioning and tolerance biology curation for M12A-P024',
    'Tracker-derived materialization from Module_12B_TRACKER.md'
  FROM _m12_paper_map WHERE tracker_id = 'M12A-P024'
  RETURNING paradigm_id
)
INSERT INTO _m12_paradigm_map (tracker_id, paradigm_id) SELECT 'M12A-P024', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M12A-P001-E001',
    'Module 12B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M12B-O001"], "source_experiment_tracker_id": "M12A-P001-E001", "source_paper_tracker_id": "M12A-P001", "tracker_key": "M12A-P001::M12A-P001-E001"}'
  FROM _m12_paper_map p
  JOIN _m12_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M12A-P001'
  RETURNING experiment_id
)
INSERT INTO _m12_experiment_map (tracker_id, experiment_id) SELECT 'M12A-P001::M12A-P001-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M12A-P002-E001',
    'Module 12B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M12B-O002"], "source_experiment_tracker_id": "M12A-P002-E001", "source_paper_tracker_id": "M12A-P002", "tracker_key": "M12A-P002::M12A-P002-E001"}'
  FROM _m12_paper_map p
  JOIN _m12_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M12A-P002'
  RETURNING experiment_id
)
INSERT INTO _m12_experiment_map (tracker_id, experiment_id) SELECT 'M12A-P002::M12A-P002-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M12A-P003-E001',
    'Module 12B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M12B-O003"], "source_experiment_tracker_id": "M12A-P003-E001", "source_paper_tracker_id": "M12A-P003", "tracker_key": "M12A-P003::M12A-P003-E001"}'
  FROM _m12_paper_map p
  JOIN _m12_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M12A-P003'
  RETURNING experiment_id
)
INSERT INTO _m12_experiment_map (tracker_id, experiment_id) SELECT 'M12A-P003::M12A-P003-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M12A-P004-E001',
    'Module 12B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M12B-O004"], "source_experiment_tracker_id": "M12A-P004-E001", "source_paper_tracker_id": "M12A-P004", "tracker_key": "M12A-P004::M12A-P004-E001"}'
  FROM _m12_paper_map p
  JOIN _m12_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M12A-P004'
  RETURNING experiment_id
)
INSERT INTO _m12_experiment_map (tracker_id, experiment_id) SELECT 'M12A-P004::M12A-P004-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M12A-P005-E001',
    'Module 12B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M12B-O005"], "source_experiment_tracker_id": "M12A-P005-E001", "source_paper_tracker_id": "M12A-P005", "tracker_key": "M12A-P005::M12A-P005-E001"}'
  FROM _m12_paper_map p
  JOIN _m12_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M12A-P005'
  RETURNING experiment_id
)
INSERT INTO _m12_experiment_map (tracker_id, experiment_id) SELECT 'M12A-P005::M12A-P005-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M12A-P006-E001',
    'Module 12B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M12B-O006"], "source_experiment_tracker_id": "M12A-P006-E001", "source_paper_tracker_id": "M12A-P006", "tracker_key": "M12A-P006::M12A-P006-E001"}'
  FROM _m12_paper_map p
  JOIN _m12_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M12A-P006'
  RETURNING experiment_id
)
INSERT INTO _m12_experiment_map (tracker_id, experiment_id) SELECT 'M12A-P006::M12A-P006-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M12A-P007-E001',
    'Module 12B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M12B-O007"], "source_experiment_tracker_id": "M12A-P007-E001", "source_paper_tracker_id": "M12A-P007", "tracker_key": "M12A-P007::M12A-P007-E001"}'
  FROM _m12_paper_map p
  JOIN _m12_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M12A-P007'
  RETURNING experiment_id
)
INSERT INTO _m12_experiment_map (tracker_id, experiment_id) SELECT 'M12A-P007::M12A-P007-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M12A-P008-E001',
    'Module 12B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M12B-O008"], "source_experiment_tracker_id": "M12A-P008-E001", "source_paper_tracker_id": "M12A-P008", "tracker_key": "M12A-P008::M12A-P008-E001"}'
  FROM _m12_paper_map p
  JOIN _m12_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M12A-P008'
  RETURNING experiment_id
)
INSERT INTO _m12_experiment_map (tracker_id, experiment_id) SELECT 'M12A-P008::M12A-P008-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M12A-P009-E001',
    'Module 12B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M12B-O009"], "source_experiment_tracker_id": "M12A-P009-E001", "source_paper_tracker_id": "M12A-P009", "tracker_key": "M12A-P009::M12A-P009-E001"}'
  FROM _m12_paper_map p
  JOIN _m12_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M12A-P009'
  RETURNING experiment_id
)
INSERT INTO _m12_experiment_map (tracker_id, experiment_id) SELECT 'M12A-P009::M12A-P009-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M12A-P010-E001',
    'Module 12B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M12B-O010"], "source_experiment_tracker_id": "M12A-P010-E001", "source_paper_tracker_id": "M12A-P010", "tracker_key": "M12A-P010::M12A-P010-E001"}'
  FROM _m12_paper_map p
  JOIN _m12_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M12A-P010'
  RETURNING experiment_id
)
INSERT INTO _m12_experiment_map (tracker_id, experiment_id) SELECT 'M12A-P010::M12A-P010-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M12A-P011-E001',
    'Module 12B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M12B-O011"], "source_experiment_tracker_id": "M12A-P011-E001", "source_paper_tracker_id": "M12A-P011", "tracker_key": "M12A-P011::M12A-P011-E001"}'
  FROM _m12_paper_map p
  JOIN _m12_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M12A-P011'
  RETURNING experiment_id
)
INSERT INTO _m12_experiment_map (tracker_id, experiment_id) SELECT 'M12A-P011::M12A-P011-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M12A-P012-E001',
    'Module 12B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M12B-O012"], "source_experiment_tracker_id": "M12A-P012-E001", "source_paper_tracker_id": "M12A-P012", "tracker_key": "M12A-P012::M12A-P012-E001"}'
  FROM _m12_paper_map p
  JOIN _m12_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M12A-P012'
  RETURNING experiment_id
)
INSERT INTO _m12_experiment_map (tracker_id, experiment_id) SELECT 'M12A-P012::M12A-P012-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M12A-P013-E001',
    'Module 12B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M12B-O013"], "source_experiment_tracker_id": "M12A-P013-E001", "source_paper_tracker_id": "M12A-P013", "tracker_key": "M12A-P013::M12A-P013-E001"}'
  FROM _m12_paper_map p
  JOIN _m12_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M12A-P013'
  RETURNING experiment_id
)
INSERT INTO _m12_experiment_map (tracker_id, experiment_id) SELECT 'M12A-P013::M12A-P013-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M12A-P014-E001',
    'Module 12B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M12B-O014"], "source_experiment_tracker_id": "M12A-P014-E001", "source_paper_tracker_id": "M12A-P014", "tracker_key": "M12A-P014::M12A-P014-E001"}'
  FROM _m12_paper_map p
  JOIN _m12_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M12A-P014'
  RETURNING experiment_id
)
INSERT INTO _m12_experiment_map (tracker_id, experiment_id) SELECT 'M12A-P014::M12A-P014-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M12A-P015-E001',
    'Module 12B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M12B-O015"], "source_experiment_tracker_id": "M12A-P015-E001", "source_paper_tracker_id": "M12A-P015", "tracker_key": "M12A-P015::M12A-P015-E001"}'
  FROM _m12_paper_map p
  JOIN _m12_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M12A-P015'
  RETURNING experiment_id
)
INSERT INTO _m12_experiment_map (tracker_id, experiment_id) SELECT 'M12A-P015::M12A-P015-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M12A-P016-E001',
    'Module 12B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M12B-O016"], "source_experiment_tracker_id": "M12A-P016-E001", "source_paper_tracker_id": "M12A-P016", "tracker_key": "M12A-P016::M12A-P016-E001"}'
  FROM _m12_paper_map p
  JOIN _m12_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M12A-P016'
  RETURNING experiment_id
)
INSERT INTO _m12_experiment_map (tracker_id, experiment_id) SELECT 'M12A-P016::M12A-P016-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M12A-P017-E001',
    'Module 12B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M12B-O017"], "source_experiment_tracker_id": "M12A-P017-E001", "source_paper_tracker_id": "M12A-P017", "tracker_key": "M12A-P017::M12A-P017-E001"}'
  FROM _m12_paper_map p
  JOIN _m12_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M12A-P017'
  RETURNING experiment_id
)
INSERT INTO _m12_experiment_map (tracker_id, experiment_id) SELECT 'M12A-P017::M12A-P017-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M12A-P018-E001',
    'Module 12B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M12B-O018"], "source_experiment_tracker_id": "M12A-P018-E001", "source_paper_tracker_id": "M12A-P018", "tracker_key": "M12A-P018::M12A-P018-E001"}'
  FROM _m12_paper_map p
  JOIN _m12_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M12A-P018'
  RETURNING experiment_id
)
INSERT INTO _m12_experiment_map (tracker_id, experiment_id) SELECT 'M12A-P018::M12A-P018-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M12A-P019-E001',
    'Module 12B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M12B-O019"], "source_experiment_tracker_id": "M12A-P019-E001", "source_paper_tracker_id": "M12A-P019", "tracker_key": "M12A-P019::M12A-P019-E001"}'
  FROM _m12_paper_map p
  JOIN _m12_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M12A-P019'
  RETURNING experiment_id
)
INSERT INTO _m12_experiment_map (tracker_id, experiment_id) SELECT 'M12A-P019::M12A-P019-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M12A-P020-E001',
    'Module 12B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M12B-O020"], "source_experiment_tracker_id": "M12A-P020-E001", "source_paper_tracker_id": "M12A-P020", "tracker_key": "M12A-P020::M12A-P020-E001"}'
  FROM _m12_paper_map p
  JOIN _m12_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M12A-P020'
  RETURNING experiment_id
)
INSERT INTO _m12_experiment_map (tracker_id, experiment_id) SELECT 'M12A-P020::M12A-P020-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M12A-P021-E001',
    'Module 12B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M12B-O021"], "source_experiment_tracker_id": "M12A-P021-E001", "source_paper_tracker_id": "M12A-P021", "tracker_key": "M12A-P021::M12A-P021-E001"}'
  FROM _m12_paper_map p
  JOIN _m12_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M12A-P021'
  RETURNING experiment_id
)
INSERT INTO _m12_experiment_map (tracker_id, experiment_id) SELECT 'M12A-P021::M12A-P021-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M12A-P022-E001',
    'Module 12B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M12B-O022"], "source_experiment_tracker_id": "M12A-P022-E001", "source_paper_tracker_id": "M12A-P022", "tracker_key": "M12A-P022::M12A-P022-E001"}'
  FROM _m12_paper_map p
  JOIN _m12_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M12A-P022'
  RETURNING experiment_id
)
INSERT INTO _m12_experiment_map (tracker_id, experiment_id) SELECT 'M12A-P022::M12A-P022-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M12A-P023-E001',
    'Module 12B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M12B-O023"], "source_experiment_tracker_id": "M12A-P023-E001", "source_paper_tracker_id": "M12A-P023", "tracker_key": "M12A-P023::M12A-P023-E001"}'
  FROM _m12_paper_map p
  JOIN _m12_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M12A-P023'
  RETURNING experiment_id
)
INSERT INTO _m12_experiment_map (tracker_id, experiment_id) SELECT 'M12A-P023::M12A-P023-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M12A-P024-E001',
    'Module 12B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M12B-O024"], "source_experiment_tracker_id": "M12A-P024-E001", "source_paper_tracker_id": "M12A-P024", "tracker_key": "M12A-P024::M12A-P024-E001"}'
  FROM _m12_paper_map p
  JOIN _m12_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M12A-P024'
  RETURNING experiment_id
)
INSERT INTO _m12_experiment_map (tracker_id, experiment_id) SELECT 'M12A-P024::M12A-P024-E001', experiment_id FROM inserted;

INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Dataset/in vitro candidate evidence', 'Module 12B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Mechanistic comparator evidence', 'Module 12B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Project logic evidence', 'Module 12B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('SCI innate repair boundary evidence', 'Module 12B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('SCI innate-conditioning evidence', 'Module 12B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Spinal microglia-endothelial evidence', 'Module 12B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;

INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Innate immune conditioning / protection', 'Module 12B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Lipopolysaccharide preconditioning facilitates M2 activation of resident microglia after spinal cord injury tested or summarized Endotoxin/LPS or innate agonist conditioning in Traumatic SCI or post-SCI host response model; first-pass note: Mouse thoracic contusion; systemic low-dose LPS 48 h before SCI; resident microglia M2/IL-10/IRF3 and functional/tissue repair signal.',
    'qualitative',
    'Lipopolysaccharide preconditioning facilitates M2 activation of resident microglia after spinal cord injury tested or summarized Endotoxin/LPS or innate agonist conditioning in Traumatic SCI or post-SCI host response model; first-pass note: Mouse thoracic contusion; systemic low-dose LPS 48 h before SCI; resident microglia M2/IL-10/IRF3 and functional/tissue repair signal.',
    'endotoxin/lps or innate agonist conditioning',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Preserve innate-conditioning stimulus, timing, cell-population, and endpoint boundaries.", "experiment_tracker_id": "M12A-P001-E001", "paper_tracker_id": "M12A-P001", "quantitative": "YES", "statistics_reported": "Mouse thoracic contusion; systemic low-dose LPS 48 h before SCI; resident microglia M2/IL-10/IRF3 and functional/tissue repair signal.", "topic_id": "M12B-T001", "tracker_id": "M12B-O001"}'
  FROM _m12_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M12A-P001::M12A-P001-E001'
    AND et.evidence_type_name = 'SCI innate-conditioning evidence'
    AND ot.outcome_type_name = 'Innate immune conditioning / protection'
  RETURNING observation_id
)
INSERT INTO _m12_observation_map (tracker_id, observation_id) SELECT 'M12B-O001', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Serial Systemic Injections of Endotoxin (LPS) Elicit Neuroprotective Spinal Cord Microglia through IL-1-Dependent Cross Talk with Endothelial Cells tested or summarized Endotoxin/LPS or innate agonist conditioning in Spinal cord ischemia / ischemia-reperfusion model; first-pass note: Repeated systemic LPS primes spinal cord microglia/endothelium and protects in ischemic SCI; IL-1-dependent cross-talk boundary.',
    'qualitative',
    'Serial Systemic Injections of Endotoxin (LPS) Elicit Neuroprotective Spinal Cord Microglia through IL-1-Dependent Cross Talk with Endothelial Cells tested or summarized Endotoxin/LPS or innate agonist conditioning in Spinal cord ischemia / ischemia-reperfusion model; first-pass note: Repeated systemic LPS primes spinal cord microglia/endothelium and protects in ischemic SCI; IL-1-dependent cross-talk boundary.',
    'endotoxin/lps or innate agonist conditioning',
    'Abstract/source page',
    'Abstract/source page',
    'high',
    '{"curator_notes": "Preserve innate-conditioning stimulus, timing, cell-population, and endpoint boundaries.", "experiment_tracker_id": "M12A-P002-E001", "paper_tracker_id": "M12A-P002", "quantitative": "YES", "statistics_reported": "Repeated systemic LPS primes spinal cord microglia/endothelium and protects in ischemic SCI; IL-1-dependent cross-talk boundary.", "topic_id": "M12B-T002", "tracker_id": "M12B-O002"}'
  FROM _m12_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M12A-P002::M12A-P002-E001'
    AND et.evidence_type_name = 'Spinal microglia-endothelial evidence'
    AND ot.outcome_type_name = 'Innate immune conditioning / protection'
  RETURNING observation_id
)
INSERT INTO _m12_observation_map (tracker_id, observation_id) SELECT 'M12B-O002', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Dynamic Interleukin-1 Receptor Type 1 Signaling Mediates Microglia-Vasculature Interactions Following Repeated Systemic LPS tested or summarized Endotoxin/LPS or innate agonist conditioning in Spinal cord ischemia / ischemia-reperfusion model; first-pass note: Repeated LPS programs spinal microglia-vascular interactions through IL-1R1 signaling; mechanistic follow-up to Freria.',
    'qualitative',
    'Dynamic Interleukin-1 Receptor Type 1 Signaling Mediates Microglia-Vasculature Interactions Following Repeated Systemic LPS tested or summarized Endotoxin/LPS or innate agonist conditioning in Spinal cord ischemia / ischemia-reperfusion model; first-pass note: Repeated LPS programs spinal microglia-vascular interactions through IL-1R1 signaling; mechanistic follow-up to Freria.',
    'endotoxin/lps or innate agonist conditioning',
    'Abstract/source page',
    'Abstract/source page',
    'high',
    '{"curator_notes": "Preserve innate-conditioning stimulus, timing, cell-population, and endpoint boundaries.", "experiment_tracker_id": "M12A-P003-E001", "paper_tracker_id": "M12A-P003", "quantitative": "YES", "statistics_reported": "Repeated LPS programs spinal microglia-vascular interactions through IL-1R1 signaling; mechanistic follow-up to Freria.", "topic_id": "M12B-T003", "tracker_id": "M12B-O003"}'
  FROM _m12_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M12A-P003::M12A-P003-E001'
    AND et.evidence_type_name = 'Spinal microglia-endothelial evidence'
    AND ot.outcome_type_name = 'Innate immune conditioning / protection'
  RETURNING observation_id
)
INSERT INTO _m12_observation_map (tracker_id, observation_id) SELECT 'M12B-O003', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'LPS Preconditioning Attenuates Apoptosis Mechanism by Inhibiting NF-kB and Caspase-3 Activity: TLR4 Pre-activation in the Signaling Pathway of LPS-Induced Neuroprotection tested or summarized Endotoxin/LPS or innate agonist conditioning in Review, project, or mechanism anchor; first-pass note: Review anchor for LPS/TLR4 preconditioning mechanisms and apoptosis/NF-kB/caspase-3 boundaries.',
    'qualitative',
    'LPS Preconditioning Attenuates Apoptosis Mechanism by Inhibiting NF-kB and Caspase-3 Activity: TLR4 Pre-activation in the Signaling Pathway of LPS-Induced Neuroprotection tested or summarized Endotoxin/LPS or innate agonist conditioning in Review, project, or mechanism anchor; first-pass note: Review anchor for LPS/TLR4 preconditioning mechanisms and apoptosis/NF-kB/caspase-3 boundaries.',
    'endotoxin/lps or innate agonist conditioning',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Preserve innate-conditioning stimulus, timing, cell-population, and endpoint boundaries.", "experiment_tracker_id": "M12A-P004-E001", "paper_tracker_id": "M12A-P004", "quantitative": "NO", "statistics_reported": "Source-page mechanistic or project-anchor row; exact quantitative estimates not extracted", "topic_id": "M12B-T004", "tracker_id": "M12B-O004"}'
  FROM _m12_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M12A-P004::M12A-P004-E001'
    AND et.evidence_type_name = 'Mechanistic comparator evidence'
    AND ot.outcome_type_name = 'Innate immune conditioning / protection'
  RETURNING observation_id
)
INSERT INTO _m12_observation_map (tracker_id, observation_id) SELECT 'M12B-O004', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'LPS preconditioning redirects TLR signaling following stroke: TRIF-IRF3 plays a seminal role in mediating tolerance to ischemic injury tested or summarized Endotoxin/LPS or innate agonist conditioning in Non-SCI neuroprotection comparator; first-pass note: Brain ischemia comparator; TRIF-IRF3 and NF-kB redirection provide mechanistic boundary for innate conditioning.',
    'qualitative',
    'LPS preconditioning redirects TLR signaling following stroke: TRIF-IRF3 plays a seminal role in mediating tolerance to ischemic injury tested or summarized Endotoxin/LPS or innate agonist conditioning in Non-SCI neuroprotection comparator; first-pass note: Brain ischemia comparator; TRIF-IRF3 and NF-kB redirection provide mechanistic boundary for innate conditioning.',
    'endotoxin/lps or innate agonist conditioning',
    'Abstract/source page',
    'Abstract/source page',
    'high',
    '{"curator_notes": "Preserve innate-conditioning stimulus, timing, cell-population, and endpoint boundaries.", "experiment_tracker_id": "M12A-P005-E001", "paper_tracker_id": "M12A-P005", "quantitative": "NO", "statistics_reported": "Source-page mechanistic or project-anchor row; exact quantitative estimates not extracted", "topic_id": "M12B-T005", "tracker_id": "M12B-O005"}'
  FROM _m12_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M12A-P005::M12A-P005-E001'
    AND et.evidence_type_name = 'Mechanistic comparator evidence'
    AND ot.outcome_type_name = 'Innate immune conditioning / protection'
  RETURNING observation_id
)
INSERT INTO _m12_observation_map (tracker_id, observation_id) SELECT 'M12B-O005', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Endogenous Protection from Ischemic Brain Injury by Preconditioned Monocytes tested or summarized Endotoxin/LPS or innate agonist conditioning in Non-SCI neuroprotection comparator; first-pass note: Peripheral monocyte preconditioning comparator; IL-10/iNOS/CCR2 and adoptive-transfer logic for systemic conditioning.',
    'qualitative',
    'Endogenous Protection from Ischemic Brain Injury by Preconditioned Monocytes tested or summarized Endotoxin/LPS or innate agonist conditioning in Non-SCI neuroprotection comparator; first-pass note: Peripheral monocyte preconditioning comparator; IL-10/iNOS/CCR2 and adoptive-transfer logic for systemic conditioning.',
    'endotoxin/lps or innate agonist conditioning',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Preserve innate-conditioning stimulus, timing, cell-population, and endpoint boundaries.", "experiment_tracker_id": "M12A-P006-E001", "paper_tracker_id": "M12A-P006", "quantitative": "NO", "statistics_reported": "Source-page mechanistic or project-anchor row; exact quantitative estimates not extracted", "topic_id": "M12B-T006", "tracker_id": "M12B-O006"}'
  FROM _m12_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M12A-P006::M12A-P006-E001'
    AND et.evidence_type_name = 'Mechanistic comparator evidence'
    AND ot.outcome_type_name = 'Innate immune conditioning / protection'
  RETURNING observation_id
)
INSERT INTO _m12_observation_map (tracker_id, observation_id) SELECT 'M12B-O006', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Neuroprotection by Preconditioning in Mice is Dependent on MyD88-Mediated CXCL10 Expression in Endothelial Cells tested or summarized Endotoxin/LPS or innate agonist conditioning in Non-SCI neuroprotection comparator; first-pass note: Peripheral LPS preconditioning brain ischemia model; endothelial MyD88/CXCL10 upstream regulatory-node comparator.',
    'qualitative',
    'Neuroprotection by Preconditioning in Mice is Dependent on MyD88-Mediated CXCL10 Expression in Endothelial Cells tested or summarized Endotoxin/LPS or innate agonist conditioning in Non-SCI neuroprotection comparator; first-pass note: Peripheral LPS preconditioning brain ischemia model; endothelial MyD88/CXCL10 upstream regulatory-node comparator.',
    'endotoxin/lps or innate agonist conditioning',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Preserve innate-conditioning stimulus, timing, cell-population, and endpoint boundaries.", "experiment_tracker_id": "M12A-P007-E001", "paper_tracker_id": "M12A-P007", "quantitative": "NO", "statistics_reported": "Source-page mechanistic or project-anchor row; exact quantitative estimates not extracted", "topic_id": "M12B-T007", "tracker_id": "M12B-O007"}'
  FROM _m12_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M12A-P007::M12A-P007-E001'
    AND et.evidence_type_name = 'Mechanistic comparator evidence'
    AND ot.outcome_type_name = 'Innate immune conditioning / protection'
  RETURNING observation_id
)
INSERT INTO _m12_observation_map (tracker_id, observation_id) SELECT 'M12B-O007', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'TLR4 Deficiency Impairs Oligodendrocyte Formation in the Injured Spinal Cord tested or summarized SCI innate immune mechanism / boundary evidence in Traumatic SCI or post-SCI host response model; first-pass note: SCI TLR4 boundary; innate inflammatory signaling can support myelin debris clearance, oligodendrocyte replacement, and recovery.',
    'qualitative',
    'TLR4 Deficiency Impairs Oligodendrocyte Formation in the Injured Spinal Cord tested or summarized SCI innate immune mechanism / boundary evidence in Traumatic SCI or post-SCI host response model; first-pass note: SCI TLR4 boundary; innate inflammatory signaling can support myelin debris clearance, oligodendrocyte replacement, and recovery.',
    'sci innate immune mechanism / boundary evidence',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Preserve innate-conditioning stimulus, timing, cell-population, and endpoint boundaries.", "experiment_tracker_id": "M12A-P008-E001", "paper_tracker_id": "M12A-P008", "quantitative": "NO", "statistics_reported": "Source-page mechanistic or project-anchor row; exact quantitative estimates not extracted", "topic_id": "M12B-T008", "tracker_id": "M12B-O008"}'
  FROM _m12_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M12A-P008::M12A-P008-E001'
    AND et.evidence_type_name = 'SCI innate repair boundary evidence'
    AND ot.outcome_type_name = 'Innate immune conditioning / protection'
  RETURNING observation_id
)
INSERT INTO _m12_observation_map (tracker_id, observation_id) SELECT 'M12B-O008', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Spinal cord injury in the rat: treatment with bacterial lipopolysaccharide and indomethacin enhances cellular repair and locomotor function tested or summarized SCI innate immune mechanism / boundary evidence in Traumatic SCI or post-SCI host response model; first-pass note: Older traumatic SCI treatment row; LPS plus indomethacin after SCI improves repair/locomotion but not preconditioning.',
    'qualitative',
    'Spinal cord injury in the rat: treatment with bacterial lipopolysaccharide and indomethacin enhances cellular repair and locomotor function tested or summarized SCI innate immune mechanism / boundary evidence in Traumatic SCI or post-SCI host response model; first-pass note: Older traumatic SCI treatment row; LPS plus indomethacin after SCI improves repair/locomotion but not preconditioning.',
    'sci innate immune mechanism / boundary evidence',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Preserve innate-conditioning stimulus, timing, cell-population, and endpoint boundaries.", "experiment_tracker_id": "M12A-P009-E001", "paper_tracker_id": "M12A-P009", "quantitative": "NO", "statistics_reported": "Source-page mechanistic or project-anchor row; exact quantitative estimates not extracted", "topic_id": "M12B-T001", "tracker_id": "M12B-O009"}'
  FROM _m12_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M12A-P009::M12A-P009-E001'
    AND et.evidence_type_name = 'SCI innate-conditioning evidence'
    AND ot.outcome_type_name = 'Innate immune conditioning / protection'
  RETURNING observation_id
)
INSERT INTO _m12_observation_map (tracker_id, observation_id) SELECT 'M12B-O009', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Reawakening inflammation in the chronically injured spinal cord using lipopolysaccharide induces diverse microglial states tested or summarized SCI innate immune mechanism / boundary evidence in Traumatic SCI or post-SCI host response model; first-pass note: Chronic SCI scRNA-seq/plasticity row; LPS reawakens inflammatory/microglial states after chronic injury.',
    'qualitative',
    'Reawakening inflammation in the chronically injured spinal cord using lipopolysaccharide induces diverse microglial states tested or summarized SCI innate immune mechanism / boundary evidence in Traumatic SCI or post-SCI host response model; first-pass note: Chronic SCI scRNA-seq/plasticity row; LPS reawakens inflammatory/microglial states after chronic injury.',
    'sci innate immune mechanism / boundary evidence',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Preserve innate-conditioning stimulus, timing, cell-population, and endpoint boundaries.", "experiment_tracker_id": "M12A-P010-E001", "paper_tracker_id": "M12A-P010", "quantitative": "YES", "statistics_reported": "Chronic SCI scRNA-seq/plasticity row; LPS reawakens inflammatory/microglial states after chronic injury.", "topic_id": "M12B-T002", "tracker_id": "M12B-O010"}'
  FROM _m12_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M12A-P010::M12A-P010-E001'
    AND et.evidence_type_name = 'SCI innate-conditioning evidence'
    AND ot.outcome_type_name = 'Innate immune conditioning / protection'
  RETURNING observation_id
)
INSERT INTO _m12_observation_map (tracker_id, observation_id) SELECT 'M12B-O010', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Different TLR4 expression and microglia/macrophage activation induced by hemorrhage in the rat spinal cord after compressive injury tested or summarized SCI innate immune mechanism / boundary evidence in Traumatic SCI or post-SCI host response model; first-pass note: Traumatic SCI hemorrhage boundary; TLR4/microglia activation varies with lesion context.',
    'qualitative',
    'Different TLR4 expression and microglia/macrophage activation induced by hemorrhage in the rat spinal cord after compressive injury tested or summarized SCI innate immune mechanism / boundary evidence in Traumatic SCI or post-SCI host response model; first-pass note: Traumatic SCI hemorrhage boundary; TLR4/microglia activation varies with lesion context.',
    'sci innate immune mechanism / boundary evidence',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Preserve innate-conditioning stimulus, timing, cell-population, and endpoint boundaries.", "experiment_tracker_id": "M12A-P011-E001", "paper_tracker_id": "M12A-P011", "quantitative": "NO", "statistics_reported": "Source-page mechanistic or project-anchor row; exact quantitative estimates not extracted", "topic_id": "M12B-T003", "tracker_id": "M12B-O011"}'
  FROM _m12_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M12A-P011::M12A-P011-E001'
    AND et.evidence_type_name = 'SCI innate repair boundary evidence'
    AND ot.outcome_type_name = 'Innate immune conditioning / protection'
  RETURNING observation_id
)
INSERT INTO _m12_observation_map (tracker_id, observation_id) SELECT 'M12B-O011', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Redefining macrophage phenotypes after spinal cord injury: An open data approach tested or summarized SCI innate immune mechanism / boundary evidence in Traumatic SCI or post-SCI host response model; first-pass note: Open-data macrophage phenotype boundary; limits simple M1/M2 interpretation in SCI.',
    'qualitative',
    'Redefining macrophage phenotypes after spinal cord injury: An open data approach tested or summarized SCI innate immune mechanism / boundary evidence in Traumatic SCI or post-SCI host response model; first-pass note: Open-data macrophage phenotype boundary; limits simple M1/M2 interpretation in SCI.',
    'sci innate immune mechanism / boundary evidence',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Preserve innate-conditioning stimulus, timing, cell-population, and endpoint boundaries.", "experiment_tracker_id": "M12A-P012-E001", "paper_tracker_id": "M12A-P012", "quantitative": "NO", "statistics_reported": "Source-page mechanistic or project-anchor row; exact quantitative estimates not extracted", "topic_id": "M12B-T004", "tracker_id": "M12B-O012"}'
  FROM _m12_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M12A-P012::M12A-P012-E001'
    AND et.evidence_type_name = 'SCI innate repair boundary evidence'
    AND ot.outcome_type_name = 'Innate immune conditioning / protection'
  RETURNING observation_id
)
INSERT INTO _m12_observation_map (tracker_id, observation_id) SELECT 'M12B-O012', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Single low-dose lipopolysaccharide preconditioning: neuroprotective against axonal injury and modulates glial cells tested or summarized Endotoxin/LPS or innate agonist conditioning in Non-SCI neuroprotection comparator; first-pass note: TBI comparator; single low-dose LPS preconditioning reduces axonal injury and changes glial responses.',
    'qualitative',
    'Single low-dose lipopolysaccharide preconditioning: neuroprotective against axonal injury and modulates glial cells tested or summarized Endotoxin/LPS or innate agonist conditioning in Non-SCI neuroprotection comparator; first-pass note: TBI comparator; single low-dose LPS preconditioning reduces axonal injury and changes glial responses.',
    'endotoxin/lps or innate agonist conditioning',
    'Abstract/source page',
    'Abstract/source page',
    'high',
    '{"curator_notes": "Preserve innate-conditioning stimulus, timing, cell-population, and endpoint boundaries.", "experiment_tracker_id": "M12A-P013-E001", "paper_tracker_id": "M12A-P013", "quantitative": "YES", "statistics_reported": "TBI comparator; single low-dose LPS preconditioning reduces axonal injury and changes glial responses.", "topic_id": "M12B-T005", "tracker_id": "M12B-O013"}'
  FROM _m12_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M12A-P013::M12A-P013-E001'
    AND et.evidence_type_name = 'Mechanistic comparator evidence'
    AND ot.outcome_type_name = 'Innate immune conditioning / protection'
  RETURNING observation_id
)
INSERT INTO _m12_observation_map (tracker_id, observation_id) SELECT 'M12B-O013', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Sevoflurane preconditioning ameliorates spinal cord ischemia/reperfusion injury by modulating microglia/macrophage polarization via GSK-3b/Nrf2 tested or summarized Non-LPS conditioning comparator in Spinal cord ischemia / ischemia-reperfusion model; first-pass note: Non-LPS comparator preserving polarization endpoint and regulatory-node logic in spinal cord ischemia.',
    'qualitative',
    'Sevoflurane preconditioning ameliorates spinal cord ischemia/reperfusion injury by modulating microglia/macrophage polarization via GSK-3b/Nrf2 tested or summarized Non-LPS conditioning comparator in Spinal cord ischemia / ischemia-reperfusion model; first-pass note: Non-LPS comparator preserving polarization endpoint and regulatory-node logic in spinal cord ischemia.',
    'non-lps conditioning comparator',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Preserve innate-conditioning stimulus, timing, cell-population, and endpoint boundaries.", "experiment_tracker_id": "M12A-P014-E001", "paper_tracker_id": "M12A-P014", "quantitative": "NO", "statistics_reported": "Source-page mechanistic or project-anchor row; exact quantitative estimates not extracted", "topic_id": "M12B-T006", "tracker_id": "M12B-O014"}'
  FROM _m12_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M12A-P014::M12A-P014-E001'
    AND et.evidence_type_name = 'Mechanistic comparator evidence'
    AND ot.outcome_type_name = 'Innate immune conditioning / protection'
  RETURNING observation_id
)
INSERT INTO _m12_observation_map (tracker_id, observation_id) SELECT 'M12B-O014', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Ischemic preconditioning protects against spinal cord ischemia-reperfusion injury in rabbits by attenuating blood spinal cord barrier disruption tested or summarized Non-LPS conditioning comparator in Spinal cord ischemia / ischemia-reperfusion model; first-pass note: Non-LPS spinal ischemia comparator; barrier, ZO-1, MMP-9, TNF-alpha boundaries.',
    'qualitative',
    'Ischemic preconditioning protects against spinal cord ischemia-reperfusion injury in rabbits by attenuating blood spinal cord barrier disruption tested or summarized Non-LPS conditioning comparator in Spinal cord ischemia / ischemia-reperfusion model; first-pass note: Non-LPS spinal ischemia comparator; barrier, ZO-1, MMP-9, TNF-alpha boundaries.',
    'non-lps conditioning comparator',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Preserve innate-conditioning stimulus, timing, cell-population, and endpoint boundaries.", "experiment_tracker_id": "M12A-P015-E001", "paper_tracker_id": "M12A-P015", "quantitative": "NO", "statistics_reported": "Source-page mechanistic or project-anchor row; exact quantitative estimates not extracted", "topic_id": "M12B-T007", "tracker_id": "M12B-O015"}'
  FROM _m12_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M12A-P015::M12A-P015-E001'
    AND et.evidence_type_name = 'Mechanistic comparator evidence'
    AND ot.outcome_type_name = 'Innate immune conditioning / protection'
  RETURNING observation_id
)
INSERT INTO _m12_observation_map (tracker_id, observation_id) SELECT 'M12B-O015', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Co-application of ischemic preconditioning and postconditioning provides additive neuroprotection against spinal cord ischemia in rabbits tested or summarized Non-LPS conditioning comparator in Spinal cord ischemia / ischemia-reperfusion model; first-pass note: Non-LPS spinal ischemia conditioning comparator; timing/additivity boundary.',
    'qualitative',
    'Co-application of ischemic preconditioning and postconditioning provides additive neuroprotection against spinal cord ischemia in rabbits tested or summarized Non-LPS conditioning comparator in Spinal cord ischemia / ischemia-reperfusion model; first-pass note: Non-LPS spinal ischemia conditioning comparator; timing/additivity boundary.',
    'non-lps conditioning comparator',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Preserve innate-conditioning stimulus, timing, cell-population, and endpoint boundaries.", "experiment_tracker_id": "M12A-P016-E001", "paper_tracker_id": "M12A-P016", "quantitative": "NO", "statistics_reported": "Source-page mechanistic or project-anchor row; exact quantitative estimates not extracted", "topic_id": "M12B-T008", "tracker_id": "M12B-O016"}'
  FROM _m12_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M12A-P016::M12A-P016-E001'
    AND et.evidence_type_name = 'Mechanistic comparator evidence'
    AND ot.outcome_type_name = 'Innate immune conditioning / protection'
  RETURNING observation_id
)
INSERT INTO _m12_observation_map (tracker_id, observation_id) SELECT 'M12B-O016', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'TLR2 agonist Pam3CSK4 dose-response testing after SCI tested or summarized Endotoxin/LPS or innate agonist conditioning in Traumatic SCI or post-SCI host response model; first-pass note: ODC dataset row from prior audit; TLR agonist/dose-response comparator for innate immune conditioning.',
    'qualitative',
    'TLR2 agonist Pam3CSK4 dose-response testing after SCI tested or summarized Endotoxin/LPS or innate agonist conditioning in Traumatic SCI or post-SCI host response model; first-pass note: ODC dataset row from prior audit; TLR agonist/dose-response comparator for innate immune conditioning.',
    'endotoxin/lps or innate agonist conditioning',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Preserve innate-conditioning stimulus, timing, cell-population, and endpoint boundaries.", "experiment_tracker_id": "M12A-P017-E001", "paper_tracker_id": "M12A-P017", "quantitative": "YES", "statistics_reported": "ODC dataset row from prior audit; TLR agonist/dose-response comparator for innate immune conditioning.", "topic_id": "M12B-T001", "tracker_id": "M12B-O017"}'
  FROM _m12_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M12A-P017::M12A-P017-E001'
    AND et.evidence_type_name = 'SCI innate-conditioning evidence'
    AND ot.outcome_type_name = 'Innate immune conditioning / protection'
  RETURNING observation_id
)
INSERT INTO _m12_observation_map (tracker_id, observation_id) SELECT 'M12B-O017', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'TLR2 and TLR4 agonist testing in SCI tested or summarized Endotoxin/LPS or innate agonist conditioning in Traumatic SCI or post-SCI host response model; first-pass note: ODC dataset row from prior audit; innate agonist boundary requiring source extraction.',
    'qualitative',
    'TLR2 and TLR4 agonist testing in SCI tested or summarized Endotoxin/LPS or innate agonist conditioning in Traumatic SCI or post-SCI host response model; first-pass note: ODC dataset row from prior audit; innate agonist boundary requiring source extraction.',
    'endotoxin/lps or innate agonist conditioning',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Preserve innate-conditioning stimulus, timing, cell-population, and endpoint boundaries.", "experiment_tracker_id": "M12A-P018-E001", "paper_tracker_id": "M12A-P018", "quantitative": "YES", "statistics_reported": "ODC dataset row from prior audit; innate agonist boundary requiring source extraction.", "topic_id": "M12B-T002", "tracker_id": "M12B-O018"}'
  FROM _m12_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M12A-P018::M12A-P018-E001'
    AND et.evidence_type_name = 'SCI innate-conditioning evidence'
    AND ot.outcome_type_name = 'Innate immune conditioning / protection'
  RETURNING observation_id
)
INSERT INTO _m12_observation_map (tracker_id, observation_id) SELECT 'M12B-O018', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Systemic LPS drives microglia-mediated perineuronal net degradation after cervical SCI tested or summarized Endotoxin/LPS or innate agonist conditioning in Traumatic SCI or post-SCI host response model; first-pass note: ODC dataset row from prior audit; systemic LPS after cervical SCI and PNN/plasticity endpoint.',
    'qualitative',
    'Systemic LPS drives microglia-mediated perineuronal net degradation after cervical SCI tested or summarized Endotoxin/LPS or innate agonist conditioning in Traumatic SCI or post-SCI host response model; first-pass note: ODC dataset row from prior audit; systemic LPS after cervical SCI and PNN/plasticity endpoint.',
    'endotoxin/lps or innate agonist conditioning',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Preserve innate-conditioning stimulus, timing, cell-population, and endpoint boundaries.", "experiment_tracker_id": "M12A-P019-E001", "paper_tracker_id": "M12A-P019", "quantitative": "YES", "statistics_reported": "ODC dataset row from prior audit; systemic LPS after cervical SCI and PNN/plasticity endpoint.", "topic_id": "M12B-T003", "tracker_id": "M12B-O019"}'
  FROM _m12_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M12A-P019::M12A-P019-E001'
    AND et.evidence_type_name = 'SCI innate-conditioning evidence'
    AND ot.outcome_type_name = 'Innate immune conditioning / protection'
  RETURNING observation_id
)
INSERT INTO _m12_observation_map (tracker_id, observation_id) SELECT 'M12B-O019', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Cultured macrophage with spinal cord homogenate and PI3K inhibition tested or summarized SCI innate immune mechanism / boundary evidence in Cell culture or validation dataset; first-pass note: In vitro bridge for macrophage activation/regulatory-node validation after SCI homogenate exposure.',
    'qualitative',
    'Cultured macrophage with spinal cord homogenate and PI3K inhibition tested or summarized SCI innate immune mechanism / boundary evidence in Cell culture or validation dataset; first-pass note: In vitro bridge for macrophage activation/regulatory-node validation after SCI homogenate exposure.',
    'sci innate immune mechanism / boundary evidence',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Preserve innate-conditioning stimulus, timing, cell-population, and endpoint boundaries.", "experiment_tracker_id": "M12A-P020-E001", "paper_tracker_id": "M12A-P020", "quantitative": "NO", "statistics_reported": "Source-page mechanistic or project-anchor row; exact quantitative estimates not extracted", "topic_id": "M12B-T004", "tracker_id": "M12B-O020"}'
  FROM _m12_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M12A-P020::M12A-P020-E001'
    AND et.evidence_type_name = 'Dataset/in vitro candidate evidence'
    AND ot.outcome_type_name = 'Innate immune conditioning / protection'
  RETURNING observation_id
)
INSERT INTO _m12_observation_map (tracker_id, observation_id) SELECT 'M12B-O020', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Pleiotrophin in vitro and dose-response in vivo SCI dataset tested or summarized SCI innate immune mechanism / boundary evidence in Cell culture or validation dataset; first-pass note: In vitro/in vivo validation structure comparator for conditioning-derived candidate testing.',
    'qualitative',
    'Pleiotrophin in vitro and dose-response in vivo SCI dataset tested or summarized SCI innate immune mechanism / boundary evidence in Cell culture or validation dataset; first-pass note: In vitro/in vivo validation structure comparator for conditioning-derived candidate testing.',
    'sci innate immune mechanism / boundary evidence',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Preserve innate-conditioning stimulus, timing, cell-population, and endpoint boundaries.", "experiment_tracker_id": "M12A-P021-E001", "paper_tracker_id": "M12A-P021", "quantitative": "NO", "statistics_reported": "Source-page mechanistic or project-anchor row; exact quantitative estimates not extracted", "topic_id": "M12B-T005", "tracker_id": "M12B-O021"}'
  FROM _m12_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M12A-P021::M12A-P021-E001'
    AND et.evidence_type_name = 'Dataset/in vitro candidate evidence'
    AND ot.outcome_type_name = 'Innate immune conditioning / protection'
  RETURNING observation_id
)
INSERT INTO _m12_observation_map (tracker_id, observation_id) SELECT 'M12B-O021', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Probiotic treatment after C5 contusion tested or summarized Non-LPS conditioning comparator in Traumatic SCI or post-SCI host response model; first-pass note: Microbiome/systemic inflammation safer host-conditioning comparator.',
    'qualitative',
    'Probiotic treatment after C5 contusion tested or summarized Non-LPS conditioning comparator in Traumatic SCI or post-SCI host response model; first-pass note: Microbiome/systemic inflammation safer host-conditioning comparator.',
    'non-lps conditioning comparator',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Preserve innate-conditioning stimulus, timing, cell-population, and endpoint boundaries.", "experiment_tracker_id": "M12A-P022-E001", "paper_tracker_id": "M12A-P022", "quantitative": "NO", "statistics_reported": "Source-page mechanistic or project-anchor row; exact quantitative estimates not extracted", "topic_id": "M12B-T006", "tracker_id": "M12B-O022"}'
  FROM _m12_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M12A-P022::M12A-P022-E001'
    AND et.evidence_type_name = 'Dataset/in vitro candidate evidence'
    AND ot.outcome_type_name = 'Innate immune conditioning / protection'
  RETURNING observation_id
)
INSERT INTO _m12_observation_map (tracker_id, observation_id) SELECT 'M12B-O022', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Fecal transplant after unilateral cervical contusion tested or summarized Non-LPS conditioning comparator in Traumatic SCI or post-SCI host response model; first-pass note: Microbiota-transfer host-conditioning comparator; separates LPS mechanism from translational alternatives.',
    'qualitative',
    'Fecal transplant after unilateral cervical contusion tested or summarized Non-LPS conditioning comparator in Traumatic SCI or post-SCI host response model; first-pass note: Microbiota-transfer host-conditioning comparator; separates LPS mechanism from translational alternatives.',
    'non-lps conditioning comparator',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Preserve innate-conditioning stimulus, timing, cell-population, and endpoint boundaries.", "experiment_tracker_id": "M12A-P023-E001", "paper_tracker_id": "M12A-P023", "quantitative": "NO", "statistics_reported": "Source-page mechanistic or project-anchor row; exact quantitative estimates not extracted", "topic_id": "M12B-T007", "tracker_id": "M12B-O023"}'
  FROM _m12_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M12A-P023::M12A-P023-E001'
    AND et.evidence_type_name = 'Dataset/in vitro candidate evidence'
    AND ot.outcome_type_name = 'Innate immune conditioning / protection'
  RETURNING observation_id
)
INSERT INTO _m12_observation_map (tracker_id, observation_id) SELECT 'M12B-O023', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Revised Specific Aims Preconditioning Logic tested or summarized Endotoxin/LPS or innate agonist conditioning in Review, project, or mechanism anchor; first-pass note: Project logic anchor: innate immune conditioning is broader than LPS; endotoxin/LPS is one discovery platform, not a clinical therapeutic.',
    'qualitative',
    'Revised Specific Aims Preconditioning Logic tested or summarized Endotoxin/LPS or innate agonist conditioning in Review, project, or mechanism anchor; first-pass note: Project logic anchor: innate immune conditioning is broader than LPS; endotoxin/LPS is one discovery platform, not a clinical therapeutic.',
    'endotoxin/lps or innate agonist conditioning',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Preserve innate-conditioning stimulus, timing, cell-population, and endpoint boundaries.", "experiment_tracker_id": "M12A-P024-E001", "paper_tracker_id": "M12A-P024", "quantitative": "YES", "statistics_reported": "Project logic anchor: innate immune conditioning is broader than LPS; endotoxin/LPS is one discovery platform, not a clinical therapeutic.", "topic_id": "M12B-T008", "tracker_id": "M12B-O024"}'
  FROM _m12_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M12A-P024::M12A-P024-E001'
    AND et.evidence_type_name = 'Project logic evidence'
    AND ot.outcome_type_name = 'Innate immune conditioning / protection'
  RETURNING observation_id
)
INSERT INTO _m12_observation_map (tracker_id, observation_id) SELECT 'M12B-O024', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'LPS or repeated endotoxin exposure can induce protective spinal cord immune programs when dose, timing, and cell compartment are controlled.',
    'synthesis',
    'medium',
    'Module 12A tracker / source-page, full-text PMC, database, or project metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text and dataset extraction queued where available.", "source_paper_tracker_id": "M12A-P001", "topic_id": "M12B-T001", "tracker_id": "M12B-C001"}'
  FROM _m12_paper_map p
  WHERE p.tracker_id = 'M12A-P001'
  RETURNING claim_id
)
INSERT INTO _m12_claim_map (tracker_id, claim_id) SELECT 'M12B-C001', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'LPS or repeated endotoxin exposure can induce protective spinal cord immune programs when dose, timing, and cell compartment are controlled.',
    'synthesis',
    'high',
    'Module 12A tracker / source-page, full-text PMC, database, or project metadata',
    'high',
    '{"curator_notes": "First-pass claim abstraction; full text and dataset extraction queued where available.", "source_paper_tracker_id": "M12A-P002", "topic_id": "M12B-T002", "tracker_id": "M12B-C002"}'
  FROM _m12_paper_map p
  WHERE p.tracker_id = 'M12A-P002'
  RETURNING claim_id
)
INSERT INTO _m12_claim_map (tracker_id, claim_id) SELECT 'M12B-C002', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'LPS or repeated endotoxin exposure can induce protective spinal cord immune programs when dose, timing, and cell compartment are controlled.',
    'synthesis',
    'high',
    'Module 12A tracker / source-page, full-text PMC, database, or project metadata',
    'high',
    '{"curator_notes": "First-pass claim abstraction; full text and dataset extraction queued where available.", "source_paper_tracker_id": "M12A-P003", "topic_id": "M12B-T003", "tracker_id": "M12B-C003"}'
  FROM _m12_paper_map p
  WHERE p.tracker_id = 'M12A-P003'
  RETURNING claim_id
)
INSERT INTO _m12_claim_map (tracker_id, claim_id) SELECT 'M12B-C003', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Innate immune preconditioning depends on pathway routing rather than generic inflammation, with TLR adaptor and cytokine context determining outcome.',
    'synthesis',
    'medium',
    'Module 12A tracker / source-page, full-text PMC, database, or project metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text and dataset extraction queued where available.", "source_paper_tracker_id": "M12A-P004", "topic_id": "M12B-T004", "tracker_id": "M12B-C004"}'
  FROM _m12_paper_map p
  WHERE p.tracker_id = 'M12A-P004'
  RETURNING claim_id
)
INSERT INTO _m12_claim_map (tracker_id, claim_id) SELECT 'M12B-C004', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Innate immune preconditioning depends on pathway routing rather than generic inflammation, with TLR adaptor and cytokine context determining outcome.',
    'synthesis',
    'high',
    'Module 12A tracker / source-page, full-text PMC, database, or project metadata',
    'high',
    '{"curator_notes": "First-pass claim abstraction; full text and dataset extraction queued where available.", "source_paper_tracker_id": "M12A-P005", "topic_id": "M12B-T005", "tracker_id": "M12B-C005"}'
  FROM _m12_paper_map p
  WHERE p.tracker_id = 'M12A-P005'
  RETURNING claim_id
)
INSERT INTO _m12_claim_map (tracker_id, claim_id) SELECT 'M12B-C005', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Peripheral monocytes can carry preconditioned neuroprotective programs, supporting systemic-to-CNS host-conditioning logic.',
    'synthesis',
    'medium',
    'Module 12A tracker / source-page, full-text PMC, database, or project metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text and dataset extraction queued where available.", "source_paper_tracker_id": "M12A-P006", "topic_id": "M12B-T006", "tracker_id": "M12B-C006"}'
  FROM _m12_paper_map p
  WHERE p.tracker_id = 'M12A-P006'
  RETURNING claim_id
)
INSERT INTO _m12_claim_map (tracker_id, claim_id) SELECT 'M12B-C006', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Innate immune preconditioning depends on pathway routing rather than generic inflammation, with TLR adaptor and cytokine context determining outcome.',
    'synthesis',
    'medium',
    'Module 12A tracker / source-page, full-text PMC, database, or project metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text and dataset extraction queued where available.", "source_paper_tracker_id": "M12A-P007", "topic_id": "M12B-T007", "tracker_id": "M12B-C007"}'
  FROM _m12_paper_map p
  WHERE p.tracker_id = 'M12A-P007'
  RETURNING claim_id
)
INSERT INTO _m12_claim_map (tracker_id, claim_id) SELECT 'M12B-C007', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'TLR4 signaling after SCI can support repair-relevant processes, so complete suppression of innate inflammation may remove beneficial responses.',
    'synthesis',
    'medium',
    'Module 12A tracker / source-page, full-text PMC, database, or project metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text and dataset extraction queued where available.", "source_paper_tracker_id": "M12A-P008", "topic_id": "M12B-T008", "tracker_id": "M12B-C008"}'
  FROM _m12_paper_map p
  WHERE p.tracker_id = 'M12A-P008'
  RETURNING claim_id
)
INSERT INTO _m12_claim_map (tracker_id, claim_id) SELECT 'M12B-C008', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Comparator conditioning evidence supports mechanism generation but cannot substitute for direct traumatic SCI innate-conditioning evidence.',
    'boundary condition',
    'medium',
    'Module 12A tracker / source-page, full-text PMC, database, or project metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text and dataset extraction queued where available.", "source_paper_tracker_id": "M12A-P009", "topic_id": "M12B-T001", "tracker_id": "M12B-C009"}'
  FROM _m12_paper_map p
  WHERE p.tracker_id = 'M12A-P009'
  RETURNING claim_id
)
INSERT INTO _m12_claim_map (tracker_id, claim_id) SELECT 'M12B-C009', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Post-injury or chronic innate-stimulation rows indicate inducible spinal plasticity and microglial-state shifts, but should not be merged with pre-injury or peri-procedural conditioning rows.',
    'boundary condition',
    'medium',
    'Module 12A tracker / source-page, full-text PMC, database, or project metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text and dataset extraction queued where available.", "source_paper_tracker_id": "M12A-P010", "topic_id": "M12B-T002", "tracker_id": "M12B-C010"}'
  FROM _m12_paper_map p
  WHERE p.tracker_id = 'M12A-P010'
  RETURNING claim_id
)
INSERT INTO _m12_claim_map (tracker_id, claim_id) SELECT 'M12B-C010', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Comparator conditioning evidence supports mechanism generation but cannot substitute for direct traumatic SCI innate-conditioning evidence.',
    'boundary condition',
    'medium',
    'Module 12A tracker / source-page, full-text PMC, database, or project metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text and dataset extraction queued where available.", "source_paper_tracker_id": "M12A-P011", "topic_id": "M12B-T003", "tracker_id": "M12B-C011"}'
  FROM _m12_paper_map p
  WHERE p.tracker_id = 'M12A-P011'
  RETURNING claim_id
)
INSERT INTO _m12_claim_map (tracker_id, claim_id) SELECT 'M12B-C011', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'SCI macrophage phenotypes require state-resolved interpretation beyond simple M1/M2 labels.',
    'boundary condition',
    'medium',
    'Module 12A tracker / source-page, full-text PMC, database, or project metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text and dataset extraction queued where available.", "source_paper_tracker_id": "M12A-P012", "topic_id": "M12B-T004", "tracker_id": "M12B-C012"}'
  FROM _m12_paper_map p
  WHERE p.tracker_id = 'M12A-P012'
  RETURNING claim_id
)
INSERT INTO _m12_claim_map (tracker_id, claim_id) SELECT 'M12B-C012', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Comparator conditioning evidence supports mechanism generation but cannot substitute for direct traumatic SCI innate-conditioning evidence.',
    'boundary condition',
    'high',
    'Module 12A tracker / source-page, full-text PMC, database, or project metadata',
    'high',
    '{"curator_notes": "First-pass claim abstraction; full text and dataset extraction queued where available.", "source_paper_tracker_id": "M12A-P013", "topic_id": "M12B-T005", "tracker_id": "M12B-C013"}'
  FROM _m12_paper_map p
  WHERE p.tracker_id = 'M12A-P013'
  RETURNING claim_id
)
INSERT INTO _m12_claim_map (tracker_id, claim_id) SELECT 'M12B-C013', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Comparator conditioning evidence supports mechanism generation but cannot substitute for direct traumatic SCI innate-conditioning evidence.',
    'boundary condition',
    'medium',
    'Module 12A tracker / source-page, full-text PMC, database, or project metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text and dataset extraction queued where available.", "source_paper_tracker_id": "M12A-P014", "topic_id": "M12B-T006", "tracker_id": "M12B-C014"}'
  FROM _m12_paper_map p
  WHERE p.tracker_id = 'M12A-P014'
  RETURNING claim_id
)
INSERT INTO _m12_claim_map (tracker_id, claim_id) SELECT 'M12B-C014', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Comparator conditioning evidence supports mechanism generation but cannot substitute for direct traumatic SCI innate-conditioning evidence.',
    'boundary condition',
    'medium',
    'Module 12A tracker / source-page, full-text PMC, database, or project metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text and dataset extraction queued where available.", "source_paper_tracker_id": "M12A-P015", "topic_id": "M12B-T007", "tracker_id": "M12B-C015"}'
  FROM _m12_paper_map p
  WHERE p.tracker_id = 'M12A-P015'
  RETURNING claim_id
)
INSERT INTO _m12_claim_map (tracker_id, claim_id) SELECT 'M12B-C015', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Comparator conditioning evidence supports mechanism generation but cannot substitute for direct traumatic SCI innate-conditioning evidence.',
    'boundary condition',
    'medium',
    'Module 12A tracker / source-page, full-text PMC, database, or project metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text and dataset extraction queued where available.", "source_paper_tracker_id": "M12A-P016", "topic_id": "M12B-T008", "tracker_id": "M12B-C016"}'
  FROM _m12_paper_map p
  WHERE p.tracker_id = 'M12A-P016'
  RETURNING claim_id
)
INSERT INTO _m12_claim_map (tracker_id, claim_id) SELECT 'M12B-C016', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Comparator conditioning evidence supports mechanism generation but cannot substitute for direct traumatic SCI innate-conditioning evidence.',
    'boundary condition',
    'medium',
    'Module 12A tracker / source-page, full-text PMC, database, or project metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text and dataset extraction queued where available.", "source_paper_tracker_id": "M12A-P017", "topic_id": "M12B-T001", "tracker_id": "M12B-C017"}'
  FROM _m12_paper_map p
  WHERE p.tracker_id = 'M12A-P017'
  RETURNING claim_id
)
INSERT INTO _m12_claim_map (tracker_id, claim_id) SELECT 'M12B-C017', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Comparator conditioning evidence supports mechanism generation but cannot substitute for direct traumatic SCI innate-conditioning evidence.',
    'boundary condition',
    'medium',
    'Module 12A tracker / source-page, full-text PMC, database, or project metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text and dataset extraction queued where available.", "source_paper_tracker_id": "M12A-P018", "topic_id": "M12B-T002", "tracker_id": "M12B-C018"}'
  FROM _m12_paper_map p
  WHERE p.tracker_id = 'M12A-P018'
  RETURNING claim_id
)
INSERT INTO _m12_claim_map (tracker_id, claim_id) SELECT 'M12B-C018', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Post-injury or chronic innate-stimulation rows indicate inducible spinal plasticity and microglial-state shifts, but should not be merged with pre-injury or peri-procedural conditioning rows.',
    'boundary condition',
    'medium',
    'Module 12A tracker / source-page, full-text PMC, database, or project metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text and dataset extraction queued where available.", "source_paper_tracker_id": "M12A-P019", "topic_id": "M12B-T003", "tracker_id": "M12B-C019"}'
  FROM _m12_paper_map p
  WHERE p.tracker_id = 'M12A-P019'
  RETURNING claim_id
)
INSERT INTO _m12_claim_map (tracker_id, claim_id) SELECT 'M12B-C019', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'ODC-SCI and in vitro/microbiome rows provide validation candidates, but remain dataset-level until source extraction is completed.',
    'boundary condition',
    'medium',
    'Module 12A tracker / source-page, full-text PMC, database, or project metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text and dataset extraction queued where available.", "source_paper_tracker_id": "M12A-P020", "topic_id": "M12B-T004", "tracker_id": "M12B-C020"}'
  FROM _m12_paper_map p
  WHERE p.tracker_id = 'M12A-P020'
  RETURNING claim_id
)
INSERT INTO _m12_claim_map (tracker_id, claim_id) SELECT 'M12B-C020', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'ODC-SCI and in vitro/microbiome rows provide validation candidates, but remain dataset-level until source extraction is completed.',
    'boundary condition',
    'medium',
    'Module 12A tracker / source-page, full-text PMC, database, or project metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text and dataset extraction queued where available.", "source_paper_tracker_id": "M12A-P021", "topic_id": "M12B-T005", "tracker_id": "M12B-C021"}'
  FROM _m12_paper_map p
  WHERE p.tracker_id = 'M12A-P021'
  RETURNING claim_id
)
INSERT INTO _m12_claim_map (tracker_id, claim_id) SELECT 'M12B-C021', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'ODC-SCI and in vitro/microbiome rows provide validation candidates, but remain dataset-level until source extraction is completed.',
    'boundary condition',
    'medium',
    'Module 12A tracker / source-page, full-text PMC, database, or project metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text and dataset extraction queued where available.", "source_paper_tracker_id": "M12A-P022", "topic_id": "M12B-T006", "tracker_id": "M12B-C022"}'
  FROM _m12_paper_map p
  WHERE p.tracker_id = 'M12A-P022'
  RETURNING claim_id
)
INSERT INTO _m12_claim_map (tracker_id, claim_id) SELECT 'M12B-C022', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'ODC-SCI and in vitro/microbiome rows provide validation candidates, but remain dataset-level until source extraction is completed.',
    'boundary condition',
    'medium',
    'Module 12A tracker / source-page, full-text PMC, database, or project metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text and dataset extraction queued where available.", "source_paper_tracker_id": "M12A-P023", "topic_id": "M12B-T007", "tracker_id": "M12B-C023"}'
  FROM _m12_paper_map p
  WHERE p.tracker_id = 'M12A-P023'
  RETURNING claim_id
)
INSERT INTO _m12_claim_map (tracker_id, claim_id) SELECT 'M12B-C023', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Project logic frames innate immune conditioning broadly, with LPS as one discovery platform for endogenous protective programs rather than a direct clinical therapeutic.',
    'boundary condition',
    'medium',
    'Module 12A tracker / source-page, full-text PMC, database, or project metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text and dataset extraction queued where available.", "source_paper_tracker_id": "M12A-P024", "topic_id": "M12B-T008", "tracker_id": "M12B-C024"}'
  FROM _m12_paper_map p
  WHERE p.tracker_id = 'M12A-P024'
  RETURNING claim_id
)
INSERT INTO _m12_claim_map (tracker_id, claim_id) SELECT 'M12B-C024', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary source-level linkage preserving source-specific timing and endpoint boundaries.", "strength": "medium", "tracker_id": "M12B-L001"}'
  FROM _m12_claim_map c
  JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O001'
  WHERE c.tracker_id = 'M12B-C001'
  RETURNING link_id
)
INSERT INTO _m12_link_map (tracker_id, link_id) SELECT 'M12B-L001', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary source-level linkage preserving source-specific timing and endpoint boundaries.", "strength": "medium", "tracker_id": "M12B-L002"}'
  FROM _m12_claim_map c
  JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O002'
  WHERE c.tracker_id = 'M12B-C002'
  RETURNING link_id
)
INSERT INTO _m12_link_map (tracker_id, link_id) SELECT 'M12B-L002', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary source-level linkage preserving source-specific timing and endpoint boundaries.", "strength": "medium", "tracker_id": "M12B-L003"}'
  FROM _m12_claim_map c
  JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O003'
  WHERE c.tracker_id = 'M12B-C003'
  RETURNING link_id
)
INSERT INTO _m12_link_map (tracker_id, link_id) SELECT 'M12B-L003', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary source-level linkage preserving source-specific timing and endpoint boundaries.", "strength": "medium", "tracker_id": "M12B-L004"}'
  FROM _m12_claim_map c
  JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O004'
  WHERE c.tracker_id = 'M12B-C004'
  RETURNING link_id
)
INSERT INTO _m12_link_map (tracker_id, link_id) SELECT 'M12B-L004', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary source-level linkage preserving source-specific timing and endpoint boundaries.", "strength": "medium", "tracker_id": "M12B-L005"}'
  FROM _m12_claim_map c
  JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O005'
  WHERE c.tracker_id = 'M12B-C005'
  RETURNING link_id
)
INSERT INTO _m12_link_map (tracker_id, link_id) SELECT 'M12B-L005', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary source-level linkage preserving source-specific timing and endpoint boundaries.", "strength": "medium", "tracker_id": "M12B-L006"}'
  FROM _m12_claim_map c
  JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O006'
  WHERE c.tracker_id = 'M12B-C006'
  RETURNING link_id
)
INSERT INTO _m12_link_map (tracker_id, link_id) SELECT 'M12B-L006', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary source-level linkage preserving source-specific timing and endpoint boundaries.", "strength": "medium", "tracker_id": "M12B-L007"}'
  FROM _m12_claim_map c
  JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O007'
  WHERE c.tracker_id = 'M12B-C007'
  RETURNING link_id
)
INSERT INTO _m12_link_map (tracker_id, link_id) SELECT 'M12B-L007', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary source-level linkage preserving source-specific timing and endpoint boundaries.", "strength": "medium", "tracker_id": "M12B-L008"}'
  FROM _m12_claim_map c
  JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O008'
  WHERE c.tracker_id = 'M12B-C008'
  RETURNING link_id
)
INSERT INTO _m12_link_map (tracker_id, link_id) SELECT 'M12B-L008', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary source-level linkage preserving source-specific timing and endpoint boundaries.", "strength": "medium", "tracker_id": "M12B-L009"}'
  FROM _m12_claim_map c
  JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O009'
  WHERE c.tracker_id = 'M12B-C009'
  RETURNING link_id
)
INSERT INTO _m12_link_map (tracker_id, link_id) SELECT 'M12B-L009', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary source-level linkage preserving source-specific timing and endpoint boundaries.", "strength": "medium", "tracker_id": "M12B-L010"}'
  FROM _m12_claim_map c
  JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O010'
  WHERE c.tracker_id = 'M12B-C010'
  RETURNING link_id
)
INSERT INTO _m12_link_map (tracker_id, link_id) SELECT 'M12B-L010', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary source-level linkage preserving source-specific timing and endpoint boundaries.", "strength": "medium", "tracker_id": "M12B-L011"}'
  FROM _m12_claim_map c
  JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O011'
  WHERE c.tracker_id = 'M12B-C011'
  RETURNING link_id
)
INSERT INTO _m12_link_map (tracker_id, link_id) SELECT 'M12B-L011', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary source-level linkage preserving source-specific timing and endpoint boundaries.", "strength": "medium", "tracker_id": "M12B-L012"}'
  FROM _m12_claim_map c
  JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O012'
  WHERE c.tracker_id = 'M12B-C012'
  RETURNING link_id
)
INSERT INTO _m12_link_map (tracker_id, link_id) SELECT 'M12B-L012', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary source-level linkage preserving source-specific timing and endpoint boundaries.", "strength": "medium", "tracker_id": "M12B-L013"}'
  FROM _m12_claim_map c
  JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O013'
  WHERE c.tracker_id = 'M12B-C013'
  RETURNING link_id
)
INSERT INTO _m12_link_map (tracker_id, link_id) SELECT 'M12B-L013', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary source-level linkage preserving source-specific timing and endpoint boundaries.", "strength": "medium", "tracker_id": "M12B-L014"}'
  FROM _m12_claim_map c
  JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O014'
  WHERE c.tracker_id = 'M12B-C014'
  RETURNING link_id
)
INSERT INTO _m12_link_map (tracker_id, link_id) SELECT 'M12B-L014', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary source-level linkage preserving source-specific timing and endpoint boundaries.", "strength": "medium", "tracker_id": "M12B-L015"}'
  FROM _m12_claim_map c
  JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O015'
  WHERE c.tracker_id = 'M12B-C015'
  RETURNING link_id
)
INSERT INTO _m12_link_map (tracker_id, link_id) SELECT 'M12B-L015', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary source-level linkage preserving source-specific timing and endpoint boundaries.", "strength": "medium", "tracker_id": "M12B-L016"}'
  FROM _m12_claim_map c
  JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O016'
  WHERE c.tracker_id = 'M12B-C016'
  RETURNING link_id
)
INSERT INTO _m12_link_map (tracker_id, link_id) SELECT 'M12B-L016', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary source-level linkage preserving source-specific timing and endpoint boundaries.", "strength": "medium", "tracker_id": "M12B-L017"}'
  FROM _m12_claim_map c
  JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O017'
  WHERE c.tracker_id = 'M12B-C017'
  RETURNING link_id
)
INSERT INTO _m12_link_map (tracker_id, link_id) SELECT 'M12B-L017', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary source-level linkage preserving source-specific timing and endpoint boundaries.", "strength": "medium", "tracker_id": "M12B-L018"}'
  FROM _m12_claim_map c
  JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O018'
  WHERE c.tracker_id = 'M12B-C018'
  RETURNING link_id
)
INSERT INTO _m12_link_map (tracker_id, link_id) SELECT 'M12B-L018', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary source-level linkage preserving source-specific timing and endpoint boundaries.", "strength": "medium", "tracker_id": "M12B-L019"}'
  FROM _m12_claim_map c
  JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O019'
  WHERE c.tracker_id = 'M12B-C019'
  RETURNING link_id
)
INSERT INTO _m12_link_map (tracker_id, link_id) SELECT 'M12B-L019', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary source-level linkage preserving source-specific timing and endpoint boundaries.", "strength": "medium", "tracker_id": "M12B-L020"}'
  FROM _m12_claim_map c
  JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O020'
  WHERE c.tracker_id = 'M12B-C020'
  RETURNING link_id
)
INSERT INTO _m12_link_map (tracker_id, link_id) SELECT 'M12B-L020', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary source-level linkage preserving source-specific timing and endpoint boundaries.", "strength": "medium", "tracker_id": "M12B-L021"}'
  FROM _m12_claim_map c
  JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O021'
  WHERE c.tracker_id = 'M12B-C021'
  RETURNING link_id
)
INSERT INTO _m12_link_map (tracker_id, link_id) SELECT 'M12B-L021', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary source-level linkage preserving source-specific timing and endpoint boundaries.", "strength": "medium", "tracker_id": "M12B-L022"}'
  FROM _m12_claim_map c
  JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O022'
  WHERE c.tracker_id = 'M12B-C022'
  RETURNING link_id
)
INSERT INTO _m12_link_map (tracker_id, link_id) SELECT 'M12B-L022', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary source-level linkage preserving source-specific timing and endpoint boundaries.", "strength": "medium", "tracker_id": "M12B-L023"}'
  FROM _m12_claim_map c
  JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O023'
  WHERE c.tracker_id = 'M12B-C023'
  RETURNING link_id
)
INSERT INTO _m12_link_map (tracker_id, link_id) SELECT 'M12B-L023', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary source-level linkage preserving source-specific timing and endpoint boundaries.", "strength": "medium", "tracker_id": "M12B-L024"}'
  FROM _m12_claim_map c
  JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O024'
  WHERE c.tracker_id = 'M12B-C024'
  RETURNING link_id
)
INSERT INTO _m12_link_map (tracker_id, link_id) SELECT 'M12B-L024', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cross-topic contextual linkage; not used as primary causal support.", "strength": "low", "tracker_id": "M12B-L025"}'
  FROM _m12_claim_map c
  JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O009'
  WHERE c.tracker_id = 'M12B-C001'
  RETURNING link_id
)
INSERT INTO _m12_link_map (tracker_id, link_id) SELECT 'M12B-L025', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cross-topic contextual linkage; not used as primary causal support.", "strength": "low", "tracker_id": "M12B-L026"}'
  FROM _m12_claim_map c
  JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O010'
  WHERE c.tracker_id = 'M12B-C002'
  RETURNING link_id
)
INSERT INTO _m12_link_map (tracker_id, link_id) SELECT 'M12B-L026', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cross-topic contextual linkage; not used as primary causal support.", "strength": "low", "tracker_id": "M12B-L027"}'
  FROM _m12_claim_map c
  JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O011'
  WHERE c.tracker_id = 'M12B-C003'
  RETURNING link_id
)
INSERT INTO _m12_link_map (tracker_id, link_id) SELECT 'M12B-L027', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cross-topic contextual linkage; not used as primary causal support.", "strength": "low", "tracker_id": "M12B-L028"}'
  FROM _m12_claim_map c
  JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O012'
  WHERE c.tracker_id = 'M12B-C004'
  RETURNING link_id
)
INSERT INTO _m12_link_map (tracker_id, link_id) SELECT 'M12B-L028', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cross-topic contextual linkage; not used as primary causal support.", "strength": "low", "tracker_id": "M12B-L029"}'
  FROM _m12_claim_map c
  JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O013'
  WHERE c.tracker_id = 'M12B-C005'
  RETURNING link_id
)
INSERT INTO _m12_link_map (tracker_id, link_id) SELECT 'M12B-L029', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cross-topic contextual linkage; not used as primary causal support.", "strength": "low", "tracker_id": "M12B-L030"}'
  FROM _m12_claim_map c
  JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O014'
  WHERE c.tracker_id = 'M12B-C006'
  RETURNING link_id
)
INSERT INTO _m12_link_map (tracker_id, link_id) SELECT 'M12B-L030', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cross-topic contextual linkage; not used as primary causal support.", "strength": "low", "tracker_id": "M12B-L031"}'
  FROM _m12_claim_map c
  JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O015'
  WHERE c.tracker_id = 'M12B-C007'
  RETURNING link_id
)
INSERT INTO _m12_link_map (tracker_id, link_id) SELECT 'M12B-L031', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cross-topic contextual linkage; not used as primary causal support.", "strength": "low", "tracker_id": "M12B-L032"}'
  FROM _m12_claim_map c
  JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O016'
  WHERE c.tracker_id = 'M12B-C008'
  RETURNING link_id
)
INSERT INTO _m12_link_map (tracker_id, link_id) SELECT 'M12B-L032', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cross-topic contextual linkage; not used as primary causal support.", "strength": "low", "tracker_id": "M12B-L033"}'
  FROM _m12_claim_map c
  JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O017'
  WHERE c.tracker_id = 'M12B-C009'
  RETURNING link_id
)
INSERT INTO _m12_link_map (tracker_id, link_id) SELECT 'M12B-L033', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cross-topic contextual linkage; not used as primary causal support.", "strength": "low", "tracker_id": "M12B-L034"}'
  FROM _m12_claim_map c
  JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O018'
  WHERE c.tracker_id = 'M12B-C010'
  RETURNING link_id
)
INSERT INTO _m12_link_map (tracker_id, link_id) SELECT 'M12B-L034', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cross-topic contextual linkage; not used as primary causal support.", "strength": "low", "tracker_id": "M12B-L035"}'
  FROM _m12_claim_map c
  JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O019'
  WHERE c.tracker_id = 'M12B-C011'
  RETURNING link_id
)
INSERT INTO _m12_link_map (tracker_id, link_id) SELECT 'M12B-L035', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cross-topic contextual linkage; not used as primary causal support.", "strength": "low", "tracker_id": "M12B-L036"}'
  FROM _m12_claim_map c
  JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O020'
  WHERE c.tracker_id = 'M12B-C012'
  RETURNING link_id
)
INSERT INTO _m12_link_map (tracker_id, link_id) SELECT 'M12B-L036', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cross-topic contextual linkage; not used as primary causal support.", "strength": "low", "tracker_id": "M12B-L037"}'
  FROM _m12_claim_map c
  JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O021'
  WHERE c.tracker_id = 'M12B-C013'
  RETURNING link_id
)
INSERT INTO _m12_link_map (tracker_id, link_id) SELECT 'M12B-L037', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cross-topic contextual linkage; not used as primary causal support.", "strength": "low", "tracker_id": "M12B-L038"}'
  FROM _m12_claim_map c
  JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O022'
  WHERE c.tracker_id = 'M12B-C014'
  RETURNING link_id
)
INSERT INTO _m12_link_map (tracker_id, link_id) SELECT 'M12B-L038', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cross-topic contextual linkage; not used as primary causal support.", "strength": "low", "tracker_id": "M12B-L039"}'
  FROM _m12_claim_map c
  JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O023'
  WHERE c.tracker_id = 'M12B-C015'
  RETURNING link_id
)
INSERT INTO _m12_link_map (tracker_id, link_id) SELECT 'M12B-L039', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cross-topic contextual linkage; not used as primary causal support.", "strength": "low", "tracker_id": "M12B-L040"}'
  FROM _m12_claim_map c
  JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O024'
  WHERE c.tracker_id = 'M12B-C016'
  RETURNING link_id
)
INSERT INTO _m12_link_map (tracker_id, link_id) SELECT 'M12B-L040', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cross-topic contextual linkage; not used as primary causal support.", "strength": "low", "tracker_id": "M12B-L041"}'
  FROM _m12_claim_map c
  JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O001'
  WHERE c.tracker_id = 'M12B-C017'
  RETURNING link_id
)
INSERT INTO _m12_link_map (tracker_id, link_id) SELECT 'M12B-L041', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cross-topic contextual linkage; not used as primary causal support.", "strength": "low", "tracker_id": "M12B-L042"}'
  FROM _m12_claim_map c
  JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O002'
  WHERE c.tracker_id = 'M12B-C018'
  RETURNING link_id
)
INSERT INTO _m12_link_map (tracker_id, link_id) SELECT 'M12B-L042', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cross-topic contextual linkage; not used as primary causal support.", "strength": "low", "tracker_id": "M12B-L043"}'
  FROM _m12_claim_map c
  JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O003'
  WHERE c.tracker_id = 'M12B-C019'
  RETURNING link_id
)
INSERT INTO _m12_link_map (tracker_id, link_id) SELECT 'M12B-L043', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cross-topic contextual linkage; not used as primary causal support.", "strength": "low", "tracker_id": "M12B-L044"}'
  FROM _m12_claim_map c
  JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O004'
  WHERE c.tracker_id = 'M12B-C020'
  RETURNING link_id
)
INSERT INTO _m12_link_map (tracker_id, link_id) SELECT 'M12B-L044', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cross-topic contextual linkage; not used as primary causal support.", "strength": "low", "tracker_id": "M12B-L045"}'
  FROM _m12_claim_map c
  JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O005'
  WHERE c.tracker_id = 'M12B-C021'
  RETURNING link_id
)
INSERT INTO _m12_link_map (tracker_id, link_id) SELECT 'M12B-L045', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cross-topic contextual linkage; not used as primary causal support.", "strength": "low", "tracker_id": "M12B-L046"}'
  FROM _m12_claim_map c
  JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O006'
  WHERE c.tracker_id = 'M12B-C022'
  RETURNING link_id
)
INSERT INTO _m12_link_map (tracker_id, link_id) SELECT 'M12B-L046', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cross-topic contextual linkage; not used as primary causal support.", "strength": "low", "tracker_id": "M12B-L047"}'
  FROM _m12_claim_map c
  JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O007'
  WHERE c.tracker_id = 'M12B-C023'
  RETURNING link_id
)
INSERT INTO _m12_link_map (tracker_id, link_id) SELECT 'M12B-L047', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cross-topic contextual linkage; not used as primary causal support.", "strength": "low", "tracker_id": "M12B-L048"}'
  FROM _m12_claim_map c
  JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O008'
  WHERE c.tracker_id = 'M12B-C024'
  RETURNING link_id
)
INSERT INTO _m12_link_map (tracker_id, link_id) SELECT 'M12B-L048', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Topic-level bridge to later-source boundary or comparator observation.", "strength": "low", "tracker_id": "M12B-L049"}'
  FROM _m12_claim_map c
  JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O016'
  WHERE c.tracker_id = 'M12B-C001'
  RETURNING link_id
)
INSERT INTO _m12_link_map (tracker_id, link_id) SELECT 'M12B-L049', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Topic-level bridge to later-source boundary or comparator observation.", "strength": "low", "tracker_id": "M12B-L050"}'
  FROM _m12_claim_map c
  JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O017'
  WHERE c.tracker_id = 'M12B-C002'
  RETURNING link_id
)
INSERT INTO _m12_link_map (tracker_id, link_id) SELECT 'M12B-L050', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Topic-level bridge to later-source boundary or comparator observation.", "strength": "low", "tracker_id": "M12B-L051"}'
  FROM _m12_claim_map c
  JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O018'
  WHERE c.tracker_id = 'M12B-C003'
  RETURNING link_id
)
INSERT INTO _m12_link_map (tracker_id, link_id) SELECT 'M12B-L051', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Topic-level bridge to later-source boundary or comparator observation.", "strength": "low", "tracker_id": "M12B-L052"}'
  FROM _m12_claim_map c
  JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O019'
  WHERE c.tracker_id = 'M12B-C004'
  RETURNING link_id
)
INSERT INTO _m12_link_map (tracker_id, link_id) SELECT 'M12B-L052', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Topic-level bridge to later-source boundary or comparator observation.", "strength": "low", "tracker_id": "M12B-L053"}'
  FROM _m12_claim_map c
  JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O020'
  WHERE c.tracker_id = 'M12B-C005'
  RETURNING link_id
)
INSERT INTO _m12_link_map (tracker_id, link_id) SELECT 'M12B-L053', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Topic-level bridge to later-source boundary or comparator observation.", "strength": "low", "tracker_id": "M12B-L054"}'
  FROM _m12_claim_map c
  JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O021'
  WHERE c.tracker_id = 'M12B-C006'
  RETURNING link_id
)
INSERT INTO _m12_link_map (tracker_id, link_id) SELECT 'M12B-L054', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Topic-level bridge to later-source boundary or comparator observation.", "strength": "low", "tracker_id": "M12B-L055"}'
  FROM _m12_claim_map c
  JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O022'
  WHERE c.tracker_id = 'M12B-C007'
  RETURNING link_id
)
INSERT INTO _m12_link_map (tracker_id, link_id) SELECT 'M12B-L055', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Topic-level bridge to later-source boundary or comparator observation.", "strength": "low", "tracker_id": "M12B-L056"}'
  FROM _m12_claim_map c
  JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O023'
  WHERE c.tracker_id = 'M12B-C008'
  RETURNING link_id
)
INSERT INTO _m12_link_map (tracker_id, link_id) SELECT 'M12B-L056', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Innate immune conditioning is consensus-ready as a mechanistic discovery framework for SCI because timed host stimulation can shift resident and recruited immune responses toward protective programs; LPS is one anchor stimulus, and the result should not be summarized as simple inflammatory suppression.',
    'M12B-T001',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M12B-B001", "M12B-B002", "M12B-B003", "M12B-B004", "M12B-B005", "M12B-B006", "M12B-B007", "M12B-B008"], "claim_tracker_ids": ["M12B-C001", "M12B-C002", "M12B-C003"], "consensus_draft_id": "M12B-S001", "observation_tracker_ids": ["M12B-O001", "M12B-O002", "M12B-O003"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 12 first-pass curation freeze.", "topic_id": "M12B-T001"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m12_consensus_map (tracker_id, consensus_id) SELECT 'M12B-S001', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m12_consensus_map c
JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O001'
WHERE c.tracker_id = 'M12B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m12_consensus_map c
JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O002'
WHERE c.tracker_id = 'M12B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m12_consensus_map c
JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O003'
WHERE c.tracker_id = 'M12B-S001';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Repeated systemic innate stimulation can induce protective spinal microglia-endothelial states in spinal ischemia contexts, with stimulus schedule, endothelial/microglial compartment, and IL-1/IL-1R1 signaling acting as essential boundaries for interpreting protection.',
    'M12B-T002',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M12B-B001", "M12B-B002", "M12B-B003", "M12B-B004", "M12B-B005", "M12B-B006", "M12B-B007", "M12B-B008"], "claim_tracker_ids": ["M12B-C004", "M12B-C005", "M12B-C006"], "consensus_draft_id": "M12B-S002", "observation_tracker_ids": ["M12B-O004", "M12B-O005", "M12B-O006"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 12 first-pass curation freeze.", "topic_id": "M12B-T002"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m12_consensus_map (tracker_id, consensus_id) SELECT 'M12B-S002', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m12_consensus_map c
JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O004'
WHERE c.tracker_id = 'M12B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m12_consensus_map c
JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O005'
WHERE c.tracker_id = 'M12B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m12_consensus_map c
JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O006'
WHERE c.tracker_id = 'M12B-S002';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Innate-adaptor and cytokine routing determine whether stimulation becomes protective tolerance, trained repair competence, or damaging inflammation; TRIF/IRF3, MyD88/CXCL10, IL-10, IL-1, NF-kB, caspase, and non-TLR innate boundaries must be retained.',
    'M12B-T003',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M12B-B001", "M12B-B002", "M12B-B003", "M12B-B004", "M12B-B005", "M12B-B006", "M12B-B007", "M12B-B008"], "claim_tracker_ids": ["M12B-C007", "M12B-C008", "M12B-C009"], "consensus_draft_id": "M12B-S003", "observation_tracker_ids": ["M12B-O007", "M12B-O008", "M12B-O009"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 12 first-pass curation freeze.", "topic_id": "M12B-T003"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m12_consensus_map (tracker_id, consensus_id) SELECT 'M12B-S003', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m12_consensus_map c
JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O007'
WHERE c.tracker_id = 'M12B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m12_consensus_map c
JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O008'
WHERE c.tracker_id = 'M12B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m12_consensus_map c
JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O009'
WHERE c.tracker_id = 'M12B-S003';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Peripheral monocytes and endothelial cells are credible upstream regulatory compartments for conditioning because systemic innate priming can alter CNS injury response without requiring the spinal cord parenchyma to be the initial target.',
    'M12B-T004',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M12B-B001", "M12B-B002", "M12B-B003", "M12B-B004", "M12B-B005", "M12B-B006", "M12B-B007", "M12B-B008"], "claim_tracker_ids": ["M12B-C010", "M12B-C011", "M12B-C012"], "consensus_draft_id": "M12B-S004", "observation_tracker_ids": ["M12B-O010", "M12B-O011", "M12B-O012"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 12 first-pass curation freeze.", "topic_id": "M12B-T004"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m12_consensus_map (tracker_id, consensus_id) SELECT 'M12B-S004', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m12_consensus_map c
JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O010'
WHERE c.tracker_id = 'M12B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m12_consensus_map c
JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O011'
WHERE c.tracker_id = 'M12B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m12_consensus_map c
JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O012'
WHERE c.tracker_id = 'M12B-S004';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'TLR4 and inflammatory signaling after SCI can support repair-relevant processes as well as injury amplification, so the project should pursue state- and timing-specific regulatory nodes rather than a blanket anti-inflammatory framing.',
    'M12B-T005',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M12B-B001", "M12B-B002", "M12B-B003", "M12B-B004", "M12B-B005", "M12B-B006", "M12B-B007", "M12B-B008"], "claim_tracker_ids": ["M12B-C013", "M12B-C014", "M12B-C015"], "consensus_draft_id": "M12B-S005", "observation_tracker_ids": ["M12B-O013", "M12B-O014", "M12B-O015"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 12 first-pass curation freeze.", "topic_id": "M12B-T005"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m12_consensus_map (tracker_id, consensus_id) SELECT 'M12B-S005', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m12_consensus_map c
JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O013'
WHERE c.tracker_id = 'M12B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m12_consensus_map c
JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O014'
WHERE c.tracker_id = 'M12B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m12_consensus_map c
JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O015'
WHERE c.tracker_id = 'M12B-S005';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Post-injury or chronic innate stimulation studies reveal inducible spinal plasticity and microglial-state capacity, but they should be treated as boundary and comparator evidence unless the experiment tests pre-injury or peri-procedural conditioning timing.',
    'M12B-T006',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M12B-B001", "M12B-B002", "M12B-B003", "M12B-B004", "M12B-B005", "M12B-B006", "M12B-B007", "M12B-B008"], "claim_tracker_ids": ["M12B-C016", "M12B-C017", "M12B-C018"], "consensus_draft_id": "M12B-S006", "observation_tracker_ids": ["M12B-O016", "M12B-O017", "M12B-O018"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 12 first-pass curation freeze.", "topic_id": "M12B-T006"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m12_consensus_map (tracker_id, consensus_id) SELECT 'M12B-S006', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m12_consensus_map c
JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O016'
WHERE c.tracker_id = 'M12B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m12_consensus_map c
JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O017'
WHERE c.tracker_id = 'M12B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m12_consensus_map c
JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O018'
WHERE c.tracker_id = 'M12B-S006';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'In vitro rows, ODC-SCI datasets, TLR-agonist studies, and microbiome host-conditioning analogs define validation paths for candidate regulatory nodes, but they require source extraction before they can carry high-confidence mechanistic claims.',
    'M12B-T007',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M12B-B001", "M12B-B002", "M12B-B003", "M12B-B004", "M12B-B005", "M12B-B006", "M12B-B007", "M12B-B008"], "claim_tracker_ids": ["M12B-C019", "M12B-C020", "M12B-C021"], "consensus_draft_id": "M12B-S007", "observation_tracker_ids": ["M12B-O019", "M12B-O020", "M12B-O021"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 12 first-pass curation freeze.", "topic_id": "M12B-T007"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m12_consensus_map (tracker_id, consensus_id) SELECT 'M12B-S007', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m12_consensus_map c
JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O019'
WHERE c.tracker_id = 'M12B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m12_consensus_map c
JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O020'
WHERE c.tracker_id = 'M12B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m12_consensus_map c
JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O021'
WHERE c.tracker_id = 'M12B-S007';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Module 12 should be used to identify endogenous protective programs and safer host-conditioning analogs across innate immune tolerance, trained/tolerized states, microbiome/systemic inflammatory priming, monocyte/endothelial signaling, and TLR/non-TLR agonist biology. LPS remains one discovery platform for Aim 1 biology, not a proposed clinical conditioning agent before implantation or reconstruction.',
    'M12B-T008',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M12B-B001", "M12B-B002", "M12B-B003", "M12B-B004", "M12B-B005", "M12B-B006", "M12B-B007", "M12B-B008"], "claim_tracker_ids": ["M12B-C022", "M12B-C023", "M12B-C024"], "consensus_draft_id": "M12B-S008", "observation_tracker_ids": ["M12B-O022", "M12B-O023", "M12B-O024"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 12 first-pass curation freeze.", "topic_id": "M12B-T008"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m12_consensus_map (tracker_id, consensus_id) SELECT 'M12B-S008', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m12_consensus_map c
JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O022'
WHERE c.tracker_id = 'M12B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m12_consensus_map c
JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O023'
WHERE c.tracker_id = 'M12B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m12_consensus_map c
JOIN _m12_observation_map o ON o.tracker_id = 'M12B-O024'
WHERE c.tracker_id = 'M12B-S008';

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
  SELECT COUNT(*) INTO paper_count FROM _m12_paper_map;
  SELECT COUNT(*) INTO experiment_count FROM _m12_experiment_map;
  SELECT COUNT(*) INTO observation_count FROM _m12_observation_map;
  SELECT COUNT(*) INTO claim_count FROM _m12_claim_map;
  SELECT COUNT(*) INTO link_count FROM _m12_link_map;
  SELECT COUNT(*) INTO consensus_count FROM _m12_consensus_map;
  SELECT COUNT(*) INTO consensus_observation_count
  FROM Consensus_Observation co
  JOIN _m12_consensus_map cm ON cm.consensus_id = co.consensus_id;
  IF paper_count <> 24 THEN RAISE EXCEPTION 'Expected 24 papers, found %', paper_count; END IF;
  IF experiment_count <> 24 THEN RAISE EXCEPTION 'Unexpected experiment count %', experiment_count; END IF;
  IF observation_count <> 24 THEN RAISE EXCEPTION 'Expected 24 observations, found %', observation_count; END IF;
  IF claim_count <> 24 THEN RAISE EXCEPTION 'Expected 24 claims, found %', claim_count; END IF;
  IF link_count <> 56 THEN RAISE EXCEPTION 'Expected 56 evidence links, found %', link_count; END IF;
  IF consensus_count <> 8 THEN RAISE EXCEPTION 'Expected 8 consensus rows, found %', consensus_count; END IF;
  IF consensus_observation_count <> 24 THEN RAISE EXCEPTION 'Unexpected consensus-observation count %', consensus_observation_count; END IF;
END $$;

COMMIT;
