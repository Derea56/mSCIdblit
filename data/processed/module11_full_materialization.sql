-- Module 11B full first-pass materialization generated from tracker-derived JSON.
-- This script is intended for a fresh database loaded with schema/schema.sql and scripts/seed_controlled_vocab.sql.
BEGIN;

CREATE TEMP TABLE _m11_paper_map (tracker_id TEXT PRIMARY KEY, paper_id INTEGER NOT NULL);
CREATE TEMP TABLE _m11_paradigm_map (tracker_id TEXT PRIMARY KEY, paradigm_id INTEGER NOT NULL);
CREATE TEMP TABLE _m11_experiment_map (tracker_id TEXT PRIMARY KEY, experiment_id INTEGER NOT NULL);
CREATE TEMP TABLE _m11_observation_map (tracker_id TEXT PRIMARY KEY, observation_id INTEGER NOT NULL);
CREATE TEMP TABLE _m11_claim_map (tracker_id TEXT PRIMARY KEY, claim_id INTEGER NOT NULL);
CREATE TEMP TABLE _m11_link_map (tracker_id TEXT PRIMARY KEY, link_id INTEGER NOT NULL);
CREATE TEMP TABLE _m11_consensus_map (tracker_id TEXT PRIMARY KEY, consensus_id INTEGER NOT NULL);

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Cerebrospinal fluid drainage for thoracic and thoracoabdominal aortic aneurysm surgery', 'mSCIdblit curator', 2012,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Cochrane review; 3 RCTs, 287 participants; limited but supportive evidence with boundary conditions.", "module": "Module 11B", "tracker_id": "M11A-P001"}'
  )
  RETURNING paper_id
)
INSERT INTO _m11_paper_map (tracker_id, paper_id) SELECT 'M11A-P001', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Prospective randomized pilot trial comparing prophylactic and therapeutic cerebrospinal fluid drainage during complex endovascular thoracoabdominal aortic aneurysm repair', 'mSCIdblit curator', 2024,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "20-patient randomized feasibility trial; one SCI event and one drain-related epidural hematoma.", "module": "Module 11B", "tracker_id": "M11A-P002"}'
  )
  RETURNING paper_id
)
INSERT INTO _m11_paper_map (tracker_id, paper_id) SELECT 'M11A-P002', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Current strategies of spinal cord protection during thoracoabdominal aortic surgery', 'mSCIdblit curator', 2018,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Emphasizes no single protective measure and recommends multimodal protection.", "module": "Module 11B", "tracker_id": "M11A-P003"}'
  )
  RETURNING paper_id
)
INSERT INTO _m11_paper_map (tracker_id, paper_id) SELECT 'M11A-P003', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Spinal cord protection for thoracoabdominal aortic aneurysm repair: from bench to bedside', 'mSCIdblit curator', 2023,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Review of anatomy, mechanisms, laboratory and clinical protective strategies.", "module": "Module 11B", "tracker_id": "M11A-P004"}'
  )
  RETURNING paper_id
)
INSERT INTO _m11_paper_map (tracker_id, paper_id) SELECT 'M11A-P004', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Staging Endovascular Thoracic and Thoracoabdominal Aortic Aneurysm Repairs and the Risk of Post-operative Spinal Cord Ischemia', 'mSCIdblit curator', 2022,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "1421 VQI cases; staged repair not independently associated with lower SCI after adjustment; trend toward less permanent SCI among SCI cases.", "module": "Module 11B", "tracker_id": "M11A-P005"}'
  )
  RETURNING paper_id
)
INSERT INTO _m11_paper_map (tracker_id, paper_id) SELECT 'M11A-P005', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Staged procedures for prevention of spinal cord ischemia in endovascular aortic surgery', 'mSCIdblit curator', 2018,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Review of staging methods to reinforce collateral spinal perfusion.", "module": "Module 11B", "tracker_id": "M11A-P006"}'
  )
  RETURNING paper_id
)
INSERT INTO _m11_paper_map (tracker_id, paper_id) SELECT 'M11A-P006', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Open, closed or a bit of both: a systematic review and meta-analysis of staged thoraco-abdominal aortic aneurysm repair', 'mSCIdblit curator', 2023,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "20 studies, 924 patients; SCI differed by approach while all used drainage/monitoring/staging components.", "module": "Module 11B", "tracker_id": "M11A-P007"}'
  )
  RETURNING paper_id
)
INSERT INTO _m11_paper_map (tracker_id, paper_id) SELECT 'M11A-P007', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Planned Staged Repair of Thoracoabdominal Aortic Aneurysms to Minimize Spinal Cord Injury: A Proof of Concept', 'mSCIdblit curator', 2015,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Proof-of-concept for planned staging to reduce spinal cord injury risk.", "module": "Module 11B", "tracker_id": "M11A-P008"}'
  )
  RETURNING paper_id
)
INSERT INTO _m11_paper_map (tracker_id, paper_id) SELECT 'M11A-P008', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Patterns of collateral arteries to the spinal cord after thoraco-abdominal aortic aneurysm repair', 'mSCIdblit curator', 2024,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "179 patients; postoperative collateral pathways assessed after AKA-segmental artery occlusion.", "module": "Module 11B", "tracker_id": "M11A-P009"}'
  )
  RETURNING paper_id
)
INSERT INTO _m11_paper_map (tracker_id, paper_id) SELECT 'M11A-P009', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Comparison of the protective effects of direct ischemic preconditioning and remote ischemic preconditioning in a rabbit model of transient spinal cord ischemia', 'mSCIdblit curator', 2018,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "DIPC protected neurologic/histologic outcomes; kidney/limb RIPC did not; Akt2 signal implicated.", "module": "Module 11B", "tracker_id": "M11A-P010"}'
  )
  RETURNING paper_id
)
INSERT INTO _m11_paper_map (tracker_id, paper_id) SELECT 'M11A-P010', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Ischaemic preconditioning of the spinal cord to prevent spinal cord ischaemia during endovascular repair of thoracoabdominal aortic aneurysm: first clinical experience', 'mSCIdblit curator', 2018,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "57 patients underwent MISACE; 55 proceeded to endovascular repair; no 30-day SCI reported.", "module": "Module 11B", "tracker_id": "M11A-P011"}'
  )
  RETURNING paper_id
)
INSERT INTO _m11_paper_map (tracker_id, paper_id) SELECT 'M11A-P011', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Remote ischaemic preconditioning versus sham procedure for abdominal aortic aneurysm repair: an external feasibility randomized controlled trial', 'mSCIdblit curator', 2015,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "69 randomized; feasible and acceptable; not spinal-cord-specific and confounded by EVAR complexity.", "module": "Module 11B", "tracker_id": "M11A-P012"}'
  )
  RETURNING paper_id
)
INSERT INTO _m11_paper_map (tracker_id, paper_id) SELECT 'M11A-P012', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Sevoflurane preconditioning induces rapid ischemic tolerance against spinal cord ischemia/reperfusion through activation of extracellular signal-regulated kinase in rabbits', 'mSCIdblit curator', 2009,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Sevoflurane improved neurologic/histologic outcomes; ERK blockade attenuated effect.", "module": "Module 11B", "tracker_id": "M11A-P013"}'
  )
  RETURNING paper_id
)
INSERT INTO _m11_paper_map (tracker_id, paper_id) SELECT 'M11A-P013', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Ischemic preconditioning protects against spinal cord ischemia-reperfusion injury in rabbits by attenuating blood spinal cord barrier disruption', 'mSCIdblit curator', 2013,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "IPC improved Tarlov scores, reduced barrier permeability/edema, preserved ZO-1, reduced MMP-9/TNF-alpha.", "module": "Module 11B", "tracker_id": "M11A-P014"}'
  )
  RETURNING paper_id
)
INSERT INTO _m11_paper_map (tracker_id, paper_id) SELECT 'M11A-P014', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Co-application of ischemic preconditioning and postconditioning provides additive neuroprotection against spinal cord ischemia in rabbits', 'mSCIdblit curator', 2008,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Combined IPC/postconditioning improved Tarlov scores and preserved motor neurons/white matter.", "module": "Module 11B", "tracker_id": "M11A-P015"}'
  )
  RETURNING paper_id
)
INSERT INTO _m11_paper_map (tracker_id, paper_id) SELECT 'M11A-P015', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Postconditioning, a series of brief interruptions of early reperfusion, prevents neurologic injury after spinal cord ischemia', 'mSCIdblit curator', 2006,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "4-cycle postconditioning protected; benefit disappeared when delayed 10 minutes.", "module": "Module 11B", "tracker_id": "M11A-P016"}'
  )
  RETURNING paper_id
)
INSERT INTO _m11_paper_map (tracker_id, paper_id) SELECT 'M11A-P016', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Isoflurane produces delayed preconditioning against spinal cord ischemic injury via release of free radicals in rabbits', 'mSCIdblit curator', 2006,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Delayed protection at 24-48 h; free-radical scavenger blocked benefit.", "module": "Module 11B", "tracker_id": "M11A-P017"}'
  )
  RETURNING paper_id
)
INSERT INTO _m11_paper_map (tracker_id, paper_id) SELECT 'M11A-P017', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Epidural perfusion cooling protection against protracted spinal cord ischemia in rabbits', 'mSCIdblit curator', 1993,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Cold epidural perfusion protected even after prolonged ischemia relative to normothermia.", "module": "Module 11B", "tracker_id": "M11A-P018"}'
  )
  RETURNING paper_id
)
INSERT INTO _m11_paper_map (tracker_id, paper_id) SELECT 'M11A-P018', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Appraisal of cerebrospinal fluid alterations during aortic surgery with intrathecal papaverine administration and cerebrospinal fluid drainage', 'mSCIdblit curator', 1990,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "11-patient physiologic study; CSF pressure rose with induction/cross-clamp and fell with drainage.", "module": "Module 11B", "tracker_id": "M11A-P019"}'
  )
  RETURNING paper_id
)
INSERT INTO _m11_paper_map (tracker_id, paper_id) SELECT 'M11A-P019', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Effects of darbepoetin-alpha in spinal cord ischemia-reperfusion injury in the rabbit', 'mSCIdblit curator', 2012,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Darbepoetin reduced oxidative/apoptotic markers and improved neurologic outcomes.", "module": "Module 11B", "tracker_id": "M11A-P020"}'
  )
  RETURNING paper_id
)
INSERT INTO _m11_paper_map (tracker_id, paper_id) SELECT 'M11A-P020', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Naloxone infusion and drainage of cerebrospinal fluid as adjuncts to postoperative care after repair of thoracoabdominal aneurysms', 'mSCIdblit curator', 1999,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Review frames paraplegia as multifactorial and supports combined adjunctive postoperative care.", "module": "Module 11B", "tracker_id": "M11A-P021"}'
  )
  RETURNING paper_id
)
INSERT INTO _m11_paper_map (tracker_id, paper_id) SELECT 'M11A-P021', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Strategy for spinal cord protection during thoracoabdominal aortic surgery', 'mSCIdblit curator', 2004,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Japanese strategy paper; multimodal surgical protection bundle.", "module": "Module 11B", "tracker_id": "M11A-P022"}'
  )
  RETURNING paper_id
)
INSERT INTO _m11_paper_map (tracker_id, paper_id) SELECT 'M11A-P022', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'The combination of insulin-like growth factor 1 and erythropoietin protects against ischemic spinal cord injury in rabbits', 'mSCIdblit curator', 2015,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Combination treatment tested for post-ischemic neuroprotection and signaling activation.", "module": "Module 11B", "tracker_id": "M11A-P023"}'
  )
  RETURNING paper_id
)
INSERT INTO _m11_paper_map (tracker_id, paper_id) SELECT 'M11A-P023', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Combined use of cerebral spinal fluid drainage and naloxone reduces the risk of paraplegia in thoracoabdominal aneurysm repair', 'mSCIdblit curator', 1994,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "110-patient cohort; 1 deficit with CSFD/naloxone versus 11 without, but nonrandomized/historical boundaries.", "module": "Module 11B", "tracker_id": "M11A-P024"}'
  )
  RETURNING paper_id
)
INSERT INTO _m11_paper_map (tracker_id, paper_id) SELECT 'M11A-P024', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Intraoperative neuroprotective interventions prevent spinal cord ischemia and injury in thoracic endovascular aortic repair', 'mSCIdblit curator', 2016,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Aggressive intra/postoperative neuroprotective bundle in TEVAR; retrospective cohort boundary.", "module": "Module 11B", "tracker_id": "M11A-P025"}'
  )
  RETURNING paper_id
)
INSERT INTO _m11_paper_map (tracker_id, paper_id) SELECT 'M11A-P025', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Benefits and Risks of Prophylactic Cerebrospinal Fluid Catheter and Evoked Potential Monitoring in Symptomatic Spinal Cord Ischemia Low-Risk Thoracic Endovascular Aortic Repair', 'mSCIdblit curator', 2016,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "223 procedures; CSF drainage associated with lower symptomatic SCI; EP monitoring detected acute inflow problems.", "module": "Module 11B", "tracker_id": "M11A-P026"}'
  )
  RETURNING paper_id
)
INSERT INTO _m11_paper_map (tracker_id, paper_id) SELECT 'M11A-P026', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Safety of cerebrospinal fluid drainage for spinal cord ischemia prevention in thoracic endovascular aortic repair', 'mSCIdblit curator', 2022,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "936 TEVAR procedures; 390 drains; assesses complication severity and timing.", "module": "Module 11B", "tracker_id": "M11A-P027"}'
  )
  RETURNING paper_id
)
INSERT INTO _m11_paper_map (tracker_id, paper_id) SELECT 'M11A-P027', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Open reconstruction of thoracoabdominal aortic aneurysms', 'mSCIdblit curator', 2013,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "SCI occurred in 10.5%; risk factors included prior aortic surgery, diabetes, and post-bypass hypotension.", "module": "Module 11B", "tracker_id": "M11A-P028"}'
  )
  RETURNING paper_id
)
INSERT INTO _m11_paper_map (tracker_id, paper_id) SELECT 'M11A-P028', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Prophylactic vs Therapeutic Cerebrospinal Fluid Drain Placement During Endovascular Thoracoabdominal Aortic Aneurysm Repair', 'mSCIdblit curator', 2025,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "ClinicalTrials.gov source-page row; primary endpoint is SCI onset baseline to 1 year.", "module": "Module 11B", "tracker_id": "M11A-P029"}'
  )
  RETURNING paper_id
)
INSERT INTO _m11_paper_map (tracker_id, paper_id) SELECT 'M11A-P029', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'OSA as a Remote Ischemic Preconditioning in Vascular Surgery', 'mSCIdblit curator', 2025,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Recruiting vascular-surgery trial; primary endpoints are I/R injury markers, not spinal cord-specific endpoints.", "module": "Module 11B", "tracker_id": "M11A-P030"}'
  )
  RETURNING paper_id
)
INSERT INTO _m11_paper_map (tracker_id, paper_id) SELECT 'M11A-P030', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'NIRS Monitoring of Spinal Cord Ischemia in Aortic Surgery', 'mSCIdblit curator', 2026,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Observational monitoring/prevention trial; estimated completion 2027; endpoint boundary with neuromonitoring.", "module": "Module 11B", "tracker_id": "M11A-P031"}'
  )
  RETURNING paper_id
)
INSERT INTO _m11_paper_map (tracker_id, paper_id) SELECT 'M11A-P031', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Randomized trial anchors summarized in CSF-drainage reviews', 'mSCIdblit curator', 1990,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Composite anchor for the three RCTs because individual trial metadata should be expanded in full-text pass.", "module": "Module 11B", "tracker_id": "M11A-P032"}'
  )
  RETURNING paper_id
)
INSERT INTO _m11_paper_map (tracker_id, paper_id) SELECT 'M11A-P032', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 11B curated evidence extraction',
    'First-pass Module 11B spinal cord ischemic conditioning in cardiac and aortic surgery curation for M11A-P001',
    'Tracker-derived materialization from Module_11B_TRACKER.md'
  FROM _m11_paper_map WHERE tracker_id = 'M11A-P001'
  RETURNING paradigm_id
)
INSERT INTO _m11_paradigm_map (tracker_id, paradigm_id) SELECT 'M11A-P001', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 11B curated evidence extraction',
    'First-pass Module 11B spinal cord ischemic conditioning in cardiac and aortic surgery curation for M11A-P002',
    'Tracker-derived materialization from Module_11B_TRACKER.md'
  FROM _m11_paper_map WHERE tracker_id = 'M11A-P002'
  RETURNING paradigm_id
)
INSERT INTO _m11_paradigm_map (tracker_id, paradigm_id) SELECT 'M11A-P002', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 11B curated evidence extraction',
    'First-pass Module 11B spinal cord ischemic conditioning in cardiac and aortic surgery curation for M11A-P003',
    'Tracker-derived materialization from Module_11B_TRACKER.md'
  FROM _m11_paper_map WHERE tracker_id = 'M11A-P003'
  RETURNING paradigm_id
)
INSERT INTO _m11_paradigm_map (tracker_id, paradigm_id) SELECT 'M11A-P003', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 11B curated evidence extraction',
    'First-pass Module 11B spinal cord ischemic conditioning in cardiac and aortic surgery curation for M11A-P004',
    'Tracker-derived materialization from Module_11B_TRACKER.md'
  FROM _m11_paper_map WHERE tracker_id = 'M11A-P004'
  RETURNING paradigm_id
)
INSERT INTO _m11_paradigm_map (tracker_id, paradigm_id) SELECT 'M11A-P004', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 11B curated evidence extraction',
    'First-pass Module 11B spinal cord ischemic conditioning in cardiac and aortic surgery curation for M11A-P005',
    'Tracker-derived materialization from Module_11B_TRACKER.md'
  FROM _m11_paper_map WHERE tracker_id = 'M11A-P005'
  RETURNING paradigm_id
)
INSERT INTO _m11_paradigm_map (tracker_id, paradigm_id) SELECT 'M11A-P005', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 11B curated evidence extraction',
    'First-pass Module 11B spinal cord ischemic conditioning in cardiac and aortic surgery curation for M11A-P006',
    'Tracker-derived materialization from Module_11B_TRACKER.md'
  FROM _m11_paper_map WHERE tracker_id = 'M11A-P006'
  RETURNING paradigm_id
)
INSERT INTO _m11_paradigm_map (tracker_id, paradigm_id) SELECT 'M11A-P006', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 11B curated evidence extraction',
    'First-pass Module 11B spinal cord ischemic conditioning in cardiac and aortic surgery curation for M11A-P007',
    'Tracker-derived materialization from Module_11B_TRACKER.md'
  FROM _m11_paper_map WHERE tracker_id = 'M11A-P007'
  RETURNING paradigm_id
)
INSERT INTO _m11_paradigm_map (tracker_id, paradigm_id) SELECT 'M11A-P007', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 11B curated evidence extraction',
    'First-pass Module 11B spinal cord ischemic conditioning in cardiac and aortic surgery curation for M11A-P008',
    'Tracker-derived materialization from Module_11B_TRACKER.md'
  FROM _m11_paper_map WHERE tracker_id = 'M11A-P008'
  RETURNING paradigm_id
)
INSERT INTO _m11_paradigm_map (tracker_id, paradigm_id) SELECT 'M11A-P008', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 11B curated evidence extraction',
    'First-pass Module 11B spinal cord ischemic conditioning in cardiac and aortic surgery curation for M11A-P009',
    'Tracker-derived materialization from Module_11B_TRACKER.md'
  FROM _m11_paper_map WHERE tracker_id = 'M11A-P009'
  RETURNING paradigm_id
)
INSERT INTO _m11_paradigm_map (tracker_id, paradigm_id) SELECT 'M11A-P009', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 11B curated evidence extraction',
    'First-pass Module 11B spinal cord ischemic conditioning in cardiac and aortic surgery curation for M11A-P010',
    'Tracker-derived materialization from Module_11B_TRACKER.md'
  FROM _m11_paper_map WHERE tracker_id = 'M11A-P010'
  RETURNING paradigm_id
)
INSERT INTO _m11_paradigm_map (tracker_id, paradigm_id) SELECT 'M11A-P010', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 11B curated evidence extraction',
    'First-pass Module 11B spinal cord ischemic conditioning in cardiac and aortic surgery curation for M11A-P011',
    'Tracker-derived materialization from Module_11B_TRACKER.md'
  FROM _m11_paper_map WHERE tracker_id = 'M11A-P011'
  RETURNING paradigm_id
)
INSERT INTO _m11_paradigm_map (tracker_id, paradigm_id) SELECT 'M11A-P011', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 11B curated evidence extraction',
    'First-pass Module 11B spinal cord ischemic conditioning in cardiac and aortic surgery curation for M11A-P012',
    'Tracker-derived materialization from Module_11B_TRACKER.md'
  FROM _m11_paper_map WHERE tracker_id = 'M11A-P012'
  RETURNING paradigm_id
)
INSERT INTO _m11_paradigm_map (tracker_id, paradigm_id) SELECT 'M11A-P012', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 11B curated evidence extraction',
    'First-pass Module 11B spinal cord ischemic conditioning in cardiac and aortic surgery curation for M11A-P013',
    'Tracker-derived materialization from Module_11B_TRACKER.md'
  FROM _m11_paper_map WHERE tracker_id = 'M11A-P013'
  RETURNING paradigm_id
)
INSERT INTO _m11_paradigm_map (tracker_id, paradigm_id) SELECT 'M11A-P013', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 11B curated evidence extraction',
    'First-pass Module 11B spinal cord ischemic conditioning in cardiac and aortic surgery curation for M11A-P014',
    'Tracker-derived materialization from Module_11B_TRACKER.md'
  FROM _m11_paper_map WHERE tracker_id = 'M11A-P014'
  RETURNING paradigm_id
)
INSERT INTO _m11_paradigm_map (tracker_id, paradigm_id) SELECT 'M11A-P014', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 11B curated evidence extraction',
    'First-pass Module 11B spinal cord ischemic conditioning in cardiac and aortic surgery curation for M11A-P015',
    'Tracker-derived materialization from Module_11B_TRACKER.md'
  FROM _m11_paper_map WHERE tracker_id = 'M11A-P015'
  RETURNING paradigm_id
)
INSERT INTO _m11_paradigm_map (tracker_id, paradigm_id) SELECT 'M11A-P015', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 11B curated evidence extraction',
    'First-pass Module 11B spinal cord ischemic conditioning in cardiac and aortic surgery curation for M11A-P016',
    'Tracker-derived materialization from Module_11B_TRACKER.md'
  FROM _m11_paper_map WHERE tracker_id = 'M11A-P016'
  RETURNING paradigm_id
)
INSERT INTO _m11_paradigm_map (tracker_id, paradigm_id) SELECT 'M11A-P016', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 11B curated evidence extraction',
    'First-pass Module 11B spinal cord ischemic conditioning in cardiac and aortic surgery curation for M11A-P017',
    'Tracker-derived materialization from Module_11B_TRACKER.md'
  FROM _m11_paper_map WHERE tracker_id = 'M11A-P017'
  RETURNING paradigm_id
)
INSERT INTO _m11_paradigm_map (tracker_id, paradigm_id) SELECT 'M11A-P017', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 11B curated evidence extraction',
    'First-pass Module 11B spinal cord ischemic conditioning in cardiac and aortic surgery curation for M11A-P018',
    'Tracker-derived materialization from Module_11B_TRACKER.md'
  FROM _m11_paper_map WHERE tracker_id = 'M11A-P018'
  RETURNING paradigm_id
)
INSERT INTO _m11_paradigm_map (tracker_id, paradigm_id) SELECT 'M11A-P018', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 11B curated evidence extraction',
    'First-pass Module 11B spinal cord ischemic conditioning in cardiac and aortic surgery curation for M11A-P019',
    'Tracker-derived materialization from Module_11B_TRACKER.md'
  FROM _m11_paper_map WHERE tracker_id = 'M11A-P019'
  RETURNING paradigm_id
)
INSERT INTO _m11_paradigm_map (tracker_id, paradigm_id) SELECT 'M11A-P019', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 11B curated evidence extraction',
    'First-pass Module 11B spinal cord ischemic conditioning in cardiac and aortic surgery curation for M11A-P020',
    'Tracker-derived materialization from Module_11B_TRACKER.md'
  FROM _m11_paper_map WHERE tracker_id = 'M11A-P020'
  RETURNING paradigm_id
)
INSERT INTO _m11_paradigm_map (tracker_id, paradigm_id) SELECT 'M11A-P020', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 11B curated evidence extraction',
    'First-pass Module 11B spinal cord ischemic conditioning in cardiac and aortic surgery curation for M11A-P021',
    'Tracker-derived materialization from Module_11B_TRACKER.md'
  FROM _m11_paper_map WHERE tracker_id = 'M11A-P021'
  RETURNING paradigm_id
)
INSERT INTO _m11_paradigm_map (tracker_id, paradigm_id) SELECT 'M11A-P021', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 11B curated evidence extraction',
    'First-pass Module 11B spinal cord ischemic conditioning in cardiac and aortic surgery curation for M11A-P022',
    'Tracker-derived materialization from Module_11B_TRACKER.md'
  FROM _m11_paper_map WHERE tracker_id = 'M11A-P022'
  RETURNING paradigm_id
)
INSERT INTO _m11_paradigm_map (tracker_id, paradigm_id) SELECT 'M11A-P022', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 11B curated evidence extraction',
    'First-pass Module 11B spinal cord ischemic conditioning in cardiac and aortic surgery curation for M11A-P023',
    'Tracker-derived materialization from Module_11B_TRACKER.md'
  FROM _m11_paper_map WHERE tracker_id = 'M11A-P023'
  RETURNING paradigm_id
)
INSERT INTO _m11_paradigm_map (tracker_id, paradigm_id) SELECT 'M11A-P023', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 11B curated evidence extraction',
    'First-pass Module 11B spinal cord ischemic conditioning in cardiac and aortic surgery curation for M11A-P024',
    'Tracker-derived materialization from Module_11B_TRACKER.md'
  FROM _m11_paper_map WHERE tracker_id = 'M11A-P024'
  RETURNING paradigm_id
)
INSERT INTO _m11_paradigm_map (tracker_id, paradigm_id) SELECT 'M11A-P024', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 11B curated evidence extraction',
    'First-pass Module 11B spinal cord ischemic conditioning in cardiac and aortic surgery curation for M11A-P025',
    'Tracker-derived materialization from Module_11B_TRACKER.md'
  FROM _m11_paper_map WHERE tracker_id = 'M11A-P025'
  RETURNING paradigm_id
)
INSERT INTO _m11_paradigm_map (tracker_id, paradigm_id) SELECT 'M11A-P025', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 11B curated evidence extraction',
    'First-pass Module 11B spinal cord ischemic conditioning in cardiac and aortic surgery curation for M11A-P026',
    'Tracker-derived materialization from Module_11B_TRACKER.md'
  FROM _m11_paper_map WHERE tracker_id = 'M11A-P026'
  RETURNING paradigm_id
)
INSERT INTO _m11_paradigm_map (tracker_id, paradigm_id) SELECT 'M11A-P026', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 11B curated evidence extraction',
    'First-pass Module 11B spinal cord ischemic conditioning in cardiac and aortic surgery curation for M11A-P027',
    'Tracker-derived materialization from Module_11B_TRACKER.md'
  FROM _m11_paper_map WHERE tracker_id = 'M11A-P027'
  RETURNING paradigm_id
)
INSERT INTO _m11_paradigm_map (tracker_id, paradigm_id) SELECT 'M11A-P027', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 11B curated evidence extraction',
    'First-pass Module 11B spinal cord ischemic conditioning in cardiac and aortic surgery curation for M11A-P028',
    'Tracker-derived materialization from Module_11B_TRACKER.md'
  FROM _m11_paper_map WHERE tracker_id = 'M11A-P028'
  RETURNING paradigm_id
)
INSERT INTO _m11_paradigm_map (tracker_id, paradigm_id) SELECT 'M11A-P028', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 11B curated evidence extraction',
    'First-pass Module 11B spinal cord ischemic conditioning in cardiac and aortic surgery curation for M11A-P029',
    'Tracker-derived materialization from Module_11B_TRACKER.md'
  FROM _m11_paper_map WHERE tracker_id = 'M11A-P029'
  RETURNING paradigm_id
)
INSERT INTO _m11_paradigm_map (tracker_id, paradigm_id) SELECT 'M11A-P029', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 11B curated evidence extraction',
    'First-pass Module 11B spinal cord ischemic conditioning in cardiac and aortic surgery curation for M11A-P030',
    'Tracker-derived materialization from Module_11B_TRACKER.md'
  FROM _m11_paper_map WHERE tracker_id = 'M11A-P030'
  RETURNING paradigm_id
)
INSERT INTO _m11_paradigm_map (tracker_id, paradigm_id) SELECT 'M11A-P030', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 11B curated evidence extraction',
    'First-pass Module 11B spinal cord ischemic conditioning in cardiac and aortic surgery curation for M11A-P031',
    'Tracker-derived materialization from Module_11B_TRACKER.md'
  FROM _m11_paper_map WHERE tracker_id = 'M11A-P031'
  RETURNING paradigm_id
)
INSERT INTO _m11_paradigm_map (tracker_id, paradigm_id) SELECT 'M11A-P031', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 11B curated evidence extraction',
    'First-pass Module 11B spinal cord ischemic conditioning in cardiac and aortic surgery curation for M11A-P032',
    'Tracker-derived materialization from Module_11B_TRACKER.md'
  FROM _m11_paper_map WHERE tracker_id = 'M11A-P032'
  RETURNING paradigm_id
)
INSERT INTO _m11_paradigm_map (tracker_id, paradigm_id) SELECT 'M11A-P032', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M11A-P001-E001',
    'Module 11B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M11B-O001"], "source_experiment_tracker_id": "M11A-P001-E001", "source_paper_tracker_id": "M11A-P001", "tracker_key": "M11A-P001::M11A-P001-E001"}'
  FROM _m11_paper_map p
  JOIN _m11_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M11A-P001'
  RETURNING experiment_id
)
INSERT INTO _m11_experiment_map (tracker_id, experiment_id) SELECT 'M11A-P001::M11A-P001-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M11A-P002-E001',
    'Module 11B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M11B-O002"], "source_experiment_tracker_id": "M11A-P002-E001", "source_paper_tracker_id": "M11A-P002", "tracker_key": "M11A-P002::M11A-P002-E001"}'
  FROM _m11_paper_map p
  JOIN _m11_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M11A-P002'
  RETURNING experiment_id
)
INSERT INTO _m11_experiment_map (tracker_id, experiment_id) SELECT 'M11A-P002::M11A-P002-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M11A-P003-E001',
    'Module 11B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M11B-O003"], "source_experiment_tracker_id": "M11A-P003-E001", "source_paper_tracker_id": "M11A-P003", "tracker_key": "M11A-P003::M11A-P003-E001"}'
  FROM _m11_paper_map p
  JOIN _m11_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M11A-P003'
  RETURNING experiment_id
)
INSERT INTO _m11_experiment_map (tracker_id, experiment_id) SELECT 'M11A-P003::M11A-P003-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M11A-P004-E001',
    'Module 11B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M11B-O004"], "source_experiment_tracker_id": "M11A-P004-E001", "source_paper_tracker_id": "M11A-P004", "tracker_key": "M11A-P004::M11A-P004-E001"}'
  FROM _m11_paper_map p
  JOIN _m11_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M11A-P004'
  RETURNING experiment_id
)
INSERT INTO _m11_experiment_map (tracker_id, experiment_id) SELECT 'M11A-P004::M11A-P004-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M11A-P005-E001',
    'Module 11B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M11B-O005"], "source_experiment_tracker_id": "M11A-P005-E001", "source_paper_tracker_id": "M11A-P005", "tracker_key": "M11A-P005::M11A-P005-E001"}'
  FROM _m11_paper_map p
  JOIN _m11_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M11A-P005'
  RETURNING experiment_id
)
INSERT INTO _m11_experiment_map (tracker_id, experiment_id) SELECT 'M11A-P005::M11A-P005-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M11A-P006-E001',
    'Module 11B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M11B-O006"], "source_experiment_tracker_id": "M11A-P006-E001", "source_paper_tracker_id": "M11A-P006", "tracker_key": "M11A-P006::M11A-P006-E001"}'
  FROM _m11_paper_map p
  JOIN _m11_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M11A-P006'
  RETURNING experiment_id
)
INSERT INTO _m11_experiment_map (tracker_id, experiment_id) SELECT 'M11A-P006::M11A-P006-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M11A-P007-E001',
    'Module 11B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M11B-O007"], "source_experiment_tracker_id": "M11A-P007-E001", "source_paper_tracker_id": "M11A-P007", "tracker_key": "M11A-P007::M11A-P007-E001"}'
  FROM _m11_paper_map p
  JOIN _m11_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M11A-P007'
  RETURNING experiment_id
)
INSERT INTO _m11_experiment_map (tracker_id, experiment_id) SELECT 'M11A-P007::M11A-P007-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M11A-P008-E001',
    'Module 11B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M11B-O008"], "source_experiment_tracker_id": "M11A-P008-E001", "source_paper_tracker_id": "M11A-P008", "tracker_key": "M11A-P008::M11A-P008-E001"}'
  FROM _m11_paper_map p
  JOIN _m11_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M11A-P008'
  RETURNING experiment_id
)
INSERT INTO _m11_experiment_map (tracker_id, experiment_id) SELECT 'M11A-P008::M11A-P008-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M11A-P009-E001',
    'Module 11B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M11B-O009"], "source_experiment_tracker_id": "M11A-P009-E001", "source_paper_tracker_id": "M11A-P009", "tracker_key": "M11A-P009::M11A-P009-E001"}'
  FROM _m11_paper_map p
  JOIN _m11_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M11A-P009'
  RETURNING experiment_id
)
INSERT INTO _m11_experiment_map (tracker_id, experiment_id) SELECT 'M11A-P009::M11A-P009-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M11A-P010-E001',
    'Module 11B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M11B-O010"], "source_experiment_tracker_id": "M11A-P010-E001", "source_paper_tracker_id": "M11A-P010", "tracker_key": "M11A-P010::M11A-P010-E001"}'
  FROM _m11_paper_map p
  JOIN _m11_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M11A-P010'
  RETURNING experiment_id
)
INSERT INTO _m11_experiment_map (tracker_id, experiment_id) SELECT 'M11A-P010::M11A-P010-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M11A-P011-E001',
    'Module 11B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M11B-O011"], "source_experiment_tracker_id": "M11A-P011-E001", "source_paper_tracker_id": "M11A-P011", "tracker_key": "M11A-P011::M11A-P011-E001"}'
  FROM _m11_paper_map p
  JOIN _m11_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M11A-P011'
  RETURNING experiment_id
)
INSERT INTO _m11_experiment_map (tracker_id, experiment_id) SELECT 'M11A-P011::M11A-P011-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M11A-P012-E001',
    'Module 11B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M11B-O012"], "source_experiment_tracker_id": "M11A-P012-E001", "source_paper_tracker_id": "M11A-P012", "tracker_key": "M11A-P012::M11A-P012-E001"}'
  FROM _m11_paper_map p
  JOIN _m11_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M11A-P012'
  RETURNING experiment_id
)
INSERT INTO _m11_experiment_map (tracker_id, experiment_id) SELECT 'M11A-P012::M11A-P012-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M11A-P013-E001',
    'Module 11B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M11B-O013"], "source_experiment_tracker_id": "M11A-P013-E001", "source_paper_tracker_id": "M11A-P013", "tracker_key": "M11A-P013::M11A-P013-E001"}'
  FROM _m11_paper_map p
  JOIN _m11_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M11A-P013'
  RETURNING experiment_id
)
INSERT INTO _m11_experiment_map (tracker_id, experiment_id) SELECT 'M11A-P013::M11A-P013-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M11A-P014-E001',
    'Module 11B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M11B-O014"], "source_experiment_tracker_id": "M11A-P014-E001", "source_paper_tracker_id": "M11A-P014", "tracker_key": "M11A-P014::M11A-P014-E001"}'
  FROM _m11_paper_map p
  JOIN _m11_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M11A-P014'
  RETURNING experiment_id
)
INSERT INTO _m11_experiment_map (tracker_id, experiment_id) SELECT 'M11A-P014::M11A-P014-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M11A-P015-E001',
    'Module 11B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M11B-O015"], "source_experiment_tracker_id": "M11A-P015-E001", "source_paper_tracker_id": "M11A-P015", "tracker_key": "M11A-P015::M11A-P015-E001"}'
  FROM _m11_paper_map p
  JOIN _m11_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M11A-P015'
  RETURNING experiment_id
)
INSERT INTO _m11_experiment_map (tracker_id, experiment_id) SELECT 'M11A-P015::M11A-P015-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M11A-P016-E001',
    'Module 11B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M11B-O016"], "source_experiment_tracker_id": "M11A-P016-E001", "source_paper_tracker_id": "M11A-P016", "tracker_key": "M11A-P016::M11A-P016-E001"}'
  FROM _m11_paper_map p
  JOIN _m11_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M11A-P016'
  RETURNING experiment_id
)
INSERT INTO _m11_experiment_map (tracker_id, experiment_id) SELECT 'M11A-P016::M11A-P016-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M11A-P017-E001',
    'Module 11B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M11B-O017"], "source_experiment_tracker_id": "M11A-P017-E001", "source_paper_tracker_id": "M11A-P017", "tracker_key": "M11A-P017::M11A-P017-E001"}'
  FROM _m11_paper_map p
  JOIN _m11_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M11A-P017'
  RETURNING experiment_id
)
INSERT INTO _m11_experiment_map (tracker_id, experiment_id) SELECT 'M11A-P017::M11A-P017-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M11A-P018-E001',
    'Module 11B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M11B-O018"], "source_experiment_tracker_id": "M11A-P018-E001", "source_paper_tracker_id": "M11A-P018", "tracker_key": "M11A-P018::M11A-P018-E001"}'
  FROM _m11_paper_map p
  JOIN _m11_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M11A-P018'
  RETURNING experiment_id
)
INSERT INTO _m11_experiment_map (tracker_id, experiment_id) SELECT 'M11A-P018::M11A-P018-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M11A-P019-E001',
    'Module 11B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M11B-O019"], "source_experiment_tracker_id": "M11A-P019-E001", "source_paper_tracker_id": "M11A-P019", "tracker_key": "M11A-P019::M11A-P019-E001"}'
  FROM _m11_paper_map p
  JOIN _m11_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M11A-P019'
  RETURNING experiment_id
)
INSERT INTO _m11_experiment_map (tracker_id, experiment_id) SELECT 'M11A-P019::M11A-P019-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M11A-P020-E001',
    'Module 11B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M11B-O020"], "source_experiment_tracker_id": "M11A-P020-E001", "source_paper_tracker_id": "M11A-P020", "tracker_key": "M11A-P020::M11A-P020-E001"}'
  FROM _m11_paper_map p
  JOIN _m11_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M11A-P020'
  RETURNING experiment_id
)
INSERT INTO _m11_experiment_map (tracker_id, experiment_id) SELECT 'M11A-P020::M11A-P020-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M11A-P021-E001',
    'Module 11B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M11B-O021"], "source_experiment_tracker_id": "M11A-P021-E001", "source_paper_tracker_id": "M11A-P021", "tracker_key": "M11A-P021::M11A-P021-E001"}'
  FROM _m11_paper_map p
  JOIN _m11_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M11A-P021'
  RETURNING experiment_id
)
INSERT INTO _m11_experiment_map (tracker_id, experiment_id) SELECT 'M11A-P021::M11A-P021-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M11A-P022-E001',
    'Module 11B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M11B-O022"], "source_experiment_tracker_id": "M11A-P022-E001", "source_paper_tracker_id": "M11A-P022", "tracker_key": "M11A-P022::M11A-P022-E001"}'
  FROM _m11_paper_map p
  JOIN _m11_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M11A-P022'
  RETURNING experiment_id
)
INSERT INTO _m11_experiment_map (tracker_id, experiment_id) SELECT 'M11A-P022::M11A-P022-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M11A-P023-E001',
    'Module 11B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M11B-O023"], "source_experiment_tracker_id": "M11A-P023-E001", "source_paper_tracker_id": "M11A-P023", "tracker_key": "M11A-P023::M11A-P023-E001"}'
  FROM _m11_paper_map p
  JOIN _m11_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M11A-P023'
  RETURNING experiment_id
)
INSERT INTO _m11_experiment_map (tracker_id, experiment_id) SELECT 'M11A-P023::M11A-P023-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M11A-P024-E001',
    'Module 11B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M11B-O024"], "source_experiment_tracker_id": "M11A-P024-E001", "source_paper_tracker_id": "M11A-P024", "tracker_key": "M11A-P024::M11A-P024-E001"}'
  FROM _m11_paper_map p
  JOIN _m11_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M11A-P024'
  RETURNING experiment_id
)
INSERT INTO _m11_experiment_map (tracker_id, experiment_id) SELECT 'M11A-P024::M11A-P024-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M11A-P025-E001',
    'Module 11B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M11B-O025"], "source_experiment_tracker_id": "M11A-P025-E001", "source_paper_tracker_id": "M11A-P025", "tracker_key": "M11A-P025::M11A-P025-E001"}'
  FROM _m11_paper_map p
  JOIN _m11_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M11A-P025'
  RETURNING experiment_id
)
INSERT INTO _m11_experiment_map (tracker_id, experiment_id) SELECT 'M11A-P025::M11A-P025-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M11A-P026-E001',
    'Module 11B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M11B-O026"], "source_experiment_tracker_id": "M11A-P026-E001", "source_paper_tracker_id": "M11A-P026", "tracker_key": "M11A-P026::M11A-P026-E001"}'
  FROM _m11_paper_map p
  JOIN _m11_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M11A-P026'
  RETURNING experiment_id
)
INSERT INTO _m11_experiment_map (tracker_id, experiment_id) SELECT 'M11A-P026::M11A-P026-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M11A-P027-E001',
    'Module 11B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M11B-O027"], "source_experiment_tracker_id": "M11A-P027-E001", "source_paper_tracker_id": "M11A-P027", "tracker_key": "M11A-P027::M11A-P027-E001"}'
  FROM _m11_paper_map p
  JOIN _m11_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M11A-P027'
  RETURNING experiment_id
)
INSERT INTO _m11_experiment_map (tracker_id, experiment_id) SELECT 'M11A-P027::M11A-P027-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M11A-P028-E001',
    'Module 11B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M11B-O028"], "source_experiment_tracker_id": "M11A-P028-E001", "source_paper_tracker_id": "M11A-P028", "tracker_key": "M11A-P028::M11A-P028-E001"}'
  FROM _m11_paper_map p
  JOIN _m11_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M11A-P028'
  RETURNING experiment_id
)
INSERT INTO _m11_experiment_map (tracker_id, experiment_id) SELECT 'M11A-P028::M11A-P028-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M11A-P029-E001',
    'Module 11B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M11B-O029"], "source_experiment_tracker_id": "M11A-P029-E001", "source_paper_tracker_id": "M11A-P029", "tracker_key": "M11A-P029::M11A-P029-E001"}'
  FROM _m11_paper_map p
  JOIN _m11_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M11A-P029'
  RETURNING experiment_id
)
INSERT INTO _m11_experiment_map (tracker_id, experiment_id) SELECT 'M11A-P029::M11A-P029-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M11A-P030-E001',
    'Module 11B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M11B-O030"], "source_experiment_tracker_id": "M11A-P030-E001", "source_paper_tracker_id": "M11A-P030", "tracker_key": "M11A-P030::M11A-P030-E001"}'
  FROM _m11_paper_map p
  JOIN _m11_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M11A-P030'
  RETURNING experiment_id
)
INSERT INTO _m11_experiment_map (tracker_id, experiment_id) SELECT 'M11A-P030::M11A-P030-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M11A-P031-E001',
    'Module 11B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M11B-O031"], "source_experiment_tracker_id": "M11A-P031-E001", "source_paper_tracker_id": "M11A-P031", "tracker_key": "M11A-P031::M11A-P031-E001"}'
  FROM _m11_paper_map p
  JOIN _m11_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M11A-P031'
  RETURNING experiment_id
)
INSERT INTO _m11_experiment_map (tracker_id, experiment_id) SELECT 'M11A-P031::M11A-P031-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M11A-P032-E001',
    'Module 11B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M11B-O032"], "source_experiment_tracker_id": "M11A-P032-E001", "source_paper_tracker_id": "M11A-P032", "tracker_key": "M11A-P032::M11A-P032-E001"}'
  FROM _m11_paper_map p
  JOIN _m11_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M11A-P032'
  RETURNING experiment_id
)
INSERT INTO _m11_experiment_map (tracker_id, experiment_id) SELECT 'M11A-P032::M11A-P032-E001', experiment_id FROM inserted;

INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Animal spinal ischemia evidence', 'Module 11B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Clinical perioperative evidence', 'Module 11B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Map/review evidence', 'Module 11B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;

INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('CSF catheter/drainage plus evoked-potential monitoring', 'Module 11B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('CSF drainage', 'Module 11B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('CSF drainage plus naloxone', 'Module 11B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('CSF drainage, intrathecal papaverine, neurologic deficit outcomes', 'Module 11B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Collateral artery remodeling after segmental artery occlusion', 'Module 11B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Collateral perfusion and ischemia-reperfusion protection', 'Module 11B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Darbepoetin-alpha versus methylprednisolone', 'Module 11B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Direct ischemic preconditioning versus kidney/limb remote preconditioning', 'Module 11B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Distal perfusion, sequential clamping, hypothermia, evoked potentials, CSF drainage, naloxone, methylprednisolone', 'Module 11B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Early reperfusion postconditioning', 'Module 11B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Epidural perfusion cooling/deep spinal hypothermia', 'Module 11B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Hypothermia, MAP/hemoglobin targets, mannitol, methylprednisolone, naloxone, rescue protocols', 'Module 11B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('IGF-1 plus erythropoietin after reperfusion', 'Module 11B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('IPC plus ischemic postconditioning', 'Module 11B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Intercostal reconstruction, hypothermic bypass, hypotension-risk management', 'Module 11B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Intrathecal papaverine plus CSF drainage', 'Module 11B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Isoflurane delayed preconditioning', 'Module 11B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Local ischemic preconditioning', 'Module 11B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('MISACE segmental artery coil embolization preconditioning', 'Module 11B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Multimodality protection: distal perfusion, CSF drainage, segmental reattachment, MAP targets', 'Module 11B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Naloxone infusion plus CSF drainage', 'Module 11B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Obstructive sleep apnea as remote ischemic preconditioning analog', 'Module 11B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Open/endovascular/hybrid staged repair', 'Module 11B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Paraspinal NIRS plus CSF drainage/perfusion monitoring', 'Module 11B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Planned staged repair/collateral-network conditioning', 'Module 11B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Prophylactic versus therapeutic CSF drainage', 'Module 11B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Prophylactic/selective CSF drainage safety', 'Module 11B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Randomized prophylactic versus selective/therapeutic CSF drain protocol', 'Module 11B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Sevoflurane anesthetic preconditioning', 'Module 11B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Staged endovascular repair/collateral conditioning', 'Module 11B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Staged repair, perfusion branches, delayed bridging, open branch, MISACE', 'Module 11B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Upper-arm remote ischemic conditioning', 'Module 11B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Cerebrospinal fluid drainage for thoracic and thoracoabdominal aortic aneurysm surgery tested or summarized CSF drainage in Human TAA/TAAA surgery evidence review; first-pass note: Cochrane review; 3 RCTs, 287 participants; limited but supportive evidence with boundary conditions.',
    'qualitative',
    NULL,
    'Cerebrospinal fluid drainage for thoracic and thoracoabdominal aortic aneurysm surgery tested or summarized CSF drainage in Human TAA/TAAA surgery evidence review; first-pass note: Cochrane review; 3 RCTs, 287 participants; limited but supportive evidence with boundary conditions.',
    'csf drainage',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Preserve ischemic-conditioning/protection boundary; full-text extraction queued.", "experiment_tracker_id": "M11A-P001-E001", "measurement_method_inference": null, "paper_tracker_id": "M11A-P001", "quantitative": "YES", "statistics_reported": "Cochrane review; 3 RCTs, 287 participants; limited but supportive evidence with boundary conditions.", "topic_id": "M11B-T001", "tracker_id": "M11B-O001"}'
  FROM _m11_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M11A-P001::M11A-P001-E001'
    AND et.evidence_type_name = 'Clinical perioperative evidence'
    AND ot.outcome_type_name = 'CSF drainage'
  RETURNING observation_id
)
INSERT INTO _m11_observation_map (tracker_id, observation_id) SELECT 'M11B-O001', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Prospective randomized pilot trial comparing prophylactic and therapeutic cerebrospinal fluid drainage during complex endovascular thoracoabdominal aortic aneurysm repair tested or summarized Prophylactic versus therapeutic CSF drainage in Human FBEVAR/TAAA randomized pilot; first-pass note: 20-patient randomized feasibility trial; one SCI event and one drain-related epidural hematoma.',
    'qualitative',
    NULL,
    'Prospective randomized pilot trial comparing prophylactic and therapeutic cerebrospinal fluid drainage during complex endovascular thoracoabdominal aortic aneurysm repair tested or summarized Prophylactic versus therapeutic CSF drainage in Human FBEVAR/TAAA randomized pilot; first-pass note: 20-patient randomized feasibility trial; one SCI event and one drain-related epidural hematoma.',
    'prophylactic versus therapeutic csf drainage',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Preserve ischemic-conditioning/protection boundary; full-text extraction queued.", "experiment_tracker_id": "M11A-P002-E001", "measurement_method_inference": null, "paper_tracker_id": "M11A-P002", "quantitative": "YES", "statistics_reported": "20-patient randomized feasibility trial; one SCI event and one drain-related epidural hematoma.", "topic_id": "M11B-T002", "tracker_id": "M11B-O002"}'
  FROM _m11_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M11A-P002::M11A-P002-E001'
    AND et.evidence_type_name = 'Clinical perioperative evidence'
    AND ot.outcome_type_name = 'Prophylactic versus therapeutic CSF drainage'
  RETURNING observation_id
)
INSERT INTO _m11_observation_map (tracker_id, observation_id) SELECT 'M11B-O002', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Current strategies of spinal cord protection during thoracoabdominal aortic surgery tested or summarized Multimodality protection: distal perfusion, CSF drainage, segmental reattachment, MAP targets in Human TAAA operative strategy review; first-pass note: Emphasizes no single protective measure and recommends multimodal protection.',
    'qualitative',
    NULL,
    'Current strategies of spinal cord protection during thoracoabdominal aortic surgery tested or summarized Multimodality protection: distal perfusion, CSF drainage, segmental reattachment, MAP targets in Human TAAA operative strategy review; first-pass note: Emphasizes no single protective measure and recommends multimodal protection.',
    'multimodality protection: distal perfusion, csf drainage, segmental reattachment, map targets',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Preserve ischemic-conditioning/protection boundary; full-text extraction queued.", "experiment_tracker_id": "M11A-P003-E001", "measurement_method_inference": null, "paper_tracker_id": "M11A-P003", "quantitative": "NO", "statistics_reported": "Source-page mechanistic or protocol row; exact statistics not extracted", "topic_id": "M11B-T003", "tracker_id": "M11B-O003"}'
  FROM _m11_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M11A-P003::M11A-P003-E001'
    AND et.evidence_type_name = 'Clinical perioperative evidence'
    AND ot.outcome_type_name = 'Multimodality protection: distal perfusion, CSF drainage, segmental reattachment, MAP targets'
  RETURNING observation_id
)
INSERT INTO _m11_observation_map (tracker_id, observation_id) SELECT 'M11B-O003', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Spinal cord protection for thoracoabdominal aortic aneurysm repair: from bench to bedside tested or summarized Collateral perfusion and ischemia-reperfusion protection in Bench-to-bedside TAAA review; first-pass note: Review of anatomy, mechanisms, laboratory and clinical protective strategies.',
    'qualitative',
    NULL,
    'Spinal cord protection for thoracoabdominal aortic aneurysm repair: from bench to bedside tested or summarized Collateral perfusion and ischemia-reperfusion protection in Bench-to-bedside TAAA review; first-pass note: Review of anatomy, mechanisms, laboratory and clinical protective strategies.',
    'collateral perfusion and ischemia-reperfusion protection',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Preserve ischemic-conditioning/protection boundary; full-text extraction queued.", "experiment_tracker_id": "M11A-P004-E001", "measurement_method_inference": null, "paper_tracker_id": "M11A-P004", "quantitative": "NO", "statistics_reported": "Source-page mechanistic or protocol row; exact statistics not extracted", "topic_id": "M11B-T004", "tracker_id": "M11B-O004"}'
  FROM _m11_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M11A-P004::M11A-P004-E001'
    AND et.evidence_type_name = 'Map/review evidence'
    AND ot.outcome_type_name = 'Collateral perfusion and ischemia-reperfusion protection'
  RETURNING observation_id
)
INSERT INTO _m11_observation_map (tracker_id, observation_id) SELECT 'M11B-O004', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Staging Endovascular Thoracic and Thoracoabdominal Aortic Aneurysm Repairs and the Risk of Post-operative Spinal Cord Ischemia tested or summarized Staged endovascular repair/collateral conditioning in Human VQI endovascular aortic repair cohort; first-pass note: 1421 VQI cases; staged repair not independently associated with lower SCI after adjustment; trend toward less permanent SCI among SCI cases.',
    'qualitative',
    NULL,
    'Staging Endovascular Thoracic and Thoracoabdominal Aortic Aneurysm Repairs and the Risk of Post-operative Spinal Cord Ischemia tested or summarized Staged endovascular repair/collateral conditioning in Human VQI endovascular aortic repair cohort; first-pass note: 1421 VQI cases; staged repair not independently associated with lower SCI after adjustment; trend toward less permanent SCI among SCI cases.',
    'staged endovascular repair/collateral conditioning',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Preserve ischemic-conditioning/protection boundary; full-text extraction queued.", "experiment_tracker_id": "M11A-P005-E001", "measurement_method_inference": null, "paper_tracker_id": "M11A-P005", "quantitative": "YES", "statistics_reported": "1421 VQI cases; staged repair not independently associated with lower SCI after adjustment; trend toward less permanent SCI among SCI cases.", "topic_id": "M11B-T005", "tracker_id": "M11B-O005"}'
  FROM _m11_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M11A-P005::M11A-P005-E001'
    AND et.evidence_type_name = 'Clinical perioperative evidence'
    AND ot.outcome_type_name = 'Staged endovascular repair/collateral conditioning'
  RETURNING observation_id
)
INSERT INTO _m11_observation_map (tracker_id, observation_id) SELECT 'M11B-O005', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Staged procedures for prevention of spinal cord ischemia in endovascular aortic surgery tested or summarized Staged repair, perfusion branches, delayed bridging, open branch, MISACE in Human endovascular aortic surgery review; first-pass note: Review of staging methods to reinforce collateral spinal perfusion.',
    'qualitative',
    NULL,
    'Staged procedures for prevention of spinal cord ischemia in endovascular aortic surgery tested or summarized Staged repair, perfusion branches, delayed bridging, open branch, MISACE in Human endovascular aortic surgery review; first-pass note: Review of staging methods to reinforce collateral spinal perfusion.',
    'staged repair, perfusion branches, delayed bridging, open branch, misace',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Preserve ischemic-conditioning/protection boundary; full-text extraction queued.", "experiment_tracker_id": "M11A-P006-E001", "measurement_method_inference": null, "paper_tracker_id": "M11A-P006", "quantitative": "NO", "statistics_reported": "Source-page mechanistic or protocol row; exact statistics not extracted", "topic_id": "M11B-T006", "tracker_id": "M11B-O006"}'
  FROM _m11_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M11A-P006::M11A-P006-E001'
    AND et.evidence_type_name = 'Clinical perioperative evidence'
    AND ot.outcome_type_name = 'Staged repair, perfusion branches, delayed bridging, open branch, MISACE'
  RETURNING observation_id
)
INSERT INTO _m11_observation_map (tracker_id, observation_id) SELECT 'M11B-O006', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Open, closed or a bit of both: a systematic review and meta-analysis of staged thoraco-abdominal aortic aneurysm repair tested or summarized Open/endovascular/hybrid staged repair in Human staged TAAA systematic review/meta-analysis; first-pass note: 20 studies, 924 patients; SCI differed by approach while all used drainage/monitoring/staging components.',
    'qualitative',
    NULL,
    'Open, closed or a bit of both: a systematic review and meta-analysis of staged thoraco-abdominal aortic aneurysm repair tested or summarized Open/endovascular/hybrid staged repair in Human staged TAAA systematic review/meta-analysis; first-pass note: 20 studies, 924 patients; SCI differed by approach while all used drainage/monitoring/staging components.',
    'open/endovascular/hybrid staged repair',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Preserve ischemic-conditioning/protection boundary; full-text extraction queued.", "experiment_tracker_id": "M11A-P007-E001", "measurement_method_inference": null, "paper_tracker_id": "M11A-P007", "quantitative": "YES", "statistics_reported": "20 studies, 924 patients; SCI differed by approach while all used drainage/monitoring/staging components.", "topic_id": "M11B-T007", "tracker_id": "M11B-O007"}'
  FROM _m11_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M11A-P007::M11A-P007-E001'
    AND et.evidence_type_name = 'Clinical perioperative evidence'
    AND ot.outcome_type_name = 'Open/endovascular/hybrid staged repair'
  RETURNING observation_id
)
INSERT INTO _m11_observation_map (tracker_id, observation_id) SELECT 'M11B-O007', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Planned Staged Repair of Thoracoabdominal Aortic Aneurysms to Minimize Spinal Cord Injury: A Proof of Concept tested or summarized Planned staged repair/collateral-network conditioning in Human TAAA staged repair proof-of-concept; first-pass note: Proof-of-concept for planned staging to reduce spinal cord injury risk.',
    'qualitative',
    NULL,
    'Planned Staged Repair of Thoracoabdominal Aortic Aneurysms to Minimize Spinal Cord Injury: A Proof of Concept tested or summarized Planned staged repair/collateral-network conditioning in Human TAAA staged repair proof-of-concept; first-pass note: Proof-of-concept for planned staging to reduce spinal cord injury risk.',
    'planned staged repair/collateral-network conditioning',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Preserve ischemic-conditioning/protection boundary; full-text extraction queued.", "experiment_tracker_id": "M11A-P008-E001", "measurement_method_inference": null, "paper_tracker_id": "M11A-P008", "quantitative": "NO", "statistics_reported": "Source-page mechanistic or protocol row; exact statistics not extracted", "topic_id": "M11B-T008", "tracker_id": "M11B-O008"}'
  FROM _m11_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M11A-P008::M11A-P008-E001'
    AND et.evidence_type_name = 'Clinical perioperative evidence'
    AND ot.outcome_type_name = 'Planned staged repair/collateral-network conditioning'
  RETURNING observation_id
)
INSERT INTO _m11_observation_map (tracker_id, observation_id) SELECT 'M11B-O008', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Patterns of collateral arteries to the spinal cord after thoraco-abdominal aortic aneurysm repair tested or summarized Collateral artery remodeling after segmental artery occlusion in Human TAAR/TEVAR imaging cohort; first-pass note: 179 patients; postoperative collateral pathways assessed after AKA-segmental artery occlusion.',
    'qualitative',
    'MRI / imaging assay',
    'Patterns of collateral arteries to the spinal cord after thoraco-abdominal aortic aneurysm repair tested or summarized Collateral artery remodeling after segmental artery occlusion in Human TAAR/TEVAR imaging cohort; first-pass note: 179 patients; postoperative collateral pathways assessed after AKA-segmental artery occlusion.',
    'collateral artery remodeling after segmental artery occlusion',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Preserve ischemic-conditioning/protection boundary; full-text extraction queued.", "experiment_tracker_id": "M11A-P009-E001", "measurement_method_inference": "MRI / imaging assay", "paper_tracker_id": "M11A-P009", "quantitative": "YES", "statistics_reported": "179 patients; postoperative collateral pathways assessed after AKA-segmental artery occlusion.", "topic_id": "M11B-T001", "tracker_id": "M11B-O009"}'
  FROM _m11_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M11A-P009::M11A-P009-E001'
    AND et.evidence_type_name = 'Clinical perioperative evidence'
    AND ot.outcome_type_name = 'Collateral artery remodeling after segmental artery occlusion'
  RETURNING observation_id
)
INSERT INTO _m11_observation_map (tracker_id, observation_id) SELECT 'M11B-O009', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Comparison of the protective effects of direct ischemic preconditioning and remote ischemic preconditioning in a rabbit model of transient spinal cord ischemia tested or summarized Direct ischemic preconditioning versus kidney/limb remote preconditioning in Rabbit transient spinal cord ischemia; first-pass note: DIPC protected neurologic/histologic outcomes; kidney/limb RIPC did not; Akt2 signal implicated.',
    'qualitative',
    'immunostaining / histology / pathology',
    'Comparison of the protective effects of direct ischemic preconditioning and remote ischemic preconditioning in a rabbit model of transient spinal cord ischemia tested or summarized Direct ischemic preconditioning versus kidney/limb remote preconditioning in Rabbit transient spinal cord ischemia; first-pass note: DIPC protected neurologic/histologic outcomes; kidney/limb RIPC did not; Akt2 signal implicated.',
    'direct ischemic preconditioning versus kidney/limb remote preconditioning',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Preserve ischemic-conditioning/protection boundary; full-text extraction queued.", "experiment_tracker_id": "M11A-P010-E001", "measurement_method_inference": "immunostaining / histology / pathology", "paper_tracker_id": "M11A-P010", "quantitative": "NO", "statistics_reported": "Source-page mechanistic or protocol row; exact statistics not extracted", "topic_id": "M11B-T002", "tracker_id": "M11B-O010"}'
  FROM _m11_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M11A-P010::M11A-P010-E001'
    AND et.evidence_type_name = 'Animal spinal ischemia evidence'
    AND ot.outcome_type_name = 'Direct ischemic preconditioning versus kidney/limb remote preconditioning'
  RETURNING observation_id
)
INSERT INTO _m11_observation_map (tracker_id, observation_id) SELECT 'M11B-O010', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Ischaemic preconditioning of the spinal cord to prevent spinal cord ischaemia during endovascular repair of thoracoabdominal aortic aneurysm: first clinical experience tested or summarized MISACE segmental artery coil embolization preconditioning in Human endovascular TAAA repair; first-pass note: 57 patients underwent MISACE; 55 proceeded to endovascular repair; no 30-day SCI reported.',
    'qualitative',
    NULL,
    'Ischaemic preconditioning of the spinal cord to prevent spinal cord ischaemia during endovascular repair of thoracoabdominal aortic aneurysm: first clinical experience tested or summarized MISACE segmental artery coil embolization preconditioning in Human endovascular TAAA repair; first-pass note: 57 patients underwent MISACE; 55 proceeded to endovascular repair; no 30-day SCI reported.',
    'misace segmental artery coil embolization preconditioning',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Preserve ischemic-conditioning/protection boundary; full-text extraction queued.", "experiment_tracker_id": "M11A-P011-E001", "measurement_method_inference": null, "paper_tracker_id": "M11A-P011", "quantitative": "YES", "statistics_reported": "57 patients underwent MISACE; 55 proceeded to endovascular repair; no 30-day SCI reported.", "topic_id": "M11B-T003", "tracker_id": "M11B-O011"}'
  FROM _m11_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M11A-P011::M11A-P011-E001'
    AND et.evidence_type_name = 'Clinical perioperative evidence'
    AND ot.outcome_type_name = 'MISACE segmental artery coil embolization preconditioning'
  RETURNING observation_id
)
INSERT INTO _m11_observation_map (tracker_id, observation_id) SELECT 'M11B-O011', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Remote ischaemic preconditioning versus sham procedure for abdominal aortic aneurysm repair: an external feasibility randomized controlled trial tested or summarized Upper-arm remote ischemic conditioning in Human elective AAA repair feasibility RCT; first-pass note: 69 randomized; feasible and acceptable; not spinal-cord-specific and confounded by EVAR complexity.',
    'qualitative',
    NULL,
    'Remote ischaemic preconditioning versus sham procedure for abdominal aortic aneurysm repair: an external feasibility randomized controlled trial tested or summarized Upper-arm remote ischemic conditioning in Human elective AAA repair feasibility RCT; first-pass note: 69 randomized; feasible and acceptable; not spinal-cord-specific and confounded by EVAR complexity.',
    'upper-arm remote ischemic conditioning',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Preserve ischemic-conditioning/protection boundary; full-text extraction queued.", "experiment_tracker_id": "M11A-P012-E001", "measurement_method_inference": null, "paper_tracker_id": "M11A-P012", "quantitative": "NO", "statistics_reported": "Source-page mechanistic or protocol row; exact statistics not extracted", "topic_id": "M11B-T004", "tracker_id": "M11B-O012"}'
  FROM _m11_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M11A-P012::M11A-P012-E001'
    AND et.evidence_type_name = 'Clinical perioperative evidence'
    AND ot.outcome_type_name = 'Upper-arm remote ischemic conditioning'
  RETURNING observation_id
)
INSERT INTO _m11_observation_map (tracker_id, observation_id) SELECT 'M11B-O012', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Sevoflurane preconditioning induces rapid ischemic tolerance against spinal cord ischemia/reperfusion through activation of extracellular signal-regulated kinase in rabbits tested or summarized Sevoflurane anesthetic preconditioning in Rabbit infrarenal aortic occlusion spinal I/R; first-pass note: Sevoflurane improved neurologic/histologic outcomes; ERK blockade attenuated effect.',
    'qualitative',
    'immunostaining / histology / pathology',
    'Sevoflurane preconditioning induces rapid ischemic tolerance against spinal cord ischemia/reperfusion through activation of extracellular signal-regulated kinase in rabbits tested or summarized Sevoflurane anesthetic preconditioning in Rabbit infrarenal aortic occlusion spinal I/R; first-pass note: Sevoflurane improved neurologic/histologic outcomes; ERK blockade attenuated effect.',
    'sevoflurane anesthetic preconditioning',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Preserve ischemic-conditioning/protection boundary; full-text extraction queued.", "experiment_tracker_id": "M11A-P013-E001", "measurement_method_inference": "immunostaining / histology / pathology", "paper_tracker_id": "M11A-P013", "quantitative": "NO", "statistics_reported": "Source-page mechanistic or protocol row; exact statistics not extracted", "topic_id": "M11B-T005", "tracker_id": "M11B-O013"}'
  FROM _m11_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M11A-P013::M11A-P013-E001'
    AND et.evidence_type_name = 'Animal spinal ischemia evidence'
    AND ot.outcome_type_name = 'Sevoflurane anesthetic preconditioning'
  RETURNING observation_id
)
INSERT INTO _m11_observation_map (tracker_id, observation_id) SELECT 'M11B-O013', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Ischemic preconditioning protects against spinal cord ischemia-reperfusion injury in rabbits by attenuating blood spinal cord barrier disruption tested or summarized Local ischemic preconditioning in Rabbit abdominal aortic occlusion I/R; first-pass note: IPC improved Tarlov scores, reduced barrier permeability/edema, preserved ZO-1, reduced MMP-9/TNF-alpha.',
    'qualitative',
    'ELISA / cytokine protein assay; barrier / permeability / endothelial assay',
    'Ischemic preconditioning protects against spinal cord ischemia-reperfusion injury in rabbits by attenuating blood spinal cord barrier disruption tested or summarized Local ischemic preconditioning in Rabbit abdominal aortic occlusion I/R; first-pass note: IPC improved Tarlov scores, reduced barrier permeability/edema, preserved ZO-1, reduced MMP-9/TNF-alpha.',
    'local ischemic preconditioning',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Preserve ischemic-conditioning/protection boundary; full-text extraction queued.", "experiment_tracker_id": "M11A-P014-E001", "measurement_method_inference": "ELISA / cytokine protein assay; barrier / permeability / endothelial assay", "paper_tracker_id": "M11A-P014", "quantitative": "NO", "statistics_reported": "Source-page mechanistic or protocol row; exact statistics not extracted", "topic_id": "M11B-T006", "tracker_id": "M11B-O014"}'
  FROM _m11_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M11A-P014::M11A-P014-E001'
    AND et.evidence_type_name = 'Animal spinal ischemia evidence'
    AND ot.outcome_type_name = 'Local ischemic preconditioning'
  RETURNING observation_id
)
INSERT INTO _m11_observation_map (tracker_id, observation_id) SELECT 'M11B-O014', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Co-application of ischemic preconditioning and postconditioning provides additive neuroprotection against spinal cord ischemia in rabbits tested or summarized IPC plus ischemic postconditioning in Rabbit infrarenal aortic occlusion; first-pass note: Combined IPC/postconditioning improved Tarlov scores and preserved motor neurons/white matter.',
    'qualitative',
    NULL,
    'Co-application of ischemic preconditioning and postconditioning provides additive neuroprotection against spinal cord ischemia in rabbits tested or summarized IPC plus ischemic postconditioning in Rabbit infrarenal aortic occlusion; first-pass note: Combined IPC/postconditioning improved Tarlov scores and preserved motor neurons/white matter.',
    'ipc plus ischemic postconditioning',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Preserve ischemic-conditioning/protection boundary; full-text extraction queued.", "experiment_tracker_id": "M11A-P015-E001", "measurement_method_inference": null, "paper_tracker_id": "M11A-P015", "quantitative": "NO", "statistics_reported": "Source-page mechanistic or protocol row; exact statistics not extracted", "topic_id": "M11B-T007", "tracker_id": "M11B-O015"}'
  FROM _m11_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M11A-P015::M11A-P015-E001'
    AND et.evidence_type_name = 'Animal spinal ischemia evidence'
    AND ot.outcome_type_name = 'IPC plus ischemic postconditioning'
  RETURNING observation_id
)
INSERT INTO _m11_observation_map (tracker_id, observation_id) SELECT 'M11B-O015', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Postconditioning, a series of brief interruptions of early reperfusion, prevents neurologic injury after spinal cord ischemia tested or summarized Early reperfusion postconditioning in Rabbit transient spinal cord ischemia; first-pass note: 4-cycle postconditioning protected; benefit disappeared when delayed 10 minutes.',
    'qualitative',
    NULL,
    'Postconditioning, a series of brief interruptions of early reperfusion, prevents neurologic injury after spinal cord ischemia tested or summarized Early reperfusion postconditioning in Rabbit transient spinal cord ischemia; first-pass note: 4-cycle postconditioning protected; benefit disappeared when delayed 10 minutes.',
    'early reperfusion postconditioning',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Preserve ischemic-conditioning/protection boundary; full-text extraction queued.", "experiment_tracker_id": "M11A-P016-E001", "measurement_method_inference": null, "paper_tracker_id": "M11A-P016", "quantitative": "NO", "statistics_reported": "Source-page mechanistic or protocol row; exact statistics not extracted", "topic_id": "M11B-T008", "tracker_id": "M11B-O016"}'
  FROM _m11_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M11A-P016::M11A-P016-E001'
    AND et.evidence_type_name = 'Animal spinal ischemia evidence'
    AND ot.outcome_type_name = 'Early reperfusion postconditioning'
  RETURNING observation_id
)
INSERT INTO _m11_observation_map (tracker_id, observation_id) SELECT 'M11B-O016', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Isoflurane produces delayed preconditioning against spinal cord ischemic injury via release of free radicals in rabbits tested or summarized Isoflurane delayed preconditioning in Rabbit spinal ischemia; first-pass note: Delayed protection at 24-48 h; free-radical scavenger blocked benefit.',
    'qualitative',
    NULL,
    'Isoflurane produces delayed preconditioning against spinal cord ischemic injury via release of free radicals in rabbits tested or summarized Isoflurane delayed preconditioning in Rabbit spinal ischemia; first-pass note: Delayed protection at 24-48 h; free-radical scavenger blocked benefit.',
    'isoflurane delayed preconditioning',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Preserve ischemic-conditioning/protection boundary; full-text extraction queued.", "experiment_tracker_id": "M11A-P017-E001", "measurement_method_inference": null, "paper_tracker_id": "M11A-P017", "quantitative": "NO", "statistics_reported": "Source-page mechanistic or protocol row; exact statistics not extracted", "topic_id": "M11B-T001", "tracker_id": "M11B-O017"}'
  FROM _m11_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M11A-P017::M11A-P017-E001'
    AND et.evidence_type_name = 'Animal spinal ischemia evidence'
    AND ot.outcome_type_name = 'Isoflurane delayed preconditioning'
  RETURNING observation_id
)
INSERT INTO _m11_observation_map (tracker_id, observation_id) SELECT 'M11B-O017', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Epidural perfusion cooling protection against protracted spinal cord ischemia in rabbits tested or summarized Epidural perfusion cooling/deep spinal hypothermia in Rabbit aortic ligation model; first-pass note: Cold epidural perfusion protected even after prolonged ischemia relative to normothermia.',
    'qualitative',
    NULL,
    'Epidural perfusion cooling protection against protracted spinal cord ischemia in rabbits tested or summarized Epidural perfusion cooling/deep spinal hypothermia in Rabbit aortic ligation model; first-pass note: Cold epidural perfusion protected even after prolonged ischemia relative to normothermia.',
    'epidural perfusion cooling/deep spinal hypothermia',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Preserve ischemic-conditioning/protection boundary; full-text extraction queued.", "experiment_tracker_id": "M11A-P018-E001", "measurement_method_inference": null, "paper_tracker_id": "M11A-P018", "quantitative": "NO", "statistics_reported": "Source-page mechanistic or protocol row; exact statistics not extracted", "topic_id": "M11B-T002", "tracker_id": "M11B-O018"}'
  FROM _m11_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M11A-P018::M11A-P018-E001'
    AND et.evidence_type_name = 'Animal spinal ischemia evidence'
    AND ot.outcome_type_name = 'Epidural perfusion cooling/deep spinal hypothermia'
  RETURNING observation_id
)
INSERT INTO _m11_observation_map (tracker_id, observation_id) SELECT 'M11B-O018', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Appraisal of cerebrospinal fluid alterations during aortic surgery with intrathecal papaverine administration and cerebrospinal fluid drainage tested or summarized Intrathecal papaverine plus CSF drainage in Human aortic cross-clamping physiology; first-pass note: 11-patient physiologic study; CSF pressure rose with induction/cross-clamp and fell with drainage.',
    'qualitative',
    NULL,
    'Appraisal of cerebrospinal fluid alterations during aortic surgery with intrathecal papaverine administration and cerebrospinal fluid drainage tested or summarized Intrathecal papaverine plus CSF drainage in Human aortic cross-clamping physiology; first-pass note: 11-patient physiologic study; CSF pressure rose with induction/cross-clamp and fell with drainage.',
    'intrathecal papaverine plus csf drainage',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Preserve ischemic-conditioning/protection boundary; full-text extraction queued.", "experiment_tracker_id": "M11A-P019-E001", "measurement_method_inference": null, "paper_tracker_id": "M11A-P019", "quantitative": "YES", "statistics_reported": "11-patient physiologic study; CSF pressure rose with induction/cross-clamp and fell with drainage.", "topic_id": "M11B-T003", "tracker_id": "M11B-O019"}'
  FROM _m11_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M11A-P019::M11A-P019-E001'
    AND et.evidence_type_name = 'Clinical perioperative evidence'
    AND ot.outcome_type_name = 'Intrathecal papaverine plus CSF drainage'
  RETURNING observation_id
)
INSERT INTO _m11_observation_map (tracker_id, observation_id) SELECT 'M11B-O019', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Effects of darbepoetin-alpha in spinal cord ischemia-reperfusion injury in the rabbit tested or summarized Darbepoetin-alpha versus methylprednisolone in Rabbit aortic occlusion spinal I/R; first-pass note: Darbepoetin reduced oxidative/apoptotic markers and improved neurologic outcomes.',
    'qualitative',
    NULL,
    'Effects of darbepoetin-alpha in spinal cord ischemia-reperfusion injury in the rabbit tested or summarized Darbepoetin-alpha versus methylprednisolone in Rabbit aortic occlusion spinal I/R; first-pass note: Darbepoetin reduced oxidative/apoptotic markers and improved neurologic outcomes.',
    'darbepoetin-alpha versus methylprednisolone',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Preserve ischemic-conditioning/protection boundary; full-text extraction queued.", "experiment_tracker_id": "M11A-P020-E001", "measurement_method_inference": null, "paper_tracker_id": "M11A-P020", "quantitative": "NO", "statistics_reported": "Source-page mechanistic or protocol row; exact statistics not extracted", "topic_id": "M11B-T004", "tracker_id": "M11B-O020"}'
  FROM _m11_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M11A-P020::M11A-P020-E001'
    AND et.evidence_type_name = 'Animal spinal ischemia evidence'
    AND ot.outcome_type_name = 'Darbepoetin-alpha versus methylprednisolone'
  RETURNING observation_id
)
INSERT INTO _m11_observation_map (tracker_id, observation_id) SELECT 'M11B-O020', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Naloxone infusion and drainage of cerebrospinal fluid as adjuncts to postoperative care after repair of thoracoabdominal aneurysms tested or summarized Naloxone infusion plus CSF drainage in Human TAAA postoperative care review; first-pass note: Review frames paraplegia as multifactorial and supports combined adjunctive postoperative care.',
    'qualitative',
    NULL,
    'Naloxone infusion and drainage of cerebrospinal fluid as adjuncts to postoperative care after repair of thoracoabdominal aneurysms tested or summarized Naloxone infusion plus CSF drainage in Human TAAA postoperative care review; first-pass note: Review frames paraplegia as multifactorial and supports combined adjunctive postoperative care.',
    'naloxone infusion plus csf drainage',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Preserve ischemic-conditioning/protection boundary; full-text extraction queued.", "experiment_tracker_id": "M11A-P021-E001", "measurement_method_inference": null, "paper_tracker_id": "M11A-P021", "quantitative": "NO", "statistics_reported": "Source-page mechanistic or protocol row; exact statistics not extracted", "topic_id": "M11B-T005", "tracker_id": "M11B-O021"}'
  FROM _m11_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M11A-P021::M11A-P021-E001'
    AND et.evidence_type_name = 'Clinical perioperative evidence'
    AND ot.outcome_type_name = 'Naloxone infusion plus CSF drainage'
  RETURNING observation_id
)
INSERT INTO _m11_observation_map (tracker_id, observation_id) SELECT 'M11B-O021', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Strategy for spinal cord protection during thoracoabdominal aortic surgery tested or summarized Distal perfusion, sequential clamping, hypothermia, evoked potentials, CSF drainage, naloxone, methylprednisolone in Human TAAA strategy review; first-pass note: Japanese strategy paper; multimodal surgical protection bundle.',
    'qualitative',
    NULL,
    'Strategy for spinal cord protection during thoracoabdominal aortic surgery tested or summarized Distal perfusion, sequential clamping, hypothermia, evoked potentials, CSF drainage, naloxone, methylprednisolone in Human TAAA strategy review; first-pass note: Japanese strategy paper; multimodal surgical protection bundle.',
    'distal perfusion, sequential clamping, hypothermia, evoked potentials, csf drainage, naloxone, methylprednisolone',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Preserve ischemic-conditioning/protection boundary; full-text extraction queued.", "experiment_tracker_id": "M11A-P022-E001", "measurement_method_inference": null, "paper_tracker_id": "M11A-P022", "quantitative": "NO", "statistics_reported": "Source-page mechanistic or protocol row; exact statistics not extracted", "topic_id": "M11B-T006", "tracker_id": "M11B-O022"}'
  FROM _m11_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M11A-P022::M11A-P022-E001'
    AND et.evidence_type_name = 'Clinical perioperative evidence'
    AND ot.outcome_type_name = 'Distal perfusion, sequential clamping, hypothermia, evoked potentials, CSF drainage, naloxone, methylprednisolone'
  RETURNING observation_id
)
INSERT INTO _m11_observation_map (tracker_id, observation_id) SELECT 'M11B-O022', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'The combination of insulin-like growth factor 1 and erythropoietin protects against ischemic spinal cord injury in rabbits tested or summarized IGF-1 plus erythropoietin after reperfusion in Rabbit abdominal aortic occlusion; first-pass note: Combination treatment tested for post-ischemic neuroprotection and signaling activation.',
    'qualitative',
    NULL,
    'The combination of insulin-like growth factor 1 and erythropoietin protects against ischemic spinal cord injury in rabbits tested or summarized IGF-1 plus erythropoietin after reperfusion in Rabbit abdominal aortic occlusion; first-pass note: Combination treatment tested for post-ischemic neuroprotection and signaling activation.',
    'igf-1 plus erythropoietin after reperfusion',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Preserve ischemic-conditioning/protection boundary; full-text extraction queued.", "experiment_tracker_id": "M11A-P023-E001", "measurement_method_inference": null, "paper_tracker_id": "M11A-P023", "quantitative": "NO", "statistics_reported": "Source-page mechanistic or protocol row; exact statistics not extracted", "topic_id": "M11B-T007", "tracker_id": "M11B-O023"}'
  FROM _m11_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M11A-P023::M11A-P023-E001'
    AND et.evidence_type_name = 'Animal spinal ischemia evidence'
    AND ot.outcome_type_name = 'IGF-1 plus erythropoietin after reperfusion'
  RETURNING observation_id
)
INSERT INTO _m11_observation_map (tracker_id, observation_id) SELECT 'M11B-O023', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Combined use of cerebral spinal fluid drainage and naloxone reduces the risk of paraplegia in thoracoabdominal aneurysm repair tested or summarized CSF drainage plus naloxone in Human TAA/TAAA cohort; first-pass note: 110-patient cohort; 1 deficit with CSFD/naloxone versus 11 without, but nonrandomized/historical boundaries.',
    'qualitative',
    NULL,
    'Combined use of cerebral spinal fluid drainage and naloxone reduces the risk of paraplegia in thoracoabdominal aneurysm repair tested or summarized CSF drainage plus naloxone in Human TAA/TAAA cohort; first-pass note: 110-patient cohort; 1 deficit with CSFD/naloxone versus 11 without, but nonrandomized/historical boundaries.',
    'csf drainage plus naloxone',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Preserve ischemic-conditioning/protection boundary; full-text extraction queued.", "experiment_tracker_id": "M11A-P024-E001", "measurement_method_inference": null, "paper_tracker_id": "M11A-P024", "quantitative": "YES", "statistics_reported": "110-patient cohort; 1 deficit with CSFD/naloxone versus 11 without, but nonrandomized/historical boundaries.", "topic_id": "M11B-T008", "tracker_id": "M11B-O024"}'
  FROM _m11_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M11A-P024::M11A-P024-E001'
    AND et.evidence_type_name = 'Clinical perioperative evidence'
    AND ot.outcome_type_name = 'CSF drainage plus naloxone'
  RETURNING observation_id
)
INSERT INTO _m11_observation_map (tracker_id, observation_id) SELECT 'M11B-O024', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Intraoperative neuroprotective interventions prevent spinal cord ischemia and injury in thoracic endovascular aortic repair tested or summarized Hypothermia, MAP/hemoglobin targets, mannitol, methylprednisolone, naloxone, rescue protocols in Human TEVAR cohort; first-pass note: Aggressive intra/postoperative neuroprotective bundle in TEVAR; retrospective cohort boundary.',
    'qualitative',
    NULL,
    'Intraoperative neuroprotective interventions prevent spinal cord ischemia and injury in thoracic endovascular aortic repair tested or summarized Hypothermia, MAP/hemoglobin targets, mannitol, methylprednisolone, naloxone, rescue protocols in Human TEVAR cohort; first-pass note: Aggressive intra/postoperative neuroprotective bundle in TEVAR; retrospective cohort boundary.',
    'hypothermia, map/hemoglobin targets, mannitol, methylprednisolone, naloxone, rescue protocols',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Preserve ischemic-conditioning/protection boundary; full-text extraction queued.", "experiment_tracker_id": "M11A-P025-E001", "measurement_method_inference": null, "paper_tracker_id": "M11A-P025", "quantitative": "YES", "statistics_reported": "Aggressive intra/postoperative neuroprotective bundle in TEVAR; retrospective cohort boundary.", "topic_id": "M11B-T001", "tracker_id": "M11B-O025"}'
  FROM _m11_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M11A-P025::M11A-P025-E001'
    AND et.evidence_type_name = 'Clinical perioperative evidence'
    AND ot.outcome_type_name = 'Hypothermia, MAP/hemoglobin targets, mannitol, methylprednisolone, naloxone, rescue protocols'
  RETURNING observation_id
)
INSERT INTO _m11_observation_map (tracker_id, observation_id) SELECT 'M11B-O025', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Benefits and Risks of Prophylactic Cerebrospinal Fluid Catheter and Evoked Potential Monitoring in Symptomatic Spinal Cord Ischemia Low-Risk Thoracic Endovascular Aortic Repair tested or summarized CSF catheter/drainage plus evoked-potential monitoring in Human low-risk TEVAR cohort; first-pass note: 223 procedures; CSF drainage associated with lower symptomatic SCI; EP monitoring detected acute inflow problems.',
    'qualitative',
    NULL,
    'Benefits and Risks of Prophylactic Cerebrospinal Fluid Catheter and Evoked Potential Monitoring in Symptomatic Spinal Cord Ischemia Low-Risk Thoracic Endovascular Aortic Repair tested or summarized CSF catheter/drainage plus evoked-potential monitoring in Human low-risk TEVAR cohort; first-pass note: 223 procedures; CSF drainage associated with lower symptomatic SCI; EP monitoring detected acute inflow problems.',
    'csf catheter/drainage plus evoked-potential monitoring',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Preserve ischemic-conditioning/protection boundary; full-text extraction queued.", "experiment_tracker_id": "M11A-P026-E001", "measurement_method_inference": null, "paper_tracker_id": "M11A-P026", "quantitative": "YES", "statistics_reported": "223 procedures; CSF drainage associated with lower symptomatic SCI; EP monitoring detected acute inflow problems.", "topic_id": "M11B-T002", "tracker_id": "M11B-O026"}'
  FROM _m11_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M11A-P026::M11A-P026-E001'
    AND et.evidence_type_name = 'Clinical perioperative evidence'
    AND ot.outcome_type_name = 'CSF catheter/drainage plus evoked-potential monitoring'
  RETURNING observation_id
)
INSERT INTO _m11_observation_map (tracker_id, observation_id) SELECT 'M11B-O026', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Safety of cerebrospinal fluid drainage for spinal cord ischemia prevention in thoracic endovascular aortic repair tested or summarized Prophylactic/selective CSF drainage safety in Human TEVAR safety cohort; first-pass note: 936 TEVAR procedures; 390 drains; assesses complication severity and timing.',
    'qualitative',
    NULL,
    'Safety of cerebrospinal fluid drainage for spinal cord ischemia prevention in thoracic endovascular aortic repair tested or summarized Prophylactic/selective CSF drainage safety in Human TEVAR safety cohort; first-pass note: 936 TEVAR procedures; 390 drains; assesses complication severity and timing.',
    'prophylactic/selective csf drainage safety',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Preserve ischemic-conditioning/protection boundary; full-text extraction queued.", "experiment_tracker_id": "M11A-P027-E001", "measurement_method_inference": null, "paper_tracker_id": "M11A-P027", "quantitative": "YES", "statistics_reported": "936 TEVAR procedures; 390 drains; assesses complication severity and timing.", "topic_id": "M11B-T003", "tracker_id": "M11B-O027"}'
  FROM _m11_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M11A-P027::M11A-P027-E001'
    AND et.evidence_type_name = 'Clinical perioperative evidence'
    AND ot.outcome_type_name = 'Prophylactic/selective CSF drainage safety'
  RETURNING observation_id
)
INSERT INTO _m11_observation_map (tracker_id, observation_id) SELECT 'M11B-O027', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Open reconstruction of thoracoabdominal aortic aneurysms tested or summarized Intercostal reconstruction, hypothermic bypass, hypotension-risk management in Human open TAAA reconstruction cohort; first-pass note: SCI occurred in 10.5%; risk factors included prior aortic surgery, diabetes, and post-bypass hypotension.',
    'qualitative',
    NULL,
    'Open reconstruction of thoracoabdominal aortic aneurysms tested or summarized Intercostal reconstruction, hypothermic bypass, hypotension-risk management in Human open TAAA reconstruction cohort; first-pass note: SCI occurred in 10.5%; risk factors included prior aortic surgery, diabetes, and post-bypass hypotension.',
    'intercostal reconstruction, hypothermic bypass, hypotension-risk management',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Preserve ischemic-conditioning/protection boundary; full-text extraction queued.", "experiment_tracker_id": "M11A-P028-E001", "measurement_method_inference": null, "paper_tracker_id": "M11A-P028", "quantitative": "NO", "statistics_reported": "Source-page mechanistic or protocol row; exact statistics not extracted", "topic_id": "M11B-T004", "tracker_id": "M11B-O028"}'
  FROM _m11_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M11A-P028::M11A-P028-E001'
    AND et.evidence_type_name = 'Clinical perioperative evidence'
    AND ot.outcome_type_name = 'Intercostal reconstruction, hypothermic bypass, hypotension-risk management'
  RETURNING observation_id
)
INSERT INTO _m11_observation_map (tracker_id, observation_id) SELECT 'M11B-O028', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Prophylactic vs Therapeutic Cerebrospinal Fluid Drain Placement During Endovascular Thoracoabdominal Aortic Aneurysm Repair tested or summarized Randomized prophylactic versus selective/therapeutic CSF drain protocol in Human high-risk endovascular TAAA trial; first-pass note: ClinicalTrials.gov source-page row; primary endpoint is SCI onset baseline to 1 year.',
    'qualitative',
    NULL,
    'Prophylactic vs Therapeutic Cerebrospinal Fluid Drain Placement During Endovascular Thoracoabdominal Aortic Aneurysm Repair tested or summarized Randomized prophylactic versus selective/therapeutic CSF drain protocol in Human high-risk endovascular TAAA trial; first-pass note: ClinicalTrials.gov source-page row; primary endpoint is SCI onset baseline to 1 year.',
    'randomized prophylactic versus selective/therapeutic csf drain protocol',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Preserve ischemic-conditioning/protection boundary; full-text extraction queued.", "experiment_tracker_id": "M11A-P029-E001", "measurement_method_inference": null, "paper_tracker_id": "M11A-P029", "quantitative": "YES", "statistics_reported": "ClinicalTrials.gov source-page row; primary endpoint is SCI onset baseline to 1 year.", "topic_id": "M11B-T005", "tracker_id": "M11B-O029"}'
  FROM _m11_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M11A-P029::M11A-P029-E001'
    AND et.evidence_type_name = 'Clinical perioperative evidence'
    AND ot.outcome_type_name = 'Randomized prophylactic versus selective/therapeutic CSF drain protocol'
  RETURNING observation_id
)
INSERT INTO _m11_observation_map (tracker_id, observation_id) SELECT 'M11B-O029', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'OSA as a Remote Ischemic Preconditioning in Vascular Surgery tested or summarized Obstructive sleep apnea as remote ischemic preconditioning analog in Human aorto-bifemoral bypass trial; first-pass note: Recruiting vascular-surgery trial; primary endpoints are I/R injury markers, not spinal cord-specific endpoints.',
    'qualitative',
    NULL,
    'OSA as a Remote Ischemic Preconditioning in Vascular Surgery tested or summarized Obstructive sleep apnea as remote ischemic preconditioning analog in Human aorto-bifemoral bypass trial; first-pass note: Recruiting vascular-surgery trial; primary endpoints are I/R injury markers, not spinal cord-specific endpoints.',
    'obstructive sleep apnea as remote ischemic preconditioning analog',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Preserve ischemic-conditioning/protection boundary; full-text extraction queued.", "experiment_tracker_id": "M11A-P030-E001", "measurement_method_inference": null, "paper_tracker_id": "M11A-P030", "quantitative": "YES", "statistics_reported": "Recruiting vascular-surgery trial; primary endpoints are I/R injury markers, not spinal cord-specific endpoints.", "topic_id": "M11B-T006", "tracker_id": "M11B-O030"}'
  FROM _m11_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M11A-P030::M11A-P030-E001'
    AND et.evidence_type_name = 'Clinical perioperative evidence'
    AND ot.outcome_type_name = 'Obstructive sleep apnea as remote ischemic preconditioning analog'
  RETURNING observation_id
)
INSERT INTO _m11_observation_map (tracker_id, observation_id) SELECT 'M11B-O030', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NIRS Monitoring of Spinal Cord Ischemia in Aortic Surgery tested or summarized Paraspinal NIRS plus CSF drainage/perfusion monitoring in Human aortic surgery observational trial; first-pass note: Observational monitoring/prevention trial; estimated completion 2027; endpoint boundary with neuromonitoring.',
    'qualitative',
    NULL,
    'NIRS Monitoring of Spinal Cord Ischemia in Aortic Surgery tested or summarized Paraspinal NIRS plus CSF drainage/perfusion monitoring in Human aortic surgery observational trial; first-pass note: Observational monitoring/prevention trial; estimated completion 2027; endpoint boundary with neuromonitoring.',
    'paraspinal nirs plus csf drainage/perfusion monitoring',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Preserve ischemic-conditioning/protection boundary; full-text extraction queued.", "experiment_tracker_id": "M11A-P031-E001", "measurement_method_inference": null, "paper_tracker_id": "M11A-P031", "quantitative": "YES", "statistics_reported": "Observational monitoring/prevention trial; estimated completion 2027; endpoint boundary with neuromonitoring.", "topic_id": "M11B-T007", "tracker_id": "M11B-O031"}'
  FROM _m11_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M11A-P031::M11A-P031-E001'
    AND et.evidence_type_name = 'Clinical perioperative evidence'
    AND ot.outcome_type_name = 'Paraspinal NIRS plus CSF drainage/perfusion monitoring'
  RETURNING observation_id
)
INSERT INTO _m11_observation_map (tracker_id, observation_id) SELECT 'M11B-O031', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Randomized trial anchors summarized in CSF-drainage reviews tested or summarized CSF drainage, intrathecal papaverine, neurologic deficit outcomes in Human type I/II TAAA randomized evidence; first-pass note: Composite anchor for the three RCTs because individual trial metadata should be expanded in full-text pass.',
    'qualitative',
    NULL,
    'Randomized trial anchors summarized in CSF-drainage reviews tested or summarized CSF drainage, intrathecal papaverine, neurologic deficit outcomes in Human type I/II TAAA randomized evidence; first-pass note: Composite anchor for the three RCTs because individual trial metadata should be expanded in full-text pass.',
    'csf drainage, intrathecal papaverine, neurologic deficit outcomes',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Preserve ischemic-conditioning/protection boundary; full-text extraction queued.", "experiment_tracker_id": "M11A-P032-E001", "measurement_method_inference": null, "paper_tracker_id": "M11A-P032", "quantitative": "YES", "statistics_reported": "Composite anchor for the three RCTs because individual trial metadata should be expanded in full-text pass.", "topic_id": "M11B-T008", "tracker_id": "M11B-O032"}'
  FROM _m11_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M11A-P032::M11A-P032-E001'
    AND et.evidence_type_name = 'Clinical perioperative evidence'
    AND ot.outcome_type_name = 'CSF drainage, intrathecal papaverine, neurologic deficit outcomes'
  RETURNING observation_id
)
INSERT INTO _m11_observation_map (tracker_id, observation_id) SELECT 'M11B-O032', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'CSF drainage/perfusion protocols are repeatedly used as spinal cord protection measures, but benefits must be balanced against drain complications and prophylactic-versus-therapeutic timing.',
    'synthesis',
    'medium',
    'Module 11A tracker / source-page metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for exact estimates and protocol details.", "source_paper_tracker_id": "M11A-P001", "topic_id": "M11B-T001", "tracker_id": "M11B-C001"}'
  FROM _m11_paper_map p
  WHERE p.tracker_id = 'M11A-P001'
  RETURNING claim_id
)
INSERT INTO _m11_claim_map (tracker_id, claim_id) SELECT 'M11B-C001', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Staged repair and collateral-network strategies are plausible conditioning approaches, but registry and meta-analysis data require approach-specific interpretation.',
    'synthesis',
    'medium',
    'Module 11A tracker / source-page metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for exact estimates and protocol details.", "source_paper_tracker_id": "M11A-P002", "topic_id": "M11B-T002", "tracker_id": "M11B-C002"}'
  FROM _m11_paper_map p
  WHERE p.tracker_id = 'M11A-P002'
  RETURNING claim_id
)
INSERT INTO _m11_claim_map (tracker_id, claim_id) SELECT 'M11B-C002', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Direct/local ischemic preconditioning and postconditioning show stronger spinal-cord-specific animal protection than remote conditioning.',
    'synthesis',
    'medium',
    'Module 11A tracker / source-page metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for exact estimates and protocol details.", "source_paper_tracker_id": "M11A-P003", "topic_id": "M11B-T003", "tracker_id": "M11B-C003"}'
  FROM _m11_paper_map p
  WHERE p.tracker_id = 'M11A-P003'
  RETURNING claim_id
)
INSERT INTO _m11_claim_map (tracker_id, claim_id) SELECT 'M11B-C003', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Remote ischemic conditioning evidence is not yet equivalent to direct spinal cord protection unless spinal cord endpoints are measured.',
    'boundary condition',
    'medium',
    'Module 11A tracker / source-page metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for exact estimates and protocol details.", "source_paper_tracker_id": "M11A-P004", "topic_id": "M11B-T004", "tracker_id": "M11B-C004"}'
  FROM _m11_paper_map p
  WHERE p.tracker_id = 'M11A-P004'
  RETURNING claim_id
)
INSERT INTO _m11_claim_map (tracker_id, claim_id) SELECT 'M11B-C004', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Anesthetic, hypothermic, and pharmacologic protection signals are model- and bundle-dependent and should not be assigned causal weight without timing and comparator details.',
    'boundary condition',
    'medium',
    'Module 11A tracker / source-page metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for exact estimates and protocol details.", "source_paper_tracker_id": "M11A-P005", "topic_id": "M11B-T005", "tracker_id": "M11B-C005"}'
  FROM _m11_paper_map p
  WHERE p.tracker_id = 'M11A-P005'
  RETURNING claim_id
)
INSERT INTO _m11_claim_map (tracker_id, claim_id) SELECT 'M11B-C005', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Neuromonitoring can guide rescue and risk detection but is not itself proof of protection unless linked to intervention and endpoint recovery.',
    'boundary condition',
    'medium',
    'Module 11A tracker / source-page metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for exact estimates and protocol details.", "source_paper_tracker_id": "M11A-P006", "topic_id": "M11B-T006", "tracker_id": "M11B-C006"}'
  FROM _m11_paper_map p
  WHERE p.tracker_id = 'M11A-P006'
  RETURNING claim_id
)
INSERT INTO _m11_claim_map (tracker_id, claim_id) SELECT 'M11B-C006', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Registry rows should remain protocol/status evidence until results are linked and endpoint definitions are extracted.',
    'boundary condition',
    'medium',
    'Module 11A tracker / source-page metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for exact estimates and protocol details.", "source_paper_tracker_id": "M11A-P007", "topic_id": "M11B-T007", "tracker_id": "M11B-C007"}'
  FROM _m11_paper_map p
  WHERE p.tracker_id = 'M11A-P007'
  RETURNING claim_id
)
INSERT INTO _m11_claim_map (tracker_id, claim_id) SELECT 'M11B-C007', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Perioperative ischemia prophylaxis is mechanistically adjacent to, but not interchangeable with, traumatic chronic SCI reconstruction.',
    'boundary condition',
    'medium',
    'Module 11A tracker / source-page metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for exact estimates and protocol details.", "source_paper_tracker_id": "M11A-P008", "topic_id": "M11B-T008", "tracker_id": "M11B-C008"}'
  FROM _m11_paper_map p
  WHERE p.tracker_id = 'M11A-P008'
  RETURNING claim_id
)
INSERT INTO _m11_claim_map (tracker_id, claim_id) SELECT 'M11B-C008', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'CSF drainage/perfusion protocols are repeatedly used as spinal cord protection measures, but benefits must be balanced against drain complications and prophylactic-versus-therapeutic timing.',
    'synthesis',
    'medium',
    'Module 11A tracker / source-page metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for exact estimates and protocol details.", "source_paper_tracker_id": "M11A-P009", "topic_id": "M11B-T001", "tracker_id": "M11B-C009"}'
  FROM _m11_paper_map p
  WHERE p.tracker_id = 'M11A-P009'
  RETURNING claim_id
)
INSERT INTO _m11_claim_map (tracker_id, claim_id) SELECT 'M11B-C009', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Staged repair and collateral-network strategies are plausible conditioning approaches, but registry and meta-analysis data require approach-specific interpretation.',
    'synthesis',
    'medium',
    'Module 11A tracker / source-page metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for exact estimates and protocol details.", "source_paper_tracker_id": "M11A-P010", "topic_id": "M11B-T002", "tracker_id": "M11B-C010"}'
  FROM _m11_paper_map p
  WHERE p.tracker_id = 'M11A-P010'
  RETURNING claim_id
)
INSERT INTO _m11_claim_map (tracker_id, claim_id) SELECT 'M11B-C010', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Direct/local ischemic preconditioning and postconditioning show stronger spinal-cord-specific animal protection than remote conditioning.',
    'synthesis',
    'medium',
    'Module 11A tracker / source-page metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for exact estimates and protocol details.", "source_paper_tracker_id": "M11A-P011", "topic_id": "M11B-T003", "tracker_id": "M11B-C011"}'
  FROM _m11_paper_map p
  WHERE p.tracker_id = 'M11A-P011'
  RETURNING claim_id
)
INSERT INTO _m11_claim_map (tracker_id, claim_id) SELECT 'M11B-C011', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Remote ischemic conditioning evidence is not yet equivalent to direct spinal cord protection unless spinal cord endpoints are measured.',
    'boundary condition',
    'medium',
    'Module 11A tracker / source-page metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for exact estimates and protocol details.", "source_paper_tracker_id": "M11A-P012", "topic_id": "M11B-T004", "tracker_id": "M11B-C012"}'
  FROM _m11_paper_map p
  WHERE p.tracker_id = 'M11A-P012'
  RETURNING claim_id
)
INSERT INTO _m11_claim_map (tracker_id, claim_id) SELECT 'M11B-C012', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Anesthetic, hypothermic, and pharmacologic protection signals are model- and bundle-dependent and should not be assigned causal weight without timing and comparator details.',
    'boundary condition',
    'medium',
    'Module 11A tracker / source-page metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for exact estimates and protocol details.", "source_paper_tracker_id": "M11A-P013", "topic_id": "M11B-T005", "tracker_id": "M11B-C013"}'
  FROM _m11_paper_map p
  WHERE p.tracker_id = 'M11A-P013'
  RETURNING claim_id
)
INSERT INTO _m11_claim_map (tracker_id, claim_id) SELECT 'M11B-C013', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Neuromonitoring can guide rescue and risk detection but is not itself proof of protection unless linked to intervention and endpoint recovery.',
    'boundary condition',
    'medium',
    'Module 11A tracker / source-page metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for exact estimates and protocol details.", "source_paper_tracker_id": "M11A-P014", "topic_id": "M11B-T006", "tracker_id": "M11B-C014"}'
  FROM _m11_paper_map p
  WHERE p.tracker_id = 'M11A-P014'
  RETURNING claim_id
)
INSERT INTO _m11_claim_map (tracker_id, claim_id) SELECT 'M11B-C014', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Registry rows should remain protocol/status evidence until results are linked and endpoint definitions are extracted.',
    'boundary condition',
    'medium',
    'Module 11A tracker / source-page metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for exact estimates and protocol details.", "source_paper_tracker_id": "M11A-P015", "topic_id": "M11B-T007", "tracker_id": "M11B-C015"}'
  FROM _m11_paper_map p
  WHERE p.tracker_id = 'M11A-P015'
  RETURNING claim_id
)
INSERT INTO _m11_claim_map (tracker_id, claim_id) SELECT 'M11B-C015', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Perioperative ischemia prophylaxis is mechanistically adjacent to, but not interchangeable with, traumatic chronic SCI reconstruction.',
    'boundary condition',
    'medium',
    'Module 11A tracker / source-page metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for exact estimates and protocol details.", "source_paper_tracker_id": "M11A-P016", "topic_id": "M11B-T008", "tracker_id": "M11B-C016"}'
  FROM _m11_paper_map p
  WHERE p.tracker_id = 'M11A-P016'
  RETURNING claim_id
)
INSERT INTO _m11_claim_map (tracker_id, claim_id) SELECT 'M11B-C016', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'CSF drainage/perfusion protocols are repeatedly used as spinal cord protection measures, but benefits must be balanced against drain complications and prophylactic-versus-therapeutic timing.',
    'synthesis',
    'medium',
    'Module 11A tracker / source-page metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for exact estimates and protocol details.", "source_paper_tracker_id": "M11A-P017", "topic_id": "M11B-T001", "tracker_id": "M11B-C017"}'
  FROM _m11_paper_map p
  WHERE p.tracker_id = 'M11A-P017'
  RETURNING claim_id
)
INSERT INTO _m11_claim_map (tracker_id, claim_id) SELECT 'M11B-C017', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Staged repair and collateral-network strategies are plausible conditioning approaches, but registry and meta-analysis data require approach-specific interpretation.',
    'synthesis',
    'medium',
    'Module 11A tracker / source-page metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for exact estimates and protocol details.", "source_paper_tracker_id": "M11A-P018", "topic_id": "M11B-T002", "tracker_id": "M11B-C018"}'
  FROM _m11_paper_map p
  WHERE p.tracker_id = 'M11A-P018'
  RETURNING claim_id
)
INSERT INTO _m11_claim_map (tracker_id, claim_id) SELECT 'M11B-C018', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Direct/local ischemic preconditioning and postconditioning show stronger spinal-cord-specific animal protection than remote conditioning.',
    'synthesis',
    'medium',
    'Module 11A tracker / source-page metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for exact estimates and protocol details.", "source_paper_tracker_id": "M11A-P019", "topic_id": "M11B-T003", "tracker_id": "M11B-C019"}'
  FROM _m11_paper_map p
  WHERE p.tracker_id = 'M11A-P019'
  RETURNING claim_id
)
INSERT INTO _m11_claim_map (tracker_id, claim_id) SELECT 'M11B-C019', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Remote ischemic conditioning evidence is not yet equivalent to direct spinal cord protection unless spinal cord endpoints are measured.',
    'boundary condition',
    'medium',
    'Module 11A tracker / source-page metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for exact estimates and protocol details.", "source_paper_tracker_id": "M11A-P020", "topic_id": "M11B-T004", "tracker_id": "M11B-C020"}'
  FROM _m11_paper_map p
  WHERE p.tracker_id = 'M11A-P020'
  RETURNING claim_id
)
INSERT INTO _m11_claim_map (tracker_id, claim_id) SELECT 'M11B-C020', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Anesthetic, hypothermic, and pharmacologic protection signals are model- and bundle-dependent and should not be assigned causal weight without timing and comparator details.',
    'boundary condition',
    'medium',
    'Module 11A tracker / source-page metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for exact estimates and protocol details.", "source_paper_tracker_id": "M11A-P021", "topic_id": "M11B-T005", "tracker_id": "M11B-C021"}'
  FROM _m11_paper_map p
  WHERE p.tracker_id = 'M11A-P021'
  RETURNING claim_id
)
INSERT INTO _m11_claim_map (tracker_id, claim_id) SELECT 'M11B-C021', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Neuromonitoring can guide rescue and risk detection but is not itself proof of protection unless linked to intervention and endpoint recovery.',
    'boundary condition',
    'medium',
    'Module 11A tracker / source-page metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for exact estimates and protocol details.", "source_paper_tracker_id": "M11A-P022", "topic_id": "M11B-T006", "tracker_id": "M11B-C022"}'
  FROM _m11_paper_map p
  WHERE p.tracker_id = 'M11A-P022'
  RETURNING claim_id
)
INSERT INTO _m11_claim_map (tracker_id, claim_id) SELECT 'M11B-C022', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Registry rows should remain protocol/status evidence until results are linked and endpoint definitions are extracted.',
    'boundary condition',
    'medium',
    'Module 11A tracker / source-page metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for exact estimates and protocol details.", "source_paper_tracker_id": "M11A-P023", "topic_id": "M11B-T007", "tracker_id": "M11B-C023"}'
  FROM _m11_paper_map p
  WHERE p.tracker_id = 'M11A-P023'
  RETURNING claim_id
)
INSERT INTO _m11_claim_map (tracker_id, claim_id) SELECT 'M11B-C023', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Perioperative ischemia prophylaxis is mechanistically adjacent to, but not interchangeable with, traumatic chronic SCI reconstruction.',
    'boundary condition',
    'medium',
    'Module 11A tracker / source-page metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for exact estimates and protocol details.", "source_paper_tracker_id": "M11A-P024", "topic_id": "M11B-T008", "tracker_id": "M11B-C024"}'
  FROM _m11_paper_map p
  WHERE p.tracker_id = 'M11A-P024'
  RETURNING claim_id
)
INSERT INTO _m11_claim_map (tracker_id, claim_id) SELECT 'M11B-C024', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'CSF drainage/perfusion protocols are repeatedly used as spinal cord protection measures, but benefits must be balanced against drain complications and prophylactic-versus-therapeutic timing.',
    'synthesis',
    'medium',
    'Module 11A tracker / source-page metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for exact estimates and protocol details.", "source_paper_tracker_id": "M11A-P025", "topic_id": "M11B-T001", "tracker_id": "M11B-C025"}'
  FROM _m11_paper_map p
  WHERE p.tracker_id = 'M11A-P025'
  RETURNING claim_id
)
INSERT INTO _m11_claim_map (tracker_id, claim_id) SELECT 'M11B-C025', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Staged repair and collateral-network strategies are plausible conditioning approaches, but registry and meta-analysis data require approach-specific interpretation.',
    'synthesis',
    'medium',
    'Module 11A tracker / source-page metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for exact estimates and protocol details.", "source_paper_tracker_id": "M11A-P026", "topic_id": "M11B-T002", "tracker_id": "M11B-C026"}'
  FROM _m11_paper_map p
  WHERE p.tracker_id = 'M11A-P026'
  RETURNING claim_id
)
INSERT INTO _m11_claim_map (tracker_id, claim_id) SELECT 'M11B-C026', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Direct/local ischemic preconditioning and postconditioning show stronger spinal-cord-specific animal protection than remote conditioning.',
    'synthesis',
    'medium',
    'Module 11A tracker / source-page metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for exact estimates and protocol details.", "source_paper_tracker_id": "M11A-P027", "topic_id": "M11B-T003", "tracker_id": "M11B-C027"}'
  FROM _m11_paper_map p
  WHERE p.tracker_id = 'M11A-P027'
  RETURNING claim_id
)
INSERT INTO _m11_claim_map (tracker_id, claim_id) SELECT 'M11B-C027', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Remote ischemic conditioning evidence is not yet equivalent to direct spinal cord protection unless spinal cord endpoints are measured.',
    'boundary condition',
    'medium',
    'Module 11A tracker / source-page metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for exact estimates and protocol details.", "source_paper_tracker_id": "M11A-P028", "topic_id": "M11B-T004", "tracker_id": "M11B-C028"}'
  FROM _m11_paper_map p
  WHERE p.tracker_id = 'M11A-P028'
  RETURNING claim_id
)
INSERT INTO _m11_claim_map (tracker_id, claim_id) SELECT 'M11B-C028', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Anesthetic, hypothermic, and pharmacologic protection signals are model- and bundle-dependent and should not be assigned causal weight without timing and comparator details.',
    'boundary condition',
    'medium',
    'Module 11A tracker / source-page metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for exact estimates and protocol details.", "source_paper_tracker_id": "M11A-P029", "topic_id": "M11B-T005", "tracker_id": "M11B-C029"}'
  FROM _m11_paper_map p
  WHERE p.tracker_id = 'M11A-P029'
  RETURNING claim_id
)
INSERT INTO _m11_claim_map (tracker_id, claim_id) SELECT 'M11B-C029', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Neuromonitoring can guide rescue and risk detection but is not itself proof of protection unless linked to intervention and endpoint recovery.',
    'boundary condition',
    'medium',
    'Module 11A tracker / source-page metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for exact estimates and protocol details.", "source_paper_tracker_id": "M11A-P030", "topic_id": "M11B-T006", "tracker_id": "M11B-C030"}'
  FROM _m11_paper_map p
  WHERE p.tracker_id = 'M11A-P030'
  RETURNING claim_id
)
INSERT INTO _m11_claim_map (tracker_id, claim_id) SELECT 'M11B-C030', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Registry rows should remain protocol/status evidence until results are linked and endpoint definitions are extracted.',
    'boundary condition',
    'medium',
    'Module 11A tracker / source-page metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for exact estimates and protocol details.", "source_paper_tracker_id": "M11A-P031", "topic_id": "M11B-T007", "tracker_id": "M11B-C031"}'
  FROM _m11_paper_map p
  WHERE p.tracker_id = 'M11A-P031'
  RETURNING claim_id
)
INSERT INTO _m11_claim_map (tracker_id, claim_id) SELECT 'M11B-C031', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Perioperative ischemia prophylaxis is mechanistically adjacent to, but not interchangeable with, traumatic chronic SCI reconstruction.',
    'boundary condition',
    'medium',
    'Module 11A tracker / source-page metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for exact estimates and protocol details.", "source_paper_tracker_id": "M11A-P032", "topic_id": "M11B-T008", "tracker_id": "M11B-C032"}'
  FROM _m11_paper_map p
  WHERE p.tracker_id = 'M11A-P032'
  RETURNING claim_id
)
INSERT INTO _m11_claim_map (tracker_id, claim_id) SELECT 'M11B-C032', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "medium", "tracker_id": "M11B-L001"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O001'
  WHERE c.tracker_id = 'M11B-C001'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L001', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "medium", "tracker_id": "M11B-L002"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O002'
  WHERE c.tracker_id = 'M11B-C002'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L002', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "medium", "tracker_id": "M11B-L003"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O003'
  WHERE c.tracker_id = 'M11B-C003'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L003', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "medium", "tracker_id": "M11B-L004"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O004'
  WHERE c.tracker_id = 'M11B-C004'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L004', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "medium", "tracker_id": "M11B-L005"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O005'
  WHERE c.tracker_id = 'M11B-C005'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L005', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "medium", "tracker_id": "M11B-L006"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O006'
  WHERE c.tracker_id = 'M11B-C006'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L006', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "medium", "tracker_id": "M11B-L007"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O007'
  WHERE c.tracker_id = 'M11B-C007'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L007', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "medium", "tracker_id": "M11B-L008"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O008'
  WHERE c.tracker_id = 'M11B-C008'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L008', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "medium", "tracker_id": "M11B-L009"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O009'
  WHERE c.tracker_id = 'M11B-C009'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L009', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "medium", "tracker_id": "M11B-L010"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O010'
  WHERE c.tracker_id = 'M11B-C010'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L010', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "medium", "tracker_id": "M11B-L011"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O011'
  WHERE c.tracker_id = 'M11B-C011'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L011', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "medium", "tracker_id": "M11B-L012"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O012'
  WHERE c.tracker_id = 'M11B-C012'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L012', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "medium", "tracker_id": "M11B-L013"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O013'
  WHERE c.tracker_id = 'M11B-C013'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L013', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "medium", "tracker_id": "M11B-L014"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O014'
  WHERE c.tracker_id = 'M11B-C014'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L014', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "medium", "tracker_id": "M11B-L015"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O015'
  WHERE c.tracker_id = 'M11B-C015'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L015', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "medium", "tracker_id": "M11B-L016"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O016'
  WHERE c.tracker_id = 'M11B-C016'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L016', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "medium", "tracker_id": "M11B-L017"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O017'
  WHERE c.tracker_id = 'M11B-C017'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L017', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "medium", "tracker_id": "M11B-L018"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O018'
  WHERE c.tracker_id = 'M11B-C018'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L018', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "medium", "tracker_id": "M11B-L019"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O019'
  WHERE c.tracker_id = 'M11B-C019'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L019', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "medium", "tracker_id": "M11B-L020"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O020'
  WHERE c.tracker_id = 'M11B-C020'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L020', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "medium", "tracker_id": "M11B-L021"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O021'
  WHERE c.tracker_id = 'M11B-C021'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L021', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "medium", "tracker_id": "M11B-L022"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O022'
  WHERE c.tracker_id = 'M11B-C022'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L022', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "medium", "tracker_id": "M11B-L023"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O023'
  WHERE c.tracker_id = 'M11B-C023'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L023', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "medium", "tracker_id": "M11B-L024"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O024'
  WHERE c.tracker_id = 'M11B-C024'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L024', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "medium", "tracker_id": "M11B-L025"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O025'
  WHERE c.tracker_id = 'M11B-C025'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L025', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "medium", "tracker_id": "M11B-L026"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O026'
  WHERE c.tracker_id = 'M11B-C026'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L026', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "medium", "tracker_id": "M11B-L027"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O027'
  WHERE c.tracker_id = 'M11B-C027'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L027', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "medium", "tracker_id": "M11B-L028"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O028'
  WHERE c.tracker_id = 'M11B-C028'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L028', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "medium", "tracker_id": "M11B-L029"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O029'
  WHERE c.tracker_id = 'M11B-C029'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L029', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "medium", "tracker_id": "M11B-L030"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O030'
  WHERE c.tracker_id = 'M11B-C030'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L030', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "medium", "tracker_id": "M11B-L031"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O031'
  WHERE c.tracker_id = 'M11B-C031'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L031', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "medium", "tracker_id": "M11B-L032"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O032'
  WHERE c.tracker_id = 'M11B-C032'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L032', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "low", "tracker_id": "M11B-L033"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O009'
  WHERE c.tracker_id = 'M11B-C001'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L033', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "low", "tracker_id": "M11B-L034"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O010'
  WHERE c.tracker_id = 'M11B-C002'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L034', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "low", "tracker_id": "M11B-L035"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O011'
  WHERE c.tracker_id = 'M11B-C003'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L035', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "low", "tracker_id": "M11B-L036"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O012'
  WHERE c.tracker_id = 'M11B-C004'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L036', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "low", "tracker_id": "M11B-L037"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O013'
  WHERE c.tracker_id = 'M11B-C005'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L037', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "low", "tracker_id": "M11B-L038"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O014'
  WHERE c.tracker_id = 'M11B-C006'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L038', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "low", "tracker_id": "M11B-L039"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O015'
  WHERE c.tracker_id = 'M11B-C007'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L039', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "low", "tracker_id": "M11B-L040"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O016'
  WHERE c.tracker_id = 'M11B-C008'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L040', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "low", "tracker_id": "M11B-L041"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O017'
  WHERE c.tracker_id = 'M11B-C009'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L041', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "low", "tracker_id": "M11B-L042"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O018'
  WHERE c.tracker_id = 'M11B-C010'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L042', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "low", "tracker_id": "M11B-L043"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O019'
  WHERE c.tracker_id = 'M11B-C011'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L043', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "low", "tracker_id": "M11B-L044"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O020'
  WHERE c.tracker_id = 'M11B-C012'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L044', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "low", "tracker_id": "M11B-L045"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O021'
  WHERE c.tracker_id = 'M11B-C013'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L045', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "low", "tracker_id": "M11B-L046"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O022'
  WHERE c.tracker_id = 'M11B-C014'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L046', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "low", "tracker_id": "M11B-L047"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O023'
  WHERE c.tracker_id = 'M11B-C015'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L047', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "low", "tracker_id": "M11B-L048"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O024'
  WHERE c.tracker_id = 'M11B-C016'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L048', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "low", "tracker_id": "M11B-L049"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O025'
  WHERE c.tracker_id = 'M11B-C017'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L049', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "low", "tracker_id": "M11B-L050"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O026'
  WHERE c.tracker_id = 'M11B-C018'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L050', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "low", "tracker_id": "M11B-L051"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O027'
  WHERE c.tracker_id = 'M11B-C019'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L051', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "low", "tracker_id": "M11B-L052"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O028'
  WHERE c.tracker_id = 'M11B-C020'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L052', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "low", "tracker_id": "M11B-L053"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O029'
  WHERE c.tracker_id = 'M11B-C021'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L053', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "low", "tracker_id": "M11B-L054"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O030'
  WHERE c.tracker_id = 'M11B-C022'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L054', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "low", "tracker_id": "M11B-L055"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O031'
  WHERE c.tracker_id = 'M11B-C023'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L055', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "low", "tracker_id": "M11B-L056"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O032'
  WHERE c.tracker_id = 'M11B-C024'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L056', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "low", "tracker_id": "M11B-L057"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O001'
  WHERE c.tracker_id = 'M11B-C025'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L057', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "low", "tracker_id": "M11B-L058"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O002'
  WHERE c.tracker_id = 'M11B-C026'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L058', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "low", "tracker_id": "M11B-L059"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O003'
  WHERE c.tracker_id = 'M11B-C027'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L059', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "low", "tracker_id": "M11B-L060"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O004'
  WHERE c.tracker_id = 'M11B-C028'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L060', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "low", "tracker_id": "M11B-L061"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O005'
  WHERE c.tracker_id = 'M11B-C029'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L061', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "low", "tracker_id": "M11B-L062"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O006'
  WHERE c.tracker_id = 'M11B-C030'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L062', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "low", "tracker_id": "M11B-L063"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O007'
  WHERE c.tracker_id = 'M11B-C031'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L063', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "low", "tracker_id": "M11B-L064"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O008'
  WHERE c.tracker_id = 'M11B-C032'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L064', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "low", "tracker_id": "M11B-L065"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O009'
  WHERE c.tracker_id = 'M11B-C001'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L065', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "low", "tracker_id": "M11B-L066"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O010'
  WHERE c.tracker_id = 'M11B-C002'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L066', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "low", "tracker_id": "M11B-L067"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O011'
  WHERE c.tracker_id = 'M11B-C003'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L067', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "low", "tracker_id": "M11B-L068"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O012'
  WHERE c.tracker_id = 'M11B-C004'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L068', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "low", "tracker_id": "M11B-L069"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O013'
  WHERE c.tracker_id = 'M11B-C005'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L069', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "low", "tracker_id": "M11B-L070"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O014'
  WHERE c.tracker_id = 'M11B-C006'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L070', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "low", "tracker_id": "M11B-L071"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O015'
  WHERE c.tracker_id = 'M11B-C007'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L071', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass source-level linkage preserving intervention and endpoint boundaries.", "strength": "low", "tracker_id": "M11B-L072"}'
  FROM _m11_claim_map c
  JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O016'
  WHERE c.tracker_id = 'M11B-C008'
  RETURNING link_id
)
INSERT INTO _m11_link_map (tracker_id, link_id) SELECT 'M11B-L072', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'CSF drainage and perfusion-pressure protocols are established perioperative spinal-cord-protection strategies in aortic surgery contexts, but synthesis must separate prophylactic, therapeutic, rescue, pressure-target, and drain-complication endpoints.',
    'M11B-T001',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M11B-B001", "M11B-B002", "M11B-B003", "M11B-B004", "M11B-B005", "M11B-B006", "M11B-B007", "M11B-B008"], "claim_tracker_ids": ["M11B-C001", "M11B-C002", "M11B-C003", "M11B-C004"], "consensus_draft_id": "M11B-S001", "observation_tracker_ids": ["M11B-O001", "M11B-O002", "M11B-O003", "M11B-O004"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 11 first-pass curation freeze.", "topic_id": "M11B-T001"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m11_consensus_map (tracker_id, consensus_id) SELECT 'M11B-S001', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m11_consensus_map c
JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O001'
WHERE c.tracker_id = 'M11B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m11_consensus_map c
JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O002'
WHERE c.tracker_id = 'M11B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m11_consensus_map c
JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O003'
WHERE c.tracker_id = 'M11B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m11_consensus_map c
JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O004'
WHERE c.tracker_id = 'M11B-S001';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Staged aortic repair and collateral-network conditioning are plausible spinal-cord-protection strategies because they aim to preserve or recruit perfusion before definitive coverage, but open, endovascular, hybrid, interval, and extent-of-coverage designs require separate interpretation.',
    'M11B-T002',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M11B-B001", "M11B-B002", "M11B-B003", "M11B-B004", "M11B-B005", "M11B-B006", "M11B-B007", "M11B-B008"], "claim_tracker_ids": ["M11B-C005", "M11B-C006", "M11B-C007", "M11B-C008"], "consensus_draft_id": "M11B-S002", "observation_tracker_ids": ["M11B-O005", "M11B-O006", "M11B-O007", "M11B-O008"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 11 first-pass curation freeze.", "topic_id": "M11B-T002"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m11_consensus_map (tracker_id, consensus_id) SELECT 'M11B-S002', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m11_consensus_map c
JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O005'
WHERE c.tracker_id = 'M11B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m11_consensus_map c
JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O006'
WHERE c.tracker_id = 'M11B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m11_consensus_map c
JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O007'
WHERE c.tracker_id = 'M11B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m11_consensus_map c
JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O008'
WHERE c.tracker_id = 'M11B-S002';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Direct or local ischemic preconditioning and early postconditioning have the clearest spinal-cord-specific conditioning logic in animal ischemia models, but species, occlusion method, ischemia duration, timing, and reperfusion window determine applicability.',
    'M11B-T003',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M11B-B001", "M11B-B002", "M11B-B003", "M11B-B004", "M11B-B005", "M11B-B006", "M11B-B007", "M11B-B008"], "claim_tracker_ids": ["M11B-C009", "M11B-C010", "M11B-C011", "M11B-C012"], "consensus_draft_id": "M11B-S003", "observation_tracker_ids": ["M11B-O009", "M11B-O010", "M11B-O011", "M11B-O012"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 11 first-pass curation freeze.", "topic_id": "M11B-T003"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m11_consensus_map (tracker_id, consensus_id) SELECT 'M11B-S003', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m11_consensus_map c
JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O009'
WHERE c.tracker_id = 'M11B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m11_consensus_map c
JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O010'
WHERE c.tracker_id = 'M11B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m11_consensus_map c
JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O011'
WHERE c.tracker_id = 'M11B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m11_consensus_map c
JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O012'
WHERE c.tracker_id = 'M11B-S003';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Remote ischemic conditioning evidence is weaker for spinal-cord-specific protection than direct/local conditioning because limb, kidney, or obstructive-sleep-apnea analogs often measure systemic or non-spinal endpoints rather than direct cord preservation.',
    'M11B-T004',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M11B-B001", "M11B-B002", "M11B-B003", "M11B-B004", "M11B-B005", "M11B-B006", "M11B-B007", "M11B-B008"], "claim_tracker_ids": ["M11B-C013", "M11B-C014", "M11B-C015", "M11B-C016"], "consensus_draft_id": "M11B-S004", "observation_tracker_ids": ["M11B-O013", "M11B-O014", "M11B-O015", "M11B-O016"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 11 first-pass curation freeze.", "topic_id": "M11B-T004"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m11_consensus_map (tracker_id, consensus_id) SELECT 'M11B-S004', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m11_consensus_map c
JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O013'
WHERE c.tracker_id = 'M11B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m11_consensus_map c
JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O014'
WHERE c.tracker_id = 'M11B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m11_consensus_map c
JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O015'
WHERE c.tracker_id = 'M11B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m11_consensus_map c
JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O016'
WHERE c.tracker_id = 'M11B-S004';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Hypothermia, anesthetic conditioning, and pharmacologic protection form a perioperative adjunct family, but causal strength depends on whether the intervention is isolated from perfusion management, CSF drainage, monitoring, and rescue bundles.',
    'M11B-T005',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M11B-B001", "M11B-B002", "M11B-B003", "M11B-B004", "M11B-B005", "M11B-B006", "M11B-B007", "M11B-B008"], "claim_tracker_ids": ["M11B-C017", "M11B-C018", "M11B-C019", "M11B-C020"], "consensus_draft_id": "M11B-S005", "observation_tracker_ids": ["M11B-O017", "M11B-O018", "M11B-O019", "M11B-O020"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 11 first-pass curation freeze.", "topic_id": "M11B-T005"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m11_consensus_map (tracker_id, consensus_id) SELECT 'M11B-S005', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m11_consensus_map c
JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O017'
WHERE c.tracker_id = 'M11B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m11_consensus_map c
JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O018'
WHERE c.tracker_id = 'M11B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m11_consensus_map c
JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O019'
WHERE c.tracker_id = 'M11B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m11_consensus_map c
JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O020'
WHERE c.tracker_id = 'M11B-S005';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Neuromonitoring can guide risk detection and rescue during aortic procedures, but it is not itself proof of neuroprotection unless changes are linked to a defined intervention and neurologic endpoint recovery.',
    'M11B-T006',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M11B-B001", "M11B-B002", "M11B-B003", "M11B-B004", "M11B-B005", "M11B-B006", "M11B-B007", "M11B-B008"], "claim_tracker_ids": ["M11B-C021", "M11B-C022", "M11B-C023", "M11B-C024"], "consensus_draft_id": "M11B-S006", "observation_tracker_ids": ["M11B-O021", "M11B-O022", "M11B-O023", "M11B-O024"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 11 first-pass curation freeze.", "topic_id": "M11B-T006"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m11_consensus_map (tracker_id, consensus_id) SELECT 'M11B-S006', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m11_consensus_map c
JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O021'
WHERE c.tracker_id = 'M11B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m11_consensus_map c
JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O022'
WHERE c.tracker_id = 'M11B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m11_consensus_map c
JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O023'
WHERE c.tracker_id = 'M11B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m11_consensus_map c
JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O024'
WHERE c.tracker_id = 'M11B-S006';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Clinical trial and registry rows in perioperative spinal-cord ischemia should remain protocol, status, feasibility, safety, or monitoring evidence until linked outcomes define the intervention, comparator, and neurologic endpoint.',
    'M11B-T007',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M11B-B001", "M11B-B002", "M11B-B003", "M11B-B004", "M11B-B005", "M11B-B006", "M11B-B007", "M11B-B008"], "claim_tracker_ids": ["M11B-C025", "M11B-C026", "M11B-C027", "M11B-C028"], "consensus_draft_id": "M11B-S007", "observation_tracker_ids": ["M11B-O025", "M11B-O026", "M11B-O027", "M11B-O028"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 11 first-pass curation freeze.", "topic_id": "M11B-T007"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m11_consensus_map (tracker_id, consensus_id) SELECT 'M11B-S007', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m11_consensus_map c
JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O025'
WHERE c.tracker_id = 'M11B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m11_consensus_map c
JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O026'
WHERE c.tracker_id = 'M11B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m11_consensus_map c
JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O027'
WHERE c.tracker_id = 'M11B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m11_consensus_map c
JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O028'
WHERE c.tracker_id = 'M11B-S007';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Module 11 is a conditioning analog for the SCI project, not direct evidence for traumatic chronic reconstruction: perioperative ischemia prevention can inform timing, perfusion, and host-state logic only when ischemic versus traumatic mechanisms are kept separate.',
    'M11B-T008',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M11B-B001", "M11B-B002", "M11B-B003", "M11B-B004", "M11B-B005", "M11B-B006", "M11B-B007", "M11B-B008"], "claim_tracker_ids": ["M11B-C029", "M11B-C030", "M11B-C031", "M11B-C032"], "consensus_draft_id": "M11B-S008", "observation_tracker_ids": ["M11B-O029", "M11B-O030", "M11B-O031", "M11B-O032"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 11 first-pass curation freeze.", "topic_id": "M11B-T008"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m11_consensus_map (tracker_id, consensus_id) SELECT 'M11B-S008', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m11_consensus_map c
JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O029'
WHERE c.tracker_id = 'M11B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m11_consensus_map c
JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O030'
WHERE c.tracker_id = 'M11B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m11_consensus_map c
JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O031'
WHERE c.tracker_id = 'M11B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m11_consensus_map c
JOIN _m11_observation_map o ON o.tracker_id = 'M11B-O032'
WHERE c.tracker_id = 'M11B-S008';

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
  SELECT COUNT(*) INTO paper_count FROM _m11_paper_map;
  SELECT COUNT(*) INTO experiment_count FROM _m11_experiment_map;
  SELECT COUNT(*) INTO observation_count FROM _m11_observation_map;
  SELECT COUNT(*) INTO claim_count FROM _m11_claim_map;
  SELECT COUNT(*) INTO link_count FROM _m11_link_map;
  SELECT COUNT(*) INTO consensus_count FROM _m11_consensus_map;
  SELECT COUNT(*) INTO consensus_observation_count
  FROM Consensus_Observation co
  JOIN _m11_consensus_map cm ON cm.consensus_id = co.consensus_id;
  IF paper_count <> 32 THEN RAISE EXCEPTION 'Expected 32 papers, found %', paper_count; END IF;
  IF experiment_count <> 32 THEN RAISE EXCEPTION 'Unexpected experiment count %', experiment_count; END IF;
  IF observation_count <> 32 THEN RAISE EXCEPTION 'Expected 32 observations, found %', observation_count; END IF;
  IF claim_count <> 32 THEN RAISE EXCEPTION 'Expected 32 claims, found %', claim_count; END IF;
  IF link_count <> 72 THEN RAISE EXCEPTION 'Expected 72 evidence links, found %', link_count; END IF;
  IF consensus_count <> 8 THEN RAISE EXCEPTION 'Expected 8 consensus rows, found %', consensus_count; END IF;
  IF consensus_observation_count <> 32 THEN RAISE EXCEPTION 'Unexpected consensus-observation count %', consensus_observation_count; END IF;
END $$;

COMMIT;
