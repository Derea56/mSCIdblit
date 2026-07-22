-- Module 3B full first-pass materialization generated from tracker-derived JSON.
-- This script is intended for a fresh database loaded with schema/schema.sql and scripts/seed_controlled_vocab.sql.
BEGIN;

CREATE TEMP TABLE _m3_paper_map (tracker_id TEXT PRIMARY KEY, paper_id INTEGER NOT NULL);
CREATE TEMP TABLE _m3_paradigm_map (tracker_id TEXT PRIMARY KEY, paradigm_id INTEGER NOT NULL);
CREATE TEMP TABLE _m3_experiment_map (tracker_id TEXT PRIMARY KEY, experiment_id INTEGER NOT NULL);
CREATE TEMP TABLE _m3_observation_map (tracker_id TEXT PRIMARY KEY, observation_id INTEGER NOT NULL);
CREATE TEMP TABLE _m3_claim_map (tracker_id TEXT PRIMARY KEY, claim_id INTEGER NOT NULL);
CREATE TEMP TABLE _m3_link_map (tracker_id TEXT PRIMARY KEY, link_id INTEGER NOT NULL);
CREATE TEMP TABLE _m3_consensus_map (tracker_id TEXT PRIMARY KEY, consensus_id INTEGER NOT NULL);

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Delayed microglial depletion after spinal cord injury reduces chronic inflammation and neurodegeneration in the brain and improves neurological recovery in male mice', 'Li Y', 2020,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Chronic inflammation and remote degeneration anchor", "module": "Module 3B", "tracker_id": "M3A-P001"}'
  )
  RETURNING paper_id
)
INSERT INTO _m3_paper_map (tracker_id, paper_id) SELECT 'M3A-P001', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Microglia and macrophages promote corralling, wound compaction and recovery after spinal cord injury via Plexin-B2', 'Zhou X', 2020,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Immune-glial containment anchor", "module": "Module 3B", "tracker_id": "M3A-P002"}'
  )
  RETURNING paper_id
)
INSERT INTO _m3_paper_map (tracker_id, paper_id) SELECT 'M3A-P002', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'CSF1R Inhibition Reduces Microglia Proliferation, Promotes Tissue Preservation and Improves Motor Recovery After Spinal Cord Injury', 'Gerber YN', 2018,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Microglia/macrophage modulation anchor", "module": "Module 3B", "tracker_id": "M3A-P003"}'
  )
  RETURNING paper_id
)
INSERT INTO _m3_paper_map (tracker_id, paper_id) SELECT 'M3A-P003', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Inhibiting HMGB1-RAGE axis prevents pro-inflammatory macrophages/microglia polarization and affords neuroprotection after spinal cord injury', 'Fan H', 2020,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Mechanistic polarization anchor", "module": "Module 3B", "tracker_id": "M3A-P004"}'
  )
  RETURNING paper_id
)
INSERT INTO _m3_paper_map (tracker_id, paper_id) SELECT 'M3A-P004', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Macrophage Extracellular Traps Exacerbate Secondary Spinal Cord Injury by Modulating Macrophage/Microglia Polarization via LL37/P2X7R/NF-kappaB Signaling Pathway', 'Zhang C', 2022,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Innate immune injury-amplification anchor", "module": "Module 3B", "tracker_id": "M3A-P005"}'
  )
  RETURNING paper_id
)
INSERT INTO _m3_paper_map (tracker_id, paper_id) SELECT 'M3A-P005', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'IPSC-NSCs-derived exosomal let-7b-5p improves motor function after spinal cord Injury by modulating microglial/macrophage pyroptosis', 'Liu J', 2024,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Cell/exosome immune-modulation bridge", "module": "Module 3B", "tracker_id": "M3A-P006"}'
  )
  RETURNING paper_id
)
INSERT INTO _m3_paper_map (tracker_id, paper_id) SELECT 'M3A-P006', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Metabolic reprogramming through histone lactylation in microglia and macrophages recruits CD8+ T lymphocytes and aggravates spinal cord injury', 'Ge X', 2025,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Recent immune-state mechanism", "module": "Module 3B", "tracker_id": "M3A-P007"}'
  )
  RETURNING paper_id
)
INSERT INTO _m3_paper_map (tracker_id, paper_id) SELECT 'M3A-P007', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'N-Lactoyl-Phenylalanine modulates lipid metabolism in microglia/macrophage via the AMPK-PGC1alpha-PPARgamma pathway to promote recovery in mice with spinal cord injury.', 'Ying W', 2025,
    NULL, NULL, NULL,
    NULL, NULL, '40579710',
    NULL, '{"curator_notes": "N-lactoyl-phenylalanine metabolic immunomodulation anchor", "module": "Module 3B", "tracker_id": "M3A-P008"}'
  )
  RETURNING paper_id
)
INSERT INTO _m3_paper_map (tracker_id, paper_id) SELECT 'M3A-P008', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Naringenin alleviates spinal cord injury by ameliorating macrophage/microglia autophagy via progranulin stabilisation.', 'Wang C', 2026,
    NULL, NULL, NULL,
    NULL, NULL, '41520590',
    NULL, '{"curator_notes": "Natural-product autophagy/polarization anchor", "module": "Module 3B", "tracker_id": "M3A-P009"}'
  )
  RETURNING paper_id
)
INSERT INTO _m3_paper_map (tracker_id, paper_id) SELECT 'M3A-P009', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'A dual-drug sequential delivery hydrogel for programmatic microglia/macrophage polarization and function recovery in spinal cord injury.', 'Li Y', 2025,
    NULL, NULL, NULL,
    NULL, NULL, '41080728',
    NULL, '{"curator_notes": "Macrophage/microglia polarization signaling anchor", "module": "Module 3B", "tracker_id": "M3A-P010"}'
  )
  RETURNING paper_id
)
INSERT INTO _m3_paper_map (tracker_id, paper_id) SELECT 'M3A-P010', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Microenvironment Self-Adaptive Nanomedicine Promotes Spinal Cord Repair by Suppressing Inflammation Cascade and Neural Apoptosis.', 'Qian D', 2024,
    NULL, NULL, NULL,
    NULL, NULL, '39478649',
    NULL, '{"curator_notes": "Nanomedicine inflammation-cascade anchor", "module": "Module 3B", "tracker_id": "M3A-P011"}'
  )
  RETURNING paper_id
)
INSERT INTO _m3_paper_map (tracker_id, paper_id) SELECT 'M3A-P011', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Farrerol confers neuroprotection in spinal cord injury by regulating macrophages/microglia polarization through the JAK2/STAT3 pathway.', 'Chen Y', 2025,
    NULL, NULL, NULL,
    NULL, NULL, '40865787',
    NULL, '{"curator_notes": "JAK2/STAT3 polarization anchor", "module": "Module 3B", "tracker_id": "M3A-P012"}'
  )
  RETURNING paper_id
)
INSERT INTO _m3_paper_map (tracker_id, paper_id) SELECT 'M3A-P012', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'GDF11 alleviates spinal cord injury in rats by modulating microglia polarization through Smad2/3 and MAPK/NFkappaB signaling pathways.', 'Wang Z', 2025,
    NULL, NULL, NULL,
    NULL, NULL, '40674843',
    NULL, '{"curator_notes": "GDF11 microglial-polarization anchor", "module": "Module 3B", "tracker_id": "M3A-P013"}'
  )
  RETURNING paper_id
)
INSERT INTO _m3_paper_map (tracker_id, paper_id) SELECT 'M3A-P013', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Fisetin Promotes Functional Recovery after Spinal Cord Injury by Inhibiting Microglia/Macrophage M1 Polarization and JAK2/STAT3 Signaling Pathway.', 'Ji R', 2024,
    NULL, NULL, NULL,
    NULL, NULL, '39096281',
    NULL, '{"curator_notes": "Fisetin polarization anchor", "module": "Module 3B", "tracker_id": "M3A-P014"}'
  )
  RETURNING paper_id
)
INSERT INTO _m3_paper_map (tracker_id, paper_id) SELECT 'M3A-P014', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Atractylenolide III ameliorates spinal cord injury in rats by modulating microglial/macrophage polarization.', 'Xue MT', 2022,
    NULL, NULL, NULL,
    NULL, NULL, '35403332',
    NULL, '{"curator_notes": "Atractylenolide polarization anchor", "module": "Module 3B", "tracker_id": "M3A-P015"}'
  )
  RETURNING paper_id
)
INSERT INTO _m3_paper_map (tracker_id, paper_id) SELECT 'M3A-P015', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Engineered CCR2 positive macrophages coordinate immunoregulation with neural regeneration and matrix remodeling after spinal cord injury.', 'Zhao Y', 2026,
    NULL, NULL, NULL,
    NULL, NULL, '42370177',
    NULL, '{"curator_notes": "Single-cell / spatial immune-state mapping anchor", "module": "Module 3B", "tracker_id": "M3A-P016"}'
  )
  RETURNING paper_id
)
INSERT INTO _m3_paper_map (tracker_id, paper_id) SELECT 'M3A-P016', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'PLX5622 did not alter anxiety-like behaviour and showed limited microglial depletion efficacy in a spinal cord injury model in female rats.', 'Cucarian J', 2026,
    NULL, NULL, NULL,
    NULL, NULL, '42020492',
    NULL, '{"curator_notes": "Microglial depletion / CSF1R modulation anchor", "module": "Module 3B", "tracker_id": "M3A-P017"}'
  )
  RETURNING paper_id
)
INSERT INTO _m3_paper_map (tracker_id, paper_id) SELECT 'M3A-P017', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Nanoparticles loaded with a CSF1R antagonist selectively depletes microglial cells and modulates inflammation in spinal cord injury.', 'Yang J', 2025,
    NULL, NULL, NULL,
    NULL, NULL, '40749850',
    NULL, '{"curator_notes": "Microglial depletion / CSF1R modulation anchor", "module": "Module 3B", "tracker_id": "M3A-P018"}'
  )
  RETURNING paper_id
)
INSERT INTO _m3_paper_map (tracker_id, paper_id) SELECT 'M3A-P018', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Identification of repopulated microglia-associated genes in microglia depleted/repopulated mice after spinal cord injury.', 'Xue S', 2026,
    NULL, NULL, NULL,
    NULL, NULL, '41633463',
    NULL, '{"curator_notes": "Microglial depletion / CSF1R modulation anchor", "module": "Module 3B", "tracker_id": "M3A-P019"}'
  )
  RETURNING paper_id
)
INSERT INTO _m3_paper_map (tracker_id, paper_id) SELECT 'M3A-P019', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Nonresolving Neuroinflammation Regulates Axon Regeneration in Chronic Spinal Cord Injury.', 'Stewart AN', 2025,
    NULL, NULL, NULL,
    NULL, NULL, '39510834',
    NULL, '{"curator_notes": "Microglial depletion / CSF1R modulation anchor", "module": "Module 3B", "tracker_id": "M3A-P020"}'
  )
  RETURNING paper_id
)
INSERT INTO _m3_paper_map (tracker_id, paper_id) SELECT 'M3A-P020', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Depleting non-resolving neuroinflammation in chronic spinal cord injury attenuates thermal hypersensitivity.', 'Capes DE', 2026,
    NULL, NULL, NULL,
    NULL, NULL, '41698640',
    NULL, '{"curator_notes": "Microglial depletion / CSF1R modulation anchor", "module": "Module 3B", "tracker_id": "M3A-P021"}'
  )
  RETURNING paper_id
)
INSERT INTO _m3_paper_map (tracker_id, paper_id) SELECT 'M3A-P021', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Pharmacological Microglial Inhibition Remodels the Scar Microenvironment to Support Reticulospinal Circuit Reconstruction After Spinal Cord Injury.', 'Li R', 2026,
    NULL, NULL, NULL,
    NULL, NULL, '41103249',
    NULL, '{"curator_notes": "Microglial depletion / CSF1R modulation anchor", "module": "Module 3B", "tracker_id": "M3A-P022"}'
  )
  RETURNING paper_id
)
INSERT INTO _m3_paper_map (tracker_id, paper_id) SELECT 'M3A-P022', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'SYK-dependent lipid handling in monocyte-derived macrophages governs functional recovery after spinal cord injury.', 'Zhao Y', 2026,
    NULL, NULL, NULL,
    NULL, NULL, '41831796',
    NULL, '{"curator_notes": "Immune metabolism / lipid and debris handling anchor", "module": "Module 3B", "tracker_id": "M3A-P023"}'
  )
  RETURNING paper_id
)
INSERT INTO _m3_paper_map (tracker_id, paper_id) SELECT 'M3A-P023', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Lipid accumulation in foam cells drives C1q-dependent synaptic loss and impairs motor function recovery after spinal cord injury.', 'Peng Y', 2025,
    NULL, NULL, NULL,
    NULL, NULL, '41390852',
    NULL, '{"curator_notes": "Immune metabolism / lipid and debris handling anchor", "module": "Module 3B", "tracker_id": "M3A-P024"}'
  )
  RETURNING paper_id
)
INSERT INTO _m3_paper_map (tracker_id, paper_id) SELECT 'M3A-P024', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'TREM2 Facilitates Myelin Debris Clearance but Exacerbates Chronic Inflammation and Fibrosis After Spinal Cord Injury.', 'Wu Z', 2026,
    NULL, NULL, NULL,
    NULL, NULL, '41660680',
    NULL, '{"curator_notes": "Immune metabolism / lipid and debris handling anchor", "module": "Module 3B", "tracker_id": "M3A-P025"}'
  )
  RETURNING paper_id
)
INSERT INTO _m3_paper_map (tracker_id, paper_id) SELECT 'M3A-P025', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Histone H3K9 lactylation activates the TXNIP/NLRP3 pathway to drive macrophage inflammation after spinal cord injury.', 'Shi C', 2026,
    NULL, NULL, NULL,
    NULL, NULL, '41856077',
    NULL, '{"curator_notes": "Microglia/macrophage programmed inflammatory death anchor", "module": "Module 3B", "tracker_id": "M3A-P026"}'
  )
  RETURNING paper_id
)
INSERT INTO _m3_paper_map (tracker_id, paper_id) SELECT 'M3A-P026', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Targeting microglial PANoptosis through AMPK activation: Metformin as a promising therapy for spinal cord injury.', 'Liu S', 2026,
    NULL, NULL, NULL,
    NULL, NULL, '42199531',
    NULL, '{"curator_notes": "Microglia/macrophage programmed inflammatory death anchor", "module": "Module 3B", "tracker_id": "M3A-P027"}'
  )
  RETURNING paper_id
)
INSERT INTO _m3_paper_map (tracker_id, paper_id) SELECT 'M3A-P027', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Integrated Multi-Omics Analysis Reveals IRF1-Driven Microglial PANoptosis via ZBP1 in Spinal Cord Injury.', 'Xu X', 2026,
    NULL, NULL, NULL,
    NULL, NULL, '41867458',
    NULL, '{"curator_notes": "Macrophage/microglia polarization signaling anchor", "module": "Module 3B", "tracker_id": "M3A-P028"}'
  )
  RETURNING paper_id
)
INSERT INTO _m3_paper_map (tracker_id, paper_id) SELECT 'M3A-P028', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Trimethylamine N-Oxide Aggravates Neuro-inflammation in Spinal Cord Injury Through NLRP3 Inflammasome Activation in Microglia.', 'Qian S', 2026,
    NULL, NULL, NULL,
    NULL, NULL, '41954702',
    NULL, '{"curator_notes": "Microglia/macrophage programmed inflammatory death anchor", "module": "Module 3B", "tracker_id": "M3A-P029"}'
  )
  RETURNING paper_id
)
INSERT INTO _m3_paper_map (tracker_id, paper_id) SELECT 'M3A-P029', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Thiolutin attenuates neuroinflammation and neuronal apoptosis by suppressing microglial pyroptosis through NLRP3 inflammasome inhibition after spinal cord injury.', 'Zeng Y', 2026,
    NULL, NULL, NULL,
    NULL, NULL, '42240792',
    NULL, '{"curator_notes": "Macrophage/microglia polarization signaling anchor", "module": "Module 3B", "tracker_id": "M3A-P030"}'
  )
  RETURNING paper_id
)
INSERT INTO _m3_paper_map (tracker_id, paper_id) SELECT 'M3A-P030', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Type 2 Diabetes Promotes the Microglial Pyroptosis by Activating NLRP3 Inflammasome to Impede Remyelination After Spinal Cord Injury.', 'Xu J', 2026,
    NULL, NULL, NULL,
    NULL, NULL, '41988022',
    NULL, '{"curator_notes": "Macrophage/microglia polarization signaling anchor", "module": "Module 3B", "tracker_id": "M3A-P031"}'
  )
  RETURNING paper_id
)
INSERT INTO _m3_paper_map (tracker_id, paper_id) SELECT 'M3A-P031', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'FGF4 activates FGFR1 - PI3K/AKT signaling to enhance Clec10a-mediated intracellular myelin debris processing and promote spinal cord repair.', 'Lu W', 2026,
    NULL, NULL, NULL,
    NULL, NULL, '41724991',
    NULL, '{"curator_notes": "Microglia/macrophage programmed inflammatory death anchor", "module": "Module 3B", "tracker_id": "M3A-P032"}'
  )
  RETURNING paper_id
)
INSERT INTO _m3_paper_map (tracker_id, paper_id) SELECT 'M3A-P032', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'GP130 Regulates Macrophage Polarization and Functional Recovery after Spinal Cord Injury in Rats: A Single-Cell RNA Sequencing Study.', 'Gao M', 2026,
    NULL, NULL, NULL,
    NULL, NULL, '42455195',
    NULL, '{"curator_notes": "Macrophage/microglia polarization signaling anchor", "module": "Module 3B", "tracker_id": "M3A-P033"}'
  )
  RETURNING paper_id
)
INSERT INTO _m3_paper_map (tracker_id, paper_id) SELECT 'M3A-P033', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Temporal regulation of macrophage polarization by abnormally innervated CGRP + Sensory nerves following spinal cord injury.', 'Hu R', 2026,
    NULL, NULL, NULL,
    NULL, NULL, '41615465',
    NULL, '{"curator_notes": "Macrophage/microglia polarization signaling anchor", "module": "Module 3B", "tracker_id": "M3A-P034"}'
  )
  RETURNING paper_id
)
INSERT INTO _m3_paper_map (tracker_id, paper_id) SELECT 'M3A-P034', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Systemic Interleukin-4 Application Promotes Functional Recovery and Reprograms Neuroinflammatory and Molecular Responses after Spinal Cord Injury in Rats.', 'Alhalabi OT', 2026,
    NULL, NULL, NULL,
    NULL, NULL, '41799191',
    NULL, '{"curator_notes": "Macrophage/microglia polarization signaling anchor", "module": "Module 3B", "tracker_id": "M3A-P035"}'
  )
  RETURNING paper_id
)
INSERT INTO _m3_paper_map (tracker_id, paper_id) SELECT 'M3A-P035', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Omaveloxolone promotes functional recovery of spinal cord injury by reducing inflammatory response and regulating macrophage polarization.', 'Zhao P', 2025,
    NULL, NULL, NULL,
    NULL, NULL, '41602158',
    NULL, '{"curator_notes": "Macrophage/microglia polarization signaling anchor", "module": "Module 3B", "tracker_id": "M3A-P036"}'
  )
  RETURNING paper_id
)
INSERT INTO _m3_paper_map (tracker_id, paper_id) SELECT 'M3A-P036', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Localised delivery of interleukin-13 from a PLGA microparticle embedded GelMA hydrogel improves functional and histopathological recovery in a mouse contusion spinal cord injury model.', 'Walsh CM', 2025,
    NULL, NULL, NULL,
    NULL, NULL, '40822305',
    NULL, '{"curator_notes": "Immune-modifying biomaterial or vesicle delivery anchor", "module": "Module 3B", "tracker_id": "M3A-P037"}'
  )
  RETURNING paper_id
)
INSERT INTO _m3_paper_map (tracker_id, paper_id) SELECT 'M3A-P037', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Neonatal small extracellular vesicle-loaded GelNB hydrogel reprograms the vascular-immune microenvironment for spinal cord injury repair.', 'Yuan F', 2026,
    NULL, NULL, NULL,
    NULL, NULL, '42111233',
    NULL, '{"curator_notes": "Immune metabolism / lipid and debris handling anchor", "module": "Module 3B", "tracker_id": "M3A-P038"}'
  )
  RETURNING paper_id
)
INSERT INTO _m3_paper_map (tracker_id, paper_id) SELECT 'M3A-P038', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Dual-targeting nanoparticles enhance microglial P2Y12R expression to promote neuronal mitophagy for repairing spinal cord injury.', 'Tian Z', 2026,
    NULL, NULL, NULL,
    NULL, NULL, '42002569',
    NULL, '{"curator_notes": "Immune metabolism / lipid and debris handling anchor", "module": "Module 3B", "tracker_id": "M3A-P039"}'
  )
  RETURNING paper_id
)
INSERT INTO _m3_paper_map (tracker_id, paper_id) SELECT 'M3A-P039', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Targeted biohybrid nanoplatform for spinal cord injury treatment: Restoring microglial mitophagy and alleviating oxidative stress.', 'Deng Y', 2026,
    NULL, NULL, NULL,
    NULL, NULL, '42006707',
    NULL, '{"curator_notes": "Immune metabolism / lipid and debris handling anchor", "module": "Module 3B", "tracker_id": "M3A-P040"}'
  )
  RETURNING paper_id
)
INSERT INTO _m3_paper_map (tracker_id, paper_id) SELECT 'M3A-P040', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'An inflammation-targeted lipid nanoparticle inhibiting ferroptosis for spinal cord injury repair.', 'Lv Y', 2026,
    NULL, NULL, NULL,
    NULL, NULL, '42111765',
    NULL, '{"curator_notes": "Immune metabolism / lipid and debris handling anchor", "module": "Module 3B", "tracker_id": "M3A-P041"}'
  )
  RETURNING paper_id
)
INSERT INTO _m3_paper_map (tracker_id, paper_id) SELECT 'M3A-P041', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Integrating single-cell RNA sequencing and spatial multi-omics reveals the molecular signature of regeneration after spinal cord injury.', 'Dong H', 2025,
    NULL, NULL, NULL,
    NULL, NULL, '41121424',
    NULL, '{"curator_notes": "Immune metabolism / lipid and debris handling anchor", "module": "Module 3B", "tracker_id": "M3A-P042"}'
  )
  RETURNING paper_id
)
INSERT INTO _m3_paper_map (tracker_id, paper_id) SELECT 'M3A-P042', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Midkine Overexpression Promotes Functional Recovery After Spinal Cord Injury by Enhancing Microglial Efferocytosis Via LRP-1.', 'Wang Y', 2026,
    NULL, NULL, NULL,
    NULL, NULL, '41854297',
    NULL, '{"curator_notes": "Macrophage/microglia polarization signaling anchor", "module": "Module 3B", "tracker_id": "M3A-P043"}'
  )
  RETURNING paper_id
)
INSERT INTO _m3_paper_map (tracker_id, paper_id) SELECT 'M3A-P043', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'A reparative neutrophil subpopulation accelerates spinal cord regeneration in zebrafish by controlling macrophage inflammation via Il-4.', 'Tian X', 2026,
    NULL, NULL, NULL,
    NULL, NULL, '42192435',
    NULL, '{"curator_notes": "Macrophage/microglia polarization signaling anchor", "module": "Module 3B", "tracker_id": "M3A-P044"}'
  )
  RETURNING paper_id
)
INSERT INTO _m3_paper_map (tracker_id, paper_id) SELECT 'M3A-P044', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Profibrotic macrophage-derived CXCL4 promotes pericyte-to-myofibroblast transition after spinal cord injury.', 'Li G', 2026,
    NULL, NULL, NULL,
    NULL, NULL, '41836554',
    NULL, '{"curator_notes": "Macrophage-fibrotic scar interaction anchor", "module": "Module 3B", "tracker_id": "M3A-P045"}'
  )
  RETURNING paper_id
)
INSERT INTO _m3_paper_map (tracker_id, paper_id) SELECT 'M3A-P045', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'TGF--induced fibrotic scar formation limits recovery of spinal cord injury.', 'Pan D', 2026,
    NULL, NULL, NULL,
    NULL, NULL, '41741406',
    NULL, '{"curator_notes": "Macrophage-fibrotic scar interaction anchor", "module": "Module 3B", "tracker_id": "M3A-P046"}'
  )
  RETURNING paper_id
)
INSERT INTO _m3_paper_map (tracker_id, paper_id) SELECT 'M3A-P046', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Olfactory ensheathing cell transplantation targets macrophage extracellular traps and NKCC1 to alleviate pain after spinal cord injury.', 'Lei H', 2026,
    NULL, NULL, NULL,
    NULL, NULL, '42108539',
    NULL, '{"curator_notes": "Neutrophil or macrophage extracellular-trap axis anchor", "module": "Module 3B", "tracker_id": "M3A-P047"}'
  )
  RETURNING paper_id
)
INSERT INTO _m3_paper_map (tracker_id, paper_id) SELECT 'M3A-P047', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 3B curated evidence extraction',
    'First-pass Module 3B immune and myeloid modulation curation for M3A-P001',
    'Tracker-derived materialization from Module_3B_TRACKER.md'
  FROM _m3_paper_map WHERE tracker_id = 'M3A-P001'
  RETURNING paradigm_id
)
INSERT INTO _m3_paradigm_map (tracker_id, paradigm_id) SELECT 'M3A-P001', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 3B curated evidence extraction',
    'First-pass Module 3B immune and myeloid modulation curation for M3A-P002',
    'Tracker-derived materialization from Module_3B_TRACKER.md'
  FROM _m3_paper_map WHERE tracker_id = 'M3A-P002'
  RETURNING paradigm_id
)
INSERT INTO _m3_paradigm_map (tracker_id, paradigm_id) SELECT 'M3A-P002', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 3B curated evidence extraction',
    'First-pass Module 3B immune and myeloid modulation curation for M3A-P003',
    'Tracker-derived materialization from Module_3B_TRACKER.md'
  FROM _m3_paper_map WHERE tracker_id = 'M3A-P003'
  RETURNING paradigm_id
)
INSERT INTO _m3_paradigm_map (tracker_id, paradigm_id) SELECT 'M3A-P003', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 3B curated evidence extraction',
    'First-pass Module 3B immune and myeloid modulation curation for M3A-P004',
    'Tracker-derived materialization from Module_3B_TRACKER.md'
  FROM _m3_paper_map WHERE tracker_id = 'M3A-P004'
  RETURNING paradigm_id
)
INSERT INTO _m3_paradigm_map (tracker_id, paradigm_id) SELECT 'M3A-P004', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 3B curated evidence extraction',
    'First-pass Module 3B immune and myeloid modulation curation for M3A-P005',
    'Tracker-derived materialization from Module_3B_TRACKER.md'
  FROM _m3_paper_map WHERE tracker_id = 'M3A-P005'
  RETURNING paradigm_id
)
INSERT INTO _m3_paradigm_map (tracker_id, paradigm_id) SELECT 'M3A-P005', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 3B curated evidence extraction',
    'First-pass Module 3B immune and myeloid modulation curation for M3A-P006',
    'Tracker-derived materialization from Module_3B_TRACKER.md'
  FROM _m3_paper_map WHERE tracker_id = 'M3A-P006'
  RETURNING paradigm_id
)
INSERT INTO _m3_paradigm_map (tracker_id, paradigm_id) SELECT 'M3A-P006', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 3B curated evidence extraction',
    'First-pass Module 3B immune and myeloid modulation curation for M3A-P007',
    'Tracker-derived materialization from Module_3B_TRACKER.md'
  FROM _m3_paper_map WHERE tracker_id = 'M3A-P007'
  RETURNING paradigm_id
)
INSERT INTO _m3_paradigm_map (tracker_id, paradigm_id) SELECT 'M3A-P007', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 3B curated evidence extraction',
    'First-pass Module 3B immune and myeloid modulation curation for M3A-P008',
    'Tracker-derived materialization from Module_3B_TRACKER.md'
  FROM _m3_paper_map WHERE tracker_id = 'M3A-P008'
  RETURNING paradigm_id
)
INSERT INTO _m3_paradigm_map (tracker_id, paradigm_id) SELECT 'M3A-P008', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 3B curated evidence extraction',
    'First-pass Module 3B immune and myeloid modulation curation for M3A-P009',
    'Tracker-derived materialization from Module_3B_TRACKER.md'
  FROM _m3_paper_map WHERE tracker_id = 'M3A-P009'
  RETURNING paradigm_id
)
INSERT INTO _m3_paradigm_map (tracker_id, paradigm_id) SELECT 'M3A-P009', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 3B curated evidence extraction',
    'First-pass Module 3B immune and myeloid modulation curation for M3A-P010',
    'Tracker-derived materialization from Module_3B_TRACKER.md'
  FROM _m3_paper_map WHERE tracker_id = 'M3A-P010'
  RETURNING paradigm_id
)
INSERT INTO _m3_paradigm_map (tracker_id, paradigm_id) SELECT 'M3A-P010', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 3B curated evidence extraction',
    'First-pass Module 3B immune and myeloid modulation curation for M3A-P011',
    'Tracker-derived materialization from Module_3B_TRACKER.md'
  FROM _m3_paper_map WHERE tracker_id = 'M3A-P011'
  RETURNING paradigm_id
)
INSERT INTO _m3_paradigm_map (tracker_id, paradigm_id) SELECT 'M3A-P011', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 3B curated evidence extraction',
    'First-pass Module 3B immune and myeloid modulation curation for M3A-P012',
    'Tracker-derived materialization from Module_3B_TRACKER.md'
  FROM _m3_paper_map WHERE tracker_id = 'M3A-P012'
  RETURNING paradigm_id
)
INSERT INTO _m3_paradigm_map (tracker_id, paradigm_id) SELECT 'M3A-P012', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 3B curated evidence extraction',
    'First-pass Module 3B immune and myeloid modulation curation for M3A-P013',
    'Tracker-derived materialization from Module_3B_TRACKER.md'
  FROM _m3_paper_map WHERE tracker_id = 'M3A-P013'
  RETURNING paradigm_id
)
INSERT INTO _m3_paradigm_map (tracker_id, paradigm_id) SELECT 'M3A-P013', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 3B curated evidence extraction',
    'First-pass Module 3B immune and myeloid modulation curation for M3A-P014',
    'Tracker-derived materialization from Module_3B_TRACKER.md'
  FROM _m3_paper_map WHERE tracker_id = 'M3A-P014'
  RETURNING paradigm_id
)
INSERT INTO _m3_paradigm_map (tracker_id, paradigm_id) SELECT 'M3A-P014', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 3B curated evidence extraction',
    'First-pass Module 3B immune and myeloid modulation curation for M3A-P015',
    'Tracker-derived materialization from Module_3B_TRACKER.md'
  FROM _m3_paper_map WHERE tracker_id = 'M3A-P015'
  RETURNING paradigm_id
)
INSERT INTO _m3_paradigm_map (tracker_id, paradigm_id) SELECT 'M3A-P015', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 3B curated evidence extraction',
    'First-pass Module 3B immune and myeloid modulation curation for M3A-P016',
    'Tracker-derived materialization from Module_3B_TRACKER.md'
  FROM _m3_paper_map WHERE tracker_id = 'M3A-P016'
  RETURNING paradigm_id
)
INSERT INTO _m3_paradigm_map (tracker_id, paradigm_id) SELECT 'M3A-P016', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 3B curated evidence extraction',
    'First-pass Module 3B immune and myeloid modulation curation for M3A-P017',
    'Tracker-derived materialization from Module_3B_TRACKER.md'
  FROM _m3_paper_map WHERE tracker_id = 'M3A-P017'
  RETURNING paradigm_id
)
INSERT INTO _m3_paradigm_map (tracker_id, paradigm_id) SELECT 'M3A-P017', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 3B curated evidence extraction',
    'First-pass Module 3B immune and myeloid modulation curation for M3A-P018',
    'Tracker-derived materialization from Module_3B_TRACKER.md'
  FROM _m3_paper_map WHERE tracker_id = 'M3A-P018'
  RETURNING paradigm_id
)
INSERT INTO _m3_paradigm_map (tracker_id, paradigm_id) SELECT 'M3A-P018', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 3B curated evidence extraction',
    'First-pass Module 3B immune and myeloid modulation curation for M3A-P019',
    'Tracker-derived materialization from Module_3B_TRACKER.md'
  FROM _m3_paper_map WHERE tracker_id = 'M3A-P019'
  RETURNING paradigm_id
)
INSERT INTO _m3_paradigm_map (tracker_id, paradigm_id) SELECT 'M3A-P019', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 3B curated evidence extraction',
    'First-pass Module 3B immune and myeloid modulation curation for M3A-P020',
    'Tracker-derived materialization from Module_3B_TRACKER.md'
  FROM _m3_paper_map WHERE tracker_id = 'M3A-P020'
  RETURNING paradigm_id
)
INSERT INTO _m3_paradigm_map (tracker_id, paradigm_id) SELECT 'M3A-P020', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 3B curated evidence extraction',
    'First-pass Module 3B immune and myeloid modulation curation for M3A-P021',
    'Tracker-derived materialization from Module_3B_TRACKER.md'
  FROM _m3_paper_map WHERE tracker_id = 'M3A-P021'
  RETURNING paradigm_id
)
INSERT INTO _m3_paradigm_map (tracker_id, paradigm_id) SELECT 'M3A-P021', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 3B curated evidence extraction',
    'First-pass Module 3B immune and myeloid modulation curation for M3A-P022',
    'Tracker-derived materialization from Module_3B_TRACKER.md'
  FROM _m3_paper_map WHERE tracker_id = 'M3A-P022'
  RETURNING paradigm_id
)
INSERT INTO _m3_paradigm_map (tracker_id, paradigm_id) SELECT 'M3A-P022', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 3B curated evidence extraction',
    'First-pass Module 3B immune and myeloid modulation curation for M3A-P023',
    'Tracker-derived materialization from Module_3B_TRACKER.md'
  FROM _m3_paper_map WHERE tracker_id = 'M3A-P023'
  RETURNING paradigm_id
)
INSERT INTO _m3_paradigm_map (tracker_id, paradigm_id) SELECT 'M3A-P023', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 3B curated evidence extraction',
    'First-pass Module 3B immune and myeloid modulation curation for M3A-P024',
    'Tracker-derived materialization from Module_3B_TRACKER.md'
  FROM _m3_paper_map WHERE tracker_id = 'M3A-P024'
  RETURNING paradigm_id
)
INSERT INTO _m3_paradigm_map (tracker_id, paradigm_id) SELECT 'M3A-P024', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 3B curated evidence extraction',
    'First-pass Module 3B immune and myeloid modulation curation for M3A-P025',
    'Tracker-derived materialization from Module_3B_TRACKER.md'
  FROM _m3_paper_map WHERE tracker_id = 'M3A-P025'
  RETURNING paradigm_id
)
INSERT INTO _m3_paradigm_map (tracker_id, paradigm_id) SELECT 'M3A-P025', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 3B curated evidence extraction',
    'First-pass Module 3B immune and myeloid modulation curation for M3A-P026',
    'Tracker-derived materialization from Module_3B_TRACKER.md'
  FROM _m3_paper_map WHERE tracker_id = 'M3A-P026'
  RETURNING paradigm_id
)
INSERT INTO _m3_paradigm_map (tracker_id, paradigm_id) SELECT 'M3A-P026', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 3B curated evidence extraction',
    'First-pass Module 3B immune and myeloid modulation curation for M3A-P027',
    'Tracker-derived materialization from Module_3B_TRACKER.md'
  FROM _m3_paper_map WHERE tracker_id = 'M3A-P027'
  RETURNING paradigm_id
)
INSERT INTO _m3_paradigm_map (tracker_id, paradigm_id) SELECT 'M3A-P027', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 3B curated evidence extraction',
    'First-pass Module 3B immune and myeloid modulation curation for M3A-P028',
    'Tracker-derived materialization from Module_3B_TRACKER.md'
  FROM _m3_paper_map WHERE tracker_id = 'M3A-P028'
  RETURNING paradigm_id
)
INSERT INTO _m3_paradigm_map (tracker_id, paradigm_id) SELECT 'M3A-P028', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 3B curated evidence extraction',
    'First-pass Module 3B immune and myeloid modulation curation for M3A-P029',
    'Tracker-derived materialization from Module_3B_TRACKER.md'
  FROM _m3_paper_map WHERE tracker_id = 'M3A-P029'
  RETURNING paradigm_id
)
INSERT INTO _m3_paradigm_map (tracker_id, paradigm_id) SELECT 'M3A-P029', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 3B curated evidence extraction',
    'First-pass Module 3B immune and myeloid modulation curation for M3A-P030',
    'Tracker-derived materialization from Module_3B_TRACKER.md'
  FROM _m3_paper_map WHERE tracker_id = 'M3A-P030'
  RETURNING paradigm_id
)
INSERT INTO _m3_paradigm_map (tracker_id, paradigm_id) SELECT 'M3A-P030', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 3B curated evidence extraction',
    'First-pass Module 3B immune and myeloid modulation curation for M3A-P031',
    'Tracker-derived materialization from Module_3B_TRACKER.md'
  FROM _m3_paper_map WHERE tracker_id = 'M3A-P031'
  RETURNING paradigm_id
)
INSERT INTO _m3_paradigm_map (tracker_id, paradigm_id) SELECT 'M3A-P031', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 3B curated evidence extraction',
    'First-pass Module 3B immune and myeloid modulation curation for M3A-P032',
    'Tracker-derived materialization from Module_3B_TRACKER.md'
  FROM _m3_paper_map WHERE tracker_id = 'M3A-P032'
  RETURNING paradigm_id
)
INSERT INTO _m3_paradigm_map (tracker_id, paradigm_id) SELECT 'M3A-P032', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 3B curated evidence extraction',
    'First-pass Module 3B immune and myeloid modulation curation for M3A-P033',
    'Tracker-derived materialization from Module_3B_TRACKER.md'
  FROM _m3_paper_map WHERE tracker_id = 'M3A-P033'
  RETURNING paradigm_id
)
INSERT INTO _m3_paradigm_map (tracker_id, paradigm_id) SELECT 'M3A-P033', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 3B curated evidence extraction',
    'First-pass Module 3B immune and myeloid modulation curation for M3A-P034',
    'Tracker-derived materialization from Module_3B_TRACKER.md'
  FROM _m3_paper_map WHERE tracker_id = 'M3A-P034'
  RETURNING paradigm_id
)
INSERT INTO _m3_paradigm_map (tracker_id, paradigm_id) SELECT 'M3A-P034', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 3B curated evidence extraction',
    'First-pass Module 3B immune and myeloid modulation curation for M3A-P035',
    'Tracker-derived materialization from Module_3B_TRACKER.md'
  FROM _m3_paper_map WHERE tracker_id = 'M3A-P035'
  RETURNING paradigm_id
)
INSERT INTO _m3_paradigm_map (tracker_id, paradigm_id) SELECT 'M3A-P035', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 3B curated evidence extraction',
    'First-pass Module 3B immune and myeloid modulation curation for M3A-P036',
    'Tracker-derived materialization from Module_3B_TRACKER.md'
  FROM _m3_paper_map WHERE tracker_id = 'M3A-P036'
  RETURNING paradigm_id
)
INSERT INTO _m3_paradigm_map (tracker_id, paradigm_id) SELECT 'M3A-P036', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 3B curated evidence extraction',
    'First-pass Module 3B immune and myeloid modulation curation for M3A-P037',
    'Tracker-derived materialization from Module_3B_TRACKER.md'
  FROM _m3_paper_map WHERE tracker_id = 'M3A-P037'
  RETURNING paradigm_id
)
INSERT INTO _m3_paradigm_map (tracker_id, paradigm_id) SELECT 'M3A-P037', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 3B curated evidence extraction',
    'First-pass Module 3B immune and myeloid modulation curation for M3A-P038',
    'Tracker-derived materialization from Module_3B_TRACKER.md'
  FROM _m3_paper_map WHERE tracker_id = 'M3A-P038'
  RETURNING paradigm_id
)
INSERT INTO _m3_paradigm_map (tracker_id, paradigm_id) SELECT 'M3A-P038', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 3B curated evidence extraction',
    'First-pass Module 3B immune and myeloid modulation curation for M3A-P039',
    'Tracker-derived materialization from Module_3B_TRACKER.md'
  FROM _m3_paper_map WHERE tracker_id = 'M3A-P039'
  RETURNING paradigm_id
)
INSERT INTO _m3_paradigm_map (tracker_id, paradigm_id) SELECT 'M3A-P039', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 3B curated evidence extraction',
    'First-pass Module 3B immune and myeloid modulation curation for M3A-P040',
    'Tracker-derived materialization from Module_3B_TRACKER.md'
  FROM _m3_paper_map WHERE tracker_id = 'M3A-P040'
  RETURNING paradigm_id
)
INSERT INTO _m3_paradigm_map (tracker_id, paradigm_id) SELECT 'M3A-P040', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 3B curated evidence extraction',
    'First-pass Module 3B immune and myeloid modulation curation for M3A-P041',
    'Tracker-derived materialization from Module_3B_TRACKER.md'
  FROM _m3_paper_map WHERE tracker_id = 'M3A-P041'
  RETURNING paradigm_id
)
INSERT INTO _m3_paradigm_map (tracker_id, paradigm_id) SELECT 'M3A-P041', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 3B curated evidence extraction',
    'First-pass Module 3B immune and myeloid modulation curation for M3A-P042',
    'Tracker-derived materialization from Module_3B_TRACKER.md'
  FROM _m3_paper_map WHERE tracker_id = 'M3A-P042'
  RETURNING paradigm_id
)
INSERT INTO _m3_paradigm_map (tracker_id, paradigm_id) SELECT 'M3A-P042', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 3B curated evidence extraction',
    'First-pass Module 3B immune and myeloid modulation curation for M3A-P043',
    'Tracker-derived materialization from Module_3B_TRACKER.md'
  FROM _m3_paper_map WHERE tracker_id = 'M3A-P043'
  RETURNING paradigm_id
)
INSERT INTO _m3_paradigm_map (tracker_id, paradigm_id) SELECT 'M3A-P043', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 3B curated evidence extraction',
    'First-pass Module 3B immune and myeloid modulation curation for M3A-P044',
    'Tracker-derived materialization from Module_3B_TRACKER.md'
  FROM _m3_paper_map WHERE tracker_id = 'M3A-P044'
  RETURNING paradigm_id
)
INSERT INTO _m3_paradigm_map (tracker_id, paradigm_id) SELECT 'M3A-P044', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 3B curated evidence extraction',
    'First-pass Module 3B immune and myeloid modulation curation for M3A-P045',
    'Tracker-derived materialization from Module_3B_TRACKER.md'
  FROM _m3_paper_map WHERE tracker_id = 'M3A-P045'
  RETURNING paradigm_id
)
INSERT INTO _m3_paradigm_map (tracker_id, paradigm_id) SELECT 'M3A-P045', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 3B curated evidence extraction',
    'First-pass Module 3B immune and myeloid modulation curation for M3A-P046',
    'Tracker-derived materialization from Module_3B_TRACKER.md'
  FROM _m3_paper_map WHERE tracker_id = 'M3A-P046'
  RETURNING paradigm_id
)
INSERT INTO _m3_paradigm_map (tracker_id, paradigm_id) SELECT 'M3A-P046', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 3B curated evidence extraction',
    'First-pass Module 3B immune and myeloid modulation curation for M3A-P047',
    'Tracker-derived materialization from Module_3B_TRACKER.md'
  FROM _m3_paper_map WHERE tracker_id = 'M3A-P047'
  RETURNING paradigm_id
)
INSERT INTO _m3_paradigm_map (tracker_id, paradigm_id) SELECT 'M3A-P047', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / saturated A tracker',
    'Tracker experiment M3A-P001-E001',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O001"], "source_experiment_tracker_id": "M3A-P001-E001", "source_paper_tracker_id": "M3A-P001", "tracker_key": "M3A-P001::M3A-P001-E001"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P001'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P001::M3A-P001-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M3A-P001-E002',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O048"], "source_experiment_tracker_id": "M3A-P001-E002", "source_paper_tracker_id": "M3A-P001", "tracker_key": "M3A-P001::M3A-P001-E002"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P001'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P001::M3A-P001-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / saturated A tracker',
    'Tracker experiment M3A-P002-E001',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O002"], "source_experiment_tracker_id": "M3A-P002-E001", "source_paper_tracker_id": "M3A-P002", "tracker_key": "M3A-P002::M3A-P002-E001"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P002'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P002::M3A-P002-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M3A-P002-E002',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O049"], "source_experiment_tracker_id": "M3A-P002-E002", "source_paper_tracker_id": "M3A-P002", "tracker_key": "M3A-P002::M3A-P002-E002"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P002'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P002::M3A-P002-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / saturated A tracker',
    'Tracker experiment M3A-P003-E001',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O003"], "source_experiment_tracker_id": "M3A-P003-E001", "source_paper_tracker_id": "M3A-P003", "tracker_key": "M3A-P003::M3A-P003-E001"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P003'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P003::M3A-P003-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M3A-P003-E002',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O050"], "source_experiment_tracker_id": "M3A-P003-E002", "source_paper_tracker_id": "M3A-P003", "tracker_key": "M3A-P003::M3A-P003-E002"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P003'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P003::M3A-P003-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / saturated A tracker',
    'Tracker experiment M3A-P004-E001',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O004"], "source_experiment_tracker_id": "M3A-P004-E001", "source_paper_tracker_id": "M3A-P004", "tracker_key": "M3A-P004::M3A-P004-E001"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P004'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P004::M3A-P004-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M3A-P004-E002',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O051"], "source_experiment_tracker_id": "M3A-P004-E002", "source_paper_tracker_id": "M3A-P004", "tracker_key": "M3A-P004::M3A-P004-E002"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P004'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P004::M3A-P004-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / saturated A tracker',
    'Tracker experiment M3A-P005-E001',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O005"], "source_experiment_tracker_id": "M3A-P005-E001", "source_paper_tracker_id": "M3A-P005", "tracker_key": "M3A-P005::M3A-P005-E001"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P005'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P005::M3A-P005-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M3A-P005-E002',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O052"], "source_experiment_tracker_id": "M3A-P005-E002", "source_paper_tracker_id": "M3A-P005", "tracker_key": "M3A-P005::M3A-P005-E002"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P005'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P005::M3A-P005-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / saturated A tracker',
    'Tracker experiment M3A-P006-E001',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O006"], "source_experiment_tracker_id": "M3A-P006-E001", "source_paper_tracker_id": "M3A-P006", "tracker_key": "M3A-P006::M3A-P006-E001"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P006'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P006::M3A-P006-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M3A-P006-E002',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O053"], "source_experiment_tracker_id": "M3A-P006-E002", "source_paper_tracker_id": "M3A-P006", "tracker_key": "M3A-P006::M3A-P006-E002"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P006'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P006::M3A-P006-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / saturated A tracker',
    'Tracker experiment M3A-P007-E001',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O007"], "source_experiment_tracker_id": "M3A-P007-E001", "source_paper_tracker_id": "M3A-P007", "tracker_key": "M3A-P007::M3A-P007-E001"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P007'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P007::M3A-P007-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M3A-P007-E002',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O054"], "source_experiment_tracker_id": "M3A-P007-E002", "source_paper_tracker_id": "M3A-P007", "tracker_key": "M3A-P007::M3A-P007-E002"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P007'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P007::M3A-P007-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / saturated A tracker',
    'Tracker experiment M3A-P008-E001',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O008"], "source_experiment_tracker_id": "M3A-P008-E001", "source_paper_tracker_id": "M3A-P008", "tracker_key": "M3A-P008::M3A-P008-E001"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P008'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P008::M3A-P008-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M3A-P008-E002',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O055"], "source_experiment_tracker_id": "M3A-P008-E002", "source_paper_tracker_id": "M3A-P008", "tracker_key": "M3A-P008::M3A-P008-E002"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P008'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P008::M3A-P008-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / saturated A tracker',
    'Tracker experiment M3A-P009-E001',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O009"], "source_experiment_tracker_id": "M3A-P009-E001", "source_paper_tracker_id": "M3A-P009", "tracker_key": "M3A-P009::M3A-P009-E001"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P009'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P009::M3A-P009-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M3A-P009-E002',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O056"], "source_experiment_tracker_id": "M3A-P009-E002", "source_paper_tracker_id": "M3A-P009", "tracker_key": "M3A-P009::M3A-P009-E002"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P009'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P009::M3A-P009-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / saturated A tracker',
    'Tracker experiment M3A-P010-E001',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O010"], "source_experiment_tracker_id": "M3A-P010-E001", "source_paper_tracker_id": "M3A-P010", "tracker_key": "M3A-P010::M3A-P010-E001"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P010'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P010::M3A-P010-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M3A-P010-E002',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O057"], "source_experiment_tracker_id": "M3A-P010-E002", "source_paper_tracker_id": "M3A-P010", "tracker_key": "M3A-P010::M3A-P010-E002"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P010'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P010::M3A-P010-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / saturated A tracker',
    'Tracker experiment M3A-P011-E001',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O011"], "source_experiment_tracker_id": "M3A-P011-E001", "source_paper_tracker_id": "M3A-P011", "tracker_key": "M3A-P011::M3A-P011-E001"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P011'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P011::M3A-P011-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M3A-P011-E002',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O058"], "source_experiment_tracker_id": "M3A-P011-E002", "source_paper_tracker_id": "M3A-P011", "tracker_key": "M3A-P011::M3A-P011-E002"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P011'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P011::M3A-P011-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / saturated A tracker',
    'Tracker experiment M3A-P012-E001',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O012"], "source_experiment_tracker_id": "M3A-P012-E001", "source_paper_tracker_id": "M3A-P012", "tracker_key": "M3A-P012::M3A-P012-E001"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P012'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P012::M3A-P012-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M3A-P012-E002',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O059"], "source_experiment_tracker_id": "M3A-P012-E002", "source_paper_tracker_id": "M3A-P012", "tracker_key": "M3A-P012::M3A-P012-E002"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P012'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P012::M3A-P012-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / saturated A tracker',
    'Tracker experiment M3A-P013-E001',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O013"], "source_experiment_tracker_id": "M3A-P013-E001", "source_paper_tracker_id": "M3A-P013", "tracker_key": "M3A-P013::M3A-P013-E001"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P013'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P013::M3A-P013-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M3A-P013-E002',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O060"], "source_experiment_tracker_id": "M3A-P013-E002", "source_paper_tracker_id": "M3A-P013", "tracker_key": "M3A-P013::M3A-P013-E002"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P013'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P013::M3A-P013-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / saturated A tracker',
    'Tracker experiment M3A-P014-E001',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O014"], "source_experiment_tracker_id": "M3A-P014-E001", "source_paper_tracker_id": "M3A-P014", "tracker_key": "M3A-P014::M3A-P014-E001"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P014'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P014::M3A-P014-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M3A-P014-E002',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O061"], "source_experiment_tracker_id": "M3A-P014-E002", "source_paper_tracker_id": "M3A-P014", "tracker_key": "M3A-P014::M3A-P014-E002"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P014'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P014::M3A-P014-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / saturated A tracker',
    'Tracker experiment M3A-P015-E001',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O015"], "source_experiment_tracker_id": "M3A-P015-E001", "source_paper_tracker_id": "M3A-P015", "tracker_key": "M3A-P015::M3A-P015-E001"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P015'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P015::M3A-P015-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M3A-P015-E002',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O062"], "source_experiment_tracker_id": "M3A-P015-E002", "source_paper_tracker_id": "M3A-P015", "tracker_key": "M3A-P015::M3A-P015-E002"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P015'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P015::M3A-P015-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / saturated A tracker',
    'Tracker experiment M3A-P016-E001',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O016"], "source_experiment_tracker_id": "M3A-P016-E001", "source_paper_tracker_id": "M3A-P016", "tracker_key": "M3A-P016::M3A-P016-E001"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P016'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P016::M3A-P016-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M3A-P016-E002',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O063"], "source_experiment_tracker_id": "M3A-P016-E002", "source_paper_tracker_id": "M3A-P016", "tracker_key": "M3A-P016::M3A-P016-E002"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P016'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P016::M3A-P016-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / saturated A tracker',
    'Tracker experiment M3A-P017-E001',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O017"], "source_experiment_tracker_id": "M3A-P017-E001", "source_paper_tracker_id": "M3A-P017", "tracker_key": "M3A-P017::M3A-P017-E001"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P017'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P017::M3A-P017-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M3A-P017-E002',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O064"], "source_experiment_tracker_id": "M3A-P017-E002", "source_paper_tracker_id": "M3A-P017", "tracker_key": "M3A-P017::M3A-P017-E002"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P017'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P017::M3A-P017-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / saturated A tracker',
    'Tracker experiment M3A-P018-E001',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O018"], "source_experiment_tracker_id": "M3A-P018-E001", "source_paper_tracker_id": "M3A-P018", "tracker_key": "M3A-P018::M3A-P018-E001"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P018'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P018::M3A-P018-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M3A-P018-E002',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O065"], "source_experiment_tracker_id": "M3A-P018-E002", "source_paper_tracker_id": "M3A-P018", "tracker_key": "M3A-P018::M3A-P018-E002"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P018'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P018::M3A-P018-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / saturated A tracker',
    'Tracker experiment M3A-P019-E001',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O019"], "source_experiment_tracker_id": "M3A-P019-E001", "source_paper_tracker_id": "M3A-P019", "tracker_key": "M3A-P019::M3A-P019-E001"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P019'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P019::M3A-P019-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M3A-P019-E002',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O066"], "source_experiment_tracker_id": "M3A-P019-E002", "source_paper_tracker_id": "M3A-P019", "tracker_key": "M3A-P019::M3A-P019-E002"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P019'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P019::M3A-P019-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / saturated A tracker',
    'Tracker experiment M3A-P020-E001',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O020"], "source_experiment_tracker_id": "M3A-P020-E001", "source_paper_tracker_id": "M3A-P020", "tracker_key": "M3A-P020::M3A-P020-E001"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P020'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P020::M3A-P020-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M3A-P020-E002',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O067"], "source_experiment_tracker_id": "M3A-P020-E002", "source_paper_tracker_id": "M3A-P020", "tracker_key": "M3A-P020::M3A-P020-E002"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P020'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P020::M3A-P020-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / saturated A tracker',
    'Tracker experiment M3A-P021-E001',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O021"], "source_experiment_tracker_id": "M3A-P021-E001", "source_paper_tracker_id": "M3A-P021", "tracker_key": "M3A-P021::M3A-P021-E001"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P021'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P021::M3A-P021-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M3A-P021-E002',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O068"], "source_experiment_tracker_id": "M3A-P021-E002", "source_paper_tracker_id": "M3A-P021", "tracker_key": "M3A-P021::M3A-P021-E002"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P021'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P021::M3A-P021-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Full text / PMC12767085',
    'Tracker experiment M3A-P022-E001',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O022"], "source_experiment_tracker_id": "M3A-P022-E001", "source_paper_tracker_id": "M3A-P022", "tracker_key": "M3A-P022::M3A-P022-E001"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P022'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P022::M3A-P022-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M3A-P022-E002',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O069"], "source_experiment_tracker_id": "M3A-P022-E002", "source_paper_tracker_id": "M3A-P022", "tracker_key": "M3A-P022::M3A-P022-E002"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P022'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P022::M3A-P022-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / saturated A tracker',
    'Tracker experiment M3A-P023-E001',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O023"], "source_experiment_tracker_id": "M3A-P023-E001", "source_paper_tracker_id": "M3A-P023", "tracker_key": "M3A-P023::M3A-P023-E001"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P023'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P023::M3A-P023-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M3A-P023-E002',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O070"], "source_experiment_tracker_id": "M3A-P023-E002", "source_paper_tracker_id": "M3A-P023", "tracker_key": "M3A-P023::M3A-P023-E002"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P023'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P023::M3A-P023-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / saturated A tracker',
    'Tracker experiment M3A-P024-E001',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O024"], "source_experiment_tracker_id": "M3A-P024-E001", "source_paper_tracker_id": "M3A-P024", "tracker_key": "M3A-P024::M3A-P024-E001"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P024'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P024::M3A-P024-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M3A-P024-E002',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O071"], "source_experiment_tracker_id": "M3A-P024-E002", "source_paper_tracker_id": "M3A-P024", "tracker_key": "M3A-P024::M3A-P024-E002"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P024'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P024::M3A-P024-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Full text / PMC12884443',
    'Tracker experiment M3A-P025-E001',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O025"], "source_experiment_tracker_id": "M3A-P025-E001", "source_paper_tracker_id": "M3A-P025", "tracker_key": "M3A-P025::M3A-P025-E001"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P025'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P025::M3A-P025-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M3A-P025-E002',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O072"], "source_experiment_tracker_id": "M3A-P025-E002", "source_paper_tracker_id": "M3A-P025", "tracker_key": "M3A-P025::M3A-P025-E002"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P025'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P025::M3A-P025-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Full text / PMC13010529',
    'Tracker experiment M3A-P026-E001',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O026"], "source_experiment_tracker_id": "M3A-P026-E001", "source_paper_tracker_id": "M3A-P026", "tracker_key": "M3A-P026::M3A-P026-E001"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P026'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P026::M3A-P026-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M3A-P026-E002',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O073"], "source_experiment_tracker_id": "M3A-P026-E002", "source_paper_tracker_id": "M3A-P026", "tracker_key": "M3A-P026::M3A-P026-E002"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P026'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P026::M3A-P026-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Full text / PMC13199823',
    'Tracker experiment M3A-P027-E001',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O027"], "source_experiment_tracker_id": "M3A-P027-E001", "source_paper_tracker_id": "M3A-P027", "tracker_key": "M3A-P027::M3A-P027-E001"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P027'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P027::M3A-P027-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M3A-P027-E002',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O074"], "source_experiment_tracker_id": "M3A-P027-E002", "source_paper_tracker_id": "M3A-P027", "tracker_key": "M3A-P027::M3A-P027-E002"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P027'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P027::M3A-P027-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Full text / PMC13003968',
    'Tracker experiment M3A-P028-E001',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O028"], "source_experiment_tracker_id": "M3A-P028-E001", "source_paper_tracker_id": "M3A-P028", "tracker_key": "M3A-P028::M3A-P028-E001"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P028'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P028::M3A-P028-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M3A-P028-E002',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O075"], "source_experiment_tracker_id": "M3A-P028-E002", "source_paper_tracker_id": "M3A-P028", "tracker_key": "M3A-P028::M3A-P028-E002"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P028'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P028::M3A-P028-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / saturated A tracker',
    'Tracker experiment M3A-P029-E001',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O029"], "source_experiment_tracker_id": "M3A-P029-E001", "source_paper_tracker_id": "M3A-P029", "tracker_key": "M3A-P029::M3A-P029-E001"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P029'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P029::M3A-P029-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M3A-P029-E002',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O076"], "source_experiment_tracker_id": "M3A-P029-E002", "source_paper_tracker_id": "M3A-P029", "tracker_key": "M3A-P029::M3A-P029-E002"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P029'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P029::M3A-P029-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / saturated A tracker',
    'Tracker experiment M3A-P030-E001',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O030"], "source_experiment_tracker_id": "M3A-P030-E001", "source_paper_tracker_id": "M3A-P030", "tracker_key": "M3A-P030::M3A-P030-E001"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P030'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P030::M3A-P030-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M3A-P030-E002',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O077"], "source_experiment_tracker_id": "M3A-P030-E002", "source_paper_tracker_id": "M3A-P030", "tracker_key": "M3A-P030::M3A-P030-E002"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P030'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P030::M3A-P030-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / saturated A tracker',
    'Tracker experiment M3A-P031-E001',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O031"], "source_experiment_tracker_id": "M3A-P031-E001", "source_paper_tracker_id": "M3A-P031", "tracker_key": "M3A-P031::M3A-P031-E001"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P031'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P031::M3A-P031-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M3A-P031-E002',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O078"], "source_experiment_tracker_id": "M3A-P031-E002", "source_paper_tracker_id": "M3A-P031", "tracker_key": "M3A-P031::M3A-P031-E002"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P031'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P031::M3A-P031-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Full text / PMC13037223',
    'Tracker experiment M3A-P032-E001',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O032"], "source_experiment_tracker_id": "M3A-P032-E001", "source_paper_tracker_id": "M3A-P032", "tracker_key": "M3A-P032::M3A-P032-E001"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P032'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P032::M3A-P032-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M3A-P032-E002',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O079"], "source_experiment_tracker_id": "M3A-P032-E002", "source_paper_tracker_id": "M3A-P032", "tracker_key": "M3A-P032::M3A-P032-E002"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P032'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P032::M3A-P032-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / saturated A tracker',
    'Tracker experiment M3A-P033-E001',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O033"], "source_experiment_tracker_id": "M3A-P033-E001", "source_paper_tracker_id": "M3A-P033", "tracker_key": "M3A-P033::M3A-P033-E001"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P033'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P033::M3A-P033-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M3A-P033-E002',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O080"], "source_experiment_tracker_id": "M3A-P033-E002", "source_paper_tracker_id": "M3A-P033", "tracker_key": "M3A-P033::M3A-P033-E002"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P033'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P033::M3A-P033-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / saturated A tracker',
    'Tracker experiment M3A-P034-E001',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O034"], "source_experiment_tracker_id": "M3A-P034-E001", "source_paper_tracker_id": "M3A-P034", "tracker_key": "M3A-P034::M3A-P034-E001"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P034'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P034::M3A-P034-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M3A-P034-E002',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O081"], "source_experiment_tracker_id": "M3A-P034-E002", "source_paper_tracker_id": "M3A-P034", "tracker_key": "M3A-P034::M3A-P034-E002"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P034'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P034::M3A-P034-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Full text / PMC12964225',
    'Tracker experiment M3A-P035-E001',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O035"], "source_experiment_tracker_id": "M3A-P035-E001", "source_paper_tracker_id": "M3A-P035", "tracker_key": "M3A-P035::M3A-P035-E001"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P035'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P035::M3A-P035-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M3A-P035-E002',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O082"], "source_experiment_tracker_id": "M3A-P035-E002", "source_paper_tracker_id": "M3A-P035", "tracker_key": "M3A-P035::M3A-P035-E002"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P035'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P035::M3A-P035-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / saturated A tracker',
    'Tracker experiment M3A-P036-E001',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O036"], "source_experiment_tracker_id": "M3A-P036-E001", "source_paper_tracker_id": "M3A-P036", "tracker_key": "M3A-P036::M3A-P036-E001"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P036'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P036::M3A-P036-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M3A-P036-E002',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O083"], "source_experiment_tracker_id": "M3A-P036-E002", "source_paper_tracker_id": "M3A-P036", "tracker_key": "M3A-P036::M3A-P036-E002"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P036'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P036::M3A-P036-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / saturated A tracker',
    'Tracker experiment M3A-P037-E001',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O037"], "source_experiment_tracker_id": "M3A-P037-E001", "source_paper_tracker_id": "M3A-P037", "tracker_key": "M3A-P037::M3A-P037-E001"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P037'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P037::M3A-P037-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M3A-P037-E002',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O084"], "source_experiment_tracker_id": "M3A-P037-E002", "source_paper_tracker_id": "M3A-P037", "tracker_key": "M3A-P037::M3A-P037-E002"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P037'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P037::M3A-P037-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Full text / PMC13157101',
    'Tracker experiment M3A-P038-E001',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O038"], "source_experiment_tracker_id": "M3A-P038-E001", "source_paper_tracker_id": "M3A-P038", "tracker_key": "M3A-P038::M3A-P038-E001"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P038'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P038::M3A-P038-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M3A-P038-E002',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O085"], "source_experiment_tracker_id": "M3A-P038-E002", "source_paper_tracker_id": "M3A-P038", "tracker_key": "M3A-P038::M3A-P038-E002"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P038'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P038::M3A-P038-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / saturated A tracker',
    'Tracker experiment M3A-P039-E001',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O039"], "source_experiment_tracker_id": "M3A-P039-E001", "source_paper_tracker_id": "M3A-P039", "tracker_key": "M3A-P039::M3A-P039-E001"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P039'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P039::M3A-P039-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M3A-P039-E002',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O086"], "source_experiment_tracker_id": "M3A-P039-E002", "source_paper_tracker_id": "M3A-P039", "tracker_key": "M3A-P039::M3A-P039-E002"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P039'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P039::M3A-P039-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / saturated A tracker',
    'Tracker experiment M3A-P040-E001',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O040"], "source_experiment_tracker_id": "M3A-P040-E001", "source_paper_tracker_id": "M3A-P040", "tracker_key": "M3A-P040::M3A-P040-E001"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P040'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P040::M3A-P040-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M3A-P040-E002',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O087"], "source_experiment_tracker_id": "M3A-P040-E002", "source_paper_tracker_id": "M3A-P040", "tracker_key": "M3A-P040::M3A-P040-E002"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P040'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P040::M3A-P040-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / saturated A tracker',
    'Tracker experiment M3A-P041-E001',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O041"], "source_experiment_tracker_id": "M3A-P041-E001", "source_paper_tracker_id": "M3A-P041", "tracker_key": "M3A-P041::M3A-P041-E001"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P041'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P041::M3A-P041-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M3A-P041-E002',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O088"], "source_experiment_tracker_id": "M3A-P041-E002", "source_paper_tracker_id": "M3A-P041", "tracker_key": "M3A-P041::M3A-P041-E002"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P041'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P041::M3A-P041-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / saturated A tracker',
    'Tracker experiment M3A-P042-E001',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O042"], "source_experiment_tracker_id": "M3A-P042-E001", "source_paper_tracker_id": "M3A-P042", "tracker_key": "M3A-P042::M3A-P042-E001"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P042'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P042::M3A-P042-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M3A-P042-E002',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O089"], "source_experiment_tracker_id": "M3A-P042-E002", "source_paper_tracker_id": "M3A-P042", "tracker_key": "M3A-P042::M3A-P042-E002"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P042'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P042::M3A-P042-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / saturated A tracker',
    'Tracker experiment M3A-P043-E001',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O043"], "source_experiment_tracker_id": "M3A-P043-E001", "source_paper_tracker_id": "M3A-P043", "tracker_key": "M3A-P043::M3A-P043-E001"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P043'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P043::M3A-P043-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M3A-P043-E002',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O090"], "source_experiment_tracker_id": "M3A-P043-E002", "source_paper_tracker_id": "M3A-P043", "tracker_key": "M3A-P043::M3A-P043-E002"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P043'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P043::M3A-P043-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / saturated A tracker',
    'Tracker experiment M3A-P044-E001',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O044"], "source_experiment_tracker_id": "M3A-P044-E001", "source_paper_tracker_id": "M3A-P044", "tracker_key": "M3A-P044::M3A-P044-E001"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P044'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P044::M3A-P044-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M3A-P044-E002',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O091"], "source_experiment_tracker_id": "M3A-P044-E002", "source_paper_tracker_id": "M3A-P044", "tracker_key": "M3A-P044::M3A-P044-E002"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P044'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P044::M3A-P044-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Full text / PMC12988535',
    'Tracker experiment M3A-P045-E001',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O045"], "source_experiment_tracker_id": "M3A-P045-E001", "source_paper_tracker_id": "M3A-P045", "tracker_key": "M3A-P045::M3A-P045-E001"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P045'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P045::M3A-P045-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M3A-P045-E002',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O092"], "source_experiment_tracker_id": "M3A-P045-E002", "source_paper_tracker_id": "M3A-P045", "tracker_key": "M3A-P045::M3A-P045-E002"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P045'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P045::M3A-P045-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Full text / PMC12936232',
    'Tracker experiment M3A-P046-E001',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O046"], "source_experiment_tracker_id": "M3A-P046-E001", "source_paper_tracker_id": "M3A-P046", "tracker_key": "M3A-P046::M3A-P046-E001"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P046'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P046::M3A-P046-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M3A-P046-E002',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O093"], "source_experiment_tracker_id": "M3A-P046-E002", "source_paper_tracker_id": "M3A-P046", "tracker_key": "M3A-P046::M3A-P046-E002"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P046'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P046::M3A-P046-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / saturated A tracker',
    'Tracker experiment M3A-P047-E001',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O047"], "source_experiment_tracker_id": "M3A-P047-E001", "source_paper_tracker_id": "M3A-P047", "tracker_key": "M3A-P047::M3A-P047-E001"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P047'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P047::M3A-P047-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed-indexed metadata',
    'Tracker experiment M3A-P047-E002',
    'Module 3B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M3B-O094"], "source_experiment_tracker_id": "M3A-P047-E002", "source_paper_tracker_id": "M3A-P047", "tracker_key": "M3A-P047::M3A-P047-E002"}'
  FROM _m3_paper_map p
  JOIN _m3_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M3A-P047'
  RETURNING experiment_id
)
INSERT INTO _m3_experiment_map (tracker_id, experiment_id) SELECT 'M3A-P047::M3A-P047-E002', experiment_id FROM inserted;

INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Immune/myeloid intervention or mechanism', 'Module 3B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;

INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('HMGB1-RAGE / macrophage-microglia polarization', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Immune metabolism / lipid and debris handling', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Immune-modifying biomaterial or vesicle delivery', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Immune-modifying nanomedicine', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Lactylation / microglia-macrophage-T cell axis', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Macrophage extracellular traps', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Macrophage-fibrotic scar interaction', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Macrophage/microglia autophagy and polarization', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Macrophage/microglia polarization signaling', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Microglia/macrophage corralling', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Microglia/macrophage programmed inflammatory death', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Microglia/macrophage pyroptosis', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Neutrophil or macrophage extracellular-trap axis', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for A dual-drug sequential delivery hydrogel for programmatic microglia/macrophage polarization and function recovery in spinal cord injury.; first-pass row captures macrophage/microglia polarization signaling in rat sci model at abstract/source-title level.', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for A reparative neutrophil subpopulation accelerates spinal cord regeneration in zebrafish by controlling macrophage inflammation via Il-4.; first-pass row captures macrophage/microglia polarization signaling in zebrafish sci model at abstract/source-title level.', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for An inflammation-targeted lipid nanoparticle inhibiting ferroptosis for spinal cord injury repair.; first-pass row captures immune metabolism / lipid and debris handling in mouse sci model at abstract/source-title level.', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Atractylenolide III ameliorates spinal cord injury in rats by modulating microglial/macrophage polarization.; first-pass row captures macrophage/microglia polarization signaling in rat sci model at abstract/source-title level.', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for CSF1R Inhibition Reduces Microglia Proliferation, Promotes Tissue Preservation and Improves Motor Recovery After Spinal Cord Injury; first-pass row captures csf1r inhibition in mouse at abstract/source-title level.', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Delayed microglial depletion after spinal cord injury reduces chronic inflammation and neurodegeneration in the brain and improves neurological recovery in male mice; first-pass row captures microglial depletion / chronic inflammation in mouse at abstract/source-title level.', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Depleting non-resolving neuroinflammation in chronic spinal cord injury attenuates thermal hypersensitivity.; first-pass row captures microglial depletion / csf1r modulation in rat sci model at abstract/source-title level.', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Dual-targeting nanoparticles enhance microglial P2Y12R expression to promote neuronal mitophagy for repairing spinal cord injury.; first-pass row captures immune metabolism / lipid and debris handling in experimental sci model context at abstract/source-title level.', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Engineered CCR2 positive macrophages coordinate immunoregulation with neural regeneration and matrix remodeling after spinal cord injury.; first-pass row captures single-cell / spatial immune-state mapping in mouse sci model at abstract/source-title level.', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for FGF4 activates FGFR1 - PI3K/AKT signaling to enhance Clec10a-mediated intracellular myelin debris processing and promote spinal cord repair.; first-pass row captures microglia/macrophage programmed inflammatory death in rat sci model at abstract/source-title level.', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Farrerol confers neuroprotection in spinal cord injury by regulating macrophages/microglia polarization through the JAK2/STAT3 pathway.; first-pass row captures macrophage/microglia polarization signaling in rodent sci model context at abstract/source-title level.', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Fisetin Promotes Functional Recovery after Spinal Cord Injury by Inhibiting Microglia/Macrophage M1 Polarization and JAK2/STAT3 Signaling Pathway.; first-pass row captures macrophage/microglia polarization signaling in rodent sci model context at abstract/source-title level.', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for GDF11 alleviates spinal cord injury in rats by modulating microglia polarization through Smad2/3 and MAPK/NFkappaB signaling pathways.; first-pass row captures macrophage/microglia polarization signaling in rat sci model at abstract/source-title level.', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for GP130 Regulates Macrophage Polarization and Functional Recovery after Spinal Cord Injury in Rats: A Single-Cell RNA Sequencing Study.; first-pass row captures macrophage/microglia polarization signaling in rat sci model at abstract/source-title level.', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Histone H3K9 lactylation activates the TXNIP/NLRP3 pathway to drive macrophage inflammation after spinal cord injury.; first-pass row captures microglia/macrophage programmed inflammatory death in human / translational context at abstract/source-title level.', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for IPSC-NSCs-derived exosomal let-7b-5p improves motor function after spinal cord Injury by modulating microglial/macrophage pyroptosis; first-pass row captures microglia/macrophage pyroptosis in rodent model context at abstract/source-title level.', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Identification of repopulated microglia-associated genes in microglia depleted/repopulated mice after spinal cord injury.; first-pass row captures microglial depletion / csf1r modulation in mouse sci model at abstract/source-title level.', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Inhibiting HMGB1-RAGE axis prevents pro-inflammatory macrophages/microglia polarization and affords neuroprotection after spinal cord injury; first-pass row captures hmgb1-rage / macrophage-microglia polarization in rodent model context at abstract/source-title level.', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Integrated Multi-Omics Analysis Reveals IRF1-Driven Microglial PANoptosis via ZBP1 in Spinal Cord Injury.; first-pass row captures macrophage/microglia polarization signaling in rat sci model at abstract/source-title level.', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Integrating single-cell RNA sequencing and spatial multi-omics reveals the molecular signature of regeneration after spinal cord injury.; first-pass row captures immune metabolism / lipid and debris handling in rat sci model at abstract/source-title level.', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Lipid accumulation in foam cells drives C1q-dependent synaptic loss and impairs motor function recovery after spinal cord injury.; first-pass row captures immune metabolism / lipid and debris handling in mouse sci model at abstract/source-title level.', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Localised delivery of interleukin-13 from a PLGA microparticle embedded GelMA hydrogel improves functional and histopathological recovery in a mouse contusion spinal cord injury model.; first-pass row captures immune-modifying biomaterial or vesicle delivery in mouse sci model at abstract/source-title level.', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Macrophage Extracellular Traps Exacerbate Secondary Spinal Cord Injury by Modulating Macrophage/Microglia Polarization via LL37/P2X7R/NF-kappaB Signaling Pathway; first-pass row captures macrophage extracellular traps in rodent model context at abstract/source-title level.', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Metabolic reprogramming through histone lactylation in microglia and macrophages recruits CD8+ T lymphocytes and aggravates spinal cord injury; first-pass row captures lactylation / microglia-macrophage-t cell axis in rodent model context at abstract/source-title level.', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Microenvironment Self-Adaptive Nanomedicine Promotes Spinal Cord Repair by Suppressing Inflammation Cascade and Neural Apoptosis.; first-pass row captures immune-modifying nanomedicine in rodent sci model context at abstract/source-title level.', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Microglia and macrophages promote corralling, wound compaction and recovery after spinal cord injury via Plexin-B2; first-pass row captures microglia/macrophage corralling in mouse at abstract/source-title level.', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Midkine Overexpression Promotes Functional Recovery After Spinal Cord Injury by Enhancing Microglial Efferocytosis Via LRP-1.; first-pass row captures macrophage/microglia polarization signaling in rat sci model at abstract/source-title level.', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for N-Lactoyl-Phenylalanine modulates lipid metabolism in microglia/macrophage via the AMPK-PGC1alpha-PPARgamma pathway to promote recovery in mice with spinal cord injury.; first-pass row captures immune metabolism / lipid and debris handling in mouse sci model at abstract/source-title level.', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Nanoparticles loaded with a CSF1R antagonist selectively depletes microglial cells and modulates inflammation in spinal cord injury.; first-pass row captures microglial depletion / csf1r modulation in rat sci model at abstract/source-title level.', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Naringenin alleviates spinal cord injury by ameliorating macrophage/microglia autophagy via progranulin stabilisation.; first-pass row captures macrophage/microglia autophagy and polarization in rodent sci model context at abstract/source-title level.', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Neonatal small extracellular vesicle-loaded GelNB hydrogel reprograms the vascular-immune microenvironment for spinal cord injury repair.; first-pass row captures immune metabolism / lipid and debris handling in mouse sci model at abstract/source-title level.', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Nonresolving Neuroinflammation Regulates Axon Regeneration in Chronic Spinal Cord Injury.; first-pass row captures microglial depletion / csf1r modulation in mouse sci model at abstract/source-title level.', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Olfactory ensheathing cell transplantation targets macrophage extracellular traps and NKCC1 to alleviate pain after spinal cord injury.; first-pass row captures neutrophil or macrophage extracellular-trap axis in rat sci model at abstract/source-title level.', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Omaveloxolone promotes functional recovery of spinal cord injury by reducing inflammatory response and regulating macrophage polarization.; first-pass row captures macrophage/microglia polarization signaling in rat sci model at abstract/source-title level.', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for PLX5622 did not alter anxiety-like behaviour and showed limited microglial depletion efficacy in a spinal cord injury model in female rats.; first-pass row captures microglial depletion / csf1r modulation in mouse sci model at abstract/source-title level.', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Pharmacological Microglial Inhibition Remodels the Scar Microenvironment to Support Reticulospinal Circuit Reconstruction After Spinal Cord Injury.; first-pass row captures microglial depletion / csf1r modulation in mouse sci model at abstract/source-title level.', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Profibrotic macrophage-derived CXCL4 promotes pericyte-to-myofibroblast transition after spinal cord injury.; first-pass row captures macrophage-fibrotic scar interaction in mouse sci model at abstract/source-title level.', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for SYK-dependent lipid handling in monocyte-derived macrophages governs functional recovery after spinal cord injury.; first-pass row captures immune metabolism / lipid and debris handling in mouse sci model at abstract/source-title level.', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Systemic Interleukin-4 Application Promotes Functional Recovery and Reprograms Neuroinflammatory and Molecular Responses after Spinal Cord Injury in Rats.; first-pass row captures macrophage/microglia polarization signaling in human / translational context at abstract/source-title level.', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for TGF--induced fibrotic scar formation limits recovery of spinal cord injury.; first-pass row captures macrophage-fibrotic scar interaction in mouse sci model at abstract/source-title level.', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for TREM2 Facilitates Myelin Debris Clearance but Exacerbates Chronic Inflammation and Fibrosis After Spinal Cord Injury.; first-pass row captures immune metabolism / lipid and debris handling in mouse sci model at abstract/source-title level.', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Targeted biohybrid nanoplatform for spinal cord injury treatment: Restoring microglial mitophagy and alleviating oxidative stress.; first-pass row captures immune metabolism / lipid and debris handling in mouse sci model at abstract/source-title level.', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Targeting microglial PANoptosis through AMPK activation: Metformin as a promising therapy for spinal cord injury.; first-pass row captures microglia/macrophage programmed inflammatory death in rat sci model at abstract/source-title level.', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Temporal regulation of macrophage polarization by abnormally innervated CGRP + Sensory nerves following spinal cord injury.; first-pass row captures macrophage/microglia polarization signaling in rat sci model at abstract/source-title level.', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Thiolutin attenuates neuroinflammation and neuronal apoptosis by suppressing microglial pyroptosis through NLRP3 inflammasome inhibition after spinal cord injury.; first-pass row captures macrophage/microglia polarization signaling in mouse sci model at abstract/source-title level.', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Trimethylamine N-Oxide Aggravates Neuro-inflammation in Spinal Cord Injury Through NLRP3 Inflammasome Activation in Microglia.; first-pass row captures microglia/macrophage programmed inflammatory death in mouse sci model at abstract/source-title level.', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcome/mechanistic validation row for Type 2 Diabetes Promotes the Microglial Pyroptosis by Activating NLRP3 Inflammasome to Impede Remyelination After Spinal Cord Injury.; first-pass row captures macrophage/microglia polarization signaling in mouse sci model at abstract/source-title level.', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('cell-state mapping / molecular signature', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('depletion / inflammatory persistence / recovery', 'Module 3B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Li Y 2020 contributes microglial depletion / chronic inflammation evidence in mouse, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Li Y 2020 contributes microglial depletion / chronic inflammation evidence in mouse, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'li y 2020 contributes microglial depletion / chronic inflammation evidence in mouse, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'Module 3A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'medium',
    '{"curator_notes": "Primary title: Delayed microglial depletion after spinal cord injury reduces chronic inflammation and neurodegeneration in the brain and improves neurological recovery in male mice. Note: Chronic inflammation and remote degeneration anchor.", "experiment_tracker_id": "M3A-P001-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M3A-P001", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M3B-T001", "tracker_id": "M3B-O001"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P001::M3A-P001-E001'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'depletion / inflammatory persistence / recovery'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O001', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Zhou X 2020 contributes microglia/macrophage corralling evidence in mouse, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Zhou X 2020 contributes microglia/macrophage corralling evidence in mouse, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'zhou x 2020 contributes microglia/macrophage corralling evidence in mouse, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'Module 3A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'medium',
    '{"curator_notes": "Primary title: Microglia and macrophages promote corralling, wound compaction and recovery after spinal cord injury via Plexin-B2. Note: Immune-glial containment anchor.", "experiment_tracker_id": "M3A-P002-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M3A-P002", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M3B-T002", "tracker_id": "M3B-O002"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P002::M3A-P002-E001'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Microglia/macrophage corralling'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O002', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Gerber YN 2018 contributes csf1r inhibition evidence in mouse, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Gerber YN 2018 contributes csf1r inhibition evidence in mouse, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'gerber yn 2018 contributes csf1r inhibition evidence in mouse, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'Module 3A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'medium',
    '{"curator_notes": "Primary title: CSF1R Inhibition Reduces Microglia Proliferation, Promotes Tissue Preservation and Improves Motor Recovery After Spinal Cord Injury. Note: Microglia/macrophage modulation anchor.", "experiment_tracker_id": "M3A-P003-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M3A-P003", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M3B-T001", "tracker_id": "M3B-O003"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P003::M3A-P003-E001'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'depletion / inflammatory persistence / recovery'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O003', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Fan H 2020 contributes hmgb1-rage / macrophage-microglia polarization evidence in rodent model context, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'qualitative',
    NULL,
    'Fan H 2020 contributes hmgb1-rage / macrophage-microglia polarization evidence in rodent model context, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'fan h 2020 contributes hmgb1-rage / macrophage-microglia polarization evidence in rodent model context, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'Module 3A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'medium',
    '{"curator_notes": "Primary title: Inhibiting HMGB1-RAGE axis prevents pro-inflammatory macrophages/microglia polarization and affords neuroprotection after spinal cord injury. Note: Mechanistic polarization anchor.", "experiment_tracker_id": "M3A-P004-E001", "measurement_method_inference": null, "paper_tracker_id": "M3A-P004", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M3B-T003", "tracker_id": "M3B-O004"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P004::M3A-P004-E001'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'HMGB1-RAGE / macrophage-microglia polarization'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O004', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Zhang C 2022 contributes macrophage extracellular traps evidence in rodent model context, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'qualitative',
    NULL,
    'Zhang C 2022 contributes macrophage extracellular traps evidence in rodent model context, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'zhang c 2022 contributes macrophage extracellular traps evidence in rodent model context, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'Module 3A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'medium',
    '{"curator_notes": "Primary title: Macrophage Extracellular Traps Exacerbate Secondary Spinal Cord Injury by Modulating Macrophage/Microglia Polarization via LL37/P2X7R/NF-kappaB Signaling Pathway. Note: Innate immune injury-amplification anchor.", "experiment_tracker_id": "M3A-P005-E001", "measurement_method_inference": null, "paper_tracker_id": "M3A-P005", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M3B-T008", "tracker_id": "M3B-O005"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P005::M3A-P005-E001'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Macrophage extracellular traps'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O005', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Liu J 2024 contributes microglia/macrophage pyroptosis evidence in rodent model context, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'qualitative',
    NULL,
    'Liu J 2024 contributes microglia/macrophage pyroptosis evidence in rodent model context, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'liu j 2024 contributes microglia/macrophage pyroptosis evidence in rodent model context, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'Module 3A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'medium',
    '{"curator_notes": "Primary title: IPSC-NSCs-derived exosomal let-7b-5p improves motor function after spinal cord Injury by modulating microglial/macrophage pyroptosis. Note: Cell/exosome immune-modulation bridge.", "experiment_tracker_id": "M3A-P006-E001", "measurement_method_inference": null, "paper_tracker_id": "M3A-P006", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M3B-T004", "tracker_id": "M3B-O006"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P006::M3A-P006-E001'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Microglia/macrophage pyroptosis'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O006', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Ge X 2025 contributes lactylation / microglia-macrophage-t cell axis evidence in rodent model context, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'qualitative',
    NULL,
    'Ge X 2025 contributes lactylation / microglia-macrophage-t cell axis evidence in rodent model context, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'ge x 2025 contributes lactylation / microglia-macrophage-t cell axis evidence in rodent model context, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'Module 3A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'medium',
    '{"curator_notes": "Primary title: Metabolic reprogramming through histone lactylation in microglia and macrophages recruits CD8+ T lymphocytes and aggravates spinal cord injury. Note: Recent immune-state mechanism.", "experiment_tracker_id": "M3A-P007-E001", "measurement_method_inference": null, "paper_tracker_id": "M3A-P007", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M3B-T008", "tracker_id": "M3B-O007"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P007::M3A-P007-E001'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Lactylation / microglia-macrophage-T cell axis'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O007', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Ying W 2025 contributes immune metabolism / lipid and debris handling evidence in mouse sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Ying W 2025 contributes immune metabolism / lipid and debris handling evidence in mouse sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'ying w 2025 contributes immune metabolism / lipid and debris handling evidence in mouse sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'Module 3A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'medium',
    '{"curator_notes": "Primary title: N-Lactoyl-Phenylalanine modulates lipid metabolism in microglia/macrophage via the AMPK-PGC1alpha-PPARgamma pathway to promote recovery in mice with spinal cord injury.. Note: N-lactoyl-phenylalanine metabolic immunomodulation anchor.", "experiment_tracker_id": "M3A-P008-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M3A-P008", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M3B-T005", "tracker_id": "M3B-O008"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P008::M3A-P008-E001'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Immune metabolism / lipid and debris handling'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O008', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Wang C 2026 contributes macrophage/microglia autophagy and polarization evidence in rodent sci model context, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'qualitative',
    NULL,
    'Wang C 2026 contributes macrophage/microglia autophagy and polarization evidence in rodent sci model context, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'wang c 2026 contributes macrophage/microglia autophagy and polarization evidence in rodent sci model context, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'Module 3A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'low',
    '{"curator_notes": "Primary title: Naringenin alleviates spinal cord injury by ameliorating macrophage/microglia autophagy via progranulin stabilisation.. Note: Natural-product autophagy/polarization anchor.", "experiment_tracker_id": "M3A-P009-E001", "measurement_method_inference": null, "paper_tracker_id": "M3A-P009", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M3B-T003", "tracker_id": "M3B-O009"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P009::M3A-P009-E001'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Macrophage/microglia autophagy and polarization'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O009', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Li Y 2025 contributes macrophage/microglia polarization signaling evidence in rat sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Li Y 2025 contributes macrophage/microglia polarization signaling evidence in rat sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'li y 2025 contributes macrophage/microglia polarization signaling evidence in rat sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'Module 3A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'medium',
    '{"curator_notes": "Primary title: A dual-drug sequential delivery hydrogel for programmatic microglia/macrophage polarization and function recovery in spinal cord injury.. Note: Macrophage/microglia polarization signaling anchor.", "experiment_tracker_id": "M3A-P010-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M3A-P010", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M3B-T003", "tracker_id": "M3B-O010"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P010::M3A-P010-E001'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Macrophage/microglia polarization signaling'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O010', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Qian D 2024 contributes immune-modifying nanomedicine evidence in rodent sci model context, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'qualitative',
    NULL,
    'Qian D 2024 contributes immune-modifying nanomedicine evidence in rodent sci model context, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'qian d 2024 contributes immune-modifying nanomedicine evidence in rodent sci model context, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'Module 3A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'medium',
    '{"curator_notes": "Primary title: Microenvironment Self-Adaptive Nanomedicine Promotes Spinal Cord Repair by Suppressing Inflammation Cascade and Neural Apoptosis.. Note: Nanomedicine inflammation-cascade anchor.", "experiment_tracker_id": "M3A-P011-E001", "measurement_method_inference": null, "paper_tracker_id": "M3A-P011", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M3B-T008", "tracker_id": "M3B-O011"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P011::M3A-P011-E001'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Immune-modifying nanomedicine'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O011', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Chen Y 2025 contributes macrophage/microglia polarization signaling evidence in rodent sci model context, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'qualitative',
    NULL,
    'Chen Y 2025 contributes macrophage/microglia polarization signaling evidence in rodent sci model context, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'chen y 2025 contributes macrophage/microglia polarization signaling evidence in rodent sci model context, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'Module 3A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'medium',
    '{"curator_notes": "Primary title: Farrerol confers neuroprotection in spinal cord injury by regulating macrophages/microglia polarization through the JAK2/STAT3 pathway.. Note: JAK2/STAT3 polarization anchor.", "experiment_tracker_id": "M3A-P012-E001", "measurement_method_inference": null, "paper_tracker_id": "M3A-P012", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M3B-T003", "tracker_id": "M3B-O012"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P012::M3A-P012-E001'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Macrophage/microglia polarization signaling'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O012', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Wang Z 2025 contributes macrophage/microglia polarization signaling evidence in rat sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'qualitative',
    NULL,
    'Wang Z 2025 contributes macrophage/microglia polarization signaling evidence in rat sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'wang z 2025 contributes macrophage/microglia polarization signaling evidence in rat sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'Module 3A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'medium',
    '{"curator_notes": "Primary title: GDF11 alleviates spinal cord injury in rats by modulating microglia polarization through Smad2/3 and MAPK/NFkappaB signaling pathways.. Note: GDF11 microglial-polarization anchor.", "experiment_tracker_id": "M3A-P013-E001", "measurement_method_inference": null, "paper_tracker_id": "M3A-P013", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M3B-T003", "tracker_id": "M3B-O013"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P013::M3A-P013-E001'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Macrophage/microglia polarization signaling'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O013', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Ji R 2024 contributes macrophage/microglia polarization signaling evidence in rodent sci model context, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Ji R 2024 contributes macrophage/microglia polarization signaling evidence in rodent sci model context, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'ji r 2024 contributes macrophage/microglia polarization signaling evidence in rodent sci model context, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'Module 3A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'medium',
    '{"curator_notes": "Primary title: Fisetin Promotes Functional Recovery after Spinal Cord Injury by Inhibiting Microglia/Macrophage M1 Polarization and JAK2/STAT3 Signaling Pathway.. Note: Fisetin polarization anchor.", "experiment_tracker_id": "M3A-P014-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M3A-P014", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M3B-T003", "tracker_id": "M3B-O014"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P014::M3A-P014-E001'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Macrophage/microglia polarization signaling'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O014', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Xue MT 2022 contributes macrophage/microglia polarization signaling evidence in rat sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'qualitative',
    NULL,
    'Xue MT 2022 contributes macrophage/microglia polarization signaling evidence in rat sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'xue mt 2022 contributes macrophage/microglia polarization signaling evidence in rat sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'Module 3A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'medium',
    '{"curator_notes": "Primary title: Atractylenolide III ameliorates spinal cord injury in rats by modulating microglial/macrophage polarization.. Note: Atractylenolide polarization anchor.", "experiment_tracker_id": "M3A-P015-E001", "measurement_method_inference": null, "paper_tracker_id": "M3A-P015", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M3B-T003", "tracker_id": "M3B-O015"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P015::M3A-P015-E001'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Macrophage/microglia polarization signaling'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O015', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Zhao Y 2026 contributes single-cell / spatial immune-state mapping evidence in mouse sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'qualitative',
    'single-cell RNA-seq / cell-state atlas; spatial transcriptomics / spatial atlas',
    'Zhao Y 2026 contributes single-cell / spatial immune-state mapping evidence in mouse sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'zhao y 2026 contributes single-cell / spatial immune-state mapping evidence in mouse sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'Module 3A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'low',
    '{"curator_notes": "Primary title: Engineered CCR2 positive macrophages coordinate immunoregulation with neural regeneration and matrix remodeling after spinal cord injury.. Note: Single-cell / spatial immune-state mapping anchor.", "experiment_tracker_id": "M3A-P016-E001", "measurement_method_inference": "single-cell RNA-seq / cell-state atlas; spatial transcriptomics / spatial atlas", "paper_tracker_id": "M3A-P016", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M3B-T006", "tracker_id": "M3B-O016"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P016::M3A-P016-E001'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'cell-state mapping / molecular signature'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O016', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Cucarian J 2026 contributes microglial depletion / csf1r modulation evidence in mouse sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Cucarian J 2026 contributes microglial depletion / csf1r modulation evidence in mouse sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'cucarian j 2026 contributes microglial depletion / csf1r modulation evidence in mouse sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'Module 3A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'low',
    '{"curator_notes": "Primary title: PLX5622 did not alter anxiety-like behaviour and showed limited microglial depletion efficacy in a spinal cord injury model in female rats.. Note: Microglial depletion / CSF1R modulation anchor.", "experiment_tracker_id": "M3A-P017-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M3A-P017", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M3B-T001", "tracker_id": "M3B-O017"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P017::M3A-P017-E001'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'depletion / inflammatory persistence / recovery'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O017', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Yang J 2025 contributes microglial depletion / csf1r modulation evidence in rat sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Yang J 2025 contributes microglial depletion / csf1r modulation evidence in rat sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'yang j 2025 contributes microglial depletion / csf1r modulation evidence in rat sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'Module 3A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'medium',
    '{"curator_notes": "Primary title: Nanoparticles loaded with a CSF1R antagonist selectively depletes microglial cells and modulates inflammation in spinal cord injury.. Note: Microglial depletion / CSF1R modulation anchor.", "experiment_tracker_id": "M3A-P018-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M3A-P018", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M3B-T001", "tracker_id": "M3B-O018"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P018::M3A-P018-E001'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'depletion / inflammatory persistence / recovery'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O018', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Xue S 2026 contributes microglial depletion / csf1r modulation evidence in mouse sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Xue S 2026 contributes microglial depletion / csf1r modulation evidence in mouse sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'xue s 2026 contributes microglial depletion / csf1r modulation evidence in mouse sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'Module 3A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'low',
    '{"curator_notes": "Primary title: Identification of repopulated microglia-associated genes in microglia depleted/repopulated mice after spinal cord injury.. Note: Microglial depletion / CSF1R modulation anchor.", "experiment_tracker_id": "M3A-P019-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M3A-P019", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M3B-T001", "tracker_id": "M3B-O019"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P019::M3A-P019-E001'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'depletion / inflammatory persistence / recovery'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O019', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Stewart AN 2025 contributes microglial depletion / csf1r modulation evidence in mouse sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Stewart AN 2025 contributes microglial depletion / csf1r modulation evidence in mouse sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'stewart an 2025 contributes microglial depletion / csf1r modulation evidence in mouse sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'Module 3A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'medium',
    '{"curator_notes": "Primary title: Nonresolving Neuroinflammation Regulates Axon Regeneration in Chronic Spinal Cord Injury.. Note: Microglial depletion / CSF1R modulation anchor.", "experiment_tracker_id": "M3A-P020-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M3A-P020", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M3B-T001", "tracker_id": "M3B-O020"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P020::M3A-P020-E001'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'depletion / inflammatory persistence / recovery'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O020', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Capes DE 2026 contributes microglial depletion / csf1r modulation evidence in rat sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Capes DE 2026 contributes microglial depletion / csf1r modulation evidence in rat sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'capes de 2026 contributes microglial depletion / csf1r modulation evidence in rat sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'Module 3A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'low',
    '{"curator_notes": "Primary title: Depleting non-resolving neuroinflammation in chronic spinal cord injury attenuates thermal hypersensitivity.. Note: Microglial depletion / CSF1R modulation anchor.", "experiment_tracker_id": "M3A-P021-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M3A-P021", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M3B-T001", "tracker_id": "M3B-O021"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P021::M3A-P021-E001'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'depletion / inflammatory persistence / recovery'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O021', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Early beta2-adrenergic receptor agonist treatment drove microglia toward a homeostatic phenotype after SCI, reduced inhibitory extracellular-matrix deposition, remodeled the scar microenvironment, and supported reticulospinal axon regrowth/circuit reconstruction.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Early beta2-adrenergic receptor agonist treatment drove microglia toward a homeostatic phenotype after SCI, reduced inhibitory extracellular-matrix deposition, remodeled the scar microenvironment, and supported reticulospinal axon regrowth/circuit reconstruction.',
    'pharmacological microglial inhibition can remodel scar environment for reticulospinal reconstruction',
    'Full text / PMC',
    'Full text / PMC12767085',
    'high',
    '{"curator_notes": "Full-text upgrade from PMID 41103249; inhibition/remodeling rather than simple depletion.", "experiment_tracker_id": "M3A-P022-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M3A-P022", "quantitative": "YES", "statistics_reported": "Full text reports microglial phenotype, ECM/scar remodeling, reticulospinal regeneration, and functional recovery endpoints", "topic_id": "M3B-T001", "tracker_id": "M3B-O022"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P022::M3A-P022-E001'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'depletion / inflammatory persistence / recovery'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O022', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Zhao Y 2026 contributes immune metabolism / lipid and debris handling evidence in mouse sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Zhao Y 2026 contributes immune metabolism / lipid and debris handling evidence in mouse sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'zhao y 2026 contributes immune metabolism / lipid and debris handling evidence in mouse sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'Module 3A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'low',
    '{"curator_notes": "Primary title: SYK-dependent lipid handling in monocyte-derived macrophages governs functional recovery after spinal cord injury.. Note: Immune metabolism / lipid and debris handling anchor.", "experiment_tracker_id": "M3A-P023-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M3A-P023", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M3B-T005", "tracker_id": "M3B-O023"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P023::M3A-P023-E001'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Immune metabolism / lipid and debris handling'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O023', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Peng Y 2025 contributes immune metabolism / lipid and debris handling evidence in mouse sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Peng Y 2025 contributes immune metabolism / lipid and debris handling evidence in mouse sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'peng y 2025 contributes immune metabolism / lipid and debris handling evidence in mouse sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'Module 3A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'medium',
    '{"curator_notes": "Primary title: Lipid accumulation in foam cells drives C1q-dependent synaptic loss and impairs motor function recovery after spinal cord injury.. Note: Immune metabolism / lipid and debris handling anchor.", "experiment_tracker_id": "M3A-P024-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M3A-P024", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M3B-T005", "tracker_id": "M3B-O024"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P024::M3A-P024-E001'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Immune metabolism / lipid and debris handling'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O024', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'In female mouse spinal cord crush injury, TREM2 deletion and COG1410 activation experiments showed that TREM2 promotes myelin-debris clearance and disease-associated microglia activation but can also exacerbate chronic inflammation and fibrosis.',
    'qualitative',
    NULL,
    'In female mouse spinal cord crush injury, TREM2 deletion and COG1410 activation experiments showed that TREM2 promotes myelin-debris clearance and disease-associated microglia activation but can also exacerbate chronic inflammation and fibrosis.',
    'TREM2 couples myelin debris clearance to chronic inflammation/fibrosis tradeoffs after SCI',
    'Full text / PMC',
    'Full text / PMC12884443',
    'high',
    '{"curator_notes": "Full-text upgrade from PMID 41660680; contradiction boundary retained.", "experiment_tracker_id": "M3A-P025-E001", "measurement_method_inference": null, "paper_tracker_id": "M3A-P025", "quantitative": "YES", "statistics_reported": "Full text reports TREM2 expression, phagocytosis, foamy macrophages, DAM activation, axon regeneration, neuronal survival, BMS, and footprint outcomes", "topic_id": "M3B-T005", "tracker_id": "M3B-O025"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P025::M3A-P025-E001'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Immune metabolism / lipid and debris handling'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O025', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'SCI-associated lactate accumulation was linked to H3K9 lactylation in lesion-infiltrating macrophages and circulating monocytes; integrated CUT&Tag/RNA-seq identified TXNIP as an H3K9la target that activates TXNIP-NLRP3 signaling and worsens inflammatory injury.',
    'qualitative',
    'bulk transcriptomics / GEO dataset',
    'SCI-associated lactate accumulation was linked to H3K9 lactylation in lesion-infiltrating macrophages and circulating monocytes; integrated CUT&Tag/RNA-seq identified TXNIP as an H3K9la target that activates TXNIP-NLRP3 signaling and worsens inflammatory injury.',
    'lactate-H3K9 lactylation drives macrophage TXNIP/NLRP3 inflammation after SCI',
    'Full text / PMC',
    'Full text / PMC13010529',
    'high',
    '{"curator_notes": "Full-text upgrade from PMID 41856077; human/translational plus mouse mechanism.", "experiment_tracker_id": "M3A-P026-E001", "measurement_method_inference": "bulk transcriptomics / GEO dataset", "paper_tracker_id": "M3A-P026", "quantitative": "YES", "statistics_reported": "Full text reports human serum lactate association, mouse SCI macrophage/monocyte H3K9la, multi-omics, and TXNIP/NLRP3 perturbation", "topic_id": "M3B-T004", "tracker_id": "M3B-O026"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P026::M3A-P026-E001'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Microglia/macrophage programmed inflammatory death'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O026', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Integrative bioinformatic and experimental analyses identified microglia as the predominant PANoptotic cell population after SCI; metformin-mediated AMPK activation suppressed microglial PANoptosis, shifted microglia toward repair-associated phenotypes, reduced inflammatory injury, and improved recovery endpoints.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Integrative bioinformatic and experimental analyses identified microglia as the predominant PANoptotic cell population after SCI; metformin-mediated AMPK activation suppressed microglial PANoptosis, shifted microglia toward repair-associated phenotypes, reduced inflammatory injury, and improved recovery endpoints.',
    'AMPK activation suppresses microglial PANoptosis after SCI',
    'Full text / PMC',
    'Full text / PMC13199823',
    'high',
    '{"curator_notes": "Full-text upgrade from PMID 42199531.", "experiment_tracker_id": "M3A-P027-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M3A-P027", "quantitative": "YES", "statistics_reported": "Full text reports bioinformatics, microglial cell-death specificity, metformin/AMPK perturbation, inflammation, tissue preservation, and functional outcomes", "topic_id": "M3B-T004", "tracker_id": "M3B-O027"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P027::M3A-P027-E001'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Microglia/macrophage programmed inflammatory death'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O027', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Integrated bulk RNA-seq and scRNA-seq analyses after SCI implicated activated microglia in PANoptosis activity and identified an IRF1-ZBP1 axis as a candidate driver of microglial pro-inflammatory cell death.',
    'qualitative',
    'single-cell RNA-seq / cell-state atlas; bulk transcriptomics / GEO dataset',
    'Integrated bulk RNA-seq and scRNA-seq analyses after SCI implicated activated microglia in PANoptosis activity and identified an IRF1-ZBP1 axis as a candidate driver of microglial pro-inflammatory cell death.',
    'multi-omics identifies IRF1-ZBP1 microglial PANoptosis after SCI',
    'Full text / PMC',
    'Full text / PMC13003968',
    'high',
    '{"curator_notes": "Reclassified from generic polarization to programmed inflammatory death based on full text.", "experiment_tracker_id": "M3A-P028-E001", "measurement_method_inference": "single-cell RNA-seq / cell-state atlas; bulk transcriptomics / GEO dataset", "paper_tracker_id": "M3A-P028", "quantitative": "YES", "statistics_reported": "Full text reports cell-type PANoptosis scoring, candidate-gene prioritization, and therapeutic-target screening", "topic_id": "M3B-T004", "tracker_id": "M3B-O028"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P028::M3A-P028-E001'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Microglia/macrophage programmed inflammatory death'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O028', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Qian S 2026 contributes microglia/macrophage programmed inflammatory death evidence in mouse sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'qualitative',
    NULL,
    'Qian S 2026 contributes microglia/macrophage programmed inflammatory death evidence in mouse sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'qian s 2026 contributes microglia/macrophage programmed inflammatory death evidence in mouse sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'Module 3A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'low',
    '{"curator_notes": "Primary title: Trimethylamine N-Oxide Aggravates Neuro-inflammation in Spinal Cord Injury Through NLRP3 Inflammasome Activation in Microglia.. Note: Microglia/macrophage programmed inflammatory death anchor.", "experiment_tracker_id": "M3A-P029-E001", "measurement_method_inference": null, "paper_tracker_id": "M3A-P029", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M3B-T004", "tracker_id": "M3B-O029"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P029::M3A-P029-E001'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Microglia/macrophage programmed inflammatory death'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O029', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Zeng Y 2026 contributes macrophage/microglia polarization signaling evidence in mouse sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'qualitative',
    NULL,
    'Zeng Y 2026 contributes macrophage/microglia polarization signaling evidence in mouse sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'zeng y 2026 contributes macrophage/microglia polarization signaling evidence in mouse sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'Module 3A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'low',
    '{"curator_notes": "Primary title: Thiolutin attenuates neuroinflammation and neuronal apoptosis by suppressing microglial pyroptosis through NLRP3 inflammasome inhibition after spinal cord injury.. Note: Macrophage/microglia polarization signaling anchor.", "experiment_tracker_id": "M3A-P030-E001", "measurement_method_inference": null, "paper_tracker_id": "M3A-P030", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M3B-T001", "tracker_id": "M3B-O030"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P030::M3A-P030-E001'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Macrophage/microglia polarization signaling'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O030', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Xu J 2026 contributes macrophage/microglia polarization signaling evidence in mouse sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'qualitative',
    NULL,
    'Xu J 2026 contributes macrophage/microglia polarization signaling evidence in mouse sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'xu j 2026 contributes macrophage/microglia polarization signaling evidence in mouse sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'Module 3A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'low',
    '{"curator_notes": "Primary title: Type 2 Diabetes Promotes the Microglial Pyroptosis by Activating NLRP3 Inflammasome to Impede Remyelination After Spinal Cord Injury.. Note: Macrophage/microglia polarization signaling anchor.", "experiment_tracker_id": "M3A-P031-E001", "measurement_method_inference": null, "paper_tracker_id": "M3A-P031", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M3B-T003", "tracker_id": "M3B-O031"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P031::M3A-P031-E001'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Macrophage/microglia polarization signaling'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O031', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'FGF4 was identified as a regulator of macrophage-mediated myelin-debris clearance; exogenous FGF4 activated FGFR1-PI3K/AKT signaling, upregulated Clec10a, enhanced intracellular myelin-debris processing, reduced neuroinflammation, and promoted spinal cord repair.',
    'qualitative',
    'pathway activity / phospho-signaling assay',
    'FGF4 was identified as a regulator of macrophage-mediated myelin-debris clearance; exogenous FGF4 activated FGFR1-PI3K/AKT signaling, upregulated Clec10a, enhanced intracellular myelin-debris processing, reduced neuroinflammation, and promoted spinal cord repair.',
    'FGF4-FGFR1-PI3K/AKT-Clec10a signaling enhances macrophage myelin-debris processing after SCI',
    'Full text / PMC',
    'Full text / PMC13037223',
    'high',
    '{"curator_notes": "Reclassified from programmed death to lipid/debris handling based on full text.", "experiment_tracker_id": "M3A-P032-E001", "measurement_method_inference": "pathway activity / phospho-signaling assay", "paper_tracker_id": "M3A-P032", "quantitative": "YES", "statistics_reported": "Full text reports in vitro debris phagocytosis, Clec10a perturbation, macrophage lipid/debris processing, inflammation, and repair endpoints", "topic_id": "M3B-T005", "tracker_id": "M3B-O032"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P032::M3A-P032-E001'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Immune metabolism / lipid and debris handling'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O032', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Gao M 2026 contributes macrophage/microglia polarization signaling evidence in rat sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'qualitative',
    'single-cell RNA-seq / cell-state atlas; behavioral / functional recovery assay',
    'Gao M 2026 contributes macrophage/microglia polarization signaling evidence in rat sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'gao m 2026 contributes macrophage/microglia polarization signaling evidence in rat sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'Module 3A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'low',
    '{"curator_notes": "Primary title: GP130 Regulates Macrophage Polarization and Functional Recovery after Spinal Cord Injury in Rats: A Single-Cell RNA Sequencing Study.. Note: Macrophage/microglia polarization signaling anchor.", "experiment_tracker_id": "M3A-P033-E001", "measurement_method_inference": "single-cell RNA-seq / cell-state atlas; behavioral / functional recovery assay", "paper_tracker_id": "M3A-P033", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M3B-T003", "tracker_id": "M3B-O033"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P033::M3A-P033-E001'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Macrophage/microglia polarization signaling'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O033', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Hu R 2026 contributes macrophage/microglia polarization signaling evidence in rat sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'qualitative',
    NULL,
    'Hu R 2026 contributes macrophage/microglia polarization signaling evidence in rat sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'hu r 2026 contributes macrophage/microglia polarization signaling evidence in rat sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'Module 3A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'low',
    '{"curator_notes": "Primary title: Temporal regulation of macrophage polarization by abnormally innervated CGRP + Sensory nerves following spinal cord injury.. Note: Macrophage/microglia polarization signaling anchor.", "experiment_tracker_id": "M3A-P034-E001", "measurement_method_inference": null, "paper_tracker_id": "M3A-P034", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M3B-T003", "tracker_id": "M3B-O034"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P034::M3A-P034-E001'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Macrophage/microglia polarization signaling'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O034', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'In a female rat T10 contusion-compression SCI model, systemic IL-4 treatment was tested as an anti-inflammatory/M2-polarizing therapy and was reported to improve functional recovery while reprogramming local and systemic neuroinflammatory molecular responses, with human SCI cytokine signatures examined for translational relevance.',
    'qualitative',
    'ELISA / cytokine protein assay; bulk transcriptomics / GEO dataset; behavioral / functional recovery assay',
    'In a female rat T10 contusion-compression SCI model, systemic IL-4 treatment was tested as an anti-inflammatory/M2-polarizing therapy and was reported to improve functional recovery while reprogramming local and systemic neuroinflammatory molecular responses, with human SCI cytokine signatures examined for translational relevance.',
    'systemic IL-4 reprograms SCI neuroinflammation and supports functional recovery',
    'Full text / PMC',
    'Full text / PMC12964225',
    'high',
    '{"curator_notes": "Full-text upgrade from PMID 41799191; translational context retained.", "experiment_tracker_id": "M3A-P035-E001", "measurement_method_inference": "ELISA / cytokine protein assay; bulk transcriptomics / GEO dataset; behavioral / functional recovery assay", "paper_tracker_id": "M3A-P035", "quantitative": "YES", "statistics_reported": "Full text reports randomized rat SCI treatment groups, systemic IL-4 dosing, behavioral recovery, macrophage/microglia polarization, transcriptomic/cytokine analyses, and human translational signature comparison", "topic_id": "M3B-T003", "tracker_id": "M3B-O035"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P035::M3A-P035-E001'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Macrophage/microglia polarization signaling'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O035', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Zhao P 2025 contributes macrophage/microglia polarization signaling evidence in rat sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Zhao P 2025 contributes macrophage/microglia polarization signaling evidence in rat sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'zhao p 2025 contributes macrophage/microglia polarization signaling evidence in rat sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'Module 3A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'medium',
    '{"curator_notes": "Primary title: Omaveloxolone promotes functional recovery of spinal cord injury by reducing inflammatory response and regulating macrophage polarization.. Note: Macrophage/microglia polarization signaling anchor.", "experiment_tracker_id": "M3A-P036-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M3A-P036", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M3B-T003", "tracker_id": "M3B-O036"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P036::M3A-P036-E001'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Macrophage/microglia polarization signaling'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O036', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Walsh CM 2025 contributes immune-modifying biomaterial or vesicle delivery evidence in mouse sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Walsh CM 2025 contributes immune-modifying biomaterial or vesicle delivery evidence in mouse sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'walsh cm 2025 contributes immune-modifying biomaterial or vesicle delivery evidence in mouse sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'Module 3A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'medium',
    '{"curator_notes": "Primary title: Localised delivery of interleukin-13 from a PLGA microparticle embedded GelMA hydrogel improves functional and histopathological recovery in a mouse contusion spinal cord injury model.. Note: Immune-modifying biomaterial or vesicle delivery anchor.", "experiment_tracker_id": "M3A-P037-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M3A-P037", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M3B-T007", "tracker_id": "M3B-O037"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P037::M3A-P037-E001'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Immune-modifying biomaterial or vesicle delivery'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O037', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Neonatal circulating blood-derived small extracellular vesicles loaded into GelNB hydrogel reprogrammed adult spinal cord microvascular endothelial lipid metabolism, reduced immune imbalance, interrupted CXCL12-CXCR4 macrophage recruitment feedback, and supported neuroaxonal regrowth after SCI.',
    'qualitative',
    'barrier / permeability / endothelial assay',
    'Neonatal circulating blood-derived small extracellular vesicles loaded into GelNB hydrogel reprogrammed adult spinal cord microvascular endothelial lipid metabolism, reduced immune imbalance, interrupted CXCL12-CXCR4 macrophage recruitment feedback, and supported neuroaxonal regrowth after SCI.',
    'neonatal vesicle GelNB hydrogel reprograms vascular-immune lipid/inflammatory SCI microenvironment',
    'Full text / PMC',
    'Full text / PMC13157101',
    'high',
    '{"curator_notes": "Full-text upgrade from PMID 42111233; biomaterial-delivery boundary retained.", "experiment_tracker_id": "M3A-P038-E001", "measurement_method_inference": "barrier / permeability / endothelial assay", "paper_tracker_id": "M3A-P038", "quantitative": "YES", "statistics_reported": "Full text reports neonatal repair comparison, SCMEC lipid metabolism, CXCL12/CXCR4 macrophage recruitment, hydrogel vesicle delivery, scarring, and neuroaxonal repair endpoints", "topic_id": "M3B-T005", "tracker_id": "M3B-O038"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P038::M3A-P038-E001'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Immune metabolism / lipid and debris handling'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O038', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Tian Z 2026 contributes immune metabolism / lipid and debris handling evidence in experimental sci model context, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'qualitative',
    NULL,
    'Tian Z 2026 contributes immune metabolism / lipid and debris handling evidence in experimental sci model context, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'tian z 2026 contributes immune metabolism / lipid and debris handling evidence in experimental sci model context, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'Module 3A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'low',
    '{"curator_notes": "Primary title: Dual-targeting nanoparticles enhance microglial P2Y12R expression to promote neuronal mitophagy for repairing spinal cord injury.. Note: Immune metabolism / lipid and debris handling anchor.", "experiment_tracker_id": "M3A-P039-E001", "measurement_method_inference": null, "paper_tracker_id": "M3A-P039", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M3B-T005", "tracker_id": "M3B-O039"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P039::M3A-P039-E001'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Immune metabolism / lipid and debris handling'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O039', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Deng Y 2026 contributes immune metabolism / lipid and debris handling evidence in mouse sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'qualitative',
    NULL,
    'Deng Y 2026 contributes immune metabolism / lipid and debris handling evidence in mouse sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'deng y 2026 contributes immune metabolism / lipid and debris handling evidence in mouse sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'Module 3A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'low',
    '{"curator_notes": "Primary title: Targeted biohybrid nanoplatform for spinal cord injury treatment: Restoring microglial mitophagy and alleviating oxidative stress.. Note: Immune metabolism / lipid and debris handling anchor.", "experiment_tracker_id": "M3A-P040-E001", "measurement_method_inference": null, "paper_tracker_id": "M3A-P040", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M3B-T005", "tracker_id": "M3B-O040"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P040::M3A-P040-E001'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Immune metabolism / lipid and debris handling'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O040', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Lv Y 2026 contributes immune metabolism / lipid and debris handling evidence in mouse sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'qualitative',
    NULL,
    'Lv Y 2026 contributes immune metabolism / lipid and debris handling evidence in mouse sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'lv y 2026 contributes immune metabolism / lipid and debris handling evidence in mouse sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'Module 3A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'low',
    '{"curator_notes": "Primary title: An inflammation-targeted lipid nanoparticle inhibiting ferroptosis for spinal cord injury repair.. Note: Immune metabolism / lipid and debris handling anchor.", "experiment_tracker_id": "M3A-P041-E001", "measurement_method_inference": null, "paper_tracker_id": "M3A-P041", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M3B-T005", "tracker_id": "M3B-O041"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P041::M3A-P041-E001'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Immune metabolism / lipid and debris handling'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O041', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Dong H 2025 contributes immune metabolism / lipid and debris handling evidence in rat sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'qualitative',
    'single-cell RNA-seq / cell-state atlas; spatial transcriptomics / spatial atlas',
    'Dong H 2025 contributes immune metabolism / lipid and debris handling evidence in rat sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'dong h 2025 contributes immune metabolism / lipid and debris handling evidence in rat sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'Module 3A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'medium',
    '{"curator_notes": "Primary title: Integrating single-cell RNA sequencing and spatial multi-omics reveals the molecular signature of regeneration after spinal cord injury.. Note: Immune metabolism / lipid and debris handling anchor.", "experiment_tracker_id": "M3A-P042-E001", "measurement_method_inference": "single-cell RNA-seq / cell-state atlas; spatial transcriptomics / spatial atlas", "paper_tracker_id": "M3A-P042", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M3B-T005", "tracker_id": "M3B-O042"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P042::M3A-P042-E001'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Immune metabolism / lipid and debris handling'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O042', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Wang Y 2026 contributes macrophage/microglia polarization signaling evidence in rat sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Wang Y 2026 contributes macrophage/microglia polarization signaling evidence in rat sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'wang y 2026 contributes macrophage/microglia polarization signaling evidence in rat sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'Module 3A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'low',
    '{"curator_notes": "Primary title: Midkine Overexpression Promotes Functional Recovery After Spinal Cord Injury by Enhancing Microglial Efferocytosis Via LRP-1.. Note: Macrophage/microglia polarization signaling anchor.", "experiment_tracker_id": "M3A-P043-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M3A-P043", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M3B-T003", "tracker_id": "M3B-O043"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P043::M3A-P043-E001'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Macrophage/microglia polarization signaling'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O043', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Tian X 2026 contributes macrophage/microglia polarization signaling evidence in zebrafish sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'qualitative',
    NULL,
    'Tian X 2026 contributes macrophage/microglia polarization signaling evidence in zebrafish sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'tian x 2026 contributes macrophage/microglia polarization signaling evidence in zebrafish sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'Module 3A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'low',
    '{"curator_notes": "Primary title: A reparative neutrophil subpopulation accelerates spinal cord regeneration in zebrafish by controlling macrophage inflammation via Il-4.. Note: Macrophage/microglia polarization signaling anchor.", "experiment_tracker_id": "M3A-P044-E001", "measurement_method_inference": null, "paper_tracker_id": "M3A-P044", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M3B-T003", "tracker_id": "M3B-O044"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P044::M3A-P044-E001'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Macrophage/microglia polarization signaling'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O044', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'scRNA-seq and perturbation experiments identified profibrotic Spp1/Fn1 macrophage-derived CXCL4 as a driver of pericyte-to-myofibroblast transition after SCI, linking macrophage signaling to fibrotic scar formation.',
    'qualitative',
    'single-cell RNA-seq / cell-state atlas',
    'scRNA-seq and perturbation experiments identified profibrotic Spp1/Fn1 macrophage-derived CXCL4 as a driver of pericyte-to-myofibroblast transition after SCI, linking macrophage signaling to fibrotic scar formation.',
    'macrophage-derived CXCL4 promotes pericyte-to-myofibroblast fibrotic scarring after SCI',
    'Full text / PMC',
    'Full text / PMC12988535',
    'high',
    '{"curator_notes": "Full-text upgrade from PMID 41836554.", "experiment_tracker_id": "M3A-P045-E001", "measurement_method_inference": "single-cell RNA-seq / cell-state atlas", "paper_tracker_id": "M3A-P045", "quantitative": "YES", "statistics_reported": "Full text reports scRNA-seq, primary pericyte/CXCL4 assays, macrophage co-culture, PMT markers, pathway perturbation, and scar/fibrosis outcomes", "topic_id": "M3B-T002", "tracker_id": "M3B-O045"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P045::M3A-P045-E001'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Macrophage-fibrotic scar interaction'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O045', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'After SCI, recruited macrophages were identified as a major source of activated TGF-beta1, which recruited mesenchymal stromal/stem cells and acted on resident pericytes to promote fibroblast differentiation and fibrotic scar formation; inhibiting fibrotic scarring improved recovery in adult mice.',
    'qualitative',
    'behavioral / functional recovery assay',
    'After SCI, recruited macrophages were identified as a major source of activated TGF-beta1, which recruited mesenchymal stromal/stem cells and acted on resident pericytes to promote fibroblast differentiation and fibrotic scar formation; inhibiting fibrotic scarring improved recovery in adult mice.',
    'macrophage-derived active TGF-beta1 promotes pericyte/MSC fibrotic scar formation after SCI',
    'Full text / PMC',
    'Full text / PMC12936232',
    'high',
    '{"curator_notes": "Full-text upgrade from PMID 41741406.", "experiment_tracker_id": "M3A-P046-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M3A-P046", "quantitative": "YES", "statistics_reported": "Full text reports active TGF-beta elevation, macrophage source, MSC/pericyte fibroblast differentiation, fibrotic scar inhibition, and recovery endpoints", "topic_id": "M3B-T002", "tracker_id": "M3B-O046"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P046::M3A-P046-E001'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Macrophage-fibrotic scar interaction'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O046', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Lei H 2026 contributes neutrophil or macrophage extracellular-trap axis evidence in rat sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'qualitative',
    NULL,
    'Lei H 2026 contributes neutrophil or macrophage extracellular-trap axis evidence in rat sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'lei h 2026 contributes neutrophil or macrophage extracellular-trap axis evidence in rat sci model, supporting the immune and myeloid modulation after sci first-pass corpus.',
    'Module 3A tracker / PubMed-indexed metadata',
    'Abstract / saturated A tracker',
    'low',
    '{"curator_notes": "Primary title: Olfactory ensheathing cell transplantation targets macrophage extracellular traps and NKCC1 to alleviate pain after spinal cord injury.. Note: Neutrophil or macrophage extracellular-trap axis anchor.", "experiment_tracker_id": "M3A-P047-E001", "measurement_method_inference": null, "paper_tracker_id": "M3A-P047", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M3B-T008", "tracker_id": "M3B-O047"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P047::M3A-P047-E001'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Neutrophil or macrophage extracellular-trap axis'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O047', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Li Y 2020 M3A-P001-E002 preserves a distinct Mouse experiment testing Mechanistic outcome assessment after microglial depletion / chronic inflammation with endpoint/readout: Outcome/mechanistic validation row for Delayed microglial depletion after spinal cord injury reduces chronic inflammation and neurodegeneration in the brain and improves neurological recovery in male mice; first-pass row captures microglial depletion / chronic inflammation in mouse at abstract/source-title level..',
    'qualitative',
    'behavioral / functional recovery assay',
    'Li Y 2020 M3A-P001-E002 preserves a distinct Mouse experiment testing Mechanistic outcome assessment after microglial depletion / chronic inflammation with endpoint/readout: Outcome/mechanistic validation row for Delayed microglial depletion after spinal cord injury reduces chronic inflammation and neurodegeneration in the brain and improves neurological recovery in male mice; first-pass row captures microglial depletion / chronic inflammation in mouse at abstract/source-title level..',
    'M3A-P001-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Delayed microglial depletion after spinal cord injury reduces chronic inflammation and neurodegeneration in the brain and improves neurological recovery in male mice. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M3A-P001-E002", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M3A-P001", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M3B-T001", "tracker_id": "M3B-O048"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P001::M3A-P001-E002'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Delayed microglial depletion after spinal cord injury reduces chronic inflammation and neurodegeneration in the brain and improves neurological recovery in male mice; first-pass row captures microglial depletion / chronic inflammation in mouse at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O048', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Zhou X 2020 M3A-P002-E002 preserves a distinct Mouse experiment testing Mechanistic outcome assessment after microglia/macrophage corralling with endpoint/readout: Outcome/mechanistic validation row for Microglia and macrophages promote corralling, wound compaction and recovery after spinal cord injury via Plexin-B2; first-pass row captures microglia/macrophage corralling in mouse at abstract/source-title level..',
    'qualitative',
    'behavioral / functional recovery assay',
    'Zhou X 2020 M3A-P002-E002 preserves a distinct Mouse experiment testing Mechanistic outcome assessment after microglia/macrophage corralling with endpoint/readout: Outcome/mechanistic validation row for Microglia and macrophages promote corralling, wound compaction and recovery after spinal cord injury via Plexin-B2; first-pass row captures microglia/macrophage corralling in mouse at abstract/source-title level..',
    'M3A-P002-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Microglia and macrophages promote corralling, wound compaction and recovery after spinal cord injury via Plexin-B2. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M3A-P002-E002", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M3A-P002", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M3B-T002", "tracker_id": "M3B-O049"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P002::M3A-P002-E002'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Microglia and macrophages promote corralling, wound compaction and recovery after spinal cord injury via Plexin-B2; first-pass row captures microglia/macrophage corralling in mouse at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O049', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Gerber YN 2018 M3A-P003-E002 preserves a distinct Mouse experiment testing Mechanistic outcome assessment after csf1r inhibition with endpoint/readout: Outcome/mechanistic validation row for CSF1R Inhibition Reduces Microglia Proliferation, Promotes Tissue Preservation and Improves Motor Recovery After Spinal Cord Injury; first-pass row captures csf1r inhibition in mouse at abstract/source-title level..',
    'qualitative',
    'behavioral / functional recovery assay',
    'Gerber YN 2018 M3A-P003-E002 preserves a distinct Mouse experiment testing Mechanistic outcome assessment after csf1r inhibition with endpoint/readout: Outcome/mechanistic validation row for CSF1R Inhibition Reduces Microglia Proliferation, Promotes Tissue Preservation and Improves Motor Recovery After Spinal Cord Injury; first-pass row captures csf1r inhibition in mouse at abstract/source-title level..',
    'M3A-P003-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: CSF1R Inhibition Reduces Microglia Proliferation, Promotes Tissue Preservation and Improves Motor Recovery After Spinal Cord Injury. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M3A-P003-E002", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M3A-P003", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M3B-T001", "tracker_id": "M3B-O050"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P003::M3A-P003-E002'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for CSF1R Inhibition Reduces Microglia Proliferation, Promotes Tissue Preservation and Improves Motor Recovery After Spinal Cord Injury; first-pass row captures csf1r inhibition in mouse at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O050', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Fan H 2020 M3A-P004-E002 preserves a distinct Rodent model context experiment testing Mechanistic outcome assessment after hmgb1-rage / macrophage-microglia polarization with endpoint/readout: Outcome/mechanistic validation row for Inhibiting HMGB1-RAGE axis prevents pro-inflammatory macrophages/microglia polarization and affords neuroprotection after spinal cord injury; first-pass row captures hmgb1-rage / macrophage-microglia polarization in rodent model context at abstract/source-title level..',
    'qualitative',
    NULL,
    'Fan H 2020 M3A-P004-E002 preserves a distinct Rodent model context experiment testing Mechanistic outcome assessment after hmgb1-rage / macrophage-microglia polarization with endpoint/readout: Outcome/mechanistic validation row for Inhibiting HMGB1-RAGE axis prevents pro-inflammatory macrophages/microglia polarization and affords neuroprotection after spinal cord injury; first-pass row captures hmgb1-rage / macrophage-microglia polarization in rodent model context at abstract/source-title level..',
    'M3A-P004-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Inhibiting HMGB1-RAGE axis prevents pro-inflammatory macrophages/microglia polarization and affords neuroprotection after spinal cord injury. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M3A-P004-E002", "measurement_method_inference": null, "paper_tracker_id": "M3A-P004", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M3B-T003", "tracker_id": "M3B-O051"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P004::M3A-P004-E002'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Inhibiting HMGB1-RAGE axis prevents pro-inflammatory macrophages/microglia polarization and affords neuroprotection after spinal cord injury; first-pass row captures hmgb1-rage / macrophage-microglia polarization in rodent model context at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O051', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Zhang C 2022 M3A-P005-E002 preserves a distinct Rodent model context experiment testing Mechanistic outcome assessment after macrophage extracellular traps with endpoint/readout: Outcome/mechanistic validation row for Macrophage Extracellular Traps Exacerbate Secondary Spinal Cord Injury by Modulating Macrophage/Microglia Polarization via LL37/P2X7R/NF-kappaB Signaling Pathway; first-pass row captures macrophage extracellular traps in rodent model context at abstract/source-title level..',
    'qualitative',
    NULL,
    'Zhang C 2022 M3A-P005-E002 preserves a distinct Rodent model context experiment testing Mechanistic outcome assessment after macrophage extracellular traps with endpoint/readout: Outcome/mechanistic validation row for Macrophage Extracellular Traps Exacerbate Secondary Spinal Cord Injury by Modulating Macrophage/Microglia Polarization via LL37/P2X7R/NF-kappaB Signaling Pathway; first-pass row captures macrophage extracellular traps in rodent model context at abstract/source-title level..',
    'M3A-P005-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Macrophage Extracellular Traps Exacerbate Secondary Spinal Cord Injury by Modulating Macrophage/Microglia Polarization via LL37/P2X7R/NF-kappaB Signaling Pathway. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M3A-P005-E002", "measurement_method_inference": null, "paper_tracker_id": "M3A-P005", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M3B-T008", "tracker_id": "M3B-O052"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P005::M3A-P005-E002'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Macrophage Extracellular Traps Exacerbate Secondary Spinal Cord Injury by Modulating Macrophage/Microglia Polarization via LL37/P2X7R/NF-kappaB Signaling Pathway; first-pass row captures macrophage extracellular traps in rodent model context at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O052', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Liu J 2024 M3A-P006-E002 preserves a distinct Rodent model context experiment testing Mechanistic outcome assessment after microglia/macrophage pyroptosis with endpoint/readout: Outcome/mechanistic validation row for IPSC-NSCs-derived exosomal let-7b-5p improves motor function after spinal cord Injury by modulating microglial/macrophage pyroptosis; first-pass row captures microglia/macrophage pyroptosis in rodent model context at abstract/source-title level..',
    'qualitative',
    NULL,
    'Liu J 2024 M3A-P006-E002 preserves a distinct Rodent model context experiment testing Mechanistic outcome assessment after microglia/macrophage pyroptosis with endpoint/readout: Outcome/mechanistic validation row for IPSC-NSCs-derived exosomal let-7b-5p improves motor function after spinal cord Injury by modulating microglial/macrophage pyroptosis; first-pass row captures microglia/macrophage pyroptosis in rodent model context at abstract/source-title level..',
    'M3A-P006-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: IPSC-NSCs-derived exosomal let-7b-5p improves motor function after spinal cord Injury by modulating microglial/macrophage pyroptosis. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M3A-P006-E002", "measurement_method_inference": null, "paper_tracker_id": "M3A-P006", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M3B-T004", "tracker_id": "M3B-O053"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P006::M3A-P006-E002'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for IPSC-NSCs-derived exosomal let-7b-5p improves motor function after spinal cord Injury by modulating microglial/macrophage pyroptosis; first-pass row captures microglia/macrophage pyroptosis in rodent model context at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O053', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Ge X 2025 M3A-P007-E002 preserves a distinct Rodent model context experiment testing Mechanistic outcome assessment after lactylation / microglia-macrophage-t cell axis with endpoint/readout: Outcome/mechanistic validation row for Metabolic reprogramming through histone lactylation in microglia and macrophages recruits CD8+ T lymphocytes and aggravates spinal cord injury; first-pass row captures lactylation / microglia-macrophage-t cell axis in rodent model context at abstract/source-title level..',
    'qualitative',
    NULL,
    'Ge X 2025 M3A-P007-E002 preserves a distinct Rodent model context experiment testing Mechanistic outcome assessment after lactylation / microglia-macrophage-t cell axis with endpoint/readout: Outcome/mechanistic validation row for Metabolic reprogramming through histone lactylation in microglia and macrophages recruits CD8+ T lymphocytes and aggravates spinal cord injury; first-pass row captures lactylation / microglia-macrophage-t cell axis in rodent model context at abstract/source-title level..',
    'M3A-P007-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Metabolic reprogramming through histone lactylation in microglia and macrophages recruits CD8+ T lymphocytes and aggravates spinal cord injury. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M3A-P007-E002", "measurement_method_inference": null, "paper_tracker_id": "M3A-P007", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M3B-T008", "tracker_id": "M3B-O054"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P007::M3A-P007-E002'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Metabolic reprogramming through histone lactylation in microglia and macrophages recruits CD8+ T lymphocytes and aggravates spinal cord injury; first-pass row captures lactylation / microglia-macrophage-t cell axis in rodent model context at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O054', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Ying W 2025 M3A-P008-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after immune metabolism / lipid and debris handling with endpoint/readout: Outcome/mechanistic validation row for N-Lactoyl-Phenylalanine modulates lipid metabolism in microglia/macrophage via the AMPK-PGC1alpha-PPARgamma pathway to promote recovery in mice with spinal cord injury.; first-pass row captures immune metabolism / lipid and debris handling in mouse sci model at abstract/source-title level..',
    'qualitative',
    'behavioral / functional recovery assay',
    'Ying W 2025 M3A-P008-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after immune metabolism / lipid and debris handling with endpoint/readout: Outcome/mechanistic validation row for N-Lactoyl-Phenylalanine modulates lipid metabolism in microglia/macrophage via the AMPK-PGC1alpha-PPARgamma pathway to promote recovery in mice with spinal cord injury.; first-pass row captures immune metabolism / lipid and debris handling in mouse sci model at abstract/source-title level..',
    'M3A-P008-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: N-Lactoyl-Phenylalanine modulates lipid metabolism in microglia/macrophage via the AMPK-PGC1alpha-PPARgamma pathway to promote recovery in mice with spinal cord injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M3A-P008-E002", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M3A-P008", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M3B-T005", "tracker_id": "M3B-O055"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P008::M3A-P008-E002'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for N-Lactoyl-Phenylalanine modulates lipid metabolism in microglia/macrophage via the AMPK-PGC1alpha-PPARgamma pathway to promote recovery in mice with spinal cord injury.; first-pass row captures immune metabolism / lipid and debris handling in mouse sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O055', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Wang C 2026 M3A-P009-E002 preserves a distinct Rodent SCI model context experiment testing Mechanistic outcome assessment after macrophage/microglia autophagy and polarization with endpoint/readout: Outcome/mechanistic validation row for Naringenin alleviates spinal cord injury by ameliorating macrophage/microglia autophagy via progranulin stabilisation.; first-pass row captures macrophage/microglia autophagy and polarization in rodent sci model context at abstract/source-title level..',
    'qualitative',
    NULL,
    'Wang C 2026 M3A-P009-E002 preserves a distinct Rodent SCI model context experiment testing Mechanistic outcome assessment after macrophage/microglia autophagy and polarization with endpoint/readout: Outcome/mechanistic validation row for Naringenin alleviates spinal cord injury by ameliorating macrophage/microglia autophagy via progranulin stabilisation.; first-pass row captures macrophage/microglia autophagy and polarization in rodent sci model context at abstract/source-title level..',
    'M3A-P009-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Naringenin alleviates spinal cord injury by ameliorating macrophage/microglia autophagy via progranulin stabilisation.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M3A-P009-E002", "measurement_method_inference": null, "paper_tracker_id": "M3A-P009", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M3B-T003", "tracker_id": "M3B-O056"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P009::M3A-P009-E002'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Naringenin alleviates spinal cord injury by ameliorating macrophage/microglia autophagy via progranulin stabilisation.; first-pass row captures macrophage/microglia autophagy and polarization in rodent sci model context at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O056', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Li Y 2025 M3A-P010-E002 preserves a distinct Rat SCI model experiment testing Mechanistic outcome assessment after macrophage/microglia polarization signaling with endpoint/readout: Outcome/mechanistic validation row for A dual-drug sequential delivery hydrogel for programmatic microglia/macrophage polarization and function recovery in spinal cord injury.; first-pass row captures macrophage/microglia polarization signaling in rat sci model at abstract/source-title level..',
    'qualitative',
    'behavioral / functional recovery assay',
    'Li Y 2025 M3A-P010-E002 preserves a distinct Rat SCI model experiment testing Mechanistic outcome assessment after macrophage/microglia polarization signaling with endpoint/readout: Outcome/mechanistic validation row for A dual-drug sequential delivery hydrogel for programmatic microglia/macrophage polarization and function recovery in spinal cord injury.; first-pass row captures macrophage/microglia polarization signaling in rat sci model at abstract/source-title level..',
    'M3A-P010-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: A dual-drug sequential delivery hydrogel for programmatic microglia/macrophage polarization and function recovery in spinal cord injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M3A-P010-E002", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M3A-P010", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M3B-T003", "tracker_id": "M3B-O057"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P010::M3A-P010-E002'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for A dual-drug sequential delivery hydrogel for programmatic microglia/macrophage polarization and function recovery in spinal cord injury.; first-pass row captures macrophage/microglia polarization signaling in rat sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O057', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Qian D 2024 M3A-P011-E002 preserves a distinct Rodent SCI model context experiment testing Mechanistic outcome assessment after immune-modifying nanomedicine with endpoint/readout: Outcome/mechanistic validation row for Microenvironment Self-Adaptive Nanomedicine Promotes Spinal Cord Repair by Suppressing Inflammation Cascade and Neural Apoptosis.; first-pass row captures immune-modifying nanomedicine in rodent sci model context at abstract/source-title level..',
    'qualitative',
    NULL,
    'Qian D 2024 M3A-P011-E002 preserves a distinct Rodent SCI model context experiment testing Mechanistic outcome assessment after immune-modifying nanomedicine with endpoint/readout: Outcome/mechanistic validation row for Microenvironment Self-Adaptive Nanomedicine Promotes Spinal Cord Repair by Suppressing Inflammation Cascade and Neural Apoptosis.; first-pass row captures immune-modifying nanomedicine in rodent sci model context at abstract/source-title level..',
    'M3A-P011-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Microenvironment Self-Adaptive Nanomedicine Promotes Spinal Cord Repair by Suppressing Inflammation Cascade and Neural Apoptosis.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M3A-P011-E002", "measurement_method_inference": null, "paper_tracker_id": "M3A-P011", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M3B-T008", "tracker_id": "M3B-O058"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P011::M3A-P011-E002'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Microenvironment Self-Adaptive Nanomedicine Promotes Spinal Cord Repair by Suppressing Inflammation Cascade and Neural Apoptosis.; first-pass row captures immune-modifying nanomedicine in rodent sci model context at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O058', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Chen Y 2025 M3A-P012-E002 preserves a distinct Rodent SCI model context experiment testing Mechanistic outcome assessment after macrophage/microglia polarization signaling with endpoint/readout: Outcome/mechanistic validation row for Farrerol confers neuroprotection in spinal cord injury by regulating macrophages/microglia polarization through the JAK2/STAT3 pathway.; first-pass row captures macrophage/microglia polarization signaling in rodent sci model context at abstract/source-title level..',
    'qualitative',
    NULL,
    'Chen Y 2025 M3A-P012-E002 preserves a distinct Rodent SCI model context experiment testing Mechanistic outcome assessment after macrophage/microglia polarization signaling with endpoint/readout: Outcome/mechanistic validation row for Farrerol confers neuroprotection in spinal cord injury by regulating macrophages/microglia polarization through the JAK2/STAT3 pathway.; first-pass row captures macrophage/microglia polarization signaling in rodent sci model context at abstract/source-title level..',
    'M3A-P012-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Farrerol confers neuroprotection in spinal cord injury by regulating macrophages/microglia polarization through the JAK2/STAT3 pathway.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M3A-P012-E002", "measurement_method_inference": null, "paper_tracker_id": "M3A-P012", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M3B-T003", "tracker_id": "M3B-O059"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P012::M3A-P012-E002'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Farrerol confers neuroprotection in spinal cord injury by regulating macrophages/microglia polarization through the JAK2/STAT3 pathway.; first-pass row captures macrophage/microglia polarization signaling in rodent sci model context at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O059', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Wang Z 2025 M3A-P013-E002 preserves a distinct Rat SCI model experiment testing Mechanistic outcome assessment after macrophage/microglia polarization signaling with endpoint/readout: Outcome/mechanistic validation row for GDF11 alleviates spinal cord injury in rats by modulating microglia polarization through Smad2/3 and MAPK/NFkappaB signaling pathways.; first-pass row captures macrophage/microglia polarization signaling in rat sci model at abstract/source-title level..',
    'qualitative',
    NULL,
    'Wang Z 2025 M3A-P013-E002 preserves a distinct Rat SCI model experiment testing Mechanistic outcome assessment after macrophage/microglia polarization signaling with endpoint/readout: Outcome/mechanistic validation row for GDF11 alleviates spinal cord injury in rats by modulating microglia polarization through Smad2/3 and MAPK/NFkappaB signaling pathways.; first-pass row captures macrophage/microglia polarization signaling in rat sci model at abstract/source-title level..',
    'M3A-P013-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: GDF11 alleviates spinal cord injury in rats by modulating microglia polarization through Smad2/3 and MAPK/NFkappaB signaling pathways.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M3A-P013-E002", "measurement_method_inference": null, "paper_tracker_id": "M3A-P013", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M3B-T003", "tracker_id": "M3B-O060"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P013::M3A-P013-E002'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for GDF11 alleviates spinal cord injury in rats by modulating microglia polarization through Smad2/3 and MAPK/NFkappaB signaling pathways.; first-pass row captures macrophage/microglia polarization signaling in rat sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O060', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Ji R 2024 M3A-P014-E002 preserves a distinct Rodent SCI model context experiment testing Mechanistic outcome assessment after macrophage/microglia polarization signaling with endpoint/readout: Outcome/mechanistic validation row for Fisetin Promotes Functional Recovery after Spinal Cord Injury by Inhibiting Microglia/Macrophage M1 Polarization and JAK2/STAT3 Signaling Pathway.; first-pass row captures macrophage/microglia polarization signaling in rodent sci model context at abstract/source-title level..',
    'qualitative',
    'behavioral / functional recovery assay',
    'Ji R 2024 M3A-P014-E002 preserves a distinct Rodent SCI model context experiment testing Mechanistic outcome assessment after macrophage/microglia polarization signaling with endpoint/readout: Outcome/mechanistic validation row for Fisetin Promotes Functional Recovery after Spinal Cord Injury by Inhibiting Microglia/Macrophage M1 Polarization and JAK2/STAT3 Signaling Pathway.; first-pass row captures macrophage/microglia polarization signaling in rodent sci model context at abstract/source-title level..',
    'M3A-P014-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Fisetin Promotes Functional Recovery after Spinal Cord Injury by Inhibiting Microglia/Macrophage M1 Polarization and JAK2/STAT3 Signaling Pathway.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M3A-P014-E002", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M3A-P014", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M3B-T003", "tracker_id": "M3B-O061"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P014::M3A-P014-E002'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Fisetin Promotes Functional Recovery after Spinal Cord Injury by Inhibiting Microglia/Macrophage M1 Polarization and JAK2/STAT3 Signaling Pathway.; first-pass row captures macrophage/microglia polarization signaling in rodent sci model context at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O061', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Xue MT 2022 M3A-P015-E002 preserves a distinct Rat SCI model experiment testing Mechanistic outcome assessment after macrophage/microglia polarization signaling with endpoint/readout: Outcome/mechanistic validation row for Atractylenolide III ameliorates spinal cord injury in rats by modulating microglial/macrophage polarization.; first-pass row captures macrophage/microglia polarization signaling in rat sci model at abstract/source-title level..',
    'qualitative',
    NULL,
    'Xue MT 2022 M3A-P015-E002 preserves a distinct Rat SCI model experiment testing Mechanistic outcome assessment after macrophage/microglia polarization signaling with endpoint/readout: Outcome/mechanistic validation row for Atractylenolide III ameliorates spinal cord injury in rats by modulating microglial/macrophage polarization.; first-pass row captures macrophage/microglia polarization signaling in rat sci model at abstract/source-title level..',
    'M3A-P015-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Atractylenolide III ameliorates spinal cord injury in rats by modulating microglial/macrophage polarization.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M3A-P015-E002", "measurement_method_inference": null, "paper_tracker_id": "M3A-P015", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M3B-T003", "tracker_id": "M3B-O062"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P015::M3A-P015-E002'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Atractylenolide III ameliorates spinal cord injury in rats by modulating microglial/macrophage polarization.; first-pass row captures macrophage/microglia polarization signaling in rat sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O062', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Zhao Y 2026 M3A-P016-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after single-cell / spatial immune-state mapping with endpoint/readout: Outcome/mechanistic validation row for Engineered CCR2 positive macrophages coordinate immunoregulation with neural regeneration and matrix remodeling after spinal cord injury.; first-pass row captures single-cell / spatial immune-state mapping in mouse sci model at abstract/source-title level..',
    'qualitative',
    'single-cell RNA-seq / cell-state atlas; spatial transcriptomics / spatial atlas',
    'Zhao Y 2026 M3A-P016-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after single-cell / spatial immune-state mapping with endpoint/readout: Outcome/mechanistic validation row for Engineered CCR2 positive macrophages coordinate immunoregulation with neural regeneration and matrix remodeling after spinal cord injury.; first-pass row captures single-cell / spatial immune-state mapping in mouse sci model at abstract/source-title level..',
    'M3A-P016-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Engineered CCR2 positive macrophages coordinate immunoregulation with neural regeneration and matrix remodeling after spinal cord injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M3A-P016-E002", "measurement_method_inference": "single-cell RNA-seq / cell-state atlas; spatial transcriptomics / spatial atlas", "paper_tracker_id": "M3A-P016", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M3B-T006", "tracker_id": "M3B-O063"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P016::M3A-P016-E002'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Engineered CCR2 positive macrophages coordinate immunoregulation with neural regeneration and matrix remodeling after spinal cord injury.; first-pass row captures single-cell / spatial immune-state mapping in mouse sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O063', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Cucarian J 2026 M3A-P017-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after microglial depletion / csf1r modulation with endpoint/readout: Outcome/mechanistic validation row for PLX5622 did not alter anxiety-like behaviour and showed limited microglial depletion efficacy in a spinal cord injury model in female rats.; first-pass row captures microglial depletion / csf1r modulation in mouse sci model at abstract/source-title level..',
    'qualitative',
    NULL,
    'Cucarian J 2026 M3A-P017-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after microglial depletion / csf1r modulation with endpoint/readout: Outcome/mechanistic validation row for PLX5622 did not alter anxiety-like behaviour and showed limited microglial depletion efficacy in a spinal cord injury model in female rats.; first-pass row captures microglial depletion / csf1r modulation in mouse sci model at abstract/source-title level..',
    'M3A-P017-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: PLX5622 did not alter anxiety-like behaviour and showed limited microglial depletion efficacy in a spinal cord injury model in female rats.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M3A-P017-E002", "measurement_method_inference": null, "paper_tracker_id": "M3A-P017", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M3B-T001", "tracker_id": "M3B-O064"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P017::M3A-P017-E002'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for PLX5622 did not alter anxiety-like behaviour and showed limited microglial depletion efficacy in a spinal cord injury model in female rats.; first-pass row captures microglial depletion / csf1r modulation in mouse sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O064', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Yang J 2025 M3A-P018-E002 preserves a distinct Rat SCI model experiment testing Mechanistic outcome assessment after microglial depletion / csf1r modulation with endpoint/readout: Outcome/mechanistic validation row for Nanoparticles loaded with a CSF1R antagonist selectively depletes microglial cells and modulates inflammation in spinal cord injury.; first-pass row captures microglial depletion / csf1r modulation in rat sci model at abstract/source-title level..',
    'qualitative',
    NULL,
    'Yang J 2025 M3A-P018-E002 preserves a distinct Rat SCI model experiment testing Mechanistic outcome assessment after microglial depletion / csf1r modulation with endpoint/readout: Outcome/mechanistic validation row for Nanoparticles loaded with a CSF1R antagonist selectively depletes microglial cells and modulates inflammation in spinal cord injury.; first-pass row captures microglial depletion / csf1r modulation in rat sci model at abstract/source-title level..',
    'M3A-P018-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Nanoparticles loaded with a CSF1R antagonist selectively depletes microglial cells and modulates inflammation in spinal cord injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M3A-P018-E002", "measurement_method_inference": null, "paper_tracker_id": "M3A-P018", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M3B-T001", "tracker_id": "M3B-O065"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P018::M3A-P018-E002'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Nanoparticles loaded with a CSF1R antagonist selectively depletes microglial cells and modulates inflammation in spinal cord injury.; first-pass row captures microglial depletion / csf1r modulation in rat sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O065', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Xue S 2026 M3A-P019-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after microglial depletion / csf1r modulation with endpoint/readout: Outcome/mechanistic validation row for Identification of repopulated microglia-associated genes in microglia depleted/repopulated mice after spinal cord injury.; first-pass row captures microglial depletion / csf1r modulation in mouse sci model at abstract/source-title level..',
    'qualitative',
    NULL,
    'Xue S 2026 M3A-P019-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after microglial depletion / csf1r modulation with endpoint/readout: Outcome/mechanistic validation row for Identification of repopulated microglia-associated genes in microglia depleted/repopulated mice after spinal cord injury.; first-pass row captures microglial depletion / csf1r modulation in mouse sci model at abstract/source-title level..',
    'M3A-P019-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Identification of repopulated microglia-associated genes in microglia depleted/repopulated mice after spinal cord injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M3A-P019-E002", "measurement_method_inference": null, "paper_tracker_id": "M3A-P019", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M3B-T001", "tracker_id": "M3B-O066"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P019::M3A-P019-E002'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Identification of repopulated microglia-associated genes in microglia depleted/repopulated mice after spinal cord injury.; first-pass row captures microglial depletion / csf1r modulation in mouse sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O066', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Stewart AN 2025 M3A-P020-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after microglial depletion / csf1r modulation with endpoint/readout: Outcome/mechanistic validation row for Nonresolving Neuroinflammation Regulates Axon Regeneration in Chronic Spinal Cord Injury.; first-pass row captures microglial depletion / csf1r modulation in mouse sci model at abstract/source-title level..',
    'qualitative',
    NULL,
    'Stewart AN 2025 M3A-P020-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after microglial depletion / csf1r modulation with endpoint/readout: Outcome/mechanistic validation row for Nonresolving Neuroinflammation Regulates Axon Regeneration in Chronic Spinal Cord Injury.; first-pass row captures microglial depletion / csf1r modulation in mouse sci model at abstract/source-title level..',
    'M3A-P020-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Nonresolving Neuroinflammation Regulates Axon Regeneration in Chronic Spinal Cord Injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M3A-P020-E002", "measurement_method_inference": null, "paper_tracker_id": "M3A-P020", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M3B-T001", "tracker_id": "M3B-O067"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P020::M3A-P020-E002'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Nonresolving Neuroinflammation Regulates Axon Regeneration in Chronic Spinal Cord Injury.; first-pass row captures microglial depletion / csf1r modulation in mouse sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O067', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Capes DE 2026 M3A-P021-E002 preserves a distinct Rat SCI model experiment testing Mechanistic outcome assessment after microglial depletion / csf1r modulation with endpoint/readout: Outcome/mechanistic validation row for Depleting non-resolving neuroinflammation in chronic spinal cord injury attenuates thermal hypersensitivity.; first-pass row captures microglial depletion / csf1r modulation in rat sci model at abstract/source-title level..',
    'qualitative',
    NULL,
    'Capes DE 2026 M3A-P021-E002 preserves a distinct Rat SCI model experiment testing Mechanistic outcome assessment after microglial depletion / csf1r modulation with endpoint/readout: Outcome/mechanistic validation row for Depleting non-resolving neuroinflammation in chronic spinal cord injury attenuates thermal hypersensitivity.; first-pass row captures microglial depletion / csf1r modulation in rat sci model at abstract/source-title level..',
    'M3A-P021-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Depleting non-resolving neuroinflammation in chronic spinal cord injury attenuates thermal hypersensitivity.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M3A-P021-E002", "measurement_method_inference": null, "paper_tracker_id": "M3A-P021", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M3B-T001", "tracker_id": "M3B-O068"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P021::M3A-P021-E002'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Depleting non-resolving neuroinflammation in chronic spinal cord injury attenuates thermal hypersensitivity.; first-pass row captures microglial depletion / csf1r modulation in rat sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O068', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Li R 2026 M3A-P022-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after microglial depletion / csf1r modulation with endpoint/readout: Outcome/mechanistic validation row for Pharmacological Microglial Inhibition Remodels the Scar Microenvironment to Support Reticulospinal Circuit Reconstruction After Spinal Cord Injury.; first-pass row captures microglial depletion / csf1r modulation in mouse sci model at abstract/source-title level..',
    'qualitative',
    NULL,
    'Li R 2026 M3A-P022-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after microglial depletion / csf1r modulation with endpoint/readout: Outcome/mechanistic validation row for Pharmacological Microglial Inhibition Remodels the Scar Microenvironment to Support Reticulospinal Circuit Reconstruction After Spinal Cord Injury.; first-pass row captures microglial depletion / csf1r modulation in mouse sci model at abstract/source-title level..',
    'M3A-P022-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Pharmacological Microglial Inhibition Remodels the Scar Microenvironment to Support Reticulospinal Circuit Reconstruction After Spinal Cord Injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M3A-P022-E002", "measurement_method_inference": null, "paper_tracker_id": "M3A-P022", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M3B-T001", "tracker_id": "M3B-O069"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P022::M3A-P022-E002'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Pharmacological Microglial Inhibition Remodels the Scar Microenvironment to Support Reticulospinal Circuit Reconstruction After Spinal Cord Injury.; first-pass row captures microglial depletion / csf1r modulation in mouse sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O069', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Zhao Y 2026 M3A-P023-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after immune metabolism / lipid and debris handling with endpoint/readout: Outcome/mechanistic validation row for SYK-dependent lipid handling in monocyte-derived macrophages governs functional recovery after spinal cord injury.; first-pass row captures immune metabolism / lipid and debris handling in mouse sci model at abstract/source-title level..',
    'qualitative',
    'behavioral / functional recovery assay',
    'Zhao Y 2026 M3A-P023-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after immune metabolism / lipid and debris handling with endpoint/readout: Outcome/mechanistic validation row for SYK-dependent lipid handling in monocyte-derived macrophages governs functional recovery after spinal cord injury.; first-pass row captures immune metabolism / lipid and debris handling in mouse sci model at abstract/source-title level..',
    'M3A-P023-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: SYK-dependent lipid handling in monocyte-derived macrophages governs functional recovery after spinal cord injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M3A-P023-E002", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M3A-P023", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M3B-T005", "tracker_id": "M3B-O070"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P023::M3A-P023-E002'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for SYK-dependent lipid handling in monocyte-derived macrophages governs functional recovery after spinal cord injury.; first-pass row captures immune metabolism / lipid and debris handling in mouse sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O070', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Peng Y 2025 M3A-P024-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after immune metabolism / lipid and debris handling with endpoint/readout: Outcome/mechanistic validation row for Lipid accumulation in foam cells drives C1q-dependent synaptic loss and impairs motor function recovery after spinal cord injury.; first-pass row captures immune metabolism / lipid and debris handling in mouse sci model at abstract/source-title level..',
    'qualitative',
    'behavioral / functional recovery assay',
    'Peng Y 2025 M3A-P024-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after immune metabolism / lipid and debris handling with endpoint/readout: Outcome/mechanistic validation row for Lipid accumulation in foam cells drives C1q-dependent synaptic loss and impairs motor function recovery after spinal cord injury.; first-pass row captures immune metabolism / lipid and debris handling in mouse sci model at abstract/source-title level..',
    'M3A-P024-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Lipid accumulation in foam cells drives C1q-dependent synaptic loss and impairs motor function recovery after spinal cord injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M3A-P024-E002", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M3A-P024", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M3B-T005", "tracker_id": "M3B-O071"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P024::M3A-P024-E002'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Lipid accumulation in foam cells drives C1q-dependent synaptic loss and impairs motor function recovery after spinal cord injury.; first-pass row captures immune metabolism / lipid and debris handling in mouse sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O071', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Wu Z 2026 M3A-P025-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after immune metabolism / lipid and debris handling with endpoint/readout: Outcome/mechanistic validation row for TREM2 Facilitates Myelin Debris Clearance but Exacerbates Chronic Inflammation and Fibrosis After Spinal Cord Injury.; first-pass row captures immune metabolism / lipid and debris handling in mouse sci model at abstract/source-title level..',
    'qualitative',
    NULL,
    'Wu Z 2026 M3A-P025-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after immune metabolism / lipid and debris handling with endpoint/readout: Outcome/mechanistic validation row for TREM2 Facilitates Myelin Debris Clearance but Exacerbates Chronic Inflammation and Fibrosis After Spinal Cord Injury.; first-pass row captures immune metabolism / lipid and debris handling in mouse sci model at abstract/source-title level..',
    'M3A-P025-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: TREM2 Facilitates Myelin Debris Clearance but Exacerbates Chronic Inflammation and Fibrosis After Spinal Cord Injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M3A-P025-E002", "measurement_method_inference": null, "paper_tracker_id": "M3A-P025", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M3B-T005", "tracker_id": "M3B-O072"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P025::M3A-P025-E002'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for TREM2 Facilitates Myelin Debris Clearance but Exacerbates Chronic Inflammation and Fibrosis After Spinal Cord Injury.; first-pass row captures immune metabolism / lipid and debris handling in mouse sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O072', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Shi C 2026 M3A-P026-E002 preserves a distinct Human / translational context experiment testing Mechanistic outcome assessment after microglia/macrophage programmed inflammatory death with endpoint/readout: Outcome/mechanistic validation row for Histone H3K9 lactylation activates the TXNIP/NLRP3 pathway to drive macrophage inflammation after spinal cord injury.; first-pass row captures microglia/macrophage programmed inflammatory death in human / translational context at abstract/source-title level..',
    'qualitative',
    NULL,
    'Shi C 2026 M3A-P026-E002 preserves a distinct Human / translational context experiment testing Mechanistic outcome assessment after microglia/macrophage programmed inflammatory death with endpoint/readout: Outcome/mechanistic validation row for Histone H3K9 lactylation activates the TXNIP/NLRP3 pathway to drive macrophage inflammation after spinal cord injury.; first-pass row captures microglia/macrophage programmed inflammatory death in human / translational context at abstract/source-title level..',
    'M3A-P026-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Histone H3K9 lactylation activates the TXNIP/NLRP3 pathway to drive macrophage inflammation after spinal cord injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M3A-P026-E002", "measurement_method_inference": null, "paper_tracker_id": "M3A-P026", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M3B-T004", "tracker_id": "M3B-O073"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P026::M3A-P026-E002'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Histone H3K9 lactylation activates the TXNIP/NLRP3 pathway to drive macrophage inflammation after spinal cord injury.; first-pass row captures microglia/macrophage programmed inflammatory death in human / translational context at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O073', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Liu S 2026 M3A-P027-E002 preserves a distinct Rat SCI model experiment testing Mechanistic outcome assessment after microglia/macrophage programmed inflammatory death with endpoint/readout: Outcome/mechanistic validation row for Targeting microglial PANoptosis through AMPK activation: Metformin as a promising therapy for spinal cord injury.; first-pass row captures microglia/macrophage programmed inflammatory death in rat sci model at abstract/source-title level..',
    'qualitative',
    NULL,
    'Liu S 2026 M3A-P027-E002 preserves a distinct Rat SCI model experiment testing Mechanistic outcome assessment after microglia/macrophage programmed inflammatory death with endpoint/readout: Outcome/mechanistic validation row for Targeting microglial PANoptosis through AMPK activation: Metformin as a promising therapy for spinal cord injury.; first-pass row captures microglia/macrophage programmed inflammatory death in rat sci model at abstract/source-title level..',
    'M3A-P027-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Targeting microglial PANoptosis through AMPK activation: Metformin as a promising therapy for spinal cord injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M3A-P027-E002", "measurement_method_inference": null, "paper_tracker_id": "M3A-P027", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M3B-T004", "tracker_id": "M3B-O074"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P027::M3A-P027-E002'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Targeting microglial PANoptosis through AMPK activation: Metformin as a promising therapy for spinal cord injury.; first-pass row captures microglia/macrophage programmed inflammatory death in rat sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O074', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Xu X 2026 M3A-P028-E002 preserves a distinct Rat SCI model experiment testing Mechanistic outcome assessment after macrophage/microglia polarization signaling with endpoint/readout: Outcome/mechanistic validation row for Integrated Multi-Omics Analysis Reveals IRF1-Driven Microglial PANoptosis via ZBP1 in Spinal Cord Injury.; first-pass row captures macrophage/microglia polarization signaling in rat sci model at abstract/source-title level..',
    'qualitative',
    NULL,
    'Xu X 2026 M3A-P028-E002 preserves a distinct Rat SCI model experiment testing Mechanistic outcome assessment after macrophage/microglia polarization signaling with endpoint/readout: Outcome/mechanistic validation row for Integrated Multi-Omics Analysis Reveals IRF1-Driven Microglial PANoptosis via ZBP1 in Spinal Cord Injury.; first-pass row captures macrophage/microglia polarization signaling in rat sci model at abstract/source-title level..',
    'M3A-P028-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Integrated Multi-Omics Analysis Reveals IRF1-Driven Microglial PANoptosis via ZBP1 in Spinal Cord Injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M3A-P028-E002", "measurement_method_inference": null, "paper_tracker_id": "M3A-P028", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M3B-T004", "tracker_id": "M3B-O075"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P028::M3A-P028-E002'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Integrated Multi-Omics Analysis Reveals IRF1-Driven Microglial PANoptosis via ZBP1 in Spinal Cord Injury.; first-pass row captures macrophage/microglia polarization signaling in rat sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O075', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Qian S 2026 M3A-P029-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after microglia/macrophage programmed inflammatory death with endpoint/readout: Outcome/mechanistic validation row for Trimethylamine N-Oxide Aggravates Neuro-inflammation in Spinal Cord Injury Through NLRP3 Inflammasome Activation in Microglia.; first-pass row captures microglia/macrophage programmed inflammatory death in mouse sci model at abstract/source-title level..',
    'qualitative',
    NULL,
    'Qian S 2026 M3A-P029-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after microglia/macrophage programmed inflammatory death with endpoint/readout: Outcome/mechanistic validation row for Trimethylamine N-Oxide Aggravates Neuro-inflammation in Spinal Cord Injury Through NLRP3 Inflammasome Activation in Microglia.; first-pass row captures microglia/macrophage programmed inflammatory death in mouse sci model at abstract/source-title level..',
    'M3A-P029-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Trimethylamine N-Oxide Aggravates Neuro-inflammation in Spinal Cord Injury Through NLRP3 Inflammasome Activation in Microglia.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M3A-P029-E002", "measurement_method_inference": null, "paper_tracker_id": "M3A-P029", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M3B-T004", "tracker_id": "M3B-O076"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P029::M3A-P029-E002'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Trimethylamine N-Oxide Aggravates Neuro-inflammation in Spinal Cord Injury Through NLRP3 Inflammasome Activation in Microglia.; first-pass row captures microglia/macrophage programmed inflammatory death in mouse sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O076', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Zeng Y 2026 M3A-P030-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after macrophage/microglia polarization signaling with endpoint/readout: Outcome/mechanistic validation row for Thiolutin attenuates neuroinflammation and neuronal apoptosis by suppressing microglial pyroptosis through NLRP3 inflammasome inhibition after spinal cord injury.; first-pass row captures macrophage/microglia polarization signaling in mouse sci model at abstract/source-title level..',
    'qualitative',
    NULL,
    'Zeng Y 2026 M3A-P030-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after macrophage/microglia polarization signaling with endpoint/readout: Outcome/mechanistic validation row for Thiolutin attenuates neuroinflammation and neuronal apoptosis by suppressing microglial pyroptosis through NLRP3 inflammasome inhibition after spinal cord injury.; first-pass row captures macrophage/microglia polarization signaling in mouse sci model at abstract/source-title level..',
    'M3A-P030-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Thiolutin attenuates neuroinflammation and neuronal apoptosis by suppressing microglial pyroptosis through NLRP3 inflammasome inhibition after spinal cord injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M3A-P030-E002", "measurement_method_inference": null, "paper_tracker_id": "M3A-P030", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M3B-T001", "tracker_id": "M3B-O077"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P030::M3A-P030-E002'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Thiolutin attenuates neuroinflammation and neuronal apoptosis by suppressing microglial pyroptosis through NLRP3 inflammasome inhibition after spinal cord injury.; first-pass row captures macrophage/microglia polarization signaling in mouse sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O077', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Xu J 2026 M3A-P031-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after macrophage/microglia polarization signaling with endpoint/readout: Outcome/mechanistic validation row for Type 2 Diabetes Promotes the Microglial Pyroptosis by Activating NLRP3 Inflammasome to Impede Remyelination After Spinal Cord Injury.; first-pass row captures macrophage/microglia polarization signaling in mouse sci model at abstract/source-title level..',
    'qualitative',
    NULL,
    'Xu J 2026 M3A-P031-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after macrophage/microglia polarization signaling with endpoint/readout: Outcome/mechanistic validation row for Type 2 Diabetes Promotes the Microglial Pyroptosis by Activating NLRP3 Inflammasome to Impede Remyelination After Spinal Cord Injury.; first-pass row captures macrophage/microglia polarization signaling in mouse sci model at abstract/source-title level..',
    'M3A-P031-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Type 2 Diabetes Promotes the Microglial Pyroptosis by Activating NLRP3 Inflammasome to Impede Remyelination After Spinal Cord Injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M3A-P031-E002", "measurement_method_inference": null, "paper_tracker_id": "M3A-P031", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M3B-T003", "tracker_id": "M3B-O078"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P031::M3A-P031-E002'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Type 2 Diabetes Promotes the Microglial Pyroptosis by Activating NLRP3 Inflammasome to Impede Remyelination After Spinal Cord Injury.; first-pass row captures macrophage/microglia polarization signaling in mouse sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O078', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Lu W 2026 M3A-P032-E002 preserves a distinct Rat SCI model experiment testing Mechanistic outcome assessment after microglia/macrophage programmed inflammatory death with endpoint/readout: Outcome/mechanistic validation row for FGF4 activates FGFR1 - PI3K/AKT signaling to enhance Clec10a-mediated intracellular myelin debris processing and promote spinal cord repair.; first-pass row captures microglia/macrophage programmed inflammatory death in rat sci model at abstract/source-title level..',
    'qualitative',
    'pathway activity / phospho-signaling assay',
    'Lu W 2026 M3A-P032-E002 preserves a distinct Rat SCI model experiment testing Mechanistic outcome assessment after microglia/macrophage programmed inflammatory death with endpoint/readout: Outcome/mechanistic validation row for FGF4 activates FGFR1 - PI3K/AKT signaling to enhance Clec10a-mediated intracellular myelin debris processing and promote spinal cord repair.; first-pass row captures microglia/macrophage programmed inflammatory death in rat sci model at abstract/source-title level..',
    'M3A-P032-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: FGF4 activates FGFR1 - PI3K/AKT signaling to enhance Clec10a-mediated intracellular myelin debris processing and promote spinal cord repair.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M3A-P032-E002", "measurement_method_inference": "pathway activity / phospho-signaling assay", "paper_tracker_id": "M3A-P032", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M3B-T005", "tracker_id": "M3B-O079"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P032::M3A-P032-E002'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for FGF4 activates FGFR1 - PI3K/AKT signaling to enhance Clec10a-mediated intracellular myelin debris processing and promote spinal cord repair.; first-pass row captures microglia/macrophage programmed inflammatory death in rat sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O079', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Gao M 2026 M3A-P033-E002 preserves a distinct Rat SCI model experiment testing Mechanistic outcome assessment after macrophage/microglia polarization signaling with endpoint/readout: Outcome/mechanistic validation row for GP130 Regulates Macrophage Polarization and Functional Recovery after Spinal Cord Injury in Rats: A Single-Cell RNA Sequencing Study.; first-pass row captures macrophage/microglia polarization signaling in rat sci model at abstract/source-title level..',
    'qualitative',
    'single-cell RNA-seq / cell-state atlas; behavioral / functional recovery assay',
    'Gao M 2026 M3A-P033-E002 preserves a distinct Rat SCI model experiment testing Mechanistic outcome assessment after macrophage/microglia polarization signaling with endpoint/readout: Outcome/mechanistic validation row for GP130 Regulates Macrophage Polarization and Functional Recovery after Spinal Cord Injury in Rats: A Single-Cell RNA Sequencing Study.; first-pass row captures macrophage/microglia polarization signaling in rat sci model at abstract/source-title level..',
    'M3A-P033-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: GP130 Regulates Macrophage Polarization and Functional Recovery after Spinal Cord Injury in Rats: A Single-Cell RNA Sequencing Study.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M3A-P033-E002", "measurement_method_inference": "single-cell RNA-seq / cell-state atlas; behavioral / functional recovery assay", "paper_tracker_id": "M3A-P033", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M3B-T003", "tracker_id": "M3B-O080"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P033::M3A-P033-E002'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for GP130 Regulates Macrophage Polarization and Functional Recovery after Spinal Cord Injury in Rats: A Single-Cell RNA Sequencing Study.; first-pass row captures macrophage/microglia polarization signaling in rat sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O080', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Hu R 2026 M3A-P034-E002 preserves a distinct Rat SCI model experiment testing Mechanistic outcome assessment after macrophage/microglia polarization signaling with endpoint/readout: Outcome/mechanistic validation row for Temporal regulation of macrophage polarization by abnormally innervated CGRP + Sensory nerves following spinal cord injury.; first-pass row captures macrophage/microglia polarization signaling in rat sci model at abstract/source-title level..',
    'qualitative',
    NULL,
    'Hu R 2026 M3A-P034-E002 preserves a distinct Rat SCI model experiment testing Mechanistic outcome assessment after macrophage/microglia polarization signaling with endpoint/readout: Outcome/mechanistic validation row for Temporal regulation of macrophage polarization by abnormally innervated CGRP + Sensory nerves following spinal cord injury.; first-pass row captures macrophage/microglia polarization signaling in rat sci model at abstract/source-title level..',
    'M3A-P034-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Temporal regulation of macrophage polarization by abnormally innervated CGRP + Sensory nerves following spinal cord injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M3A-P034-E002", "measurement_method_inference": null, "paper_tracker_id": "M3A-P034", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M3B-T003", "tracker_id": "M3B-O081"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P034::M3A-P034-E002'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Temporal regulation of macrophage polarization by abnormally innervated CGRP + Sensory nerves following spinal cord injury.; first-pass row captures macrophage/microglia polarization signaling in rat sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O081', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Alhalabi OT 2026 M3A-P035-E002 preserves a distinct Human / translational context experiment testing Mechanistic outcome assessment after macrophage/microglia polarization signaling with endpoint/readout: Outcome/mechanistic validation row for Systemic Interleukin-4 Application Promotes Functional Recovery and Reprograms Neuroinflammatory and Molecular Responses after Spinal Cord Injury in Rats.; first-pass row captures macrophage/microglia polarization signaling in human / translational context at abstract/source-title level..',
    'qualitative',
    'behavioral / functional recovery assay',
    'Alhalabi OT 2026 M3A-P035-E002 preserves a distinct Human / translational context experiment testing Mechanistic outcome assessment after macrophage/microglia polarization signaling with endpoint/readout: Outcome/mechanistic validation row for Systemic Interleukin-4 Application Promotes Functional Recovery and Reprograms Neuroinflammatory and Molecular Responses after Spinal Cord Injury in Rats.; first-pass row captures macrophage/microglia polarization signaling in human / translational context at abstract/source-title level..',
    'M3A-P035-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Systemic Interleukin-4 Application Promotes Functional Recovery and Reprograms Neuroinflammatory and Molecular Responses after Spinal Cord Injury in Rats.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M3A-P035-E002", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M3A-P035", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M3B-T003", "tracker_id": "M3B-O082"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P035::M3A-P035-E002'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Systemic Interleukin-4 Application Promotes Functional Recovery and Reprograms Neuroinflammatory and Molecular Responses after Spinal Cord Injury in Rats.; first-pass row captures macrophage/microglia polarization signaling in human / translational context at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O082', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Zhao P 2025 M3A-P036-E002 preserves a distinct Rat SCI model experiment testing Mechanistic outcome assessment after macrophage/microglia polarization signaling with endpoint/readout: Outcome/mechanistic validation row for Omaveloxolone promotes functional recovery of spinal cord injury by reducing inflammatory response and regulating macrophage polarization.; first-pass row captures macrophage/microglia polarization signaling in rat sci model at abstract/source-title level..',
    'qualitative',
    'behavioral / functional recovery assay',
    'Zhao P 2025 M3A-P036-E002 preserves a distinct Rat SCI model experiment testing Mechanistic outcome assessment after macrophage/microglia polarization signaling with endpoint/readout: Outcome/mechanistic validation row for Omaveloxolone promotes functional recovery of spinal cord injury by reducing inflammatory response and regulating macrophage polarization.; first-pass row captures macrophage/microglia polarization signaling in rat sci model at abstract/source-title level..',
    'M3A-P036-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Omaveloxolone promotes functional recovery of spinal cord injury by reducing inflammatory response and regulating macrophage polarization.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M3A-P036-E002", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M3A-P036", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M3B-T003", "tracker_id": "M3B-O083"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P036::M3A-P036-E002'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Omaveloxolone promotes functional recovery of spinal cord injury by reducing inflammatory response and regulating macrophage polarization.; first-pass row captures macrophage/microglia polarization signaling in rat sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O083', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Walsh CM 2025 M3A-P037-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after immune-modifying biomaterial or vesicle delivery with endpoint/readout: Outcome/mechanistic validation row for Localised delivery of interleukin-13 from a PLGA microparticle embedded GelMA hydrogel improves functional and histopathological recovery in a mouse contusion spinal cord injury model.; first-pass row captures immune-modifying biomaterial or vesicle delivery in mouse sci model at abstract/source-title level..',
    'qualitative',
    'behavioral / functional recovery assay',
    'Walsh CM 2025 M3A-P037-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after immune-modifying biomaterial or vesicle delivery with endpoint/readout: Outcome/mechanistic validation row for Localised delivery of interleukin-13 from a PLGA microparticle embedded GelMA hydrogel improves functional and histopathological recovery in a mouse contusion spinal cord injury model.; first-pass row captures immune-modifying biomaterial or vesicle delivery in mouse sci model at abstract/source-title level..',
    'M3A-P037-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Localised delivery of interleukin-13 from a PLGA microparticle embedded GelMA hydrogel improves functional and histopathological recovery in a mouse contusion spinal cord injury model.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M3A-P037-E002", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M3A-P037", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M3B-T007", "tracker_id": "M3B-O084"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P037::M3A-P037-E002'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Localised delivery of interleukin-13 from a PLGA microparticle embedded GelMA hydrogel improves functional and histopathological recovery in a mouse contusion spinal cord injury model.; first-pass row captures immune-modifying biomaterial or vesicle delivery in mouse sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O084', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Yuan F 2026 M3A-P038-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after immune metabolism / lipid and debris handling with endpoint/readout: Outcome/mechanistic validation row for Neonatal small extracellular vesicle-loaded GelNB hydrogel reprograms the vascular-immune microenvironment for spinal cord injury repair.; first-pass row captures immune metabolism / lipid and debris handling in mouse sci model at abstract/source-title level..',
    'qualitative',
    NULL,
    'Yuan F 2026 M3A-P038-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after immune metabolism / lipid and debris handling with endpoint/readout: Outcome/mechanistic validation row for Neonatal small extracellular vesicle-loaded GelNB hydrogel reprograms the vascular-immune microenvironment for spinal cord injury repair.; first-pass row captures immune metabolism / lipid and debris handling in mouse sci model at abstract/source-title level..',
    'M3A-P038-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Neonatal small extracellular vesicle-loaded GelNB hydrogel reprograms the vascular-immune microenvironment for spinal cord injury repair.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M3A-P038-E002", "measurement_method_inference": null, "paper_tracker_id": "M3A-P038", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M3B-T005", "tracker_id": "M3B-O085"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P038::M3A-P038-E002'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Neonatal small extracellular vesicle-loaded GelNB hydrogel reprograms the vascular-immune microenvironment for spinal cord injury repair.; first-pass row captures immune metabolism / lipid and debris handling in mouse sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O085', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Tian Z 2026 M3A-P039-E002 preserves a distinct Experimental SCI model context experiment testing Mechanistic outcome assessment after immune metabolism / lipid and debris handling with endpoint/readout: Outcome/mechanistic validation row for Dual-targeting nanoparticles enhance microglial P2Y12R expression to promote neuronal mitophagy for repairing spinal cord injury.; first-pass row captures immune metabolism / lipid and debris handling in experimental sci model context at abstract/source-title level..',
    'qualitative',
    NULL,
    'Tian Z 2026 M3A-P039-E002 preserves a distinct Experimental SCI model context experiment testing Mechanistic outcome assessment after immune metabolism / lipid and debris handling with endpoint/readout: Outcome/mechanistic validation row for Dual-targeting nanoparticles enhance microglial P2Y12R expression to promote neuronal mitophagy for repairing spinal cord injury.; first-pass row captures immune metabolism / lipid and debris handling in experimental sci model context at abstract/source-title level..',
    'M3A-P039-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Dual-targeting nanoparticles enhance microglial P2Y12R expression to promote neuronal mitophagy for repairing spinal cord injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M3A-P039-E002", "measurement_method_inference": null, "paper_tracker_id": "M3A-P039", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M3B-T005", "tracker_id": "M3B-O086"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P039::M3A-P039-E002'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Dual-targeting nanoparticles enhance microglial P2Y12R expression to promote neuronal mitophagy for repairing spinal cord injury.; first-pass row captures immune metabolism / lipid and debris handling in experimental sci model context at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O086', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Deng Y 2026 M3A-P040-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after immune metabolism / lipid and debris handling with endpoint/readout: Outcome/mechanistic validation row for Targeted biohybrid nanoplatform for spinal cord injury treatment: Restoring microglial mitophagy and alleviating oxidative stress.; first-pass row captures immune metabolism / lipid and debris handling in mouse sci model at abstract/source-title level..',
    'qualitative',
    NULL,
    'Deng Y 2026 M3A-P040-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after immune metabolism / lipid and debris handling with endpoint/readout: Outcome/mechanistic validation row for Targeted biohybrid nanoplatform for spinal cord injury treatment: Restoring microglial mitophagy and alleviating oxidative stress.; first-pass row captures immune metabolism / lipid and debris handling in mouse sci model at abstract/source-title level..',
    'M3A-P040-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Targeted biohybrid nanoplatform for spinal cord injury treatment: Restoring microglial mitophagy and alleviating oxidative stress.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M3A-P040-E002", "measurement_method_inference": null, "paper_tracker_id": "M3A-P040", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M3B-T005", "tracker_id": "M3B-O087"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P040::M3A-P040-E002'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Targeted biohybrid nanoplatform for spinal cord injury treatment: Restoring microglial mitophagy and alleviating oxidative stress.; first-pass row captures immune metabolism / lipid and debris handling in mouse sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O087', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Lv Y 2026 M3A-P041-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after immune metabolism / lipid and debris handling with endpoint/readout: Outcome/mechanistic validation row for An inflammation-targeted lipid nanoparticle inhibiting ferroptosis for spinal cord injury repair.; first-pass row captures immune metabolism / lipid and debris handling in mouse sci model at abstract/source-title level..',
    'qualitative',
    NULL,
    'Lv Y 2026 M3A-P041-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after immune metabolism / lipid and debris handling with endpoint/readout: Outcome/mechanistic validation row for An inflammation-targeted lipid nanoparticle inhibiting ferroptosis for spinal cord injury repair.; first-pass row captures immune metabolism / lipid and debris handling in mouse sci model at abstract/source-title level..',
    'M3A-P041-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: An inflammation-targeted lipid nanoparticle inhibiting ferroptosis for spinal cord injury repair.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M3A-P041-E002", "measurement_method_inference": null, "paper_tracker_id": "M3A-P041", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M3B-T005", "tracker_id": "M3B-O088"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P041::M3A-P041-E002'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for An inflammation-targeted lipid nanoparticle inhibiting ferroptosis for spinal cord injury repair.; first-pass row captures immune metabolism / lipid and debris handling in mouse sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O088', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Dong H 2025 M3A-P042-E002 preserves a distinct Rat SCI model experiment testing Mechanistic outcome assessment after immune metabolism / lipid and debris handling with endpoint/readout: Outcome/mechanistic validation row for Integrating single-cell RNA sequencing and spatial multi-omics reveals the molecular signature of regeneration after spinal cord injury.; first-pass row captures immune metabolism / lipid and debris handling in rat sci model at abstract/source-title level..',
    'qualitative',
    'single-cell RNA-seq / cell-state atlas; spatial transcriptomics / spatial atlas',
    'Dong H 2025 M3A-P042-E002 preserves a distinct Rat SCI model experiment testing Mechanistic outcome assessment after immune metabolism / lipid and debris handling with endpoint/readout: Outcome/mechanistic validation row for Integrating single-cell RNA sequencing and spatial multi-omics reveals the molecular signature of regeneration after spinal cord injury.; first-pass row captures immune metabolism / lipid and debris handling in rat sci model at abstract/source-title level..',
    'M3A-P042-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Integrating single-cell RNA sequencing and spatial multi-omics reveals the molecular signature of regeneration after spinal cord injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M3A-P042-E002", "measurement_method_inference": "single-cell RNA-seq / cell-state atlas; spatial transcriptomics / spatial atlas", "paper_tracker_id": "M3A-P042", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M3B-T005", "tracker_id": "M3B-O089"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P042::M3A-P042-E002'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Integrating single-cell RNA sequencing and spatial multi-omics reveals the molecular signature of regeneration after spinal cord injury.; first-pass row captures immune metabolism / lipid and debris handling in rat sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O089', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Wang Y 2026 M3A-P043-E002 preserves a distinct Rat SCI model experiment testing Mechanistic outcome assessment after macrophage/microglia polarization signaling with endpoint/readout: Outcome/mechanistic validation row for Midkine Overexpression Promotes Functional Recovery After Spinal Cord Injury by Enhancing Microglial Efferocytosis Via LRP-1.; first-pass row captures macrophage/microglia polarization signaling in rat sci model at abstract/source-title level..',
    'qualitative',
    'behavioral / functional recovery assay',
    'Wang Y 2026 M3A-P043-E002 preserves a distinct Rat SCI model experiment testing Mechanistic outcome assessment after macrophage/microglia polarization signaling with endpoint/readout: Outcome/mechanistic validation row for Midkine Overexpression Promotes Functional Recovery After Spinal Cord Injury by Enhancing Microglial Efferocytosis Via LRP-1.; first-pass row captures macrophage/microglia polarization signaling in rat sci model at abstract/source-title level..',
    'M3A-P043-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Midkine Overexpression Promotes Functional Recovery After Spinal Cord Injury by Enhancing Microglial Efferocytosis Via LRP-1.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M3A-P043-E002", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M3A-P043", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M3B-T003", "tracker_id": "M3B-O090"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P043::M3A-P043-E002'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Midkine Overexpression Promotes Functional Recovery After Spinal Cord Injury by Enhancing Microglial Efferocytosis Via LRP-1.; first-pass row captures macrophage/microglia polarization signaling in rat sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O090', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Tian X 2026 M3A-P044-E002 preserves a distinct Zebrafish SCI model experiment testing Mechanistic outcome assessment after macrophage/microglia polarization signaling with endpoint/readout: Outcome/mechanistic validation row for A reparative neutrophil subpopulation accelerates spinal cord regeneration in zebrafish by controlling macrophage inflammation via Il-4.; first-pass row captures macrophage/microglia polarization signaling in zebrafish sci model at abstract/source-title level..',
    'qualitative',
    NULL,
    'Tian X 2026 M3A-P044-E002 preserves a distinct Zebrafish SCI model experiment testing Mechanistic outcome assessment after macrophage/microglia polarization signaling with endpoint/readout: Outcome/mechanistic validation row for A reparative neutrophil subpopulation accelerates spinal cord regeneration in zebrafish by controlling macrophage inflammation via Il-4.; first-pass row captures macrophage/microglia polarization signaling in zebrafish sci model at abstract/source-title level..',
    'M3A-P044-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: A reparative neutrophil subpopulation accelerates spinal cord regeneration in zebrafish by controlling macrophage inflammation via Il-4.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M3A-P044-E002", "measurement_method_inference": null, "paper_tracker_id": "M3A-P044", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M3B-T003", "tracker_id": "M3B-O091"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P044::M3A-P044-E002'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for A reparative neutrophil subpopulation accelerates spinal cord regeneration in zebrafish by controlling macrophage inflammation via Il-4.; first-pass row captures macrophage/microglia polarization signaling in zebrafish sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O091', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Li G 2026 M3A-P045-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after macrophage-fibrotic scar interaction with endpoint/readout: Outcome/mechanistic validation row for Profibrotic macrophage-derived CXCL4 promotes pericyte-to-myofibroblast transition after spinal cord injury.; first-pass row captures macrophage-fibrotic scar interaction in mouse sci model at abstract/source-title level..',
    'qualitative',
    NULL,
    'Li G 2026 M3A-P045-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after macrophage-fibrotic scar interaction with endpoint/readout: Outcome/mechanistic validation row for Profibrotic macrophage-derived CXCL4 promotes pericyte-to-myofibroblast transition after spinal cord injury.; first-pass row captures macrophage-fibrotic scar interaction in mouse sci model at abstract/source-title level..',
    'M3A-P045-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Profibrotic macrophage-derived CXCL4 promotes pericyte-to-myofibroblast transition after spinal cord injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M3A-P045-E002", "measurement_method_inference": null, "paper_tracker_id": "M3A-P045", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M3B-T002", "tracker_id": "M3B-O092"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P045::M3A-P045-E002'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Profibrotic macrophage-derived CXCL4 promotes pericyte-to-myofibroblast transition after spinal cord injury.; first-pass row captures macrophage-fibrotic scar interaction in mouse sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O092', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Pan D 2026 M3A-P046-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after macrophage-fibrotic scar interaction with endpoint/readout: Outcome/mechanistic validation row for TGF--induced fibrotic scar formation limits recovery of spinal cord injury.; first-pass row captures macrophage-fibrotic scar interaction in mouse sci model at abstract/source-title level..',
    'qualitative',
    'behavioral / functional recovery assay',
    'Pan D 2026 M3A-P046-E002 preserves a distinct Mouse SCI model experiment testing Mechanistic outcome assessment after macrophage-fibrotic scar interaction with endpoint/readout: Outcome/mechanistic validation row for TGF--induced fibrotic scar formation limits recovery of spinal cord injury.; first-pass row captures macrophage-fibrotic scar interaction in mouse sci model at abstract/source-title level..',
    'M3A-P046-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: TGF--induced fibrotic scar formation limits recovery of spinal cord injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M3A-P046-E002", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M3A-P046", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M3B-T002", "tracker_id": "M3B-O093"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P046::M3A-P046-E002'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for TGF--induced fibrotic scar formation limits recovery of spinal cord injury.; first-pass row captures macrophage-fibrotic scar interaction in mouse sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O093', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, measurement_method, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Lei H 2026 M3A-P047-E002 preserves a distinct Rat SCI model experiment testing Mechanistic outcome assessment after neutrophil or macrophage extracellular-trap axis with endpoint/readout: Outcome/mechanistic validation row for Olfactory ensheathing cell transplantation targets macrophage extracellular traps and NKCC1 to alleviate pain after spinal cord injury.; first-pass row captures neutrophil or macrophage extracellular-trap axis in rat sci model at abstract/source-title level..',
    'qualitative',
    NULL,
    'Lei H 2026 M3A-P047-E002 preserves a distinct Rat SCI model experiment testing Mechanistic outcome assessment after neutrophil or macrophage extracellular-trap axis with endpoint/readout: Outcome/mechanistic validation row for Olfactory ensheathing cell transplantation targets macrophage extracellular traps and NKCC1 to alleviate pain after spinal cord injury.; first-pass row captures neutrophil or macrophage extracellular-trap axis in rat sci model at abstract/source-title level..',
    'M3A-P047-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed-indexed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Olfactory ensheathing cell transplantation targets macrophage extracellular traps and NKCC1 to alleviate pain after spinal cord injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M3A-P047-E002", "measurement_method_inference": null, "paper_tracker_id": "M3A-P047", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M3B-T008", "tracker_id": "M3B-O094"}'
  FROM _m3_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M3A-P047::M3A-P047-E002'
    AND et.evidence_type_name = 'Immune/myeloid intervention or mechanism'
    AND ot.outcome_type_name = 'Outcome/mechanistic validation row for Olfactory ensheathing cell transplantation targets macrophage extracellular traps and NKCC1 to alleviate pain after spinal cord injury.; first-pass row captures neutrophil or macrophage extracellular-trap axis in rat sci model at abstract/source-title level.'
  RETURNING observation_id
)
INSERT INTO _m3_observation_map (tracker_id, observation_id) SELECT 'M3B-O094', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Microglial depletion and CSF1R inhibition can reduce damaging inflammation in selected contexts but efficacy is timing-, sex-, and model-sensitive.',
    'boundary condition',
    'high',
    'Module 3A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M3A-P001, P003, P013-P017", "topic_id": "M3B-T001", "tracker_id": "M3B-C001"}'
  FROM _m3_paper_map p
  WHERE p.tracker_id = 'M3A-P001'
  RETURNING claim_id
)
INSERT INTO _m3_claim_map (tracker_id, claim_id) SELECT 'M3B-C001', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Negative or limited depletion studies are important boundary evidence against treating microglia removal as uniformly reparative.',
    'boundary condition',
    'high',
    'Module 3A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M3A-P014, P016", "topic_id": "M3B-T001", "tracker_id": "M3B-C002"}'
  FROM _m3_paper_map p
  WHERE p.tracker_id = 'M3A-P014'
  RETURNING claim_id
)
INSERT INTO _m3_claim_map (tracker_id, claim_id) SELECT 'M3B-C002', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Myeloid cells can organize wound containment or fibrotic scar programs, making broad suppression biologically unsafe.',
    'boundary condition',
    'high',
    'Module 3A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M3A-P002, P045-P046", "topic_id": "M3B-T002", "tracker_id": "M3B-C003"}'
  FROM _m3_paper_map p
  WHERE p.tracker_id = 'M3A-P002'
  RETURNING claim_id
)
INSERT INTO _m3_claim_map (tracker_id, claim_id) SELECT 'M3B-C003', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Monocyte-derived macrophage lipid handling and macrophage-derived fibrotic signals connect immune state to tissue remodeling after SCI.',
    'mechanistic',
    'medium',
    'Module 3A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M3A-P018-P019, P045", "topic_id": "M3B-T002", "tracker_id": "M3B-C004"}'
  FROM _m3_paper_map p
  WHERE p.tracker_id = 'M3A-P018'
  RETURNING claim_id
)
INSERT INTO _m3_claim_map (tracker_id, claim_id) SELECT 'M3B-C004', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Multiple interventions report macrophage/microglia polarization shifts with functional or neuroprotective outcomes.',
    'synthesis',
    'medium',
    'Module 3A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M3A-P004, P008-P011, P033-P036, P044", "topic_id": "M3B-T003", "tracker_id": "M3B-C005"}'
  FROM _m3_paper_map p
  WHERE p.tracker_id = 'M3A-P004'
  RETURNING claim_id
)
INSERT INTO _m3_claim_map (tracker_id, claim_id) SELECT 'M3B-C005', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Polarization claims require marker-level extraction because drug, cytokine, and sensory-nerve programs may label different states with similar language.',
    'evidence standard',
    'high',
    'Module 3A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M3A-P004-P011, P033-P036", "topic_id": "M3B-T003", "tracker_id": "M3B-C006"}'
  FROM _m3_paper_map p
  WHERE p.tracker_id = 'M3A-P004'
  RETURNING claim_id
)
INSERT INTO _m3_claim_map (tracker_id, claim_id) SELECT 'M3B-C006', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Pyroptosis, PANoptosis, and NLRP3/inflammasome-linked programs form a distinct inflammatory injury family after SCI.',
    'synthesis',
    'medium',
    'Module 3A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M3A-P006, P022-P027", "topic_id": "M3B-T004", "tracker_id": "M3B-C007"}'
  FROM _m3_paper_map p
  WHERE p.tracker_id = 'M3A-P006'
  RETURNING claim_id
)
INSERT INTO _m3_claim_map (tracker_id, claim_id) SELECT 'M3B-C007', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Programmed inflammatory death claims should be separated from generic inflammation and from apoptotic neuroprotection claims.',
    'evidence standard',
    'high',
    'Module 3A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M3A-P022-P027", "topic_id": "M3B-T004", "tracker_id": "M3B-C008"}'
  FROM _m3_paper_map p
  WHERE p.tracker_id = 'M3A-P022'
  RETURNING claim_id
)
INSERT INTO _m3_claim_map (tracker_id, claim_id) SELECT 'M3B-C008', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Immune-metabolic and debris-handling programs link myeloid state to repair, chronic inflammation, fibrosis, and synaptic integrity.',
    'synthesis',
    'medium',
    'Module 3A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M3A-P007, P020-P021, P028-P032, P039-P043", "topic_id": "M3B-T005", "tracker_id": "M3B-C009"}'
  FROM _m3_paper_map p
  WHERE p.tracker_id = 'M3A-P007'
  RETURNING claim_id
)
INSERT INTO _m3_claim_map (tracker_id, claim_id) SELECT 'M3B-C009', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Myelin debris clearance can be reparative but may also coexist with chronic inflammation or fibrosis depending on pathway context.',
    'boundary condition',
    'high',
    'Module 3A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M3A-P021, P028, P032", "topic_id": "M3B-T005", "tracker_id": "M3B-C010"}'
  FROM _m3_paper_map p
  WHERE p.tracker_id = 'M3A-P021'
  RETURNING claim_id
)
INSERT INTO _m3_claim_map (tracker_id, claim_id) SELECT 'M3B-C010', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Single-cell and spatial data provide state maps that should refine older bulk polarization categories.',
    'implication',
    'medium',
    'Module 3A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M3A-P033, P042", "topic_id": "M3B-T006", "tracker_id": "M3B-C011"}'
  FROM _m3_paper_map p
  WHERE p.tracker_id = 'M3A-P033'
  RETURNING claim_id
)
INSERT INTO _m3_claim_map (tracker_id, claim_id) SELECT 'M3B-C011', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Omics observations are mapping evidence unless directly tied to perturbation or functional outcomes.',
    'evidence standard',
    'high',
    'Module 3A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M3A-P033, P042", "topic_id": "M3B-T006", "tracker_id": "M3B-C012"}'
  FROM _m3_paper_map p
  WHERE p.tracker_id = 'M3A-P033'
  RETURNING claim_id
)
INSERT INTO _m3_claim_map (tracker_id, claim_id) SELECT 'M3B-C012', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Exosomes, hydrogels, nanoparticles, and vesicle platforms can reprogram immune environments but confound cargo, carrier, and timing effects.',
    'boundary condition',
    'high',
    'Module 3A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M3A-P006, P012, P037-P041", "topic_id": "M3B-T007", "tracker_id": "M3B-C013"}'
  FROM _m3_paper_map p
  WHERE p.tracker_id = 'M3A-P006'
  RETURNING claim_id
)
INSERT INTO _m3_claim_map (tracker_id, claim_id) SELECT 'M3B-C013', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Delivery systems should be tagged by immune target and payload rather than collapsed into a generic biomaterial category.',
    'curation rule',
    'high',
    'Module 3A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M3A-P012, P037-P041", "topic_id": "M3B-T007", "tracker_id": "M3B-C014"}'
  FROM _m3_paper_map p
  WHERE p.tracker_id = 'M3A-P012'
  RETURNING claim_id
)
INSERT INTO _m3_claim_map (tracker_id, claim_id) SELECT 'M3B-C014', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Module 3 evidence must be stratified by acute/subacute/chronic phase because the same myeloid population can be protective or harmful at different times.',
    'synthesis rule',
    'high',
    'Module 3A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M3A-P001-M3A-P047", "topic_id": "M3B-T008", "tracker_id": "M3B-C015"}'
  FROM _m3_paper_map p
  WHERE p.tracker_id = 'M3A-P001'
  RETURNING claim_id
)
INSERT INTO _m3_claim_map (tracker_id, claim_id) SELECT 'M3B-C015', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Species and sex boundaries matter for immune modulation, especially where female-specific or zebrafish repair programs appear.',
    'boundary condition',
    'medium',
    'Module 3A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M3A-P001-M3A-P047", "topic_id": "M3B-T008", "tracker_id": "M3B-C016"}'
  FROM _m3_paper_map p
  WHERE p.tracker_id = 'M3A-P001'
  RETURNING claim_id
)
INSERT INTO _m3_claim_map (tracker_id, claim_id) SELECT 'M3B-C016', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'The saturated Module 3A corpus supports mechanism-specific immune consensus profiles rather than a single anti-inflammatory therapy claim.',
    'synthesis',
    'high',
    'Module 3A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M3A-P001-M3A-P047", "topic_id": "M3B-T008", "tracker_id": "M3B-C017"}'
  FROM _m3_paper_map p
  WHERE p.tracker_id = 'M3A-P001'
  RETURNING claim_id
)
INSERT INTO _m3_claim_map (tracker_id, claim_id) SELECT 'M3B-C017', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Repopulation after depletion is a distinct biological state and should not be treated as simple return to baseline microglia.',
    'curation rule',
    'medium',
    'Module 3A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M3A-P013-P017", "topic_id": "M3B-T001", "tracker_id": "M3B-C018"}'
  FROM _m3_paper_map p
  WHERE p.tracker_id = 'M3A-P013'
  RETURNING claim_id
)
INSERT INTO _m3_claim_map (tracker_id, claim_id) SELECT 'M3B-C018', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Plexin-B2 corralling establishes that immune-glial containment can support recovery.',
    'mechanistic',
    'medium',
    'Module 3A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M3A-P002", "topic_id": "M3B-T002", "tracker_id": "M3B-C019"}'
  FROM _m3_paper_map p
  WHERE p.tracker_id = 'M3A-P002'
  RETURNING claim_id
)
INSERT INTO _m3_claim_map (tracker_id, claim_id) SELECT 'M3B-C019', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'IL-4-type interventions can reprogram inflammatory responses but require species and route-specific interpretation.',
    'boundary condition',
    'medium',
    'Module 3A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M3A-P035", "topic_id": "M3B-T003", "tracker_id": "M3B-C020"}'
  FROM _m3_paper_map p
  WHERE p.tracker_id = 'M3A-P035'
  RETURNING claim_id
)
INSERT INTO _m3_claim_map (tracker_id, claim_id) SELECT 'M3B-C020', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Inflammasome activation can interact with systemic metabolic disease or small-molecule inhibition contexts.',
    'boundary condition',
    'medium',
    'Module 3A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M3A-P026-P027", "topic_id": "M3B-T004", "tracker_id": "M3B-C021"}'
  FROM _m3_paper_map p
  WHERE p.tracker_id = 'M3A-P026'
  RETURNING claim_id
)
INSERT INTO _m3_claim_map (tracker_id, claim_id) SELECT 'M3B-C021', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'TREM2, FGF4/Clec10a, and debris-processing pathways should be curated as debris/efferocytosis mechanisms.',
    'curation rule',
    'medium',
    'Module 3A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M3A-P020-P021", "topic_id": "M3B-T005", "tracker_id": "M3B-C022"}'
  FROM _m3_paper_map p
  WHERE p.tracker_id = 'M3A-P020'
  RETURNING claim_id
)
INSERT INTO _m3_claim_map (tracker_id, claim_id) SELECT 'M3B-C022', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Nanoparticle and vesicle studies are high-value for therapeutic delivery but often abstract-level first pass until cargo and biodistribution are extracted.',
    'curation boundary',
    'medium',
    'Module 3A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M3A-P038-P041", "topic_id": "M3B-T007", "tracker_id": "M3B-C023"}'
  FROM _m3_paper_map p
  WHERE p.tracker_id = 'M3A-P038'
  RETURNING claim_id
)
INSERT INTO _m3_claim_map (tracker_id, claim_id) SELECT 'M3B-C023', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Full-text upgrades should prioritize studies that contradict simple depletion, simple polarization, or simple anti-inflammatory interpretations.',
    'curation boundary',
    'high',
    'Module 3A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M3A-P001-M3A-P047", "topic_id": "M3B-T008", "tracker_id": "M3B-C024"}'
  FROM _m3_paper_map p
  WHERE p.tracker_id = 'M3A-P001'
  RETURNING claim_id
)
INSERT INTO _m3_claim_map (tracker_id, claim_id) SELECT 'M3B-C024', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Single-cell studies should be used to harmonize macrophage, microglia, monocyte, and neutrophil vocabularies across the database.',
    'curation rule',
    'medium',
    'Module 3A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M3A-P033, P042", "topic_id": "M3B-T006", "tracker_id": "M3B-C025"}'
  FROM _m3_paper_map p
  WHERE p.tracker_id = 'M3A-P033'
  RETURNING claim_id
)
INSERT INTO _m3_claim_map (tracker_id, claim_id) SELECT 'M3B-C025', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Macrophage-derived CXCL4 and TGF-beta scar programs connect immune state to Module 1 lesion architecture.',
    'implication',
    'medium',
    'Module 3A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M3A-P045-P046", "topic_id": "M3B-T002", "tracker_id": "M3B-C026"}'
  FROM _m3_paper_map p
  WHERE p.tracker_id = 'M3A-P045'
  RETURNING claim_id
)
INSERT INTO _m3_claim_map (tracker_id, claim_id) SELECT 'M3B-C026', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'IRF1-driven microglial PANoptosis is a candidate state program for future mechanistic extraction.',
    'mechanistic',
    'low',
    'Module 3A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M3A-P024", "topic_id": "M3B-T004", "tracker_id": "M3B-C027"}'
  FROM _m3_paper_map p
  WHERE p.tracker_id = 'M3A-P024'
  RETURNING claim_id
)
INSERT INTO _m3_claim_map (tracker_id, claim_id) SELECT 'M3B-C027', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'SYK-dependent lipid handling and foam-cell C1q programs connect metabolic macrophage states to recovery and synaptic loss.',
    'mechanistic',
    'medium',
    'Module 3A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M3A-P018-P019", "topic_id": "M3B-T005", "tracker_id": "M3B-C028"}'
  FROM _m3_paper_map p
  WHERE p.tracker_id = 'M3A-P018'
  RETURNING claim_id
)
INSERT INTO _m3_claim_map (tracker_id, claim_id) SELECT 'M3B-C028', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Localized cytokine delivery can improve repair outcomes while keeping systemic immune exposure lower in principle.',
    'implication',
    'low',
    'Module 3A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M3A-P037", "topic_id": "M3B-T007", "tracker_id": "M3B-C029"}'
  FROM _m3_paper_map p
  WHERE p.tracker_id = 'M3A-P037'
  RETURNING claim_id
)
INSERT INTO _m3_claim_map (tracker_id, claim_id) SELECT 'M3B-C029', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Module 3 consensus should remain mechanism-family based until full-text effect sizes and cell-marker panels are extracted.',
    'synthesis rule',
    'high',
    'Module 3A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M3A-P001-M3A-P047", "topic_id": "M3B-T008", "tracker_id": "M3B-C030"}'
  FROM _m3_paper_map p
  WHERE p.tracker_id = 'M3A-P001'
  RETURNING claim_id
)
INSERT INTO _m3_claim_map (tracker_id, claim_id) SELECT 'M3B-C030', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Abnormally innervated sensory nerves may regulate macrophage polarization, linking immune state with circuit remodeling.',
    'implication',
    'low',
    'Module 3A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M3A-P034", "topic_id": "M3B-T003", "tracker_id": "M3B-C031"}'
  FROM _m3_paper_map p
  WHERE p.tracker_id = 'M3A-P034'
  RETURNING claim_id
)
INSERT INTO _m3_claim_map (tracker_id, claim_id) SELECT 'M3B-C031', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Microglial efferocytosis via LRP-1 is a candidate reparative clearance mechanism.',
    'mechanistic',
    'low',
    'Module 3A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M3A-P043", "topic_id": "M3B-T005", "tracker_id": "M3B-C032"}'
  FROM _m3_paper_map p
  WHERE p.tracker_id = 'M3A-P043'
  RETURNING claim_id
)
INSERT INTO _m3_claim_map (tracker_id, claim_id) SELECT 'M3B-C032', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'OEC transplantation targeting macrophage extracellular traps cross-links immune modulation with Module 4 cell therapies.',
    'implication',
    'low',
    'Module 3A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M3A-P047", "topic_id": "M3B-T008", "tracker_id": "M3B-C033"}'
  FROM _m3_paper_map p
  WHERE p.tracker_id = 'M3A-P047'
  RETURNING claim_id
)
INSERT INTO _m3_claim_map (tracker_id, claim_id) SELECT 'M3B-C033', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Vascular-immune microenvironment reprogramming cross-links immune repair with scaffold and vascular modules.',
    'implication',
    'low',
    'Module 3A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M3A-P038", "topic_id": "M3B-T008", "tracker_id": "M3B-C034"}'
  FROM _m3_paper_map p
  WHERE p.tracker_id = 'M3A-P038'
  RETURNING claim_id
)
INSERT INTO _m3_claim_map (tracker_id, claim_id) SELECT 'M3B-C034', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Chronic nonresolving neuroinflammation is a separate target from acute protective immune activation.',
    'boundary condition',
    'high',
    'Module 3A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M3A-P001, P013-P017", "topic_id": "M3B-T001", "tracker_id": "M3B-C035"}'
  FROM _m3_paper_map p
  WHERE p.tracker_id = 'M3A-P001'
  RETURNING claim_id
)
INSERT INTO _m3_claim_map (tracker_id, claim_id) SELECT 'M3B-C035', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Consensus wording should avoid treating inflammation as one directionally bad variable.',
    'synthesis rule',
    'high',
    'Module 3A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass claim abstraction; full text needed for effect sizes.", "source_paper_tracker_id": "M3A-P001-M3A-P047", "topic_id": "M3B-T008", "tracker_id": "M3B-C036"}'
  FROM _m3_paper_map p
  WHERE p.tracker_id = 'M3A-P001'
  RETURNING claim_id
)
INSERT INTO _m3_claim_map (tracker_id, claim_id) SELECT 'M3B-C036', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M3B-L001"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O001'
  WHERE c.tracker_id = 'M3B-C001'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L001', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M3B-L002"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O014'
  WHERE c.tracker_id = 'M3B-C002'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L002', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M3B-L003"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O002'
  WHERE c.tracker_id = 'M3B-C003'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L003', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M3B-L004"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O018'
  WHERE c.tracker_id = 'M3B-C004'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L004', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M3B-L005"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O004'
  WHERE c.tracker_id = 'M3B-C005'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L005', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M3B-L006"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O004'
  WHERE c.tracker_id = 'M3B-C006'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L006', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M3B-L007"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O006'
  WHERE c.tracker_id = 'M3B-C007'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L007', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M3B-L008"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O022'
  WHERE c.tracker_id = 'M3B-C008'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L008', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M3B-L009"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O007'
  WHERE c.tracker_id = 'M3B-C009'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L009', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M3B-L010"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O021'
  WHERE c.tracker_id = 'M3B-C010'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L010', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M3B-L011"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O033'
  WHERE c.tracker_id = 'M3B-C011'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L011', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M3B-L012"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O033'
  WHERE c.tracker_id = 'M3B-C012'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L012', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M3B-L013"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O006'
  WHERE c.tracker_id = 'M3B-C013'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L013', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M3B-L014"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O012'
  WHERE c.tracker_id = 'M3B-C014'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L014', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M3B-L015"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O001'
  WHERE c.tracker_id = 'M3B-C015'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L015', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M3B-L016"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O014'
  WHERE c.tracker_id = 'M3B-C016'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L016', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M3B-L017"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O001'
  WHERE c.tracker_id = 'M3B-C017'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L017', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M3B-L018"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O013'
  WHERE c.tracker_id = 'M3B-C018'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L018', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M3B-L019"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O002'
  WHERE c.tracker_id = 'M3B-C019'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L019', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M3B-L020"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O035'
  WHERE c.tracker_id = 'M3B-C020'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L020', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M3B-L021"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O026'
  WHERE c.tracker_id = 'M3B-C021'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L021', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M3B-L022"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O020'
  WHERE c.tracker_id = 'M3B-C022'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L022', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M3B-L023"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O038'
  WHERE c.tracker_id = 'M3B-C023'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L023', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M3B-L024"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O014'
  WHERE c.tracker_id = 'M3B-C024'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L024', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M3B-L025"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O033'
  WHERE c.tracker_id = 'M3B-C025'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L025', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M3B-L026"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O045'
  WHERE c.tracker_id = 'M3B-C026'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L026', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M3B-L027"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O024'
  WHERE c.tracker_id = 'M3B-C027'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L027', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M3B-L028"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O018'
  WHERE c.tracker_id = 'M3B-C028'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L028', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M3B-L029"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O037'
  WHERE c.tracker_id = 'M3B-C029'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L029', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M3B-L030"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O001'
  WHERE c.tracker_id = 'M3B-C030'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L030', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M3B-L031"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O034'
  WHERE c.tracker_id = 'M3B-C031'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L031', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M3B-L032"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O043'
  WHERE c.tracker_id = 'M3B-C032'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L032', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M3B-L033"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O047'
  WHERE c.tracker_id = 'M3B-C033'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L033', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M3B-L034"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O038'
  WHERE c.tracker_id = 'M3B-C034'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L034', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M3B-L035"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O001'
  WHERE c.tracker_id = 'M3B-C035'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L035', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M3B-L036"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O002'
  WHERE c.tracker_id = 'M3B-C036'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L036', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'corroborates',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M3B-L037"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O003'
  WHERE c.tracker_id = 'M3B-C001'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L037', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'corroborates',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M3B-L038"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O013'
  WHERE c.tracker_id = 'M3B-C001'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L038', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'corroborates',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M3B-L039"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O014'
  WHERE c.tracker_id = 'M3B-C001'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L039', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'corroborates',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M3B-L040"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O015'
  WHERE c.tracker_id = 'M3B-C001'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L040', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'corroborates',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M3B-L041"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O016'
  WHERE c.tracker_id = 'M3B-C001'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L041', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'corroborates',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M3B-L042"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O017'
  WHERE c.tracker_id = 'M3B-C001'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L042', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'corroborates',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M3B-L043"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O016'
  WHERE c.tracker_id = 'M3B-C002'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L043', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'corroborates',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M3B-L044"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O045'
  WHERE c.tracker_id = 'M3B-C003'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L044', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'corroborates',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M3B-L045"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O046'
  WHERE c.tracker_id = 'M3B-C003'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L045', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'corroborates',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M3B-L046"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O019'
  WHERE c.tracker_id = 'M3B-C004'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L046', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'corroborates',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M3B-L047"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O045'
  WHERE c.tracker_id = 'M3B-C004'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L047', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'corroborates',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M3B-L048"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O008'
  WHERE c.tracker_id = 'M3B-C005'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L048', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'corroborates',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M3B-L049"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O009'
  WHERE c.tracker_id = 'M3B-C005'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L049', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'corroborates',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M3B-L050"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O010'
  WHERE c.tracker_id = 'M3B-C005'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L050', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'corroborates',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M3B-L051"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O011'
  WHERE c.tracker_id = 'M3B-C005'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L051', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'corroborates',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M3B-L052"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O033'
  WHERE c.tracker_id = 'M3B-C005'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L052', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'corroborates',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M3B-L053"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O034'
  WHERE c.tracker_id = 'M3B-C005'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L053', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'corroborates',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M3B-L054"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O035'
  WHERE c.tracker_id = 'M3B-C005'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L054', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'corroborates',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M3B-L055"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O036'
  WHERE c.tracker_id = 'M3B-C005'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L055', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'corroborates',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M3B-L056"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O044'
  WHERE c.tracker_id = 'M3B-C005'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L056', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'corroborates',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M3B-L057"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O005'
  WHERE c.tracker_id = 'M3B-C006'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L057', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'corroborates',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M3B-L058"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O008'
  WHERE c.tracker_id = 'M3B-C006'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L058', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'corroborates',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M3B-L059"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O009'
  WHERE c.tracker_id = 'M3B-C006'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L059', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'corroborates',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M3B-L060"}'
  FROM _m3_claim_map c
  JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O010'
  WHERE c.tracker_id = 'M3B-C006'
  RETURNING link_id
)
INSERT INTO _m3_link_map (tracker_id, link_id) SELECT 'M3B-L060', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Microglial depletion and CSF1R-pathway modulation have phase-dependent effects after SCI: early broad depletion can remove useful repair functions, while delayed or pathway-specific modulation can reduce chronic inflammatory programs and selected secondary injury endpoints.',
    'M3B-T001',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M3B-B001", "M3B-B008"], "claim_tracker_ids": ["M3B-C001", "M3B-C002", "M3B-C018", "M3B-C035"], "consensus_draft_id": "M3B-S001", "observation_tracker_ids": ["M3B-O001", "M3B-O003", "M3B-O013", "M3B-O014", "M3B-O015", "M3B-O016", "M3B-O017"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "B001, B008", "topic_id": "M3B-T001"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m3_consensus_map (tracker_id, consensus_id) SELECT 'M3B-S001', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O001'
WHERE c.tracker_id = 'M3B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O003'
WHERE c.tracker_id = 'M3B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O013'
WHERE c.tracker_id = 'M3B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O014'
WHERE c.tracker_id = 'M3B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O015'
WHERE c.tracker_id = 'M3B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O016'
WHERE c.tracker_id = 'M3B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O017'
WHERE c.tracker_id = 'M3B-S001';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Myeloid cells are not a single injury-amplifying compartment; they can compact and contain wounds while also contributing to fibrotic scarring, so consensus claims must distinguish corralling, debris handling, matrix remodeling, and fibrosis-promoting functions.',
    'M3B-T002',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M3B-B002", "M3B-B007", "M3B-B008"], "claim_tracker_ids": ["M3B-C003", "M3B-C004", "M3B-C019", "M3B-C026"], "consensus_draft_id": "M3B-S002", "observation_tracker_ids": ["M3B-O002", "M3B-O018", "M3B-O019", "M3B-O045", "M3B-O046"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "B002, B007, B008", "topic_id": "M3B-T002"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m3_consensus_map (tracker_id, consensus_id) SELECT 'M3B-S002', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O002'
WHERE c.tracker_id = 'M3B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O018'
WHERE c.tracker_id = 'M3B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O019'
WHERE c.tracker_id = 'M3B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O045'
WHERE c.tracker_id = 'M3B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O046'
WHERE c.tracker_id = 'M3B-S002';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Macrophage and microglia polarization findings support state-dependent immune modulation, but M1/M2 labels are insufficient without marker panels, timing, resident-versus-recruited identity, injury model, and endpoint-specific outcome data.',
    'M3B-T003',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M3B-B003", "M3B-B008"], "claim_tracker_ids": ["M3B-C005", "M3B-C006", "M3B-C020", "M3B-C031"], "consensus_draft_id": "M3B-S003", "observation_tracker_ids": ["M3B-O004", "M3B-O005", "M3B-O006", "M3B-O007", "M3B-O008", "M3B-O009", "M3B-O010", "M3B-O011", "M3B-O033", "M3B-O034", "M3B-O035", "M3B-O036", "M3B-O044"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "B003, B008", "topic_id": "M3B-T003"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m3_consensus_map (tracker_id, consensus_id) SELECT 'M3B-S003', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O004'
WHERE c.tracker_id = 'M3B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O005'
WHERE c.tracker_id = 'M3B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O006'
WHERE c.tracker_id = 'M3B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O007'
WHERE c.tracker_id = 'M3B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O008'
WHERE c.tracker_id = 'M3B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O009'
WHERE c.tracker_id = 'M3B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O010'
WHERE c.tracker_id = 'M3B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O011'
WHERE c.tracker_id = 'M3B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O033'
WHERE c.tracker_id = 'M3B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O034'
WHERE c.tracker_id = 'M3B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O035'
WHERE c.tracker_id = 'M3B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O036'
WHERE c.tracker_id = 'M3B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O044'
WHERE c.tracker_id = 'M3B-S003';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Inflammasome activation, pyroptosis, PANoptosis, and related inflammatory death pathways form a coherent secondary-injury axis after SCI, but pathway claims should remain tied to the assayed molecule, cell population, timing, and readout.',
    'M3B-T004',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M3B-B004", "M3B-B008"], "claim_tracker_ids": ["M3B-C007", "M3B-C008", "M3B-C021", "M3B-C027"], "consensus_draft_id": "M3B-S004", "observation_tracker_ids": ["M3B-O006", "M3B-O022", "M3B-O023", "M3B-O024", "M3B-O025", "M3B-O026", "M3B-O027"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "B004, B008", "topic_id": "M3B-T004"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m3_consensus_map (tracker_id, consensus_id) SELECT 'M3B-S004', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O006'
WHERE c.tracker_id = 'M3B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O022'
WHERE c.tracker_id = 'M3B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O023'
WHERE c.tracker_id = 'M3B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O024'
WHERE c.tracker_id = 'M3B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O025'
WHERE c.tracker_id = 'M3B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O026'
WHERE c.tracker_id = 'M3B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O027'
WHERE c.tracker_id = 'M3B-S004';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Immune metabolism, lipid handling, debris clearance, and efferocytosis link myeloid state to both repair and chronic degeneration; the strongest consensus is that phagocytic and metabolic competence must be tracked separately from inflammatory cytokine tone.',
    'M3B-T005',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M3B-B002", "M3B-B006", "M3B-B008"], "claim_tracker_ids": ["M3B-C009", "M3B-C010", "M3B-C022", "M3B-C028", "M3B-C032"], "consensus_draft_id": "M3B-S005", "observation_tracker_ids": ["M3B-O007", "M3B-O018", "M3B-O019", "M3B-O020", "M3B-O021", "M3B-O028", "M3B-O029", "M3B-O030", "M3B-O031", "M3B-O032", "M3B-O039", "M3B-O040", "M3B-O041", "M3B-O042", "M3B-O043"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "B002, B006, B008", "topic_id": "M3B-T005"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m3_consensus_map (tracker_id, consensus_id) SELECT 'M3B-S005', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O007'
WHERE c.tracker_id = 'M3B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O018'
WHERE c.tracker_id = 'M3B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O019'
WHERE c.tracker_id = 'M3B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O020'
WHERE c.tracker_id = 'M3B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O021'
WHERE c.tracker_id = 'M3B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O028'
WHERE c.tracker_id = 'M3B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O029'
WHERE c.tracker_id = 'M3B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O030'
WHERE c.tracker_id = 'M3B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O031'
WHERE c.tracker_id = 'M3B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O032'
WHERE c.tracker_id = 'M3B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O039'
WHERE c.tracker_id = 'M3B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O040'
WHERE c.tracker_id = 'M3B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O041'
WHERE c.tracker_id = 'M3B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O042'
WHERE c.tracker_id = 'M3B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O043'
WHERE c.tracker_id = 'M3B-S005';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Single-cell, spatial, and multi-omic studies should be used to refine immune-cell identity, lesion geography, and state-transition vocabulary, not as standalone proof that any one immune state is therapeutically sufficient.',
    'M3B-T006',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M3B-B006", "M3B-B008"], "claim_tracker_ids": ["M3B-C011", "M3B-C012", "M3B-C025"], "consensus_draft_id": "M3B-S006", "observation_tracker_ids": ["M3B-O033", "M3B-O042"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "B006, B008", "topic_id": "M3B-T006"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m3_consensus_map (tracker_id, consensus_id) SELECT 'M3B-S006', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O033'
WHERE c.tracker_id = 'M3B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O042'
WHERE c.tracker_id = 'M3B-S006';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Immune-modifying biomaterials, vesicles, nanoparticles, and hydrogels create actionable delivery strategies, but consensus must separate payload biology from carrier effects, route, release kinetics, lesion localization, and treatment window.',
    'M3B-T007',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M3B-B005", "M3B-B008"], "claim_tracker_ids": ["M3B-C013", "M3B-C014", "M3B-C023", "M3B-C029"], "consensus_draft_id": "M3B-S007", "observation_tracker_ids": ["M3B-O006", "M3B-O012", "M3B-O037", "M3B-O038", "M3B-O039", "M3B-O040", "M3B-O041"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "B005, B008", "topic_id": "M3B-T007"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m3_consensus_map (tracker_id, consensus_id) SELECT 'M3B-S007', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O006'
WHERE c.tracker_id = 'M3B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O012'
WHERE c.tracker_id = 'M3B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O037'
WHERE c.tracker_id = 'M3B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O038'
WHERE c.tracker_id = 'M3B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O039'
WHERE c.tracker_id = 'M3B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O040'
WHERE c.tracker_id = 'M3B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O041'
WHERE c.tracker_id = 'M3B-S007';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Module 3 supports mechanism-specific immune consensus profiles, not a broad anti-inflammatory thesis: timing, cell origin, immune function, sex/species/model context, and endpoint class are required fields for interpreting immune modulation after SCI.',
    'M3B-T008',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["all boundary records"], "claim_tracker_ids": ["M3B-C015", "M3B-C016", "M3B-C017", "M3B-C024", "M3B-C030", "M3B-C033", "M3B-C034", "M3B-C035", "M3B-C036"], "consensus_draft_id": "M3B-S008", "observation_tracker_ids": ["M3B-O001", "M3B-O002", "M3B-O003", "M3B-O004", "M3B-O005", "M3B-O006", "M3B-O007", "M3B-O008", "M3B-O009", "M3B-O010", "M3B-O011", "M3B-O012", "M3B-O013", "M3B-O014", "M3B-O015", "M3B-O016", "M3B-O017", "M3B-O018", "M3B-O019", "M3B-O020", "M3B-O021", "M3B-O022", "M3B-O023", "M3B-O024", "M3B-O025", "M3B-O026", "M3B-O027", "M3B-O028", "M3B-O029", "M3B-O030", "M3B-O031", "M3B-O032", "M3B-O033", "M3B-O034", "M3B-O035", "M3B-O036", "M3B-O037", "M3B-O038", "M3B-O039", "M3B-O040", "M3B-O041", "M3B-O042", "M3B-O043", "M3B-O044", "M3B-O045", "M3B-O046", "M3B-O047"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "all boundary records", "topic_id": "M3B-T008"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m3_consensus_map (tracker_id, consensus_id) SELECT 'M3B-S008', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O001'
WHERE c.tracker_id = 'M3B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O002'
WHERE c.tracker_id = 'M3B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O003'
WHERE c.tracker_id = 'M3B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O004'
WHERE c.tracker_id = 'M3B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O005'
WHERE c.tracker_id = 'M3B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O006'
WHERE c.tracker_id = 'M3B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O007'
WHERE c.tracker_id = 'M3B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O008'
WHERE c.tracker_id = 'M3B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O009'
WHERE c.tracker_id = 'M3B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O010'
WHERE c.tracker_id = 'M3B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O011'
WHERE c.tracker_id = 'M3B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O012'
WHERE c.tracker_id = 'M3B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O013'
WHERE c.tracker_id = 'M3B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O014'
WHERE c.tracker_id = 'M3B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O015'
WHERE c.tracker_id = 'M3B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O016'
WHERE c.tracker_id = 'M3B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O017'
WHERE c.tracker_id = 'M3B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O018'
WHERE c.tracker_id = 'M3B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O019'
WHERE c.tracker_id = 'M3B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O020'
WHERE c.tracker_id = 'M3B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O021'
WHERE c.tracker_id = 'M3B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O022'
WHERE c.tracker_id = 'M3B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O023'
WHERE c.tracker_id = 'M3B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O024'
WHERE c.tracker_id = 'M3B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O025'
WHERE c.tracker_id = 'M3B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O026'
WHERE c.tracker_id = 'M3B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O027'
WHERE c.tracker_id = 'M3B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O028'
WHERE c.tracker_id = 'M3B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O029'
WHERE c.tracker_id = 'M3B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O030'
WHERE c.tracker_id = 'M3B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O031'
WHERE c.tracker_id = 'M3B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O032'
WHERE c.tracker_id = 'M3B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O033'
WHERE c.tracker_id = 'M3B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O034'
WHERE c.tracker_id = 'M3B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O035'
WHERE c.tracker_id = 'M3B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O036'
WHERE c.tracker_id = 'M3B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O037'
WHERE c.tracker_id = 'M3B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O038'
WHERE c.tracker_id = 'M3B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O039'
WHERE c.tracker_id = 'M3B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O040'
WHERE c.tracker_id = 'M3B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O041'
WHERE c.tracker_id = 'M3B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O042'
WHERE c.tracker_id = 'M3B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O043'
WHERE c.tracker_id = 'M3B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O044'
WHERE c.tracker_id = 'M3B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O045'
WHERE c.tracker_id = 'M3B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O046'
WHERE c.tracker_id = 'M3B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m3_consensus_map c
JOIN _m3_observation_map o ON o.tracker_id = 'M3B-O047'
WHERE c.tracker_id = 'M3B-S008';

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
  SELECT COUNT(*) INTO paper_count FROM _m3_paper_map;
  SELECT COUNT(*) INTO experiment_count FROM _m3_experiment_map;
  SELECT COUNT(*) INTO observation_count FROM _m3_observation_map;
  SELECT COUNT(*) INTO claim_count FROM _m3_claim_map;
  SELECT COUNT(*) INTO link_count FROM _m3_link_map;
  SELECT COUNT(*) INTO consensus_count FROM _m3_consensus_map;
  SELECT COUNT(*) INTO consensus_observation_count
  FROM Consensus_Observation co
  JOIN _m3_consensus_map cm ON cm.consensus_id = co.consensus_id;
  IF paper_count <> 47 THEN RAISE EXCEPTION 'Expected 47 papers, found %', paper_count; END IF;
  IF experiment_count <> 94 THEN RAISE EXCEPTION 'Unexpected experiment count %', experiment_count; END IF;
  IF observation_count <> 94 THEN RAISE EXCEPTION 'Expected 94 observations, found %', observation_count; END IF;
  IF claim_count <> 36 THEN RAISE EXCEPTION 'Expected 36 claims, found %', claim_count; END IF;
  IF link_count <> 60 THEN RAISE EXCEPTION 'Expected 60 evidence links, found %', link_count; END IF;
  IF consensus_count <> 8 THEN RAISE EXCEPTION 'Expected 8 consensus rows, found %', consensus_count; END IF;
  IF consensus_observation_count <> 103 THEN RAISE EXCEPTION 'Unexpected consensus-observation count %', consensus_observation_count; END IF;
END $$;

COMMIT;
