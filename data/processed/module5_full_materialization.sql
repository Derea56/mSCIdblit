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
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Chronic scar axon-regeneration anchor", "module": "Module 5B", "tracker_id": "M5A-P001"}'
  )
  RETURNING paper_id
)
INSERT INTO _m5_paper_map (tracker_id, paper_id) SELECT 'M5A-P001', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Reducing Pericyte-Derived Scarring Promotes Recovery after Spinal Cord Injury', 'Dias DO', 2018,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
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
    NULL, NULL, NULL,
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
    NULL, NULL, NULL,
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
    NULL, NULL, NULL,
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
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "CSPG-receptor pathway anchor", "module": "Module 5B", "tracker_id": "M5A-P006"}'
  )
  RETURNING paper_id
)
INSERT INTO _m5_paper_map (tracker_id, paper_id) SELECT 'M5A-P006', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Spinal cord reconstitution with homologous neural grafts enables robust corticospinal regeneration', 'Kadoya K', 2016,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
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
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Transcriptional growth-state anchor", "module": "Module 5B", "tracker_id": "M5A-P008"}'
  )
  RETURNING paper_id
)
INSERT INTO _m5_paper_map (tracker_id, paper_id) SELECT 'M5A-P008', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Activation of MAP2K signaling by genetic engineering or HF-rTMS promotes corticospinal axon sprouting and functional regeneration', 'Boato F', 2023,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Stimulation/signaling intervention anchor", "module": "Module 5B", "tracker_id": "M5A-P009"}'
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
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O001"], "source_experiment_tracker_id": "M5A-P001-E001", "source_paper_tracker_id": "M5A-P001", "tracker_key": "M5A-P001::M5A-P001-E001"}'
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
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O048"], "source_experiment_tracker_id": "M5A-P001-E002", "source_paper_tracker_id": "M5A-P001", "tracker_key": "M5A-P001::M5A-P001-E002"}'
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
    'Abstract / saturated A tracker',
    'Tracker experiment M5A-P002-E001',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O002"], "source_experiment_tracker_id": "M5A-P002-E001", "source_paper_tracker_id": "M5A-P002", "tracker_key": "M5A-P002::M5A-P002-E001"}'
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
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M5A-P002-E002',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O049"], "source_experiment_tracker_id": "M5A-P002-E002", "source_paper_tracker_id": "M5A-P002", "tracker_key": "M5A-P002::M5A-P002-E002"}'
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
    'Abstract / saturated A tracker',
    'Tracker experiment M5A-P003-E001',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O003"], "source_experiment_tracker_id": "M5A-P003-E001", "source_paper_tracker_id": "M5A-P003", "tracker_key": "M5A-P003::M5A-P003-E001"}'
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
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M5A-P003-E002',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O050"], "source_experiment_tracker_id": "M5A-P003-E002", "source_paper_tracker_id": "M5A-P003", "tracker_key": "M5A-P003::M5A-P003-E002"}'
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
    'Abstract / saturated A tracker',
    'Tracker experiment M5A-P004-E001',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O004"], "source_experiment_tracker_id": "M5A-P004-E001", "source_paper_tracker_id": "M5A-P004", "tracker_key": "M5A-P004::M5A-P004-E001"}'
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
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M5A-P004-E002',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O051"], "source_experiment_tracker_id": "M5A-P004-E002", "source_paper_tracker_id": "M5A-P004", "tracker_key": "M5A-P004::M5A-P004-E002"}'
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
    'Abstract / saturated A tracker',
    'Tracker experiment M5A-P005-E001',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O005"], "source_experiment_tracker_id": "M5A-P005-E001", "source_paper_tracker_id": "M5A-P005", "tracker_key": "M5A-P005::M5A-P005-E001"}'
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
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M5A-P005-E002',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O052"], "source_experiment_tracker_id": "M5A-P005-E002", "source_paper_tracker_id": "M5A-P005", "tracker_key": "M5A-P005::M5A-P005-E002"}'
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
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O006"], "source_experiment_tracker_id": "M5A-P006-E001", "source_paper_tracker_id": "M5A-P006", "tracker_key": "M5A-P006::M5A-P006-E001"}'
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
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O053"], "source_experiment_tracker_id": "M5A-P006-E002", "source_paper_tracker_id": "M5A-P006", "tracker_key": "M5A-P006::M5A-P006-E002"}'
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
    'Abstract / saturated A tracker',
    'Tracker experiment M5A-P007-E001',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O007"], "source_experiment_tracker_id": "M5A-P007-E001", "source_paper_tracker_id": "M5A-P007", "tracker_key": "M5A-P007::M5A-P007-E001"}'
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
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M5A-P007-E002',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O054"], "source_experiment_tracker_id": "M5A-P007-E002", "source_paper_tracker_id": "M5A-P007", "tracker_key": "M5A-P007::M5A-P007-E002"}'
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
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O008"], "source_experiment_tracker_id": "M5A-P008-E001", "source_paper_tracker_id": "M5A-P008", "tracker_key": "M5A-P008::M5A-P008-E001"}'
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
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O055"], "source_experiment_tracker_id": "M5A-P008-E002", "source_paper_tracker_id": "M5A-P008", "tracker_key": "M5A-P008::M5A-P008-E002"}'
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
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O009"], "source_experiment_tracker_id": "M5A-P009-E001", "source_paper_tracker_id": "M5A-P009", "tracker_key": "M5A-P009::M5A-P009-E001"}'
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
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O056"], "source_experiment_tracker_id": "M5A-P009-E002", "source_paper_tracker_id": "M5A-P009", "tracker_key": "M5A-P009::M5A-P009-E002"}'
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
    'Abstract / saturated A tracker',
    'Tracker experiment M5A-P010-E001',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O010"], "source_experiment_tracker_id": "M5A-P010-E001", "source_paper_tracker_id": "M5A-P010", "tracker_key": "M5A-P010::M5A-P010-E001"}'
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
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M5A-P010-E002',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O057"], "source_experiment_tracker_id": "M5A-P010-E002", "source_paper_tracker_id": "M5A-P010", "tracker_key": "M5A-P010::M5A-P010-E002"}'
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
    'Abstract / saturated A tracker',
    'Tracker experiment M5A-P011-E001',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O011"], "source_experiment_tracker_id": "M5A-P011-E001", "source_paper_tracker_id": "M5A-P011", "tracker_key": "M5A-P011::M5A-P011-E001"}'
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
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M5A-P011-E002',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O058"], "source_experiment_tracker_id": "M5A-P011-E002", "source_paper_tracker_id": "M5A-P011", "tracker_key": "M5A-P011::M5A-P011-E002"}'
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
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O012"], "source_experiment_tracker_id": "M5A-P012-E001", "source_paper_tracker_id": "M5A-P012", "tracker_key": "M5A-P012::M5A-P012-E001"}'
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
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O059"], "source_experiment_tracker_id": "M5A-P012-E002", "source_paper_tracker_id": "M5A-P012", "tracker_key": "M5A-P012::M5A-P012-E002"}'
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
    'Abstract / saturated A tracker',
    'Tracker experiment M5A-P013-E001',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O013"], "source_experiment_tracker_id": "M5A-P013-E001", "source_paper_tracker_id": "M5A-P013", "tracker_key": "M5A-P013::M5A-P013-E001"}'
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
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M5A-P013-E002',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O060"], "source_experiment_tracker_id": "M5A-P013-E002", "source_paper_tracker_id": "M5A-P013", "tracker_key": "M5A-P013::M5A-P013-E002"}'
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
    'Abstract / saturated A tracker',
    'Tracker experiment M5A-P014-E001',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O014"], "source_experiment_tracker_id": "M5A-P014-E001", "source_paper_tracker_id": "M5A-P014", "tracker_key": "M5A-P014::M5A-P014-E001"}'
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
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M5A-P014-E002',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O061"], "source_experiment_tracker_id": "M5A-P014-E002", "source_paper_tracker_id": "M5A-P014", "tracker_key": "M5A-P014::M5A-P014-E002"}'
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
    'Abstract / saturated A tracker',
    'Tracker experiment M5A-P015-E001',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O015"], "source_experiment_tracker_id": "M5A-P015-E001", "source_paper_tracker_id": "M5A-P015", "tracker_key": "M5A-P015::M5A-P015-E001"}'
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
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M5A-P015-E002',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O062"], "source_experiment_tracker_id": "M5A-P015-E002", "source_paper_tracker_id": "M5A-P015", "tracker_key": "M5A-P015::M5A-P015-E002"}'
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
    'Abstract / saturated A tracker',
    'Tracker experiment M5A-P016-E001',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O016"], "source_experiment_tracker_id": "M5A-P016-E001", "source_paper_tracker_id": "M5A-P016", "tracker_key": "M5A-P016::M5A-P016-E001"}'
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
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M5A-P016-E002',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O063"], "source_experiment_tracker_id": "M5A-P016-E002", "source_paper_tracker_id": "M5A-P016", "tracker_key": "M5A-P016::M5A-P016-E002"}'
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
    'Abstract / saturated A tracker',
    'Tracker experiment M5A-P017-E001',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O017"], "source_experiment_tracker_id": "M5A-P017-E001", "source_paper_tracker_id": "M5A-P017", "tracker_key": "M5A-P017::M5A-P017-E001"}'
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
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M5A-P017-E002',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O064"], "source_experiment_tracker_id": "M5A-P017-E002", "source_paper_tracker_id": "M5A-P017", "tracker_key": "M5A-P017::M5A-P017-E002"}'
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
    'Full text / PMC12831131',
    'Tracker experiment M5A-P018-E001',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O018"], "source_experiment_tracker_id": "M5A-P018-E001", "source_paper_tracker_id": "M5A-P018", "tracker_key": "M5A-P018::M5A-P018-E001"}'
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
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M5A-P018-E002',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O065"], "source_experiment_tracker_id": "M5A-P018-E002", "source_paper_tracker_id": "M5A-P018", "tracker_key": "M5A-P018::M5A-P018-E002"}'
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
    'Abstract / saturated A tracker',
    'Tracker experiment M5A-P019-E001',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O019"], "source_experiment_tracker_id": "M5A-P019-E001", "source_paper_tracker_id": "M5A-P019", "tracker_key": "M5A-P019::M5A-P019-E001"}'
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
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M5A-P019-E002',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O066"], "source_experiment_tracker_id": "M5A-P019-E002", "source_paper_tracker_id": "M5A-P019", "tracker_key": "M5A-P019::M5A-P019-E002"}'
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
    'Abstract / saturated A tracker',
    'Tracker experiment M5A-P020-E001',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O020"], "source_experiment_tracker_id": "M5A-P020-E001", "source_paper_tracker_id": "M5A-P020", "tracker_key": "M5A-P020::M5A-P020-E001"}'
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
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M5A-P020-E002',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O067"], "source_experiment_tracker_id": "M5A-P020-E002", "source_paper_tracker_id": "M5A-P020", "tracker_key": "M5A-P020::M5A-P020-E002"}'
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
    'Abstract / saturated A tracker',
    'Tracker experiment M5A-P021-E001',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O021"], "source_experiment_tracker_id": "M5A-P021-E001", "source_paper_tracker_id": "M5A-P021", "tracker_key": "M5A-P021::M5A-P021-E001"}'
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
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M5A-P021-E002',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O068"], "source_experiment_tracker_id": "M5A-P021-E002", "source_paper_tracker_id": "M5A-P021", "tracker_key": "M5A-P021::M5A-P021-E002"}'
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
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O022"], "source_experiment_tracker_id": "M5A-P022-E001", "source_paper_tracker_id": "M5A-P022", "tracker_key": "M5A-P022::M5A-P022-E001"}'
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
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O069"], "source_experiment_tracker_id": "M5A-P022-E002", "source_paper_tracker_id": "M5A-P022", "tracker_key": "M5A-P022::M5A-P022-E002"}'
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
    'Abstract / saturated A tracker',
    'Tracker experiment M5A-P023-E001',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O023"], "source_experiment_tracker_id": "M5A-P023-E001", "source_paper_tracker_id": "M5A-P023", "tracker_key": "M5A-P023::M5A-P023-E001"}'
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
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M5A-P023-E002',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O070"], "source_experiment_tracker_id": "M5A-P023-E002", "source_paper_tracker_id": "M5A-P023", "tracker_key": "M5A-P023::M5A-P023-E002"}'
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
    'Full text / PMC12866793',
    'Tracker experiment M5A-P024-E001',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O024"], "source_experiment_tracker_id": "M5A-P024-E001", "source_paper_tracker_id": "M5A-P024", "tracker_key": "M5A-P024::M5A-P024-E001"}'
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
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M5A-P024-E002',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O071"], "source_experiment_tracker_id": "M5A-P024-E002", "source_paper_tracker_id": "M5A-P024", "tracker_key": "M5A-P024::M5A-P024-E002"}'
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
    'Abstract / saturated A tracker',
    'Tracker experiment M5A-P025-E001',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O025"], "source_experiment_tracker_id": "M5A-P025-E001", "source_paper_tracker_id": "M5A-P025", "tracker_key": "M5A-P025::M5A-P025-E001"}'
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
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M5A-P025-E002',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O072"], "source_experiment_tracker_id": "M5A-P025-E002", "source_paper_tracker_id": "M5A-P025", "tracker_key": "M5A-P025::M5A-P025-E002"}'
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
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O026"], "source_experiment_tracker_id": "M5A-P026-E001", "source_paper_tracker_id": "M5A-P026", "tracker_key": "M5A-P026::M5A-P026-E001"}'
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
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O073"], "source_experiment_tracker_id": "M5A-P026-E002", "source_paper_tracker_id": "M5A-P026", "tracker_key": "M5A-P026::M5A-P026-E002"}'
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
    'Full text / PMC13168246',
    'Tracker experiment M5A-P027-E001',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O027"], "source_experiment_tracker_id": "M5A-P027-E001", "source_paper_tracker_id": "M5A-P027", "tracker_key": "M5A-P027::M5A-P027-E001"}'
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
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M5A-P027-E002',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O074"], "source_experiment_tracker_id": "M5A-P027-E002", "source_paper_tracker_id": "M5A-P027", "tracker_key": "M5A-P027::M5A-P027-E002"}'
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
    'Abstract / saturated A tracker',
    'Tracker experiment M5A-P028-E001',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O028"], "source_experiment_tracker_id": "M5A-P028-E001", "source_paper_tracker_id": "M5A-P028", "tracker_key": "M5A-P028::M5A-P028-E001"}'
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
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M5A-P028-E002',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O075"], "source_experiment_tracker_id": "M5A-P028-E002", "source_paper_tracker_id": "M5A-P028", "tracker_key": "M5A-P028::M5A-P028-E002"}'
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
    'Full text / PMC12884443',
    'Tracker experiment M5A-P029-E001',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O029"], "source_experiment_tracker_id": "M5A-P029-E001", "source_paper_tracker_id": "M5A-P029", "tracker_key": "M5A-P029::M5A-P029-E001"}'
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
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M5A-P029-E002',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O076"], "source_experiment_tracker_id": "M5A-P029-E002", "source_paper_tracker_id": "M5A-P029", "tracker_key": "M5A-P029::M5A-P029-E002"}'
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
    'Full text / PMC12823418',
    'Tracker experiment M5A-P030-E001',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O030"], "source_experiment_tracker_id": "M5A-P030-E001", "source_paper_tracker_id": "M5A-P030", "tracker_key": "M5A-P030::M5A-P030-E001"}'
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
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M5A-P030-E002',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O077"], "source_experiment_tracker_id": "M5A-P030-E002", "source_paper_tracker_id": "M5A-P030", "tracker_key": "M5A-P030::M5A-P030-E002"}'
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
    'Abstract / saturated A tracker',
    'Tracker experiment M5A-P031-E001',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O031"], "source_experiment_tracker_id": "M5A-P031-E001", "source_paper_tracker_id": "M5A-P031", "tracker_key": "M5A-P031::M5A-P031-E001"}'
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
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M5A-P031-E002',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O078"], "source_experiment_tracker_id": "M5A-P031-E002", "source_paper_tracker_id": "M5A-P031", "tracker_key": "M5A-P031::M5A-P031-E002"}'
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
    'Abstract / saturated A tracker',
    'Tracker experiment M5A-P032-E001',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O032"], "source_experiment_tracker_id": "M5A-P032-E001", "source_paper_tracker_id": "M5A-P032", "tracker_key": "M5A-P032::M5A-P032-E001"}'
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
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M5A-P032-E002',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O079"], "source_experiment_tracker_id": "M5A-P032-E002", "source_paper_tracker_id": "M5A-P032", "tracker_key": "M5A-P032::M5A-P032-E002"}'
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
    'Full text / PMC12921341',
    'Tracker experiment M5A-P033-E001',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O033"], "source_experiment_tracker_id": "M5A-P033-E001", "source_paper_tracker_id": "M5A-P033", "tracker_key": "M5A-P033::M5A-P033-E001"}'
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
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M5A-P033-E002',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O080"], "source_experiment_tracker_id": "M5A-P033-E002", "source_paper_tracker_id": "M5A-P033", "tracker_key": "M5A-P033::M5A-P033-E002"}'
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
    'Abstract / saturated A tracker',
    'Tracker experiment M5A-P034-E001',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O034"], "source_experiment_tracker_id": "M5A-P034-E001", "source_paper_tracker_id": "M5A-P034", "tracker_key": "M5A-P034::M5A-P034-E001"}'
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
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M5A-P034-E002',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O081"], "source_experiment_tracker_id": "M5A-P034-E002", "source_paper_tracker_id": "M5A-P034", "tracker_key": "M5A-P034::M5A-P034-E002"}'
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
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O035"], "source_experiment_tracker_id": "M5A-P035-E001", "source_paper_tracker_id": "M5A-P035", "tracker_key": "M5A-P035::M5A-P035-E001"}'
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
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O082"], "source_experiment_tracker_id": "M5A-P035-E002", "source_paper_tracker_id": "M5A-P035", "tracker_key": "M5A-P035::M5A-P035-E002"}'
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
    'Abstract / saturated A tracker',
    'Tracker experiment M5A-P036-E001',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O036"], "source_experiment_tracker_id": "M5A-P036-E001", "source_paper_tracker_id": "M5A-P036", "tracker_key": "M5A-P036::M5A-P036-E001"}'
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
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M5A-P036-E002',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O083"], "source_experiment_tracker_id": "M5A-P036-E002", "source_paper_tracker_id": "M5A-P036", "tracker_key": "M5A-P036::M5A-P036-E002"}'
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
    'Abstract / saturated A tracker',
    'Tracker experiment M5A-P037-E001',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O037"], "source_experiment_tracker_id": "M5A-P037-E001", "source_paper_tracker_id": "M5A-P037", "tracker_key": "M5A-P037::M5A-P037-E001"}'
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
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M5A-P037-E002',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O084"], "source_experiment_tracker_id": "M5A-P037-E002", "source_paper_tracker_id": "M5A-P037", "tracker_key": "M5A-P037::M5A-P037-E002"}'
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
    'Abstract / saturated A tracker',
    'Tracker experiment M5A-P038-E001',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O038"], "source_experiment_tracker_id": "M5A-P038-E001", "source_paper_tracker_id": "M5A-P038", "tracker_key": "M5A-P038::M5A-P038-E001"}'
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
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M5A-P038-E002',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O085"], "source_experiment_tracker_id": "M5A-P038-E002", "source_paper_tracker_id": "M5A-P038", "tracker_key": "M5A-P038::M5A-P038-E002"}'
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
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O039"], "source_experiment_tracker_id": "M5A-P039-E001", "source_paper_tracker_id": "M5A-P039", "tracker_key": "M5A-P039::M5A-P039-E001"}'
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
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O086"], "source_experiment_tracker_id": "M5A-P039-E002", "source_paper_tracker_id": "M5A-P039", "tracker_key": "M5A-P039::M5A-P039-E002"}'
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
    'Abstract / saturated A tracker',
    'Tracker experiment M5A-P040-E001',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O040"], "source_experiment_tracker_id": "M5A-P040-E001", "source_paper_tracker_id": "M5A-P040", "tracker_key": "M5A-P040::M5A-P040-E001"}'
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
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M5A-P040-E002',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O087"], "source_experiment_tracker_id": "M5A-P040-E002", "source_paper_tracker_id": "M5A-P040", "tracker_key": "M5A-P040::M5A-P040-E002"}'
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
    'Abstract / saturated A tracker',
    'Tracker experiment M5A-P041-E001',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O041"], "source_experiment_tracker_id": "M5A-P041-E001", "source_paper_tracker_id": "M5A-P041", "tracker_key": "M5A-P041::M5A-P041-E001"}'
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
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M5A-P041-E002',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O088"], "source_experiment_tracker_id": "M5A-P041-E002", "source_paper_tracker_id": "M5A-P041", "tracker_key": "M5A-P041::M5A-P041-E002"}'
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
    'Abstract / saturated A tracker',
    'Tracker experiment M5A-P042-E001',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O042"], "source_experiment_tracker_id": "M5A-P042-E001", "source_paper_tracker_id": "M5A-P042", "tracker_key": "M5A-P042::M5A-P042-E001"}'
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
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M5A-P042-E002',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O089"], "source_experiment_tracker_id": "M5A-P042-E002", "source_paper_tracker_id": "M5A-P042", "tracker_key": "M5A-P042::M5A-P042-E002"}'
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
    'Full text / PMC12908063',
    'Tracker experiment M5A-P043-E001',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O043"], "source_experiment_tracker_id": "M5A-P043-E001", "source_paper_tracker_id": "M5A-P043", "tracker_key": "M5A-P043::M5A-P043-E001"}'
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
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M5A-P043-E002',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O090"], "source_experiment_tracker_id": "M5A-P043-E002", "source_paper_tracker_id": "M5A-P043", "tracker_key": "M5A-P043::M5A-P043-E002"}'
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
    'Full text / PMC13083982',
    'Tracker experiment M5A-P044-E001',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O044"], "source_experiment_tracker_id": "M5A-P044-E001", "source_paper_tracker_id": "M5A-P044", "tracker_key": "M5A-P044::M5A-P044-E001"}'
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
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M5A-P044-E002',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O091"], "source_experiment_tracker_id": "M5A-P044-E002", "source_paper_tracker_id": "M5A-P044", "tracker_key": "M5A-P044::M5A-P044-E002"}'
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
    'Abstract / saturated A tracker',
    'Tracker experiment M5A-P045-E001',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O045"], "source_experiment_tracker_id": "M5A-P045-E001", "source_paper_tracker_id": "M5A-P045", "tracker_key": "M5A-P045::M5A-P045-E001"}'
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
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M5A-P045-E002',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O092"], "source_experiment_tracker_id": "M5A-P045-E002", "source_paper_tracker_id": "M5A-P045", "tracker_key": "M5A-P045::M5A-P045-E002"}'
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
    'Abstract / saturated A tracker',
    'Tracker experiment M5A-P046-E001',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O046"], "source_experiment_tracker_id": "M5A-P046-E001", "source_paper_tracker_id": "M5A-P046", "tracker_key": "M5A-P046::M5A-P046-E001"}'
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
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M5A-P046-E002',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O093"], "source_experiment_tracker_id": "M5A-P046-E002", "source_paper_tracker_id": "M5A-P046", "tracker_key": "M5A-P046::M5A-P046-E002"}'
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
    'Abstract / saturated A tracker',
    'Tracker experiment M5A-P047-E001',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O047"], "source_experiment_tracker_id": "M5A-P047-E001", "source_paper_tracker_id": "M5A-P047", "tracker_key": "M5A-P047::M5A-P047-E001"}'
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
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M5A-P047-E002',
    'Module 5B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M5B-O094"], "source_experiment_tracker_id": "M5A-P047-E002", "source_paper_tracker_id": "M5A-P047", "tracker_key": "M5A-P047::M5A-P047-E002"}'
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
    'Dias DO 2018 contributes cst/rst regeneration after scar attenuation evidence in mouse, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Dias DO 2018 contributes cst/rst regeneration after scar attenuation evidence in mouse, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'dias do 2018 contributes cst/rst regeneration after scar attenuation evidence in mouse, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'Module 5A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'medium',
    '{"curator_notes": "Primary title: Reducing Pericyte-Derived Scarring Promotes Recovery after Spinal Cord Injury. Note: Axon regeneration with scar-modulation anchor.", "experiment_tracker_id": "M5A-P002-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P002", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M5B-T001", "tracker_id": "M5B-O002"}'
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
    'McCallum S 2026 contributes lesion-remote white matter repair evidence in mouse, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'qualitative',
    NULL,
    'McCallum S 2026 contributes lesion-remote white matter repair evidence in mouse, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'mccallum s 2026 contributes lesion-remote white matter repair evidence in mouse, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'Module 5A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'medium',
    '{"curator_notes": "Primary title: Lesion-remote astrocytes govern microglia-mediated white matter repair. Note: White matter repair anchor.", "experiment_tracker_id": "M5A-P003-E001", "measurement_method_inference": null, "paper_tracker_id": "M5A-P003", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M5B-T003", "tracker_id": "M5B-O003"}'
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
    'Grumbles RM 2017 contributes ventral-root axon loss/remyelination pathology evidence in human, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'qualitative',
    'immunostaining / histology / pathology',
    'Grumbles RM 2017 contributes ventral-root axon loss/remyelination pathology evidence in human, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'grumbles rm 2017 contributes ventral-root axon loss/remyelination pathology evidence in human, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'Module 5A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'medium',
    '{"curator_notes": "Primary title: Motoneuron Death after Human Spinal Cord Injury. Note: Human remyelination/pathology bridge.", "experiment_tracker_id": "M5A-P004-E001", "measurement_method_inference": "immunostaining / histology / pathology", "paper_tracker_id": "M5A-P004", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M5B-T003", "tracker_id": "M5B-O004"}'
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
    'Han Q 2020 contributes axonal regeneration / cellular energetics evidence in rodent model context, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Han Q 2020 contributes axonal regeneration / cellular energetics evidence in rodent model context, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'han q 2020 contributes axonal regeneration / cellular energetics evidence in rodent model context, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'Module 5A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'medium',
    '{"curator_notes": "Primary title: Restoring Cellular Energetics Promotes Axonal Regeneration and Functional Recovery after Spinal Cord Injury. Note: Metabolic mechanism anchor.", "experiment_tracker_id": "M5A-P005-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P005", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M5B-T005", "tracker_id": "M5B-O005"}'
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
    'Kadoya K 2016 contributes neural graft-enabled cst regeneration evidence in rat, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Kadoya K 2016 contributes neural graft-enabled cst regeneration evidence in rat, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'kadoya k 2016 contributes neural graft-enabled cst regeneration evidence in rat, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'Module 5A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'medium',
    '{"curator_notes": "Primary title: Spinal cord reconstitution with homologous neural grafts enables robust corticospinal regeneration. Note: Graft-regeneration bridge to Module 4A.", "experiment_tracker_id": "M5A-P007-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P007", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M5B-T006", "tracker_id": "M5B-O007"}'
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
    'Ma YH 2025 contributes corticospinal tract regeneration / sprouting evidence in mouse sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Ma YH 2025 contributes corticospinal tract regeneration / sprouting evidence in mouse sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'ma yh 2025 contributes corticospinal tract regeneration / sprouting evidence in mouse sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'Module 5A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'medium',
    '{"curator_notes": "Primary title: Transcranial Optogenetic Stimulation Promotes Corticospinal Tract Axon Regeneration to Repair Spinal Cord Injury by Activating the JAK2/STAT3 Pathway.. Note: Corticospinal tract regeneration / sprouting anchor.", "experiment_tracker_id": "M5A-P010-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P010", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M5B-T007", "tracker_id": "M5B-O010"}'
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
    'Chen W 2024 contributes corticospinal tract regeneration / sprouting evidence in rat sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Chen W 2024 contributes corticospinal tract regeneration / sprouting evidence in rat sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'chen w 2024 contributes corticospinal tract regeneration / sprouting evidence in rat sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'Module 5A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'medium',
    '{"curator_notes": "Primary title: Lipin1 depletion coordinates neuronal signaling pathways to promote motor and sensory axon regeneration after spinal cord injury.. Note: Corticospinal tract regeneration / sprouting anchor.", "experiment_tracker_id": "M5A-P011-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P011", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M5B-T005", "tracker_id": "M5B-O011"}'
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
    'Higuchi K 2024 contributes corticospinal tract regeneration / sprouting evidence in experimental sci model context, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Higuchi K 2024 contributes corticospinal tract regeneration / sprouting evidence in experimental sci model context, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'higuchi k 2024 contributes corticospinal tract regeneration / sprouting evidence in experimental sci model context, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'Module 5A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'medium',
    '{"curator_notes": "Primary title: Synaptotagmin 4 Supports Spontaneous Axon Sprouting after Spinal Cord Injury.. Note: Corticospinal tract regeneration / sprouting anchor.", "experiment_tracker_id": "M5A-P013-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P013", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M5B-T001", "tracker_id": "M5B-O013"}'
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
    'Sun W 2020 contributes corticospinal tract regeneration / sprouting evidence in mouse sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Sun W 2020 contributes corticospinal tract regeneration / sprouting evidence in mouse sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'sun w 2020 contributes corticospinal tract regeneration / sprouting evidence in mouse sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'Module 5A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'medium',
    '{"curator_notes": "Primary title: Gabapentinoid treatment promotes corticospinal plasticity and regeneration following murine spinal cord injury.. Note: Gabapentinoid CST plasticity anchor.", "experiment_tracker_id": "M5A-P014-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P014", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M5B-T001", "tracker_id": "M5B-O014"}'
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
    'Stepankova K 2025 contributes extrinsic inhibitory matrix / guidance pathway evidence in rat sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'qualitative',
    NULL,
    'Stepankova K 2025 contributes extrinsic inhibitory matrix / guidance pathway evidence in rat sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'stepankova k 2025 contributes extrinsic inhibitory matrix / guidance pathway evidence in rat sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'Module 5A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'medium',
    '{"curator_notes": "Primary title: Activated alpha 9 integrin expression enables sensory pathway reconstruction after spinal cord injury.. Note: Extrinsic inhibitory matrix / guidance pathway anchor.", "experiment_tracker_id": "M5A-P015-E001", "measurement_method_inference": null, "paper_tracker_id": "M5A-P015", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M5B-T002", "tracker_id": "M5B-O015"}'
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
    'Takatani H 2025 contributes corticospinal tract regeneration / sprouting evidence in mouse sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Takatani H 2025 contributes corticospinal tract regeneration / sprouting evidence in mouse sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'takatani h 2025 contributes corticospinal tract regeneration / sprouting evidence in mouse sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'Module 5A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'medium',
    '{"curator_notes": "Primary title: Modulation of Extrinsic and Intrinsic Signaling Together with Neuronal Activation Enhances Forelimb Motor Recovery after Cervical Spinal Cord Injury.. Note: Corticospinal tract regeneration / sprouting anchor.", "experiment_tracker_id": "M5A-P016-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P016", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M5B-T001", "tracker_id": "M5B-O016"}'
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
    'van Niekerk EA 2025 contributes corticospinal tract regeneration / sprouting evidence in human / translational context, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'qualitative',
    'behavioral / functional recovery assay',
    'van Niekerk EA 2025 contributes corticospinal tract regeneration / sprouting evidence in human / translational context, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'van niekerk ea 2025 contributes corticospinal tract regeneration / sprouting evidence in human / translational context, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'Module 5A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'medium',
    '{"curator_notes": "Primary title: Thiorphan reprograms neurons to promote functional recovery after spinal cord injury.. Note: Corticospinal tract regeneration / sprouting anchor.", "experiment_tracker_id": "M5A-P017-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P017", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M5B-T001", "tracker_id": "M5B-O017"}'
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
    'TTBK2 was manipulated in spinal neurons in vitro and in conditional knockout mice after spinal cord hemisection; behavioral assays, immunofluorescence, and BDA tracing showed that intact TTBK2/primary-cilium activity supports neuronal survival, axonal regeneration, and circuit reorganization after SCI.',
    'qualitative',
    'qPCR / RT-PCR / mRNA assay; bulk transcriptomics / GEO dataset; immunostaining / histology / pathology; genetic perturbation / knockdown assay',
    'TTBK2 was manipulated in spinal neurons in vitro and in conditional knockout mice after spinal cord hemisection; behavioral assays, immunofluorescence, and BDA tracing showed that intact TTBK2/primary-cilium activity supports neuronal survival, axonal regeneration, and circuit reorganization after SCI.',
    'TTBK2-driven ciliogenesis supports intrinsic neuronal regeneration and circuit repair after SCI',
    'Full text / PMC',
    'Full text / PMC12831131',
    'high',
    '{"curator_notes": "Full-text upgrade from PMID 41578860; preserves intrinsic-growth/ciliogenesis boundary.", "experiment_tracker_id": "M5A-P018-E001", "measurement_method_inference": "qPCR / RT-PCR / mRNA assay; bulk transcriptomics / GEO dataset; immunostaining / histology / pathology; genetic perturbation / knockdown assay", "paper_tracker_id": "M5A-P018", "quantitative": "YES", "statistics_reported": "Full text reports in vitro overexpression/knockdown, RNA-seq/RT-qPCR, conditional knockout, behavior, immunofluorescence, and BDA tracing", "topic_id": "M5B-T005", "tracker_id": "M5B-O018"}'
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
    'Attwell CL 2025 contributes intrinsic neuronal growth competence evidence in rat sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'qualitative',
    NULL,
    'Attwell CL 2025 contributes intrinsic neuronal growth competence evidence in rat sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'attwell cl 2025 contributes intrinsic neuronal growth competence evidence in rat sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'Module 5A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'medium',
    '{"curator_notes": "Primary title: The transcription factor combination MEF2 and KLF7 promotes axonal sprouting in the injured spinal cord with functional improvement and regeneration-associated gene expression.. Note: Intrinsic neuronal growth competence anchor.", "experiment_tracker_id": "M5A-P019-E001", "measurement_method_inference": null, "paper_tracker_id": "M5A-P019", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M5B-T005", "tracker_id": "M5B-O019"}'
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
    'Martinez-Rojas B 2025 contributes corticospinal tract regeneration / sprouting evidence in rat sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Martinez-Rojas B 2025 contributes corticospinal tract regeneration / sprouting evidence in rat sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'martinez-rojas b 2025 contributes corticospinal tract regeneration / sprouting evidence in rat sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'Module 5A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'medium',
    '{"curator_notes": "Primary title: Stimulation of corticospinal neurons by optogenetic cAMP inductions promotes motor recovery after spinal cord injury in female rats via raphespinal tract modulation.. Note: Corticospinal tract regeneration / sprouting anchor.", "experiment_tracker_id": "M5A-P020-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P020", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M5B-T007", "tracker_id": "M5B-O020"}'
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
    'Ji Z 2025 contributes corticospinal tract regeneration / sprouting evidence in mouse sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Ji Z 2025 contributes corticospinal tract regeneration / sprouting evidence in mouse sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'ji z 2025 contributes corticospinal tract regeneration / sprouting evidence in mouse sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'Module 5A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'medium',
    '{"curator_notes": "Primary title: Precise rewiring of corticospinal axons and spinal interneurons via near-infrared optogenetics for spinal cord injury treatment.. Note: Corticospinal tract regeneration / sprouting anchor.", "experiment_tracker_id": "M5A-P021-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P021", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M5B-T007", "tracker_id": "M5B-O021"}'
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
    'Zheng ML 2025 contributes extrinsic inhibitory matrix / guidance pathway evidence in human / translational context, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Zheng ML 2025 contributes extrinsic inhibitory matrix / guidance pathway evidence in human / translational context, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'zheng ml 2025 contributes extrinsic inhibitory matrix / guidance pathway evidence in human / translational context, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'Module 5A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'medium',
    '{"curator_notes": "Primary title: Lentivirus-mediated overexpression of netrin-1/DCC co-expression promotes axonal regeneration and functional recovery in spinal cord injury via the inhibition of the NgR1-RhoA-ROCK signaling pathway.. Note: Extrinsic inhibitory matrix / guidance pathway anchor.", "experiment_tracker_id": "M5A-P023-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P023", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M5B-T002", "tracker_id": "M5B-O023"}'
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
    'CSPGs were identified as regulators of chronic scar maturation through a pro-inflammatory microglia-astrocyte axis; targeted CSPG degradation reprogrammed microglia toward an anti-inflammatory state and attenuated scar-forming astrocyte differentiation and fibrotic matrix deposition.',
    'qualitative',
    NULL,
    'CSPGs were identified as regulators of chronic scar maturation through a pro-inflammatory microglia-astrocyte axis; targeted CSPG degradation reprogrammed microglia toward an anti-inflammatory state and attenuated scar-forming astrocyte differentiation and fibrotic matrix deposition.',
    'CSPG degradation can alter microglia-astrocyte scar crosstalk and reduce fibrotic scar maturation',
    'Full text / PMC',
    'Full text / PMC12866793',
    'high',
    '{"curator_notes": "Full-text upgrade from PMID 41221600; cross-tags Module 3 immune-glial scar boundary.", "experiment_tracker_id": "M5A-P024-E001", "measurement_method_inference": null, "paper_tracker_id": "M5A-P024", "quantitative": "YES", "statistics_reported": "Full text reports CSPG-driven microglial inflammatory signaling, astrocyte scar transition, ChABC-based intervention, and matrix/scar endpoints", "topic_id": "M5B-T002", "tracker_id": "M5B-O024"}'
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
    'Qu W 2025 contributes serotonergic/propriospinal relay plasticity evidence in human / translational context, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Qu W 2025 contributes serotonergic/propriospinal relay plasticity evidence in human / translational context, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'qu w 2025 contributes serotonergic/propriospinal relay plasticity evidence in human / translational context, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'Module 5A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'medium',
    '{"curator_notes": "Primary title: Chondroitinase ABC combined with Schwann cell transplantation enhances restoration of neural connection and functional recovery following acute and chronic spinal cord injury.. Note: Serotonergic/propriospinal relay plasticity anchor.", "experiment_tracker_id": "M5A-P025-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P025", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M5B-T004", "tracker_id": "M5B-O025"}'
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
    'In 106 participants with acute cervical SCI from the phase 2b NISCI trial, anti-Nogo-A NG101 treatment was associated with faster lesion-volume reduction and slower decline of cord area and tract-specific MTsat in corticospinal tracts and dorsal columns relative to placebo.',
    'qualitative',
    'MRI / imaging assay; behavioral / functional recovery assay',
    'In 106 participants with acute cervical SCI from the phase 2b NISCI trial, anti-Nogo-A NG101 treatment was associated with faster lesion-volume reduction and slower decline of cord area and tract-specific MTsat in corticospinal tracts and dorsal columns relative to placebo.',
    'NG101 anti-Nogo-A treatment modifies human cervical SCI MRI macro/microstructure biomarkers',
    'Full text / PMC',
    'Full text / PMC13168246',
    'high',
    '{"curator_notes": "Human trial imaging biomarker row; interpret as structural biomarker evidence, not direct axon-regrowth proof.", "experiment_tracker_id": "M5A-P027-E001", "measurement_method_inference": "MRI / imaging assay; behavioral / functional recovery assay", "paper_tracker_id": "M5A-P027", "quantitative": "YES", "statistics_reported": "Full text reports trial MRI biomarkers including lesion volume, tissue bridges, CSA, and tract-specific MTsat over six months", "topic_id": "M5B-T002", "tracker_id": "M5B-O027"}'
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
    'Nori S 2018 contributes remyelination / white matter repair evidence in human / translational context, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'qualitative',
    NULL,
    'Nori S 2018 contributes remyelination / white matter repair evidence in human / translational context, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'nori s 2018 contributes remyelination / white matter repair evidence in human / translational context, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'Module 5A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'medium',
    '{"curator_notes": "Primary title: Human Oligodendrogenic Neural Progenitor Cells Delivered with Chondroitinase ABC Facilitate Functional Repair of Chronic Spinal Cord Injury.. Note: Remyelination / white matter repair anchor.", "experiment_tracker_id": "M5A-P028-E001", "measurement_method_inference": null, "paper_tracker_id": "M5A-P028", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M5B-T003", "tracker_id": "M5B-O028"}'
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
    'In female mouse spinal cord crush injury, TREM2 deletion and COG1410 activation experiments showed that TREM2 promotes myelin-debris clearance and disease-associated microglia activation but can also exacerbate chronic inflammation and fibrosis after SCI.',
    'qualitative',
    NULL,
    'In female mouse spinal cord crush injury, TREM2 deletion and COG1410 activation experiments showed that TREM2 promotes myelin-debris clearance and disease-associated microglia activation but can also exacerbate chronic inflammation and fibrosis after SCI.',
    'TREM2 links myelin debris clearance to a repair-versus-fibrosis tradeoff after SCI',
    'Full text / PMC',
    'Full text / PMC12884443',
    'high',
    '{"curator_notes": "Full-text upgrade from PMID 41660680; preserves contradiction boundary.", "experiment_tracker_id": "M5A-P029-E001", "measurement_method_inference": null, "paper_tracker_id": "M5A-P029", "quantitative": "YES", "statistics_reported": "Full text reports TREM2 expression, phagocytosis, foamy macrophages, DAM activation, axon regeneration, neuronal survival, BMS, and footprint outcomes", "topic_id": "M5B-T003", "tracker_id": "M5B-O029"}'
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
    'Multiple transcriptional profiling methods after traumatic mouse SCI identified lesion-remote astrocyte states in degenerating white matter that direct local microglia to clear lipid-rich myelin debris and promote tissue repair.',
    'qualitative',
    'qPCR / RT-PCR / mRNA assay',
    'Multiple transcriptional profiling methods after traumatic mouse SCI identified lesion-remote astrocyte states in degenerating white matter that direct local microglia to clear lipid-rich myelin debris and promote tissue repair.',
    'lesion-remote astrocytes govern microglia-mediated white matter repair after SCI',
    'Full text / PMC',
    'Full text / PMC12823418',
    'high',
    '{"curator_notes": "Full-text upgrade from PMID 41407858; cross-links Module 3 immune-glial state.", "experiment_tracker_id": "M5A-P030-E001", "measurement_method_inference": "qPCR / RT-PCR / mRNA assay", "paper_tracker_id": "M5A-P030", "quantitative": "YES", "statistics_reported": "Full text reports LRA transcriptional states, astrocyte-specific perturbation, microglial lipid-debris clearance, and white matter repair outcomes", "topic_id": "M5B-T003", "tracker_id": "M5B-O030"}'
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
    'Manesh SB 2025 contributes remyelination / white matter repair evidence in mouse sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'qualitative',
    'genetic perturbation / knockdown assay',
    'Manesh SB 2025 contributes remyelination / white matter repair evidence in mouse sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'manesh sb 2025 contributes remyelination / white matter repair evidence in mouse sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'Module 5A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'medium',
    '{"curator_notes": "Primary title: Compensatory changes after spinal cord injury in a remyelination deficient mouse model.. Note: Remyelination / white matter repair anchor.", "experiment_tracker_id": "M5A-P031-E001", "measurement_method_inference": "genetic perturbation / knockdown assay", "paper_tracker_id": "M5A-P031", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M5B-T003", "tracker_id": "M5B-O031"}'
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
    'Zhou Y 2025 contributes remyelination / white matter repair evidence in rat sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Zhou Y 2025 contributes remyelination / white matter repair evidence in rat sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'zhou y 2025 contributes remyelination / white matter repair evidence in rat sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'Module 5A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'medium',
    '{"curator_notes": "Primary title: A Myelin Debris Cleaner for Spinal Cord Injury Recovery: Polycaprolactone / Cell Membrane Assembled Scaffolds.. Note: Remyelination / white matter repair anchor.", "experiment_tracker_id": "M5A-P032-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P032", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M5B-T003", "tracker_id": "M5B-O032"}'
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
    'A DNA/RNA heteroduplex hydrogel combined 5-HT-mediated neuronal excitability restoration with PTEN-targeted spinal circuit reconstruction, aiming to reactivate dormant spared circuits and improve reconnection after SCI.',
    'qualitative',
    NULL,
    'A DNA/RNA heteroduplex hydrogel combined 5-HT-mediated neuronal excitability restoration with PTEN-targeted spinal circuit reconstruction, aiming to reactivate dormant spared circuits and improve reconnection after SCI.',
    'serotonergic-targeted nucleic acid hydrogel couples excitability restoration with PTEN circuit reconstruction',
    'Full text / PMC',
    'Full text / PMC12921341',
    'high',
    '{"curator_notes": "Full-text upgrade from PMID 41531173; cross-tags biomaterial delivery boundary.", "experiment_tracker_id": "M5A-P033-E001", "measurement_method_inference": null, "paper_tracker_id": "M5A-P033", "quantitative": "YES", "statistics_reported": "Full text reports 5-HTP-derived targeting/neuromodulatory hydrogel design, PTEN-targeted nucleic-acid delivery, excitability, and circuit-reconstruction endpoints", "topic_id": "M5B-T004", "tracker_id": "M5B-O033"}'
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
    'Sysoev YI 2025 contributes serotonergic/propriospinal relay plasticity evidence in rat sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'qualitative',
    'genetic perturbation / knockdown assay; behavioral / functional recovery assay',
    'Sysoev YI 2025 contributes serotonergic/propriospinal relay plasticity evidence in rat sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'sysoev yi 2025 contributes serotonergic/propriospinal relay plasticity evidence in rat sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'Module 5A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'medium',
    '{"curator_notes": "Primary title: Central Serotonin Deficiency Impairs Recovery of Sensorimotor Abilities After Spinal Cord Injury in Rats.. Note: Serotonergic/propriospinal relay plasticity anchor.", "experiment_tracker_id": "M5A-P034-E001", "measurement_method_inference": "genetic perturbation / knockdown assay; behavioral / functional recovery assay", "paper_tracker_id": "M5A-P034", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M5B-T004", "tracker_id": "M5B-O034"}'
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
    'Wang Y 2025 contributes serotonergic/propriospinal relay plasticity evidence in rat sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Wang Y 2025 contributes serotonergic/propriospinal relay plasticity evidence in rat sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'wang y 2025 contributes serotonergic/propriospinal relay plasticity evidence in rat sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'Module 5A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'medium',
    '{"curator_notes": "Primary title: Functional recovery induced by KCC2-enabled relay pathways in completely injured spinal cords in adult rats.. Note: Serotonergic/propriospinal relay plasticity anchor.", "experiment_tracker_id": "M5A-P036-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P036", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M5B-T004", "tracker_id": "M5B-O036"}'
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
    'Zhao H 2025 contributes serotonergic/propriospinal relay plasticity evidence in rat sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Zhao H 2025 contributes serotonergic/propriospinal relay plasticity evidence in rat sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'zhao h 2025 contributes serotonergic/propriospinal relay plasticity evidence in rat sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'Module 5A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'medium',
    '{"curator_notes": "Primary title: Functionalized nanozyme delivery of a KCC2-activator conjugate for the promotion of functional recovery after acute spinal cord injury.. Note: Serotonergic/propriospinal relay plasticity anchor.", "experiment_tracker_id": "M5A-P037-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P037", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M5B-T004", "tracker_id": "M5B-O037"}'
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
    'Morozumi M 2025 contributes serotonergic/propriospinal relay plasticity evidence in mouse sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Morozumi M 2025 contributes serotonergic/propriospinal relay plasticity evidence in mouse sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'morozumi m 2025 contributes serotonergic/propriospinal relay plasticity evidence in mouse sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'Module 5A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'medium',
    '{"curator_notes": "Primary title: Enhanced locomotor recovery in mice lacking GlcNAc6ST1 and GlcNAc6ST4 following spinal cord injury.. Note: Serotonergic/propriospinal relay plasticity anchor.", "experiment_tracker_id": "M5A-P038-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P038", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M5B-T004", "tracker_id": "M5B-O038"}'
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
    'Wang Y 2023 contributes corticospinal tract regeneration / sprouting evidence in mouse sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Wang Y 2023 contributes corticospinal tract regeneration / sprouting evidence in mouse sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'wang y 2023 contributes corticospinal tract regeneration / sprouting evidence in mouse sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'Module 5A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'medium',
    '{"curator_notes": "Primary title: Osteopontin enhances the effect of treadmill training and promotes functional recovery after spinal cord injury.. Note: Corticospinal tract regeneration / sprouting anchor.", "experiment_tracker_id": "M5A-P040-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P040", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M5B-T007", "tracker_id": "M5B-O040"}'
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
    'Tao N 2023 contributes graft/scaffold-enabled axon repair evidence in mouse sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'qualitative',
    NULL,
    'Tao N 2023 contributes graft/scaffold-enabled axon repair evidence in mouse sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'tao n 2023 contributes graft/scaffold-enabled axon repair evidence in mouse sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'Module 5A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'medium',
    '{"curator_notes": "Primary title: Co-overexpression of OPN, IGF-1 and CNTF augment the therapeutic effect of DPSC on spinal cord injury.. Note: Graft/scaffold-enabled axon repair anchor.", "experiment_tracker_id": "M5A-P041-E001", "measurement_method_inference": null, "paper_tracker_id": "M5A-P041", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M5B-T006", "tracker_id": "M5B-O041"}'
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
    'Ye J 2025 contributes graft/scaffold-enabled axon repair evidence in rat sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Ye J 2025 contributes graft/scaffold-enabled axon repair evidence in rat sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'ye j 2025 contributes graft/scaffold-enabled axon repair evidence in rat sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'Module 5A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'medium',
    '{"curator_notes": "Primary title: Multichannel 3D-Printed Bioactive Scaffold Combined with Small Interfering RNA Delivery to Promote Neurological Recovery after Spinal Cord Injury.. Note: Graft/scaffold-enabled axon repair anchor.", "experiment_tracker_id": "M5A-P042-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P042", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M5B-T006", "tracker_id": "M5B-O042"}'
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
    'A hyaluronic-acid scaffold enriched with collagen IV and fibronectin was functionalized with GET-peptide PTEN-siRNA nanoparticles, which transfected primary neurons and significantly enhanced neurite outgrowth from the scaffold platform.',
    'qualitative',
    'genetic perturbation / knockdown assay',
    'A hyaluronic-acid scaffold enriched with collagen IV and fibronectin was functionalized with GET-peptide PTEN-siRNA nanoparticles, which transfected primary neurons and significantly enhanced neurite outgrowth from the scaffold platform.',
    'PTEN-siRNA activated scaffold promotes neurite outgrowth in an SCI repair scaffold platform',
    'Full text / PMC',
    'Full text / PMC12908063',
    'high',
    '{"curator_notes": "Full-text upgrade from PMID 41704619; scaffold/gene-therapy attribution boundary.", "experiment_tracker_id": "M5A-P043-E001", "measurement_method_inference": "genetic perturbation / knockdown assay", "paper_tracker_id": "M5A-P043", "quantitative": "YES", "statistics_reported": "Full text reports GET-siRNA nanoparticle formulation, primary-neuron transfection, scaffold incorporation, and neurite-outgrowth endpoint", "topic_id": "M5B-T005", "tracker_id": "M5B-O043"}'
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
    'CITED2 was identified as an epigenetic switch active in immature/regenerating DRG neurons but silent after non-regenerative SCI; Cited2 overexpression reactivated growth programs and enhanced in vivo regeneration after SCI, while Cited2-targeting panobinostat promoted sensory and motor neuron growth/sprouting and functional recovery.',
    'qualitative',
    'behavioral / functional recovery assay',
    'CITED2 was identified as an epigenetic switch active in immature/regenerating DRG neurons but silent after non-regenerative SCI; Cited2 overexpression reactivated growth programs and enhanced in vivo regeneration after SCI, while Cited2-targeting panobinostat promoted sensory and motor neuron growth/sprouting and functional recovery.',
    'CITED2/panobinostat reactivates neuronal growth programs after SCI',
    'Full text / PMC',
    'Full text / PMC13083982',
    'high',
    '{"curator_notes": "Full-text upgrade from PMID 41731079; intrinsic-growth epigenetic switch.", "experiment_tracker_id": "M5A-P044-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P044", "quantitative": "YES", "statistics_reported": "Full text reports developmental/regenerative DRG profiling, Cited2 gain/loss, in vivo SCI regeneration, pharmacologic HDAC inhibitor targeting, growth/sprouting, and functional endpoints", "topic_id": "M5B-T005", "tracker_id": "M5B-O044"}'
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
    'Couvrette LJ 2025 contributes graft/scaffold-enabled axon repair evidence in human / translational context, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Couvrette LJ 2025 contributes graft/scaffold-enabled axon repair evidence in human / translational context, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'couvrette lj 2025 contributes graft/scaffold-enabled axon repair evidence in human / translational context, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'Module 5A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'medium',
    '{"curator_notes": "Primary title: Poly-L-Ornithine coated plant scaffolds support motor recovery in rats after traumatic spinal cord injury.. Note: Graft/scaffold-enabled axon repair anchor.", "experiment_tracker_id": "M5A-P045-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P045", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M5B-T006", "tracker_id": "M5B-O045"}'
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
    'Dong H 2025 contributes remyelination / white matter repair evidence in rat sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'qualitative',
    'single-cell RNA-seq / cell-state atlas; spatial transcriptomics / spatial atlas',
    'Dong H 2025 contributes remyelination / white matter repair evidence in rat sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'dong h 2025 contributes remyelination / white matter repair evidence in rat sci model, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'Module 5A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'medium',
    '{"curator_notes": "Primary title: Integrating single-cell RNA sequencing and spatial multi-omics reveals the molecular signature of regeneration after spinal cord injury.. Note: Remyelination / white matter repair anchor.", "experiment_tracker_id": "M5A-P046-E001", "measurement_method_inference": "single-cell RNA-seq / cell-state atlas; spatial transcriptomics / spatial atlas", "paper_tracker_id": "M5A-P046", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M5B-T003", "tracker_id": "M5B-O046"}'
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
    'Chize CM 2025 contributes extrinsic inhibitory matrix / guidance pathway evidence in dog chronic sci, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'qualitative',
    NULL,
    'Chize CM 2025 contributes extrinsic inhibitory matrix / guidance pathway evidence in dog chronic sci, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'chize cm 2025 contributes extrinsic inhibitory matrix / guidance pathway evidence in dog chronic sci, supporting the axon regeneration, remyelination, and white matter repair after sci first-pass corpus.',
    'Module 5A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'medium',
    '{"curator_notes": "Primary title: A laminin-based therapy for dogs with chronic spinal cord injury: promising results of a longitudinal trial.. Note: Extrinsic inhibitory matrix / guidance pathway anchor.", "experiment_tracker_id": "M5A-P047-E001", "measurement_method_inference": null, "paper_tracker_id": "M5A-P047", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M5B-T002", "tracker_id": "M5B-O047"}'
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
    'Dias DO 2018 M5A-P002-E002 preserves a distinct Mouse experiment testing Mechanistic outcome assessment after cst/rst regeneration after scar attenuation with endpoint/readout: Outcome/mechanistic validation row for Reducing Pericyte-Derived Scarring Promotes Recovery after Spinal Cord Injury; first-pass row captures cst/rst regeneration after scar attenuation in mouse at abstract/source-title level..',
    'qualitative',
    'behavioral / functional recovery assay',
    'Dias DO 2018 M5A-P002-E002 preserves a distinct Mouse experiment testing Mechanistic outcome assessment after cst/rst regeneration after scar attenuation with endpoint/readout: Outcome/mechanistic validation row for Reducing Pericyte-Derived Scarring Promotes Recovery after Spinal Cord Injury; first-pass row captures cst/rst regeneration after scar attenuation in mouse at abstract/source-title level..',
    'M5A-P002-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Reducing Pericyte-Derived Scarring Promotes Recovery after Spinal Cord Injury. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M5A-P002-E002", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P002", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M5B-T001", "tracker_id": "M5B-O049"}'
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
    'McCallum S 2026 M5A-P003-E002 preserves a distinct Mouse experiment testing Mechanistic outcome assessment after lesion-remote white matter repair with endpoint/readout: Outcome/mechanistic validation row for Lesion-remote astrocytes govern microglia-mediated white matter repair; first-pass row captures lesion-remote white matter repair in mouse at abstract/source-title level..',
    'qualitative',
    NULL,
    'McCallum S 2026 M5A-P003-E002 preserves a distinct Mouse experiment testing Mechanistic outcome assessment after lesion-remote white matter repair with endpoint/readout: Outcome/mechanistic validation row for Lesion-remote astrocytes govern microglia-mediated white matter repair; first-pass row captures lesion-remote white matter repair in mouse at abstract/source-title level..',
    'M5A-P003-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Lesion-remote astrocytes govern microglia-mediated white matter repair. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M5A-P003-E002", "measurement_method_inference": null, "paper_tracker_id": "M5A-P003", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M5B-T003", "tracker_id": "M5B-O050"}'
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
    'Grumbles RM 2017 M5A-P004-E002 preserves a distinct Human experiment testing Mechanistic outcome assessment after ventral-root axon loss/remyelination pathology with endpoint/readout: Outcome/mechanistic validation row for Motoneuron Death after Human Spinal Cord Injury; first-pass row captures ventral-root axon loss/remyelination pathology in human at abstract/source-title level..',
    'qualitative',
    'immunostaining / histology / pathology',
    'Grumbles RM 2017 M5A-P004-E002 preserves a distinct Human experiment testing Mechanistic outcome assessment after ventral-root axon loss/remyelination pathology with endpoint/readout: Outcome/mechanistic validation row for Motoneuron Death after Human Spinal Cord Injury; first-pass row captures ventral-root axon loss/remyelination pathology in human at abstract/source-title level..',
    'M5A-P004-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Motoneuron Death after Human Spinal Cord Injury. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M5A-P004-E002", "measurement_method_inference": "immunostaining / histology / pathology", "paper_tracker_id": "M5A-P004", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M5B-T003", "tracker_id": "M5B-O051"}'
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
    'Han Q 2020 M5A-P005-E002 preserves a distinct Rodent model context experiment testing Mechanistic outcome assessment after axonal regeneration / cellular energetics with endpoint/readout: Outcome/mechanistic validation row for Restoring Cellular Energetics Promotes Axonal Regeneration and Functional Recovery after Spinal Cord Injury; first-pass row captures axonal regeneration / cellular energetics in rodent model context at abstract/source-title level..',
    'qualitative',
    'behavioral / functional recovery assay',
    'Han Q 2020 M5A-P005-E002 preserves a distinct Rodent model context experiment testing Mechanistic outcome assessment after axonal regeneration / cellular energetics with endpoint/readout: Outcome/mechanistic validation row for Restoring Cellular Energetics Promotes Axonal Regeneration and Functional Recovery after Spinal Cord Injury; first-pass row captures axonal regeneration / cellular energetics in rodent model context at abstract/source-title level..',
    'M5A-P005-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Restoring Cellular Energetics Promotes Axonal Regeneration and Functional Recovery after Spinal Cord Injury. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M5A-P005-E002", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P005", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M5B-T005", "tracker_id": "M5B-O052"}'
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
    'Kadoya K 2016 M5A-P007-E002 preserves a distinct Rat experiment testing Mechanistic outcome assessment after neural graft-enabled cst regeneration with endpoint/readout: Outcome/mechanistic validation row for Spinal cord reconstitution with homologous neural grafts enables robust corticospinal regeneration; first-pass row captures neural graft-enabled cst regeneration in rat at abstract/source-title level..',
    'qualitative',
    NULL,
    'Kadoya K 2016 M5A-P007-E002 preserves a distinct Rat experiment testing Mechanistic outcome assessment after neural graft-enabled cst regeneration with endpoint/readout: Outcome/mechanistic validation row for Spinal cord reconstitution with homologous neural grafts enables robust corticospinal regeneration; first-pass row captures neural graft-enabled cst regeneration in rat at abstract/source-title level..',
    'M5A-P007-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Spinal cord reconstitution with homologous neural grafts enables robust corticospinal regeneration. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M5A-P007-E002", "measurement_method_inference": null, "paper_tracker_id": "M5A-P007", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M5B-T006", "tracker_id": "M5B-O054"}'
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
    'Ma YH 2025 M5A-P010-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after corticospinal tract regeneration / sprouting with endpoint/readout: Outcome/mechanistic validation row for Transcranial Optogenetic Stimulation Promotes Corticospinal Tract Axon Regeneration to Repair Spinal Cord Injury by Activating the JAK2/STAT3 Pathway.; first-pass row captures corticospinal tract regeneration / sprouting in mouse sci model at abstract/source-title level..',
    'qualitative',
    NULL,
    'Ma YH 2025 M5A-P010-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after corticospinal tract regeneration / sprouting with endpoint/readout: Outcome/mechanistic validation row for Transcranial Optogenetic Stimulation Promotes Corticospinal Tract Axon Regeneration to Repair Spinal Cord Injury by Activating the JAK2/STAT3 Pathway.; first-pass row captures corticospinal tract regeneration / sprouting in mouse sci model at abstract/source-title level..',
    'M5A-P010-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Transcranial Optogenetic Stimulation Promotes Corticospinal Tract Axon Regeneration to Repair Spinal Cord Injury by Activating the JAK2/STAT3 Pathway.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M5A-P010-E002", "measurement_method_inference": null, "paper_tracker_id": "M5A-P010", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M5B-T007", "tracker_id": "M5B-O057"}'
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
    'Chen W 2024 M5A-P011-E002 preserves a distinct Rat SCI model experiment testing Mechanistic outcome assessment after corticospinal tract regeneration / sprouting with endpoint/readout: Outcome/mechanistic validation row for Lipin1 depletion coordinates neuronal signaling pathways to promote motor and sensory axon regeneration after spinal cord injury.; first-pass row captures corticospinal tract regeneration / sprouting in rat sci model at abstract/source-title level..',
    'qualitative',
    NULL,
    'Chen W 2024 M5A-P011-E002 preserves a distinct Rat SCI model experiment testing Mechanistic outcome assessment after corticospinal tract regeneration / sprouting with endpoint/readout: Outcome/mechanistic validation row for Lipin1 depletion coordinates neuronal signaling pathways to promote motor and sensory axon regeneration after spinal cord injury.; first-pass row captures corticospinal tract regeneration / sprouting in rat sci model at abstract/source-title level..',
    'M5A-P011-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Lipin1 depletion coordinates neuronal signaling pathways to promote motor and sensory axon regeneration after spinal cord injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M5A-P011-E002", "measurement_method_inference": null, "paper_tracker_id": "M5A-P011", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M5B-T005", "tracker_id": "M5B-O058"}'
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
    'Higuchi K 2024 M5A-P013-E002 preserves a distinct Experimental SCI model context experiment testing Mechanistic outcome assessment after corticospinal tract regeneration / sprouting with endpoint/readout: Outcome/mechanistic validation row for Synaptotagmin 4 Supports Spontaneous Axon Sprouting after Spinal Cord Injury.; first-pass row captures corticospinal tract regeneration / sprouting in experimental sci model context at abstract/source-title level..',
    'qualitative',
    NULL,
    'Higuchi K 2024 M5A-P013-E002 preserves a distinct Experimental SCI model context experiment testing Mechanistic outcome assessment after corticospinal tract regeneration / sprouting with endpoint/readout: Outcome/mechanistic validation row for Synaptotagmin 4 Supports Spontaneous Axon Sprouting after Spinal Cord Injury.; first-pass row captures corticospinal tract regeneration / sprouting in experimental sci model context at abstract/source-title level..',
    'M5A-P013-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Synaptotagmin 4 Supports Spontaneous Axon Sprouting after Spinal Cord Injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M5A-P013-E002", "measurement_method_inference": null, "paper_tracker_id": "M5A-P013", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M5B-T001", "tracker_id": "M5B-O060"}'
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
    'Sun W 2020 M5A-P014-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after corticospinal tract regeneration / sprouting with endpoint/readout: Outcome/mechanistic validation row for Gabapentinoid treatment promotes corticospinal plasticity and regeneration following murine spinal cord injury.; first-pass row captures corticospinal tract regeneration / sprouting in mouse sci model at abstract/source-title level..',
    'qualitative',
    NULL,
    'Sun W 2020 M5A-P014-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after corticospinal tract regeneration / sprouting with endpoint/readout: Outcome/mechanistic validation row for Gabapentinoid treatment promotes corticospinal plasticity and regeneration following murine spinal cord injury.; first-pass row captures corticospinal tract regeneration / sprouting in mouse sci model at abstract/source-title level..',
    'M5A-P014-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Gabapentinoid treatment promotes corticospinal plasticity and regeneration following murine spinal cord injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M5A-P014-E002", "measurement_method_inference": null, "paper_tracker_id": "M5A-P014", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M5B-T001", "tracker_id": "M5B-O061"}'
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
    'Stepankova K 2025 M5A-P015-E002 preserves a distinct Rat SCI model experiment testing Mechanistic outcome assessment after extrinsic inhibitory matrix / guidance pathway with endpoint/readout: Outcome/mechanistic validation row for Activated alpha 9 integrin expression enables sensory pathway reconstruction after spinal cord injury.; first-pass row captures extrinsic inhibitory matrix / guidance pathway in rat sci model at abstract/source-title level..',
    'qualitative',
    NULL,
    'Stepankova K 2025 M5A-P015-E002 preserves a distinct Rat SCI model experiment testing Mechanistic outcome assessment after extrinsic inhibitory matrix / guidance pathway with endpoint/readout: Outcome/mechanistic validation row for Activated alpha 9 integrin expression enables sensory pathway reconstruction after spinal cord injury.; first-pass row captures extrinsic inhibitory matrix / guidance pathway in rat sci model at abstract/source-title level..',
    'M5A-P015-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Activated alpha 9 integrin expression enables sensory pathway reconstruction after spinal cord injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M5A-P015-E002", "measurement_method_inference": null, "paper_tracker_id": "M5A-P015", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M5B-T002", "tracker_id": "M5B-O062"}'
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
    'Takatani H 2025 M5A-P016-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after corticospinal tract regeneration / sprouting with endpoint/readout: Outcome/mechanistic validation row for Modulation of Extrinsic and Intrinsic Signaling Together with Neuronal Activation Enhances Forelimb Motor Recovery after Cervical Spinal Cord Injury.; first-pass row captures corticospinal tract regeneration / sprouting in mouse sci model at abstract/source-title level..',
    'qualitative',
    'behavioral / functional recovery assay',
    'Takatani H 2025 M5A-P016-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after corticospinal tract regeneration / sprouting with endpoint/readout: Outcome/mechanistic validation row for Modulation of Extrinsic and Intrinsic Signaling Together with Neuronal Activation Enhances Forelimb Motor Recovery after Cervical Spinal Cord Injury.; first-pass row captures corticospinal tract regeneration / sprouting in mouse sci model at abstract/source-title level..',
    'M5A-P016-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Modulation of Extrinsic and Intrinsic Signaling Together with Neuronal Activation Enhances Forelimb Motor Recovery after Cervical Spinal Cord Injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M5A-P016-E002", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P016", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M5B-T001", "tracker_id": "M5B-O063"}'
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
    'van Niekerk EA 2025 M5A-P017-E002 preserves a distinct Human / translational context experiment testing Mechanistic outcome assessment after corticospinal tract regeneration / sprouting with endpoint/readout: Outcome/mechanistic validation row for Thiorphan reprograms neurons to promote functional recovery after spinal cord injury.; first-pass row captures corticospinal tract regeneration / sprouting in human / translational context at abstract/source-title level..',
    'qualitative',
    'behavioral / functional recovery assay',
    'van Niekerk EA 2025 M5A-P017-E002 preserves a distinct Human / translational context experiment testing Mechanistic outcome assessment after corticospinal tract regeneration / sprouting with endpoint/readout: Outcome/mechanistic validation row for Thiorphan reprograms neurons to promote functional recovery after spinal cord injury.; first-pass row captures corticospinal tract regeneration / sprouting in human / translational context at abstract/source-title level..',
    'M5A-P017-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Thiorphan reprograms neurons to promote functional recovery after spinal cord injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M5A-P017-E002", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P017", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M5B-T001", "tracker_id": "M5B-O064"}'
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
    'Zhang R 2026 M5A-P018-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after intrinsic neuronal growth competence with endpoint/readout: Outcome/mechanistic validation row for TTBK2-Driven Ciliogenesis Is Required for Intrinsic Neuronal Regeneration After Spinal Cord Injury.; first-pass row captures intrinsic neuronal growth competence in mouse sci model at abstract/source-title level..',
    'qualitative',
    NULL,
    'Zhang R 2026 M5A-P018-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after intrinsic neuronal growth competence with endpoint/readout: Outcome/mechanistic validation row for TTBK2-Driven Ciliogenesis Is Required for Intrinsic Neuronal Regeneration After Spinal Cord Injury.; first-pass row captures intrinsic neuronal growth competence in mouse sci model at abstract/source-title level..',
    'M5A-P018-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: TTBK2-Driven Ciliogenesis Is Required for Intrinsic Neuronal Regeneration After Spinal Cord Injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M5A-P018-E002", "measurement_method_inference": null, "paper_tracker_id": "M5A-P018", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M5B-T005", "tracker_id": "M5B-O065"}'
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
    'Attwell CL 2025 M5A-P019-E002 preserves a distinct Rat SCI model experiment testing Mechanistic outcome assessment after intrinsic neuronal growth competence with endpoint/readout: Outcome/mechanistic validation row for The transcription factor combination MEF2 and KLF7 promotes axonal sprouting in the injured spinal cord with functional improvement and regeneration-associated gene expression.; first-pass row captures intrinsic neuronal growth competence in rat sci model at abstract/source-title level..',
    'qualitative',
    NULL,
    'Attwell CL 2025 M5A-P019-E002 preserves a distinct Rat SCI model experiment testing Mechanistic outcome assessment after intrinsic neuronal growth competence with endpoint/readout: Outcome/mechanistic validation row for The transcription factor combination MEF2 and KLF7 promotes axonal sprouting in the injured spinal cord with functional improvement and regeneration-associated gene expression.; first-pass row captures intrinsic neuronal growth competence in rat sci model at abstract/source-title level..',
    'M5A-P019-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: The transcription factor combination MEF2 and KLF7 promotes axonal sprouting in the injured spinal cord with functional improvement and regeneration-associated gene expression.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M5A-P019-E002", "measurement_method_inference": null, "paper_tracker_id": "M5A-P019", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M5B-T005", "tracker_id": "M5B-O066"}'
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
    'Martinez-Rojas B 2025 M5A-P020-E002 preserves a distinct Rat SCI model experiment testing Mechanistic outcome assessment after corticospinal tract regeneration / sprouting with endpoint/readout: Outcome/mechanistic validation row for Stimulation of corticospinal neurons by optogenetic cAMP inductions promotes motor recovery after spinal cord injury in female rats via raphespinal tract modulation.; first-pass row captures corticospinal tract regeneration / sprouting in rat sci model at abstract/source-title level..',
    'qualitative',
    'behavioral / functional recovery assay',
    'Martinez-Rojas B 2025 M5A-P020-E002 preserves a distinct Rat SCI model experiment testing Mechanistic outcome assessment after corticospinal tract regeneration / sprouting with endpoint/readout: Outcome/mechanistic validation row for Stimulation of corticospinal neurons by optogenetic cAMP inductions promotes motor recovery after spinal cord injury in female rats via raphespinal tract modulation.; first-pass row captures corticospinal tract regeneration / sprouting in rat sci model at abstract/source-title level..',
    'M5A-P020-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Stimulation of corticospinal neurons by optogenetic cAMP inductions promotes motor recovery after spinal cord injury in female rats via raphespinal tract modulation.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M5A-P020-E002", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P020", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M5B-T007", "tracker_id": "M5B-O067"}'
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
    'Ji Z 2025 M5A-P021-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after corticospinal tract regeneration / sprouting with endpoint/readout: Outcome/mechanistic validation row for Precise rewiring of corticospinal axons and spinal interneurons via near-infrared optogenetics for spinal cord injury treatment.; first-pass row captures corticospinal tract regeneration / sprouting in mouse sci model at abstract/source-title level..',
    'qualitative',
    NULL,
    'Ji Z 2025 M5A-P021-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after corticospinal tract regeneration / sprouting with endpoint/readout: Outcome/mechanistic validation row for Precise rewiring of corticospinal axons and spinal interneurons via near-infrared optogenetics for spinal cord injury treatment.; first-pass row captures corticospinal tract regeneration / sprouting in mouse sci model at abstract/source-title level..',
    'M5A-P021-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Precise rewiring of corticospinal axons and spinal interneurons via near-infrared optogenetics for spinal cord injury treatment.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M5A-P021-E002", "measurement_method_inference": null, "paper_tracker_id": "M5A-P021", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M5B-T007", "tracker_id": "M5B-O068"}'
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
    'Zheng ML 2025 M5A-P023-E002 preserves a distinct Human / translational context experiment testing Mechanistic outcome assessment after extrinsic inhibitory matrix / guidance pathway with endpoint/readout: Outcome/mechanistic validation row for Lentivirus-mediated overexpression of netrin-1/DCC co-expression promotes axonal regeneration and functional recovery in spinal cord injury via the inhibition of the NgR1-RhoA-ROCK signaling pathway.; first-pass row captures extrinsic inhibitory matrix / guidance pathway in human / translational context at abstract/source-title level..',
    'qualitative',
    'behavioral / functional recovery assay',
    'Zheng ML 2025 M5A-P023-E002 preserves a distinct Human / translational context experiment testing Mechanistic outcome assessment after extrinsic inhibitory matrix / guidance pathway with endpoint/readout: Outcome/mechanistic validation row for Lentivirus-mediated overexpression of netrin-1/DCC co-expression promotes axonal regeneration and functional recovery in spinal cord injury via the inhibition of the NgR1-RhoA-ROCK signaling pathway.; first-pass row captures extrinsic inhibitory matrix / guidance pathway in human / translational context at abstract/source-title level..',
    'M5A-P023-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Lentivirus-mediated overexpression of netrin-1/DCC co-expression promotes axonal regeneration and functional recovery in spinal cord injury via the inhibition of the NgR1-RhoA-ROCK signaling pathway.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M5A-P023-E002", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P023", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M5B-T002", "tracker_id": "M5B-O070"}'
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
    'Zheng Y 2026 M5A-P024-E002 preserves a distinct Rat SCI model experiment testing Mechanistic outcome assessment after extrinsic inhibitory matrix / guidance pathway with endpoint/readout: Outcome/mechanistic validation row for Disrupting CSPG-Driven Microglia-Astrocyte Crosstalk Enables Scar-Free Repair in Spinal Cord Injury.; first-pass row captures extrinsic inhibitory matrix / guidance pathway in rat sci model at abstract/source-title level..',
    'qualitative',
    NULL,
    'Zheng Y 2026 M5A-P024-E002 preserves a distinct Rat SCI model experiment testing Mechanistic outcome assessment after extrinsic inhibitory matrix / guidance pathway with endpoint/readout: Outcome/mechanistic validation row for Disrupting CSPG-Driven Microglia-Astrocyte Crosstalk Enables Scar-Free Repair in Spinal Cord Injury.; first-pass row captures extrinsic inhibitory matrix / guidance pathway in rat sci model at abstract/source-title level..',
    'M5A-P024-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Disrupting CSPG-Driven Microglia-Astrocyte Crosstalk Enables Scar-Free Repair in Spinal Cord Injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M5A-P024-E002", "measurement_method_inference": null, "paper_tracker_id": "M5A-P024", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M5B-T002", "tracker_id": "M5B-O071"}'
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
    'Qu W 2025 M5A-P025-E002 preserves a distinct Human / translational context experiment testing Mechanistic outcome assessment after serotonergic/propriospinal relay plasticity with endpoint/readout: Outcome/mechanistic validation row for Chondroitinase ABC combined with Schwann cell transplantation enhances restoration of neural connection and functional recovery following acute and chronic spinal cord injury.; first-pass row captures serotonergic/propriospinal relay plasticity in human / translational context at abstract/source-title level..',
    'qualitative',
    'behavioral / functional recovery assay',
    'Qu W 2025 M5A-P025-E002 preserves a distinct Human / translational context experiment testing Mechanistic outcome assessment after serotonergic/propriospinal relay plasticity with endpoint/readout: Outcome/mechanistic validation row for Chondroitinase ABC combined with Schwann cell transplantation enhances restoration of neural connection and functional recovery following acute and chronic spinal cord injury.; first-pass row captures serotonergic/propriospinal relay plasticity in human / translational context at abstract/source-title level..',
    'M5A-P025-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Chondroitinase ABC combined with Schwann cell transplantation enhances restoration of neural connection and functional recovery following acute and chronic spinal cord injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M5A-P025-E002", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P025", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M5B-T004", "tracker_id": "M5B-O072"}'
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
    'Farner L 2026 M5A-P027-E002 preserves a distinct Rat SCI model experiment testing Mechanistic outcome assessment after corticospinal tract regeneration / sprouting with endpoint/readout: Outcome/mechanistic validation row for Anti-Nogo-A NG101 treatment induces changes in spinal cord micro- and macrostructure following spinal cord injury.; first-pass row captures corticospinal tract regeneration / sprouting in rat sci model at abstract/source-title level..',
    'qualitative',
    NULL,
    'Farner L 2026 M5A-P027-E002 preserves a distinct Rat SCI model experiment testing Mechanistic outcome assessment after corticospinal tract regeneration / sprouting with endpoint/readout: Outcome/mechanistic validation row for Anti-Nogo-A NG101 treatment induces changes in spinal cord micro- and macrostructure following spinal cord injury.; first-pass row captures corticospinal tract regeneration / sprouting in rat sci model at abstract/source-title level..',
    'M5A-P027-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Anti-Nogo-A NG101 treatment induces changes in spinal cord micro- and macrostructure following spinal cord injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M5A-P027-E002", "measurement_method_inference": null, "paper_tracker_id": "M5A-P027", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M5B-T002", "tracker_id": "M5B-O074"}'
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
    'Nori S 2018 M5A-P028-E002 preserves a distinct Human / translational context experiment testing Mechanistic outcome assessment after remyelination / white matter repair with endpoint/readout: Outcome/mechanistic validation row for Human Oligodendrogenic Neural Progenitor Cells Delivered with Chondroitinase ABC Facilitate Functional Repair of Chronic Spinal Cord Injury.; first-pass row captures remyelination / white matter repair in human / translational context at abstract/source-title level..',
    'qualitative',
    NULL,
    'Nori S 2018 M5A-P028-E002 preserves a distinct Human / translational context experiment testing Mechanistic outcome assessment after remyelination / white matter repair with endpoint/readout: Outcome/mechanistic validation row for Human Oligodendrogenic Neural Progenitor Cells Delivered with Chondroitinase ABC Facilitate Functional Repair of Chronic Spinal Cord Injury.; first-pass row captures remyelination / white matter repair in human / translational context at abstract/source-title level..',
    'M5A-P028-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Human Oligodendrogenic Neural Progenitor Cells Delivered with Chondroitinase ABC Facilitate Functional Repair of Chronic Spinal Cord Injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M5A-P028-E002", "measurement_method_inference": null, "paper_tracker_id": "M5A-P028", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M5B-T003", "tracker_id": "M5B-O075"}'
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
    'Wu Z 2026 M5A-P029-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after remyelination / white matter repair with endpoint/readout: Outcome/mechanistic validation row for TREM2 Facilitates Myelin Debris Clearance but Exacerbates Chronic Inflammation and Fibrosis After Spinal Cord Injury.; first-pass row captures remyelination / white matter repair in mouse sci model at abstract/source-title level..',
    'qualitative',
    NULL,
    'Wu Z 2026 M5A-P029-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after remyelination / white matter repair with endpoint/readout: Outcome/mechanistic validation row for TREM2 Facilitates Myelin Debris Clearance but Exacerbates Chronic Inflammation and Fibrosis After Spinal Cord Injury.; first-pass row captures remyelination / white matter repair in mouse sci model at abstract/source-title level..',
    'M5A-P029-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: TREM2 Facilitates Myelin Debris Clearance but Exacerbates Chronic Inflammation and Fibrosis After Spinal Cord Injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M5A-P029-E002", "measurement_method_inference": null, "paper_tracker_id": "M5A-P029", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M5B-T003", "tracker_id": "M5B-O076"}'
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
    'McCallum S 2026 M5A-P030-E002 preserves a distinct Human / translational context experiment testing Mechanistic outcome assessment after remyelination / white matter repair with endpoint/readout: Outcome/mechanistic validation row for Lesion-remote astrocytes govern microglia-mediated white matter repair.; first-pass row captures remyelination / white matter repair in human / translational context at abstract/source-title level..',
    'qualitative',
    NULL,
    'McCallum S 2026 M5A-P030-E002 preserves a distinct Human / translational context experiment testing Mechanistic outcome assessment after remyelination / white matter repair with endpoint/readout: Outcome/mechanistic validation row for Lesion-remote astrocytes govern microglia-mediated white matter repair.; first-pass row captures remyelination / white matter repair in human / translational context at abstract/source-title level..',
    'M5A-P030-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Lesion-remote astrocytes govern microglia-mediated white matter repair.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M5A-P030-E002", "measurement_method_inference": null, "paper_tracker_id": "M5A-P030", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M5B-T003", "tracker_id": "M5B-O077"}'
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
    'Manesh SB 2025 M5A-P031-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after remyelination / white matter repair with endpoint/readout: Outcome/mechanistic validation row for Compensatory changes after spinal cord injury in a remyelination deficient mouse model.; first-pass row captures remyelination / white matter repair in mouse sci model at abstract/source-title level..',
    'qualitative',
    'genetic perturbation / knockdown assay',
    'Manesh SB 2025 M5A-P031-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after remyelination / white matter repair with endpoint/readout: Outcome/mechanistic validation row for Compensatory changes after spinal cord injury in a remyelination deficient mouse model.; first-pass row captures remyelination / white matter repair in mouse sci model at abstract/source-title level..',
    'M5A-P031-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Compensatory changes after spinal cord injury in a remyelination deficient mouse model.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M5A-P031-E002", "measurement_method_inference": "genetic perturbation / knockdown assay", "paper_tracker_id": "M5A-P031", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M5B-T003", "tracker_id": "M5B-O078"}'
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
    'Zhou Y 2025 M5A-P032-E002 preserves a distinct Rat SCI model experiment testing Mechanistic outcome assessment after remyelination / white matter repair with endpoint/readout: Outcome/mechanistic validation row for A Myelin Debris Cleaner for Spinal Cord Injury Recovery: Polycaprolactone / Cell Membrane Assembled Scaffolds.; first-pass row captures remyelination / white matter repair in rat sci model at abstract/source-title level..',
    'qualitative',
    'behavioral / functional recovery assay',
    'Zhou Y 2025 M5A-P032-E002 preserves a distinct Rat SCI model experiment testing Mechanistic outcome assessment after remyelination / white matter repair with endpoint/readout: Outcome/mechanistic validation row for A Myelin Debris Cleaner for Spinal Cord Injury Recovery: Polycaprolactone / Cell Membrane Assembled Scaffolds.; first-pass row captures remyelination / white matter repair in rat sci model at abstract/source-title level..',
    'M5A-P032-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: A Myelin Debris Cleaner for Spinal Cord Injury Recovery: Polycaprolactone / Cell Membrane Assembled Scaffolds.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M5A-P032-E002", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P032", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M5B-T003", "tracker_id": "M5B-O079"}'
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
    'Li C 2026 M5A-P033-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after serotonergic/propriospinal relay plasticity with endpoint/readout: Outcome/mechanistic validation row for Serotonergic System-Targeted Nucleic Acid Hydrogel Coordinates Excitability Restoration and Circuit Reconstruction for Spinal Cord Injury Therapy.; first-pass row captures serotonergic/propriospinal relay plasticity in mouse sci model at abstract/source-title level..',
    'qualitative',
    NULL,
    'Li C 2026 M5A-P033-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after serotonergic/propriospinal relay plasticity with endpoint/readout: Outcome/mechanistic validation row for Serotonergic System-Targeted Nucleic Acid Hydrogel Coordinates Excitability Restoration and Circuit Reconstruction for Spinal Cord Injury Therapy.; first-pass row captures serotonergic/propriospinal relay plasticity in mouse sci model at abstract/source-title level..',
    'M5A-P033-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Serotonergic System-Targeted Nucleic Acid Hydrogel Coordinates Excitability Restoration and Circuit Reconstruction for Spinal Cord Injury Therapy.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M5A-P033-E002", "measurement_method_inference": null, "paper_tracker_id": "M5A-P033", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M5B-T004", "tracker_id": "M5B-O080"}'
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
    'Sysoev YI 2025 M5A-P034-E002 preserves a distinct Rat SCI model experiment testing Mechanistic outcome assessment after serotonergic/propriospinal relay plasticity with endpoint/readout: Outcome/mechanistic validation row for Central Serotonin Deficiency Impairs Recovery of Sensorimotor Abilities After Spinal Cord Injury in Rats.; first-pass row captures serotonergic/propriospinal relay plasticity in rat sci model at abstract/source-title level..',
    'qualitative',
    'genetic perturbation / knockdown assay; behavioral / functional recovery assay',
    'Sysoev YI 2025 M5A-P034-E002 preserves a distinct Rat SCI model experiment testing Mechanistic outcome assessment after serotonergic/propriospinal relay plasticity with endpoint/readout: Outcome/mechanistic validation row for Central Serotonin Deficiency Impairs Recovery of Sensorimotor Abilities After Spinal Cord Injury in Rats.; first-pass row captures serotonergic/propriospinal relay plasticity in rat sci model at abstract/source-title level..',
    'M5A-P034-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Central Serotonin Deficiency Impairs Recovery of Sensorimotor Abilities After Spinal Cord Injury in Rats.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M5A-P034-E002", "measurement_method_inference": "genetic perturbation / knockdown assay; behavioral / functional recovery assay", "paper_tracker_id": "M5A-P034", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M5B-T004", "tracker_id": "M5B-O081"}'
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
    'Wang Y 2025 M5A-P036-E002 preserves a distinct Rat SCI model experiment testing Mechanistic outcome assessment after serotonergic/propriospinal relay plasticity with endpoint/readout: Outcome/mechanistic validation row for Functional recovery induced by KCC2-enabled relay pathways in completely injured spinal cords in adult rats.; first-pass row captures serotonergic/propriospinal relay plasticity in rat sci model at abstract/source-title level..',
    'qualitative',
    'behavioral / functional recovery assay',
    'Wang Y 2025 M5A-P036-E002 preserves a distinct Rat SCI model experiment testing Mechanistic outcome assessment after serotonergic/propriospinal relay plasticity with endpoint/readout: Outcome/mechanistic validation row for Functional recovery induced by KCC2-enabled relay pathways in completely injured spinal cords in adult rats.; first-pass row captures serotonergic/propriospinal relay plasticity in rat sci model at abstract/source-title level..',
    'M5A-P036-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Functional recovery induced by KCC2-enabled relay pathways in completely injured spinal cords in adult rats.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M5A-P036-E002", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P036", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M5B-T004", "tracker_id": "M5B-O083"}'
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
    'Zhao H 2025 M5A-P037-E002 preserves a distinct Rat SCI model experiment testing Mechanistic outcome assessment after serotonergic/propriospinal relay plasticity with endpoint/readout: Outcome/mechanistic validation row for Functionalized nanozyme delivery of a KCC2-activator conjugate for the promotion of functional recovery after acute spinal cord injury.; first-pass row captures serotonergic/propriospinal relay plasticity in rat sci model at abstract/source-title level..',
    'qualitative',
    'behavioral / functional recovery assay',
    'Zhao H 2025 M5A-P037-E002 preserves a distinct Rat SCI model experiment testing Mechanistic outcome assessment after serotonergic/propriospinal relay plasticity with endpoint/readout: Outcome/mechanistic validation row for Functionalized nanozyme delivery of a KCC2-activator conjugate for the promotion of functional recovery after acute spinal cord injury.; first-pass row captures serotonergic/propriospinal relay plasticity in rat sci model at abstract/source-title level..',
    'M5A-P037-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Functionalized nanozyme delivery of a KCC2-activator conjugate for the promotion of functional recovery after acute spinal cord injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M5A-P037-E002", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P037", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M5B-T004", "tracker_id": "M5B-O084"}'
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
    'Morozumi M 2025 M5A-P038-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after serotonergic/propriospinal relay plasticity with endpoint/readout: Outcome/mechanistic validation row for Enhanced locomotor recovery in mice lacking GlcNAc6ST1 and GlcNAc6ST4 following spinal cord injury.; first-pass row captures serotonergic/propriospinal relay plasticity in mouse sci model at abstract/source-title level..',
    'qualitative',
    'behavioral / functional recovery assay',
    'Morozumi M 2025 M5A-P038-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after serotonergic/propriospinal relay plasticity with endpoint/readout: Outcome/mechanistic validation row for Enhanced locomotor recovery in mice lacking GlcNAc6ST1 and GlcNAc6ST4 following spinal cord injury.; first-pass row captures serotonergic/propriospinal relay plasticity in mouse sci model at abstract/source-title level..',
    'M5A-P038-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Enhanced locomotor recovery in mice lacking GlcNAc6ST1 and GlcNAc6ST4 following spinal cord injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M5A-P038-E002", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P038", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M5B-T004", "tracker_id": "M5B-O085"}'
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
    'Wang Y 2023 M5A-P040-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after corticospinal tract regeneration / sprouting with endpoint/readout: Outcome/mechanistic validation row for Osteopontin enhances the effect of treadmill training and promotes functional recovery after spinal cord injury.; first-pass row captures corticospinal tract regeneration / sprouting in mouse sci model at abstract/source-title level..',
    'qualitative',
    'behavioral / functional recovery assay',
    'Wang Y 2023 M5A-P040-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after corticospinal tract regeneration / sprouting with endpoint/readout: Outcome/mechanistic validation row for Osteopontin enhances the effect of treadmill training and promotes functional recovery after spinal cord injury.; first-pass row captures corticospinal tract regeneration / sprouting in mouse sci model at abstract/source-title level..',
    'M5A-P040-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Osteopontin enhances the effect of treadmill training and promotes functional recovery after spinal cord injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M5A-P040-E002", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P040", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M5B-T007", "tracker_id": "M5B-O087"}'
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
    'Tao N 2023 M5A-P041-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after graft/scaffold-enabled axon repair with endpoint/readout: Outcome/mechanistic validation row for Co-overexpression of OPN, IGF-1 and CNTF augment the therapeutic effect of DPSC on spinal cord injury.; first-pass row captures graft/scaffold-enabled axon repair in mouse sci model at abstract/source-title level..',
    'qualitative',
    NULL,
    'Tao N 2023 M5A-P041-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after graft/scaffold-enabled axon repair with endpoint/readout: Outcome/mechanistic validation row for Co-overexpression of OPN, IGF-1 and CNTF augment the therapeutic effect of DPSC on spinal cord injury.; first-pass row captures graft/scaffold-enabled axon repair in mouse sci model at abstract/source-title level..',
    'M5A-P041-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Co-overexpression of OPN, IGF-1 and CNTF augment the therapeutic effect of DPSC on spinal cord injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M5A-P041-E002", "measurement_method_inference": null, "paper_tracker_id": "M5A-P041", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M5B-T006", "tracker_id": "M5B-O088"}'
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
    'Ye J 2025 M5A-P042-E002 preserves a distinct Rat SCI model experiment testing Mechanistic outcome assessment after graft/scaffold-enabled axon repair with endpoint/readout: Outcome/mechanistic validation row for Multichannel 3D-Printed Bioactive Scaffold Combined with Small Interfering RNA Delivery to Promote Neurological Recovery after Spinal Cord Injury.; first-pass row captures graft/scaffold-enabled axon repair in rat sci model at abstract/source-title level..',
    'qualitative',
    'behavioral / functional recovery assay',
    'Ye J 2025 M5A-P042-E002 preserves a distinct Rat SCI model experiment testing Mechanistic outcome assessment after graft/scaffold-enabled axon repair with endpoint/readout: Outcome/mechanistic validation row for Multichannel 3D-Printed Bioactive Scaffold Combined with Small Interfering RNA Delivery to Promote Neurological Recovery after Spinal Cord Injury.; first-pass row captures graft/scaffold-enabled axon repair in rat sci model at abstract/source-title level..',
    'M5A-P042-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Multichannel 3D-Printed Bioactive Scaffold Combined with Small Interfering RNA Delivery to Promote Neurological Recovery after Spinal Cord Injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M5A-P042-E002", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P042", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M5B-T006", "tracker_id": "M5B-O089"}'
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
    'McGuire TK 2026 M5A-P043-E002 preserves a distinct Rat SCI model experiment testing Mechanistic outcome assessment after intrinsic neuronal growth competence with endpoint/readout: Outcome/mechanistic validation row for Development of a <i>PTEN</i>-siRNA activated scaffold to promote axonal regrowth following spinal cord injury.; first-pass row captures intrinsic neuronal growth competence in rat sci model at abstract/source-title level..',
    'qualitative',
    'genetic perturbation / knockdown assay',
    'McGuire TK 2026 M5A-P043-E002 preserves a distinct Rat SCI model experiment testing Mechanistic outcome assessment after intrinsic neuronal growth competence with endpoint/readout: Outcome/mechanistic validation row for Development of a <i>PTEN</i>-siRNA activated scaffold to promote axonal regrowth following spinal cord injury.; first-pass row captures intrinsic neuronal growth competence in rat sci model at abstract/source-title level..',
    'M5A-P043-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Development of a <i>PTEN</i>-siRNA activated scaffold to promote axonal regrowth following spinal cord injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M5A-P043-E002", "measurement_method_inference": "genetic perturbation / knockdown assay", "paper_tracker_id": "M5A-P043", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M5B-T005", "tracker_id": "M5B-O090"}'
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
    'Muller F 2026 M5A-P044-E002 preserves a distinct Rat SCI model experiment testing Mechanistic outcome assessment after intrinsic neuronal growth competence with endpoint/readout: Outcome/mechanistic validation row for CITED2 is a druggable epigenetic switch coupling neuronal maturation to regenerative decline.; first-pass row captures intrinsic neuronal growth competence in rat sci model at abstract/source-title level..',
    'qualitative',
    NULL,
    'Muller F 2026 M5A-P044-E002 preserves a distinct Rat SCI model experiment testing Mechanistic outcome assessment after intrinsic neuronal growth competence with endpoint/readout: Outcome/mechanistic validation row for CITED2 is a druggable epigenetic switch coupling neuronal maturation to regenerative decline.; first-pass row captures intrinsic neuronal growth competence in rat sci model at abstract/source-title level..',
    'M5A-P044-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: CITED2 is a druggable epigenetic switch coupling neuronal maturation to regenerative decline.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M5A-P044-E002", "measurement_method_inference": null, "paper_tracker_id": "M5A-P044", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M5B-T005", "tracker_id": "M5B-O091"}'
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
    'Couvrette LJ 2025 M5A-P045-E002 preserves a distinct Human / translational context experiment testing Mechanistic outcome assessment after graft/scaffold-enabled axon repair with endpoint/readout: Outcome/mechanistic validation row for Poly-L-Ornithine coated plant scaffolds support motor recovery in rats after traumatic spinal cord injury.; first-pass row captures graft/scaffold-enabled axon repair in human / translational context at abstract/source-title level..',
    'qualitative',
    'behavioral / functional recovery assay',
    'Couvrette LJ 2025 M5A-P045-E002 preserves a distinct Human / translational context experiment testing Mechanistic outcome assessment after graft/scaffold-enabled axon repair with endpoint/readout: Outcome/mechanistic validation row for Poly-L-Ornithine coated plant scaffolds support motor recovery in rats after traumatic spinal cord injury.; first-pass row captures graft/scaffold-enabled axon repair in human / translational context at abstract/source-title level..',
    'M5A-P045-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Poly-L-Ornithine coated plant scaffolds support motor recovery in rats after traumatic spinal cord injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M5A-P045-E002", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M5A-P045", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M5B-T006", "tracker_id": "M5B-O092"}'
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
    'Dong H 2025 M5A-P046-E002 preserves a distinct Rat SCI model experiment testing Mechanistic outcome assessment after remyelination / white matter repair with endpoint/readout: Outcome/mechanistic validation row for Integrating single-cell RNA sequencing and spatial multi-omics reveals the molecular signature of regeneration after spinal cord injury.; first-pass row captures remyelination / white matter repair in rat sci model at abstract/source-title level..',
    'qualitative',
    'single-cell RNA-seq / cell-state atlas; spatial transcriptomics / spatial atlas',
    'Dong H 2025 M5A-P046-E002 preserves a distinct Rat SCI model experiment testing Mechanistic outcome assessment after remyelination / white matter repair with endpoint/readout: Outcome/mechanistic validation row for Integrating single-cell RNA sequencing and spatial multi-omics reveals the molecular signature of regeneration after spinal cord injury.; first-pass row captures remyelination / white matter repair in rat sci model at abstract/source-title level..',
    'M5A-P046-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Integrating single-cell RNA sequencing and spatial multi-omics reveals the molecular signature of regeneration after spinal cord injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M5A-P046-E002", "measurement_method_inference": "single-cell RNA-seq / cell-state atlas; spatial transcriptomics / spatial atlas", "paper_tracker_id": "M5A-P046", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M5B-T003", "tracker_id": "M5B-O093"}'
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
    'Chize CM 2025 M5A-P047-E002 preserves a distinct Dog chronic SCI experiment testing Mechanistic outcome assessment after extrinsic inhibitory matrix / guidance pathway with endpoint/readout: Outcome/mechanistic validation row for A laminin-based therapy for dogs with chronic spinal cord injury: promising results of a longitudinal trial.; first-pass row captures extrinsic inhibitory matrix / guidance pathway in dog chronic sci at abstract/source-title level..',
    'qualitative',
    NULL,
    'Chize CM 2025 M5A-P047-E002 preserves a distinct Dog chronic SCI experiment testing Mechanistic outcome assessment after extrinsic inhibitory matrix / guidance pathway with endpoint/readout: Outcome/mechanistic validation row for A laminin-based therapy for dogs with chronic spinal cord injury: promising results of a longitudinal trial.; first-pass row captures extrinsic inhibitory matrix / guidance pathway in dog chronic sci at abstract/source-title level..',
    'M5A-P047-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: A laminin-based therapy for dogs with chronic spinal cord injury: promising results of a longitudinal trial.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M5A-P047-E002", "measurement_method_inference": null, "paper_tracker_id": "M5A-P047", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M5B-T002", "tracker_id": "M5B-O094"}'
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
    'Module 5A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M5A-P004", "topic_id": "M5B-T003", "tracker_id": "M5B-C018"}'
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
    'Module 5A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M5A-P023", "topic_id": "M5B-T002", "tracker_id": "M5B-C019"}'
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
    'Module 5A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M5A-P018", "topic_id": "M5B-T005", "tracker_id": "M5B-C021"}'
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
    'Module 5A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M5A-P044", "topic_id": "M5B-T005", "tracker_id": "M5B-C022"}'
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
    'Module 5A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M5A-P030", "topic_id": "M5B-T003", "tracker_id": "M5B-C023"}'
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
    'Module 5A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M5A-P028", "topic_id": "M5B-T006", "tracker_id": "M5B-C024"}'
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
    'Module 5A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M5A-P017", "topic_id": "M5B-T001", "tracker_id": "M5B-C025"}'
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
    'Module 5A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M5A-P047", "topic_id": "M5B-T002", "tracker_id": "M5B-C026"}'
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
    'Module 5A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M5A-P046", "topic_id": "M5B-T008", "tracker_id": "M5B-C028"}'
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
    'Module 5A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M5A-P031", "topic_id": "M5B-T003", "tracker_id": "M5B-C029"}'
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
    'Module 5A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M5A-P005", "topic_id": "M5B-T005", "tracker_id": "M5B-C030"}'
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
    'Module 5A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M5A-P045", "topic_id": "M5B-T006", "tracker_id": "M5B-C031"}'
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
    'Module 5A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M5A-P013", "topic_id": "M5B-T001", "tracker_id": "M5B-C033"}'
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
    'Module 5A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M5A-P033", "topic_id": "M5B-T004", "tracker_id": "M5B-C034"}'
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
