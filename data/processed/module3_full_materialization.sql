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
    NULL, NULL, '33052221',
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
    NULL, NULL, '32112058',
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
    NULL, NULL, '30386212',
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
    NULL, NULL, '33036632',
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
    NULL, NULL, '36466087',
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
    NULL, NULL, '38982427',
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
    NULL, NULL, '40328251',
    NULL, '{"curator_notes": "Recent immune-state mechanism; no PMC full text located", "module": "Module 3B", "tracker_id": "M3A-P007"}'
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
    'A-layer full text; Full text PMC; Fig. 1-2',
    'Tracker experiment M3A-P001-E001',
    'Extracted details: Flow cytometry and qPCR at 2 dpi quantified CD45int microglia, infiltrating monocytes, neutrophils, and ROS at the lesion epicenter. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "PLX5622 begun 3 weeks before injury and continued to 2 dpi", "control_type": "Sham/vehicle, sham/PLX, SCI/vehicle, SCI/PLX; n=6-7 for flow cytometry arms", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Infinite Horizon impactor", "injury_model": "T10 thoracic contusion SCI", "injury_severity": "60 or 70 kdyn moderate/severe contusion", "intervention_type": "PLX5622 1200 ppm chow for pre-injury microglial and myeloid depletion", "methods_summary": "Flow cytometry and qPCR at 2 dpi quantified CD45int microglia, infiltrating monocytes, neutrophils, and ROS at the lesion epicenter.", "observation_tracker_ids": ["M3B-O001"], "sex": "Male", "source_experiment_tracker_id": "M3A-P001-E001", "source_paper_tracker_id": "M3A-P001", "species": "Mouse", "strain": "C57BL/6 and Cx3cr1-GFP", "tracker_key": "M3A-P001::M3A-P001-E001", "vertebral_level": "T10"}'
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
    'A-layer full text; Full text PMC; Fig. 3-5',
    'Tracker experiment M3A-P001-E002',
    'Extracted details: Post-injury depletion reduced spinal-cord and brain inflammatory programs, improved neuronal survival, and improved motor, cognitive, and depressive-like outcomes; systemic myeloid effects are part of the interpretation. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "PLX5622 begun on injury day and continued for 6 weeks; BMS through 42 dpi and neurobehavioral tests at 5-6 weeks", "control_type": "Sham/vehicle, sham/PLX, SCI/vehicle, SCI/PLX; blinded longitudinal behavioral assessment", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Infinite Horizon impactor", "injury_model": "T10 thoracic contusion SCI", "injury_severity": "60 or 70 kdyn moderate/severe contusion", "intervention_type": "Post-injury PLX5622 1200 ppm chow", "methods_summary": "Post-injury depletion reduced spinal-cord and brain inflammatory programs, improved neuronal survival, and improved motor, cognitive, and depressive-like outcomes; systemic myeloid effects are part of the interpretation.", "observation_tracker_ids": ["M3B-O048"], "sex": "Male", "source_experiment_tracker_id": "M3A-P001-E002", "source_paper_tracker_id": "M3A-P001", "species": "Mouse", "strain": "C57BL/6 and Cx3cr1-GFP", "tracker_key": "M3A-P001::M3A-P001-E002", "vertebral_level": "T10"}'
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
    'A-layer full text; Full text PMC; Fig. 1-2',
    'Tracker experiment M3A-P002-E001',
    'Extracted details: INTACT RNA-seq, immunostaining, and targeted validation showed injury-activated microglia/macrophages upregulated Plexin-B2 and axon-guidance, motility, and matrix-interaction programs. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Myeloid nuclei profiled at 3, 7, and 14 dpi; tamoxifen at 3 and 1 days before injury", "control_type": "Sham surgery, littermate controls, and myeloid Plexin-B2 conditional knockout controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Microsurgical dorsal-column transection", "injury_model": "T8 dorsal-column transection", "injury_severity": "Transection as reported", "intervention_type": "Plexin-B2 induction and myeloid-cell-specific deletion", "methods_summary": "INTACT RNA-seq, immunostaining, and targeted validation showed injury-activated microglia/macrophages upregulated Plexin-B2 and axon-guidance, motility, and matrix-interaction programs.", "observation_tracker_ids": ["M3B-O002"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M3A-P002-E001", "source_paper_tracker_id": "M3A-P002", "species": "Mouse", "strain": "Cx3cr1CreER/INTACT and Plxnb2 conditional knockout lines", "tracker_key": "M3A-P002::M3A-P002-E001", "vertebral_level": "T8"}'
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
    'A-layer full text; Full text PMC; Fig. 3-5',
    'Tracker experiment M3A-P002-E002',
    'Extracted details: Plexin-B2 loss impaired corralling, wound compaction, inflammatory confinement, axon and 5-HT fiber preservation, and BMS, rotarod, ladder, and sensory recovery. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Tamoxifen every other day from 3 days before injury through 5 weeks; behavioral and tissue follow-up to 35 dpi", "control_type": "Littermate controls with the same tamoxifen regimen", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Infinite Horizon impactor", "injury_model": "T8 moderate contusion SCI", "injury_severity": "45 kdyn moderate contusion", "intervention_type": "Myeloid Plexin-B2 ablation", "methods_summary": "Plexin-B2 loss impaired corralling, wound compaction, inflammatory confinement, axon and 5-HT fiber preservation, and BMS, rotarod, ladder, and sensory recovery.", "observation_tracker_ids": ["M3B-O049"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M3A-P002-E002", "source_paper_tracker_id": "M3A-P002", "species": "Mouse", "strain": "Plxnb2 conditional knockout and littermate controls", "tracker_key": "M3A-P002::M3A-P002-E002", "vertebral_level": "T8"}'
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
    'A-layer full text; Full text PMC; Fig. 1-3',
    'Tracker experiment M3A-P003-E001',
    'Extracted details: Chronic CSF1R blockade selectively reduced SCI-induced microglial proliferation and IBA1 response without changing the non-injured microglial response. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "GW2580 begun 4 weeks before injury and continued to 6 weeks post-lesion", "control_type": "Untreated diet and GW2580 diet; n=12 per behavioral group", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Microsurgical lateral hemisection", "injury_model": "T9 lateral spinal cord hemisection", "injury_severity": "Incomplete hemisection", "intervention_type": "GW2580 0.1% incorporated into chow", "methods_summary": "Chronic CSF1R blockade selectively reduced SCI-induced microglial proliferation and IBA1 response without changing the non-injured microglial response.", "observation_tracker_ids": ["M3B-O003"], "sex": "Female", "source_experiment_tracker_id": "M3A-P003-E001", "source_paper_tracker_id": "M3A-P003", "species": "Mouse", "strain": "Female CX3CR1-GFP heterozygotes on C57BL/6", "tracker_key": "M3A-P003::M3A-P003-E001", "vertebral_level": "T9"}'
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
    'A-layer full text; Full text PMC; Fig. 4-7',
    'Tracker experiment M3A-P003-E002',
    'Extracted details: Treatment reduced gliosis and microcavity formation and improved fine paw-placement and CatWalk parameters, while lesion extension and volume by MRI were not changed. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "MRI at 4 and 6 weeks; histology at 2 and 6 weeks; behavioral testing through 6 weeks", "control_type": "Untreated diet versus GW2580 diet", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Microsurgical lateral hemisection", "injury_model": "T9 lateral spinal cord hemisection", "injury_severity": "Incomplete hemisection", "intervention_type": "GW2580 0.1% chow", "methods_summary": "Treatment reduced gliosis and microcavity formation and improved fine paw-placement and CatWalk parameters, while lesion extension and volume by MRI were not changed.", "observation_tracker_ids": ["M3B-O050"], "sex": "Female", "source_experiment_tracker_id": "M3A-P003-E002", "source_paper_tracker_id": "M3A-P003", "species": "Mouse", "strain": "Female CX3CR1-GFP heterozygotes on C57BL/6", "tracker_key": "M3A-P003::M3A-P003-E002", "vertebral_level": "T9"}'
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
    'A-layer full text; Full text PMC; in vitro and Fig. 1-4',
    'Tracker experiment M3A-P004-E001',
    'Extracted details: HMGB1 release from necroptotic astrocytes and HMGB1 stimulation of microglia in vitro were linked to RAGE-NF-kB pro-inflammatory polarization; qRT-PCR, immunostaining, western blot, and ELISA assessed the pathway. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Glycyrrhizin or FPS-ZM1 begun immediately after injury and given daily for 14 days", "control_type": "Sham, SCI saline, SCI glycyrrhizin, and SCI FPS-ZM1 groups", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "0.5 mm forceps closure for 20 s", "injury_model": "T8 spinal cord crush SCI", "injury_severity": "Crush injury as reported", "intervention_type": "HMGB1 inhibition with glycyrrhizin or RAGE inhibition with FPS-ZM1", "methods_summary": "HMGB1 release from necroptotic astrocytes and HMGB1 stimulation of microglia in vitro were linked to RAGE-NF-kB pro-inflammatory polarization; qRT-PCR, immunostaining, western blot, and ELISA assessed the pathway.", "observation_tracker_ids": ["M3B-O004"], "sex": "Male", "source_experiment_tracker_id": "M3A-P004-E001", "source_paper_tracker_id": "M3A-P004", "species": "Rat", "strain": "Sprague-Dawley", "tracker_key": "M3A-P004::M3A-P004-E001", "vertebral_level": "T8"}'
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
    'A-layer full text; Full text PMC; Fig. 5-8',
    'Tracker experiment M3A-P004-E002',
    'Extracted details: Inhibiting HMGB1 or RAGE shifted macrophage/microglia markers away from pro-inflammatory and toward anti-inflammatory states, reduced neuronal loss and demyelination, and improved BBB and rump-height-index recovery. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Functional and tissue follow-up through 14 dpi and later recovery assessment", "control_type": "Sham and SCI saline controls; glycyrrhizin and FPS-ZM1 treatment groups", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "0.5 mm forceps closure for 20 s", "injury_model": "T8 spinal cord crush SCI", "injury_severity": "Crush injury as reported", "intervention_type": "HMGB1-RAGE axis inhibition", "methods_summary": "Inhibiting HMGB1 or RAGE shifted macrophage/microglia markers away from pro-inflammatory and toward anti-inflammatory states, reduced neuronal loss and demyelination, and improved BBB and rump-height-index recovery.", "observation_tracker_ids": ["M3B-O051"], "sex": "Male", "source_experiment_tracker_id": "M3A-P004-E002", "source_paper_tracker_id": "M3A-P004", "species": "Rat", "strain": "Sprague-Dawley", "tracker_key": "M3A-P004::M3A-P004-E002", "vertebral_level": "T8"}'
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
    'A-layer full text; Full text PMC; Fig. 1-4',
    'Tracker experiment M3A-P005-E001',
    'Extracted details: CitH3/CD68-positive macrophage extracellular traps were detected in the lesion; DNase I reduced trap-associated M1-like polarization, tissue injury, and motor deficits. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "DNase I immediately after injury; BBB and inclined-plane testing at 0, 1, 7, 14, 21, and 28 dpi; tissue at 7 dpi", "control_type": "Sham, SCI, and SCI plus DNase I; n=32 per group initially", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "NYU/MASCIS impactor; 10 g rod from 25 mm", "injury_model": "T10 spinal cord contusion SCI", "injury_severity": "Contusion as reported", "intervention_type": "DNase I 5 mg/kg tail vein to limit macrophage extracellular traps", "methods_summary": "CitH3/CD68-positive macrophage extracellular traps were detected in the lesion; DNase I reduced trap-associated M1-like polarization, tissue injury, and motor deficits.", "observation_tracker_ids": ["M3B-O005"], "sex": "Male", "source_experiment_tracker_id": "M3A-P005-E001", "source_paper_tracker_id": "M3A-P005", "species": "Rat", "strain": "Adult male Sprague-Dawley", "tracker_key": "M3A-P005::M3A-P005-E001", "vertebral_level": "T10"}'
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
    'A-layer full text; Full text PMC; Fig. 5-8 and human cohort',
    'Tracker experiment M3A-P005-E002',
    'Extracted details: Co-IP and western blot linked macrophage-trap products to LL37-P2X7R-NF-kB signaling and M1 polarization; serum trap markers showed a severity association with human ASIA scores, not a treatment effect. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Rat pathway assays at 7 dpi; human serum markers correlated with ASIA scores", "control_type": "Vehicle/SCI controls, DNase I treatment, and human severity comparisons", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "NYU/MASCIS impactor for rat arm", "injury_model": "Rat SCI contusion plus human serum biomarker cohort", "injury_severity": "Contusion as reported", "intervention_type": "LL37-P2X7R-NF-kB extracellular signaling mechanism", "methods_summary": "Co-IP and western blot linked macrophage-trap products to LL37-P2X7R-NF-kB signaling and M1 polarization; serum trap markers showed a severity association with human ASIA scores, not a treatment effect.", "observation_tracker_ids": ["M3B-O052"], "sex": "Male rats; human sex as reported", "source_experiment_tracker_id": "M3A-P005-E002", "source_paper_tracker_id": "M3A-P005", "species": "Rat plus human SCI serum", "strain": "Sprague-Dawley rats; human cohort", "tracker_key": "M3A-P005::M3A-P005-E002", "vertebral_level": "T10 rat lesion; human levels as reported"}'
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
    'A-layer full text; Full text PMC; Fig. 1-7',
    'Tracker experiment M3A-P006-E001',
    'Extracted details: Exosomes reduced IBA1-positive GSDMD/Caspase-1 pyroptosis, preserved myelin, increased NF200 and NeuN outcomes, and improved BMS, swimming, footprint, and MEP recovery. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "iPSC-NSC exosomes administered immediately after SCI; BMS, swimming, footprint, MEP, myelin, and axon outcomes through 28 dpi; pyroptosis assessed at 7 dpi", "control_type": "Sham, SCI plus PBS, and SCI plus exosome groups", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "5 g rod dropped from 6.5 cm", "injury_model": "T8 impact SCI", "injury_severity": "Contusion as reported", "intervention_type": "Intrathecal iPSC-NSC-derived exosomes at 20 ug/uL", "methods_summary": "Exosomes reduced IBA1-positive GSDMD/Caspase-1 pyroptosis, preserved myelin, increased NF200 and NeuN outcomes, and improved BMS, swimming, footprint, and MEP recovery.", "observation_tracker_ids": ["M3B-O006"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M3A-P006-E001", "source_paper_tracker_id": "M3A-P006", "species": "Mouse", "strain": "C57BL/6", "tracker_key": "M3A-P006::M3A-P006-E001", "vertebral_level": "T8"}'
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
    'A-layer full text; Full text PMC; Fig. 8 and rescue assays',
    'Tracker experiment M3A-P006-E002',
    'Extracted details: let-7b-5p was enriched in exosomes, directly bound the LRIG3 3-prime UTR, and reduced pyroptosis; LRIG3 overexpression reversed protection while LRIG3 knockdown rescued the let-7b-5p loss condition. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "let-7b-5p gain/loss, LRIG3 rescue, luciferase, RNA-ChIP, and exosome treatment", "control_type": "PBS, miR-negative-control, let-7b-5p knockdown/overexpression, and LRIG3 rescue controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "N/A for cell culture; T8 impact for in vivo arm", "injury_model": "LPS plus ATP pyroptosis assay; SCI context for exosome validation", "injury_severity": "N/A for cell culture; contusion as reported in vivo", "intervention_type": "Exosomal let-7b-5p targeting LRIG3", "methods_summary": "let-7b-5p was enriched in exosomes, directly bound the LRIG3 3-prime UTR, and reduced pyroptosis; LRIG3 overexpression reversed protection while LRIG3 knockdown rescued the let-7b-5p loss condition.", "observation_tracker_ids": ["M3B-O053"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M3A-P006-E002", "source_paper_tracker_id": "M3A-P006", "species": "Mouse BV2 cells plus SCI mice", "strain": "BV2 microglia; iPSC-NSCs", "tracker_key": "M3A-P006::M3A-P006-E002", "vertebral_level": "T8 in vivo"}'
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
    'Extracted details: Primary intervention or mechanism experiment for Metabolic reprogramming through histone lactylation in microglia and macrophages recruits CD8+ T lymphocytes and aggravates spinal cord injury; first-pass row captures lactylation / microglia-macrophage-t cell axis in rodent model context at abstract/source-title level. Extraction status: YES (abstract-level)',
    '{"chronicity_dpi_wpi": "UNKNOWN", "control_type": "Injury / vehicle / wild-type / comparator as reported", "experiment_extracted": "YES (abstract-level)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "UNKNOWN", "intervention_type": "Lactylation / microglia-macrophage-T cell axis", "methods_summary": "Primary intervention or mechanism experiment for Metabolic reprogramming through histone lactylation in microglia and macrophages recruits CD8+ T lymphocytes and aggravates spinal cord injury; first-pass row captures lactylation / microglia-macrophage-t cell axis in rodent model context at abstract/source-title level.", "observation_tracker_ids": ["M3B-O007"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M3A-P007-E001", "source_paper_tracker_id": "M3A-P007", "species": "Rodent model context", "strain": "UNKNOWN", "tracker_key": "M3A-P007::M3A-P007-E001", "vertebral_level": "UNKNOWN"}'
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
    'Extracted details: Outcome/mechanistic validation row for Metabolic reprogramming through histone lactylation in microglia and macrophages recruits CD8+ T lymphocytes and aggravates spinal cord injury; first-pass row captures lactylation / microglia-macrophage-t cell axis in rodent model context at abstract/source-title level. Extraction status: YES (abstract-level)',
    '{"chronicity_dpi_wpi": "UNKNOWN", "control_type": "Comparator/control arm as reported", "experiment_extracted": "YES (abstract-level)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "UNKNOWN", "intervention_type": "Mechanistic outcome assessment after lactylation / microglia-macrophage-t cell axis", "methods_summary": "Outcome/mechanistic validation row for Metabolic reprogramming through histone lactylation in microglia and macrophages recruits CD8+ T lymphocytes and aggravates spinal cord injury; first-pass row captures lactylation / microglia-macrophage-t cell axis in rodent model context at abstract/source-title level.", "observation_tracker_ids": ["M3B-O054"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M3A-P007-E002", "source_paper_tracker_id": "M3A-P007", "species": "Rodent model context", "strain": "UNKNOWN", "tracker_key": "M3A-P007::M3A-P007-E002", "vertebral_level": "UNKNOWN"}'
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
    'A-layer full text; Full text PMC',
    'Tracker experiment M3A-P008-E001',
    'Extracted details: L-P reduced lesion lipid accumulation and lipid droplets in Iba1+ cells, shifted microglia/macrophages from CD86+ M1-like toward CD163+ M2-like states, activated AMPK-PGC1alpha-PPARgamma, reduced CD36 and PLIN2, suppressed inflammatory signaling, and improved BMS and locomotor outcomes. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "1-28 dpi; L-P daily for 7 d", "control_type": "Sham, SCI vehicle, exercise, and 10 or 30 mg/kg L-P comparators", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Reward Spinal Cord Impactor; 1.5 m/s, 0.6 mm", "injury_model": "T9 contusion SCI", "injury_severity": "Moderate contusion", "intervention_type": "N-lactoyl-phenylalanine 20 mg/kg tail vein immediately after injury and daily for 7 d", "methods_summary": "L-P reduced lesion lipid accumulation and lipid droplets in Iba1+ cells, shifted microglia/macrophages from CD86+ M1-like toward CD163+ M2-like states, activated AMPK-PGC1alpha-PPARgamma, reduced CD36 and PLIN2, suppressed inflammatory signaling, and improved BMS and locomotor outcomes.", "observation_tracker_ids": ["M3B-O008"], "sex": "Male and female", "source_experiment_tracker_id": "M3A-P008-E001", "source_paper_tracker_id": "M3A-P008", "species": "Mouse SCI model", "strain": "C57BL/6; AMPK flox and myeloid Cre lines for validation", "tracker_key": "M3A-P008::M3A-P008-E001", "vertebral_level": "T9"}'
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
    'A-layer full text; Full text PMC',
    'Tracker experiment M3A-P008-E002',
    'Extracted details: L-P increased AMPK phosphorylation and anti-inflammatory markers, but the AMPK conditional experiments were used to test pathway dependence rather than to establish a separate behavioral treatment effect. BV2 assays showed reduced lipid-droplet and inflammatory responses with M2-associated marker induction. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "1-28 dpi; pathway validation after L-P", "control_type": "SCI vehicle or L-P; AMPK conditional deletion and Cre-negative controls; untreated or LPS BV2 controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Reward Spinal Cord Impactor; 1.5 m/s, 0.6 mm; in vitro LPS challenge", "injury_model": "T9 contusion SCI plus LPS-stimulated BV2 model", "injury_severity": "Moderate contusion; in vitro inflammatory stimulation", "intervention_type": "L-P 20 mg/kg daily for 7 d with AMPK deletion or microglial lineage tracing; in vitro L-P and LPS", "methods_summary": "L-P increased AMPK phosphorylation and anti-inflammatory markers, but the AMPK conditional experiments were used to test pathway dependence rather than to establish a separate behavioral treatment effect. BV2 assays showed reduced lipid-droplet and inflammatory responses with M2-associated marker induction.", "observation_tracker_ids": ["M3B-O055"], "sex": "Male and female", "source_experiment_tracker_id": "M3A-P008-E002", "source_paper_tracker_id": "M3A-P008", "species": "Mouse SCI model plus microglia/macrophage validation", "strain": "AMPK flox; Tmem119CreERT and Cx3cr1-iCre lines", "tracker_key": "M3A-P008::M3A-P008-E002", "vertebral_level": "T9"}'
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
    'Extracted details: Primary intervention or mechanism experiment for Naringenin alleviates spinal cord injury by ameliorating macrophage/microglia autophagy via progranulin stabilisation.; first-pass row captures macrophage/microglia autophagy and polarization in rodent sci model context at abstract/source-title level. Extraction status: YES (abstract-level)',
    '{"chronicity_dpi_wpi": "UNKNOWN", "control_type": "Injury / vehicle / wild-type / comparator as reported", "experiment_extracted": "YES (abstract-level)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "UNKNOWN", "intervention_type": "Macrophage/microglia autophagy and polarization", "methods_summary": "Primary intervention or mechanism experiment for Naringenin alleviates spinal cord injury by ameliorating macrophage/microglia autophagy via progranulin stabilisation.; first-pass row captures macrophage/microglia autophagy and polarization in rodent sci model context at abstract/source-title level.", "observation_tracker_ids": ["M3B-O009"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M3A-P009-E001", "source_paper_tracker_id": "M3A-P009", "species": "Rodent SCI model context", "strain": "UNKNOWN", "tracker_key": "M3A-P009::M3A-P009-E001", "vertebral_level": "UNKNOWN"}'
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
    'Extracted details: Outcome/mechanistic validation row for Naringenin alleviates spinal cord injury by ameliorating macrophage/microglia autophagy via progranulin stabilisation.; first-pass row captures macrophage/microglia autophagy and polarization in rodent sci model context at abstract/source-title level. Extraction status: YES (abstract-level)',
    '{"chronicity_dpi_wpi": "UNKNOWN", "control_type": "Comparator/control arm as reported", "experiment_extracted": "YES (abstract-level)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "UNKNOWN", "intervention_type": "Mechanistic outcome assessment after macrophage/microglia autophagy and polarization", "methods_summary": "Outcome/mechanistic validation row for Naringenin alleviates spinal cord injury by ameliorating macrophage/microglia autophagy via progranulin stabilisation.; first-pass row captures macrophage/microglia autophagy and polarization in rodent sci model context at abstract/source-title level.", "observation_tracker_ids": ["M3B-O056"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M3A-P009-E002", "source_paper_tracker_id": "M3A-P009", "species": "Rodent SCI model context", "strain": "UNKNOWN", "tracker_key": "M3A-P009::M3A-P009-E002", "vertebral_level": "UNKNOWN"}'
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
    'A-layer full text; Full text PMC; Fig. 3-5',
    'Tracker experiment M3A-P010-E001',
    'Extracted details: DSDH reduced iNOS and increased CD206/Arg1, improved BBB to about 6.2 at 28 days versus about 2.5-2.7 in untreated/non-DSDH groups, improved footprint and MEPs, reduced lesion cavity and GFAP, and increased Tuj1, neurofilament, and synapsin-I signals. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "BBB, footprint, MEP, bladder, histology, and polarization assays at 7 and 28 days", "control_type": "Sham, untreated SCI, and non-programmed dual-drug hydrogel controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Forceps, 3-mm width, fully closed for 10 s; 50 microliters hydrogel injected in situ containing 300 micrograms minocycline and 500 ng IL-4", "injury_model": "T9 complete spinal cord crush", "injury_severity": "Complete crush", "intervention_type": "Dual-drug sequential delivery hydrogel (DSDH) with minocycline-loaded fucose nanoparticles and IL-4-biotin/streptavidin complexes", "methods_summary": "DSDH reduced iNOS and increased CD206/Arg1, improved BBB to about 6.2 at 28 days versus about 2.5-2.7 in untreated/non-DSDH groups, improved footprint and MEPs, reduced lesion cavity and GFAP, and increased Tuj1, neurofilament, and synapsin-I signals.", "observation_tracker_ids": ["M3B-O010"], "sex": "Female", "source_experiment_tracker_id": "M3A-P010-E001", "source_paper_tracker_id": "M3A-P010", "species": "Rat", "strain": "Female Sprague-Dawley rats, 190-210 g", "tracker_key": "M3A-P010::M3A-P010-E001", "vertebral_level": "T9"}'
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
    'A-layer full text; Full text PMC; release and timing mechanism',
    'Tracker experiment M3A-P010-E002',
    'Extracted details: DSDH matched the intended inflammatory sequence: early iNOS suppression and later CD206/p-STAT6 increase, with less cytotoxicity than burst-release non-DSDH. The study did not include MH-only, IL-4-only, or empty-hydrogel in vivo controls, so synergy and component-specific necessity remain unresolved. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "BV2 assays 24 h; rat readouts 7 and 28 days", "control_type": "HAG, minocycline-HAG, IL-4-HAG, and non-DSDH controls as reported", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "DSDH released minocycline earlier (about 42.7% by 24 h, 77.7% by 7 d) and IL-4 gradually (about 20.2% by 24 h, 64.4% by 30 d); non-DSDH released both rapidly", "injury_model": "In vitro microglial polarization and T9 crush SCI", "injury_severity": "LPS-induced in vitro assay and complete crush in vivo", "intervention_type": "Programmed early M1 suppression followed by later IL-4-driven M2 support", "methods_summary": "DSDH matched the intended inflammatory sequence: early iNOS suppression and later CD206/p-STAT6 increase, with less cytotoxicity than burst-release non-DSDH. The study did not include MH-only, IL-4-only, or empty-hydrogel in vivo controls, so synergy and component-specific necessity remain unresolved.", "observation_tracker_ids": ["M3B-O057"], "sex": "Female in vivo; not applicable in vitro", "source_experiment_tracker_id": "M3A-P010-E002", "source_paper_tracker_id": "M3A-P010", "species": "Rat and BV2 cells", "strain": "Female SD rats; BV2 LPS polarization assays", "tracker_key": "M3A-P010::M3A-P010-E002", "vertebral_level": "T9 in vivo"}'
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
    'Extracted details: Primary intervention or mechanism experiment for Microenvironment Self-Adaptive Nanomedicine Promotes Spinal Cord Repair by Suppressing Inflammation Cascade and Neural Apoptosis.; first-pass row captures immune-modifying nanomedicine in rodent sci model context at abstract/source-title level. Extraction status: YES (abstract-level)',
    '{"chronicity_dpi_wpi": "UNKNOWN", "control_type": "Injury / vehicle / wild-type / comparator as reported", "experiment_extracted": "YES (abstract-level)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "UNKNOWN", "intervention_type": "Immune-modifying nanomedicine", "methods_summary": "Primary intervention or mechanism experiment for Microenvironment Self-Adaptive Nanomedicine Promotes Spinal Cord Repair by Suppressing Inflammation Cascade and Neural Apoptosis.; first-pass row captures immune-modifying nanomedicine in rodent sci model context at abstract/source-title level.", "observation_tracker_ids": ["M3B-O011"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M3A-P011-E001", "source_paper_tracker_id": "M3A-P011", "species": "Rodent SCI model context", "strain": "UNKNOWN", "tracker_key": "M3A-P011::M3A-P011-E001", "vertebral_level": "UNKNOWN"}'
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
    'Extracted details: Outcome/mechanistic validation row for Microenvironment Self-Adaptive Nanomedicine Promotes Spinal Cord Repair by Suppressing Inflammation Cascade and Neural Apoptosis.; first-pass row captures immune-modifying nanomedicine in rodent sci model context at abstract/source-title level. Extraction status: YES (abstract-level)',
    '{"chronicity_dpi_wpi": "UNKNOWN", "control_type": "Comparator/control arm as reported", "experiment_extracted": "YES (abstract-level)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "UNKNOWN", "intervention_type": "Mechanistic outcome assessment after immune-modifying nanomedicine", "methods_summary": "Outcome/mechanistic validation row for Microenvironment Self-Adaptive Nanomedicine Promotes Spinal Cord Repair by Suppressing Inflammation Cascade and Neural Apoptosis.; first-pass row captures immune-modifying nanomedicine in rodent sci model context at abstract/source-title level.", "observation_tracker_ids": ["M3B-O058"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M3A-P011-E002", "source_paper_tracker_id": "M3A-P011", "species": "Rodent SCI model context", "strain": "UNKNOWN", "tracker_key": "M3A-P011::M3A-P011-E002", "vertebral_level": "UNKNOWN"}'
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
    'Extracted details: Primary intervention or mechanism experiment for Farrerol confers neuroprotection in spinal cord injury by regulating macrophages/microglia polarization through the JAK2/STAT3 pathway.; first-pass row captures macrophage/microglia polarization signaling in rodent sci model context at abstract/source-title level. Extraction status: YES (abstract-level)',
    '{"chronicity_dpi_wpi": "UNKNOWN", "control_type": "Injury / vehicle / wild-type / comparator as reported", "experiment_extracted": "YES (abstract-level)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "UNKNOWN", "intervention_type": "Macrophage/microglia polarization signaling", "methods_summary": "Primary intervention or mechanism experiment for Farrerol confers neuroprotection in spinal cord injury by regulating macrophages/microglia polarization through the JAK2/STAT3 pathway.; first-pass row captures macrophage/microglia polarization signaling in rodent sci model context at abstract/source-title level.", "observation_tracker_ids": ["M3B-O012"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M3A-P012-E001", "source_paper_tracker_id": "M3A-P012", "species": "Rodent SCI model context", "strain": "UNKNOWN", "tracker_key": "M3A-P012::M3A-P012-E001", "vertebral_level": "UNKNOWN"}'
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
    'Extracted details: Outcome/mechanistic validation row for Farrerol confers neuroprotection in spinal cord injury by regulating macrophages/microglia polarization through the JAK2/STAT3 pathway.; first-pass row captures macrophage/microglia polarization signaling in rodent sci model context at abstract/source-title level. Extraction status: YES (abstract-level)',
    '{"chronicity_dpi_wpi": "UNKNOWN", "control_type": "Comparator/control arm as reported", "experiment_extracted": "YES (abstract-level)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "UNKNOWN", "intervention_type": "Mechanistic outcome assessment after macrophage/microglia polarization signaling", "methods_summary": "Outcome/mechanistic validation row for Farrerol confers neuroprotection in spinal cord injury by regulating macrophages/microglia polarization through the JAK2/STAT3 pathway.; first-pass row captures macrophage/microglia polarization signaling in rodent sci model context at abstract/source-title level.", "observation_tracker_ids": ["M3B-O059"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M3A-P012-E002", "source_paper_tracker_id": "M3A-P012", "species": "Rodent SCI model context", "strain": "UNKNOWN", "tracker_key": "M3A-P012::M3A-P012-E002", "vertebral_level": "UNKNOWN"}'
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
    'Extracted details: Primary intervention or mechanism experiment for GDF11 alleviates spinal cord injury in rats by modulating microglia polarization through Smad2/3 and MAPK/NFkappaB signaling pathways.; first-pass row captures macrophage/microglia polarization signaling in rat sci model at abstract/source-title level. Extraction status: YES (abstract-level)',
    '{"chronicity_dpi_wpi": "UNKNOWN", "control_type": "Injury / vehicle / wild-type / comparator as reported", "experiment_extracted": "YES (abstract-level)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "UNKNOWN", "intervention_type": "Macrophage/microglia polarization signaling", "methods_summary": "Primary intervention or mechanism experiment for GDF11 alleviates spinal cord injury in rats by modulating microglia polarization through Smad2/3 and MAPK/NFkappaB signaling pathways.; first-pass row captures macrophage/microglia polarization signaling in rat sci model at abstract/source-title level.", "observation_tracker_ids": ["M3B-O013"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M3A-P013-E001", "source_paper_tracker_id": "M3A-P013", "species": "Rat SCI model", "strain": "UNKNOWN", "tracker_key": "M3A-P013::M3A-P013-E001", "vertebral_level": "UNKNOWN"}'
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
    'Extracted details: Outcome/mechanistic validation row for GDF11 alleviates spinal cord injury in rats by modulating microglia polarization through Smad2/3 and MAPK/NFkappaB signaling pathways.; first-pass row captures macrophage/microglia polarization signaling in rat sci model at abstract/source-title level. Extraction status: YES (abstract-level)',
    '{"chronicity_dpi_wpi": "UNKNOWN", "control_type": "Comparator/control arm as reported", "experiment_extracted": "YES (abstract-level)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "UNKNOWN", "intervention_type": "Mechanistic outcome assessment after macrophage/microglia polarization signaling", "methods_summary": "Outcome/mechanistic validation row for GDF11 alleviates spinal cord injury in rats by modulating microglia polarization through Smad2/3 and MAPK/NFkappaB signaling pathways.; first-pass row captures macrophage/microglia polarization signaling in rat sci model at abstract/source-title level.", "observation_tracker_ids": ["M3B-O060"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M3A-P013-E002", "source_paper_tracker_id": "M3A-P013", "species": "Rat SCI model", "strain": "UNKNOWN", "tracker_key": "M3A-P013::M3A-P013-E002", "vertebral_level": "UNKNOWN"}'
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
    'Extracted details: Primary intervention or mechanism experiment for Fisetin Promotes Functional Recovery after Spinal Cord Injury by Inhibiting Microglia/Macrophage M1 Polarization and JAK2/STAT3 Signaling Pathway.; first-pass row captures macrophage/microglia polarization signaling in rodent sci model context at abstract/source-title level. Extraction status: YES (abstract-level)',
    '{"chronicity_dpi_wpi": "UNKNOWN", "control_type": "Injury / vehicle / wild-type / comparator as reported", "experiment_extracted": "YES (abstract-level)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "UNKNOWN", "intervention_type": "Macrophage/microglia polarization signaling", "methods_summary": "Primary intervention or mechanism experiment for Fisetin Promotes Functional Recovery after Spinal Cord Injury by Inhibiting Microglia/Macrophage M1 Polarization and JAK2/STAT3 Signaling Pathway.; first-pass row captures macrophage/microglia polarization signaling in rodent sci model context at abstract/source-title level.", "observation_tracker_ids": ["M3B-O014"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M3A-P014-E001", "source_paper_tracker_id": "M3A-P014", "species": "Rodent SCI model context", "strain": "UNKNOWN", "tracker_key": "M3A-P014::M3A-P014-E001", "vertebral_level": "UNKNOWN"}'
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
    'Extracted details: Outcome/mechanistic validation row for Fisetin Promotes Functional Recovery after Spinal Cord Injury by Inhibiting Microglia/Macrophage M1 Polarization and JAK2/STAT3 Signaling Pathway.; first-pass row captures macrophage/microglia polarization signaling in rodent sci model context at abstract/source-title level. Extraction status: YES (abstract-level)',
    '{"chronicity_dpi_wpi": "UNKNOWN", "control_type": "Comparator/control arm as reported", "experiment_extracted": "YES (abstract-level)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "UNKNOWN", "intervention_type": "Mechanistic outcome assessment after macrophage/microglia polarization signaling", "methods_summary": "Outcome/mechanistic validation row for Fisetin Promotes Functional Recovery after Spinal Cord Injury by Inhibiting Microglia/Macrophage M1 Polarization and JAK2/STAT3 Signaling Pathway.; first-pass row captures macrophage/microglia polarization signaling in rodent sci model context at abstract/source-title level.", "observation_tracker_ids": ["M3B-O061"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M3A-P014-E002", "source_paper_tracker_id": "M3A-P014", "species": "Rodent SCI model context", "strain": "UNKNOWN", "tracker_key": "M3A-P014::M3A-P014-E002", "vertebral_level": "UNKNOWN"}'
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
    'A-layer full text; Full text PMC',
    'Tracker experiment M3A-P015-E001',
    'Extracted details: ATL-III improved BBB scores from 14-42 dpi, reduced grid-walk errors, improved footprint patterns, reduced lesion area and myelin disruption, and increased surviving neurons. It reduced M1-associated iNOS, TNF-alpha, IL-1beta and IL-6 while increasing Arg1 and IL-10 and shifting spinal microglia/macrophages toward an M2-associated phenotype. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "3-42 dpi; daily treatment from 3 h after injury", "control_type": "Sham and untreated SCI controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Infinite Horizon impactor; 2.5 mm rod, 120 kdyn", "injury_model": "T9 moderate contusion SCI", "injury_severity": "Moderate contusion", "intervention_type": "Atractylenolide III 5 mg/kg by gavage 3 h after surgery and daily until sacrifice", "methods_summary": "ATL-III improved BBB scores from 14-42 dpi, reduced grid-walk errors, improved footprint patterns, reduced lesion area and myelin disruption, and increased surviving neurons. It reduced M1-associated iNOS, TNF-alpha, IL-1beta and IL-6 while increasing Arg1 and IL-10 and shifting spinal microglia/macrophages toward an M2-associated phenotype.", "observation_tracker_ids": ["M3B-O015"], "sex": "Female", "source_experiment_tracker_id": "M3A-P015-E001", "source_paper_tracker_id": "M3A-P015", "species": "Rat SCI model", "strain": "Sprague-Dawley", "tracker_key": "M3A-P015::M3A-P015-E001", "vertebral_level": "T9"}'
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
    'A-layer full text; Full text PMC',
    'Tracker experiment M3A-P015-E002',
    'Extracted details: ATL-III was not toxic to BV2 cells and dose-dependently reduced LPS-induced iNOS, TNF-alpha, IL-1beta and IL-6 while increasing Arg1 and IL-10. In vivo and in vitro it reduced NF-kB IκBalpha/p65 and JNK/p38 phosphorylation, increased Akt phosphorylation, and did not materially change ERK phosphorylation. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "24 h LPS assay; 7 dpi pathway readout; 14-42 dpi behavior", "control_type": "Vehicle, LPS, and ATL-III dose controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Not applicable in vitro; Infinite Horizon impactor in vivo", "injury_model": "LPS-stimulated microglial model plus rat T9 contusion", "injury_severity": "LPS inflammatory stimulation; moderate contusion in vivo", "intervention_type": "ATL-III 1, 10, or 100 uM for 1 h before 100 ng/ml LPS; rat ATL-III treatment as above", "methods_summary": "ATL-III was not toxic to BV2 cells and dose-dependently reduced LPS-induced iNOS, TNF-alpha, IL-1beta and IL-6 while increasing Arg1 and IL-10. In vivo and in vitro it reduced NF-kB I\u03baBalpha/p65 and JNK/p38 phosphorylation, increased Akt phosphorylation, and did not materially change ERK phosphorylation.", "observation_tracker_ids": ["M3B-O062"], "sex": "Not applicable in vitro", "source_experiment_tracker_id": "M3A-P015-E002", "source_paper_tracker_id": "M3A-P015", "species": "BV2 microglial culture with rat SCI pathway validation", "strain": "BV2 cell line; rat tissue for in vivo validation", "tracker_key": "M3A-P015::M3A-P015-E002", "vertebral_level": "T9 for in vivo validation"}'
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
    'A-layer full text; Full text PMC; engineering, secretion, and conditioned-medium assays',
    'Tracker experiment M3A-P016-E001',
    'Extracted details: Electroporation produced viable engineered macrophages expressing ANXA1, GDNF, and CTGF without a marked CD86/CD206 shift and sustained secretion through day 14. Conditioned medium protected PC12 cells and DRG explants from oxidative-stress injury and promoted neurite outgrowth, supporting a paracrine neuroprotective/regenerative effect rather than proving contact-dependent action. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Protein expression/viability and secretion days 1-14; PC12 and DRG neurite assays after oxidative stress", "control_type": "Unmodified macrophages, oxidative-stress-only cells, and macrophage-conditioned medium controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Not applicable", "injury_model": "CCR2-enriched macrophages were flow-sorted after thioglycollate plus myelin induction and electroporated at 1 x 10^6 cells with 6 micrograms total ANXA1, GDNF, and CTGF mRNA at a 1:1:1 mass ratio plus eGFP reporter; PC12 cells/DRG explants received conditioned medium after 200 micromolar H2O2", "injury_severity": "200 micromolar H2O2 for 3 h in vitro", "intervention_type": "CCR2 enrichment plus transient multimodal mRNA delivery", "methods_summary": "Electroporation produced viable engineered macrophages expressing ANXA1, GDNF, and CTGF without a marked CD86/CD206 shift and sustained secretion through day 14. Conditioned medium protected PC12 cells and DRG explants from oxidative-stress injury and promoted neurite outgrowth, supporting a paracrine neuroprotective/regenerative effect rather than proving contact-dependent action.", "observation_tracker_ids": ["M3B-O016"], "sex": "In vitro oxidative-stress and neurite-outgrowth assays", "source_experiment_tracker_id": "M3A-P016-E001", "source_paper_tracker_id": "M3A-P016", "species": "Mouse peritoneal macrophages; newborn Sprague-Dawley rat DRG and PC12 cells", "strain": "Adult donor mice; newborn rat tissue; sex not stated", "tracker_key": "M3A-P016::M3A-P016-E001", "vertebral_level": "Not applicable"}'
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
    'A-layer full text; Full text PMC; in vivo biodistribution, repair, tracing, and function',
    'Tracker experiment M3A-P016-E002',
    'Extracted details: Engineered cells accumulated more at the lesion, reduced inflammatory/scar-associated signals, increased GDNF/GFRalpha1, NF and MBP repair signals, and improved ultrastructure (g-ratio 0.77 versus 0.90 SCI and 0.86 macrophage). BDA/FB tracing and synaptophysin were higher at the lesion; BMS reached 5 versus 2, stride was 35.33 mm while controls could not walk, and MEP latency/amplitude improved to 13.46 ms/0.16 mV versus 18.02 ms/0.02 mV. These findings support partial structural and functional recovery, not complete circuit restoration. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Lesion accumulation at 30 min, 48 h, and 7 d; tissue/flow/RNA-seq at 3-8 d; BDA motor-cortex and Fast Blue sensory tracing, histology, gait, BMS, EMG, and MEP at 8 weeks", "control_type": "Saline SCI, unmodified macrophage, and sham controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Vascular clip applied for 30 s; one tail-vein infusion of 1 x 10^6 DiR-labeled engineered or unmodified macrophages in 10 microliters saline", "injury_model": "T8 contusive SCI", "injury_severity": "Clip contusion", "intervention_type": "Systemically delivered CCR2-enriched macrophages co-delivering ANXA1, GDNF, and CTGF mRNAs", "methods_summary": "Engineered cells accumulated more at the lesion, reduced inflammatory/scar-associated signals, increased GDNF/GFRalpha1, NF and MBP repair signals, and improved ultrastructure (g-ratio 0.77 versus 0.90 SCI and 0.86 macrophage). BDA/FB tracing and synaptophysin were higher at the lesion; BMS reached 5 versus 2, stride was 35.33 mm while controls could not walk, and MEP latency/amplitude improved to 13.46 ms/0.16 mV versus 18.02 ms/0.02 mV. These findings support partial structural and functional recovery, not complete circuit restoration.", "observation_tracker_ids": ["M3B-O063"], "sex": "Female", "source_experiment_tracker_id": "M3A-P016-E002", "source_paper_tracker_id": "M3A-P016", "species": "Mouse", "strain": "C57BL/6, 8 weeks, 18-22 g; total n=98", "tracker_key": "M3A-P016::M3A-P016-E002", "vertebral_level": "T8"}'
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
    'A-layer full text; Full text PMC; Fig. 1-2',
    'Tracker experiment M3A-P017-E001',
    'Extracted details: Delayed PLX5622 did not change elevated-plus-maze open-arm time, light-dark entries, open-field exploration, or locomotor activity relative to SCI controls. The result argues against a detectable anxiety or locomotor effect under this dosing and partial-depletion regimen, but does not establish that microglia are behaviorally irrelevant. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "PLX5622 started 7 days post-injury and continued for 28 days; anxiety/locomotor tests at baseline and treatment weeks 2 and 4", "control_type": "Standard chow control, n=7 per group; blinded behavioral scoring", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Custom laser-cut blade, 1.4-mm depth marker", "injury_model": "C4 unilateral dorsolateral-quadrant transection", "injury_severity": "Dorsolateral quadrant transection", "intervention_type": "PLX5622 1200 ppm chow during the subacute phase", "methods_summary": "Delayed PLX5622 did not change elevated-plus-maze open-arm time, light-dark entries, open-field exploration, or locomotor activity relative to SCI controls. The result argues against a detectable anxiety or locomotor effect under this dosing and partial-depletion regimen, but does not establish that microglia are behaviorally irrelevant.", "observation_tracker_ids": ["M3B-O017"], "sex": "Female", "source_experiment_tracker_id": "M3A-P017-E001", "source_paper_tracker_id": "M3A-P017", "species": "Rat", "strain": "Lewis", "tracker_key": "M3A-P017::M3A-P017-E001", "vertebral_level": "C4"}'
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
    'A-layer full text; Full text PMC; Fig. 3-6',
    'Tracker experiment M3A-P017-E002',
    'Extracted details: PLX5622 reduced Iba1+ microglia/macrophage counts by about 50-60% across CNS regions and reduced lesion-core counts by 52%, but did not change lesion size or microglial morphology. The astrocytic scar was thinner (58.5 versus 91.3 micrometers), while liver Kupffer cells fell by about 78%, demonstrating incomplete CNS depletion and substantial peripheral macrophage effects. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Tissue collected after 28-day diet; brain, cervical cord, lesion core, and liver assessed", "control_type": "Standard chow control, n=7 per group", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Custom laser-cut blade, 1.4-mm depth marker", "injury_model": "C4 unilateral dorsolateral-quadrant transection", "injury_severity": "Dorsolateral quadrant transection", "intervention_type": "PLX5622 1200 ppm chow", "methods_summary": "PLX5622 reduced Iba1+ microglia/macrophage counts by about 50-60% across CNS regions and reduced lesion-core counts by 52%, but did not change lesion size or microglial morphology. The astrocytic scar was thinner (58.5 versus 91.3 micrometers), while liver Kupffer cells fell by about 78%, demonstrating incomplete CNS depletion and substantial peripheral macrophage effects.", "observation_tracker_ids": ["M3B-O064"], "sex": "Female", "source_experiment_tracker_id": "M3A-P017-E002", "source_paper_tracker_id": "M3A-P017", "species": "Rat", "strain": "Lewis", "tracker_key": "M3A-P017::M3A-P017-E002", "vertebral_level": "C4"}'
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
    'Extracted details: Primary intervention or mechanism experiment for Nanoparticles loaded with a CSF1R antagonist selectively depletes microglial cells and modulates inflammation in spinal cord injury.; first-pass row captures microglial depletion / csf1r modulation in rat sci model at abstract/source-title level. Extraction status: YES (abstract-level)',
    '{"chronicity_dpi_wpi": "UNKNOWN", "control_type": "Injury / vehicle / wild-type / comparator as reported", "experiment_extracted": "YES (abstract-level)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "UNKNOWN", "intervention_type": "Microglial depletion / CSF1R modulation", "methods_summary": "Primary intervention or mechanism experiment for Nanoparticles loaded with a CSF1R antagonist selectively depletes microglial cells and modulates inflammation in spinal cord injury.; first-pass row captures microglial depletion / csf1r modulation in rat sci model at abstract/source-title level.", "observation_tracker_ids": ["M3B-O018"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M3A-P018-E001", "source_paper_tracker_id": "M3A-P018", "species": "Rat SCI model", "strain": "UNKNOWN", "tracker_key": "M3A-P018::M3A-P018-E001", "vertebral_level": "UNKNOWN"}'
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
    'Extracted details: Outcome/mechanistic validation row for Nanoparticles loaded with a CSF1R antagonist selectively depletes microglial cells and modulates inflammation in spinal cord injury.; first-pass row captures microglial depletion / csf1r modulation in rat sci model at abstract/source-title level. Extraction status: YES (abstract-level)',
    '{"chronicity_dpi_wpi": "UNKNOWN", "control_type": "Comparator/control arm as reported", "experiment_extracted": "YES (abstract-level)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "UNKNOWN", "intervention_type": "Mechanistic outcome assessment after microglial depletion / csf1r modulation", "methods_summary": "Outcome/mechanistic validation row for Nanoparticles loaded with a CSF1R antagonist selectively depletes microglial cells and modulates inflammation in spinal cord injury.; first-pass row captures microglial depletion / csf1r modulation in rat sci model at abstract/source-title level.", "observation_tracker_ids": ["M3B-O065"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M3A-P018-E002", "source_paper_tracker_id": "M3A-P018", "species": "Rat SCI model", "strain": "UNKNOWN", "tracker_key": "M3A-P018::M3A-P018-E002", "vertebral_level": "UNKNOWN"}'
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
    'Extracted details: Primary intervention or mechanism experiment for Identification of repopulated microglia-associated genes in microglia depleted/repopulated mice after spinal cord injury.; first-pass row captures microglial depletion / csf1r modulation in mouse sci model at abstract/source-title level. Extraction status: YES (abstract-level)',
    '{"chronicity_dpi_wpi": "UNKNOWN", "control_type": "Injury / vehicle / wild-type / comparator as reported", "experiment_extracted": "YES (abstract-level)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "UNKNOWN", "intervention_type": "Microglial depletion / CSF1R modulation", "methods_summary": "Primary intervention or mechanism experiment for Identification of repopulated microglia-associated genes in microglia depleted/repopulated mice after spinal cord injury.; first-pass row captures microglial depletion / csf1r modulation in mouse sci model at abstract/source-title level.", "observation_tracker_ids": ["M3B-O019"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M3A-P019-E001", "source_paper_tracker_id": "M3A-P019", "species": "Mouse SCI model", "strain": "UNKNOWN", "tracker_key": "M3A-P019::M3A-P019-E001", "vertebral_level": "UNKNOWN"}'
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
    'Extracted details: Outcome/mechanistic validation row for Identification of repopulated microglia-associated genes in microglia depleted/repopulated mice after spinal cord injury.; first-pass row captures microglial depletion / csf1r modulation in mouse sci model at abstract/source-title level. Extraction status: YES (abstract-level)',
    '{"chronicity_dpi_wpi": "UNKNOWN", "control_type": "Comparator/control arm as reported", "experiment_extracted": "YES (abstract-level)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "UNKNOWN", "intervention_type": "Mechanistic outcome assessment after microglial depletion / csf1r modulation", "methods_summary": "Outcome/mechanistic validation row for Identification of repopulated microglia-associated genes in microglia depleted/repopulated mice after spinal cord injury.; first-pass row captures microglial depletion / csf1r modulation in mouse sci model at abstract/source-title level.", "observation_tracker_ids": ["M3B-O066"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M3A-P019-E002", "source_paper_tracker_id": "M3A-P019", "species": "Mouse SCI model", "strain": "UNKNOWN", "tracker_key": "M3A-P019::M3A-P019-E002", "vertebral_level": "UNKNOWN"}'
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
    'A-layer full text; Full text PMC',
    'Tracker experiment M3A-P020-E001',
    'Extracted details: Chronic PLX depleted Iba1+ microglia/macrophages and reduced inflammatory transcriptional signatures. Axon density within the lesion increased after 14 d PLX, supporting sustained chronic inflammation as a barrier to regeneration of selected axon populations. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Chronic 7-13 weeks post-SCI", "control_type": "Vehicle or normal diet controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Fine-tipped forceps closed around cord for 8 s", "injury_model": "Complete T9 spinal crush", "injury_severity": "Complete crush", "intervention_type": "PLX5622 1,200 ppm chow for 9, 14, or 21 d beginning 7-11 weeks after injury", "methods_summary": "Chronic PLX depleted Iba1+ microglia/macrophages and reduced inflammatory transcriptional signatures. Axon density within the lesion increased after 14 d PLX, supporting sustained chronic inflammation as a barrier to regeneration of selected axon populations.", "observation_tracker_ids": ["M3B-O020"], "sex": "Female", "source_experiment_tracker_id": "M3A-P020-E001", "source_paper_tracker_id": "M3A-P020", "species": "Mouse SCI model", "strain": "C57BL/6J wild type; PTEN-flox for combination study", "tracker_key": "M3A-P020::M3A-P020-E001", "vertebral_level": "T9"}'
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
    'A-layer full text; Full text PMC',
    'Tracker experiment M3A-P020-E002',
    'Extracted details: Removing PLX allowed Iba1+ cells to repopulate to predepletion densities and increased neuronal-enriched transcripts. PTEN-KO did not increase lesion axon density beyond PLX, and the axons entering the lesion were identified mainly as CGRP+ with some 5-HT+ fibers. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "9-13 weeks post-SCI; 3 weeks repopulation after PLX removal", "control_type": "Vehicle, PTEN-KO alone, PLX plus PTEN-KO, and repopulation groups", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Fine-tipped forceps closed around cord for 8 s; retrograde AAV injection near lesion", "injury_model": "Complete T9 spinal crush", "injury_severity": "Complete crush", "intervention_type": "PLX 1,200 ppm for 14-28 d followed by 3 weeks off diet; retrograde AAV PTEN-KO at 8 weeks post-SCI", "methods_summary": "Removing PLX allowed Iba1+ cells to repopulate to predepletion densities and increased neuronal-enriched transcripts. PTEN-KO did not increase lesion axon density beyond PLX, and the axons entering the lesion were identified mainly as CGRP+ with some 5-HT+ fibers.", "observation_tracker_ids": ["M3B-O067"], "sex": "Female", "source_experiment_tracker_id": "M3A-P020-E002", "source_paper_tracker_id": "M3A-P020", "species": "Mouse chronic SCI model with repopulation and PTEN-KO validation", "strain": "C57BL/6J wild type and PTEN-flox", "tracker_key": "M3A-P020::M3A-P020-E002", "vertebral_level": "T9"}'
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
    'Extracted details: Primary intervention or mechanism experiment for Depleting non-resolving neuroinflammation in chronic spinal cord injury attenuates thermal hypersensitivity.; first-pass row captures microglial depletion / csf1r modulation in rat sci model at abstract/source-title level. Extraction status: YES (abstract-level)',
    '{"chronicity_dpi_wpi": "UNKNOWN", "control_type": "Injury / vehicle / wild-type / comparator as reported", "experiment_extracted": "YES (abstract-level)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "UNKNOWN", "intervention_type": "Microglial depletion / CSF1R modulation", "methods_summary": "Primary intervention or mechanism experiment for Depleting non-resolving neuroinflammation in chronic spinal cord injury attenuates thermal hypersensitivity.; first-pass row captures microglial depletion / csf1r modulation in rat sci model at abstract/source-title level.", "observation_tracker_ids": ["M3B-O021"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M3A-P021-E001", "source_paper_tracker_id": "M3A-P021", "species": "Rat SCI model", "strain": "UNKNOWN", "tracker_key": "M3A-P021::M3A-P021-E001", "vertebral_level": "UNKNOWN"}'
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
    'Extracted details: Outcome/mechanistic validation row for Depleting non-resolving neuroinflammation in chronic spinal cord injury attenuates thermal hypersensitivity.; first-pass row captures microglial depletion / csf1r modulation in rat sci model at abstract/source-title level. Extraction status: YES (abstract-level)',
    '{"chronicity_dpi_wpi": "UNKNOWN", "control_type": "Comparator/control arm as reported", "experiment_extracted": "YES (abstract-level)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "UNKNOWN", "intervention_type": "Mechanistic outcome assessment after microglial depletion / csf1r modulation", "methods_summary": "Outcome/mechanistic validation row for Depleting non-resolving neuroinflammation in chronic spinal cord injury attenuates thermal hypersensitivity.; first-pass row captures microglial depletion / csf1r modulation in rat sci model at abstract/source-title level.", "observation_tracker_ids": ["M3B-O068"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M3A-P021-E002", "source_paper_tracker_id": "M3A-P021", "species": "Rat SCI model", "strain": "UNKNOWN", "tracker_key": "M3A-P021::M3A-P021-E002", "vertebral_level": "UNKNOWN"}'
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
    'A-layer full text; Full text PMC',
    'Tracker experiment M3A-P022-E001',
    'Extracted details: Beta2-adrenergic agonist intervention tested after complete SCI, with lesion microenvironment and microglial state as primary readouts. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Early post-injury treatment; chronic circuit assessment", "control_type": "SCI vehicle and sham controls; treatment comparator", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "UNKNOWN", "injury_model": "Complete SCI model", "injury_severity": "Complete SCI as reported", "intervention_type": "Early beta2-adrenergic receptor agonist treatment pharmacologically inhibited microglial activation and shifted the post-SCI scar toward a homeostatic state.", "methods_summary": "Beta2-adrenergic agonist intervention tested after complete SCI, with lesion microenvironment and microglial state as primary readouts.", "observation_tracker_ids": ["M3B-O022"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M3A-P022-E001", "source_paper_tracker_id": "M3A-P022", "species": "Mouse SCI model", "strain": "UNKNOWN", "tracker_key": "M3A-P022::M3A-P022-E001", "vertebral_level": "UNKNOWN"}'
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
    'A-layer full text; Full text PMC',
    'Tracker experiment M3A-P022-E002',
    'Extracted details: Full-text result supports a glial-scar and circuit-reconstruction mechanism; exact figure-level effect sizes remain in the source figures. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Early treatment with later recovery assessment", "control_type": "SCI vehicle and sham controls; treatment comparator", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "UNKNOWN", "injury_model": "Complete SCI model", "injury_severity": "Complete SCI as reported", "intervention_type": "Agonist treatment reduced inhibitory extracellular-matrix deposition, enabled reticulospinal tract regrowth and synaptic connectivity with thoracolumbar circuits, and improved motor recovery.", "methods_summary": "Full-text result supports a glial-scar and circuit-reconstruction mechanism; exact figure-level effect sizes remain in the source figures.", "observation_tracker_ids": ["M3B-O069"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M3A-P022-E002", "source_paper_tracker_id": "M3A-P022", "species": "Mouse SCI model", "strain": "UNKNOWN", "tracker_key": "M3A-P022::M3A-P022-E002", "vertebral_level": "UNKNOWN"}'
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
    'Extracted details: Primary intervention or mechanism experiment for SYK-dependent lipid handling in monocyte-derived macrophages governs functional recovery after spinal cord injury.; first-pass row captures immune metabolism / lipid and debris handling in mouse sci model at abstract/source-title level. Extraction status: YES (abstract-level)',
    '{"chronicity_dpi_wpi": "UNKNOWN", "control_type": "Injury / vehicle / wild-type / comparator as reported", "experiment_extracted": "YES (abstract-level)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "UNKNOWN", "intervention_type": "Immune metabolism / lipid and debris handling", "methods_summary": "Primary intervention or mechanism experiment for SYK-dependent lipid handling in monocyte-derived macrophages governs functional recovery after spinal cord injury.; first-pass row captures immune metabolism / lipid and debris handling in mouse sci model at abstract/source-title level.", "observation_tracker_ids": ["M3B-O023"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M3A-P023-E001", "source_paper_tracker_id": "M3A-P023", "species": "Mouse SCI model", "strain": "UNKNOWN", "tracker_key": "M3A-P023::M3A-P023-E001", "vertebral_level": "UNKNOWN"}'
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
    'Extracted details: Outcome/mechanistic validation row for SYK-dependent lipid handling in monocyte-derived macrophages governs functional recovery after spinal cord injury.; first-pass row captures immune metabolism / lipid and debris handling in mouse sci model at abstract/source-title level. Extraction status: YES (abstract-level)',
    '{"chronicity_dpi_wpi": "UNKNOWN", "control_type": "Comparator/control arm as reported", "experiment_extracted": "YES (abstract-level)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "UNKNOWN", "intervention_type": "Mechanistic outcome assessment after immune metabolism / lipid and debris handling", "methods_summary": "Outcome/mechanistic validation row for SYK-dependent lipid handling in monocyte-derived macrophages governs functional recovery after spinal cord injury.; first-pass row captures immune metabolism / lipid and debris handling in mouse sci model at abstract/source-title level.", "observation_tracker_ids": ["M3B-O070"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M3A-P023-E002", "source_paper_tracker_id": "M3A-P023", "species": "Mouse SCI model", "strain": "UNKNOWN", "tracker_key": "M3A-P023::M3A-P023-E002", "vertebral_level": "UNKNOWN"}'
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
    'A-layer full text; Full text PMC',
    'Tracker experiment M3A-P024-E001',
    'Extracted details: Clodronate depletion of blood-derived macrophages improved BMS, swimming, and inclined-plate performance at 28 dpi. Integrated single-cell data identified phagocytic, remodeling, and persistent lipid-laden foam-cell states, with foam cells emerging by 5 dpi and persisting into chronic SCI. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "0.5-90 dpi across integrated datasets; 28 dpi functional endpoint", "control_type": "Empty liposome and untreated SCI controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Forceps clamping for 2 s", "injury_model": "T10 forceps-clamp SCI", "injury_severity": "Moderate contusion/compression", "intervention_type": "Continuous intraperitoneal clodronate liposomes for macrophage depletion; anti-C1q antibody or IgG for synapse validation", "methods_summary": "Clodronate depletion of blood-derived macrophages improved BMS, swimming, and inclined-plate performance at 28 dpi. Integrated single-cell data identified phagocytic, remodeling, and persistent lipid-laden foam-cell states, with foam cells emerging by 5 dpi and persisting into chronic SCI.", "observation_tracker_ids": ["M3B-O024"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M3A-P024-E001", "source_paper_tracker_id": "M3A-P024", "species": "Mouse SCI model and integrated single-cell atlas", "strain": "Mouse; strain and sex not stated in extracted methods", "tracker_key": "M3A-P024::M3A-P024-E001", "vertebral_level": "T10"}'
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
    'A-layer full text; Full text PMC',
    'Tracker experiment M3A-P024-E002',
    'Extracted details: Foam-cell lipid accumulation increased C1q and microglial engulfment of VGLUT2+/PSD95+ synapses near the lesion. Bazedoxifene reduced foam-cell lipid load and C1q, preserved synapses, reduced microglial synapse engulfment, and improved motor recovery; the precise lipid-lowering mechanism was not resolved. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Bazedoxifene from 4-11 dpi; C1q and synapse readouts at 11 dpi; behavior at 28 dpi", "control_type": "IgG, vehicle, DMSO, and untreated macrophage controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Forceps clamping for 2 s; in vitro homogenate-induced foam cells", "injury_model": "T10 forceps-clamp SCI and SCI-homogenate foam-cell model", "injury_severity": "Moderate contusion/compression; in vitro lipid-loading model", "intervention_type": "Bazedoxifene 5 uM in vitro and intraperitoneal treatment in SCI mice; anti-C1q antibody for causal complement blockade", "methods_summary": "Foam-cell lipid accumulation increased C1q and microglial engulfment of VGLUT2+/PSD95+ synapses near the lesion. Bazedoxifene reduced foam-cell lipid load and C1q, preserved synapses, reduced microglial synapse engulfment, and improved motor recovery; the precise lipid-lowering mechanism was not resolved.", "observation_tracker_ids": ["M3B-O071"], "sex": "UNKNOWN in vivo; not applicable in vitro", "source_experiment_tracker_id": "M3A-P024-E002", "source_paper_tracker_id": "M3A-P024", "species": "Mouse SCI model plus bone-marrow-derived macrophage culture", "strain": "Mouse; strain and sex not stated in extracted methods", "tracker_key": "M3A-P024::M3A-P024-E002", "vertebral_level": "T10 in vivo"}'
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
    'A-layer full text; Full text PMC',
    'Tracker experiment M3A-P025-E001',
    'Extracted details: Full-text intervention and knockout design separates debris-clearance benefit from later scar/inflammation liability. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "TREM2 peaks at 7 dpi; short- versus long-term activation tested", "control_type": "Sham/vehicle, TREM2 knockout, and scrambled-peptide controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Crush injury as reported", "injury_model": "T10 spinal cord crush injury", "injury_severity": "Crush injury as reported", "intervention_type": "TREM2 was localized mainly to Iba1+ macrophages/microglia; TREM2 knockout impaired myelin-debris engulfment and degradation, increased foamy macrophages, and reduced DAM activation through the PI3K/AKT pathway.", "methods_summary": "Full-text intervention and knockout design separates debris-clearance benefit from later scar/inflammation liability.", "observation_tracker_ids": ["M3B-O025"], "sex": "Female", "source_experiment_tracker_id": "M3A-P025-E001", "source_paper_tracker_id": "M3A-P025", "species": "Mouse SCI model", "strain": "UNKNOWN", "tracker_key": "M3A-P025::M3A-P025-E001", "vertebral_level": "T10"}'
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
    'A-layer full text; Full text PMC',
    'Tracker experiment M3A-P025-E002',
    'Extracted details: Full-text finding is explicitly bidirectional and timing-sensitive, not a simple TREM2 neuroprotection claim. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "COG1410 at 5 min post-injury, daily to 56 dpi or only to 3 dpi", "control_type": "Vehicle and scrambled-peptide controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Crush injury as reported", "injury_model": "T10 spinal cord crush injury", "injury_severity": "Crush injury as reported", "intervention_type": "Long-term COG1410 TREM2 activation improved early locomotion but later impaired locomotor recovery, 5-HT+ axon regeneration, neuronal survival, and increased fibrosis/inflammation; short-term activation produced only transient early benefit without structural neuroprotection.", "methods_summary": "Full-text finding is explicitly bidirectional and timing-sensitive, not a simple TREM2 neuroprotection claim.", "observation_tracker_ids": ["M3B-O072"], "sex": "Female", "source_experiment_tracker_id": "M3A-P025-E002", "source_paper_tracker_id": "M3A-P025", "species": "Mouse SCI model", "strain": "UNKNOWN", "tracker_key": "M3A-P025::M3A-P025-E002", "vertebral_level": "T10"}'
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
    'A-layer full text; Full text PMC',
    'Tracker experiment M3A-P026-E001',
    'Extracted details: Targeted metabolomics linked elevated lactate in SCI patient serum to glycolytic changes; mouse lesion macrophages and circulating monocytes showed subacute H3K9la enrichment, with CUT&Tag/RNA-seq identifying TXNIP as a direct H3K9la-associated inflammatory target. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "14 dpi macrophage focus", "control_type": "SCI patient serum within 7 days; sham/SCI and lactate/PBS/2-DG controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "SCI as reported", "intervention_type": "Human metabolic profiling and mouse macrophage H3K9la mapping", "methods_summary": "Targeted metabolomics linked elevated lactate in SCI patient serum to glycolytic changes; mouse lesion macrophages and circulating monocytes showed subacute H3K9la enrichment, with CUT&Tag/RNA-seq identifying TXNIP as a direct H3K9la-associated inflammatory target.", "observation_tracker_ids": ["M3B-O026"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M3A-P026-E001", "source_paper_tracker_id": "M3A-P026", "species": "Mouse SCI model plus human serum", "strain": "UNKNOWN", "tracker_key": "M3A-P026::M3A-P026-E001", "vertebral_level": "UNKNOWN"}'
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
    'A-layer full text; Full text PMC',
    'Tracker experiment M3A-P026-E002',
    'Extracted details: Lactate increased TXNIP/NLRP3 signaling, inflammatory markers, ROS, and mitochondrial dysfunction; 2-DG or TXNIP knockdown attenuated these effects. The hypoxia-responsive peptide reduced inflammatory signaling, restored mitochondrial integrity, increased axon regeneration, and improved MEP, BMS, swimming, kinematic, and bladder outcomes. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "14-28 dpi treatment window", "control_type": "Vehicle, glycolysis inhibition, TXNIP knockdown, and peptide controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "SCI as reported", "intervention_type": "H3K9la-pe macrophage-targeted peptide inhibition", "methods_summary": "Lactate increased TXNIP/NLRP3 signaling, inflammatory markers, ROS, and mitochondrial dysfunction; 2-DG or TXNIP knockdown attenuated these effects. The hypoxia-responsive peptide reduced inflammatory signaling, restored mitochondrial integrity, increased axon regeneration, and improved MEP, BMS, swimming, kinematic, and bladder outcomes.", "observation_tracker_ids": ["M3B-O073"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M3A-P026-E002", "source_paper_tracker_id": "M3A-P026", "species": "Mouse SCI model", "strain": "UNKNOWN", "tracker_key": "M3A-P026::M3A-P026-E002", "vertebral_level": "UNKNOWN"}'
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
    'A-layer full text; Full text PMC',
    'Tracker experiment M3A-P027-E001',
    'Extracted details: Full-text design includes both in vitro pathway dissection and in vivo AMPK-dependence testing. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Subacute treatment; behavioral testing to 56 dpi", "control_type": "Sham, SCI saline, metformin, compound C, and metformin+compound C groups", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "MASCIS Impactor Model III", "injury_model": "Moderate T10 contusion SCI", "injury_severity": "Moderate contusion", "intervention_type": "Integrated transcriptomic and single-cell analyses identified microglia as the predominant PANoptotic population after SCI; in BV2 microglia, 1 uM metformin with LPS/ATP challenge reduced pyroptosis, apoptosis, necroptosis, inflammatory cytokines, and M1 polarization through AMPK/NF-kB signaling.", "methods_summary": "Full-text design includes both in vitro pathway dissection and in vivo AMPK-dependence testing.", "observation_tracker_ids": ["M3B-O027"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M3A-P027-E001", "source_paper_tracker_id": "M3A-P027", "species": "Rat SCI model", "strain": "UNKNOWN", "tracker_key": "M3A-P027::M3A-P027-E001", "vertebral_level": "T10"}'
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
    'A-layer full text; Full text PMC',
    'Tracker experiment M3A-P027-E002',
    'Extracted details: Full-text result is pharmacological mechanism evidence with an inhibitor control, not genetic proof of AMPK specificity. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Metformin 50 mg/kg/day i.p.; assessments at 3-56 dpi", "control_type": "Vehicle, compound C, and metformin+compound C controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "MASCIS Impactor Model III", "injury_model": "Moderate T10 contusion SCI", "injury_severity": "Moderate contusion", "intervention_type": "Metformin promoted tissue repair, axon regrowth, remyelination, motor and electrophysiological recovery, and reduced microglia/macrophage M1 polarization; compound C abrogated the neuroprotective effects, supporting AMPK dependence.", "methods_summary": "Full-text result is pharmacological mechanism evidence with an inhibitor control, not genetic proof of AMPK specificity.", "observation_tracker_ids": ["M3B-O074"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M3A-P027-E002", "source_paper_tracker_id": "M3A-P027", "species": "Rat SCI model", "strain": "UNKNOWN", "tracker_key": "M3A-P027::M3A-P027-E002", "vertebral_level": "T10"}'
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
    'A-layer full text; Full text PMC',
    'Tracker experiment M3A-P028-E001',
    'Extracted details: Full-text record is primarily multi-omics and regulatory mapping evidence. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Acute/subacute transcriptomic time course", "control_type": "Sham and SCI bulk/scRNA-seq comparisons", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "UNKNOWN", "intervention_type": "Bulk RNA-seq and scRNA-seq showed persistent pyroptosis, apoptosis, and necroptosis signatures concentrated in microglia; machine-learning and TF analyses identified IRF1 as an independent PANoptosis-associated regulator and ZBP1 as a prominent PANoptosome sensor.", "methods_summary": "Full-text record is primarily multi-omics and regulatory mapping evidence.", "observation_tracker_ids": ["M3B-O028"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M3A-P028-E001", "source_paper_tracker_id": "M3A-P028", "species": "Rat SCI model", "strain": "UNKNOWN", "tracker_key": "M3A-P028::M3A-P028-E001", "vertebral_level": "UNKNOWN"}'
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
    'A-layer full text; Full text PMC',
    'Tracker experiment M3A-P028-E002',
    'Extracted details: Full-text result supports an IRF1-ZBP1 mechanistic target, while functional recovery was not the primary endpoint of this paper. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Vehicle/inhibitor comparisons", "control_type": "IRF1 DNA-binding domain inhibition", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "UNKNOWN", "intervention_type": "IRF1 occupied the Zbp1 promoter; pharmacological inhibition of the IRF1 DNA-binding domain reduced ZBP1, PANoptosis execution markers, TNF-alpha and IL-6 release, and M1-like polarization.", "methods_summary": "Full-text result supports an IRF1-ZBP1 mechanistic target, while functional recovery was not the primary endpoint of this paper.", "observation_tracker_ids": ["M3B-O075"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M3A-P028-E002", "source_paper_tracker_id": "M3A-P028", "species": "Rat SCI model plus microglial cell model", "strain": "UNKNOWN", "tracker_key": "M3A-P028::M3A-P028-E002", "vertebral_level": "UNKNOWN"}'
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
    'Extracted details: Primary intervention or mechanism experiment for Trimethylamine N-Oxide Aggravates Neuro-inflammation in Spinal Cord Injury Through NLRP3 Inflammasome Activation in Microglia.; first-pass row captures microglia/macrophage programmed inflammatory death in mouse sci model at abstract/source-title level. Extraction status: YES (abstract-level)',
    '{"chronicity_dpi_wpi": "UNKNOWN", "control_type": "Injury / vehicle / wild-type / comparator as reported", "experiment_extracted": "YES (abstract-level)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "UNKNOWN", "intervention_type": "Microglia/macrophage programmed inflammatory death", "methods_summary": "Primary intervention or mechanism experiment for Trimethylamine N-Oxide Aggravates Neuro-inflammation in Spinal Cord Injury Through NLRP3 Inflammasome Activation in Microglia.; first-pass row captures microglia/macrophage programmed inflammatory death in mouse sci model at abstract/source-title level.", "observation_tracker_ids": ["M3B-O029"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M3A-P029-E001", "source_paper_tracker_id": "M3A-P029", "species": "Mouse SCI model", "strain": "UNKNOWN", "tracker_key": "M3A-P029::M3A-P029-E001", "vertebral_level": "UNKNOWN"}'
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
    'Extracted details: Outcome/mechanistic validation row for Trimethylamine N-Oxide Aggravates Neuro-inflammation in Spinal Cord Injury Through NLRP3 Inflammasome Activation in Microglia.; first-pass row captures microglia/macrophage programmed inflammatory death in mouse sci model at abstract/source-title level. Extraction status: YES (abstract-level)',
    '{"chronicity_dpi_wpi": "UNKNOWN", "control_type": "Comparator/control arm as reported", "experiment_extracted": "YES (abstract-level)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "UNKNOWN", "intervention_type": "Mechanistic outcome assessment after microglia/macrophage programmed inflammatory death", "methods_summary": "Outcome/mechanistic validation row for Trimethylamine N-Oxide Aggravates Neuro-inflammation in Spinal Cord Injury Through NLRP3 Inflammasome Activation in Microglia.; first-pass row captures microglia/macrophage programmed inflammatory death in mouse sci model at abstract/source-title level.", "observation_tracker_ids": ["M3B-O076"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M3A-P029-E002", "source_paper_tracker_id": "M3A-P029", "species": "Mouse SCI model", "strain": "UNKNOWN", "tracker_key": "M3A-P029::M3A-P029-E002", "vertebral_level": "UNKNOWN"}'
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
    'Extracted details: Primary intervention or mechanism experiment for Thiolutin attenuates neuroinflammation and neuronal apoptosis by suppressing microglial pyroptosis through NLRP3 inflammasome inhibition after spinal cord injury.; first-pass row captures macrophage/microglia polarization signaling in mouse sci model at abstract/source-title level. Extraction status: YES (abstract-level)',
    '{"chronicity_dpi_wpi": "UNKNOWN", "control_type": "Injury / vehicle / wild-type / comparator as reported", "experiment_extracted": "YES (abstract-level)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "UNKNOWN", "intervention_type": "Macrophage/microglia polarization signaling", "methods_summary": "Primary intervention or mechanism experiment for Thiolutin attenuates neuroinflammation and neuronal apoptosis by suppressing microglial pyroptosis through NLRP3 inflammasome inhibition after spinal cord injury.; first-pass row captures macrophage/microglia polarization signaling in mouse sci model at abstract/source-title level.", "observation_tracker_ids": ["M3B-O030"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M3A-P030-E001", "source_paper_tracker_id": "M3A-P030", "species": "Mouse SCI model", "strain": "UNKNOWN", "tracker_key": "M3A-P030::M3A-P030-E001", "vertebral_level": "UNKNOWN"}'
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
    'Extracted details: Outcome/mechanistic validation row for Thiolutin attenuates neuroinflammation and neuronal apoptosis by suppressing microglial pyroptosis through NLRP3 inflammasome inhibition after spinal cord injury.; first-pass row captures macrophage/microglia polarization signaling in mouse sci model at abstract/source-title level. Extraction status: YES (abstract-level)',
    '{"chronicity_dpi_wpi": "UNKNOWN", "control_type": "Comparator/control arm as reported", "experiment_extracted": "YES (abstract-level)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "UNKNOWN", "intervention_type": "Mechanistic outcome assessment after macrophage/microglia polarization signaling", "methods_summary": "Outcome/mechanistic validation row for Thiolutin attenuates neuroinflammation and neuronal apoptosis by suppressing microglial pyroptosis through NLRP3 inflammasome inhibition after spinal cord injury.; first-pass row captures macrophage/microglia polarization signaling in mouse sci model at abstract/source-title level.", "observation_tracker_ids": ["M3B-O077"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M3A-P030-E002", "source_paper_tracker_id": "M3A-P030", "species": "Mouse SCI model", "strain": "UNKNOWN", "tracker_key": "M3A-P030::M3A-P030-E002", "vertebral_level": "UNKNOWN"}'
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
    'A-layer full text; Full text PMC; Fig. 1-4',
    'Tracker experiment M3A-P031-E001',
    'Extracted details: T2D mice had worse BMS scores (1.1 versus 3.5 at 7 d; 1.8 versus 5.5 at 14 d), poorer electrophysiological conduction, larger lesion/demyelination, fewer Iba1+ cells, impaired microglial myelin-debris phagocytosis, and lower remyelination than non-diabetic SCI mice. Survival through 14 d was 35% in T2D SCI versus 80% in SCI. RNA-seq and protein data linked the phenotype to increased NLRP3/Caspase-1/GSDMD/IL-1beta/IL-18 and oxidative-stress programs. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "T2D induction with 60% fat diet for 6 weeks plus STZ 75 mg/kg for 2 days; behavioral and tissue readouts at 5 and 14 days", "control_type": "Normal-diet sham, normal-diet SCI, T2D sham, and T2D SCI groups", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Allne striker after T9 laminectomy", "injury_model": "T2D combined with T9 impact SCI", "injury_severity": "Severe acute injury; post-injury BMS approximately 0", "intervention_type": "Type 2 diabetes model without therapeutic intervention", "methods_summary": "T2D mice had worse BMS scores (1.1 versus 3.5 at 7 d; 1.8 versus 5.5 at 14 d), poorer electrophysiological conduction, larger lesion/demyelination, fewer Iba1+ cells, impaired microglial myelin-debris phagocytosis, and lower remyelination than non-diabetic SCI mice. Survival through 14 d was 35% in T2D SCI versus 80% in SCI. RNA-seq and protein data linked the phenotype to increased NLRP3/Caspase-1/GSDMD/IL-1beta/IL-18 and oxidative-stress programs.", "observation_tracker_ids": ["M3B-O031"], "sex": "Male", "source_experiment_tracker_id": "M3A-P031-E001", "source_paper_tracker_id": "M3A-P031", "species": "Mouse", "strain": "C57BL/6J", "tracker_key": "M3A-P031::M3A-P031-E001", "vertebral_level": "T9"}'
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
    'A-layer full text; Full text PMC; Fig. 6',
    'Tracker experiment M3A-P031-E002',
    'Extracted details: Microglial Caspase-1 deletion increased BMS scores, reduced persistent hindlimb dragging and damaged area, improved LFB-defined remyelination, and reduced spinal Caspase-1 and cleaved-Caspase-1/Iba1 colocalization in diabetic SCI. This supports microglial pyroptosis as an important contributor, although the model and marker strategy do not isolate every microglial subtype or exclude all non-microglial effects. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "BMS/footprints and H&E/LFB at 14 days; Caspase-1 and Iba1 assays at 5 days", "control_type": "Sham WT, sham Caspase-1 KO, T2D SCI WT, and T2D SCI conditional microglial Caspase-1 KO", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Allne striker after T9 laminectomy", "injury_model": "T2D combined with T9 impact SCI", "injury_severity": "Severe acute injury; post-injury BMS approximately 0", "intervention_type": "Conditional microglial Caspase-1 knockout", "methods_summary": "Microglial Caspase-1 deletion increased BMS scores, reduced persistent hindlimb dragging and damaged area, improved LFB-defined remyelination, and reduced spinal Caspase-1 and cleaved-Caspase-1/Iba1 colocalization in diabetic SCI. This supports microglial pyroptosis as an important contributor, although the model and marker strategy do not isolate every microglial subtype or exclude all non-microglial effects.", "observation_tracker_ids": ["M3B-O078"], "sex": "Male background as reported", "source_experiment_tracker_id": "M3A-P031-E002", "source_paper_tracker_id": "M3A-P031", "species": "Mouse", "strain": "Caspase-1 flox/flox with conditional microglial iCRE deletion; WT controls", "tracker_key": "M3A-P031::M3A-P031-E002", "vertebral_level": "T9"}'
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
    'A-layer full text; Full text PMC',
    'Tracker experiment M3A-P032-E001',
    'Extracted details: Endogenous FGF4 rose transiently early after SCI. Exogenous FGF4 increased myelin-debris phagocytosis in BMDMs through FGFR1-PI3K/AKT and upregulated Clec10a; it also improved phagosome maturation from Rab5+ to Rab7+ to Lamp1+ compartments and restored CTSD-dependent lysosomal degradation. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Early transient FGF4 response; longer-term repair assessment", "control_type": "Vehicle, FGF4, FGFR1 inhibition, Clec10a knockdown, and myelin-debris controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "SCI as reported", "intervention_type": "FGF4 treatment and myelin-debris phagocytosis", "methods_summary": "Endogenous FGF4 rose transiently early after SCI. Exogenous FGF4 increased myelin-debris phagocytosis in BMDMs through FGFR1-PI3K/AKT and upregulated Clec10a; it also improved phagosome maturation from Rab5+ to Rab7+ to Lamp1+ compartments and restored CTSD-dependent lysosomal degradation.", "observation_tracker_ids": ["M3B-O032"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M3A-P032-E001", "source_paper_tracker_id": "M3A-P032", "species": "Mouse SCI model plus BMDMs", "strain": "UNKNOWN", "tracker_key": "M3A-P032::M3A-P032-E001", "vertebral_level": "UNKNOWN"}'
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
    'A-layer full text; Full text PMC',
    'Tracker experiment M3A-P032-E002',
    'Extracted details: FGF4 reduced lipid accumulation, NLRP3 activity, lysosomal membrane permeabilization, and inflammatory polarization after SCI; it improved axon regeneration and locomotor recovery, while FGFR1 inhibition or Clec10a silencing attenuated phagocytic and neuronal-protective effects. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "In vivo structural and locomotor follow-up", "control_type": "Vehicle, FGF4, FGFR1 inhibitor, Clec10a knockdown, and myelin-debris controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "SCI as reported", "intervention_type": "FGF4 treatment and Clec10a-mediated repair validation", "methods_summary": "FGF4 reduced lipid accumulation, NLRP3 activity, lysosomal membrane permeabilization, and inflammatory polarization after SCI; it improved axon regeneration and locomotor recovery, while FGFR1 inhibition or Clec10a silencing attenuated phagocytic and neuronal-protective effects.", "observation_tracker_ids": ["M3B-O079"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M3A-P032-E002", "source_paper_tracker_id": "M3A-P032", "species": "Mouse SCI model plus neuron-conditioned-medium assay", "strain": "UNKNOWN", "tracker_key": "M3A-P032::M3A-P032-E002", "vertebral_level": "UNKNOWN"}'
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
    'Extracted details: Primary intervention or mechanism experiment for GP130 Regulates Macrophage Polarization and Functional Recovery after Spinal Cord Injury in Rats: A Single-Cell RNA Sequencing Study.; first-pass row captures macrophage/microglia polarization signaling in rat sci model at abstract/source-title level. Extraction status: YES (abstract-level)',
    '{"chronicity_dpi_wpi": "UNKNOWN", "control_type": "Injury / vehicle / wild-type / comparator as reported", "experiment_extracted": "YES (abstract-level)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "UNKNOWN", "intervention_type": "Macrophage/microglia polarization signaling", "methods_summary": "Primary intervention or mechanism experiment for GP130 Regulates Macrophage Polarization and Functional Recovery after Spinal Cord Injury in Rats: A Single-Cell RNA Sequencing Study.; first-pass row captures macrophage/microglia polarization signaling in rat sci model at abstract/source-title level.", "observation_tracker_ids": ["M3B-O033"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M3A-P033-E001", "source_paper_tracker_id": "M3A-P033", "species": "Rat SCI model", "strain": "UNKNOWN", "tracker_key": "M3A-P033::M3A-P033-E001", "vertebral_level": "UNKNOWN"}'
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
    'Extracted details: Outcome/mechanistic validation row for GP130 Regulates Macrophage Polarization and Functional Recovery after Spinal Cord Injury in Rats: A Single-Cell RNA Sequencing Study.; first-pass row captures macrophage/microglia polarization signaling in rat sci model at abstract/source-title level. Extraction status: YES (abstract-level)',
    '{"chronicity_dpi_wpi": "UNKNOWN", "control_type": "Comparator/control arm as reported", "experiment_extracted": "YES (abstract-level)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "UNKNOWN", "intervention_type": "Mechanistic outcome assessment after macrophage/microglia polarization signaling", "methods_summary": "Outcome/mechanistic validation row for GP130 Regulates Macrophage Polarization and Functional Recovery after Spinal Cord Injury in Rats: A Single-Cell RNA Sequencing Study.; first-pass row captures macrophage/microglia polarization signaling in rat sci model at abstract/source-title level.", "observation_tracker_ids": ["M3B-O080"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M3A-P033-E002", "source_paper_tracker_id": "M3A-P033", "species": "Rat SCI model", "strain": "UNKNOWN", "tracker_key": "M3A-P033::M3A-P033-E002", "vertebral_level": "UNKNOWN"}'
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
    'A-layer full text; Full text PMC; narrative review scope',
    'Tracker experiment M3A-P034-E001',
    'Extracted details: The article synthesizes evidence that CGRP-positive sensory fibers sprout or become ectopically distributed after SCI and that CGRP-CGRP-receptor signaling can influence macrophage polarization through cAMP/PKA, MAPK, and related pathways. It is a narrative review, not a new in vivo or in vitro SCI experiment. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Cited studies span acute, subacute, and chronic post-SCI phases", "control_type": "No new experimental controls; evidence is drawn from cited primary studies", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Not applicable", "injury_model": "SCI literature synthesis", "injury_severity": "Not applicable", "intervention_type": "Review of CGRP-positive sensory-fiber remodeling and macrophage polarization", "methods_summary": "The article synthesizes evidence that CGRP-positive sensory fibers sprout or become ectopically distributed after SCI and that CGRP-CGRP-receptor signaling can influence macrophage polarization through cAMP/PKA, MAPK, and related pathways. It is a narrative review, not a new in vivo or in vitro SCI experiment.", "observation_tracker_ids": ["M3B-O034"], "sex": "Not applicable", "source_experiment_tracker_id": "M3A-P034-E001", "source_paper_tracker_id": "M3A-P034", "species": "Not applicable; literature synthesis", "strain": "Not applicable", "tracker_key": "M3A-P034::M3A-P034-E001", "vertebral_level": "Not applicable"}'
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
    'A-layer full text; Full text PMC; evidence-boundary assessment',
    'Tracker experiment M3A-P034-E002',
    'Extracted details: The review proposes CGRP as a context- and time-dependent immunomodulator, but it does not provide a single primary SCI experiment demonstrating that CGRP manipulation alone causes functional recovery. Specific therapeutic claims require retrieval and extraction of the cited primary studies. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Temporal claims include macrophage pro-inflammatory peaks around days 3-7 and reparative states around days 14-28 in cited work", "control_type": "No direct comparator arms in this review article", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Not applicable", "injury_model": "SCI literature synthesis", "injury_severity": "Not applicable", "intervention_type": "Evidence appraisal of sensory-neuropeptide/macrophage crosstalk", "methods_summary": "The review proposes CGRP as a context- and time-dependent immunomodulator, but it does not provide a single primary SCI experiment demonstrating that CGRP manipulation alone causes functional recovery. Specific therapeutic claims require retrieval and extraction of the cited primary studies.", "observation_tracker_ids": ["M3B-O081"], "sex": "Not consistently specified", "source_experiment_tracker_id": "M3A-P034-E002", "source_paper_tracker_id": "M3A-P034", "species": "Cited animal and cell studies as reported by the review", "strain": "Not consistently specified", "tracker_key": "M3A-P034::M3A-P034-E002", "vertebral_level": "Not applicable"}'
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
    'A-layer full text; Full text PMC',
    'Tracker experiment M3A-P035-E001',
    'Extracted details: Full-text methods provide a complete dosing, injury, sex, and endpoint record. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "IL-4 begun 12 h post-injury, twice daily through 7 dpi", "control_type": "Sham, SCI vehicle, and SCI IL-4; n=30/45/45", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "28 g modified aneurysm clip, 60 s", "injury_model": "T10 clip contusion-compression", "injury_severity": "Contusion-compression", "intervention_type": "Systemic recombinant rat IL-4, 0.5 ug/kg i.p., was tested with BBB, CatWalk XT, gridwalk, tissue immunohistochemistry, RNA-seq, proteomics, and serum cytokine profiling at 1, 3, 7, 14, and 28 dpi.", "methods_summary": "Full-text methods provide a complete dosing, injury, sex, and endpoint record.", "observation_tracker_ids": ["M3B-O035"], "sex": "Female", "source_experiment_tracker_id": "M3A-P035-E001", "source_paper_tracker_id": "M3A-P035", "species": "Rat SCI model", "strain": "Wistar", "tracker_key": "M3A-P035::M3A-P035-E001", "vertebral_level": "T10"}'
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
    'A-layer full text; Full text PMC',
    'Tracker experiment M3A-P035-E002',
    'Extracted details: Full-text finding supports systemic immunomodulation and translational association, not direct evidence that the rat pathway transfers unchanged to humans. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Functional follow-up to 28 dpi; patient cytokine association", "control_type": "Vehicle and sham controls; longitudinal human SCI comparison", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "28 g modified aneurysm clip, 60 s", "injury_model": "T10 clip contusion-compression", "injury_severity": "Contusion-compression", "intervention_type": "IL-4 improved BBB by 14 dpi and reduced hindlimb gridwalk errors; it increased IBA1+/ARG1+ and IBA1+/CD206+ macrophages, reduced IBA1+/iNOS+ cells, cystic cavity size, astrogliosis and oligodendrocyte loss, and suppressed 1-7 dpi cytokine surges. Human lower cytokine levels were associated with better neurological outcomes.", "methods_summary": "Full-text finding supports systemic immunomodulation and translational association, not direct evidence that the rat pathway transfers unchanged to humans.", "observation_tracker_ids": ["M3B-O082"], "sex": "Female; human sex as reported", "source_experiment_tracker_id": "M3A-P035-E002", "source_paper_tracker_id": "M3A-P035", "species": "Rat SCI model plus human SCI serum", "strain": "Wistar; human comparator cohort", "tracker_key": "M3A-P035::M3A-P035-E002", "vertebral_level": "T10"}'
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
    'A-layer full text; Full text PMC',
    'Tracker experiment M3A-P036-E001',
    'Extracted details: Omaveloxolone improved BMS recovery, CatWalk gait metrics, hindlimb motor-evoked potentials, and lesion morphology through 8 weeks. At 7 dpi it reduced CD68+/iNOS+ and Iba1+/iNOS+ cells, increased CD206-associated macrophage/microglial states, and lowered inflammatory cytokine and immune-pathway signals. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "0.5 h after injury through 8 weeks; daily treatment for 7 d", "control_type": "Sham and PBS-treated SCI controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "NYU Impactor-III after T10 laminectomy; modified Allen method", "injury_model": "T10 contusion SCI", "injury_severity": "Moderate contusion", "intervention_type": "Omaveloxolone 10 mg/kg intraperitoneally beginning 30 min after SCI and daily for 7 d", "methods_summary": "Omaveloxolone improved BMS recovery, CatWalk gait metrics, hindlimb motor-evoked potentials, and lesion morphology through 8 weeks. At 7 dpi it reduced CD68+/iNOS+ and Iba1+/iNOS+ cells, increased CD206-associated macrophage/microglial states, and lowered inflammatory cytokine and immune-pathway signals.", "observation_tracker_ids": ["M3B-O036"], "sex": "Female", "source_experiment_tracker_id": "M3A-P036-E001", "source_paper_tracker_id": "M3A-P036", "species": "Mouse SCI model", "strain": "C57BL/6JNifdc", "tracker_key": "M3A-P036::M3A-P036-E001", "vertebral_level": "T10"}'
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
    'A-layer full text; Full text PMC',
    'Tracker experiment M3A-P036-E002',
    'Extracted details: In LPS-stimulated BMDMs, omaveloxolone reduced CD86/iNOS-associated M1 polarization and increased CD206-associated M2 polarization. RNA-seq showed lower chemokine and cytokine programs and higher antioxidant or cytoprotective programs; direct Nrf2-to-polarization causality was not fully tested. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "24 h in vitro; 3-7 dpi cytokine and polarization readouts; 8 week function", "control_type": "Vehicle, LPS, and SCI controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "NYU Impactor-III in vivo; LPS stimulation in vitro", "injury_model": "T10 contusion SCI plus LPS-stimulated BMDM model", "injury_severity": "Moderate contusion; inflammatory polarization assay", "intervention_type": "Omaveloxolone with LPS for 24 h in BMDMs; in vivo treatment as above", "methods_summary": "In LPS-stimulated BMDMs, omaveloxolone reduced CD86/iNOS-associated M1 polarization and increased CD206-associated M2 polarization. RNA-seq showed lower chemokine and cytokine programs and higher antioxidant or cytoprotective programs; direct Nrf2-to-polarization causality was not fully tested.", "observation_tracker_ids": ["M3B-O083"], "sex": "Male in vitro; female in vivo", "source_experiment_tracker_id": "M3A-P036-E002", "source_paper_tracker_id": "M3A-P036", "species": "Mouse SCI model plus bone-marrow-derived macrophage culture", "strain": "C57BL/6 mice; male for BMDM culture and female in vivo", "tracker_key": "M3A-P036::M3A-P036-E002", "vertebral_level": "T10 in vivo"}'
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
    'A-layer full text; Full text PMC',
    'Tracker experiment M3A-P037-E001',
    'Extracted details: HGIL13 improved BMS locomotor recovery and histopathology, reduced resident microglial abundance and CD86 expression, increased Arg1 in resident microglia and infiltrating monocyte-derived macrophages, and altered the early microglial transcriptome toward a less activated state. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "1-28 dpi", "control_type": "PBS and blank GelMA plus blank PLGA controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "PinPoint Precision Cortical Impactor; 1.5 m/s, 1.7 mm depth, 85 ms dwell", "injury_model": "T8-T10 contusion SCI", "injury_severity": "Moderate contusion", "intervention_type": "1.5 uL lesion-directed GelMA hydrogel containing 1,000 ng/ml free IL-13 and 2% IL-13-loaded PLGA microparticles, injected immediately after injury at lesion, 1 mm rostral, and 1 mm caudal sites", "methods_summary": "HGIL13 improved BMS locomotor recovery and histopathology, reduced resident microglial abundance and CD86 expression, increased Arg1 in resident microglia and infiltrating monocyte-derived macrophages, and altered the early microglial transcriptome toward a less activated state.", "observation_tracker_ids": ["M3B-O037"], "sex": "Male and female", "source_experiment_tracker_id": "M3A-P037-E001", "source_paper_tracker_id": "M3A-P037", "species": "Mouse SCI model", "strain": "C57BL/6J and Hexb-tdTomato", "tracker_key": "M3A-P037::M3A-P037-E001", "vertebral_level": "T8-T10"}'
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
    'A-layer full text; Full text PMC',
    'Tracker experiment M3A-P037-E002',
    'Extracted details: Released IL-13 retained bioactivity, increased Arg1 and CD206 and reduced inflammatory marker expression and TNF-alpha secretion in LPS-stimulated BV2 cells. The in vivo study linked this immune shift to lower microglial activation, improved myelin and tissue outcomes, and better locomotor recovery. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "24 h in vitro; 7-28 dpi in vivo", "control_type": "Untreated BV2, LPS, recombinant IL-13, blank hydrogel, and PBS controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Not applicable in vitro; PinPoint impactor in vivo", "injury_model": "LPS-stimulated BV2 model plus T8-T10 contusion", "injury_severity": "LPS inflammatory stimulation; moderate contusion in vivo", "intervention_type": "HGIL13 release samples or 20 ng/ml recombinant IL-13 with 10 ng/ml LPS; in vivo HGIL13 as above", "methods_summary": "Released IL-13 retained bioactivity, increased Arg1 and CD206 and reduced inflammatory marker expression and TNF-alpha secretion in LPS-stimulated BV2 cells. The in vivo study linked this immune shift to lower microglial activation, improved myelin and tissue outcomes, and better locomotor recovery.", "observation_tracker_ids": ["M3B-O084"], "sex": "Male and female in vivo; not applicable in vitro", "source_experiment_tracker_id": "M3A-P037-E002", "source_paper_tracker_id": "M3A-P037", "species": "BV2 microglia and mouse contusion SCI validation", "strain": "BV2 cells; C57BL/6J and Hexb-tdTomato mice", "tracker_key": "M3A-P037::M3A-P037-E002", "vertebral_level": "T8-T10 in vivo"}'
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
    'A-layer full text; Full text PMC',
    'Tracker experiment M3A-P038-E001',
    'Extracted details: Neonatal mouse circulating blood-derived small extracellular vesicles delivered miR-487b-3p to spinal cord microvascular endothelial cells; myelin debris-induced IRS1-PI3K-Akt-mTOR overactivation, lipid-droplet buildup, EndoMT, and CXCL12 secretion were used as the vascular-immune injury model. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Adult SCI with neonatal vesicle/hydrogel intervention", "control_type": "Vehicle, blank hydrogel, NCE, and NCE-loaded GelNB comparators", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "SCI as reported", "intervention_type": "Neonatal sEV/miR-487b-3p vascular-immune reprogramming", "methods_summary": "Neonatal mouse circulating blood-derived small extracellular vesicles delivered miR-487b-3p to spinal cord microvascular endothelial cells; myelin debris-induced IRS1-PI3K-Akt-mTOR overactivation, lipid-droplet buildup, EndoMT, and CXCL12 secretion were used as the vascular-immune injury model.", "observation_tracker_ids": ["M3B-O038"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M3A-P038-E001", "source_paper_tracker_id": "M3A-P038", "species": "Mouse SCI model plus SCMECs", "strain": "UNKNOWN", "tracker_key": "M3A-P038::M3A-P038-E001", "vertebral_level": "UNKNOWN"}'
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
    'A-layer full text; Full text PMC',
    'Tracker experiment M3A-P038-E002',
    'Extracted details: Ago-miR-487b-3p@GelNB reduced endothelial lipid deposition and EndoMT, suppressed CXCL12-CXCR4 macrophage recruitment and TNF-alpha/GDF15 signaling, promoted neuroregeneration, and improved functional recovery. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Hydrogel treatment with neural and vascular-immune follow-up", "control_type": "Blank hydrogel/NCE and vehicle controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "SCI as reported", "intervention_type": "Ago-miR-487b-3p@GelNB treatment", "methods_summary": "Ago-miR-487b-3p@GelNB reduced endothelial lipid deposition and EndoMT, suppressed CXCL12-CXCR4 macrophage recruitment and TNF-alpha/GDF15 signaling, promoted neuroregeneration, and improved functional recovery.", "observation_tracker_ids": ["M3B-O085"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M3A-P038-E002", "source_paper_tracker_id": "M3A-P038", "species": "Mouse SCI model", "strain": "UNKNOWN", "tracker_key": "M3A-P038::M3A-P038-E002", "vertebral_level": "UNKNOWN"}'
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
    'A-layer full text; Full text PMC; Fig. 3-4 and supplementary co-culture assays',
    'Tracker experiment M3A-P039-E001',
    'Extracted details: P2Y12R-overexpressing microglia degraded neuron-derived ATP through CD39/CD73, increased adenosine, and promoted A1R-dependent neuronal mitophagy through PINK1/Parkin/LC3. This reduced ROS, restored mitochondrial membrane potential and ATP, and improved neuronal viability; blockade of P2Y12R, A1R, PINK1, or Parkin attenuated the effect. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Acute oxidative-stress assays with ATP/adenosine, mitophagy, mitochondrial membrane potential, ATP, ROS, and PINK1/Parkin/LC3 readouts", "control_type": "Untreated/injury controls, non-transfected microglia, P2Y12R antagonist, CD39/CD73 blockade, adenosine rescue, A1R/A2R inhibitors, and PINK1/Parkin knockdown", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "H2O2 injury; primary microglia transfected with P2ry12-Nano and co-cultured with injured neurons, with Transwell assays preventing direct contact", "injury_model": "In vitro oxidative-stress co-culture", "injury_severity": "Not applicable", "intervention_type": "Microglial P2Y12R overexpression and purine-metabolism pathway validation", "methods_summary": "P2Y12R-overexpressing microglia degraded neuron-derived ATP through CD39/CD73, increased adenosine, and promoted A1R-dependent neuronal mitophagy through PINK1/Parkin/LC3. This reduced ROS, restored mitochondrial membrane potential and ATP, and improved neuronal viability; blockade of P2Y12R, A1R, PINK1, or Parkin attenuated the effect.", "observation_tracker_ids": ["M3B-O039"], "sex": "Not applicable", "source_experiment_tracker_id": "M3A-P039-E001", "source_paper_tracker_id": "M3A-P039", "species": "Primary mouse microglia, neurons, astrocytes, and HT22 neurons", "strain": "Neonatal C57BL/6 cultures; both sexes for primary cells", "tracker_key": "M3A-P039::M3A-P039-E001", "vertebral_level": "Not applicable"}'
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
    'A-layer full text; Full text PMC; Fig. 1-2, 5, and supplementary biodistribution/ex vivo slice assays',
    'Tracker experiment M3A-P039-E002',
    'Extracted details: P2Y-TK-Nano showed ROS-responsive lesion accumulation, highest microglial co-localization, and greater restoration of P2Y12R than TK-Nano or P2Y-Nano. At 7 days it reduced lesion cavity and neuronal apoptosis and increased neuronal Tomm20-LC3 co-localization and healthy mitochondria in tissue slices and injured spinal cord. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Nanoparticle accumulation 1-24 h; microglial/P2Y12R, neuronal mitophagy, lesion, and apoptosis readouts at 7 days", "control_type": "Saline SCI, TK-Nano, P2Y-Nano, empty/non-targeted formulations, and non-MG1 targeting comparisons", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Circumferential 5-mm microforceps compression for 5 s; 50 microliters of 10 mg/ml nanoparticle formulation by tail vein from 2 h after injury through day 6", "injury_model": "T10 contusion SCI", "injury_severity": "Microforceps contusion", "intervention_type": "ROS-responsive thioketal, MG1 microglia-targeting P2Y-TK-Nano carrying P2ry12 plasmid", "methods_summary": "P2Y-TK-Nano showed ROS-responsive lesion accumulation, highest microglial co-localization, and greater restoration of P2Y12R than TK-Nano or P2Y-Nano. At 7 days it reduced lesion cavity and neuronal apoptosis and increased neuronal Tomm20-LC3 co-localization and healthy mitochondria in tissue slices and injured spinal cord.", "observation_tracker_ids": ["M3B-O086"], "sex": "Female in vivo; both sexes for ex vivo cultures", "source_experiment_tracker_id": "M3A-P039-E002", "source_paper_tracker_id": "M3A-P039", "species": "Mouse and ex vivo spinal cord slices", "strain": "C57BL/6 mice and neonatal C57BL/6 cultures", "tracker_key": "M3A-P039::M3A-P039-E002", "vertebral_level": "T10"}'
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
    'A-layer full text; Full text PMC; Fig. 5-9 and supplementary mechanism assays',
    'Tracker experiment M3A-P040-E001',
    'Extracted details: PM-Lipo@PB-NPs improved mitochondrial membrane potential and cristae, reduced ROS, MDA, cleaved-caspase-3, and apoptosis, increased mitochondria-lysosome/TOMM20-LC3 co-localization, and shifted BV2 cells toward a reparative phenotype with lower IL-1beta/TNF-alpha. PI3K/AKT/mTOR inhibition tracked with mitophagy restoration; MHY1485 partly reversed and LY294002 enhanced the effect, supporting but not fully proving pathway necessity. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Acute mitochondrial, ROS, apoptosis, mitophagy, PI3K/AKT/mTOR, and polarization assays", "control_type": "Injury-only, PB-NPs, and PM-Lipo@PB-NPs controls; MHY1485 mTOR activator and LY294002 PI3K inhibitor for pathway validation", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "60 micromolar H2O2 exposure as reported", "injury_model": "H2O2-induced oxidative-stress microglial model", "injury_severity": "Oxidative-stress injury in vitro", "intervention_type": "Biohybrid PM-Lipo@PB NPs consisting of platelet-derived membrane vesicles, M2 macrophage extracellular vesicles, and a Prussian blue nanozyme shell", "methods_summary": "PM-Lipo@PB-NPs improved mitochondrial membrane potential and cristae, reduced ROS, MDA, cleaved-caspase-3, and apoptosis, increased mitochondria-lysosome/TOMM20-LC3 co-localization, and shifted BV2 cells toward a reparative phenotype with lower IL-1beta/TNF-alpha. PI3K/AKT/mTOR inhibition tracked with mitophagy restoration; MHY1485 partly reversed and LY294002 enhanced the effect, supporting but not fully proving pathway necessity.", "observation_tracker_ids": ["M3B-O040"], "sex": "Not applicable", "source_experiment_tracker_id": "M3A-P040-E001", "source_paper_tracker_id": "M3A-P040", "species": "BV2 microglial cells", "strain": "Cell line; strain/sex not applicable", "tracker_key": "M3A-P040::M3A-P040-E001", "vertebral_level": "Not applicable"}'
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
    'A-layer full text; Full text PMC; Fig. 4, 10 and supplementary targeting/repair assays',
    'Tracker experiment M3A-P040-E002',
    'Extracted details: PM-Lipo@PB-NPs showed greater lesion accumulation, longer circulation, and higher IBA-1+ microglial uptake than PB-NPs. In vivo treatment was associated with smaller cavities/scars, more preserved NeuN and NEFH, less LFB demyelination, improved footprint/BMS/inclined-plane performance, less reactive microglial morphology, and improved tissue preservation. Because the captured text omits key animal-method details and no single-component membrane controls are reported, the platform’s individual contributions remain unresolved. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Lesion targeting and microglial uptake; tissue repair and motor outcomes reported through 4-8 weeks; 28-day safety assessment also reported", "control_type": "SCI controls and PB-NP comparator; sham/safety comparisons as reported", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Injury device not stated in captured full text", "injury_model": "Experimental SCI", "injury_severity": "Injury severity not stated in captured full text", "intervention_type": "PM-Lipo@PB-NPs versus plain PB-NPs", "methods_summary": "PM-Lipo@PB-NPs showed greater lesion accumulation, longer circulation, and higher IBA-1+ microglial uptake than PB-NPs. In vivo treatment was associated with smaller cavities/scars, more preserved NeuN and NEFH, less LFB demyelination, improved footprint/BMS/inclined-plane performance, less reactive microglial morphology, and improved tissue preservation. Because the captured text omits key animal-method details and no single-component membrane controls are reported, the platform\u2019s individual contributions remain unresolved.", "observation_tracker_ids": ["M3B-O087"], "sex": "Not stated in captured full text", "source_experiment_tracker_id": "M3A-P040-E002", "source_paper_tracker_id": "M3A-P040", "species": "Mouse SCI model", "strain": "Not stated in captured full text", "tracker_key": "M3A-P040::M3A-P040-E002", "vertebral_level": "Vertebral level not stated in captured full text"}'
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
    'A-layer full text; Full text PMC; Fig. 2-4 and targeting/inflammation assays',
    'Tracker experiment M3A-P041-E001',
    'Extracted details: EPO@MLNP showed higher lesion-region expression and microglial enrichment than untargeted LNP, sustained local EPO production, lower BV2 iNOS after LPS, fewer CD86+ microglia, reduced microglial infiltration, and lower plasma TNF-alpha, IL-1beta, and IL-6. The delivery-route discrepancy between results and methods should remain attached to this evidence. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Biodistribution at 6 h; EPO expression peaked at 2 d and persisted to 2 weeks; inflammatory readouts at 3 d", "control_type": "PBS/SCI, untargeted EPO@LNP, and LPS-stimulated BV2 controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "T10 cord crushed for 3 s with calibrated 100-g F11020-11 forceps; EPO mRNA-LNP intervention route is described as tail vein in results but local injection before closure in methods", "injury_model": "T10 crush SCI plus LPS-stimulated BV2 inflammation assay", "injury_severity": "Crush injury; 100-g forceps", "intervention_type": "Mannose-modified EPO mRNA lipid nanoparticle (EPO@MLNP) targeting CD206-enriched macrophages/microglia", "methods_summary": "EPO@MLNP showed higher lesion-region expression and microglial enrichment than untargeted LNP, sustained local EPO production, lower BV2 iNOS after LPS, fewer CD86+ microglia, reduced microglial infiltration, and lower plasma TNF-alpha, IL-1beta, and IL-6. The delivery-route discrepancy between results and methods should remain attached to this evidence.", "observation_tracker_ids": ["M3B-O041"], "sex": "Sex not stated in mouse methods; not applicable for BV2", "source_experiment_tracker_id": "M3A-P041-E001", "source_paper_tracker_id": "M3A-P041", "species": "Mouse and BV2 microglial cells", "strain": "C57BL/6 mice, 8 weeks, 25-30 g; BV2 cell line", "tracker_key": "M3A-P041::M3A-P041-E001", "vertebral_level": "T10"}'
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
    'A-layer full text; Full text PMC; Fig. 5-6',
    'Tracker experiment M3A-P041-E002',
    'Extracted details: EPO@MLNP preserved more NeuN+ neurons, reduced lesion area, preserved 5-HT axonal signal near the epicenter, and produced the strongest BMS, stride, hind-paw pressure, speed, and inclined-plane recovery through 28 days. EPO@LNP also showed some benefit, so the results support improved targeting rather than proving that the mannose ligand is solely responsible for efficacy. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "BMS, footprint, CatWalk, inclined-plane, NeuN, lesion area, and 5-HT readouts through 28 days", "control_type": "PBS/SCI and untargeted EPO@LNP controls; MLNP comparison as reported", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "T10 cord crushed for 3 s with calibrated 100-g forceps; designated treatment route is reported inconsistently as tail vein versus local injection", "injury_model": "T10 crush SCI", "injury_severity": "Crush injury; 100-g forceps", "intervention_type": "EPO@MLNP versus EPO@LNP", "methods_summary": "EPO@MLNP preserved more NeuN+ neurons, reduced lesion area, preserved 5-HT axonal signal near the epicenter, and produced the strongest BMS, stride, hind-paw pressure, speed, and inclined-plane recovery through 28 days. EPO@LNP also showed some benefit, so the results support improved targeting rather than proving that the mannose ligand is solely responsible for efficacy.", "observation_tracker_ids": ["M3B-O088"], "sex": "Sex not stated", "source_experiment_tracker_id": "M3A-P041-E002", "source_paper_tracker_id": "M3A-P041", "species": "Mouse SCI model", "strain": "C57BL/6 mice, 8 weeks, 25-30 g", "tracker_key": "M3A-P041::M3A-P041-E002", "vertebral_level": "T10"}'
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
    'A-layer full text; Fig. 1-3; immune-cell single-cell and spatial metabolomics atlas',
    'Tracker experiment M3A-P042-E001',
    'Extracted details: The study profiled 35,799 cells and identified a SCI-enriched Mic2 microglial subset expressing Spp1, Hopx, Lgals3, Anxa2, and Tspo, with wound-healing and adhesion programs. Mic2 localized mainly to dorsal white matter and its spatially enriched region contained taurine; predicted Cd99-Cd99 and Psap-Gpr37l1 interactions increased after SCI. This is a candidate immune-metabolic repair state, not proof that taurine or Mic2 is necessary for recovery; omics samples were separate animals and neuronal information was limited by scRNA-seq. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Injury-versus-sham profiling; exact post-injury sampling day not stated in captured full text", "control_type": "Sham laminectomy; SCI", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Quick-release 50 g clip for 10 seconds", "injury_model": "T1 compression SCI and sham laminectomy", "injury_severity": "Not otherwise graded", "intervention_type": "10X scRNA-seq, Visium spatial transcriptomics, and mass-spectrometry-imaging spatial metabolomics", "methods_summary": "The study profiled 35,799 cells and identified a SCI-enriched Mic2 microglial subset expressing Spp1, Hopx, Lgals3, Anxa2, and Tspo, with wound-healing and adhesion programs. Mic2 localized mainly to dorsal white matter and its spatially enriched region contained taurine; predicted Cd99-Cd99 and Psap-Gpr37l1 interactions increased after SCI. This is a candidate immune-metabolic repair state, not proof that taurine or Mic2 is necessary for recovery; omics samples were separate animals and neuronal information was limited by scRNA-seq.", "observation_tracker_ids": ["M3B-O042"], "sex": "Male", "source_experiment_tracker_id": "M3A-P042-E001", "source_paper_tracker_id": "M3A-P042", "species": "Rat", "strain": "8-week-old male Sprague-Dawley, 200-250 g", "tracker_key": "M3A-P042::M3A-P042-E001", "vertebral_level": "T1"}'
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
    'A-layer full text; Fig. 4-5 and Supplementary Fig. S8; Mac4/c Copalic-acid validation',
    'Tracker experiment M3A-P042-E002',
    'Extracted details: Mac4 was an anti-inflammatory macrophage branch with clustered spatial distribution and copalic-acid enrichment. Copalic acid reduced CD86, CD80, and IL-1beta in LPS-treated BV2 and RAW264.7 cells and increased ARG1 while reducing iNOS after SCI. The paper states mice were used for validation but describes the compression parameters under the rat model, so this species linkage remains unresolved; there was no direct Mac4 depletion or copalic-acid necessity experiment. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "CA cell assay 6 hours; SCI inflammatory validation at 1, 3, and 7 days post-injury", "control_type": "Sham/PBS/vehicle and LPS-only controls as reported", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Rat model described as quick-release 50 g clip for 10 seconds; no device for culture", "injury_model": "T1 compression SCI; LPS inflammatory culture", "injury_severity": "Not otherwise graded", "intervention_type": "Copalic acid 3 micromolar in LPS-treated cultures; 1 mg/kg local injection in reported mouse validation", "methods_summary": "Mac4 was an anti-inflammatory macrophage branch with clustered spatial distribution and copalic-acid enrichment. Copalic acid reduced CD86, CD80, and IL-1beta in LPS-treated BV2 and RAW264.7 cells and increased ARG1 while reducing iNOS after SCI. The paper states mice were used for validation but describes the compression parameters under the rat model, so this species linkage remains unresolved; there was no direct Mac4 depletion or copalic-acid necessity experiment.", "observation_tracker_ids": ["M3B-O089"], "sex": "Male or not applicable", "source_experiment_tracker_id": "M3A-P042-E002", "source_paper_tracker_id": "M3A-P042", "species": "Rat atlas plus BV2/RAW264.7 cultures and mouse validation model as reported", "strain": "Male Sprague-Dawley rats for atlas; BV2 and RAW264.7 cell lines; article states male mice for validation", "tracker_key": "M3A-P042::M3A-P042-E002", "vertebral_level": "T1 for SCI model"}'
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
    'A-layer full text; Full text PMC; in vivo time course and LV-MDK validation',
    'Tracker experiment M3A-P043-E001',
    'Extracted details: LV-MDK increased MDK around microglia, improved BBB and CatWalk gait and MEPs through 42 days, reduced inflammatory mediators and neuronal apoptosis, preserved neurons/axons, and increased CD206-associated reparative microglial features and LRP-1/AKT/mTOR/BDNF signaling. Because treatment was delivered before injury, translational post-injury efficacy remains untested. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "MDK expression time course days 1-28; lentiviral validation day 7; BBB/gait/MEP and tissue outcomes through day 42", "control_type": "Sham, SCI plus LV-NC, SCI plus LV-MDK, and sham plus LV-MDK; blinded behavioral assessment", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Allen impactor, 250 kdyn after T9-T10 laminectomy", "injury_model": "T9-T10 moderate incomplete contusion SCI", "injury_severity": "Moderate incomplete contusion", "intervention_type": "Intrathecal 10 microliters LV-MDK or LV-NC at 1 x 10^9 TU/ml, administered 3 days before SCI", "methods_summary": "LV-MDK increased MDK around microglia, improved BBB and CatWalk gait and MEPs through 42 days, reduced inflammatory mediators and neuronal apoptosis, preserved neurons/axons, and increased CD206-associated reparative microglial features and LRP-1/AKT/mTOR/BDNF signaling. Because treatment was delivered before injury, translational post-injury efficacy remains untested.", "observation_tracker_ids": ["M3B-O043"], "sex": "Female", "source_experiment_tracker_id": "M3A-P043-E001", "source_paper_tracker_id": "M3A-P043", "species": "Rat", "strain": "Adult female Sprague-Dawley, 200-230 g, 9-11 weeks", "tracker_key": "M3A-P043::M3A-P043-E001", "vertebral_level": "T9-T10"}'
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
    'A-layer full text; Full text PMC; BV2 efferocytosis and neuronal-protection mechanism assays',
    'Tracker experiment M3A-P043-E002',
    'Extracted details: MDK restored LPS-impaired efferocytosis, increased LRP-1 and Rac1, activated AKT/mTOR and BDNF, increased IL-10/TGF-beta/CD206, and reduced IL-1beta/TNF-alpha/IL-6 and neuronal apoptosis. RAP abolished the efferocytic, anti-inflammatory, and neuroprotective effects, supporting an MDK-LRP-1 mechanism in vitro; LRP-1 necessity was not directly tested in vivo. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Efferocytosis, cytokines, LRP-1/Rac1, AKT/mTOR/BDNF, polarization, and neuronal apoptosis readouts", "control_type": "Untreated, LPS, MDK, and LPS+MDK groups with RAP blockade; apoptotic-neuron and microglia controls as reported", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "1 microgram/ml LPS plus 200 ng/ml recombinant human MDK for 12 h; receptor-associated protein added at 50 micromolar 30 min before treatment", "injury_model": "LPS-impaired microglial efferocytosis and apoptotic-neuron co-culture assays", "injury_severity": "In vitro inflammatory/efferocytosis model", "intervention_type": "Recombinant MDK with pharmacologic LRP-1 inhibition", "methods_summary": "MDK restored LPS-impaired efferocytosis, increased LRP-1 and Rac1, activated AKT/mTOR and BDNF, increased IL-10/TGF-beta/CD206, and reduced IL-1beta/TNF-alpha/IL-6 and neuronal apoptosis. RAP abolished the efferocytic, anti-inflammatory, and neuroprotective effects, supporting an MDK-LRP-1 mechanism in vitro; LRP-1 necessity was not directly tested in vivo.", "observation_tracker_ids": ["M3B-O090"], "sex": "Not applicable in vitro", "source_experiment_tracker_id": "M3A-P043-E002", "source_paper_tracker_id": "M3A-P043", "species": "BV2 microglia and primary fetal-rat cortical neurons", "strain": "BV2 cell line; embryonic Sprague-Dawley rat neurons", "tracker_key": "M3A-P043::M3A-P043-E002", "vertebral_level": "Not applicable"}'
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
    'Extracted details: Primary intervention or mechanism experiment for A reparative neutrophil subpopulation accelerates spinal cord regeneration in zebrafish by controlling macrophage inflammation via Il-4.; first-pass row captures macrophage/microglia polarization signaling in zebrafish sci model at abstract/source-title level. Extraction status: YES (abstract-level)',
    '{"chronicity_dpi_wpi": "UNKNOWN", "control_type": "Injury / vehicle / wild-type / comparator as reported", "experiment_extracted": "YES (abstract-level)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "UNKNOWN", "intervention_type": "Macrophage/microglia polarization signaling", "methods_summary": "Primary intervention or mechanism experiment for A reparative neutrophil subpopulation accelerates spinal cord regeneration in zebrafish by controlling macrophage inflammation via Il-4.; first-pass row captures macrophage/microglia polarization signaling in zebrafish sci model at abstract/source-title level.", "observation_tracker_ids": ["M3B-O044"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M3A-P044-E001", "source_paper_tracker_id": "M3A-P044", "species": "Zebrafish SCI model", "strain": "UNKNOWN", "tracker_key": "M3A-P044::M3A-P044-E001", "vertebral_level": "UNKNOWN"}'
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
    'Extracted details: Outcome/mechanistic validation row for A reparative neutrophil subpopulation accelerates spinal cord regeneration in zebrafish by controlling macrophage inflammation via Il-4.; first-pass row captures macrophage/microglia polarization signaling in zebrafish sci model at abstract/source-title level. Extraction status: YES (abstract-level)',
    '{"chronicity_dpi_wpi": "UNKNOWN", "control_type": "Comparator/control arm as reported", "experiment_extracted": "YES (abstract-level)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "UNKNOWN", "intervention_type": "Mechanistic outcome assessment after macrophage/microglia polarization signaling", "methods_summary": "Outcome/mechanistic validation row for A reparative neutrophil subpopulation accelerates spinal cord regeneration in zebrafish by controlling macrophage inflammation via Il-4.; first-pass row captures macrophage/microglia polarization signaling in zebrafish sci model at abstract/source-title level.", "observation_tracker_ids": ["M3B-O091"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M3A-P044-E002", "source_paper_tracker_id": "M3A-P044", "species": "Zebrafish SCI model", "strain": "UNKNOWN", "tracker_key": "M3A-P044::M3A-P044-E002", "vertebral_level": "UNKNOWN"}'
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
    'A-layer full text; Full text PMC',
    'Tracker experiment M3A-P045-E001',
    'Extracted details: scRNA-seq identified Spp1+Fn1+ macrophages as the major CXCL4 source; CXCL4 was increased after SCI, pericytes expressed CXCR3, and exogenous CXCL4 induced pericyte-to-myofibroblast transition through CXCR3/PI3K/Akt in vitro. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Post-injury fibrotic remodeling", "control_type": "Vehicle, CXCL4-neutralizing antibody, and PI3K inhibitor controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "SCI as reported", "intervention_type": "CXCL4/CXCR3/PI3K-Akt PMT mechanism", "methods_summary": "scRNA-seq identified Spp1+Fn1+ macrophages as the major CXCL4 source; CXCL4 was increased after SCI, pericytes expressed CXCR3, and exogenous CXCL4 induced pericyte-to-myofibroblast transition through CXCR3/PI3K/Akt in vitro.", "observation_tracker_ids": ["M3B-O045"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M3A-P045-E001", "source_paper_tracker_id": "M3A-P045", "species": "Mouse SCI model plus pericytes", "strain": "UNKNOWN", "tracker_key": "M3A-P045::M3A-P045-E001", "vertebral_level": "UNKNOWN"}'
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
    'A-layer full text; Full text PMC',
    'Tracker experiment M3A-P045-E002',
    'Extracted details: Full-text result supports a macrophage-to-pericyte fibrotic relay and an intervention-sensitive boundary. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Post-injury intrathecal blockade and functional follow-up", "control_type": "Vehicle, CXCL4-neutralizing antibody, and PI3K inhibitor controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Crush model as reported", "injury_model": "Complete spinal cord crush as reported", "injury_severity": "SCI as reported", "intervention_type": "Blocking CXCL4 or PI3K reduced PMT and fibrotic scar deposition, enhanced corticospinal and serotonergic axon regeneration, and improved BMS and footprint outcomes. MAFB was linked to CXCL4 expression in the Spp1+Fn1+ macrophage subset.", "methods_summary": "Full-text result supports a macrophage-to-pericyte fibrotic relay and an intervention-sensitive boundary.", "observation_tracker_ids": ["M3B-O092"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M3A-P045-E002", "source_paper_tracker_id": "M3A-P045", "species": "Mouse SCI model", "strain": "UNKNOWN", "tracker_key": "M3A-P045::M3A-P045-E002", "vertebral_level": "UNKNOWN"}'
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
    'A-layer full text; Full text PMC',
    'Tracker experiment M3A-P046-E001',
    'Extracted details: Macrophages were a major source of activated TGF-beta1 after SCI; macrophage-lineage TGF-beta1 recruited MSCs and promoted fibroblast differentiation, while TGF-beta signaling in resident pericytes also drove fibroblast formation at the blood-spinal cord barrier. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Adult versus neonatal recovery comparison", "control_type": "Conditional macrophage-lineage Tgfbr1/Tgfb1, pericyte Tgfbr2, antibody, and neonatal controls", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "SCI as reported", "intervention_type": "TGF-beta pathway genetic and antibody interruption", "methods_summary": "Macrophages were a major source of activated TGF-beta1 after SCI; macrophage-lineage TGF-beta1 recruited MSCs and promoted fibroblast differentiation, while TGF-beta signaling in resident pericytes also drove fibroblast formation at the blood-spinal cord barrier.", "observation_tracker_ids": ["M3B-O046"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M3A-P046-E001", "source_paper_tracker_id": "M3A-P046", "species": "Mouse SCI model", "strain": "UNKNOWN", "tracker_key": "M3A-P046::M3A-P046-E001", "vertebral_level": "UNKNOWN"}'
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
    'A-layer full text; Full text PMC',
    'Tracker experiment M3A-P046-E002',
    'Extracted details: Macrophage or pericyte pathway interruption reduced fibrotic scar and improved functional recovery; neonatal mice recovered scarlessly with no detectable active TGF-beta at the injury site, defining a developmental boundary rather than a universal anti-TGF-beta rule. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "Functional recovery follow-up; neonatal scarless comparator", "control_type": "Genetic controls, systemic TGF-beta-neutralizing antibody, and neonatal SCI comparator", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "UNKNOWN", "injury_model": "Experimental SCI", "injury_severity": "SCI as reported", "intervention_type": "TGF-beta neutralization and developmental scarless-repair comparison", "methods_summary": "Macrophage or pericyte pathway interruption reduced fibrotic scar and improved functional recovery; neonatal mice recovered scarlessly with no detectable active TGF-beta at the injury site, defining a developmental boundary rather than a universal anti-TGF-beta rule.", "observation_tracker_ids": ["M3B-O093"], "sex": "UNKNOWN", "source_experiment_tracker_id": "M3A-P046-E002", "source_paper_tracker_id": "M3A-P046", "species": "Mouse SCI model", "strain": "UNKNOWN", "tracker_key": "M3A-P046::M3A-P046-E002", "vertebral_level": "UNKNOWN"}'
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
    'A-layer full text; Full text PMC; in vivo transplantation and pain-recovery assays',
    'Tracker experiment M3A-P047-E001',
    'Extracted details: OEC transplantation improved BBB recovery, mechanical withdrawal threshold, and thermal withdrawal latency, reduced lesion cavitation and GFAP-associated activation, and increased NF200 axon-associated signal. It reduced H3Cit/CD68 MET-associated staining and NKCC1 in spinal cord and L4-L6 DRG. The phenotype supports analgesic and motor benefit but does not prove MET/NKCC1 causality. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "OECs injected 30 min after injury; BBB and mechanical/thermal sensitivity days 0-35; tissue at 5 weeks", "control_type": "Sham, SCI plus OEC culture medium, and SCI plus OEC transplantation; blinded behavioral scoring", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "Infinite Horizons impactor, 150 kdyn, 2.5-mm tip after T9-T10 laminectomy", "injury_model": "T10 incomplete contusive SCI", "injury_severity": "Incomplete contusion", "intervention_type": "Four-site intraspinal transplantation of 4 microliters OEC suspension at 1 x 10^5 cells/microliter, 1 microliter per site", "methods_summary": "OEC transplantation improved BBB recovery, mechanical withdrawal threshold, and thermal withdrawal latency, reduced lesion cavitation and GFAP-associated activation, and increased NF200 axon-associated signal. It reduced H3Cit/CD68 MET-associated staining and NKCC1 in spinal cord and L4-L6 DRG. The phenotype supports analgesic and motor benefit but does not prove MET/NKCC1 causality.", "observation_tracker_ids": ["M3B-O047"], "sex": "Female", "source_experiment_tracker_id": "M3A-P047-E001", "source_paper_tracker_id": "M3A-P047", "species": "Rat", "strain": "Female Sprague-Dawley, 8 weeks, 260+/-15 g", "tracker_key": "M3A-P047::M3A-P047-E001", "vertebral_level": "T10"}'
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
    'A-layer full text; Full text PMC; OEC-conditioned-medium macrophage assay',
    'Tracker experiment M3A-P047-E002',
    'Extracted details: OEC-conditioned medium suppressed TNF-alpha-induced H3Cit/CD68 MET markers and reduced NKCC1 expression in RAW264.7 macrophages, supporting a secreted-factor mechanism. The active OEC components were not identified, and no in vivo MET or NKCC1 blockade/overexpression was performed. Extraction status: YES (full-text upgraded)',
    '{"chronicity_dpi_wpi": "H3Cit, CD68, and NKCC1 by staining and western blot", "control_type": "Standard medium, TNF-alpha, and TNF-alpha plus OEC-conditioned medium", "experiment_extracted": "YES (full-text upgraded)", "injury_device": "TNF-alpha stimulation followed by standard medium or 48-h OEC-conditioned medium", "injury_model": "TNF-alpha-induced macrophage extracellular-trap formation", "injury_severity": "In vitro inflammatory/MET model", "intervention_type": "Cell-free OEC-conditioned medium", "methods_summary": "OEC-conditioned medium suppressed TNF-alpha-induced H3Cit/CD68 MET markers and reduced NKCC1 expression in RAW264.7 macrophages, supporting a secreted-factor mechanism. The active OEC components were not identified, and no in vivo MET or NKCC1 blockade/overexpression was performed.", "observation_tracker_ids": ["M3B-O094"], "sex": "Not applicable in vitro", "source_experiment_tracker_id": "M3A-P047-E002", "source_paper_tracker_id": "M3A-P047", "species": "RAW264.7 macrophages and primary rat OECs", "strain": "RAW264.7 cell line; OECs from Sprague-Dawley olfactory bulbs", "tracker_key": "M3A-P047::M3A-P047-E002", "vertebral_level": "Not applicable"}'
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
    'Full-text source localization for M3A-P001-E001 confirms the curated PLX5622 1200 ppm chow for pre-injury microglial and myeloid depletion experiment in Mouse. Methods/readouts recorded in the A-layer: Flow cytometry and qPCR at 2 dpi quantified CD45int microglia, infiltrating monocytes, neutrophils, and ROS at the lesion epicenter.',
    'qualitative',
    'qPCR / RT-PCR / mRNA assay; flow cytometry / FACS; behavioral / functional recovery assay',
    'Full-text source localization for M3A-P001-E001 confirms the curated PLX5622 1200 ppm chow for pre-injury microglial and myeloid depletion experiment in Mouse. Methods/readouts recorded in the A-layer: Flow cytometry and qPCR at 2 dpi quantified CD45int microglia, infiltrating monocytes, neutrophils, and ROS at the lesion epicenter.',
    'full-text source localization for m3a-p001-e001 confirms the curated plx5622 1200 ppm chow for pre-injury microglial and myeloid depletion experiment in mouse. methods/readouts recorded in the a-layer: flow cytometry and qpcr at 2 dpi quantified cd45int microglia, infiltrating monocytes, neutrophils, and ros at the lesion epicenter.',
    'Module 3A full-text extraction; Full text PMC; Fig. 1-2',
    'A-layer full text; Full text PMC; Fig. 1-2',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P001-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P001-E001", "measurement_method_inference": "qPCR / RT-PCR / mRNA assay; flow cytometry / FACS; behavioral / functional recovery assay", "paper_tracker_id": "M3A-P001", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T001", "tracker_id": "M3B-O001"}'
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
    'Full-text source localization for M3A-P002-E001 confirms the curated Plexin-B2 induction and myeloid-cell-specific deletion experiment in Mouse. Methods/readouts recorded in the A-layer: INTACT RNA-seq, immunostaining, and targeted validation showed injury-activated microglia/macrophages upregulated Plexin-B2 and axon-guidance, motility, and matrix-interaction programs.',
    'qualitative',
    'bulk transcriptomics / GEO dataset',
    'Full-text source localization for M3A-P002-E001 confirms the curated Plexin-B2 induction and myeloid-cell-specific deletion experiment in Mouse. Methods/readouts recorded in the A-layer: INTACT RNA-seq, immunostaining, and targeted validation showed injury-activated microglia/macrophages upregulated Plexin-B2 and axon-guidance, motility, and matrix-interaction programs.',
    'full-text source localization for m3a-p002-e001 confirms the curated plexin-b2 induction and myeloid-cell-specific deletion experiment in mouse. methods/readouts recorded in the a-layer: intact rna-seq, immunostaining, and targeted validation showed injury-activated microglia/macrophages upregulated plexin-b2 and axon-guidance, motility, and matrix-interaction programs.',
    'Module 3A full-text extraction; Full text PMC; Fig. 1-2',
    'A-layer full text; Full text PMC; Fig. 1-2',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P002-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P002-E001", "measurement_method_inference": "bulk transcriptomics / GEO dataset", "paper_tracker_id": "M3A-P002", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T002", "tracker_id": "M3B-O002"}'
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
    'Full-text source localization for M3A-P003-E001 confirms the curated GW2580 0.1% incorporated into chow experiment in Mouse. Methods/readouts recorded in the A-layer: Chronic CSF1R blockade selectively reduced SCI-induced microglial proliferation and IBA1 response without changing the non-injured microglial response.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Full-text source localization for M3A-P003-E001 confirms the curated GW2580 0.1% incorporated into chow experiment in Mouse. Methods/readouts recorded in the A-layer: Chronic CSF1R blockade selectively reduced SCI-induced microglial proliferation and IBA1 response without changing the non-injured microglial response.',
    'full-text source localization for m3a-p003-e001 confirms the curated gw2580 0.1% incorporated into chow experiment in mouse. methods/readouts recorded in the a-layer: chronic csf1r blockade selectively reduced sci-induced microglial proliferation and iba1 response without changing the non-injured microglial response.',
    'Module 3A full-text extraction; Full text PMC; Fig. 1-3',
    'A-layer full text; Full text PMC; Fig. 1-3',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P003-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P003-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M3A-P003", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T001", "tracker_id": "M3B-O003"}'
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
    'Full-text source localization for M3A-P004-E001 confirms the curated HMGB1 inhibition with glycyrrhizin or RAGE inhibition with FPS-ZM1 experiment in Rat. Methods/readouts recorded in the A-layer: HMGB1 release from necroptotic astrocytes and HMGB1 stimulation of microglia in vitro were linked to RAGE-NF-kB pro-inflammatory polarization; qRT-PCR, immunostaining, western blot, and ELISA assessed the pathway.',
    'qualitative',
    'western blot / immunoblot; ELISA / cytokine protein assay',
    'Full-text source localization for M3A-P004-E001 confirms the curated HMGB1 inhibition with glycyrrhizin or RAGE inhibition with FPS-ZM1 experiment in Rat. Methods/readouts recorded in the A-layer: HMGB1 release from necroptotic astrocytes and HMGB1 stimulation of microglia in vitro were linked to RAGE-NF-kB pro-inflammatory polarization; qRT-PCR, immunostaining, western blot, and ELISA assessed the pathway.',
    'full-text source localization for m3a-p004-e001 confirms the curated hmgb1 inhibition with glycyrrhizin or rage inhibition with fps-zm1 experiment in rat. methods/readouts recorded in the a-layer: hmgb1 release from necroptotic astrocytes and hmgb1 stimulation of microglia in vitro were linked to rage-nf-kb pro-inflammatory polarization; qrt-pcr, immunostaining, western blot, and elisa assessed the pathway.',
    'Module 3A full-text extraction; Full text PMC; in vitro and Fig. 1-4',
    'A-layer full text; Full text PMC; in vitro and Fig. 1-4',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P004-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P004-E001", "measurement_method_inference": "western blot / immunoblot; ELISA / cytokine protein assay", "paper_tracker_id": "M3A-P004", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T003", "tracker_id": "M3B-O004"}'
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
    'Full-text source localization for M3A-P005-E001 confirms the curated DNase I 5 mg/kg tail vein to limit macrophage extracellular traps experiment in Rat. Methods/readouts recorded in the A-layer: CitH3/CD68-positive macrophage extracellular traps were detected in the lesion; DNase I reduced trap-associated M1-like polarization, tissue injury, and motor deficits.',
    'qualitative',
    NULL,
    'Full-text source localization for M3A-P005-E001 confirms the curated DNase I 5 mg/kg tail vein to limit macrophage extracellular traps experiment in Rat. Methods/readouts recorded in the A-layer: CitH3/CD68-positive macrophage extracellular traps were detected in the lesion; DNase I reduced trap-associated M1-like polarization, tissue injury, and motor deficits.',
    'full-text source localization for m3a-p005-e001 confirms the curated dnase i 5 mg/kg tail vein to limit macrophage extracellular traps experiment in rat. methods/readouts recorded in the a-layer: cith3/cd68-positive macrophage extracellular traps were detected in the lesion; dnase i reduced trap-associated m1-like polarization, tissue injury, and motor deficits.',
    'Module 3A full-text extraction; Full text PMC; Fig. 1-4',
    'A-layer full text; Full text PMC; Fig. 1-4',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P005-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P005-E001", "measurement_method_inference": null, "paper_tracker_id": "M3A-P005", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T008", "tracker_id": "M3B-O005"}'
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
    'Full-text source localization for M3A-P006-E001 confirms the curated Intrathecal iPSC-NSC-derived exosomes at 20 ug/uL experiment in Mouse. Methods/readouts recorded in the A-layer: Exosomes reduced IBA1-positive GSDMD/Caspase-1 pyroptosis, preserved myelin, increased NF200 and NeuN outcomes, and improved BMS, swimming, footprint, and MEP recovery.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Full-text source localization for M3A-P006-E001 confirms the curated Intrathecal iPSC-NSC-derived exosomes at 20 ug/uL experiment in Mouse. Methods/readouts recorded in the A-layer: Exosomes reduced IBA1-positive GSDMD/Caspase-1 pyroptosis, preserved myelin, increased NF200 and NeuN outcomes, and improved BMS, swimming, footprint, and MEP recovery.',
    'full-text source localization for m3a-p006-e001 confirms the curated intrathecal ipsc-nsc-derived exosomes at 20 ug/ul experiment in mouse. methods/readouts recorded in the a-layer: exosomes reduced iba1-positive gsdmd/caspase-1 pyroptosis, preserved myelin, increased nf200 and neun outcomes, and improved bms, swimming, footprint, and mep recovery.',
    'Module 3A full-text extraction; Full text PMC; Fig. 1-7',
    'A-layer full text; Full text PMC; Fig. 1-7',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P006-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P006-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M3A-P006", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T004", "tracker_id": "M3B-O006"}'
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
    'Full-text source localization for M3A-P008-E001 confirms the curated N-lactoyl-phenylalanine 20 mg/kg tail vein immediately after injury and daily for 7 d experiment in Mouse SCI model. Methods/readouts recorded in the A-layer: L-P reduced lesion lipid accumulation and lipid droplets in Iba1+ cells, shifted microglia/macrophages from CD86+ M1-like toward CD163+ M2-like states, activated AMPK-PGC1alpha-PPARgamma, reduced CD36 and PLIN2, suppressed inflammatory signaling, and improved BMS and locomotor outcomes.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Full-text source localization for M3A-P008-E001 confirms the curated N-lactoyl-phenylalanine 20 mg/kg tail vein immediately after injury and daily for 7 d experiment in Mouse SCI model. Methods/readouts recorded in the A-layer: L-P reduced lesion lipid accumulation and lipid droplets in Iba1+ cells, shifted microglia/macrophages from CD86+ M1-like toward CD163+ M2-like states, activated AMPK-PGC1alpha-PPARgamma, reduced CD36 and PLIN2, suppressed inflammatory signaling, and improved BMS and locomotor outcomes.',
    'full-text source localization for m3a-p008-e001 confirms the curated n-lactoyl-phenylalanine 20 mg/kg tail vein immediately after injury and daily for 7 d experiment in mouse sci model. methods/readouts recorded in the a-layer: l-p reduced lesion lipid accumulation and lipid droplets in iba1+ cells, shifted microglia/macrophages from cd86+ m1-like toward cd163+ m2-like states, activated ampk-pgc1alpha-ppargamma, reduced cd36 and plin2, suppressed inflammatory signaling, and improved bms and locomotor outcomes.',
    'Module 3A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P008-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P008-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M3A-P008", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T005", "tracker_id": "M3B-O008"}'
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
    'Full-text source localization for M3A-P010-E001 confirms the curated Dual-drug sequential delivery hydrogel (DSDH) with minocycline-loaded fucose nanoparticles and IL-4-biotin/streptavidin complexes experiment in Rat. Methods/readouts recorded in the A-layer: DSDH reduced iNOS and increased CD206/Arg1, improved BBB to about 6.2 at 28 days versus about 2.5-2.7 in untreated/non-DSDH groups, improved footprint and MEPs, reduced lesion cavity and GFAP, and increased Tuj1, neurofilament, and synapsin-I signals.',
    'qualitative',
    'barrier / permeability / endothelial assay',
    'Full-text source localization for M3A-P010-E001 confirms the curated Dual-drug sequential delivery hydrogel (DSDH) with minocycline-loaded fucose nanoparticles and IL-4-biotin/streptavidin complexes experiment in Rat. Methods/readouts recorded in the A-layer: DSDH reduced iNOS and increased CD206/Arg1, improved BBB to about 6.2 at 28 days versus about 2.5-2.7 in untreated/non-DSDH groups, improved footprint and MEPs, reduced lesion cavity and GFAP, and increased Tuj1, neurofilament, and synapsin-I signals.',
    'full-text source localization for m3a-p010-e001 confirms the curated dual-drug sequential delivery hydrogel (dsdh) with minocycline-loaded fucose nanoparticles and il-4-biotin/streptavidin complexes experiment in rat. methods/readouts recorded in the a-layer: dsdh reduced inos and increased cd206/arg1, improved bbb to about 6.2 at 28 days versus about 2.5-2.7 in untreated/non-dsdh groups, improved footprint and meps, reduced lesion cavity and gfap, and increased tuj1, neurofilament, and synapsin-i signals.',
    'Module 3A full-text extraction; Full text PMC; Fig. 3-5',
    'A-layer full text; Full text PMC; Fig. 3-5',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P010-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P010-E001", "measurement_method_inference": "barrier / permeability / endothelial assay", "paper_tracker_id": "M3A-P010", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T003", "tracker_id": "M3B-O010"}'
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
    'Full-text source localization for M3A-P015-E001 confirms the curated Atractylenolide III 5 mg/kg by gavage 3 h after surgery and daily until sacrifice experiment in Rat SCI model. Methods/readouts recorded in the A-layer: ATL-III improved BBB scores from 14-42 dpi, reduced grid-walk errors, improved footprint patterns, reduced lesion area and myelin disruption, and increased surviving neurons. It reduced M1-associated iNOS, TNF-alpha, IL-1beta and IL-6 while increasing Arg1 and IL-10 and shifting spinal microglia/macrophages toward an M2-associated phenotype.',
    'qualitative',
    'ELISA / cytokine protein assay; barrier / permeability / endothelial assay',
    'Full-text source localization for M3A-P015-E001 confirms the curated Atractylenolide III 5 mg/kg by gavage 3 h after surgery and daily until sacrifice experiment in Rat SCI model. Methods/readouts recorded in the A-layer: ATL-III improved BBB scores from 14-42 dpi, reduced grid-walk errors, improved footprint patterns, reduced lesion area and myelin disruption, and increased surviving neurons. It reduced M1-associated iNOS, TNF-alpha, IL-1beta and IL-6 while increasing Arg1 and IL-10 and shifting spinal microglia/macrophages toward an M2-associated phenotype.',
    'full-text source localization for m3a-p015-e001 confirms the curated atractylenolide iii 5 mg/kg by gavage 3 h after surgery and daily until sacrifice experiment in rat sci model. methods/readouts recorded in the a-layer: atl-iii improved bbb scores from 14-42 dpi, reduced grid-walk errors, improved footprint patterns, reduced lesion area and myelin disruption, and increased surviving neurons. it reduced m1-associated inos, tnf-alpha, il-1beta and il-6 while increasing arg1 and il-10 and shifting spinal microglia/macrophages toward an m2-associated phenotype.',
    'Module 3A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P015-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P015-E001", "measurement_method_inference": "ELISA / cytokine protein assay; barrier / permeability / endothelial assay", "paper_tracker_id": "M3A-P015", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T003", "tracker_id": "M3B-O015"}'
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
    'Full-text source localization for M3A-P016-E001 confirms the curated CCR2 enrichment plus transient multimodal mRNA delivery experiment in Mouse peritoneal macrophages; newborn Sprague-Dawley rat DRG and PC12 cells. Methods/readouts recorded in the A-layer: Electroporation produced viable engineered macrophages expressing ANXA1, GDNF, and CTGF without a marked CD86/CD206 shift and sustained secretion through day 14. Conditioned medium protected PC12 cells and DRG explants from oxidative-stress injury and promoted neurite outgrowth, supporting a paracrine neuroprotective/regenerative effect rather than proving contact-dependent action.',
    'qualitative',
    'qPCR / RT-PCR / mRNA assay; single-cell RNA-seq / cell-state atlas',
    'Full-text source localization for M3A-P016-E001 confirms the curated CCR2 enrichment plus transient multimodal mRNA delivery experiment in Mouse peritoneal macrophages; newborn Sprague-Dawley rat DRG and PC12 cells. Methods/readouts recorded in the A-layer: Electroporation produced viable engineered macrophages expressing ANXA1, GDNF, and CTGF without a marked CD86/CD206 shift and sustained secretion through day 14. Conditioned medium protected PC12 cells and DRG explants from oxidative-stress injury and promoted neurite outgrowth, supporting a paracrine neuroprotective/regenerative effect rather than proving contact-dependent action.',
    'full-text source localization for m3a-p016-e001 confirms the curated ccr2 enrichment plus transient multimodal mrna delivery experiment in mouse peritoneal macrophages; newborn sprague-dawley rat drg and pc12 cells. methods/readouts recorded in the a-layer: electroporation produced viable engineered macrophages expressing anxa1, gdnf, and ctgf without a marked cd86/cd206 shift and sustained secretion through day 14. conditioned medium protected pc12 cells and drg explants from oxidative-stress injury and promoted neurite outgrowth, supporting a paracrine neuroprotective/regenerative effect rather than proving contact-dependent action.',
    'Module 3A full-text extraction; Full text PMC; engineering, secretion, and conditioned-medium assays',
    'A-layer full text; Full text PMC; engineering, secretion, and conditioned-medium assays',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P016-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P016-E001", "measurement_method_inference": "qPCR / RT-PCR / mRNA assay; single-cell RNA-seq / cell-state atlas", "paper_tracker_id": "M3A-P016", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T006", "tracker_id": "M3B-O016"}'
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
    'Full-text source localization for M3A-P017-E001 confirms the curated PLX5622 1200 ppm chow during the subacute phase experiment in Rat. Methods/readouts recorded in the A-layer: Delayed PLX5622 did not change elevated-plus-maze open-arm time, light-dark entries, open-field exploration, or locomotor activity relative to SCI controls. The result argues against a detectable anxiety or locomotor effect under this dosing and partial-depletion regimen, but does not establish that microglia are behaviorally irrelevant.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Full-text source localization for M3A-P017-E001 confirms the curated PLX5622 1200 ppm chow during the subacute phase experiment in Rat. Methods/readouts recorded in the A-layer: Delayed PLX5622 did not change elevated-plus-maze open-arm time, light-dark entries, open-field exploration, or locomotor activity relative to SCI controls. The result argues against a detectable anxiety or locomotor effect under this dosing and partial-depletion regimen, but does not establish that microglia are behaviorally irrelevant.',
    'full-text source localization for m3a-p017-e001 confirms the curated plx5622 1200 ppm chow during the subacute phase experiment in rat. methods/readouts recorded in the a-layer: delayed plx5622 did not change elevated-plus-maze open-arm time, light-dark entries, open-field exploration, or locomotor activity relative to sci controls. the result argues against a detectable anxiety or locomotor effect under this dosing and partial-depletion regimen, but does not establish that microglia are behaviorally irrelevant.',
    'Module 3A full-text extraction; Full text PMC; Fig. 1-2',
    'A-layer full text; Full text PMC; Fig. 1-2',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P017-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P017-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M3A-P017", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T001", "tracker_id": "M3B-O017"}'
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
    'Full-text source localization for M3A-P020-E001 confirms the curated PLX5622 1,200 ppm chow for 9, 14, or 21 d beginning 7-11 weeks after injury experiment in Mouse SCI model. Methods/readouts recorded in the A-layer: Chronic PLX depleted Iba1+ microglia/macrophages and reduced inflammatory transcriptional signatures. Axon density within the lesion increased after 14 d PLX, supporting sustained chronic inflammation as a barrier to regeneration of selected axon populations.',
    'qualitative',
    'qPCR / RT-PCR / mRNA assay; barrier / permeability / endothelial assay; behavioral / functional recovery assay',
    'Full-text source localization for M3A-P020-E001 confirms the curated PLX5622 1,200 ppm chow for 9, 14, or 21 d beginning 7-11 weeks after injury experiment in Mouse SCI model. Methods/readouts recorded in the A-layer: Chronic PLX depleted Iba1+ microglia/macrophages and reduced inflammatory transcriptional signatures. Axon density within the lesion increased after 14 d PLX, supporting sustained chronic inflammation as a barrier to regeneration of selected axon populations.',
    'full-text source localization for m3a-p020-e001 confirms the curated plx5622 1,200 ppm chow for 9, 14, or 21 d beginning 7-11 weeks after injury experiment in mouse sci model. methods/readouts recorded in the a-layer: chronic plx depleted iba1+ microglia/macrophages and reduced inflammatory transcriptional signatures. axon density within the lesion increased after 14 d plx, supporting sustained chronic inflammation as a barrier to regeneration of selected axon populations.',
    'Module 3A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P020-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P020-E001", "measurement_method_inference": "qPCR / RT-PCR / mRNA assay; barrier / permeability / endothelial assay; behavioral / functional recovery assay", "paper_tracker_id": "M3A-P020", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T001", "tracker_id": "M3B-O020"}'
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
    'Full-text source localization for M3A-P022-E001 confirms the curated Early beta2-adrenergic receptor agonist treatment pharmacologically inhibited microglial activation and shifted the post-SCI scar toward a homeostatic state. experiment in Mouse SCI model. Methods/readouts recorded in the A-layer: Beta2-adrenergic agonist intervention tested after complete SCI, with lesion microenvironment and microglial state as primary readouts.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Full-text source localization for M3A-P022-E001 confirms the curated Early beta2-adrenergic receptor agonist treatment pharmacologically inhibited microglial activation and shifted the post-SCI scar toward a homeostatic state. experiment in Mouse SCI model. Methods/readouts recorded in the A-layer: Beta2-adrenergic agonist intervention tested after complete SCI, with lesion microenvironment and microglial state as primary readouts.',
    'full-text source localization for m3a-p022-e001 confirms the curated early beta2-adrenergic receptor agonist treatment pharmacologically inhibited microglial activation and shifted the post-sci scar toward a homeostatic state. experiment in mouse sci model. methods/readouts recorded in the a-layer: beta2-adrenergic agonist intervention tested after complete sci, with lesion microenvironment and microglial state as primary readouts.',
    'Module 3A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P022-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P022-E001", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M3A-P022", "quantitative": "YES", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T001", "tracker_id": "M3B-O022"}'
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
    'Full-text source localization for M3A-P024-E001 confirms the curated Continuous intraperitoneal clodronate liposomes for macrophage depletion; anti-C1q antibody or IgG for synapse validation experiment in Mouse SCI model and integrated single-cell atlas. Methods/readouts recorded in the A-layer: Clodronate depletion of blood-derived macrophages improved BMS, swimming, and inclined-plate performance at 28 dpi. Integrated single-cell data identified phagocytic, remodeling, and persistent lipid-laden foam-cell states, with foam cells emerging by 5 dpi and persisting into chronic SCI.',
    'qualitative',
    'single-cell RNA-seq / cell-state atlas',
    'Full-text source localization for M3A-P024-E001 confirms the curated Continuous intraperitoneal clodronate liposomes for macrophage depletion; anti-C1q antibody or IgG for synapse validation experiment in Mouse SCI model and integrated single-cell atlas. Methods/readouts recorded in the A-layer: Clodronate depletion of blood-derived macrophages improved BMS, swimming, and inclined-plate performance at 28 dpi. Integrated single-cell data identified phagocytic, remodeling, and persistent lipid-laden foam-cell states, with foam cells emerging by 5 dpi and persisting into chronic SCI.',
    'full-text source localization for m3a-p024-e001 confirms the curated continuous intraperitoneal clodronate liposomes for macrophage depletion; anti-c1q antibody or igg for synapse validation experiment in mouse sci model and integrated single-cell atlas. methods/readouts recorded in the a-layer: clodronate depletion of blood-derived macrophages improved bms, swimming, and inclined-plate performance at 28 dpi. integrated single-cell data identified phagocytic, remodeling, and persistent lipid-laden foam-cell states, with foam cells emerging by 5 dpi and persisting into chronic sci.',
    'Module 3A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P024-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P024-E001", "measurement_method_inference": "single-cell RNA-seq / cell-state atlas", "paper_tracker_id": "M3A-P024", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T005", "tracker_id": "M3B-O024"}'
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
    'Full-text source localization for M3A-P025-E001 confirms the curated TREM2 was localized mainly to Iba1+ macrophages/microglia; TREM2 knockout impaired myelin-debris engulfment and degradation, increased foamy macrophages, and reduced DAM activation through the PI3K/AKT pathway. experiment in Mouse SCI model. Methods/readouts recorded in the A-layer: Full-text intervention and knockout design separates debris-clearance benefit from later scar/inflammation liability.',
    'qualitative',
    'pathway activity / phospho-signaling assay; genetic perturbation / knockdown assay',
    'Full-text source localization for M3A-P025-E001 confirms the curated TREM2 was localized mainly to Iba1+ macrophages/microglia; TREM2 knockout impaired myelin-debris engulfment and degradation, increased foamy macrophages, and reduced DAM activation through the PI3K/AKT pathway. experiment in Mouse SCI model. Methods/readouts recorded in the A-layer: Full-text intervention and knockout design separates debris-clearance benefit from later scar/inflammation liability.',
    'full-text source localization for m3a-p025-e001 confirms the curated trem2 was localized mainly to iba1+ macrophages/microglia; trem2 knockout impaired myelin-debris engulfment and degradation, increased foamy macrophages, and reduced dam activation through the pi3k/akt pathway. experiment in mouse sci model. methods/readouts recorded in the a-layer: full-text intervention and knockout design separates debris-clearance benefit from later scar/inflammation liability.',
    'Module 3A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P025-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P025-E001", "measurement_method_inference": "pathway activity / phospho-signaling assay; genetic perturbation / knockdown assay", "paper_tracker_id": "M3A-P025", "quantitative": "YES", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T005", "tracker_id": "M3B-O025"}'
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
    'Full-text source localization for M3A-P026-E001 confirms the curated Human metabolic profiling and mouse macrophage H3K9la mapping experiment in Mouse SCI model plus human serum. Methods/readouts recorded in the A-layer: Targeted metabolomics linked elevated lactate in SCI patient serum to glycolytic changes; mouse lesion macrophages and circulating monocytes showed subacute H3K9la enrichment, with CUT&Tag/RNA-seq identifying TXNIP as a direct H3K9la-associated inflammatory target.',
    'qualitative',
    'bulk transcriptomics / GEO dataset',
    'Full-text source localization for M3A-P026-E001 confirms the curated Human metabolic profiling and mouse macrophage H3K9la mapping experiment in Mouse SCI model plus human serum. Methods/readouts recorded in the A-layer: Targeted metabolomics linked elevated lactate in SCI patient serum to glycolytic changes; mouse lesion macrophages and circulating monocytes showed subacute H3K9la enrichment, with CUT&Tag/RNA-seq identifying TXNIP as a direct H3K9la-associated inflammatory target.',
    'full-text source localization for m3a-p026-e001 confirms the curated human metabolic profiling and mouse macrophage h3k9la mapping experiment in mouse sci model plus human serum. methods/readouts recorded in the a-layer: targeted metabolomics linked elevated lactate in sci patient serum to glycolytic changes; mouse lesion macrophages and circulating monocytes showed subacute h3k9la enrichment, with cut&tag/rna-seq identifying txnip as a direct h3k9la-associated inflammatory target.',
    'Module 3A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P026-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P026-E001", "measurement_method_inference": "bulk transcriptomics / GEO dataset", "paper_tracker_id": "M3A-P026", "quantitative": "YES", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T004", "tracker_id": "M3B-O026"}'
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
    'Full-text source localization for M3A-P027-E001 confirms the curated Integrated transcriptomic and single-cell analyses identified microglia as the predominant PANoptotic population after SCI; in BV2 microglia, 1 uM metformin with LPS/ATP challenge reduced pyroptosis, apoptosis, necroptosis, inflammatory cytokines, and M1 polarization through AMPK/NF-kB signaling. experiment in Rat SCI model. Methods/readouts recorded in the A-layer: Full-text design includes both in vitro pathway dissection and in vivo AMPK-dependence testing.',
    'qualitative',
    'single-cell RNA-seq / cell-state atlas; bulk transcriptomics / GEO dataset',
    'Full-text source localization for M3A-P027-E001 confirms the curated Integrated transcriptomic and single-cell analyses identified microglia as the predominant PANoptotic population after SCI; in BV2 microglia, 1 uM metformin with LPS/ATP challenge reduced pyroptosis, apoptosis, necroptosis, inflammatory cytokines, and M1 polarization through AMPK/NF-kB signaling. experiment in Rat SCI model. Methods/readouts recorded in the A-layer: Full-text design includes both in vitro pathway dissection and in vivo AMPK-dependence testing.',
    'full-text source localization for m3a-p027-e001 confirms the curated integrated transcriptomic and single-cell analyses identified microglia as the predominant panoptotic population after sci; in bv2 microglia, 1 um metformin with lps/atp challenge reduced pyroptosis, apoptosis, necroptosis, inflammatory cytokines, and m1 polarization through ampk/nf-kb signaling. experiment in rat sci model. methods/readouts recorded in the a-layer: full-text design includes both in vitro pathway dissection and in vivo ampk-dependence testing.',
    'Module 3A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P027-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P027-E001", "measurement_method_inference": "single-cell RNA-seq / cell-state atlas; bulk transcriptomics / GEO dataset", "paper_tracker_id": "M3A-P027", "quantitative": "YES", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T004", "tracker_id": "M3B-O027"}'
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
    'Full-text source localization for M3A-P028-E001 confirms the curated Bulk RNA-seq and scRNA-seq showed persistent pyroptosis, apoptosis, and necroptosis signatures concentrated in microglia; machine-learning and TF analyses identified IRF1 as an independent PANoptosis-associated regulator and ZBP1 as a prominent PANoptosome sensor. experiment in Rat SCI model. Methods/readouts recorded in the A-layer: Full-text record is primarily multi-omics and regulatory mapping evidence.',
    'qualitative',
    'single-cell RNA-seq / cell-state atlas; bulk transcriptomics / GEO dataset',
    'Full-text source localization for M3A-P028-E001 confirms the curated Bulk RNA-seq and scRNA-seq showed persistent pyroptosis, apoptosis, and necroptosis signatures concentrated in microglia; machine-learning and TF analyses identified IRF1 as an independent PANoptosis-associated regulator and ZBP1 as a prominent PANoptosome sensor. experiment in Rat SCI model. Methods/readouts recorded in the A-layer: Full-text record is primarily multi-omics and regulatory mapping evidence.',
    'full-text source localization for m3a-p028-e001 confirms the curated bulk rna-seq and scrna-seq showed persistent pyroptosis, apoptosis, and necroptosis signatures concentrated in microglia; machine-learning and tf analyses identified irf1 as an independent panoptosis-associated regulator and zbp1 as a prominent panoptosome sensor. experiment in rat sci model. methods/readouts recorded in the a-layer: full-text record is primarily multi-omics and regulatory mapping evidence.',
    'Module 3A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P028-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P028-E001", "measurement_method_inference": "single-cell RNA-seq / cell-state atlas; bulk transcriptomics / GEO dataset", "paper_tracker_id": "M3A-P028", "quantitative": "YES", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T004", "tracker_id": "M3B-O028"}'
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
    'Full-text source localization for M3A-P031-E001 confirms the curated Type 2 diabetes model without therapeutic intervention experiment in Mouse. Methods/readouts recorded in the A-layer: T2D mice had worse BMS scores (1.1 versus 3.5 at 7 d; 1.8 versus 5.5 at 14 d), poorer electrophysiological conduction, larger lesion/demyelination, fewer Iba1+ cells, impaired microglial myelin-debris phagocytosis, and lower remyelination than non-diabetic SCI mice. Survival through 14 d was 35% in T2D SCI versus 80% in SCI. RNA-seq and protein data linked the phenotype to increased NLRP3/Caspase-1/GSDMD/IL-1beta/IL-18 and oxidative-stress programs.',
    'qualitative',
    'bulk transcriptomics / GEO dataset',
    'Full-text source localization for M3A-P031-E001 confirms the curated Type 2 diabetes model without therapeutic intervention experiment in Mouse. Methods/readouts recorded in the A-layer: T2D mice had worse BMS scores (1.1 versus 3.5 at 7 d; 1.8 versus 5.5 at 14 d), poorer electrophysiological conduction, larger lesion/demyelination, fewer Iba1+ cells, impaired microglial myelin-debris phagocytosis, and lower remyelination than non-diabetic SCI mice. Survival through 14 d was 35% in T2D SCI versus 80% in SCI. RNA-seq and protein data linked the phenotype to increased NLRP3/Caspase-1/GSDMD/IL-1beta/IL-18 and oxidative-stress programs.',
    'full-text source localization for m3a-p031-e001 confirms the curated type 2 diabetes model without therapeutic intervention experiment in mouse. methods/readouts recorded in the a-layer: t2d mice had worse bms scores (1.1 versus 3.5 at 7 d; 1.8 versus 5.5 at 14 d), poorer electrophysiological conduction, larger lesion/demyelination, fewer iba1+ cells, impaired microglial myelin-debris phagocytosis, and lower remyelination than non-diabetic sci mice. survival through 14 d was 35% in t2d sci versus 80% in sci. rna-seq and protein data linked the phenotype to increased nlrp3/caspase-1/gsdmd/il-1beta/il-18 and oxidative-stress programs.',
    'Module 3A full-text extraction; Full text PMC; Fig. 1-4',
    'A-layer full text; Full text PMC; Fig. 1-4',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P031-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P031-E001", "measurement_method_inference": "bulk transcriptomics / GEO dataset", "paper_tracker_id": "M3A-P031", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T003", "tracker_id": "M3B-O031"}'
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
    'Full-text source localization for M3A-P032-E001 confirms the curated FGF4 treatment and myelin-debris phagocytosis experiment in Mouse SCI model plus BMDMs. Methods/readouts recorded in the A-layer: Endogenous FGF4 rose transiently early after SCI. Exogenous FGF4 increased myelin-debris phagocytosis in BMDMs through FGFR1-PI3K/AKT and upregulated Clec10a; it also improved phagosome maturation from Rab5+ to Rab7+ to Lamp1+ compartments and restored CTSD-dependent lysosomal degradation.',
    'qualitative',
    'pathway activity / phospho-signaling assay',
    'Full-text source localization for M3A-P032-E001 confirms the curated FGF4 treatment and myelin-debris phagocytosis experiment in Mouse SCI model plus BMDMs. Methods/readouts recorded in the A-layer: Endogenous FGF4 rose transiently early after SCI. Exogenous FGF4 increased myelin-debris phagocytosis in BMDMs through FGFR1-PI3K/AKT and upregulated Clec10a; it also improved phagosome maturation from Rab5+ to Rab7+ to Lamp1+ compartments and restored CTSD-dependent lysosomal degradation.',
    'full-text source localization for m3a-p032-e001 confirms the curated fgf4 treatment and myelin-debris phagocytosis experiment in mouse sci model plus bmdms. methods/readouts recorded in the a-layer: endogenous fgf4 rose transiently early after sci. exogenous fgf4 increased myelin-debris phagocytosis in bmdms through fgfr1-pi3k/akt and upregulated clec10a; it also improved phagosome maturation from rab5+ to rab7+ to lamp1+ compartments and restored ctsd-dependent lysosomal degradation.',
    'Module 3A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P032-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P032-E001", "measurement_method_inference": "pathway activity / phospho-signaling assay", "paper_tracker_id": "M3A-P032", "quantitative": "YES", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T005", "tracker_id": "M3B-O032"}'
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
    'Full-text source localization for M3A-P034-E001 confirms the curated Review of CGRP-positive sensory-fiber remodeling and macrophage polarization experiment in Not applicable; literature synthesis. Methods/readouts recorded in the A-layer: The article synthesizes evidence that CGRP-positive sensory fibers sprout or become ectopically distributed after SCI and that CGRP-CGRP-receptor signaling can influence macrophage polarization through cAMP/PKA, MAPK, and related pathways. It is a narrative review, not a new in vivo or in vitro SCI experiment.',
    'qualitative',
    NULL,
    'Full-text source localization for M3A-P034-E001 confirms the curated Review of CGRP-positive sensory-fiber remodeling and macrophage polarization experiment in Not applicable; literature synthesis. Methods/readouts recorded in the A-layer: The article synthesizes evidence that CGRP-positive sensory fibers sprout or become ectopically distributed after SCI and that CGRP-CGRP-receptor signaling can influence macrophage polarization through cAMP/PKA, MAPK, and related pathways. It is a narrative review, not a new in vivo or in vitro SCI experiment.',
    'full-text source localization for m3a-p034-e001 confirms the curated review of cgrp-positive sensory-fiber remodeling and macrophage polarization experiment in not applicable; literature synthesis. methods/readouts recorded in the a-layer: the article synthesizes evidence that cgrp-positive sensory fibers sprout or become ectopically distributed after sci and that cgrp-cgrp-receptor signaling can influence macrophage polarization through camp/pka, mapk, and related pathways. it is a narrative review, not a new in vivo or in vitro sci experiment.',
    'Module 3A full-text extraction; Full text PMC; narrative review scope',
    'A-layer full text; Full text PMC; narrative review scope',
    'medium',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P034-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P034-E001", "measurement_method_inference": null, "paper_tracker_id": "M3A-P034", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T003", "tracker_id": "M3B-O034"}'
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
    'Full-text source localization for M3A-P035-E001 confirms the curated Systemic recombinant rat IL-4, 0.5 ug/kg i.p., was tested with BBB, CatWalk XT, gridwalk, tissue immunohistochemistry, RNA-seq, proteomics, and serum cytokine profiling at 1, 3, 7, 14, and 28 dpi. experiment in Rat SCI model. Methods/readouts recorded in the A-layer: Full-text methods provide a complete dosing, injury, sex, and endpoint record.',
    'qualitative',
    'ELISA / cytokine protein assay; bulk transcriptomics / GEO dataset; immunostaining / histology / pathology; barrier / permeability / endothelial assay',
    'Full-text source localization for M3A-P035-E001 confirms the curated Systemic recombinant rat IL-4, 0.5 ug/kg i.p., was tested with BBB, CatWalk XT, gridwalk, tissue immunohistochemistry, RNA-seq, proteomics, and serum cytokine profiling at 1, 3, 7, 14, and 28 dpi. experiment in Rat SCI model. Methods/readouts recorded in the A-layer: Full-text methods provide a complete dosing, injury, sex, and endpoint record.',
    'full-text source localization for m3a-p035-e001 confirms the curated systemic recombinant rat il-4, 0.5 ug/kg i.p., was tested with bbb, catwalk xt, gridwalk, tissue immunohistochemistry, rna-seq, proteomics, and serum cytokine profiling at 1, 3, 7, 14, and 28 dpi. experiment in rat sci model. methods/readouts recorded in the a-layer: full-text methods provide a complete dosing, injury, sex, and endpoint record.',
    'Module 3A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P035-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P035-E001", "measurement_method_inference": "ELISA / cytokine protein assay; bulk transcriptomics / GEO dataset; immunostaining / histology / pathology; barrier / permeability / endothelial assay", "paper_tracker_id": "M3A-P035", "quantitative": "YES", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T003", "tracker_id": "M3B-O035"}'
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
    'Full-text source localization for M3A-P036-E001 confirms the curated Omaveloxolone 10 mg/kg intraperitoneally beginning 30 min after SCI and daily for 7 d experiment in Mouse SCI model. Methods/readouts recorded in the A-layer: Omaveloxolone improved BMS recovery, CatWalk gait metrics, hindlimb motor-evoked potentials, and lesion morphology through 8 weeks. At 7 dpi it reduced CD68+/iNOS+ and Iba1+/iNOS+ cells, increased CD206-associated macrophage/microglial states, and lowered inflammatory cytokine and immune-pathway signals.',
    'qualitative',
    'ELISA / cytokine protein assay; behavioral / functional recovery assay',
    'Full-text source localization for M3A-P036-E001 confirms the curated Omaveloxolone 10 mg/kg intraperitoneally beginning 30 min after SCI and daily for 7 d experiment in Mouse SCI model. Methods/readouts recorded in the A-layer: Omaveloxolone improved BMS recovery, CatWalk gait metrics, hindlimb motor-evoked potentials, and lesion morphology through 8 weeks. At 7 dpi it reduced CD68+/iNOS+ and Iba1+/iNOS+ cells, increased CD206-associated macrophage/microglial states, and lowered inflammatory cytokine and immune-pathway signals.',
    'full-text source localization for m3a-p036-e001 confirms the curated omaveloxolone 10 mg/kg intraperitoneally beginning 30 min after sci and daily for 7 d experiment in mouse sci model. methods/readouts recorded in the a-layer: omaveloxolone improved bms recovery, catwalk gait metrics, hindlimb motor-evoked potentials, and lesion morphology through 8 weeks. at 7 dpi it reduced cd68+/inos+ and iba1+/inos+ cells, increased cd206-associated macrophage/microglial states, and lowered inflammatory cytokine and immune-pathway signals.',
    'Module 3A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P036-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P036-E001", "measurement_method_inference": "ELISA / cytokine protein assay; behavioral / functional recovery assay", "paper_tracker_id": "M3A-P036", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T003", "tracker_id": "M3B-O036"}'
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
    'Full-text source localization for M3A-P037-E001 confirms the curated 1.5 uL lesion-directed GelMA hydrogel containing 1,000 ng/ml free IL-13 and 2% IL-13-loaded PLGA microparticles, injected immediately after injury at lesion, 1 mm rostral, and 1 mm caudal sites experiment in Mouse SCI model. Methods/readouts recorded in the A-layer: HGIL13 improved BMS locomotor recovery and histopathology, reduced resident microglial abundance and CD86 expression, increased Arg1 in resident microglia and infiltrating monocyte-derived macrophages, and altered the early microglial transcriptome toward a less activated state.',
    'qualitative',
    'immunostaining / histology / pathology; behavioral / functional recovery assay',
    'Full-text source localization for M3A-P037-E001 confirms the curated 1.5 uL lesion-directed GelMA hydrogel containing 1,000 ng/ml free IL-13 and 2% IL-13-loaded PLGA microparticles, injected immediately after injury at lesion, 1 mm rostral, and 1 mm caudal sites experiment in Mouse SCI model. Methods/readouts recorded in the A-layer: HGIL13 improved BMS locomotor recovery and histopathology, reduced resident microglial abundance and CD86 expression, increased Arg1 in resident microglia and infiltrating monocyte-derived macrophages, and altered the early microglial transcriptome toward a less activated state.',
    'full-text source localization for m3a-p037-e001 confirms the curated 1.5 ul lesion-directed gelma hydrogel containing 1,000 ng/ml free il-13 and 2% il-13-loaded plga microparticles, injected immediately after injury at lesion, 1 mm rostral, and 1 mm caudal sites experiment in mouse sci model. methods/readouts recorded in the a-layer: hgil13 improved bms locomotor recovery and histopathology, reduced resident microglial abundance and cd86 expression, increased arg1 in resident microglia and infiltrating monocyte-derived macrophages, and altered the early microglial transcriptome toward a less activated state.',
    'Module 3A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P037-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P037-E001", "measurement_method_inference": "immunostaining / histology / pathology; behavioral / functional recovery assay", "paper_tracker_id": "M3A-P037", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T007", "tracker_id": "M3B-O037"}'
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
    'Full-text source localization for M3A-P038-E001 confirms the curated Neonatal sEV/miR-487b-3p vascular-immune reprogramming experiment in Mouse SCI model plus SCMECs. Methods/readouts recorded in the A-layer: Neonatal mouse circulating blood-derived small extracellular vesicles delivered miR-487b-3p to spinal cord microvascular endothelial cells; myelin debris-induced IRS1-PI3K-Akt-mTOR overactivation, lipid-droplet buildup, EndoMT, and CXCL12 secretion were used as the vascular-immune injury model.',
    'qualitative',
    'barrier / permeability / endothelial assay; pathway activity / phospho-signaling assay',
    'Full-text source localization for M3A-P038-E001 confirms the curated Neonatal sEV/miR-487b-3p vascular-immune reprogramming experiment in Mouse SCI model plus SCMECs. Methods/readouts recorded in the A-layer: Neonatal mouse circulating blood-derived small extracellular vesicles delivered miR-487b-3p to spinal cord microvascular endothelial cells; myelin debris-induced IRS1-PI3K-Akt-mTOR overactivation, lipid-droplet buildup, EndoMT, and CXCL12 secretion were used as the vascular-immune injury model.',
    'full-text source localization for m3a-p038-e001 confirms the curated neonatal sev/mir-487b-3p vascular-immune reprogramming experiment in mouse sci model plus scmecs. methods/readouts recorded in the a-layer: neonatal mouse circulating blood-derived small extracellular vesicles delivered mir-487b-3p to spinal cord microvascular endothelial cells; myelin debris-induced irs1-pi3k-akt-mtor overactivation, lipid-droplet buildup, endomt, and cxcl12 secretion were used as the vascular-immune injury model.',
    'Module 3A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P038-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P038-E001", "measurement_method_inference": "barrier / permeability / endothelial assay; pathway activity / phospho-signaling assay", "paper_tracker_id": "M3A-P038", "quantitative": "YES", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T005", "tracker_id": "M3B-O038"}'
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
    'Full-text source localization for M3A-P039-E001 confirms the curated Microglial P2Y12R overexpression and purine-metabolism pathway validation experiment in Primary mouse microglia, neurons, astrocytes, and HT22 neurons. Methods/readouts recorded in the A-layer: P2Y12R-overexpressing microglia degraded neuron-derived ATP through CD39/CD73, increased adenosine, and promoted A1R-dependent neuronal mitophagy through PINK1/Parkin/LC3. This reduced ROS, restored mitochondrial membrane potential and ATP, and improved neuronal viability; blockade of P2Y12R, A1R, PINK1, or Parkin attenuated the effect.',
    'qualitative',
    NULL,
    'Full-text source localization for M3A-P039-E001 confirms the curated Microglial P2Y12R overexpression and purine-metabolism pathway validation experiment in Primary mouse microglia, neurons, astrocytes, and HT22 neurons. Methods/readouts recorded in the A-layer: P2Y12R-overexpressing microglia degraded neuron-derived ATP through CD39/CD73, increased adenosine, and promoted A1R-dependent neuronal mitophagy through PINK1/Parkin/LC3. This reduced ROS, restored mitochondrial membrane potential and ATP, and improved neuronal viability; blockade of P2Y12R, A1R, PINK1, or Parkin attenuated the effect.',
    'full-text source localization for m3a-p039-e001 confirms the curated microglial p2y12r overexpression and purine-metabolism pathway validation experiment in primary mouse microglia, neurons, astrocytes, and ht22 neurons. methods/readouts recorded in the a-layer: p2y12r-overexpressing microglia degraded neuron-derived atp through cd39/cd73, increased adenosine, and promoted a1r-dependent neuronal mitophagy through pink1/parkin/lc3. this reduced ros, restored mitochondrial membrane potential and atp, and improved neuronal viability; blockade of p2y12r, a1r, pink1, or parkin attenuated the effect.',
    'Module 3A full-text extraction; Full text PMC; Fig. 3-4 and supplementary co-culture assays',
    'A-layer full text; Full text PMC; Fig. 3-4 and supplementary co-culture assays',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P039-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P039-E001", "measurement_method_inference": null, "paper_tracker_id": "M3A-P039", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T005", "tracker_id": "M3B-O039"}'
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
    'Full-text source localization for M3A-P040-E001 confirms the curated Biohybrid PM-Lipo@PB NPs consisting of platelet-derived membrane vesicles, M2 macrophage extracellular vesicles, and a Prussian blue nanozyme shell experiment in BV2 microglial cells. Methods/readouts recorded in the A-layer: PM-Lipo@PB-NPs improved mitochondrial membrane potential and cristae, reduced ROS, MDA, cleaved-caspase-3, and apoptosis, increased mitochondria-lysosome/TOMM20-LC3 co-localization, and shifted BV2 cells toward a reparative phenotype with lower IL-1beta/TNF-alpha. PI3K/AKT/mTOR inhibition tracked with mitophagy restoration; MHY1485 partly reversed and LY294002 enhanced the effect, supporting but not fully proving pathway necessity.',
    'qualitative',
    'ELISA / cytokine protein assay; pathway activity / phospho-signaling assay',
    'Full-text source localization for M3A-P040-E001 confirms the curated Biohybrid PM-Lipo@PB NPs consisting of platelet-derived membrane vesicles, M2 macrophage extracellular vesicles, and a Prussian blue nanozyme shell experiment in BV2 microglial cells. Methods/readouts recorded in the A-layer: PM-Lipo@PB-NPs improved mitochondrial membrane potential and cristae, reduced ROS, MDA, cleaved-caspase-3, and apoptosis, increased mitochondria-lysosome/TOMM20-LC3 co-localization, and shifted BV2 cells toward a reparative phenotype with lower IL-1beta/TNF-alpha. PI3K/AKT/mTOR inhibition tracked with mitophagy restoration; MHY1485 partly reversed and LY294002 enhanced the effect, supporting but not fully proving pathway necessity.',
    'full-text source localization for m3a-p040-e001 confirms the curated biohybrid pm-lipo@pb nps consisting of platelet-derived membrane vesicles, m2 macrophage extracellular vesicles, and a prussian blue nanozyme shell experiment in bv2 microglial cells. methods/readouts recorded in the a-layer: pm-lipo@pb-nps improved mitochondrial membrane potential and cristae, reduced ros, mda, cleaved-caspase-3, and apoptosis, increased mitochondria-lysosome/tomm20-lc3 co-localization, and shifted bv2 cells toward a reparative phenotype with lower il-1beta/tnf-alpha. pi3k/akt/mtor inhibition tracked with mitophagy restoration; mhy1485 partly reversed and ly294002 enhanced the effect, supporting but not fully proving pathway necessity.',
    'Module 3A full-text extraction; Full text PMC; Fig. 5-9 and supplementary mechanism assays',
    'A-layer full text; Full text PMC; Fig. 5-9 and supplementary mechanism assays',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P040-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P040-E001", "measurement_method_inference": "ELISA / cytokine protein assay; pathway activity / phospho-signaling assay", "paper_tracker_id": "M3A-P040", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T005", "tracker_id": "M3B-O040"}'
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
    'Full-text source localization for M3A-P041-E001 confirms the curated Mannose-modified EPO mRNA lipid nanoparticle (EPO@MLNP) targeting CD206-enriched macrophages/microglia experiment in Mouse and BV2 microglial cells. Methods/readouts recorded in the A-layer: EPO@MLNP showed higher lesion-region expression and microglial enrichment than untargeted LNP, sustained local EPO production, lower BV2 iNOS after LPS, fewer CD86+ microglia, reduced microglial infiltration, and lower plasma TNF-alpha, IL-1beta, and IL-6. The delivery-route discrepancy between results and methods should remain attached to this evidence.',
    'qualitative',
    'ELISA / cytokine protein assay; qPCR / RT-PCR / mRNA assay',
    'Full-text source localization for M3A-P041-E001 confirms the curated Mannose-modified EPO mRNA lipid nanoparticle (EPO@MLNP) targeting CD206-enriched macrophages/microglia experiment in Mouse and BV2 microglial cells. Methods/readouts recorded in the A-layer: EPO@MLNP showed higher lesion-region expression and microglial enrichment than untargeted LNP, sustained local EPO production, lower BV2 iNOS after LPS, fewer CD86+ microglia, reduced microglial infiltration, and lower plasma TNF-alpha, IL-1beta, and IL-6. The delivery-route discrepancy between results and methods should remain attached to this evidence.',
    'full-text source localization for m3a-p041-e001 confirms the curated mannose-modified epo mrna lipid nanoparticle (epo@mlnp) targeting cd206-enriched macrophages/microglia experiment in mouse and bv2 microglial cells. methods/readouts recorded in the a-layer: epo@mlnp showed higher lesion-region expression and microglial enrichment than untargeted lnp, sustained local epo production, lower bv2 inos after lps, fewer cd86+ microglia, reduced microglial infiltration, and lower plasma tnf-alpha, il-1beta, and il-6. the delivery-route discrepancy between results and methods should remain attached to this evidence.',
    'Module 3A full-text extraction; Full text PMC; Fig. 2-4 and targeting/inflammation assays',
    'A-layer full text; Full text PMC; Fig. 2-4 and targeting/inflammation assays',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P041-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P041-E001", "measurement_method_inference": "ELISA / cytokine protein assay; qPCR / RT-PCR / mRNA assay", "paper_tracker_id": "M3A-P041", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T005", "tracker_id": "M3B-O041"}'
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
    'Full-text source localization for M3A-P042-E001 confirms the curated 10X scRNA-seq, Visium spatial transcriptomics, and mass-spectrometry-imaging spatial metabolomics experiment in Rat. Methods/readouts recorded in the A-layer: The study profiled 35,799 cells and identified a SCI-enriched Mic2 microglial subset expressing Spp1, Hopx, Lgals3, Anxa2, and Tspo, with wound-healing and adhesion programs. Mic2 localized mainly to dorsal white matter and its spatially enriched region contained taurine; predicted Cd99-Cd99 and Psap-Gpr37l1 interactions increased after SCI. This is a candidate immune-metabolic repair state, not proof that taurine or Mic2 is necessary for recovery; omics samples were separate animals and neuronal information was limited by scRNA-seq.',
    'qualitative',
    'single-cell RNA-seq / cell-state atlas; spatial transcriptomics / spatial atlas; MRI / imaging assay; behavioral / functional recovery assay',
    'Full-text source localization for M3A-P042-E001 confirms the curated 10X scRNA-seq, Visium spatial transcriptomics, and mass-spectrometry-imaging spatial metabolomics experiment in Rat. Methods/readouts recorded in the A-layer: The study profiled 35,799 cells and identified a SCI-enriched Mic2 microglial subset expressing Spp1, Hopx, Lgals3, Anxa2, and Tspo, with wound-healing and adhesion programs. Mic2 localized mainly to dorsal white matter and its spatially enriched region contained taurine; predicted Cd99-Cd99 and Psap-Gpr37l1 interactions increased after SCI. This is a candidate immune-metabolic repair state, not proof that taurine or Mic2 is necessary for recovery; omics samples were separate animals and neuronal information was limited by scRNA-seq.',
    'full-text source localization for m3a-p042-e001 confirms the curated 10x scrna-seq, visium spatial transcriptomics, and mass-spectrometry-imaging spatial metabolomics experiment in rat. methods/readouts recorded in the a-layer: the study profiled 35,799 cells and identified a sci-enriched mic2 microglial subset expressing spp1, hopx, lgals3, anxa2, and tspo, with wound-healing and adhesion programs. mic2 localized mainly to dorsal white matter and its spatially enriched region contained taurine; predicted cd99-cd99 and psap-gpr37l1 interactions increased after sci. this is a candidate immune-metabolic repair state, not proof that taurine or mic2 is necessary for recovery; omics samples were separate animals and neuronal information was limited by scrna-seq.',
    'Module 3A full-text extraction; Fig. 1-3; immune-cell single-cell and spatial metabolomics atlas',
    'A-layer full text; Fig. 1-3; immune-cell single-cell and spatial metabolomics atlas',
    'medium',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P042-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P042-E001", "measurement_method_inference": "single-cell RNA-seq / cell-state atlas; spatial transcriptomics / spatial atlas; MRI / imaging assay; behavioral / functional recovery assay", "paper_tracker_id": "M3A-P042", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T005", "tracker_id": "M3B-O042"}'
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
    'Full-text source localization for M3A-P043-E001 confirms the curated Intrathecal 10 microliters LV-MDK or LV-NC at 1 x 10^9 TU/ml, administered 3 days before SCI experiment in Rat. Methods/readouts recorded in the A-layer: LV-MDK increased MDK around microglia, improved BBB and CatWalk gait and MEPs through 42 days, reduced inflammatory mediators and neuronal apoptosis, preserved neurons/axons, and increased CD206-associated reparative microglial features and LRP-1/AKT/mTOR/BDNF signaling. Because treatment was delivered before injury, translational post-injury efficacy remains untested.',
    'qualitative',
    'barrier / permeability / endothelial assay; pathway activity / phospho-signaling assay',
    'Full-text source localization for M3A-P043-E001 confirms the curated Intrathecal 10 microliters LV-MDK or LV-NC at 1 x 10^9 TU/ml, administered 3 days before SCI experiment in Rat. Methods/readouts recorded in the A-layer: LV-MDK increased MDK around microglia, improved BBB and CatWalk gait and MEPs through 42 days, reduced inflammatory mediators and neuronal apoptosis, preserved neurons/axons, and increased CD206-associated reparative microglial features and LRP-1/AKT/mTOR/BDNF signaling. Because treatment was delivered before injury, translational post-injury efficacy remains untested.',
    'full-text source localization for m3a-p043-e001 confirms the curated intrathecal 10 microliters lv-mdk or lv-nc at 1 x 10^9 tu/ml, administered 3 days before sci experiment in rat. methods/readouts recorded in the a-layer: lv-mdk increased mdk around microglia, improved bbb and catwalk gait and meps through 42 days, reduced inflammatory mediators and neuronal apoptosis, preserved neurons/axons, and increased cd206-associated reparative microglial features and lrp-1/akt/mtor/bdnf signaling. because treatment was delivered before injury, translational post-injury efficacy remains untested.',
    'Module 3A full-text extraction; Full text PMC; in vivo time course and LV-MDK validation',
    'A-layer full text; Full text PMC; in vivo time course and LV-MDK validation',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P043-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P043-E001", "measurement_method_inference": "barrier / permeability / endothelial assay; pathway activity / phospho-signaling assay", "paper_tracker_id": "M3A-P043", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T003", "tracker_id": "M3B-O043"}'
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
    'Full-text source localization for M3A-P045-E001 confirms the curated CXCL4/CXCR3/PI3K-Akt PMT mechanism experiment in Mouse SCI model plus pericytes. Methods/readouts recorded in the A-layer: scRNA-seq identified Spp1+Fn1+ macrophages as the major CXCL4 source; CXCL4 was increased after SCI, pericytes expressed CXCR3, and exogenous CXCL4 induced pericyte-to-myofibroblast transition through CXCR3/PI3K/Akt in vitro.',
    'qualitative',
    'single-cell RNA-seq / cell-state atlas; pathway activity / phospho-signaling assay',
    'Full-text source localization for M3A-P045-E001 confirms the curated CXCL4/CXCR3/PI3K-Akt PMT mechanism experiment in Mouse SCI model plus pericytes. Methods/readouts recorded in the A-layer: scRNA-seq identified Spp1+Fn1+ macrophages as the major CXCL4 source; CXCL4 was increased after SCI, pericytes expressed CXCR3, and exogenous CXCL4 induced pericyte-to-myofibroblast transition through CXCR3/PI3K/Akt in vitro.',
    'full-text source localization for m3a-p045-e001 confirms the curated cxcl4/cxcr3/pi3k-akt pmt mechanism experiment in mouse sci model plus pericytes. methods/readouts recorded in the a-layer: scrna-seq identified spp1+fn1+ macrophages as the major cxcl4 source; cxcl4 was increased after sci, pericytes expressed cxcr3, and exogenous cxcl4 induced pericyte-to-myofibroblast transition through cxcr3/pi3k/akt in vitro.',
    'Module 3A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P045-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P045-E001", "measurement_method_inference": "single-cell RNA-seq / cell-state atlas; pathway activity / phospho-signaling assay", "paper_tracker_id": "M3A-P045", "quantitative": "YES", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T002", "tracker_id": "M3B-O045"}'
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
    'Full-text source localization for M3A-P046-E001 confirms the curated TGF-beta pathway genetic and antibody interruption experiment in Mouse SCI model. Methods/readouts recorded in the A-layer: Macrophages were a major source of activated TGF-beta1 after SCI; macrophage-lineage TGF-beta1 recruited MSCs and promoted fibroblast differentiation, while TGF-beta signaling in resident pericytes also drove fibroblast formation at the blood-spinal cord barrier.',
    'qualitative',
    'barrier / permeability / endothelial assay',
    'Full-text source localization for M3A-P046-E001 confirms the curated TGF-beta pathway genetic and antibody interruption experiment in Mouse SCI model. Methods/readouts recorded in the A-layer: Macrophages were a major source of activated TGF-beta1 after SCI; macrophage-lineage TGF-beta1 recruited MSCs and promoted fibroblast differentiation, while TGF-beta signaling in resident pericytes also drove fibroblast formation at the blood-spinal cord barrier.',
    'full-text source localization for m3a-p046-e001 confirms the curated tgf-beta pathway genetic and antibody interruption experiment in mouse sci model. methods/readouts recorded in the a-layer: macrophages were a major source of activated tgf-beta1 after sci; macrophage-lineage tgf-beta1 recruited mscs and promoted fibroblast differentiation, while tgf-beta signaling in resident pericytes also drove fibroblast formation at the blood-spinal cord barrier.',
    'Module 3A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P046-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P046-E001", "measurement_method_inference": "barrier / permeability / endothelial assay", "paper_tracker_id": "M3A-P046", "quantitative": "YES", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T002", "tracker_id": "M3B-O046"}'
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
    'Full-text source localization for M3A-P047-E001 confirms the curated Four-site intraspinal transplantation of 4 microliters OEC suspension at 1 x 10^5 cells/microliter, 1 microliter per site experiment in Rat. Methods/readouts recorded in the A-layer: OEC transplantation improved BBB recovery, mechanical withdrawal threshold, and thermal withdrawal latency, reduced lesion cavitation and GFAP-associated activation, and increased NF200 axon-associated signal. It reduced H3Cit/CD68 MET-associated staining and NKCC1 in spinal cord and L4-L6 DRG. The phenotype supports analgesic and motor benefit but does not prove MET/NKCC1 causality.',
    'qualitative',
    'immunostaining / histology / pathology; barrier / permeability / endothelial assay; behavioral / functional recovery assay',
    'Full-text source localization for M3A-P047-E001 confirms the curated Four-site intraspinal transplantation of 4 microliters OEC suspension at 1 x 10^5 cells/microliter, 1 microliter per site experiment in Rat. Methods/readouts recorded in the A-layer: OEC transplantation improved BBB recovery, mechanical withdrawal threshold, and thermal withdrawal latency, reduced lesion cavitation and GFAP-associated activation, and increased NF200 axon-associated signal. It reduced H3Cit/CD68 MET-associated staining and NKCC1 in spinal cord and L4-L6 DRG. The phenotype supports analgesic and motor benefit but does not prove MET/NKCC1 causality.',
    'full-text source localization for m3a-p047-e001 confirms the curated four-site intraspinal transplantation of 4 microliters oec suspension at 1 x 10^5 cells/microliter, 1 microliter per site experiment in rat. methods/readouts recorded in the a-layer: oec transplantation improved bbb recovery, mechanical withdrawal threshold, and thermal withdrawal latency, reduced lesion cavitation and gfap-associated activation, and increased nf200 axon-associated signal. it reduced h3cit/cd68 met-associated staining and nkcc1 in spinal cord and l4-l6 drg. the phenotype supports analgesic and motor benefit but does not prove met/nkcc1 causality.',
    'Module 3A full-text extraction; Full text PMC; in vivo transplantation and pain-recovery assays',
    'A-layer full text; Full text PMC; in vivo transplantation and pain-recovery assays',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P047-E001; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P047-E001", "measurement_method_inference": "immunostaining / histology / pathology; barrier / permeability / endothelial assay; behavioral / functional recovery assay", "paper_tracker_id": "M3A-P047", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T008", "tracker_id": "M3B-O047"}'
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
    'Full-text source localization for M3A-P001-E002 confirms the curated Post-injury PLX5622 1200 ppm chow experiment in Mouse. Methods/readouts recorded in the A-layer: Post-injury depletion reduced spinal-cord and brain inflammatory programs, improved neuronal survival, and improved motor, cognitive, and depressive-like outcomes; systemic myeloid effects are part of the interpretation.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Full-text source localization for M3A-P001-E002 confirms the curated Post-injury PLX5622 1200 ppm chow experiment in Mouse. Methods/readouts recorded in the A-layer: Post-injury depletion reduced spinal-cord and brain inflammatory programs, improved neuronal survival, and improved motor, cognitive, and depressive-like outcomes; systemic myeloid effects are part of the interpretation.',
    'full-text source localization for m3a-p001-e002 confirms the curated post-injury plx5622 1200 ppm chow experiment in mouse. methods/readouts recorded in the a-layer: post-injury depletion reduced spinal-cord and brain inflammatory programs, improved neuronal survival, and improved motor, cognitive, and depressive-like outcomes; systemic myeloid effects are part of the interpretation.',
    'Module 3A full-text extraction; Full text PMC; Fig. 3-5',
    'A-layer full text; Full text PMC; Fig. 3-5',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P001-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P001-E002", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M3A-P001", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T001", "tracker_id": "M3B-O048"}'
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
    'Full-text source localization for M3A-P002-E002 confirms the curated Myeloid Plexin-B2 ablation experiment in Mouse. Methods/readouts recorded in the A-layer: Plexin-B2 loss impaired corralling, wound compaction, inflammatory confinement, axon and 5-HT fiber preservation, and BMS, rotarod, ladder, and sensory recovery.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Full-text source localization for M3A-P002-E002 confirms the curated Myeloid Plexin-B2 ablation experiment in Mouse. Methods/readouts recorded in the A-layer: Plexin-B2 loss impaired corralling, wound compaction, inflammatory confinement, axon and 5-HT fiber preservation, and BMS, rotarod, ladder, and sensory recovery.',
    'full-text source localization for m3a-p002-e002 confirms the curated myeloid plexin-b2 ablation experiment in mouse. methods/readouts recorded in the a-layer: plexin-b2 loss impaired corralling, wound compaction, inflammatory confinement, axon and 5-ht fiber preservation, and bms, rotarod, ladder, and sensory recovery.',
    'Module 3A full-text extraction; Full text PMC; Fig. 3-5',
    'A-layer full text; Full text PMC; Fig. 3-5',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P002-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P002-E002", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M3A-P002", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T002", "tracker_id": "M3B-O049"}'
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
    'Full-text source localization for M3A-P003-E002 confirms the curated GW2580 0.1% chow experiment in Mouse. Methods/readouts recorded in the A-layer: Treatment reduced gliosis and microcavity formation and improved fine paw-placement and CatWalk parameters, while lesion extension and volume by MRI were not changed.',
    'qualitative',
    'MRI / imaging assay; behavioral / functional recovery assay',
    'Full-text source localization for M3A-P003-E002 confirms the curated GW2580 0.1% chow experiment in Mouse. Methods/readouts recorded in the A-layer: Treatment reduced gliosis and microcavity formation and improved fine paw-placement and CatWalk parameters, while lesion extension and volume by MRI were not changed.',
    'full-text source localization for m3a-p003-e002 confirms the curated gw2580 0.1% chow experiment in mouse. methods/readouts recorded in the a-layer: treatment reduced gliosis and microcavity formation and improved fine paw-placement and catwalk parameters, while lesion extension and volume by mri were not changed.',
    'Module 3A full-text extraction; Full text PMC; Fig. 4-7',
    'A-layer full text; Full text PMC; Fig. 4-7',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P003-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P003-E002", "measurement_method_inference": "MRI / imaging assay; behavioral / functional recovery assay", "paper_tracker_id": "M3A-P003", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T001", "tracker_id": "M3B-O050"}'
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
    'Full-text source localization for M3A-P004-E002 confirms the curated HMGB1-RAGE axis inhibition experiment in Rat. Methods/readouts recorded in the A-layer: Inhibiting HMGB1 or RAGE shifted macrophage/microglia markers away from pro-inflammatory and toward anti-inflammatory states, reduced neuronal loss and demyelination, and improved BBB and rump-height-index recovery.',
    'qualitative',
    'barrier / permeability / endothelial assay; behavioral / functional recovery assay',
    'Full-text source localization for M3A-P004-E002 confirms the curated HMGB1-RAGE axis inhibition experiment in Rat. Methods/readouts recorded in the A-layer: Inhibiting HMGB1 or RAGE shifted macrophage/microglia markers away from pro-inflammatory and toward anti-inflammatory states, reduced neuronal loss and demyelination, and improved BBB and rump-height-index recovery.',
    'full-text source localization for m3a-p004-e002 confirms the curated hmgb1-rage axis inhibition experiment in rat. methods/readouts recorded in the a-layer: inhibiting hmgb1 or rage shifted macrophage/microglia markers away from pro-inflammatory and toward anti-inflammatory states, reduced neuronal loss and demyelination, and improved bbb and rump-height-index recovery.',
    'Module 3A full-text extraction; Full text PMC; Fig. 5-8',
    'A-layer full text; Full text PMC; Fig. 5-8',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P004-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P004-E002", "measurement_method_inference": "barrier / permeability / endothelial assay; behavioral / functional recovery assay", "paper_tracker_id": "M3A-P004", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T003", "tracker_id": "M3B-O051"}'
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
    'Full-text source localization for M3A-P005-E002 confirms the curated LL37-P2X7R-NF-kB extracellular signaling mechanism experiment in Rat plus human SCI serum. Methods/readouts recorded in the A-layer: Co-IP and western blot linked macrophage-trap products to LL37-P2X7R-NF-kB signaling and M1 polarization; serum trap markers showed a severity association with human ASIA scores, not a treatment effect.',
    'qualitative',
    'western blot / immunoblot',
    'Full-text source localization for M3A-P005-E002 confirms the curated LL37-P2X7R-NF-kB extracellular signaling mechanism experiment in Rat plus human SCI serum. Methods/readouts recorded in the A-layer: Co-IP and western blot linked macrophage-trap products to LL37-P2X7R-NF-kB signaling and M1 polarization; serum trap markers showed a severity association with human ASIA scores, not a treatment effect.',
    'full-text source localization for m3a-p005-e002 confirms the curated ll37-p2x7r-nf-kb extracellular signaling mechanism experiment in rat plus human sci serum. methods/readouts recorded in the a-layer: co-ip and western blot linked macrophage-trap products to ll37-p2x7r-nf-kb signaling and m1 polarization; serum trap markers showed a severity association with human asia scores, not a treatment effect.',
    'Module 3A full-text extraction; Full text PMC; Fig. 5-8 and human cohort',
    'A-layer full text; Full text PMC; Fig. 5-8 and human cohort',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P005-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P005-E002", "measurement_method_inference": "western blot / immunoblot", "paper_tracker_id": "M3A-P005", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T008", "tracker_id": "M3B-O052"}'
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
    'Full-text source localization for M3A-P006-E002 confirms the curated Exosomal let-7b-5p targeting LRIG3 experiment in Mouse BV2 cells plus SCI mice. Methods/readouts recorded in the A-layer: let-7b-5p was enriched in exosomes, directly bound the LRIG3 3-prime UTR, and reduced pyroptosis; LRIG3 overexpression reversed protection while LRIG3 knockdown rescued the let-7b-5p loss condition.',
    'qualitative',
    NULL,
    'Full-text source localization for M3A-P006-E002 confirms the curated Exosomal let-7b-5p targeting LRIG3 experiment in Mouse BV2 cells plus SCI mice. Methods/readouts recorded in the A-layer: let-7b-5p was enriched in exosomes, directly bound the LRIG3 3-prime UTR, and reduced pyroptosis; LRIG3 overexpression reversed protection while LRIG3 knockdown rescued the let-7b-5p loss condition.',
    'full-text source localization for m3a-p006-e002 confirms the curated exosomal let-7b-5p targeting lrig3 experiment in mouse bv2 cells plus sci mice. methods/readouts recorded in the a-layer: let-7b-5p was enriched in exosomes, directly bound the lrig3 3-prime utr, and reduced pyroptosis; lrig3 overexpression reversed protection while lrig3 knockdown rescued the let-7b-5p loss condition.',
    'Module 3A full-text extraction; Full text PMC; Fig. 8 and rescue assays',
    'A-layer full text; Full text PMC; Fig. 8 and rescue assays',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P006-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P006-E002", "measurement_method_inference": null, "paper_tracker_id": "M3A-P006", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T004", "tracker_id": "M3B-O053"}'
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
    'Full-text source localization for M3A-P008-E002 confirms the curated L-P 20 mg/kg daily for 7 d with AMPK deletion or microglial lineage tracing; in vitro L-P and LPS experiment in Mouse SCI model plus microglia/macrophage validation. Methods/readouts recorded in the A-layer: L-P increased AMPK phosphorylation and anti-inflammatory markers, but the AMPK conditional experiments were used to test pathway dependence rather than to establish a separate behavioral treatment effect. BV2 assays showed reduced lipid-droplet and inflammatory responses with M2-associated marker induction.',
    'qualitative',
    'pathway activity / phospho-signaling assay; behavioral / functional recovery assay',
    'Full-text source localization for M3A-P008-E002 confirms the curated L-P 20 mg/kg daily for 7 d with AMPK deletion or microglial lineage tracing; in vitro L-P and LPS experiment in Mouse SCI model plus microglia/macrophage validation. Methods/readouts recorded in the A-layer: L-P increased AMPK phosphorylation and anti-inflammatory markers, but the AMPK conditional experiments were used to test pathway dependence rather than to establish a separate behavioral treatment effect. BV2 assays showed reduced lipid-droplet and inflammatory responses with M2-associated marker induction.',
    'full-text source localization for m3a-p008-e002 confirms the curated l-p 20 mg/kg daily for 7 d with ampk deletion or microglial lineage tracing; in vitro l-p and lps experiment in mouse sci model plus microglia/macrophage validation. methods/readouts recorded in the a-layer: l-p increased ampk phosphorylation and anti-inflammatory markers, but the ampk conditional experiments were used to test pathway dependence rather than to establish a separate behavioral treatment effect. bv2 assays showed reduced lipid-droplet and inflammatory responses with m2-associated marker induction.',
    'Module 3A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P008-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P008-E002", "measurement_method_inference": "pathway activity / phospho-signaling assay; behavioral / functional recovery assay", "paper_tracker_id": "M3A-P008", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T005", "tracker_id": "M3B-O055"}'
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
    'Full-text source localization for M3A-P010-E002 confirms the curated Programmed early M1 suppression followed by later IL-4-driven M2 support experiment in Rat and BV2 cells. Methods/readouts recorded in the A-layer: DSDH matched the intended inflammatory sequence: early iNOS suppression and later CD206/p-STAT6 increase, with less cytotoxicity than burst-release non-DSDH. The study did not include MH-only, IL-4-only, or empty-hydrogel in vivo controls, so synergy and component-specific necessity remain unresolved.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Full-text source localization for M3A-P010-E002 confirms the curated Programmed early M1 suppression followed by later IL-4-driven M2 support experiment in Rat and BV2 cells. Methods/readouts recorded in the A-layer: DSDH matched the intended inflammatory sequence: early iNOS suppression and later CD206/p-STAT6 increase, with less cytotoxicity than burst-release non-DSDH. The study did not include MH-only, IL-4-only, or empty-hydrogel in vivo controls, so synergy and component-specific necessity remain unresolved.',
    'full-text source localization for m3a-p010-e002 confirms the curated programmed early m1 suppression followed by later il-4-driven m2 support experiment in rat and bv2 cells. methods/readouts recorded in the a-layer: dsdh matched the intended inflammatory sequence: early inos suppression and later cd206/p-stat6 increase, with less cytotoxicity than burst-release non-dsdh. the study did not include mh-only, il-4-only, or empty-hydrogel in vivo controls, so synergy and component-specific necessity remain unresolved.',
    'Module 3A full-text extraction; Full text PMC; release and timing mechanism',
    'A-layer full text; Full text PMC; release and timing mechanism',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P010-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P010-E002", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M3A-P010", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T003", "tracker_id": "M3B-O057"}'
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
    'Full-text source localization for M3A-P015-E002 confirms the curated ATL-III 1, 10, or 100 uM for 1 h before 100 ng/ml LPS; rat ATL-III treatment as above experiment in BV2 microglial culture with rat SCI pathway validation. Methods/readouts recorded in the A-layer: ATL-III was not toxic to BV2 cells and dose-dependently reduced LPS-induced iNOS, TNF-alpha, IL-1beta and IL-6 while increasing Arg1 and IL-10. In vivo and in vitro it reduced NF-kB IκBalpha/p65 and JNK/p38 phosphorylation, increased Akt phosphorylation, and did not materially change ERK phosphorylation.',
    'qualitative',
    'ELISA / cytokine protein assay; pathway activity / phospho-signaling assay',
    'Full-text source localization for M3A-P015-E002 confirms the curated ATL-III 1, 10, or 100 uM for 1 h before 100 ng/ml LPS; rat ATL-III treatment as above experiment in BV2 microglial culture with rat SCI pathway validation. Methods/readouts recorded in the A-layer: ATL-III was not toxic to BV2 cells and dose-dependently reduced LPS-induced iNOS, TNF-alpha, IL-1beta and IL-6 while increasing Arg1 and IL-10. In vivo and in vitro it reduced NF-kB IκBalpha/p65 and JNK/p38 phosphorylation, increased Akt phosphorylation, and did not materially change ERK phosphorylation.',
    'full-text source localization for m3a-p015-e002 confirms the curated atl-iii 1, 10, or 100 um for 1 h before 100 ng/ml lps; rat atl-iii treatment as above experiment in bv2 microglial culture with rat sci pathway validation. methods/readouts recorded in the a-layer: atl-iii was not toxic to bv2 cells and dose-dependently reduced lps-induced inos, tnf-alpha, il-1beta and il-6 while increasing arg1 and il-10. in vivo and in vitro it reduced nf-kb iκbalpha/p65 and jnk/p38 phosphorylation, increased akt phosphorylation, and did not materially change erk phosphorylation.',
    'Module 3A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P015-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P015-E002", "measurement_method_inference": "ELISA / cytokine protein assay; pathway activity / phospho-signaling assay", "paper_tracker_id": "M3A-P015", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T003", "tracker_id": "M3B-O062"}'
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
    'Full-text source localization for M3A-P016-E002 confirms the curated Systemically delivered CCR2-enriched macrophages co-delivering ANXA1, GDNF, and CTGF mRNAs experiment in Mouse. Methods/readouts recorded in the A-layer: Engineered cells accumulated more at the lesion, reduced inflammatory/scar-associated signals, increased GDNF/GFRalpha1, NF and MBP repair signals, and improved ultrastructure (g-ratio 0.77 versus 0.90 SCI and 0.86 macrophage). BDA/FB tracing and synaptophysin were higher at the lesion; BMS reached 5 versus 2, stride was 35.33 mm while controls could not walk, and MEP latency/amplitude improved to 13.46 ms/0.16 mV versus 18.02 ms/0.02 mV. These findings support partial structural and functional recovery, not complete circuit restoration.',
    'qualitative',
    'single-cell RNA-seq / cell-state atlas; spatial transcriptomics / spatial atlas; behavioral / functional recovery assay',
    'Full-text source localization for M3A-P016-E002 confirms the curated Systemically delivered CCR2-enriched macrophages co-delivering ANXA1, GDNF, and CTGF mRNAs experiment in Mouse. Methods/readouts recorded in the A-layer: Engineered cells accumulated more at the lesion, reduced inflammatory/scar-associated signals, increased GDNF/GFRalpha1, NF and MBP repair signals, and improved ultrastructure (g-ratio 0.77 versus 0.90 SCI and 0.86 macrophage). BDA/FB tracing and synaptophysin were higher at the lesion; BMS reached 5 versus 2, stride was 35.33 mm while controls could not walk, and MEP latency/amplitude improved to 13.46 ms/0.16 mV versus 18.02 ms/0.02 mV. These findings support partial structural and functional recovery, not complete circuit restoration.',
    'full-text source localization for m3a-p016-e002 confirms the curated systemically delivered ccr2-enriched macrophages co-delivering anxa1, gdnf, and ctgf mrnas experiment in mouse. methods/readouts recorded in the a-layer: engineered cells accumulated more at the lesion, reduced inflammatory/scar-associated signals, increased gdnf/gfralpha1, nf and mbp repair signals, and improved ultrastructure (g-ratio 0.77 versus 0.90 sci and 0.86 macrophage). bda/fb tracing and synaptophysin were higher at the lesion; bms reached 5 versus 2, stride was 35.33 mm while controls could not walk, and mep latency/amplitude improved to 13.46 ms/0.16 mv versus 18.02 ms/0.02 mv. these findings support partial structural and functional recovery, not complete circuit restoration.',
    'Module 3A full-text extraction; Full text PMC; in vivo biodistribution, repair, tracing, and function',
    'A-layer full text; Full text PMC; in vivo biodistribution, repair, tracing, and function',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P016-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P016-E002", "measurement_method_inference": "single-cell RNA-seq / cell-state atlas; spatial transcriptomics / spatial atlas; behavioral / functional recovery assay", "paper_tracker_id": "M3A-P016", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T006", "tracker_id": "M3B-O063"}'
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
    'Full-text source localization for M3A-P017-E002 confirms the curated PLX5622 1200 ppm chow experiment in Rat. Methods/readouts recorded in the A-layer: PLX5622 reduced Iba1+ microglia/macrophage counts by about 50-60% across CNS regions and reduced lesion-core counts by 52%, but did not change lesion size or microglial morphology. The astrocytic scar was thinner (58.5 versus 91.3 micrometers), while liver Kupffer cells fell by about 78%, demonstrating incomplete CNS depletion and substantial peripheral macrophage effects.',
    'qualitative',
    NULL,
    'Full-text source localization for M3A-P017-E002 confirms the curated PLX5622 1200 ppm chow experiment in Rat. Methods/readouts recorded in the A-layer: PLX5622 reduced Iba1+ microglia/macrophage counts by about 50-60% across CNS regions and reduced lesion-core counts by 52%, but did not change lesion size or microglial morphology. The astrocytic scar was thinner (58.5 versus 91.3 micrometers), while liver Kupffer cells fell by about 78%, demonstrating incomplete CNS depletion and substantial peripheral macrophage effects.',
    'full-text source localization for m3a-p017-e002 confirms the curated plx5622 1200 ppm chow experiment in rat. methods/readouts recorded in the a-layer: plx5622 reduced iba1+ microglia/macrophage counts by about 50-60% across cns regions and reduced lesion-core counts by 52%, but did not change lesion size or microglial morphology. the astrocytic scar was thinner (58.5 versus 91.3 micrometers), while liver kupffer cells fell by about 78%, demonstrating incomplete cns depletion and substantial peripheral macrophage effects.',
    'Module 3A full-text extraction; Full text PMC; Fig. 3-6',
    'A-layer full text; Full text PMC; Fig. 3-6',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P017-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P017-E002", "measurement_method_inference": null, "paper_tracker_id": "M3A-P017", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T001", "tracker_id": "M3B-O064"}'
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
    'Full-text source localization for M3A-P020-E002 confirms the curated PLX 1,200 ppm for 14-28 d followed by 3 weeks off diet; retrograde AAV PTEN-KO at 8 weeks post-SCI experiment in Mouse chronic SCI model with repopulation and PTEN-KO validation. Methods/readouts recorded in the A-layer: Removing PLX allowed Iba1+ cells to repopulate to predepletion densities and increased neuronal-enriched transcripts. PTEN-KO did not increase lesion axon density beyond PLX, and the axons entering the lesion were identified mainly as CGRP+ with some 5-HT+ fibers.',
    'qualitative',
    NULL,
    'Full-text source localization for M3A-P020-E002 confirms the curated PLX 1,200 ppm for 14-28 d followed by 3 weeks off diet; retrograde AAV PTEN-KO at 8 weeks post-SCI experiment in Mouse chronic SCI model with repopulation and PTEN-KO validation. Methods/readouts recorded in the A-layer: Removing PLX allowed Iba1+ cells to repopulate to predepletion densities and increased neuronal-enriched transcripts. PTEN-KO did not increase lesion axon density beyond PLX, and the axons entering the lesion were identified mainly as CGRP+ with some 5-HT+ fibers.',
    'full-text source localization for m3a-p020-e002 confirms the curated plx 1,200 ppm for 14-28 d followed by 3 weeks off diet; retrograde aav pten-ko at 8 weeks post-sci experiment in mouse chronic sci model with repopulation and pten-ko validation. methods/readouts recorded in the a-layer: removing plx allowed iba1+ cells to repopulate to predepletion densities and increased neuronal-enriched transcripts. pten-ko did not increase lesion axon density beyond plx, and the axons entering the lesion were identified mainly as cgrp+ with some 5-ht+ fibers.',
    'Module 3A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P020-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P020-E002", "measurement_method_inference": null, "paper_tracker_id": "M3A-P020", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T001", "tracker_id": "M3B-O067"}'
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
    'Full-text source localization for M3A-P022-E002 confirms the curated Agonist treatment reduced inhibitory extracellular-matrix deposition, enabled reticulospinal tract regrowth and synaptic connectivity with thoracolumbar circuits, and improved motor recovery. experiment in Mouse SCI model. Methods/readouts recorded in the A-layer: Full-text result supports a glial-scar and circuit-reconstruction mechanism; exact figure-level effect sizes remain in the source figures.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Full-text source localization for M3A-P022-E002 confirms the curated Agonist treatment reduced inhibitory extracellular-matrix deposition, enabled reticulospinal tract regrowth and synaptic connectivity with thoracolumbar circuits, and improved motor recovery. experiment in Mouse SCI model. Methods/readouts recorded in the A-layer: Full-text result supports a glial-scar and circuit-reconstruction mechanism; exact figure-level effect sizes remain in the source figures.',
    'full-text source localization for m3a-p022-e002 confirms the curated agonist treatment reduced inhibitory extracellular-matrix deposition, enabled reticulospinal tract regrowth and synaptic connectivity with thoracolumbar circuits, and improved motor recovery. experiment in mouse sci model. methods/readouts recorded in the a-layer: full-text result supports a glial-scar and circuit-reconstruction mechanism; exact figure-level effect sizes remain in the source figures.',
    'Module 3A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P022-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P022-E002", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M3A-P022", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T001", "tracker_id": "M3B-O069"}'
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
    'Full-text source localization for M3A-P024-E002 confirms the curated Bazedoxifene 5 uM in vitro and intraperitoneal treatment in SCI mice; anti-C1q antibody for causal complement blockade experiment in Mouse SCI model plus bone-marrow-derived macrophage culture. Methods/readouts recorded in the A-layer: Foam-cell lipid accumulation increased C1q and microglial engulfment of VGLUT2+/PSD95+ synapses near the lesion. Bazedoxifene reduced foam-cell lipid load and C1q, preserved synapses, reduced microglial synapse engulfment, and improved motor recovery; the precise lipid-lowering mechanism was not resolved.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Full-text source localization for M3A-P024-E002 confirms the curated Bazedoxifene 5 uM in vitro and intraperitoneal treatment in SCI mice; anti-C1q antibody for causal complement blockade experiment in Mouse SCI model plus bone-marrow-derived macrophage culture. Methods/readouts recorded in the A-layer: Foam-cell lipid accumulation increased C1q and microglial engulfment of VGLUT2+/PSD95+ synapses near the lesion. Bazedoxifene reduced foam-cell lipid load and C1q, preserved synapses, reduced microglial synapse engulfment, and improved motor recovery; the precise lipid-lowering mechanism was not resolved.',
    'full-text source localization for m3a-p024-e002 confirms the curated bazedoxifene 5 um in vitro and intraperitoneal treatment in sci mice; anti-c1q antibody for causal complement blockade experiment in mouse sci model plus bone-marrow-derived macrophage culture. methods/readouts recorded in the a-layer: foam-cell lipid accumulation increased c1q and microglial engulfment of vglut2+/psd95+ synapses near the lesion. bazedoxifene reduced foam-cell lipid load and c1q, preserved synapses, reduced microglial synapse engulfment, and improved motor recovery; the precise lipid-lowering mechanism was not resolved.',
    'Module 3A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P024-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P024-E002", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M3A-P024", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T005", "tracker_id": "M3B-O071"}'
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
    'Full-text source localization for M3A-P025-E002 confirms the curated Long-term COG1410 TREM2 activation improved early locomotion but later impaired locomotor recovery, 5-HT+ axon regeneration, neuronal survival, and increased fibrosis/inflammation; short-term activation produced only transient early benefit without structural neuroprotection. experiment in Mouse SCI model. Methods/readouts recorded in the A-layer: Full-text finding is explicitly bidirectional and timing-sensitive, not a simple TREM2 neuroprotection claim.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Full-text source localization for M3A-P025-E002 confirms the curated Long-term COG1410 TREM2 activation improved early locomotion but later impaired locomotor recovery, 5-HT+ axon regeneration, neuronal survival, and increased fibrosis/inflammation; short-term activation produced only transient early benefit without structural neuroprotection. experiment in Mouse SCI model. Methods/readouts recorded in the A-layer: Full-text finding is explicitly bidirectional and timing-sensitive, not a simple TREM2 neuroprotection claim.',
    'full-text source localization for m3a-p025-e002 confirms the curated long-term cog1410 trem2 activation improved early locomotion but later impaired locomotor recovery, 5-ht+ axon regeneration, neuronal survival, and increased fibrosis/inflammation; short-term activation produced only transient early benefit without structural neuroprotection. experiment in mouse sci model. methods/readouts recorded in the a-layer: full-text finding is explicitly bidirectional and timing-sensitive, not a simple trem2 neuroprotection claim.',
    'Module 3A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P025-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P025-E002", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M3A-P025", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T005", "tracker_id": "M3B-O072"}'
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
    'Full-text source localization for M3A-P026-E002 confirms the curated H3K9la-pe macrophage-targeted peptide inhibition experiment in Mouse SCI model. Methods/readouts recorded in the A-layer: Lactate increased TXNIP/NLRP3 signaling, inflammatory markers, ROS, and mitochondrial dysfunction; 2-DG or TXNIP knockdown attenuated these effects. The hypoxia-responsive peptide reduced inflammatory signaling, restored mitochondrial integrity, increased axon regeneration, and improved MEP, BMS, swimming, kinematic, and bladder outcomes.',
    'qualitative',
    NULL,
    'Full-text source localization for M3A-P026-E002 confirms the curated H3K9la-pe macrophage-targeted peptide inhibition experiment in Mouse SCI model. Methods/readouts recorded in the A-layer: Lactate increased TXNIP/NLRP3 signaling, inflammatory markers, ROS, and mitochondrial dysfunction; 2-DG or TXNIP knockdown attenuated these effects. The hypoxia-responsive peptide reduced inflammatory signaling, restored mitochondrial integrity, increased axon regeneration, and improved MEP, BMS, swimming, kinematic, and bladder outcomes.',
    'full-text source localization for m3a-p026-e002 confirms the curated h3k9la-pe macrophage-targeted peptide inhibition experiment in mouse sci model. methods/readouts recorded in the a-layer: lactate increased txnip/nlrp3 signaling, inflammatory markers, ros, and mitochondrial dysfunction; 2-dg or txnip knockdown attenuated these effects. the hypoxia-responsive peptide reduced inflammatory signaling, restored mitochondrial integrity, increased axon regeneration, and improved mep, bms, swimming, kinematic, and bladder outcomes.',
    'Module 3A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P026-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P026-E002", "measurement_method_inference": null, "paper_tracker_id": "M3A-P026", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T004", "tracker_id": "M3B-O073"}'
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
    'Full-text source localization for M3A-P027-E002 confirms the curated Metformin promoted tissue repair, axon regrowth, remyelination, motor and electrophysiological recovery, and reduced microglia/macrophage M1 polarization; compound C abrogated the neuroprotective effects, supporting AMPK dependence. experiment in Rat SCI model. Methods/readouts recorded in the A-layer: Full-text result is pharmacological mechanism evidence with an inhibitor control, not genetic proof of AMPK specificity.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Full-text source localization for M3A-P027-E002 confirms the curated Metformin promoted tissue repair, axon regrowth, remyelination, motor and electrophysiological recovery, and reduced microglia/macrophage M1 polarization; compound C abrogated the neuroprotective effects, supporting AMPK dependence. experiment in Rat SCI model. Methods/readouts recorded in the A-layer: Full-text result is pharmacological mechanism evidence with an inhibitor control, not genetic proof of AMPK specificity.',
    'full-text source localization for m3a-p027-e002 confirms the curated metformin promoted tissue repair, axon regrowth, remyelination, motor and electrophysiological recovery, and reduced microglia/macrophage m1 polarization; compound c abrogated the neuroprotective effects, supporting ampk dependence. experiment in rat sci model. methods/readouts recorded in the a-layer: full-text result is pharmacological mechanism evidence with an inhibitor control, not genetic proof of ampk specificity.',
    'Module 3A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P027-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P027-E002", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M3A-P027", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T004", "tracker_id": "M3B-O074"}'
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
    'Full-text source localization for M3A-P028-E002 confirms the curated IRF1 occupied the Zbp1 promoter; pharmacological inhibition of the IRF1 DNA-binding domain reduced ZBP1, PANoptosis execution markers, TNF-alpha and IL-6 release, and M1-like polarization. experiment in Rat SCI model plus microglial cell model. Methods/readouts recorded in the A-layer: Full-text result supports an IRF1-ZBP1 mechanistic target, while functional recovery was not the primary endpoint of this paper.',
    'qualitative',
    'ELISA / cytokine protein assay; behavioral / functional recovery assay',
    'Full-text source localization for M3A-P028-E002 confirms the curated IRF1 occupied the Zbp1 promoter; pharmacological inhibition of the IRF1 DNA-binding domain reduced ZBP1, PANoptosis execution markers, TNF-alpha and IL-6 release, and M1-like polarization. experiment in Rat SCI model plus microglial cell model. Methods/readouts recorded in the A-layer: Full-text result supports an IRF1-ZBP1 mechanistic target, while functional recovery was not the primary endpoint of this paper.',
    'full-text source localization for m3a-p028-e002 confirms the curated irf1 occupied the zbp1 promoter; pharmacological inhibition of the irf1 dna-binding domain reduced zbp1, panoptosis execution markers, tnf-alpha and il-6 release, and m1-like polarization. experiment in rat sci model plus microglial cell model. methods/readouts recorded in the a-layer: full-text result supports an irf1-zbp1 mechanistic target, while functional recovery was not the primary endpoint of this paper.',
    'Module 3A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P028-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P028-E002", "measurement_method_inference": "ELISA / cytokine protein assay; behavioral / functional recovery assay", "paper_tracker_id": "M3A-P028", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T004", "tracker_id": "M3B-O075"}'
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
    'Full-text source localization for M3A-P031-E002 confirms the curated Conditional microglial Caspase-1 knockout experiment in Mouse. Methods/readouts recorded in the A-layer: Microglial Caspase-1 deletion increased BMS scores, reduced persistent hindlimb dragging and damaged area, improved LFB-defined remyelination, and reduced spinal Caspase-1 and cleaved-Caspase-1/Iba1 colocalization in diabetic SCI. This supports microglial pyroptosis as an important contributor, although the model and marker strategy do not isolate every microglial subtype or exclude all non-microglial effects.',
    'qualitative',
    'genetic perturbation / knockdown assay',
    'Full-text source localization for M3A-P031-E002 confirms the curated Conditional microglial Caspase-1 knockout experiment in Mouse. Methods/readouts recorded in the A-layer: Microglial Caspase-1 deletion increased BMS scores, reduced persistent hindlimb dragging and damaged area, improved LFB-defined remyelination, and reduced spinal Caspase-1 and cleaved-Caspase-1/Iba1 colocalization in diabetic SCI. This supports microglial pyroptosis as an important contributor, although the model and marker strategy do not isolate every microglial subtype or exclude all non-microglial effects.',
    'full-text source localization for m3a-p031-e002 confirms the curated conditional microglial caspase-1 knockout experiment in mouse. methods/readouts recorded in the a-layer: microglial caspase-1 deletion increased bms scores, reduced persistent hindlimb dragging and damaged area, improved lfb-defined remyelination, and reduced spinal caspase-1 and cleaved-caspase-1/iba1 colocalization in diabetic sci. this supports microglial pyroptosis as an important contributor, although the model and marker strategy do not isolate every microglial subtype or exclude all non-microglial effects.',
    'Module 3A full-text extraction; Full text PMC; Fig. 6',
    'A-layer full text; Full text PMC; Fig. 6',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P031-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P031-E002", "measurement_method_inference": "genetic perturbation / knockdown assay", "paper_tracker_id": "M3A-P031", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T003", "tracker_id": "M3B-O078"}'
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
    'Full-text source localization for M3A-P032-E002 confirms the curated FGF4 treatment and Clec10a-mediated repair validation experiment in Mouse SCI model plus neuron-conditioned-medium assay. Methods/readouts recorded in the A-layer: FGF4 reduced lipid accumulation, NLRP3 activity, lysosomal membrane permeabilization, and inflammatory polarization after SCI; it improved axon regeneration and locomotor recovery, while FGFR1 inhibition or Clec10a silencing attenuated phagocytic and neuronal-protective effects.',
    'qualitative',
    'pathway activity / phospho-signaling assay; behavioral / functional recovery assay',
    'Full-text source localization for M3A-P032-E002 confirms the curated FGF4 treatment and Clec10a-mediated repair validation experiment in Mouse SCI model plus neuron-conditioned-medium assay. Methods/readouts recorded in the A-layer: FGF4 reduced lipid accumulation, NLRP3 activity, lysosomal membrane permeabilization, and inflammatory polarization after SCI; it improved axon regeneration and locomotor recovery, while FGFR1 inhibition or Clec10a silencing attenuated phagocytic and neuronal-protective effects.',
    'full-text source localization for m3a-p032-e002 confirms the curated fgf4 treatment and clec10a-mediated repair validation experiment in mouse sci model plus neuron-conditioned-medium assay. methods/readouts recorded in the a-layer: fgf4 reduced lipid accumulation, nlrp3 activity, lysosomal membrane permeabilization, and inflammatory polarization after sci; it improved axon regeneration and locomotor recovery, while fgfr1 inhibition or clec10a silencing attenuated phagocytic and neuronal-protective effects.',
    'Module 3A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P032-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P032-E002", "measurement_method_inference": "pathway activity / phospho-signaling assay; behavioral / functional recovery assay", "paper_tracker_id": "M3A-P032", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T005", "tracker_id": "M3B-O079"}'
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
    'Full-text source localization for M3A-P034-E002 confirms the curated Evidence appraisal of sensory-neuropeptide/macrophage crosstalk experiment in Cited animal and cell studies as reported by the review. Methods/readouts recorded in the A-layer: The review proposes CGRP as a context- and time-dependent immunomodulator, but it does not provide a single primary SCI experiment demonstrating that CGRP manipulation alone causes functional recovery. Specific therapeutic claims require retrieval and extraction of the cited primary studies.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Full-text source localization for M3A-P034-E002 confirms the curated Evidence appraisal of sensory-neuropeptide/macrophage crosstalk experiment in Cited animal and cell studies as reported by the review. Methods/readouts recorded in the A-layer: The review proposes CGRP as a context- and time-dependent immunomodulator, but it does not provide a single primary SCI experiment demonstrating that CGRP manipulation alone causes functional recovery. Specific therapeutic claims require retrieval and extraction of the cited primary studies.',
    'full-text source localization for m3a-p034-e002 confirms the curated evidence appraisal of sensory-neuropeptide/macrophage crosstalk experiment in cited animal and cell studies as reported by the review. methods/readouts recorded in the a-layer: the review proposes cgrp as a context- and time-dependent immunomodulator, but it does not provide a single primary sci experiment demonstrating that cgrp manipulation alone causes functional recovery. specific therapeutic claims require retrieval and extraction of the cited primary studies.',
    'Module 3A full-text extraction; Full text PMC; evidence-boundary assessment',
    'A-layer full text; Full text PMC; evidence-boundary assessment',
    'medium',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P034-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P034-E002", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M3A-P034", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T003", "tracker_id": "M3B-O081"}'
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
    'Full-text source localization for M3A-P035-E002 confirms the curated IL-4 improved BBB by 14 dpi and reduced hindlimb gridwalk errors; it increased IBA1+/ARG1+ and IBA1+/CD206+ macrophages, reduced IBA1+/iNOS+ cells, cystic cavity size, astrogliosis and oligodendrocyte loss, and suppressed 1-7 dpi cytokine surges. Human lower cytokine levels were associated with better neurological outcomes. experiment in Rat SCI model plus human SCI serum. Methods/readouts recorded in the A-layer: Full-text finding supports systemic immunomodulation and translational association, not direct evidence that the rat pathway transfers unchanged to humans.',
    'qualitative',
    'ELISA / cytokine protein assay; barrier / permeability / endothelial assay; behavioral / functional recovery assay',
    'Full-text source localization for M3A-P035-E002 confirms the curated IL-4 improved BBB by 14 dpi and reduced hindlimb gridwalk errors; it increased IBA1+/ARG1+ and IBA1+/CD206+ macrophages, reduced IBA1+/iNOS+ cells, cystic cavity size, astrogliosis and oligodendrocyte loss, and suppressed 1-7 dpi cytokine surges. Human lower cytokine levels were associated with better neurological outcomes. experiment in Rat SCI model plus human SCI serum. Methods/readouts recorded in the A-layer: Full-text finding supports systemic immunomodulation and translational association, not direct evidence that the rat pathway transfers unchanged to humans.',
    'full-text source localization for m3a-p035-e002 confirms the curated il-4 improved bbb by 14 dpi and reduced hindlimb gridwalk errors; it increased iba1+/arg1+ and iba1+/cd206+ macrophages, reduced iba1+/inos+ cells, cystic cavity size, astrogliosis and oligodendrocyte loss, and suppressed 1-7 dpi cytokine surges. human lower cytokine levels were associated with better neurological outcomes. experiment in rat sci model plus human sci serum. methods/readouts recorded in the a-layer: full-text finding supports systemic immunomodulation and translational association, not direct evidence that the rat pathway transfers unchanged to humans.',
    'Module 3A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P035-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P035-E002", "measurement_method_inference": "ELISA / cytokine protein assay; barrier / permeability / endothelial assay; behavioral / functional recovery assay", "paper_tracker_id": "M3A-P035", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T003", "tracker_id": "M3B-O082"}'
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
    'Full-text source localization for M3A-P036-E002 confirms the curated Omaveloxolone with LPS for 24 h in BMDMs; in vivo treatment as above experiment in Mouse SCI model plus bone-marrow-derived macrophage culture. Methods/readouts recorded in the A-layer: In LPS-stimulated BMDMs, omaveloxolone reduced CD86/iNOS-associated M1 polarization and increased CD206-associated M2 polarization. RNA-seq showed lower chemokine and cytokine programs and higher antioxidant or cytoprotective programs; direct Nrf2-to-polarization causality was not fully tested.',
    'qualitative',
    'ELISA / cytokine protein assay; bulk transcriptomics / GEO dataset; pathway activity / phospho-signaling assay; behavioral / functional recovery assay',
    'Full-text source localization for M3A-P036-E002 confirms the curated Omaveloxolone with LPS for 24 h in BMDMs; in vivo treatment as above experiment in Mouse SCI model plus bone-marrow-derived macrophage culture. Methods/readouts recorded in the A-layer: In LPS-stimulated BMDMs, omaveloxolone reduced CD86/iNOS-associated M1 polarization and increased CD206-associated M2 polarization. RNA-seq showed lower chemokine and cytokine programs and higher antioxidant or cytoprotective programs; direct Nrf2-to-polarization causality was not fully tested.',
    'full-text source localization for m3a-p036-e002 confirms the curated omaveloxolone with lps for 24 h in bmdms; in vivo treatment as above experiment in mouse sci model plus bone-marrow-derived macrophage culture. methods/readouts recorded in the a-layer: in lps-stimulated bmdms, omaveloxolone reduced cd86/inos-associated m1 polarization and increased cd206-associated m2 polarization. rna-seq showed lower chemokine and cytokine programs and higher antioxidant or cytoprotective programs; direct nrf2-to-polarization causality was not fully tested.',
    'Module 3A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P036-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P036-E002", "measurement_method_inference": "ELISA / cytokine protein assay; bulk transcriptomics / GEO dataset; pathway activity / phospho-signaling assay; behavioral / functional recovery assay", "paper_tracker_id": "M3A-P036", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T003", "tracker_id": "M3B-O083"}'
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
    'Full-text source localization for M3A-P037-E002 confirms the curated HGIL13 release samples or 20 ng/ml recombinant IL-13 with 10 ng/ml LPS; in vivo HGIL13 as above experiment in BV2 microglia and mouse contusion SCI validation. Methods/readouts recorded in the A-layer: Released IL-13 retained bioactivity, increased Arg1 and CD206 and reduced inflammatory marker expression and TNF-alpha secretion in LPS-stimulated BV2 cells. The in vivo study linked this immune shift to lower microglial activation, improved myelin and tissue outcomes, and better locomotor recovery.',
    'qualitative',
    'ELISA / cytokine protein assay; behavioral / functional recovery assay',
    'Full-text source localization for M3A-P037-E002 confirms the curated HGIL13 release samples or 20 ng/ml recombinant IL-13 with 10 ng/ml LPS; in vivo HGIL13 as above experiment in BV2 microglia and mouse contusion SCI validation. Methods/readouts recorded in the A-layer: Released IL-13 retained bioactivity, increased Arg1 and CD206 and reduced inflammatory marker expression and TNF-alpha secretion in LPS-stimulated BV2 cells. The in vivo study linked this immune shift to lower microglial activation, improved myelin and tissue outcomes, and better locomotor recovery.',
    'full-text source localization for m3a-p037-e002 confirms the curated hgil13 release samples or 20 ng/ml recombinant il-13 with 10 ng/ml lps; in vivo hgil13 as above experiment in bv2 microglia and mouse contusion sci validation. methods/readouts recorded in the a-layer: released il-13 retained bioactivity, increased arg1 and cd206 and reduced inflammatory marker expression and tnf-alpha secretion in lps-stimulated bv2 cells. the in vivo study linked this immune shift to lower microglial activation, improved myelin and tissue outcomes, and better locomotor recovery.',
    'Module 3A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P037-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P037-E002", "measurement_method_inference": "ELISA / cytokine protein assay; behavioral / functional recovery assay", "paper_tracker_id": "M3A-P037", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T007", "tracker_id": "M3B-O084"}'
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
    'Full-text source localization for M3A-P038-E002 confirms the curated Ago-miR-487b-3p@GelNB treatment experiment in Mouse SCI model. Methods/readouts recorded in the A-layer: Ago-miR-487b-3p@GelNB reduced endothelial lipid deposition and EndoMT, suppressed CXCL12-CXCR4 macrophage recruitment and TNF-alpha/GDF15 signaling, promoted neuroregeneration, and improved functional recovery.',
    'qualitative',
    'ELISA / cytokine protein assay; barrier / permeability / endothelial assay; behavioral / functional recovery assay',
    'Full-text source localization for M3A-P038-E002 confirms the curated Ago-miR-487b-3p@GelNB treatment experiment in Mouse SCI model. Methods/readouts recorded in the A-layer: Ago-miR-487b-3p@GelNB reduced endothelial lipid deposition and EndoMT, suppressed CXCL12-CXCR4 macrophage recruitment and TNF-alpha/GDF15 signaling, promoted neuroregeneration, and improved functional recovery.',
    'full-text source localization for m3a-p038-e002 confirms the curated ago-mir-487b-3p@gelnb treatment experiment in mouse sci model. methods/readouts recorded in the a-layer: ago-mir-487b-3p@gelnb reduced endothelial lipid deposition and endomt, suppressed cxcl12-cxcr4 macrophage recruitment and tnf-alpha/gdf15 signaling, promoted neuroregeneration, and improved functional recovery.',
    'Module 3A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P038-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P038-E002", "measurement_method_inference": "ELISA / cytokine protein assay; barrier / permeability / endothelial assay; behavioral / functional recovery assay", "paper_tracker_id": "M3A-P038", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T005", "tracker_id": "M3B-O085"}'
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
    'Full-text source localization for M3A-P039-E002 confirms the curated ROS-responsive thioketal, MG1 microglia-targeting P2Y-TK-Nano carrying P2ry12 plasmid experiment in Mouse and ex vivo spinal cord slices. Methods/readouts recorded in the A-layer: P2Y-TK-Nano showed ROS-responsive lesion accumulation, highest microglial co-localization, and greater restoration of P2Y12R than TK-Nano or P2Y-Nano. At 7 days it reduced lesion cavity and neuronal apoptosis and increased neuronal Tomm20-LC3 co-localization and healthy mitochondria in tissue slices and injured spinal cord.',
    'qualitative',
    NULL,
    'Full-text source localization for M3A-P039-E002 confirms the curated ROS-responsive thioketal, MG1 microglia-targeting P2Y-TK-Nano carrying P2ry12 plasmid experiment in Mouse and ex vivo spinal cord slices. Methods/readouts recorded in the A-layer: P2Y-TK-Nano showed ROS-responsive lesion accumulation, highest microglial co-localization, and greater restoration of P2Y12R than TK-Nano or P2Y-Nano. At 7 days it reduced lesion cavity and neuronal apoptosis and increased neuronal Tomm20-LC3 co-localization and healthy mitochondria in tissue slices and injured spinal cord.',
    'full-text source localization for m3a-p039-e002 confirms the curated ros-responsive thioketal, mg1 microglia-targeting p2y-tk-nano carrying p2ry12 plasmid experiment in mouse and ex vivo spinal cord slices. methods/readouts recorded in the a-layer: p2y-tk-nano showed ros-responsive lesion accumulation, highest microglial co-localization, and greater restoration of p2y12r than tk-nano or p2y-nano. at 7 days it reduced lesion cavity and neuronal apoptosis and increased neuronal tomm20-lc3 co-localization and healthy mitochondria in tissue slices and injured spinal cord.',
    'Module 3A full-text extraction; Full text PMC; Fig. 1-2, 5, and supplementary biodistribution/ex vivo slice assays',
    'A-layer full text; Full text PMC; Fig. 1-2, 5, and supplementary biodistribution/ex vivo slice assays',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P039-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P039-E002", "measurement_method_inference": null, "paper_tracker_id": "M3A-P039", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T005", "tracker_id": "M3B-O086"}'
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
    'Full-text source localization for M3A-P040-E002 confirms the curated PM-Lipo@PB-NPs versus plain PB-NPs experiment in Mouse SCI model. Methods/readouts recorded in the A-layer: PM-Lipo@PB-NPs showed greater lesion accumulation, longer circulation, and higher IBA-1+ microglial uptake than PB-NPs. In vivo treatment was associated with smaller cavities/scars, more preserved NeuN and NEFH, less LFB demyelination, improved footprint/BMS/inclined-plane performance, less reactive microglial morphology, and improved tissue preservation. Because the captured text omits key animal-method details and no single-component membrane controls are reported, the platform’s individual contributions remain unresolved.',
    'qualitative',
    NULL,
    'Full-text source localization for M3A-P040-E002 confirms the curated PM-Lipo@PB-NPs versus plain PB-NPs experiment in Mouse SCI model. Methods/readouts recorded in the A-layer: PM-Lipo@PB-NPs showed greater lesion accumulation, longer circulation, and higher IBA-1+ microglial uptake than PB-NPs. In vivo treatment was associated with smaller cavities/scars, more preserved NeuN and NEFH, less LFB demyelination, improved footprint/BMS/inclined-plane performance, less reactive microglial morphology, and improved tissue preservation. Because the captured text omits key animal-method details and no single-component membrane controls are reported, the platform’s individual contributions remain unresolved.',
    'full-text source localization for m3a-p040-e002 confirms the curated pm-lipo@pb-nps versus plain pb-nps experiment in mouse sci model. methods/readouts recorded in the a-layer: pm-lipo@pb-nps showed greater lesion accumulation, longer circulation, and higher iba-1+ microglial uptake than pb-nps. in vivo treatment was associated with smaller cavities/scars, more preserved neun and nefh, less lfb demyelination, improved footprint/bms/inclined-plane performance, less reactive microglial morphology, and improved tissue preservation. because the captured text omits key animal-method details and no single-component membrane controls are reported, the platform’s individual contributions remain unresolved.',
    'Module 3A full-text extraction; Full text PMC; Fig. 4, 10 and supplementary targeting/repair assays',
    'A-layer full text; Full text PMC; Fig. 4, 10 and supplementary targeting/repair assays',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P040-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P040-E002", "measurement_method_inference": null, "paper_tracker_id": "M3A-P040", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T005", "tracker_id": "M3B-O087"}'
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
    'Full-text source localization for M3A-P041-E002 confirms the curated EPO@MLNP versus EPO@LNP experiment in Mouse SCI model. Methods/readouts recorded in the A-layer: EPO@MLNP preserved more NeuN+ neurons, reduced lesion area, preserved 5-HT axonal signal near the epicenter, and produced the strongest BMS, stride, hind-paw pressure, speed, and inclined-plane recovery through 28 days. EPO@LNP also showed some benefit, so the results support improved targeting rather than proving that the mannose ligand is solely responsible for efficacy.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Full-text source localization for M3A-P041-E002 confirms the curated EPO@MLNP versus EPO@LNP experiment in Mouse SCI model. Methods/readouts recorded in the A-layer: EPO@MLNP preserved more NeuN+ neurons, reduced lesion area, preserved 5-HT axonal signal near the epicenter, and produced the strongest BMS, stride, hind-paw pressure, speed, and inclined-plane recovery through 28 days. EPO@LNP also showed some benefit, so the results support improved targeting rather than proving that the mannose ligand is solely responsible for efficacy.',
    'full-text source localization for m3a-p041-e002 confirms the curated epo@mlnp versus epo@lnp experiment in mouse sci model. methods/readouts recorded in the a-layer: epo@mlnp preserved more neun+ neurons, reduced lesion area, preserved 5-ht axonal signal near the epicenter, and produced the strongest bms, stride, hind-paw pressure, speed, and inclined-plane recovery through 28 days. epo@lnp also showed some benefit, so the results support improved targeting rather than proving that the mannose ligand is solely responsible for efficacy.',
    'Module 3A full-text extraction; Full text PMC; Fig. 5-6',
    'A-layer full text; Full text PMC; Fig. 5-6',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P041-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P041-E002", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M3A-P041", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T005", "tracker_id": "M3B-O088"}'
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
    'Full-text source localization for M3A-P042-E002 confirms the curated Copalic acid 3 micromolar in LPS-treated cultures; 1 mg/kg local injection in reported mouse validation experiment in Rat atlas plus BV2/RAW264.7 cultures and mouse validation model as reported. Methods/readouts recorded in the A-layer: Mac4 was an anti-inflammatory macrophage branch with clustered spatial distribution and copalic-acid enrichment. Copalic acid reduced CD86, CD80, and IL-1beta in LPS-treated BV2 and RAW264.7 cells and increased ARG1 while reducing iNOS after SCI. The paper states mice were used for validation but describes the compression parameters under the rat model, so this species linkage remains unresolved; there was no direct Mac4 depletion or copalic-acid necessity experiment.',
    'qualitative',
    'single-cell RNA-seq / cell-state atlas; spatial transcriptomics / spatial atlas',
    'Full-text source localization for M3A-P042-E002 confirms the curated Copalic acid 3 micromolar in LPS-treated cultures; 1 mg/kg local injection in reported mouse validation experiment in Rat atlas plus BV2/RAW264.7 cultures and mouse validation model as reported. Methods/readouts recorded in the A-layer: Mac4 was an anti-inflammatory macrophage branch with clustered spatial distribution and copalic-acid enrichment. Copalic acid reduced CD86, CD80, and IL-1beta in LPS-treated BV2 and RAW264.7 cells and increased ARG1 while reducing iNOS after SCI. The paper states mice were used for validation but describes the compression parameters under the rat model, so this species linkage remains unresolved; there was no direct Mac4 depletion or copalic-acid necessity experiment.',
    'full-text source localization for m3a-p042-e002 confirms the curated copalic acid 3 micromolar in lps-treated cultures; 1 mg/kg local injection in reported mouse validation experiment in rat atlas plus bv2/raw264.7 cultures and mouse validation model as reported. methods/readouts recorded in the a-layer: mac4 was an anti-inflammatory macrophage branch with clustered spatial distribution and copalic-acid enrichment. copalic acid reduced cd86, cd80, and il-1beta in lps-treated bv2 and raw264.7 cells and increased arg1 while reducing inos after sci. the paper states mice were used for validation but describes the compression parameters under the rat model, so this species linkage remains unresolved; there was no direct mac4 depletion or copalic-acid necessity experiment.',
    'Module 3A full-text extraction; Fig. 4-5 and Supplementary Fig. S8; Mac4/c Copalic-acid validation',
    'A-layer full text; Fig. 4-5 and Supplementary Fig. S8; Mac4/c Copalic-acid validation',
    'medium',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P042-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P042-E002", "measurement_method_inference": "single-cell RNA-seq / cell-state atlas; spatial transcriptomics / spatial atlas", "paper_tracker_id": "M3A-P042", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T005", "tracker_id": "M3B-O089"}'
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
    'Full-text source localization for M3A-P043-E002 confirms the curated Recombinant MDK with pharmacologic LRP-1 inhibition experiment in BV2 microglia and primary fetal-rat cortical neurons. Methods/readouts recorded in the A-layer: MDK restored LPS-impaired efferocytosis, increased LRP-1 and Rac1, activated AKT/mTOR and BDNF, increased IL-10/TGF-beta/CD206, and reduced IL-1beta/TNF-alpha/IL-6 and neuronal apoptosis. RAP abolished the efferocytic, anti-inflammatory, and neuroprotective effects, supporting an MDK-LRP-1 mechanism in vitro; LRP-1 necessity was not directly tested in vivo.',
    'qualitative',
    'ELISA / cytokine protein assay; pathway activity / phospho-signaling assay; behavioral / functional recovery assay',
    'Full-text source localization for M3A-P043-E002 confirms the curated Recombinant MDK with pharmacologic LRP-1 inhibition experiment in BV2 microglia and primary fetal-rat cortical neurons. Methods/readouts recorded in the A-layer: MDK restored LPS-impaired efferocytosis, increased LRP-1 and Rac1, activated AKT/mTOR and BDNF, increased IL-10/TGF-beta/CD206, and reduced IL-1beta/TNF-alpha/IL-6 and neuronal apoptosis. RAP abolished the efferocytic, anti-inflammatory, and neuroprotective effects, supporting an MDK-LRP-1 mechanism in vitro; LRP-1 necessity was not directly tested in vivo.',
    'full-text source localization for m3a-p043-e002 confirms the curated recombinant mdk with pharmacologic lrp-1 inhibition experiment in bv2 microglia and primary fetal-rat cortical neurons. methods/readouts recorded in the a-layer: mdk restored lps-impaired efferocytosis, increased lrp-1 and rac1, activated akt/mtor and bdnf, increased il-10/tgf-beta/cd206, and reduced il-1beta/tnf-alpha/il-6 and neuronal apoptosis. rap abolished the efferocytic, anti-inflammatory, and neuroprotective effects, supporting an mdk-lrp-1 mechanism in vitro; lrp-1 necessity was not directly tested in vivo.',
    'Module 3A full-text extraction; Full text PMC; BV2 efferocytosis and neuronal-protection mechanism assays',
    'A-layer full text; Full text PMC; BV2 efferocytosis and neuronal-protection mechanism assays',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P043-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P043-E002", "measurement_method_inference": "ELISA / cytokine protein assay; pathway activity / phospho-signaling assay; behavioral / functional recovery assay", "paper_tracker_id": "M3A-P043", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T003", "tracker_id": "M3B-O090"}'
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
    'Full-text source localization for M3A-P045-E002 confirms the curated Blocking CXCL4 or PI3K reduced PMT and fibrotic scar deposition, enhanced corticospinal and serotonergic axon regeneration, and improved BMS and footprint outcomes. MAFB was linked to CXCL4 expression in the Spp1+Fn1+ macrophage subset. experiment in Mouse SCI model. Methods/readouts recorded in the A-layer: Full-text result supports a macrophage-to-pericyte fibrotic relay and an intervention-sensitive boundary.',
    'qualitative',
    NULL,
    'Full-text source localization for M3A-P045-E002 confirms the curated Blocking CXCL4 or PI3K reduced PMT and fibrotic scar deposition, enhanced corticospinal and serotonergic axon regeneration, and improved BMS and footprint outcomes. MAFB was linked to CXCL4 expression in the Spp1+Fn1+ macrophage subset. experiment in Mouse SCI model. Methods/readouts recorded in the A-layer: Full-text result supports a macrophage-to-pericyte fibrotic relay and an intervention-sensitive boundary.',
    'full-text source localization for m3a-p045-e002 confirms the curated blocking cxcl4 or pi3k reduced pmt and fibrotic scar deposition, enhanced corticospinal and serotonergic axon regeneration, and improved bms and footprint outcomes. mafb was linked to cxcl4 expression in the spp1+fn1+ macrophage subset. experiment in mouse sci model. methods/readouts recorded in the a-layer: full-text result supports a macrophage-to-pericyte fibrotic relay and an intervention-sensitive boundary.',
    'Module 3A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P045-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P045-E002", "measurement_method_inference": null, "paper_tracker_id": "M3A-P045", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T002", "tracker_id": "M3B-O092"}'
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
    'Full-text source localization for M3A-P046-E002 confirms the curated TGF-beta neutralization and developmental scarless-repair comparison experiment in Mouse SCI model. Methods/readouts recorded in the A-layer: Macrophage or pericyte pathway interruption reduced fibrotic scar and improved functional recovery; neonatal mice recovered scarlessly with no detectable active TGF-beta at the injury site, defining a developmental boundary rather than a universal anti-TGF-beta rule.',
    'qualitative',
    'behavioral / functional recovery assay',
    'Full-text source localization for M3A-P046-E002 confirms the curated TGF-beta neutralization and developmental scarless-repair comparison experiment in Mouse SCI model. Methods/readouts recorded in the A-layer: Macrophage or pericyte pathway interruption reduced fibrotic scar and improved functional recovery; neonatal mice recovered scarlessly with no detectable active TGF-beta at the injury site, defining a developmental boundary rather than a universal anti-TGF-beta rule.',
    'full-text source localization for m3a-p046-e002 confirms the curated tgf-beta neutralization and developmental scarless-repair comparison experiment in mouse sci model. methods/readouts recorded in the a-layer: macrophage or pericyte pathway interruption reduced fibrotic scar and improved functional recovery; neonatal mice recovered scarlessly with no detectable active tgf-beta at the injury site, defining a developmental boundary rather than a universal anti-tgf-beta rule.',
    'Module 3A full-text extraction; Full text PMC',
    'A-layer full text; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P046-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P046-E002", "measurement_method_inference": "behavioral / functional recovery assay", "paper_tracker_id": "M3A-P046", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T002", "tracker_id": "M3B-O093"}'
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
    'Full-text source localization for M3A-P047-E002 confirms the curated Cell-free OEC-conditioned medium experiment in RAW264.7 macrophages and primary rat OECs. Methods/readouts recorded in the A-layer: OEC-conditioned medium suppressed TNF-alpha-induced H3Cit/CD68 MET markers and reduced NKCC1 expression in RAW264.7 macrophages, supporting a secreted-factor mechanism. The active OEC components were not identified, and no in vivo MET or NKCC1 blockade/overexpression was performed.',
    'qualitative',
    'ELISA / cytokine protein assay',
    'Full-text source localization for M3A-P047-E002 confirms the curated Cell-free OEC-conditioned medium experiment in RAW264.7 macrophages and primary rat OECs. Methods/readouts recorded in the A-layer: OEC-conditioned medium suppressed TNF-alpha-induced H3Cit/CD68 MET markers and reduced NKCC1 expression in RAW264.7 macrophages, supporting a secreted-factor mechanism. The active OEC components were not identified, and no in vivo MET or NKCC1 blockade/overexpression was performed.',
    'full-text source localization for m3a-p047-e002 confirms the curated cell-free oec-conditioned medium experiment in raw264.7 macrophages and primary rat oecs. methods/readouts recorded in the a-layer: oec-conditioned medium suppressed tnf-alpha-induced h3cit/cd68 met markers and reduced nkcc1 expression in raw264.7 macrophages, supporting a secreted-factor mechanism. the active oec components were not identified, and no in vivo met or nkcc1 blockade/overexpression was performed.',
    'Module 3A full-text extraction; Full text PMC; OEC-conditioned-medium macrophage assay',
    'A-layer full text; Full text PMC; OEC-conditioned-medium macrophage assay',
    'high',
    '{"curator_notes": "Full-text provenance synchronized from Module 3A M3A-P047-E002; observation wording remains source-bound and does not add an outcome beyond the A-layer extraction.", "experiment_tracker_id": "M3A-P047-E002", "measurement_method_inference": "ELISA / cytokine protein assay", "paper_tracker_id": "M3A-P047", "quantitative": "NO", "statistics_reported": "No statistics promoted here; this synchronization carries the A-layer methods/source locator only.", "topic_id": "M3B-T008", "tracker_id": "M3B-O094"}'
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
    'Module 3A full-text extraction; Full text PMC; Fig. 1-2; Full text PMC; Fig. 3-5',
    'high',
    '{"curator_notes": "Full-text provenance localized; author-claim wording retained and no new claim added.", "source_paper_tracker_id": "M3A-P002", "topic_id": "M3B-T002", "tracker_id": "M3B-C019"}'
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
    'Module 3A full-text extraction; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance localized; author-claim wording retained and no new claim added.", "source_paper_tracker_id": "M3A-P035", "topic_id": "M3B-T003", "tracker_id": "M3B-C020"}'
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
    'Module 3A full-text extraction; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance localized; author-claim wording retained and no new claim added.", "source_paper_tracker_id": "M3A-P024", "topic_id": "M3B-T004", "tracker_id": "M3B-C027"}'
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
    'Module 3A full-text extraction; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance localized; author-claim wording retained and no new claim added.", "source_paper_tracker_id": "M3A-P037", "topic_id": "M3B-T007", "tracker_id": "M3B-C029"}'
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
    'Module 3A full-text extraction; Full text PMC; narrative review scope; Full text PMC; evidence-boundary assessment',
    'medium',
    '{"curator_notes": "Full-text provenance localized; author-claim wording retained and no new claim added.", "source_paper_tracker_id": "M3A-P034", "topic_id": "M3B-T003", "tracker_id": "M3B-C031"}'
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
    'Module 3A full-text extraction; Full text PMC; in vivo time course and LV-MDK validation; Full text PMC; BV2 efferocytosis and neuronal-protection mechanism assays',
    'high',
    '{"curator_notes": "Full-text provenance localized; author-claim wording retained and no new claim added.", "source_paper_tracker_id": "M3A-P043", "topic_id": "M3B-T005", "tracker_id": "M3B-C032"}'
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
    'Module 3A full-text extraction; Full text PMC; in vivo transplantation and pain-recovery assays; Full text PMC; OEC-conditioned-medium macrophage assay',
    'high',
    '{"curator_notes": "Full-text provenance localized; author-claim wording retained and no new claim added.", "source_paper_tracker_id": "M3A-P047", "topic_id": "M3B-T008", "tracker_id": "M3B-C033"}'
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
    'Module 3A full-text extraction; Full text PMC',
    'high',
    '{"curator_notes": "Full-text provenance localized; author-claim wording retained and no new claim added.", "source_paper_tracker_id": "M3A-P038", "topic_id": "M3B-T008", "tracker_id": "M3B-C034"}'
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
