-- Module 4B full first-pass materialization generated from tracker-derived JSON.
-- This script is intended for a fresh database loaded with schema/schema.sql and scripts/seed_controlled_vocab.sql.
BEGIN;

CREATE TEMP TABLE _m4_paper_map (tracker_id TEXT PRIMARY KEY, paper_id INTEGER NOT NULL);
CREATE TEMP TABLE _m4_paradigm_map (tracker_id TEXT PRIMARY KEY, paradigm_id INTEGER NOT NULL);
CREATE TEMP TABLE _m4_experiment_map (tracker_id TEXT PRIMARY KEY, experiment_id INTEGER NOT NULL);
CREATE TEMP TABLE _m4_observation_map (tracker_id TEXT PRIMARY KEY, observation_id INTEGER NOT NULL);
CREATE TEMP TABLE _m4_claim_map (tracker_id TEXT PRIMARY KEY, claim_id INTEGER NOT NULL);
CREATE TEMP TABLE _m4_link_map (tracker_id TEXT PRIMARY KEY, link_id INTEGER NOT NULL);
CREATE TEMP TABLE _m4_consensus_map (tracker_id TEXT PRIMARY KEY, consensus_id INTEGER NOT NULL);

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Axon regeneration through scars and into sites of chronic spinal cord injury', 'Lu P', 2007,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Chronic scar/graft permissiveness anchor", "module": "Module 4B", "tracker_id": "M4A-P001"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P001', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'One-year clinical study of NeuroRegen scaffold implantation following scar resection in complete chronic spinal cord injury patients', 'Xiao Z', 2016,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Human scaffold-cell anchor", "module": "Module 4B", "tracker_id": "M4A-P002"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P002', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Histological effects of combined therapy involving scar resection, decellularized scaffolds, and human iPSC-NS/PCs transplantation in chronic complete spinal cord injury.', 'Ito K', 2024,
    NULL, NULL, NULL,
    NULL, NULL, '39733145',
    NULL, '{"curator_notes": "Chronic complete SCI hNS/PC scaffold anchor", "module": "Module 4B", "tracker_id": "M4A-P003"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P003', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Long-term safety and clinical outcomes from a single-site phase 1 study of neural stem cell transplantation for chronic cervical spinal cord injury.', 'Abraham ME', 2026,
    NULL, NULL, NULL,
    NULL, NULL, '42167221',
    NULL, '{"curator_notes": "Long-term cervical phase I safety/outcomes", "module": "Module 4B", "tracker_id": "M4A-P004"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P004', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Long-term clinical and safety outcomes from a single-site phase 1 study of neural stem cell transplantation for chronic thoracic spinal cord injury.', 'Martin JR', 2024,
    NULL, NULL, NULL,
    NULL, NULL, '39626671',
    NULL, '{"curator_notes": "Long-term thoracic phase I safety/outcomes", "module": "Module 4B", "tracker_id": "M4A-P005"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P005', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Phase 1 Safety Trial of Autologous Human Schwann Cell Transplantation in Chronic Spinal Cord Injury.', 'Gant KL', 2022,
    NULL, NULL, NULL,
    NULL, NULL, '33757304',
    NULL, '{"curator_notes": "Phase I Schwann-cell safety anchor", "module": "Module 4B", "tracker_id": "M4A-P006"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P006', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Multiroute administration of Wharton''s jelly mesenchymal stem cells in chronic complete spinal cord injury: A phase I safety and feasibility study.', 'Kaplan N', 2025,
    NULL, NULL, NULL,
    NULL, NULL, '40503363',
    NULL, '{"curator_notes": "Multiroute MSC phase I feasibility", "module": "Module 4B", "tracker_id": "M4A-P007"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P007', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Transplantation of autologous mesenchymal stromal cells in complete cervical spinal cord injury: a pilot study.', 'Macêdo CT', 2024,
    NULL, NULL, NULL,
    NULL, NULL, '39328312',
    NULL, '{"curator_notes": "Pilot autologous MSC study", "module": "Module 4B", "tracker_id": "M4A-P008"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P008', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Safety and feasibility of autologous olfactory ensheathing cell and bone marrow mesenchymal stem cell co-transplantation in chronic human spinal cord injury: a clinical trial.', 'Zamani H', 2022,
    NULL, NULL, NULL,
    NULL, NULL, '34504283',
    NULL, '{"curator_notes": "OEC/BM-MSC co-transplant feasibility", "module": "Module 4B", "tracker_id": "M4A-P009"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P009', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'NeuroRegen Scaffolds Combined with Autologous Bone Marrow Mononuclear Cells for the Repair of Acute Complete Spinal Cord Injury: A 3-Year Clinical Study.', 'Chen W', 2020,
    NULL, NULL, NULL,
    NULL, NULL, '32862715',
    NULL, '{"curator_notes": "Acute complete scaffold/BMMC clinical anchor", "module": "Module 4B", "tracker_id": "M4A-P010"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P010', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Extensive restoration of forelimb function in primates with spinal cord injury by neural stem cell transplantation.', 'Sinopoulou E', 2025,
    NULL, NULL, NULL,
    NULL, NULL, '41249838',
    NULL, '{"curator_notes": "Primate skilled forelimb recovery anchor", "module": "Module 4B", "tracker_id": "M4A-P011"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P011', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Allogeneic Neural Stem/Progenitor Cells Derived From Embryonic Stem Cells Promote Functional Recovery After Transplantation Into Injured Spinal Cord of Nonhuman Primates.', 'Iwai H', 2015,
    NULL, NULL, NULL,
    NULL, NULL, '26019226',
    NULL, '{"curator_notes": "Non-human primate safety/efficacy bridge", "module": "Module 4B", "tracker_id": "M4A-P012"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P012', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Functional synaptic connectivity of engrafted spinal cord neurons with hindlimb motor circuitry in the injured spinal cord.', 'Tucker A', 2025,
    NULL, NULL, NULL,
    NULL, NULL, '41285866',
    NULL, '{"curator_notes": "Functional synaptic connectivity with hindlimb circuitry", "module": "Module 4B", "tracker_id": "M4A-P013"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P013', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Neural Stem Cell Grafts Form Extensive Synaptic Networks that Integrate with Host Circuits after Spinal Cord Injury.', 'Ceto S', 2020,
    NULL, NULL, NULL,
    NULL, NULL, '32758426',
    NULL, '{"curator_notes": "In vivo graft network integration anchor", "module": "Module 4B", "tracker_id": "M4A-P014"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P014', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Comprehensive Monosynaptic Rabies Virus Mapping of Host Connectivity with Neural Progenitor Grafts after Spinal Cord Injury.', 'Adler AF', 2017,
    NULL, NULL, NULL,
    NULL, NULL, '28479302',
    NULL, '{"curator_notes": "Host connectivity mapping anchor", "module": "Module 4B", "tracker_id": "M4A-P015"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P015', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Grafted neural progenitors integrate and restore synaptic connectivity across the injured spinal cord.', 'Bonner JF', 2011,
    NULL, NULL, NULL,
    NULL, NULL, '21430166',
    NULL, '{"curator_notes": "Relay connectivity across injured cord", "module": "Module 4B", "tracker_id": "M4A-P016"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P016', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Human spinal interneurons repair the injured spinal cord through synaptic integration.', 'Zholudeva LV', 2024,
    NULL, NULL, NULL,
    NULL, NULL, '38260390',
    NULL, '{"curator_notes": "Human interneuron synaptic integration anchor", "module": "Module 4B", "tracker_id": "M4A-P017"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P017', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Engineered thoracic spinal cord organoids for transplantation after spinal cord injury.', 'Zhu Y', 2025,
    NULL, NULL, NULL,
    NULL, NULL, '41136603',
    NULL, '{"curator_notes": "Tissueoid/organoid transplantation anchor", "module": "Module 4B", "tracker_id": "M4A-P018"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P018', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Human iPSC-derived spinal neural progenitors enhance sensorimotor recovery in spinal cord-injured NOD-SCID mice via differentiation and microenvironment regulation.', 'Yao X', 2025,
    NULL, NULL, NULL,
    NULL, NULL, '40846836',
    NULL, '{"curator_notes": "iPSC spinal progenitor differentiation and microenvironment regulation", "module": "Module 4B", "tracker_id": "M4A-P019"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P019', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Functional Recovery by Transplantation of Human iPSC-Derived A2B5 Positive Neural Progenitor Cell After Spinal Cord Injury in Mice.', 'Zheng Y', 2025,
    NULL, NULL, NULL,
    NULL, NULL, '41009511',
    NULL, '{"curator_notes": "A2B5+ iPSC progenitor functional recovery anchor", "module": "Module 4B", "tracker_id": "M4A-P020"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P020', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Rehabilitative Training Enhances Therapeutic Effect of Human-iPSC-Derived Neural Stem/Progenitor Cells Transplantation in Chronic Spinal Cord Injury.', 'Shibata T', 2023,
    NULL, NULL, NULL,
    NULL, NULL, '36647673',
    NULL, '{"curator_notes": "Rehabilitation as graft-effect amplifier", "module": "Module 4B", "tracker_id": "M4A-P021"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P021', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Human-induced pluripotent stem cell-derived neural stem/progenitor cell ex vivo gene therapy with synaptic organizer CPTX for spinal cord injury.', 'Saijo Y', 2024,
    NULL, NULL, NULL,
    NULL, NULL, '38366597',
    NULL, '{"curator_notes": "Ex vivo gene therapy to enhance synapse formation", "module": "Module 4B", "tracker_id": "M4A-P022"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P022', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Hepatocyte growth factor pretreatment boosts functional recovery after spinal cord injury through human iPSC-derived neural stem/progenitor cell transplantation.', 'Suematsu Y', 2023,
    NULL, NULL, NULL,
    NULL, NULL, '37845736',
    NULL, '{"curator_notes": "Microenvironment/growth-factor pretreatment combination", "module": "Module 4B", "tracker_id": "M4A-P023"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P023', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Transplantation of neural stem progenitor cells from different sources for severe spinal cord injury repair in rat.', 'Xu B', 2023,
    NULL, NULL, NULL,
    NULL, NULL, '36439085',
    NULL, '{"curator_notes": "Cell-source comparison anchor", "module": "Module 4B", "tracker_id": "M4A-P024"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P024', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'BDNF guides neural stem cell-derived axons to ventral interneurons and motor neurons after spinal cord injury.', 'Li Y', 2023,
    NULL, NULL, NULL,
    NULL, NULL, '36309123',
    NULL, '{"curator_notes": "Host target guidance of graft-derived axons", "module": "Module 4B", "tracker_id": "M4A-P025"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P025', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Human induced pluripotent stem cell/embryonic stem cell-derived pyramidal neuronal precursors show safety and efficacy in a rat spinal cord injury model.', 'Li M', 2024,
    NULL, NULL, NULL,
    NULL, NULL, '39073571',
    NULL, '{"curator_notes": "Pyramidal neuronal precursor safety/efficacy", "module": "Module 4B", "tracker_id": "M4A-P026"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P026', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Human Embryonic Stem Cell-Derived Oligodendrocyte Progenitor Cells: Preclinical Efficacy and Safety in Cervical Spinal Cord Injury.', 'Manley NC', 2017,
    NULL, NULL, NULL,
    NULL, NULL, '28834391',
    NULL, '{"curator_notes": "OPC preclinical efficacy and safety anchor", "module": "Module 4B", "tracker_id": "M4A-P027"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P027', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Oligodendrogenic neural progenitors for treatment of chronic compressive cervical spinal cord injury.', 'Luo Z', 2025,
    NULL, NULL, NULL,
    NULL, NULL, '41173548',
    NULL, '{"curator_notes": "Chronic compressive cervical progenitor anchor", "module": "Module 4B", "tracker_id": "M4A-P028"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P028', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'DLK1-expressing neural progenitor cells promote tissue repair and functional recovery after cervical spinal cord injury.', 'Hejrati N', 2025,
    NULL, NULL, NULL,
    NULL, NULL, '40448964',
    NULL, '{"curator_notes": "Neural progenitor subtype/tissue repair anchor", "module": "Module 4B", "tracker_id": "M4A-P029"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P029', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Integrated cryopreservation-thawing-transplantation platform for neural stem cell-based spinal cord injury repair.', 'Ren J', 2026,
    NULL, NULL, NULL,
    NULL, NULL, '41657951',
    NULL, '{"curator_notes": "Cryopreservation-thaw-transplant platform", "module": "Module 4B", "tracker_id": "M4A-P030"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P030', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Chondroitinase ABC combined with Schwann cell transplantation enhances restoration of neural connection and functional recovery following acute and chronic spinal cord injury.', 'Qu W', 2025,
    NULL, NULL, NULL,
    NULL, NULL, '39075913',
    NULL, '{"curator_notes": "Schwann/chABC acute and chronic connectivity anchor", "module": "Module 4B", "tracker_id": "M4A-P031"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P031', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Regeneration of Propriospinal Axons in Rat Transected Spinal Cord Injury through a Growth-Promoting Pathway Constructed by Schwann Cells Overexpressing GDNF.', 'Du X', 2024,
    NULL, NULL, NULL,
    NULL, NULL, '38995011',
    NULL, '{"curator_notes": "Propriospinal axon pathway construction", "module": "Module 4B", "tracker_id": "M4A-P032"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P032', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Cotransplantation of glial restricted precursor cells and Schwann cells promotes functional recovery after spinal cord injury.', 'Hu JG', 2013,
    NULL, NULL, NULL,
    NULL, NULL, '23295060',
    NULL, '{"curator_notes": "GRP/Schwann cotransplant functional recovery", "module": "Module 4B", "tracker_id": "M4A-P033"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P033', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'A combination therapy of neural and glial restricted precursor cells and chronic quipazine treatment paired with passive cycling promotes quipazine-induced stepping in adult spinalized rats.', 'Dugan EA', 2015,
    NULL, NULL, NULL,
    NULL, NULL, '25329574',
    NULL, '{"curator_notes": "Cell transplant plus serotonergic pharmacology/rehab-like combination", "module": "Module 4B", "tracker_id": "M4A-P034"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P034', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Transplantation of neuronal and glial restricted precursors into contused spinal cord improves bladder and motor functions, decreases thermal hypersensitivity, and modifies intraspinal circuitry.', 'Mitsui T', 2005,
    NULL, NULL, NULL,
    NULL, NULL, '16237167',
    NULL, '{"curator_notes": "Restricted precursor bladder/motor/sensory circuitry anchor", "module": "Module 4B", "tracker_id": "M4A-P035"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P035', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Olfactory Ensheathing Cell Ameliorate Neuroinflammation Following Spinal Cord Injury Through Upregulating REV-ERBα in Microglia.', 'Zhang L', 2024,
    NULL, NULL, NULL,
    NULL, NULL, '39068549',
    NULL, '{"curator_notes": "OEC microglia/REV-ERBalpha neuroinflammation anchor", "module": "Module 4B", "tracker_id": "M4A-P036"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P036', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Transplantation of olfactory ensheathing cells decreases local and serological monocyte chemoattractant protein 1 level during the acute phase of rat spinal cord injury.', 'Wang Y', 2022,
    NULL, NULL, NULL,
    NULL, NULL, '36250430',
    NULL, '{"curator_notes": "OEC MCP-1/local-serological inflammation anchor", "module": "Module 4B", "tracker_id": "M4A-P037"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P037', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Olfactory mucosal mesenchymal stem cells delivered by gelatin sponge scaffolds promote functional recovery of spinal cord injury.', 'Li W', 2025,
    NULL, NULL, NULL,
    NULL, NULL, '40704099',
    NULL, '{"curator_notes": "Olfactory mucosal MSC scaffold-delivery anchor", "module": "Module 4B", "tracker_id": "M4A-P038"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P038', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Cell Sheets Formation Enhances Therapeutic Effects of Human Umbilical Cord Mesenchymal Stem Cells on Spinal Cord Injury.', 'Zhao Y', 2024,
    NULL, NULL, NULL,
    NULL, NULL, '39670537',
    NULL, '{"curator_notes": "Cell-sheet MSC delivery anchor", "module": "Module 4B", "tracker_id": "M4A-P039"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P039', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Initial IL-10 production dominates the therapy of mesenchymal stem cell scaffold in spinal cord injury.', 'Yang L', 2024,
    NULL, NULL, NULL,
    NULL, NULL, '38169599',
    NULL, '{"curator_notes": "MSC scaffold immunomodulatory mechanism anchor", "module": "Module 4B", "tracker_id": "M4A-P040"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P040', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'ROS-Scavenging Hydrogels Synergize with Neural Stem Cells to Enhance Spinal Cord Injury Repair via Regulating Microenvironment and Facilitating Nerve Regeneration.', 'Liu D', 2023,
    NULL, NULL, NULL,
    NULL, NULL, '36989238',
    NULL, '{"curator_notes": "Microenvironment-modulating hydrogel plus NSC anchor", "module": "Module 4B", "tracker_id": "M4A-P041"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P041', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Spinal cord decellularized matrix scaffold loaded with engineered basic fibroblast growth factor-overexpressed human umbilical cord mesenchymal stromal cells promoted the recovery of spinal cord injury.', 'He W', 2023,
    NULL, NULL, NULL,
    NULL, NULL, '35799479',
    NULL, '{"curator_notes": "Engineered MSC + decellularized matrix scaffold", "module": "Module 4B", "tracker_id": "M4A-P042"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P042', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Conjugated therapy with coaxially printed neural stem cell-laden microfibers and umbilical cord mesenchymal stem cell derived exosomes on complete transactional spinal cord defects.', 'Li X', 2025,
    NULL, NULL, NULL,
    NULL, NULL, '40160243',
    NULL, '{"curator_notes": "Printed NSC/exosome conjugated therapy", "module": "Module 4B", "tracker_id": "M4A-P043"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P043', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Synergistic restoration of spinal cord injury through hyaluronic acid conjugated hydrogel-polydopamine nanoparticles combined with human mesenchymal stem cell transplantation.', 'Kao Y', 2025,
    NULL, NULL, NULL,
    NULL, NULL, '40027446',
    NULL, '{"curator_notes": "hMSC/hydrogel nanoparticle combination", "module": "Module 4B", "tracker_id": "M4A-P044"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P044', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Nitric Oxide-Releasing Mesoporous Hollow Cerium Oxide Nanozyme-Based Hydrogel Synergizes with Neural Stem Cell for Spinal Cord Injury Repair.', 'Liu D', 2025,
    NULL, NULL, NULL,
    NULL, NULL, '39723955',
    NULL, '{"curator_notes": "NO/nanozyme hydrogel plus NSC anchor", "module": "Module 4B", "tracker_id": "M4A-P045"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P045', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Fetal rat neural progenitor cell transplantation after spinal cord injury improves motor recovery following optogenetic stimulation.', 'Sánchez-Martín MDM', 2025,
    NULL, NULL, NULL,
    NULL, NULL, '40734274',
    NULL, '{"curator_notes": "Fetal NPC optogenetic stimulation motor recovery", "module": "Module 4B", "tracker_id": "M4A-P046"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P046', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Transplantation of Human-Fetal-Spinal-Cord-Derived NPCs Primed with a Polyglutamate-Conjugated Rho/Rock Inhibitor in Acute Spinal Cord Injury.', 'Giraldo E', 2022,
    NULL, NULL, NULL,
    NULL, NULL, '36291170',
    NULL, '{"curator_notes": "Human fetal spinal NPC priming acute SCI", "module": "Module 4B", "tracker_id": "M4A-P047"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P047', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Clinical Trial of Human Fetal Brain-Derived Neural Stem/Progenitor Cell Transplantation in Patients with Traumatic Cervical Spinal Cord Injury.', 'Shin JC', 2015,
    NULL, NULL, NULL,
    NULL, NULL, '26568892',
    NULL, '{"curator_notes": "Human fetal NSPC traumatic cervical clinical trial", "module": "Module 4B", "tracker_id": "M4A-P048"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P048', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Human fetal neural stem cells grafted into contusion-injured rat spinal cords improve behavior.', 'Tarasenko YI', 2007,
    NULL, NULL, NULL,
    NULL, NULL, '17075895',
    NULL, '{"curator_notes": "Human fetal NSC grafting into contusion-injured rat cord", "module": "Module 4B", "tracker_id": "M4A-P049"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P049', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'The Therapeutic Effectiveness of Delayed Fetal Spinal Cord Tissue Transplantation on Respiratory Function Following Mid-Cervical Spinal Cord Injury.', 'Lin CC', 2017,
    NULL, NULL, NULL,
    NULL, NULL, '28097486',
    NULL, '{"curator_notes": "Delayed fetal spinal tissue respiratory recovery", "module": "Module 4B", "tracker_id": "M4A-P050"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P050', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'A phase 1/2a dose-escalation study of oligodendrocyte progenitor cells in individuals with subacute cervical spinal cord injury.', 'Fessler RG', 2022,
    NULL, NULL, NULL,
    NULL, NULL, '35901693',
    NULL, '{"curator_notes": "OPC phase 1/2a dose-escalation clinical study", "module": "Module 4B", "tracker_id": "M4A-P051"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P051', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Preclinical safety of human embryonic stem cell-derived oligodendrocyte progenitors supporting clinical trials in spinal cord injury.', 'Priest CA', 2015,
    NULL, NULL, NULL,
    NULL, NULL, '26345388',
    NULL, '{"curator_notes": "hESC-OPC preclinical safety for SCI clinical trials", "module": "Module 4B", "tracker_id": "M4A-P052"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P052', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Safety of Autologous Human Schwann Cell Transplantation in Subacute Thoracic Spinal Cord Injury.', 'Anderson KD', 2017,
    NULL, NULL, NULL,
    NULL, NULL, '28225648',
    NULL, '{"curator_notes": "Autologous Schwann cell subacute thoracic safety", "module": "Module 4B", "tracker_id": "M4A-P053"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P053', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Transplanting Neural Progenitor Cells Improves Neural Regulation But Not Hormonal Reliance of Cardiovascular Function Following Spinal Cord Injury.', 'Trueblood CT', 2025,
    NULL, NULL, NULL,
    NULL, NULL, '40841167',
    NULL, '{"curator_notes": "Neural progenitor cardiovascular/autonomic regulation", "module": "Module 4B", "tracker_id": "M4A-P054"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P054', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Improvement of Neurogenic Bladder Dysfunction Following Combined Cell Therapy with Mesenchymal Stem Cell and Schwann Cell in Spinal Cord Injury: A Randomized, Open-Label, Phase II Clinical Trial.', 'Akhlaghpasand M', 2025,
    NULL, NULL, NULL,
    NULL, NULL, '39522809',
    NULL, '{"curator_notes": "Combined MSC/Schwann neurogenic bladder clinical outcome", "module": "Module 4B", "tracker_id": "M4A-P055"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P055', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Effects of Combined Intrathecal Mesenchymal Stem Cells and Schwann Cells Transplantation on Neuropathic Pain in Complete Spinal Cord Injury: A Phase II Randomized Active-Controlled Trial.', 'Akhlaghpasand M', 2025,
    NULL, NULL, NULL,
    NULL, NULL, '39874104',
    NULL, '{"curator_notes": "Combined MSC/Schwann neuropathic pain clinical outcome", "module": "Module 4B", "tracker_id": "M4A-P056"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P056', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Olfactory mucosa autografts in human spinal cord injury: a pilot clinical study.', 'Lima C', 2006,
    NULL, NULL, NULL,
    NULL, NULL, '16859223',
    NULL, '{"curator_notes": "Olfactory mucosa autograft human pilot", "module": "Module 4B", "tracker_id": "M4A-P057"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P057', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'A Pilot Clinical Study of Olfactory Mucosa Autograft for Chronic Complete Spinal Cord Injury.', 'Iwatsuki K', 2016,
    NULL, NULL, NULL,
    NULL, NULL, '27053327',
    NULL, '{"curator_notes": "Olfactory mucosa autograft chronic complete pilot", "module": "Module 4B", "tracker_id": "M4A-P058"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P058', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Combinatory repair strategy to promote axon regeneration and functional recovery after chronic spinal cord injury.', 'DePaul MA', 2017,
    NULL, NULL, NULL,
    NULL, NULL, '28827771',
    NULL, '{"curator_notes": "Combinatory repair strategy after chronic SCI", "module": "Module 4B", "tracker_id": "M4A-P059"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P059', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Phase I-II Clinical Trial Assessing Safety and Efficacy of Umbilical Cord Blood Mononuclear Cell Transplant Therapy of Chronic Complete Spinal Cord Injury.', 'Zhu H', 2016,
    NULL, NULL, NULL,
    NULL, NULL, '27075659',
    NULL, '{"curator_notes": "UCB mononuclear phase I/II clinical trial", "module": "Module 4B", "tracker_id": "M4A-P060"}'
  )
  RETURNING paper_id
)
INSERT INTO _m4_paper_map (tracker_id, paper_id) SELECT 'M4A-P060', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P001',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P001'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P001', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P002',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P002'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P002', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P003',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P003'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P003', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P004',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P004'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P004', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P005',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P005'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P005', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P006',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P006'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P006', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P007',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P007'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P007', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P008',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P008'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P008', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P009',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P009'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P009', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P010',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P010'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P010', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P011',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P011'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P011', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P012',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P012'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P012', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P013',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P013'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P013', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P014',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P014'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P014', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P015',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P015'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P015', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P016',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P016'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P016', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P017',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P017'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P017', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P018',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P018'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P018', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P019',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P019'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P019', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P020',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P020'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P020', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P021',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P021'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P021', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P022',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P022'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P022', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P023',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P023'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P023', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P024',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P024'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P024', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P025',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P025'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P025', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P026',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P026'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P026', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P027',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P027'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P027', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P028',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P028'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P028', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P029',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P029'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P029', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P030',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P030'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P030', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P031',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P031'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P031', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P032',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P032'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P032', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P033',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P033'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P033', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P034',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P034'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P034', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P035',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P035'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P035', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P036',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P036'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P036', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P037',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P037'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P037', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P038',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P038'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P038', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P039',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P039'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P039', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P040',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P040'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P040', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P041',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P041'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P041', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P042',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P042'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P042', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P043',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P043'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P043', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P044',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P044'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P044', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P045',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P045'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P045', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P046',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P046'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P046', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P047',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P047'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P047', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P048',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P048'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P048', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P049',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P049'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P049', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P050',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P050'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P050', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P051',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P051'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P051', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P052',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P052'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P052', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P053',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P053'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P053', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P054',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P054'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P054', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P055',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P055'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P055', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P056',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P056'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P056', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P057',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P057'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P057', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P058',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P058'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P058', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P059',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P059'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P059', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 4B curated evidence extraction',
    'First-pass Module 4B cell transplantation and graft integration curation for M4A-P060',
    'Tracker-derived materialization from Module_4B_TRACKER.md'
  FROM _m4_paper_map WHERE tracker_id = 'M4A-P060'
  RETURNING paradigm_id
)
INSERT INTO _m4_paradigm_map (tracker_id, paradigm_id) SELECT 'M4A-P060', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P001-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O001"], "source_experiment_tracker_id": "M4A-P001-E001", "source_paper_tracker_id": "M4A-P001", "tracker_key": "M4A-P001::M4A-P001-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P001'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P001::M4A-P001-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed metadata',
    'Tracker experiment M4A-P001-E002',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O061"], "source_experiment_tracker_id": "M4A-P001-E002", "source_paper_tracker_id": "M4A-P001", "tracker_key": "M4A-P001::M4A-P001-E002"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P001'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P001::M4A-P001-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P002-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O002"], "source_experiment_tracker_id": "M4A-P002-E001", "source_paper_tracker_id": "M4A-P002", "tracker_key": "M4A-P002::M4A-P002-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P002'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P002::M4A-P002-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P003-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O003"], "source_experiment_tracker_id": "M4A-P003-E001", "source_paper_tracker_id": "M4A-P003", "tracker_key": "M4A-P003::M4A-P003-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P003'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P003::M4A-P003-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed metadata',
    'Tracker experiment M4A-P003-E002',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O062"], "source_experiment_tracker_id": "M4A-P003-E002", "source_paper_tracker_id": "M4A-P003", "tracker_key": "M4A-P003::M4A-P003-E002"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P003'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P003::M4A-P003-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P004-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O004"], "source_experiment_tracker_id": "M4A-P004-E001", "source_paper_tracker_id": "M4A-P004", "tracker_key": "M4A-P004::M4A-P004-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P004'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P004::M4A-P004-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed metadata',
    'Tracker experiment M4A-P004-E002',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O063"], "source_experiment_tracker_id": "M4A-P004-E002", "source_paper_tracker_id": "M4A-P004", "tracker_key": "M4A-P004::M4A-P004-E002"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P004'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P004::M4A-P004-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P005-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O005"], "source_experiment_tracker_id": "M4A-P005-E001", "source_paper_tracker_id": "M4A-P005", "tracker_key": "M4A-P005::M4A-P005-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P005'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P005::M4A-P005-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed metadata',
    'Tracker experiment M4A-P005-E002',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O064"], "source_experiment_tracker_id": "M4A-P005-E002", "source_paper_tracker_id": "M4A-P005", "tracker_key": "M4A-P005::M4A-P005-E002"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P005'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P005::M4A-P005-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P006-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O006"], "source_experiment_tracker_id": "M4A-P006-E001", "source_paper_tracker_id": "M4A-P006", "tracker_key": "M4A-P006::M4A-P006-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P006'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P006::M4A-P006-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed metadata',
    'Tracker experiment M4A-P006-E002',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O065"], "source_experiment_tracker_id": "M4A-P006-E002", "source_paper_tracker_id": "M4A-P006", "tracker_key": "M4A-P006::M4A-P006-E002"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P006'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P006::M4A-P006-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P007-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O007"], "source_experiment_tracker_id": "M4A-P007-E001", "source_paper_tracker_id": "M4A-P007", "tracker_key": "M4A-P007::M4A-P007-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P007'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P007::M4A-P007-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed metadata',
    'Tracker experiment M4A-P007-E002',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O066"], "source_experiment_tracker_id": "M4A-P007-E002", "source_paper_tracker_id": "M4A-P007", "tracker_key": "M4A-P007::M4A-P007-E002"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P007'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P007::M4A-P007-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P008-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O008"], "source_experiment_tracker_id": "M4A-P008-E001", "source_paper_tracker_id": "M4A-P008", "tracker_key": "M4A-P008::M4A-P008-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P008'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P008::M4A-P008-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed metadata',
    'Tracker experiment M4A-P008-E002',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O067"], "source_experiment_tracker_id": "M4A-P008-E002", "source_paper_tracker_id": "M4A-P008", "tracker_key": "M4A-P008::M4A-P008-E002"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P008'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P008::M4A-P008-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P009-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O009"], "source_experiment_tracker_id": "M4A-P009-E001", "source_paper_tracker_id": "M4A-P009", "tracker_key": "M4A-P009::M4A-P009-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P009'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P009::M4A-P009-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed metadata',
    'Tracker experiment M4A-P009-E002',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O068"], "source_experiment_tracker_id": "M4A-P009-E002", "source_paper_tracker_id": "M4A-P009", "tracker_key": "M4A-P009::M4A-P009-E002"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P009'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P009::M4A-P009-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P010-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O010"], "source_experiment_tracker_id": "M4A-P010-E001", "source_paper_tracker_id": "M4A-P010", "tracker_key": "M4A-P010::M4A-P010-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P010'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P010::M4A-P010-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P011-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O011"], "source_experiment_tracker_id": "M4A-P011-E001", "source_paper_tracker_id": "M4A-P011", "tracker_key": "M4A-P011::M4A-P011-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P011'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P011::M4A-P011-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed metadata',
    'Tracker experiment M4A-P011-E002',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O069"], "source_experiment_tracker_id": "M4A-P011-E002", "source_paper_tracker_id": "M4A-P011", "tracker_key": "M4A-P011::M4A-P011-E002"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P011'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P011::M4A-P011-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P012-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O012"], "source_experiment_tracker_id": "M4A-P012-E001", "source_paper_tracker_id": "M4A-P012", "tracker_key": "M4A-P012::M4A-P012-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P012'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P012::M4A-P012-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed metadata',
    'Tracker experiment M4A-P012-E002',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O070"], "source_experiment_tracker_id": "M4A-P012-E002", "source_paper_tracker_id": "M4A-P012", "tracker_key": "M4A-P012::M4A-P012-E002"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P012'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P012::M4A-P012-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P013-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O013"], "source_experiment_tracker_id": "M4A-P013-E001", "source_paper_tracker_id": "M4A-P013", "tracker_key": "M4A-P013::M4A-P013-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P013'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P013::M4A-P013-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed metadata',
    'Tracker experiment M4A-P013-E002',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O071"], "source_experiment_tracker_id": "M4A-P013-E002", "source_paper_tracker_id": "M4A-P013", "tracker_key": "M4A-P013::M4A-P013-E002"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P013'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P013::M4A-P013-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P014-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O014"], "source_experiment_tracker_id": "M4A-P014-E001", "source_paper_tracker_id": "M4A-P014", "tracker_key": "M4A-P014::M4A-P014-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P014'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P014::M4A-P014-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed metadata',
    'Tracker experiment M4A-P014-E002',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O072"], "source_experiment_tracker_id": "M4A-P014-E002", "source_paper_tracker_id": "M4A-P014", "tracker_key": "M4A-P014::M4A-P014-E002"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P014'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P014::M4A-P014-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P015-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O015"], "source_experiment_tracker_id": "M4A-P015-E001", "source_paper_tracker_id": "M4A-P015", "tracker_key": "M4A-P015::M4A-P015-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P015'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P015::M4A-P015-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P016-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O016"], "source_experiment_tracker_id": "M4A-P016-E001", "source_paper_tracker_id": "M4A-P016", "tracker_key": "M4A-P016::M4A-P016-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P016'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P016::M4A-P016-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed metadata',
    'Tracker experiment M4A-P016-E002',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O073"], "source_experiment_tracker_id": "M4A-P016-E002", "source_paper_tracker_id": "M4A-P016", "tracker_key": "M4A-P016::M4A-P016-E002"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P016'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P016::M4A-P016-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P017-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O017"], "source_experiment_tracker_id": "M4A-P017-E001", "source_paper_tracker_id": "M4A-P017", "tracker_key": "M4A-P017::M4A-P017-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P017'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P017::M4A-P017-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P018-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O018"], "source_experiment_tracker_id": "M4A-P018-E001", "source_paper_tracker_id": "M4A-P018", "tracker_key": "M4A-P018::M4A-P018-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P018'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P018::M4A-P018-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed metadata',
    'Tracker experiment M4A-P018-E002',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O074"], "source_experiment_tracker_id": "M4A-P018-E002", "source_paper_tracker_id": "M4A-P018", "tracker_key": "M4A-P018::M4A-P018-E002"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P018'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P018::M4A-P018-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P019-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O019"], "source_experiment_tracker_id": "M4A-P019-E001", "source_paper_tracker_id": "M4A-P019", "tracker_key": "M4A-P019::M4A-P019-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P019'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P019::M4A-P019-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed metadata',
    'Tracker experiment M4A-P019-E002',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O075"], "source_experiment_tracker_id": "M4A-P019-E002", "source_paper_tracker_id": "M4A-P019", "tracker_key": "M4A-P019::M4A-P019-E002"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P019'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P019::M4A-P019-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P020-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O020"], "source_experiment_tracker_id": "M4A-P020-E001", "source_paper_tracker_id": "M4A-P020", "tracker_key": "M4A-P020::M4A-P020-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P020'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P020::M4A-P020-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed metadata',
    'Tracker experiment M4A-P020-E002',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O076"], "source_experiment_tracker_id": "M4A-P020-E002", "source_paper_tracker_id": "M4A-P020", "tracker_key": "M4A-P020::M4A-P020-E002"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P020'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P020::M4A-P020-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P021-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O021"], "source_experiment_tracker_id": "M4A-P021-E001", "source_paper_tracker_id": "M4A-P021", "tracker_key": "M4A-P021::M4A-P021-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P021'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P021::M4A-P021-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed metadata',
    'Tracker experiment M4A-P021-E002',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O077"], "source_experiment_tracker_id": "M4A-P021-E002", "source_paper_tracker_id": "M4A-P021", "tracker_key": "M4A-P021::M4A-P021-E002"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P021'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P021::M4A-P021-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P022-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O022"], "source_experiment_tracker_id": "M4A-P022-E001", "source_paper_tracker_id": "M4A-P022", "tracker_key": "M4A-P022::M4A-P022-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P022'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P022::M4A-P022-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed metadata',
    'Tracker experiment M4A-P022-E002',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O078"], "source_experiment_tracker_id": "M4A-P022-E002", "source_paper_tracker_id": "M4A-P022", "tracker_key": "M4A-P022::M4A-P022-E002"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P022'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P022::M4A-P022-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P023-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O023"], "source_experiment_tracker_id": "M4A-P023-E001", "source_paper_tracker_id": "M4A-P023", "tracker_key": "M4A-P023::M4A-P023-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P023'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P023::M4A-P023-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed metadata',
    'Tracker experiment M4A-P023-E002',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O079"], "source_experiment_tracker_id": "M4A-P023-E002", "source_paper_tracker_id": "M4A-P023", "tracker_key": "M4A-P023::M4A-P023-E002"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P023'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P023::M4A-P023-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P024-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O024"], "source_experiment_tracker_id": "M4A-P024-E001", "source_paper_tracker_id": "M4A-P024", "tracker_key": "M4A-P024::M4A-P024-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P024'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P024::M4A-P024-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P025-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O025"], "source_experiment_tracker_id": "M4A-P025-E001", "source_paper_tracker_id": "M4A-P025", "tracker_key": "M4A-P025::M4A-P025-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P025'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P025::M4A-P025-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed metadata',
    'Tracker experiment M4A-P025-E002',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O080"], "source_experiment_tracker_id": "M4A-P025-E002", "source_paper_tracker_id": "M4A-P025", "tracker_key": "M4A-P025::M4A-P025-E002"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P025'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P025::M4A-P025-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P026-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O026"], "source_experiment_tracker_id": "M4A-P026-E001", "source_paper_tracker_id": "M4A-P026", "tracker_key": "M4A-P026::M4A-P026-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P026'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P026::M4A-P026-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P027-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O027"], "source_experiment_tracker_id": "M4A-P027-E001", "source_paper_tracker_id": "M4A-P027", "tracker_key": "M4A-P027::M4A-P027-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P027'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P027::M4A-P027-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed metadata',
    'Tracker experiment M4A-P027-E002',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O081"], "source_experiment_tracker_id": "M4A-P027-E002", "source_paper_tracker_id": "M4A-P027", "tracker_key": "M4A-P027::M4A-P027-E002"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P027'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P027::M4A-P027-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P028-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O028"], "source_experiment_tracker_id": "M4A-P028-E001", "source_paper_tracker_id": "M4A-P028", "tracker_key": "M4A-P028::M4A-P028-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P028'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P028::M4A-P028-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed metadata',
    'Tracker experiment M4A-P028-E002',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O082"], "source_experiment_tracker_id": "M4A-P028-E002", "source_paper_tracker_id": "M4A-P028", "tracker_key": "M4A-P028::M4A-P028-E002"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P028'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P028::M4A-P028-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P029-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O029"], "source_experiment_tracker_id": "M4A-P029-E001", "source_paper_tracker_id": "M4A-P029", "tracker_key": "M4A-P029::M4A-P029-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P029'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P029::M4A-P029-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P030-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O030"], "source_experiment_tracker_id": "M4A-P030-E001", "source_paper_tracker_id": "M4A-P030", "tracker_key": "M4A-P030::M4A-P030-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P030'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P030::M4A-P030-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed metadata',
    'Tracker experiment M4A-P030-E002',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O083"], "source_experiment_tracker_id": "M4A-P030-E002", "source_paper_tracker_id": "M4A-P030", "tracker_key": "M4A-P030::M4A-P030-E002"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P030'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P030::M4A-P030-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P031-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O031"], "source_experiment_tracker_id": "M4A-P031-E001", "source_paper_tracker_id": "M4A-P031", "tracker_key": "M4A-P031::M4A-P031-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P031'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P031::M4A-P031-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed metadata',
    'Tracker experiment M4A-P031-E002',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O084"], "source_experiment_tracker_id": "M4A-P031-E002", "source_paper_tracker_id": "M4A-P031", "tracker_key": "M4A-P031::M4A-P031-E002"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P031'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P031::M4A-P031-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P032-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O032"], "source_experiment_tracker_id": "M4A-P032-E001", "source_paper_tracker_id": "M4A-P032", "tracker_key": "M4A-P032::M4A-P032-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P032'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P032::M4A-P032-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed metadata',
    'Tracker experiment M4A-P032-E002',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O085"], "source_experiment_tracker_id": "M4A-P032-E002", "source_paper_tracker_id": "M4A-P032", "tracker_key": "M4A-P032::M4A-P032-E002"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P032'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P032::M4A-P032-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P033-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O033"], "source_experiment_tracker_id": "M4A-P033-E001", "source_paper_tracker_id": "M4A-P033", "tracker_key": "M4A-P033::M4A-P033-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P033'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P033::M4A-P033-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed metadata',
    'Tracker experiment M4A-P033-E002',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O086"], "source_experiment_tracker_id": "M4A-P033-E002", "source_paper_tracker_id": "M4A-P033", "tracker_key": "M4A-P033::M4A-P033-E002"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P033'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P033::M4A-P033-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P034-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O034"], "source_experiment_tracker_id": "M4A-P034-E001", "source_paper_tracker_id": "M4A-P034", "tracker_key": "M4A-P034::M4A-P034-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P034'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P034::M4A-P034-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed metadata',
    'Tracker experiment M4A-P034-E002',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O087"], "source_experiment_tracker_id": "M4A-P034-E002", "source_paper_tracker_id": "M4A-P034", "tracker_key": "M4A-P034::M4A-P034-E002"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P034'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P034::M4A-P034-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P035-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O035"], "source_experiment_tracker_id": "M4A-P035-E001", "source_paper_tracker_id": "M4A-P035", "tracker_key": "M4A-P035::M4A-P035-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P035'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P035::M4A-P035-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed metadata',
    'Tracker experiment M4A-P035-E002',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O088"], "source_experiment_tracker_id": "M4A-P035-E002", "source_paper_tracker_id": "M4A-P035", "tracker_key": "M4A-P035::M4A-P035-E002"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P035'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P035::M4A-P035-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P036-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O036"], "source_experiment_tracker_id": "M4A-P036-E001", "source_paper_tracker_id": "M4A-P036", "tracker_key": "M4A-P036::M4A-P036-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P036'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P036::M4A-P036-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed metadata',
    'Tracker experiment M4A-P036-E002',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O089"], "source_experiment_tracker_id": "M4A-P036-E002", "source_paper_tracker_id": "M4A-P036", "tracker_key": "M4A-P036::M4A-P036-E002"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P036'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P036::M4A-P036-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P037-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O037"], "source_experiment_tracker_id": "M4A-P037-E001", "source_paper_tracker_id": "M4A-P037", "tracker_key": "M4A-P037::M4A-P037-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P037'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P037::M4A-P037-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed metadata',
    'Tracker experiment M4A-P037-E002',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O090"], "source_experiment_tracker_id": "M4A-P037-E002", "source_paper_tracker_id": "M4A-P037", "tracker_key": "M4A-P037::M4A-P037-E002"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P037'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P037::M4A-P037-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P038-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O038"], "source_experiment_tracker_id": "M4A-P038-E001", "source_paper_tracker_id": "M4A-P038", "tracker_key": "M4A-P038::M4A-P038-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P038'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P038::M4A-P038-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed metadata',
    'Tracker experiment M4A-P038-E002',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O091"], "source_experiment_tracker_id": "M4A-P038-E002", "source_paper_tracker_id": "M4A-P038", "tracker_key": "M4A-P038::M4A-P038-E002"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P038'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P038::M4A-P038-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P039-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O039"], "source_experiment_tracker_id": "M4A-P039-E001", "source_paper_tracker_id": "M4A-P039", "tracker_key": "M4A-P039::M4A-P039-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P039'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P039::M4A-P039-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed metadata',
    'Tracker experiment M4A-P039-E002',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O092"], "source_experiment_tracker_id": "M4A-P039-E002", "source_paper_tracker_id": "M4A-P039", "tracker_key": "M4A-P039::M4A-P039-E002"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P039'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P039::M4A-P039-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P040-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O040"], "source_experiment_tracker_id": "M4A-P040-E001", "source_paper_tracker_id": "M4A-P040", "tracker_key": "M4A-P040::M4A-P040-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P040'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P040::M4A-P040-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed metadata',
    'Tracker experiment M4A-P040-E002',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O093"], "source_experiment_tracker_id": "M4A-P040-E002", "source_paper_tracker_id": "M4A-P040", "tracker_key": "M4A-P040::M4A-P040-E002"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P040'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P040::M4A-P040-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P041-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O041"], "source_experiment_tracker_id": "M4A-P041-E001", "source_paper_tracker_id": "M4A-P041", "tracker_key": "M4A-P041::M4A-P041-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P041'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P041::M4A-P041-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed metadata',
    'Tracker experiment M4A-P041-E002',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O094"], "source_experiment_tracker_id": "M4A-P041-E002", "source_paper_tracker_id": "M4A-P041", "tracker_key": "M4A-P041::M4A-P041-E002"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P041'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P041::M4A-P041-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P042-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O042"], "source_experiment_tracker_id": "M4A-P042-E001", "source_paper_tracker_id": "M4A-P042", "tracker_key": "M4A-P042::M4A-P042-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P042'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P042::M4A-P042-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed metadata',
    'Tracker experiment M4A-P042-E002',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O095"], "source_experiment_tracker_id": "M4A-P042-E002", "source_paper_tracker_id": "M4A-P042", "tracker_key": "M4A-P042::M4A-P042-E002"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P042'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P042::M4A-P042-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P043-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O043"], "source_experiment_tracker_id": "M4A-P043-E001", "source_paper_tracker_id": "M4A-P043", "tracker_key": "M4A-P043::M4A-P043-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P043'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P043::M4A-P043-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed metadata',
    'Tracker experiment M4A-P043-E002',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O096"], "source_experiment_tracker_id": "M4A-P043-E002", "source_paper_tracker_id": "M4A-P043", "tracker_key": "M4A-P043::M4A-P043-E002"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P043'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P043::M4A-P043-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P044-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O044"], "source_experiment_tracker_id": "M4A-P044-E001", "source_paper_tracker_id": "M4A-P044", "tracker_key": "M4A-P044::M4A-P044-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P044'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P044::M4A-P044-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed metadata',
    'Tracker experiment M4A-P044-E002',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O097"], "source_experiment_tracker_id": "M4A-P044-E002", "source_paper_tracker_id": "M4A-P044", "tracker_key": "M4A-P044::M4A-P044-E002"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P044'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P044::M4A-P044-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P045-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O045"], "source_experiment_tracker_id": "M4A-P045-E001", "source_paper_tracker_id": "M4A-P045", "tracker_key": "M4A-P045::M4A-P045-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P045'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P045::M4A-P045-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract / PubMed metadata',
    'Tracker experiment M4A-P045-E002',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O098"], "source_experiment_tracker_id": "M4A-P045-E002", "source_paper_tracker_id": "M4A-P045", "tracker_key": "M4A-P045::M4A-P045-E002"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P045'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P045::M4A-P045-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P046-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O046"], "source_experiment_tracker_id": "M4A-P046-E001", "source_paper_tracker_id": "M4A-P046", "tracker_key": "M4A-P046::M4A-P046-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P046'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P046::M4A-P046-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P047-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O047"], "source_experiment_tracker_id": "M4A-P047-E001", "source_paper_tracker_id": "M4A-P047", "tracker_key": "M4A-P047::M4A-P047-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P047'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P047::M4A-P047-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P048-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O048"], "source_experiment_tracker_id": "M4A-P048-E001", "source_paper_tracker_id": "M4A-P048", "tracker_key": "M4A-P048::M4A-P048-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P048'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P048::M4A-P048-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P049-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O049"], "source_experiment_tracker_id": "M4A-P049-E001", "source_paper_tracker_id": "M4A-P049", "tracker_key": "M4A-P049::M4A-P049-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P049'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P049::M4A-P049-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P050-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O050"], "source_experiment_tracker_id": "M4A-P050-E001", "source_paper_tracker_id": "M4A-P050", "tracker_key": "M4A-P050::M4A-P050-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P050'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P050::M4A-P050-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P051-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O051"], "source_experiment_tracker_id": "M4A-P051-E001", "source_paper_tracker_id": "M4A-P051", "tracker_key": "M4A-P051::M4A-P051-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P051'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P051::M4A-P051-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P052-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O052"], "source_experiment_tracker_id": "M4A-P052-E001", "source_paper_tracker_id": "M4A-P052", "tracker_key": "M4A-P052::M4A-P052-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P052'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P052::M4A-P052-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P053-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O053"], "source_experiment_tracker_id": "M4A-P053-E001", "source_paper_tracker_id": "M4A-P053", "tracker_key": "M4A-P053::M4A-P053-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P053'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P053::M4A-P053-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P054-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O054"], "source_experiment_tracker_id": "M4A-P054-E001", "source_paper_tracker_id": "M4A-P054", "tracker_key": "M4A-P054::M4A-P054-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P054'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P054::M4A-P054-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P055-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O055"], "source_experiment_tracker_id": "M4A-P055-E001", "source_paper_tracker_id": "M4A-P055", "tracker_key": "M4A-P055::M4A-P055-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P055'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P055::M4A-P055-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P056-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O056"], "source_experiment_tracker_id": "M4A-P056-E001", "source_paper_tracker_id": "M4A-P056", "tracker_key": "M4A-P056::M4A-P056-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P056'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P056::M4A-P056-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P057-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O057"], "source_experiment_tracker_id": "M4A-P057-E001", "source_paper_tracker_id": "M4A-P057", "tracker_key": "M4A-P057::M4A-P057-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P057'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P057::M4A-P057-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P058-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O058"], "source_experiment_tracker_id": "M4A-P058-E001", "source_paper_tracker_id": "M4A-P058", "tracker_key": "M4A-P058::M4A-P058-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P058'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P058::M4A-P058-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P059-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O059"], "source_experiment_tracker_id": "M4A-P059-E001", "source_paper_tracker_id": "M4A-P059", "tracker_key": "M4A-P059::M4A-P059-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P059'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P059::M4A-P059-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract / carried',
    'Tracker experiment M4A-P060-E001',
    'Module 4B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M4B-O060"], "source_experiment_tracker_id": "M4A-P060-E001", "source_paper_tracker_id": "M4A-P060", "tracker_key": "M4A-P060::M4A-P060-E001"}'
  FROM _m4_paper_map p
  JOIN _m4_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M4A-P060'
  RETURNING experiment_id
)
INSERT INTO _m4_experiment_map (tracker_id, experiment_id) SELECT 'M4A-P060::M4A-P060-E001', experiment_id FROM inserted;

INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Clinical intervention', 'Module 4B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Combination scaffold-cell intervention', 'Module 4B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Glial-lineage intervention', 'Module 4B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Legacy or specialized graft intervention', 'Module 4B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Neural graft intervention', 'Module 4B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Trophic or immunomodulatory cell intervention', 'Module 4B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;

INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Autonomic / respiratory / motor / historical translation', 'Module 4B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Autonomic, bladder, pain, or respiratory endpoint', 'Module 4B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Combination-enhanced neural graft function', 'Module 4B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Delivery / microenvironment / regeneration', 'Module 4B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Differentiation / synaptic integration / recovery', 'Module 4B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Inflammation / trophic support / clinical feasibility', 'Module 4B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('OPC / oligodendrogenic safety and repair', 'Module 4B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Remyelination / axon support / autonomic or motor outcome', 'Module 4B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Safety / feasibility / clinical outcome', 'Module 4B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Schwann / glial support', 'Module 4B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Second abstract-level experiment row isolates the primary mechanistic endpoint for BDNF axon guidance: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.', 'Module 4B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Second abstract-level experiment row isolates the primary mechanistic endpoint for GRP Schwann combination: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.', 'Module 4B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Second abstract-level experiment row isolates the primary mechanistic endpoint for MSC IL-10 scaffold: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.', 'Module 4B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Second abstract-level experiment row isolates the primary mechanistic endpoint for MSC cell sheet: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.', 'Module 4B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Second abstract-level experiment row isolates the primary mechanistic endpoint for MSC hydrogel nanoparticle: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.', 'Module 4B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Second abstract-level experiment row isolates the primary mechanistic endpoint for NRP GRP quipazine: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.', 'Module 4B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Second abstract-level experiment row isolates the primary mechanistic endpoint for NRP/GRP contusion circuitry: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.', 'Module 4B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Second abstract-level experiment row isolates the primary mechanistic endpoint for NSC NO hydrogel: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.', 'Module 4B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Second abstract-level experiment row isolates the primary mechanistic endpoint for NSC exosome microfiber: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.', 'Module 4B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Second abstract-level experiment row isolates the primary mechanistic endpoint for NSC hydrogel microenvironment: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.', 'Module 4B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Second abstract-level experiment row isolates the primary mechanistic endpoint for NSC manufacturing: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.', 'Module 4B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Second abstract-level experiment row isolates the primary mechanistic endpoint for OEC immunomodulation: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.', 'Module 4B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Second abstract-level experiment row isolates the primary mechanistic endpoint for OEC inflammation: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.', 'Module 4B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Second abstract-level experiment row isolates the primary mechanistic endpoint for OPC remyelination: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.', 'Module 4B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Second abstract-level experiment row isolates the primary mechanistic endpoint for Schwann GDNF pathway: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.', 'Module 4B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Second abstract-level experiment row isolates the primary mechanistic endpoint for Schwann chABC: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.', 'Module 4B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Second abstract-level experiment row isolates the primary mechanistic endpoint for chronic MSC graft permissiveness: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.', 'Module 4B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Second abstract-level experiment row isolates the primary mechanistic endpoint for chronic iPSC-NS/PC scaffold histology: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.', 'Module 4B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Second abstract-level experiment row isolates the primary mechanistic endpoint for clinical MSC pilot: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.', 'Module 4B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Second abstract-level experiment row isolates the primary mechanistic endpoint for clinical MSC safety: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.', 'Module 4B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Second abstract-level experiment row isolates the primary mechanistic endpoint for clinical NSC safety: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.', 'Module 4B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Second abstract-level experiment row isolates the primary mechanistic endpoint for clinical OEC MSC safety: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.', 'Module 4B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Second abstract-level experiment row isolates the primary mechanistic endpoint for clinical Schwann safety: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.', 'Module 4B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Second abstract-level experiment row isolates the primary mechanistic endpoint for engineered MSC scaffold: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.', 'Module 4B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Second abstract-level experiment row isolates the primary mechanistic endpoint for iPSC A2B5 progenitors: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.', 'Module 4B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Second abstract-level experiment row isolates the primary mechanistic endpoint for iPSC HGF pretreatment: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.', 'Module 4B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Second abstract-level experiment row isolates the primary mechanistic endpoint for iPSC rehabilitation combination: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.', 'Module 4B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Second abstract-level experiment row isolates the primary mechanistic endpoint for iPSC spinal progenitors: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.', 'Module 4B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Second abstract-level experiment row isolates the primary mechanistic endpoint for iPSC synaptic organizer: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.', 'Module 4B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Second abstract-level experiment row isolates the primary mechanistic endpoint for olfactory mucosal MSC scaffold: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.', 'Module 4B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Second abstract-level experiment row isolates the primary mechanistic endpoint for oligodendrogenic progenitors: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.', 'Module 4B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Second abstract-level experiment row isolates the primary mechanistic endpoint for organoid graft: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.', 'Module 4B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Second abstract-level experiment row isolates the primary mechanistic endpoint for primate ESC-NSPC safety: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.', 'Module 4B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Second abstract-level experiment row isolates the primary mechanistic endpoint for primate NSC function: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.', 'Module 4B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Second abstract-level experiment row isolates the primary mechanistic endpoint for synaptic integration: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.', 'Module 4B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Second abstract-level experiment row isolates the primary mechanistic endpoint for synaptic relay: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.', 'Module 4B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Synaptic integration / host-graft connectivity', 'Module 4B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Lu P 2007 combined MSC graft with scaffold, scar, hydrogel, exosome, or microenvironmental features, making attribution to the cell product alone limited.',
    'qualitative',
    'Lu P 2007 combined MSC graft with scaffold, scar, hydrogel, exosome, or microenvironmental features, making attribution to the cell product alone limited.',
    'lu p 2007 combined msc graft with scaffold, scar, hydrogel, exosome, or microenvironmental features, making attribution to the cell product alone limited.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'low',
    '{"curator_notes": "Primary title: Axon regeneration through scars and into sites of chronic spinal cord injury. Note: Chronic scar/graft permissiveness anchor.", "experiment_tracker_id": "M4A-P001-E001", "paper_tracker_id": "M4A-P001", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T006", "tracker_id": "M4B-O001"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P001::M4A-P001-E001'
    AND et.evidence_type_name = 'Combination scaffold-cell intervention'
    AND ot.outcome_type_name = 'Delivery / microenvironment / regeneration'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O001', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Xiao Z 2016 tested BMMC + NeuroRegen scaffold in Human, providing a clinical feasibility or safety anchor for cell transplantation after SCI.',
    'qualitative',
    'Xiao Z 2016 tested BMMC + NeuroRegen scaffold in Human, providing a clinical feasibility or safety anchor for cell transplantation after SCI.',
    'xiao z 2016 tested bmmc + neuroregen scaffold in human, providing a clinical feasibility or safety anchor for cell transplantation after sci.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'low',
    '{"curator_notes": "Primary title: One-year clinical study of NeuroRegen scaffold implantation following scar resection in complete chronic spinal cord injury patients. Note: Human scaffold-cell anchor.", "experiment_tracker_id": "M4A-P002-E001", "paper_tracker_id": "M4A-P002", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T001", "tracker_id": "M4B-O002"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P002::M4A-P002-E001'
    AND et.evidence_type_name = 'Clinical intervention'
    AND ot.outcome_type_name = 'Safety / feasibility / clinical outcome'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O002', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Ito K 2024 combined hNS/PC + dECM scaffold with scaffold, scar, hydrogel, exosome, or microenvironmental features, making attribution to the cell product alone limited.',
    'qualitative',
    'Ito K 2024 combined hNS/PC + dECM scaffold with scaffold, scar, hydrogel, exosome, or microenvironmental features, making attribution to the cell product alone limited.',
    'ito k 2024 combined hns/pc + decm scaffold with scaffold, scar, hydrogel, exosome, or microenvironmental features, making attribution to the cell product alone limited.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'low',
    '{"curator_notes": "Primary title: Histological effects of combined therapy involving scar resection, decellularized scaffolds, and human iPSC-NS/PCs transplantation in chronic complete spinal cord injury.. Note: Chronic complete SCI hNS/PC scaffold anchor.", "experiment_tracker_id": "M4A-P003-E001", "paper_tracker_id": "M4A-P003", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T006", "tracker_id": "M4B-O003"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P003::M4A-P003-E001'
    AND et.evidence_type_name = 'Combination scaffold-cell intervention'
    AND ot.outcome_type_name = 'Delivery / microenvironment / regeneration'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O003', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Abraham ME 2026 tested NSI-566 human spinal cord-derived neural stem cells in Human chronic cervical SCI, providing a clinical feasibility or safety anchor for cell transplantation after SCI.',
    'qualitative',
    'Abraham ME 2026 tested NSI-566 human spinal cord-derived neural stem cells in Human chronic cervical SCI, providing a clinical feasibility or safety anchor for cell transplantation after SCI.',
    'abraham me 2026 tested nsi-566 human spinal cord-derived neural stem cells in human chronic cervical sci, providing a clinical feasibility or safety anchor for cell transplantation after sci.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'medium',
    '{"curator_notes": "Primary title: Long-term safety and clinical outcomes from a single-site phase 1 study of neural stem cell transplantation for chronic cervical spinal cord injury.. Note: Long-term cervical phase I safety/outcomes.", "experiment_tracker_id": "M4A-P004-E001", "paper_tracker_id": "M4A-P004", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T001", "tracker_id": "M4B-O004"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P004::M4A-P004-E001'
    AND et.evidence_type_name = 'Clinical intervention'
    AND ot.outcome_type_name = 'Safety / feasibility / clinical outcome'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O004', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Martin JR 2024 tested NSI-566 human spinal cord-derived neural stem cells in Human chronic thoracic SCI, providing a clinical feasibility or safety anchor for cell transplantation after SCI.',
    'qualitative',
    'Martin JR 2024 tested NSI-566 human spinal cord-derived neural stem cells in Human chronic thoracic SCI, providing a clinical feasibility or safety anchor for cell transplantation after SCI.',
    'martin jr 2024 tested nsi-566 human spinal cord-derived neural stem cells in human chronic thoracic sci, providing a clinical feasibility or safety anchor for cell transplantation after sci.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'medium',
    '{"curator_notes": "Primary title: Long-term clinical and safety outcomes from a single-site phase 1 study of neural stem cell transplantation for chronic thoracic spinal cord injury.. Note: Long-term thoracic phase I safety/outcomes.", "experiment_tracker_id": "M4A-P005-E001", "paper_tracker_id": "M4A-P005", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T001", "tracker_id": "M4B-O005"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P005::M4A-P005-E001'
    AND et.evidence_type_name = 'Clinical intervention'
    AND ot.outcome_type_name = 'Safety / feasibility / clinical outcome'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O005', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Gant KL 2022 tested Autologous Schwann cells in Human chronic SCI, providing a clinical feasibility or safety anchor for cell transplantation after SCI.',
    'qualitative',
    'Gant KL 2022 tested Autologous Schwann cells in Human chronic SCI, providing a clinical feasibility or safety anchor for cell transplantation after SCI.',
    'gant kl 2022 tested autologous schwann cells in human chronic sci, providing a clinical feasibility or safety anchor for cell transplantation after sci.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'medium',
    '{"curator_notes": "Primary title: Phase 1 Safety Trial of Autologous Human Schwann Cell Transplantation in Chronic Spinal Cord Injury.. Note: Phase I Schwann-cell safety anchor.", "experiment_tracker_id": "M4A-P006-E001", "paper_tracker_id": "M4A-P006", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T001", "tracker_id": "M4B-O006"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P006::M4A-P006-E001'
    AND et.evidence_type_name = 'Clinical intervention'
    AND ot.outcome_type_name = 'Safety / feasibility / clinical outcome'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O006', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Kaplan N 2025 tested Wharton jelly MSCs in Human chronic complete SCI, providing a clinical feasibility or safety anchor for cell transplantation after SCI.',
    'qualitative',
    'Kaplan N 2025 tested Wharton jelly MSCs in Human chronic complete SCI, providing a clinical feasibility or safety anchor for cell transplantation after SCI.',
    'kaplan n 2025 tested wharton jelly mscs in human chronic complete sci, providing a clinical feasibility or safety anchor for cell transplantation after sci.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'low',
    '{"curator_notes": "Primary title: Multiroute administration of Wharton''s jelly mesenchymal stem cells in chronic complete spinal cord injury: A phase I safety and feasibility study.. Note: Multiroute MSC phase I feasibility.", "experiment_tracker_id": "M4A-P007-E001", "paper_tracker_id": "M4A-P007", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T001", "tracker_id": "M4B-O007"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P007::M4A-P007-E001'
    AND et.evidence_type_name = 'Clinical intervention'
    AND ot.outcome_type_name = 'Safety / feasibility / clinical outcome'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O007', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Macedo CT 2024 tested Autologous mesenchymal stromal cells in Human complete cervical SCI, providing a clinical feasibility or safety anchor for cell transplantation after SCI.',
    'qualitative',
    'Macedo CT 2024 tested Autologous mesenchymal stromal cells in Human complete cervical SCI, providing a clinical feasibility or safety anchor for cell transplantation after SCI.',
    'macedo ct 2024 tested autologous mesenchymal stromal cells in human complete cervical sci, providing a clinical feasibility or safety anchor for cell transplantation after sci.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'low',
    '{"curator_notes": "Primary title: Transplantation of autologous mesenchymal stromal cells in complete cervical spinal cord injury: a pilot study.. Note: Pilot autologous MSC study.", "experiment_tracker_id": "M4A-P008-E001", "paper_tracker_id": "M4A-P008", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T001", "tracker_id": "M4B-O008"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P008::M4A-P008-E001'
    AND et.evidence_type_name = 'Clinical intervention'
    AND ot.outcome_type_name = 'Safety / feasibility / clinical outcome'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O008', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Zamani H 2022 tested Autologous OEC + BM-MSC in Human chronic SCI, providing a clinical feasibility or safety anchor for cell transplantation after SCI.',
    'qualitative',
    'Zamani H 2022 tested Autologous OEC + BM-MSC in Human chronic SCI, providing a clinical feasibility or safety anchor for cell transplantation after SCI.',
    'zamani h 2022 tested autologous oec + bm-msc in human chronic sci, providing a clinical feasibility or safety anchor for cell transplantation after sci.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'medium',
    '{"curator_notes": "Primary title: Safety and feasibility of autologous olfactory ensheathing cell and bone marrow mesenchymal stem cell co-transplantation in chronic human spinal cord injury: a clinical trial.. Note: OEC/BM-MSC co-transplant feasibility.", "experiment_tracker_id": "M4A-P009-E001", "paper_tracker_id": "M4A-P009", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T001", "tracker_id": "M4B-O009"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P009::M4A-P009-E001'
    AND et.evidence_type_name = 'Clinical intervention'
    AND ot.outcome_type_name = 'Safety / feasibility / clinical outcome'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O009', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Chen W 2020 tested BMMC + NeuroRegen scaffold in Human acute complete SCI, providing a clinical feasibility or safety anchor for cell transplantation after SCI.',
    'qualitative',
    'Chen W 2020 tested BMMC + NeuroRegen scaffold in Human acute complete SCI, providing a clinical feasibility or safety anchor for cell transplantation after SCI.',
    'chen w 2020 tested bmmc + neuroregen scaffold in human acute complete sci, providing a clinical feasibility or safety anchor for cell transplantation after sci.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'medium',
    '{"curator_notes": "Primary title: NeuroRegen Scaffolds Combined with Autologous Bone Marrow Mononuclear Cells for the Repair of Acute Complete Spinal Cord Injury: A 3-Year Clinical Study.. Note: Acute complete scaffold/BMMC clinical anchor.", "experiment_tracker_id": "M4A-P010-E001", "paper_tracker_id": "M4A-P010", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T001", "tracker_id": "M4B-O010"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P010::M4A-P010-E001'
    AND et.evidence_type_name = 'Clinical intervention'
    AND ot.outcome_type_name = 'Safety / feasibility / clinical outcome'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O010', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Sinopoulou E 2025 evaluated Human ESC-derived spinal cord NSCs in Non-human primate, supporting the neural-graft evidence stream for integration, differentiation, or functional recovery after SCI.',
    'qualitative',
    'Sinopoulou E 2025 evaluated Human ESC-derived spinal cord NSCs in Non-human primate, supporting the neural-graft evidence stream for integration, differentiation, or functional recovery after SCI.',
    'sinopoulou e 2025 evaluated human esc-derived spinal cord nscs in non-human primate, supporting the neural-graft evidence stream for integration, differentiation, or functional recovery after sci.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'medium',
    '{"curator_notes": "Primary title: Extensive restoration of forelimb function in primates with spinal cord injury by neural stem cell transplantation.. Note: Primate skilled forelimb recovery anchor.", "experiment_tracker_id": "M4A-P011-E001", "paper_tracker_id": "M4A-P011", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T002", "tracker_id": "M4B-O011"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P011::M4A-P011-E001'
    AND et.evidence_type_name = 'Neural graft intervention'
    AND ot.outcome_type_name = 'Differentiation / synaptic integration / recovery'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O011', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Iwai H 2015 evaluated ESC-derived NS/PCs in Common marmoset, supporting the neural-graft evidence stream for integration, differentiation, or functional recovery after SCI.',
    'qualitative',
    'Iwai H 2015 evaluated ESC-derived NS/PCs in Common marmoset, supporting the neural-graft evidence stream for integration, differentiation, or functional recovery after SCI.',
    'iwai h 2015 evaluated esc-derived ns/pcs in common marmoset, supporting the neural-graft evidence stream for integration, differentiation, or functional recovery after sci.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'medium',
    '{"curator_notes": "Primary title: Allogeneic Neural Stem/Progenitor Cells Derived From Embryonic Stem Cells Promote Functional Recovery After Transplantation Into Injured Spinal Cord of Nonhuman Primates.. Note: Non-human primate safety/efficacy bridge.", "experiment_tracker_id": "M4A-P012-E001", "paper_tracker_id": "M4A-P012", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T002", "tracker_id": "M4B-O012"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P012::M4A-P012-E001'
    AND et.evidence_type_name = 'Neural graft intervention'
    AND ot.outcome_type_name = 'Differentiation / synaptic integration / recovery'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O012', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Tucker A 2025 is a core synaptic-connectivity anchor showing that neural grafts can be interrogated for host-graft network integration after SCI.',
    'qualitative',
    'Tucker A 2025 is a core synaptic-connectivity anchor showing that neural grafts can be interrogated for host-graft network integration after SCI.',
    'tucker a 2025 is a core synaptic-connectivity anchor showing that neural grafts can be interrogated for host-graft network integration after sci.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'medium',
    '{"curator_notes": "Primary title: Functional synaptic connectivity of engrafted spinal cord neurons with hindlimb motor circuitry in the injured spinal cord.. Note: Functional synaptic connectivity with hindlimb circuitry.", "experiment_tracker_id": "M4A-P013-E001", "paper_tracker_id": "M4A-P013", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T002", "tracker_id": "M4B-O013"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P013::M4A-P013-E001'
    AND et.evidence_type_name = 'Neural graft intervention'
    AND ot.outcome_type_name = 'Synaptic integration / host-graft connectivity'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O013', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Ceto S 2020 is a core synaptic-connectivity anchor showing that neural grafts can be interrogated for host-graft network integration after SCI.',
    'qualitative',
    'Ceto S 2020 is a core synaptic-connectivity anchor showing that neural grafts can be interrogated for host-graft network integration after SCI.',
    'ceto s 2020 is a core synaptic-connectivity anchor showing that neural grafts can be interrogated for host-graft network integration after sci.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'medium',
    '{"curator_notes": "Primary title: Neural Stem Cell Grafts Form Extensive Synaptic Networks that Integrate with Host Circuits after Spinal Cord Injury.. Note: In vivo graft network integration anchor.", "experiment_tracker_id": "M4A-P014-E001", "paper_tracker_id": "M4A-P014", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T002", "tracker_id": "M4B-O014"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P014::M4A-P014-E001'
    AND et.evidence_type_name = 'Neural graft intervention'
    AND ot.outcome_type_name = 'Synaptic integration / host-graft connectivity'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O014', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Adler AF 2017 is a core synaptic-connectivity anchor showing that neural grafts can be interrogated for host-graft network integration after SCI.',
    'qualitative',
    'Adler AF 2017 is a core synaptic-connectivity anchor showing that neural grafts can be interrogated for host-graft network integration after SCI.',
    'adler af 2017 is a core synaptic-connectivity anchor showing that neural grafts can be interrogated for host-graft network integration after sci.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'medium',
    '{"curator_notes": "Primary title: Comprehensive Monosynaptic Rabies Virus Mapping of Host Connectivity with Neural Progenitor Grafts after Spinal Cord Injury.. Note: Host connectivity mapping anchor.", "experiment_tracker_id": "M4A-P015-E001", "paper_tracker_id": "M4A-P015", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T002", "tracker_id": "M4B-O015"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P015::M4A-P015-E001'
    AND et.evidence_type_name = 'Neural graft intervention'
    AND ot.outcome_type_name = 'Synaptic integration / host-graft connectivity'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O015', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Bonner JF 2011 is a core synaptic-connectivity anchor showing that neural grafts can be interrogated for host-graft network integration after SCI.',
    'qualitative',
    'Bonner JF 2011 is a core synaptic-connectivity anchor showing that neural grafts can be interrogated for host-graft network integration after SCI.',
    'bonner jf 2011 is a core synaptic-connectivity anchor showing that neural grafts can be interrogated for host-graft network integration after sci.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'medium',
    '{"curator_notes": "Primary title: Grafted neural progenitors integrate and restore synaptic connectivity across the injured spinal cord.. Note: Relay connectivity across injured cord.", "experiment_tracker_id": "M4A-P016-E001", "paper_tracker_id": "M4A-P016", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T002", "tracker_id": "M4B-O016"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P016::M4A-P016-E001'
    AND et.evidence_type_name = 'Neural graft intervention'
    AND ot.outcome_type_name = 'Synaptic integration / host-graft connectivity'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O016', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Zholudeva LV 2024 is a core synaptic-connectivity anchor showing that neural grafts can be interrogated for host-graft network integration after SCI.',
    'qualitative',
    'Zholudeva LV 2024 is a core synaptic-connectivity anchor showing that neural grafts can be interrogated for host-graft network integration after SCI.',
    'zholudeva lv 2024 is a core synaptic-connectivity anchor showing that neural grafts can be interrogated for host-graft network integration after sci.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'medium',
    '{"curator_notes": "Primary title: Human spinal interneurons repair the injured spinal cord through synaptic integration.. Note: Human interneuron synaptic integration anchor.", "experiment_tracker_id": "M4A-P017-E001", "paper_tracker_id": "M4A-P017", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T002", "tracker_id": "M4B-O017"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P017::M4A-P017-E001'
    AND et.evidence_type_name = 'Neural graft intervention'
    AND ot.outcome_type_name = 'Synaptic integration / host-graft connectivity'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O017', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Zhu Y 2025 evaluated Engineered thoracic spinal cord organoids in Organoid / rodent SCI, supporting the neural-graft evidence stream for integration, differentiation, or functional recovery after SCI.',
    'qualitative',
    'Zhu Y 2025 evaluated Engineered thoracic spinal cord organoids in Organoid / rodent SCI, supporting the neural-graft evidence stream for integration, differentiation, or functional recovery after SCI.',
    'zhu y 2025 evaluated engineered thoracic spinal cord organoids in organoid / rodent sci, supporting the neural-graft evidence stream for integration, differentiation, or functional recovery after sci.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'low',
    '{"curator_notes": "Primary title: Engineered thoracic spinal cord organoids for transplantation after spinal cord injury.. Note: Tissueoid/organoid transplantation anchor.", "experiment_tracker_id": "M4A-P018-E001", "paper_tracker_id": "M4A-P018", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T002", "tracker_id": "M4B-O018"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P018::M4A-P018-E001'
    AND et.evidence_type_name = 'Neural graft intervention'
    AND ot.outcome_type_name = 'Differentiation / synaptic integration / recovery'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O018', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Yao X 2025 evaluated Human iPSC-derived spinal neural progenitors in NOD-SCID mouse contusion, supporting the neural-graft evidence stream for integration, differentiation, or functional recovery after SCI.',
    'qualitative',
    'Yao X 2025 evaluated Human iPSC-derived spinal neural progenitors in NOD-SCID mouse contusion, supporting the neural-graft evidence stream for integration, differentiation, or functional recovery after SCI.',
    'yao x 2025 evaluated human ipsc-derived spinal neural progenitors in nod-scid mouse contusion, supporting the neural-graft evidence stream for integration, differentiation, or functional recovery after sci.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'low',
    '{"curator_notes": "Primary title: Human iPSC-derived spinal neural progenitors enhance sensorimotor recovery in spinal cord-injured NOD-SCID mice via differentiation and microenvironment regulation.. Note: iPSC spinal progenitor differentiation and microenvironment regulation.", "experiment_tracker_id": "M4A-P019-E001", "paper_tracker_id": "M4A-P019", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T002", "tracker_id": "M4B-O019"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P019::M4A-P019-E001'
    AND et.evidence_type_name = 'Neural graft intervention'
    AND ot.outcome_type_name = 'Differentiation / synaptic integration / recovery'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O019', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Zheng Y 2025 evaluated Human iPSC-derived A2B5+ neural progenitors in Mouse SCI, supporting the neural-graft evidence stream for integration, differentiation, or functional recovery after SCI.',
    'qualitative',
    'Zheng Y 2025 evaluated Human iPSC-derived A2B5+ neural progenitors in Mouse SCI, supporting the neural-graft evidence stream for integration, differentiation, or functional recovery after SCI.',
    'zheng y 2025 evaluated human ipsc-derived a2b5+ neural progenitors in mouse sci, supporting the neural-graft evidence stream for integration, differentiation, or functional recovery after sci.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'low',
    '{"curator_notes": "Primary title: Functional Recovery by Transplantation of Human iPSC-Derived A2B5 Positive Neural Progenitor Cell After Spinal Cord Injury in Mice.. Note: A2B5+ iPSC progenitor functional recovery anchor.", "experiment_tracker_id": "M4A-P020-E001", "paper_tracker_id": "M4A-P020", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T002", "tracker_id": "M4B-O020"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P020::M4A-P020-E001'
    AND et.evidence_type_name = 'Neural graft intervention'
    AND ot.outcome_type_name = 'Differentiation / synaptic integration / recovery'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O020', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Shibata T 2023 links neural graft effects to rehabilitation, synaptic organizer, trophic pretreatment, or axon-guidance enhancement rather than grafting alone.',
    'qualitative',
    'Shibata T 2023 links neural graft effects to rehabilitation, synaptic organizer, trophic pretreatment, or axon-guidance enhancement rather than grafting alone.',
    'shibata t 2023 links neural graft effects to rehabilitation, synaptic organizer, trophic pretreatment, or axon-guidance enhancement rather than grafting alone.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'medium',
    '{"curator_notes": "Primary title: Rehabilitative Training Enhances Therapeutic Effect of Human-iPSC-Derived Neural Stem/Progenitor Cells Transplantation in Chronic Spinal Cord Injury.. Note: Rehabilitation as graft-effect amplifier.", "experiment_tracker_id": "M4A-P021-E001", "paper_tracker_id": "M4A-P021", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T002", "tracker_id": "M4B-O021"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P021::M4A-P021-E001'
    AND et.evidence_type_name = 'Neural graft intervention'
    AND ot.outcome_type_name = 'Combination-enhanced neural graft function'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O021', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Saijo Y 2024 links neural graft effects to rehabilitation, synaptic organizer, trophic pretreatment, or axon-guidance enhancement rather than grafting alone.',
    'qualitative',
    'Saijo Y 2024 links neural graft effects to rehabilitation, synaptic organizer, trophic pretreatment, or axon-guidance enhancement rather than grafting alone.',
    'saijo y 2024 links neural graft effects to rehabilitation, synaptic organizer, trophic pretreatment, or axon-guidance enhancement rather than grafting alone.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'medium',
    '{"curator_notes": "Primary title: Human-induced pluripotent stem cell-derived neural stem/progenitor cell ex vivo gene therapy with synaptic organizer CPTX for spinal cord injury.. Note: Ex vivo gene therapy to enhance synapse formation.", "experiment_tracker_id": "M4A-P022-E001", "paper_tracker_id": "M4A-P022", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T002", "tracker_id": "M4B-O022"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P022::M4A-P022-E001'
    AND et.evidence_type_name = 'Neural graft intervention'
    AND ot.outcome_type_name = 'Combination-enhanced neural graft function'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O022', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Suematsu Y 2023 links neural graft effects to rehabilitation, synaptic organizer, trophic pretreatment, or axon-guidance enhancement rather than grafting alone.',
    'qualitative',
    'Suematsu Y 2023 links neural graft effects to rehabilitation, synaptic organizer, trophic pretreatment, or axon-guidance enhancement rather than grafting alone.',
    'suematsu y 2023 links neural graft effects to rehabilitation, synaptic organizer, trophic pretreatment, or axon-guidance enhancement rather than grafting alone.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'low',
    '{"curator_notes": "Primary title: Hepatocyte growth factor pretreatment boosts functional recovery after spinal cord injury through human iPSC-derived neural stem/progenitor cell transplantation.. Note: Microenvironment/growth-factor pretreatment combination.", "experiment_tracker_id": "M4A-P023-E001", "paper_tracker_id": "M4A-P023", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T002", "tracker_id": "M4B-O023"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P023::M4A-P023-E001'
    AND et.evidence_type_name = 'Neural graft intervention'
    AND ot.outcome_type_name = 'Combination-enhanced neural graft function'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O023', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Xu B 2023 evaluated NS/PCs from fetal brain, spinal cord, and ESC sources in Rat severe SCI, supporting the neural-graft evidence stream for integration, differentiation, or functional recovery after SCI.',
    'qualitative',
    'Xu B 2023 evaluated NS/PCs from fetal brain, spinal cord, and ESC sources in Rat severe SCI, supporting the neural-graft evidence stream for integration, differentiation, or functional recovery after SCI.',
    'xu b 2023 evaluated ns/pcs from fetal brain, spinal cord, and esc sources in rat severe sci, supporting the neural-graft evidence stream for integration, differentiation, or functional recovery after sci.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'low',
    '{"curator_notes": "Primary title: Transplantation of neural stem progenitor cells from different sources for severe spinal cord injury repair in rat.. Note: Cell-source comparison anchor.", "experiment_tracker_id": "M4A-P024-E001", "paper_tracker_id": "M4A-P024", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T002", "tracker_id": "M4B-O024"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P024::M4A-P024-E001'
    AND et.evidence_type_name = 'Neural graft intervention'
    AND ot.outcome_type_name = 'Differentiation / synaptic integration / recovery'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O024', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Li Y 2023 links neural graft effects to rehabilitation, synaptic organizer, trophic pretreatment, or axon-guidance enhancement rather than grafting alone.',
    'qualitative',
    'Li Y 2023 links neural graft effects to rehabilitation, synaptic organizer, trophic pretreatment, or axon-guidance enhancement rather than grafting alone.',
    'li y 2023 links neural graft effects to rehabilitation, synaptic organizer, trophic pretreatment, or axon-guidance enhancement rather than grafting alone.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'medium',
    '{"curator_notes": "Primary title: BDNF guides neural stem cell-derived axons to ventral interneurons and motor neurons after spinal cord injury.. Note: Host target guidance of graft-derived axons.", "experiment_tracker_id": "M4A-P025-E001", "paper_tracker_id": "M4A-P025", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T002", "tracker_id": "M4B-O025"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P025::M4A-P025-E001'
    AND et.evidence_type_name = 'Neural graft intervention'
    AND ot.outcome_type_name = 'Combination-enhanced neural graft function'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O025', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Li M 2024 evaluated iPSC/ESC-derived pyramidal neuronal precursors in Rat contusion SCI, supporting the neural-graft evidence stream for integration, differentiation, or functional recovery after SCI.',
    'qualitative',
    'Li M 2024 evaluated iPSC/ESC-derived pyramidal neuronal precursors in Rat contusion SCI, supporting the neural-graft evidence stream for integration, differentiation, or functional recovery after SCI.',
    'li m 2024 evaluated ipsc/esc-derived pyramidal neuronal precursors in rat contusion sci, supporting the neural-graft evidence stream for integration, differentiation, or functional recovery after sci.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'low',
    '{"curator_notes": "Primary title: Human induced pluripotent stem cell/embryonic stem cell-derived pyramidal neuronal precursors show safety and efficacy in a rat spinal cord injury model.. Note: Pyramidal neuronal precursor safety/efficacy.", "experiment_tracker_id": "M4A-P026-E001", "paper_tracker_id": "M4A-P026", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T002", "tracker_id": "M4B-O026"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P026::M4A-P026-E001'
    AND et.evidence_type_name = 'Neural graft intervention'
    AND ot.outcome_type_name = 'Differentiation / synaptic integration / recovery'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O026', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Manley NC 2017 anchors OPC or oligodendrogenic transplantation evidence where remyelination and safety are distinct from neuronal relay claims.',
    'qualitative',
    'Manley NC 2017 anchors OPC or oligodendrogenic transplantation evidence where remyelination and safety are distinct from neuronal relay claims.',
    'manley nc 2017 anchors opc or oligodendrogenic transplantation evidence where remyelination and safety are distinct from neuronal relay claims.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'medium',
    '{"curator_notes": "Primary title: Human Embryonic Stem Cell-Derived Oligodendrocyte Progenitor Cells: Preclinical Efficacy and Safety in Cervical Spinal Cord Injury.. Note: OPC preclinical efficacy and safety anchor.", "experiment_tracker_id": "M4A-P027-E001", "paper_tracker_id": "M4A-P027", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T004", "tracker_id": "M4B-O027"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P027::M4A-P027-E001'
    AND et.evidence_type_name = 'Glial-lineage intervention'
    AND ot.outcome_type_name = 'OPC / oligodendrogenic safety and repair'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O027', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Luo Z 2025 anchors OPC or oligodendrogenic transplantation evidence where remyelination and safety are distinct from neuronal relay claims.',
    'qualitative',
    'Luo Z 2025 anchors OPC or oligodendrogenic transplantation evidence where remyelination and safety are distinct from neuronal relay claims.',
    'luo z 2025 anchors opc or oligodendrogenic transplantation evidence where remyelination and safety are distinct from neuronal relay claims.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'low',
    '{"curator_notes": "Primary title: Oligodendrogenic neural progenitors for treatment of chronic compressive cervical spinal cord injury.. Note: Chronic compressive cervical progenitor anchor.", "experiment_tracker_id": "M4A-P028-E001", "paper_tracker_id": "M4A-P028", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T004", "tracker_id": "M4B-O028"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P028::M4A-P028-E001'
    AND et.evidence_type_name = 'Glial-lineage intervention'
    AND ot.outcome_type_name = 'OPC / oligodendrogenic safety and repair'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O028', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Hejrati N 2025 evaluated DLK1-expressing neural progenitor cells in Cervical SCI, supporting the neural-graft evidence stream for integration, differentiation, or functional recovery after SCI.',
    'qualitative',
    'Hejrati N 2025 evaluated DLK1-expressing neural progenitor cells in Cervical SCI, supporting the neural-graft evidence stream for integration, differentiation, or functional recovery after SCI.',
    'hejrati n 2025 evaluated dlk1-expressing neural progenitor cells in cervical sci, supporting the neural-graft evidence stream for integration, differentiation, or functional recovery after sci.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'low',
    '{"curator_notes": "Primary title: DLK1-expressing neural progenitor cells promote tissue repair and functional recovery after cervical spinal cord injury.. Note: Neural progenitor subtype/tissue repair anchor.", "experiment_tracker_id": "M4A-P029-E001", "paper_tracker_id": "M4A-P029", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T002", "tracker_id": "M4B-O029"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P029::M4A-P029-E001'
    AND et.evidence_type_name = 'Neural graft intervention'
    AND ot.outcome_type_name = 'Differentiation / synaptic integration / recovery'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O029', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Ren J 2026 evaluated Cryopreserved neural stem cells in SCI repair platform, supporting the neural-graft evidence stream for integration, differentiation, or functional recovery after SCI.',
    'qualitative',
    'Ren J 2026 evaluated Cryopreserved neural stem cells in SCI repair platform, supporting the neural-graft evidence stream for integration, differentiation, or functional recovery after SCI.',
    'ren j 2026 evaluated cryopreserved neural stem cells in sci repair platform, supporting the neural-graft evidence stream for integration, differentiation, or functional recovery after sci.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'low',
    '{"curator_notes": "Primary title: Integrated cryopreservation-thawing-transplantation platform for neural stem cell-based spinal cord injury repair.. Note: Cryopreservation-thaw-transplant platform.", "experiment_tracker_id": "M4A-P030-E001", "paper_tracker_id": "M4A-P030", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T002", "tracker_id": "M4B-O030"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P030::M4A-P030-E001'
    AND et.evidence_type_name = 'Neural graft intervention'
    AND ot.outcome_type_name = 'Differentiation / synaptic integration / recovery'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O030', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Qu W 2025 anchors Schwann or glial-support transplantation evidence for axon growth, connectivity, remyelination, or safety.',
    'qualitative',
    'Qu W 2025 anchors Schwann or glial-support transplantation evidence for axon growth, connectivity, remyelination, or safety.',
    'qu w 2025 anchors schwann or glial-support transplantation evidence for axon growth, connectivity, remyelination, or safety.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'medium',
    '{"curator_notes": "Primary title: Chondroitinase ABC combined with Schwann cell transplantation enhances restoration of neural connection and functional recovery following acute and chronic spinal cord injury.. Note: Schwann/chABC acute and chronic connectivity anchor.", "experiment_tracker_id": "M4A-P031-E001", "paper_tracker_id": "M4A-P031", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T004", "tracker_id": "M4B-O031"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P031::M4A-P031-E001'
    AND et.evidence_type_name = 'Glial-lineage intervention'
    AND ot.outcome_type_name = 'Schwann / glial support'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O031', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Du X 2024 anchors Schwann or glial-support transplantation evidence for axon growth, connectivity, remyelination, or safety.',
    'qualitative',
    'Du X 2024 anchors Schwann or glial-support transplantation evidence for axon growth, connectivity, remyelination, or safety.',
    'du x 2024 anchors schwann or glial-support transplantation evidence for axon growth, connectivity, remyelination, or safety.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'low',
    '{"curator_notes": "Primary title: Regeneration of Propriospinal Axons in Rat Transected Spinal Cord Injury through a Growth-Promoting Pathway Constructed by Schwann Cells Overexpressing GDNF.. Note: Propriospinal axon pathway construction.", "experiment_tracker_id": "M4A-P032-E001", "paper_tracker_id": "M4A-P032", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T004", "tracker_id": "M4B-O032"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P032::M4A-P032-E001'
    AND et.evidence_type_name = 'Glial-lineage intervention'
    AND ot.outcome_type_name = 'Schwann / glial support'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O032', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Hu JG 2013 anchors Schwann or glial-support transplantation evidence for axon growth, connectivity, remyelination, or safety.',
    'qualitative',
    'Hu JG 2013 anchors Schwann or glial-support transplantation evidence for axon growth, connectivity, remyelination, or safety.',
    'hu jg 2013 anchors schwann or glial-support transplantation evidence for axon growth, connectivity, remyelination, or safety.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'low',
    '{"curator_notes": "Primary title: Cotransplantation of glial restricted precursor cells and Schwann cells promotes functional recovery after spinal cord injury.. Note: GRP/Schwann cotransplant functional recovery.", "experiment_tracker_id": "M4A-P033-E001", "paper_tracker_id": "M4A-P033", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T004", "tracker_id": "M4B-O033"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P033::M4A-P033-E001'
    AND et.evidence_type_name = 'Glial-lineage intervention'
    AND ot.outcome_type_name = 'Schwann / glial support'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O033', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Dugan EA 2015 tested Neural + glial restricted precursors + quipazine in Rat SCI, contributing glial-lineage evidence for remyelination, axon support, circuitry, or functional recovery.',
    'qualitative',
    'Dugan EA 2015 tested Neural + glial restricted precursors + quipazine in Rat SCI, contributing glial-lineage evidence for remyelination, axon support, circuitry, or functional recovery.',
    'dugan ea 2015 tested neural + glial restricted precursors + quipazine in rat sci, contributing glial-lineage evidence for remyelination, axon support, circuitry, or functional recovery.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'low',
    '{"curator_notes": "Primary title: A combination therapy of neural and glial restricted precursor cells and chronic quipazine treatment paired with passive cycling promotes quipazine-induced stepping in adult spinalized rats.. Note: Cell transplant plus serotonergic pharmacology/rehab-like combination.", "experiment_tracker_id": "M4A-P034-E001", "paper_tracker_id": "M4A-P034", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T004", "tracker_id": "M4B-O034"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P034::M4A-P034-E001'
    AND et.evidence_type_name = 'Glial-lineage intervention'
    AND ot.outcome_type_name = 'Remyelination / axon support / autonomic or motor outcome'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O034', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Mitsui T 2005 shows that transplantation outcomes include autonomic, bladder, pain, respiratory, or cardiovascular readouts that should not be collapsed into locomotor recovery.',
    'qualitative',
    'Mitsui T 2005 shows that transplantation outcomes include autonomic, bladder, pain, respiratory, or cardiovascular readouts that should not be collapsed into locomotor recovery.',
    'mitsui t 2005 shows that transplantation outcomes include autonomic, bladder, pain, respiratory, or cardiovascular readouts that should not be collapsed into locomotor recovery.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'medium',
    '{"curator_notes": "Primary title: Transplantation of neuronal and glial restricted precursors into contused spinal cord improves bladder and motor functions, decreases thermal hypersensitivity, and modifies intraspinal circuitry.. Note: Restricted precursor bladder/motor/sensory circuitry anchor.", "experiment_tracker_id": "M4A-P035-E001", "paper_tracker_id": "M4A-P035", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T004", "tracker_id": "M4B-O035"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P035::M4A-P035-E001'
    AND et.evidence_type_name = 'Glial-lineage intervention'
    AND ot.outcome_type_name = 'Autonomic, bladder, pain, or respiratory endpoint'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O035', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Zhang L 2024 tested Olfactory ensheathing cells as an OEC, MSC, BMMC, or UCB-family intervention, supporting a trophic or immunomodulatory transplantation profile.',
    'qualitative',
    'Zhang L 2024 tested Olfactory ensheathing cells as an OEC, MSC, BMMC, or UCB-family intervention, supporting a trophic or immunomodulatory transplantation profile.',
    'zhang l 2024 tested olfactory ensheathing cells as an oec, msc, bmmc, or ucb-family intervention, supporting a trophic or immunomodulatory transplantation profile.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'low',
    '{"curator_notes": "Primary title: Olfactory Ensheathing Cell Ameliorate Neuroinflammation Following Spinal Cord Injury Through Upregulating REV-ERB in Microglia.. Note: OEC microglia/REV-ERBalpha neuroinflammation anchor.", "experiment_tracker_id": "M4A-P036-E001", "paper_tracker_id": "M4A-P036", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T005", "tracker_id": "M4B-O036"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P036::M4A-P036-E001'
    AND et.evidence_type_name = 'Trophic or immunomodulatory cell intervention'
    AND ot.outcome_type_name = 'Inflammation / trophic support / clinical feasibility'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O036', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Wang Y 2022 tested Olfactory ensheathing cells as an OEC, MSC, BMMC, or UCB-family intervention, supporting a trophic or immunomodulatory transplantation profile.',
    'qualitative',
    'Wang Y 2022 tested Olfactory ensheathing cells as an OEC, MSC, BMMC, or UCB-family intervention, supporting a trophic or immunomodulatory transplantation profile.',
    'wang y 2022 tested olfactory ensheathing cells as an oec, msc, bmmc, or ucb-family intervention, supporting a trophic or immunomodulatory transplantation profile.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'low',
    '{"curator_notes": "Primary title: Transplantation of olfactory ensheathing cells decreases local and serological monocyte chemoattractant protein 1 level during the acute phase of rat spinal cord injury.. Note: OEC MCP-1/local-serological inflammation anchor.", "experiment_tracker_id": "M4A-P037-E001", "paper_tracker_id": "M4A-P037", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T005", "tracker_id": "M4B-O037"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P037::M4A-P037-E001'
    AND et.evidence_type_name = 'Trophic or immunomodulatory cell intervention'
    AND ot.outcome_type_name = 'Inflammation / trophic support / clinical feasibility'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O037', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Li W 2025 tested Olfactory mucosal MSCs + gelatin sponge as an OEC, MSC, BMMC, or UCB-family intervention, supporting a trophic or immunomodulatory transplantation profile.',
    'qualitative',
    'Li W 2025 tested Olfactory mucosal MSCs + gelatin sponge as an OEC, MSC, BMMC, or UCB-family intervention, supporting a trophic or immunomodulatory transplantation profile.',
    'li w 2025 tested olfactory mucosal mscs + gelatin sponge as an oec, msc, bmmc, or ucb-family intervention, supporting a trophic or immunomodulatory transplantation profile.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'low',
    '{"curator_notes": "Primary title: Olfactory mucosal mesenchymal stem cells delivered by gelatin sponge scaffolds promote functional recovery of spinal cord injury.. Note: Olfactory mucosal MSC scaffold-delivery anchor.", "experiment_tracker_id": "M4A-P038-E001", "paper_tracker_id": "M4A-P038", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T005", "tracker_id": "M4B-O038"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P038::M4A-P038-E001'
    AND et.evidence_type_name = 'Trophic or immunomodulatory cell intervention'
    AND ot.outcome_type_name = 'Inflammation / trophic support / clinical feasibility'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O038', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Zhao Y 2024 tested hUC-MSC cell sheets as an OEC, MSC, BMMC, or UCB-family intervention, supporting a trophic or immunomodulatory transplantation profile.',
    'qualitative',
    'Zhao Y 2024 tested hUC-MSC cell sheets as an OEC, MSC, BMMC, or UCB-family intervention, supporting a trophic or immunomodulatory transplantation profile.',
    'zhao y 2024 tested huc-msc cell sheets as an oec, msc, bmmc, or ucb-family intervention, supporting a trophic or immunomodulatory transplantation profile.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'low',
    '{"curator_notes": "Primary title: Cell Sheets Formation Enhances Therapeutic Effects of Human Umbilical Cord Mesenchymal Stem Cells on Spinal Cord Injury.. Note: Cell-sheet MSC delivery anchor.", "experiment_tracker_id": "M4A-P039-E001", "paper_tracker_id": "M4A-P039", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T005", "tracker_id": "M4B-O039"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P039::M4A-P039-E001'
    AND et.evidence_type_name = 'Trophic or immunomodulatory cell intervention'
    AND ot.outcome_type_name = 'Inflammation / trophic support / clinical feasibility'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O039', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Yang L 2024 tested MSC scaffold / IL-10 response as an OEC, MSC, BMMC, or UCB-family intervention, supporting a trophic or immunomodulatory transplantation profile.',
    'qualitative',
    'Yang L 2024 tested MSC scaffold / IL-10 response as an OEC, MSC, BMMC, or UCB-family intervention, supporting a trophic or immunomodulatory transplantation profile.',
    'yang l 2024 tested msc scaffold / il-10 response as an oec, msc, bmmc, or ucb-family intervention, supporting a trophic or immunomodulatory transplantation profile.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'low',
    '{"curator_notes": "Primary title: Initial IL-10 production dominates the therapy of mesenchymal stem cell scaffold in spinal cord injury.. Note: MSC scaffold immunomodulatory mechanism anchor.", "experiment_tracker_id": "M4A-P040-E001", "paper_tracker_id": "M4A-P040", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T005", "tracker_id": "M4B-O040"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P040::M4A-P040-E001'
    AND et.evidence_type_name = 'Trophic or immunomodulatory cell intervention'
    AND ot.outcome_type_name = 'Inflammation / trophic support / clinical feasibility'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O040', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Liu D 2023 combined NSCs + ROS-scavenging hydrogel with scaffold, scar, hydrogel, exosome, or microenvironmental features, making attribution to the cell product alone limited.',
    'qualitative',
    'Liu D 2023 combined NSCs + ROS-scavenging hydrogel with scaffold, scar, hydrogel, exosome, or microenvironmental features, making attribution to the cell product alone limited.',
    'liu d 2023 combined nscs + ros-scavenging hydrogel with scaffold, scar, hydrogel, exosome, or microenvironmental features, making attribution to the cell product alone limited.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'low',
    '{"curator_notes": "Primary title: ROS-Scavenging Hydrogels Synergize with Neural Stem Cells to Enhance Spinal Cord Injury Repair via Regulating Microenvironment and Facilitating Nerve Regeneration.. Note: Microenvironment-modulating hydrogel plus NSC anchor.", "experiment_tracker_id": "M4A-P041-E001", "paper_tracker_id": "M4A-P041", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T006", "tracker_id": "M4B-O041"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P041::M4A-P041-E001'
    AND et.evidence_type_name = 'Combination scaffold-cell intervention'
    AND ot.outcome_type_name = 'Delivery / microenvironment / regeneration'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O041', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'He W 2023 tested bFGF-overexpressing hUC-MSC + dSCM scaffold as an OEC, MSC, BMMC, or UCB-family intervention, supporting a trophic or immunomodulatory transplantation profile.',
    'qualitative',
    'He W 2023 tested bFGF-overexpressing hUC-MSC + dSCM scaffold as an OEC, MSC, BMMC, or UCB-family intervention, supporting a trophic or immunomodulatory transplantation profile.',
    'he w 2023 tested bfgf-overexpressing huc-msc + dscm scaffold as an oec, msc, bmmc, or ucb-family intervention, supporting a trophic or immunomodulatory transplantation profile.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'low',
    '{"curator_notes": "Primary title: Spinal cord decellularized matrix scaffold loaded with engineered basic fibroblast growth factor-overexpressed human umbilical cord mesenchymal stromal cells promoted the recovery of spinal cord injury.. Note: Engineered MSC + decellularized matrix scaffold.", "experiment_tracker_id": "M4A-P042-E001", "paper_tracker_id": "M4A-P042", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T005", "tracker_id": "M4B-O042"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P042::M4A-P042-E001'
    AND et.evidence_type_name = 'Trophic or immunomodulatory cell intervention'
    AND ot.outcome_type_name = 'Inflammation / trophic support / clinical feasibility'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O042', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Li X 2025 combined NSC-laden microfibers + UC-MSC exosomes with scaffold, scar, hydrogel, exosome, or microenvironmental features, making attribution to the cell product alone limited.',
    'qualitative',
    'Li X 2025 combined NSC-laden microfibers + UC-MSC exosomes with scaffold, scar, hydrogel, exosome, or microenvironmental features, making attribution to the cell product alone limited.',
    'li x 2025 combined nsc-laden microfibers + uc-msc exosomes with scaffold, scar, hydrogel, exosome, or microenvironmental features, making attribution to the cell product alone limited.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'low',
    '{"curator_notes": "Primary title: Conjugated therapy with coaxially printed neural stem cell-laden microfibers and umbilical cord mesenchymal stem cell derived exosomes on complete transactional spinal cord defects.. Note: Printed NSC/exosome conjugated therapy.", "experiment_tracker_id": "M4A-P043-E001", "paper_tracker_id": "M4A-P043", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T006", "tracker_id": "M4B-O043"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P043::M4A-P043-E001'
    AND et.evidence_type_name = 'Combination scaffold-cell intervention'
    AND ot.outcome_type_name = 'Delivery / microenvironment / regeneration'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O043', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Kao Y 2025 combined hMSC + HA hydrogel/polydopamine nanoparticles with scaffold, scar, hydrogel, exosome, or microenvironmental features, making attribution to the cell product alone limited.',
    'qualitative',
    'Kao Y 2025 combined hMSC + HA hydrogel/polydopamine nanoparticles with scaffold, scar, hydrogel, exosome, or microenvironmental features, making attribution to the cell product alone limited.',
    'kao y 2025 combined hmsc + ha hydrogel/polydopamine nanoparticles with scaffold, scar, hydrogel, exosome, or microenvironmental features, making attribution to the cell product alone limited.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'low',
    '{"curator_notes": "Primary title: Synergistic restoration of spinal cord injury through hyaluronic acid conjugated hydrogel-polydopamine nanoparticles combined with human mesenchymal stem cell transplantation.. Note: hMSC/hydrogel nanoparticle combination.", "experiment_tracker_id": "M4A-P044-E001", "paper_tracker_id": "M4A-P044", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T006", "tracker_id": "M4B-O044"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P044::M4A-P044-E001'
    AND et.evidence_type_name = 'Combination scaffold-cell intervention'
    AND ot.outcome_type_name = 'Delivery / microenvironment / regeneration'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O044', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Liu D 2025 combined NSC + NO-releasing cerium oxide hydrogel with scaffold, scar, hydrogel, exosome, or microenvironmental features, making attribution to the cell product alone limited.',
    'qualitative',
    'Liu D 2025 combined NSC + NO-releasing cerium oxide hydrogel with scaffold, scar, hydrogel, exosome, or microenvironmental features, making attribution to the cell product alone limited.',
    'liu d 2025 combined nsc + no-releasing cerium oxide hydrogel with scaffold, scar, hydrogel, exosome, or microenvironmental features, making attribution to the cell product alone limited.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'low',
    '{"curator_notes": "Primary title: Nitric Oxide-Releasing Mesoporous Hollow Cerium Oxide Nanozyme-Based Hydrogel Synergizes with Neural Stem Cell for Spinal Cord Injury Repair.. Note: NO/nanozyme hydrogel plus NSC anchor.", "experiment_tracker_id": "M4A-P045-E001", "paper_tracker_id": "M4A-P045", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T006", "tracker_id": "M4B-O045"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P045::M4A-P045-E001'
    AND et.evidence_type_name = 'Combination scaffold-cell intervention'
    AND ot.outcome_type_name = 'Delivery / microenvironment / regeneration'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O045', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Sanchez-Martin MDM 2025 used Fetal rat neural progenitor cells + optogenetic stimulation in Rodent SCI, extending transplantation evidence to fetal, embryonic, autonomic, respiratory, or historical graft paradigms.',
    'qualitative',
    'Sanchez-Martin MDM 2025 used Fetal rat neural progenitor cells + optogenetic stimulation in Rodent SCI, extending transplantation evidence to fetal, embryonic, autonomic, respiratory, or historical graft paradigms.',
    'sanchez-martin mdm 2025 used fetal rat neural progenitor cells + optogenetic stimulation in rodent sci, extending transplantation evidence to fetal, embryonic, autonomic, respiratory, or historical graft paradigms.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'low',
    '{"curator_notes": "Primary title: Fetal rat neural progenitor cell transplantation after spinal cord injury improves motor recovery following optogenetic stimulation.. Note: Fetal NPC optogenetic stimulation motor recovery.", "experiment_tracker_id": "M4A-P046-E001", "paper_tracker_id": "M4A-P046", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T007", "tracker_id": "M4B-O046"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P046::M4A-P046-E001'
    AND et.evidence_type_name = 'Legacy or specialized graft intervention'
    AND ot.outcome_type_name = 'Autonomic / respiratory / motor / historical translation'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O046', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Giraldo E 2022 used Human fetal spinal-cord-derived NPCs primed with Rho/ROCK inhibitor in Rodent acute SCI, extending transplantation evidence to fetal, embryonic, autonomic, respiratory, or historical graft paradigms.',
    'qualitative',
    'Giraldo E 2022 used Human fetal spinal-cord-derived NPCs primed with Rho/ROCK inhibitor in Rodent acute SCI, extending transplantation evidence to fetal, embryonic, autonomic, respiratory, or historical graft paradigms.',
    'giraldo e 2022 used human fetal spinal-cord-derived npcs primed with rho/rock inhibitor in rodent acute sci, extending transplantation evidence to fetal, embryonic, autonomic, respiratory, or historical graft paradigms.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'low',
    '{"curator_notes": "Primary title: Transplantation of Human-Fetal-Spinal-Cord-Derived NPCs Primed with a Polyglutamate-Conjugated Rho/Rock Inhibitor in Acute Spinal Cord Injury.. Note: Human fetal spinal NPC priming acute SCI.", "experiment_tracker_id": "M4A-P047-E001", "paper_tracker_id": "M4A-P047", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T007", "tracker_id": "M4B-O047"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P047::M4A-P047-E001'
    AND et.evidence_type_name = 'Legacy or specialized graft intervention'
    AND ot.outcome_type_name = 'Autonomic / respiratory / motor / historical translation'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O047', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Shin JC 2015 tested Human fetal brain-derived neural stem/progenitor cells in Human traumatic cervical SCI, providing a clinical feasibility or safety anchor for cell transplantation after SCI.',
    'qualitative',
    'Shin JC 2015 tested Human fetal brain-derived neural stem/progenitor cells in Human traumatic cervical SCI, providing a clinical feasibility or safety anchor for cell transplantation after SCI.',
    'shin jc 2015 tested human fetal brain-derived neural stem/progenitor cells in human traumatic cervical sci, providing a clinical feasibility or safety anchor for cell transplantation after sci.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'medium',
    '{"curator_notes": "Primary title: Clinical Trial of Human Fetal Brain-Derived Neural Stem/Progenitor Cell Transplantation in Patients with Traumatic Cervical Spinal Cord Injury.. Note: Human fetal NSPC traumatic cervical clinical trial.", "experiment_tracker_id": "M4A-P048-E001", "paper_tracker_id": "M4A-P048", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T001", "tracker_id": "M4B-O048"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P048::M4A-P048-E001'
    AND et.evidence_type_name = 'Clinical intervention'
    AND ot.outcome_type_name = 'Safety / feasibility / clinical outcome'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O048', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Tarasenko YI 2007 used Human fetal neural stem cells in Rat contusion SCI, extending transplantation evidence to fetal, embryonic, autonomic, respiratory, or historical graft paradigms.',
    'qualitative',
    'Tarasenko YI 2007 used Human fetal neural stem cells in Rat contusion SCI, extending transplantation evidence to fetal, embryonic, autonomic, respiratory, or historical graft paradigms.',
    'tarasenko yi 2007 used human fetal neural stem cells in rat contusion sci, extending transplantation evidence to fetal, embryonic, autonomic, respiratory, or historical graft paradigms.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'low',
    '{"curator_notes": "Primary title: Human fetal neural stem cells grafted into contusion-injured rat spinal cords improve behavior.. Note: Human fetal NSC grafting into contusion-injured rat cord.", "experiment_tracker_id": "M4A-P049-E001", "paper_tracker_id": "M4A-P049", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T007", "tracker_id": "M4B-O049"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P049::M4A-P049-E001'
    AND et.evidence_type_name = 'Legacy or specialized graft intervention'
    AND ot.outcome_type_name = 'Autonomic / respiratory / motor / historical translation'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O049', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Lin CC 2017 shows that transplantation outcomes include autonomic, bladder, pain, respiratory, or cardiovascular readouts that should not be collapsed into locomotor recovery.',
    'qualitative',
    'Lin CC 2017 shows that transplantation outcomes include autonomic, bladder, pain, respiratory, or cardiovascular readouts that should not be collapsed into locomotor recovery.',
    'lin cc 2017 shows that transplantation outcomes include autonomic, bladder, pain, respiratory, or cardiovascular readouts that should not be collapsed into locomotor recovery.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'low',
    '{"curator_notes": "Primary title: The Therapeutic Effectiveness of Delayed Fetal Spinal Cord Tissue Transplantation on Respiratory Function Following Mid-Cervical Spinal Cord Injury.. Note: Delayed fetal spinal tissue respiratory recovery.", "experiment_tracker_id": "M4A-P050-E001", "paper_tracker_id": "M4A-P050", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T007", "tracker_id": "M4B-O050"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P050::M4A-P050-E001'
    AND et.evidence_type_name = 'Legacy or specialized graft intervention'
    AND ot.outcome_type_name = 'Autonomic, bladder, pain, or respiratory endpoint'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O050', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Fessler RG 2022 anchors OPC or oligodendrogenic transplantation evidence where remyelination and safety are distinct from neuronal relay claims.',
    'qualitative',
    'Fessler RG 2022 anchors OPC or oligodendrogenic transplantation evidence where remyelination and safety are distinct from neuronal relay claims.',
    'fessler rg 2022 anchors opc or oligodendrogenic transplantation evidence where remyelination and safety are distinct from neuronal relay claims.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'medium',
    '{"curator_notes": "Primary title: A phase 1/2a dose-escalation study of oligodendrocyte progenitor cells in individuals with subacute cervical spinal cord injury.. Note: OPC phase 1/2a dose-escalation clinical study.", "experiment_tracker_id": "M4A-P051-E001", "paper_tracker_id": "M4A-P051", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T001", "tracker_id": "M4B-O051"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P051::M4A-P051-E001'
    AND et.evidence_type_name = 'Clinical intervention'
    AND ot.outcome_type_name = 'OPC / oligodendrogenic safety and repair'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O051', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Priest CA 2015 anchors OPC or oligodendrogenic transplantation evidence where remyelination and safety are distinct from neuronal relay claims.',
    'qualitative',
    'Priest CA 2015 anchors OPC or oligodendrogenic transplantation evidence where remyelination and safety are distinct from neuronal relay claims.',
    'priest ca 2015 anchors opc or oligodendrogenic transplantation evidence where remyelination and safety are distinct from neuronal relay claims.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'low',
    '{"curator_notes": "Primary title: Preclinical safety of human embryonic stem cell-derived oligodendrocyte progenitors supporting clinical trials in spinal cord injury.. Note: hESC-OPC preclinical safety for SCI clinical trials.", "experiment_tracker_id": "M4A-P052-E001", "paper_tracker_id": "M4A-P052", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T004", "tracker_id": "M4B-O052"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P052::M4A-P052-E001'
    AND et.evidence_type_name = 'Glial-lineage intervention'
    AND ot.outcome_type_name = 'OPC / oligodendrogenic safety and repair'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O052', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Anderson KD 2017 anchors Schwann or glial-support transplantation evidence for axon growth, connectivity, remyelination, or safety.',
    'qualitative',
    'Anderson KD 2017 anchors Schwann or glial-support transplantation evidence for axon growth, connectivity, remyelination, or safety.',
    'anderson kd 2017 anchors schwann or glial-support transplantation evidence for axon growth, connectivity, remyelination, or safety.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'medium',
    '{"curator_notes": "Primary title: Safety of Autologous Human Schwann Cell Transplantation in Subacute Thoracic Spinal Cord Injury.. Note: Autologous Schwann cell subacute thoracic safety.", "experiment_tracker_id": "M4A-P053-E001", "paper_tracker_id": "M4A-P053", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T001", "tracker_id": "M4B-O053"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P053::M4A-P053-E001'
    AND et.evidence_type_name = 'Clinical intervention'
    AND ot.outcome_type_name = 'Schwann / glial support'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O053', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Trueblood CT 2025 shows that transplantation outcomes include autonomic, bladder, pain, respiratory, or cardiovascular readouts that should not be collapsed into locomotor recovery.',
    'qualitative',
    'Trueblood CT 2025 shows that transplantation outcomes include autonomic, bladder, pain, respiratory, or cardiovascular readouts that should not be collapsed into locomotor recovery.',
    'trueblood ct 2025 shows that transplantation outcomes include autonomic, bladder, pain, respiratory, or cardiovascular readouts that should not be collapsed into locomotor recovery.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'low',
    '{"curator_notes": "Primary title: Transplanting Neural Progenitor Cells Improves Neural Regulation But Not Hormonal Reliance of Cardiovascular Function Following Spinal Cord Injury.. Note: Neural progenitor cardiovascular/autonomic regulation.", "experiment_tracker_id": "M4A-P054-E001", "paper_tracker_id": "M4A-P054", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T007", "tracker_id": "M4B-O054"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P054::M4A-P054-E001'
    AND et.evidence_type_name = 'Legacy or specialized graft intervention'
    AND ot.outcome_type_name = 'Autonomic, bladder, pain, or respiratory endpoint'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O054', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Akhlaghpasand M 2025 shows that transplantation outcomes include autonomic, bladder, pain, respiratory, or cardiovascular readouts that should not be collapsed into locomotor recovery.',
    'qualitative',
    'Akhlaghpasand M 2025 shows that transplantation outcomes include autonomic, bladder, pain, respiratory, or cardiovascular readouts that should not be collapsed into locomotor recovery.',
    'akhlaghpasand m 2025 shows that transplantation outcomes include autonomic, bladder, pain, respiratory, or cardiovascular readouts that should not be collapsed into locomotor recovery.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'medium',
    '{"curator_notes": "Primary title: Improvement of Neurogenic Bladder Dysfunction Following Combined Cell Therapy with Mesenchymal Stem Cell and Schwann Cell in Spinal Cord Injury: A Randomized, Open-Label, Phase II Clinical Trial.. Note: Combined MSC/Schwann neurogenic bladder clinical outcome.", "experiment_tracker_id": "M4A-P055-E001", "paper_tracker_id": "M4A-P055", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T001", "tracker_id": "M4B-O055"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P055::M4A-P055-E001'
    AND et.evidence_type_name = 'Clinical intervention'
    AND ot.outcome_type_name = 'Autonomic, bladder, pain, or respiratory endpoint'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O055', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Akhlaghpasand M 2025 shows that transplantation outcomes include autonomic, bladder, pain, respiratory, or cardiovascular readouts that should not be collapsed into locomotor recovery.',
    'qualitative',
    'Akhlaghpasand M 2025 shows that transplantation outcomes include autonomic, bladder, pain, respiratory, or cardiovascular readouts that should not be collapsed into locomotor recovery.',
    'akhlaghpasand m 2025 shows that transplantation outcomes include autonomic, bladder, pain, respiratory, or cardiovascular readouts that should not be collapsed into locomotor recovery.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'medium',
    '{"curator_notes": "Primary title: Effects of Combined Intrathecal Mesenchymal Stem Cells and Schwann Cells Transplantation on Neuropathic Pain in Complete Spinal Cord Injury: A Phase II Randomized Active-Controlled Trial.. Note: Combined MSC/Schwann neuropathic pain clinical outcome.", "experiment_tracker_id": "M4A-P056-E001", "paper_tracker_id": "M4A-P056", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T001", "tracker_id": "M4B-O056"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P056::M4A-P056-E001'
    AND et.evidence_type_name = 'Clinical intervention'
    AND ot.outcome_type_name = 'Autonomic, bladder, pain, or respiratory endpoint'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O056', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Lima C 2006 tested Olfactory mucosa autograft in Human SCI, providing a clinical feasibility or safety anchor for cell transplantation after SCI.',
    'qualitative',
    'Lima C 2006 tested Olfactory mucosa autograft in Human SCI, providing a clinical feasibility or safety anchor for cell transplantation after SCI.',
    'lima c 2006 tested olfactory mucosa autograft in human sci, providing a clinical feasibility or safety anchor for cell transplantation after sci.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'medium',
    '{"curator_notes": "Primary title: Olfactory mucosa autografts in human spinal cord injury: a pilot clinical study.. Note: Olfactory mucosa autograft human pilot.", "experiment_tracker_id": "M4A-P057-E001", "paper_tracker_id": "M4A-P057", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T001", "tracker_id": "M4B-O057"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P057::M4A-P057-E001'
    AND et.evidence_type_name = 'Clinical intervention'
    AND ot.outcome_type_name = 'Safety / feasibility / clinical outcome'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O057', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Iwatsuki K 2016 tested Olfactory mucosa autograft in Human chronic complete SCI, providing a clinical feasibility or safety anchor for cell transplantation after SCI.',
    'qualitative',
    'Iwatsuki K 2016 tested Olfactory mucosa autograft in Human chronic complete SCI, providing a clinical feasibility or safety anchor for cell transplantation after SCI.',
    'iwatsuki k 2016 tested olfactory mucosa autograft in human chronic complete sci, providing a clinical feasibility or safety anchor for cell transplantation after sci.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'medium',
    '{"curator_notes": "Primary title: A Pilot Clinical Study of Olfactory Mucosa Autograft for Chronic Complete Spinal Cord Injury.. Note: Olfactory mucosa autograft chronic complete pilot.", "experiment_tracker_id": "M4A-P058-E001", "paper_tracker_id": "M4A-P058", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T001", "tracker_id": "M4B-O058"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P058::M4A-P058-E001'
    AND et.evidence_type_name = 'Clinical intervention'
    AND ot.outcome_type_name = 'Safety / feasibility / clinical outcome'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O058', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'DePaul MA 2017 anchors Schwann or glial-support transplantation evidence for axon growth, connectivity, remyelination, or safety.',
    'qualitative',
    'DePaul MA 2017 anchors Schwann or glial-support transplantation evidence for axon growth, connectivity, remyelination, or safety.',
    'depaul ma 2017 anchors schwann or glial-support transplantation evidence for axon growth, connectivity, remyelination, or safety.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'low',
    '{"curator_notes": "Primary title: Combinatory repair strategy to promote axon regeneration and functional recovery after chronic spinal cord injury.. Note: Combinatory repair strategy after chronic SCI.", "experiment_tracker_id": "M4A-P059-E001", "paper_tracker_id": "M4A-P059", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T004", "tracker_id": "M4B-O059"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P059::M4A-P059-E001'
    AND et.evidence_type_name = 'Glial-lineage intervention'
    AND ot.outcome_type_name = 'Schwann / glial support'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O059', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Zhu H 2016 tested Umbilical cord blood mononuclear cells in Human chronic complete SCI, providing a clinical feasibility or safety anchor for cell transplantation after SCI.',
    'qualitative',
    'Zhu H 2016 tested Umbilical cord blood mononuclear cells in Human chronic complete SCI, providing a clinical feasibility or safety anchor for cell transplantation after SCI.',
    'zhu h 2016 tested umbilical cord blood mononuclear cells in human chronic complete sci, providing a clinical feasibility or safety anchor for cell transplantation after sci.',
    'Module 4A tracker / PubMed metadata',
    'Abstract / carried',
    'medium',
    '{"curator_notes": "Primary title: Phase I-II Clinical Trial Assessing Safety and Efficacy of Umbilical Cord Blood Mononuclear Cell Transplant Therapy of Chronic Complete Spinal Cord Injury.. Note: UCB mononuclear phase I/II clinical trial.", "experiment_tracker_id": "M4A-P060-E001", "paper_tracker_id": "M4A-P060", "quantitative": "NO", "statistics_reported": "Abstract-level first pass; exact statistics not extracted", "topic_id": "M4B-T001", "tracker_id": "M4B-O060"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P060::M4A-P060-E001'
    AND et.evidence_type_name = 'Clinical intervention'
    AND ot.outcome_type_name = 'Safety / feasibility / clinical outcome'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O060', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Lu P 2007 M4A-P001-E002 preserves a distinct Rat experiment testing Mechanistic outcome assessment after MSC graft transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for chronic MSC graft permissiveness: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'qualitative',
    'Lu P 2007 M4A-P001-E002 preserves a distinct Rat experiment testing Mechanistic outcome assessment after MSC graft transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for chronic MSC graft permissiveness: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'M4A-P001-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Axon regeneration through scars and into sites of chronic spinal cord injury. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M4A-P001-E002", "paper_tracker_id": "M4A-P001", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M4B-T006", "tracker_id": "M4B-O061"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P001::M4A-P001-E002'
    AND et.evidence_type_name = 'Combination scaffold-cell intervention'
    AND ot.outcome_type_name = 'Second abstract-level experiment row isolates the primary mechanistic endpoint for chronic MSC graft permissiveness: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O061', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Ito K 2024 M4A-P003-E002 preserves a distinct Rodent chronic complete SCI model experiment testing Mechanistic outcome assessment after hNS/PC + dECM scaffold transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for chronic iPSC-NS/PC scaffold histology: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'qualitative',
    'Ito K 2024 M4A-P003-E002 preserves a distinct Rodent chronic complete SCI model experiment testing Mechanistic outcome assessment after hNS/PC + dECM scaffold transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for chronic iPSC-NS/PC scaffold histology: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'M4A-P003-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Histological effects of combined therapy involving scar resection, decellularized scaffolds, and human iPSC-NS/PCs transplantation in chronic complete spinal cord injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M4A-P003-E002", "paper_tracker_id": "M4A-P003", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M4B-T006", "tracker_id": "M4B-O062"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P003::M4A-P003-E002'
    AND et.evidence_type_name = 'Combination scaffold-cell intervention'
    AND ot.outcome_type_name = 'Second abstract-level experiment row isolates the primary mechanistic endpoint for chronic iPSC-NS/PC scaffold histology: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O062', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Abraham ME 2026 M4A-P004-E002 preserves a distinct Human chronic cervical SCI experiment testing Mechanistic outcome assessment after NSI-566 human spinal cord-derived neural stem cells transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for clinical NSC safety: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'qualitative',
    'Abraham ME 2026 M4A-P004-E002 preserves a distinct Human chronic cervical SCI experiment testing Mechanistic outcome assessment after NSI-566 human spinal cord-derived neural stem cells transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for clinical NSC safety: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'M4A-P004-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Long-term safety and clinical outcomes from a single-site phase 1 study of neural stem cell transplantation for chronic cervical spinal cord injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M4A-P004-E002", "paper_tracker_id": "M4A-P004", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M4B-T001", "tracker_id": "M4B-O063"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P004::M4A-P004-E002'
    AND et.evidence_type_name = 'Clinical intervention'
    AND ot.outcome_type_name = 'Second abstract-level experiment row isolates the primary mechanistic endpoint for clinical NSC safety: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O063', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Martin JR 2024 M4A-P005-E002 preserves a distinct Human chronic thoracic SCI experiment testing Mechanistic outcome assessment after NSI-566 human spinal cord-derived neural stem cells transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for clinical NSC safety: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'qualitative',
    'Martin JR 2024 M4A-P005-E002 preserves a distinct Human chronic thoracic SCI experiment testing Mechanistic outcome assessment after NSI-566 human spinal cord-derived neural stem cells transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for clinical NSC safety: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'M4A-P005-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Long-term clinical and safety outcomes from a single-site phase 1 study of neural stem cell transplantation for chronic thoracic spinal cord injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M4A-P005-E002", "paper_tracker_id": "M4A-P005", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M4B-T001", "tracker_id": "M4B-O064"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P005::M4A-P005-E002'
    AND et.evidence_type_name = 'Clinical intervention'
    AND ot.outcome_type_name = 'Second abstract-level experiment row isolates the primary mechanistic endpoint for clinical NSC safety: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O064', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Gant KL 2022 M4A-P006-E002 preserves a distinct Human chronic SCI experiment testing Mechanistic outcome assessment after Autologous Schwann cells transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for clinical Schwann safety: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'qualitative',
    'Gant KL 2022 M4A-P006-E002 preserves a distinct Human chronic SCI experiment testing Mechanistic outcome assessment after Autologous Schwann cells transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for clinical Schwann safety: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'M4A-P006-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Phase 1 Safety Trial of Autologous Human Schwann Cell Transplantation in Chronic Spinal Cord Injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M4A-P006-E002", "paper_tracker_id": "M4A-P006", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M4B-T001", "tracker_id": "M4B-O065"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P006::M4A-P006-E002'
    AND et.evidence_type_name = 'Clinical intervention'
    AND ot.outcome_type_name = 'Second abstract-level experiment row isolates the primary mechanistic endpoint for clinical Schwann safety: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O065', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Kaplan N 2025 M4A-P007-E002 preserves a distinct Human chronic complete SCI experiment testing Mechanistic outcome assessment after Wharton jelly MSCs transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for clinical MSC safety: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'qualitative',
    'Kaplan N 2025 M4A-P007-E002 preserves a distinct Human chronic complete SCI experiment testing Mechanistic outcome assessment after Wharton jelly MSCs transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for clinical MSC safety: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'M4A-P007-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Multiroute administration of Wharton''s jelly mesenchymal stem cells in chronic complete spinal cord injury: A phase I safety and feasibility study.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M4A-P007-E002", "paper_tracker_id": "M4A-P007", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M4B-T001", "tracker_id": "M4B-O066"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P007::M4A-P007-E002'
    AND et.evidence_type_name = 'Clinical intervention'
    AND ot.outcome_type_name = 'Second abstract-level experiment row isolates the primary mechanistic endpoint for clinical MSC safety: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O066', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Macêdo CT 2024 M4A-P008-E002 preserves a distinct Human complete cervical SCI experiment testing Mechanistic outcome assessment after Autologous mesenchymal stromal cells transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for clinical MSC pilot: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'qualitative',
    'Macêdo CT 2024 M4A-P008-E002 preserves a distinct Human complete cervical SCI experiment testing Mechanistic outcome assessment after Autologous mesenchymal stromal cells transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for clinical MSC pilot: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'M4A-P008-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Transplantation of autologous mesenchymal stromal cells in complete cervical spinal cord injury: a pilot study.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M4A-P008-E002", "paper_tracker_id": "M4A-P008", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M4B-T001", "tracker_id": "M4B-O067"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P008::M4A-P008-E002'
    AND et.evidence_type_name = 'Clinical intervention'
    AND ot.outcome_type_name = 'Second abstract-level experiment row isolates the primary mechanistic endpoint for clinical MSC pilot: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O067', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Zamani H 2022 M4A-P009-E002 preserves a distinct Human chronic SCI experiment testing Mechanistic outcome assessment after Autologous OEC + BM-MSC transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for clinical OEC MSC safety: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'qualitative',
    'Zamani H 2022 M4A-P009-E002 preserves a distinct Human chronic SCI experiment testing Mechanistic outcome assessment after Autologous OEC + BM-MSC transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for clinical OEC MSC safety: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'M4A-P009-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Safety and feasibility of autologous olfactory ensheathing cell and bone marrow mesenchymal stem cell co-transplantation in chronic human spinal cord injury: a clinical trial.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M4A-P009-E002", "paper_tracker_id": "M4A-P009", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M4B-T001", "tracker_id": "M4B-O068"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P009::M4A-P009-E002'
    AND et.evidence_type_name = 'Clinical intervention'
    AND ot.outcome_type_name = 'Second abstract-level experiment row isolates the primary mechanistic endpoint for clinical OEC MSC safety: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O068', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Sinopoulou E 2025 M4A-P011-E002 preserves a distinct Non-human primate experiment testing Mechanistic outcome assessment after Human ESC-derived spinal cord NSCs transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for primate NSC function: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'qualitative',
    'Sinopoulou E 2025 M4A-P011-E002 preserves a distinct Non-human primate experiment testing Mechanistic outcome assessment after Human ESC-derived spinal cord NSCs transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for primate NSC function: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'M4A-P011-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Extensive restoration of forelimb function in primates with spinal cord injury by neural stem cell transplantation.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M4A-P011-E002", "paper_tracker_id": "M4A-P011", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M4B-T002", "tracker_id": "M4B-O069"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P011::M4A-P011-E002'
    AND et.evidence_type_name = 'Neural graft intervention'
    AND ot.outcome_type_name = 'Second abstract-level experiment row isolates the primary mechanistic endpoint for primate NSC function: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O069', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Iwai H 2015 M4A-P012-E002 preserves a distinct Common marmoset experiment testing Mechanistic outcome assessment after ESC-derived NS/PCs transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for primate ESC-NSPC safety: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'qualitative',
    'Iwai H 2015 M4A-P012-E002 preserves a distinct Common marmoset experiment testing Mechanistic outcome assessment after ESC-derived NS/PCs transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for primate ESC-NSPC safety: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'M4A-P012-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Allogeneic Neural Stem/Progenitor Cells Derived From Embryonic Stem Cells Promote Functional Recovery After Transplantation Into Injured Spinal Cord of Nonhuman Primates.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M4A-P012-E002", "paper_tracker_id": "M4A-P012", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M4B-T002", "tracker_id": "M4B-O070"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P012::M4A-P012-E002'
    AND et.evidence_type_name = 'Neural graft intervention'
    AND ot.outcome_type_name = 'Second abstract-level experiment row isolates the primary mechanistic endpoint for primate ESC-NSPC safety: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O070', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Tucker A 2025 M4A-P013-E002 preserves a distinct Mouse thoracic contusion experiment testing Mechanistic outcome assessment after Engrafted spinal cord neurons / NPC-derived neurons transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for synaptic integration: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'qualitative',
    'Tucker A 2025 M4A-P013-E002 preserves a distinct Mouse thoracic contusion experiment testing Mechanistic outcome assessment after Engrafted spinal cord neurons / NPC-derived neurons transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for synaptic integration: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'M4A-P013-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Functional synaptic connectivity of engrafted spinal cord neurons with hindlimb motor circuitry in the injured spinal cord.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M4A-P013-E002", "paper_tracker_id": "M4A-P013", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M4B-T002", "tracker_id": "M4B-O071"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P013::M4A-P013-E002'
    AND et.evidence_type_name = 'Neural graft intervention'
    AND ot.outcome_type_name = 'Second abstract-level experiment row isolates the primary mechanistic endpoint for synaptic integration: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O071', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Ceto S 2020 M4A-P014-E002 preserves a distinct Rodent SCI experiment testing Mechanistic outcome assessment after NS/PC grafts transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for synaptic integration: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'qualitative',
    'Ceto S 2020 M4A-P014-E002 preserves a distinct Rodent SCI experiment testing Mechanistic outcome assessment after NS/PC grafts transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for synaptic integration: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'M4A-P014-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Neural Stem Cell Grafts Form Extensive Synaptic Networks that Integrate with Host Circuits after Spinal Cord Injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M4A-P014-E002", "paper_tracker_id": "M4A-P014", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M4B-T002", "tracker_id": "M4B-O072"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P014::M4A-P014-E002'
    AND et.evidence_type_name = 'Neural graft intervention'
    AND ot.outcome_type_name = 'Second abstract-level experiment row isolates the primary mechanistic endpoint for synaptic integration: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O072', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Bonner JF 2011 M4A-P016-E002 preserves a distinct Rat dorsal column SCI experiment testing Mechanistic outcome assessment after Neuronal/glial restricted precursor graft transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for synaptic relay: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'qualitative',
    'Bonner JF 2011 M4A-P016-E002 preserves a distinct Rat dorsal column SCI experiment testing Mechanistic outcome assessment after Neuronal/glial restricted precursor graft transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for synaptic relay: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'M4A-P016-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Grafted neural progenitors integrate and restore synaptic connectivity across the injured spinal cord.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M4A-P016-E002", "paper_tracker_id": "M4A-P016", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M4B-T002", "tracker_id": "M4B-O073"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P016::M4A-P016-E002'
    AND et.evidence_type_name = 'Neural graft intervention'
    AND ot.outcome_type_name = 'Second abstract-level experiment row isolates the primary mechanistic endpoint for synaptic relay: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O073', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Zhu Y 2025 M4A-P018-E002 preserves a distinct Organoid / rodent SCI experiment testing Mechanistic outcome assessment after Engineered thoracic spinal cord organoids transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for organoid graft: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'qualitative',
    'Zhu Y 2025 M4A-P018-E002 preserves a distinct Organoid / rodent SCI experiment testing Mechanistic outcome assessment after Engineered thoracic spinal cord organoids transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for organoid graft: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'M4A-P018-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Engineered thoracic spinal cord organoids for transplantation after spinal cord injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M4A-P018-E002", "paper_tracker_id": "M4A-P018", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M4B-T002", "tracker_id": "M4B-O074"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P018::M4A-P018-E002'
    AND et.evidence_type_name = 'Neural graft intervention'
    AND ot.outcome_type_name = 'Second abstract-level experiment row isolates the primary mechanistic endpoint for organoid graft: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O074', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Yao X 2025 M4A-P019-E002 preserves a distinct NOD-SCID mouse contusion experiment testing Mechanistic outcome assessment after Human iPSC-derived spinal neural progenitors transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for iPSC spinal progenitors: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'qualitative',
    'Yao X 2025 M4A-P019-E002 preserves a distinct NOD-SCID mouse contusion experiment testing Mechanistic outcome assessment after Human iPSC-derived spinal neural progenitors transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for iPSC spinal progenitors: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'M4A-P019-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Human iPSC-derived spinal neural progenitors enhance sensorimotor recovery in spinal cord-injured NOD-SCID mice via differentiation and microenvironment regulation.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M4A-P019-E002", "paper_tracker_id": "M4A-P019", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M4B-T002", "tracker_id": "M4B-O075"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P019::M4A-P019-E002'
    AND et.evidence_type_name = 'Neural graft intervention'
    AND ot.outcome_type_name = 'Second abstract-level experiment row isolates the primary mechanistic endpoint for iPSC spinal progenitors: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O075', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Zheng Y 2025 M4A-P020-E002 preserves a distinct Mouse SCI experiment testing Mechanistic outcome assessment after Human iPSC-derived A2B5+ neural progenitors transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for iPSC A2B5 progenitors: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'qualitative',
    'Zheng Y 2025 M4A-P020-E002 preserves a distinct Mouse SCI experiment testing Mechanistic outcome assessment after Human iPSC-derived A2B5+ neural progenitors transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for iPSC A2B5 progenitors: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'M4A-P020-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Functional Recovery by Transplantation of Human iPSC-Derived A2B5 Positive Neural Progenitor Cell After Spinal Cord Injury in Mice.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M4A-P020-E002", "paper_tracker_id": "M4A-P020", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M4B-T002", "tracker_id": "M4B-O076"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P020::M4A-P020-E002'
    AND et.evidence_type_name = 'Neural graft intervention'
    AND ot.outcome_type_name = 'Second abstract-level experiment row isolates the primary mechanistic endpoint for iPSC A2B5 progenitors: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O076', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Shibata T 2023 M4A-P021-E002 preserves a distinct Chronic SCI model experiment testing Mechanistic outcome assessment after hiPSC-derived NS/PC + rehabilitation transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for iPSC rehabilitation combination: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'qualitative',
    'Shibata T 2023 M4A-P021-E002 preserves a distinct Chronic SCI model experiment testing Mechanistic outcome assessment after hiPSC-derived NS/PC + rehabilitation transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for iPSC rehabilitation combination: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'M4A-P021-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Rehabilitative Training Enhances Therapeutic Effect of Human-iPSC-Derived Neural Stem/Progenitor Cells Transplantation in Chronic Spinal Cord Injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M4A-P021-E002", "paper_tracker_id": "M4A-P021", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M4B-T002", "tracker_id": "M4B-O077"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P021::M4A-P021-E002'
    AND et.evidence_type_name = 'Neural graft intervention'
    AND ot.outcome_type_name = 'Second abstract-level experiment row isolates the primary mechanistic endpoint for iPSC rehabilitation combination: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O077', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Saijo Y 2024 M4A-P022-E002 preserves a distinct Rodent SCI experiment testing Mechanistic outcome assessment after hiPSC-NS/PCs expressing synaptic organizer CPTX transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for iPSC synaptic organizer: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'qualitative',
    'Saijo Y 2024 M4A-P022-E002 preserves a distinct Rodent SCI experiment testing Mechanistic outcome assessment after hiPSC-NS/PCs expressing synaptic organizer CPTX transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for iPSC synaptic organizer: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'M4A-P022-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Human-induced pluripotent stem cell-derived neural stem/progenitor cell ex vivo gene therapy with synaptic organizer CPTX for spinal cord injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M4A-P022-E002", "paper_tracker_id": "M4A-P022", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M4B-T002", "tracker_id": "M4B-O078"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P022::M4A-P022-E002'
    AND et.evidence_type_name = 'Neural graft intervention'
    AND ot.outcome_type_name = 'Second abstract-level experiment row isolates the primary mechanistic endpoint for iPSC synaptic organizer: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O078', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Suematsu Y 2023 M4A-P023-E002 preserves a distinct Rodent SCI experiment testing Mechanistic outcome assessment after HGF-pretreated hiPSC-NS/PC strategy transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for iPSC HGF pretreatment: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'qualitative',
    'Suematsu Y 2023 M4A-P023-E002 preserves a distinct Rodent SCI experiment testing Mechanistic outcome assessment after HGF-pretreated hiPSC-NS/PC strategy transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for iPSC HGF pretreatment: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'M4A-P023-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Hepatocyte growth factor pretreatment boosts functional recovery after spinal cord injury through human iPSC-derived neural stem/progenitor cell transplantation.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M4A-P023-E002", "paper_tracker_id": "M4A-P023", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M4B-T002", "tracker_id": "M4B-O079"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P023::M4A-P023-E002'
    AND et.evidence_type_name = 'Neural graft intervention'
    AND ot.outcome_type_name = 'Second abstract-level experiment row isolates the primary mechanistic endpoint for iPSC HGF pretreatment: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O079', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Li Y 2023 M4A-P025-E002 preserves a distinct Rat SCI experiment testing Mechanistic outcome assessment after NSC grafts + caudal BDNF guidance transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for BDNF axon guidance: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'qualitative',
    'Li Y 2023 M4A-P025-E002 preserves a distinct Rat SCI experiment testing Mechanistic outcome assessment after NSC grafts + caudal BDNF guidance transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for BDNF axon guidance: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'M4A-P025-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: BDNF guides neural stem cell-derived axons to ventral interneurons and motor neurons after spinal cord injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M4A-P025-E002", "paper_tracker_id": "M4A-P025", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M4B-T002", "tracker_id": "M4B-O080"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P025::M4A-P025-E002'
    AND et.evidence_type_name = 'Neural graft intervention'
    AND ot.outcome_type_name = 'Second abstract-level experiment row isolates the primary mechanistic endpoint for BDNF axon guidance: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O080', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Manley NC 2017 M4A-P027-E002 preserves a distinct Rat cervical SCI / clinical-enabling experiment testing Mechanistic outcome assessment after hESC-derived oligodendrocyte progenitor cells transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for OPC remyelination: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'qualitative',
    'Manley NC 2017 M4A-P027-E002 preserves a distinct Rat cervical SCI / clinical-enabling experiment testing Mechanistic outcome assessment after hESC-derived oligodendrocyte progenitor cells transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for OPC remyelination: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'M4A-P027-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Human Embryonic Stem Cell-Derived Oligodendrocyte Progenitor Cells: Preclinical Efficacy and Safety in Cervical Spinal Cord Injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M4A-P027-E002", "paper_tracker_id": "M4A-P027", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M4B-T004", "tracker_id": "M4B-O081"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P027::M4A-P027-E002'
    AND et.evidence_type_name = 'Glial-lineage intervention'
    AND ot.outcome_type_name = 'Second abstract-level experiment row isolates the primary mechanistic endpoint for OPC remyelination: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O081', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Luo Z 2025 M4A-P028-E002 preserves a distinct Chronic compressive cervical SCI experiment testing Mechanistic outcome assessment after Oligodendrogenic neural progenitors transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for oligodendrogenic progenitors: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'qualitative',
    'Luo Z 2025 M4A-P028-E002 preserves a distinct Chronic compressive cervical SCI experiment testing Mechanistic outcome assessment after Oligodendrogenic neural progenitors transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for oligodendrogenic progenitors: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'M4A-P028-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Oligodendrogenic neural progenitors for treatment of chronic compressive cervical spinal cord injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M4A-P028-E002", "paper_tracker_id": "M4A-P028", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M4B-T004", "tracker_id": "M4B-O082"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P028::M4A-P028-E002'
    AND et.evidence_type_name = 'Glial-lineage intervention'
    AND ot.outcome_type_name = 'Second abstract-level experiment row isolates the primary mechanistic endpoint for oligodendrogenic progenitors: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O082', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Ren J 2026 M4A-P030-E002 preserves a distinct SCI repair platform experiment testing Mechanistic outcome assessment after Cryopreserved neural stem cells transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for NSC manufacturing: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'qualitative',
    'Ren J 2026 M4A-P030-E002 preserves a distinct SCI repair platform experiment testing Mechanistic outcome assessment after Cryopreserved neural stem cells transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for NSC manufacturing: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'M4A-P030-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Integrated cryopreservation-thawing-transplantation platform for neural stem cell-based spinal cord injury repair.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M4A-P030-E002", "paper_tracker_id": "M4A-P030", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M4B-T002", "tracker_id": "M4B-O083"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P030::M4A-P030-E002'
    AND et.evidence_type_name = 'Neural graft intervention'
    AND ot.outcome_type_name = 'Second abstract-level experiment row isolates the primary mechanistic endpoint for NSC manufacturing: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O083', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Qu W 2025 M4A-P031-E002 preserves a distinct Acute/chronic SCI models experiment testing Mechanistic outcome assessment after Schwann cells + chondroitinase ABC transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for Schwann chABC: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'qualitative',
    'Qu W 2025 M4A-P031-E002 preserves a distinct Acute/chronic SCI models experiment testing Mechanistic outcome assessment after Schwann cells + chondroitinase ABC transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for Schwann chABC: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'M4A-P031-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Chondroitinase ABC combined with Schwann cell transplantation enhances restoration of neural connection and functional recovery following acute and chronic spinal cord injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M4A-P031-E002", "paper_tracker_id": "M4A-P031", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M4B-T004", "tracker_id": "M4B-O084"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P031::M4A-P031-E002'
    AND et.evidence_type_name = 'Glial-lineage intervention'
    AND ot.outcome_type_name = 'Second abstract-level experiment row isolates the primary mechanistic endpoint for Schwann chABC: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O084', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Du X 2024 M4A-P032-E002 preserves a distinct Rat transection SCI experiment testing Mechanistic outcome assessment after GDNF-overexpressing Schwann cells transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for Schwann GDNF pathway: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'qualitative',
    'Du X 2024 M4A-P032-E002 preserves a distinct Rat transection SCI experiment testing Mechanistic outcome assessment after GDNF-overexpressing Schwann cells transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for Schwann GDNF pathway: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'M4A-P032-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Regeneration of Propriospinal Axons in Rat Transected Spinal Cord Injury through a Growth-Promoting Pathway Constructed by Schwann Cells Overexpressing GDNF.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M4A-P032-E002", "paper_tracker_id": "M4A-P032", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M4B-T004", "tracker_id": "M4B-O085"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P032::M4A-P032-E002'
    AND et.evidence_type_name = 'Glial-lineage intervention'
    AND ot.outcome_type_name = 'Second abstract-level experiment row isolates the primary mechanistic endpoint for Schwann GDNF pathway: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O085', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Hu JG 2013 M4A-P033-E002 preserves a distinct Rat SCI experiment testing Mechanistic outcome assessment after Glial restricted precursor + Schwann cells transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for GRP Schwann combination: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'qualitative',
    'Hu JG 2013 M4A-P033-E002 preserves a distinct Rat SCI experiment testing Mechanistic outcome assessment after Glial restricted precursor + Schwann cells transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for GRP Schwann combination: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'M4A-P033-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Cotransplantation of glial restricted precursor cells and Schwann cells promotes functional recovery after spinal cord injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M4A-P033-E002", "paper_tracker_id": "M4A-P033", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M4B-T004", "tracker_id": "M4B-O086"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P033::M4A-P033-E002'
    AND et.evidence_type_name = 'Glial-lineage intervention'
    AND ot.outcome_type_name = 'Second abstract-level experiment row isolates the primary mechanistic endpoint for GRP Schwann combination: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O086', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Dugan EA 2015 M4A-P034-E002 preserves a distinct Rat SCI experiment testing Mechanistic outcome assessment after Neural + glial restricted precursors + quipazine transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for NRP GRP quipazine: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'qualitative',
    'Dugan EA 2015 M4A-P034-E002 preserves a distinct Rat SCI experiment testing Mechanistic outcome assessment after Neural + glial restricted precursors + quipazine transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for NRP GRP quipazine: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'M4A-P034-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: A combination therapy of neural and glial restricted precursor cells and chronic quipazine treatment paired with passive cycling promotes quipazine-induced stepping in adult spinalized rats.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M4A-P034-E002", "paper_tracker_id": "M4A-P034", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M4B-T004", "tracker_id": "M4B-O087"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P034::M4A-P034-E002'
    AND et.evidence_type_name = 'Glial-lineage intervention'
    AND ot.outcome_type_name = 'Second abstract-level experiment row isolates the primary mechanistic endpoint for NRP GRP quipazine: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O087', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Mitsui T 2005 M4A-P035-E002 preserves a distinct Rat contusion SCI experiment testing Mechanistic outcome assessment after Neuronal and glial restricted precursors transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for NRP/GRP contusion circuitry: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'qualitative',
    'Mitsui T 2005 M4A-P035-E002 preserves a distinct Rat contusion SCI experiment testing Mechanistic outcome assessment after Neuronal and glial restricted precursors transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for NRP/GRP contusion circuitry: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'M4A-P035-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Transplantation of neuronal and glial restricted precursors into contused spinal cord improves bladder and motor functions, decreases thermal hypersensitivity, and modifies intraspinal circuitry.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M4A-P035-E002", "paper_tracker_id": "M4A-P035", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M4B-T004", "tracker_id": "M4B-O088"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P035::M4A-P035-E002'
    AND et.evidence_type_name = 'Glial-lineage intervention'
    AND ot.outcome_type_name = 'Second abstract-level experiment row isolates the primary mechanistic endpoint for NRP/GRP contusion circuitry: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O088', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Zhang L 2024 M4A-P036-E002 preserves a distinct Rodent SCI experiment testing Mechanistic outcome assessment after Olfactory ensheathing cells transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for OEC immunomodulation: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'qualitative',
    'Zhang L 2024 M4A-P036-E002 preserves a distinct Rodent SCI experiment testing Mechanistic outcome assessment after Olfactory ensheathing cells transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for OEC immunomodulation: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'M4A-P036-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Olfactory Ensheathing Cell Ameliorate Neuroinflammation Following Spinal Cord Injury Through Upregulating REV-ERB\u03b1 in Microglia.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M4A-P036-E002", "paper_tracker_id": "M4A-P036", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M4B-T005", "tracker_id": "M4B-O089"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P036::M4A-P036-E002'
    AND et.evidence_type_name = 'Trophic or immunomodulatory cell intervention'
    AND ot.outcome_type_name = 'Second abstract-level experiment row isolates the primary mechanistic endpoint for OEC immunomodulation: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O089', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Wang Y 2022 M4A-P037-E002 preserves a distinct Rodent SCI experiment testing Mechanistic outcome assessment after Olfactory ensheathing cells transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for OEC inflammation: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'qualitative',
    'Wang Y 2022 M4A-P037-E002 preserves a distinct Rodent SCI experiment testing Mechanistic outcome assessment after Olfactory ensheathing cells transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for OEC inflammation: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'M4A-P037-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Transplantation of olfactory ensheathing cells decreases local and serological monocyte chemoattractant protein 1 level during the acute phase of rat spinal cord injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M4A-P037-E002", "paper_tracker_id": "M4A-P037", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M4B-T005", "tracker_id": "M4B-O090"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P037::M4A-P037-E002'
    AND et.evidence_type_name = 'Trophic or immunomodulatory cell intervention'
    AND ot.outcome_type_name = 'Second abstract-level experiment row isolates the primary mechanistic endpoint for OEC inflammation: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O090', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Li W 2025 M4A-P038-E002 preserves a distinct Rodent SCI experiment testing Mechanistic outcome assessment after Olfactory mucosal MSCs + gelatin sponge transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for olfactory mucosal MSC scaffold: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'qualitative',
    'Li W 2025 M4A-P038-E002 preserves a distinct Rodent SCI experiment testing Mechanistic outcome assessment after Olfactory mucosal MSCs + gelatin sponge transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for olfactory mucosal MSC scaffold: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'M4A-P038-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Olfactory mucosal mesenchymal stem cells delivered by gelatin sponge scaffolds promote functional recovery of spinal cord injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M4A-P038-E002", "paper_tracker_id": "M4A-P038", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M4B-T005", "tracker_id": "M4B-O091"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P038::M4A-P038-E002'
    AND et.evidence_type_name = 'Trophic or immunomodulatory cell intervention'
    AND ot.outcome_type_name = 'Second abstract-level experiment row isolates the primary mechanistic endpoint for olfactory mucosal MSC scaffold: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O091', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Zhao Y 2024 M4A-P039-E002 preserves a distinct Rodent SCI experiment testing Mechanistic outcome assessment after hUC-MSC cell sheets transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for MSC cell sheet: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'qualitative',
    'Zhao Y 2024 M4A-P039-E002 preserves a distinct Rodent SCI experiment testing Mechanistic outcome assessment after hUC-MSC cell sheets transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for MSC cell sheet: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'M4A-P039-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Cell Sheets Formation Enhances Therapeutic Effects of Human Umbilical Cord Mesenchymal Stem Cells on Spinal Cord Injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M4A-P039-E002", "paper_tracker_id": "M4A-P039", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M4B-T005", "tracker_id": "M4B-O092"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P039::M4A-P039-E002'
    AND et.evidence_type_name = 'Trophic or immunomodulatory cell intervention'
    AND ot.outcome_type_name = 'Second abstract-level experiment row isolates the primary mechanistic endpoint for MSC cell sheet: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O092', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Yang L 2024 M4A-P040-E002 preserves a distinct Rodent SCI experiment testing Mechanistic outcome assessment after MSC scaffold / IL-10 response transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for MSC IL-10 scaffold: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'qualitative',
    'Yang L 2024 M4A-P040-E002 preserves a distinct Rodent SCI experiment testing Mechanistic outcome assessment after MSC scaffold / IL-10 response transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for MSC IL-10 scaffold: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'M4A-P040-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Initial IL-10 production dominates the therapy of mesenchymal stem cell scaffold in spinal cord injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M4A-P040-E002", "paper_tracker_id": "M4A-P040", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M4B-T005", "tracker_id": "M4B-O093"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P040::M4A-P040-E002'
    AND et.evidence_type_name = 'Trophic or immunomodulatory cell intervention'
    AND ot.outcome_type_name = 'Second abstract-level experiment row isolates the primary mechanistic endpoint for MSC IL-10 scaffold: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O093', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Liu D 2023 M4A-P041-E002 preserves a distinct Rodent SCI experiment testing Mechanistic outcome assessment after NSCs + ROS-scavenging hydrogel transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for NSC hydrogel microenvironment: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'qualitative',
    'Liu D 2023 M4A-P041-E002 preserves a distinct Rodent SCI experiment testing Mechanistic outcome assessment after NSCs + ROS-scavenging hydrogel transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for NSC hydrogel microenvironment: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'M4A-P041-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: ROS-Scavenging Hydrogels Synergize with Neural Stem Cells to Enhance Spinal Cord Injury Repair via Regulating Microenvironment and Facilitating Nerve Regeneration.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M4A-P041-E002", "paper_tracker_id": "M4A-P041", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M4B-T006", "tracker_id": "M4B-O094"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P041::M4A-P041-E002'
    AND et.evidence_type_name = 'Combination scaffold-cell intervention'
    AND ot.outcome_type_name = 'Second abstract-level experiment row isolates the primary mechanistic endpoint for NSC hydrogel microenvironment: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O094', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'He W 2023 M4A-P042-E002 preserves a distinct Rodent SCI experiment testing Mechanistic outcome assessment after bFGF-overexpressing hUC-MSC + dSCM scaffold transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for engineered MSC scaffold: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'qualitative',
    'He W 2023 M4A-P042-E002 preserves a distinct Rodent SCI experiment testing Mechanistic outcome assessment after bFGF-overexpressing hUC-MSC + dSCM scaffold transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for engineered MSC scaffold: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'M4A-P042-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Spinal cord decellularized matrix scaffold loaded with engineered basic fibroblast growth factor-overexpressed human umbilical cord mesenchymal stromal cells promoted the recovery of spinal cord injury.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M4A-P042-E002", "paper_tracker_id": "M4A-P042", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M4B-T005", "tracker_id": "M4B-O095"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P042::M4A-P042-E002'
    AND et.evidence_type_name = 'Trophic or immunomodulatory cell intervention'
    AND ot.outcome_type_name = 'Second abstract-level experiment row isolates the primary mechanistic endpoint for engineered MSC scaffold: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O095', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Li X 2025 M4A-P043-E002 preserves a distinct Complete transection defect experiment testing Mechanistic outcome assessment after NSC-laden microfibers + UC-MSC exosomes transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for NSC exosome microfiber: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'qualitative',
    'Li X 2025 M4A-P043-E002 preserves a distinct Complete transection defect experiment testing Mechanistic outcome assessment after NSC-laden microfibers + UC-MSC exosomes transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for NSC exosome microfiber: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'M4A-P043-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Conjugated therapy with coaxially printed neural stem cell-laden microfibers and umbilical cord mesenchymal stem cell derived exosomes on complete transactional spinal cord defects.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M4A-P043-E002", "paper_tracker_id": "M4A-P043", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M4B-T006", "tracker_id": "M4B-O096"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P043::M4A-P043-E002'
    AND et.evidence_type_name = 'Combination scaffold-cell intervention'
    AND ot.outcome_type_name = 'Second abstract-level experiment row isolates the primary mechanistic endpoint for NSC exosome microfiber: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O096', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Kao Y 2025 M4A-P044-E002 preserves a distinct Rodent SCI experiment testing Mechanistic outcome assessment after hMSC + HA hydrogel/polydopamine nanoparticles transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for MSC hydrogel nanoparticle: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'qualitative',
    'Kao Y 2025 M4A-P044-E002 preserves a distinct Rodent SCI experiment testing Mechanistic outcome assessment after hMSC + HA hydrogel/polydopamine nanoparticles transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for MSC hydrogel nanoparticle: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'M4A-P044-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Synergistic restoration of spinal cord injury through hyaluronic acid conjugated hydrogel-polydopamine nanoparticles combined with human mesenchymal stem cell transplantation.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M4A-P044-E002", "paper_tracker_id": "M4A-P044", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M4B-T006", "tracker_id": "M4B-O097"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P044::M4A-P044-E002'
    AND et.evidence_type_name = 'Combination scaffold-cell intervention'
    AND ot.outcome_type_name = 'Second abstract-level experiment row isolates the primary mechanistic endpoint for MSC hydrogel nanoparticle: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O097', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Liu D 2025 M4A-P045-E002 preserves a distinct Rodent SCI experiment testing Mechanistic outcome assessment after NSC + NO-releasing cerium oxide hydrogel transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for NSC NO hydrogel: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'qualitative',
    'Liu D 2025 M4A-P045-E002 preserves a distinct Rodent SCI experiment testing Mechanistic outcome assessment after NSC + NO-releasing cerium oxide hydrogel transplantation with endpoint/readout: Second abstract-level experiment row isolates the primary mechanistic endpoint for NSC NO hydrogel: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout..',
    'M4A-P045-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract / PubMed metadata',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Nitric Oxide-Releasing Mesoporous Hollow Cerium Oxide Nanozyme-Based Hydrogel Synergizes with Neural Stem Cell for Spinal Cord Injury Repair.. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M4A-P045-E002", "paper_tracker_id": "M4A-P045", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M4B-T006", "tracker_id": "M4B-O098"}'
  FROM _m4_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M4A-P045::M4A-P045-E002'
    AND et.evidence_type_name = 'Combination scaffold-cell intervention'
    AND ot.outcome_type_name = 'Second abstract-level experiment row isolates the primary mechanistic endpoint for NSC NO hydrogel: host-graft connectivity, differentiation, immunomodulation, remyelination, microenvironment conditioning, or functional readout.'
  RETURNING observation_id
)
INSERT INTO _m4_observation_map (tracker_id, observation_id) SELECT 'M4B-O098', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Human spinal-cord-derived neural stem cell transplantation has phase I chronic cervical and thoracic safety evidence but remains feasibility-grade rather than efficacy-grade.',
    'boundary condition',
    'high',
    'Module 4A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass author-claim abstraction; full text needed for paper-specific wording.", "source_paper_tracker_id": "M4A-P004-M4A-P005", "topic_id": "M4B-T001", "tracker_id": "M4B-C001"}'
  FROM _m4_paper_map p
  WHERE p.tracker_id = 'M4A-P004'
  RETURNING claim_id
)
INSERT INTO _m4_claim_map (tracker_id, claim_id) SELECT 'M4B-C001', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Autologous Schwann-cell transplantation has human subacute and chronic safety anchors, but clinical functional efficacy remains unsettled.',
    'boundary condition',
    'high',
    'Module 4A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass author-claim abstraction; full text needed for paper-specific wording.", "source_paper_tracker_id": "M4A-P006,M4A-P053", "topic_id": "M4B-T001", "tracker_id": "M4B-C002"}'
  FROM _m4_paper_map p
  WHERE p.tracker_id = 'M4A-P006'
  RETURNING claim_id
)
INSERT INTO _m4_claim_map (tracker_id, claim_id) SELECT 'M4B-C002', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'MSC, OEC, BMMC, UCB, and mixed-cell clinical studies mainly support safety and feasibility across small cohorts and heterogeneous routes.',
    'synthesis',
    'medium',
    'Module 4A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass author-claim abstraction; full text needed for paper-specific wording.", "source_paper_tracker_id": "M4A-P007-M4A-P010,M4A-P055-M4A-P060", "topic_id": "M4B-T001", "tracker_id": "M4B-C003"}'
  FROM _m4_paper_map p
  WHERE p.tracker_id = 'M4A-P007'
  RETURNING claim_id
)
INSERT INTO _m4_claim_map (tracker_id, claim_id) SELECT 'M4B-C003', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'NeuroRegen scaffold plus cell transplantation is a recurring human clinical strategy, but scaffold, scar resection, and cell effects are inseparable at first pass.',
    'boundary condition',
    'high',
    'Module 4A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass author-claim abstraction; full text needed for paper-specific wording.", "source_paper_tracker_id": "M4A-P002,M4A-P010", "topic_id": "M4B-T001", "tracker_id": "M4B-C004"}'
  FROM _m4_paper_map p
  WHERE p.tracker_id = 'M4A-P002'
  RETURNING claim_id
)
INSERT INTO _m4_claim_map (tracker_id, claim_id) SELECT 'M4B-C004', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Non-human primate NS/PC transplantation provides an important translational bridge between rodent neural graft experiments and human trials.',
    'implication',
    'medium',
    'Module 4A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass author-claim abstraction; full text needed for paper-specific wording.", "source_paper_tracker_id": "M4A-P011-M4A-P012", "topic_id": "M4B-T002", "tracker_id": "M4B-C005"}'
  FROM _m4_paper_map p
  WHERE p.tracker_id = 'M4A-P011'
  RETURNING claim_id
)
INSERT INTO _m4_claim_map (tracker_id, claim_id) SELECT 'M4B-C005', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Neural grafts can be evaluated for synaptic integration and host-graft connectivity rather than only graft survival or lesion filling.',
    'conclusion',
    'medium',
    'Module 4A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass author-claim abstraction; full text needed for paper-specific wording.", "source_paper_tracker_id": "M4A-P013-M4A-P017", "topic_id": "M4B-T002", "tracker_id": "M4B-C006"}'
  FROM _m4_paper_map p
  WHERE p.tracker_id = 'M4A-P013'
  RETURNING claim_id
)
INSERT INTO _m4_claim_map (tracker_id, claim_id) SELECT 'M4B-C006', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Circuit-relay claims are strongest when tracing, synaptic mapping, or functional connectivity assays accompany behavioral endpoints.',
    'evidence standard',
    'high',
    'Module 4A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass author-claim abstraction; full text needed for paper-specific wording.", "source_paper_tracker_id": "M4A-P014-M4A-P016", "topic_id": "M4B-T002", "tracker_id": "M4B-C007"}'
  FROM _m4_paper_map p
  WHERE p.tracker_id = 'M4A-P014'
  RETURNING claim_id
)
INSERT INTO _m4_claim_map (tracker_id, claim_id) SELECT 'M4B-C007', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Human interneuron and organoid approaches extend graft replacement toward regionally specified circuit repair.',
    'implication',
    'medium',
    'Module 4A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass author-claim abstraction; full text needed for paper-specific wording.", "source_paper_tracker_id": "M4A-P017-M4A-P018", "topic_id": "M4B-T002", "tracker_id": "M4B-C008"}'
  FROM _m4_paper_map p
  WHERE p.tracker_id = 'M4A-P017'
  RETURNING claim_id
)
INSERT INTO _m4_claim_map (tracker_id, claim_id) SELECT 'M4B-C008', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Human iPSC-derived spinal progenitors can support sensorimotor recovery signals in immunodeficient or controlled rodent SCI models.',
    'conclusion',
    'medium',
    'Module 4A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass author-claim abstraction; full text needed for paper-specific wording.", "source_paper_tracker_id": "M4A-P019-M4A-P020", "topic_id": "M4B-T002", "tracker_id": "M4B-C009"}'
  FROM _m4_paper_map p
  WHERE p.tracker_id = 'M4A-P019'
  RETURNING claim_id
)
INSERT INTO _m4_claim_map (tracker_id, claim_id) SELECT 'M4B-C009', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Rehabilitation, synaptic organizers, and growth-factor pretreatment can amplify hiPSC-NS/PC graft effects but complicate attribution to cells alone.',
    'boundary condition',
    'high',
    'Module 4A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass author-claim abstraction; full text needed for paper-specific wording.", "source_paper_tracker_id": "M4A-P021-M4A-P023", "topic_id": "M4B-T002", "tracker_id": "M4B-C010"}'
  FROM _m4_paper_map p
  WHERE p.tracker_id = 'M4A-P021'
  RETURNING claim_id
)
INSERT INTO _m4_claim_map (tracker_id, claim_id) SELECT 'M4B-C010', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Cell source comparisons indicate that fetal, spinal, brain, ESC, and iPSC-derived NS/PCs should not be treated as one interchangeable product class.',
    'boundary condition',
    'high',
    'Module 4A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass author-claim abstraction; full text needed for paper-specific wording.", "source_paper_tracker_id": "M4A-P024", "topic_id": "M4B-T003", "tracker_id": "M4B-C011"}'
  FROM _m4_paper_map p
  WHERE p.tracker_id = 'M4A-P024'
  RETURNING claim_id
)
INSERT INTO _m4_claim_map (tracker_id, claim_id) SELECT 'M4B-C011', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Guidance cues such as BDNF can direct graft-derived axons toward host targets, supporting a directed-connectivity model of repair.',
    'mechanistic',
    'medium',
    'Module 4A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass author-claim abstraction; full text needed for paper-specific wording.", "source_paper_tracker_id": "M4A-P025", "topic_id": "M4B-T002", "tracker_id": "M4B-C012"}'
  FROM _m4_paper_map p
  WHERE p.tracker_id = 'M4A-P025'
  RETURNING claim_id
)
INSERT INTO _m4_claim_map (tracker_id, claim_id) SELECT 'M4B-C012', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Defined neuronal precursor identity and cryopreservation-thaw platforms are translationally relevant variables for scalable transplantation.',
    'implication',
    'medium',
    'Module 4A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass author-claim abstraction; full text needed for paper-specific wording.", "source_paper_tracker_id": "M4A-P026,M4A-P030", "topic_id": "M4B-T003", "tracker_id": "M4B-C013"}'
  FROM _m4_paper_map p
  WHERE p.tracker_id = 'M4A-P026'
  RETURNING claim_id
)
INSERT INTO _m4_claim_map (tracker_id, claim_id) SELECT 'M4B-C013', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'OPC transplantation evidence should be synthesized around remyelination and safety, not assumed to share neural relay mechanisms.',
    'boundary condition',
    'high',
    'Module 4A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass author-claim abstraction; full text needed for paper-specific wording.", "source_paper_tracker_id": "M4A-P027,M4A-P051,M4A-P052", "topic_id": "M4B-T004", "tracker_id": "M4B-C014"}'
  FROM _m4_paper_map p
  WHERE p.tracker_id = 'M4A-P027'
  RETURNING claim_id
)
INSERT INTO _m4_claim_map (tracker_id, claim_id) SELECT 'M4B-C014', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Oligodendrogenic neural progenitors add a chronic cervical repair subtype where glial lineage and compression context matter.',
    'implication',
    'medium',
    'Module 4A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass author-claim abstraction; full text needed for paper-specific wording.", "source_paper_tracker_id": "M4A-P028", "topic_id": "M4B-T004", "tracker_id": "M4B-C015"}'
  FROM _m4_paper_map p
  WHERE p.tracker_id = 'M4A-P028'
  RETURNING claim_id
)
INSERT INTO _m4_claim_map (tracker_id, claim_id) SELECT 'M4B-C015', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Schwann and glial-support strategies can promote axon growth, remyelination, or connectivity, especially when paired with permissive enzymes or trophic cues.',
    'synthesis',
    'medium',
    'Module 4A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass author-claim abstraction; full text needed for paper-specific wording.", "source_paper_tracker_id": "M4A-P031-M4A-P033,M4A-P059", "topic_id": "M4B-T004", "tracker_id": "M4B-C016"}'
  FROM _m4_paper_map p
  WHERE p.tracker_id = 'M4A-P031'
  RETURNING claim_id
)
INSERT INTO _m4_claim_map (tracker_id, claim_id) SELECT 'M4B-C016', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Restricted precursor grafts often combine with pharmacologic, cycling, bladder, or sensory endpoints, requiring endpoint-specific synthesis.',
    'boundary condition',
    'high',
    'Module 4A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass author-claim abstraction; full text needed for paper-specific wording.", "source_paper_tracker_id": "M4A-P034-M4A-P035", "topic_id": "M4B-T004", "tracker_id": "M4B-C017"}'
  FROM _m4_paper_map p
  WHERE p.tracker_id = 'M4A-P034'
  RETURNING claim_id
)
INSERT INTO _m4_claim_map (tracker_id, claim_id) SELECT 'M4B-C017', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'OEC transplantation can modulate neuroinflammatory signals such as microglial state or MCP-1 after SCI.',
    'mechanistic',
    'medium',
    'Module 4A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass author-claim abstraction; full text needed for paper-specific wording.", "source_paper_tracker_id": "M4A-P036-M4A-P037", "topic_id": "M4B-T005", "tracker_id": "M4B-C018"}'
  FROM _m4_paper_map p
  WHERE p.tracker_id = 'M4A-P036'
  RETURNING claim_id
)
INSERT INTO _m4_claim_map (tracker_id, claim_id) SELECT 'M4B-C018', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'MSC-family interventions frequently act through scaffold delivery, cell-sheet format, or cytokine-mediated immunomodulation rather than neuronal replacement.',
    'synthesis',
    'medium',
    'Module 4A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass author-claim abstraction; full text needed for paper-specific wording.", "source_paper_tracker_id": "M4A-P038-M4A-P040", "topic_id": "M4B-T005", "tracker_id": "M4B-C019"}'
  FROM _m4_paper_map p
  WHERE p.tracker_id = 'M4A-P038'
  RETURNING claim_id
)
INSERT INTO _m4_claim_map (tracker_id, claim_id) SELECT 'M4B-C019', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Hydrogel, nanozyme, decellularized matrix, microfiber, exosome, and nanoparticle combinations can strengthen repair signals but limit single-component causal claims.',
    'boundary condition',
    'high',
    'Module 4A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass author-claim abstraction; full text needed for paper-specific wording.", "source_paper_tracker_id": "M4A-P041-M4A-P045", "topic_id": "M4B-T006", "tracker_id": "M4B-C020"}'
  FROM _m4_paper_map p
  WHERE p.tracker_id = 'M4A-P041'
  RETURNING claim_id
)
INSERT INTO _m4_claim_map (tracker_id, claim_id) SELECT 'M4B-C020', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Chronic scar or lesion microenvironment modification can make grafting more permissive, linking Module 4 evidence back to lesion-architecture findings.',
    'implication',
    'medium',
    'Module 4A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass author-claim abstraction; full text needed for paper-specific wording.", "source_paper_tracker_id": "M4A-P001,M4A-P003", "topic_id": "M4B-T006", "tracker_id": "M4B-C021"}'
  FROM _m4_paper_map p
  WHERE p.tracker_id = 'M4A-P001'
  RETURNING claim_id
)
INSERT INTO _m4_claim_map (tracker_id, claim_id) SELECT 'M4B-C021', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Fetal and embryonic graft studies remain important for circuit and respiratory recovery concepts but carry source, ethics, and translation boundaries.',
    'boundary condition',
    'high',
    'Module 4A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass author-claim abstraction; full text needed for paper-specific wording.", "source_paper_tracker_id": "M4A-P046-M4A-P050", "topic_id": "M4B-T007", "tracker_id": "M4B-C022"}'
  FROM _m4_paper_map p
  WHERE p.tracker_id = 'M4A-P046'
  RETURNING claim_id
)
INSERT INTO _m4_claim_map (tracker_id, claim_id) SELECT 'M4B-C022', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Autonomic, bladder, pain, respiratory, and cardiovascular outcomes are meaningful transplantation endpoints separate from locomotor recovery.',
    'evidence standard',
    'high',
    'Module 4A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass author-claim abstraction; full text needed for paper-specific wording.", "source_paper_tracker_id": "M4A-P050,M4A-P054-M4A-P056", "topic_id": "M4B-T007", "tracker_id": "M4B-C023"}'
  FROM _m4_paper_map p
  WHERE p.tracker_id = 'M4A-P050'
  RETURNING claim_id
)
INSERT INTO _m4_claim_map (tracker_id, claim_id) SELECT 'M4B-C023', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Clinical feasibility signals should not be promoted to efficacy consensus without controlled endpoints, adverse-event detail, and durability review.',
    'boundary condition',
    'high',
    'Module 4A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass author-claim abstraction; full text needed for paper-specific wording.", "source_paper_tracker_id": "M4A-P004-M4A-P060", "topic_id": "M4B-T008", "tracker_id": "M4B-C024"}'
  FROM _m4_paper_map p
  WHERE p.tracker_id = 'M4A-P004'
  RETURNING claim_id
)
INSERT INTO _m4_claim_map (tracker_id, claim_id) SELECT 'M4B-C024', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Species context strongly shapes interpretation because rodent, primate, and human SCI transplantation studies test different immunologic and scale constraints.',
    'boundary condition',
    'high',
    'Module 4A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass author-claim abstraction; full text needed for paper-specific wording.", "source_paper_tracker_id": "M4A-P011-M4A-P060", "topic_id": "M4B-T008", "tracker_id": "M4B-C025"}'
  FROM _m4_paper_map p
  WHERE p.tracker_id = 'M4A-P011'
  RETURNING claim_id
)
INSERT INTO _m4_claim_map (tracker_id, claim_id) SELECT 'M4B-C025', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Immunodeficient host models and xenograft settings support mechanism discovery but require caution for immune-competent translation.',
    'boundary condition',
    'high',
    'Module 4A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass author-claim abstraction; full text needed for paper-specific wording.", "source_paper_tracker_id": "M4A-P019-M4A-P026", "topic_id": "M4B-T008", "tracker_id": "M4B-C026"}'
  FROM _m4_paper_map p
  WHERE p.tracker_id = 'M4A-P019'
  RETURNING claim_id
)
INSERT INTO _m4_claim_map (tracker_id, claim_id) SELECT 'M4B-C026', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Graft survival or differentiation alone is not enough for circuit-restoration claims; connectivity and functional assay alignment matter.',
    'evidence standard',
    'high',
    'Module 4A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass author-claim abstraction; full text needed for paper-specific wording.", "source_paper_tracker_id": "M4A-P013-M4A-P017", "topic_id": "M4B-T008", "tracker_id": "M4B-C027"}'
  FROM _m4_paper_map p
  WHERE p.tracker_id = 'M4A-P013'
  RETURNING claim_id
)
INSERT INTO _m4_claim_map (tracker_id, claim_id) SELECT 'M4B-C027', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Remyelination, axon support, relay formation, and immunomodulation are different mechanisms that should not be merged into a generic cell-therapy label.',
    'boundary condition',
    'high',
    'Module 4A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass author-claim abstraction; full text needed for paper-specific wording.", "source_paper_tracker_id": "M4A-P027-M4A-P035", "topic_id": "M4B-T008", "tracker_id": "M4B-C028"}'
  FROM _m4_paper_map p
  WHERE p.tracker_id = 'M4A-P027'
  RETURNING claim_id
)
INSERT INTO _m4_claim_map (tracker_id, claim_id) SELECT 'M4B-C028', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Combination therapies should be tagged as multi-component interventions unless comparator design isolates the cell, scaffold, cargo, or stimulation component.',
    'evidence standard',
    'high',
    'Module 4A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass author-claim abstraction; full text needed for paper-specific wording.", "source_paper_tracker_id": "M4A-P041-M4A-P045", "topic_id": "M4B-T006", "tracker_id": "M4B-C029"}'
  FROM _m4_paper_map p
  WHERE p.tracker_id = 'M4A-P041'
  RETURNING claim_id
)
INSERT INTO _m4_claim_map (tracker_id, claim_id) SELECT 'M4B-C029', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Human cell-transplant studies span chronic, subacute, acute, complete, and cervical/thoracic contexts, so clinical consensus requires stage- and injury-level stratification.',
    'boundary condition',
    'high',
    'Module 4A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass author-claim abstraction; full text needed for paper-specific wording.", "source_paper_tracker_id": "M4A-P004-M4A-P010,M4A-P048-M4A-P060", "topic_id": "M4B-T001", "tracker_id": "M4B-C030"}'
  FROM _m4_paper_map p
  WHERE p.tracker_id = 'M4A-P004'
  RETURNING claim_id
)
INSERT INTO _m4_claim_map (tracker_id, claim_id) SELECT 'M4B-C030', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Activity, rehabilitation, or stimulation can convert grafts into activity-dependent repair platforms rather than passive implants.',
    'implication',
    'medium',
    'Module 4A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass author-claim abstraction; full text needed for paper-specific wording.", "source_paper_tracker_id": "M4A-P021,M4A-P046", "topic_id": "M4B-T002", "tracker_id": "M4B-C031"}'
  FROM _m4_paper_map p
  WHERE p.tracker_id = 'M4A-P021'
  RETURNING claim_id
)
INSERT INTO _m4_claim_map (tracker_id, claim_id) SELECT 'M4B-C031', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Chondroitinase, GDNF, and other permissive modifiers can make Schwann-cell grafts stronger axon-growth platforms but blur cell-only effects.',
    'boundary condition',
    'high',
    'Module 4A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass author-claim abstraction; full text needed for paper-specific wording.", "source_paper_tracker_id": "M4A-P031-M4A-P032", "topic_id": "M4B-T004", "tracker_id": "M4B-C032"}'
  FROM _m4_paper_map p
  WHERE p.tracker_id = 'M4A-P031'
  RETURNING claim_id
)
INSERT INTO _m4_claim_map (tracker_id, claim_id) SELECT 'M4B-C032', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'OEC evidence spans inflammatory mechanisms and human mucosal/autologous feasibility, but the product class is heterogeneous.',
    'boundary condition',
    'high',
    'Module 4A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass author-claim abstraction; full text needed for paper-specific wording.", "source_paper_tracker_id": "M4A-P009,M4A-P036-M4A-P037,M4A-P057-M4A-P058", "topic_id": "M4B-T005", "tracker_id": "M4B-C033"}'
  FROM _m4_paper_map p
  WHERE p.tracker_id = 'M4A-P009'
  RETURNING claim_id
)
INSERT INTO _m4_claim_map (tracker_id, claim_id) SELECT 'M4B-C033', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'MSC-family products should be curated as stromal or trophic interventions unless direct neural differentiation is demonstrated.',
    'evidence standard',
    'high',
    'Module 4A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass author-claim abstraction; full text needed for paper-specific wording.", "source_paper_tracker_id": "M4A-P007-M4A-P008,M4A-P038-M4A-P040", "topic_id": "M4B-T005", "tracker_id": "M4B-C034"}'
  FROM _m4_paper_map p
  WHERE p.tracker_id = 'M4A-P007'
  RETURNING claim_id
)
INSERT INTO _m4_claim_map (tracker_id, claim_id) SELECT 'M4B-C034', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Cryopreservation and thaw-to-transplant platforms should be captured because logistics can determine whether promising grafts are clinically usable.',
    'implication',
    'high',
    'Module 4A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass author-claim abstraction; full text needed for paper-specific wording.", "source_paper_tracker_id": "M4A-P030", "topic_id": "M4B-T003", "tracker_id": "M4B-C035"}'
  FROM _m4_paper_map p
  WHERE p.tracker_id = 'M4A-P030'
  RETURNING claim_id
)
INSERT INTO _m4_claim_map (tracker_id, claim_id) SELECT 'M4B-C035', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Scaffold-cell studies are especially relevant to chronic complete SCI but are also the highest-risk area for over-attribution.',
    'boundary condition',
    'high',
    'Module 4A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass author-claim abstraction; full text needed for paper-specific wording.", "source_paper_tracker_id": "M4A-P002-M4A-P003,M4A-P041-M4A-P045", "topic_id": "M4B-T006", "tracker_id": "M4B-C036"}'
  FROM _m4_paper_map p
  WHERE p.tracker_id = 'M4A-P002'
  RETURNING claim_id
)
INSERT INTO _m4_claim_map (tracker_id, claim_id) SELECT 'M4B-C036', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Respiratory and cardiovascular regulation studies show that transplantation may repair specific circuits without broad motor restoration.',
    'boundary condition',
    'high',
    'Module 4A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass author-claim abstraction; full text needed for paper-specific wording.", "source_paper_tracker_id": "M4A-P050,M4A-P054", "topic_id": "M4B-T007", "tracker_id": "M4B-C037"}'
  FROM _m4_paper_map p
  WHERE p.tracker_id = 'M4A-P050'
  RETURNING claim_id
)
INSERT INTO _m4_claim_map (tracker_id, claim_id) SELECT 'M4B-C037', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Module 4 synthesis should stratify by cell source, lesion stage, species, delivery context, and endpoint before any pooled conclusion.',
    'synthesis rule',
    'high',
    'Module 4A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass author-claim abstraction; full text needed for paper-specific wording.", "source_paper_tracker_id": "M4A-P001-M4A-P060", "topic_id": "M4B-T008", "tracker_id": "M4B-C038"}'
  FROM _m4_paper_map p
  WHERE p.tracker_id = 'M4A-P001'
  RETURNING claim_id
)
INSERT INTO _m4_claim_map (tracker_id, claim_id) SELECT 'M4B-C038', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Most Module 4B rows are abstract-level first pass, so full-text upgrades are needed before quantitative effect-size consensus.',
    'curation boundary',
    'high',
    'Module 4A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass author-claim abstraction; full text needed for paper-specific wording.", "source_paper_tracker_id": "M4A-P001-M4A-P060", "topic_id": "M4B-T008", "tracker_id": "M4B-C039"}'
  FROM _m4_paper_map p
  WHERE p.tracker_id = 'M4A-P001'
  RETURNING claim_id
)
INSERT INTO _m4_claim_map (tracker_id, claim_id) SELECT 'M4B-C039', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'The current corpus supports several consensus-ready qualitative profiles but not a single universal claim that transplantation works after SCI.',
    'synthesis',
    'high',
    'Module 4A tracker / abstract metadata',
    'medium',
    '{"curator_notes": "First-pass author-claim abstraction; full text needed for paper-specific wording.", "source_paper_tracker_id": "M4A-P001-M4A-P060", "topic_id": "M4B-T008", "tracker_id": "M4B-C040"}'
  FROM _m4_paper_map p
  WHERE p.tracker_id = 'M4A-P001'
  RETURNING claim_id
)
INSERT INTO _m4_claim_map (tracker_id, claim_id) SELECT 'M4B-C040', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M4B-L001"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O004'
  WHERE c.tracker_id = 'M4B-C001'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L001', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M4B-L002"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O006'
  WHERE c.tracker_id = 'M4B-C002'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L002', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M4B-L003"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O007'
  WHERE c.tracker_id = 'M4B-C003'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L003', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M4B-L004"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O002'
  WHERE c.tracker_id = 'M4B-C004'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L004', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M4B-L005"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O011'
  WHERE c.tracker_id = 'M4B-C005'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L005', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M4B-L006"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O013'
  WHERE c.tracker_id = 'M4B-C006'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L006', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M4B-L007"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O014'
  WHERE c.tracker_id = 'M4B-C007'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L007', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M4B-L008"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O017'
  WHERE c.tracker_id = 'M4B-C008'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L008', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M4B-L009"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O019'
  WHERE c.tracker_id = 'M4B-C009'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L009', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M4B-L010"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O021'
  WHERE c.tracker_id = 'M4B-C010'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L010', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M4B-L011"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O024'
  WHERE c.tracker_id = 'M4B-C011'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L011', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M4B-L012"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O025'
  WHERE c.tracker_id = 'M4B-C012'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L012', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M4B-L013"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O026'
  WHERE c.tracker_id = 'M4B-C013'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L013', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M4B-L014"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O027'
  WHERE c.tracker_id = 'M4B-C014'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L014', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M4B-L015"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O028'
  WHERE c.tracker_id = 'M4B-C015'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L015', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M4B-L016"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O031'
  WHERE c.tracker_id = 'M4B-C016'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L016', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M4B-L017"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O034'
  WHERE c.tracker_id = 'M4B-C017'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L017', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M4B-L018"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O036'
  WHERE c.tracker_id = 'M4B-C018'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L018', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M4B-L019"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O038'
  WHERE c.tracker_id = 'M4B-C019'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L019', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M4B-L020"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O041'
  WHERE c.tracker_id = 'M4B-C020'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L020', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M4B-L021"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O001'
  WHERE c.tracker_id = 'M4B-C021'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L021', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M4B-L022"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O046'
  WHERE c.tracker_id = 'M4B-C022'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L022', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M4B-L023"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O035'
  WHERE c.tracker_id = 'M4B-C023'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L023', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M4B-L024"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O004'
  WHERE c.tracker_id = 'M4B-C024'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L024', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M4B-L025"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O011'
  WHERE c.tracker_id = 'M4B-C025'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L025', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M4B-L026"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O019'
  WHERE c.tracker_id = 'M4B-C026'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L026', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M4B-L027"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O013'
  WHERE c.tracker_id = 'M4B-C027'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L027', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M4B-L028"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O027'
  WHERE c.tracker_id = 'M4B-C028'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L028', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M4B-L029"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O041'
  WHERE c.tracker_id = 'M4B-C029'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L029', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M4B-L030"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O004'
  WHERE c.tracker_id = 'M4B-C030'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L030', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M4B-L031"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O021'
  WHERE c.tracker_id = 'M4B-C031'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L031', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M4B-L032"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O031'
  WHERE c.tracker_id = 'M4B-C032'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L032', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M4B-L033"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O009'
  WHERE c.tracker_id = 'M4B-C033'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L033', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M4B-L034"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O007'
  WHERE c.tracker_id = 'M4B-C034'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L034', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M4B-L035"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O030'
  WHERE c.tracker_id = 'M4B-C035'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L035', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M4B-L036"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O002'
  WHERE c.tracker_id = 'M4B-C036'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L036', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M4B-L037"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O050'
  WHERE c.tracker_id = 'M4B-C037'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L037', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M4B-L038"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O001'
  WHERE c.tracker_id = 'M4B-C038'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L038', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M4B-L039"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O001'
  WHERE c.tracker_id = 'M4B-C039'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L039', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Primary supporting observation.", "strength": "medium", "tracker_id": "M4B-L040"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O004'
  WHERE c.tracker_id = 'M4B-C040'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L040', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M4B-L041"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O005'
  WHERE c.tracker_id = 'M4B-C001'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L041', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M4B-L042"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O053'
  WHERE c.tracker_id = 'M4B-C002'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L042', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M4B-L043"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O008'
  WHERE c.tracker_id = 'M4B-C003'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L043', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M4B-L044"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O009'
  WHERE c.tracker_id = 'M4B-C003'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L044', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M4B-L045"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O055'
  WHERE c.tracker_id = 'M4B-C003'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L045', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M4B-L046"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O056'
  WHERE c.tracker_id = 'M4B-C003'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L046', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M4B-L047"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O057'
  WHERE c.tracker_id = 'M4B-C003'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L047', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M4B-L048"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O058'
  WHERE c.tracker_id = 'M4B-C003'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L048', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M4B-L049"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O060'
  WHERE c.tracker_id = 'M4B-C003'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L049', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M4B-L050"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O010'
  WHERE c.tracker_id = 'M4B-C004'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L050', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M4B-L051"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O012'
  WHERE c.tracker_id = 'M4B-C005'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L051', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M4B-L052"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O014'
  WHERE c.tracker_id = 'M4B-C006'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L052', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M4B-L053"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O015'
  WHERE c.tracker_id = 'M4B-C006'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L053', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M4B-L054"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O016'
  WHERE c.tracker_id = 'M4B-C006'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L054', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M4B-L055"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O017'
  WHERE c.tracker_id = 'M4B-C006'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L055', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M4B-L056"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O015'
  WHERE c.tracker_id = 'M4B-C007'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L056', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M4B-L057"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O016'
  WHERE c.tracker_id = 'M4B-C007'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L057', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M4B-L058"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O018'
  WHERE c.tracker_id = 'M4B-C008'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L058', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M4B-L059"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O020'
  WHERE c.tracker_id = 'M4B-C009'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L059', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M4B-L060"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O022'
  WHERE c.tracker_id = 'M4B-C010'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L060', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M4B-L061"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O023'
  WHERE c.tracker_id = 'M4B-C010'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L061', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M4B-L062"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O030'
  WHERE c.tracker_id = 'M4B-C013'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L062', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M4B-L063"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O051'
  WHERE c.tracker_id = 'M4B-C014'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L063', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M4B-L064"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O052'
  WHERE c.tracker_id = 'M4B-C014'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L064', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M4B-L065"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O032'
  WHERE c.tracker_id = 'M4B-C016'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L065', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M4B-L066"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O033'
  WHERE c.tracker_id = 'M4B-C016'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L066', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M4B-L067"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O059'
  WHERE c.tracker_id = 'M4B-C016'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L067', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M4B-L068"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O035'
  WHERE c.tracker_id = 'M4B-C017'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L068', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M4B-L069"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O037'
  WHERE c.tracker_id = 'M4B-C018'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L069', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M4B-L070"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O039'
  WHERE c.tracker_id = 'M4B-C019'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L070', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M4B-L071"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O040'
  WHERE c.tracker_id = 'M4B-C019'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L071', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'boundary support',
  '{"notes": "Additional corroborating or boundary observation.", "strength": "low", "tracker_id": "M4B-L072"}'
  FROM _m4_claim_map c
  JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O042'
  WHERE c.tracker_id = 'M4B-C020'
  RETURNING link_id
)
INSERT INTO _m4_link_map (tracker_id, link_id) SELECT 'M4B-L072', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Human SCI cell-transplantation studies most strongly support procedural feasibility, safety monitoring, and trial design lessons; efficacy claims should remain provisional unless linked to controlled functional, imaging, electrophysiologic, or histologic endpoints.',
    'M4B-T001',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M4B-B001", "M4B-B007", "M4B-B008"], "claim_tracker_ids": ["M4B-C001", "M4B-C002", "M4B-C003", "M4B-C004", "M4B-C024", "M4B-C030"], "consensus_draft_id": "M4B-S001", "observation_tracker_ids": ["M4B-O004", "M4B-O005", "M4B-O006", "M4B-O007", "M4B-O008", "M4B-O009", "M4B-O010", "M4B-O048", "M4B-O051", "M4B-O053", "M4B-O055", "M4B-O056", "M4B-O057", "M4B-O058", "M4B-O059", "M4B-O060"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "B001, B007, B008", "topic_id": "M4B-T001"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m4_consensus_map (tracker_id, consensus_id) SELECT 'M4B-S001', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O004'
WHERE c.tracker_id = 'M4B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O005'
WHERE c.tracker_id = 'M4B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O006'
WHERE c.tracker_id = 'M4B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O007'
WHERE c.tracker_id = 'M4B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O008'
WHERE c.tracker_id = 'M4B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O009'
WHERE c.tracker_id = 'M4B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O010'
WHERE c.tracker_id = 'M4B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O048'
WHERE c.tracker_id = 'M4B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O051'
WHERE c.tracker_id = 'M4B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O053'
WHERE c.tracker_id = 'M4B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O055'
WHERE c.tracker_id = 'M4B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O056'
WHERE c.tracker_id = 'M4B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O057'
WHERE c.tracker_id = 'M4B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O058'
WHERE c.tracker_id = 'M4B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O059'
WHERE c.tracker_id = 'M4B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O060'
WHERE c.tracker_id = 'M4B-S001';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Neural progenitor, iPSC, ESC, interneuron, and organoid-derived grafts provide the clearest mechanistic evidence for host-graft integration when survival, differentiation, synaptic connectivity, axon extension, and behavior are measured as separate outcomes.',
    'M4B-T002',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M4B-B002", "M4B-B005", "M4B-B008"], "claim_tracker_ids": ["M4B-C005", "M4B-C006", "M4B-C007", "M4B-C008", "M4B-C009", "M4B-C010", "M4B-C012", "M4B-C027", "M4B-C031"], "consensus_draft_id": "M4B-S002", "observation_tracker_ids": ["M4B-O011", "M4B-O012", "M4B-O013", "M4B-O014", "M4B-O015", "M4B-O016", "M4B-O017", "M4B-O018", "M4B-O019", "M4B-O020", "M4B-O021", "M4B-O022", "M4B-O023", "M4B-O024", "M4B-O025", "M4B-O026"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "B002, B005, B008", "topic_id": "M4B-T002"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m4_consensus_map (tracker_id, consensus_id) SELECT 'M4B-S002', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O011'
WHERE c.tracker_id = 'M4B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O012'
WHERE c.tracker_id = 'M4B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O013'
WHERE c.tracker_id = 'M4B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O014'
WHERE c.tracker_id = 'M4B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O015'
WHERE c.tracker_id = 'M4B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O016'
WHERE c.tracker_id = 'M4B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O017'
WHERE c.tracker_id = 'M4B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O018'
WHERE c.tracker_id = 'M4B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O019'
WHERE c.tracker_id = 'M4B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O020'
WHERE c.tracker_id = 'M4B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O021'
WHERE c.tracker_id = 'M4B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O022'
WHERE c.tracker_id = 'M4B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O023'
WHERE c.tracker_id = 'M4B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O024'
WHERE c.tracker_id = 'M4B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O025'
WHERE c.tracker_id = 'M4B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O026'
WHERE c.tracker_id = 'M4B-S002';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Cell identity, maturity, manufacturing route, purity, dose, and graft composition are core evidence fields for transplantation synthesis because nominally similar cell therapies can differ in mechanism, risk, and expected repair function.',
    'M4B-T003',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M4B-B003", "M4B-B008"], "claim_tracker_ids": ["M4B-C011", "M4B-C013", "M4B-C035", "M4B-C038"], "consensus_draft_id": "M4B-S003", "observation_tracker_ids": ["M4B-O024", "M4B-O026", "M4B-O030"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "B003, B008", "topic_id": "M4B-T003"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m4_consensus_map (tracker_id, consensus_id) SELECT 'M4B-S003', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O024'
WHERE c.tracker_id = 'M4B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O026'
WHERE c.tracker_id = 'M4B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O030'
WHERE c.tracker_id = 'M4B-S003';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Glial, Schwann, OPC, and restricted-precursor strategies form a distinct repair family focused on myelination, axon support, substrate provision, and circuit-specific outcomes rather than broad neuronal replacement.',
    'M4B-T004',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M4B-B003", "M4B-B006", "M4B-B008"], "claim_tracker_ids": ["M4B-C014", "M4B-C015", "M4B-C016", "M4B-C017", "M4B-C028", "M4B-C032"], "consensus_draft_id": "M4B-S004", "observation_tracker_ids": ["M4B-O027", "M4B-O028", "M4B-O029", "M4B-O030", "M4B-O031", "M4B-O032", "M4B-O033", "M4B-O034", "M4B-O035", "M4B-O051", "M4B-O052", "M4B-O053", "M4B-O059"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "B003, B006, B008", "topic_id": "M4B-T004"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m4_consensus_map (tracker_id, consensus_id) SELECT 'M4B-S004', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O027'
WHERE c.tracker_id = 'M4B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O028'
WHERE c.tracker_id = 'M4B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O029'
WHERE c.tracker_id = 'M4B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O030'
WHERE c.tracker_id = 'M4B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O031'
WHERE c.tracker_id = 'M4B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O032'
WHERE c.tracker_id = 'M4B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O033'
WHERE c.tracker_id = 'M4B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O034'
WHERE c.tracker_id = 'M4B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O035'
WHERE c.tracker_id = 'M4B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O051'
WHERE c.tracker_id = 'M4B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O052'
WHERE c.tracker_id = 'M4B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O053'
WHERE c.tracker_id = 'M4B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O059'
WHERE c.tracker_id = 'M4B-S004';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'OEC, MSC, BMMC, UCB, and other stromal or mixed-cell interventions should be synthesized primarily as trophic, immunomodulatory, supportive, or delivery-associated therapies unless direct replacement, integration, and lineage-specific function are demonstrated.',
    'M4B-T005',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M4B-B003", "M4B-B006", "M4B-B008"], "claim_tracker_ids": ["M4B-C018", "M4B-C019", "M4B-C033", "M4B-C034"], "consensus_draft_id": "M4B-S005", "observation_tracker_ids": ["M4B-O007", "M4B-O008", "M4B-O009", "M4B-O036", "M4B-O037", "M4B-O038", "M4B-O039", "M4B-O040", "M4B-O055", "M4B-O056", "M4B-O057", "M4B-O058", "M4B-O059", "M4B-O060"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "B003, B006, B008", "topic_id": "M4B-T005"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m4_consensus_map (tracker_id, consensus_id) SELECT 'M4B-S005', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O007'
WHERE c.tracker_id = 'M4B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O008'
WHERE c.tracker_id = 'M4B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O009'
WHERE c.tracker_id = 'M4B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O036'
WHERE c.tracker_id = 'M4B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O037'
WHERE c.tracker_id = 'M4B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O038'
WHERE c.tracker_id = 'M4B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O039'
WHERE c.tracker_id = 'M4B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O040'
WHERE c.tracker_id = 'M4B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O055'
WHERE c.tracker_id = 'M4B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O056'
WHERE c.tracker_id = 'M4B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O057'
WHERE c.tracker_id = 'M4B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O058'
WHERE c.tracker_id = 'M4B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O059'
WHERE c.tracker_id = 'M4B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O060'
WHERE c.tracker_id = 'M4B-S005';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Scaffold-cell and microenvironment combination therapies are especially relevant to chronic or complete lesions, but attribution must remain bundled unless the design separates scaffold architecture, cell source, matrix/cargo effects, lesion preparation, and rehabilitation or stimulation.',
    'M4B-T006',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M4B-B004", "M4B-B007", "M4B-B008"], "claim_tracker_ids": ["M4B-C020", "M4B-C021", "M4B-C029", "M4B-C036"], "consensus_draft_id": "M4B-S006", "observation_tracker_ids": ["M4B-O001", "M4B-O002", "M4B-O003", "M4B-O041", "M4B-O042", "M4B-O043", "M4B-O044", "M4B-O045", "M4B-O059"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "B004, B007, B008", "topic_id": "M4B-T006"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m4_consensus_map (tracker_id, consensus_id) SELECT 'M4B-S006', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O001'
WHERE c.tracker_id = 'M4B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O002'
WHERE c.tracker_id = 'M4B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O003'
WHERE c.tracker_id = 'M4B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O041'
WHERE c.tracker_id = 'M4B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O042'
WHERE c.tracker_id = 'M4B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O043'
WHERE c.tracker_id = 'M4B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O044'
WHERE c.tracker_id = 'M4B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O045'
WHERE c.tracker_id = 'M4B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O059'
WHERE c.tracker_id = 'M4B-S006';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Fetal, embryonic, respiratory, autonomic, bladder, pain, and cardiovascular graft studies show that transplantation endpoints extend beyond locomotion; consensus rows should preserve the target circuit, outcome domain, and risk profile.',
    'M4B-T007',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M4B-B003", "M4B-B006", "M4B-B008"], "claim_tracker_ids": ["M4B-C022", "M4B-C023", "M4B-C037"], "consensus_draft_id": "M4B-S007", "observation_tracker_ids": ["M4B-O046", "M4B-O047", "M4B-O048", "M4B-O049", "M4B-O050", "M4B-O054", "M4B-O055", "M4B-O056"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "B003, B006, B008", "topic_id": "M4B-T007"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m4_consensus_map (tracker_id, consensus_id) SELECT 'M4B-S007', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O046'
WHERE c.tracker_id = 'M4B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O047'
WHERE c.tracker_id = 'M4B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O048'
WHERE c.tracker_id = 'M4B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O049'
WHERE c.tracker_id = 'M4B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O050'
WHERE c.tracker_id = 'M4B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O054'
WHERE c.tracker_id = 'M4B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O055'
WHERE c.tracker_id = 'M4B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O056'
WHERE c.tracker_id = 'M4B-S007';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Module 4 should be organized into mechanism- and context-specific transplantation profiles defined by cell identity, host lesion state, delivery environment, integration assay, and endpoint class rather than one pooled cell-therapy efficacy claim.',
    'M4B-T008',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["all boundary records"], "claim_tracker_ids": ["M4B-C024", "M4B-C025", "M4B-C026", "M4B-C027", "M4B-C028", "M4B-C029", "M4B-C030", "M4B-C031", "M4B-C032", "M4B-C033", "M4B-C034", "M4B-C035", "M4B-C036", "M4B-C037", "M4B-C038", "M4B-C039", "M4B-C040"], "consensus_draft_id": "M4B-S008", "observation_tracker_ids": ["M4B-O001", "M4B-O002", "M4B-O003", "M4B-O004", "M4B-O005", "M4B-O006", "M4B-O007", "M4B-O008", "M4B-O009", "M4B-O010", "M4B-O011", "M4B-O012", "M4B-O013", "M4B-O014", "M4B-O015", "M4B-O016", "M4B-O017", "M4B-O018", "M4B-O019", "M4B-O020", "M4B-O021", "M4B-O022", "M4B-O023", "M4B-O024", "M4B-O025", "M4B-O026", "M4B-O027", "M4B-O028", "M4B-O029", "M4B-O030", "M4B-O031", "M4B-O032", "M4B-O033", "M4B-O034", "M4B-O035", "M4B-O036", "M4B-O037", "M4B-O038", "M4B-O039", "M4B-O040", "M4B-O041", "M4B-O042", "M4B-O043", "M4B-O044", "M4B-O045", "M4B-O046", "M4B-O047", "M4B-O048", "M4B-O049", "M4B-O050", "M4B-O051", "M4B-O052", "M4B-O053", "M4B-O054", "M4B-O055", "M4B-O056", "M4B-O057", "M4B-O058", "M4B-O059", "M4B-O060"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": null, "supporting_evidence_notes": "all boundary records", "topic_id": "M4B-T008"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m4_consensus_map (tracker_id, consensus_id) SELECT 'M4B-S008', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O001'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O002'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O003'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O004'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O005'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O006'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O007'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O008'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O009'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O010'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O011'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O012'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O013'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O014'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O015'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O016'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O017'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O018'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O019'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O020'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O021'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O022'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O023'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O024'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O025'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O026'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O027'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O028'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O029'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O030'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O031'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O032'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O033'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O034'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O035'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O036'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O037'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O038'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O039'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O040'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O041'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O042'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O043'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O044'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O045'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O046'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O047'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O048'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O049'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O050'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O051'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O052'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O053'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O054'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O055'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O056'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O057'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O058'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O059'
WHERE c.tracker_id = 'M4B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m4_consensus_map c
JOIN _m4_observation_map o ON o.tracker_id = 'M4B-O060'
WHERE c.tracker_id = 'M4B-S008';

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
  SELECT COUNT(*) INTO paper_count FROM _m4_paper_map;
  SELECT COUNT(*) INTO experiment_count FROM _m4_experiment_map;
  SELECT COUNT(*) INTO observation_count FROM _m4_observation_map;
  SELECT COUNT(*) INTO claim_count FROM _m4_claim_map;
  SELECT COUNT(*) INTO link_count FROM _m4_link_map;
  SELECT COUNT(*) INTO consensus_count FROM _m4_consensus_map;
  SELECT COUNT(*) INTO consensus_observation_count
  FROM Consensus_Observation co
  JOIN _m4_consensus_map cm ON cm.consensus_id = co.consensus_id;
  IF paper_count <> 60 THEN RAISE EXCEPTION 'Expected 60 papers, found %', paper_count; END IF;
  IF experiment_count <> 98 THEN RAISE EXCEPTION 'Unexpected experiment count %', experiment_count; END IF;
  IF observation_count <> 98 THEN RAISE EXCEPTION 'Expected 98 observations, found %', observation_count; END IF;
  IF claim_count <> 40 THEN RAISE EXCEPTION 'Expected 40 claims, found %', claim_count; END IF;
  IF link_count <> 72 THEN RAISE EXCEPTION 'Expected 72 evidence links, found %', link_count; END IF;
  IF consensus_count <> 8 THEN RAISE EXCEPTION 'Expected 8 consensus rows, found %', consensus_count; END IF;
  IF consensus_observation_count <> 139 THEN RAISE EXCEPTION 'Unexpected consensus-observation count %', consensus_observation_count; END IF;
END $$;

COMMIT;
