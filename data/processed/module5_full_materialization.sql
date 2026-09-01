-- Module 5B full first-pass materialization generated from tracker-derived JSON.
-- This script is intended for a fresh database loaded with schema/schema.sql and scripts/seed_controlled_vocab.sql.
BEGIN;

CREATE TEMP TABLE _m5_paper_map (tracker_id TEXT PRIMARY KEY, paper_id INTEGER NOT NULL);
CREATE TEMP TABLE _m5_paradigm_map (tracker_id TEXT PRIMARY KEY, paradigm_id INTEGER NOT NULL);
CREATE TEMP TABLE _m5_experiment_map (tracker_id TEXT PRIMARY KEY, experiment_id INTEGER NOT NULL);
CREATE TEMP TABLE _m5_observation_map (tracker_id TEXT PRIMARY KEY, observation_id INTEGER NOT NULL);
CREATE TEMP TABLE _m5_claim_map (tracker_id TEXT PRIMARY KEY, claim_id INTEGER NOT NULL);
CREATE TEMP TABLE _m5_link_map (tracker_id TEXT PRIMARY KEY, link_id INTEGER NOT NULL);
CREATE TEMP TABLE _m5_consensus_map (tracker_id TEXT PRIMARY KEY, consensus_id INTEGER NOT NULL);

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Axon regeneration through scars and into sites of chronic spinal cord injury', 'Lu P', 2007,
    NULL, NULL, NULL,
    NULL, NULL, '17014846',
    NULL, '{"curator_notes": "Chronic scar axon-regeneration anchor; no PMC full text located", "module": "Module 5B", "tracker_id": "M5A-P001"}'
  )
  RETURNING paper_id
)
INSERT INTO _m5_paper_map (tracker_id, paper_id) SELECT 'M5A-P001', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Reducing Pericyte-Derived Scarring Promotes Recovery after Spinal Cord Injury', 'Dias DO', 2018,
    NULL, NULL, NULL,
    NULL, NULL, '29502968',
    NULL, '{"curator_notes": "Axon regeneration with scar-modulation anchor", "module": "Module 5B", "tracker_id": "M5A-P002"}'
  )
  RETURNING paper_id
)
INSERT INTO _m5_paper_map (tracker_id, paper_id) SELECT 'M5A-P002', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Lesion-remote astrocytes govern microglia-mediated white matter repair', 'McCallum S', 2026,
    NULL, NULL, NULL,
    NULL, NULL, '41407858',
    NULL, '{"curator_notes": "White matter repair anchor", "module": "Module 5B", "tracker_id": "M5A-P003"}'
  )
  RETURNING paper_id
)
INSERT INTO _m5_paper_map (tracker_id, paper_id) SELECT 'M5A-P003', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Motoneuron Death after Human Spinal Cord Injury', 'Grumbles RM', 2017,
    NULL, NULL, NULL,
    NULL, NULL, '27349409',
    NULL, '{"curator_notes": "Human remyelination/pathology bridge", "module": "Module 5B", "tracker_id": "M5A-P004"}'
  )
  RETURNING paper_id
)
INSERT INTO _m5_paper_map (tracker_id, paper_id) SELECT 'M5A-P004', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Restoring Cellular Energetics Promotes Axonal Regeneration and Functional Recovery after Spinal Cord Injury', 'Han Q', 2020,
    NULL, NULL, NULL,
    NULL, NULL, '32130884',
    NULL, '{"curator_notes": "Metabolic mechanism anchor", "module": "Module 5B", "tracker_id": "M5A-P005"}'
  )
  RETURNING paper_id
)
INSERT INTO _m5_paper_map (tracker_id, paper_id) SELECT 'M5A-P005', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Corticospinal tract regeneration after spinal cord injury in receptor protein tyrosine phosphatase sigma deficient mice', 'Fry EJ', 2010,
    NULL, NULL, NULL,
    NULL, NULL, '19780196',
    NULL, '{"curator_notes": "CSPG-receptor pathway anchor; no PMC full text located", "module": "Module 5B", "tracker_id": "M5A-P006"}'
  )
  RETURNING paper_id
)
INSERT INTO _m5_paper_map (tracker_id, paper_id) SELECT 'M5A-P006', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Spinal cord reconstitution with homologous neural grafts enables robust corticospinal regeneration', 'Kadoya K', 2016,
    NULL, NULL, NULL,
    NULL, NULL, '27019328',
    NULL, '{"curator_notes": "Graft-regeneration bridge to Module 4A", "module": "Module 5B", "tracker_id": "M5A-P007"}'
  )
  RETURNING paper_id
)
INSERT INTO _m5_paper_map (tracker_id, paper_id) SELECT 'M5A-P007', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Injured adult neurons regress to an embryonic transcriptional growth state', 'Poplawski GHD', 2020,
    NULL, NULL, NULL,
    NULL, NULL, '32376949',
    NULL, '{"curator_notes": "Transcriptional growth-state anchor; no PMC full text located", "module": "Module 5B", "tracker_id": "M5A-P008"}'
  )
  RETURNING paper_id
)
INSERT INTO _m5_paper_map (tracker_id, paper_id) SELECT 'M5A-P008', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Activation of MAP2K signaling by genetic engineering or HF-rTMS promotes corticospinal axon sprouting and functional regeneration', 'Boato F', 2023,
    NULL, NULL, NULL,
    NULL, NULL, '36599003',
    NULL, '{"curator_notes": "Stimulation/signaling intervention anchor; no PMC full text located", "module": "Module 5B", "tracker_id": "M5A-P009"}'
  )
  RETURNING paper_id
)
INSERT INTO _m5_paper_map (tracker_id, paper_id) SELECT 'M5A-P009', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Transcranial Optogenetic Stimulation Promotes Corticospinal Tract Axon Regeneration to Repair Spinal Cord Injury by Activating the JAK2/STAT3 Pathway.', 'Ma YH', 2025,
    NULL, NULL, NULL,
    NULL, NULL, '40624993',
    NULL, '{"curator_notes": "Corticospinal tract regeneration / sprouting anchor", "module": "Module 5B", "tracker_id": "M5A-P010"}'
  )
  RETURNING paper_id
)
INSERT INTO _m5_paper_map (tracker_id, paper_id) SELECT 'M5A-P010', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Lipin1 depletion coordinates neuronal signaling pathways to promote motor and sensory axon regeneration after spinal cord injury.', 'Chen W', 2024,
    NULL, NULL, NULL,
    NULL, NULL, '39292743',
    NULL, '{"curator_notes": "Corticospinal tract regeneration / sprouting anchor", "module": "Module 5B", "tracker_id": "M5A-P011"}'
  )
  RETURNING paper_id
)
INSERT INTO _m5_paper_map (tracker_id, paper_id) SELECT 'M5A-P011', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Effects of transcranial magnetic stimulation on axonal regeneration in the corticospinal tract of female rats with spinal cord injury.', 'Hu M', 2024,
    NULL, NULL, NULL,
    NULL, NULL, '39191303',
    NULL, '{"curator_notes": "TMS corticospinal regeneration anchor", "module": "Module 5B", "tracker_id": "M5A-P012"}'
  )
  RETURNING paper_id
)
INSERT INTO _m5_paper_map (tracker_id, paper_id) SELECT 'M5A-P012', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Synaptotagmin 4 Supports Spontaneous Axon Sprouting after Spinal Cord Injury.', 'Higuchi K', 2024,
    NULL, NULL, NULL,
    NULL, NULL, '39266302',
    NULL, '{"curator_notes": "Corticospinal tract regeneration / sprouting anchor", "module": "Module 5B", "tracker_id": "M5A-P013"}'
  )
  RETURNING paper_id
)
INSERT INTO _m5_paper_map (tracker_id, paper_id) SELECT 'M5A-P013', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Gabapentinoid treatment promotes corticospinal plasticity and regeneration following murine spinal cord injury.', 'Sun W', 2020,
    NULL, NULL, NULL,
    NULL, NULL, '31793909',
    NULL, '{"curator_notes": "Gabapentinoid CST plasticity anchor", "module": "Module 5B", "tracker_id": "M5A-P014"}'
  )
  RETURNING paper_id
)
INSERT INTO _m5_paper_map (tracker_id, paper_id) SELECT 'M5A-P014', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Activated alpha 9 integrin expression enables sensory pathway reconstruction after spinal cord injury.', 'Stepankova K', 2025,
    NULL, NULL, NULL,
    NULL, NULL, '40317093',
    NULL, '{"curator_notes": "Extrinsic inhibitory matrix / guidance pathway anchor", "module": "Module 5B", "tracker_id": "M5A-P015"}'
  )
  RETURNING paper_id
)
INSERT INTO _m5_paper_map (tracker_id, paper_id) SELECT 'M5A-P015', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Modulation of Extrinsic and Intrinsic Signaling Together with Neuronal Activation Enhances Forelimb Motor Recovery after Cervical Spinal Cord Injury.', 'Takatani H', 2025,
    NULL, NULL, NULL,
    NULL, NULL, '39919817',
    NULL, '{"curator_notes": "Corticospinal tract regeneration / sprouting anchor", "module": "Module 5B", "tracker_id": "M5A-P016"}'
  )
  RETURNING paper_id
)
INSERT INTO _m5_paper_map (tracker_id, paper_id) SELECT 'M5A-P016', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Thiorphan reprograms neurons to promote functional recovery after spinal cord injury.', 'van Niekerk EA', 2025,
    NULL, NULL, NULL,
    NULL, NULL, '41162703',
    NULL, '{"curator_notes": "Corticospinal tract regeneration / sprouting anchor", "module": "Module 5B", "tracker_id": "M5A-P017"}'
  )
  RETURNING paper_id
)
INSERT INTO _m5_paper_map (tracker_id, paper_id) SELECT 'M5A-P017', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'TTBK2-Driven Ciliogenesis Is Required for Intrinsic Neuronal Regeneration After Spinal Cord Injury.', 'Zhang R', 2026,
    NULL, NULL, NULL,
    NULL, NULL, '41578860',
    NULL, '{"curator_notes": "Intrinsic neuronal growth competence anchor", "module": "Module 5B", "tracker_id": "M5A-P018"}'
  )
  RETURNING paper_id
)
INSERT INTO _m5_paper_map (tracker_id, paper_id) SELECT 'M5A-P018', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'The transcription factor combination MEF2 and KLF7 promotes axonal sprouting in the injured spinal cord with functional improvement and regeneration-associated gene expression.', 'Attwell CL', 2025,
    NULL, NULL, NULL,
    NULL, NULL, '39923113',
    NULL, '{"curator_notes": "Intrinsic neuronal growth competence anchor", "module": "Module 5B", "tracker_id": "M5A-P019"}'
  )
  RETURNING paper_id
)
INSERT INTO _m5_paper_map (tracker_id, paper_id) SELECT 'M5A-P019', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Stimulation of corticospinal neurons by optogenetic cAMP inductions promotes motor recovery after spinal cord injury in female rats via raphespinal tract modulation.', 'Martinez-Rojas B', 2025,
    NULL, NULL, NULL,
    NULL, NULL, '40592902',
    NULL, '{"curator_notes": "Corticospinal tract regeneration / sprouting anchor", "module": "Module 5B", "tracker_id": "M5A-P020"}'
  )
  RETURNING paper_id
)
INSERT INTO _m5_paper_map (tracker_id, paper_id) SELECT 'M5A-P020', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Precise rewiring of corticospinal axons and spinal interneurons via near-infrared optogenetics for spinal cord injury treatment.', 'Ji Z', 2025,
    NULL, NULL, NULL,
    NULL, NULL, '40749050',
    NULL, '{"curator_notes": "Corticospinal tract regeneration / sprouting anchor", "module": "Module 5B", "tracker_id": "M5A-P021"}'
  )
  RETURNING paper_id
)
INSERT INTO _m5_paper_map (tracker_id, paper_id) SELECT 'M5A-P021', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Netrin-1 Therapy Restores Partial Hindlimb Movement in a Rat Model of High-Severity Chronic Spinal Cord Injury.', 'Schmidt J', 2026,
    NULL, NULL, NULL,
    NULL, NULL, '41163574',
    NULL, '{"curator_notes": "Corticospinal tract regeneration / sprouting anchor", "module": "Module 5B", "tracker_id": "M5A-P022"}'
  )
  RETURNING paper_id
)
INSERT INTO _m5_paper_map (tracker_id, paper_id) SELECT 'M5A-P022', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Lentivirus-mediated overexpression of netrin-1/DCC co-expression promotes axonal regeneration and functional recovery in spinal cord injury via the inhibition of the NgR1-RhoA-ROCK signaling pathway.', 'Zheng ML', 2025,
    NULL, NULL, NULL,
    NULL, NULL, '40092657',
    NULL, '{"curator_notes": "Extrinsic inhibitory matrix / guidance pathway anchor", "module": "Module 5B", "tracker_id": "M5A-P023"}'
  )
  RETURNING paper_id
)
INSERT INTO _m5_paper_map (tracker_id, paper_id) SELECT 'M5A-P023', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Disrupting CSPG-Driven Microglia-Astrocyte Crosstalk Enables Scar-Free Repair in Spinal Cord Injury.', 'Zheng Y', 2026,
    NULL, NULL, NULL,
    NULL, NULL, '41221600',
    NULL, '{"curator_notes": "Extrinsic inhibitory matrix / guidance pathway anchor", "module": "Module 5B", "tracker_id": "M5A-P024"}'
  )
  RETURNING paper_id
)
INSERT INTO _m5_paper_map (tracker_id, paper_id) SELECT 'M5A-P024', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Chondroitinase ABC combined with Schwann cell transplantation enhances restoration of neural connection and functional recovery following acute and chronic spinal cord injury.', 'Qu W', 2025,
    NULL, NULL, NULL,
    NULL, NULL, '39075913',
    NULL, '{"curator_notes": "Serotonergic/propriospinal relay plasticity anchor", "module": "Module 5B", "tracker_id": "M5A-P025"}'
  )
  RETURNING paper_id
)
INSERT INTO _m5_paper_map (tracker_id, paper_id) SELECT 'M5A-P025', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Schwann Cell-Derived Exosomes Induced Axon Growth after Spinal Cord Injury by Decreasing PTP- Activation on CSPGs via the Rho/ROCK Pathway.', 'Zhu S', 2024,
    NULL, NULL, NULL,
    NULL, NULL, '38819695',
    NULL, '{"curator_notes": "Extrinsic inhibitory matrix / guidance pathway anchor", "module": "Module 5B", "tracker_id": "M5A-P026"}'
  )
  RETURNING paper_id
)
INSERT INTO _m5_paper_map (tracker_id, paper_id) SELECT 'M5A-P026', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Anti-Nogo-A NG101 treatment induces changes in spinal cord micro- and macrostructure following spinal cord injury.', 'Farner L', 2026,
    NULL, NULL, NULL,
    NULL, NULL, '42120375',
    NULL, '{"curator_notes": "Corticospinal tract regeneration / sprouting anchor", "module": "Module 5B", "tracker_id": "M5A-P027"}'
  )
  RETURNING paper_id
)
INSERT INTO _m5_paper_map (tracker_id, paper_id) SELECT 'M5A-P027', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Human Oligodendrogenic Neural Progenitor Cells Delivered with Chondroitinase ABC Facilitate Functional Repair of Chronic Spinal Cord Injury.', 'Nori S', 2018,
    NULL, NULL, NULL,
    NULL, NULL, '30472009',
    NULL, '{"curator_notes": "Remyelination / white matter repair anchor", "module": "Module 5B", "tracker_id": "M5A-P028"}'
  )
  RETURNING paper_id
)
INSERT INTO _m5_paper_map (tracker_id, paper_id) SELECT 'M5A-P028', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'TREM2 Facilitates Myelin Debris Clearance but Exacerbates Chronic Inflammation and Fibrosis After Spinal Cord Injury.', 'Wu Z', 2026,
    NULL, NULL, NULL,
    NULL, NULL, '41660680',
    NULL, '{"curator_notes": "Remyelination / white matter repair anchor", "module": "Module 5B", "tracker_id": "M5A-P029"}'
  )
  RETURNING paper_id
)
INSERT INTO _m5_paper_map (tracker_id, paper_id) SELECT 'M5A-P029', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Lesion-remote astrocytes govern microglia-mediated white matter repair.', 'McCallum S', 2026,
    NULL, NULL, NULL,
    NULL, NULL, '41407858',
    NULL, '{"curator_notes": "Remyelination / white matter repair anchor", "module": "Module 5B", "tracker_id": "M5A-P030"}'
  )
  RETURNING paper_id
)
INSERT INTO _m5_paper_map (tracker_id, paper_id) SELECT 'M5A-P030', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Compensatory changes after spinal cord injury in a remyelination deficient mouse model.', 'Manesh SB', 2025,
    NULL, NULL, NULL,
    NULL, NULL, '39268880',
    NULL, '{"curator_notes": "Remyelination / white matter repair anchor", "module": "Module 5B", "tracker_id": "M5A-P031"}'
  )
  RETURNING paper_id
)
INSERT INTO _m5_paper_map (tracker_id, paper_id) SELECT 'M5A-P031', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'A Myelin Debris Cleaner for Spinal Cord Injury Recovery: Polycaprolactone / Cell Membrane Assembled Scaffolds.', 'Zhou Y', 2025,
    NULL, NULL, NULL,
    NULL, NULL, '40568983',
    NULL, '{"curator_notes": "Remyelination / white matter repair anchor", "module": "Module 5B", "tracker_id": "M5A-P032"}'
  )
  RETURNING paper_id
)
INSERT INTO _m5_paper_map (tracker_id, paper_id) SELECT 'M5A-P032', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Serotonergic System-Targeted Nucleic Acid Hydrogel Coordinates Excitability Restoration and Circuit Reconstruction for Spinal Cord Injury Therapy.', 'Li C', 2026,
    NULL, NULL, NULL,
    NULL, NULL, '41531173',
    NULL, '{"curator_notes": "Serotonergic/propriospinal relay plasticity anchor", "module": "Module 5B", "tracker_id": "M5A-P033"}'
  )
  RETURNING paper_id
)
INSERT INTO _m5_paper_map (tracker_id, paper_id) SELECT 'M5A-P033', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Central Serotonin Deficiency Impairs Recovery of Sensorimotor Abilities After Spinal Cord Injury in Rats.', 'Sysoev YI', 2025,
    NULL, NULL, NULL,
    NULL, NULL, '40141402',
    NULL, '{"curator_notes": "Serotonergic/propriospinal relay plasticity anchor", "module": "Module 5B", "tracker_id": "M5A-P034"}'
  )
  RETURNING paper_id
)
INSERT INTO _m5_paper_map (tracker_id, paper_id) SELECT 'M5A-P034', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Neuronal HDAC3 knockdown promotes propriospinal detour pathway formation and locomotor recovery in a mouse model of spinal cord injury.', 'Gao Z', 2025,
    NULL, NULL, NULL,
    NULL, NULL, '40632834',
    NULL, '{"curator_notes": "Serotonergic/propriospinal relay plasticity anchor", "module": "Module 5B", "tracker_id": "M5A-P035"}'
  )
  RETURNING paper_id
)
INSERT INTO _m5_paper_map (tracker_id, paper_id) SELECT 'M5A-P035', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Functional recovery induced by KCC2-enabled relay pathways in completely injured spinal cords in adult rats.', 'Wang Y', 2025,
    NULL, NULL, NULL,
    NULL, NULL, '41359836',
    NULL, '{"curator_notes": "Serotonergic/propriospinal relay plasticity anchor", "module": "Module 5B", "tracker_id": "M5A-P036"}'
  )
  RETURNING paper_id
)
INSERT INTO _m5_paper_map (tracker_id, paper_id) SELECT 'M5A-P036', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Functionalized nanozyme delivery of a KCC2-activator conjugate for the promotion of functional recovery after acute spinal cord injury.', 'Zhao H', 2025,
    NULL, NULL, NULL,
    NULL, NULL, '41445781',
    NULL, '{"curator_notes": "Serotonergic/propriospinal relay plasticity anchor", "module": "Module 5B", "tracker_id": "M5A-P037"}'
  )
  RETURNING paper_id
)
INSERT INTO _m5_paper_map (tracker_id, paper_id) SELECT 'M5A-P037', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Enhanced locomotor recovery in mice lacking GlcNAc6ST1 and GlcNAc6ST4 following spinal cord injury.', 'Morozumi M', 2025,
    NULL, NULL, NULL,
    NULL, NULL, '40876929',
    NULL, '{"curator_notes": "Serotonergic/propriospinal relay plasticity anchor", "module": "Module 5B", "tracker_id": "M5A-P038"}'
  )
  RETURNING paper_id
)
INSERT INTO _m5_paper_map (tracker_id, paper_id) SELECT 'M5A-P038', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Treadmill exercise supplemented by OPN promote axon regeneration through the IGF-1R/Akt/mTOR signaling pathway.', 'Zhao Q', 2025,
    NULL, NULL, NULL,
    NULL, NULL, '39657897',
    NULL, '{"curator_notes": "Corticospinal tract regeneration / sprouting anchor", "module": "Module 5B", "tracker_id": "M5A-P039"}'
  )
  RETURNING paper_id
)
INSERT INTO _m5_paper_map (tracker_id, paper_id) SELECT 'M5A-P039', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Osteopontin enhances the effect of treadmill training and promotes functional recovery after spinal cord injury.', 'Wang Y', 2023,
    NULL, NULL, NULL,
    NULL, NULL, '38015348',
    NULL, '{"curator_notes": "Corticospinal tract regeneration / sprouting anchor", "module": "Module 5B", "tracker_id": "M5A-P040"}'
  )
  RETURNING paper_id
)
INSERT INTO _m5_paper_map (tracker_id, paper_id) SELECT 'M5A-P040', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Co-overexpression of OPN, IGF-1 and CNTF augment the therapeutic effect of DPSC on spinal cord injury.', 'Tao N', 2023,
    NULL, NULL, NULL,
    NULL, NULL, '38074191',
    NULL, '{"curator_notes": "Graft/scaffold-enabled axon repair anchor", "module": "Module 5B", "tracker_id": "M5A-P041"}'
  )
  RETURNING paper_id
)
INSERT INTO _m5_paper_map (tracker_id, paper_id) SELECT 'M5A-P041', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Multichannel 3D-Printed Bioactive Scaffold Combined with Small Interfering RNA Delivery to Promote Neurological Recovery after Spinal Cord Injury.', 'Ye J', 2025,
    NULL, NULL, NULL,
    NULL, NULL, '41127263',
    NULL, '{"curator_notes": "Graft/scaffold-enabled axon repair anchor", "module": "Module 5B", "tracker_id": "M5A-P042"}'
  )
  RETURNING paper_id
)
INSERT INTO _m5_paper_map (tracker_id, paper_id) SELECT 'M5A-P042', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Development of a <i>PTEN</i>-siRNA activated scaffold to promote axonal regrowth following spinal cord injury.', 'McGuire TK', 2026,
    NULL, NULL, NULL,
    NULL, NULL, '41704619',
    NULL, '{"curator_notes": "Intrinsic neuronal growth competence anchor", "module": "Module 5B", "tracker_id": "M5A-P043"}'
  )
  RETURNING paper_id
)
INSERT INTO _m5_paper_map (tracker_id, paper_id) SELECT 'M5A-P043', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'CITED2 is a druggable epigenetic switch coupling neuronal maturation to regenerative decline.', 'Muller F', 2026,
    NULL, NULL, NULL,
    NULL, NULL, '41731079',
    NULL, '{"curator_notes": "Intrinsic neuronal growth competence anchor", "module": "Module 5B", "tracker_id": "M5A-P044"}'
  )
  RETURNING paper_id
)
INSERT INTO _m5_paper_map (tracker_id, paper_id) SELECT 'M5A-P044', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Poly-L-Ornithine coated plant scaffolds support motor recovery in rats after traumatic spinal cord injury.', 'Couvrette LJ', 2025,
    NULL, NULL, NULL,
    NULL, NULL, '41168240',
    NULL, '{"curator_notes": "Graft/scaffold-enabled axon repair anchor", "module": "Module 5B", "tracker_id": "M5A-P045"}'
  )
  RETURNING paper_id
)
INSERT INTO _m5_paper_map (tracker_id, paper_id) SELECT 'M5A-P045', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Integrating single-cell RNA sequencing and spatial multi-omics reveals the molecular signature of regeneration after spinal cord injury.', 'Dong H', 2025,
    NULL, NULL, NULL,
    NULL, NULL, '41121424',
    NULL, '{"curator_notes": "Remyelination / white matter repair anchor", "module": "Module 5B", "tracker_id": "M5A-P046"}'
  )
  RETURNING paper_id
)
INSERT INTO _m5_paper_map (tracker_id, paper_id) SELECT 'M5A-P046', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'A laminin-based therapy for dogs with chronic spinal cord injury: promising results of a longitudinal trial.', 'Chize CM', 2025,
    NULL, NULL, NULL,
    NULL, NULL, '40881640',
    NULL, '{"curator_notes": "Extrinsic inhibitory matrix / guidance pathway anchor", "module": "Module 5B", "tracker_id": "M5A-P047"}'
  )
  RETURNING paper_id
)
INSERT INTO _m5_paper_map (tracker_id, paper_id) SELECT 'M5A-P047', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 5B curated evidence extraction',
    'First-pass Module 5B axon regeneration, remyelination, and white matter repair curation for M5A-P001',
    'Tracker-derived materialization from Module_5B_TRACKER.md'
  FROM _m5_paper_map WHERE tracker_id = 'M5A-P001'
  RETURNING paradigm_id
)
INSERT INTO _m5_paradigm_map (tracker_id, paradigm_id) SELECT 'M5A-P001', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 5B curated evidence extraction',
    'First-pass Module 5B axon regeneration, remyelination, and white matter repair curation for M5A-P002',
    'Tracker-derived materialization from Module_5B_TRACKER.md'
  FROM _m5_paper_map WHERE tracker_id = 'M5A-P002'
  RETURNING paradigm_id
)
INSERT INTO _m5_paradigm_map (tracker_id, paradigm_id) SELECT 'M5A-P002', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 5B curated evidence extraction',
    'First-pass Module 5B axon regeneration, remyelination, and white matter repair curation for M5A-P003',
    'Tracker-derived materialization from Module_5B_TRACKER.md'
  FROM _m5_paper_map WHERE tracker_id = 'M5A-P003'
  RETURNING paradigm_id
)
INSERT INTO _m5_paradigm_map (tracker_id, paradigm_id) SELECT 'M5A-P003', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 5B curated evidence extraction',
    'First-pass Module 5B axon regeneration, remyelination, and white matter repair curation for M5A-P004',
    'Tracker-derived materialization from Module_5B_TRACKER.md'
  FROM _m5_paper_map WHERE tracker_id = 'M5A-P004'
  RETURNING paradigm_id
)
INSERT INTO _m5_paradigm_map (tracker_id, paradigm_id) SELECT 'M5A-P004', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 5B curated evidence extraction',
    'First-pass Module 5B axon regeneration, remyelination, and white matter repair curation for M5A-P005',
    'Tracker-derived materialization from Module_5B_TRACKER.md'
  FROM _m5_paper_map WHERE tracker_id = 'M5A-P005'
  RETURNING paradigm_id
)
INSERT INTO _m5_paradigm_map (tracker_id, paradigm_id) SELECT 'M5A-P005', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 5B curated evidence extraction',
    'First-pass Module 5B axon regeneration, remyelination, and white matter repair curation for M5A-P006',
    'Tracker-derived materialization from Module_5B_TRACKER.md'
  FROM _m5_paper_map WHERE tracker_id = 'M5A-P006'
  RETURNING paradigm_id
)
INSERT INTO _m5_paradigm_map (tracker_id, paradigm_id) SELECT 'M5A-P006', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 5B curated evidence extraction',
    'First-pass Module 5B axon regeneration, remyelination, and white matter repair curation for M5A-P007',
    'Tracker-derived materialization from Module_5B_TRACKER.md'
  FROM _m5_paper_map WHERE tracker_id = 'M5A-P007'
  RETURNING paradigm_id
)
INSERT INTO _m5_paradigm_map (tracker_id, paradigm_id) SELECT 'M5A-P007', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 5B curated evidence extraction',
    'First-pass Module 5B axon regeneration, remyelination, and white matter repair curation for M5A-P008',
    'Tracker-derived materialization from Module_5B_TRACKER.md'
  FROM _m5_paper_map WHERE tracker_id = 'M5A-P008'
  RETURNING paradigm_id
)
INSERT INTO _m5_paradigm_map (tracker_id, paradigm_id) SELECT 'M5A-P008', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 5B curated evidence extraction',
    'First-pass Module 5B axon regeneration, remyelination, and white matter repair curation for M5A-P009',
    'Tracker-derived materialization from Module_5B_TRACKER.md'
  FROM _m5_paper_map WHERE tracker_id = 'M5A-P009'
  RETURNING paradigm_id
)
INSERT INTO _m5_paradigm_map (tracker_id, paradigm_id) SELECT 'M5A-P009', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 5B curated evidence extraction',
    'First-pass Module 5B axon regeneration, remyelination, and white matter repair curation for M5A-P010',
    'Tracker-derived materialization from Module_5B_TRACKER.md'
  FROM _m5_paper_map WHERE tracker_id = 'M5A-P010'
  RETURNING paradigm_id
)
INSERT INTO _m5_paradigm_map (tracker_id, paradigm_id) SELECT 'M5A-P010', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 5B curated evidence extraction',
    'First-pass Module 5B axon regeneration, remyelination, and white matter repair curation for M5A-P011',
    'Tracker-derived materialization from Module_5B_TRACKER.md'
  FROM _m5_paper_map WHERE tracker_id = 'M5A-P011'
  RETURNING paradigm_id
)
INSERT INTO _m5_paradigm_map (tracker_id, paradigm_id) SELECT 'M5A-P011', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 5B curated evidence extraction',
    'First-pass Module 5B axon regeneration, remyelination, and white matter repair curation for M5A-P012',
    'Tracker-derived materialization from Module_5B_TRACKER.md'
  FROM _m5_paper_map WHERE tracker_id = 'M5A-P012'
  RETURNING paradigm_id
)
INSERT INTO _m5_paradigm_map (tracker_id, paradigm_id) SELECT 'M5A-P012', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 5B curated evidence extraction',
    'First-pass Module 5B axon regeneration, remyelination, and white matter repair curation for M5A-P013',
    'Tracker-derived materialization from Module_5B_TRACKER.md'
  FROM _m5_paper_map WHERE tracker_id = 'M5A-P013'
  RETURNING paradigm_id
)
INSERT INTO _m5_paradigm_map (tracker_id, paradigm_id) SELECT 'M5A-P013', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 5B curated evidence extraction',
    'First-pass Module 5B axon regeneration, remyelination, and white matter repair curation for M5A-P014',
    'Tracker-derived materialization from Module_5B_TRACKER.md'
  FROM _m5_paper_map WHERE tracker_id = 'M5A-P014'
  RETURNING paradigm_id
)
INSERT INTO _m5_paradigm_map (tracker_id, paradigm_id) SELECT 'M5A-P014', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 5B curated evidence extraction',
    'First-pass Module 5B axon regeneration, remyelination, and white matter repair curation for M5A-P015',
    'Tracker-derived materialization from Module_5B_TRACKER.md'
  FROM _m5_paper_map WHERE tracker_id = 'M5A-P015'
  RETURNING paradigm_id
)
INSERT INTO _m5_paradigm_map (tracker_id, paradigm_id) SELECT 'M5A-P015', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 5B curated evidence extraction',
    'First-pass Module 5B axon regeneration, remyelination, and white matter repair curation for M5A-P016',
    'Tracker-derived materialization from Module_5B_TRACKER.md'
  FROM _m5_paper_map WHERE tracker_id = 'M5A-P016'
  RETURNING paradigm_id
)
INSERT INTO _m5_paradigm_map (tracker_id, paradigm_id) SELECT 'M5A-P016', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 5B curated evidence extraction',
    'First-pass Module 5B axon regeneration, remyelination, and white matter repair curation for M5A-P017',
    'Tracker-derived materialization from Module_5B_TRACKER.md'
  FROM _m5_paper_map WHERE tracker_id = 'M5A-P017'
  RETURNING paradigm_id
)
INSERT INTO _m5_paradigm_map (tracker_id, paradigm_id) SELECT 'M5A-P017', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 5B curated evidence extraction',
    'First-pass Module 5B axon regeneration, remyelination, and white matter repair curation for M5A-P018',
    'Tracker-derived materialization from Module_5B_TRACKER.md'
  FROM _m5_paper_map WHERE tracker_id = 'M5A-P018'
  RETURNING paradigm_id
)
INSERT INTO _m5_paradigm_map (tracker_id, paradigm_id) SELECT 'M5A-P018', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 5B curated evidence extraction',
    'First-pass Module 5B axon regeneration, remyelination, and white matter repair curation for M5A-P019',
    'Tracker-derived materialization from Module_5B_TRACKER.md'
  FROM _m5_paper_map WHERE tracker_id = 'M5A-P019'
  RETURNING paradigm_id
)
INSERT INTO _m5_paradigm_map (tracker_id, paradigm_id) SELECT 'M5A-P019', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 5B curated evidence extraction',
    'First-pass Module 5B axon regeneration, remyelination, and white matter repair curation for M5A-P020',
    'Tracker-derived materialization from Module_5B_TRACKER.md'
  FROM _m5_paper_map WHERE tracker_id = 'M5A-P020'
  RETURNING paradigm_id
)
INSERT INTO _m5_paradigm_map (tracker_id, paradigm_id) SELECT 'M5A-P020', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 5B curated evidence extraction',
    'First-pass Module 5B axon regeneration, remyelination, and white matter repair curation for M5A-P021',
    'Tracker-derived materialization from Module_5B_TRACKER.md'
  FROM _m5_paper_map WHERE tracker_id = 'M5A-P021'
  RETURNING paradigm_id
)
INSERT INTO _m5_paradigm_map (tracker_id, paradigm_id) SELECT 'M5A-P021', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 5B curated evidence extraction',
    'First-pass Module 5B axon regeneration, remyelination, and white matter repair curation for M5A-P022',
    'Tracker-derived materialization from Module_5B_TRACKER.md'
  FROM _m5_paper_map WHERE tracker_id = 'M5A-P022'
  RETURNING paradigm_id
)
INSERT INTO _m5_paradigm_map (tracker_id, paradigm_id) SELECT 'M5A-P022', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 5B curated evidence extraction',
    'First-pass Module 5B axon regeneration, remyelination, and white matter repair curation for M5A-P023',
    'Tracker-derived materialization from Module_5B_TRACKER.md'
  FROM _m5_paper_map WHERE tracker_id = 'M5A-P023'
  RETURNING paradigm_id
)
INSERT INTO _m5_paradigm_map (tracker_id, paradigm_id) SELECT 'M5A-P023', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 5B curated evidence extraction',
    'First-pass Module 5B axon regeneration, remyelination, and white matter repair curation for M5A-P024',
    'Tracker-derived materialization from Module_5B_TRACKER.md'
  FROM _m5_paper_map WHERE tracker_id = 'M5A-P024'
  RETURNING paradigm_id
)
INSERT INTO _m5_paradigm_map (tracker_id, paradigm_id) SELECT 'M5A-P024', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 5B curated evidence extraction',
    'First-pass Module 5B axon regeneration, remyelination, and white matter repair curation for M5A-P025',
    'Tracker-derived materialization from Module_5B_TRACKER.md'
  FROM _m5_paper_map WHERE tracker_id = 'M5A-P025'
  RETURNING paradigm_id
)
INSERT INTO _m5_paradigm_map (tracker_id, paradigm_id) SELECT 'M5A-P025', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 5B curated evidence extraction',
    'First-pass Module 5B axon regeneration, remyelination, and white matter repair curation for M5A-P026',
    'Tracker-derived materialization from Module_5B_TRACKER.md'
  FROM _m5_paper_map WHERE tracker_id = 'M5A-P026'
  RETURNING paradigm_id
)
INSERT INTO _m5_paradigm_map (tracker_id, paradigm_id) SELECT 'M5A-P026', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 5B curated evidence extraction',
    'First-pass Module 5B axon regeneration, remyelination, and white matter repair curation for M5A-P027',
    'Tracker-derived materialization from Module_5B_TRACKER.md'
  FROM _m5_paper_map WHERE tracker_id = 'M5A-P027'
  RETURNING paradigm_id
)
INSERT INTO _m5_paradigm_map (tracker_id, paradigm_id) SELECT 'M5A-P027', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 5B curated evidence extraction',
    'First-pass Module 5B axon regeneration, remyelination, and white matter repair curation for M5A-P028',
    'Tracker-derived materialization from Module_5B_TRACKER.md'
  FROM _m5_paper_map WHERE tracker_id = 'M5A-P028'
  RETURNING paradigm_id
)
INSERT INTO _m5_paradigm_map (tracker_id, paradigm_id) SELECT 'M5A-P028', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 5B curated evidence extraction',
    'First-pass Module 5B axon regeneration, remyelination, and white matter repair curation for M5A-P029',
    'Tracker-derived materialization from Module_5B_TRACKER.md'
  FROM _m5_paper_map WHERE tracker_id = 'M5A-P029'
  RETURNING paradigm_id
)
INSERT INTO _m5_paradigm_map (tracker_id, paradigm_id) SELECT 'M5A-P029', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 5B curated evidence extraction',
    'First-pass Module 5B axon regeneration, remyelination, and white matter repair curation for M5A-P030',
    'Tracker-derived materialization from Module_5B_TRACKER.md'
  FROM _m5_paper_map WHERE tracker_id = 'M5A-P030'
  RETURNING paradigm_id
)
INSERT INTO _m5_paradigm_map (tracker_id, paradigm_id) SELECT 'M5A-P030', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 5B curated evidence extraction',
    'First-pass Module 5B axon regeneration, remyelination, and white matter repair curation for M5A-P031',
    'Tracker-derived materialization from Module_5B_TRACKER.md'
  FROM _m5_paper_map WHERE tracker_id = 'M5A-P031'
  RETURNING paradigm_id
)
INSERT INTO _m5_paradigm_map (tracker_id, paradigm_id) SELECT 'M5A-P031', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 5B curated evidence extraction',
    'First-pass Module 5B axon regeneration, remyelination, and white matter repair curation for M5A-P032',
    'Tracker-derived materialization from Module_5B_TRACKER.md'
  FROM _m5_paper_map WHERE tracker_id = 'M5A-P032'
  RETURNING paradigm_id
)
INSERT INTO _m5_paradigm_map (tracker_id, paradigm_id) SELECT 'M5A-P032', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 5B curated evidence extraction',
    'First-pass Module 5B axon regeneration, remyelination, and white matter repair curation for M5A-P033',
    'Tracker-derived materialization from Module_5B_TRACKER.md'
  FROM _m5_paper_map WHERE tracker_id = 'M5A-P033'
  RETURNING paradigm_id
)
INSERT INTO _m5_paradigm_map (tracker_id, paradigm_id) SELECT 'M5A-P033', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 5B curated evidence extraction',
    'First-pass Module 5B axon regeneration, remyelination, and white matter repair curation for M5A-P034',
    'Tracker-derived materialization from Module_5B_TRACKER.md'
  FROM _m5_paper_map WHERE tracker_id = 'M5A-P034'
  RETURNING paradigm_id
)
INSERT INTO _m5_paradigm_map (tracker_id, paradigm_id) SELECT 'M5A-P034', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 5B curated evidence extraction',
    'First-pass Module 5B axon regeneration, remyelination, and white matter repair curation for M5A-P035',
    'Tracker-derived materialization from Module_5B_TRACKER.md'
  FROM _m5_paper_map WHERE tracker_id = 'M5A-P035'
  RETURNING paradigm_id
)
INSERT INTO _m5_paradigm_map (tracker_id, paradigm_id) SELECT 'M5A-P035', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 5B curated evidence extraction',
    'First-pass Module 5B axon regeneration, remyelination, and white matter repair curation for M5A-P036',
    'Tracker-derived materialization from Module_5B_TRACKER.md'
  FROM _m5_paper_map WHERE tracker_id = 'M5A-P036'
  RETURNING paradigm_id
)
INSERT INTO _m5_paradigm_map (tracker_id, paradigm_id) SELECT 'M5A-P036', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 5B curated evidence extraction',
    'First-pass Module 5B axon regeneration, remyelination, and white matter repair curation for M5A-P037',
    'Tracker-derived materialization from Module_5B_TRACKER.md'
  FROM _m5_paper_map WHERE tracker_id = 'M5A-P037'
  RETURNING paradigm_id
)
INSERT INTO _m5_paradigm_map (tracker_id, paradigm_id) SELECT 'M5A-P037', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 5B curated evidence extraction',
    'First-pass Module 5B axon regeneration, remyelination, and white matter repair curation for M5A-P038',
    'Tracker-derived materialization from Module_5B_TRACKER.md'
  FROM _m5_paper_map WHERE tracker_id = 'M5A-P038'
  RETURNING paradigm_id
)
INSERT INTO _m5_paradigm_map (tracker_id, paradigm_id) SELECT 'M5A-P038', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 5B curated evidence extraction',
    'First-pass Module 5B axon regeneration, remyelination, and white matter repair curation for M5A-P039',
    'Tracker-derived materialization from Module_5B_TRACKER.md'
  FROM _m5_paper_map WHERE tracker_id = 'M5A-P039'
  RETURNING paradigm_id
)
INSERT INTO _m5_paradigm_map (tracker_id, paradigm_id) SELECT 'M5A-P039', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 5B curated evidence extraction',
    'First-pass Module 5B axon regeneration, remyelination, and white matter repair curation for M5A-P040',
    'Tracker-derived materialization from Module_5B_TRACKER.md'
  FROM _m5_paper_map WHERE tracker_id = 'M5A-P040'
  RETURNING paradigm_id
)
INSERT INTO _m5_paradigm_map (tracker_id, paradigm_id) SELECT 'M5A-P040', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 5B curated evidence extraction',
    'First-pass Module 5B axon regeneration, remyelination, and white matter repair curation for M5A-P041',
    'Tracker-derived materialization from Module_5B_TRACKER.md'
  FROM _m5_paper_map WHERE tracker_id = 'M5A-P041'
  RETURNING paradigm_id
)
INSERT INTO _m5_paradigm_map (tracker_id, paradigm_id) SELECT 'M5A-P041', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 5B curated evidence extraction',
    'First-pass Module 5B axon regeneration, remyelination, and white matter repair curation for M5A-P042',
    'Tracker-derived materialization from Module_5B_TRACKER.md'
  FROM _m5_paper_map WHERE tracker_id = 'M5A-P042'
  RETURNING paradigm_id
)
INSERT INTO _m5_paradigm_map (tracker_id, paradigm_id) SELECT 'M5A-P042', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 5B curated evidence extraction',
    'First-pass Module 5B axon regeneration, remyelination, and white matter repair curation for M5A-P043',
    'Tracker-derived materialization from Module_5B_TRACKER.md'
  FROM _m5_paper_map WHERE tracker_id = 'M5A-P043'
  RETURNING paradigm_id
)
INSERT INTO _m5_paradigm_map (tracker_id, paradigm_id) SELECT 'M5A-P043', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 5B curated evidence extraction',
    'First-pass Module 5B axon regeneration, remyelination, and white matter repair curation for M5A-P044',
    'Tracker-derived materialization from Module_5B_TRACKER.md'
  FROM _m5_paper_map WHERE tracker_id = 'M5A-P044'
  RETURNING paradigm_id
)
INSERT INTO _m5_paradigm_map (tracker_id, paradigm_id) SELECT 'M5A-P044', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 5B curated evidence extraction',
    'First-pass Module 5B axon regeneration, remyelination, and white matter repair curation for M5A-P045',
    'Tracker-derived materialization from Module_5B_TRACKER.md'
  FROM _m5_paper_map WHERE tracker_id = 'M5A-P045'
  RETURNING paradigm_id
)
INSERT INTO _m5_paradigm_map (tracker_id, paradigm_id) SELECT 'M5A-P045', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 5B curated evidence extraction',
    'First-pass Module 5B axon regeneration, remyelination, and white matter repair curation for M5A-P046',
    'Tracker-derived materialization from Module_5B_TRACKER.md'
  FROM _m5_paper_map WHERE tracker_id = 'M5A-P046'
  RETURNING paradigm_id
)
INSERT INTO _m5_paradigm_map (tracker_id, paradigm_id) SELECT 'M5A-P046', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 5B curated evidence extraction',
    'First-pass Module 5B axon regeneration, remyelination, and white matter repair curation for M5A-P047',
    'Tracker-derived materialization from Module_5B_TRACKER.md'
  FROM _m5_paper_map WHERE tracker_id = 'M5A-P047'
  RETURNING paradigm_id
)
INSERT INTO _m5_paradigm_map (tracker_id, paradigm_id) SELECT 'M5A-P047', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / saturated A tracker',
    'Tracker experiment M5A-P001-E001',
    'Extracted details: Primary intervention or mechanism experiment for Axon regeneration through scars and into sites of chronic spinal cord injury; first-pass row captures axon regeneration through chronic scar/graft in rat at abstract/source-title level. Extraction status: YES (abstract-level)',
    '{"chronicity_dpi_wpi": "UNKNOWN", "control_type": "Injury / vehicle / wild-type / comparator as reported", "experiment_extracted": "YES (abstract-level)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "UNKNOWN", "intervention_type": "Axon regeneration through chronic scar/graft", "methods_summary": "Primary intervention or mechanism experiment for Axon regeneration through scars and into sites of chronic spinal cord injury; first-pass row captures axon regeneration through chronic scar/graft in rat at abstract/source-title level.", "observation_tracker_ids": ["M5B-O001"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M5A-P001-E001", "source_paper_tracker_id": "M5A-P001", "species": "Rat", "strain": "UNKNOWN", "tracker_key": "M5A-P001::M5A-P001-E001", "vertebral_level": "UNKNOWN"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P001'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P001::M5A-P001-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M5A-P001-E002',
    'Extracted details: Outcome/mechanistic validation row for Axon regeneration through scars and into sites of chronic spinal cord injury; first-pass row captures axon regeneration through chronic scar/graft in rat at abstract/source-title level. Extraction status: YES (abstract-level)',
    '{"chronicity_dpi_wpi": "UNKNOWN", "control_type": "Comparator/control arm as reported", "experiment_extracted": "YES (abstract-level)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "UNKNOWN", "intervention_type": "Mechanistic outcome assessment after axon regeneration through chronic scar/graft", "methods_summary": "Outcome/mechanistic validation row for Axon regeneration through scars and into sites of chronic spinal cord injury; first-pass row captures axon regeneration through chronic scar/graft in rat at abstract/source-title level.", "observation_tracker_ids": ["M5B-O048"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M5A-P001-E002", "source_paper_tracker_id": "M5A-P001", "species": "Rat", "strain": "UNKNOWN", "tracker_key": "M5A-P001::M5A-P001-E002", "vertebral_level": "UNKNOWN"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P001'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P001::M5A-P001-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'A-layer full text; Full text PMC; Fig. 1-2',
    'Tracker experiment M5A-P002-E001',
    'Extracted details: Reducing type A pericyte proliferation decreased PDGFRB-positive fibrotic scar cells and broad extracellular-matrix and collagen deposition; complete recombination could prevent tissue closure, defining a dose-response boundary. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Tamoxifen recombination assessed at 2 and 4 weeks post-injury", "control_type": "Vehicle, intermediate-recombination Tam, and high-recombination Tam-tissue-defect groups", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Microsurgical dorsal hemisection", "injury_model": "Dorsal spinal cord hemisection", "injury_severity": "Incomplete dorsal hemisection", "intervention_type": "Cell-specific KRas deletion to attenuate type A pericyte progeny", "methods_summary": "Reducing type A pericyte proliferation decreased PDGFRB-positive fibrotic scar cells and broad extracellular-matrix and collagen deposition; complete recombination could prevent tissue closure, defining a dose-response boundary.", "observation_tracker_ids": ["M5B-O002"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M5A-P002-E001", "source_paper_tracker_id": "M5A-P002", "species": "Mouse", "strain": "Glast-CreERT2; Glast-Rasless-YFP", "tracker_key": "M5A-P002::M5A-P002-E001", "vertebral_level": "As reported"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P002'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P002::M5A-P002-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'A-layer full text; Full text PMC; Fig. 3-5',
    'Tracker experiment M5A-P002-E002',
    'Extracted details: Moderate scar attenuation enabled CST and raphespinal axons to enter and extend beyond the lesion, form synaptic and optogenetically responsive connections below the lesion, and improve sensorimotor recovery; the highest recombination caused tissue defects. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "BDA tracing and behavioral follow-up to 18 weeks; optogenetic and electrophysiologic circuit testing", "control_type": "Vehicle and Tam-tissue-def controls; tamoxifen-treated intermediate-recombination animals", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Microsurgical dorsal hemisection", "injury_model": "Dorsal spinal cord hemisection", "injury_severity": "Incomplete dorsal hemisection", "intervention_type": "Attenuated pericyte-derived fibrosis", "methods_summary": "Moderate scar attenuation enabled CST and raphespinal axons to enter and extend beyond the lesion, form synaptic and optogenetically responsive connections below the lesion, and improve sensorimotor recovery; the highest recombination caused tissue defects.", "observation_tracker_ids": ["M5B-O049"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M5A-P002-E002", "source_paper_tracker_id": "M5A-P002", "species": "Mouse", "strain": "Glast-Rasless-YFP", "tracker_key": "M5A-P002::M5A-P002-E002", "vertebral_level": "As reported"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P002'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P002::M5A-P002-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'A-layer full text; Full text PMC; Fig. 1-2 and spatial/single-nucleus atlas',
    'Tracker experiment M5A-P003-E001',
    'Extracted details: LRAs acquired region- and time-specific molecular states distinct from border-forming astrocytes. White-matter LRAs (WM3/4) co-localized with Mg2/Mg5 white-matter degeneration-associated microglia (WDM) that upregulated phagocytosis/lipid-metabolism programs, formed nodules in Wallerian-degenerating tracts, and phagocytosed myelin/axon debris. Ccn1 was selectively induced in WDM-adjacent white-matter LRAs. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "LRA RiboTag RNA-seq at 3, 7, 14, and 28 dpi; snRNA-seq/spatial transcriptomics at 3, 7, and 28 dpi; additional white-matter follow-up to 90 dpi", "control_type": "Healthy age/genotype-matched spinal cord and lesion-remote rostral/caudal regions; BFAs and non-traumatic astrocyte states as transcriptional comparators", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Unilateral T12 hemisection with microknife; parallel T12 crush model with no. 5 Dumont forceps and 0.4-mm spacer", "injury_model": "T12 anatomically and functionally incomplete SCI", "injury_severity": "Hemisection or crush as reported", "intervention_type": "Integrative mapping of lesion-remote astrocyte and white-matter degeneration-associated microglia states", "methods_summary": "LRAs acquired region- and time-specific molecular states distinct from border-forming astrocytes. White-matter LRAs (WM3/4) co-localized with Mg2/Mg5 white-matter degeneration-associated microglia (WDM) that upregulated phagocytosis/lipid-metabolism programs, formed nodules in Wallerian-degenerating tracts, and phagocytosed myelin/axon debris. Ccn1 was selectively induced in WDM-adjacent white-matter LRAs.", "observation_tracker_ids": ["M5B-O003"], "sex": "Male and female", "source_experiment_tracker_id": "M5A-P003-E001", "source_paper_tracker_id": "M5A-P003", "species": "Mouse", "strain": "C57BL/6J, RiboTag and astrocyte-Cre reporter backgrounds; 2-4 months", "tracker_key": "M5A-P003::M5A-P003-E001", "vertebral_level": "T12"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P003'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P003::M5A-P003-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'A-layer full text; Full text PMC; Fig. 2-3 and Extended Data Fig. 7-8',
    'Tracker experiment M5A-P003-E002',
    'Extracted details: Ccn1-cKO accelerated and spatially mislocalized WDM nodule formation, increased intracellular myelin and axon debris while attenuating extracellular debris clearance, reduced TREM2/Gpnmb/Igf1 WDM specification and lipid-droplet buffering, and impaired cold thermoception and mechanosensory recovery. Locomotor recovery was equivalent to wild type, showing tract-specific rather than universal functional loss. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "WDM nodule, debris, lipid, sensory, and modified-BMS outcomes at 7, 28, and 90 dpi; thermal/mechanical sensory recovery through 84 dpi", "control_type": "Wild-type littermate/age-matched mice and healthy controls; tamoxifen-treated conditional knockout and wild-type comparisons", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Unilateral T12 hemisection with microknife; study inclusion required complete unilateral hindlimb paralysis for 3 days", "injury_model": "T12 incomplete hemisection SCI", "injury_severity": "Incomplete hemisection", "intervention_type": "Astrocyte-specific Ccn1 deletion", "methods_summary": "Ccn1-cKO accelerated and spatially mislocalized WDM nodule formation, increased intracellular myelin and axon debris while attenuating extracellular debris clearance, reduced TREM2/Gpnmb/Igf1 WDM specification and lipid-droplet buffering, and impaired cold thermoception and mechanosensory recovery. Locomotor recovery was equivalent to wild type, showing tract-specific rather than universal functional loss.", "observation_tracker_ids": ["M5B-O050"], "sex": "Male and female", "source_experiment_tracker_id": "M5A-P003-E002", "source_paper_tracker_id": "M5A-P003", "species": "Mouse", "strain": "Aldh1l1-CreERT2::Ccn1 flox/flox conditional astrocyte knockout and wild-type controls", "tracker_key": "M5A-P003::M5A-P003-E002", "vertebral_level": "T12"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P003'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P003::M5A-P003-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'A-layer full text; Full text PMC; ventral-root histology',
    'Tracker experiment M5A-P004-E001',
    'Extracted details: Large-diameter myelinated axons were counted in formalin-fixed ventral roots from human SCI cases to estimate motoneuron loss and denervation. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "At least 6 months after SCI; postmortem sampling within 24 h of death", "control_type": "Uninjured or above-lesion ventral roots and roots at/below the lesion", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Postmortem ventral-root sampling", "injury_model": "Human traumatic SCI, contusion or laceration", "injury_severity": "Lesion epicenters at C7, C8, T4, and L1 in reported cases", "intervention_type": "Ventral-root axon and motoneuron-surrogate quantification", "methods_summary": "Large-diameter myelinated axons were counted in formalin-fixed ventral roots from human SCI cases to estimate motoneuron loss and denervation.", "observation_tracker_ids": ["M5B-O004"], "sex": "Sex and age as reported", "source_experiment_tracker_id": "M5A-P004-E001", "source_paper_tracker_id": "M5A-P004", "species": "Human", "strain": "Postmortem SCI tissue-bank cases", "tracker_key": "M5A-P004::M5A-P004-E001", "vertebral_level": "Injury levels as reported"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P004'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P004::M5A-P004-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'A-layer full text; Full text PMC; myelin g-ratio analysis',
    'Tracker experiment M5A-P004-E002',
    'Extracted details: Roots at or below the epicenter contained unusually thinly myelinated large fibers and increased g-ratios, supporting incomplete remyelination alongside motoneuron loss and chronic muscle denervation. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Chronic postmortem tissue; roots at, above, and below epicenters", "control_type": "Above-lesion comparator roots and uninjured reference values", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Ventral-root histology and solochrome cyanine/axon staining", "injury_model": "Human traumatic SCI, contusion or laceration", "injury_severity": "Lesion epicenters at C7, C8, T4, and L1 in reported cases", "intervention_type": "Myelin thickness and g-ratio analysis", "methods_summary": "Roots at or below the epicenter contained unusually thinly myelinated large fibers and increased g-ratios, supporting incomplete remyelination alongside motoneuron loss and chronic muscle denervation.", "observation_tracker_ids": ["M5B-O051"], "sex": "Sex and age as reported", "source_experiment_tracker_id": "M5A-P004-E002", "source_paper_tracker_id": "M5A-P004", "species": "Human", "strain": "Postmortem SCI tissue-bank cases", "tracker_key": "M5A-P004::M5A-P004-E002", "vertebral_level": "Injury levels as reported"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P004'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P004::M5A-P004-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'A-layer full text; Full text PMC; C5 dorsal hemisection',
    'Tracker experiment M5A-P005-E001',
    'Extracted details: Snph loss reduced injury-associated mitochondrial damage and axonal energy deficit, limited CST dieback, and increased CST regeneration after C5 dorsal hemisection. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "BDA tracing and regeneration follow-up to 8 weeks", "control_type": "Wild-type littermates versus Snph knockout; blinded axon and behavior analyses", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Microsurgical dorsal hemisection", "injury_model": "C5 dorsal hemisection SCI", "injury_severity": "Dorsal hemisection as reported", "intervention_type": "Syntaphilin deletion to increase axonal mitochondrial transport", "methods_summary": "Snph loss reduced injury-associated mitochondrial damage and axonal energy deficit, limited CST dieback, and increased CST regeneration after C5 dorsal hemisection.", "observation_tracker_ids": ["M5B-O005"], "sex": "Both sexes unless otherwise stated", "source_experiment_tracker_id": "M5A-P005-E001", "source_paper_tracker_id": "M5A-P005", "species": "Mouse", "strain": "Snph knockout and C57BL/6 wild-type", "tracker_key": "M5A-P005::M5A-P005-E001", "vertebral_level": "C5"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P005'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P005::M5A-P005-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'A-layer full text; Full text PMC; T8 transection and creatine/DREADD assays',
    'Tracker experiment M5A-P005-E002',
    'Extracted details: Snph knockout promoted monoaminergic and CST regeneration, functional synapses, and skilled forelimb recovery; creatine boosted regeneration in knockout mice, and DREADD silencing tested the regenerated-CST contribution to behavior. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Regeneration and behavioral follow-up to 8 weeks; creatine twice daily", "control_type": "Wild-type or saline controls; DREADD silencing of regenerated CST axons", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Complete transection; cortical and spinal viral tracing/manipulation", "injury_model": "T8 complete transection plus CST sprouting and functional-recovery assays", "injury_severity": "Complete transection as reported", "intervention_type": "Enhanced mitochondrial transport or creatine 2 g/kg by gavage", "methods_summary": "Snph knockout promoted monoaminergic and CST regeneration, functional synapses, and skilled forelimb recovery; creatine boosted regeneration in knockout mice, and DREADD silencing tested the regenerated-CST contribution to behavior.", "observation_tracker_ids": ["M5B-O052"], "sex": "Both sexes unless otherwise stated", "source_experiment_tracker_id": "M5A-P005-E002", "source_paper_tracker_id": "M5A-P005", "species": "Mouse", "strain": "Snph knockout and wild-type", "tracker_key": "M5A-P005::M5A-P005-E002", "vertebral_level": "T8"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P005'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P005::M5A-P005-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / saturated A tracker',
    'Tracker experiment M5A-P006-E001',
    'Extracted details: Primary intervention or mechanism experiment for Corticospinal tract regeneration after spinal cord injury in receptor protein tyrosine phosphatase sigma deficient mice; first-pass row captures cst regeneration / receptor ptp sigma in mouse at abstract/source-title level. Extraction status: YES (abstract-level)',
    '{"chronicity_dpi_wpi": "UNKNOWN", "control_type": "Injury / vehicle / wild-type / comparator as reported", "experiment_extracted": "YES (abstract-level)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "UNKNOWN", "intervention_type": "CST regeneration / receptor PTP sigma", "methods_summary": "Primary intervention or mechanism experiment for Corticospinal tract regeneration after spinal cord injury in receptor protein tyrosine phosphatase sigma deficient mice; first-pass row captures cst regeneration / receptor ptp sigma in mouse at abstract/source-title level.", "observation_tracker_ids": ["M5B-O006"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M5A-P006-E001", "source_paper_tracker_id": "M5A-P006", "species": "Mouse", "strain": "UNKNOWN", "tracker_key": "M5A-P006::M5A-P006-E001", "vertebral_level": "UNKNOWN"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P006'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P006::M5A-P006-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M5A-P006-E002',
    'Extracted details: Outcome/mechanistic validation row for Corticospinal tract regeneration after spinal cord injury in receptor protein tyrosine phosphatase sigma deficient mice; first-pass row captures cst regeneration / receptor ptp sigma in mouse at abstract/source-title level. Extraction status: YES (abstract-level)',
    '{"chronicity_dpi_wpi": "UNKNOWN", "control_type": "Comparator/control arm as reported", "experiment_extracted": "YES (abstract-level)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "UNKNOWN", "intervention_type": "Mechanistic outcome assessment after cst regeneration / receptor ptp sigma", "methods_summary": "Outcome/mechanistic validation row for Corticospinal tract regeneration after spinal cord injury in receptor protein tyrosine phosphatase sigma deficient mice; first-pass row captures cst regeneration / receptor ptp sigma in mouse at abstract/source-title level.", "observation_tracker_ids": ["M5B-O053"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M5A-P006-E002", "source_paper_tracker_id": "M5A-P006", "species": "Mouse", "strain": "UNKNOWN", "tracker_key": "M5A-P006::M5A-P006-E002", "vertebral_level": "UNKNOWN"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P006'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P006::M5A-P006-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'A-layer full text; Full text PMC; Fig. 1',
    'Tracker experiment M5A-P007-E001',
    'Extracted details: Grafts supported extensive BDA-labeled CST regeneration into the lesion, with about 1,650 axons at 0.5 mm inside the graft and synaptic-marker and ultrastructural evidence of graft contacts. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Graft follow-up 6 weeks after transplantation", "control_type": "No graft, syngeneic bone-marrow stromal-cell graft, and other non-neural graft controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Complete transection with NPC grafting 2 weeks later", "injury_model": "T3 complete transection SCI", "injury_severity": "Complete transection", "intervention_type": "Caudalized embryonic spinal neural progenitor-cell graft", "methods_summary": "Grafts supported extensive BDA-labeled CST regeneration into the lesion, with about 1,650 axons at 0.5 mm inside the graft and synaptic-marker and ultrastructural evidence of graft contacts.", "observation_tracker_ids": ["M5B-O007"], "sex": "Female", "source_experiment_tracker_id": "M5A-P007-E001", "source_paper_tracker_id": "M5A-P007", "species": "Rat", "strain": "Female Fischer 344; E14 rat spinal NPC grafts", "tracker_key": "M5A-P007::M5A-P007-E001", "vertebral_level": "T3"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P007'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P007::M5A-P007-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'A-layer full text; Full text PMC; Fig. 2-3',
    'Tracker experiment M5A-P007-E002',
    'Extracted details: Smaller grafts allowed some CST axons to cross the caudal host-graft interface; regenerated CST axons formed functional glutamatergic EPSCs in graft neurons, supporting a graft-mediated relay rather than axon presence alone. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Graft and circuit follow-up 4-6 weeks after injury", "control_type": "Lesion-only and non-neural graft controls; glutamatergic blockade during electrophysiology", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Focal CST lesion and NPC graft at injury site", "injury_model": "C4 focal CST lesion or transection with NPC graft", "injury_severity": "Focal lesion as reported", "intervention_type": "Homologous spinal NPC graft for relay formation", "methods_summary": "Smaller grafts allowed some CST axons to cross the caudal host-graft interface; regenerated CST axons formed functional glutamatergic EPSCs in graft neurons, supporting a graft-mediated relay rather than axon presence alone.", "observation_tracker_ids": ["M5B-O054"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M5A-P007-E002", "source_paper_tracker_id": "M5A-P007", "species": "Rat", "strain": "Adult rats with E14 spinal NPC grafts", "tracker_key": "M5A-P007::M5A-P007-E002", "vertebral_level": "C4"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P007'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P007::M5A-P007-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / saturated A tracker',
    'Tracker experiment M5A-P008-E001',
    'Extracted details: Primary intervention or mechanism experiment for Injured adult neurons regress to an embryonic transcriptional growth state; first-pass row captures intrinsic neuronal growth state in mouse at abstract/source-title level. Extraction status: YES (abstract-level)',
    '{"chronicity_dpi_wpi": "UNKNOWN", "control_type": "Injury / vehicle / wild-type / comparator as reported", "experiment_extracted": "YES (abstract-level)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "UNKNOWN", "intervention_type": "Intrinsic neuronal growth state", "methods_summary": "Primary intervention or mechanism experiment for Injured adult neurons regress to an embryonic transcriptional growth state; first-pass row captures intrinsic neuronal growth state in mouse at abstract/source-title level.", "observation_tracker_ids": ["M5B-O008"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M5A-P008-E001", "source_paper_tracker_id": "M5A-P008", "species": "Mouse", "strain": "UNKNOWN", "tracker_key": "M5A-P008::M5A-P008-E001", "vertebral_level": "UNKNOWN"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P008'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P008::M5A-P008-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M5A-P008-E002',
    'Extracted details: Outcome/mechanistic validation row for Injured adult neurons regress to an embryonic transcriptional growth state; first-pass row captures intrinsic neuronal growth state in mouse at abstract/source-title level. Extraction status: YES (abstract-level)',
    '{"chronicity_dpi_wpi": "UNKNOWN", "control_type": "Comparator/control arm as reported", "experiment_extracted": "YES (abstract-level)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "UNKNOWN", "intervention_type": "Mechanistic outcome assessment after intrinsic neuronal growth state", "methods_summary": "Outcome/mechanistic validation row for Injured adult neurons regress to an embryonic transcriptional growth state; first-pass row captures intrinsic neuronal growth state in mouse at abstract/source-title level.", "observation_tracker_ids": ["M5B-O055"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M5A-P008-E002", "source_paper_tracker_id": "M5A-P008", "species": "Mouse", "strain": "UNKNOWN", "tracker_key": "M5A-P008::M5A-P008-E002", "vertebral_level": "UNKNOWN"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P008'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P008::M5A-P008-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / saturated A tracker',
    'Tracker experiment M5A-P009-E001',
    'Extracted details: Primary intervention or mechanism experiment for Activation of MAP2K signaling by genetic engineering or HF-rTMS promotes corticospinal axon sprouting and functional regeneration; first-pass row captures cst sprouting/regeneration in rodent model context at abstract/source-title level. Extraction status: YES (abstract-level)',
    '{"chronicity_dpi_wpi": "UNKNOWN", "control_type": "Injury / vehicle / wild-type / comparator as reported", "experiment_extracted": "YES (abstract-level)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "UNKNOWN", "intervention_type": "CST sprouting/regeneration", "methods_summary": "Primary intervention or mechanism experiment for Activation of MAP2K signaling by genetic engineering or HF-rTMS promotes corticospinal axon sprouting and functional regeneration; first-pass row captures cst sprouting/regeneration in rodent model context at abstract/source-title level.", "observation_tracker_ids": ["M5B-O009"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M5A-P009-E001", "source_paper_tracker_id": "M5A-P009", "species": "Rodent model context", "strain": "UNKNOWN", "tracker_key": "M5A-P009::M5A-P009-E001", "vertebral_level": "UNKNOWN"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P009'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P009::M5A-P009-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M5A-P009-E002',
    'Extracted details: Outcome/mechanistic validation row for Activation of MAP2K signaling by genetic engineering or HF-rTMS promotes corticospinal axon sprouting and functional regeneration; first-pass row captures cst sprouting/regeneration in rodent model context at abstract/source-title level. Extraction status: YES (abstract-level)',
    '{"chronicity_dpi_wpi": "UNKNOWN", "control_type": "Comparator/control arm as reported", "experiment_extracted": "YES (abstract-level)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "UNKNOWN", "intervention_type": "Mechanistic outcome assessment after cst sprouting/regeneration", "methods_summary": "Outcome/mechanistic validation row for Activation of MAP2K signaling by genetic engineering or HF-rTMS promotes corticospinal axon sprouting and functional regeneration; first-pass row captures cst sprouting/regeneration in rodent model context at abstract/source-title level.", "observation_tracker_ids": ["M5B-O056"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M5A-P009-E002", "source_paper_tracker_id": "M5A-P009", "species": "Rodent model context", "strain": "UNKNOWN", "tracker_key": "M5A-P009::M5A-P009-E002", "vertebral_level": "UNKNOWN"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P009'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P009::M5A-P009-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'A-layer full text; Full text PMC; Fig. 3-4',
    'Tracker experiment M5A-P010-E001',
    'Extracted details: Optogenetic stimulation increased BDA-labeled CST axon index at the injury site (9.75% vs 0.49%) and caudal within 2 mm (5.56% vs 0.34%), increased motor-evoked-potential amplitude and improved BMS/grid/open-field hindlimb movement after complete transection. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Stimulation from 2 weeks post-SCI for 14 days; BDA and behavior through 6 weeks", "control_type": "Nonstimulated ChR2-YFP mice", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Complete transection after T9-T10 laminectomy and durotomy; bilateral cortical LED device", "injury_model": "T10 complete spinal transection with 1-mm segment removed", "injury_severity": "Complete transection", "intervention_type": "Bilateral transcranial 473-nm LED stimulation, 10 Hz selected from in vitro screen, 40 min daily for 14 days", "methods_summary": "Optogenetic stimulation increased BDA-labeled CST axon index at the injury site (9.75% vs 0.49%) and caudal within 2 mm (5.56% vs 0.34%), increased motor-evoked-potential amplitude and improved BMS/grid/open-field hindlimb movement after complete transection.", "observation_tracker_ids": ["M5B-O010"], "sex": "Female", "source_experiment_tracker_id": "M5A-P010-E001", "source_paper_tracker_id": "M5A-P010", "species": "Mouse", "strain": "Female Thy1-ChR2-YFP transgenic mice, 6-8 weeks, 18-22 g", "tracker_key": "M5A-P010::M5A-P010-E001", "vertebral_level": "T10"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P010'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P010::M5A-P010-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'A-layer full text; Full text PMC; Fig. 2, 5-6',
    'Tracker experiment M5A-P010-E002',
    'Extracted details: Blue light increased ChR2-specific neurite number/length and in vivo cortical p-JAK2/p-STAT3; FLLL31 attenuated stimulated neurite outgrowth, supporting pathway involvement but not proving in vivo JAK2/STAT3 necessity. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Slice assay acute; cortical proteomics at 6 weeks; inhibitor assay during 40-min stimulation", "control_type": "ChR2 without light, WT with light, and ChR2+light with FLLL31 controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Blue-light stimulation of ChR2+ cortical neurons; JAK2/STAT3 pathway analysis and FLLL31 blockade", "injury_model": "Organotypic motor-cortex neurite assay and complete T10 transection", "injury_severity": "In vitro neurite injury/regrowth assay and complete transection", "intervention_type": "FLLL31 STAT3-phosphorylation inhibitor in stimulated ChR2+ slices", "methods_summary": "Blue light increased ChR2-specific neurite number/length and in vivo cortical p-JAK2/p-STAT3; FLLL31 attenuated stimulated neurite outgrowth, supporting pathway involvement but not proving in vivo JAK2/STAT3 necessity.", "observation_tracker_ids": ["M5B-O057"], "sex": "Female in vivo; not applicable in vitro", "source_experiment_tracker_id": "M5A-P010-E002", "source_paper_tracker_id": "M5A-P010", "species": "ChR2-YFP cortical slices and mouse SCI model", "strain": "ChR2-YFP and wild-type mice; slice cultures plus injured transgenic mice", "tracker_key": "M5A-P010::M5A-P010-E002", "vertebral_level": "T10 in vivo"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P010'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P010::M5A-P010-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'A-layer full text; Full text PMC',
    'Tracker experiment M5A-P011-E001',
    'Extracted details: Lipin1 knockdown promoted CST sprouting after pyramidotomy and robust CST regeneration after complete T8 SCI. Neonatal delivery before adult SCI produced axons extending up to about 3 mm caudal to the lesion, while adult delivery also increased regeneration. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "P14 and adult; 2-18 weeks after intervention", "control_type": "AAV9-shCtrl or GFP controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Complete T8 crush; AAV9 cortical delivery and cortical pyramidotomy for sprouting", "injury_model": "Complete T8 spinal crush plus unilateral pyramidotomy", "injury_severity": "Complete crush; unilateral CST lesion", "intervention_type": "AAV9-shLipin1 in cortex before injury; adult complete T8 SCI tested after neonatal or adult cortical delivery", "methods_summary": "Lipin1 knockdown promoted CST sprouting after pyramidotomy and robust CST regeneration after complete T8 SCI. Neonatal delivery before adult SCI produced axons extending up to about 3 mm caudal to the lesion, while adult delivery also increased regeneration.", "observation_tracker_ids": ["M5B-O011"], "sex": "Female for complete SCI experiments", "source_experiment_tracker_id": "M5A-P011-E001", "source_paper_tracker_id": "M5A-P011", "species": "Mouse SCI and cortical neuron model", "strain": "WT mice; exact strain not stated in extracted methods", "tracker_key": "M5A-P011::M5A-P011-E001", "vertebral_level": "T8"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P011'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P011::M5A-P011-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'A-layer full text; Full text PMC',
    'Tracker experiment M5A-P011-E002',
    'Extracted details: Lipin1 knockdown increased PA and LPA and activated mTOR and/or STAT3 in neuronal models. mTOR or STAT3 loss reduced lipin1-KD-induced regeneration, while DRG lipin1 knockdown promoted ascending sensory axon growth through the lesion. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Acute to 18 weeks depending on assay", "control_type": "shCtrl, vehicle, conditional knockout, and lipid vehicle controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "AAV2/AAV9 shRNA or Cre delivery; lipid vesicles for PA/LPA", "injury_model": "Optic nerve crush, cultured neurons, dorsal column crush, and complete T8 SCI", "injury_severity": "Injury models as reported", "intervention_type": "Lipin1 knockdown or PA/LPA delivery; mTOR and STAT3 conditional deletion for mechanism testing", "methods_summary": "Lipin1 knockdown increased PA and LPA and activated mTOR and/or STAT3 in neuronal models. mTOR or STAT3 loss reduced lipin1-KD-induced regeneration, while DRG lipin1 knockdown promoted ascending sensory axon growth through the lesion.", "observation_tracker_ids": ["M5B-O058"], "sex": "Female for complete SCI experiments; other assays as reported", "source_experiment_tracker_id": "M5A-P011-E002", "source_paper_tracker_id": "M5A-P011", "species": "Mouse retinal, cortical, DRG, and SCI validation models", "strain": "WT, mTOR-flox, Rptor-flox, Stat3-flox, and related conditional lines", "tracker_key": "M5A-P011::M5A-P011-E002", "vertebral_level": "T8 for SCI; optic nerve and DRG assays otherwise"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P011'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P011::M5A-P011-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / saturated A tracker',
    'Tracker experiment M5A-P012-E001',
    'Extracted details: Primary intervention or mechanism experiment for Effects of transcranial magnetic stimulation on axonal regeneration in the corticospinal tract of female rats with spinal cord injury.; first-pass row captures activity or stimulation-enabled axon repair in rat sci model at abstract/source-title level. Extraction status: YES (abstract-level)',
    '{"chronicity_dpi_wpi": "UNKNOWN", "control_type": "Injury / vehicle / wild-type / comparator as reported", "experiment_extracted": "YES (abstract-level)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "UNKNOWN", "intervention_type": "Activity or stimulation-enabled axon repair", "methods_summary": "Primary intervention or mechanism experiment for Effects of transcranial magnetic stimulation on axonal regeneration in the corticospinal tract of female rats with spinal cord injury.; first-pass row captures activity or stimulation-enabled axon repair in rat sci model at abstract/source-title level.", "observation_tracker_ids": ["M5B-O012"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M5A-P012-E001", "source_paper_tracker_id": "M5A-P012", "species": "Rat SCI model", "strain": "UNKNOWN", "tracker_key": "M5A-P012::M5A-P012-E001", "vertebral_level": "UNKNOWN"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P012'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P012::M5A-P012-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M5A-P012-E002',
    'Extracted details: Outcome/mechanistic validation row for Effects of transcranial magnetic stimulation on axonal regeneration in the corticospinal tract of female rats with spinal cord injury.; first-pass row captures activity or stimulation-enabled axon repair in rat sci model at abstract/source-title level. Extraction status: YES (abstract-level)',
    '{"chronicity_dpi_wpi": "UNKNOWN", "control_type": "Comparator/control arm as reported", "experiment_extracted": "YES (abstract-level)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "UNKNOWN", "intervention_type": "Mechanistic outcome assessment after activity or stimulation-enabled axon repair", "methods_summary": "Outcome/mechanistic validation row for Effects of transcranial magnetic stimulation on axonal regeneration in the corticospinal tract of female rats with spinal cord injury.; first-pass row captures activity or stimulation-enabled axon repair in rat sci model at abstract/source-title level.", "observation_tracker_ids": ["M5B-O059"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M5A-P012-E002", "source_paper_tracker_id": "M5A-P012", "species": "Rat SCI model", "strain": "UNKNOWN", "tracker_key": "M5A-P012::M5A-P012-E002", "vertebral_level": "UNKNOWN"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P012'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P012::M5A-P012-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'A-layer full text; Full text PMC',
    'Tracker experiment M5A-P013-E001',
    'Extracted details: Syt4 silencing inhibited neurite elongation in primary cortical neurons without reducing cell number. RNA-seq showed altered neuronal development and neurite projection programs, supporting Syt4 as an intrinsic growth regulator. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "1-4 d culture", "control_type": "Control siRNA and non-targeting screen controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Trypsinization and replating to remove pre-existing neurites", "injury_model": "In vitro neurite regrowth assay after neurite removal", "injury_severity": "In vitro axonal injury mimic", "intervention_type": "Syt4 siRNA pool or individual siRNAs after plating, followed by neurite removal and regrowth", "methods_summary": "Syt4 silencing inhibited neurite elongation in primary cortical neurons without reducing cell number. RNA-seq showed altered neuronal development and neurite projection programs, supporting Syt4 as an intrinsic growth regulator.", "observation_tracker_ids": ["M5B-O013"], "sex": "Not applicable in vitro", "source_experiment_tracker_id": "M5A-P013-E001", "source_paper_tracker_id": "M5A-P013", "species": "Primary cortical neurons", "strain": "C57BL/6J; postnatal day 1 cultures", "tracker_key": "M5A-P013::M5A-P013-E001", "vertebral_level": "Not applicable"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P013'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P013::M5A-P013-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'A-layer full text; Full text PMC',
    'Tracker experiment M5A-P013-E002',
    'Extracted details: Cortical Syt4 knockdown reduced CST collateral sprouting and worsened ladder-walking hindlimb errors after SCI, whereas the paper’s central comparison supports endogenous Syt4 as necessary for spontaneous CST sprouting and neurological recovery. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "21-56 dpi", "control_type": "AAV control shRNA or control overexpression vectors", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Dorsal hemisection to 1 mm depth", "injury_model": "Th10 dorsal hemisection", "injury_severity": "Partial thoracic transection", "intervention_type": "AAV9-shSyt4, control shRNA, Syt4 overexpression, or control vector injected into hindlimb motor cortex", "methods_summary": "Cortical Syt4 knockdown reduced CST collateral sprouting and worsened ladder-walking hindlimb errors after SCI, whereas the paper\u2019s central comparison supports endogenous Syt4 as necessary for spontaneous CST sprouting and neurological recovery.", "observation_tracker_ids": ["M5B-O060"], "sex": "Female", "source_experiment_tracker_id": "M5A-P013-E002", "source_paper_tracker_id": "M5A-P013", "species": "Mouse SCI model", "strain": "C57BL/6J", "tracker_key": "M5A-P013::M5A-P013-E002", "vertebral_level": "Th10"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P013'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P013::M5A-P013-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'A-layer full text; Full text PMC',
    'Tracker experiment M5A-P014-E001',
    'Extracted details: Early gabapentin treatment promoted CST sprouting and regeneration, improved forelimb skilled walking and reduced hypersensitivity. Regenerating CST axons formed synaptic structures and increased functional connectivity rostral and caudal to the lesion. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "1 h after injury through 4 months", "control_type": "Vehicle-treated SCI mice", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "No. 5 modified forceps; complete unilateral hemisection", "injury_model": "C5 lateral hemisection", "injury_severity": "Complete unilateral cervical hemisection", "intervention_type": "Gabapentin 46 mg/kg intraperitoneally, 3 times daily for 1 week then 2 times daily until endpoint", "methods_summary": "Early gabapentin treatment promoted CST sprouting and regeneration, improved forelimb skilled walking and reduced hypersensitivity. Regenerating CST axons formed synaptic structures and increased functional connectivity rostral and caudal to the lesion.", "observation_tracker_ids": ["M5B-O014"], "sex": "Female and male", "source_experiment_tracker_id": "M5A-P014-E001", "source_paper_tracker_id": "M5A-P014", "species": "Mouse SCI model", "strain": "C57BL/6J", "tracker_key": "M5A-P014::M5A-P014-E001", "vertebral_level": "C5"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P014'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P014::M5A-P014-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'A-layer full text; Full text PMC',
    'Tracker experiment M5A-P014-E002',
    'Extracted details: Silencing the regenerated or reorganized CST projections with CNO abolished gabapentin-associated forelimb recovery, supporting a causal role for CST circuit reorganization. Gabapentin’s repair effect was interpreted as alpha2delta2 blockade-linked plasticity rather than only analgesia. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "4 months after SCI; acute and developmental comparisons also reported", "control_type": "Vehicle, sham, and CNO or vehicle chemogenetic controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Forceps hemisection; AAV-ChR2 or AAV-hM4D injection into forelimb motor cortex", "injury_model": "C5 lateral hemisection; cortical pyramidotomy for sprouting comparison", "injury_severity": "Complete unilateral cervical hemisection", "intervention_type": "Gabapentin as above; transient hM4D-mediated silencing of injured CST projections", "methods_summary": "Silencing the regenerated or reorganized CST projections with CNO abolished gabapentin-associated forelimb recovery, supporting a causal role for CST circuit reorganization. Gabapentin\u2019s repair effect was interpreted as alpha2delta2 blockade-linked plasticity rather than only analgesia.", "observation_tracker_ids": ["M5B-O061"], "sex": "Female and male", "source_experiment_tracker_id": "M5A-P014-E002", "source_paper_tracker_id": "M5A-P014", "species": "Mouse SCI model with optogenetic and chemogenetic validation", "strain": "C57BL/6J; GFP-M reporter mice for selected assays", "tracker_key": "M5A-P014::M5A-P014-E002", "vertebral_level": "C5"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P014'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P014::M5A-P014-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'A-layer full text; Full text PMC',
    'Tracker experiment M5A-P015-E001',
    'Extracted details: Activated alpha9 integrin-kindlin-1 enabled sensory axons to regenerate through the lesion and along the spinal cord, with roughly half of labeled axons crossing the lesion and near-complete functional sensory pathway reconstruction on tape-removal, von Frey, and thermal tests. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "4-12 weeks post-injury; behavioral testing every 2 weeks", "control_type": "Uninjured and vector/control groups", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Fine Bonn forceps, 1.5 mm at C4 or 1 mm at T10, held 15 s", "injury_model": "C4 or T10 dorsal-column crush", "injury_severity": "Complete dorsal-column lesion", "intervention_type": "AAV1 activated alpha9 integrin with kindlin-1 delivered to C6/C7 or L4/L5 DRGs at the time of lesion", "methods_summary": "Activated alpha9 integrin-kindlin-1 enabled sensory axons to regenerate through the lesion and along the spinal cord, with roughly half of labeled axons crossing the lesion and near-complete functional sensory pathway reconstruction on tape-removal, von Frey, and thermal tests.", "observation_tracker_ids": ["M5B-O015"], "sex": "Female main cohort; male supportive time course", "source_experiment_tracker_id": "M5A-P015-E001", "source_paper_tracker_id": "M5A-P015", "species": "Rat sensory SCI model", "strain": "Lister-Hooded", "tracker_key": "M5A-P015::M5A-P015-E001", "vertebral_level": "C4 or T10"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P015'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P015::M5A-P015-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'A-layer full text; Full text PMC',
    'Tracker experiment M5A-P015-E002',
    'Extracted details: Regenerating alpha9-kindlin axons crossed the lesion through laminin-111 and tenascin-C-positive connective bridges, extended toward high cervical segments, and formed rostral and caudal collateral branches. The study supports a sensory-pathway repair strategy, not direct motor CST regeneration. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "4, 6, 8, and 12 weeks for axon time course; 12 week endpoint", "control_type": "Control vector, uninjured, and integrin-only or kindlin-only comparisons", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Fine Bonn forceps after laminectomy", "injury_model": "C4 or T10 dorsal-column crush", "injury_severity": "Complete dorsal-column lesion", "intervention_type": "AAV alpha9-V5 plus kindlin-1-GFP; DRG injection and tissue-clearing or light-sheet analysis", "methods_summary": "Regenerating alpha9-kindlin axons crossed the lesion through laminin-111 and tenascin-C-positive connective bridges, extended toward high cervical segments, and formed rostral and caudal collateral branches. The study supports a sensory-pathway repair strategy, not direct motor CST regeneration.", "observation_tracker_ids": ["M5B-O062"], "sex": "Female main cohort; male supportive cohort", "source_experiment_tracker_id": "M5A-P015-E002", "source_paper_tracker_id": "M5A-P015", "species": "Rat sensory SCI model with tract and bridge validation", "strain": "Lister-Hooded females; Wistar males for time course", "tracker_key": "M5A-P015::M5A-P015-E002", "vertebral_level": "C4 or T10"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P015'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P015::M5A-P015-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'A-layer full text; Full text PMC',
    'Tracker experiment M5A-P016-E001',
    'Extracted details: RhoA/Pten deletion reduced CST axon dieback but alone did not fully restore function. Adding neuronal stimulation promoted greater CST collateral growth and forelimb motor recovery than genetic manipulation alone, with grid-walking improvement and new presynaptic bouton formation near the lesion. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "3-7 weeks post-lesion", "control_type": "LacZ, vehicle, and single-strategy genetic controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Complete dorsal column transection after cervical exposure", "injury_model": "C5 dorsal column lesion", "injury_severity": "Complete dorsal column lesion", "intervention_type": "AAV-mediated RhoA/Pten deletion in corticospinal neurons combined with excitatory hM3Dq DREADD stimulation using DCZ", "methods_summary": "RhoA/Pten deletion reduced CST axon dieback but alone did not fully restore function. Adding neuronal stimulation promoted greater CST collateral growth and forelimb motor recovery than genetic manipulation alone, with grid-walking improvement and new presynaptic bouton formation near the lesion.", "observation_tracker_ids": ["M5B-O016"], "sex": "Male and female", "source_experiment_tracker_id": "M5A-P016-E001", "source_paper_tracker_id": "M5A-P016", "species": "Mouse cervical SCI model", "strain": "RhoA-flox;Pten-flox on C57BL/6 background", "tracker_key": "M5A-P016::M5A-P016-E001", "vertebral_level": "C5"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P016'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P016::M5A-P016-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'A-layer full text; Full text PMC',
    'Tracker experiment M5A-P016-E002',
    'Extracted details: Stimulation increased c-Fos activation in targeted corticospinal neurons, suppressed CST dieback, increased collateral projections and presynaptic boutons in spinal gray matter, and improved skilled forelimb behavior. The combined intervention supports circuit rewiring rather than simple lesion-site axon passage. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "21-49 dpi", "control_type": "LacZ, water, DCZ, and genetic control cohorts", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Complete dorsal column transection; cortical and retrograde AAV targeting", "injury_model": "C5 dorsal column lesion", "injury_severity": "Complete dorsal column lesion", "intervention_type": "AAV8/AAVretro targeting of C5-projecting CST neurons, RhoA/Pten conditional deletion, and hM3Dq activation by DCZ", "methods_summary": "Stimulation increased c-Fos activation in targeted corticospinal neurons, suppressed CST dieback, increased collateral projections and presynaptic boutons in spinal gray matter, and improved skilled forelimb behavior. The combined intervention supports circuit rewiring rather than simple lesion-site axon passage.", "observation_tracker_ids": ["M5B-O063"], "sex": "Male and female", "source_experiment_tracker_id": "M5A-P016-E002", "source_paper_tracker_id": "M5A-P016", "species": "Mouse cervical SCI model with pathway and circuit validation", "strain": "RhoA-flox;Pten-flox on C57BL/6 background", "tracker_key": "M5A-P016::M5A-P016-E002", "vertebral_level": "C5"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P016'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P016::M5A-P016-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'A-layer full text; Fig. 1c-e; adult mouse motor cortex screen',
    'Tracker experiment M5A-P017-E001',
    'Extracted details: Adult mouse motor cortex neurons were exposed to candidate compounds for 5 days. Thiorphan at 250 micromolar increased total neurite outgrowth by 80% and longest neurite length by 30% versus control, with peak effects at 100-250 micromolar; triflusal was modest and non-significant, milrinone had no effect, and adiphenine reduced outgrowth. The CMap screen selected compounds by similarity to a regenerating corticospinal-neuron transcriptomic signature, but the in vitro assay was the causal growth screen. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "5 days in vitro", "control_type": "DMSO vehicle; triflusal, milrinone, and adiphenine comparator compounds", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Not applicable", "injury_model": "Primary cortical neuron culture", "injury_severity": "Not applicable", "intervention_type": "Thiorphan dose-response screen, 100-250 micromolar peak range", "methods_summary": "Adult mouse motor cortex neurons were exposed to candidate compounds for 5 days. Thiorphan at 250 micromolar increased total neurite outgrowth by 80% and longest neurite length by 30% versus control, with peak effects at 100-250 micromolar; triflusal was modest and non-significant, milrinone had no effect, and adiphenine reduced outgrowth. The CMap screen selected compounds by similarity to a regenerating corticospinal-neuron transcriptomic signature, but the in vitro assay was the causal growth screen.", "observation_tracker_ids": ["M5B-O017"], "sex": "Not applicable", "source_experiment_tracker_id": "M5A-P017-E001", "source_paper_tracker_id": "M5A-P017", "species": "Mouse", "strain": "Adult C57-derived primary motor cortex neurons; postnatal day 60 source", "tracker_key": "M5A-P017::M5A-P017-E001", "vertebral_level": "Not applicable"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P017'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P017::M5A-P017-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'A-layer full text; Fig. 2-3; severe bilateral C5 contusion and NPC graft experiment',
    'Tracker experiment M5A-P017-E002',
    'Extracted details: Adult rats received delayed continuous thiorphan infusion into left motor cortex because thiorphan does not cross the blood-brain barrier, with NPC grafting at 2 weeks post-injury. Thiorphan plus NPC graft produced a significant twofold forelimb pellet-retrieval success improvement versus lesion control (P=0.005), improved accuracy to 60% versus 30% (P=0.001), and increased corticospinal axon regeneration into the graft by 60% versus graft alone (P<0.05), with putative synaptophysin-apposed host axon/graft-neuron contacts. Thiorphan alone and NPC graft alone trended but were not significant; there was no significant change in CST sprouting above the lesion, serotonergic or CGRP axons into graft, GFAP border, graft differentiation, or graft-derived axon extension. The study supports substrate-dependent CST regeneration and functional benefit, not complete circuit restoration. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Delayed treatment beginning 2 weeks post-injury; 12-week endpoint", "control_type": "Lesion alone; thiorphan alone; diluent plus NPC graft", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Contusion; device not stated in captured full text", "injury_model": "Severe bilateral cervical contusion", "injury_severity": "Severe", "intervention_type": "Intracortical thiorphan infusion, 100 mM at 0.25 microliters/hour for 4 weeks, with or without E14 spinal-cord NPC graft into lesion cavity", "methods_summary": "Adult rats received delayed continuous thiorphan infusion into left motor cortex because thiorphan does not cross the blood-brain barrier, with NPC grafting at 2 weeks post-injury. Thiorphan plus NPC graft produced a significant twofold forelimb pellet-retrieval success improvement versus lesion control (P=0.005), improved accuracy to 60% versus 30% (P=0.001), and increased corticospinal axon regeneration into the graft by 60% versus graft alone (P<0.05), with putative synaptophysin-apposed host axon/graft-neuron contacts. Thiorphan alone and NPC graft alone trended but were not significant; there was no significant change in CST sprouting above the lesion, serotonergic or CGRP axons into graft, GFAP border, graft differentiation, or graft-derived axon extension. The study supports substrate-dependent CST regeneration and functional benefit, not complete circuit restoration.", "observation_tracker_ids": ["M5B-O064"], "sex": "Not stated", "source_experiment_tracker_id": "M5A-P017-E002", "source_paper_tracker_id": "M5A-P017", "species": "Rat", "strain": "Fischer 344", "tracker_key": "M5A-P017::M5A-P017-E002", "vertebral_level": "C5 spinal cord segment"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P017'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P017::M5A-P017-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'A-layer full text; Full text PMC',
    'Tracker experiment M5A-P018-E001',
    'Extracted details: Full-text record adds the in vitro causal cilium assay and the TTBK2 gain/loss design. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "In vitro knockdown/overexpression and post-injury knockout", "control_type": "shKIF3A, shTTBK2, TTBK2 overexpression, and control neurons", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Hemisection", "injury_model": "T10 lateral hemisection", "injury_severity": "As reported", "intervention_type": "Adenoviral manipulation showed that TTBK2 supports primary-cilium formation and spinal-neuron axon growth; TTBK2 or KIF3A loss shortened cilia and reduced axon-growth and cilium/SHH-associated transcriptional programs.", "methods_summary": "Full-text record adds the in vitro causal cilium assay and the TTBK2 gain/loss design.", "observation_tracker_ids": ["M5B-O018"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M5A-P018-E001", "source_paper_tracker_id": "M5A-P018", "species": "Mouse SCI model plus cultured spinal neurons", "strain": "C57-derived neurons; Ttbk2 conditional knockout", "tracker_key": "M5A-P018::M5A-P018-E001", "vertebral_level": "T10"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P018'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P018::M5A-P018-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'A-layer full text; Full text PMC',
    'Tracker experiment M5A-P018-E002',
    'Extracted details: Full-text result supports an endogenous repair pathway with partial pharmacological rescue, not complete circuit restoration. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Tamoxifen-induced knockout; follow-up to 14 dpi and behavioral recovery", "control_type": "WT-SCI, conditional knockout, AAV9-hSyn-Cre, cyclopamine, and SAG controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Hemisection", "injury_model": "T10 lateral hemisection", "injury_severity": "As reported", "intervention_type": "Ttbk2 deletion reduced GAP43, MAP2, newborn-neuron and downstream-circuit markers, increased PSD95/Nogo pathway signals, impaired BDA-defined downstream connectivity and BMS recovery; SHH agonist SAG partially rescued MAP2, placing SHH downstream of TTBK2-dependent ciliary regulation.", "methods_summary": "Full-text result supports an endogenous repair pathway with partial pharmacological rescue, not complete circuit restoration.", "observation_tracker_ids": ["M5B-O065"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M5A-P018-E002", "source_paper_tracker_id": "M5A-P018", "species": "Mouse SCI model", "strain": "Ttbk2fl/fl-Rosa-CreERT2+/-", "tracker_key": "M5A-P018::M5A-P018-E002", "vertebral_level": "T10"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P018'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P018::M5A-P018-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'A-layer full text; Full text PMC',
    'Tracker experiment M5A-P019-E001',
    'Extracted details: In vitro screening identified KLF7/MEF2 and ATF3/KLF7/MEF2 as potent neurite-growth combinations. The triple combination was strongest in vitro, but KLF7/MEF2 was the combination that retained benefit in vivo without the same apoptosis-associated gene signature. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "24-72 h in vitro; 12 weeks in vivo", "control_type": "No-TF, single-TF, and sham controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "AAV5 transcription-factor expression; in vitro plasmid transfection", "injury_model": "In vitro neurite-growth screen plus C4 dorsal-column lesion", "injury_severity": "In vitro growth assay; complete dorsal-column lesion in vivo", "intervention_type": "KLF7, MEF2, MEF2-VP16, ATF3, and combination expression constructs", "methods_summary": "In vitro screening identified KLF7/MEF2 and ATF3/KLF7/MEF2 as potent neurite-growth combinations. The triple combination was strongest in vitro, but KLF7/MEF2 was the combination that retained benefit in vivo without the same apoptosis-associated gene signature.", "observation_tracker_ids": ["M5B-O019"], "sex": "Not applicable in vitro; female rats in vivo", "source_experiment_tracker_id": "M5A-P019-E001", "source_paper_tracker_id": "M5A-P019", "species": "F11 neurite-outgrowth assay and rat DRG neurons", "strain": "F11 cell line; rat DRG neurons for in vivo profiling", "tracker_key": "M5A-P019::M5A-P019-E001", "vertebral_level": "C4"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P019'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P019::M5A-P019-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'A-layer full text; Full text PMC',
    'Tracker experiment M5A-P019-E002',
    'Extracted details: KLF7/MEF2, but not KLF7 or MEF2 alone and not the triple combination, promoted axonal sprouting into and around the lesion, reduced axonal retraction, improved ladder-based functional recovery, and induced a substantial regeneration-associated gene program. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "4 weeks after AAV delivery, then 12 week post-lesion endpoint", "control_type": "No-TF, KLF7, MEF2, ATF3/KLF7/MEF2, and sham groups", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "C4 laminectomy and microscissor dorsal-column transection after AAV delivery to left L4/L5 DRGs", "injury_model": "C4 dorsal-column lesion", "injury_severity": "Complete dorsal-column lesion", "intervention_type": "AAV5 KLF7/MEF2 or comparator TF constructs, 1 uL per DRG", "methods_summary": "KLF7/MEF2, but not KLF7 or MEF2 alone and not the triple combination, promoted axonal sprouting into and around the lesion, reduced axonal retraction, improved ladder-based functional recovery, and induced a substantial regeneration-associated gene program.", "observation_tracker_ids": ["M5B-O066"], "sex": "Female", "source_experiment_tracker_id": "M5A-P019-E002", "source_paper_tracker_id": "M5A-P019", "species": "Rat dorsal-column SCI model", "strain": "Wistar rats; 9-12 weeks", "tracker_key": "M5A-P019::M5A-P019-E002", "vertebral_level": "C4"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P019'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P019::M5A-P019-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'A-layer full text; Full text PMC; Fig. 1-4',
    'Tracker experiment M5A-P020-E001',
    'Extracted details: Cortical bPAC stimulation raised cAMP, p-CREB and c-Fos, restored layer-V neuron electrophysiology, increased early and sustained BBB locomotor recovery, and increased CST plasticity. The study frames benefit as cortical rerouting rather than long-distance CST regeneration. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "bPAC stimulation began 1 day post-SCI, 30 min daily, 1-s ON/4-s OFF; motor follow-up to 35 days", "control_type": "CAMKII-mCherry or inactive delta-bPAC controls and injured untreated controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Dorsal hemisection after AAV delivery to layer V motor cortex; wireless cortical optogenetic device", "injury_model": "T8 dorsal hemisection SCI", "injury_severity": "Dorsal hemisection", "intervention_type": "AAV2/9-CAMKII-bPAC-mCherry in cortical layer V with daily blue-light cAMP induction", "methods_summary": "Cortical bPAC stimulation raised cAMP, p-CREB and c-Fos, restored layer-V neuron electrophysiology, increased early and sustained BBB locomotor recovery, and increased CST plasticity. The study frames benefit as cortical rerouting rather than long-distance CST regeneration.", "observation_tracker_ids": ["M5B-O020"], "sex": "Female", "source_experiment_tracker_id": "M5A-P020-E001", "source_paper_tracker_id": "M5A-P020", "species": "Rat", "strain": "Female rats, 3-5 months", "tracker_key": "M5A-P020::M5A-P020-E001", "vertebral_level": "T8"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P020'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P020::M5A-P020-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'A-layer full text; Full text PMC; Fig. 5-6',
    'Tracker experiment M5A-P020-E002',
    'Extracted details: bPAC increased lumbar-projecting brainstem neuron sparing, raphe-reticular cAMP signaling, caudal 5-HT tract density and excitatory/inhibitory balance; 5,7-DHT depletion abolished bPAC-mediated motor recovery, supporting serotonergic pathway necessity. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Circuit tracing and neurotransmitter assays through 35 days; 5,7-DHT at 22 days post-SCI", "control_type": "Control/bPAC with or without intraventricular 5,7-DHT; sham vehicle controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Cortical bPAC stimulation, WGA tracing, brainstem retrograde tracing, and serotonergic depletion", "injury_model": "T8 dorsal hemisection with circuit-mechanism validation", "injury_severity": "Dorsal hemisection", "intervention_type": "5,7-DHT serotonergic neurotoxin with desipramine protection of noradrenergic neurons", "methods_summary": "bPAC increased lumbar-projecting brainstem neuron sparing, raphe-reticular cAMP signaling, caudal 5-HT tract density and excitatory/inhibitory balance; 5,7-DHT depletion abolished bPAC-mediated motor recovery, supporting serotonergic pathway necessity.", "observation_tracker_ids": ["M5B-O067"], "sex": "Female", "source_experiment_tracker_id": "M5A-P020-E002", "source_paper_tracker_id": "M5A-P020", "species": "Rat", "strain": "Female rats; lumbar-projecting brainstem and serotonergic tract analyses", "tracker_key": "M5A-P020::M5A-P020-E002", "vertebral_level": "T8"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P020'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P020::M5A-P020-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'A-layer full text; Full text PMC; Fig. 1-4',
    'Tracker experiment M5A-P021-E001',
    'Extracted details: Glu-UCNP plus NIR increased CST sprouting across the lesion toward Chx10+/PSD95+ interneurons, raised GAP43 and synaptic-marker signals, and produced greater calcium activity in reconnected circuits than nanoparticle or light controls. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Glu-UCNP or PEG-UCNP 200 microgram/ml, 2 microliters at four sites; pulsed NIR 15 ms/20 Hz every other day for 84 days", "control_type": "PEG-UCNP, Glu-UCNP, and no-NIR controls; vehicle/sham and toxicity controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "AAV-EF1a-VChR1-GFP or mCherry in sensorimotor cortex; dorsal cord cut to central canal; spinal UCNP injections", "injury_model": "C4-C6 dorsal hemisection", "injury_severity": "Cervical dorsal hemisection", "intervention_type": "Glutamate-linked upconversion nanoparticles to target glutamatergic postsynaptic neurons and transduce NIR into VChR1 excitation", "methods_summary": "Glu-UCNP plus NIR increased CST sprouting across the lesion toward Chx10+/PSD95+ interneurons, raised GAP43 and synaptic-marker signals, and produced greater calcium activity in reconnected circuits than nanoparticle or light controls.", "observation_tracker_ids": ["M5B-O021"], "sex": "Not stated", "source_experiment_tracker_id": "M5A-P021-E001", "source_paper_tracker_id": "M5A-P021", "species": "Mouse", "strain": "C57BL/6J mice; sex not stated in extracted methods", "tracker_key": "M5A-P021::M5A-P021-E001", "vertebral_level": "C4-C6"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P021'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P021::M5A-P021-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'A-layer full text; Full text PMC; Fig. 5-7',
    'Tracker experiment M5A-P021-E002',
    'Extracted details: Glu-UCNP plus NIR raised pellet-reaching success to about 48% by 70 days versus below 20% in other SCI groups; retransection reduced performance, and KYNA reduced caudal calcium activity, supporting functional glutamatergic reconnection rather than axon presence alone. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Functional testing to 84 days; retransection after recovery; KYNA used as glutamatergic antagonist", "control_type": "PEG-UCNP/NIR, Glu-UCNP/NIR, Glu-UCNP without NIR, and Glu-UCNP/NIR plus KYNA controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "In vivo calcium/fiber photometry, pellet reaching, retransection, and KYNA blockade", "injury_model": "C4-C6 dorsal hemisection with functional and necessity validation", "injury_severity": "Cervical dorsal hemisection", "intervention_type": "Glu-UCNP plus NIR guided CST-to-interneuron rewiring; retransection and KYNA challenged circuit dependence", "methods_summary": "Glu-UCNP plus NIR raised pellet-reaching success to about 48% by 70 days versus below 20% in other SCI groups; retransection reduced performance, and KYNA reduced caudal calcium activity, supporting functional glutamatergic reconnection rather than axon presence alone.", "observation_tracker_ids": ["M5B-O068"], "sex": "Not stated", "source_experiment_tracker_id": "M5A-P021-E002", "source_paper_tracker_id": "M5A-P021", "species": "Mouse", "strain": "C57BL/6J mice with cortical VChR1 and spinal interneuron readouts", "tracker_key": "M5A-P021::M5A-P021-E002", "vertebral_level": "C4-C6"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P021'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P021::M5A-P021-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'PubMed abstract verified',
    'Tracker experiment M5A-P022-E001',
    'Extracted details: Primary intervention or mechanism experiment for Netrin-1 Therapy Restores Partial Hindlimb Movement in a Rat Model of High-Severity Chronic Spinal Cord Injury.; first-pass row captures corticospinal tract regeneration / sprouting in human / translational context at abstract/source-title level. Extraction status: YES (abstract-level)',
    '{"chronicity_dpi_wpi": "UNKNOWN", "control_type": "Injury / vehicle / wild-type / comparator as reported", "experiment_extracted": "YES (abstract-level)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "UNKNOWN", "intervention_type": "Corticospinal tract regeneration / sprouting", "methods_summary": "Primary intervention or mechanism experiment for Netrin-1 Therapy Restores Partial Hindlimb Movement in a Rat Model of High-Severity Chronic Spinal Cord Injury.; first-pass row captures corticospinal tract regeneration / sprouting in human / translational context at abstract/source-title level.", "observation_tracker_ids": ["M5B-O022"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M5A-P022-E001", "source_paper_tracker_id": "M5A-P022", "species": "Human / translational context", "strain": "UNKNOWN", "tracker_key": "M5A-P022::M5A-P022-E001", "vertebral_level": "UNKNOWN"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P022'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P022::M5A-P022-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M5A-P022-E002',
    'Extracted details: Outcome/mechanistic validation row for Netrin-1 Therapy Restores Partial Hindlimb Movement in a Rat Model of High-Severity Chronic Spinal Cord Injury.; first-pass row captures corticospinal tract regeneration / sprouting in human / translational context at abstract/source-title level. Extraction status: YES (abstract-level)',
    '{"chronicity_dpi_wpi": "UNKNOWN", "control_type": "Comparator/control arm as reported", "experiment_extracted": "YES (abstract-level)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "UNKNOWN", "intervention_type": "Mechanistic outcome assessment after corticospinal tract regeneration / sprouting", "methods_summary": "Outcome/mechanistic validation row for Netrin-1 Therapy Restores Partial Hindlimb Movement in a Rat Model of High-Severity Chronic Spinal Cord Injury.; first-pass row captures corticospinal tract regeneration / sprouting in human / translational context at abstract/source-title level.", "observation_tracker_ids": ["M5B-O069"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M5A-P022-E002", "source_paper_tracker_id": "M5A-P022", "species": "Human / translational context", "strain": "UNKNOWN", "tracker_key": "M5A-P022::M5A-P022-E002", "vertebral_level": "UNKNOWN"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P022'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P022::M5A-P022-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'A-layer full text; Full text PMC',
    'Tracker experiment M5A-P023-E001',
    'Extracted details: Co-overexpression of Netrin-1 and DCC increased GAP43 and synaptophysin-associated axon growth, reduced apoptosis, lowered NgR1-RhoA-ROCK pathway signals, and improved BBB motor recovery during subacute and chronic follow-up. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Immediate treatment through 63 dpi", "control_type": "Sham, SCI, and lentiviral negative-control groups", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Full transection after T9-T11 exposure", "injury_model": "Complete T10 spinal transection", "injury_severity": "Complete transection", "intervention_type": "Local Netrin-1 and DCC overexpression lentiviruses injected around the transection site immediately after injury", "methods_summary": "Co-overexpression of Netrin-1 and DCC increased GAP43 and synaptophysin-associated axon growth, reduced apoptosis, lowered NgR1-RhoA-ROCK pathway signals, and improved BBB motor recovery during subacute and chronic follow-up.", "observation_tracker_ids": ["M5B-O023"], "sex": "Sex not stated", "source_experiment_tracker_id": "M5A-P023-E001", "source_paper_tracker_id": "M5A-P023", "species": "Rat SCI model", "strain": "Adult Sprague-Dawley; 200-250 g", "tracker_key": "M5A-P023::M5A-P023-E001", "vertebral_level": "T10"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P023'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P023::M5A-P023-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'A-layer full text; Full text PMC',
    'Tracker experiment M5A-P023-E002',
    'Extracted details: Netrin-1 or DCC knockdown reduced GAP43/SYP-associated regeneration and worsened BBB recovery, while combined overexpression produced the strongest axon-growth and synaptic-marker response. The study supports association with NgR1-RhoA-ROCK inhibition but does not directly establish receptor-pathway necessity. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "1-63 dpi; molecular readouts at 1, 7, 14, and 28 dpi", "control_type": "Netrin-1 or DCC scramble controls; single-gene and dual-gene knockdown groups", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Full transection; local lentiviral injection at upper and lower lesion margins", "injury_model": "Complete T10 spinal transection", "injury_severity": "Complete transection", "intervention_type": "Netrin-1 or DCC overexpression, low-expression lentiviruses, and combined gain/loss conditions", "methods_summary": "Netrin-1 or DCC knockdown reduced GAP43/SYP-associated regeneration and worsened BBB recovery, while combined overexpression produced the strongest axon-growth and synaptic-marker response. The study supports association with NgR1-RhoA-ROCK inhibition but does not directly establish receptor-pathway necessity.", "observation_tracker_ids": ["M5B-O070"], "sex": "Sex not stated", "source_experiment_tracker_id": "M5A-P023-E002", "source_paper_tracker_id": "M5A-P023", "species": "Rat SCI model with gain- and loss-of-function validation", "strain": "Adult Sprague-Dawley; 200-250 g", "tracker_key": "M5A-P023::M5A-P023-E002", "vertebral_level": "T10"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P023'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P023::M5A-P023-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'A-layer full text; Full text PMC',
    'Tracker experiment M5A-P024-E001',
    'Extracted details: CSPGs induced a pro-inflammatory microglial state by suppressing CYP450 metabolic activity; this state drove reactive-astrocyte transition toward scar-forming astrocytes and reinforced a CSPG-rich feedback loop. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Chronic scar maturation mechanism", "control_type": "CSPG exposure, reactive-astrocyte and microglial assays, and dFLPP-ChABC versus control formulations", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "SCI as reported", "intervention_type": "CSPG-driven microglia-astrocyte mechanism", "methods_summary": "CSPGs induced a pro-inflammatory microglial state by suppressing CYP450 metabolic activity; this state drove reactive-astrocyte transition toward scar-forming astrocytes and reinforced a CSPG-rich feedback loop.", "observation_tracker_ids": ["M5B-O024"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M5A-P024-E001", "source_paper_tracker_id": "M5A-P024", "species": "Rat SCI model plus reactive astrocytes/microglia", "strain": "UNKNOWN", "tracker_key": "M5A-P024::M5A-P024-E001", "vertebral_level": "UNKNOWN"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P024'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P024::M5A-P024-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'A-layer full text; Full text PMC',
    'Tracker experiment M5A-P024-E002',
    'Extracted details: Reactive-astrocyte-targeted ROS-responsive dFLPP delivered ChABC to degrade CSPGs, reprogrammed microglial phenotype/metabolism, reduced scar-forming astrocytes and fibrotic matrix, and improved neuronal regeneration, locomotor and autonomic recovery. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Lesion-border, ROS-responsive treatment and recovery follow-up", "control_type": "Vehicle/untreated, dFLPP, and dFLPP-ChABC controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "SCI as reported", "intervention_type": "dFLPP-ChABC targeted CSPG degradation", "methods_summary": "Reactive-astrocyte-targeted ROS-responsive dFLPP delivered ChABC to degrade CSPGs, reprogrammed microglial phenotype/metabolism, reduced scar-forming astrocytes and fibrotic matrix, and improved neuronal regeneration, locomotor and autonomic recovery.", "observation_tracker_ids": ["M5B-O071"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M5A-P024-E002", "source_paper_tracker_id": "M5A-P024", "species": "Rat SCI model", "strain": "UNKNOWN", "tracker_key": "M5A-P024::M5A-P024-E002", "vertebral_level": "UNKNOWN"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P024'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P024::M5A-P024-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'A-layer full text; Full text PMC',
    'Tracker experiment M5A-P025-E001',
    'Extracted details: The combination degraded CSPGs at lesion borders, allowed Schwann cells to migrate into host cord, increased serotonergic and dopaminergic axonal regrowth, improved BBB, grid-walk, gait, and bladder outcomes, and outperformed either monotherapy. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Treatment at 7 dpi; acute endpoint 2 months", "control_type": "Vehicle, Schwann-cell-only, and lenti-ChABC-only controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "NYU impactor; 10 g rod, 2.5 mm diameter, 12.5 mm drop after T9-T10 laminectomy", "injury_model": "T10 moderate contusion SCI", "injury_severity": "Moderate contusion", "intervention_type": "6 x 10^5 GFP+ Schwann cells injected at lesion epicenter plus lenti-ChABC 2 x 10^7 TU/uL at 1.5 mm rostral and caudal to lesion", "methods_summary": "The combination degraded CSPGs at lesion borders, allowed Schwann cells to migrate into host cord, increased serotonergic and dopaminergic axonal regrowth, improved BBB, grid-walk, gait, and bladder outcomes, and outperformed either monotherapy.", "observation_tracker_ids": ["M5B-O025"], "sex": "Female", "source_experiment_tracker_id": "M5A-P025-E001", "source_paper_tracker_id": "M5A-P025", "species": "Rat SCI transplantation model", "strain": "Sprague-Dawley; female; 7-8 weeks", "tracker_key": "M5A-P025::M5A-P025-E001", "vertebral_level": "T10"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P025'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P025::M5A-P025-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'A-layer full text; Full text PMC',
    'Tracker experiment M5A-P025-E002',
    'Extracted details: Delayed combination treatment produced persistent Schwann-cell survival and axonal regrowth through 6 months, supporting repair in chronic SCI. The chronic cohort was small and had mortality, so the long-term finding is supportive rather than definitive. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Treatment at 3 months post-SCI; endpoint 6 months post-SCI", "control_type": "Delayed untreated or single-treatment context; acute treatment groups for comparison", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "NYU impactor; 10 g rod, 2.5 mm diameter, 12.5 mm drop", "injury_model": "Chronic T10 contusion SCI", "injury_severity": "Moderate chronic contusion", "intervention_type": "Schwann cells plus lenti-ChABC delivered at 3 months, with cyclosporin A immunosuppression", "methods_summary": "Delayed combination treatment produced persistent Schwann-cell survival and axonal regrowth through 6 months, supporting repair in chronic SCI. The chronic cohort was small and had mortality, so the long-term finding is supportive rather than definitive.", "observation_tracker_ids": ["M5B-O072"], "sex": "Female", "source_experiment_tracker_id": "M5A-P025-E002", "source_paper_tracker_id": "M5A-P025", "species": "Rat chronic SCI transplantation model", "strain": "Sprague-Dawley; female; 7-8 weeks", "tracker_key": "M5A-P025::M5A-P025-E002", "vertebral_level": "T10"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P025'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P025::M5A-P025-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / saturated A tracker',
    'Tracker experiment M5A-P026-E001',
    'Extracted details: Primary intervention or mechanism experiment for Schwann Cell-Derived Exosomes Induced Axon Growth after Spinal Cord Injury by Decreasing PTP- Activation on CSPGs via the Rho/ROCK Pathway.; first-pass row captures extrinsic inhibitory matrix / guidance pathway in mouse sci model at abstract/source-title level. Extraction status: YES (abstract-level)',
    '{"chronicity_dpi_wpi": "UNKNOWN", "control_type": "Injury / vehicle / wild-type / comparator as reported", "experiment_extracted": "YES (abstract-level)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "UNKNOWN", "intervention_type": "Extrinsic inhibitory matrix / guidance pathway", "methods_summary": "Primary intervention or mechanism experiment for Schwann Cell-Derived Exosomes Induced Axon Growth after Spinal Cord Injury by Decreasing PTP- Activation on CSPGs via the Rho/ROCK Pathway.; first-pass row captures extrinsic inhibitory matrix / guidance pathway in mouse sci model at abstract/source-title level.", "observation_tracker_ids": ["M5B-O026"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M5A-P026-E001", "source_paper_tracker_id": "M5A-P026", "species": "Mouse SCI model", "strain": "UNKNOWN", "tracker_key": "M5A-P026::M5A-P026-E001", "vertebral_level": "UNKNOWN"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P026'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P026::M5A-P026-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M5A-P026-E002',
    'Extracted details: Outcome/mechanistic validation row for Schwann Cell-Derived Exosomes Induced Axon Growth after Spinal Cord Injury by Decreasing PTP- Activation on CSPGs via the Rho/ROCK Pathway.; first-pass row captures extrinsic inhibitory matrix / guidance pathway in mouse sci model at abstract/source-title level. Extraction status: YES (abstract-level)',
    '{"chronicity_dpi_wpi": "UNKNOWN", "control_type": "Comparator/control arm as reported", "experiment_extracted": "YES (abstract-level)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "UNKNOWN", "intervention_type": "Mechanistic outcome assessment after extrinsic inhibitory matrix / guidance pathway", "methods_summary": "Outcome/mechanistic validation row for Schwann Cell-Derived Exosomes Induced Axon Growth after Spinal Cord Injury by Decreasing PTP- Activation on CSPGs via the Rho/ROCK Pathway.; first-pass row captures extrinsic inhibitory matrix / guidance pathway in mouse sci model at abstract/source-title level.", "observation_tracker_ids": ["M5B-O073"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M5A-P026-E002", "source_paper_tracker_id": "M5A-P026", "species": "Mouse SCI model", "strain": "UNKNOWN", "tracker_key": "M5A-P026::M5A-P026-E002", "vertebral_level": "UNKNOWN"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P026'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P026::M5A-P026-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'A-layer full text; Full text PMC',
    'Tracker experiment M5A-P027-E001',
    'Extracted details: Full-text record is a clinical biomarker/intervention study, not an animal regeneration experiment. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Six-month phase 2b NISCI follow-up", "control_type": "Placebo-controlled NG101 trial; NCT03935321", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Clinical injury", "injury_model": "Acute cervical SCI", "injury_severity": "Acute cervical SCI", "intervention_type": "Clinical participants receiving the Nogo-A-neutralizing antibody NG101 were assessed with lesion volume, tissue bridges, cross-sectional cord area, and tract-specific myelin-sensitive MTsat MRI biomarkers.", "methods_summary": "Full-text record is a clinical biomarker/intervention study, not an animal regeneration experiment.", "observation_tracker_ids": ["M5B-O027"], "sex": "Sex as reported", "source_experiment_tracker_id": "M5A-P027-E001", "source_paper_tracker_id": "M5A-P027", "species": "Human clinical SCI cohort", "strain": "Acute cervical SCI participants; n=106", "tracker_key": "M5A-P027::M5A-P027-E001", "vertebral_level": "Cervical"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P027'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P027::M5A-P027-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'A-layer full text; Full text PMC',
    'Tracker experiment M5A-P027-E002',
    'Extracted details: Full-text evidence supports structural preservation or sprouting interpretation, while the clinical functional endpoint remains stratification-sensitive. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Six months after treatment; MRI plus electrophysiology", "control_type": "NG101 versus placebo; electrophysiologic stratification", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Clinical injury", "injury_model": "Acute cervical SCI", "injury_severity": "Acute cervical SCI", "intervention_type": "Compared with placebo, NG101 was associated with faster lesion-volume reduction and slower decline of cord area and MTsat in corticospinal tracts and dorsal columns; combined MRI/electrophysiology improved treatment-effect stratification and reduced projected trial sample size.", "methods_summary": "Full-text evidence supports structural preservation or sprouting interpretation, while the clinical functional endpoint remains stratification-sensitive.", "observation_tracker_ids": ["M5B-O074"], "sex": "Sex as reported", "source_experiment_tracker_id": "M5A-P027-E002", "source_paper_tracker_id": "M5A-P027", "species": "Human clinical SCI cohort", "strain": "Acute cervical SCI participants; n=106", "tracker_key": "M5A-P027::M5A-P027-E002", "vertebral_level": "Cervical"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P027'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P027::M5A-P027-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'A-layer full text; Full text PMC',
    'Tracker experiment M5A-P028-E001',
    'Extracted details: The XMC-ChABC plus oNPC combination increased graft survival and migration, oligodendrocyte differentiation, graft-derived myelination of spared axons, preserved synaptic boutons, and BBB/CatWalk functional recovery in chronic SCI. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Treatment at 6-7 weeks post-SCI; endpoint 19 weeks", "control_type": "aCSF, XMC, and no-cell or no-ChABC factorial controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "23 g clip compression after Th7-Th9 laminectomy", "injury_model": "Th7 chronic clip-contusion SCI", "injury_severity": "Moderate chronic contusion", "intervention_type": "Single intrathecal XMC-ChABC injection at 6 weeks followed 1 week later by 4 x 10^5 human directly reprogrammed oligodendrogenic NPCs injected into the cord parenchyma", "methods_summary": "The XMC-ChABC plus oNPC combination increased graft survival and migration, oligodendrocyte differentiation, graft-derived myelination of spared axons, preserved synaptic boutons, and BBB/CatWalk functional recovery in chronic SCI.", "observation_tracker_ids": ["M5B-O028"], "sex": "Female", "source_experiment_tracker_id": "M5A-P028-E001", "source_paper_tracker_id": "M5A-P028", "species": "Chronic rat SCI xenograft model", "strain": "Athymic Rowett nude RNU rats; female", "tracker_key": "M5A-P028::M5A-P028-E001", "vertebral_level": "Th7"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P028'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P028::M5A-P028-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'A-layer full text; Full text PMC',
    'Tracker experiment M5A-P028-E002',
    'Extracted details: XMC-ChABC degraded CS56/C4S CSPGs, reduced the astrocytic bias induced by SCI homogenate, increased oligodendrocyte-lineage markers, and promoted STEM121-positive graft-derived myelin with functional nodes of Ranvier. The combination did not significantly preserve total tissue area, so the repair claim is strongest for remyelination, synaptic preservation, and behavior. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "1 week in vitro; 7-19 weeks post-SCI in vivo", "control_type": "Naive homogenate, XMC, aCSF, and no-ChABC controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "In vitro CSPG-coated culture; 23 g clip in vivo", "injury_model": "SCI homogenate differentiation assay plus chronic Th7 clip-contusion", "injury_severity": "CSPG-mediated differentiation bias; chronic contusion in vivo", "intervention_type": "XMC-ChABC affinity-release hydrogel; oNPC transplantation as above", "methods_summary": "XMC-ChABC degraded CS56/C4S CSPGs, reduced the astrocytic bias induced by SCI homogenate, increased oligodendrocyte-lineage markers, and promoted STEM121-positive graft-derived myelin with functional nodes of Ranvier. The combination did not significantly preserve total tissue area, so the repair claim is strongest for remyelination, synaptic preservation, and behavior.", "observation_tracker_ids": ["M5B-O075"], "sex": "Not applicable in vitro; female in vivo", "source_experiment_tracker_id": "M5A-P028-E002", "source_paper_tracker_id": "M5A-P028", "species": "Human oNPC in vitro and chronic rat SCI mechanism validation", "strain": "Human directly reprogrammed oNPCs; RNU rats for in vivo validation", "tracker_key": "M5A-P028::M5A-P028-E002", "vertebral_level": "Th7 in vivo"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P028'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P028::M5A-P028-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'A-layer full text; Full text PMC',
    'Tracker experiment M5A-P029-E001',
    'Extracted details: Full-text evidence supports TREM2 for debris handling but not automatically for remyelination or long-term repair. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "TREM2 peaks at 7 dpi; short- versus long-term activation tested", "control_type": "Sham/vehicle, TREM2 knockout, and scrambled-peptide controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Crush injury as reported", "injury_model": "T10 spinal cord crush injury", "injury_severity": "Crush injury as reported", "intervention_type": "TREM2 was concentrated in Iba1+ macrophages/microglia; deletion impaired myelin-debris engulfment and degradation, increased foamy macrophage accumulation, and reduced PI3K/AKT-linked DAM activation.", "methods_summary": "Full-text evidence supports TREM2 for debris handling but not automatically for remyelination or long-term repair.", "observation_tracker_ids": ["M5B-O029"], "sex": "Female", "source_experiment_tracker_id": "M5A-P029-E001", "source_paper_tracker_id": "M5A-P029", "species": "Mouse SCI model", "strain": "UNKNOWN", "tracker_key": "M5A-P029::M5A-P029-E001", "vertebral_level": "T10"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P029'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P029::M5A-P029-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'A-layer full text; Full text PMC',
    'Tracker experiment M5A-P029-E002',
    'Extracted details: Full-text result defines a timing-dependent clearance-versus-fibrosis tradeoff. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "COG1410 at 5 min post-injury daily to 56 dpi or only to 3 dpi", "control_type": "Vehicle and scrambled-peptide controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Crush injury as reported", "injury_model": "T10 spinal cord crush injury", "injury_severity": "Crush injury as reported", "intervention_type": "Sustained COG1410 activation worsened fibrosis, chronic inflammation, axon regeneration, neuronal survival, and late locomotion despite early benefit; short-term activation produced transient early locomotor improvement without structural neuroprotection.", "methods_summary": "Full-text result defines a timing-dependent clearance-versus-fibrosis tradeoff.", "observation_tracker_ids": ["M5B-O076"], "sex": "Female", "source_experiment_tracker_id": "M5A-P029-E002", "source_paper_tracker_id": "M5A-P029", "species": "Mouse SCI model", "strain": "UNKNOWN", "tracker_key": "M5A-P029::M5A-P029-E002", "vertebral_level": "T10"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P029'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P029::M5A-P029-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'A-layer full text; Full text PMC',
    'Tracker experiment M5A-P030-E001',
    'Extracted details: Full-text record corrects the first-pass human placeholder and adds multi-omics/spatial evidence. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Spatial and temporal follow-up after injury", "control_type": "Wild-type versus astrocyte Ccn1 depletion; tissue and cell-state controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "As reported", "injury_model": "Traumatic SCI and demyelination comparators", "injury_severity": "As reported", "intervention_type": "Lesion-remote astrocytes acquired distinct white-matter reactivity states and expressed CCN1; CCN1 loss caused aberrant microglial activation, impaired myelin/axon-debris processing, altered lipid metabolism, and reduced lipid-droplet buffering.", "methods_summary": "Full-text record corrects the first-pass human placeholder and adds multi-omics/spatial evidence.", "observation_tracker_ids": ["M5B-O030"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M5A-P030-E001", "source_paper_tracker_id": "M5A-P030", "species": "Mouse SCI model plus human tissue comparator", "strain": "Mouse model; human CNS tissue context", "tracker_key": "M5A-P030::M5A-P030-E001", "vertebral_level": "Lesion-remote white matter"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P030'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P030::M5A-P030-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'A-layer full text; Full text PMC',
    'Tracker experiment M5A-P030-E002',
    'Extracted details: Full-text result is mechanistic and mapping-heavy, with repair outcome evidence but no therapeutic dosing claim. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Recovery and white-matter repair follow-up", "control_type": "Astrocyte Ccn1 depletion and CCN1-SDC4 mechanistic controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "As reported", "injury_model": "Traumatic SCI with lesion-remote white-matter analysis", "injury_severity": "As reported", "intervention_type": "Astrocyte-derived CCN1 bound microglial SDC4 to promote lipid storage and repair-associated buffering; Ccn1 depletion blunted debris clearance and neurological recovery, establishing an astrocyte-to-microglia repair relay.", "methods_summary": "Full-text result is mechanistic and mapping-heavy, with repair outcome evidence but no therapeutic dosing claim.", "observation_tracker_ids": ["M5B-O077"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M5A-P030-E002", "source_paper_tracker_id": "M5A-P030", "species": "Mouse SCI model", "strain": "UNKNOWN", "tracker_key": "M5A-P030::M5A-P030-E002", "vertebral_level": "Lesion-remote white matter"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P030'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P030::M5A-P030-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'A-layer full text; Full text PMC; severe injury cohort',
    'Tracker experiment M5A-P031-E001',
    'Extracted details: Myrf ICKO mice had fewer spared myelin sheaths than controls but showed no worse BMS or inclined-plane recovery after severe contusion; both groups remained largely unable to step, so absence of a genotype difference does not demonstrate robust functional recovery. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "BMS and inclined-plane testing through 6 weeks, with a small longitudinal cohort to 36 weeks", "control_type": "Injured remyelination-competent Myrf-Intact littermates", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Infinite Horizon 70 kDyne impact with 1-s dwell after T9 laminectomy; tamoxifen 100 mg/kg/day for 5 days before injury", "injury_model": "T9 severe thoracic contusion", "injury_severity": "Severe contusion", "intervention_type": "Inducible Myrf deletion in OPC lineage to prevent new myelin formation", "methods_summary": "Myrf ICKO mice had fewer spared myelin sheaths than controls but showed no worse BMS or inclined-plane recovery after severe contusion; both groups remained largely unable to step, so absence of a genotype difference does not demonstrate robust functional recovery.", "observation_tracker_ids": ["M5B-O031"], "sex": "Approximately equal male/female numbers", "source_experiment_tracker_id": "M5A-P031-E001", "source_paper_tracker_id": "M5A-P031", "species": "Mouse", "strain": "Myrf-flox;PDGFRalpha-CreERT2 inducible conditional knockout and Myrf-flox littermate controls; 3 months, 18-35 g", "tracker_key": "M5A-P031::M5A-P031-E001", "vertebral_level": "T9/10"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P031'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P031::M5A-P031-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'A-layer full text; Full text PMC; moderate injury physiology and gait cohort',
    'Tracker experiment M5A-P031-E002',
    'Extracted details: Moderate-injury Myrf ICKOs conducted action potentials across the lesion at similar velocity to controls (28.2 vs 27.2 m/s), with Nav1.2/Kv1.2 co-expression uniquely extended along ICKO axons and only subtle gait differences. The data support compensatory conduction, not proof that remyelination is unnecessary in all injury severities. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "CAP and gait analyses at 6 weeks post-injury", "control_type": "Myrf-Intact remyelination-competent controls; transection abolished CAP signal", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Infinite Horizon 70 kDyne impact without dwell; terminal CAP recording rostral-to-caudal across lesion and treadmill kinematics", "injury_model": "T9/10 moderate thoracic contusion", "injury_severity": "Moderate contusion", "intervention_type": "Persistent postinjury remyelination failure through Myrf deletion", "methods_summary": "Moderate-injury Myrf ICKOs conducted action potentials across the lesion at similar velocity to controls (28.2 vs 27.2 m/s), with Nav1.2/Kv1.2 co-expression uniquely extended along ICKO axons and only subtle gait differences. The data support compensatory conduction, not proof that remyelination is unnecessary in all injury severities.", "observation_tracker_ids": ["M5B-O078"], "sex": "Approximately equal male/female numbers", "source_experiment_tracker_id": "M5A-P031-E002", "source_paper_tracker_id": "M5A-P031", "species": "Mouse", "strain": "Myrf ICKO and Myrf-Intact littermates; approximately equal male/female numbers", "tracker_key": "M5A-P031::M5A-P031-E002", "vertebral_level": "T9/10"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P031'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P031::M5A-P031-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'A-layer full text; Full text PMC',
    'Tracker experiment M5A-P032-E001',
    'Extracted details: pMM-PCL adsorbed myelin debris, reduced foam-cell accumulation and inflammatory markers, reduced collagen and GFAP scar signals, increased MAP2, TUBB3, and NF200-associated neuronal/axon markers, and improved gait and BBB scores by 42 dpi. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "0-6 weeks post-injury", "control_type": "Sham, SCI, PCL, and macrophage-membrane-only controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Allen percussion after T10 exposure", "injury_model": "T10 contusion SCI", "injury_severity": "Moderate contusion", "intervention_type": "Polycaprolactone nanofiber scaffold coated with spinal-cord-homogenate-pretreated macrophage membrane, 10 x 5 mm, placed over the opened dura", "methods_summary": "pMM-PCL adsorbed myelin debris, reduced foam-cell accumulation and inflammatory markers, reduced collagen and GFAP scar signals, increased MAP2, TUBB3, and NF200-associated neuronal/axon markers, and improved gait and BBB scores by 42 dpi.", "observation_tracker_ids": ["M5B-O032"], "sex": "Female", "source_experiment_tracker_id": "M5A-P032-E001", "source_paper_tracker_id": "M5A-P032", "species": "Rat SCI model", "strain": "Sprague-Dawley; female; 8 weeks; about 250 g", "tracker_key": "M5A-P032::M5A-P032-E001", "vertebral_level": "T10"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P032'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P032::M5A-P032-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'A-layer full text; Full text PMC',
    'Tracker experiment M5A-P032-E002',
    'Extracted details: pMM-PCL reduced Oil Red O-positive foam-cell formation, attracted macrophages toward adsorbed debris, increased Arg1 while reducing iNOS in the repair microenvironment, and relieved myelin-debris-mediated inhibition of PC12 migration. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "24-48 h in vitro; 6 weeks in vivo", "control_type": "PCL, pMM, plain-slide, and untreated controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Allen percussion in vivo; spinal-cord homogenate or isolated myelin debris in vitro", "injury_model": "T10 contusion SCI and homogenate/myelin-debris assays", "injury_severity": "Moderate contusion; lipid-debris challenge in vitro", "intervention_type": "Pretreated macrophage membrane adsorption on PCL; pMM-PCL co-culture with myelin debris, macrophages, and PC12 cells", "methods_summary": "pMM-PCL reduced Oil Red O-positive foam-cell formation, attracted macrophages toward adsorbed debris, increased Arg1 while reducing iNOS in the repair microenvironment, and relieved myelin-debris-mediated inhibition of PC12 migration.", "observation_tracker_ids": ["M5B-O079"], "sex": "Female in vivo; not applicable in vitro", "source_experiment_tracker_id": "M5A-P032-E002", "source_paper_tracker_id": "M5A-P032", "species": "Rat SCI model plus macrophage and neuronal in vitro models", "strain": "Female Sprague-Dawley rats for SCI tissue; RAW264.7 and PC12 cells", "tracker_key": "M5A-P032::M5A-P032-E002", "vertebral_level": "T10 in vivo"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P032'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P032::M5A-P032-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'A-layer full text; Full text PMC',
    'Tracker experiment M5A-P033-E001',
    'Extracted details: Full-text methods define a dual-function material rather than a single serotonergic drug. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Lesion-site hydrogel administration with longitudinal behavioral follow-up", "control_type": "Blank hydrogel, non-targeted nucleic-acid, and vehicle comparators as reported", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Hemisection as reported", "injury_model": "Spinal cord hemisection model", "injury_severity": "As reported", "intervention_type": "SeroPTEN-CG is a DNA/RNA heteroduplex hydrogel built from a 5-HTP-derived targeting/neuromodulatory motif and PTEN siRNA; DNase-mediated disassembly releases nanogels for serotonergic targeting and PTEN silencing.", "methods_summary": "Full-text methods define a dual-function material rather than a single serotonergic drug.", "observation_tracker_ids": ["M5B-O033"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M5A-P033-E001", "source_paper_tracker_id": "M5A-P033", "species": "Mouse SCI model plus primary neurons", "strain": "UNKNOWN", "tracker_key": "M5A-P033::M5A-P033-E001", "vertebral_level": "Lesion site as reported"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P033'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P033::M5A-P033-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'A-layer full text; Full text PMC',
    'Tracker experiment M5A-P033-E002',
    'Extracted details: Full-text result supports coordinated excitability plus structural reconstruction; the two actions are not independently isolated in the final in vivo formulation. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Behavioral, sensory, electrophysiological, tracing, histological and molecular follow-up", "control_type": "Vehicle/material controls as reported", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Hemisection as reported", "injury_model": "Spinal cord hemisection model", "injury_severity": "As reported", "intervention_type": "Lesion-site SeroPTEN-CG restored neuronal excitability, silenced PTEN, promoted axonal elongation and ECM remodeling, reactivated spared spinal circuits, and improved sensory and locomotor outcomes with reported biosafety assessment.", "methods_summary": "Full-text result supports coordinated excitability plus structural reconstruction; the two actions are not independently isolated in the final in vivo formulation.", "observation_tracker_ids": ["M5B-O080"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M5A-P033-E002", "source_paper_tracker_id": "M5A-P033", "species": "Mouse SCI model", "strain": "UNKNOWN", "tracker_key": "M5A-P033::M5A-P033-E002", "vertebral_level": "Lesion site as reported"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P033'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P033::M5A-P033-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'A-layer full text; Full text PMC; serotonin depletion and behavior',
    'Tracker experiment M5A-P034-E001',
    'Extracted details: TPH2 KO rats had near-undetectable spinal serotonin/5-HIAA and significantly greater tapered-beam and ladder deficits at weeks 3-4, with slower recovery of hindlimb tone and voluntary movement than WT despite comparable lesion size. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Tapered-beam, ladder, static-rod, tone and voluntary-movement testing for 4 weeks", "control_type": "Wild-type littermates; preinjury WT and KO behavior was comparable", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Microscalpel lateral hemisection after T8 laminectomy", "injury_model": "T8 left lateral hemisection", "injury_severity": "Lateral hemisection", "intervention_type": "Constitutive TPH2 loss causing central serotonin deficiency", "methods_summary": "TPH2 KO rats had near-undetectable spinal serotonin/5-HIAA and significantly greater tapered-beam and ladder deficits at weeks 3-4, with slower recovery of hindlimb tone and voluntary movement than WT despite comparable lesion size.", "observation_tracker_ids": ["M5B-O034"], "sex": "Female", "source_experiment_tracker_id": "M5A-P034-E001", "source_paper_tracker_id": "M5A-P034", "species": "Rat", "strain": "Female Dark Agouti TPH2-knockout and wild-type rats, 13-16 months; n=6 per SCI group", "tracker_key": "M5A-P034::M5A-P034-E001", "vertebral_level": "T8"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P034'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P034::M5A-P034-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'A-layer full text; Full text PMC; electrophysiological validation',
    'Tracker experiment M5A-P034-E002',
    'Extracted details: TPH2 KO animals showed lower submaximal/maximal CMAP amplitudes on the ipsilateral hindlimb and altered recruitment curves, consistent with slower sensorimotor pathway recovery. The paper does not directly quantify serotonergic axon sprouting or establish a receptor-specific mechanism. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Terminal compound-muscle-action-potential testing at 4 weeks; HPLC regional serotonin assay in independent cohort", "control_type": "WT controls and contralateral muscles", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Sciatic-nerve or L5-L6 spinal stimulation with gastrocnemius and tibialis CMAP recording at 4 weeks", "injury_model": "T8 left lateral hemisection with neuromuscular pathway assessment", "injury_severity": "Lateral hemisection", "intervention_type": "Central serotonin deficiency via TPH2 knockout", "methods_summary": "TPH2 KO animals showed lower submaximal/maximal CMAP amplitudes on the ipsilateral hindlimb and altered recruitment curves, consistent with slower sensorimotor pathway recovery. The paper does not directly quantify serotonergic axon sprouting or establish a receptor-specific mechanism.", "observation_tracker_ids": ["M5B-O081"], "sex": "Female", "source_experiment_tracker_id": "M5A-P034-E002", "source_paper_tracker_id": "M5A-P034", "species": "Rat", "strain": "Female TPH2 KO and WT rats; n=4 per group for terminal CMAP assays", "tracker_key": "M5A-P034::M5A-P034-E002", "vertebral_level": "T8"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P034'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P034::M5A-P034-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / saturated A tracker',
    'Tracker experiment M5A-P035-E001',
    'Extracted details: Primary intervention or mechanism experiment for Neuronal HDAC3 knockdown promotes propriospinal detour pathway formation and locomotor recovery in a mouse model of spinal cord injury.; first-pass row captures serotonergic/propriospinal relay plasticity in human / translational context at abstract/source-title level. Extraction status: YES (abstract-level)',
    '{"chronicity_dpi_wpi": "UNKNOWN", "control_type": "Injury / vehicle / wild-type / comparator as reported", "experiment_extracted": "YES (abstract-level)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "UNKNOWN", "intervention_type": "Serotonergic/propriospinal relay plasticity", "methods_summary": "Primary intervention or mechanism experiment for Neuronal HDAC3 knockdown promotes propriospinal detour pathway formation and locomotor recovery in a mouse model of spinal cord injury.; first-pass row captures serotonergic/propriospinal relay plasticity in human / translational context at abstract/source-title level.", "observation_tracker_ids": ["M5B-O035"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M5A-P035-E001", "source_paper_tracker_id": "M5A-P035", "species": "Human / translational context", "strain": "UNKNOWN", "tracker_key": "M5A-P035::M5A-P035-E001", "vertebral_level": "UNKNOWN"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P035'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P035::M5A-P035-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M5A-P035-E002',
    'Extracted details: Outcome/mechanistic validation row for Neuronal HDAC3 knockdown promotes propriospinal detour pathway formation and locomotor recovery in a mouse model of spinal cord injury.; first-pass row captures serotonergic/propriospinal relay plasticity in human / translational context at abstract/source-title level. Extraction status: YES (abstract-level)',
    '{"chronicity_dpi_wpi": "UNKNOWN", "control_type": "Comparator/control arm as reported", "experiment_extracted": "YES (abstract-level)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "UNKNOWN", "intervention_type": "Mechanistic outcome assessment after serotonergic/propriospinal relay plasticity", "methods_summary": "Outcome/mechanistic validation row for Neuronal HDAC3 knockdown promotes propriospinal detour pathway formation and locomotor recovery in a mouse model of spinal cord injury.; first-pass row captures serotonergic/propriospinal relay plasticity in human / translational context at abstract/source-title level.", "observation_tracker_ids": ["M5B-O082"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M5A-P035-E002", "source_paper_tracker_id": "M5A-P035", "species": "Human / translational context", "strain": "UNKNOWN", "tracker_key": "M5A-P035::M5A-P035-E002", "vertebral_level": "UNKNOWN"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P035'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P035::M5A-P035-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'A-layer full text; Fig. 1-2; OPN/IGF1 regeneration plus NSC bridge formation',
    'Tracker experiment M5A-P036-E001',
    'Extracted details: OPN/IGF1 alone did not regenerate axons through the complete crush and NSCs alone did not integrate with host pathways. Combined treatment filled the cavity, reduced the glial scar, enabled host axons to enter the graft, produced SYN/PSD95-associated contacts and approximately 30% NeuN-positive graft-neuron differentiation with axons extending caudally. Structural synapse markers were partly immature or nonsynaptic, so this row supports anatomical bridge formation but not functional transmission by itself. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "AAV-OPN/IGF1 2 weeks before injury; NSC transplantation 1 week after injury; endpoint 9 weeks post-injury", "control_type": "No-treatment/control; OPN/IGF1 alone; NSC transplantation alone", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Crush; device not stated in captured full text", "injury_model": "Complete T10 spinal cord crush", "injury_severity": "Complete", "intervention_type": "AAV2/9-OPN plus AAV2/9-IGF1 in T8 neurons and 1 million E14 spinal NSCs transplanted into the lesion cavity", "methods_summary": "OPN/IGF1 alone did not regenerate axons through the complete crush and NSCs alone did not integrate with host pathways. Combined treatment filled the cavity, reduced the glial scar, enabled host axons to enter the graft, produced SYN/PSD95-associated contacts and approximately 30% NeuN-positive graft-neuron differentiation with axons extending caudally. Structural synapse markers were partly immature or nonsynaptic, so this row supports anatomical bridge formation but not functional transmission by itself.", "observation_tracker_ids": ["M5B-O036"], "sex": "Female", "source_experiment_tracker_id": "M5A-P036-E001", "source_paper_tracker_id": "M5A-P036", "species": "Rat", "strain": "Adult female Sprague Dawley, including GFP-expressing rats", "tracker_key": "M5A-P036::M5A-P036-E001", "vertebral_level": "T10"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P036'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P036::M5A-P036-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'A-layer full text; Fig. 3; CLP290 dose-response, behavior, and electrophysiology',
    'Tracker experiment M5A-P036-E002',
    'Extracted details: Adding CLP290 to OPN/IGF1 plus NSCs increased BBB scores to approximately 6 versus approximately 2-3 with the bridge regimen alone, improved hindlimb joint oscillation, and produced weak but consistent rostral-to-caudal evoked responses across the graft. A 1.75 mg/kg dose was ineffective; 17.5 and 175 mg/kg improved behavior without added benefit at the higher dose. CLP290 did not change bridge anatomy or host T8 c-Fos pattern, indicating functional enabling rather than increased axon regeneration. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "CLP290 started 2 weeks after NSC transplantation; 8-week treatment/behavioral course; endpoint 9 weeks post-injury", "control_type": "OPN/IGF1 alone; OPN/IGF1 plus NSCs; vehicle; CLP290 dose controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Crush; device not stated in captured full text", "injury_model": "Complete T10 spinal cord crush", "injury_severity": "Complete", "intervention_type": "Systemic KCC2 agonist CLP290 daily, selected dose 17.5 mg/kg, with OPN/IGF1 plus NSC transplantation", "methods_summary": "Adding CLP290 to OPN/IGF1 plus NSCs increased BBB scores to approximately 6 versus approximately 2-3 with the bridge regimen alone, improved hindlimb joint oscillation, and produced weak but consistent rostral-to-caudal evoked responses across the graft. A 1.75 mg/kg dose was ineffective; 17.5 and 175 mg/kg improved behavior without added benefit at the higher dose. CLP290 did not change bridge anatomy or host T8 c-Fos pattern, indicating functional enabling rather than increased axon regeneration.", "observation_tracker_ids": ["M5B-O083"], "sex": "Female", "source_experiment_tracker_id": "M5A-P036-E002", "source_paper_tracker_id": "M5A-P036", "species": "Rat", "strain": "Adult female Sprague Dawley", "tracker_key": "M5A-P036::M5A-P036-E002", "vertebral_level": "T10"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P036'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P036::M5A-P036-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'A-layer full text; Full text PMC',
    'Tracker experiment M5A-P037-E001',
    'Extracted details: QZIF-polymersomes accumulated at the lesion, reduced lesion volume and TNF-alpha/IL-1beta, increased neuronal density, improved BBB scores from 14 dpi, and shortened MEP latency while increasing MEP amplitude. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Immediate treatment through 28 dpi", "control_type": "Sham and untreated SCI controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Infinite Horizon impactor; 200 kdyn, 2.0 mm tip", "injury_model": "T9 moderate contusion SCI", "injury_severity": "Moderate contusion", "intervention_type": "ROS-responsive QZIF-polymersomes containing quercetin, 30 mg/kg intraperitoneally once daily for 7 d from immediately after injury", "methods_summary": "QZIF-polymersomes accumulated at the lesion, reduced lesion volume and TNF-alpha/IL-1beta, increased neuronal density, improved BBB scores from 14 dpi, and shortened MEP latency while increasing MEP amplitude.", "observation_tracker_ids": ["M5B-O037"], "sex": "Male and female", "source_experiment_tracker_id": "M5A-P037-E001", "source_paper_tracker_id": "M5A-P037", "species": "Rat SCI model", "strain": "Sprague-Dawley; 6-8 weeks; 180-220 g", "tracker_key": "M5A-P037::M5A-P037-E001", "vertebral_level": "T9"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P037'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P037::M5A-P037-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'A-layer full text; Full text PMC',
    'Tracker experiment M5A-P037-E002',
    'Extracted details: Quercetin enhanced KCC2 activation in electrophysiology, while QZIF-polymersomes restored KCC2, mitochondrial respiration, glucose metabolism, COXI/UCP2/TFAM, and neurite length under inflammatory stress. Delayed treatment increased NF200+ axons and both oligodendrocyte- and Schwann-cell-associated remyelinated fibers; KCC2 necessity was not directly tested by loss of function. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "24-48 h in vitro; day 14 treatment and 28 dpi remyelination endpoint in vivo", "control_type": "Vehicle, quercetin, QZIF, untreated SCI, and sham controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Infinite Horizon impactor; transwell neuronal-microglial model in vitro", "injury_model": "T9 contusion SCI and LPS/IFN-gamma inflammatory co-culture", "injury_severity": "Moderate contusion; inflammatory stress in vitro", "intervention_type": "Quercetin 100 uM, QZIF, or QZIF-polymersomes in vitro; QZIF-polymersomes 30 mg/kg from day 14 for remyelination cohort", "methods_summary": "Quercetin enhanced KCC2 activation in electrophysiology, while QZIF-polymersomes restored KCC2, mitochondrial respiration, glucose metabolism, COXI/UCP2/TFAM, and neurite length under inflammatory stress. Delayed treatment increased NF200+ axons and both oligodendrocyte- and Schwann-cell-associated remyelinated fibers; KCC2 necessity was not directly tested by loss of function.", "observation_tracker_ids": ["M5B-O084"], "sex": "Male and female in vivo; not applicable in vitro", "source_experiment_tracker_id": "M5A-P037-E002", "source_paper_tracker_id": "M5A-P037", "species": "Rat SCI model plus primary neuron and microglia validation", "strain": "Sprague-Dawley rats; P0-P1 cortical neurons and microglia for in vitro assays", "tracker_key": "M5A-P037::M5A-P037-E002", "vertebral_level": "T9 in vivo"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P037'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P037::M5A-P037-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'A-layer full text; Full text PMC; Fig. 1-3',
    'Tracker experiment M5A-P038-E001',
    'Extracted details: Double-KO mice, but not either single KO, showed significantly improved BMS recovery from week 4 through week 8, with greater white-matter preservation and increased 5-HT-positive fibers rostral and caudal to the lesion. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "BMS follow-up to 8 weeks; molecular and cellular assays at 7 dpi and chronic endpoint", "control_type": "WT, single-KO, sham, and unrelated sulfotransferase-KO controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Infinite Horizon 100 kDyne contusion after T10 laminectomy; sham laminectomy controls", "injury_model": "T10 contusive SCI", "injury_severity": "Contusion", "intervention_type": "Combined GlcNAc6ST1/Chst2 and GlcNAc6ST4/Chst7 deficiency", "methods_summary": "Double-KO mice, but not either single KO, showed significantly improved BMS recovery from week 4 through week 8, with greater white-matter preservation and increased 5-HT-positive fibers rostral and caudal to the lesion.", "observation_tracker_ids": ["M5B-O038"], "sex": "Male and female", "source_experiment_tracker_id": "M5A-P038-E001", "source_paper_tracker_id": "M5A-P038", "species": "Mouse", "strain": "C57BL/6J background GlcNAc6ST1-KO, GlcNAc6ST4-KO, double-KO, and WT mice; 3.5-6 months", "tracker_key": "M5A-P038::M5A-P038-E001", "vertebral_level": "T10"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P038'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P038::M5A-P038-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'A-layer full text; Full text PMC; Fig. 4-6',
    'Tracker experiment M5A-P038-E002',
    'Extracted details: Double deficiency reduced recruited monocytes, CD68+ activated macrophage/microglia, fibronectin and collagen/ECM gene programs, while increasing synaptic-membrane transcripts and eliminating GlcNAc-6-sulfated N-glycans. Increased serotonergic fibers correlated with recovery, but their causal contribution was not directly tested. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Immune and molecular readouts at 7 dpi; histology and locomotor outcome through 8 weeks", "control_type": "WT and single-KO controls; GlcNAc6ST3, KSGal6ST, and C6ST1 KO comparisons", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "CD11b+ cell isolation, histology, RNA-seq at 7 dpi, and GALAXY glycomics", "injury_model": "T10 contusive SCI with inflammation and matrix mechanism assays", "injury_severity": "Contusion", "intervention_type": "Loss of GlcNAc6ST1/4-dependent glycan sulfation", "methods_summary": "Double deficiency reduced recruited monocytes, CD68+ activated macrophage/microglia, fibronectin and collagen/ECM gene programs, while increasing synaptic-membrane transcripts and eliminating GlcNAc-6-sulfated N-glycans. Increased serotonergic fibers correlated with recovery, but their causal contribution was not directly tested.", "observation_tracker_ids": ["M5B-O085"], "sex": "Male and female", "source_experiment_tracker_id": "M5A-P038-E002", "source_paper_tracker_id": "M5A-P038", "species": "Mouse", "strain": "GlcNAc6ST1/4 double-KO and WT mice; myeloid-cell, transcriptomic, and glycomic validation cohorts", "tracker_key": "M5A-P038::M5A-P038-E002", "vertebral_level": "T10"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P038'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P038::M5A-P038-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / saturated A tracker',
    'Tracker experiment M5A-P039-E001',
    'Extracted details: Primary intervention or mechanism experiment for Treadmill exercise supplemented by OPN promote axon regeneration through the IGF-1R/Akt/mTOR signaling pathway.; first-pass row captures corticospinal tract regeneration / sprouting in human / translational context at abstract/source-title level. Extraction status: YES (abstract-level)',
    '{"chronicity_dpi_wpi": "UNKNOWN", "control_type": "Injury / vehicle / wild-type / comparator as reported", "experiment_extracted": "YES (abstract-level)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "UNKNOWN", "intervention_type": "Corticospinal tract regeneration / sprouting", "methods_summary": "Primary intervention or mechanism experiment for Treadmill exercise supplemented by OPN promote axon regeneration through the IGF-1R/Akt/mTOR signaling pathway.; first-pass row captures corticospinal tract regeneration / sprouting in human / translational context at abstract/source-title level.", "observation_tracker_ids": ["M5B-O039"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M5A-P039-E001", "source_paper_tracker_id": "M5A-P039", "species": "Human / translational context", "strain": "UNKNOWN", "tracker_key": "M5A-P039::M5A-P039-E001", "vertebral_level": "UNKNOWN"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P039'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P039::M5A-P039-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M5A-P039-E002',
    'Extracted details: Outcome/mechanistic validation row for Treadmill exercise supplemented by OPN promote axon regeneration through the IGF-1R/Akt/mTOR signaling pathway.; first-pass row captures corticospinal tract regeneration / sprouting in human / translational context at abstract/source-title level. Extraction status: YES (abstract-level)',
    '{"chronicity_dpi_wpi": "UNKNOWN", "control_type": "Comparator/control arm as reported", "experiment_extracted": "YES (abstract-level)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "UNKNOWN", "intervention_type": "Mechanistic outcome assessment after corticospinal tract regeneration / sprouting", "methods_summary": "Outcome/mechanistic validation row for Treadmill exercise supplemented by OPN promote axon regeneration through the IGF-1R/Akt/mTOR signaling pathway.; first-pass row captures corticospinal tract regeneration / sprouting in human / translational context at abstract/source-title level.", "observation_tracker_ids": ["M5B-O086"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M5A-P039-E002", "source_paper_tracker_id": "M5A-P039", "species": "Human / translational context", "strain": "UNKNOWN", "tracker_key": "M5A-P039::M5A-P039-E002", "vertebral_level": "UNKNOWN"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P039'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P039::M5A-P039-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'A-layer full text; Full text PMC',
    'Tracker experiment M5A-P040-E001',
    'Extracted details: OPN plus treadmill training produced the strongest functional improvement, amplified cortical mTOR signaling and IGF-1 receptor expression, attenuated CST dieback, and enabled limited CST axon regeneration up to 2 mm caudal to the lesion. Exercise or OPN alone did not produce the same lesion-crossing CST result. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "1-9 weeks post-injury; treadmill for 8 weeks", "control_type": "Sham, SCI, exercise-only, and OPN-only controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Cervical crush injury as reported", "injury_model": "Incomplete C5 crush SCI", "injury_severity": "Incomplete crush", "intervention_type": "AAV9-SPP1-GFP injected into right sensorimotor cortex 2 weeks before injury; treadmill at 50% maximum speed 5 times weekly for 30 min from 1 week post-injury", "methods_summary": "OPN plus treadmill training produced the strongest functional improvement, amplified cortical mTOR signaling and IGF-1 receptor expression, attenuated CST dieback, and enabled limited CST axon regeneration up to 2 mm caudal to the lesion. Exercise or OPN alone did not produce the same lesion-crossing CST result.", "observation_tracker_ids": ["M5B-O040"], "sex": "Female", "source_experiment_tracker_id": "M5A-P040-E001", "source_paper_tracker_id": "M5A-P040", "species": "Mouse cervical SCI model", "strain": "C57BL/6", "tracker_key": "M5A-P040::M5A-P040-E001", "vertebral_level": "C5"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P040'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P040::M5A-P040-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'A-layer full text; Full text PMC',
    'Tracker experiment M5A-P040-E002',
    'Extracted details: Combined OPN and exercise increased p-S6 and GAP43, reduced forelimb ladder errors, and increased BDA-labeled CST fibers caudal to the lesion. The study notes that the functional benefit may also involve sprouting and activity-dependent plasticity, not only the limited lesion-crossing axons. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "1-9 weeks post-injury", "control_type": "Sham, control virus, exercise-only, and OPN-only controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Cervical crush; BDA anterograde CST tracing", "injury_model": "Incomplete C5 crush SCI", "injury_severity": "Incomplete crush", "intervention_type": "AAV9-SPP1-GFP or AAV-GFP; BDA tracing at 7 weeks; treadmill at 50% maximum speed", "methods_summary": "Combined OPN and exercise increased p-S6 and GAP43, reduced forelimb ladder errors, and increased BDA-labeled CST fibers caudal to the lesion. The study notes that the functional benefit may also involve sprouting and activity-dependent plasticity, not only the limited lesion-crossing axons.", "observation_tracker_ids": ["M5B-O087"], "sex": "Female", "source_experiment_tracker_id": "M5A-P040-E002", "source_paper_tracker_id": "M5A-P040", "species": "Mouse cervical SCI model with cortical signaling and tract tracing", "strain": "C57BL/6", "tracker_key": "M5A-P040::M5A-P040-E002", "vertebral_level": "C5"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P040'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P040::M5A-P040-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'A-layer full text; Full text PMC',
    'Tracker experiment M5A-P041-E001',
    'Extracted details: DPSC-OIC grafts improved BMS recovery, MRI appearance, and bladder function; reduced cleaved caspase-3, increased Ki-67 and Nestin/Sox2-associated progenitor signals, reduced NG2, and increased fibronectin. Transplanted cells remained detectable for about 2 weeks. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Immediate post-injury graft through 27 dpi; cell survival assessed to 15 d", "control_type": "PBS, DPSC-Null, and DPSC-GFP-Luc controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "2 mm impactor tip, 10 g weight, 20 mm drop", "injury_model": "T9-T10 moderate contusion SCI", "injury_severity": "Moderate contusion", "intervention_type": "Human DPSCs infected with adenovirus encoding OPN, IGF-1, and CNTF, 1 x 10^5 cells per site at four in situ sites", "methods_summary": "DPSC-OIC grafts improved BMS recovery, MRI appearance, and bladder function; reduced cleaved caspase-3, increased Ki-67 and Nestin/Sox2-associated progenitor signals, reduced NG2, and increased fibronectin. Transplanted cells remained detectable for about 2 weeks.", "observation_tracker_ids": ["M5B-O041"], "sex": "Sex not stated", "source_experiment_tracker_id": "M5A-P041-E001", "source_paper_tracker_id": "M5A-P041", "species": "Mouse SCI model with human dental pulp stem-cell grafts", "strain": "Human DPSCs; mouse SCI model; sex not stated in extracted methods", "tracker_key": "M5A-P041::M5A-P041-E001", "vertebral_level": "T9-T10"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P041'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P041::M5A-P041-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'A-layer full text; Full text PMC',
    'Tracker experiment M5A-P041-E002',
    'Extracted details: DPSC-OIC supernatant increased HT-22 proliferation, Tubb3/Syn1 and neurite length and reduced H2O2-associated apoptosis. In vivo, the OIC payload improved neural-support markers and spinal structure, but the study did not directly quantify long-distance axon regeneration. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "24-48 h in vitro; 14-27 dpi behavioral and tissue outcomes", "control_type": "Medium, DPSC-Null, PBS, and unmodified-graft controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "400 uM H2O2 for 15 min in vitro; 2 mm, 10 g, 20 mm drop in vivo", "injury_model": "H2O2 neuronal-stress assay plus T9-T10 contusion SCI", "injury_severity": "Oxidative-stress assay; moderate contusion in vivo", "intervention_type": "DPSC-OIC supernatant in vitro; DPSC-OIC grafts in vivo", "methods_summary": "DPSC-OIC supernatant increased HT-22 proliferation, Tubb3/Syn1 and neurite length and reduced H2O2-associated apoptosis. In vivo, the OIC payload improved neural-support markers and spinal structure, but the study did not directly quantify long-distance axon regeneration.", "observation_tracker_ids": ["M5B-O088"], "sex": "Not applicable in vitro; sex not stated in vivo", "source_experiment_tracker_id": "M5A-P041-E002", "source_paper_tracker_id": "M5A-P041", "species": "HT-22 neuronal culture plus mouse SCI validation", "strain": "HT-22 cells; human DPSCs; mouse SCI model", "tracker_key": "M5A-P041::M5A-P041-E002", "vertebral_level": "T9-T10"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P041'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P041::M5A-P041-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'A-layer full text; Full text PMC; Fig. 4-6',
    'Tracker experiment M5A-P042-E001',
    'Extracted details: GM-RA4IV reduced cavity area, reactive astrocytes and myeloid markers while increasing axon, 5-HT, and NF200 density. The combined siRNA@LNP plus GM-3Dpro group produced the best BBB, stride, body-support and EMG outcomes, consistent with combined PTEN knockdown and physical guidance. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "BBB, Vicon kinematics, and EMG to 8 weeks; AAV2/9-mCherry labeling at 6 weeks", "control_type": "Ctrl, GM-PEGDA, GM-RA4IV, siRNA@LNPs plus GM-RA4IV, and intact controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Lesion cavity filled with GM-PEGDA or GM-RA4IV hydrogel; separate 3D-printed scaffold and siRNA@LNP groups", "injury_model": "3-mm T10 hemisection SCI", "injury_severity": "Hemisection", "intervention_type": "GM-RA4IV bioactive hydrogel, parallel-channel GM-3Dpro scaffold, and local PTEN-siRNA lipid nanoparticles", "methods_summary": "GM-RA4IV reduced cavity area, reactive astrocytes and myeloid markers while increasing axon, 5-HT, and NF200 density. The combined siRNA@LNP plus GM-3Dpro group produced the best BBB, stride, body-support and EMG outcomes, consistent with combined PTEN knockdown and physical guidance.", "observation_tracker_ids": ["M5B-O042"], "sex": "Not stated", "source_experiment_tracker_id": "M5A-P042-E001", "source_paper_tracker_id": "M5A-P042", "species": "Rat", "strain": "Rat SCI model; sex and strain not stated in extracted methods", "tracker_key": "M5A-P042::M5A-P042-E001", "vertebral_level": "T10"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P042'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P042::M5A-P042-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'A-layer full text; Full text PMC; Fig. 7-8 and retransection',
    'Tracker experiment M5A-P042-E002',
    'Extracted details: Combined treatment aligned regenerated axons at about 9.7 degrees versus about 37-40 degrees in non-channeled comparators, increased MBP/synaptophysin-associated fibers, and enriched Ephrin/Eph guidance programs. Retransection abolished the functional gain within 1 week, supporting graft-dependent circuit transmission; direct synaptic function was not fully established. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Histology and single-cell RNA-seq at 8 weeks; retransection assessed functional dependence", "control_type": "Hydrogel and siRNA/scaffold comparator groups; intact controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "GM-3Dpro contained 20 parallel 200-micrometer channels in a 3-mm scaffold; PTEN-siRNA delivered by LNP; second transection at graft site at 8 weeks", "injury_model": "T10 hemisection with axon-orientation and circuit validation", "injury_severity": "Hemisection with graft retranssection validation", "intervention_type": "PTEN knockdown plus GM-RA4IV-filled parallel-channel scaffold", "methods_summary": "Combined treatment aligned regenerated axons at about 9.7 degrees versus about 37-40 degrees in non-channeled comparators, increased MBP/synaptophysin-associated fibers, and enriched Ephrin/Eph guidance programs. Retransection abolished the functional gain within 1 week, supporting graft-dependent circuit transmission; direct synaptic function was not fully established.", "observation_tracker_ids": ["M5B-O089"], "sex": "Not stated", "source_experiment_tracker_id": "M5A-P042-E002", "source_paper_tracker_id": "M5A-P042", "species": "Rat", "strain": "Same rat hemisection cohorts; single-cell and kinematic subsets", "tracker_key": "M5A-P042::M5A-P042-E002", "vertebral_level": "T10"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P042'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P042::M5A-P042-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'A-layer full text; Full text PMC',
    'Tracker experiment M5A-P043-E001',
    'Extracted details: Full-text evidence is in vitro/ex vivo platform validation, not an in vivo SCI treatment experiment. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Nanoparticle transfection and 3D scaffold culture to 21 days", "control_type": "Non-targeting siRNA, siGLO, blank scaffold, and nanoparticle-free scaffold controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "N/A", "injury_model": "In vitro primary-injury and ex vivo tissue models", "injury_severity": "N/A", "intervention_type": "GET peptide-siRNA nanoparticles delivered PTEN siRNA into primary neurons and were incorporated into an aligned hyaluronic-acid scaffold containing collagen IV and fibronectin; delivery was assessed in monolayer, 3D culture, and chick brain explants.", "methods_summary": "Full-text evidence is in vitro/ex vivo platform validation, not an in vivo SCI treatment experiment.", "observation_tracker_ids": ["M5B-O043"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M5A-P043-E001", "source_paper_tracker_id": "M5A-P043", "species": "Primary cortical neurons plus chick brain explant", "strain": "In vitro neuronal cultures; chick E12 tissue", "tracker_key": "M5A-P043::M5A-P043-E001", "vertebral_level": "N/A"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P043'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P043::M5A-P043-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'A-layer full text; Full text PMC',
    'Tracker experiment M5A-P043-E002',
    'Extracted details: Full-text result supports delivery and growth competence; it does not establish axon regeneration or functional recovery in an injured animal. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Long-term scaffold culture and neurite-outgrowth assays", "control_type": "Blank scaffold, non-targeting siRNA, and nanoparticle-free controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "N/A", "injury_model": "In vitro neuronal injury model and ex vivo brain tissue", "injury_severity": "N/A", "intervention_type": "PTEN-siRNA scaffolds sustained PTEN suppression, increased BCL2 and GAP43, preserved neuronal/glial biocompatibility, enhanced neurite outgrowth after in vitro injury, and delivered siRNA to neurons in chick explants.", "methods_summary": "Full-text result supports delivery and growth competence; it does not establish axon regeneration or functional recovery in an injured animal.", "observation_tracker_ids": ["M5B-O090"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M5A-P043-E002", "source_paper_tracker_id": "M5A-P043", "species": "Primary cortical neurons plus chick brain explant", "strain": "Primary neuronal mixed cultures; chick E12 tissue", "tracker_key": "M5A-P043::M5A-P043-E002", "vertebral_level": "N/A"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P043'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P043::M5A-P043-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'A-layer full text; Full text PMC',
    'Tracker experiment M5A-P044-E001',
    'Extracted details: Full-text methods correct the first-pass rat placeholder and show that the core mechanistic work is in mouse DRG/SCI systems. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Cited2 gain/loss and regenerative versus non-regenerative neuronal-state comparisons", "control_type": "GFP/empty-vector, Cited2 overexpression/knockdown, and injury controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "As reported", "injury_model": "Experimental SCI and peripheral nerve injury comparator", "injury_severity": "As reported", "intervention_type": "Cited2 was active in immature and regenerating DRG neurons but silent after non-regenerative SCI; neuronal Cited2 overexpression reinstated developmental growth-associated transcriptional and epigenetic signatures, with RNA-seq, ATAC-seq and CUT&Tag support.", "methods_summary": "Full-text methods correct the first-pass rat placeholder and show that the core mechanistic work is in mouse DRG/SCI systems.", "observation_tracker_ids": ["M5B-O044"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M5A-P044-E001", "source_paper_tracker_id": "M5A-P044", "species": "Mouse SCI model plus cultured DRG neurons", "strain": "Mouse; DRG/F11 neuronal cultures", "tracker_key": "M5A-P044::M5A-P044-E001", "vertebral_level": "As reported"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P044'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P044::M5A-P044-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'A-layer full text; Full text PMC',
    'Tracker experiment M5A-P044-E002',
    'Extracted details: Full-text result supports a druggable Cited2 mechanism but leaves long-term structural-stability and broad-HDAC safety questions open. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Panobinostat treatment with axonal and functional follow-up", "control_type": "Vehicle, GFP, and Cited2 knockdown controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "As reported", "injury_model": "Experimental SCI", "injury_severity": "As reported", "intervention_type": "Pharmacogenomic screening identified Panobinostat as a Cited2-linked HDAC inhibitor; it promoted sensory axon growth, 5-HT sprouting and neurological recovery after SCI, while Cited2 knockdown abrogated the in vitro growth benefit.", "methods_summary": "Full-text result supports a druggable Cited2 mechanism but leaves long-term structural-stability and broad-HDAC safety questions open.", "observation_tracker_ids": ["M5B-O091"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M5A-P044-E002", "source_paper_tracker_id": "M5A-P044", "species": "Mouse SCI model", "strain": "Mouse; sex as reported", "tracker_key": "M5A-P044::M5A-P044-E002", "vertebral_level": "As reported"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P044'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P044::M5A-P044-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'A-layer full text; Full text PMC; Fig. 1-2',
    'Tracker experiment M5A-P045-E001',
    'Extracted details: PLO-coated scaffolds supported host-cell migration and vascularization, increased BBB and swim-score recovery over time, and outperformed no-scaffold and generally uncoated-scaffold groups. The study supports bridge-associated repair, not complete restoration of locomotion. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "BBB weekly and KSAT every 2 weeks through 11 weeks; tissue at 12 weeks", "control_type": "No scaffold and uncoated asparagus scaffold controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Full cord transection; 4-mm diameter, approximately 2.9-mm long decellularized Asparagus officinalis scaffold implanted acutely", "injury_model": "T8-T9 complete spinal transection with tissue gap", "injury_severity": "Complete transection", "intervention_type": "Poly-L-ornithine-coated lignocellulosic plant scaffold, 100 microgram/ml coating", "methods_summary": "PLO-coated scaffolds supported host-cell migration and vascularization, increased BBB and swim-score recovery over time, and outperformed no-scaffold and generally uncoated-scaffold groups. The study supports bridge-associated repair, not complete restoration of locomotion.", "observation_tracker_ids": ["M5B-O045"], "sex": "Female", "source_experiment_tracker_id": "M5A-P045-E001", "source_paper_tracker_id": "M5A-P045", "species": "Rat", "strain": "Juvenile female Sprague-Dawley rats, 250-300 g at surgery", "tracker_key": "M5A-P045::M5A-P045-E001", "vertebral_level": "T8-T9"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P045'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P045::M5A-P045-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'A-layer full text; Full text PMC; tract-tracing and histology',
    'Tracker experiment M5A-P045-E002',
    'Extracted details: PLO-coated implants showed more rostral CTb-labeled sensory fibers, CST fibers extending along the scaffold, greater neural-cell infiltration and myelin-associated LFB signal. Fiber labeling within the scaffold indicates sprouting/extension, not proof of functional long-distance synaptic reconnection. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Tracing at 11 weeks with 2-week transport period; endpoint 12 weeks", "control_type": "No scaffold and uncoated scaffold controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "CTb injected into sciatic nerves for ascending sensory tracing; dextran amine injected into motor cortex for CST tracing; LFB and NF200/beta-III-tubulin histology", "injury_model": "T8-T9 complete transection with scaffold bridge", "injury_severity": "Complete transection", "intervention_type": "PLO-coated plant scaffold", "methods_summary": "PLO-coated implants showed more rostral CTb-labeled sensory fibers, CST fibers extending along the scaffold, greater neural-cell infiltration and myelin-associated LFB signal. Fiber labeling within the scaffold indicates sprouting/extension, not proof of functional long-distance synaptic reconnection.", "observation_tracker_ids": ["M5B-O092"], "sex": "Female", "source_experiment_tracker_id": "M5A-P045-E002", "source_paper_tracker_id": "M5A-P045", "species": "Rat", "strain": "Same female Sprague-Dawley transection cohort", "tracker_key": "M5A-P045::M5A-P045-E002", "vertebral_level": "T8-T9"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P045'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P045::M5A-P045-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'A-layer full text; Fig. 1-6; scRNA-seq, spatial transcriptomics, and spatial metabolomics atlas',
    'Tracker experiment M5A-P046-E001',
    'Extracted details: Across 35,799 cells, the atlas identified Mic2 microglia, Mac4 macrophages, and Fib4 fibroblasts as repair-associated subsets. Mic2 localized mainly to dorsal white matter and was enriched for wound-healing markers and taurine; Mac4 formed clusters associated with copalic acid; Fib4 localized around the injured cord, expressed Igf2, and was associated with uridine and Upp1/Nt5e/Uck1 metabolism. The study is spatially and molecularly informative but primarily descriptive: no Mic2, taurine, Mac4, copalic acid, Fib4, or uridine perturbation proves necessity, and scRNA-seq lacked neuronal information. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Injury-versus-sham tissue profiling; exact post-injury sampling day not stated in captured full text", "control_type": "Sham laminectomy; SCI", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Quick-release 50 g clip for 10 seconds", "injury_model": "T1 compression SCI and sham laminectomy", "injury_severity": "Not otherwise graded", "intervention_type": "10X scRNA-seq, Visium spatial transcriptomics, and mass-spectrometry-imaging spatial metabolomics on separate biological samples", "methods_summary": "Across 35,799 cells, the atlas identified Mic2 microglia, Mac4 macrophages, and Fib4 fibroblasts as repair-associated subsets. Mic2 localized mainly to dorsal white matter and was enriched for wound-healing markers and taurine; Mac4 formed clusters associated with copalic acid; Fib4 localized around the injured cord, expressed Igf2, and was associated with uridine and Upp1/Nt5e/Uck1 metabolism. The study is spatially and molecularly informative but primarily descriptive: no Mic2, taurine, Mac4, copalic acid, Fib4, or uridine perturbation proves necessity, and scRNA-seq lacked neuronal information.", "observation_tracker_ids": ["M5B-O046"], "sex": "Male", "source_experiment_tracker_id": "M5A-P046-E001", "source_paper_tracker_id": "M5A-P046", "species": "Rat", "strain": "8-week-old male Sprague-Dawley, 200-250 g", "tracker_key": "M5A-P046::M5A-P046-E001", "vertebral_level": "T1"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P046'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P046::M5A-P046-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'A-layer full text; Fig. 5 and Supplementary Fig. S8; copalic-acid inflammatory cell assay',
    'Tracker experiment M5A-P046-E002',
    'Extracted details: In BV2 and RAW264.7 cultures, 6-hour copalic-acid treatment reduced LPS-associated pro-inflammatory CD86, CD80, and IL-1beta expression by qPCR. This supports anti-inflammatory activity in resident-like and monocyte-derived macrophage cultures, but it does not establish that the spatially enriched Mac4 subset is the direct cellular source or that copalic acid is required for SCI recovery. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "6 hours LPS/CA exposure", "control_type": "Untreated or LPS-only comparator", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Not applicable", "injury_model": "LPS-induced inflammatory culture", "injury_severity": "Not applicable", "intervention_type": "LPS 1 microgram/ml with copalic acid 3 micromolar", "methods_summary": "In BV2 and RAW264.7 cultures, 6-hour copalic-acid treatment reduced LPS-associated pro-inflammatory CD86, CD80, and IL-1beta expression by qPCR. This supports anti-inflammatory activity in resident-like and monocyte-derived macrophage cultures, but it does not establish that the spatially enriched Mac4 subset is the direct cellular source or that copalic acid is required for SCI recovery.", "observation_tracker_ids": ["M5B-O093"], "sex": "Not applicable", "source_experiment_tracker_id": "M5A-P046-E002", "source_paper_tracker_id": "M5A-P046", "species": "Mouse cell lines", "strain": "BV2 microglia and RAW264.7 macrophages", "tracker_key": "M5A-P046::M5A-P046-E002", "vertebral_level": "Not applicable"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P046'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P046::M5A-P046-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'A-layer full text; Full text PMC; prospective longitudinal trial',
    'Tracker experiment M5A-P047-E001',
    'Extracted details: Mean TSCIS rose from 2.2 to 3.2 and OFS from 1.5 to 3.1 during follow-up, with no neurological deterioration or major safety signal. The longitudinal design reduces spontaneous-recovery concern but cannot isolate treatment effects. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Six-month follow-up after stabilization screening; monthly gait scores", "control_type": "Within-subject stabilized screening baseline; no placebo group", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Intraspinal injections targeted to preserved tissue near lesion; poly laminin 1 microgram/kg plus either GDNF or ChABC one week apart; physiotherapy continued", "injury_model": "Chronic thoracolumbar SCI, stable after at least 4-5 months screening physiotherapy", "injury_severity": "Chronic naturally occurring SCI", "intervention_type": "Poly laminin with GDNF in three dogs or ChABC in three dogs", "methods_summary": "Mean TSCIS rose from 2.2 to 3.2 and OFS from 1.5 to 3.1 during follow-up, with no neurological deterioration or major safety signal. The longitudinal design reduces spontaneous-recovery concern but cannot isolate treatment effects.", "observation_tracker_ids": ["M5B-O047"], "sex": "Three male and three female", "source_experiment_tracker_id": "M5A-P047-E001", "source_paper_tracker_id": "M5A-P047", "species": "Dog", "strain": "Six non-ambulatory dogs with severe chronic T3-L3 SCI; 2 traumatic and 4 disc-degeneration cases; mixed breeds, 3-9 years", "tracker_key": "M5A-P047::M5A-P047-E001", "vertebral_level": "T3-L3"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P047'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P047::M5A-P047-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'A-layer full text; Full text PMC; safety and limitation assessment',
    'Tracker experiment M5A-P047-E002',
    'Extracted details: Treatment was associated with gradual gait improvement and appeared safe, but no blinding, no placebo group, small heterogeneous sample, and no single-agent arms prevent attribution to poly laminin versus GDNF, ChABC, injection, or continued rehabilitation. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Safety sampled before injections and days 2, 7, 9, and 14; gait through 6 months", "control_type": "Poly laminin plus GDNF versus poly laminin plus ChABC; no untreated or vehicle arm", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Neurological examinations, blood tests, monthly TSCIS/OFS, and continued physiotherapy", "injury_model": "Chronic T3-L3 SCI with heterogeneous lesion causes and prior surgery", "injury_severity": "Chronic naturally occurring SCI", "intervention_type": "Combination treatment as above", "methods_summary": "Treatment was associated with gradual gait improvement and appeared safe, but no blinding, no placebo group, small heterogeneous sample, and no single-agent arms prevent attribution to poly laminin versus GDNF, ChABC, injection, or continued rehabilitation.", "observation_tracker_ids": ["M5B-O094"], "sex": "Three male and three female", "source_experiment_tracker_id": "M5A-P047-E002", "source_paper_tracker_id": "M5A-P047", "species": "Dog", "strain": "Same six chronic SCI participants", "tracker_key": "M5A-P047::M5A-P047-E002", "vertebral_level": "T3-L3"}'
  FROM _m5_paper_map p
  JOIN _m5_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M5A-P047'
  RETURNING experiment_id
)
INSERT INTO _m5_experiment_map (tracker_id, experiment_id) SELECT 'M5A-P047::M5A-P047-E002', experiment_id FROM inserted;

INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Axon/white-matter repair intervention or mechanism', 'Module 5B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;

INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Activity or stimulation-enabled axon repair', 'Module 5B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Axon regeneration through chronic scar/graft', 'Module 5B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Axonal regeneration / cellular energetics', 'Module 5B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Extrinsic inhibitory matrix / guidance pathway', 'Module 5B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Graft/scaffold-enabled axon repair', 'Module 5B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for A Myelin Debris Cleaner for Spinal Cord Injury Recovery: Polycaprolactone / Cell Membrane Assembled Scaffolds.; first-pass row captures remyelination / white matter repair in rat sci model at abstract/source-title level.', 'Module 5B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for A laminin-based therapy for dogs with chronic spinal cord injury: promising results of a longitudinal trial.; first-pass row captures extrinsic inhibitory matrix / guidance pathway in dog chronic sci at abstract/source-title level.', 'Module 5B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Activated alpha 9 integrin expression enables sensory pathway reconstruction after spinal cord injury.; first-pass row captures extrinsic inhibitory matrix / guidance pathway in rat sci model at abstract/source-title level.', 'Module 5B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Activation of MAP2K signaling by genetic engineering or HF-rTMS promotes corticospinal axon sprouting and functional regeneration; first-pass row captures cst sprouting/regeneration in rodent model context at abstract/source-title level.', 'Module 5B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Anti-Nogo-A NG101 treatment induces changes in spinal cord micro- and macrostructure following spinal cord injury.; first-pass row captures corticospinal tract regeneration / sprouting in rat sci model at abstract/source-title level.', 'Module 5B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Axon regeneration through scars and into sites of chronic spinal cord injury; first-pass row captures axon regeneration through chronic scar/graft in rat at abstract/source-title level.', 'Module 5B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for CITED2 is a druggable epigenetic switch coupling neuronal maturation to regenerative decline.; first-pass row captures intrinsic neuronal growth competence in rat sci model at abstract/source-title level.', 'Module 5B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Central Serotonin Deficiency Impairs Recovery of Sensorimotor Abilities After Spinal Cord Injury in Rats.; first-pass row captures serotonergic/propriospinal relay plasticity in rat sci model at abstract/source-title level.', 'Module 5B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Chondroitinase ABC combined with Schwann cell transplantation enhances restoration of neural connection and functional recovery following acute and chronic spinal cord injury.; first-pass row captures serotonergic/propriospinal relay plasticity in human / translational context at abstract/source-title level.', 'Module 5B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Co-overexpression of OPN, IGF-1 and CNTF augment the therapeutic effect of DPSC on spinal cord injury.; first-pass row captures graft/scaffold-enabled axon repair in mouse sci model at abstract/source-title level.', 'Module 5B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Compensatory changes after spinal cord injury in a remyelination deficient mouse model.; first-pass row captures remyelination / white matter repair in mouse sci model at abstract/source-title level.', 'Module 5B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Corticospinal tract regeneration after spinal cord injury in receptor protein tyrosine phosphatase sigma deficient mice; first-pass row captures cst regeneration / receptor ptp sigma in mouse at abstract/source-title level.', 'Module 5B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Development of a <i>PTEN</i>-siRNA activated scaffold to promote axonal regrowth following spinal cord injury.; first-pass row captures intrinsic neuronal growth competence in rat sci model at abstract/source-title level.', 'Module 5B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Disrupting CSPG-Driven Microglia-Astrocyte Crosstalk Enables Scar-Free Repair in Spinal Cord Injury.; first-pass row captures extrinsic inhibitory matrix / guidance pathway in rat sci model at abstract/source-title level.', 'Module 5B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Effects of transcranial magnetic stimulation on axonal regeneration in the corticospinal tract of female rats with spinal cord injury.; first-pass row captures activity or stimulation-enabled axon repair in rat sci model at abstract/source-title level.', 'Module 5B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Enhanced locomotor recovery in mice lacking GlcNAc6ST1 and GlcNAc6ST4 following spinal cord injury.; first-pass row captures serotonergic/propriospinal relay plasticity in mouse sci model at abstract/source-title level.', 'Module 5B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Functional recovery induced by KCC2-enabled relay pathways in completely injured spinal cords in adult rats.; first-pass row captures serotonergic/propriospinal relay plasticity in rat sci model at abstract/source-title level.', 'Module 5B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Functionalized nanozyme delivery of a KCC2-activator conjugate for the promotion of functional recovery after acute spinal cord injury.; first-pass row captures serotonergic/propriospinal relay plasticity in rat sci model at abstract/source-title level.', 'Module 5B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Gabapentinoid treatment promotes corticospinal plasticity and regeneration following murine spinal cord injury.; first-pass row captures corticospinal tract regeneration / sprouting in mouse sci model at abstract/source-title level.', 'Module 5B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Human Oligodendrogenic Neural Progenitor Cells Delivered with Chondroitinase ABC Facilitate Functional Repair of Chronic Spinal Cord Injury.; first-pass row captures remyelination / white matter repair in human / translational context at abstract/source-title level.', 'Module 5B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Injured adult neurons regress to an embryonic transcriptional growth state; first-pass row captures intrinsic neuronal growth state in mouse at abstract/source-title level.', 'Module 5B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Integrating single-cell RNA sequencing and spatial multi-omics reveals the molecular signature of regeneration after spinal cord injury.; first-pass row captures remyelination / white matter repair in rat sci model at abstract/source-title level.', 'Module 5B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Lentivirus-mediated overexpression of netrin-1/DCC co-expression promotes axonal regeneration and functional recovery in spinal cord injury via the inhibition of the NgR1-RhoA-ROCK signaling pathway.; first-pass row captures extrinsic inhibitory matrix / guidance pathway in human / translational context at abstract/source-title level.', 'Module 5B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Lesion-remote astrocytes govern microglia-mediated white matter repair.; first-pass row captures remyelination / white matter repair in human / translational context at abstract/source-title level.', 'Module 5B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Lesion-remote astrocytes govern microglia-mediated white matter repair; first-pass row captures lesion-remote white matter repair in mouse at abstract/source-title level.', 'Module 5B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Lipin1 depletion coordinates neuronal signaling pathways to promote motor and sensory axon regeneration after spinal cord injury.; first-pass row captures corticospinal tract regeneration / sprouting in rat sci model at abstract/source-title level.', 'Module 5B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Modulation of Extrinsic and Intrinsic Signaling Together with Neuronal Activation Enhances Forelimb Motor Recovery after Cervical Spinal Cord Injury.; first-pass row captures corticospinal tract regeneration / sprouting in mouse sci model at abstract/source-title level.', 'Module 5B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Motoneuron Death after Human Spinal Cord Injury; first-pass row captures ventral-root axon loss/remyelination pathology in human at abstract/source-title level.', 'Module 5B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Multichannel 3D-Printed Bioactive Scaffold Combined with Small Interfering RNA Delivery to Promote Neurological Recovery after Spinal Cord Injury.; first-pass row captures graft/scaffold-enabled axon repair in rat sci model at abstract/source-title level.', 'Module 5B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Netrin-1 Therapy Restores Partial Hindlimb Movement in a Rat Model of High-Severity Chronic Spinal Cord Injury.; first-pass row captures corticospinal tract regeneration / sprouting in human / translational context at abstract/source-title level.', 'Module 5B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Neuronal HDAC3 knockdown promotes propriospinal detour pathway formation and locomotor recovery in a mouse model of spinal cord injury.; first-pass row captures serotonergic/propriospinal relay plasticity in human / translational context at abstract/source-title level.', 'Module 5B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Osteopontin enhances the effect of treadmill training and promotes functional recovery after spinal cord injury.; first-pass row captures corticospinal tract regeneration / sprouting in mouse sci model at abstract/source-title level.', 'Module 5B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Poly-L-Ornithine coated plant scaffolds support motor recovery in rats after traumatic spinal cord injury.; first-pass row captures graft/scaffold-enabled axon repair in human / translational context at abstract/source-title level.', 'Module 5B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Precise rewiring of corticospinal axons and spinal interneurons via near-infrared optogenetics for spinal cord injury treatment.; first-pass row captures corticospinal tract regeneration / sprouting in mouse sci model at abstract/source-title level.', 'Module 5B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Reducing Pericyte-Derived Scarring Promotes Recovery after Spinal Cord Injury; first-pass row captures cst/rst regeneration after scar attenuation in mouse at abstract/source-title level.', 'Module 5B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Restoring Cellular Energetics Promotes Axonal Regeneration and Functional Recovery after Spinal Cord Injury; first-pass row captures axonal regeneration / cellular energetics in rodent model context at abstract/source-title level.', 'Module 5B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Schwann Cell-Derived Exosomes Induced Axon Growth after Spinal Cord Injury by Decreasing PTP- Activation on CSPGs via the Rho/ROCK Pathway.; first-pass row captures extrinsic inhibitory matrix / guidance pathway in mouse sci model at abstract/source-title level.', 'Module 5B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Serotonergic System-Targeted Nucleic Acid Hydrogel Coordinates Excitability Restoration and Circuit Reconstruction for Spinal Cord Injury Therapy.; first-pass row captures serotonergic/propriospinal relay plasticity in mouse sci model at abstract/source-title level.', 'Module 5B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Spinal cord reconstitution with homologous neural grafts enables robust corticospinal regeneration; first-pass row captures neural graft-enabled cst regeneration in rat at abstract/source-title level.', 'Module 5B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Stimulation of corticospinal neurons by optogenetic cAMP inductions promotes motor recovery after spinal cord injury in female rats via raphespinal tract modulation.; first-pass row captures corticospinal tract regeneration / sprouting in rat sci model at abstract/source-title level.', 'Module 5B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Synaptotagmin 4 Supports Spontaneous Axon Sprouting after Spinal Cord Injury.; first-pass row captures corticospinal tract regeneration / sprouting in experimental sci model context at abstract/source-title level.', 'Module 5B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for TREM2 Facilitates Myelin Debris Clearance but Exacerbates Chronic Inflammation and Fibrosis After Spinal Cord Injury.; first-pass row captures remyelination / white matter repair in mouse sci model at abstract/source-title level.', 'Module 5B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for TTBK2-Driven Ciliogenesis Is Required for Intrinsic Neuronal Regeneration After Spinal Cord Injury.; first-pass row captures intrinsic neuronal growth competence in mouse sci model at abstract/source-title level.', 'Module 5B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for The transcription factor combination MEF2 and KLF7 promotes axonal sprouting in the injured spinal cord with functional improvement and regeneration-associated gene expression.; first-pass row captures intrinsic neuronal growth competence in rat sci model at abstract/source-title level.', 'Module 5B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Thiorphan reprograms neurons to promote functional recovery after spinal cord injury.; first-pass row captures corticospinal tract regeneration / sprouting in human / translational context at abstract/source-title level.', 'Module 5B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Transcranial Optogenetic Stimulation Promotes Corticospinal Tract Axon Regeneration to Repair Spinal Cord Injury by Activating the JAK2/STAT3 Pathway.; first-pass row captures corticospinal tract regeneration / sprouting in mouse sci model at abstract/source-title level.', 'Module 5B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Treadmill exercise supplemented by OPN promote axon regeneration through the IGF-1R/Akt/mTOR signaling pathway.; first-pass row captures corticospinal tract regeneration / sprouting in human / translational context at abstract/source-title level.', 'Module 5B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('intrinsic growth competence', 'Module 5B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('relay plasticity / circuit reconstruction', 'Module 5B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('tract regeneration / sprouting / recovery', 'Module 5B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('white matter / remyelination / debris handling', 'Module 5B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Lu P 2007 contributes axon regeneration through chronic scar/graft evidence in rat, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'qualitative',
    NULL,
    'Lu P 2007 contributes axon regeneration through chronic scar/graft evidence in rat, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'lu p 2007 contributes axon regeneration through chronic scar/graft evidence in rat, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'Module 5A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'medium',
    '{"curator_notes": "Primary title: Axon regeneration through scars and into sites of chronic spinal cord injury. Note: Chronic scar axon-regeneration anchor.", "experiment_tracker_id": "M5A-P001-E001", "measurement_method_inference": null, "paper_tracker_id": "M5A-P001", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M5B-T006", "tracker_id": "M5B-O001"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P001::M5A-P001-E001'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'Axon regeneration through chronic scar/graft'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O001', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P002-E001 confirms the curated Cell-specific KRas deletion to attenuate type A pericyte progeny experiment in Mouse. Methods/readouts recorded in the A-layer: Reducing type A pericyte proliferation decreased PDGFRB-positive fibrotic scar cells and broad extracellular-matrix and collagen deposition; complete recombination could prevent tissue closure, defining a dose-response boundary.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Full-text source localization for M5A-P002-E001 confirms the curated Cell-specific KRas deletion to attenuate type A pericyte progeny experiment in Mouse. Methods/readouts recorded in the A-layer: Reducing type A pericyte proliferation decreased PDGFRB-positive fibrotic scar cells and broad extracellular-matrix and collagen deposition; complete recombination could prevent tissue closure, defining a dose-response boundary.',
    'full-text source localization for m5a-p002-e001 confirms the curated cell-specific kras deletion to attenuate type a pericyte progeny experiment in mouse. methods/readouts recorded in the a-layer: reducing type a pericyte proliferation decreased pdgfrb-positive fibrotic scar cells and broad extracellular-matrix and collagen deposition; complete recombination could prevent tissue closure, defining a dose-response boundary.',
    'Module 5A full-text extraction; Full text PMC; Fig. 1-2',
    'A-layer full text; Full text PMC; Fig. 1-2',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P002-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P002-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P002", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T001", "tracker_id": "M5B-O002"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P002::M5A-P002-E001'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'tract regeneration / sprouting / recovery'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O002', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P003-E001 confirms the curated Integrative mapping of lesion-remote astrocyte and white-matter degeneration-associated microglia states experiment in Mouse. Methods/readouts recorded in the A-layer: LRAs acquired region- and time-specific molecular states distinct from border-forming astrocytes. White-matter LRAs (WM3/4) co-localized with Mg2/Mg5 white-matter degeneration-associated microglia (WDM) that upregulated phagocytosis/lipid-metabolism programs, formed nodules in Wallerian-degenerating tracts, and phagocytosed myelin/axon debris. Ccn1 was selectively induced in WDM-adjacent white-matter LRAs.',
    'qualitative',
    'single-cell RNA-seq / cell-state atlas; spatial transcriptomics / spatial atlas',
    'Full-text source localization for M5A-P003-E001 confirms the curated Integrative mapping of lesion-remote astrocyte and white-matter degeneration-associated microglia states experiment in Mouse. Methods/readouts recorded in the A-layer: LRAs acquired region- and time-specific molecular states distinct from border-forming astrocytes. White-matter LRAs (WM3/4) co-localized with Mg2/Mg5 white-matter degeneration-associated microglia (WDM) that upregulated phagocytosis/lipid-metabolism programs, formed nodules in Wallerian-degenerating tracts, and phagocytosed myelin/axon debris. Ccn1 was selectively induced in WDM-adjacent white-matter LRAs.',
    'full-text source localization for m5a-p003-e001 confirms the curated integrative mapping of lesion-remote astrocyte and white-matter degeneration-associated microglia states experiment in mouse. methods/readouts recorded in the a-layer: lras acquired region- and time-specific molecular states distinct from border-forming astrocytes. white-matter lras (wm3/4) co-localized with mg2/mg5 white-matter degeneration-associated microglia (wdm) that upregulated phagocytosis/lipid-metabolism programs, formed nodules in wallerian-degenerating tracts, and phagocytosed myelin/axon debris. ccn1 was selectively induced in wdm-adjacent white-matter lras.',
    'Module 5A full-text extraction; Full text PMC; Fig. 1-2 and spatial/single-nucleus atlas',
    'A-layer full text; Full text PMC; Fig. 1-2 and spatial/single-nucleus atlas',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P003-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P003-E001", "measurement_method_inference": "single-cell RNA-seq / cell-state atlas; spatial transcriptomics / spatial atlas", "paper_tracker_id": "M5A-P003", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T003", "tracker_id": "M5B-O003"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P003::M5A-P003-E001'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'white matter / remyelination / debris handling'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O003', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P004-E001 confirms the curated Ventral-root axon and motoneuron-surrogate quantification experiment in Human. Methods/readouts recorded in the A-layer: Large-diameter myelinated axons were counted in formalin-fixed ventral roots from human SCI cases to estimate motoneuron loss and denervation.',
    'qualitative',
    'immunostaining / histology / pathology',
    'Full-text source localization for M5A-P004-E001 confirms the curated Ventral-root axon and motoneuron-surrogate quantification experiment in Human. Methods/readouts recorded in the A-layer: Large-diameter myelinated axons were counted in formalin-fixed ventral roots from human SCI cases to estimate motoneuron loss and denervation.',
    'full-text source localization for m5a-p004-e001 confirms the curated ventral-root axon and motoneuron-surrogate quantification experiment in human. methods/readouts recorded in the a-layer: large-diameter myelinated axons were counted in formalin-fixed ventral roots from human sci cases to estimate motoneuron loss and denervation.',
    'Module 5A full-text extraction; Full text PMC; ventral-root histology',
    'A-layer full text; Full text PMC; ventral-root histology',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P004-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P004-E001", "measurement_method_inference": "immunostaining / histology / pathology", "paper_tracker_id": "M5A-P004", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T003", "tracker_id": "M5B-O004"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P004::M5A-P004-E001'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'white matter / remyelination / debris handling'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O004', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P005-E001 confirms the curated Syntaphilin deletion to increase axonal mitochondrial transport experiment in Mouse. Methods/readouts recorded in the A-layer: Snph loss reduced injury-associated mitochondrial damage and axonal energy deficit, limited CST dieback, and increased CST regeneration after C5 dorsal hemisection.',
    'qualitative',
    NULL,
    'Full-text source localization for M5A-P005-E001 confirms the curated Syntaphilin deletion to increase axonal mitochondrial transport experiment in Mouse. Methods/readouts recorded in the A-layer: Snph loss reduced injury-associated mitochondrial damage and axonal energy deficit, limited CST dieback, and increased CST regeneration after C5 dorsal hemisection.',
    'full-text source localization for m5a-p005-e001 confirms the curated syntaphilin deletion to increase axonal mitochondrial transport experiment in mouse. methods/readouts recorded in the a-layer: snph loss reduced injury-associated mitochondrial damage and axonal energy deficit, limited cst dieback, and increased cst regeneration after c5 dorsal hemisection.',
    'Module 5A full-text extraction; Full text PMC; C5 dorsal hemisection',
    'A-layer full text; Full text PMC; C5 dorsal hemisection',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P005-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P005-E001", "measurement_method_inference": null, "paper_tracker_id": "M5A-P005", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T005", "tracker_id": "M5B-O005"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P005::M5A-P005-E001'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'Axonal regeneration / cellular energetics'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O005', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Fry EJ 2010 contributes cst regeneration / receptor ptp sigma evidence in mouse, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'qualitative',
    'genetic perturbation / knockdown assay; behavioral / functional recovery assay',
    'Fry EJ 2010 contributes cst regeneration / receptor ptp sigma evidence in mouse, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'fry ej 2010 contributes cst regeneration / receptor ptp sigma evidence in mouse, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'Module 5A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'medium',
    '{"curator_notes": "Primary title: Corticospinal tract regeneration after spinal cord injury in receptor protein tyrosine phosphatase sigma deficient mice. Note: CSPG-receptor pathway anchor.", "experiment_tracker_id": "M5A-P006-E001", "measurement_method_inference": "genetic perturbation / knockdown assay; behavioral / functional recovery assay", "paper_tracker_id": "M5A-P006", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M5B-T001", "tracker_id": "M5B-O006"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P006::M5A-P006-E001'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'tract regeneration / sprouting / recovery'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O006', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P007-E001 confirms the curated Caudalized embryonic spinal neural progenitor-cell graft experiment in Rat. Methods/readouts recorded in the A-layer: Grafts supported extensive BDA-labeled CST regeneration into the lesion, with about 1,650 axons at 0.5 mm inside the graft and synaptic-marker and ultrastructural evidence of graft contacts.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Full-text source localization for M5A-P007-E001 confirms the curated Caudalized embryonic spinal neural progenitor-cell graft experiment in Rat. Methods/readouts recorded in the A-layer: Grafts supported extensive BDA-labeled CST regeneration into the lesion, with about 1,650 axons at 0.5 mm inside the graft and synaptic-marker and ultrastructural evidence of graft contacts.',
    'full-text source localization for m5a-p007-e001 confirms the curated caudalized embryonic spinal neural progenitor-cell graft experiment in rat. methods/readouts recorded in the a-layer: grafts supported extensive bda-labeled cst regeneration into the lesion, with about 1,650 axons at 0.5 mm inside the graft and synaptic-marker and ultrastructural evidence of graft contacts.',
    'Module 5A full-text extraction; Full text PMC; Fig. 1',
    'A-layer full text; Full text PMC; Fig. 1',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P007-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P007-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P007", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T006", "tracker_id": "M5B-O007"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P007::M5A-P007-E001'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'tract regeneration / sprouting / recovery'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O007', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Poplawski GHD 2020 contributes intrinsic neuronal growth state evidence in mouse, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'qualitative',
    'qPCR / RT-PCR / mRNA assay',
    'Poplawski GHD 2020 contributes intrinsic neuronal growth state evidence in mouse, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'poplawski ghd 2020 contributes intrinsic neuronal growth state evidence in mouse, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'Module 5A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'medium',
    '{"curator_notes": "Primary title: Injured adult neurons regress to an embryonic transcriptional growth state. Note: Transcriptional growth-state anchor.", "experiment_tracker_id": "M5A-P008-E001", "measurement_method_inference": "qPCR / RT-PCR / mRNA assay", "paper_tracker_id": "M5A-P008", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M5B-T005", "tracker_id": "M5B-O008"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P008::M5A-P008-E001'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'intrinsic growth competence'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O008', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Boato F 2023 contributes cst sprouting/regeneration evidence in rodent model context, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Boato F 2023 contributes cst sprouting/regeneration evidence in rodent model context, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'boato f 2023 contributes cst sprouting/regeneration evidence in rodent model context, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'Module 5A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'medium',
    '{"curator_notes": "Primary title: Activation of MAP2K signaling by genetic engineering or HF-rTMS promotes corticospinal axon sprouting and functional regeneration. Note: Stimulation/signaling intervention anchor.", "experiment_tracker_id": "M5A-P009-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P009", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M5B-T001", "tracker_id": "M5B-O009"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P009::M5A-P009-E001'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'tract regeneration / sprouting / recovery'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O009', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P010-E001 confirms the curated Bilateral transcranial 473-nm LED stimulation, 10 Hz selected from in vitro screen, 40 min daily for 14 days experiment in Mouse. Methods/readouts recorded in the A-layer: Optogenetic stimulation increased BDA-labeled CST axon index at the injury site (9.75% vs 0.49%) and caudal within 2 mm (5.56% vs 0.34%), increased motor-evoked-potential amplitude and improved BMS/grid/open-field hindlimb movement after complete transection.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Full-text source localization for M5A-P010-E001 confirms the curated Bilateral transcranial 473-nm LED stimulation, 10 Hz selected from in vitro screen, 40 min daily for 14 days experiment in Mouse. Methods/readouts recorded in the A-layer: Optogenetic stimulation increased BDA-labeled CST axon index at the injury site (9.75% vs 0.49%) and caudal within 2 mm (5.56% vs 0.34%), increased motor-evoked-potential amplitude and improved BMS/grid/open-field hindlimb movement after complete transection.',
    'full-text source localization for m5a-p010-e001 confirms the curated bilateral transcranial 473-nm led stimulation, 10 hz selected from in vitro screen, 40 min daily for 14 days experiment in mouse. methods/readouts recorded in the a-layer: optogenetic stimulation increased bda-labeled cst axon index at the injury site (9.75% vs 0.49%) and caudal within 2 mm (5.56% vs 0.34%), increased motor-evoked-potential amplitude and improved bms/grid/open-field hindlimb movement after complete transection.',
    'Module 5A full-text extraction; Full text PMC; Fig. 3-4',
    'A-layer full text; Full text PMC; Fig. 3-4',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P010-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P010-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P010", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T007", "tracker_id": "M5B-O010"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P010::M5A-P010-E001'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'tract regeneration / sprouting / recovery'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O010', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P011-E001 confirms the curated AAV9-shLipin1 in cortex before injury; adult complete T8 SCI tested after neonatal or adult cortical delivery experiment in Mouse SCI and cortical neuron model. Methods/readouts recorded in the A-layer: Lipin1 knockdown promoted CST sprouting after pyramidotomy and robust CST regeneration after complete T8 SCI. Neonatal delivery before adult SCI produced axons extending up to about 3 mm caudal to the lesion, while adult delivery also increased regeneration.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Full-text source localization for M5A-P011-E001 confirms the curated AAV9-shLipin1 in cortex before injury; adult complete T8 SCI tested after neonatal or adult cortical delivery experiment in Mouse SCI and cortical neuron model. Methods/readouts recorded in the A-layer: Lipin1 knockdown promoted CST sprouting after pyramidotomy and robust CST regeneration after complete T8 SCI. Neonatal delivery before adult SCI produced axons extending up to about 3 mm caudal to the lesion, while adult delivery also increased regeneration.',
    'full-text source localization for m5a-p011-e001 confirms the curated aav9-shlipin1 in cortex before injury; adult complete t8 sci tested after neonatal or adult cortical delivery experiment in mouse sci and cortical neuron model. methods/readouts recorded in the a-layer: lipin1 knockdown promoted cst sprouting after pyramidotomy and robust cst regeneration after complete t8 sci. neonatal delivery before adult sci produced axons extending up to about 3 mm caudal to the lesion, while adult delivery also increased regeneration.',
    'Module 5A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P011-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P011-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P011", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T005", "tracker_id": "M5B-O011"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P011::M5A-P011-E001'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'tract regeneration / sprouting / recovery'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O011', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Hu M 2024 contributes activity or stimulation-enabled axon repair evidence in rat sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'qualitative',
    NULL,
    'Hu M 2024 contributes activity or stimulation-enabled axon repair evidence in rat sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'hu m 2024 contributes activity or stimulation-enabled axon repair evidence in rat sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'Module 5A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'medium',
    '{"curator_notes": "Primary title: Effects of transcranial magnetic stimulation on axonal regeneration in the corticospinal tract of female rats with spinal cord injury.. Note: TMS corticospinal regeneration anchor.", "experiment_tracker_id": "M5A-P012-E001", "measurement_method_inference": null, "paper_tracker_id": "M5A-P012", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M5B-T007", "tracker_id": "M5B-O012"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P012::M5A-P012-E001'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'Activity or stimulation-enabled axon repair'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O012', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P013-E001 confirms the curated Syt4 siRNA pool or individual siRNAs after plating, followed by neurite removal and regrowth experiment in Primary cortical neurons. Methods/readouts recorded in the A-layer: Syt4 silencing inhibited neurite elongation in primary cortical neurons without reducing cell number. RNA-seq showed altered neuronal development and neurite projection programs, supporting Syt4 as an intrinsic growth regulator.',
    'qualitative',
    'bulk transcriptomics / GEO dataset; genetic perturbation / knockdown assay; behavioral / functional recovery assay',
    'Full-text source localization for M5A-P013-E001 confirms the curated Syt4 siRNA pool or individual siRNAs after plating, followed by neurite removal and regrowth experiment in Primary cortical neurons. Methods/readouts recorded in the A-layer: Syt4 silencing inhibited neurite elongation in primary cortical neurons without reducing cell number. RNA-seq showed altered neuronal development and neurite projection programs, supporting Syt4 as an intrinsic growth regulator.',
    'full-text source localization for m5a-p013-e001 confirms the curated syt4 sirna pool or individual sirnas after plating, followed by neurite removal and regrowth experiment in primary cortical neurons. methods/readouts recorded in the a-layer: syt4 silencing inhibited neurite elongation in primary cortical neurons without reducing cell number. rna-seq showed altered neuronal development and neurite projection programs, supporting syt4 as an intrinsic growth regulator.',
    'Module 5A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P013-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P013-E001", "measurement_method_inference": "bulk transcriptomics / GEO dataset; genetic perturbation / knockdown assay; behavioral / functional recovery assay", "paper_tracker_id": "M5A-P013", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T001", "tracker_id": "M5B-O013"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P013::M5A-P013-E001'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'tract regeneration / sprouting / recovery'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O013', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P014-E001 confirms the curated Gabapentin 46 mg/kg intraperitoneally, 3 times daily for 1 week then 2 times daily until endpoint experiment in Mouse SCI model. Methods/readouts recorded in the A-layer: Early gabapentin treatment promoted CST sprouting and regeneration, improved forelimb skilled walking and reduced hypersensitivity. Regenerating CST axons formed synaptic structures and increased functional connectivity rostral and caudal to the lesion.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Full-text source localization for M5A-P014-E001 confirms the curated Gabapentin 46 mg/kg intraperitoneally, 3 times daily for 1 week then 2 times daily until endpoint experiment in Mouse SCI model. Methods/readouts recorded in the A-layer: Early gabapentin treatment promoted CST sprouting and regeneration, improved forelimb skilled walking and reduced hypersensitivity. Regenerating CST axons formed synaptic structures and increased functional connectivity rostral and caudal to the lesion.',
    'full-text source localization for m5a-p014-e001 confirms the curated gabapentin 46 mg/kg intraperitoneally, 3 times daily for 1 week then 2 times daily until endpoint experiment in mouse sci model. methods/readouts recorded in the a-layer: early gabapentin treatment promoted cst sprouting and regeneration, improved forelimb skilled walking and reduced hypersensitivity. regenerating cst axons formed synaptic structures and increased functional connectivity rostral and caudal to the lesion.',
    'Module 5A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P014-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P014-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P014", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T001", "tracker_id": "M5B-O014"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P014::M5A-P014-E001'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'tract regeneration / sprouting / recovery'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O014', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P015-E001 confirms the curated AAV1 activated alpha9 integrin with kindlin-1 delivered to C6/C7 or L4/L5 DRGs at the time of lesion experiment in Rat sensory SCI model. Methods/readouts recorded in the A-layer: Activated alpha9 integrin-kindlin-1 enabled sensory axons to regenerate through the lesion and along the spinal cord, with roughly half of labeled axons crossing the lesion and near-complete functional sensory pathway reconstruction on tape-removal, von Frey, and thermal tests.',
    'qualitative',
    NULL,
    'Full-text source localization for M5A-P015-E001 confirms the curated AAV1 activated alpha9 integrin with kindlin-1 delivered to C6/C7 or L4/L5 DRGs at the time of lesion experiment in Rat sensory SCI model. Methods/readouts recorded in the A-layer: Activated alpha9 integrin-kindlin-1 enabled sensory axons to regenerate through the lesion and along the spinal cord, with roughly half of labeled axons crossing the lesion and near-complete functional sensory pathway reconstruction on tape-removal, von Frey, and thermal tests.',
    'full-text source localization for m5a-p015-e001 confirms the curated aav1 activated alpha9 integrin with kindlin-1 delivered to c6/c7 or l4/l5 drgs at the time of lesion experiment in rat sensory sci model. methods/readouts recorded in the a-layer: activated alpha9 integrin-kindlin-1 enabled sensory axons to regenerate through the lesion and along the spinal cord, with roughly half of labeled axons crossing the lesion and near-complete functional sensory pathway reconstruction on tape-removal, von frey, and thermal tests.',
    'Module 5A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P015-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P015-E001", "measurement_method_inference": null, "paper_tracker_id": "M5A-P015", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T002", "tracker_id": "M5B-O015"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P015::M5A-P015-E001'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'Extrinsic inhibitory matrix / guidance pathway'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O015', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P016-E001 confirms the curated AAV-mediated RhoA/Pten deletion in corticospinal neurons combined with excitatory hM3Dq DREADD stimulation using DCZ experiment in Mouse cervical SCI model. Methods/readouts recorded in the A-layer: RhoA/Pten deletion reduced CST axon dieback but alone did not fully restore function. Adding neuronal stimulation promoted greater CST collateral growth and forelimb motor recovery than genetic manipulation alone, with grid-walking improvement and new presynaptic bouton formation near the lesion.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Full-text source localization for M5A-P016-E001 confirms the curated AAV-mediated RhoA/Pten deletion in corticospinal neurons combined with excitatory hM3Dq DREADD stimulation using DCZ experiment in Mouse cervical SCI model. Methods/readouts recorded in the A-layer: RhoA/Pten deletion reduced CST axon dieback but alone did not fully restore function. Adding neuronal stimulation promoted greater CST collateral growth and forelimb motor recovery than genetic manipulation alone, with grid-walking improvement and new presynaptic bouton formation near the lesion.',
    'full-text source localization for m5a-p016-e001 confirms the curated aav-mediated rhoa/pten deletion in corticospinal neurons combined with excitatory hm3dq dreadd stimulation using dcz experiment in mouse cervical sci model. methods/readouts recorded in the a-layer: rhoa/pten deletion reduced cst axon dieback but alone did not fully restore function. adding neuronal stimulation promoted greater cst collateral growth and forelimb motor recovery than genetic manipulation alone, with grid-walking improvement and new presynaptic bouton formation near the lesion.',
    'Module 5A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P016-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P016-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P016", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T001", "tracker_id": "M5B-O016"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P016::M5A-P016-E001'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'tract regeneration / sprouting / recovery'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O016', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P017-E001 confirms the curated Thiorphan dose-response screen, 100-250 micromolar peak range experiment in Mouse. Methods/readouts recorded in the A-layer: Adult mouse motor cortex neurons were exposed to candidate compounds for 5 days. Thiorphan at 250 micromolar increased total neurite outgrowth by 80% and longest neurite length by 30% versus control, with peak effects at 100-250 micromolar; triflusal was modest and non-significant, milrinone had no effect, and adiphenine reduced outgrowth. The CMap screen selected compounds by similarity to a regenerating corticospinal-neuron transcriptomic signature, but the in vitro assay was the causal growth screen.',
    'qualitative',
    'bulk transcriptomics / GEO dataset; behavioral / functional recovery assay',
    'Full-text source localization for M5A-P017-E001 confirms the curated Thiorphan dose-response screen, 100-250 micromolar peak range experiment in Mouse. Methods/readouts recorded in the A-layer: Adult mouse motor cortex neurons were exposed to candidate compounds for 5 days. Thiorphan at 250 micromolar increased total neurite outgrowth by 80% and longest neurite length by 30% versus control, with peak effects at 100-250 micromolar; triflusal was modest and non-significant, milrinone had no effect, and adiphenine reduced outgrowth. The CMap screen selected compounds by similarity to a regenerating corticospinal-neuron transcriptomic signature, but the in vitro assay was the causal growth screen.',
    'full-text source localization for m5a-p017-e001 confirms the curated thiorphan dose-response screen, 100-250 micromolar peak range experiment in mouse. methods/readouts recorded in the a-layer: adult mouse motor cortex neurons were exposed to candidate compounds for 5 days. thiorphan at 250 micromolar increased total neurite outgrowth by 80% and longest neurite length by 30% versus control, with peak effects at 100-250 micromolar; triflusal was modest and non-significant, milrinone had no effect, and adiphenine reduced outgrowth. the cmap screen selected compounds by similarity to a regenerating corticospinal-neuron transcriptomic signature, but the in vitro assay was the causal growth screen.',
    'Module 5A full-text extraction; Fig. 1c-e; adult mouse motor cortex screen',
    'A-layer full text; Fig. 1c-e; adult mouse motor cortex screen',
    'medium',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P017-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P017-E001", "measurement_method_inference": "bulk transcriptomics / GEO dataset; behavioral / functional recovery assay", "paper_tracker_id": "M5A-P017", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T001", "tracker_id": "M5B-O017"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P017::M5A-P017-E001'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'tract regeneration / sprouting / recovery'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O017', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P018-E001 confirms the curated Adenoviral manipulation showed that TTBK2 supports primary-cilium formation and spinal-neuron axon growth; TTBK2 or KIF3A loss shortened cilia and reduced axon-growth and cilium/SHH-associated transcriptional programs. experiment in Mouse SCI model plus cultured spinal neurons. Methods/readouts recorded in the A-layer: Full-text record adds the in vitro causal cilium assay and the TTBK2 gain/loss design.',
    'qualitative',
    'qPCR / RT-PCR / mRNA assay',
    'Full-text source localization for M5A-P018-E001 confirms the curated Adenoviral manipulation showed that TTBK2 supports primary-cilium formation and spinal-neuron axon growth; TTBK2 or KIF3A loss shortened cilia and reduced axon-growth and cilium/SHH-associated transcriptional programs. experiment in Mouse SCI model plus cultured spinal neurons. Methods/readouts recorded in the A-layer: Full-text record adds the in vitro causal cilium assay and the TTBK2 gain/loss design.',
    'full-text source localization for m5a-p018-e001 confirms the curated adenoviral manipulation showed that ttbk2 supports primary-cilium formation and spinal-neuron axon growth; ttbk2 or kif3a loss shortened cilia and reduced axon-growth and cilium/shh-associated transcriptional programs. experiment in mouse sci model plus cultured spinal neurons. methods/readouts recorded in the a-layer: full-text record adds the in vitro causal cilium assay and the ttbk2 gain/loss design.',
    'Module 5A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P018-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P018-E001", "measurement_method_inference": "qPCR / RT-PCR / mRNA assay", "paper_tracker_id": "M5A-P018", "quantitative": "YES", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T005", "tracker_id": "M5B-O018"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P018::M5A-P018-E001'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'intrinsic growth competence'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O018', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P019-E001 confirms the curated KLF7, MEF2, MEF2-VP16, ATF3, and combination expression constructs experiment in F11 neurite-outgrowth assay and rat DRG neurons. Methods/readouts recorded in the A-layer: In vitro screening identified KLF7/MEF2 and ATF3/KLF7/MEF2 as potent neurite-growth combinations. The triple combination was strongest in vitro, but KLF7/MEF2 was the combination that retained benefit in vivo without the same apoptosis-associated gene signature.',
    'qualitative',
    NULL,
    'Full-text source localization for M5A-P019-E001 confirms the curated KLF7, MEF2, MEF2-VP16, ATF3, and combination expression constructs experiment in F11 neurite-outgrowth assay and rat DRG neurons. Methods/readouts recorded in the A-layer: In vitro screening identified KLF7/MEF2 and ATF3/KLF7/MEF2 as potent neurite-growth combinations. The triple combination was strongest in vitro, but KLF7/MEF2 was the combination that retained benefit in vivo without the same apoptosis-associated gene signature.',
    'full-text source localization for m5a-p019-e001 confirms the curated klf7, mef2, mef2-vp16, atf3, and combination expression constructs experiment in f11 neurite-outgrowth assay and rat drg neurons. methods/readouts recorded in the a-layer: in vitro screening identified klf7/mef2 and atf3/klf7/mef2 as potent neurite-growth combinations. the triple combination was strongest in vitro, but klf7/mef2 was the combination that retained benefit in vivo without the same apoptosis-associated gene signature.',
    'Module 5A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P019-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P019-E001", "measurement_method_inference": null, "paper_tracker_id": "M5A-P019", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T005", "tracker_id": "M5B-O019"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P019::M5A-P019-E001'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'intrinsic growth competence'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O019', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P020-E001 confirms the curated AAV2/9-CAMKII-bPAC-mCherry in cortical layer V with daily blue-light cAMP induction experiment in Rat. Methods/readouts recorded in the A-layer: Cortical bPAC stimulation raised cAMP, p-CREB and c-Fos, restored layer-V neuron electrophysiology, increased early and sustained BBB locomotor recovery, and increased CST plasticity. The study frames benefit as cortical rerouting rather than long-distance CST regeneration.',
    'qualitative',
    'barrier / permeability / endothelial assay; behavioral / functional recovery assay',
    'Full-text source localization for M5A-P020-E001 confirms the curated AAV2/9-CAMKII-bPAC-mCherry in cortical layer V with daily blue-light cAMP induction experiment in Rat. Methods/readouts recorded in the A-layer: Cortical bPAC stimulation raised cAMP, p-CREB and c-Fos, restored layer-V neuron electrophysiology, increased early and sustained BBB locomotor recovery, and increased CST plasticity. The study frames benefit as cortical rerouting rather than long-distance CST regeneration.',
    'full-text source localization for m5a-p020-e001 confirms the curated aav2/9-camkii-bpac-mcherry in cortical layer v with daily blue-light camp induction experiment in rat. methods/readouts recorded in the a-layer: cortical bpac stimulation raised camp, p-creb and c-fos, restored layer-v neuron electrophysiology, increased early and sustained bbb locomotor recovery, and increased cst plasticity. the study frames benefit as cortical rerouting rather than long-distance cst regeneration.',
    'Module 5A full-text extraction; Full text PMC; Fig. 1-4',
    'A-layer full text; Full text PMC; Fig. 1-4',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P020-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P020-E001", "measurement_method_inference": "barrier / permeability / endothelial assay; behavioral / functional recovery assay", "paper_tracker_id": "M5A-P020", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T007", "tracker_id": "M5B-O020"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P020::M5A-P020-E001'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'tract regeneration / sprouting / recovery'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O020', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P021-E001 confirms the curated Glutamate-linked upconversion nanoparticles to target glutamatergic postsynaptic neurons and transduce NIR into VChR1 excitation experiment in Mouse. Methods/readouts recorded in the A-layer: Glu-UCNP plus NIR increased CST sprouting across the lesion toward Chx10+/PSD95+ interneurons, raised GAP43 and synaptic-marker signals, and produced greater calcium activity in reconnected circuits than nanoparticle or light controls.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Full-text source localization for M5A-P021-E001 confirms the curated Glutamate-linked upconversion nanoparticles to target glutamatergic postsynaptic neurons and transduce NIR into VChR1 excitation experiment in Mouse. Methods/readouts recorded in the A-layer: Glu-UCNP plus NIR increased CST sprouting across the lesion toward Chx10+/PSD95+ interneurons, raised GAP43 and synaptic-marker signals, and produced greater calcium activity in reconnected circuits than nanoparticle or light controls.',
    'full-text source localization for m5a-p021-e001 confirms the curated glutamate-linked upconversion nanoparticles to target glutamatergic postsynaptic neurons and transduce nir into vchr1 excitation experiment in mouse. methods/readouts recorded in the a-layer: glu-ucnp plus nir increased cst sprouting across the lesion toward chx10+/psd95+ interneurons, raised gap43 and synaptic-marker signals, and produced greater calcium activity in reconnected circuits than nanoparticle or light controls.',
    'Module 5A full-text extraction; Full text PMC; Fig. 1-4',
    'A-layer full text; Full text PMC; Fig. 1-4',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P021-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P021-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P021", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T007", "tracker_id": "M5B-O021"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P021::M5A-P021-E001'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'tract regeneration / sprouting / recovery'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O021', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'In a rat high-severity chronic SCI model at Th10-Th11, Netrin-1 delivery to the lesion epicenter promoted recovery of hindlimb joint movement plus partial climbing/grasping and was associated with CST regrowth/sprouting/remyelination, extrapyramidal and serotonergic/dopaminergic axon reconnection, lower motoneuron preservation, and sensory-pathway neuroprotection.',
    'qualitative',
    'behavioral / functional recovery assay',
    'In a rat high-severity chronic SCI model at Th10-Th11, Netrin-1 delivery to the lesion epicenter promoted recovery of hindlimb joint movement plus partial climbing/grasping and was associated with CST regrowth/sprouting/remyelination, extrapyramidal and serotonergic/dopaminergic axon reconnection, lower motoneuron preservation, and sensory-pathway neuroprotection.',
    'Netrin-1 promotes functional and anatomical repair signals in high-severity chronic rat SCI',
    'PubMed abstract',
    'PubMed abstract verified',
    'medium',
    '{"curator_notes": "Source-verified but not full-text upgraded; PMID 41163574.", "experiment_tracker_id": "M5A-P022-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P022", "quantitative": "YES", "statistics_reported": "PubMed abstract reports functional and anatomical endpoints; open full text not identified in metadata batch", "topic_id": "M5B-T002", "tracker_id": "M5B-O022"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P022::M5A-P022-E001'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'tract regeneration / sprouting / recovery'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O022', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P023-E001 confirms the curated Local Netrin-1 and DCC overexpression lentiviruses injected around the transection site immediately after injury experiment in Rat SCI model. Methods/readouts recorded in the A-layer: Co-overexpression of Netrin-1 and DCC increased GAP43 and synaptophysin-associated axon growth, reduced apoptosis, lowered NgR1-RhoA-ROCK pathway signals, and improved BBB motor recovery during subacute and chronic follow-up.',
    'qualitative',
    'barrier / permeability / endothelial assay; behavioral / functional recovery assay',
    'Full-text source localization for M5A-P023-E001 confirms the curated Local Netrin-1 and DCC overexpression lentiviruses injected around the transection site immediately after injury experiment in Rat SCI model. Methods/readouts recorded in the A-layer: Co-overexpression of Netrin-1 and DCC increased GAP43 and synaptophysin-associated axon growth, reduced apoptosis, lowered NgR1-RhoA-ROCK pathway signals, and improved BBB motor recovery during subacute and chronic follow-up.',
    'full-text source localization for m5a-p023-e001 confirms the curated local netrin-1 and dcc overexpression lentiviruses injected around the transection site immediately after injury experiment in rat sci model. methods/readouts recorded in the a-layer: co-overexpression of netrin-1 and dcc increased gap43 and synaptophysin-associated axon growth, reduced apoptosis, lowered ngr1-rhoa-rock pathway signals, and improved bbb motor recovery during subacute and chronic follow-up.',
    'Module 5A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P023-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P023-E001", "measurement_method_inference": "barrier / permeability / endothelial assay; behavioral / functional recovery assay", "paper_tracker_id": "M5A-P023", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T002", "tracker_id": "M5B-O023"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P023::M5A-P023-E001'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'Extrinsic inhibitory matrix / guidance pathway'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O023', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P024-E001 confirms the curated CSPG-driven microglia-astrocyte mechanism experiment in Rat SCI model plus reactive astrocytes/microglia. Methods/readouts recorded in the A-layer: CSPGs induced a pro-inflammatory microglial state by suppressing CYP450 metabolic activity; this state drove reactive-astrocyte transition toward scar-forming astrocytes and reinforced a CSPG-rich feedback loop.',
    'qualitative',
    NULL,
    'Full-text source localization for M5A-P024-E001 confirms the curated CSPG-driven microglia-astrocyte mechanism experiment in Rat SCI model plus reactive astrocytes/microglia. Methods/readouts recorded in the A-layer: CSPGs induced a pro-inflammatory microglial state by suppressing CYP450 metabolic activity; this state drove reactive-astrocyte transition toward scar-forming astrocytes and reinforced a CSPG-rich feedback loop.',
    'full-text source localization for m5a-p024-e001 confirms the curated cspg-driven microglia-astrocyte mechanism experiment in rat sci model plus reactive astrocytes/microglia. methods/readouts recorded in the a-layer: cspgs induced a pro-inflammatory microglial state by suppressing cyp450 metabolic activity; this state drove reactive-astrocyte transition toward scar-forming astrocytes and reinforced a cspg-rich feedback loop.',
    'Module 5A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P024-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P024-E001", "measurement_method_inference": null, "paper_tracker_id": "M5A-P024", "quantitative": "YES", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T002", "tracker_id": "M5B-O024"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P024::M5A-P024-E001'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'Extrinsic inhibitory matrix / guidance pathway'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O024', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P025-E001 confirms the curated 6 x 10^5 GFP+ Schwann cells injected at lesion epicenter plus lenti-ChABC 2 x 10^7 TU/uL at 1.5 mm rostral and caudal to lesion experiment in Rat SCI transplantation model. Methods/readouts recorded in the A-layer: The combination degraded CSPGs at lesion borders, allowed Schwann cells to migrate into host cord, increased serotonergic and dopaminergic axonal regrowth, improved BBB, grid-walk, gait, and bladder outcomes, and outperformed either monotherapy.',
    'qualitative',
    'barrier / permeability / endothelial assay',
    'Full-text source localization for M5A-P025-E001 confirms the curated 6 x 10^5 GFP+ Schwann cells injected at lesion epicenter plus lenti-ChABC 2 x 10^7 TU/uL at 1.5 mm rostral and caudal to lesion experiment in Rat SCI transplantation model. Methods/readouts recorded in the A-layer: The combination degraded CSPGs at lesion borders, allowed Schwann cells to migrate into host cord, increased serotonergic and dopaminergic axonal regrowth, improved BBB, grid-walk, gait, and bladder outcomes, and outperformed either monotherapy.',
    'full-text source localization for m5a-p025-e001 confirms the curated 6 x 10^5 gfp+ schwann cells injected at lesion epicenter plus lenti-chabc 2 x 10^7 tu/ul at 1.5 mm rostral and caudal to lesion experiment in rat sci transplantation model. methods/readouts recorded in the a-layer: the combination degraded cspgs at lesion borders, allowed schwann cells to migrate into host cord, increased serotonergic and dopaminergic axonal regrowth, improved bbb, grid-walk, gait, and bladder outcomes, and outperformed either monotherapy.',
    'Module 5A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P025-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P025-E001", "measurement_method_inference": "barrier / permeability / endothelial assay", "paper_tracker_id": "M5A-P025", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T004", "tracker_id": "M5B-O025"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P025::M5A-P025-E001'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'relay plasticity / circuit reconstruction'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O025', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Zhu S 2024 contributes extrinsic inhibitory matrix / guidance pathway evidence in mouse sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'qualitative',
    NULL,
    'Zhu S 2024 contributes extrinsic inhibitory matrix / guidance pathway evidence in mouse sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'zhu s 2024 contributes extrinsic inhibitory matrix / guidance pathway evidence in mouse sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'Module 5A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'medium',
    '{"curator_notes": "Primary title: Schwann Cell-Derived Exosomes Induced Axon Growth after Spinal Cord Injury by Decreasing PTP- Activation on CSPGs via the Rho/ROCK Pathway.. Note: Extrinsic inhibitory matrix / guidance pathway anchor.", "experiment_tracker_id": "M5A-P026-E001", "measurement_method_inference": null, "paper_tracker_id": "M5A-P026", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M5B-T002", "tracker_id": "M5B-O026"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P026::M5A-P026-E001'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'Extrinsic inhibitory matrix / guidance pathway'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O026', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P027-E001 confirms the curated Clinical participants receiving the Nogo-A-neutralizing antibody NG101 were assessed with lesion volume, tissue bridges, cross-sectional cord area, and tract-specific myelin-sensitive MTsat MRI biomarkers. experiment in Human clinical SCI cohort. Methods/readouts recorded in the A-layer: Full-text record is a clinical biomarker/intervention study, not an animal regeneration experiment.',
    'qualitative',
    'MRI / imaging assay; behavioral / functional recovery assay',
    'Full-text source localization for M5A-P027-E001 confirms the curated Clinical participants receiving the Nogo-A-neutralizing antibody NG101 were assessed with lesion volume, tissue bridges, cross-sectional cord area, and tract-specific myelin-sensitive MTsat MRI biomarkers. experiment in Human clinical SCI cohort. Methods/readouts recorded in the A-layer: Full-text record is a clinical biomarker/intervention study, not an animal regeneration experiment.',
    'full-text source localization for m5a-p027-e001 confirms the curated clinical participants receiving the nogo-a-neutralizing antibody ng101 were assessed with lesion volume, tissue bridges, cross-sectional cord area, and tract-specific myelin-sensitive mtsat mri biomarkers. experiment in human clinical sci cohort. methods/readouts recorded in the a-layer: full-text record is a clinical biomarker/intervention study, not an animal regeneration experiment.',
    'Module 5A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P027-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P027-E001", "measurement_method_inference": "MRI / imaging assay; behavioral / functional recovery assay", "paper_tracker_id": "M5A-P027", "quantitative": "YES", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T002", "tracker_id": "M5B-O027"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P027::M5A-P027-E001'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'tract regeneration / sprouting / recovery'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O027', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P028-E001 confirms the curated Single intrathecal XMC-ChABC injection at 6 weeks followed 1 week later by 4 x 10^5 human directly reprogrammed oligodendrogenic NPCs injected into the cord parenchyma experiment in Chronic rat SCI xenograft model. Methods/readouts recorded in the A-layer: The XMC-ChABC plus oNPC combination increased graft survival and migration, oligodendrocyte differentiation, graft-derived myelination of spared axons, preserved synaptic boutons, and BBB/CatWalk functional recovery in chronic SCI.',
    'qualitative',
    'barrier / permeability / endothelial assay; behavioral / functional recovery assay',
    'Full-text source localization for M5A-P028-E001 confirms the curated Single intrathecal XMC-ChABC injection at 6 weeks followed 1 week later by 4 x 10^5 human directly reprogrammed oligodendrogenic NPCs injected into the cord parenchyma experiment in Chronic rat SCI xenograft model. Methods/readouts recorded in the A-layer: The XMC-ChABC plus oNPC combination increased graft survival and migration, oligodendrocyte differentiation, graft-derived myelination of spared axons, preserved synaptic boutons, and BBB/CatWalk functional recovery in chronic SCI.',
    'full-text source localization for m5a-p028-e001 confirms the curated single intrathecal xmc-chabc injection at 6 weeks followed 1 week later by 4 x 10^5 human directly reprogrammed oligodendrogenic npcs injected into the cord parenchyma experiment in chronic rat sci xenograft model. methods/readouts recorded in the a-layer: the xmc-chabc plus onpc combination increased graft survival and migration, oligodendrocyte differentiation, graft-derived myelination of spared axons, preserved synaptic boutons, and bbb/catwalk functional recovery in chronic sci.',
    'Module 5A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P028-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P028-E001", "measurement_method_inference": "barrier / permeability / endothelial assay; behavioral / functional recovery assay", "paper_tracker_id": "M5A-P028", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T003", "tracker_id": "M5B-O028"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P028::M5A-P028-E001'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'white matter / remyelination / debris handling'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O028', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P029-E001 confirms the curated TREM2 was concentrated in Iba1+ macrophages/microglia; deletion impaired myelin-debris engulfment and degradation, increased foamy macrophage accumulation, and reduced PI3K/AKT-linked DAM activation. experiment in Mouse SCI model. Methods/readouts recorded in the A-layer: Full-text evidence supports TREM2 for debris handling but not automatically for remyelination or long-term repair.',
    'qualitative',
    'pathway activity / phospho-signaling assay',
    'Full-text source localization for M5A-P029-E001 confirms the curated TREM2 was concentrated in Iba1+ macrophages/microglia; deletion impaired myelin-debris engulfment and degradation, increased foamy macrophage accumulation, and reduced PI3K/AKT-linked DAM activation. experiment in Mouse SCI model. Methods/readouts recorded in the A-layer: Full-text evidence supports TREM2 for debris handling but not automatically for remyelination or long-term repair.',
    'full-text source localization for m5a-p029-e001 confirms the curated trem2 was concentrated in iba1+ macrophages/microglia; deletion impaired myelin-debris engulfment and degradation, increased foamy macrophage accumulation, and reduced pi3k/akt-linked dam activation. experiment in mouse sci model. methods/readouts recorded in the a-layer: full-text evidence supports trem2 for debris handling but not automatically for remyelination or long-term repair.',
    'Module 5A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P029-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P029-E001", "measurement_method_inference": "pathway activity / phospho-signaling assay", "paper_tracker_id": "M5A-P029", "quantitative": "YES", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T003", "tracker_id": "M5B-O029"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P029::M5A-P029-E001'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'white matter / remyelination / debris handling'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O029', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P030-E001 confirms the curated Lesion-remote astrocytes acquired distinct white-matter reactivity states and expressed CCN1; CCN1 loss caused aberrant microglial activation, impaired myelin/axon-debris processing, altered lipid metabolism, and reduced lipid-droplet buffering. experiment in Mouse SCI model plus human tissue comparator. Methods/readouts recorded in the A-layer: Full-text record corrects the first-pass human placeholder and adds multi-omics/spatial evidence.',
    'qualitative',
    'spatial transcriptomics / spatial atlas',
    'Full-text source localization for M5A-P030-E001 confirms the curated Lesion-remote astrocytes acquired distinct white-matter reactivity states and expressed CCN1; CCN1 loss caused aberrant microglial activation, impaired myelin/axon-debris processing, altered lipid metabolism, and reduced lipid-droplet buffering. experiment in Mouse SCI model plus human tissue comparator. Methods/readouts recorded in the A-layer: Full-text record corrects the first-pass human placeholder and adds multi-omics/spatial evidence.',
    'full-text source localization for m5a-p030-e001 confirms the curated lesion-remote astrocytes acquired distinct white-matter reactivity states and expressed ccn1; ccn1 loss caused aberrant microglial activation, impaired myelin/axon-debris processing, altered lipid metabolism, and reduced lipid-droplet buffering. experiment in mouse sci model plus human tissue comparator. methods/readouts recorded in the a-layer: full-text record corrects the first-pass human placeholder and adds multi-omics/spatial evidence.',
    'Module 5A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P030-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P030-E001", "measurement_method_inference": "spatial transcriptomics / spatial atlas", "paper_tracker_id": "M5A-P030", "quantitative": "YES", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T003", "tracker_id": "M5B-O030"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P030::M5A-P030-E001'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'white matter / remyelination / debris handling'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O030', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P031-E001 confirms the curated Inducible Myrf deletion in OPC lineage to prevent new myelin formation experiment in Mouse. Methods/readouts recorded in the A-layer: Myrf ICKO mice had fewer spared myelin sheaths than controls but showed no worse BMS or inclined-plane recovery after severe contusion; both groups remained largely unable to step, so absence of a genotype difference does not demonstrate robust functional recovery.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Full-text source localization for M5A-P031-E001 confirms the curated Inducible Myrf deletion in OPC lineage to prevent new myelin formation experiment in Mouse. Methods/readouts recorded in the A-layer: Myrf ICKO mice had fewer spared myelin sheaths than controls but showed no worse BMS or inclined-plane recovery after severe contusion; both groups remained largely unable to step, so absence of a genotype difference does not demonstrate robust functional recovery.',
    'full-text source localization for m5a-p031-e001 confirms the curated inducible myrf deletion in opc lineage to prevent new myelin formation experiment in mouse. methods/readouts recorded in the a-layer: myrf icko mice had fewer spared myelin sheaths than controls but showed no worse bms or inclined-plane recovery after severe contusion; both groups remained largely unable to step, so absence of a genotype difference does not demonstrate robust functional recovery.',
    'Module 5A full-text extraction; Full text PMC; severe injury cohort',
    'A-layer full text; Full text PMC; severe injury cohort',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P031-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P031-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P031", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T003", "tracker_id": "M5B-O031"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P031::M5A-P031-E001'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'white matter / remyelination / debris handling'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O031', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P032-E001 confirms the curated Polycaprolactone nanofiber scaffold coated with spinal-cord-homogenate-pretreated macrophage membrane, 10 x 5 mm, placed over the opened dura experiment in Rat SCI model. Methods/readouts recorded in the A-layer: pMM-PCL adsorbed myelin debris, reduced foam-cell accumulation and inflammatory markers, reduced collagen and GFAP scar signals, increased MAP2, TUBB3, and NF200-associated neuronal/axon markers, and improved gait and BBB scores by 42 dpi.',
    'qualitative',
    'barrier / permeability / endothelial assay',
    'Full-text source localization for M5A-P032-E001 confirms the curated Polycaprolactone nanofiber scaffold coated with spinal-cord-homogenate-pretreated macrophage membrane, 10 x 5 mm, placed over the opened dura experiment in Rat SCI model. Methods/readouts recorded in the A-layer: pMM-PCL adsorbed myelin debris, reduced foam-cell accumulation and inflammatory markers, reduced collagen and GFAP scar signals, increased MAP2, TUBB3, and NF200-associated neuronal/axon markers, and improved gait and BBB scores by 42 dpi.',
    'full-text source localization for m5a-p032-e001 confirms the curated polycaprolactone nanofiber scaffold coated with spinal-cord-homogenate-pretreated macrophage membrane, 10 x 5 mm, placed over the opened dura experiment in rat sci model. methods/readouts recorded in the a-layer: pmm-pcl adsorbed myelin debris, reduced foam-cell accumulation and inflammatory markers, reduced collagen and gfap scar signals, increased map2, tubb3, and nf200-associated neuronal/axon markers, and improved gait and bbb scores by 42 dpi.',
    'Module 5A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P032-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P032-E001", "measurement_method_inference": "barrier / permeability / endothelial assay", "paper_tracker_id": "M5A-P032", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T003", "tracker_id": "M5B-O032"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P032::M5A-P032-E001'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'white matter / remyelination / debris handling'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O032', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P033-E001 confirms the curated SeroPTEN-CG is a DNA/RNA heteroduplex hydrogel built from a 5-HTP-derived targeting/neuromodulatory motif and PTEN siRNA; DNase-mediated disassembly releases nanogels for serotonergic targeting and PTEN silencing. experiment in Mouse SCI model plus primary neurons. Methods/readouts recorded in the A-layer: Full-text methods define a dual-function material rather than a single serotonergic drug.',
    'qualitative',
    'genetic perturbation / knockdown assay',
    'Full-text source localization for M5A-P033-E001 confirms the curated SeroPTEN-CG is a DNA/RNA heteroduplex hydrogel built from a 5-HTP-derived targeting/neuromodulatory motif and PTEN siRNA; DNase-mediated disassembly releases nanogels for serotonergic targeting and PTEN silencing. experiment in Mouse SCI model plus primary neurons. Methods/readouts recorded in the A-layer: Full-text methods define a dual-function material rather than a single serotonergic drug.',
    'full-text source localization for m5a-p033-e001 confirms the curated seropten-cg is a dna/rna heteroduplex hydrogel built from a 5-htp-derived targeting/neuromodulatory motif and pten sirna; dnase-mediated disassembly releases nanogels for serotonergic targeting and pten silencing. experiment in mouse sci model plus primary neurons. methods/readouts recorded in the a-layer: full-text methods define a dual-function material rather than a single serotonergic drug.',
    'Module 5A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P033-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P033-E001", "measurement_method_inference": "genetic perturbation / knockdown assay", "paper_tracker_id": "M5A-P033", "quantitative": "YES", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T004", "tracker_id": "M5B-O033"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P033::M5A-P033-E001'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'relay plasticity / circuit reconstruction'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O033', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P034-E001 confirms the curated Constitutive TPH2 loss causing central serotonin deficiency experiment in Rat. Methods/readouts recorded in the A-layer: TPH2 KO rats had near-undetectable spinal serotonin/5-HIAA and significantly greater tapered-beam and ladder deficits at weeks 3-4, with slower recovery of hindlimb tone and voluntary movement than WT despite comparable lesion size.',
    'qualitative',
    'genetic perturbation / knockdown assay; behavioral / functional recovery assay',
    'Full-text source localization for M5A-P034-E001 confirms the curated Constitutive TPH2 loss causing central serotonin deficiency experiment in Rat. Methods/readouts recorded in the A-layer: TPH2 KO rats had near-undetectable spinal serotonin/5-HIAA and significantly greater tapered-beam and ladder deficits at weeks 3-4, with slower recovery of hindlimb tone and voluntary movement than WT despite comparable lesion size.',
    'full-text source localization for m5a-p034-e001 confirms the curated constitutive tph2 loss causing central serotonin deficiency experiment in rat. methods/readouts recorded in the a-layer: tph2 ko rats had near-undetectable spinal serotonin/5-hiaa and significantly greater tapered-beam and ladder deficits at weeks 3-4, with slower recovery of hindlimb tone and voluntary movement than wt despite comparable lesion size.',
    'Module 5A full-text extraction; Full text PMC; serotonin depletion and behavior',
    'A-layer full text; Full text PMC; serotonin depletion and behavior',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P034-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P034-E001", "measurement_method_inference": "genetic perturbation / knockdown assay; behavioral / functional recovery assay", "paper_tracker_id": "M5A-P034", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T004", "tracker_id": "M5B-O034"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P034::M5A-P034-E001'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'relay plasticity / circuit reconstruction'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O034', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Gao Z 2025 contributes serotonergic/propriospinal relay plasticity evidence in human / translational context, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Gao Z 2025 contributes serotonergic/propriospinal relay plasticity evidence in human / translational context, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'gao z 2025 contributes serotonergic/propriospinal relay plasticity evidence in human / translational context, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'Module 5A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'medium',
    '{"curator_notes": "Primary title: Neuronal HDAC3 knockdown promotes propriospinal detour pathway formation and locomotor recovery in a mouse model of spinal cord injury.. Note: Serotonergic/propriospinal relay plasticity anchor.", "experiment_tracker_id": "M5A-P035-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P035", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M5B-T004", "tracker_id": "M5B-O035"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P035::M5A-P035-E001'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'relay plasticity / circuit reconstruction'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O035', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P036-E001 confirms the curated AAV2/9-OPN plus AAV2/9-IGF1 in T8 neurons and 1 million E14 spinal NSCs transplanted into the lesion cavity experiment in Rat. Methods/readouts recorded in the A-layer: OPN/IGF1 alone did not regenerate axons through the complete crush and NSCs alone did not integrate with host pathways. Combined treatment filled the cavity, reduced the glial scar, enabled host axons to enter the graft, produced SYN/PSD95-associated contacts and approximately 30% NeuN-positive graft-neuron differentiation with axons extending caudally. Structural synapse markers were partly immature or nonsynaptic, so this row supports anatomical bridge formation but not functional transmission by itself.',
    'qualitative',
    NULL,
    'Full-text source localization for M5A-P036-E001 confirms the curated AAV2/9-OPN plus AAV2/9-IGF1 in T8 neurons and 1 million E14 spinal NSCs transplanted into the lesion cavity experiment in Rat. Methods/readouts recorded in the A-layer: OPN/IGF1 alone did not regenerate axons through the complete crush and NSCs alone did not integrate with host pathways. Combined treatment filled the cavity, reduced the glial scar, enabled host axons to enter the graft, produced SYN/PSD95-associated contacts and approximately 30% NeuN-positive graft-neuron differentiation with axons extending caudally. Structural synapse markers were partly immature or nonsynaptic, so this row supports anatomical bridge formation but not functional transmission by itself.',
    'full-text source localization for m5a-p036-e001 confirms the curated aav2/9-opn plus aav2/9-igf1 in t8 neurons and 1 million e14 spinal nscs transplanted into the lesion cavity experiment in rat. methods/readouts recorded in the a-layer: opn/igf1 alone did not regenerate axons through the complete crush and nscs alone did not integrate with host pathways. combined treatment filled the cavity, reduced the glial scar, enabled host axons to enter the graft, produced syn/psd95-associated contacts and approximately 30% neun-positive graft-neuron differentiation with axons extending caudally. structural synapse markers were partly immature or nonsynaptic, so this row supports anatomical bridge formation but not functional transmission by itself.',
    'Module 5A full-text extraction; Fig. 1-2; OPN/IGF1 regeneration plus NSC bridge formation',
    'A-layer full text; Fig. 1-2; OPN/IGF1 regeneration plus NSC bridge formation',
    'medium',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P036-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P036-E001", "measurement_method_inference": null, "paper_tracker_id": "M5A-P036", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T004", "tracker_id": "M5B-O036"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P036::M5A-P036-E001'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'relay plasticity / circuit reconstruction'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O036', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P037-E001 confirms the curated ROS-responsive QZIF-polymersomes containing quercetin, 30 mg/kg intraperitoneally once daily for 7 d from immediately after injury experiment in Rat SCI model. Methods/readouts recorded in the A-layer: QZIF-polymersomes accumulated at the lesion, reduced lesion volume and TNF-alpha/IL-1beta, increased neuronal density, improved BBB scores from 14 dpi, and shortened MEP latency while increasing MEP amplitude.',
    'qualitative',
    'ELISA / cytokine protein assay; barrier / permeability / endothelial assay',
    'Full-text source localization for M5A-P037-E001 confirms the curated ROS-responsive QZIF-polymersomes containing quercetin, 30 mg/kg intraperitoneally once daily for 7 d from immediately after injury experiment in Rat SCI model. Methods/readouts recorded in the A-layer: QZIF-polymersomes accumulated at the lesion, reduced lesion volume and TNF-alpha/IL-1beta, increased neuronal density, improved BBB scores from 14 dpi, and shortened MEP latency while increasing MEP amplitude.',
    'full-text source localization for m5a-p037-e001 confirms the curated ros-responsive qzif-polymersomes containing quercetin, 30 mg/kg intraperitoneally once daily for 7 d from immediately after injury experiment in rat sci model. methods/readouts recorded in the a-layer: qzif-polymersomes accumulated at the lesion, reduced lesion volume and tnf-alpha/il-1beta, increased neuronal density, improved bbb scores from 14 dpi, and shortened mep latency while increasing mep amplitude.',
    'Module 5A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P037-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P037-E001", "measurement_method_inference": "ELISA / cytokine protein assay; barrier / permeability / endothelial assay", "paper_tracker_id": "M5A-P037", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T004", "tracker_id": "M5B-O037"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P037::M5A-P037-E001'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'relay plasticity / circuit reconstruction'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O037', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P038-E001 confirms the curated Combined GlcNAc6ST1/Chst2 and GlcNAc6ST4/Chst7 deficiency experiment in Mouse. Methods/readouts recorded in the A-layer: Double-KO mice, but not either single KO, showed significantly improved BMS recovery from week 4 through week 8, with greater white-matter preservation and increased 5-HT-positive fibers rostral and caudal to the lesion.',
    'qualitative',
    'genetic perturbation / knockdown assay; behavioral / functional recovery assay',
    'Full-text source localization for M5A-P038-E001 confirms the curated Combined GlcNAc6ST1/Chst2 and GlcNAc6ST4/Chst7 deficiency experiment in Mouse. Methods/readouts recorded in the A-layer: Double-KO mice, but not either single KO, showed significantly improved BMS recovery from week 4 through week 8, with greater white-matter preservation and increased 5-HT-positive fibers rostral and caudal to the lesion.',
    'full-text source localization for m5a-p038-e001 confirms the curated combined glcnac6st1/chst2 and glcnac6st4/chst7 deficiency experiment in mouse. methods/readouts recorded in the a-layer: double-ko mice, but not either single ko, showed significantly improved bms recovery from week 4 through week 8, with greater white-matter preservation and increased 5-ht-positive fibers rostral and caudal to the lesion.',
    'Module 5A full-text extraction; Full text PMC; Fig. 1-3',
    'A-layer full text; Full text PMC; Fig. 1-3',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P038-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P038-E001", "measurement_method_inference": "genetic perturbation / knockdown assay; behavioral / functional recovery assay", "paper_tracker_id": "M5A-P038", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T004", "tracker_id": "M5B-O038"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P038::M5A-P038-E001'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'relay plasticity / circuit reconstruction'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O038', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Zhao Q 2025 contributes corticospinal tract regeneration / sprouting evidence in human / translational context, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'qualitative',
    'pathway activity / phospho-signaling assay; behavioral / functional recovery assay',
    'Zhao Q 2025 contributes corticospinal tract regeneration / sprouting evidence in human / translational context, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'zhao q 2025 contributes corticospinal tract regeneration / sprouting evidence in human / translational context, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'Module 5A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'medium',
    '{"curator_notes": "Primary title: Treadmill exercise supplemented by OPN promote axon regeneration through the IGF-1R/Akt/mTOR signaling pathway.. Note: Corticospinal tract regeneration / sprouting anchor.", "experiment_tracker_id": "M5A-P039-E001", "measurement_method_inference": "pathway activity / phospho-signaling assay; behavioral / functional recovery assay", "paper_tracker_id": "M5A-P039", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M5B-T007", "tracker_id": "M5B-O039"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P039::M5A-P039-E001'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'tract regeneration / sprouting / recovery'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O039', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P040-E001 confirms the curated AAV9-SPP1-GFP injected into right sensorimotor cortex 2 weeks before injury; treadmill at 50% maximum speed 5 times weekly for 30 min from 1 week post-injury experiment in Mouse cervical SCI model. Methods/readouts recorded in the A-layer: OPN plus treadmill training produced the strongest functional improvement, amplified cortical mTOR signaling and IGF-1 receptor expression, attenuated CST dieback, and enabled limited CST axon regeneration up to 2 mm caudal to the lesion. Exercise or OPN alone did not produce the same lesion-crossing CST result.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Full-text source localization for M5A-P040-E001 confirms the curated AAV9-SPP1-GFP injected into right sensorimotor cortex 2 weeks before injury; treadmill at 50% maximum speed 5 times weekly for 30 min from 1 week post-injury experiment in Mouse cervical SCI model. Methods/readouts recorded in the A-layer: OPN plus treadmill training produced the strongest functional improvement, amplified cortical mTOR signaling and IGF-1 receptor expression, attenuated CST dieback, and enabled limited CST axon regeneration up to 2 mm caudal to the lesion. Exercise or OPN alone did not produce the same lesion-crossing CST result.',
    'full-text source localization for m5a-p040-e001 confirms the curated aav9-spp1-gfp injected into right sensorimotor cortex 2 weeks before injury; treadmill at 50% maximum speed 5 times weekly for 30 min from 1 week post-injury experiment in mouse cervical sci model. methods/readouts recorded in the a-layer: opn plus treadmill training produced the strongest functional improvement, amplified cortical mtor signaling and igf-1 receptor expression, attenuated cst dieback, and enabled limited cst axon regeneration up to 2 mm caudal to the lesion. exercise or opn alone did not produce the same lesion-crossing cst result.',
    'Module 5A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P040-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P040-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P040", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T007", "tracker_id": "M5B-O040"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P040::M5A-P040-E001'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'tract regeneration / sprouting / recovery'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O040', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P041-E001 confirms the curated Human DPSCs infected with adenovirus encoding OPN, IGF-1, and CNTF, 1 x 10^5 cells per site at four in situ sites experiment in Mouse SCI model with human dental pulp stem-cell grafts. Methods/readouts recorded in the A-layer: DPSC-OIC grafts improved BMS recovery, MRI appearance, and bladder function; reduced cleaved caspase-3, increased Ki-67 and Nestin/Sox2-associated progenitor signals, reduced NG2, and increased fibronectin. Transplanted cells remained detectable for about 2 weeks.',
    'qualitative',
    'MRI / imaging assay; behavioral / functional recovery assay',
    'Full-text source localization for M5A-P041-E001 confirms the curated Human DPSCs infected with adenovirus encoding OPN, IGF-1, and CNTF, 1 x 10^5 cells per site at four in situ sites experiment in Mouse SCI model with human dental pulp stem-cell grafts. Methods/readouts recorded in the A-layer: DPSC-OIC grafts improved BMS recovery, MRI appearance, and bladder function; reduced cleaved caspase-3, increased Ki-67 and Nestin/Sox2-associated progenitor signals, reduced NG2, and increased fibronectin. Transplanted cells remained detectable for about 2 weeks.',
    'full-text source localization for m5a-p041-e001 confirms the curated human dpscs infected with adenovirus encoding opn, igf-1, and cntf, 1 x 10^5 cells per site at four in situ sites experiment in mouse sci model with human dental pulp stem-cell grafts. methods/readouts recorded in the a-layer: dpsc-oic grafts improved bms recovery, mri appearance, and bladder function; reduced cleaved caspase-3, increased ki-67 and nestin/sox2-associated progenitor signals, reduced ng2, and increased fibronectin. transplanted cells remained detectable for about 2 weeks.',
    'Module 5A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P041-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P041-E001", "measurement_method_inference": "MRI / imaging assay; behavioral / functional recovery assay", "paper_tracker_id": "M5A-P041", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T006", "tracker_id": "M5B-O041"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P041::M5A-P041-E001'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'Graft/scaffold-enabled axon repair'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O041', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P042-E001 confirms the curated GM-RA4IV bioactive hydrogel, parallel-channel GM-3Dpro scaffold, and local PTEN-siRNA lipid nanoparticles experiment in Rat. Methods/readouts recorded in the A-layer: GM-RA4IV reduced cavity area, reactive astrocytes and myeloid markers while increasing axon, 5-HT, and NF200 density. The combined siRNA@LNP plus GM-3Dpro group produced the best BBB, stride, body-support and EMG outcomes, consistent with combined PTEN knockdown and physical guidance.',
    'qualitative',
    'barrier / permeability / endothelial assay; genetic perturbation / knockdown assay',
    'Full-text source localization for M5A-P042-E001 confirms the curated GM-RA4IV bioactive hydrogel, parallel-channel GM-3Dpro scaffold, and local PTEN-siRNA lipid nanoparticles experiment in Rat. Methods/readouts recorded in the A-layer: GM-RA4IV reduced cavity area, reactive astrocytes and myeloid markers while increasing axon, 5-HT, and NF200 density. The combined siRNA@LNP plus GM-3Dpro group produced the best BBB, stride, body-support and EMG outcomes, consistent with combined PTEN knockdown and physical guidance.',
    'full-text source localization for m5a-p042-e001 confirms the curated gm-ra4iv bioactive hydrogel, parallel-channel gm-3dpro scaffold, and local pten-sirna lipid nanoparticles experiment in rat. methods/readouts recorded in the a-layer: gm-ra4iv reduced cavity area, reactive astrocytes and myeloid markers while increasing axon, 5-ht, and nf200 density. the combined sirna@lnp plus gm-3dpro group produced the best bbb, stride, body-support and emg outcomes, consistent with combined pten knockdown and physical guidance.',
    'Module 5A full-text extraction; Full text PMC; Fig. 4-6',
    'A-layer full text; Full text PMC; Fig. 4-6',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P042-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P042-E001", "measurement_method_inference": "barrier / permeability / endothelial assay; genetic perturbation / knockdown assay", "paper_tracker_id": "M5A-P042", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T006", "tracker_id": "M5B-O042"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P042::M5A-P042-E001'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'Graft/scaffold-enabled axon repair'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O042', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P043-E001 confirms the curated GET peptide-siRNA nanoparticles delivered PTEN siRNA into primary neurons and were incorporated into an aligned hyaluronic-acid scaffold containing collagen IV and fibronectin; delivery was assessed in monolayer, 3D culture, and chick brain explants. experiment in Primary cortical neurons plus chick brain explant. Methods/readouts recorded in the A-layer: Full-text evidence is in vitro/ex vivo platform validation, not an in vivo SCI treatment experiment.',
    'qualitative',
    'genetic perturbation / knockdown assay',
    'Full-text source localization for M5A-P043-E001 confirms the curated GET peptide-siRNA nanoparticles delivered PTEN siRNA into primary neurons and were incorporated into an aligned hyaluronic-acid scaffold containing collagen IV and fibronectin; delivery was assessed in monolayer, 3D culture, and chick brain explants. experiment in Primary cortical neurons plus chick brain explant. Methods/readouts recorded in the A-layer: Full-text evidence is in vitro/ex vivo platform validation, not an in vivo SCI treatment experiment.',
    'full-text source localization for m5a-p043-e001 confirms the curated get peptide-sirna nanoparticles delivered pten sirna into primary neurons and were incorporated into an aligned hyaluronic-acid scaffold containing collagen iv and fibronectin; delivery was assessed in monolayer, 3d culture, and chick brain explants. experiment in primary cortical neurons plus chick brain explant. methods/readouts recorded in the a-layer: full-text evidence is in vitro/ex vivo platform validation, not an in vivo sci treatment experiment.',
    'Module 5A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P043-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P043-E001", "measurement_method_inference": "genetic perturbation / knockdown assay", "paper_tracker_id": "M5A-P043", "quantitative": "YES", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T005", "tracker_id": "M5B-O043"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P043::M5A-P043-E001'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'intrinsic growth competence'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O043', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P044-E001 confirms the curated Cited2 was active in immature and regenerating DRG neurons but silent after non-regenerative SCI; neuronal Cited2 overexpression reinstated developmental growth-associated transcriptional and epigenetic signatures, with RNA-seq, ATAC-seq and CUT&Tag support. experiment in Mouse SCI model plus cultured DRG neurons. Methods/readouts recorded in the A-layer: Full-text methods correct the first-pass rat placeholder and show that the core mechanistic work is in mouse DRG/SCI systems.',
    'qualitative',
    'qPCR / RT-PCR / mRNA assay; bulk transcriptomics / GEO dataset',
    'Full-text source localization for M5A-P044-E001 confirms the curated Cited2 was active in immature and regenerating DRG neurons but silent after non-regenerative SCI; neuronal Cited2 overexpression reinstated developmental growth-associated transcriptional and epigenetic signatures, with RNA-seq, ATAC-seq and CUT&Tag support. experiment in Mouse SCI model plus cultured DRG neurons. Methods/readouts recorded in the A-layer: Full-text methods correct the first-pass rat placeholder and show that the core mechanistic work is in mouse DRG/SCI systems.',
    'full-text source localization for m5a-p044-e001 confirms the curated cited2 was active in immature and regenerating drg neurons but silent after non-regenerative sci; neuronal cited2 overexpression reinstated developmental growth-associated transcriptional and epigenetic signatures, with rna-seq, atac-seq and cut&tag support. experiment in mouse sci model plus cultured drg neurons. methods/readouts recorded in the a-layer: full-text methods correct the first-pass rat placeholder and show that the core mechanistic work is in mouse drg/sci systems.',
    'Module 5A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P044-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P044-E001", "measurement_method_inference": "qPCR / RT-PCR / mRNA assay; bulk transcriptomics / GEO dataset", "paper_tracker_id": "M5A-P044", "quantitative": "YES", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T005", "tracker_id": "M5B-O044"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P044::M5A-P044-E001'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'intrinsic growth competence'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O044', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P045-E001 confirms the curated Poly-L-ornithine-coated lignocellulosic plant scaffold, 100 microgram/ml coating experiment in Rat. Methods/readouts recorded in the A-layer: PLO-coated scaffolds supported host-cell migration and vascularization, increased BBB and swim-score recovery over time, and outperformed no-scaffold and generally uncoated-scaffold groups. The study supports bridge-associated repair, not complete restoration of locomotion.',
    'qualitative',
    'barrier / permeability / endothelial assay; behavioral / functional recovery assay',
    'Full-text source localization for M5A-P045-E001 confirms the curated Poly-L-ornithine-coated lignocellulosic plant scaffold, 100 microgram/ml coating experiment in Rat. Methods/readouts recorded in the A-layer: PLO-coated scaffolds supported host-cell migration and vascularization, increased BBB and swim-score recovery over time, and outperformed no-scaffold and generally uncoated-scaffold groups. The study supports bridge-associated repair, not complete restoration of locomotion.',
    'full-text source localization for m5a-p045-e001 confirms the curated poly-l-ornithine-coated lignocellulosic plant scaffold, 100 microgram/ml coating experiment in rat. methods/readouts recorded in the a-layer: plo-coated scaffolds supported host-cell migration and vascularization, increased bbb and swim-score recovery over time, and outperformed no-scaffold and generally uncoated-scaffold groups. the study supports bridge-associated repair, not complete restoration of locomotion.',
    'Module 5A full-text extraction; Full text PMC; Fig. 1-2',
    'A-layer full text; Full text PMC; Fig. 1-2',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P045-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P045-E001", "measurement_method_inference": "barrier / permeability / endothelial assay; behavioral / functional recovery assay", "paper_tracker_id": "M5A-P045", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T006", "tracker_id": "M5B-O045"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P045::M5A-P045-E001'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'Graft/scaffold-enabled axon repair'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O045', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P046-E001 confirms the curated 10X scRNA-seq, Visium spatial transcriptomics, and mass-spectrometry-imaging spatial metabolomics on separate biological samples experiment in Rat. Methods/readouts recorded in the A-layer: Across 35,799 cells, the atlas identified Mic2 microglia, Mac4 macrophages, and Fib4 fibroblasts as repair-associated subsets. Mic2 localized mainly to dorsal white matter and was enriched for wound-healing markers and taurine; Mac4 formed clusters associated with copalic acid; Fib4 localized around the injured cord, expressed Igf2, and was associated with uridine and Upp1/Nt5e/Uck1 metabolism. The study is spatially and molecularly informative but primarily descriptive: no Mic2, taurine, Mac4, copalic acid, Fib4, or uridine perturbation proves necessity, and scRNA-seq lacked neuronal information.',
    'qualitative',
    'single-cell RNA-seq / cell-state atlas; spatial transcriptomics / spatial atlas; MRI / imaging assay',
    'Full-text source localization for M5A-P046-E001 confirms the curated 10X scRNA-seq, Visium spatial transcriptomics, and mass-spectrometry-imaging spatial metabolomics on separate biological samples experiment in Rat. Methods/readouts recorded in the A-layer: Across 35,799 cells, the atlas identified Mic2 microglia, Mac4 macrophages, and Fib4 fibroblasts as repair-associated subsets. Mic2 localized mainly to dorsal white matter and was enriched for wound-healing markers and taurine; Mac4 formed clusters associated with copalic acid; Fib4 localized around the injured cord, expressed Igf2, and was associated with uridine and Upp1/Nt5e/Uck1 metabolism. The study is spatially and molecularly informative but primarily descriptive: no Mic2, taurine, Mac4, copalic acid, Fib4, or uridine perturbation proves necessity, and scRNA-seq lacked neuronal information.',
    'full-text source localization for m5a-p046-e001 confirms the curated 10x scrna-seq, visium spatial transcriptomics, and mass-spectrometry-imaging spatial metabolomics on separate biological samples experiment in rat. methods/readouts recorded in the a-layer: across 35,799 cells, the atlas identified mic2 microglia, mac4 macrophages, and fib4 fibroblasts as repair-associated subsets. mic2 localized mainly to dorsal white matter and was enriched for wound-healing markers and taurine; mac4 formed clusters associated with copalic acid; fib4 localized around the injured cord, expressed igf2, and was associated with uridine and upp1/nt5e/uck1 metabolism. the study is spatially and molecularly informative but primarily descriptive: no mic2, taurine, mac4, copalic acid, fib4, or uridine perturbation proves necessity, and scrna-seq lacked neuronal information.',
    'Module 5A full-text extraction; Fig. 1-6; scRNA-seq, spatial transcriptomics, and spatial metabolomics atlas',
    'A-layer full text; Fig. 1-6; scRNA-seq, spatial transcriptomics, and spatial metabolomics atlas',
    'medium',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P046-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P046-E001", "measurement_method_inference": "single-cell RNA-seq / cell-state atlas; spatial transcriptomics / spatial atlas; MRI / imaging assay", "paper_tracker_id": "M5A-P046", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T003", "tracker_id": "M5B-O046"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P046::M5A-P046-E001'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'white matter / remyelination / debris handling'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O046', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P047-E001 confirms the curated Poly laminin with GDNF in three dogs or ChABC in three dogs experiment in Dog. Methods/readouts recorded in the A-layer: Mean TSCIS rose from 2.2 to 3.2 and OFS from 1.5 to 3.1 during follow-up, with no neurological deterioration or major safety signal. The longitudinal design reduces spontaneous-recovery concern but cannot isolate treatment effects.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Full-text source localization for M5A-P047-E001 confirms the curated Poly laminin with GDNF in three dogs or ChABC in three dogs experiment in Dog. Methods/readouts recorded in the A-layer: Mean TSCIS rose from 2.2 to 3.2 and OFS from 1.5 to 3.1 during follow-up, with no neurological deterioration or major safety signal. The longitudinal design reduces spontaneous-recovery concern but cannot isolate treatment effects.',
    'full-text source localization for m5a-p047-e001 confirms the curated poly laminin with gdnf in three dogs or chabc in three dogs experiment in dog. methods/readouts recorded in the a-layer: mean tscis rose from 2.2 to 3.2 and ofs from 1.5 to 3.1 during follow-up, with no neurological deterioration or major safety signal. the longitudinal design reduces spontaneous-recovery concern but cannot isolate treatment effects.',
    'Module 5A full-text extraction; Full text PMC; prospective longitudinal trial',
    'A-layer full text; Full text PMC; prospective longitudinal trial',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P047-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P047-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P047", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T002", "tracker_id": "M5B-O047"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P047::M5A-P047-E001'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'Extrinsic inhibitory matrix / guidance pathway'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O047', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Lu P 2007 M5A-P001-E002 preserves a distinct Rat experiment testing Mechanistic outcome assessment after axon regeneration through chronic scar/graft with endpoint/readout: Outcome/mechanistic validation row for Axon regeneration through scars and into sites of chronic spinal cord injury; first-pass row captures axon regeneration through chronic scar/graft in rat at abstract/source-title level..',
    'qualitative',
    NULL,
    'Lu P 2007 M5A-P001-E002 preserves a distinct Rat experiment testing Mechanistic outcome assessment after axon regeneration through chronic scar/graft with endpoint/readout: Outcome/mechanistic validation row for Axon regeneration through scars and into sites of chronic spinal cord injury; first-pass row captures axon regeneration through chronic scar/graft in rat at abstract/source-title level..',
    'M5A-P001-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Axon regeneration through scars and into sites of chronic spinal cord injury. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M5A-P001-E002", "measurement_method_inference": null, "paper_tracker_id": "M5A-P001", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M5B-T006", "tracker_id": "M5B-O048"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P001::M5A-P001-E002'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Axon regeneration through scars and into sites of chronic spinal cord injury; first-pass row captures axon regeneration through chronic scar/graft in rat at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O048', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P002-E002 confirms the curated Attenuated pericyte-derived fibrosis experiment in Mouse. Methods/readouts recorded in the A-layer: Moderate scar attenuation enabled CST and raphespinal axons to enter and extend beyond the lesion, form synaptic and optogenetically responsive connections below the lesion, and improve sensorimotor recovery; the highest recombination caused tissue defects.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Full-text source localization for M5A-P002-E002 confirms the curated Attenuated pericyte-derived fibrosis experiment in Mouse. Methods/readouts recorded in the A-layer: Moderate scar attenuation enabled CST and raphespinal axons to enter and extend beyond the lesion, form synaptic and optogenetically responsive connections below the lesion, and improve sensorimotor recovery; the highest recombination caused tissue defects.',
    'full-text source localization for m5a-p002-e002 confirms the curated attenuated pericyte-derived fibrosis experiment in mouse. methods/readouts recorded in the a-layer: moderate scar attenuation enabled cst and raphespinal axons to enter and extend beyond the lesion, form synaptic and optogenetically responsive connections below the lesion, and improve sensorimotor recovery; the highest recombination caused tissue defects.',
    'Module 5A full-text extraction; Full text PMC; Fig. 3-5',
    'A-layer full text; Full text PMC; Fig. 3-5',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P002-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P002-E002", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P002", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T001", "tracker_id": "M5B-O049"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P002::M5A-P002-E002'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Reducing Pericyte-Derived Scarring Promotes Recovery after Spinal Cord Injury; first-pass row captures cst/rst regeneration after scar attenuation in mouse at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O049', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P003-E002 confirms the curated Astrocyte-specific Ccn1 deletion experiment in Mouse. Methods/readouts recorded in the A-layer: Ccn1-cKO accelerated and spatially mislocalized WDM nodule formation, increased intracellular myelin and axon debris while attenuating extracellular debris clearance, reduced TREM2/Gpnmb/Igf1 WDM specification and lipid-droplet buffering, and impaired cold thermoception and mechanosensory recovery. Locomotor recovery was equivalent to wild type, showing tract-specific rather than universal functional loss.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Full-text source localization for M5A-P003-E002 confirms the curated Astrocyte-specific Ccn1 deletion experiment in Mouse. Methods/readouts recorded in the A-layer: Ccn1-cKO accelerated and spatially mislocalized WDM nodule formation, increased intracellular myelin and axon debris while attenuating extracellular debris clearance, reduced TREM2/Gpnmb/Igf1 WDM specification and lipid-droplet buffering, and impaired cold thermoception and mechanosensory recovery. Locomotor recovery was equivalent to wild type, showing tract-specific rather than universal functional loss.',
    'full-text source localization for m5a-p003-e002 confirms the curated astrocyte-specific ccn1 deletion experiment in mouse. methods/readouts recorded in the a-layer: ccn1-cko accelerated and spatially mislocalized wdm nodule formation, increased intracellular myelin and axon debris while attenuating extracellular debris clearance, reduced trem2/gpnmb/igf1 wdm specification and lipid-droplet buffering, and impaired cold thermoception and mechanosensory recovery. locomotor recovery was equivalent to wild type, showing tract-specific rather than universal functional loss.',
    'Module 5A full-text extraction; Full text PMC; Fig. 2-3 and Extended Data Fig. 7-8',
    'A-layer full text; Full text PMC; Fig. 2-3 and Extended Data Fig. 7-8',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P003-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P003-E002", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P003", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T003", "tracker_id": "M5B-O050"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P003::M5A-P003-E002'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Lesion-remote astrocytes govern microglia-mediated white matter repair; first-pass row captures lesion-remote white matter repair in mouse at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O050', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P004-E002 confirms the curated Myelin thickness and g-ratio analysis experiment in Human. Methods/readouts recorded in the A-layer: Roots at or below the epicenter contained unusually thinly myelinated large fibers and increased g-ratios, supporting incomplete remyelination alongside motoneuron loss and chronic muscle denervation.',
    'qualitative',
    'immunostaining / histology / pathology',
    'Full-text source localization for M5A-P004-E002 confirms the curated Myelin thickness and g-ratio analysis experiment in Human. Methods/readouts recorded in the A-layer: Roots at or below the epicenter contained unusually thinly myelinated large fibers and increased g-ratios, supporting incomplete remyelination alongside motoneuron loss and chronic muscle denervation.',
    'full-text source localization for m5a-p004-e002 confirms the curated myelin thickness and g-ratio analysis experiment in human. methods/readouts recorded in the a-layer: roots at or below the epicenter contained unusually thinly myelinated large fibers and increased g-ratios, supporting incomplete remyelination alongside motoneuron loss and chronic muscle denervation.',
    'Module 5A full-text extraction; Full text PMC; myelin g-ratio analysis',
    'A-layer full text; Full text PMC; myelin g-ratio analysis',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P004-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P004-E002", "measurement_method_inference": "immunostaining / histology / pathology", "paper_tracker_id": "M5A-P004", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T003", "tracker_id": "M5B-O051"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P004::M5A-P004-E002'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Motoneuron Death after Human Spinal Cord Injury; first-pass row captures ventral-root axon loss/remyelination pathology in human at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O051', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P005-E002 confirms the curated Enhanced mitochondrial transport or creatine 2 g/kg by gavage experiment in Mouse. Methods/readouts recorded in the A-layer: Snph knockout promoted monoaminergic and CST regeneration, functional synapses, and skilled forelimb recovery; creatine boosted regeneration in knockout mice, and DREADD silencing tested the regenerated-CST contribution to behavior.',
    'qualitative',
    'genetic perturbation / knockdown assay; behavioral / functional recovery assay',
    'Full-text source localization for M5A-P005-E002 confirms the curated Enhanced mitochondrial transport or creatine 2 g/kg by gavage experiment in Mouse. Methods/readouts recorded in the A-layer: Snph knockout promoted monoaminergic and CST regeneration, functional synapses, and skilled forelimb recovery; creatine boosted regeneration in knockout mice, and DREADD silencing tested the regenerated-CST contribution to behavior.',
    'full-text source localization for m5a-p005-e002 confirms the curated enhanced mitochondrial transport or creatine 2 g/kg by gavage experiment in mouse. methods/readouts recorded in the a-layer: snph knockout promoted monoaminergic and cst regeneration, functional synapses, and skilled forelimb recovery; creatine boosted regeneration in knockout mice, and dreadd silencing tested the regenerated-cst contribution to behavior.',
    'Module 5A full-text extraction; Full text PMC; T8 transection and creatine/DREADD assays',
    'A-layer full text; Full text PMC; T8 transection and creatine/DREADD assays',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P005-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P005-E002", "measurement_method_inference": "genetic perturbation / knockdown assay; behavioral / functional recovery assay", "paper_tracker_id": "M5A-P005", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T005", "tracker_id": "M5B-O052"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P005::M5A-P005-E002'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Restoring Cellular Energetics Promotes Axonal Regeneration and Functional Recovery after Spinal Cord Injury; first-pass row captures axonal regeneration / cellular energetics in rodent model context at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O052', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Fry EJ 2010 M5A-P006-E002 preserves a distinct Mouse experiment testing Mechanistic outcome assessment after cst regeneration / receptor ptp sigma with endpoint/readout: Outcome/mechanistic validation row for Corticospinal tract regeneration after spinal cord injury in receptor protein tyrosine phosphatase sigma deficient mice; first-pass row captures cst regeneration / receptor ptp sigma in mouse at abstract/source-title level..',
    'qualitative',
    'genetic perturbation / knockdown assay',
    'Fry EJ 2010 M5A-P006-E002 preserves a distinct Mouse experiment testing Mechanistic outcome assessment after cst regeneration / receptor ptp sigma with endpoint/readout: Outcome/mechanistic validation row for Corticospinal tract regeneration after spinal cord injury in receptor protein tyrosine phosphatase sigma deficient mice; first-pass row captures cst regeneration / receptor ptp sigma in mouse at abstract/source-title level..',
    'M5A-P006-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Corticospinal tract regeneration after spinal cord injury in receptor protein tyrosine phosphatase sigma deficient mice. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M5A-P006-E002", "measurement_method_inference": "genetic perturbation / knockdown assay", "paper_tracker_id": "M5A-P006", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M5B-T001", "tracker_id": "M5B-O053"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P006::M5A-P006-E002'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Corticospinal tract regeneration after spinal cord injury in receptor protein tyrosine phosphatase sigma deficient mice; first-pass row captures cst regeneration / receptor ptp sigma in mouse at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O053', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P007-E002 confirms the curated Homologous spinal NPC graft for relay formation experiment in Rat. Methods/readouts recorded in the A-layer: Smaller grafts allowed some CST axons to cross the caudal host-graft interface; regenerated CST axons formed functional glutamatergic EPSCs in graft neurons, supporting a graft-mediated relay rather than axon presence alone.',
    'qualitative',
    NULL,
    'Full-text source localization for M5A-P007-E002 confirms the curated Homologous spinal NPC graft for relay formation experiment in Rat. Methods/readouts recorded in the A-layer: Smaller grafts allowed some CST axons to cross the caudal host-graft interface; regenerated CST axons formed functional glutamatergic EPSCs in graft neurons, supporting a graft-mediated relay rather than axon presence alone.',
    'full-text source localization for m5a-p007-e002 confirms the curated homologous spinal npc graft for relay formation experiment in rat. methods/readouts recorded in the a-layer: smaller grafts allowed some cst axons to cross the caudal host-graft interface; regenerated cst axons formed functional glutamatergic epscs in graft neurons, supporting a graft-mediated relay rather than axon presence alone.',
    'Module 5A full-text extraction; Full text PMC; Fig. 2-3',
    'A-layer full text; Full text PMC; Fig. 2-3',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P007-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P007-E002", "measurement_method_inference": null, "paper_tracker_id": "M5A-P007", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T006", "tracker_id": "M5B-O054"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P007::M5A-P007-E002'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Spinal cord reconstitution with homologous neural grafts enables robust corticospinal regeneration; first-pass row captures neural graft-enabled cst regeneration in rat at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O054', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Poplawski GHD 2020 M5A-P008-E002 preserves a distinct Mouse experiment testing Mechanistic outcome assessment after intrinsic neuronal growth state with endpoint/readout: Outcome/mechanistic validation row for Injured adult neurons regress to an embryonic transcriptional growth state; first-pass row captures intrinsic neuronal growth state in mouse at abstract/source-title level..',
    'qualitative',
    'qPCR / RT-PCR / mRNA assay',
    'Poplawski GHD 2020 M5A-P008-E002 preserves a distinct Mouse experiment testing Mechanistic outcome assessment after intrinsic neuronal growth state with endpoint/readout: Outcome/mechanistic validation row for Injured adult neurons regress to an embryonic transcriptional growth state; first-pass row captures intrinsic neuronal growth state in mouse at abstract/source-title level..',
    'M5A-P008-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Injured adult neurons regress to an embryonic transcriptional growth state. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M5A-P008-E002", "measurement_method_inference": "qPCR / RT-PCR / mRNA assay", "paper_tracker_id": "M5A-P008", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M5B-T005", "tracker_id": "M5B-O055"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P008::M5A-P008-E002'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Injured adult neurons regress to an embryonic transcriptional growth state; first-pass row captures intrinsic neuronal growth state in mouse at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O055', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Boato F 2023 M5A-P009-E002 preserves a distinct Rodent model context experiment testing Mechanistic outcome assessment after cst sprouting/regeneration with endpoint/readout: Outcome/mechanistic validation row for Activation of MAP2K signaling by genetic engineering or HF-rTMS promotes corticospinal axon sprouting and functional regeneration; first-pass row captures cst sprouting/regeneration in rodent model context at abstract/source-title level..',
    'qualitative',
    NULL,
    'Boato F 2023 M5A-P009-E002 preserves a distinct Rodent model context experiment testing Mechanistic outcome assessment after cst sprouting/regeneration with endpoint/readout: Outcome/mechanistic validation row for Activation of MAP2K signaling by genetic engineering or HF-rTMS promotes corticospinal axon sprouting and functional regeneration; first-pass row captures cst sprouting/regeneration in rodent model context at abstract/source-title level..',
    'M5A-P009-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Activation of MAP2K signaling by genetic engineering or HF-rTMS promotes corticospinal axon sprouting and functional regeneration. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M5A-P009-E002", "measurement_method_inference": null, "paper_tracker_id": "M5A-P009", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M5B-T001", "tracker_id": "M5B-O056"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P009::M5A-P009-E002'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Activation of MAP2K signaling by genetic engineering or HF-rTMS promotes corticospinal axon sprouting and functional regeneration; first-pass row captures cst sprouting/regeneration in rodent model context at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O056', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P010-E002 confirms the curated FLLL31 STAT3-phosphorylation inhibitor in stimulated ChR2+ slices experiment in ChR2-YFP cortical slices and mouse SCI model. Methods/readouts recorded in the A-layer: Blue light increased ChR2-specific neurite number/length and in vivo cortical p-JAK2/p-STAT3; FLLL31 attenuated stimulated neurite outgrowth, supporting pathway involvement but not proving in vivo JAK2/STAT3 necessity.',
    'qualitative',
    'pathway activity / phospho-signaling assay',
    'Full-text source localization for M5A-P010-E002 confirms the curated FLLL31 STAT3-phosphorylation inhibitor in stimulated ChR2+ slices experiment in ChR2-YFP cortical slices and mouse SCI model. Methods/readouts recorded in the A-layer: Blue light increased ChR2-specific neurite number/length and in vivo cortical p-JAK2/p-STAT3; FLLL31 attenuated stimulated neurite outgrowth, supporting pathway involvement but not proving in vivo JAK2/STAT3 necessity.',
    'full-text source localization for m5a-p010-e002 confirms the curated flll31 stat3-phosphorylation inhibitor in stimulated chr2+ slices experiment in chr2-yfp cortical slices and mouse sci model. methods/readouts recorded in the a-layer: blue light increased chr2-specific neurite number/length and in vivo cortical p-jak2/p-stat3; flll31 attenuated stimulated neurite outgrowth, supporting pathway involvement but not proving in vivo jak2/stat3 necessity.',
    'Module 5A full-text extraction; Full text PMC; Fig. 2, 5-6',
    'A-layer full text; Full text PMC; Fig. 2, 5-6',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P010-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P010-E002", "measurement_method_inference": "pathway activity / phospho-signaling assay", "paper_tracker_id": "M5A-P010", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T007", "tracker_id": "M5B-O057"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P010::M5A-P010-E002'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Transcranial Optogenetic Stimulation Promotes Corticospinal Tract Axon Regeneration to Repair Spinal Cord Injury by Activating the JAK2/STAT3 Pathway.; first-pass row captures corticospinal tract regeneration / sprouting in mouse sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O057', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P011-E002 confirms the curated Lipin1 knockdown or PA/LPA delivery; mTOR and STAT3 conditional deletion for mechanism testing experiment in Mouse retinal, cortical, DRG, and SCI validation models. Methods/readouts recorded in the A-layer: Lipin1 knockdown increased PA and LPA and activated mTOR and/or STAT3 in neuronal models. mTOR or STAT3 loss reduced lipin1-KD-induced regeneration, while DRG lipin1 knockdown promoted ascending sensory axon growth through the lesion.',
    'qualitative',
    NULL,
    'Full-text source localization for M5A-P011-E002 confirms the curated Lipin1 knockdown or PA/LPA delivery; mTOR and STAT3 conditional deletion for mechanism testing experiment in Mouse retinal, cortical, DRG, and SCI validation models. Methods/readouts recorded in the A-layer: Lipin1 knockdown increased PA and LPA and activated mTOR and/or STAT3 in neuronal models. mTOR or STAT3 loss reduced lipin1-KD-induced regeneration, while DRG lipin1 knockdown promoted ascending sensory axon growth through the lesion.',
    'full-text source localization for m5a-p011-e002 confirms the curated lipin1 knockdown or pa/lpa delivery; mtor and stat3 conditional deletion for mechanism testing experiment in mouse retinal, cortical, drg, and sci validation models. methods/readouts recorded in the a-layer: lipin1 knockdown increased pa and lpa and activated mtor and/or stat3 in neuronal models. mtor or stat3 loss reduced lipin1-kd-induced regeneration, while drg lipin1 knockdown promoted ascending sensory axon growth through the lesion.',
    'Module 5A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P011-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P011-E002", "measurement_method_inference": null, "paper_tracker_id": "M5A-P011", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T005", "tracker_id": "M5B-O058"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P011::M5A-P011-E002'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Lipin1 depletion coordinates neuronal signaling pathways to promote motor and sensory axon regeneration after spinal cord injury.; first-pass row captures corticospinal tract regeneration / sprouting in rat sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O058', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Hu M 2024 M5A-P012-E002 preserves a distinct Rat SCI model experiment testing Mechanistic outcome assessment after activity or stimulation-enabled axon repair with endpoint/readout: Outcome/mechanistic validation row for Effects of transcranial magnetic stimulation on axonal regeneration in the corticospinal tract of female rats with spinal cord injury.; first-pass row captures activity or stimulation-enabled axon repair in rat sci model at abstract/source-title level..',
    'qualitative',
    NULL,
    'Hu M 2024 M5A-P012-E002 preserves a distinct Rat SCI model experiment testing Mechanistic outcome assessment after activity or stimulation-enabled axon repair with endpoint/readout: Outcome/mechanistic validation row for Effects of transcranial magnetic stimulation on axonal regeneration in the corticospinal tract of female rats with spinal cord injury.; first-pass row captures activity or stimulation-enabled axon repair in rat sci model at abstract/source-title level..',
    'M5A-P012-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Effects of transcranial magnetic stimulation on axonal regeneration in the corticospinal tract of female rats with spinal cord injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M5A-P012-E002", "measurement_method_inference": null, "paper_tracker_id": "M5A-P012", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M5B-T007", "tracker_id": "M5B-O059"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P012::M5A-P012-E002'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Effects of transcranial magnetic stimulation on axonal regeneration in the corticospinal tract of female rats with spinal cord injury.; first-pass row captures activity or stimulation-enabled axon repair in rat sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O059', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P013-E002 confirms the curated AAV9-shSyt4, control shRNA, Syt4 overexpression, or control vector injected into hindlimb motor cortex experiment in Mouse SCI model. Methods/readouts recorded in the A-layer: Cortical Syt4 knockdown reduced CST collateral sprouting and worsened ladder-walking hindlimb errors after SCI, whereas the paper’s central comparison supports endogenous Syt4 as necessary for spontaneous CST sprouting and neurological recovery.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Full-text source localization for M5A-P013-E002 confirms the curated AAV9-shSyt4, control shRNA, Syt4 overexpression, or control vector injected into hindlimb motor cortex experiment in Mouse SCI model. Methods/readouts recorded in the A-layer: Cortical Syt4 knockdown reduced CST collateral sprouting and worsened ladder-walking hindlimb errors after SCI, whereas the paper’s central comparison supports endogenous Syt4 as necessary for spontaneous CST sprouting and neurological recovery.',
    'full-text source localization for m5a-p013-e002 confirms the curated aav9-shsyt4, control shrna, syt4 overexpression, or control vector injected into hindlimb motor cortex experiment in mouse sci model. methods/readouts recorded in the a-layer: cortical syt4 knockdown reduced cst collateral sprouting and worsened ladder-walking hindlimb errors after sci, whereas the paper’s central comparison supports endogenous syt4 as necessary for spontaneous cst sprouting and neurological recovery.',
    'Module 5A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P013-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P013-E002", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P013", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T001", "tracker_id": "M5B-O060"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P013::M5A-P013-E002'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Synaptotagmin 4 Supports Spontaneous Axon Sprouting after Spinal Cord Injury.; first-pass row captures corticospinal tract regeneration / sprouting in experimental sci model context at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O060', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P014-E002 confirms the curated Gabapentin as above; transient hM4D-mediated silencing of injured CST projections experiment in Mouse SCI model with optogenetic and chemogenetic validation. Methods/readouts recorded in the A-layer: Silencing the regenerated or reorganized CST projections with CNO abolished gabapentin-associated forelimb recovery, supporting a causal role for CST circuit reorganization. Gabapentin’s repair effect was interpreted as alpha2delta2 blockade-linked plasticity rather than only analgesia.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Full-text source localization for M5A-P014-E002 confirms the curated Gabapentin as above; transient hM4D-mediated silencing of injured CST projections experiment in Mouse SCI model with optogenetic and chemogenetic validation. Methods/readouts recorded in the A-layer: Silencing the regenerated or reorganized CST projections with CNO abolished gabapentin-associated forelimb recovery, supporting a causal role for CST circuit reorganization. Gabapentin’s repair effect was interpreted as alpha2delta2 blockade-linked plasticity rather than only analgesia.',
    'full-text source localization for m5a-p014-e002 confirms the curated gabapentin as above; transient hm4d-mediated silencing of injured cst projections experiment in mouse sci model with optogenetic and chemogenetic validation. methods/readouts recorded in the a-layer: silencing the regenerated or reorganized cst projections with cno abolished gabapentin-associated forelimb recovery, supporting a causal role for cst circuit reorganization. gabapentin’s repair effect was interpreted as alpha2delta2 blockade-linked plasticity rather than only analgesia.',
    'Module 5A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P014-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P014-E002", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P014", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T001", "tracker_id": "M5B-O061"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P014::M5A-P014-E002'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Gabapentinoid treatment promotes corticospinal plasticity and regeneration following murine spinal cord injury.; first-pass row captures corticospinal tract regeneration / sprouting in mouse sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O061', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P015-E002 confirms the curated AAV alpha9-V5 plus kindlin-1-GFP; DRG injection and tissue-clearing or light-sheet analysis experiment in Rat sensory SCI model with tract and bridge validation. Methods/readouts recorded in the A-layer: Regenerating alpha9-kindlin axons crossed the lesion through laminin-111 and tenascin-C-positive connective bridges, extended toward high cervical segments, and formed rostral and caudal collateral branches. The study supports a sensory-pathway repair strategy, not direct motor CST regeneration.',
    'qualitative',
    NULL,
    'Full-text source localization for M5A-P015-E002 confirms the curated AAV alpha9-V5 plus kindlin-1-GFP; DRG injection and tissue-clearing or light-sheet analysis experiment in Rat sensory SCI model with tract and bridge validation. Methods/readouts recorded in the A-layer: Regenerating alpha9-kindlin axons crossed the lesion through laminin-111 and tenascin-C-positive connective bridges, extended toward high cervical segments, and formed rostral and caudal collateral branches. The study supports a sensory-pathway repair strategy, not direct motor CST regeneration.',
    'full-text source localization for m5a-p015-e002 confirms the curated aav alpha9-v5 plus kindlin-1-gfp; drg injection and tissue-clearing or light-sheet analysis experiment in rat sensory sci model with tract and bridge validation. methods/readouts recorded in the a-layer: regenerating alpha9-kindlin axons crossed the lesion through laminin-111 and tenascin-c-positive connective bridges, extended toward high cervical segments, and formed rostral and caudal collateral branches. the study supports a sensory-pathway repair strategy, not direct motor cst regeneration.',
    'Module 5A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P015-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P015-E002", "measurement_method_inference": null, "paper_tracker_id": "M5A-P015", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T002", "tracker_id": "M5B-O062"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P015::M5A-P015-E002'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Activated alpha 9 integrin expression enables sensory pathway reconstruction after spinal cord injury.; first-pass row captures extrinsic inhibitory matrix / guidance pathway in rat sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O062', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P016-E002 confirms the curated AAV8/AAVretro targeting of C5-projecting CST neurons, RhoA/Pten conditional deletion, and hM3Dq activation by DCZ experiment in Mouse cervical SCI model with pathway and circuit validation. Methods/readouts recorded in the A-layer: Stimulation increased c-Fos activation in targeted corticospinal neurons, suppressed CST dieback, increased collateral projections and presynaptic boutons in spinal gray matter, and improved skilled forelimb behavior. The combined intervention supports circuit rewiring rather than simple lesion-site axon passage.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Full-text source localization for M5A-P016-E002 confirms the curated AAV8/AAVretro targeting of C5-projecting CST neurons, RhoA/Pten conditional deletion, and hM3Dq activation by DCZ experiment in Mouse cervical SCI model with pathway and circuit validation. Methods/readouts recorded in the A-layer: Stimulation increased c-Fos activation in targeted corticospinal neurons, suppressed CST dieback, increased collateral projections and presynaptic boutons in spinal gray matter, and improved skilled forelimb behavior. The combined intervention supports circuit rewiring rather than simple lesion-site axon passage.',
    'full-text source localization for m5a-p016-e002 confirms the curated aav8/aavretro targeting of c5-projecting cst neurons, rhoa/pten conditional deletion, and hm3dq activation by dcz experiment in mouse cervical sci model with pathway and circuit validation. methods/readouts recorded in the a-layer: stimulation increased c-fos activation in targeted corticospinal neurons, suppressed cst dieback, increased collateral projections and presynaptic boutons in spinal gray matter, and improved skilled forelimb behavior. the combined intervention supports circuit rewiring rather than simple lesion-site axon passage.',
    'Module 5A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P016-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P016-E002", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P016", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T001", "tracker_id": "M5B-O063"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P016::M5A-P016-E002'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Modulation of Extrinsic and Intrinsic Signaling Together with Neuronal Activation Enhances Forelimb Motor Recovery after Cervical Spinal Cord Injury.; first-pass row captures corticospinal tract regeneration / sprouting in mouse sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O063', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P017-E002 confirms the curated Intracortical thiorphan infusion, 100 mM at 0.25 microliters/hour for 4 weeks, with or without E14 spinal-cord NPC graft into lesion cavity experiment in Rat. Methods/readouts recorded in the A-layer: Adult rats received delayed continuous thiorphan infusion into left motor cortex because thiorphan does not cross the blood-brain barrier, with NPC grafting at 2 weeks post-injury. Thiorphan plus NPC graft produced a significant twofold forelimb pellet-retrieval success improvement versus lesion control (P=0.005), improved accuracy to 60% versus 30% (P=0.001), and increased corticospinal axon regeneration into the graft by 60% versus graft alone (P<0.05), with putative synaptophysin-apposed host axon/graft-neuron contacts. Thiorphan alone and NPC graft alone trended but were not significant; there was no significant change in CST sprouting above the lesion, serotonergic or CGRP axons into graft, GFAP border, graft differentiation, or graft-derived axon extension. The study supports substrate-dependent CST regeneration and functional benefit, not complete circuit restoration.',
    'qualitative',
    'barrier / permeability / endothelial assay; behavioral / functional recovery assay',
    'Full-text source localization for M5A-P017-E002 confirms the curated Intracortical thiorphan infusion, 100 mM at 0.25 microliters/hour for 4 weeks, with or without E14 spinal-cord NPC graft into lesion cavity experiment in Rat. Methods/readouts recorded in the A-layer: Adult rats received delayed continuous thiorphan infusion into left motor cortex because thiorphan does not cross the blood-brain barrier, with NPC grafting at 2 weeks post-injury. Thiorphan plus NPC graft produced a significant twofold forelimb pellet-retrieval success improvement versus lesion control (P=0.005), improved accuracy to 60% versus 30% (P=0.001), and increased corticospinal axon regeneration into the graft by 60% versus graft alone (P<0.05), with putative synaptophysin-apposed host axon/graft-neuron contacts. Thiorphan alone and NPC graft alone trended but were not significant; there was no significant change in CST sprouting above the lesion, serotonergic or CGRP axons into graft, GFAP border, graft differentiation, or graft-derived axon extension. The study supports substrate-dependent CST regeneration and functional benefit, not complete circuit restoration.',
    'full-text source localization for m5a-p017-e002 confirms the curated intracortical thiorphan infusion, 100 mm at 0.25 microliters/hour for 4 weeks, with or without e14 spinal-cord npc graft into lesion cavity experiment in rat. methods/readouts recorded in the a-layer: adult rats received delayed continuous thiorphan infusion into left motor cortex because thiorphan does not cross the blood-brain barrier, with npc grafting at 2 weeks post-injury. thiorphan plus npc graft produced a significant twofold forelimb pellet-retrieval success improvement versus lesion control (p=0.005), improved accuracy to 60% versus 30% (p=0.001), and increased corticospinal axon regeneration into the graft by 60% versus graft alone (p<0.05), with putative synaptophysin-apposed host axon/graft-neuron contacts. thiorphan alone and npc graft alone trended but were not significant; there was no significant change in cst sprouting above the lesion, serotonergic or cgrp axons into graft, gfap border, graft differentiation, or graft-derived axon extension. the study supports substrate-dependent cst regeneration and functional benefit, not complete circuit restoration.',
    'Module 5A full-text extraction; Fig. 2-3; severe bilateral C5 contusion and NPC graft experiment',
    'A-layer full text; Fig. 2-3; severe bilateral C5 contusion and NPC graft experiment',
    'medium',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P017-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P017-E002", "measurement_method_inference": "barrier / permeability / endothelial assay; behavioral / functional recovery assay", "paper_tracker_id": "M5A-P017", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T001", "tracker_id": "M5B-O064"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P017::M5A-P017-E002'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Thiorphan reprograms neurons to promote functional recovery after spinal cord injury.; first-pass row captures corticospinal tract regeneration / sprouting in human / translational context at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O064', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P018-E002 confirms the curated Ttbk2 deletion reduced GAP43, MAP2, newborn-neuron and downstream-circuit markers, increased PSD95/Nogo pathway signals, impaired BDA-defined downstream connectivity and BMS recovery; SHH agonist SAG partially rescued MAP2, placing SHH downstream of TTBK2-dependent ciliary regulation. experiment in Mouse SCI model. Methods/readouts recorded in the A-layer: Full-text result supports an endogenous repair pathway with partial pharmacological rescue, not complete circuit restoration.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Full-text source localization for M5A-P018-E002 confirms the curated Ttbk2 deletion reduced GAP43, MAP2, newborn-neuron and downstream-circuit markers, increased PSD95/Nogo pathway signals, impaired BDA-defined downstream connectivity and BMS recovery; SHH agonist SAG partially rescued MAP2, placing SHH downstream of TTBK2-dependent ciliary regulation. experiment in Mouse SCI model. Methods/readouts recorded in the A-layer: Full-text result supports an endogenous repair pathway with partial pharmacological rescue, not complete circuit restoration.',
    'full-text source localization for m5a-p018-e002 confirms the curated ttbk2 deletion reduced gap43, map2, newborn-neuron and downstream-circuit markers, increased psd95/nogo pathway signals, impaired bda-defined downstream connectivity and bms recovery; shh agonist sag partially rescued map2, placing shh downstream of ttbk2-dependent ciliary regulation. experiment in mouse sci model. methods/readouts recorded in the a-layer: full-text result supports an endogenous repair pathway with partial pharmacological rescue, not complete circuit restoration.',
    'Module 5A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P018-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P018-E002", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P018", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T005", "tracker_id": "M5B-O065"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P018::M5A-P018-E002'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for TTBK2-Driven Ciliogenesis Is Required for Intrinsic Neuronal Regeneration After Spinal Cord Injury.; first-pass row captures intrinsic neuronal growth competence in mouse sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O065', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P019-E002 confirms the curated AAV5 KLF7/MEF2 or comparator TF constructs, 1 uL per DRG experiment in Rat dorsal-column SCI model. Methods/readouts recorded in the A-layer: KLF7/MEF2, but not KLF7 or MEF2 alone and not the triple combination, promoted axonal sprouting into and around the lesion, reduced axonal retraction, improved ladder-based functional recovery, and induced a substantial regeneration-associated gene program.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Full-text source localization for M5A-P019-E002 confirms the curated AAV5 KLF7/MEF2 or comparator TF constructs, 1 uL per DRG experiment in Rat dorsal-column SCI model. Methods/readouts recorded in the A-layer: KLF7/MEF2, but not KLF7 or MEF2 alone and not the triple combination, promoted axonal sprouting into and around the lesion, reduced axonal retraction, improved ladder-based functional recovery, and induced a substantial regeneration-associated gene program.',
    'full-text source localization for m5a-p019-e002 confirms the curated aav5 klf7/mef2 or comparator tf constructs, 1 ul per drg experiment in rat dorsal-column sci model. methods/readouts recorded in the a-layer: klf7/mef2, but not klf7 or mef2 alone and not the triple combination, promoted axonal sprouting into and around the lesion, reduced axonal retraction, improved ladder-based functional recovery, and induced a substantial regeneration-associated gene program.',
    'Module 5A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P019-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P019-E002", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P019", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T005", "tracker_id": "M5B-O066"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P019::M5A-P019-E002'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for The transcription factor combination MEF2 and KLF7 promotes axonal sprouting in the injured spinal cord with functional improvement and regeneration-associated gene expression.; first-pass row captures intrinsic neuronal growth competence in rat sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O066', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P020-E002 confirms the curated 5,7-DHT serotonergic neurotoxin with desipramine protection of noradrenergic neurons experiment in Rat. Methods/readouts recorded in the A-layer: bPAC increased lumbar-projecting brainstem neuron sparing, raphe-reticular cAMP signaling, caudal 5-HT tract density and excitatory/inhibitory balance; 5,7-DHT depletion abolished bPAC-mediated motor recovery, supporting serotonergic pathway necessity.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Full-text source localization for M5A-P020-E002 confirms the curated 5,7-DHT serotonergic neurotoxin with desipramine protection of noradrenergic neurons experiment in Rat. Methods/readouts recorded in the A-layer: bPAC increased lumbar-projecting brainstem neuron sparing, raphe-reticular cAMP signaling, caudal 5-HT tract density and excitatory/inhibitory balance; 5,7-DHT depletion abolished bPAC-mediated motor recovery, supporting serotonergic pathway necessity.',
    'full-text source localization for m5a-p020-e002 confirms the curated 5,7-dht serotonergic neurotoxin with desipramine protection of noradrenergic neurons experiment in rat. methods/readouts recorded in the a-layer: bpac increased lumbar-projecting brainstem neuron sparing, raphe-reticular camp signaling, caudal 5-ht tract density and excitatory/inhibitory balance; 5,7-dht depletion abolished bpac-mediated motor recovery, supporting serotonergic pathway necessity.',
    'Module 5A full-text extraction; Full text PMC; Fig. 5-6',
    'A-layer full text; Full text PMC; Fig. 5-6',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P020-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P020-E002", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P020", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T007", "tracker_id": "M5B-O067"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P020::M5A-P020-E002'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Stimulation of corticospinal neurons by optogenetic cAMP inductions promotes motor recovery after spinal cord injury in female rats via raphespinal tract modulation.; first-pass row captures corticospinal tract regeneration / sprouting in rat sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O067', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P021-E002 confirms the curated Glu-UCNP plus NIR guided CST-to-interneuron rewiring; retransection and KYNA challenged circuit dependence experiment in Mouse. Methods/readouts recorded in the A-layer: Glu-UCNP plus NIR raised pellet-reaching success to about 48% by 70 days versus below 20% in other SCI groups; retransection reduced performance, and KYNA reduced caudal calcium activity, supporting functional glutamatergic reconnection rather than axon presence alone.',
    'qualitative',
    NULL,
    'Full-text source localization for M5A-P021-E002 confirms the curated Glu-UCNP plus NIR guided CST-to-interneuron rewiring; retransection and KYNA challenged circuit dependence experiment in Mouse. Methods/readouts recorded in the A-layer: Glu-UCNP plus NIR raised pellet-reaching success to about 48% by 70 days versus below 20% in other SCI groups; retransection reduced performance, and KYNA reduced caudal calcium activity, supporting functional glutamatergic reconnection rather than axon presence alone.',
    'full-text source localization for m5a-p021-e002 confirms the curated glu-ucnp plus nir guided cst-to-interneuron rewiring; retransection and kyna challenged circuit dependence experiment in mouse. methods/readouts recorded in the a-layer: glu-ucnp plus nir raised pellet-reaching success to about 48% by 70 days versus below 20% in other sci groups; retransection reduced performance, and kyna reduced caudal calcium activity, supporting functional glutamatergic reconnection rather than axon presence alone.',
    'Module 5A full-text extraction; Full text PMC; Fig. 5-7',
    'A-layer full text; Full text PMC; Fig. 5-7',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P021-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P021-E002", "measurement_method_inference": null, "paper_tracker_id": "M5A-P021", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T007", "tracker_id": "M5B-O068"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P021::M5A-P021-E002'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Precise rewiring of corticospinal axons and spinal interneurons via near-infrared optogenetics for spinal cord injury treatment.; first-pass row captures corticospinal tract regeneration / sprouting in mouse sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O068', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Schmidt J 2026 M5A-P022-E002 preserves a distinct Human / translational context experiment testing Mechanistic outcome assessment after corticospinal tract regeneration / sprouting with endpoint/readout: Outcome/mechanistic validation row for Netrin-1 Therapy Restores Partial Hindlimb Movement in a Rat Model of High-Severity Chronic Spinal Cord Injury.; first-pass row captures corticospinal tract regeneration / sprouting in human / translational context at abstract/source-title level..',
    'qualitative',
    NULL,
    'Schmidt J 2026 M5A-P022-E002 preserves a distinct Human / translational context experiment testing Mechanistic outcome assessment after corticospinal tract regeneration / sprouting with endpoint/readout: Outcome/mechanistic validation row for Netrin-1 Therapy Restores Partial Hindlimb Movement in a Rat Model of High-Severity Chronic Spinal Cord Injury.; first-pass row captures corticospinal tract regeneration / sprouting in human / translational context at abstract/source-title level..',
    'M5A-P022-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Netrin-1 Therapy Restores Partial Hindlimb Movement in a Rat Model of High-Severity Chronic Spinal Cord Injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M5A-P022-E002", "measurement_method_inference": null, "paper_tracker_id": "M5A-P022", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M5B-T002", "tracker_id": "M5B-O069"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P022::M5A-P022-E002'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Netrin-1 Therapy Restores Partial Hindlimb Movement in a Rat Model of High-Severity Chronic Spinal Cord Injury.; first-pass row captures corticospinal tract regeneration / sprouting in human / translational context at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O069', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P023-E002 confirms the curated Netrin-1 or DCC overexpression, low-expression lentiviruses, and combined gain/loss conditions experiment in Rat SCI model with gain- and loss-of-function validation. Methods/readouts recorded in the A-layer: Netrin-1 or DCC knockdown reduced GAP43/SYP-associated regeneration and worsened BBB recovery, while combined overexpression produced the strongest axon-growth and synaptic-marker response. The study supports association with NgR1-RhoA-ROCK inhibition but does not directly establish receptor-pathway necessity.',
    'qualitative',
    'barrier / permeability / endothelial assay; behavioral / functional recovery assay',
    'Full-text source localization for M5A-P023-E002 confirms the curated Netrin-1 or DCC overexpression, low-expression lentiviruses, and combined gain/loss conditions experiment in Rat SCI model with gain- and loss-of-function validation. Methods/readouts recorded in the A-layer: Netrin-1 or DCC knockdown reduced GAP43/SYP-associated regeneration and worsened BBB recovery, while combined overexpression produced the strongest axon-growth and synaptic-marker response. The study supports association with NgR1-RhoA-ROCK inhibition but does not directly establish receptor-pathway necessity.',
    'full-text source localization for m5a-p023-e002 confirms the curated netrin-1 or dcc overexpression, low-expression lentiviruses, and combined gain/loss conditions experiment in rat sci model with gain- and loss-of-function validation. methods/readouts recorded in the a-layer: netrin-1 or dcc knockdown reduced gap43/syp-associated regeneration and worsened bbb recovery, while combined overexpression produced the strongest axon-growth and synaptic-marker response. the study supports association with ngr1-rhoa-rock inhibition but does not directly establish receptor-pathway necessity.',
    'Module 5A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P023-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P023-E002", "measurement_method_inference": "barrier / permeability / endothelial assay; behavioral / functional recovery assay", "paper_tracker_id": "M5A-P023", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T002", "tracker_id": "M5B-O070"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P023::M5A-P023-E002'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Lentivirus-mediated overexpression of netrin-1/DCC co-expression promotes axonal regeneration and functional recovery in spinal cord injury via the inhibition of the NgR1-RhoA-ROCK signaling pathway.; first-pass row captures extrinsic inhibitory matrix / guidance pathway in human / translational context at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O070', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P024-E002 confirms the curated dFLPP-ChABC targeted CSPG degradation experiment in Rat SCI model. Methods/readouts recorded in the A-layer: Reactive-astrocyte-targeted ROS-responsive dFLPP delivered ChABC to degrade CSPGs, reprogrammed microglial phenotype/metabolism, reduced scar-forming astrocytes and fibrotic matrix, and improved neuronal regeneration, locomotor and autonomic recovery.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Full-text source localization for M5A-P024-E002 confirms the curated dFLPP-ChABC targeted CSPG degradation experiment in Rat SCI model. Methods/readouts recorded in the A-layer: Reactive-astrocyte-targeted ROS-responsive dFLPP delivered ChABC to degrade CSPGs, reprogrammed microglial phenotype/metabolism, reduced scar-forming astrocytes and fibrotic matrix, and improved neuronal regeneration, locomotor and autonomic recovery.',
    'full-text source localization for m5a-p024-e002 confirms the curated dflpp-chabc targeted cspg degradation experiment in rat sci model. methods/readouts recorded in the a-layer: reactive-astrocyte-targeted ros-responsive dflpp delivered chabc to degrade cspgs, reprogrammed microglial phenotype/metabolism, reduced scar-forming astrocytes and fibrotic matrix, and improved neuronal regeneration, locomotor and autonomic recovery.',
    'Module 5A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P024-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P024-E002", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P024", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T002", "tracker_id": "M5B-O071"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P024::M5A-P024-E002'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Disrupting CSPG-Driven Microglia-Astrocyte Crosstalk Enables Scar-Free Repair in Spinal Cord Injury.; first-pass row captures extrinsic inhibitory matrix / guidance pathway in rat sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O071', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P025-E002 confirms the curated Schwann cells plus lenti-ChABC delivered at 3 months, with cyclosporin A immunosuppression experiment in Rat chronic SCI transplantation model. Methods/readouts recorded in the A-layer: Delayed combination treatment produced persistent Schwann-cell survival and axonal regrowth through 6 months, supporting repair in chronic SCI. The chronic cohort was small and had mortality, so the long-term finding is supportive rather than definitive.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Full-text source localization for M5A-P025-E002 confirms the curated Schwann cells plus lenti-ChABC delivered at 3 months, with cyclosporin A immunosuppression experiment in Rat chronic SCI transplantation model. Methods/readouts recorded in the A-layer: Delayed combination treatment produced persistent Schwann-cell survival and axonal regrowth through 6 months, supporting repair in chronic SCI. The chronic cohort was small and had mortality, so the long-term finding is supportive rather than definitive.',
    'full-text source localization for m5a-p025-e002 confirms the curated schwann cells plus lenti-chabc delivered at 3 months, with cyclosporin a immunosuppression experiment in rat chronic sci transplantation model. methods/readouts recorded in the a-layer: delayed combination treatment produced persistent schwann-cell survival and axonal regrowth through 6 months, supporting repair in chronic sci. the chronic cohort was small and had mortality, so the long-term finding is supportive rather than definitive.',
    'Module 5A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P025-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P025-E002", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P025", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T004", "tracker_id": "M5B-O072"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P025::M5A-P025-E002'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Chondroitinase ABC combined with Schwann cell transplantation enhances restoration of neural connection and functional recovery following acute and chronic spinal cord injury.; first-pass row captures serotonergic/propriospinal relay plasticity in human / translational context at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O072', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Zhu S 2024 M5A-P026-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after extrinsic inhibitory matrix / guidance pathway with endpoint/readout: Outcome/mechanistic validation row for Schwann Cell-Derived Exosomes Induced Axon Growth after Spinal Cord Injury by Decreasing PTP- Activation on CSPGs via the Rho/ROCK Pathway.; first-pass row captures extrinsic inhibitory matrix / guidance pathway in mouse sci model at abstract/source-title level..',
    'qualitative',
    NULL,
    'Zhu S 2024 M5A-P026-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after extrinsic inhibitory matrix / guidance pathway with endpoint/readout: Outcome/mechanistic validation row for Schwann Cell-Derived Exosomes Induced Axon Growth after Spinal Cord Injury by Decreasing PTP- Activation on CSPGs via the Rho/ROCK Pathway.; first-pass row captures extrinsic inhibitory matrix / guidance pathway in mouse sci model at abstract/source-title level..',
    'M5A-P026-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Schwann Cell-Derived Exosomes Induced Axon Growth after Spinal Cord Injury by Decreasing PTP- Activation on CSPGs via the Rho/ROCK Pathway.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M5A-P026-E002", "measurement_method_inference": null, "paper_tracker_id": "M5A-P026", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M5B-T002", "tracker_id": "M5B-O073"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P026::M5A-P026-E002'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Schwann Cell-Derived Exosomes Induced Axon Growth after Spinal Cord Injury by Decreasing PTP- Activation on CSPGs via the Rho/ROCK Pathway.; first-pass row captures extrinsic inhibitory matrix / guidance pathway in mouse sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O073', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P027-E002 confirms the curated Compared with placebo, NG101 was associated with faster lesion-volume reduction and slower decline of cord area and MTsat in corticospinal tracts and dorsal columns; combined MRI/electrophysiology improved treatment-effect stratification and reduced projected trial sample size. experiment in Human clinical SCI cohort. Methods/readouts recorded in the A-layer: Full-text evidence supports structural preservation or sprouting interpretation, while the clinical functional endpoint remains stratification-sensitive.',
    'qualitative',
    'MRI / imaging assay',
    'Full-text source localization for M5A-P027-E002 confirms the curated Compared with placebo, NG101 was associated with faster lesion-volume reduction and slower decline of cord area and MTsat in corticospinal tracts and dorsal columns; combined MRI/electrophysiology improved treatment-effect stratification and reduced projected trial sample size. experiment in Human clinical SCI cohort. Methods/readouts recorded in the A-layer: Full-text evidence supports structural preservation or sprouting interpretation, while the clinical functional endpoint remains stratification-sensitive.',
    'full-text source localization for m5a-p027-e002 confirms the curated compared with placebo, ng101 was associated with faster lesion-volume reduction and slower decline of cord area and mtsat in corticospinal tracts and dorsal columns; combined mri/electrophysiology improved treatment-effect stratification and reduced projected trial sample size. experiment in human clinical sci cohort. methods/readouts recorded in the a-layer: full-text evidence supports structural preservation or sprouting interpretation, while the clinical functional endpoint remains stratification-sensitive.',
    'Module 5A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P027-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P027-E002", "measurement_method_inference": "MRI / imaging assay", "paper_tracker_id": "M5A-P027", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T002", "tracker_id": "M5B-O074"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P027::M5A-P027-E002'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Anti-Nogo-A NG101 treatment induces changes in spinal cord micro- and macrostructure following spinal cord injury.; first-pass row captures corticospinal tract regeneration / sprouting in rat sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O074', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P028-E002 confirms the curated XMC-ChABC affinity-release hydrogel; oNPC transplantation as above experiment in Human oNPC in vitro and chronic rat SCI mechanism validation. Methods/readouts recorded in the A-layer: XMC-ChABC degraded CS56/C4S CSPGs, reduced the astrocytic bias induced by SCI homogenate, increased oligodendrocyte-lineage markers, and promoted STEM121-positive graft-derived myelin with functional nodes of Ranvier. The combination did not significantly preserve total tissue area, so the repair claim is strongest for remyelination, synaptic preservation, and behavior.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Full-text source localization for M5A-P028-E002 confirms the curated XMC-ChABC affinity-release hydrogel; oNPC transplantation as above experiment in Human oNPC in vitro and chronic rat SCI mechanism validation. Methods/readouts recorded in the A-layer: XMC-ChABC degraded CS56/C4S CSPGs, reduced the astrocytic bias induced by SCI homogenate, increased oligodendrocyte-lineage markers, and promoted STEM121-positive graft-derived myelin with functional nodes of Ranvier. The combination did not significantly preserve total tissue area, so the repair claim is strongest for remyelination, synaptic preservation, and behavior.',
    'full-text source localization for m5a-p028-e002 confirms the curated xmc-chabc affinity-release hydrogel; onpc transplantation as above experiment in human onpc in vitro and chronic rat sci mechanism validation. methods/readouts recorded in the a-layer: xmc-chabc degraded cs56/c4s cspgs, reduced the astrocytic bias induced by sci homogenate, increased oligodendrocyte-lineage markers, and promoted stem121-positive graft-derived myelin with functional nodes of ranvier. the combination did not significantly preserve total tissue area, so the repair claim is strongest for remyelination, synaptic preservation, and behavior.',
    'Module 5A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P028-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P028-E002", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P028", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T003", "tracker_id": "M5B-O075"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P028::M5A-P028-E002'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Human Oligodendrogenic Neural Progenitor Cells Delivered with Chondroitinase ABC Facilitate Functional Repair of Chronic Spinal Cord Injury.; first-pass row captures remyelination / white matter repair in human / translational context at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O075', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P029-E002 confirms the curated Sustained COG1410 activation worsened fibrosis, chronic inflammation, axon regeneration, neuronal survival, and late locomotion despite early benefit; short-term activation produced transient early locomotor improvement without structural neuroprotection. experiment in Mouse SCI model. Methods/readouts recorded in the A-layer: Full-text result defines a timing-dependent clearance-versus-fibrosis tradeoff.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Full-text source localization for M5A-P029-E002 confirms the curated Sustained COG1410 activation worsened fibrosis, chronic inflammation, axon regeneration, neuronal survival, and late locomotion despite early benefit; short-term activation produced transient early locomotor improvement without structural neuroprotection. experiment in Mouse SCI model. Methods/readouts recorded in the A-layer: Full-text result defines a timing-dependent clearance-versus-fibrosis tradeoff.',
    'full-text source localization for m5a-p029-e002 confirms the curated sustained cog1410 activation worsened fibrosis, chronic inflammation, axon regeneration, neuronal survival, and late locomotion despite early benefit; short-term activation produced transient early locomotor improvement without structural neuroprotection. experiment in mouse sci model. methods/readouts recorded in the a-layer: full-text result defines a timing-dependent clearance-versus-fibrosis tradeoff.',
    'Module 5A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P029-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P029-E002", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P029", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T003", "tracker_id": "M5B-O076"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P029::M5A-P029-E002'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for TREM2 Facilitates Myelin Debris Clearance but Exacerbates Chronic Inflammation and Fibrosis After Spinal Cord Injury.; first-pass row captures remyelination / white matter repair in mouse sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O076', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P030-E002 confirms the curated Astrocyte-derived CCN1 bound microglial SDC4 to promote lipid storage and repair-associated buffering; Ccn1 depletion blunted debris clearance and neurological recovery, establishing an astrocyte-to-microglia repair relay. experiment in Mouse SCI model. Methods/readouts recorded in the A-layer: Full-text result is mechanistic and mapping-heavy, with repair outcome evidence but no therapeutic dosing claim.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Full-text source localization for M5A-P030-E002 confirms the curated Astrocyte-derived CCN1 bound microglial SDC4 to promote lipid storage and repair-associated buffering; Ccn1 depletion blunted debris clearance and neurological recovery, establishing an astrocyte-to-microglia repair relay. experiment in Mouse SCI model. Methods/readouts recorded in the A-layer: Full-text result is mechanistic and mapping-heavy, with repair outcome evidence but no therapeutic dosing claim.',
    'full-text source localization for m5a-p030-e002 confirms the curated astrocyte-derived ccn1 bound microglial sdc4 to promote lipid storage and repair-associated buffering; ccn1 depletion blunted debris clearance and neurological recovery, establishing an astrocyte-to-microglia repair relay. experiment in mouse sci model. methods/readouts recorded in the a-layer: full-text result is mechanistic and mapping-heavy, with repair outcome evidence but no therapeutic dosing claim.',
    'Module 5A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P030-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P030-E002", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P030", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T003", "tracker_id": "M5B-O077"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P030::M5A-P030-E002'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Lesion-remote astrocytes govern microglia-mediated white matter repair.; first-pass row captures remyelination / white matter repair in human / translational context at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O077', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P031-E002 confirms the curated Persistent postinjury remyelination failure through Myrf deletion experiment in Mouse. Methods/readouts recorded in the A-layer: Moderate-injury Myrf ICKOs conducted action potentials across the lesion at similar velocity to controls (28.2 vs 27.2 m/s), with Nav1.2/Kv1.2 co-expression uniquely extended along ICKO axons and only subtle gait differences. The data support compensatory conduction, not proof that remyelination is unnecessary in all injury severities.',
    'qualitative',
    'genetic perturbation / knockdown assay',
    'Full-text source localization for M5A-P031-E002 confirms the curated Persistent postinjury remyelination failure through Myrf deletion experiment in Mouse. Methods/readouts recorded in the A-layer: Moderate-injury Myrf ICKOs conducted action potentials across the lesion at similar velocity to controls (28.2 vs 27.2 m/s), with Nav1.2/Kv1.2 co-expression uniquely extended along ICKO axons and only subtle gait differences. The data support compensatory conduction, not proof that remyelination is unnecessary in all injury severities.',
    'full-text source localization for m5a-p031-e002 confirms the curated persistent postinjury remyelination failure through myrf deletion experiment in mouse. methods/readouts recorded in the a-layer: moderate-injury myrf ickos conducted action potentials across the lesion at similar velocity to controls (28.2 vs 27.2 m/s), with nav1.2/kv1.2 co-expression uniquely extended along icko axons and only subtle gait differences. the data support compensatory conduction, not proof that remyelination is unnecessary in all injury severities.',
    'Module 5A full-text extraction; Full text PMC; moderate injury physiology and gait cohort',
    'A-layer full text; Full text PMC; moderate injury physiology and gait cohort',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P031-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P031-E002", "measurement_method_inference": "genetic perturbation / knockdown assay", "paper_tracker_id": "M5A-P031", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T003", "tracker_id": "M5B-O078"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P031::M5A-P031-E002'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Compensatory changes after spinal cord injury in a remyelination deficient mouse model.; first-pass row captures remyelination / white matter repair in mouse sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O078', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P032-E002 confirms the curated Pretreated macrophage membrane adsorption on PCL; pMM-PCL co-culture with myelin debris, macrophages, and PC12 cells experiment in Rat SCI model plus macrophage and neuronal in vitro models. Methods/readouts recorded in the A-layer: pMM-PCL reduced Oil Red O-positive foam-cell formation, attracted macrophages toward adsorbed debris, increased Arg1 while reducing iNOS in the repair microenvironment, and relieved myelin-debris-mediated inhibition of PC12 migration.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Full-text source localization for M5A-P032-E002 confirms the curated Pretreated macrophage membrane adsorption on PCL; pMM-PCL co-culture with myelin debris, macrophages, and PC12 cells experiment in Rat SCI model plus macrophage and neuronal in vitro models. Methods/readouts recorded in the A-layer: pMM-PCL reduced Oil Red O-positive foam-cell formation, attracted macrophages toward adsorbed debris, increased Arg1 while reducing iNOS in the repair microenvironment, and relieved myelin-debris-mediated inhibition of PC12 migration.',
    'full-text source localization for m5a-p032-e002 confirms the curated pretreated macrophage membrane adsorption on pcl; pmm-pcl co-culture with myelin debris, macrophages, and pc12 cells experiment in rat sci model plus macrophage and neuronal in vitro models. methods/readouts recorded in the a-layer: pmm-pcl reduced oil red o-positive foam-cell formation, attracted macrophages toward adsorbed debris, increased arg1 while reducing inos in the repair microenvironment, and relieved myelin-debris-mediated inhibition of pc12 migration.',
    'Module 5A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P032-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P032-E002", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P032", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T003", "tracker_id": "M5B-O079"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P032::M5A-P032-E002'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for A Myelin Debris Cleaner for Spinal Cord Injury Recovery: Polycaprolactone / Cell Membrane Assembled Scaffolds.; first-pass row captures remyelination / white matter repair in rat sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O079', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P033-E002 confirms the curated Lesion-site SeroPTEN-CG restored neuronal excitability, silenced PTEN, promoted axonal elongation and ECM remodeling, reactivated spared spinal circuits, and improved sensory and locomotor outcomes with reported biosafety assessment. experiment in Mouse SCI model. Methods/readouts recorded in the A-layer: Full-text result supports coordinated excitability plus structural reconstruction; the two actions are not independently isolated in the final in vivo formulation.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Full-text source localization for M5A-P033-E002 confirms the curated Lesion-site SeroPTEN-CG restored neuronal excitability, silenced PTEN, promoted axonal elongation and ECM remodeling, reactivated spared spinal circuits, and improved sensory and locomotor outcomes with reported biosafety assessment. experiment in Mouse SCI model. Methods/readouts recorded in the A-layer: Full-text result supports coordinated excitability plus structural reconstruction; the two actions are not independently isolated in the final in vivo formulation.',
    'full-text source localization for m5a-p033-e002 confirms the curated lesion-site seropten-cg restored neuronal excitability, silenced pten, promoted axonal elongation and ecm remodeling, reactivated spared spinal circuits, and improved sensory and locomotor outcomes with reported biosafety assessment. experiment in mouse sci model. methods/readouts recorded in the a-layer: full-text result supports coordinated excitability plus structural reconstruction; the two actions are not independently isolated in the final in vivo formulation.',
    'Module 5A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P033-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P033-E002", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P033", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T004", "tracker_id": "M5B-O080"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P033::M5A-P033-E002'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Serotonergic System-Targeted Nucleic Acid Hydrogel Coordinates Excitability Restoration and Circuit Reconstruction for Spinal Cord Injury Therapy.; first-pass row captures serotonergic/propriospinal relay plasticity in mouse sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O080', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P034-E002 confirms the curated Central serotonin deficiency via TPH2 knockout experiment in Rat. Methods/readouts recorded in the A-layer: TPH2 KO animals showed lower submaximal/maximal CMAP amplitudes on the ipsilateral hindlimb and altered recruitment curves, consistent with slower sensorimotor pathway recovery. The paper does not directly quantify serotonergic axon sprouting or establish a receptor-specific mechanism.',
    'qualitative',
    'genetic perturbation / knockdown assay; behavioral / functional recovery assay',
    'Full-text source localization for M5A-P034-E002 confirms the curated Central serotonin deficiency via TPH2 knockout experiment in Rat. Methods/readouts recorded in the A-layer: TPH2 KO animals showed lower submaximal/maximal CMAP amplitudes on the ipsilateral hindlimb and altered recruitment curves, consistent with slower sensorimotor pathway recovery. The paper does not directly quantify serotonergic axon sprouting or establish a receptor-specific mechanism.',
    'full-text source localization for m5a-p034-e002 confirms the curated central serotonin deficiency via tph2 knockout experiment in rat. methods/readouts recorded in the a-layer: tph2 ko animals showed lower submaximal/maximal cmap amplitudes on the ipsilateral hindlimb and altered recruitment curves, consistent with slower sensorimotor pathway recovery. the paper does not directly quantify serotonergic axon sprouting or establish a receptor-specific mechanism.',
    'Module 5A full-text extraction; Full text PMC; electrophysiological validation',
    'A-layer full text; Full text PMC; electrophysiological validation',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P034-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P034-E002", "measurement_method_inference": "genetic perturbation / knockdown assay; behavioral / functional recovery assay", "paper_tracker_id": "M5A-P034", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T004", "tracker_id": "M5B-O081"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P034::M5A-P034-E002'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Central Serotonin Deficiency Impairs Recovery of Sensorimotor Abilities After Spinal Cord Injury in Rats.; first-pass row captures serotonergic/propriospinal relay plasticity in rat sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O081', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Gao Z 2025 M5A-P035-E002 preserves a distinct Human / translational context experiment testing Mechanistic outcome assessment after serotonergic/propriospinal relay plasticity with endpoint/readout: Outcome/mechanistic validation row for Neuronal HDAC3 knockdown promotes propriospinal detour pathway formation and locomotor recovery in a mouse model of spinal cord injury.; first-pass row captures serotonergic/propriospinal relay plasticity in human / translational context at abstract/source-title level..',
    'qualitative',
    'behavioral / functional recovery assay',
    'Gao Z 2025 M5A-P035-E002 preserves a distinct Human / translational context experiment testing Mechanistic outcome assessment after serotonergic/propriospinal relay plasticity with endpoint/readout: Outcome/mechanistic validation row for Neuronal HDAC3 knockdown promotes propriospinal detour pathway formation and locomotor recovery in a mouse model of spinal cord injury.; first-pass row captures serotonergic/propriospinal relay plasticity in human / translational context at abstract/source-title level..',
    'M5A-P035-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Neuronal HDAC3 knockdown promotes propriospinal detour pathway formation and locomotor recovery in a mouse model of spinal cord injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M5A-P035-E002", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P035", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M5B-T004", "tracker_id": "M5B-O082"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P035::M5A-P035-E002'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Neuronal HDAC3 knockdown promotes propriospinal detour pathway formation and locomotor recovery in a mouse model of spinal cord injury.; first-pass row captures serotonergic/propriospinal relay plasticity in human / translational context at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O082', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P036-E002 confirms the curated Systemic KCC2 agonist CLP290 daily, selected dose 17.5 mg/kg, with OPN/IGF1 plus NSC transplantation experiment in Rat. Methods/readouts recorded in the A-layer: Adding CLP290 to OPN/IGF1 plus NSCs increased BBB scores to approximately 6 versus approximately 2-3 with the bridge regimen alone, improved hindlimb joint oscillation, and produced weak but consistent rostral-to-caudal evoked responses across the graft. A 1.75 mg/kg dose was ineffective; 17.5 and 175 mg/kg improved behavior without added benefit at the higher dose. CLP290 did not change bridge anatomy or host T8 c-Fos pattern, indicating functional enabling rather than increased axon regeneration.',
    'qualitative',
    'barrier / permeability / endothelial assay; behavioral / functional recovery assay',
    'Full-text source localization for M5A-P036-E002 confirms the curated Systemic KCC2 agonist CLP290 daily, selected dose 17.5 mg/kg, with OPN/IGF1 plus NSC transplantation experiment in Rat. Methods/readouts recorded in the A-layer: Adding CLP290 to OPN/IGF1 plus NSCs increased BBB scores to approximately 6 versus approximately 2-3 with the bridge regimen alone, improved hindlimb joint oscillation, and produced weak but consistent rostral-to-caudal evoked responses across the graft. A 1.75 mg/kg dose was ineffective; 17.5 and 175 mg/kg improved behavior without added benefit at the higher dose. CLP290 did not change bridge anatomy or host T8 c-Fos pattern, indicating functional enabling rather than increased axon regeneration.',
    'full-text source localization for m5a-p036-e002 confirms the curated systemic kcc2 agonist clp290 daily, selected dose 17.5 mg/kg, with opn/igf1 plus nsc transplantation experiment in rat. methods/readouts recorded in the a-layer: adding clp290 to opn/igf1 plus nscs increased bbb scores to approximately 6 versus approximately 2-3 with the bridge regimen alone, improved hindlimb joint oscillation, and produced weak but consistent rostral-to-caudal evoked responses across the graft. a 1.75 mg/kg dose was ineffective; 17.5 and 175 mg/kg improved behavior without added benefit at the higher dose. clp290 did not change bridge anatomy or host t8 c-fos pattern, indicating functional enabling rather than increased axon regeneration.',
    'Module 5A full-text extraction; Fig. 3; CLP290 dose-response, behavior, and electrophysiology',
    'A-layer full text; Fig. 3; CLP290 dose-response, behavior, and electrophysiology',
    'medium',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P036-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P036-E002", "measurement_method_inference": "barrier / permeability / endothelial assay; behavioral / functional recovery assay", "paper_tracker_id": "M5A-P036", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T004", "tracker_id": "M5B-O083"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P036::M5A-P036-E002'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Functional recovery induced by KCC2-enabled relay pathways in completely injured spinal cords in adult rats.; first-pass row captures serotonergic/propriospinal relay plasticity in rat sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O083', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P037-E002 confirms the curated Quercetin 100 uM, QZIF, or QZIF-polymersomes in vitro; QZIF-polymersomes 30 mg/kg from day 14 for remyelination cohort experiment in Rat SCI model plus primary neuron and microglia validation. Methods/readouts recorded in the A-layer: Quercetin enhanced KCC2 activation in electrophysiology, while QZIF-polymersomes restored KCC2, mitochondrial respiration, glucose metabolism, COXI/UCP2/TFAM, and neurite length under inflammatory stress. Delayed treatment increased NF200+ axons and both oligodendrocyte- and Schwann-cell-associated remyelinated fibers; KCC2 necessity was not directly tested by loss of function.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Full-text source localization for M5A-P037-E002 confirms the curated Quercetin 100 uM, QZIF, or QZIF-polymersomes in vitro; QZIF-polymersomes 30 mg/kg from day 14 for remyelination cohort experiment in Rat SCI model plus primary neuron and microglia validation. Methods/readouts recorded in the A-layer: Quercetin enhanced KCC2 activation in electrophysiology, while QZIF-polymersomes restored KCC2, mitochondrial respiration, glucose metabolism, COXI/UCP2/TFAM, and neurite length under inflammatory stress. Delayed treatment increased NF200+ axons and both oligodendrocyte- and Schwann-cell-associated remyelinated fibers; KCC2 necessity was not directly tested by loss of function.',
    'full-text source localization for m5a-p037-e002 confirms the curated quercetin 100 um, qzif, or qzif-polymersomes in vitro; qzif-polymersomes 30 mg/kg from day 14 for remyelination cohort experiment in rat sci model plus primary neuron and microglia validation. methods/readouts recorded in the a-layer: quercetin enhanced kcc2 activation in electrophysiology, while qzif-polymersomes restored kcc2, mitochondrial respiration, glucose metabolism, coxi/ucp2/tfam, and neurite length under inflammatory stress. delayed treatment increased nf200+ axons and both oligodendrocyte- and schwann-cell-associated remyelinated fibers; kcc2 necessity was not directly tested by loss of function.',
    'Module 5A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P037-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P037-E002", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P037", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T004", "tracker_id": "M5B-O084"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P037::M5A-P037-E002'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Functionalized nanozyme delivery of a KCC2-activator conjugate for the promotion of functional recovery after acute spinal cord injury.; first-pass row captures serotonergic/propriospinal relay plasticity in rat sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O084', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P038-E002 confirms the curated Loss of GlcNAc6ST1/4-dependent glycan sulfation experiment in Mouse. Methods/readouts recorded in the A-layer: Double deficiency reduced recruited monocytes, CD68+ activated macrophage/microglia, fibronectin and collagen/ECM gene programs, while increasing synaptic-membrane transcripts and eliminating GlcNAc-6-sulfated N-glycans. Increased serotonergic fibers correlated with recovery, but their causal contribution was not directly tested.',
    'qualitative',
    'genetic perturbation / knockdown assay; behavioral / functional recovery assay',
    'Full-text source localization for M5A-P038-E002 confirms the curated Loss of GlcNAc6ST1/4-dependent glycan sulfation experiment in Mouse. Methods/readouts recorded in the A-layer: Double deficiency reduced recruited monocytes, CD68+ activated macrophage/microglia, fibronectin and collagen/ECM gene programs, while increasing synaptic-membrane transcripts and eliminating GlcNAc-6-sulfated N-glycans. Increased serotonergic fibers correlated with recovery, but their causal contribution was not directly tested.',
    'full-text source localization for m5a-p038-e002 confirms the curated loss of glcnac6st1/4-dependent glycan sulfation experiment in mouse. methods/readouts recorded in the a-layer: double deficiency reduced recruited monocytes, cd68+ activated macrophage/microglia, fibronectin and collagen/ecm gene programs, while increasing synaptic-membrane transcripts and eliminating glcnac-6-sulfated n-glycans. increased serotonergic fibers correlated with recovery, but their causal contribution was not directly tested.',
    'Module 5A full-text extraction; Full text PMC; Fig. 4-6',
    'A-layer full text; Full text PMC; Fig. 4-6',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P038-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P038-E002", "measurement_method_inference": "genetic perturbation / knockdown assay; behavioral / functional recovery assay", "paper_tracker_id": "M5A-P038", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T004", "tracker_id": "M5B-O085"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P038::M5A-P038-E002'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Enhanced locomotor recovery in mice lacking GlcNAc6ST1 and GlcNAc6ST4 following spinal cord injury.; first-pass row captures serotonergic/propriospinal relay plasticity in mouse sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O085', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Zhao Q 2025 M5A-P039-E002 preserves a distinct Human / translational context experiment testing Mechanistic outcome assessment after corticospinal tract regeneration / sprouting with endpoint/readout: Outcome/mechanistic validation row for Treadmill exercise supplemented by OPN promote axon regeneration through the IGF-1R/Akt/mTOR signaling pathway.; first-pass row captures corticospinal tract regeneration / sprouting in human / translational context at abstract/source-title level..',
    'qualitative',
    'pathway activity / phospho-signaling assay',
    'Zhao Q 2025 M5A-P039-E002 preserves a distinct Human / translational context experiment testing Mechanistic outcome assessment after corticospinal tract regeneration / sprouting with endpoint/readout: Outcome/mechanistic validation row for Treadmill exercise supplemented by OPN promote axon regeneration through the IGF-1R/Akt/mTOR signaling pathway.; first-pass row captures corticospinal tract regeneration / sprouting in human / translational context at abstract/source-title level..',
    'M5A-P039-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Treadmill exercise supplemented by OPN promote axon regeneration through the IGF-1R/Akt/mTOR signaling pathway.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M5A-P039-E002", "measurement_method_inference": "pathway activity / phospho-signaling assay", "paper_tracker_id": "M5A-P039", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M5B-T007", "tracker_id": "M5B-O086"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P039::M5A-P039-E002'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Treadmill exercise supplemented by OPN promote axon regeneration through the IGF-1R/Akt/mTOR signaling pathway.; first-pass row captures corticospinal tract regeneration / sprouting in human / translational context at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O086', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P040-E002 confirms the curated AAV9-SPP1-GFP or AAV-GFP; BDA tracing at 7 weeks; treadmill at 50% maximum speed experiment in Mouse cervical SCI model with cortical signaling and tract tracing. Methods/readouts recorded in the A-layer: Combined OPN and exercise increased p-S6 and GAP43, reduced forelimb ladder errors, and increased BDA-labeled CST fibers caudal to the lesion. The study notes that the functional benefit may also involve sprouting and activity-dependent plasticity, not only the limited lesion-crossing axons.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Full-text source localization for M5A-P040-E002 confirms the curated AAV9-SPP1-GFP or AAV-GFP; BDA tracing at 7 weeks; treadmill at 50% maximum speed experiment in Mouse cervical SCI model with cortical signaling and tract tracing. Methods/readouts recorded in the A-layer: Combined OPN and exercise increased p-S6 and GAP43, reduced forelimb ladder errors, and increased BDA-labeled CST fibers caudal to the lesion. The study notes that the functional benefit may also involve sprouting and activity-dependent plasticity, not only the limited lesion-crossing axons.',
    'full-text source localization for m5a-p040-e002 confirms the curated aav9-spp1-gfp or aav-gfp; bda tracing at 7 weeks; treadmill at 50% maximum speed experiment in mouse cervical sci model with cortical signaling and tract tracing. methods/readouts recorded in the a-layer: combined opn and exercise increased p-s6 and gap43, reduced forelimb ladder errors, and increased bda-labeled cst fibers caudal to the lesion. the study notes that the functional benefit may also involve sprouting and activity-dependent plasticity, not only the limited lesion-crossing axons.',
    'Module 5A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P040-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P040-E002", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P040", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T007", "tracker_id": "M5B-O087"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P040::M5A-P040-E002'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Osteopontin enhances the effect of treadmill training and promotes functional recovery after spinal cord injury.; first-pass row captures corticospinal tract regeneration / sprouting in mouse sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O087', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P041-E002 confirms the curated DPSC-OIC supernatant in vitro; DPSC-OIC grafts in vivo experiment in HT-22 neuronal culture plus mouse SCI validation. Methods/readouts recorded in the A-layer: DPSC-OIC supernatant increased HT-22 proliferation, Tubb3/Syn1 and neurite length and reduced H2O2-associated apoptosis. In vivo, the OIC payload improved neural-support markers and spinal structure, but the study did not directly quantify long-distance axon regeneration.',
    'qualitative',
    NULL,
    'Full-text source localization for M5A-P041-E002 confirms the curated DPSC-OIC supernatant in vitro; DPSC-OIC grafts in vivo experiment in HT-22 neuronal culture plus mouse SCI validation. Methods/readouts recorded in the A-layer: DPSC-OIC supernatant increased HT-22 proliferation, Tubb3/Syn1 and neurite length and reduced H2O2-associated apoptosis. In vivo, the OIC payload improved neural-support markers and spinal structure, but the study did not directly quantify long-distance axon regeneration.',
    'full-text source localization for m5a-p041-e002 confirms the curated dpsc-oic supernatant in vitro; dpsc-oic grafts in vivo experiment in ht-22 neuronal culture plus mouse sci validation. methods/readouts recorded in the a-layer: dpsc-oic supernatant increased ht-22 proliferation, tubb3/syn1 and neurite length and reduced h2o2-associated apoptosis. in vivo, the oic payload improved neural-support markers and spinal structure, but the study did not directly quantify long-distance axon regeneration.',
    'Module 5A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P041-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P041-E002", "measurement_method_inference": null, "paper_tracker_id": "M5A-P041", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T006", "tracker_id": "M5B-O088"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P041::M5A-P041-E002'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Co-overexpression of OPN, IGF-1 and CNTF augment the therapeutic effect of DPSC on spinal cord injury.; first-pass row captures graft/scaffold-enabled axon repair in mouse sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O088', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P042-E002 confirms the curated PTEN knockdown plus GM-RA4IV-filled parallel-channel scaffold experiment in Rat. Methods/readouts recorded in the A-layer: Combined treatment aligned regenerated axons at about 9.7 degrees versus about 37-40 degrees in non-channeled comparators, increased MBP/synaptophysin-associated fibers, and enriched Ephrin/Eph guidance programs. Retransection abolished the functional gain within 1 week, supporting graft-dependent circuit transmission; direct synaptic function was not fully established.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Full-text source localization for M5A-P042-E002 confirms the curated PTEN knockdown plus GM-RA4IV-filled parallel-channel scaffold experiment in Rat. Methods/readouts recorded in the A-layer: Combined treatment aligned regenerated axons at about 9.7 degrees versus about 37-40 degrees in non-channeled comparators, increased MBP/synaptophysin-associated fibers, and enriched Ephrin/Eph guidance programs. Retransection abolished the functional gain within 1 week, supporting graft-dependent circuit transmission; direct synaptic function was not fully established.',
    'full-text source localization for m5a-p042-e002 confirms the curated pten knockdown plus gm-ra4iv-filled parallel-channel scaffold experiment in rat. methods/readouts recorded in the a-layer: combined treatment aligned regenerated axons at about 9.7 degrees versus about 37-40 degrees in non-channeled comparators, increased mbp/synaptophysin-associated fibers, and enriched ephrin/eph guidance programs. retransection abolished the functional gain within 1 week, supporting graft-dependent circuit transmission; direct synaptic function was not fully established.',
    'Module 5A full-text extraction; Full text PMC; Fig. 7-8 and retransection',
    'A-layer full text; Full text PMC; Fig. 7-8 and retransection',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P042-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P042-E002", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P042", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T006", "tracker_id": "M5B-O089"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P042::M5A-P042-E002'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Multichannel 3D-Printed Bioactive Scaffold Combined with Small Interfering RNA Delivery to Promote Neurological Recovery after Spinal Cord Injury.; first-pass row captures graft/scaffold-enabled axon repair in rat sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O089', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P043-E002 confirms the curated PTEN-siRNA scaffolds sustained PTEN suppression, increased BCL2 and GAP43, preserved neuronal/glial biocompatibility, enhanced neurite outgrowth after in vitro injury, and delivered siRNA to neurons in chick explants. experiment in Primary cortical neurons plus chick brain explant. Methods/readouts recorded in the A-layer: Full-text result supports delivery and growth competence; it does not establish axon regeneration or functional recovery in an injured animal.',
    'qualitative',
    'genetic perturbation / knockdown assay; behavioral / functional recovery assay',
    'Full-text source localization for M5A-P043-E002 confirms the curated PTEN-siRNA scaffolds sustained PTEN suppression, increased BCL2 and GAP43, preserved neuronal/glial biocompatibility, enhanced neurite outgrowth after in vitro injury, and delivered siRNA to neurons in chick explants. experiment in Primary cortical neurons plus chick brain explant. Methods/readouts recorded in the A-layer: Full-text result supports delivery and growth competence; it does not establish axon regeneration or functional recovery in an injured animal.',
    'full-text source localization for m5a-p043-e002 confirms the curated pten-sirna scaffolds sustained pten suppression, increased bcl2 and gap43, preserved neuronal/glial biocompatibility, enhanced neurite outgrowth after in vitro injury, and delivered sirna to neurons in chick explants. experiment in primary cortical neurons plus chick brain explant. methods/readouts recorded in the a-layer: full-text result supports delivery and growth competence; it does not establish axon regeneration or functional recovery in an injured animal.',
    'Module 5A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P043-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P043-E002", "measurement_method_inference": "genetic perturbation / knockdown assay; behavioral / functional recovery assay", "paper_tracker_id": "M5A-P043", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T005", "tracker_id": "M5B-O090"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P043::M5A-P043-E002'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Development of a <i>PTEN</i>-siRNA activated scaffold to promote axonal regrowth following spinal cord injury.; first-pass row captures intrinsic neuronal growth competence in rat sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O090', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P044-E002 confirms the curated Pharmacogenomic screening identified Panobinostat as a Cited2-linked HDAC inhibitor; it promoted sensory axon growth, 5-HT sprouting and neurological recovery after SCI, while Cited2 knockdown abrogated the in vitro growth benefit. experiment in Mouse SCI model. Methods/readouts recorded in the A-layer: Full-text result supports a druggable Cited2 mechanism but leaves long-term structural-stability and broad-HDAC safety questions open.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Full-text source localization for M5A-P044-E002 confirms the curated Pharmacogenomic screening identified Panobinostat as a Cited2-linked HDAC inhibitor; it promoted sensory axon growth, 5-HT sprouting and neurological recovery after SCI, while Cited2 knockdown abrogated the in vitro growth benefit. experiment in Mouse SCI model. Methods/readouts recorded in the A-layer: Full-text result supports a druggable Cited2 mechanism but leaves long-term structural-stability and broad-HDAC safety questions open.',
    'full-text source localization for m5a-p044-e002 confirms the curated pharmacogenomic screening identified panobinostat as a cited2-linked hdac inhibitor; it promoted sensory axon growth, 5-ht sprouting and neurological recovery after sci, while cited2 knockdown abrogated the in vitro growth benefit. experiment in mouse sci model. methods/readouts recorded in the a-layer: full-text result supports a druggable cited2 mechanism but leaves long-term structural-stability and broad-hdac safety questions open.',
    'Module 5A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P044-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P044-E002", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P044", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T005", "tracker_id": "M5B-O091"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P044::M5A-P044-E002'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for CITED2 is a druggable epigenetic switch coupling neuronal maturation to regenerative decline.; first-pass row captures intrinsic neuronal growth competence in rat sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O091', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P045-E002 confirms the curated PLO-coated plant scaffold experiment in Rat. Methods/readouts recorded in the A-layer: PLO-coated implants showed more rostral CTb-labeled sensory fibers, CST fibers extending along the scaffold, greater neural-cell infiltration and myelin-associated LFB signal. Fiber labeling within the scaffold indicates sprouting/extension, not proof of functional long-distance synaptic reconnection.',
    'qualitative',
    'immunostaining / histology / pathology; behavioral / functional recovery assay',
    'Full-text source localization for M5A-P045-E002 confirms the curated PLO-coated plant scaffold experiment in Rat. Methods/readouts recorded in the A-layer: PLO-coated implants showed more rostral CTb-labeled sensory fibers, CST fibers extending along the scaffold, greater neural-cell infiltration and myelin-associated LFB signal. Fiber labeling within the scaffold indicates sprouting/extension, not proof of functional long-distance synaptic reconnection.',
    'full-text source localization for m5a-p045-e002 confirms the curated plo-coated plant scaffold experiment in rat. methods/readouts recorded in the a-layer: plo-coated implants showed more rostral ctb-labeled sensory fibers, cst fibers extending along the scaffold, greater neural-cell infiltration and myelin-associated lfb signal. fiber labeling within the scaffold indicates sprouting/extension, not proof of functional long-distance synaptic reconnection.',
    'Module 5A full-text extraction; Full text PMC; tract-tracing and histology',
    'A-layer full text; Full text PMC; tract-tracing and histology',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P045-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P045-E002", "measurement_method_inference": "immunostaining / histology / pathology; behavioral / functional recovery assay", "paper_tracker_id": "M5A-P045", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T006", "tracker_id": "M5B-O092"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P045::M5A-P045-E002'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Poly-L-Ornithine coated plant scaffolds support motor recovery in rats after traumatic spinal cord injury.; first-pass row captures graft/scaffold-enabled axon repair in human / translational context at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O092', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P046-E002 confirms the curated LPS 1 microgram/ml with copalic acid 3 micromolar experiment in Mouse cell lines. Methods/readouts recorded in the A-layer: In BV2 and RAW264.7 cultures, 6-hour copalic-acid treatment reduced LPS-associated pro-inflammatory CD86, CD80, and IL-1beta expression by qPCR. This supports anti-inflammatory activity in resident-like and monocyte-derived macrophage cultures, but it does not establish that the spatially enriched Mac4 subset is the direct cellular source or that copalic acid is required for SCI recovery.',
    'qualitative',
    'qPCR / RT-PCR / mRNA assay; single-cell RNA-seq / cell-state atlas; spatial transcriptomics / spatial atlas; behavioral / functional recovery assay',
    'Full-text source localization for M5A-P046-E002 confirms the curated LPS 1 microgram/ml with copalic acid 3 micromolar experiment in Mouse cell lines. Methods/readouts recorded in the A-layer: In BV2 and RAW264.7 cultures, 6-hour copalic-acid treatment reduced LPS-associated pro-inflammatory CD86, CD80, and IL-1beta expression by qPCR. This supports anti-inflammatory activity in resident-like and monocyte-derived macrophage cultures, but it does not establish that the spatially enriched Mac4 subset is the direct cellular source or that copalic acid is required for SCI recovery.',
    'full-text source localization for m5a-p046-e002 confirms the curated lps 1 microgram/ml with copalic acid 3 micromolar experiment in mouse cell lines. methods/readouts recorded in the a-layer: in bv2 and raw264.7 cultures, 6-hour copalic-acid treatment reduced lps-associated pro-inflammatory cd86, cd80, and il-1beta expression by qpcr. this supports anti-inflammatory activity in resident-like and monocyte-derived macrophage cultures, but it does not establish that the spatially enriched mac4 subset is the direct cellular source or that copalic acid is required for sci recovery.',
    'Module 5A full-text extraction; Fig. 5 and Supplementary Fig. S8; copalic-acid inflammatory cell assay',
    'A-layer full text; Fig. 5 and Supplementary Fig. S8; copalic-acid inflammatory cell assay',
    'medium',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P046-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P046-E002", "measurement_method_inference": "qPCR / RT-PCR / mRNA assay; single-cell RNA-seq / cell-state atlas; spatial transcriptomics / spatial atlas; behavioral / functional recovery assay", "paper_tracker_id": "M5A-P046", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T003", "tracker_id": "M5B-O093"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P046::M5A-P046-E002'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Integrating single-cell RNA sequencing and spatial multi-omics reveals the molecular signature of regeneration after spinal cord injury.; first-pass row captures remyelination / white matter repair in rat sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O093', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Full-text source localization for M5A-P047-E002 confirms the curated Combination treatment as above experiment in Dog. Methods/readouts recorded in the A-layer: Treatment was associated with gradual gait improvement and appeared safe, but no blinding, no placebo group, small heterogeneous sample, and no single-agent arms prevent attribution to poly laminin versus GDNF, ChABC, injection, or continued rehabilitation.',
    'qualitative',
    NULL,
    'Full-text source localization for M5A-P047-E002 confirms the curated Combination treatment as above experiment in Dog. Methods/readouts recorded in the A-layer: Treatment was associated with gradual gait improvement and appeared safe, but no blinding, no placebo group, small heterogeneous sample, and no single-agent arms prevent attribution to poly laminin versus GDNF, ChABC, injection, or continued rehabilitation.',
    'full-text source localization for m5a-p047-e002 confirms the curated combination treatment as above experiment in dog. methods/readouts recorded in the a-layer: treatment was associated with gradual gait improvement and appeared safe, but no blinding, no placebo group, small heterogeneous sample, and no single-agent arms prevent attribution to poly laminin versus gdnf, chabc, injection, or continued rehabilitation.',
    'Module 5A full-text extraction; Full text PMC; safety and limitation assessment',
    'A-layer full text; Full text PMC; safety and limitation assessment',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 5A M5A-P047-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M5A-P047-E002", "measurement_method_inference": null, "paper_tracker_id": "M5A-P047", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M5B-T002", "tracker_id": "M5B-O094"}'
  FROM _m5_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M5A-P047::M5A-P047-E002'
    AND et.evidence_type_name = 'Axon/white-matter repair intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for A laminin-based therapy for dogs with chronic spinal cord injury: promising results of a longitudinal trial.; first-pass row captures extrinsic inhibitory matrix / guidance pathway in dog chronic sci at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m5_observation_map (tracker_id, observation_id) SELECT 'M5B-O094', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Corticospinal and descending-tract repair evidence includes regeneration, sprouting, plasticity, and functional recovery signals that should be separated.',
    'evidence standard',
    'high',
    'Module 5A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M5A-P001, P002, P006, P009-P014, P016-P021, P027, P039-P040", "topic_id": "M5B-T001", "tracker_id": "M5B-C001"}'
  FROM _m5_paper_map p
  WHERE p.tracker_id = 'M5A-P001'
  RETURNING claim_id
)
INSERT INTO _m5_claim_map (tracker_id, claim_id) SELECT 'M5B-C001', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Optogenetic, magnetic, gabapentinoid, and molecular interventions can enhance CST-related growth or plasticity in selected models.',
    'synthesis',
    'medium',
    'Module 5A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M5A-P010-P014, P020-P021", "topic_id": "M5B-T001", "tracker_id": "M5B-C002"}'
  FROM _m5_paper_map p
  WHERE p.tracker_id = 'M5A-P010'
  RETURNING claim_id
)
INSERT INTO _m5_claim_map (tracker_id, claim_id) SELECT 'M5B-C002', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'CSPG, PTP-sigma, Nogo, Rho/ROCK, netrin, integrin, and laminin pathways define extrinsic growth-permissiveness boundaries.',
    'synthesis',
    'medium',
    'Module 5A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M5A-P006, P015, P023-P027, P047", "topic_id": "M5B-T002", "tracker_id": "M5B-C003"}'
  FROM _m5_paper_map p
  WHERE p.tracker_id = 'M5A-P006'
  RETURNING claim_id
)
INSERT INTO _m5_claim_map (tracker_id, claim_id) SELECT 'M5B-C003', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Matrix/guidance interventions often overlap with immune-glial scar and Schwann/cell-therapy mechanisms.',
    'boundary condition',
    'high',
    'Module 5A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M5A-P024-P027", "topic_id": "M5B-T002", "tracker_id": "M5B-C004"}'
  FROM _m5_paper_map p
  WHERE p.tracker_id = 'M5A-P024'
  RETURNING claim_id
)
INSERT INTO _m5_claim_map (tracker_id, claim_id) SELECT 'M5B-C004', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Remyelination, myelin debris clearance, ventral-root pathology, and white matter repair form a distinct evidence family.',
    'synthesis',
    'high',
    'Module 5A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M5A-P003-P004, P028-P032, P046", "topic_id": "M5B-T003", "tracker_id": "M5B-C005"}'
  FROM _m5_paper_map p
  WHERE p.tracker_id = 'M5A-P003'
  RETURNING claim_id
)
INSERT INTO _m5_claim_map (tracker_id, claim_id) SELECT 'M5B-C005', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Myelin debris clearance can support repair but may also be linked to chronic inflammation or fibrosis.',
    'boundary condition',
    'high',
    'Module 5A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M5A-P029-P032", "topic_id": "M5B-T003", "tracker_id": "M5B-C006"}'
  FROM _m5_paper_map p
  WHERE p.tracker_id = 'M5A-P029'
  RETURNING claim_id
)
INSERT INTO _m5_claim_map (tracker_id, claim_id) SELECT 'M5B-C006', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Serotonergic, propriospinal, KCC2, and relay-pathway studies show repair can proceed via circuit reconstruction without literal CST regrowth.',
    'synthesis',
    'medium',
    'Module 5A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M5A-P020, P025, P033-P038", "topic_id": "M5B-T004", "tracker_id": "M5B-C007"}'
  FROM _m5_paper_map p
  WHERE p.tracker_id = 'M5A-P020'
  RETURNING claim_id
)
INSERT INTO _m5_claim_map (tracker_id, claim_id) SELECT 'M5B-C007', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Relay and excitability restoration endpoints should be curated separately from anatomical regeneration endpoints.',
    'evidence standard',
    'high',
    'Module 5A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M5A-P033-P038", "topic_id": "M5B-T004", "tracker_id": "M5B-C008"}'
  FROM _m5_paper_map p
  WHERE p.tracker_id = 'M5A-P033'
  RETURNING claim_id
)
INSERT INTO _m5_claim_map (tracker_id, claim_id) SELECT 'M5B-C008', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Intrinsic growth competence includes cellular energetics, transcriptional state, ciliogenesis, PTEN/mTOR, and maturation-linked epigenetic programs.',
    'synthesis',
    'medium',
    'Module 5A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M5A-P005, P008, P011, P018-P019, P043-P044", "topic_id": "M5B-T005", "tracker_id": "M5B-C009"}'
  FROM _m5_paper_map p
  WHERE p.tracker_id = 'M5A-P005'
  RETURNING claim_id
)
INSERT INTO _m5_claim_map (tracker_id, claim_id) SELECT 'M5B-C009', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Intrinsic-growth claims need neuron-type specificity and distinction between sprouting, regeneration, and survival.',
    'boundary condition',
    'high',
    'Module 5A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M5A-P018-P019, P043-P044", "topic_id": "M5B-T005", "tracker_id": "M5B-C010"}'
  FROM _m5_paper_map p
  WHERE p.tracker_id = 'M5A-P018'
  RETURNING claim_id
)
INSERT INTO _m5_claim_map (tracker_id, claim_id) SELECT 'M5B-C010', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Grafts, scaffolds, laminin, Schwann/cell products, and biomaterials can enable axon repair but confound cell/material/molecular attribution.',
    'boundary condition',
    'high',
    'Module 5A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M5A-P001, P007, P028, P041-P042, P045, P047", "topic_id": "M5B-T006", "tracker_id": "M5B-C011"}'
  FROM _m5_paper_map p
  WHERE p.tracker_id = 'M5A-P001'
  RETURNING claim_id
)
INSERT INTO _m5_claim_map (tracker_id, claim_id) SELECT 'M5B-C011', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Graft-enabled CST regeneration should be cross-tagged with Module 4 transplantation and Module 2 biomaterials.',
    'curation rule',
    'high',
    'Module 5A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M5A-P007, P041-P042", "topic_id": "M5B-T006", "tracker_id": "M5B-C012"}'
  FROM _m5_paper_map p
  WHERE p.tracker_id = 'M5A-P007'
  RETURNING claim_id
)
INSERT INTO _m5_claim_map (tracker_id, claim_id) SELECT 'M5B-C012', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Activity, stimulation, and training can amplify molecular repair programs and should be treated as combination interventions.',
    'synthesis',
    'medium',
    'Module 5A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M5A-P012, P020-P021, P039-P040", "topic_id": "M5B-T007", "tracker_id": "M5B-C013"}'
  FROM _m5_paper_map p
  WHERE p.tracker_id = 'M5A-P012'
  RETURNING claim_id
)
INSERT INTO _m5_claim_map (tracker_id, claim_id) SELECT 'M5B-C013', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Treadmill/OPN/IGF-1R/Akt/mTOR evidence bridges intrinsic growth and activity-dependent plasticity.',
    'implication',
    'medium',
    'Module 5A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M5A-P039-P040", "topic_id": "M5B-T007", "tracker_id": "M5B-C014"}'
  FROM _m5_paper_map p
  WHERE p.tracker_id = 'M5A-P039'
  RETURNING claim_id
)
INSERT INTO _m5_claim_map (tracker_id, claim_id) SELECT 'M5B-C014', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Module 5 consensus must distinguish CST, RST, sensory, propriospinal, serotonergic, and white matter endpoints.',
    'synthesis rule',
    'high',
    'Module 5A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M5A-P001-M5A-P047", "topic_id": "M5B-T008", "tracker_id": "M5B-C015"}'
  FROM _m5_paper_map p
  WHERE p.tracker_id = 'M5A-P001'
  RETURNING claim_id
)
INSERT INTO _m5_claim_map (tracker_id, claim_id) SELECT 'M5B-C015', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Functional recovery does not by itself identify whether repair occurred through regeneration, sprouting, remyelination, relay, or compensation.',
    'boundary condition',
    'high',
    'Module 5A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M5A-P001-M5A-P047", "topic_id": "M5B-T008", "tracker_id": "M5B-C016"}'
  FROM _m5_paper_map p
  WHERE p.tracker_id = 'M5A-P001'
  RETURNING claim_id
)
INSERT INTO _m5_claim_map (tracker_id, claim_id) SELECT 'M5B-C016', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'The saturated 5A corpus supports mechanism-family consensus profiles rather than one pooled axon-regeneration efficacy claim.',
    'synthesis',
    'high',
    'Module 5A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M5A-P001-M5A-P047", "topic_id": "M5B-T008", "tracker_id": "M5B-C017"}'
  FROM _m5_paper_map p
  WHERE p.tracker_id = 'M5A-P001'
  RETURNING claim_id
)
INSERT INTO _m5_claim_map (tracker_id, claim_id) SELECT 'M5B-C017', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Human ventral-root and motoneuron pathology should constrain translation from rodent remyelination and axon-repair models.',
    'boundary condition',
    'medium',
    'Module 5A full-text extraction; Full text PMC; ventral-root histology; Full text PMC; myelin g-ratio analysis',
    'high',
    '{"curator_notes": "Full-text provenance localized; author-claim wording retained and no new claim added.", "source_paper_tracker_id": "M5A-P004", "topic_id": "M5B-T003", "tracker_id": "M5B-C018"}'
  FROM _m5_paper_map p
  WHERE p.tracker_id = 'M5A-P004'
  RETURNING claim_id
)
INSERT INTO _m5_claim_map (tracker_id, claim_id) SELECT 'M5B-C018', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Netrin/DCC and NgR/RhoA/ROCK evidence should be curated as guidance plus inhibitory-pathway modulation.',
    'curation rule',
    'medium',
    'Module 5A full-text extraction; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance localized; author-claim wording retained and no new claim added.", "source_paper_tracker_id": "M5A-P023", "topic_id": "M5B-T002", "tracker_id": "M5B-C019"}'
  FROM _m5_paper_map p
  WHERE p.tracker_id = 'M5A-P023'
  RETURNING claim_id
)
INSERT INTO _m5_claim_map (tracker_id, claim_id) SELECT 'M5B-C019', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Propriospinal detours and KCC2-enabled relay pathways are circuit-level repair mechanisms.',
    'mechanistic',
    'medium',
    'Module 5A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M5A-P035-P036", "topic_id": "M5B-T004", "tracker_id": "M5B-C020"}'
  FROM _m5_paper_map p
  WHERE p.tracker_id = 'M5A-P035'
  RETURNING claim_id
)
INSERT INTO _m5_claim_map (tracker_id, claim_id) SELECT 'M5B-C020', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'TTBK2-driven ciliogenesis is a candidate intrinsic neuronal regeneration program.',
    'mechanistic',
    'low',
    'Module 5A full-text extraction; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance localized; author-claim wording retained and no new claim added.", "source_paper_tracker_id": "M5A-P018", "topic_id": "M5B-T005", "tracker_id": "M5B-C021"}'
  FROM _m5_paper_map p
  WHERE p.tracker_id = 'M5A-P018'
  RETURNING claim_id
)
INSERT INTO _m5_claim_map (tracker_id, claim_id) SELECT 'M5B-C021', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'CITED2 links neuronal maturation to regenerative decline and is a candidate epigenetic repair switch.',
    'mechanistic',
    'low',
    'Module 5A full-text extraction; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance localized; author-claim wording retained and no new claim added.", "source_paper_tracker_id": "M5A-P044", "topic_id": "M5B-T005", "tracker_id": "M5B-C022"}'
  FROM _m5_paper_map p
  WHERE p.tracker_id = 'M5A-P044'
  RETURNING claim_id
)
INSERT INTO _m5_claim_map (tracker_id, claim_id) SELECT 'M5B-C022', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Lesion-remote astrocyte-microglia control of white matter repair cross-links Module 5 with Module 3.',
    'implication',
    'medium',
    'Module 5A full-text extraction; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance localized; author-claim wording retained and no new claim added.", "source_paper_tracker_id": "M5A-P030", "topic_id": "M5B-T003", "tracker_id": "M5B-C023"}'
  FROM _m5_paper_map p
  WHERE p.tracker_id = 'M5A-P030'
  RETURNING claim_id
)
INSERT INTO _m5_claim_map (tracker_id, claim_id) SELECT 'M5B-C023', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Oligodendrogenic progenitors plus chondroitinase ABC cross-link remyelination, inhibitory matrix digestion, and cell transplantation.',
    'boundary condition',
    'medium',
    'Module 5A full-text extraction; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance localized; author-claim wording retained and no new claim added.", "source_paper_tracker_id": "M5A-P028", "topic_id": "M5B-T006", "tracker_id": "M5B-C024"}'
  FROM _m5_paper_map p
  WHERE p.tracker_id = 'M5A-P028'
  RETURNING claim_id
)
INSERT INTO _m5_claim_map (tracker_id, claim_id) SELECT 'M5B-C024', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Thiorphan-like neuronal reprogramming suggests pharmacologic growth-state manipulation can improve functional recovery.',
    'implication',
    'low',
    'Module 5A full-text extraction; Fig. 1c-e; adult mouse motor cortex screen; Fig. 2-3; severe bilateral C5 contusion and NPC graft experiment; Fig. 4a-i; primate and human cortical cultures plus rat cortical mechanism assay',
    'medium',
    '{"curator_notes": "Full-text provenance localized; author-claim wording retained and no new claim added.", "source_paper_tracker_id": "M5A-P017", "topic_id": "M5B-T001", "tracker_id": "M5B-C025"}'
  FROM _m5_paper_map p
  WHERE p.tracker_id = 'M5A-P017'
  RETURNING claim_id
)
INSERT INTO _m5_claim_map (tracker_id, claim_id) SELECT 'M5B-C025', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Large-animal laminin therapy supports translational relevance but should remain feasibility/context evidence until full endpoints are extracted.',
    'boundary condition',
    'medium',
    'Module 5A full-text extraction; Full text PMC; prospective longitudinal trial; Full text PMC; safety and limitation assessment',
    'high',
    '{"curator_notes": "Full-text provenance localized; author-claim wording retained and no new claim added.", "source_paper_tracker_id": "M5A-P047", "topic_id": "M5B-T002", "tracker_id": "M5B-C026"}'
  FROM _m5_paper_map p
  WHERE p.tracker_id = 'M5A-P047'
  RETURNING claim_id
)
INSERT INTO _m5_claim_map (tracker_id, claim_id) SELECT 'M5B-C026', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Female-rat TMS evidence should retain sex/model details in the outcome vocabulary.',
    'curation rule',
    'medium',
    'Module 5A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M5A-P012", "topic_id": "M5B-T007", "tracker_id": "M5B-C027"}'
  FROM _m5_paper_map p
  WHERE p.tracker_id = 'M5A-P012'
  RETURNING claim_id
)
INSERT INTO _m5_claim_map (tracker_id, claim_id) SELECT 'M5B-C027', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Single-cell regeneration signatures are mapping evidence unless tied to perturbation and tract-specific outcomes.',
    'evidence standard',
    'high',
    'Module 5A full-text extraction; Fig. 1-6; scRNA-seq, spatial transcriptomics, and spatial metabolomics atlas; Fig. 5 and Supplementary Fig. S8; copalic-acid inflammatory cell assay; Fig. 5e and Supplementary Fig. S8b; copalic-acid SCI validation; Fig. 6-7 and Supplementary Fig. S10; Fib4/IGF2 validation',
    'medium',
    '{"curator_notes": "Full-text provenance localized; author-claim wording retained and no new claim added.", "source_paper_tracker_id": "M5A-P046", "topic_id": "M5B-T008", "tracker_id": "M5B-C028"}'
  FROM _m5_paper_map p
  WHERE p.tracker_id = 'M5A-P046'
  RETURNING claim_id
)
INSERT INTO _m5_claim_map (tracker_id, claim_id) SELECT 'M5B-C028', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Remyelination-deficient models help separate compensation from true myelin repair.',
    'evidence standard',
    'medium',
    'Module 5A full-text extraction; Full text PMC; severe injury cohort; Full text PMC; moderate injury physiology and gait cohort',
    'high',
    '{"curator_notes": "Full-text provenance localized; author-claim wording retained and no new claim added.", "source_paper_tracker_id": "M5A-P031", "topic_id": "M5B-T003", "tracker_id": "M5B-C029"}'
  FROM _m5_paper_map p
  WHERE p.tracker_id = 'M5A-P031'
  RETURNING claim_id
)
INSERT INTO _m5_claim_map (tracker_id, claim_id) SELECT 'M5B-C029', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Cellular energetics is a core intrinsic-growth axis and should not be merged with trophic support alone.',
    'curation rule',
    'medium',
    'Module 5A full-text extraction; Full text PMC; C5 dorsal hemisection; Full text PMC; T8 transection and creatine/DREADD assays',
    'high',
    '{"curator_notes": "Full-text provenance localized; author-claim wording retained and no new claim added.", "source_paper_tracker_id": "M5A-P005", "topic_id": "M5B-T005", "tracker_id": "M5B-C030"}'
  FROM _m5_paper_map p
  WHERE p.tracker_id = 'M5A-P005'
  RETURNING claim_id
)
INSERT INTO _m5_claim_map (tracker_id, claim_id) SELECT 'M5B-C030', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Scaffold-supported motor recovery requires material, tract, and behavioral endpoint separation.',
    'boundary condition',
    'medium',
    'Module 5A full-text extraction; Full text PMC; Fig. 1-2; Full text PMC; tract-tracing and histology',
    'high',
    '{"curator_notes": "Full-text provenance localized; author-claim wording retained and no new claim added.", "source_paper_tracker_id": "M5A-P045", "topic_id": "M5B-T006", "tracker_id": "M5B-C031"}'
  FROM _m5_paper_map p
  WHERE p.tracker_id = 'M5A-P045'
  RETURNING claim_id
)
INSERT INTO _m5_claim_map (tracker_id, claim_id) SELECT 'M5B-C031', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Full-text upgrades should prioritize anchors that directly test tract anatomy alongside functional behavior.',
    'curation boundary',
    'high',
    'Module 5A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M5A-P001-M5A-P047", "topic_id": "M5B-T008", "tracker_id": "M5B-C032"}'
  FROM _m5_paper_map p
  WHERE p.tracker_id = 'M5A-P001'
  RETURNING claim_id
)
INSERT INTO _m5_claim_map (tracker_id, claim_id) SELECT 'M5B-C032', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Synaptotagmin 4 supports spontaneous sprouting and should be distinguished from experimentally induced regeneration.',
    'mechanistic',
    'medium',
    'Module 5A full-text extraction; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance localized; author-claim wording retained and no new claim added.", "source_paper_tracker_id": "M5A-P013", "topic_id": "M5B-T001", "tracker_id": "M5B-C033"}'
  FROM _m5_paper_map p
  WHERE p.tracker_id = 'M5A-P013'
  RETURNING claim_id
)
INSERT INTO _m5_claim_map (tracker_id, claim_id) SELECT 'M5B-C033', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Serotonergic-targeted hydrogel evidence cross-links circuit excitability and biomaterial delivery.',
    'boundary condition',
    'medium',
    'Module 5A full-text extraction; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance localized; author-claim wording retained and no new claim added.", "source_paper_tracker_id": "M5A-P033", "topic_id": "M5B-T004", "tracker_id": "M5B-C034"}'
  FROM _m5_paper_map p
  WHERE p.tracker_id = 'M5A-P033'
  RETURNING claim_id
)
INSERT INTO _m5_claim_map (tracker_id, claim_id) SELECT 'M5B-C034', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Species and chronicity boundaries are essential before comparing chronic scar, acute injury, dog, human pathology, and rodent repair models.',
    'boundary condition',
    'high',
    'Module 5A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M5A-P001-M5A-P047", "topic_id": "M5B-T008", "tracker_id": "M5B-C035"}'
  FROM _m5_paper_map p
  WHERE p.tracker_id = 'M5A-P001'
  RETURNING claim_id
)
INSERT INTO _m5_claim_map (tracker_id, claim_id) SELECT 'M5B-C035', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Consensus wording should avoid treating all axon growth, remyelination, and circuit compensation as the same repair process.',
    'synthesis rule',
    'high',
    'Module 5A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M5A-P001-M5A-P047", "topic_id": "M5B-T008", "tracker_id": "M5B-C036"}'
  FROM _m5_paper_map p
  WHERE p.tracker_id = 'M5A-P001'
  RETURNING claim_id
)
INSERT INTO _m5_claim_map (tracker_id, claim_id) SELECT 'M5B-C036', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M5B-L001"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O001'
  WHERE c.tracker_id = 'M5B-C001'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L001', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M5B-L002"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O010'
  WHERE c.tracker_id = 'M5B-C002'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L002', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M5B-L003"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O006'
  WHERE c.tracker_id = 'M5B-C003'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L003', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M5B-L004"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O024'
  WHERE c.tracker_id = 'M5B-C004'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L004', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M5B-L005"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O003'
  WHERE c.tracker_id = 'M5B-C005'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L005', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M5B-L006"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O029'
  WHERE c.tracker_id = 'M5B-C006'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L006', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M5B-L007"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O020'
  WHERE c.tracker_id = 'M5B-C007'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L007', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M5B-L008"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O033'
  WHERE c.tracker_id = 'M5B-C008'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L008', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M5B-L009"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O005'
  WHERE c.tracker_id = 'M5B-C009'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L009', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M5B-L010"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O018'
  WHERE c.tracker_id = 'M5B-C010'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L010', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M5B-L011"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O001'
  WHERE c.tracker_id = 'M5B-C011'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L011', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M5B-L012"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O007'
  WHERE c.tracker_id = 'M5B-C012'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L012', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M5B-L013"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O012'
  WHERE c.tracker_id = 'M5B-C013'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L013', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M5B-L014"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O039'
  WHERE c.tracker_id = 'M5B-C014'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L014', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M5B-L015"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O001'
  WHERE c.tracker_id = 'M5B-C015'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L015', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M5B-L016"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O001'
  WHERE c.tracker_id = 'M5B-C016'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L016', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M5B-L017"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O001'
  WHERE c.tracker_id = 'M5B-C017'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L017', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M5B-L018"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O004'
  WHERE c.tracker_id = 'M5B-C018'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L018', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M5B-L019"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O023'
  WHERE c.tracker_id = 'M5B-C019'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L019', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M5B-L020"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O035'
  WHERE c.tracker_id = 'M5B-C020'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L020', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M5B-L021"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O018'
  WHERE c.tracker_id = 'M5B-C021'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L021', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M5B-L022"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O044'
  WHERE c.tracker_id = 'M5B-C022'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L022', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M5B-L023"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O030'
  WHERE c.tracker_id = 'M5B-C023'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L023', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M5B-L024"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O028'
  WHERE c.tracker_id = 'M5B-C024'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L024', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M5B-L025"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O017'
  WHERE c.tracker_id = 'M5B-C025'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L025', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M5B-L026"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O047'
  WHERE c.tracker_id = 'M5B-C026'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L026', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M5B-L027"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O012'
  WHERE c.tracker_id = 'M5B-C027'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L027', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M5B-L028"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O046'
  WHERE c.tracker_id = 'M5B-C028'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L028', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M5B-L029"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O031'
  WHERE c.tracker_id = 'M5B-C029'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L029', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M5B-L030"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O005'
  WHERE c.tracker_id = 'M5B-C030'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L030', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M5B-L031"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O045'
  WHERE c.tracker_id = 'M5B-C031'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L031', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M5B-L032"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O010'
  WHERE c.tracker_id = 'M5B-C032'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L032', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M5B-L033"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O013'
  WHERE c.tracker_id = 'M5B-C033'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L033', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M5B-L034"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O033'
  WHERE c.tracker_id = 'M5B-C034'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L034', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M5B-L035"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O001'
  WHERE c.tracker_id = 'M5B-C035'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L035', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M5B-L036"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O001'
  WHERE c.tracker_id = 'M5B-C036'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L036', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'corroborates',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M5B-L037"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O002'
  WHERE c.tracker_id = 'M5B-C001'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L037', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'corroborates',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M5B-L038"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O006'
  WHERE c.tracker_id = 'M5B-C001'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L038', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'corroborates',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M5B-L039"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O009'
  WHERE c.tracker_id = 'M5B-C001'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L039', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'corroborates',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M5B-L040"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O010'
  WHERE c.tracker_id = 'M5B-C001'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L040', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'corroborates',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M5B-L041"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O011'
  WHERE c.tracker_id = 'M5B-C001'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L041', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'corroborates',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M5B-L042"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O012'
  WHERE c.tracker_id = 'M5B-C001'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L042', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'corroborates',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M5B-L043"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O013'
  WHERE c.tracker_id = 'M5B-C001'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L043', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'corroborates',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M5B-L044"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O014'
  WHERE c.tracker_id = 'M5B-C001'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L044', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'corroborates',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M5B-L045"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O016'
  WHERE c.tracker_id = 'M5B-C001'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L045', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'corroborates',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M5B-L046"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O017'
  WHERE c.tracker_id = 'M5B-C001'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L046', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'corroborates',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M5B-L047"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O020'
  WHERE c.tracker_id = 'M5B-C001'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L047', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'corroborates',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M5B-L048"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O021'
  WHERE c.tracker_id = 'M5B-C001'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L048', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'corroborates',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M5B-L049"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O027'
  WHERE c.tracker_id = 'M5B-C001'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L049', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'corroborates',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M5B-L050"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O039'
  WHERE c.tracker_id = 'M5B-C001'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L050', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'corroborates',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M5B-L051"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O040'
  WHERE c.tracker_id = 'M5B-C001'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L051', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'corroborates',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M5B-L052"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O012'
  WHERE c.tracker_id = 'M5B-C002'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L052', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'corroborates',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M5B-L053"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O013'
  WHERE c.tracker_id = 'M5B-C002'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L053', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'corroborates',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M5B-L054"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O014'
  WHERE c.tracker_id = 'M5B-C002'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L054', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'corroborates',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M5B-L055"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O020'
  WHERE c.tracker_id = 'M5B-C002'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L055', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'corroborates',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M5B-L056"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O021'
  WHERE c.tracker_id = 'M5B-C002'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L056', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'corroborates',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M5B-L057"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O015'
  WHERE c.tracker_id = 'M5B-C003'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L057', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'corroborates',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M5B-L058"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O023'
  WHERE c.tracker_id = 'M5B-C003'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L058', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'corroborates',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M5B-L059"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O024'
  WHERE c.tracker_id = 'M5B-C003'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L059', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'corroborates',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M5B-L060"}'
  FROM _m5_claim_map c
  JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O025'
  WHERE c.tracker_id = 'M5B-C003'
  RETURNING link_id
)
INSERT INTO _m5_link_map (tracker_id, link_id) SELECT 'M5B-L060', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Descending-tract repair claims must specify whether the evidence shows true long-distance regeneration, local sprouting, spared-tract plasticity, relay engagement, or behavioral association; these outcomes should not be collapsed into one regeneration label.',
    'M5B-T001',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M5B-B001", "M5B-B008"], "claim_tracker_ids": ["M5B-C001", "M5B-C002", "M5B-C025", "M5B-C033"], "consensus_draft_id": "M5B-S001", "observation_tracker_ids": ["M5B-O001", "M5B-O002", "M5B-O006", "M5B-O009", "M5B-O010", "M5B-O011", "M5B-O012", "M5B-O013", "M5B-O014", "M5B-O016", "M5B-O017", "M5B-O018", "M5B-O019", "M5B-O020", "M5B-O021", "M5B-O027", "M5B-O039", "M5B-O040"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "B001, B008", "topic_id": "M5B-T001"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m5_consensus_map (tracker_id, consensus_id) SELECT 'M5B-S001', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O001'
WHERE c.tracker_id = 'M5B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O002'
WHERE c.tracker_id = 'M5B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O006'
WHERE c.tracker_id = 'M5B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O009'
WHERE c.tracker_id = 'M5B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O010'
WHERE c.tracker_id = 'M5B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O011'
WHERE c.tracker_id = 'M5B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O012'
WHERE c.tracker_id = 'M5B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O013'
WHERE c.tracker_id = 'M5B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O014'
WHERE c.tracker_id = 'M5B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O016'
WHERE c.tracker_id = 'M5B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O017'
WHERE c.tracker_id = 'M5B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O018'
WHERE c.tracker_id = 'M5B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O019'
WHERE c.tracker_id = 'M5B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O020'
WHERE c.tracker_id = 'M5B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O021'
WHERE c.tracker_id = 'M5B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O027'
WHERE c.tracker_id = 'M5B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O039'
WHERE c.tracker_id = 'M5B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O040'
WHERE c.tracker_id = 'M5B-S001';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Extrinsic matrix, CSPG/Nogo/Rho/ROCK, and guidance-pathway interventions define environmental permissiveness, but their effects overlap with scar architecture, immune state, graft support, and tract-specific growth competence.',
    'M5B-T002',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M5B-B002", "M5B-B005", "M5B-B008"], "claim_tracker_ids": ["M5B-C003", "M5B-C004", "M5B-C019", "M5B-C026"], "consensus_draft_id": "M5B-S002", "observation_tracker_ids": ["M5B-O006", "M5B-O015", "M5B-O023", "M5B-O024", "M5B-O025", "M5B-O026", "M5B-O027", "M5B-O047"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "B002, B005, B008", "topic_id": "M5B-T002"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m5_consensus_map (tracker_id, consensus_id) SELECT 'M5B-S002', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O006'
WHERE c.tracker_id = 'M5B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O015'
WHERE c.tracker_id = 'M5B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O023'
WHERE c.tracker_id = 'M5B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O024'
WHERE c.tracker_id = 'M5B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O025'
WHERE c.tracker_id = 'M5B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O026'
WHERE c.tracker_id = 'M5B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O027'
WHERE c.tracker_id = 'M5B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O047'
WHERE c.tracker_id = 'M5B-S002';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Remyelination, oligodendrocyte lineage repair, myelin-debris clearance, and white-matter preservation are a distinct repair axis from axon regrowth; consensus statements should retain myelin, axon, glial, and functional endpoints separately.',
    'M5B-T003',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M5B-B003", "M5B-B006", "M5B-B008"], "claim_tracker_ids": ["M5B-C005", "M5B-C006", "M5B-C018", "M5B-C023", "M5B-C024", "M5B-C029"], "consensus_draft_id": "M5B-S003", "observation_tracker_ids": ["M5B-O003", "M5B-O004", "M5B-O028", "M5B-O029", "M5B-O030", "M5B-O031", "M5B-O032", "M5B-O046"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "B003, B006, B008", "topic_id": "M5B-T003"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m5_consensus_map (tracker_id, consensus_id) SELECT 'M5B-S003', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O003'
WHERE c.tracker_id = 'M5B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O004'
WHERE c.tracker_id = 'M5B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O028'
WHERE c.tracker_id = 'M5B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O029'
WHERE c.tracker_id = 'M5B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O030'
WHERE c.tracker_id = 'M5B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O031'
WHERE c.tracker_id = 'M5B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O032'
WHERE c.tracker_id = 'M5B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O046'
WHERE c.tracker_id = 'M5B-S003';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Serotonergic, propriospinal, relay, KCC2, and circuit-rebalancing mechanisms support recovery through network reconstruction and plasticity, which may complement or substitute for direct long-tract regeneration depending on lesion completeness and target behavior.',
    'M5B-T004',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M5B-B004", "M5B-B008"], "claim_tracker_ids": ["M5B-C007", "M5B-C008", "M5B-C020", "M5B-C034"], "consensus_draft_id": "M5B-S004", "observation_tracker_ids": ["M5B-O020", "M5B-O025", "M5B-O033", "M5B-O034", "M5B-O035", "M5B-O036", "M5B-O037", "M5B-O038"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "B004, B008", "topic_id": "M5B-T004"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m5_consensus_map (tracker_id, consensus_id) SELECT 'M5B-S004', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O020'
WHERE c.tracker_id = 'M5B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O025'
WHERE c.tracker_id = 'M5B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O033'
WHERE c.tracker_id = 'M5B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O034'
WHERE c.tracker_id = 'M5B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O035'
WHERE c.tracker_id = 'M5B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O036'
WHERE c.tracker_id = 'M5B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O037'
WHERE c.tracker_id = 'M5B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O038'
WHERE c.tracker_id = 'M5B-S004';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Neuron-intrinsic growth competence spans metabolic, transcriptional, epigenetic, PTEN/mTOR, SOCS3/STAT, and ciliogenesis programs; these should be interpreted separately from environmental permissiveness unless the experiment tests both axes.',
    'M5B-T005',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M5B-B002", "M5B-B008"], "claim_tracker_ids": ["M5B-C009", "M5B-C010", "M5B-C021", "M5B-C022", "M5B-C030"], "consensus_draft_id": "M5B-S005", "observation_tracker_ids": ["M5B-O005", "M5B-O008", "M5B-O011", "M5B-O018", "M5B-O019", "M5B-O043", "M5B-O044"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "B002, B008", "topic_id": "M5B-T005"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m5_consensus_map (tracker_id, consensus_id) SELECT 'M5B-S005', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O005'
WHERE c.tracker_id = 'M5B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O008'
WHERE c.tracker_id = 'M5B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O011'
WHERE c.tracker_id = 'M5B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O018'
WHERE c.tracker_id = 'M5B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O019'
WHERE c.tracker_id = 'M5B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O043'
WHERE c.tracker_id = 'M5B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O044'
WHERE c.tracker_id = 'M5B-S005';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Graft- and scaffold-enabled axon repair is a combination-intervention family: axon growth claims should be cross-tagged with cell source, biomaterial architecture, trophic/cargo support, host lesion state, and whether axons enter, traverse, or exit the graft.',
    'M5B-T006',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M5B-B005", "M5B-B007", "M5B-B008"], "claim_tracker_ids": ["M5B-C011", "M5B-C012", "M5B-C024", "M5B-C031"], "consensus_draft_id": "M5B-S006", "observation_tracker_ids": ["M5B-O001", "M5B-O007", "M5B-O028", "M5B-O041", "M5B-O042", "M5B-O045", "M5B-O047"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "B005, B007, B008", "topic_id": "M5B-T006"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m5_consensus_map (tracker_id, consensus_id) SELECT 'M5B-S006', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O001'
WHERE c.tracker_id = 'M5B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O007'
WHERE c.tracker_id = 'M5B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O028'
WHERE c.tracker_id = 'M5B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O041'
WHERE c.tracker_id = 'M5B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O042'
WHERE c.tracker_id = 'M5B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O045'
WHERE c.tracker_id = 'M5B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O047'
WHERE c.tracker_id = 'M5B-S006';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Activity, stimulation, training, and neuromodulation can amplify repair-associated plasticity, but they should be modeled as timing- and dose-dependent combination axes rather than evidence that the paired biologic intervention works alone.',
    'M5B-T007',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M5B-B001", "M5B-B005", "M5B-B008"], "claim_tracker_ids": ["M5B-C013", "M5B-C014", "M5B-C027"], "consensus_draft_id": "M5B-S007", "observation_tracker_ids": ["M5B-O012", "M5B-O020", "M5B-O021", "M5B-O039", "M5B-O040"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "B001, B005, B008", "topic_id": "M5B-T007"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m5_consensus_map (tracker_id, consensus_id) SELECT 'M5B-S007', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O012'
WHERE c.tracker_id = 'M5B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O020'
WHERE c.tracker_id = 'M5B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O021'
WHERE c.tracker_id = 'M5B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O039'
WHERE c.tracker_id = 'M5B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O040'
WHERE c.tracker_id = 'M5B-S007';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Module 5 consensus should separate tract class, growth mechanism, myelin/white-matter repair, circuit compensation, intrinsic growth state, combination therapy, species, chronicity, and endpoint rather than producing a single axon-regeneration efficacy summary.',
    'M5B-T008',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["all boundary records"], "claim_tracker_ids": ["M5B-C015", "M5B-C016", "M5B-C017", "M5B-C028", "M5B-C032", "M5B-C035", "M5B-C036"], "consensus_draft_id": "M5B-S008", "observation_tracker_ids": ["M5B-O001", "M5B-O002", "M5B-O003", "M5B-O004", "M5B-O005", "M5B-O006", "M5B-O007", "M5B-O008", "M5B-O009", "M5B-O010", "M5B-O011", "M5B-O012", "M5B-O013", "M5B-O014", "M5B-O015", "M5B-O016", "M5B-O017", "M5B-O018", "M5B-O019", "M5B-O020", "M5B-O021", "M5B-O022", "M5B-O023", "M5B-O024", "M5B-O025", "M5B-O026", "M5B-O027", "M5B-O028", "M5B-O029", "M5B-O030", "M5B-O031", "M5B-O032", "M5B-O033", "M5B-O034", "M5B-O035", "M5B-O036", "M5B-O037", "M5B-O038", "M5B-O039", "M5B-O040", "M5B-O041", "M5B-O042", "M5B-O043", "M5B-O044", "M5B-O045", "M5B-O046", "M5B-O047"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "all boundary records", "topic_id": "M5B-T008"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m5_consensus_map (tracker_id, consensus_id) SELECT 'M5B-S008', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O001'
WHERE c.tracker_id = 'M5B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O002'
WHERE c.tracker_id = 'M5B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O003'
WHERE c.tracker_id = 'M5B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O004'
WHERE c.tracker_id = 'M5B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O005'
WHERE c.tracker_id = 'M5B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O006'
WHERE c.tracker_id = 'M5B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O007'
WHERE c.tracker_id = 'M5B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O008'
WHERE c.tracker_id = 'M5B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O009'
WHERE c.tracker_id = 'M5B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O010'
WHERE c.tracker_id = 'M5B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O011'
WHERE c.tracker_id = 'M5B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O012'
WHERE c.tracker_id = 'M5B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O013'
WHERE c.tracker_id = 'M5B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O014'
WHERE c.tracker_id = 'M5B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O015'
WHERE c.tracker_id = 'M5B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O016'
WHERE c.tracker_id = 'M5B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O017'
WHERE c.tracker_id = 'M5B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O018'
WHERE c.tracker_id = 'M5B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O019'
WHERE c.tracker_id = 'M5B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O020'
WHERE c.tracker_id = 'M5B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O021'
WHERE c.tracker_id = 'M5B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O022'
WHERE c.tracker_id = 'M5B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O023'
WHERE c.tracker_id = 'M5B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O024'
WHERE c.tracker_id = 'M5B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O025'
WHERE c.tracker_id = 'M5B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O026'
WHERE c.tracker_id = 'M5B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O027'
WHERE c.tracker_id = 'M5B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O028'
WHERE c.tracker_id = 'M5B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O029'
WHERE c.tracker_id = 'M5B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O030'
WHERE c.tracker_id = 'M5B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O031'
WHERE c.tracker_id = 'M5B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O032'
WHERE c.tracker_id = 'M5B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O033'
WHERE c.tracker_id = 'M5B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O034'
WHERE c.tracker_id = 'M5B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O035'
WHERE c.tracker_id = 'M5B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O036'
WHERE c.tracker_id = 'M5B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O037'
WHERE c.tracker_id = 'M5B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O038'
WHERE c.tracker_id = 'M5B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O039'
WHERE c.tracker_id = 'M5B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O040'
WHERE c.tracker_id = 'M5B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O041'
WHERE c.tracker_id = 'M5B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O042'
WHERE c.tracker_id = 'M5B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O043'
WHERE c.tracker_id = 'M5B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O044'
WHERE c.tracker_id = 'M5B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O045'
WHERE c.tracker_id = 'M5B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O046'
WHERE c.tracker_id = 'M5B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m5_consensus_map c
JOIN _m5_observation_map o ON o.tracker_id = 'M5B-O047'
WHERE c.tracker_id = 'M5B-S008';

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
  SELECT COUNT(*) INTO paper_count FROM _m5_paper_map;
  SELECT COUNT(*) INTO experiment_count FROM _m5_experiment_map;
  SELECT COUNT(*) INTO observation_count FROM _m5_observation_map;
  SELECT COUNT(*) INTO claim_count FROM _m5_claim_map;
  SELECT COUNT(*) INTO link_count FROM _m5_link_map;
  SELECT COUNT(*) INTO consensus_count FROM _m5_consensus_map;
  SELECT COUNT(*) INTO consensus_observation_count
  FROM Consensus_Observation co
  JOIN _m5_consensus_map cm ON cm.consensus_id = co.consensus_id;
  IF paper_count <> 47 THEN RAISE EXCEPTION 'Expected 47 papers, found %', paper_count; END IF;
  IF experiment_count <> 94 THEN RAISE EXCEPTION 'Unexpected experiment count %', experiment_count; END IF;
  IF observation_count <> 94 THEN RAISE EXCEPTION 'Expected 94 observations, found %', observation_count; END IF;
  IF claim_count <> 36 THEN RAISE EXCEPTION 'Expected 36 claims, found %', claim_count; END IF;
  IF link_count <> 60 THEN RAISE EXCEPTION 'Expected 60 evidence links, found %', link_count; END IF;
  IF consensus_count <> 8 THEN RAISE EXCEPTION 'Expected 8 consensus rows, found %', consensus_count; END IF;
  IF consensus_observation_count <> 108 THEN RAISE EXCEPTION 'Unexpected consensus-observation count %', consensus_observation_count; END IF;
END $$;

COMMIT;
