-- Module 10B full first-pass materialization generated from tracker-derived JSON.
-- This script is intended for a fresh database loaded with schema/schema.sql and scripts/seed_controlled_vocab.sql.
BEGIN;

CREATE TEMP TABLE _m10_paper_map (tracker_id TEXT PRIMARY KEY, paper_id INTEGER NOT NULL);
CREATE TEMP TABLE _m10_paradigm_map (tracker_id TEXT PRIMARY KEY, paradigm_id INTEGER NOT NULL);
CREATE TEMP TABLE _m10_experiment_map (tracker_id TEXT PRIMARY KEY, experiment_id INTEGER NOT NULL);
CREATE TEMP TABLE _m10_observation_map (tracker_id TEXT PRIMARY KEY, observation_id INTEGER NOT NULL);
CREATE TEMP TABLE _m10_claim_map (tracker_id TEXT PRIMARY KEY, claim_id INTEGER NOT NULL);
CREATE TEMP TABLE _m10_link_map (tracker_id TEXT PRIMARY KEY, link_id INTEGER NOT NULL);
CREATE TEMP TABLE _m10_consensus_map (tracker_id TEXT PRIMARY KEY, consensus_id INTEGER NOT NULL);

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Impact of Intermittent Hypoxia and Prednisolone on Motor Performance in Persons With SCI', 'Shirley Ryan AbilityLab', 2018,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'OTHER', 'NCT03752749',
    NULL, '{"curator_notes": "COMPLETED / verified 2018-11 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P001"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P001', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Fenofibrate Treatment in SCI', 'VA Office of Research and Development', 2019,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'DRUG, OTHER', 'NCT02455336',
    NULL, '{"curator_notes": "COMPLETED / verified 2019-05 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P002"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P002', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Retrospective Study on the WalkOn AFO in Children or Teenagers With Neurological Pathologies', 'Otto Bock France SNC', 2025,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'OTHER', 'NCT06740006',
    NULL, '{"curator_notes": "COMPLETED / verified 2025-09 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P003"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P003', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'FES and Upper Limb Loading Exercises Outcome Comparison on Hand Function in Spinal Cord Injury Patients', 'Riphah International University', 2023,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'OTHER', 'NCT05863988',
    NULL, '{"curator_notes": "UNKNOWN / verified 2023-05 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P004"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P004', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'LEAP a New Overground Body Weight Support Robot: Usability Trial', 'Clinique Romande de Readaptation', 2019,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'DEVICE', 'NCT03458169',
    NULL, '{"curator_notes": "COMPLETED / verified 2018-03 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P005"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P005', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Comparison of Lokomat and Aquatic Exercise for Individuals With Chronic Incomplete Spinal Cord Injury', 'University of Maryland, Baltimore', 2021,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'DEVICE, OTHER', 'NCT01407354',
    NULL, '{"curator_notes": "COMPLETED / verified 2021-05 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P006"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P006', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Negative Pressure Wound Therapy vs. Sterile Dressing for Patients Undergoing Thoracolumbar Spine Surgery', 'John Street', 2018,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'DEVICE, OTHER', 'NCT03632005',
    NULL, '{"curator_notes": "UNKNOWN / verified 2018-08 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P007"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P007', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Upper Limb Activity in Human SCI Rehabilitation', 'University of Zurich', 2019,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'OTHER', 'NCT02098122',
    NULL, '{"curator_notes": "COMPLETED / verified 2019-06 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P008"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P008', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'FES Cycling and Nutritional Counseling for Battling Obesity After SCI', 'William Carey University', 2019,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'COMBINATION_PRODUCT, OTHER', 'NCT03810963',
    NULL, '{"curator_notes": "COMPLETED / verified 2019-10 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P009"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P009', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Feasibility Study of the Instrumented Evaluation of Eccentric Strengthening in Paresis Patients', 'Nantes University Hospital', 2024,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'OTHER', 'NCT05415514',
    NULL, '{"curator_notes": "COMPLETED / verified 2024-07 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P010"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P010', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Assessment of the Effects of Early Proprioceptive Stimulations in Patients With Spinal Cord Injury', 'Assistance Publique - Hôpitaux de Paris', 2021,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'DEVICE', 'NCT05094752',
    NULL, '{"curator_notes": "UNKNOWN / verified 2021-09 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P011"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P011', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Acute and Chronic Effects of Inhaled Steroids on Pulmonary Function in Persons With Spinal Cord Injury', 'James J. Peters Veterans Affairs Medical Center', 2015,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'DRUG', 'NCT01353599',
    NULL, '{"curator_notes": "UNKNOWN / verified 2015-10 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P012"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P012', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Time-effect of FEST+TST in the Upper-extremity Rehabilitation of Individuals with Traumatic SCI', 'University Health Network, Toronto', 2024,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'OTHER', 'NCT04910204',
    NULL, '{"curator_notes": "NOT_YET_RECRUITING / verified 2024-12 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P013"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P013', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'A Pragmatic Evaluation of the Canadian C-Spine Rule by Paramedics', 'Ottawa Hospital Research Institute', 2025,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'OTHER', 'NCT02786966',
    NULL, '{"curator_notes": "COMPLETED / verified 2025-09 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P014"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P014', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Brain/Neural Hand Exoskeleton Control for Restoration of Bimanual Tasks', 'University Hospital Tuebingen', 2020,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'DEVICE', 'NCT04440709',
    NULL, '{"curator_notes": "UNKNOWN / verified 2020-06 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P015"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P015', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Validity and Reliability Study of the Muscle Excitability Scale in Spinal Cord Injury Patients', 'University Hospital, Motol', 2023,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'PROCEDURE', 'NCT04266964',
    NULL, '{"curator_notes": "COMPLETED / verified 2023-03 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P016"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P016', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Pilot Study for Peripheral Neuromuscular Electrical Stimulation of the Quadriceps Muscle', 'University of Sao Paulo General Hospital', 2023,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'DEVICE, OTHER', 'NCT05888714',
    NULL, '{"curator_notes": "UNKNOWN / verified 2023-05 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P017"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P017', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'EINTER PROGRAM in Spinal Cord Injury Patients', 'Instituto de Investigación Sanitaria Aragón', 2025,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'OTHER', 'NCT06624566',
    NULL, '{"curator_notes": "COMPLETED / verified 2024-09 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P018"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P018', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Nerve Transfers for Restoration of Hand Function in Cervical Spinal Cord Injury: Effects and Influencing Factors', 'Roessingh Research and Development', 2025,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'OTHER', 'NCT06596629',
    NULL, '{"curator_notes": "COMPLETED / verified 2025-01 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P019"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P019', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Efficacy and Safety of hUC-MSCs and hUCB-MSCs in the Treatment of Chronic Spinal Cord Injury', 'The First Affiliated Hospital of Dalian Medical University', 2019,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'OTHER', 'NCT04213131',
    NULL, '{"curator_notes": "UNKNOWN / verified 2019-12 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P020"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P020', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'S-cystatin C vs.Injection Clearance Measurements to Estimate Kidney Function in Patients With Spinal Cord Injuries', 'Rigshospitalet, Denmark', 2024,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'OTHER', 'NCT06565351',
    NULL, '{"curator_notes": "COMPLETED / verified 2024-08 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P021"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P021', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Nomad P-KAFO Study', 'Shirley Ryan AbilityLab', 2026,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'DEVICE', 'NCT05644522',
    NULL, '{"curator_notes": "RECRUITING / verified 2026-05 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P022"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P022', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Subarachnoid-Subarachnoid (S-S) Bypass Versus Adhesion Lysis in Spinal Arachnoiditis and Syringomyelia', 'Xuanwu Hospital, Beijing', 2024,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'PROCEDURE', 'NCT06375759',
    NULL, '{"curator_notes": "RECRUITING / verified 2024-04 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P023"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P023', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Effects of a Computerised Exercise System on Functionality of the Arm,Cognition and Quality of Life in Stroke Patients', 'Baskent University', 2021,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'DEVICE, OTHER', 'NCT04036422',
    NULL, '{"curator_notes": "COMPLETED / verified 2021-05 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P024"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P024', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Absorption of Rivaroxaban in Patients With Cervical Spinal Cord Injury', 'Swiss Paraplegic Research, Nottwil', 2019,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'DRUG', 'NCT02970773',
    NULL, '{"curator_notes": "WITHDRAWN / verified 2019-01 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P025"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P025', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Implant for Walking After Incomplete SCI', 'Louis Stokes VA Medical Center', 2025,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'DEVICE', 'NCT06965127',
    NULL, '{"curator_notes": "RECRUITING / verified 2025-05 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P026"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P026', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Early Myofascial Manual Treatment in Subjects With Spasticity Following Acquired Brain Injury', 'Fondazione Policlinico Universitario Agostino Gemelli IRCCS', 2025,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'OTHER', 'NCT06898242',
    NULL, '{"curator_notes": "ACTIVE_NOT_RECRUITING / verified 2025-03 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P027"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P027', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Gait Training Through a Novel Over-ground Wearable Robotic System in People with Pyramidal Hemisyndromes', 'IRCCS San Raffaele Roma', 2024,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'DEVICE', 'NCT04559724',
    NULL, '{"curator_notes": "UNKNOWN / verified 2024-04 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P028"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P028', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Effect of Three Training Programs on the Cardiovascular Condition of Individuals with Spinal Cord Injury', 'Instituto Nacional de Rehabilitacion', 2024,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'OTHER', 'NCT06627881',
    NULL, '{"curator_notes": "UNKNOWN / verified 2024-01 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P029"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P029', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Effect of Teriparatide, Vibration and the Combination on Bone Mass and Bone Architecture in Chronic Spinal Cord Injury', 'Thomas J. Schnitzer', 2025,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'DEVICE, DRUG', 'NCT01225055',
    NULL, '{"curator_notes": "COMPLETED / verified 2025-11 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P030"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P030', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Chronic Pain and Brain Activity in Spinal Cord Injury', 'University of Washington', 2013,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'OTHER', 'NCT01012635',
    NULL, '{"curator_notes": "COMPLETED / verified 2013-01 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P031"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P031', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Safety Study of Stem Cells Treatment in Diabetic Foot Ulcers', 'Sheba Medical Center', 2016,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'BIOLOGICAL', 'NCT01686139',
    NULL, '{"curator_notes": "UNKNOWN / verified 2016-01 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P032"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P032', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Phase II Randomized Pilot Study of Body Weight Support and Treadmill Training for Chronic Thoracic Spinal Cord Injury', 'National Institute of Neurological Disorders and Stroke (NINDS)', 2005,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'BEHAVIORAL', 'NCT00004812',
    NULL, '{"curator_notes": "COMPLETED / verified 2001-12 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P033"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P033', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Long Duration Activity and Metabolic Control After Spinal Cord Injury', 'Richard K Shields', 2023,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'OTHER', 'NCT03139344',
    NULL, '{"curator_notes": "COMPLETED / verified 2023-01 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P034"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P034', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Assess Specific Kinds of Children Challenges for Neurologic Devices Study', 'Carlos Pena, PhD, MS', 2016,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'OTHER', 'NCT01191307',
    NULL, '{"curator_notes": "TERMINATED / verified 2016-10 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P035"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P035', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Gut-Brain Neural Coupling in Spinal Cord Injury', 'University of Miami', 2025,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'OTHER', 'NCT07052344',
    NULL, '{"curator_notes": "RECRUITING / verified 2025-11 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P036"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P036', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Sleep Quality & Spinal Cord Injury', 'Istanbul Physical Medicine Rehabilitation Training and Research Hospital', 2019,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'OTHER', 'NCT04161612',
    NULL, '{"curator_notes": "COMPLETED / verified 2019-11 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P037"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P037', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Multimodality Intervention for Function and Metabolism in SCI', 'Brigham and Women''s Hospital', 2026,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'BEHAVIORAL, DRUG', 'NCT03576001',
    NULL, '{"curator_notes": "COMPLETED / verified 2025-09 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P038"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P038', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Health in Individuals With a Spinal Cord Injury: a Prospective Study', 'Columbia University', 2021,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'BEHAVIORAL', 'NCT03743077',
    NULL, '{"curator_notes": "COMPLETED / verified 2021-01 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P039"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P039', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'The Utilization Effects of Powered Wearable Orthotics in Improving Upper Extremity Function and ADL in Persons With SCI', 'Kessler Foundation', 2025,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'DEVICE, OTHER', 'NCT06349434',
    NULL, '{"curator_notes": "RECRUITING / verified 2025-11 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P040"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P040', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Cardiovascular Effects of High Intensity Interval Training in Individuals With Paraplegia', 'Mayo Clinic', 2021,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'BEHAVIORAL', 'NCT04378218',
    NULL, '{"curator_notes": "COMPLETED / verified 2021-08 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P041"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P041', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Feasibility of Thioridazine as a Mobilizing Agent for CD34+ Hematopoietic Progenitor Cells', 'New Mexico Cancer Research Alliance', 2016,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'DRUG', 'NCT01765803',
    NULL, '{"curator_notes": "TERMINATED / verified 2016-03 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P042"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P042', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'An Online Rehabilitation Programme for People with SCI', 'Glasgow Caledonian University', 2024,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'OTHER', 'NCT06583538',
    NULL, '{"curator_notes": "COMPLETED / verified 2024-11 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P043"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P043', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Use of Neural Functional Electrical Stimulation for the Recovery of Grasping Movements for Patient With Quadriplegia.', 'Clinique Beau Soleil', 2021,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'DEVICE', 'NCT03721861',
    NULL, '{"curator_notes": "TERMINATED / verified 2021-02 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P044"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P044', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Measuring Signatures in the Fluid Surrounding the Spinal Cord in Patients Who Have Problems With Intrathecal Drug Delivery', 'MedtronicNeuro', 2017,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'OTHER', 'NCT01117090',
    NULL, '{"curator_notes": "COMPLETED / verified 2017-04 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P045"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P045', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'The Reversal of Neuromuscular Adaptation in Human With Spinal Cord Injury II', 'Chang Gung University', 2013,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'DEVICE', 'NCT01968096',
    NULL, '{"curator_notes": "UNKNOWN / verified 2013-10 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P046"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P046', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Mechanisms of Orthostatic Intolerance in Spinal Cord Injured Individuals and Following Bed Rest', 'University of British Columbia', 2019,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'OTHER', 'NCT00175773',
    NULL, '{"curator_notes": "COMPLETED / verified 2019-09 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P047"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P047', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Neuromodulation of Ankle Muscles in Persons With SCI', 'Shepherd Center, Atlanta GA', 2022,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'OTHER', 'NCT04238013',
    NULL, '{"curator_notes": "TERMINATED / verified 2022-06 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P048"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P048', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Inspiratory Strength and Respiratory Complications After SCI Injury', 'Swiss Paraplegic Research, Nottwil', 2025,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'PROCEDURE', 'NCT02891096',
    NULL, '{"curator_notes": "COMPLETED / verified 2025-01 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P049"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P049', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Access-H20: Sensor-driven Smart Faucet', 'Old Dominion University', 2026,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'DEVICE', 'NCT07062796',
    NULL, '{"curator_notes": "COMPLETED / verified 2025-07 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P050"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P050', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Bone-biomarkers of Spinal Cord Injury Patients', 'Yeungnam University Hospital', 2021,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'OTHER', 'NCT04403256',
    NULL, '{"curator_notes": "COMPLETED / verified 2021-08 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P051"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P051', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Walking Adaptability Post-Spinal Cord Injury', 'University of Florida', 2015,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'BEHAVIORAL, OTHER', 'NCT01851629',
    NULL, '{"curator_notes": "COMPLETED / verified 2015-04 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P052"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P052', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Improving Adherence to Spinal Cord Injury Exercise Guidelines Using Smartphone Technology and E-coaching', 'Shirley Ryan AbilityLab', 2026,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'BEHAVIORAL', 'NCT05424172',
    NULL, '{"curator_notes": "RECRUITING / verified 2026-05 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P053"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P053', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Romosozumab in Women With Chronic SCI', 'Northwestern University', 2025,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'DRUG', 'NCT04708886',
    NULL, '{"curator_notes": "COMPLETED / verified 2025-09 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P054"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P054', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Ketamine''s Efficiency in the Treatment of Chronic Pain: Kynurenin Pathway', 'Redar', 2018,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'DRUG', 'NCT03513822',
    NULL, '{"curator_notes": "UNKNOWN / verified 2018-04 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P055"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P055', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'The Relationship of DASH and Mediterranean Diet Score With Serum Adiponectin Levels in Patients With Spinal Cord Injury', 'Ankara City Hospital Bilkent', 2023,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'OTHER', 'NCT05997251',
    NULL, '{"curator_notes": "COMPLETED / verified 2023-08 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P056"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P056', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Comparison of Three Different Assisting Devices to Power Manual Wheelchairs in Patients With Spinal Cord Injury', 'Assistance Publique - Hôpitaux de Paris', 2014,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'DEVICE', 'NCT02244931',
    NULL, '{"curator_notes": "COMPLETED / verified 2013-09 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P057"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P057', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Sexual Health of Spinal Cord Injured Females', 'Assistance Publique - Hôpitaux de Paris', 2020,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'OTHER', 'NCT02398331',
    NULL, '{"curator_notes": "COMPLETED / verified 2017-11 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P058"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P058', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Vibration Induced Reflex Responses and Estimation of TVR', 'Istanbul Physical Medicine Rehabilitation Training and Research Hospital', 2019,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'DEVICE', 'NCT03424551',
    NULL, '{"curator_notes": "COMPLETED / verified 2019-08 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P059"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P059', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Functional Electrical Stimulation (FES) and Reconstructive Tetraplegia Hand and Arm Surgery', 'Swiss Paraplegic Research, Nottwil', 2025,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'DEVICE', 'NCT03048331',
    NULL, '{"curator_notes": "TERMINATED / verified 2025-11 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P060"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P060', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Effect of Vibration Therapy on Bone in Persons With Sub-acute Spinal Cord Injury', 'William A. Bauman, M.D.', 2016,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'DEVICE', 'NCT00886145',
    NULL, '{"curator_notes": "COMPLETED / verified 2016-02 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P061"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P061', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Cerebellar Transcranial Direct Current Stimulation for Dysphagia After Supratentorial Stroke', 'Zhejiang Provincial People''s Hospital', 2025,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'DEVICE, OTHER', 'NCT07212634',
    NULL, '{"curator_notes": "NOT_YET_RECRUITING / verified 2025-10 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P062"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P062', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Non-invasive Nerve Stimulation for Inhibition of Bladder Incontinence in Spinal Cord Injured Subjects.', 'Taipei Medical University', 2021,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'DEVICE', 'NCT03877432',
    NULL, '{"curator_notes": "UNKNOWN / verified 2020-10 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P063"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P063', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'The Use of Modern Technologies in Neurorehabilitation', 'University of Rzeszow', 2022,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'OTHER', 'NCT05550987',
    NULL, '{"curator_notes": "UNKNOWN / verified 2022-11 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P064"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P064', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Investigating the Impact of Spinal Cord Electrical Stimulation Combined With Individualized Physical Therapy on Lower Extremity Function in Patients With Spinal Cord Injury', 'Lian-Cing Yan, MSPT', 2025,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'OTHER', 'NCT07037628',
    NULL, '{"curator_notes": "NOT_YET_RECRUITING / verified 2025-06 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P065"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P065', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Efficacy of a Brain-Computer Interface Controlled Functional Electrical Stimulation Therapy for Spinal Cord Injury Neurorehabilitation', 'Instituto Nacional de Rehabilitacion', 2025,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'DEVICE', 'NCT05343130',
    NULL, '{"curator_notes": "RECRUITING / verified 2025-06 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P066"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P066', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Effect of Adaptive Sports After Acquired Physical Disability', 'Université Catholique de Louvain', 2021,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'OTHER', 'NCT04625309',
    NULL, '{"curator_notes": "COMPLETED / verified 2021-09 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P067"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P067', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Whole Body Vibration on Muscle Strength in Patients With Postpolio Syndrome', 'Koç University', 2020,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'DEVICE', 'NCT04387864',
    NULL, '{"curator_notes": "COMPLETED / verified 2020-05 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P068"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P068', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Pilot Study of Ejaculatory Dyssynergia by Electronic Microsensors of Sphincters', 'Lille Catholic University', 2020,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'PROCEDURE', 'NCT02974673',
    NULL, '{"curator_notes": "TERMINATED / verified 2020-06 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P069"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P069', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Prevalence of Acute Critical Neurological Disease in Children: a Global Epidemiological Assessment', 'University of Pittsburgh', 2015,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'OTHER', 'NCT02381977',
    NULL, '{"curator_notes": "COMPLETED / verified 2015-03 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P070"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P070', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'European Home Mechanical Ventilation Registry', 'ResMed', 2020,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'OTHER', 'NCT02315339',
    NULL, '{"curator_notes": "TERMINATED / verified 2020-04 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P071"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P071', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Safety and Feasibility of Paired Transcutaneous Auricular Vagus Nerve Stimulation (taVNS) With Upper Limb Rehabilitation in Incomplete Spinal Cord Injury', 'The University of Texas Health Science Center, Houston', 2025,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'DEVICE', 'NCT06543277',
    NULL, '{"curator_notes": "RECRUITING / verified 2025-09 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P072"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P072', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Noninvasive Spinal Cord Stimulation for Early SCI', 'University of British Columbia', 2026,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'DEVICE', 'NCT06587841',
    NULL, '{"curator_notes": "RECRUITING / verified 2026-02 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P073"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P073', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'CompaRison of FEmorofemoral Bypass and Left-Heart ByPass Techniques in Open Thoracoabdominal AortIc Aneurysm Repair', 'Beijing Anzhen Hospital', 2026,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'PROCEDURE', 'NCT07518251',
    NULL, '{"curator_notes": "RECRUITING / verified 2026-03 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P074"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P074', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'The Effect of Individualized Intervention on the Quality of Bowel Preparation', 'Second Affiliated Hospital of Xi''an Jiaotong University', 2020,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'BEHAVIORAL', 'NCT04446195',
    NULL, '{"curator_notes": "UNKNOWN / verified 2020-06 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P075"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P075', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'The Biophysical Impact of Transcutaneous Spinal Cord Stimulation Within a Single Session', 'Hugo W. Moser Research Institute at Kennedy Krieger, Inc.', 2018,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'OTHER', 'NCT03046875',
    NULL, '{"curator_notes": "WITHDRAWN / verified 2018-02 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P076"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P076', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Feasibility of Telephone Counseling to Increase Physical Fitness in SCI', 'University of Washington', 2017,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'BEHAVIORAL', 'NCT02225028',
    NULL, '{"curator_notes": "COMPLETED / verified 2017-05 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P077"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P077', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Spaulding-Harvard Model System: Effects of Transcranial Direct Current Stimulation (tDCS) on Chronic Pain in Spinal Cord Injury', 'Spaulding Rehabilitation Hospital', 2020,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'DEVICE', 'NCT01599767',
    NULL, '{"curator_notes": "COMPLETED / verified 2020-04 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P078"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P078', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Virtual Reality and Spinal Stimulation to Improve Arm Function', 'Virginia Commonwealth University', 2022,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'OTHER', 'NCT05065437',
    NULL, '{"curator_notes": "WITHDRAWN / verified 2022-06 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P079"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P079', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Acute Intermittent Hypoxia on Leg Function Following Spinal Cord Injury', 'Spaulding Rehabilitation Hospital', 2026,
    'ClinicalTrials.gov registry', NULL, NULL,
    NULL, 'OTHER', 'NCT02274116',
    NULL, '{"curator_notes": "ACTIVE_NOT_RECRUITING / verified 2026-03 / accessed 2026-07-16", "module": "Module 10B", "tracker_id": "M10A-P080"}'
  )
  RETURNING paper_id
)
INSERT INTO _m10_paper_map (tracker_id, paper_id) SELECT 'M10A-P080', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P001',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P001'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P001', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P002',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P002'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P002', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P003',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P003'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P003', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P004',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P004'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P004', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P005',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P005'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P005', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P006',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P006'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P006', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P007',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P007'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P007', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P008',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P008'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P008', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P009',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P009'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P009', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P010',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P010'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P010', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P011',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P011'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P011', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P012',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P012'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P012', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P013',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P013'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P013', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P014',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P014'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P014', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P015',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P015'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P015', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P016',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P016'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P016', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P017',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P017'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P017', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P018',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P018'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P018', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P019',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P019'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P019', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P020',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P020'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P020', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P021',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P021'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P021', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P022',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P022'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P022', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P023',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P023'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P023', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P024',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P024'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P024', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P025',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P025'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P025', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P026',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P026'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P026', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P027',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P027'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P027', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P028',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P028'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P028', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P029',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P029'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P029', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P030',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P030'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P030', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P031',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P031'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P031', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P032',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P032'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P032', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P033',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P033'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P033', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P034',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P034'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P034', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P035',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P035'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P035', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P036',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P036'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P036', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P037',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P037'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P037', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P038',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P038'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P038', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P039',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P039'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P039', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P040',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P040'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P040', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P041',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P041'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P041', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P042',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P042'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P042', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P043',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P043'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P043', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P044',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P044'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P044', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P045',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P045'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P045', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P046',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P046'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P046', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P047',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P047'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P047', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P048',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P048'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P048', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P049',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P049'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P049', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P050',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P050'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P050', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P051',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P051'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P051', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P052',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P052'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P052', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P053',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P053'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P053', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P054',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P054'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P054', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P055',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P055'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P055', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P056',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P056'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P056', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P057',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P057'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P057', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P058',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P058'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P058', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P059',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P059'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P059', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P060',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P060'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P060', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P061',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P061'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P061', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P062',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P062'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P062', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P063',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P063'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P063', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P064',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P064'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P064', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P065',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P065'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P065', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P066',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P066'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P066', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P067',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P067'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P067', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P068',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P068'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P068', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P069',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P069'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P069', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P070',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P070'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P070', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P071',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P071'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P071', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P072',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P072'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P072', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P073',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P073'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P073', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P074',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P074'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P074', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P075',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P075'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P075', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P076',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P076'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P076', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P077',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P077'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P077', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P078',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P078'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P078', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P079',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P079'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P079', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 10B curated evidence extraction',
    'First-pass Module 10B SCI clinical trials curation for M10A-P080',
    'Tracker-derived materialization from Module_10B_TRACKER.md'
  FROM _m10_paper_map WHERE tracker_id = 'M10A-P080'
  RETURNING paradigm_id
)
INSERT INTO _m10_paradigm_map (tracker_id, paradigm_id) SELECT 'M10A-P080', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T001-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O001"], "source_experiment_tracker_id": "M10A-T001-E001", "source_paper_tracker_id": "M10A-P001", "tracker_key": "M10A-P001::M10A-T001-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P001'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P001::M10A-T001-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T002-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O002"], "source_experiment_tracker_id": "M10A-T002-E001", "source_paper_tracker_id": "M10A-P002", "tracker_key": "M10A-P002::M10A-T002-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P002'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P002::M10A-T002-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T003-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O003"], "source_experiment_tracker_id": "M10A-T003-E001", "source_paper_tracker_id": "M10A-P003", "tracker_key": "M10A-P003::M10A-T003-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P003'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P003::M10A-T003-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T004-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O004"], "source_experiment_tracker_id": "M10A-T004-E001", "source_paper_tracker_id": "M10A-P004", "tracker_key": "M10A-P004::M10A-T004-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P004'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P004::M10A-T004-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T005-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O005"], "source_experiment_tracker_id": "M10A-T005-E001", "source_paper_tracker_id": "M10A-P005", "tracker_key": "M10A-P005::M10A-T005-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P005'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P005::M10A-T005-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T006-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O006"], "source_experiment_tracker_id": "M10A-T006-E001", "source_paper_tracker_id": "M10A-P006", "tracker_key": "M10A-P006::M10A-T006-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P006'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P006::M10A-T006-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T007-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O007"], "source_experiment_tracker_id": "M10A-T007-E001", "source_paper_tracker_id": "M10A-P007", "tracker_key": "M10A-P007::M10A-T007-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P007'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P007::M10A-T007-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T008-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O008"], "source_experiment_tracker_id": "M10A-T008-E001", "source_paper_tracker_id": "M10A-P008", "tracker_key": "M10A-P008::M10A-T008-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P008'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P008::M10A-T008-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T009-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O009"], "source_experiment_tracker_id": "M10A-T009-E001", "source_paper_tracker_id": "M10A-P009", "tracker_key": "M10A-P009::M10A-T009-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P009'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P009::M10A-T009-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T010-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O010"], "source_experiment_tracker_id": "M10A-T010-E001", "source_paper_tracker_id": "M10A-P010", "tracker_key": "M10A-P010::M10A-T010-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P010'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P010::M10A-T010-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T011-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O011"], "source_experiment_tracker_id": "M10A-T011-E001", "source_paper_tracker_id": "M10A-P011", "tracker_key": "M10A-P011::M10A-T011-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P011'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P011::M10A-T011-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T012-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O012"], "source_experiment_tracker_id": "M10A-T012-E001", "source_paper_tracker_id": "M10A-P012", "tracker_key": "M10A-P012::M10A-T012-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P012'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P012::M10A-T012-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T013-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O013"], "source_experiment_tracker_id": "M10A-T013-E001", "source_paper_tracker_id": "M10A-P013", "tracker_key": "M10A-P013::M10A-T013-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P013'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P013::M10A-T013-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T014-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O014"], "source_experiment_tracker_id": "M10A-T014-E001", "source_paper_tracker_id": "M10A-P014", "tracker_key": "M10A-P014::M10A-T014-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P014'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P014::M10A-T014-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T015-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O015"], "source_experiment_tracker_id": "M10A-T015-E001", "source_paper_tracker_id": "M10A-P015", "tracker_key": "M10A-P015::M10A-T015-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P015'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P015::M10A-T015-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T016-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O016"], "source_experiment_tracker_id": "M10A-T016-E001", "source_paper_tracker_id": "M10A-P016", "tracker_key": "M10A-P016::M10A-T016-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P016'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P016::M10A-T016-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T017-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O017"], "source_experiment_tracker_id": "M10A-T017-E001", "source_paper_tracker_id": "M10A-P017", "tracker_key": "M10A-P017::M10A-T017-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P017'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P017::M10A-T017-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T018-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O018"], "source_experiment_tracker_id": "M10A-T018-E001", "source_paper_tracker_id": "M10A-P018", "tracker_key": "M10A-P018::M10A-T018-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P018'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P018::M10A-T018-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T019-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O019"], "source_experiment_tracker_id": "M10A-T019-E001", "source_paper_tracker_id": "M10A-P019", "tracker_key": "M10A-P019::M10A-T019-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P019'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P019::M10A-T019-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T020-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O020"], "source_experiment_tracker_id": "M10A-T020-E001", "source_paper_tracker_id": "M10A-P020", "tracker_key": "M10A-P020::M10A-T020-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P020'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P020::M10A-T020-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T021-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O021"], "source_experiment_tracker_id": "M10A-T021-E001", "source_paper_tracker_id": "M10A-P021", "tracker_key": "M10A-P021::M10A-T021-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P021'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P021::M10A-T021-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T022-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O022"], "source_experiment_tracker_id": "M10A-T022-E001", "source_paper_tracker_id": "M10A-P022", "tracker_key": "M10A-P022::M10A-T022-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P022'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P022::M10A-T022-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T023-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O023"], "source_experiment_tracker_id": "M10A-T023-E001", "source_paper_tracker_id": "M10A-P023", "tracker_key": "M10A-P023::M10A-T023-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P023'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P023::M10A-T023-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T024-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O024"], "source_experiment_tracker_id": "M10A-T024-E001", "source_paper_tracker_id": "M10A-P024", "tracker_key": "M10A-P024::M10A-T024-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P024'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P024::M10A-T024-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T025-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O025"], "source_experiment_tracker_id": "M10A-T025-E001", "source_paper_tracker_id": "M10A-P025", "tracker_key": "M10A-P025::M10A-T025-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P025'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P025::M10A-T025-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T026-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O026"], "source_experiment_tracker_id": "M10A-T026-E001", "source_paper_tracker_id": "M10A-P026", "tracker_key": "M10A-P026::M10A-T026-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P026'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P026::M10A-T026-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T027-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O027"], "source_experiment_tracker_id": "M10A-T027-E001", "source_paper_tracker_id": "M10A-P027", "tracker_key": "M10A-P027::M10A-T027-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P027'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P027::M10A-T027-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T028-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O028"], "source_experiment_tracker_id": "M10A-T028-E001", "source_paper_tracker_id": "M10A-P028", "tracker_key": "M10A-P028::M10A-T028-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P028'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P028::M10A-T028-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T029-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O029"], "source_experiment_tracker_id": "M10A-T029-E001", "source_paper_tracker_id": "M10A-P029", "tracker_key": "M10A-P029::M10A-T029-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P029'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P029::M10A-T029-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T030-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O030"], "source_experiment_tracker_id": "M10A-T030-E001", "source_paper_tracker_id": "M10A-P030", "tracker_key": "M10A-P030::M10A-T030-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P030'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P030::M10A-T030-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T031-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O031"], "source_experiment_tracker_id": "M10A-T031-E001", "source_paper_tracker_id": "M10A-P031", "tracker_key": "M10A-P031::M10A-T031-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P031'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P031::M10A-T031-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T032-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O032"], "source_experiment_tracker_id": "M10A-T032-E001", "source_paper_tracker_id": "M10A-P032", "tracker_key": "M10A-P032::M10A-T032-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P032'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P032::M10A-T032-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T033-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O033"], "source_experiment_tracker_id": "M10A-T033-E001", "source_paper_tracker_id": "M10A-P033", "tracker_key": "M10A-P033::M10A-T033-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P033'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P033::M10A-T033-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T034-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O034"], "source_experiment_tracker_id": "M10A-T034-E001", "source_paper_tracker_id": "M10A-P034", "tracker_key": "M10A-P034::M10A-T034-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P034'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P034::M10A-T034-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T035-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O035"], "source_experiment_tracker_id": "M10A-T035-E001", "source_paper_tracker_id": "M10A-P035", "tracker_key": "M10A-P035::M10A-T035-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P035'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P035::M10A-T035-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T036-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O036"], "source_experiment_tracker_id": "M10A-T036-E001", "source_paper_tracker_id": "M10A-P036", "tracker_key": "M10A-P036::M10A-T036-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P036'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P036::M10A-T036-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T037-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O037"], "source_experiment_tracker_id": "M10A-T037-E001", "source_paper_tracker_id": "M10A-P037", "tracker_key": "M10A-P037::M10A-T037-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P037'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P037::M10A-T037-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T038-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O038"], "source_experiment_tracker_id": "M10A-T038-E001", "source_paper_tracker_id": "M10A-P038", "tracker_key": "M10A-P038::M10A-T038-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P038'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P038::M10A-T038-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T039-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O039"], "source_experiment_tracker_id": "M10A-T039-E001", "source_paper_tracker_id": "M10A-P039", "tracker_key": "M10A-P039::M10A-T039-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P039'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P039::M10A-T039-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T040-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O040"], "source_experiment_tracker_id": "M10A-T040-E001", "source_paper_tracker_id": "M10A-P040", "tracker_key": "M10A-P040::M10A-T040-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P040'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P040::M10A-T040-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T041-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O041"], "source_experiment_tracker_id": "M10A-T041-E001", "source_paper_tracker_id": "M10A-P041", "tracker_key": "M10A-P041::M10A-T041-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P041'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P041::M10A-T041-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T042-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O042"], "source_experiment_tracker_id": "M10A-T042-E001", "source_paper_tracker_id": "M10A-P042", "tracker_key": "M10A-P042::M10A-T042-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P042'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P042::M10A-T042-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T043-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O043"], "source_experiment_tracker_id": "M10A-T043-E001", "source_paper_tracker_id": "M10A-P043", "tracker_key": "M10A-P043::M10A-T043-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P043'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P043::M10A-T043-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T044-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O044"], "source_experiment_tracker_id": "M10A-T044-E001", "source_paper_tracker_id": "M10A-P044", "tracker_key": "M10A-P044::M10A-T044-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P044'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P044::M10A-T044-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T045-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O045"], "source_experiment_tracker_id": "M10A-T045-E001", "source_paper_tracker_id": "M10A-P045", "tracker_key": "M10A-P045::M10A-T045-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P045'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P045::M10A-T045-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T046-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O046"], "source_experiment_tracker_id": "M10A-T046-E001", "source_paper_tracker_id": "M10A-P046", "tracker_key": "M10A-P046::M10A-T046-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P046'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P046::M10A-T046-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T047-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O047"], "source_experiment_tracker_id": "M10A-T047-E001", "source_paper_tracker_id": "M10A-P047", "tracker_key": "M10A-P047::M10A-T047-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P047'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P047::M10A-T047-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T048-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O048"], "source_experiment_tracker_id": "M10A-T048-E001", "source_paper_tracker_id": "M10A-P048", "tracker_key": "M10A-P048::M10A-T048-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P048'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P048::M10A-T048-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T049-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O049"], "source_experiment_tracker_id": "M10A-T049-E001", "source_paper_tracker_id": "M10A-P049", "tracker_key": "M10A-P049::M10A-T049-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P049'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P049::M10A-T049-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T050-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O050"], "source_experiment_tracker_id": "M10A-T050-E001", "source_paper_tracker_id": "M10A-P050", "tracker_key": "M10A-P050::M10A-T050-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P050'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P050::M10A-T050-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T051-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O051"], "source_experiment_tracker_id": "M10A-T051-E001", "source_paper_tracker_id": "M10A-P051", "tracker_key": "M10A-P051::M10A-T051-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P051'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P051::M10A-T051-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T052-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O052"], "source_experiment_tracker_id": "M10A-T052-E001", "source_paper_tracker_id": "M10A-P052", "tracker_key": "M10A-P052::M10A-T052-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P052'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P052::M10A-T052-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T053-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O053"], "source_experiment_tracker_id": "M10A-T053-E001", "source_paper_tracker_id": "M10A-P053", "tracker_key": "M10A-P053::M10A-T053-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P053'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P053::M10A-T053-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T054-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O054"], "source_experiment_tracker_id": "M10A-T054-E001", "source_paper_tracker_id": "M10A-P054", "tracker_key": "M10A-P054::M10A-T054-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P054'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P054::M10A-T054-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T055-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O055"], "source_experiment_tracker_id": "M10A-T055-E001", "source_paper_tracker_id": "M10A-P055", "tracker_key": "M10A-P055::M10A-T055-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P055'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P055::M10A-T055-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T056-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O056"], "source_experiment_tracker_id": "M10A-T056-E001", "source_paper_tracker_id": "M10A-P056", "tracker_key": "M10A-P056::M10A-T056-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P056'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P056::M10A-T056-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T057-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O057"], "source_experiment_tracker_id": "M10A-T057-E001", "source_paper_tracker_id": "M10A-P057", "tracker_key": "M10A-P057::M10A-T057-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P057'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P057::M10A-T057-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T058-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O058"], "source_experiment_tracker_id": "M10A-T058-E001", "source_paper_tracker_id": "M10A-P058", "tracker_key": "M10A-P058::M10A-T058-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P058'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P058::M10A-T058-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T059-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O059"], "source_experiment_tracker_id": "M10A-T059-E001", "source_paper_tracker_id": "M10A-P059", "tracker_key": "M10A-P059::M10A-T059-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P059'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P059::M10A-T059-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T060-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O060"], "source_experiment_tracker_id": "M10A-T060-E001", "source_paper_tracker_id": "M10A-P060", "tracker_key": "M10A-P060::M10A-T060-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P060'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P060::M10A-T060-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T061-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O061"], "source_experiment_tracker_id": "M10A-T061-E001", "source_paper_tracker_id": "M10A-P061", "tracker_key": "M10A-P061::M10A-T061-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P061'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P061::M10A-T061-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T062-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O062"], "source_experiment_tracker_id": "M10A-T062-E001", "source_paper_tracker_id": "M10A-P062", "tracker_key": "M10A-P062::M10A-T062-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P062'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P062::M10A-T062-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T063-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O063"], "source_experiment_tracker_id": "M10A-T063-E001", "source_paper_tracker_id": "M10A-P063", "tracker_key": "M10A-P063::M10A-T063-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P063'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P063::M10A-T063-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T064-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O064"], "source_experiment_tracker_id": "M10A-T064-E001", "source_paper_tracker_id": "M10A-P064", "tracker_key": "M10A-P064::M10A-T064-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P064'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P064::M10A-T064-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T065-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O065"], "source_experiment_tracker_id": "M10A-T065-E001", "source_paper_tracker_id": "M10A-P065", "tracker_key": "M10A-P065::M10A-T065-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P065'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P065::M10A-T065-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T066-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O066"], "source_experiment_tracker_id": "M10A-T066-E001", "source_paper_tracker_id": "M10A-P066", "tracker_key": "M10A-P066::M10A-T066-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P066'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P066::M10A-T066-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T067-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O067"], "source_experiment_tracker_id": "M10A-T067-E001", "source_paper_tracker_id": "M10A-P067", "tracker_key": "M10A-P067::M10A-T067-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P067'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P067::M10A-T067-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T068-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O068"], "source_experiment_tracker_id": "M10A-T068-E001", "source_paper_tracker_id": "M10A-P068", "tracker_key": "M10A-P068::M10A-T068-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P068'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P068::M10A-T068-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T069-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O069"], "source_experiment_tracker_id": "M10A-T069-E001", "source_paper_tracker_id": "M10A-P069", "tracker_key": "M10A-P069::M10A-T069-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P069'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P069::M10A-T069-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T070-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O070"], "source_experiment_tracker_id": "M10A-T070-E001", "source_paper_tracker_id": "M10A-P070", "tracker_key": "M10A-P070::M10A-T070-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P070'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P070::M10A-T070-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T071-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O071"], "source_experiment_tracker_id": "M10A-T071-E001", "source_paper_tracker_id": "M10A-P071", "tracker_key": "M10A-P071::M10A-T071-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P071'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P071::M10A-T071-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T072-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O072"], "source_experiment_tracker_id": "M10A-T072-E001", "source_paper_tracker_id": "M10A-P072", "tracker_key": "M10A-P072::M10A-T072-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P072'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P072::M10A-T072-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T073-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O073"], "source_experiment_tracker_id": "M10A-T073-E001", "source_paper_tracker_id": "M10A-P073", "tracker_key": "M10A-P073::M10A-T073-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P073'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P073::M10A-T073-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T074-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O074"], "source_experiment_tracker_id": "M10A-T074-E001", "source_paper_tracker_id": "M10A-P074", "tracker_key": "M10A-P074::M10A-T074-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P074'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P074::M10A-T074-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T075-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O075"], "source_experiment_tracker_id": "M10A-T075-E001", "source_paper_tracker_id": "M10A-P075", "tracker_key": "M10A-P075::M10A-T075-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P075'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P075::M10A-T075-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T076-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O076"], "source_experiment_tracker_id": "M10A-T076-E001", "source_paper_tracker_id": "M10A-P076", "tracker_key": "M10A-P076::M10A-T076-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P076'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P076::M10A-T076-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T077-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O077"], "source_experiment_tracker_id": "M10A-T077-E001", "source_paper_tracker_id": "M10A-P077", "tracker_key": "M10A-P077::M10A-T077-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P077'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P077::M10A-T077-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T078-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O078"], "source_experiment_tracker_id": "M10A-T078-E001", "source_paper_tracker_id": "M10A-P078", "tracker_key": "M10A-P078::M10A-T078-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P078'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P078::M10A-T078-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T079-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O079"], "source_experiment_tracker_id": "M10A-T079-E001", "source_paper_tracker_id": "M10A-P079", "tracker_key": "M10A-P079::M10A-T079-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P079'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P079::M10A-T079-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'ClinicalTrials.gov registry',
    'Tracker experiment M10A-T080-E001',
    'Module 10B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M10B-O080"], "source_experiment_tracker_id": "M10A-T080-E001", "source_paper_tracker_id": "M10A-P080", "tracker_key": "M10A-P080::M10A-T080-E001"}'
  FROM _m10_paper_map p
  JOIN _m10_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M10A-P080'
  RETURNING experiment_id
)
INSERT INTO _m10_experiment_map (tracker_id, experiment_id) SELECT 'M10A-P080::M10A-T080-E001', experiment_id FROM inserted;

INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Clinical trial registry evidence', 'Module 10B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;

INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('BEHAVIORAL', 'Module 10B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('BEHAVIORAL, DRUG', 'Module 10B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('BEHAVIORAL, OTHER', 'Module 10B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('BIOLOGICAL', 'Module 10B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('COMBINATION_PRODUCT, OTHER', 'Module 10B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('DEVICE', 'Module 10B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('DEVICE, DRUG', 'Module 10B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('DEVICE, OTHER', 'Module 10B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('DRUG', 'Module 10B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('DRUG, OTHER', 'Module 10B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('OTHER', 'Module 10B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('PROCEDURE', 'Module 10B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT03752749 status COMPLETED verified 2018-11 accessed 2026-07-16; intervention Prednisolone + Acute Intermittent Hypoxia, Placebo + Acute Intermittent Hypoxia; population Spinal Cord Injuries.',
    'qualitative',
    NULL,
    'NCT03752749 status COMPLETED verified 2018-11 accessed 2026-07-16; intervention Prednisolone + Acute Intermittent Hypoxia, Placebo + Acute Intermittent Hypoxia; population Spinal Cord Injuries.',
    'completed',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T001-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P001", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T001", "tracker_id": "M10B-O001"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P001::M10A-T001-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'OTHER'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O001', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT02455336 status COMPLETED verified 2019-05 accessed 2026-07-16; intervention Fenofibrate, No intervention; population Spinal Cord Injury, Dyslipidemia.',
    'qualitative',
    NULL,
    'NCT02455336 status COMPLETED verified 2019-05 accessed 2026-07-16; intervention Fenofibrate, No intervention; population Spinal Cord Injury, Dyslipidemia.',
    'completed',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T002-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P002", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T002", "tracker_id": "M10B-O002"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P002::M10A-T002-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'DRUG, OTHER'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O002', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT06740006 status COMPLETED verified 2025-09 accessed 2026-07-16; intervention Not specified; population Cerebral Palsy (CP), Spastic Paraplegia, Spinal Cord Injuries (SCI), Spina Bifida, Neuropathy (Disorder).',
    'qualitative',
    NULL,
    'NCT06740006 status COMPLETED verified 2025-09 accessed 2026-07-16; intervention Not specified; population Cerebral Palsy (CP), Spastic Paraplegia, Spinal Cord Injuries (SCI), Spina Bifida, Neuropathy (Disorder).',
    'completed',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T003-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P003", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T003", "tracker_id": "M10B-O003"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P003::M10A-T003-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'OTHER'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O003', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT05863988 status UNKNOWN verified 2023-05 accessed 2026-07-16; intervention Functional Electrical Stimulation, Upper Limb Loading Exercises; population Spinal Cord Injuries.',
    'qualitative',
    NULL,
    'NCT05863988 status UNKNOWN verified 2023-05 accessed 2026-07-16; intervention Functional Electrical Stimulation, Upper Limb Loading Exercises; population Spinal Cord Injuries.',
    'unknown',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T004-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P004", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T004", "tracker_id": "M10B-O004"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P004::M10A-T004-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'OTHER'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O004', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT03458169 status COMPLETED verified 2018-03 accessed 2026-07-16; intervention Therapist LEAP session feedback, Participant LEAP session feedback, LEAP risk control validation; population Spinal Cord Injuries, Cerebral Palsy, Parkinson Disease, Multiple Sclerosis, Stroke.',
    'qualitative',
    NULL,
    'NCT03458169 status COMPLETED verified 2018-03 accessed 2026-07-16; intervention Therapist LEAP session feedback, Participant LEAP session feedback, LEAP risk control validation; population Spinal Cord Injuries, Cerebral Palsy, Parkinson Disease, Multiple Sclerosis, Stroke.',
    'completed',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T005-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P005", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T005", "tracker_id": "M10B-O005"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P005::M10A-T005-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'DEVICE'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O005', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT01407354 status COMPLETED verified 2021-05 accessed 2026-07-16; intervention Lokomat treadmill training, Aquatic exercise therapy; population Spinal Cord Injury.',
    'qualitative',
    NULL,
    'NCT01407354 status COMPLETED verified 2021-05 accessed 2026-07-16; intervention Lokomat treadmill training, Aquatic exercise therapy; population Spinal Cord Injury.',
    'completed',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T006-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P006", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T006", "tracker_id": "M10B-O006"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P006::M10A-T006-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'DEVICE, OTHER'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O006', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT03632005 status UNKNOWN verified 2018-08 accessed 2026-07-16; intervention Vacuum Assisted Closure, Sterile dressing; population Metastatic Disease, Spinal Cord Injury, Spinal Degeneration, Spinal Deformity.',
    'qualitative',
    NULL,
    'NCT03632005 status UNKNOWN verified 2018-08 accessed 2026-07-16; intervention Vacuum Assisted Closure, Sterile dressing; population Metastatic Disease, Spinal Cord Injury, Spinal Degeneration, Spinal Deformity.',
    'unknown',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T007-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P007", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T007", "tracker_id": "M10B-O007"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P007::M10A-T007-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'DEVICE, OTHER'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O007', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT02098122 status COMPLETED verified 2019-06 accessed 2026-07-16; intervention Not specified; population Spinal Cord Injury.',
    'qualitative',
    NULL,
    'NCT02098122 status COMPLETED verified 2019-06 accessed 2026-07-16; intervention Not specified; population Spinal Cord Injury.',
    'completed',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T008-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P008", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T008", "tracker_id": "M10B-O008"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P008::M10A-T008-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'OTHER'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O008', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT03810963 status COMPLETED verified 2019-10 accessed 2026-07-16; intervention HIIT-FES Cycling combined with Nutritional Counseling, Nutritional Counseling Only; population Spinal Cord Injuries.',
    'qualitative',
    NULL,
    'NCT03810963 status COMPLETED verified 2019-10 accessed 2026-07-16; intervention HIIT-FES Cycling combined with Nutritional Counseling, Nutritional Counseling Only; population Spinal Cord Injuries.',
    'completed',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T009-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P009", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T001", "tracker_id": "M10B-O009"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P009::M10A-T009-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'COMBINATION_PRODUCT, OTHER'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O009', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT05415514 status COMPLETED verified 2024-07 accessed 2026-07-16; intervention Instrumented assessment of muscle function; population Paralysis.',
    'qualitative',
    NULL,
    'NCT05415514 status COMPLETED verified 2024-07 accessed 2026-07-16; intervention Instrumented assessment of muscle function; population Paralysis.',
    'completed',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T010-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P010", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T002", "tracker_id": "M10B-O010"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P010::M10A-T010-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'OTHER'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O010', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT05094752 status UNKNOWN verified 2021-09 accessed 2026-07-16; intervention Proprioceptive stimulations, Sham stimulations; population Spinal Cord Injuries.',
    'qualitative',
    NULL,
    'NCT05094752 status UNKNOWN verified 2021-09 accessed 2026-07-16; intervention Proprioceptive stimulations, Sham stimulations; population Spinal Cord Injuries.',
    'unknown',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T011-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P011", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T003", "tracker_id": "M10B-O011"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P011::M10A-T011-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'DEVICE'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O011', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT01353599 status UNKNOWN verified 2015-10 accessed 2026-07-16; intervention Mometasone furoate; population Spinal Cord Injury.',
    'qualitative',
    NULL,
    'NCT01353599 status UNKNOWN verified 2015-10 accessed 2026-07-16; intervention Mometasone furoate; population Spinal Cord Injury.',
    'unknown',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T012-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P012", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T004", "tracker_id": "M10B-O012"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P012::M10A-T012-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'DRUG'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O012', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT04910204 status NOT_YET_RECRUITING verified 2024-12 accessed 2026-07-16; intervention FES Therapy combined with task-specific training (FEST+TST); population Spinal Cord Injuries.',
    'qualitative',
    NULL,
    'NCT04910204 status NOT_YET_RECRUITING verified 2024-12 accessed 2026-07-16; intervention FES Therapy combined with task-specific training (FEST+TST); population Spinal Cord Injuries.',
    'not_yet_recruiting',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T013-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P013", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T005", "tracker_id": "M10B-O013"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P013::M10A-T013-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'OTHER'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O013', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT02786966 status COMPLETED verified 2025-09 accessed 2026-07-16; intervention Canadian C-Spine Rule; population Neck Injuries.',
    'qualitative',
    NULL,
    'NCT02786966 status COMPLETED verified 2025-09 accessed 2026-07-16; intervention Canadian C-Spine Rule; population Neck Injuries.',
    'completed',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T014-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P014", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T006", "tracker_id": "M10B-O014"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P014::M10A-T014-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'OTHER'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O014', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT04440709 status UNKNOWN verified 2020-06 accessed 2026-07-16; intervention Brain/neural hand exoskeleton (B/NHE); population Spinal Cord Injury, Stroke.',
    'qualitative',
    NULL,
    'NCT04440709 status UNKNOWN verified 2020-06 accessed 2026-07-16; intervention Brain/neural hand exoskeleton (B/NHE); population Spinal Cord Injury, Stroke.',
    'unknown',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T015-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P015", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T007", "tracker_id": "M10B-O015"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P015::M10A-T015-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'DEVICE'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O015', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT04266964 status COMPLETED verified 2023-03 accessed 2026-07-16; intervention Manual examination; population Spasticity, Muscle, Spinal Cord Injuries.',
    'qualitative',
    NULL,
    'NCT04266964 status COMPLETED verified 2023-03 accessed 2026-07-16; intervention Manual examination; population Spasticity, Muscle, Spinal Cord Injuries.',
    'completed',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T016-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P016", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T008", "tracker_id": "M10B-O016"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P016::M10A-T016-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'PROCEDURE'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O016', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT05888714 status UNKNOWN verified 2023-05 accessed 2026-07-16; intervention Experimental FES cycling, Comparator FES cycling, Conventional physical therapy; population Spinal Cord Injuries, Brain Injuries, Muscle Atrophy.',
    'qualitative',
    NULL,
    'NCT05888714 status UNKNOWN verified 2023-05 accessed 2026-07-16; intervention Experimental FES cycling, Comparator FES cycling, Conventional physical therapy; population Spinal Cord Injuries, Brain Injuries, Muscle Atrophy.',
    'unknown',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T017-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P017", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T001", "tracker_id": "M10B-O017"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P017::M10A-T017-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'DEVICE, OTHER'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O017', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT06624566 status COMPLETED verified 2024-09 accessed 2026-07-16; intervention Experimental: Implementation of an intensive therapeutic group exercise program in the neurorehabilitation process; population Spinal Cord Injury.',
    'qualitative',
    NULL,
    'NCT06624566 status COMPLETED verified 2024-09 accessed 2026-07-16; intervention Experimental: Implementation of an intensive therapeutic group exercise program in the neurorehabilitation process; population Spinal Cord Injury.',
    'completed',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T018-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P018", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T002", "tracker_id": "M10B-O018"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P018::M10A-T018-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'OTHER'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O018', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT06596629 status COMPLETED verified 2025-01 accessed 2026-07-16; intervention Not specified; population Nerve Transfer.',
    'qualitative',
    NULL,
    'NCT06596629 status COMPLETED verified 2025-01 accessed 2026-07-16; intervention Not specified; population Nerve Transfer.',
    'completed',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T019-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P019", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T003", "tracker_id": "M10B-O019"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P019::M10A-T019-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'OTHER'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O019', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT04213131 status UNKNOWN verified 2019-12 accessed 2026-07-16; intervention Stem cell transplantation; population Spinal Cord Injuries.',
    'qualitative',
    NULL,
    'NCT04213131 status UNKNOWN verified 2019-12 accessed 2026-07-16; intervention Stem cell transplantation; population Spinal Cord Injuries.',
    'unknown',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T020-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P020", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T004", "tracker_id": "M10B-O020"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P020::M10A-T020-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'OTHER'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O020', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT06565351 status COMPLETED verified 2024-08 accessed 2026-07-16; intervention eGFR estimated from creatinine and cystatin C; population Spinal Cord Injuries, Renal Failure.',
    'qualitative',
    NULL,
    'NCT06565351 status COMPLETED verified 2024-08 accessed 2026-07-16; intervention eGFR estimated from creatinine and cystatin C; population Spinal Cord Injuries, Renal Failure.',
    'completed',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T021-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P021", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T005", "tracker_id": "M10B-O021"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P021::M10A-T021-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'OTHER'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O021', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT05644522 status RECRUITING verified 2026-05 accessed 2026-07-16; intervention Indego Nomad® Powered Knee-Ankle-Foot Orthosis (P-KAFO) (Parker Hannifin Corp., Cleveland, OH); population Cerebrovascular Accident, Post-polio Syndrome, Spinal Cord Injuries, Multiple Sclerosis, Muscular Dystrophy.',
    'qualitative',
    NULL,
    'NCT05644522 status RECRUITING verified 2026-05 accessed 2026-07-16; intervention Indego Nomad® Powered Knee-Ankle-Foot Orthosis (P-KAFO) (Parker Hannifin Corp., Cleveland, OH); population Cerebrovascular Accident, Post-polio Syndrome, Spinal Cord Injuries, Multiple Sclerosis, Muscular Dystrophy.',
    'recruiting',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T022-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P022", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T006", "tracker_id": "M10B-O022"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P022::M10A-T022-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'DEVICE'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O022', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT06375759 status RECRUITING verified 2024-04 accessed 2026-07-16; intervention Subarachnoid-Subarachnoid (S-S) Bypass, Intradural Adhesion Lysis; population Syringomyelia.',
    'qualitative',
    NULL,
    'NCT06375759 status RECRUITING verified 2024-04 accessed 2026-07-16; intervention Subarachnoid-Subarachnoid (S-S) Bypass, Intradural Adhesion Lysis; population Syringomyelia.',
    'recruiting',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T023-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P023", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T007", "tracker_id": "M10B-O023"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P023::M10A-T023-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'PROCEDURE'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O023', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT04036422 status COMPLETED verified 2021-05 accessed 2026-07-16; intervention Rejoyce (Rehabilitation Joystick for Computerized Exercise), Conventional physical therapy, Occupational therapy; population Stroke, Neuronal Plasticity, Hemiplegia.',
    'qualitative',
    NULL,
    'NCT04036422 status COMPLETED verified 2021-05 accessed 2026-07-16; intervention Rejoyce (Rehabilitation Joystick for Computerized Exercise), Conventional physical therapy, Occupational therapy; population Stroke, Neuronal Plasticity, Hemiplegia.',
    'completed',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T024-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P024", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T008", "tracker_id": "M10B-O024"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P024::M10A-T024-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'DEVICE, OTHER'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O024', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT02970773 status WITHDRAWN verified 2019-01 accessed 2026-07-16; intervention Rivaroxaban Oral Tablet; population Spinal Cord Injuries, Thromboembolism.',
    'qualitative',
    NULL,
    'NCT02970773 status WITHDRAWN verified 2019-01 accessed 2026-07-16; intervention Rivaroxaban Oral Tablet; population Spinal Cord Injuries, Thromboembolism.',
    'withdrawn',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T025-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P025", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T001", "tracker_id": "M10B-O025"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P025::M10A-T025-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'DRUG'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O025', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT06965127 status RECRUITING verified 2025-05 accessed 2026-07-16; intervention NNP-LE; population Spinal Cord Injury (SCI), Gait.',
    'qualitative',
    NULL,
    'NCT06965127 status RECRUITING verified 2025-05 accessed 2026-07-16; intervention NNP-LE; population Spinal Cord Injury (SCI), Gait.',
    'recruiting',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T026-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P026", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T002", "tracker_id": "M10B-O026"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P026::M10A-T026-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'DEVICE'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O026', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT06898242 status ACTIVE_NOT_RECRUITING verified 2025-03 accessed 2026-07-16; intervention Manual myofascial treatment direct to upper and lower limb, Rehabilitative treatment following rehabilitation project; population Brain Injury, Brain Injury, Vascular, Brain Injuries, Traumatic.',
    'qualitative',
    NULL,
    'NCT06898242 status ACTIVE_NOT_RECRUITING verified 2025-03 accessed 2026-07-16; intervention Manual myofascial treatment direct to upper and lower limb, Rehabilitative treatment following rehabilitation project; population Brain Injury, Brain Injury, Vascular, Brain Injuries, Traumatic.',
    'active_not_recruiting',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T027-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P027", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T003", "tracker_id": "M10B-O027"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P027::M10A-T027-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'OTHER'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O027', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT04559724 status UNKNOWN verified 2024-04 accessed 2026-07-16; intervention Indego Therapy; population Stroke, Brain Injuries, Traumatic, Brain Tumor Benign.',
    'qualitative',
    NULL,
    'NCT04559724 status UNKNOWN verified 2024-04 accessed 2026-07-16; intervention Indego Therapy; population Stroke, Brain Injuries, Traumatic, Brain Tumor Benign.',
    'unknown',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T028-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P028", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T004", "tracker_id": "M10B-O028"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P028::M10A-T028-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'DEVICE'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O028', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT06627881 status UNKNOWN verified 2024-01 accessed 2026-07-16; intervention Continuous aerobic kayak training program, Aerobic Endurance Circuit Program, High intensity interval program with rope; population Spinal Cord Injuries, Cardiovascular Condition, Exercise.',
    'qualitative',
    NULL,
    'NCT06627881 status UNKNOWN verified 2024-01 accessed 2026-07-16; intervention Continuous aerobic kayak training program, Aerobic Endurance Circuit Program, High intensity interval program with rope; population Spinal Cord Injuries, Cardiovascular Condition, Exercise.',
    'unknown',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T029-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P029", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T005", "tracker_id": "M10B-O029"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P029::M10A-T029-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'OTHER'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O029', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT01225055 status COMPLETED verified 2025-11 accessed 2026-07-16; intervention Teriparatide, vibration; population Spinal Cord Injury, Bone Loss, Osteoporosis.',
    'qualitative',
    NULL,
    'NCT01225055 status COMPLETED verified 2025-11 accessed 2026-07-16; intervention Teriparatide, vibration; population Spinal Cord Injury, Bone Loss, Osteoporosis.',
    'completed',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T030-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P030", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T006", "tracker_id": "M10B-O030"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P030::M10A-T030-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'DEVICE, DRUG'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O030', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT01012635 status COMPLETED verified 2013-01 accessed 2026-07-16; intervention Hypnosis, Meditation, Neurofeedback training, Two different levels of tDCS; population Spinal Cord Injury.',
    'qualitative',
    NULL,
    'NCT01012635 status COMPLETED verified 2013-01 accessed 2026-07-16; intervention Hypnosis, Meditation, Neurofeedback training, Two different levels of tDCS; population Spinal Cord Injury.',
    'completed',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T031-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P031", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T007", "tracker_id": "M10B-O031"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P031::M10A-T031-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'OTHER'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O031', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT01686139 status UNKNOWN verified 2016-01 accessed 2026-07-16; intervention ABMD-MSC; population Type I Diabetes Mellitus With Ulcer, Type II Diabetes Mellitus With Ulcer.',
    'qualitative',
    NULL,
    'NCT01686139 status UNKNOWN verified 2016-01 accessed 2026-07-16; intervention ABMD-MSC; population Type I Diabetes Mellitus With Ulcer, Type II Diabetes Mellitus With Ulcer.',
    'unknown',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T032-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P032", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T008", "tracker_id": "M10B-O032"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P032::M10A-T032-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'BIOLOGICAL'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O032', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT00004812 status COMPLETED verified 2001-12 accessed 2026-07-16; intervention Exercise; population Spinal Cord Injury.',
    'qualitative',
    'behavioral / functional recovery assay',
    'NCT00004812 status COMPLETED verified 2001-12 accessed 2026-07-16; intervention Exercise; population Spinal Cord Injury.',
    'completed',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T033-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M10A-P033", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T001", "tracker_id": "M10B-O033"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P033::M10A-T033-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'BEHAVIORAL'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O033', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT03139344 status COMPLETED verified 2023-01 accessed 2026-07-16; intervention Low-frequency Exercise, High-frequency Exercise; population Spinal Cord Injuries.',
    'qualitative',
    NULL,
    'NCT03139344 status COMPLETED verified 2023-01 accessed 2026-07-16; intervention Low-frequency Exercise, High-frequency Exercise; population Spinal Cord Injuries.',
    'completed',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T034-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P034", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T002", "tracker_id": "M10B-O034"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P034::M10A-T034-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'OTHER'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O034', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT01191307 status TERMINATED verified 2016-10 accessed 2026-07-16; intervention Not specified; population Primary Dystonia, Epilepsy, Hydrocephalus, Bladder Control, Hearing Impaired (Partially).',
    'qualitative',
    NULL,
    'NCT01191307 status TERMINATED verified 2016-10 accessed 2026-07-16; intervention Not specified; population Primary Dystonia, Epilepsy, Hydrocephalus, Bladder Control, Hearing Impaired (Partially).',
    'terminated',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T035-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P035", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T003", "tracker_id": "M10B-O035"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P035::M10A-T035-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'OTHER'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O035', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT07052344 status RECRUITING verified 2025-11 accessed 2026-07-16; intervention Preload condition, Ad-libitum control condition; population SCI - Spinal Cord Injury.',
    'qualitative',
    NULL,
    'NCT07052344 status RECRUITING verified 2025-11 accessed 2026-07-16; intervention Preload condition, Ad-libitum control condition; population SCI - Spinal Cord Injury.',
    'recruiting',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T036-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P036", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T004", "tracker_id": "M10B-O036"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P036::M10A-T036-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'OTHER'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O036', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT04161612 status COMPLETED verified 2019-11 accessed 2026-07-16; intervention Demographic characteristics, duration of spinal cord injury, spinal cord injurylevel, etiology, number of intermittent bladder catheterization (IC), number of night time; population Sleep Disorder.',
    'qualitative',
    NULL,
    'NCT04161612 status COMPLETED verified 2019-11 accessed 2026-07-16; intervention Demographic characteristics, duration of spinal cord injury, spinal cord injurylevel, etiology, number of intermittent bladder catheterization (IC), number of night time; population Sleep Disorder.',
    'completed',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T037-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P037", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T005", "tracker_id": "M10B-O037"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P037::M10A-T037-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'OTHER'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O037', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT03576001 status COMPLETED verified 2025-09 accessed 2026-07-16; intervention Testosterone Undecanoate, hybrid exercise; population Spinal Cord Injuries.',
    'qualitative',
    'behavioral / functional recovery assay',
    'NCT03576001 status COMPLETED verified 2025-09 accessed 2026-07-16; intervention Testosterone Undecanoate, hybrid exercise; population Spinal Cord Injuries.',
    'completed',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T038-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M10A-P038", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T006", "tracker_id": "M10B-O038"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P038::M10A-T038-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'BEHAVIORAL, DRUG'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O038', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT03743077 status COMPLETED verified 2021-01 accessed 2026-07-16; intervention Exercise training including inspiratory muscle training; population Spinal Cord Injuries.',
    'qualitative',
    'behavioral / functional recovery assay',
    'NCT03743077 status COMPLETED verified 2021-01 accessed 2026-07-16; intervention Exercise training including inspiratory muscle training; population Spinal Cord Injuries.',
    'completed',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T039-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M10A-P039", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T007", "tracker_id": "M10B-O039"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P039::M10A-T039-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'BEHAVIORAL'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O039', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT06349434 status RECRUITING verified 2025-11 accessed 2026-07-16; intervention MyoMo, conventional therapy; population SCI - Spinal Cord Injury, Upper Extremity Dysfunction, Upper Extremity Problem.',
    'qualitative',
    NULL,
    'NCT06349434 status RECRUITING verified 2025-11 accessed 2026-07-16; intervention MyoMo, conventional therapy; population SCI - Spinal Cord Injury, Upper Extremity Dysfunction, Upper Extremity Problem.',
    'recruiting',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T040-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P040", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T008", "tracker_id": "M10B-O040"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P040::M10A-T040-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'DEVICE, OTHER'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O040', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT04378218 status COMPLETED verified 2021-08 accessed 2026-07-16; intervention High Intensity Interval Training (HIIT); population Paraplegia, Spinal, Spinal Cord Trauma.',
    'qualitative',
    'behavioral / functional recovery assay',
    'NCT04378218 status COMPLETED verified 2021-08 accessed 2026-07-16; intervention High Intensity Interval Training (HIIT); population Paraplegia, Spinal, Spinal Cord Trauma.',
    'completed',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T041-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M10A-P041", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T001", "tracker_id": "M10B-O041"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P041::M10A-T041-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'BEHAVIORAL'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O041', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT01765803 status TERMINATED verified 2016-03 accessed 2026-07-16; intervention Mellaril; population Healthy Subjects.',
    'qualitative',
    NULL,
    'NCT01765803 status TERMINATED verified 2016-03 accessed 2026-07-16; intervention Mellaril; population Healthy Subjects.',
    'terminated',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T042-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P042", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T002", "tracker_id": "M10B-O042"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P042::M10A-T042-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'DRUG'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O042', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT06583538 status COMPLETED verified 2024-11 accessed 2026-07-16; intervention Giraffe Healthcare; population Spinal Cord Injuries, Physical Inactivity, Spinal Cord Injury, Acute.',
    'qualitative',
    NULL,
    'NCT06583538 status COMPLETED verified 2024-11 accessed 2026-07-16; intervention Giraffe Healthcare; population Spinal Cord Injuries, Physical Inactivity, Spinal Cord Injury, Acute.',
    'completed',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T043-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P043", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T003", "tracker_id": "M10B-O043"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P043::M10A-T043-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'OTHER'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O043', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT03721861 status TERMINATED verified 2021-02 accessed 2026-07-16; intervention Intra-operative neural cuff stimulation; population Spinal Cord Injuries.',
    'qualitative',
    NULL,
    'NCT03721861 status TERMINATED verified 2021-02 accessed 2026-07-16; intervention Intra-operative neural cuff stimulation; population Spinal Cord Injuries.',
    'terminated',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T044-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P044", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T004", "tracker_id": "M10B-O044"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P044::M10A-T044-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'DEVICE'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O044', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT01117090 status COMPLETED verified 2017-04 accessed 2026-07-16; intervention Not specified; population Cerebral Palsy, Multiple Sclerosis, Traumatic Brain Injury, Spinal Cord Injury.',
    'qualitative',
    NULL,
    'NCT01117090 status COMPLETED verified 2017-04 accessed 2026-07-16; intervention Not specified; population Cerebral Palsy, Multiple Sclerosis, Traumatic Brain Injury, Spinal Cord Injury.',
    'completed',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T045-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P045", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T005", "tracker_id": "M10B-O045"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P045::M10A-T045-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'OTHER'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O045', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT01968096 status UNKNOWN verified 2013-10 accessed 2026-07-16; intervention home-based ankle continuous passive motion machine.; population Spinal Cord Injury(SCI).',
    'qualitative',
    NULL,
    'NCT01968096 status UNKNOWN verified 2013-10 accessed 2026-07-16; intervention home-based ankle continuous passive motion machine.; population Spinal Cord Injury(SCI).',
    'unknown',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T046-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P046", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T006", "tracker_id": "M10B-O046"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P046::M10A-T046-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'DEVICE'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O046', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT00175773 status COMPLETED verified 2019-09 accessed 2026-07-16; intervention Not specified; population Spinal Cord Injury.',
    'qualitative',
    NULL,
    'NCT00175773 status COMPLETED verified 2019-09 accessed 2026-07-16; intervention Not specified; population Spinal Cord Injury.',
    'completed',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T047-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P047", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T007", "tracker_id": "M10B-O047"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P047::M10A-T047-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'OTHER'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O047', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT04238013 status TERMINATED verified 2022-06 accessed 2026-07-16; intervention Whole Body Vibration (WBV), Electrical Stimulation; population Spinal Cord Injuries, Spastic Gait, Foot Drop.',
    'qualitative',
    NULL,
    'NCT04238013 status TERMINATED verified 2022-06 accessed 2026-07-16; intervention Whole Body Vibration (WBV), Electrical Stimulation; population Spinal Cord Injuries, Spastic Gait, Foot Drop.',
    'terminated',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T048-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P048", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T008", "tracker_id": "M10B-O048"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P048::M10A-T048-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'OTHER'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O048', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT02891096 status COMPLETED verified 2025-01 accessed 2026-07-16; intervention inspiratory muscle strength; population Spinal Cord Injuries, Pneumonia.',
    'qualitative',
    NULL,
    'NCT02891096 status COMPLETED verified 2025-01 accessed 2026-07-16; intervention inspiratory muscle strength; population Spinal Cord Injuries, Pneumonia.',
    'completed',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T049-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P049", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T001", "tracker_id": "M10B-O049"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P049::M10A-T049-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'PROCEDURE'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O049', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT07062796 status COMPLETED verified 2025-07 accessed 2026-07-16; intervention Water Faucet; population Spinal Cord Injury Cervical.',
    'qualitative',
    NULL,
    'NCT07062796 status COMPLETED verified 2025-07 accessed 2026-07-16; intervention Water Faucet; population Spinal Cord Injury Cervical.',
    'completed',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T050-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P050", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T002", "tracker_id": "M10B-O050"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P050::M10A-T050-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'DEVICE'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O050', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT04403256 status COMPLETED verified 2021-08 accessed 2026-07-16; intervention Not specified; population Spinal Cord Injuries, Bone Resorption, Osteoporosis.',
    'qualitative',
    NULL,
    'NCT04403256 status COMPLETED verified 2021-08 accessed 2026-07-16; intervention Not specified; population Spinal Cord Injuries, Bone Resorption, Osteoporosis.',
    'completed',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T051-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P051", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T003", "tracker_id": "M10B-O051"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P051::M10A-T051-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'OTHER'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O051', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT01851629 status COMPLETED verified 2015-04 accessed 2026-07-16; intervention Locomotor Training, Cross-Sectional Testing (No Intervention); population Incomplete Spinal Cord Injury, Brown Sequard Syndrome.',
    'qualitative',
    'behavioral / functional recovery assay',
    'NCT01851629 status COMPLETED verified 2015-04 accessed 2026-07-16; intervention Locomotor Training, Cross-Sectional Testing (No Intervention); population Incomplete Spinal Cord Injury, Brown Sequard Syndrome.',
    'completed',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T052-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M10A-P052", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T004", "tracker_id": "M10B-O052"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P052::M10A-T052-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'BEHAVIORAL, OTHER'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O052', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT05424172 status RECRUITING verified 2026-05 accessed 2026-07-16; intervention Stage-I, Group 1: Self monitoring using Non-interactive App, Stage-I, Group 2: Self monitoring using Interactive App, Stage-II, Groups 1a/2a: E-Coaching 1x per month, Stage-II, Groups 1b/2b: E-Coaching 2x per month; population Spinal Cord Injuries.',
    'qualitative',
    'behavioral / functional recovery assay',
    'NCT05424172 status RECRUITING verified 2026-05 accessed 2026-07-16; intervention Stage-I, Group 1: Self monitoring using Non-interactive App, Stage-I, Group 2: Self monitoring using Interactive App, Stage-II, Groups 1a/2a: E-Coaching 1x per month, Stage-II, Groups 1b/2b: E-Coaching 2x per month; population Spinal Cord Injuries.',
    'recruiting',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T053-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M10A-P053", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T005", "tracker_id": "M10B-O053"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P053::M10A-T053-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'BEHAVIORAL'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O053', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT04708886 status COMPLETED verified 2025-09 accessed 2026-07-16; intervention Romosozumab, Alendronate; population Osteoporosis, Bone Loss, Osteopenia, Osteoporosis, Spinal Cord Injuries, Chronic Spinal Paralysis.',
    'qualitative',
    NULL,
    'NCT04708886 status COMPLETED verified 2025-09 accessed 2026-07-16; intervention Romosozumab, Alendronate; population Osteoporosis, Bone Loss, Osteopenia, Osteoporosis, Spinal Cord Injuries, Chronic Spinal Paralysis.',
    'completed',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T054-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P054", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T006", "tracker_id": "M10B-O054"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P054::M10A-T054-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'DRUG'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O054', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT03513822 status UNKNOWN verified 2018-04 accessed 2026-07-16; intervention Ketamine 10 MG/ML, Placebos, Midazolam 1 MG/ML; population Neuralgia, Chronic Pain, Inflammation.',
    'qualitative',
    NULL,
    'NCT03513822 status UNKNOWN verified 2018-04 accessed 2026-07-16; intervention Ketamine 10 MG/ML, Placebos, Midazolam 1 MG/ML; population Neuralgia, Chronic Pain, Inflammation.',
    'unknown',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T055-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P055", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T007", "tracker_id": "M10B-O055"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P055::M10A-T055-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'DRUG'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O055', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT05997251 status COMPLETED verified 2023-08 accessed 2026-07-16; intervention Keeping a 1-day food consumption record by the patient, Measurement of adiponectin level; population Spinal Cord Injuries.',
    'qualitative',
    NULL,
    'NCT05997251 status COMPLETED verified 2023-08 accessed 2026-07-16; intervention Keeping a 1-day food consumption record by the patient, Measurement of adiponectin level; population Spinal Cord Injuries.',
    'completed',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T056-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P056", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T008", "tracker_id": "M10B-O056"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P056::M10A-T056-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'OTHER'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O056', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT02244931 status COMPLETED verified 2013-09 accessed 2026-07-16; intervention Servomatic™ assisting device, E.Motion© assisting device, Standard manual Wheelchair; population Spinal Cord Injuries.',
    'qualitative',
    NULL,
    'NCT02244931 status COMPLETED verified 2013-09 accessed 2026-07-16; intervention Servomatic™ assisting device, E.Motion© assisting device, Standard manual Wheelchair; population Spinal Cord Injuries.',
    'completed',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T057-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P057", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T001", "tracker_id": "M10B-O057"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P057::M10A-T057-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'DEVICE'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O057', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT02398331 status COMPLETED verified 2017-11 accessed 2026-07-16; intervention Standardised information and education on sexuality in women with spinal cord injury; population Spinal Cord Injuries.',
    'qualitative',
    NULL,
    'NCT02398331 status COMPLETED verified 2017-11 accessed 2026-07-16; intervention Standardised information and education on sexuality in women with spinal cord injury; population Spinal Cord Injuries.',
    'completed',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T058-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P058", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T002", "tracker_id": "M10B-O058"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P058::M10A-T058-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'OTHER'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O058', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT03424551 status COMPLETED verified 2019-08 accessed 2026-07-16; intervention vibrator; population Muscle, Physiology.',
    'qualitative',
    NULL,
    'NCT03424551 status COMPLETED verified 2019-08 accessed 2026-07-16; intervention vibrator; population Muscle, Physiology.',
    'completed',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T059-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P059", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T003", "tracker_id": "M10B-O059"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P059::M10A-T059-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'DEVICE'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O059', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT03048331 status TERMINATED verified 2025-11 accessed 2026-07-16; intervention Functional Electrical Stimulation; population Spinal Cord Injury Cervical.',
    'qualitative',
    NULL,
    'NCT03048331 status TERMINATED verified 2025-11 accessed 2026-07-16; intervention Functional Electrical Stimulation; population Spinal Cord Injury Cervical.',
    'terminated',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T060-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P060", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T004", "tracker_id": "M10B-O060"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P060::M10A-T060-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'DEVICE'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O060', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT00886145 status COMPLETED verified 2016-02 accessed 2026-07-16; intervention Vibration: Right Leg and No Vibration: Left Leg.; population Spinal Cord Injuries.',
    'qualitative',
    NULL,
    'NCT00886145 status COMPLETED verified 2016-02 accessed 2026-07-16; intervention Vibration: Right Leg and No Vibration: Left Leg.; population Spinal Cord Injuries.',
    'completed',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T061-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P061", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T005", "tracker_id": "M10B-O061"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P061::M10A-T061-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'DEVICE'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O061', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT07212634 status NOT_YET_RECRUITING verified 2025-10 accessed 2026-07-16; intervention Transcranial Direct Current Stimulation, Sham tDCS; population Dysphagia After Stroke.',
    'qualitative',
    NULL,
    'NCT07212634 status NOT_YET_RECRUITING verified 2025-10 accessed 2026-07-16; intervention Transcranial Direct Current Stimulation, Sham tDCS; population Dysphagia After Stroke.',
    'not_yet_recruiting',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T062-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P062", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T006", "tracker_id": "M10B-O062"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P062::M10A-T062-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'DEVICE, OTHER'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O062', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT03877432 status UNKNOWN verified 2020-10 accessed 2026-07-16; intervention Dermatome stimulation; population Spinal Cord Injuries.',
    'qualitative',
    NULL,
    'NCT03877432 status UNKNOWN verified 2020-10 accessed 2026-07-16; intervention Dermatome stimulation; population Spinal Cord Injuries.',
    'unknown',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T063-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P063", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T007", "tracker_id": "M10B-O063"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P063::M10A-T063-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'DEVICE'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O063', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT05550987 status UNKNOWN verified 2022-11 accessed 2026-07-16; intervention Rehabilitation program with the use of mechanical vibration using the Vibramoov device and conventional physiotherapy, Rehabilitation program with gait training using the Ekso GT exoskeleton and conventional physiotherapy, Rehabilitation program with the use of gait training with the use of a RoboGait stationary robot and conventional physiotherapy., Rehabilitation program with',
    'qualitative',
    NULL,
    'NCT05550987 status UNKNOWN verified 2022-11 accessed 2026-07-16; intervention Rehabilitation program with the use of mechanical vibration using the Vibramoov device and conventional physiotherapy, Rehabilitation program with gait training using the Ekso GT exoskeleton and conventional physiotherapy, Rehabilitation program with the use of gait training with the use of a RoboGait stationary robot and conventional physiotherapy., Rehabilitation program with',
    'unknown',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T064-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P064", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T008", "tracker_id": "M10B-O064"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P064::M10A-T064-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'OTHER'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O064', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT07037628 status NOT_YET_RECRUITING verified 2025-06 accessed 2026-07-16; intervention Not specified; population Spinal Cord Injury, Spinal Cord Injury Thoracic, Spinal Cord Injury/Damage, Spinal Cord Injury T1-L2, Spinal Cord Stimulation (SCS).',
    'qualitative',
    NULL,
    'NCT07037628 status NOT_YET_RECRUITING verified 2025-06 accessed 2026-07-16; intervention Not specified; population Spinal Cord Injury, Spinal Cord Injury Thoracic, Spinal Cord Injury/Damage, Spinal Cord Injury T1-L2, Spinal Cord Stimulation (SCS).',
    'not_yet_recruiting',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T065-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P065", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T001", "tracker_id": "M10B-O065"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P065::M10A-T065-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'OTHER'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O065', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT05343130 status RECRUITING verified 2025-06 accessed 2026-07-16; intervention Brain-Computer Interface, Sham Brain-Computer Interface; population Cervical Spinal Cord Injury.',
    'qualitative',
    NULL,
    'NCT05343130 status RECRUITING verified 2025-06 accessed 2026-07-16; intervention Brain-Computer Interface, Sham Brain-Computer Interface; population Cervical Spinal Cord Injury.',
    'recruiting',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T066-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P066", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T002", "tracker_id": "M10B-O066"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P066::M10A-T066-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'DEVICE'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O066', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT04625309 status COMPLETED verified 2021-09 accessed 2026-07-16; intervention Adaptive sports; population Spinal Cord Injuries, Sports Physical Therapy.',
    'qualitative',
    NULL,
    'NCT04625309 status COMPLETED verified 2021-09 accessed 2026-07-16; intervention Adaptive sports; population Spinal Cord Injuries, Sports Physical Therapy.',
    'completed',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T067-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P067", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T003", "tracker_id": "M10B-O067"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P067::M10A-T067-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'OTHER'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O067', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT04387864 status COMPLETED verified 2020-05 accessed 2026-07-16; intervention Whole-body Vibration Device; population Postpolio Syndrome.',
    'qualitative',
    NULL,
    'NCT04387864 status COMPLETED verified 2020-05 accessed 2026-07-16; intervention Whole-body Vibration Device; population Postpolio Syndrome.',
    'completed',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T068-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P068", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T004", "tracker_id": "M10B-O068"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P068::M10A-T068-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'DEVICE'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O068', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT02974673 status TERMINATED verified 2020-06 accessed 2026-07-16; intervention Ejaculatory test; population Spinal Cord Diseases, Disorder of Ejaculation.',
    'qualitative',
    NULL,
    'NCT02974673 status TERMINATED verified 2020-06 accessed 2026-07-16; intervention Ejaculatory test; population Spinal Cord Diseases, Disorder of Ejaculation.',
    'terminated',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T069-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P069", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T005", "tracker_id": "M10B-O069"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P069::M10A-T069-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'PROCEDURE'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O069', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT02381977 status COMPLETED verified 2015-03 accessed 2026-07-16; intervention No intervention; population Cardiac Arrest, Stroke, Traumatic Brain Injury, Brain Mass, Status Epilepticus.',
    'qualitative',
    NULL,
    'NCT02381977 status COMPLETED verified 2015-03 accessed 2026-07-16; intervention No intervention; population Cardiac Arrest, Stroke, Traumatic Brain Injury, Brain Mass, Status Epilepticus.',
    'completed',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T070-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P070", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T006", "tracker_id": "M10B-O070"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P070::M10A-T070-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'OTHER'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O070', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT02315339 status TERMINATED verified 2020-04 accessed 2026-07-16; intervention Not specified; population Pulmonary Disease, Chronic Obstructive, Amyotrophic Lateral Sclerosis, Spinal Cord Injury, Muscular Dystrophies, Obesity Hypoventilation Syndrome.',
    'qualitative',
    NULL,
    'NCT02315339 status TERMINATED verified 2020-04 accessed 2026-07-16; intervention Not specified; population Pulmonary Disease, Chronic Obstructive, Amyotrophic Lateral Sclerosis, Spinal Cord Injury, Muscular Dystrophies, Obesity Hypoventilation Syndrome.',
    'terminated',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T071-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P071", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T007", "tracker_id": "M10B-O071"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P071::M10A-T071-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'OTHER'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O071', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT06543277 status RECRUITING verified 2025-09 accessed 2026-07-16; intervention Transcutaneous Auricular Vagus Nerve Stimulation (taVNS); population Chronic Incomplete Cervical Spinal Cord Injury (SCI).',
    'qualitative',
    NULL,
    'NCT06543277 status RECRUITING verified 2025-09 accessed 2026-07-16; intervention Transcutaneous Auricular Vagus Nerve Stimulation (taVNS); population Chronic Incomplete Cervical Spinal Cord Injury (SCI).',
    'recruiting',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T072-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P072", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T008", "tracker_id": "M10B-O072"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P072::M10A-T072-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'DEVICE'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O072', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT06587841 status RECRUITING verified 2026-02 accessed 2026-07-16; intervention Spinal COrd NEuromodulation™ (SCONE™) for transcutaneous spinal cord stimulation (TSCS); population Spinal Cord Injuries, Bowel Dysfunction, Sexual Dysfunction, Autonomic Dysfunction, Urologic Disorders.',
    'qualitative',
    NULL,
    'NCT06587841 status RECRUITING verified 2026-02 accessed 2026-07-16; intervention Spinal COrd NEuromodulation™ (SCONE™) for transcutaneous spinal cord stimulation (TSCS); population Spinal Cord Injuries, Bowel Dysfunction, Sexual Dysfunction, Autonomic Dysfunction, Urologic Disorders.',
    'recruiting',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T073-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P073", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T001", "tracker_id": "M10B-O073"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P073::M10A-T073-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'DEVICE'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O073', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT07518251 status RECRUITING verified 2026-03 accessed 2026-07-16; intervention Thoracoabdominal aortic aneurysm repair under fCPB, Thoracoabdominal aortic aneurysm repair under LHB; population Thoracoabdominal Aortic Aneurysm, Cardiopulmonary Bypass, Open Repair.',
    'qualitative',
    NULL,
    'NCT07518251 status RECRUITING verified 2026-03 accessed 2026-07-16; intervention Thoracoabdominal aortic aneurysm repair under fCPB, Thoracoabdominal aortic aneurysm repair under LHB; population Thoracoabdominal Aortic Aneurysm, Cardiopulmonary Bypass, Open Repair.',
    'recruiting',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T074-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P074", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T002", "tracker_id": "M10B-O074"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P074::M10A-T074-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'PROCEDURE'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O074', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT04446195 status UNKNOWN verified 2020-06 accessed 2026-07-16; intervention Individualized Intervention; population Bowel Preparation Solutions.',
    'qualitative',
    'behavioral / functional recovery assay',
    'NCT04446195 status UNKNOWN verified 2020-06 accessed 2026-07-16; intervention Individualized Intervention; population Bowel Preparation Solutions.',
    'unknown',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T075-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M10A-P075", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T003", "tracker_id": "M10B-O075"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P075::M10A-T075-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'BEHAVIORAL'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O075', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT03046875 status WITHDRAWN verified 2018-02 accessed 2026-07-16; intervention Transcutaneous Spinal Cord Stimulation, Sham stimulation; population Spinal Cord Injuries.',
    'qualitative',
    NULL,
    'NCT03046875 status WITHDRAWN verified 2018-02 accessed 2026-07-16; intervention Transcutaneous Spinal Cord Stimulation, Sham stimulation; population Spinal Cord Injuries.',
    'withdrawn',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T076-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P076", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T004", "tracker_id": "M10B-O076"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P076::M10A-T076-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'OTHER'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O076', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT02225028 status COMPLETED verified 2017-05 accessed 2026-07-16; intervention Physical Activity Counseling; population Spinal Cord Injury.',
    'qualitative',
    'behavioral / functional recovery assay',
    'NCT02225028 status COMPLETED verified 2017-05 accessed 2026-07-16; intervention Physical Activity Counseling; population Spinal Cord Injury.',
    'completed',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T077-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M10A-P077", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T005", "tracker_id": "M10B-O077"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P077::M10A-T077-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'BEHAVIORAL'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O077', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT01599767 status COMPLETED verified 2020-04 accessed 2026-07-16; intervention Transcranial direct current stimulation (tDCS); population Spinal Cord Injury, Chronic Pain, Neuropathic Pain.',
    'qualitative',
    NULL,
    'NCT01599767 status COMPLETED verified 2020-04 accessed 2026-07-16; intervention Transcranial direct current stimulation (tDCS); population Spinal Cord Injury, Chronic Pain, Neuropathic Pain.',
    'completed',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T078-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P078", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T006", "tracker_id": "M10B-O078"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P078::M10A-T078-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'DEVICE'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O078', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT05065437 status WITHDRAWN verified 2022-06 accessed 2026-07-16; intervention Active (Virtual reality and spinal stimulation); population Tetraplegia.',
    'qualitative',
    NULL,
    'NCT05065437 status WITHDRAWN verified 2022-06 accessed 2026-07-16; intervention Active (Virtual reality and spinal stimulation); population Tetraplegia.',
    'withdrawn',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T079-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P079", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T007", "tracker_id": "M10B-O079"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P079::M10A-T079-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'OTHER'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O079', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NCT02274116 status ACTIVE_NOT_RECRUITING verified 2026-03 accessed 2026-07-16; intervention SHAM - Intermittent Room Air - room air mixture, AIH - Intermittent Hypoxia - hypoxia air mixture; population Spinal Cord Injuries.',
    'qualitative',
    NULL,
    'NCT02274116 status ACTIVE_NOT_RECRUITING verified 2026-03 accessed 2026-07-16; intervention SHAM - Intermittent Room Air - room air mixture, AIH - Intermittent Hypoxia - hypoxia air mixture; population Spinal Cord Injuries.',
    'active_not_recruiting',
    'ClinicalTrials.gov registry',
    'ClinicalTrials.gov registry',
    'medium',
    '{"curator_notes": "Source-page/registry first pass; full extraction queued.", "experiment_tracker_id": "M10A-T080-E001", "measurement_method_inference": null, "paper_tracker_id": "M10A-P080", "quantitative": "YES", "statistics_reported": "Registry status/design fields extracted; results linkage queued", "topic_id": "M10B-T008", "tracker_id": "M10B-O080"}'
  FROM _m10_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M10A-P080::M10A-T080-E001'
    AND et.evidence_type_name = 'Clinical trial registry evidence'
    AND ot.outcome_type_name = 'OTHER'
  RETURNING observation_id
)
INSERT INTO _m10_observation_map (tracker_id, observation_id) SELECT 'M10B-O080', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Trial status currency requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 10A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M10A-P001", "topic_id": "M10B-T001", "tracker_id": "M10B-C001"}'
  FROM _m10_paper_map p
  WHERE p.tracker_id = 'M10A-P001'
  RETURNING claim_id
)
INSERT INTO _m10_claim_map (tracker_id, claim_id) SELECT 'M10B-C001', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Safety/feasibility versus efficacy requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 10A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M10A-P002", "topic_id": "M10B-T002", "tracker_id": "M10B-C002"}'
  FROM _m10_paper_map p
  WHERE p.tracker_id = 'M10A-P002'
  RETURNING claim_id
)
INSERT INTO _m10_claim_map (tracker_id, claim_id) SELECT 'M10B-C002', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Registry-publication result linkage requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 10A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M10A-P003", "topic_id": "M10B-T003", "tracker_id": "M10B-C003"}'
  FROM _m10_paper_map p
  WHERE p.tracker_id = 'M10A-P003'
  RETURNING claim_id
)
INSERT INTO _m10_claim_map (tracker_id, claim_id) SELECT 'M10B-C003', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Intervention-class ontology requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 10A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M10A-P004", "topic_id": "M10B-T004", "tracker_id": "M10B-C004"}'
  FROM _m10_paper_map p
  WHERE p.tracker_id = 'M10A-P004'
  RETURNING claim_id
)
INSERT INTO _m10_claim_map (tracker_id, claim_id) SELECT 'M10B-C004', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'SCI population boundaries requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 10A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M10A-P005", "topic_id": "M10B-T005", "tracker_id": "M10B-C005"}'
  FROM _m10_paper_map p
  WHERE p.tracker_id = 'M10A-P005'
  RETURNING claim_id
)
INSERT INTO _m10_claim_map (tracker_id, claim_id) SELECT 'M10B-C005', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Terminated/withdrawn trial interpretation requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 10A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M10A-P006", "topic_id": "M10B-T006", "tracker_id": "M10B-C006"}'
  FROM _m10_paper_map p
  WHERE p.tracker_id = 'M10A-P006'
  RETURNING claim_id
)
INSERT INTO _m10_claim_map (tracker_id, claim_id) SELECT 'M10B-C006', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Endpoint-family separation requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 10A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M10A-P007", "topic_id": "M10B-T007", "tracker_id": "M10B-C007"}'
  FROM _m10_paper_map p
  WHERE p.tracker_id = 'M10A-P007'
  RETURNING claim_id
)
INSERT INTO _m10_claim_map (tracker_id, claim_id) SELECT 'M10B-C007', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Clinical translation evidence tier requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 10A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M10A-P008", "topic_id": "M10B-T008", "tracker_id": "M10B-C008"}'
  FROM _m10_paper_map p
  WHERE p.tracker_id = 'M10A-P008'
  RETURNING claim_id
)
INSERT INTO _m10_claim_map (tracker_id, claim_id) SELECT 'M10B-C008', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Trial status currency requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 10A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M10A-P009", "topic_id": "M10B-T001", "tracker_id": "M10B-C009"}'
  FROM _m10_paper_map p
  WHERE p.tracker_id = 'M10A-P009'
  RETURNING claim_id
)
INSERT INTO _m10_claim_map (tracker_id, claim_id) SELECT 'M10B-C009', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Safety/feasibility versus efficacy requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 10A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M10A-P010", "topic_id": "M10B-T002", "tracker_id": "M10B-C010"}'
  FROM _m10_paper_map p
  WHERE p.tracker_id = 'M10A-P010'
  RETURNING claim_id
)
INSERT INTO _m10_claim_map (tracker_id, claim_id) SELECT 'M10B-C010', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Registry-publication result linkage requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 10A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M10A-P011", "topic_id": "M10B-T003", "tracker_id": "M10B-C011"}'
  FROM _m10_paper_map p
  WHERE p.tracker_id = 'M10A-P011'
  RETURNING claim_id
)
INSERT INTO _m10_claim_map (tracker_id, claim_id) SELECT 'M10B-C011', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Intervention-class ontology requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 10A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M10A-P012", "topic_id": "M10B-T004", "tracker_id": "M10B-C012"}'
  FROM _m10_paper_map p
  WHERE p.tracker_id = 'M10A-P012'
  RETURNING claim_id
)
INSERT INTO _m10_claim_map (tracker_id, claim_id) SELECT 'M10B-C012', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'SCI population boundaries requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 10A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M10A-P013", "topic_id": "M10B-T005", "tracker_id": "M10B-C013"}'
  FROM _m10_paper_map p
  WHERE p.tracker_id = 'M10A-P013'
  RETURNING claim_id
)
INSERT INTO _m10_claim_map (tracker_id, claim_id) SELECT 'M10B-C013', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Terminated/withdrawn trial interpretation requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 10A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M10A-P014", "topic_id": "M10B-T006", "tracker_id": "M10B-C014"}'
  FROM _m10_paper_map p
  WHERE p.tracker_id = 'M10A-P014'
  RETURNING claim_id
)
INSERT INTO _m10_claim_map (tracker_id, claim_id) SELECT 'M10B-C014', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Endpoint-family separation requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 10A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M10A-P015", "topic_id": "M10B-T007", "tracker_id": "M10B-C015"}'
  FROM _m10_paper_map p
  WHERE p.tracker_id = 'M10A-P015'
  RETURNING claim_id
)
INSERT INTO _m10_claim_map (tracker_id, claim_id) SELECT 'M10B-C015', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Clinical translation evidence tier requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 10A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M10A-P016", "topic_id": "M10B-T008", "tracker_id": "M10B-C016"}'
  FROM _m10_paper_map p
  WHERE p.tracker_id = 'M10A-P016'
  RETURNING claim_id
)
INSERT INTO _m10_claim_map (tracker_id, claim_id) SELECT 'M10B-C016', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Trial status currency requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 10A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M10A-P017", "topic_id": "M10B-T001", "tracker_id": "M10B-C017"}'
  FROM _m10_paper_map p
  WHERE p.tracker_id = 'M10A-P017'
  RETURNING claim_id
)
INSERT INTO _m10_claim_map (tracker_id, claim_id) SELECT 'M10B-C017', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Safety/feasibility versus efficacy requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 10A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M10A-P018", "topic_id": "M10B-T002", "tracker_id": "M10B-C018"}'
  FROM _m10_paper_map p
  WHERE p.tracker_id = 'M10A-P018'
  RETURNING claim_id
)
INSERT INTO _m10_claim_map (tracker_id, claim_id) SELECT 'M10B-C018', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Registry-publication result linkage requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 10A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M10A-P019", "topic_id": "M10B-T003", "tracker_id": "M10B-C019"}'
  FROM _m10_paper_map p
  WHERE p.tracker_id = 'M10A-P019'
  RETURNING claim_id
)
INSERT INTO _m10_claim_map (tracker_id, claim_id) SELECT 'M10B-C019', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Intervention-class ontology requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 10A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M10A-P020", "topic_id": "M10B-T004", "tracker_id": "M10B-C020"}'
  FROM _m10_paper_map p
  WHERE p.tracker_id = 'M10A-P020'
  RETURNING claim_id
)
INSERT INTO _m10_claim_map (tracker_id, claim_id) SELECT 'M10B-C020', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'SCI population boundaries requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 10A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M10A-P021", "topic_id": "M10B-T005", "tracker_id": "M10B-C021"}'
  FROM _m10_paper_map p
  WHERE p.tracker_id = 'M10A-P021'
  RETURNING claim_id
)
INSERT INTO _m10_claim_map (tracker_id, claim_id) SELECT 'M10B-C021', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Terminated/withdrawn trial interpretation requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 10A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M10A-P022", "topic_id": "M10B-T006", "tracker_id": "M10B-C022"}'
  FROM _m10_paper_map p
  WHERE p.tracker_id = 'M10A-P022'
  RETURNING claim_id
)
INSERT INTO _m10_claim_map (tracker_id, claim_id) SELECT 'M10B-C022', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Endpoint-family separation requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 10A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M10A-P023", "topic_id": "M10B-T007", "tracker_id": "M10B-C023"}'
  FROM _m10_paper_map p
  WHERE p.tracker_id = 'M10A-P023'
  RETURNING claim_id
)
INSERT INTO _m10_claim_map (tracker_id, claim_id) SELECT 'M10B-C023', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Clinical translation evidence tier requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 10A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M10A-P024", "topic_id": "M10B-T008", "tracker_id": "M10B-C024"}'
  FROM _m10_paper_map p
  WHERE p.tracker_id = 'M10A-P024'
  RETURNING claim_id
)
INSERT INTO _m10_claim_map (tracker_id, claim_id) SELECT 'M10B-C024', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Trial status currency requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 10A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M10A-P025", "topic_id": "M10B-T001", "tracker_id": "M10B-C025"}'
  FROM _m10_paper_map p
  WHERE p.tracker_id = 'M10A-P025'
  RETURNING claim_id
)
INSERT INTO _m10_claim_map (tracker_id, claim_id) SELECT 'M10B-C025', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Safety/feasibility versus efficacy requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 10A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M10A-P026", "topic_id": "M10B-T002", "tracker_id": "M10B-C026"}'
  FROM _m10_paper_map p
  WHERE p.tracker_id = 'M10A-P026'
  RETURNING claim_id
)
INSERT INTO _m10_claim_map (tracker_id, claim_id) SELECT 'M10B-C026', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Registry-publication result linkage requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 10A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M10A-P027", "topic_id": "M10B-T003", "tracker_id": "M10B-C027"}'
  FROM _m10_paper_map p
  WHERE p.tracker_id = 'M10A-P027'
  RETURNING claim_id
)
INSERT INTO _m10_claim_map (tracker_id, claim_id) SELECT 'M10B-C027', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Intervention-class ontology requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 10A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M10A-P028", "topic_id": "M10B-T004", "tracker_id": "M10B-C028"}'
  FROM _m10_paper_map p
  WHERE p.tracker_id = 'M10A-P028'
  RETURNING claim_id
)
INSERT INTO _m10_claim_map (tracker_id, claim_id) SELECT 'M10B-C028', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'SCI population boundaries requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 10A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M10A-P029", "topic_id": "M10B-T005", "tracker_id": "M10B-C029"}'
  FROM _m10_paper_map p
  WHERE p.tracker_id = 'M10A-P029'
  RETURNING claim_id
)
INSERT INTO _m10_claim_map (tracker_id, claim_id) SELECT 'M10B-C029', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Terminated/withdrawn trial interpretation requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 10A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M10A-P030", "topic_id": "M10B-T006", "tracker_id": "M10B-C030"}'
  FROM _m10_paper_map p
  WHERE p.tracker_id = 'M10A-P030'
  RETURNING claim_id
)
INSERT INTO _m10_claim_map (tracker_id, claim_id) SELECT 'M10B-C030', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Endpoint-family separation requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 10A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M10A-P031", "topic_id": "M10B-T007", "tracker_id": "M10B-C031"}'
  FROM _m10_paper_map p
  WHERE p.tracker_id = 'M10A-P031'
  RETURNING claim_id
)
INSERT INTO _m10_claim_map (tracker_id, claim_id) SELECT 'M10B-C031', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Clinical translation evidence tier requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 10A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M10A-P032", "topic_id": "M10B-T008", "tracker_id": "M10B-C032"}'
  FROM _m10_paper_map p
  WHERE p.tracker_id = 'M10A-P032'
  RETURNING claim_id
)
INSERT INTO _m10_claim_map (tracker_id, claim_id) SELECT 'M10B-C032', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Trial status currency requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 10A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M10A-P033", "topic_id": "M10B-T001", "tracker_id": "M10B-C033"}'
  FROM _m10_paper_map p
  WHERE p.tracker_id = 'M10A-P033'
  RETURNING claim_id
)
INSERT INTO _m10_claim_map (tracker_id, claim_id) SELECT 'M10B-C033', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Safety/feasibility versus efficacy requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 10A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M10A-P034", "topic_id": "M10B-T002", "tracker_id": "M10B-C034"}'
  FROM _m10_paper_map p
  WHERE p.tracker_id = 'M10A-P034'
  RETURNING claim_id
)
INSERT INTO _m10_claim_map (tracker_id, claim_id) SELECT 'M10B-C034', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Registry-publication result linkage requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 10A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M10A-P035", "topic_id": "M10B-T003", "tracker_id": "M10B-C035"}'
  FROM _m10_paper_map p
  WHERE p.tracker_id = 'M10A-P035'
  RETURNING claim_id
)
INSERT INTO _m10_claim_map (tracker_id, claim_id) SELECT 'M10B-C035', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Intervention-class ontology requires preserved source, population/model, timing, and endpoint boundaries before synthesis.',
    'synthesis',
    'medium',
    'Module 10A tracker / source metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full-text/results linkage needed for strength claims.", "source_paper_tracker_id": "M10A-P036", "topic_id": "M10B-T004", "tracker_id": "M10B-C036"}'
  FROM _m10_paper_map p
  WHERE p.tracker_id = 'M10A-P036'
  RETURNING claim_id
)
INSERT INTO _m10_claim_map (tracker_id, claim_id) SELECT 'M10B-C036', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M10B-L001"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O001'
  WHERE c.tracker_id = 'M10B-C001'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L001', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M10B-L002"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O002'
  WHERE c.tracker_id = 'M10B-C002'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L002', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M10B-L003"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O003'
  WHERE c.tracker_id = 'M10B-C003'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L003', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M10B-L004"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O004'
  WHERE c.tracker_id = 'M10B-C004'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L004', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M10B-L005"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O005'
  WHERE c.tracker_id = 'M10B-C005'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L005', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M10B-L006"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O006'
  WHERE c.tracker_id = 'M10B-C006'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L006', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M10B-L007"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O007'
  WHERE c.tracker_id = 'M10B-C007'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L007', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M10B-L008"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O008'
  WHERE c.tracker_id = 'M10B-C008'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L008', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M10B-L009"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O009'
  WHERE c.tracker_id = 'M10B-C009'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L009', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M10B-L010"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O010'
  WHERE c.tracker_id = 'M10B-C010'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L010', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M10B-L011"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O011'
  WHERE c.tracker_id = 'M10B-C011'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L011', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M10B-L012"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O012'
  WHERE c.tracker_id = 'M10B-C012'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L012', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M10B-L013"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O013'
  WHERE c.tracker_id = 'M10B-C013'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L013', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M10B-L014"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O014'
  WHERE c.tracker_id = 'M10B-C014'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L014', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M10B-L015"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O015'
  WHERE c.tracker_id = 'M10B-C015'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L015', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M10B-L016"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O016'
  WHERE c.tracker_id = 'M10B-C016'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L016', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M10B-L017"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O017'
  WHERE c.tracker_id = 'M10B-C017'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L017', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M10B-L018"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O018'
  WHERE c.tracker_id = 'M10B-C018'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L018', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M10B-L019"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O019'
  WHERE c.tracker_id = 'M10B-C019'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L019', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M10B-L020"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O020'
  WHERE c.tracker_id = 'M10B-C020'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L020', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M10B-L021"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O021'
  WHERE c.tracker_id = 'M10B-C021'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L021', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M10B-L022"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O022'
  WHERE c.tracker_id = 'M10B-C022'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L022', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M10B-L023"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O023'
  WHERE c.tracker_id = 'M10B-C023'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L023', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M10B-L024"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O024'
  WHERE c.tracker_id = 'M10B-C024'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L024', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M10B-L025"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O025'
  WHERE c.tracker_id = 'M10B-C025'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L025', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M10B-L026"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O026'
  WHERE c.tracker_id = 'M10B-C026'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L026', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M10B-L027"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O027'
  WHERE c.tracker_id = 'M10B-C027'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L027', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M10B-L028"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O028'
  WHERE c.tracker_id = 'M10B-C028'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L028', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M10B-L029"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O029'
  WHERE c.tracker_id = 'M10B-C029'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L029', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M10B-L030"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O030'
  WHERE c.tracker_id = 'M10B-C030'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L030', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M10B-L031"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O031'
  WHERE c.tracker_id = 'M10B-C031'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L031', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M10B-L032"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O032'
  WHERE c.tracker_id = 'M10B-C032'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L032', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M10B-L033"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O033'
  WHERE c.tracker_id = 'M10B-C033'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L033', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M10B-L034"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O034'
  WHERE c.tracker_id = 'M10B-C034'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L034', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M10B-L035"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O035'
  WHERE c.tracker_id = 'M10B-C035'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L035', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "medium", "tracker_id": "M10B-L036"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O036'
  WHERE c.tracker_id = 'M10B-C036'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L036', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L037"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O037'
  WHERE c.tracker_id = 'M10B-C001'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L037', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L038"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O038'
  WHERE c.tracker_id = 'M10B-C002'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L038', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L039"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O039'
  WHERE c.tracker_id = 'M10B-C003'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L039', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L040"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O040'
  WHERE c.tracker_id = 'M10B-C004'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L040', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L041"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O041'
  WHERE c.tracker_id = 'M10B-C005'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L041', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L042"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O042'
  WHERE c.tracker_id = 'M10B-C006'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L042', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L043"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O043'
  WHERE c.tracker_id = 'M10B-C007'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L043', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L044"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O044'
  WHERE c.tracker_id = 'M10B-C008'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L044', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L045"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O045'
  WHERE c.tracker_id = 'M10B-C009'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L045', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L046"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O046'
  WHERE c.tracker_id = 'M10B-C010'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L046', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L047"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O047'
  WHERE c.tracker_id = 'M10B-C011'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L047', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L048"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O048'
  WHERE c.tracker_id = 'M10B-C012'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L048', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L049"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O049'
  WHERE c.tracker_id = 'M10B-C013'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L049', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L050"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O050'
  WHERE c.tracker_id = 'M10B-C014'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L050', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L051"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O051'
  WHERE c.tracker_id = 'M10B-C015'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L051', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L052"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O052'
  WHERE c.tracker_id = 'M10B-C016'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L052', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L053"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O053'
  WHERE c.tracker_id = 'M10B-C017'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L053', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L054"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O054'
  WHERE c.tracker_id = 'M10B-C018'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L054', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L055"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O055'
  WHERE c.tracker_id = 'M10B-C019'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L055', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L056"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O056'
  WHERE c.tracker_id = 'M10B-C020'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L056', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L057"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O057'
  WHERE c.tracker_id = 'M10B-C021'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L057', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L058"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O058'
  WHERE c.tracker_id = 'M10B-C022'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L058', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L059"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O059'
  WHERE c.tracker_id = 'M10B-C023'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L059', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L060"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O060'
  WHERE c.tracker_id = 'M10B-C024'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L060', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L061"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O061'
  WHERE c.tracker_id = 'M10B-C025'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L061', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L062"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O062'
  WHERE c.tracker_id = 'M10B-C026'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L062', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L063"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O063'
  WHERE c.tracker_id = 'M10B-C027'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L063', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L064"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O064'
  WHERE c.tracker_id = 'M10B-C028'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L064', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L065"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O065'
  WHERE c.tracker_id = 'M10B-C029'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L065', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L066"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O066'
  WHERE c.tracker_id = 'M10B-C030'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L066', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L067"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O067'
  WHERE c.tracker_id = 'M10B-C031'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L067', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L068"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O068'
  WHERE c.tracker_id = 'M10B-C032'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L068', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L069"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O069'
  WHERE c.tracker_id = 'M10B-C033'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L069', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L070"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O070'
  WHERE c.tracker_id = 'M10B-C034'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L070', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L071"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O071'
  WHERE c.tracker_id = 'M10B-C035'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L071', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L072"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O072'
  WHERE c.tracker_id = 'M10B-C036'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L072', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L073"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O073'
  WHERE c.tracker_id = 'M10B-C001'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L073', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L074"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O074'
  WHERE c.tracker_id = 'M10B-C002'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L074', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L075"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O075'
  WHERE c.tracker_id = 'M10B-C003'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L075', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L076"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O076'
  WHERE c.tracker_id = 'M10B-C004'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L076', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L077"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O077'
  WHERE c.tracker_id = 'M10B-C005'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L077', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L078"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O078'
  WHERE c.tracker_id = 'M10B-C006'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L078', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L079"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O079'
  WHERE c.tracker_id = 'M10B-C007'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L079', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L080"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O080'
  WHERE c.tracker_id = 'M10B-C008'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L080', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L081"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O001'
  WHERE c.tracker_id = 'M10B-C009'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L081', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L082"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O002'
  WHERE c.tracker_id = 'M10B-C010'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L082', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L083"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O003'
  WHERE c.tracker_id = 'M10B-C011'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L083', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L084"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O004'
  WHERE c.tracker_id = 'M10B-C012'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L084', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L085"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O005'
  WHERE c.tracker_id = 'M10B-C013'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L085', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L086"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O006'
  WHERE c.tracker_id = 'M10B-C014'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L086', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L087"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O007'
  WHERE c.tracker_id = 'M10B-C015'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L087', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L088"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O008'
  WHERE c.tracker_id = 'M10B-C016'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L088', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L089"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O009'
  WHERE c.tracker_id = 'M10B-C017'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L089', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L090"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O010'
  WHERE c.tracker_id = 'M10B-C018'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L090', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L091"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O011'
  WHERE c.tracker_id = 'M10B-C019'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L091', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L092"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O012'
  WHERE c.tracker_id = 'M10B-C020'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L092', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L093"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O013'
  WHERE c.tracker_id = 'M10B-C021'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L093', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L094"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O014'
  WHERE c.tracker_id = 'M10B-C022'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L094', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L095"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O015'
  WHERE c.tracker_id = 'M10B-C023'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L095', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L096"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O016'
  WHERE c.tracker_id = 'M10B-C024'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L096', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L097"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O017'
  WHERE c.tracker_id = 'M10B-C025'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L097', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L098"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O018'
  WHERE c.tracker_id = 'M10B-C026'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L098', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L099"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O019'
  WHERE c.tracker_id = 'M10B-C027'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L099', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L100"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O020'
  WHERE c.tracker_id = 'M10B-C028'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L100', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L101"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O021'
  WHERE c.tracker_id = 'M10B-C029'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L101', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L102"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O022'
  WHERE c.tracker_id = 'M10B-C030'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L102', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L103"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O023'
  WHERE c.tracker_id = 'M10B-C031'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L103', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L104"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O024'
  WHERE c.tracker_id = 'M10B-C032'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L104', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L105"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O025'
  WHERE c.tracker_id = 'M10B-C033'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L105', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L106"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O026'
  WHERE c.tracker_id = 'M10B-C034'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L106', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L107"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O027'
  WHERE c.tracker_id = 'M10B-C035'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L107', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L108"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O028'
  WHERE c.tracker_id = 'M10B-C036'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L108', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L109"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O029'
  WHERE c.tracker_id = 'M10B-C001'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L109', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L110"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O030'
  WHERE c.tracker_id = 'M10B-C002'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L110', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L111"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O031'
  WHERE c.tracker_id = 'M10B-C003'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L111', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L112"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O032'
  WHERE c.tracker_id = 'M10B-C004'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L112', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L113"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O033'
  WHERE c.tracker_id = 'M10B-C005'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L113', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L114"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O034'
  WHERE c.tracker_id = 'M10B-C006'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L114', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L115"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O035'
  WHERE c.tracker_id = 'M10B-C007'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L115', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "First-pass evidence link preserving source-level confidence.", "strength": "low", "tracker_id": "M10B-L116"}'
  FROM _m10_claim_map c
  JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O036'
  WHERE c.tracker_id = 'M10B-C008'
  RETURNING link_id
)
INSERT INTO _m10_link_map (tracker_id, link_id) SELECT 'M10B-L116', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'SCI clinical-trial evidence must preserve registry status and verification date because recruiting, active, completed, terminated, withdrawn, unknown, and results-posted trials carry different evidentiary meanings.',
    'M10B-T001',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M10B-B001", "M10B-B002", "M10B-B003", "M10B-B004", "M10B-B005", "M10B-B006", "M10B-B007", "M10B-B008"], "claim_tracker_ids": ["M10B-C001", "M10B-C002", "M10B-C003"], "consensus_draft_id": "M10B-S001", "observation_tracker_ids": ["M10B-O001", "M10B-O002", "M10B-O003", "M10B-O004", "M10B-O005", "M10B-O006", "M10B-O007", "M10B-O008", "M10B-O009", "M10B-O010"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 10 first-pass curation freeze.", "topic_id": "M10B-T001"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m10_consensus_map (tracker_id, consensus_id) SELECT 'M10B-S001', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O001'
WHERE c.tracker_id = 'M10B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O002'
WHERE c.tracker_id = 'M10B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O003'
WHERE c.tracker_id = 'M10B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O004'
WHERE c.tracker_id = 'M10B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O005'
WHERE c.tracker_id = 'M10B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O006'
WHERE c.tracker_id = 'M10B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O007'
WHERE c.tracker_id = 'M10B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O008'
WHERE c.tracker_id = 'M10B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O009'
WHERE c.tracker_id = 'M10B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O010'
WHERE c.tracker_id = 'M10B-S001';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Most SCI trials in the registry-first corpus should be interpreted initially as safety, feasibility, dosing, device, rehabilitation, or endpoint-development evidence unless controlled results support efficacy.',
    'M10B-T002',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M10B-B001", "M10B-B002", "M10B-B003", "M10B-B004", "M10B-B005", "M10B-B006", "M10B-B007", "M10B-B008"], "claim_tracker_ids": ["M10B-C004", "M10B-C005", "M10B-C006"], "consensus_draft_id": "M10B-S002", "observation_tracker_ids": ["M10B-O011", "M10B-O012", "M10B-O013", "M10B-O014", "M10B-O015", "M10B-O016", "M10B-O017", "M10B-O018", "M10B-O019", "M10B-O020"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 10 first-pass curation freeze.", "topic_id": "M10B-T002"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m10_consensus_map (tracker_id, consensus_id) SELECT 'M10B-S002', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O011'
WHERE c.tracker_id = 'M10B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O012'
WHERE c.tracker_id = 'M10B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O013'
WHERE c.tracker_id = 'M10B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O014'
WHERE c.tracker_id = 'M10B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O015'
WHERE c.tracker_id = 'M10B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O016'
WHERE c.tracker_id = 'M10B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O017'
WHERE c.tracker_id = 'M10B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O018'
WHERE c.tracker_id = 'M10B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O019'
WHERE c.tracker_id = 'M10B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O020'
WHERE c.tracker_id = 'M10B-S002';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Registry records are not equivalent to published outcomes; each trial needs linkage to results postings, publications, intervention details, sample size, comparator, and endpoint definitions before quantitative clinical synthesis.',
    'M10B-T003',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M10B-B001", "M10B-B002", "M10B-B003", "M10B-B004", "M10B-B005", "M10B-B006", "M10B-B007", "M10B-B008"], "claim_tracker_ids": ["M10B-C007", "M10B-C008", "M10B-C009"], "consensus_draft_id": "M10B-S003", "observation_tracker_ids": ["M10B-O021", "M10B-O022", "M10B-O023", "M10B-O024", "M10B-O025", "M10B-O026", "M10B-O027", "M10B-O028", "M10B-O029", "M10B-O030"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 10 first-pass curation freeze.", "topic_id": "M10B-T003"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m10_consensus_map (tracker_id, consensus_id) SELECT 'M10B-S003', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O021'
WHERE c.tracker_id = 'M10B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O022'
WHERE c.tracker_id = 'M10B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O023'
WHERE c.tracker_id = 'M10B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O024'
WHERE c.tracker_id = 'M10B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O025'
WHERE c.tracker_id = 'M10B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O026'
WHERE c.tracker_id = 'M10B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O027'
WHERE c.tracker_id = 'M10B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O028'
WHERE c.tracker_id = 'M10B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O029'
WHERE c.tracker_id = 'M10B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O030'
WHERE c.tracker_id = 'M10B-S003';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Intervention-class ontology is essential for clinical synthesis because cells, devices, drugs, rehabilitation, stimulation, surgery, biologics, behavioral interventions, and observational protocols answer different translational questions.',
    'M10B-T004',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M10B-B001", "M10B-B002", "M10B-B003", "M10B-B004", "M10B-B005", "M10B-B006", "M10B-B007", "M10B-B008"], "claim_tracker_ids": ["M10B-C010", "M10B-C011", "M10B-C012"], "consensus_draft_id": "M10B-S004", "observation_tracker_ids": ["M10B-O031", "M10B-O032", "M10B-O033", "M10B-O034", "M10B-O035", "M10B-O036", "M10B-O037", "M10B-O038", "M10B-O039", "M10B-O040"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 10 first-pass curation freeze.", "topic_id": "M10B-T004"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m10_consensus_map (tracker_id, consensus_id) SELECT 'M10B-S004', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O031'
WHERE c.tracker_id = 'M10B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O032'
WHERE c.tracker_id = 'M10B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O033'
WHERE c.tracker_id = 'M10B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O034'
WHERE c.tracker_id = 'M10B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O035'
WHERE c.tracker_id = 'M10B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O036'
WHERE c.tracker_id = 'M10B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O037'
WHERE c.tracker_id = 'M10B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O038'
WHERE c.tracker_id = 'M10B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O039'
WHERE c.tracker_id = 'M10B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O040'
WHERE c.tracker_id = 'M10B-S004';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'SCI clinical-trial rows must retain population boundaries, including traumatic versus nontraumatic injury, acute versus chronic stage, complete versus incomplete injury, neurological level, age, comorbidity, and whether SCI is the primary condition.',
    'M10B-T005',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M10B-B001", "M10B-B002", "M10B-B003", "M10B-B004", "M10B-B005", "M10B-B006", "M10B-B007", "M10B-B008"], "claim_tracker_ids": ["M10B-C013", "M10B-C014", "M10B-C015"], "consensus_draft_id": "M10B-S005", "observation_tracker_ids": ["M10B-O041", "M10B-O042", "M10B-O043", "M10B-O044", "M10B-O045", "M10B-O046", "M10B-O047", "M10B-O048", "M10B-O049", "M10B-O050"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 10 first-pass curation freeze.", "topic_id": "M10B-T005"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m10_consensus_map (tracker_id, consensus_id) SELECT 'M10B-S005', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O041'
WHERE c.tracker_id = 'M10B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O042'
WHERE c.tracker_id = 'M10B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O043'
WHERE c.tracker_id = 'M10B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O044'
WHERE c.tracker_id = 'M10B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O045'
WHERE c.tracker_id = 'M10B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O046'
WHERE c.tracker_id = 'M10B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O047'
WHERE c.tracker_id = 'M10B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O048'
WHERE c.tracker_id = 'M10B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O049'
WHERE c.tracker_id = 'M10B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O050'
WHERE c.tracker_id = 'M10B-S005';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Terminated, withdrawn, suspended, and unknown-status trials are informative about feasibility and translation risk, but they should not be treated as negative efficacy evidence without documented reasons and outcome data.',
    'M10B-T006',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M10B-B001", "M10B-B002", "M10B-B003", "M10B-B004", "M10B-B005", "M10B-B006", "M10B-B007", "M10B-B008"], "claim_tracker_ids": ["M10B-C016", "M10B-C017", "M10B-C018"], "consensus_draft_id": "M10B-S006", "observation_tracker_ids": ["M10B-O051", "M10B-O052", "M10B-O053", "M10B-O054", "M10B-O055", "M10B-O056", "M10B-O057", "M10B-O058", "M10B-O059", "M10B-O060"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 10 first-pass curation freeze.", "topic_id": "M10B-T006"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m10_consensus_map (tracker_id, consensus_id) SELECT 'M10B-S006', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O051'
WHERE c.tracker_id = 'M10B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O052'
WHERE c.tracker_id = 'M10B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O053'
WHERE c.tracker_id = 'M10B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O054'
WHERE c.tracker_id = 'M10B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O055'
WHERE c.tracker_id = 'M10B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O056'
WHERE c.tracker_id = 'M10B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O057'
WHERE c.tracker_id = 'M10B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O058'
WHERE c.tracker_id = 'M10B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O059'
WHERE c.tracker_id = 'M10B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O060'
WHERE c.tracker_id = 'M10B-S006';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Clinical endpoints should be grouped by functional domain and evidence role: safety, adverse events, AIS or motor scores, walking, hand function, bladder, pain, autonomic function, quality of life, imaging, biomarkers, and device performance require separate synthesis fields.',
    'M10B-T007',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M10B-B001", "M10B-B002", "M10B-B003", "M10B-B004", "M10B-B005", "M10B-B006", "M10B-B007", "M10B-B008"], "claim_tracker_ids": ["M10B-C019", "M10B-C020", "M10B-C021"], "consensus_draft_id": "M10B-S007", "observation_tracker_ids": ["M10B-O061", "M10B-O062", "M10B-O063", "M10B-O064", "M10B-O065", "M10B-O066", "M10B-O067", "M10B-O068", "M10B-O069", "M10B-O070"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 10 first-pass curation freeze.", "topic_id": "M10B-T007"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m10_consensus_map (tracker_id, consensus_id) SELECT 'M10B-S007', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O061'
WHERE c.tracker_id = 'M10B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O062'
WHERE c.tracker_id = 'M10B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O063'
WHERE c.tracker_id = 'M10B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O064'
WHERE c.tracker_id = 'M10B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O065'
WHERE c.tracker_id = 'M10B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O066'
WHERE c.tracker_id = 'M10B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O067'
WHERE c.tracker_id = 'M10B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O068'
WHERE c.tracker_id = 'M10B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O069'
WHERE c.tracker_id = 'M10B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O070'
WHERE c.tracker_id = 'M10B-S007';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Module 10 should serve as the clinical translation map for the database: it can identify what has reached humans and where evidence is thin, but causal or efficacy claims require linked results and intervention-specific review.',
    'M10B-T008',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M10B-B001", "M10B-B002", "M10B-B003", "M10B-B004", "M10B-B005", "M10B-B006", "M10B-B007", "M10B-B008"], "claim_tracker_ids": ["M10B-C022", "M10B-C023", "M10B-C024"], "consensus_draft_id": "M10B-S008", "observation_tracker_ids": ["M10B-O071", "M10B-O072", "M10B-O073", "M10B-O074", "M10B-O075", "M10B-O076", "M10B-O077", "M10B-O078", "M10B-O079", "M10B-O080"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "Module 10 first-pass curation freeze.", "topic_id": "M10B-T008"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m10_consensus_map (tracker_id, consensus_id) SELECT 'M10B-S008', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O071'
WHERE c.tracker_id = 'M10B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O072'
WHERE c.tracker_id = 'M10B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O073'
WHERE c.tracker_id = 'M10B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O074'
WHERE c.tracker_id = 'M10B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O075'
WHERE c.tracker_id = 'M10B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O076'
WHERE c.tracker_id = 'M10B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O077'
WHERE c.tracker_id = 'M10B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O078'
WHERE c.tracker_id = 'M10B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O079'
WHERE c.tracker_id = 'M10B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m10_consensus_map c
JOIN _m10_observation_map o ON o.tracker_id = 'M10B-O080'
WHERE c.tracker_id = 'M10B-S008';

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
  SELECT COUNT(*) INTO paper_count FROM _m10_paper_map;
  SELECT COUNT(*) INTO experiment_count FROM _m10_experiment_map;
  SELECT COUNT(*) INTO observation_count FROM _m10_observation_map;
  SELECT COUNT(*) INTO claim_count FROM _m10_claim_map;
  SELECT COUNT(*) INTO link_count FROM _m10_link_map;
  SELECT COUNT(*) INTO consensus_count FROM _m10_consensus_map;
  SELECT COUNT(*) INTO consensus_observation_count
  FROM Consensus_Observation co
  JOIN _m10_consensus_map cm ON cm.consensus_id = co.consensus_id;
  IF paper_count <> 80 THEN RAISE EXCEPTION 'Expected 80 papers, found %', paper_count; END IF;
  IF experiment_count <> 80 THEN RAISE EXCEPTION 'Unexpected experiment count %', experiment_count; END IF;
  IF observation_count <> 80 THEN RAISE EXCEPTION 'Expected 80 observations, found %', observation_count; END IF;
  IF claim_count <> 36 THEN RAISE EXCEPTION 'Expected 36 claims, found %', claim_count; END IF;
  IF link_count <> 116 THEN RAISE EXCEPTION 'Expected 116 evidence links, found %', link_count; END IF;
  IF consensus_count <> 8 THEN RAISE EXCEPTION 'Expected 8 consensus rows, found %', consensus_count; END IF;
  IF consensus_observation_count <> 80 THEN RAISE EXCEPTION 'Unexpected consensus-observation count %', consensus_observation_count; END IF;
END $$;

COMMIT;
