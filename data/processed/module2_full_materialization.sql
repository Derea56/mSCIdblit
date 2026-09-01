-- Module 2 full first-pass materialization generated from tracker-derived JSON.
-- This script is intended for a fresh database loaded with schema/schema.sql and scripts/seed_controlled_vocab.sql.
BEGIN;

CREATE TEMP TABLE _m2_paper_map (tracker_id TEXT PRIMARY KEY, paper_id INTEGER NOT NULL);
CREATE TEMP TABLE _m2_paradigm_map (tracker_id TEXT PRIMARY KEY, paradigm_id INTEGER NOT NULL);
CREATE TEMP TABLE _m2_experiment_map (tracker_id TEXT PRIMARY KEY, experiment_id INTEGER NOT NULL);
CREATE TEMP TABLE _m2_observation_map (tracker_id TEXT PRIMARY KEY, observation_id INTEGER NOT NULL);
CREATE TEMP TABLE _m2_claim_map (tracker_id TEXT PRIMARY KEY, claim_id INTEGER NOT NULL);
CREATE TEMP TABLE _m2_consensus_map (tracker_id TEXT PRIMARY KEY, consensus_id INTEGER NOT NULL);

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'One-year clinical study of NeuroRegen scaffold implantation following scar resection in complete chronic spinal cord injury patients', 'Xiao Z', 2016,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Clinical chronic scar-resection scaffold anchor", "module": "Module 2", "tracker_id": "M2A-P001"}'
  )
  RETURNING paper_id
)
INSERT INTO _m2_paper_map (tracker_id, paper_id) SELECT 'M2A-P001', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Collagen scaffold combined with human umbilical cord-derived mesenchymal stem cells promote functional recovery after scar resection in rats with chronic spinal cord injury', 'Wang N', 2018,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Chronic scar-resection scaffold anchor", "module": "Module 2", "tracker_id": "M2A-P002"}'
  )
  RETURNING paper_id
)
INSERT INTO _m2_paper_map (tracker_id, paper_id) SELECT 'M2A-P002', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Histological effects of combined therapy involving scar resection, decellularized scaffolds, and human iPSC-NS/PCs transplantation in chronic complete spinal cord injury', 'Ito K', 2024,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Chronic complete SCI scaffold/cell anchor; upgraded here from M1A carryover with PMC full text and explicit no-functional-recovery boundary", "module": "Module 2", "tracker_id": "M2A-P003"}'
  )
  RETURNING paper_id
)
INSERT INTO _m2_paper_map (tracker_id, paper_id) SELECT 'M2A-P003', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Biomimetic 3D-printed scaffolds for spinal cord injury repair', 'Koffler J', 2019,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "High-yield scaffold architecture and NPC-relay anchor", "module": "Module 2", "tracker_id": "M2A-P004"}'
  )
  RETURNING paper_id
)
INSERT INTO _m2_paper_map (tracker_id, paper_id) SELECT 'M2A-P004', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Aligned hydrogel tubes guide regeneration following spinal cord injury', 'Dumont CM', 2019,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Modular alignment/guidance scaffold anchor", "module": "Module 2", "tracker_id": "M2A-P005"}'
  )
  RETURNING paper_id
)
INSERT INTO _m2_paper_map (tracker_id, paper_id) SELECT 'M2A-P005', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Anisotropic Alginate Hydrogels Promote Axonal Growth across Chronic Spinal Cord Transections after Scar Removal', 'Huang L', 2020,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Chronic scar-removal scaffold bridge; anisotropic alginate channels improved conductivity, locomotion, host-cell infiltration, and raphaespinal/propriospinal/sensory axon growth after chronic scar resection", "module": "Module 2", "tracker_id": "M2A-P006"}'
  )
  RETURNING paper_id
)
INSERT INTO _m2_paper_map (tracker_id, paper_id) SELECT 'M2A-P006', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'A functionalized collagen-I scaffold delivers microRNA 21-loaded exosomes for spinal cord injury repair', 'Liu X', 2022,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Scaffold cargo-delivery anchor; collagen-I scaffold enriched with CBD-Lamp2b miR21 exosomes improved retention, sustained release, anti-apoptotic signaling, and rat transection repair", "module": "Module 2", "tracker_id": "M2A-P007"}'
  )
  RETURNING paper_id
)
INSERT INTO _m2_paper_map (tracker_id, paper_id) SELECT 'M2A-P007', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Three-dimensional aligned nanofibers-hydrogel scaffold for controlled non-viral drug/gene delivery to direct axon regeneration in spinal cord injury treatment', 'Nguyen LH', 2017,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Gene/drug delivery plus alignment", "module": "Module 2", "tracker_id": "M2A-P008"}'
  )
  RETURNING paper_id
)
INSERT INTO _m2_paper_map (tracker_id, paper_id) SELECT 'M2A-P008', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Clinical Study of NeuroRegen Scaffold Combined With Human Mesenchymal Stem Cells for the Repair of Chronic Complete Spinal Cord Injury', 'Zhao Y', 2017,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Human chronic complete SCI scaffold-cell clinical anchor", "module": "Module 2", "tracker_id": "M2A-P009"}'
  )
  RETURNING paper_id
)
INSERT INTO _m2_paper_map (tracker_id, paper_id) SELECT 'M2A-P009', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Multiple-channel scaffolds to promote spinal cord axon regeneration', 'Moore MJ', 2006,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Early synthetic channel-architecture scaffold anchor; tunable 7-channel PLGA platform combined high wall porosity with sustained surrogate release and supported Schwann-cell-associated axon growth after transection", "module": "Module 2", "tracker_id": "M2A-P010"}'
  )
  RETURNING paper_id
)
INSERT INTO _m2_paper_map (tracker_id, paper_id) SELECT 'M2A-P010', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Reknitting the injured spinal cord by self-assembling peptide nanofiber scaffold', 'Guo J', 2007,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Peptide nanofiber bridge anchor; SAPNS supported donor-cell delivery plus host-cell, vascular, and axonal ingrowth in transected dorsal column lesions", "module": "Module 2", "tracker_id": "M2A-P011"}'
  )
  RETURNING paper_id
)
INSERT INTO _m2_paper_map (tracker_id, paper_id) SELECT 'M2A-P011', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Tissue engineered regeneration of completely transected spinal cord using human mesenchymal stem cells', 'Kang KN', 2012,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Complete-transection PLGA/cell bridge anchor; hMSC-loaded PLGA scaffolds improved BBB, MEP, donor persistence, and neural-marker outcomes versus scaffold alone", "module": "Module 2", "tracker_id": "M2A-P012"}'
  )
  RETURNING paper_id
)
INSERT INTO _m2_paper_map (tracker_id, paper_id) SELECT 'M2A-P012', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'A Hydrogel Bridge Incorporating Immobilized Growth Factors and Neural Stem/Progenitor Cells to Treat Spinal Cord Injury', 'Li H', 2016,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Patterned growth-factor/cell bridge anchor; MAC/chitosan bridge reduced lesion area and increased tracing/differentiation readouts, but BBB differences were not significant", "module": "Module 2", "tracker_id": "M2A-P013"}'
  )
  RETURNING paper_id
)
INSERT INTO _m2_paper_map (tracker_id, paper_id) SELECT 'M2A-P013', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Injectable Extracellular Matrix Hydrogels as Scaffolds for Spinal Cord Injury Repair', 'Tukmachev D', 2016,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Injectable ECM hydrogel scaffold anchor", "module": "Module 2", "tracker_id": "M2A-P014"}'
  )
  RETURNING paper_id
)
INSERT INTO _m2_paper_map (tracker_id, paper_id) SELECT 'M2A-P014', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Transplantation of hUC-MSCs seeded collagen scaffolds reduces scar formation and promotes functional recovery in canines with chronic spinal cord injury', 'Li X', 2017,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Large-animal chronic NeuroRegen scaffold/cell anchor", "module": "Module 2", "tracker_id": "M2A-P015"}'
  )
  RETURNING paper_id
)
INSERT INTO _m2_paper_map (tracker_id, paper_id) SELECT 'M2A-P015', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Decellularized peripheral nerve supports Schwann cell transplants and axon growth following spinal cord injury', 'Cerqueira SR', 2018,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Clinically oriented dPN matrix/Schwann-cell anchor", "module": "Module 2", "tracker_id": "M2A-P016"}'
  )
  RETURNING paper_id
)
INSERT INTO _m2_paper_map (tracker_id, paper_id) SELECT 'M2A-P016', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Significant Improvement of Acute Complete Spinal Cord Injury Patients Diagnosed by a Combined Criteria Implanted with NeuroRegen Scaffolds and Mesenchymal Stem Cells', 'Xiao Z', 2018,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Acute complete human NeuroRegen scaffold/cell clinical anchor", "module": "Module 2", "tracker_id": "M2A-P017"}'
  )
  RETURNING paper_id
)
INSERT INTO _m2_paper_map (tracker_id, paper_id) SELECT 'M2A-P017', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Aligned collagen scaffold combination with human spinal cord-derived neural stem cells to improve spinal cord injury repair', 'Zou Y', 2020,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Human spinal cord-derived NSPC plus aligned collagen anchor; hSC-NSPCs outperformed hbNSPCs for survival, migration, inflammatory suppression, and recovery", "module": "Module 2", "tracker_id": "M2A-P018"}'
  )
  RETURNING paper_id
)
INSERT INTO _m2_paper_map (tracker_id, paper_id) SELECT 'M2A-P018', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'A multi-modal delivery strategy for spinal cord regeneration using a composite hydrogel presenting biophysical and biochemical cues synergistically', 'Man W', 2021,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Multimodal biophysical/biochemical hydrogel anchor; AFG/fSAP improved BBB, CatWalk, MEP, cavitation, axon growth, remyelination, and angiogenesis versus AFG alone and saline after lateral hemisection", "module": "Module 2", "tracker_id": "M2A-P019"}'
  )
  RETURNING paper_id
)
INSERT INTO _m2_paper_map (tracker_id, paper_id) SELECT 'M2A-P019', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'A decellularized spinal cord extracellular matrix-gel/GelMA hydrogel three-dimensional composite scaffold promotes recovery from spinal cord injury via synergism with human menstrual blood-derived stem cells', 'He W', 2022,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Spinal cord dECM/GelMA plus stem-cell anchor; 3D7G scaffold best supported MenSCs and combined implant outperformed component groups in transection repair", "module": "Module 2", "tracker_id": "M2A-P020"}'
  )
  RETURNING paper_id
)
INSERT INTO _m2_paper_map (tracker_id, paper_id) SELECT 'M2A-P020', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Magnetic alignment of injectable hydrogel scaffolds for spinal cord injury repair', 'Tran KA', 2022,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Injectable alignment strategy anchor; 100-G magnetic alignment improved axon orientation and CGRP/GAP43 outcomes with short-endpoint boundaries", "module": "Module 2", "tracker_id": "M2A-P021"}'
  )
  RETURNING paper_id
)
INSERT INTO _m2_paper_map (tracker_id, paper_id) SELECT 'M2A-P021', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Multimodal therapy strategy based on a bioactive hydrogel for repair of spinal cord injury', 'Roh EJ', 2023,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Complex multimodal hydrogel/cell/EV strategy anchor; injectable DBM/PDRN/TI-EV/NPC hydrogel reduced inflammation and apoptosis while improving neurotrophin, remyelination, and BBB outcomes after complete transection", "module": "Module 2", "tracker_id": "M2A-P022"}'
  )
  RETURNING paper_id
)
INSERT INTO _m2_paper_map (tracker_id, paper_id) SELECT 'M2A-P022', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Enhanced spinal cord regeneration by gelatin/alginate hydrogel scaffolds containing human endometrial stem cells and curcumin-loaded PLGA nanoparticles in rat', 'Ai A', 2023,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Hydrogel plus stem cell plus anti-inflammatory nanoparticle anchor; delayed hydrogel injection after contusion showed strongest BBB and histology in the combined hEnSC plus nanocurcumin condition", "module": "Module 2", "tracker_id": "M2A-P023"}'
  )
  RETURNING paper_id
)
INSERT INTO _m2_paper_map (tracker_id, paper_id) SELECT 'M2A-P023', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Therapeutic potential of placenta-derived stem cells cultivated on noggin-loaded nanochitosan/polypyrrole-alginate conductive scaffold to restore spinal cord injury', 'Manzari-Tavakoli A', 2024,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Conductive chitosan/alginate stem-cell scaffold anchor", "module": "Module 2", "tracker_id": "M2A-P024"}'
  )
  RETURNING paper_id
)
INSERT INTO _m2_paper_map (tracker_id, paper_id) SELECT 'M2A-P024', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Delivery of neurotrophin-3 from fibrin enhances neuronal fiber sprouting after spinal cord injury', 'Taylor SJ', 2006,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Early controlled neurotrophin-release scaffold anchor", "module": "Module 2", "tracker_id": "M2A-P025"}'
  )
  RETURNING paper_id
)
INSERT INTO _m2_paper_map (tracker_id, paper_id) SELECT 'M2A-P025', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Repair of spinal cord injury by implantation of bFGF-incorporated HEMA-MOETACL hydrogel in rats', 'Chen B', 2015,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Methacrylate hydrogel plus growth-factor anchor", "module": "Module 2", "tracker_id": "M2A-P026"}'
  )
  RETURNING paper_id
)
INSERT INTO _m2_paper_map (tracker_id, paper_id) SELECT 'M2A-P026', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Spinal cord injury repair by implantation of structured hyaluronic acid scaffold with PLGA microspheres in the rat', 'Wen Y', 2016,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Longitudinal HA hydrogel plus multi-cargo microsphere anchor; structured HA+PLGA improved BBB, vascularization, axon growth, and scar/inflammation metrics after dorsal hemisection", "module": "Module 2", "tracker_id": "M2A-P027"}'
  )
  RETURNING paper_id
)
INSERT INTO _m2_paper_map (tracker_id, paper_id) SELECT 'M2A-P027', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Therapeutic Effect of Neurotrophin-3 Treatment in an Injectable Collagen Scaffold Following Rat Spinal Cord Hemisection Injury', 'Breen BA', 2017,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Injectable collagen/NT-3 repair and scar-response anchor; collagen hydrogel improved BBB and scar indices, while NT-3 mainly added axonal and collagen-deposition benefits", "module": "Module 2", "tracker_id": "M2A-P028"}'
  )
  RETURNING paper_id
)
INSERT INTO _m2_paper_map (tracker_id, paper_id) SELECT 'M2A-P028', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Biodegradable scaffolds promote tissue remodeling and functional improvement in non-human primates with acute spinal cord injury', 'Slotkin JR', 2017,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Non-human primate translational scaffold anchor; PLGA-PLL porous scaffold improved 12-week locomotor recovery and appositional tissue remodeling after T9-T10 lateral hemisection in African green monkeys", "module": "Module 2", "tracker_id": "M2A-P029"}'
  )
  RETURNING paper_id
)
INSERT INTO _m2_paper_map (tracker_id, paper_id) SELECT 'M2A-P029', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Neurotrophin-3 released from implant of tissue-engineered fibroin scaffolds inhibits inflammation, enhances nerve fiber regeneration, and improves motor function in canine spinal cord injury', 'Li G', 2018,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Large-animal sustained NT-3/fibroin scaffold anchor; NF-GS outperformed fibroin-only GS at 4 weeks in Olby score, CMEP, IBA1 burden, and NF-fiber density, while GFAP scar density was unchanged.", "module": "Module 2", "tracker_id": "M2A-P030"}'
  )
  RETURNING paper_id
)
INSERT INTO _m2_paper_map (tracker_id, paper_id) SELECT 'M2A-P030', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Polycaprolactone/polysialic acid hybrid, multifunctional nanofiber scaffolds for treatment of spinal cord injury', 'Zhang S', 2018,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Electrospun drug-loaded nanofiber scaffold anchor; PCL/PSA/MP nanofibers reduced inflammatory and apoptotic markers while improving BBB, NF-200, and myelination after rat transection SCI", "module": "Module 2", "tracker_id": "M2A-P031"}'
  )
  RETURNING paper_id
)
INSERT INTO _m2_paper_map (tracker_id, paper_id) SELECT 'M2A-P031', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Effect of hyaluronic acid hydrogels containing astrocyte-derived extracellular matrix and/or V2a interneurons on histologic outcomes following spinal cord injury', 'Thompson RE', 2018,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Astrocyte-ECM and interneuron-supporting HA hydrogel anchor; protoplasmic ECM, not fibrous ECM, reduced scar/immune staining and increased neurite penetration, while V2a aggregates increased neuronal-process staining without functional testing.", "module": "Module 2", "tracker_id": "M2A-P032"}'
  )
  RETURNING paper_id
)
INSERT INTO _m2_paper_map (tracker_id, paper_id) SELECT 'M2A-P032', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Collagen scaffold combined with human umbilical cord-mesenchymal stem cells transplantation for acute complete spinal cord injury', 'Deng WS', 2020,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Animal-to-phase-I acute complete SCI translational anchor", "module": "Module 2", "tracker_id": "M2A-P033"}'
  )
  RETURNING paper_id
)
INSERT INTO _m2_paper_map (tracker_id, paper_id) SELECT 'M2A-P033', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'A Hyaluronic Acid Demilune Scaffold and Polypyrrole-Coated Fibers Carrying Embedded Human Neural Precursor Cells and Curcumin for Surface Capping of Spinal Cord Injuries', 'Elkhenany H', 2021,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Surface-capping conductive/combinatorial scaffold anchor; fully functionalized cap preserved beta-III-tubulin fibers and reduced GFAP-negative lesion area at 1 week, but did not reduce Iba1/ED1 neuroinflammation.", "module": "Module 2", "tracker_id": "M2A-P034"}'
  )
  RETURNING paper_id
)
INSERT INTO _m2_paper_map (tracker_id, paper_id) SELECT 'M2A-P034', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Therapeutic Effect of Biomimetic Scaffold Loaded with Human Amniotic Epithelial Cell-Derived Neural-like Cells for Spinal Cord Injury', 'Qiu C', 2022,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "GelMA microchannel scaffold plus hAEC-derived neural cells anchor; cell-loaded scaffolds improved BBB (5.667 vs 2.333 empty vs 0.667 transection control) and MEP at 8 weeks, but key analyses had N=3 because of postoperative deaths and cells were neural-like rather than demonstrated mature neurons.", "module": "Module 2", "tracker_id": "M2A-P035"}'
  )
  RETURNING paper_id
)
INSERT INTO _m2_paper_map (tracker_id, paper_id) SELECT 'M2A-P035', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Dual-phase SilMA hydrogel: a dynamic scaffold for sequential drug release and enhanced spinal cord repair via neural differentiation and immunomodulation', 'Zhang R', 2024,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Sequential release silk methacryloyl hydrogel anchor; Ang-(1-7) released >40% by day 3 and nearly all by day 7, while NT-3 remained in delayed release through days 28-56; 4D-SilMA improved M2/M1 markers, neuronal markers, tissue structure, and 8-week BMS to 6 in mice (n=6/group).", "module": "Module 2", "tracker_id": "M2A-P036"}'
  )
  RETURNING paper_id
)
INSERT INTO _m2_paper_map (tracker_id, paper_id) SELECT 'M2A-P036', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Coaxial 3D printing of hierarchical structured hydrogel scaffolds for on-demand repair of spinal cord injury', 'Li Y', 2023,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Time-programmed 3D-printed hydrogel scaffold anchor; coaxial scaffold paired rapid MnTBAP antioxidant release with aligned N-cadherin hydrogel cues to improve endogenous NSC migration, neuronal differentiation, and motor recovery", "module": "Module 2", "tracker_id": "M2A-P037"}'
  )
  RETURNING paper_id
)
INSERT INTO _m2_paper_map (tracker_id, paper_id) SELECT 'M2A-P037', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Schwann Cell-Derived Exosomes and Methylprednisolone Composite Patch for Spinal Cord Injury Repair', 'Zhu B', 2023,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Surface patch/exosome/steroid hydrogel scaffold anchor; noninvasive surface patch reduced acute inflammation and apoptosis and improved 28-day gait, MEP, and cavitation after T10 contusion", "module": "Module 2", "tracker_id": "M2A-P038"}'
  )
  RETURNING paper_id
)
INSERT INTO _m2_paper_map (tracker_id, paper_id) SELECT 'M2A-P038', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Axon-like aligned conductive CNT/GelMA hydrogel fibers combined with electrical stimulation for spinal cord injury recovery', 'Yao S', 2024,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Conductive aligned scaffold plus electrical stimulation anchor; 2CNT/GelMA+ES improved inflammation, axon density, remyelination, tissue conductivity (1.50 x 10^-3 S/cm vs normal 2.13 x 10^-3), BBB, pain response, and MEP.", "module": "Module 2", "tracker_id": "M2A-P039"}'
  )
  RETURNING paper_id
)
INSERT INTO _m2_paper_map (tracker_id, paper_id) SELECT 'M2A-P039', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Time Controlled Protein Release from Layer-by-Layer Assembled Multilayer Functionalized Agarose Hydrogels', 'Mehrotra S', 2010,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Agarose channel/protein-release scaffold methods anchor; PEG/PAA/protein LbL films gave pH-triggered, active protein release for more than four weeks in vitro, with rate controlled by agarose porosity and film composition.", "module": "Module 2", "tracker_id": "M2A-P040"}'
  )
  RETURNING paper_id
)
INSERT INTO _m2_paper_map (tracker_id, paper_id) SELECT 'M2A-P040', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Graft of a tissue-engineered neural scaffold serves as a promising strategy to restore myelination after rat spinal cord transection', 'Lai BQ', 2014,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Myelination-focused NT-3/TrkC neural scaffold anchor; after 8 weeks, GFP-positive graft cells, NSC-derived cells, and NT-3-Schwann cells formed MBP-positive myelin around host and graft axons, without a primary functional endpoint.", "module": "Module 2", "tracker_id": "M2A-P041"}'
  )
  RETURNING paper_id
)
INSERT INTO _m2_paper_map (tracker_id, paper_id) SELECT 'M2A-P041', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Three-dimensional bioprinting collagen/silk fibroin scaffold combined with neural stem cells promotes nerve regeneration after spinal cord injury', 'Sun Y', 2020,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "3D-bioprinted silk/collagen cell scaffold anchor; scaffold plus NSCs increased NF-H and reduced GFAP relative to SCI/scaffold-only conditions, with n=10/group, while NSC tracing and objective neurological testing were identified limitations.", "module": "Module 2", "tracker_id": "M2A-P042"}'
  )
  RETURNING paper_id
)
INSERT INTO _m2_paper_map (tracker_id, paper_id) SELECT 'M2A-P042', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Functional recovery not correlated with axon regeneration through olfactory ensheathing cell-seeded scaffolds in a model of acute spinal cord injury', 'Führmann T', 2016,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "OEC-seeded scaffold boundary/negative-mechanism anchor; seeded and non-seeded scaffolds improved skilled forelimb function despite only a trend in scaffold axon counts, directly separating functional recovery from simple axon bridging.", "module": "Module 2", "tracker_id": "M2A-P043"}'
  )
  RETURNING paper_id
)
INSERT INTO _m2_paper_map (tracker_id, paper_id) SELECT 'M2A-P043', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Biodegradable polymer grafts for surgical repair of the injured spinal cord', 'Friedman JA', 2002,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Historical surgical scaffold framing", "module": "Module 2", "tracker_id": "M2A-R001"}'
  )
  RETURNING paper_id
)
INSERT INTO _m2_paper_map (tracker_id, paper_id) SELECT 'M2A-R001', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Hydrogels in spinal cord injury repair strategies', 'Straley KS', 2010,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Hydrogel-focused scaffold review", "module": "Module 2", "tracker_id": "M2A-R002"}'
  )
  RETURNING paper_id
)
INSERT INTO _m2_paper_map (tracker_id, paper_id) SELECT 'M2A-R002', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Injectable hydrogel materials for spinal cord regeneration: a review', 'Macaya D', 2012,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Human-lesion geometry and injectable delivery framing", "module": "Module 2", "tracker_id": "M2A-R003"}'
  )
  RETURNING paper_id
)
INSERT INTO _m2_paper_map (tracker_id, paper_id) SELECT 'M2A-R003', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Biomaterial scaffolds used for the regeneration of spinal cord injury (SCI)', 'Ansorena E', 2014,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Broad biomaterial taxonomy", "module": "Module 2", "tracker_id": "M2A-R004"}'
  )
  RETURNING paper_id
)
INSERT INTO _m2_paper_map (tracker_id, paper_id) SELECT 'M2A-R004', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Biomaterial-Supported Cell Transplantation Treatments for Spinal Cord Injury: Challenges and Perspectives', 'Liu S', 2017,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Cell-plus-scaffold integration review", "module": "Module 2", "tracker_id": "M2A-R005"}'
  )
  RETURNING paper_id
)
INSERT INTO _m2_paper_map (tracker_id, paper_id) SELECT 'M2A-R005', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Spinal cord injuries: how could cell therapy help?', 'Badner A', 2017,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Helps separate scaffold effects from cell-source effects", "module": "Module 2", "tracker_id": "M2A-R006"}'
  )
  RETURNING paper_id
)
INSERT INTO _m2_paper_map (tracker_id, paper_id) SELECT 'M2A-R006', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Regeneration of Spinal Cord Connectivity Through Stem Cell Transplantation and Biomaterial Scaffolds', 'Katoh H', 2019,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Mechanistic integration of grafts and biomaterial bridges", "module": "Module 2", "tracker_id": "M2A-R007"}'
  )
  RETURNING paper_id
)
INSERT INTO _m2_paper_map (tracker_id, paper_id) SELECT 'M2A-R007', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Translational Regenerative Therapies for Chronic Spinal Cord Injury', 'Dalamagkas K', 2018,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Chronic-stage translational boundary context", "module": "Module 2", "tracker_id": "M2A-R008"}'
  )
  RETURNING paper_id
)
INSERT INTO _m2_paper_map (tracker_id, paper_id) SELECT 'M2A-R008', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 2 curated evidence extraction',
    'First-pass Module 2 biomaterials/scaffold curation for M2A-P001',
    'Tracker-derived materialization from Module_2A_TRACKER.md and Module_2B_TRACKER.md'
  FROM _m2_paper_map WHERE tracker_id = 'M2A-P001'
  RETURNING paradigm_id
)
INSERT INTO _m2_paradigm_map (tracker_id, paradigm_id) SELECT 'M2A-P001', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 2 curated evidence extraction',
    'First-pass Module 2 biomaterials/scaffold curation for M2A-P002',
    'Tracker-derived materialization from Module_2A_TRACKER.md and Module_2B_TRACKER.md'
  FROM _m2_paper_map WHERE tracker_id = 'M2A-P002'
  RETURNING paradigm_id
)
INSERT INTO _m2_paradigm_map (tracker_id, paradigm_id) SELECT 'M2A-P002', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 2 curated evidence extraction',
    'First-pass Module 2 biomaterials/scaffold curation for M2A-P003',
    'Tracker-derived materialization from Module_2A_TRACKER.md and Module_2B_TRACKER.md'
  FROM _m2_paper_map WHERE tracker_id = 'M2A-P003'
  RETURNING paradigm_id
)
INSERT INTO _m2_paradigm_map (tracker_id, paradigm_id) SELECT 'M2A-P003', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 2 curated evidence extraction',
    'First-pass Module 2 biomaterials/scaffold curation for M2A-P004',
    'Tracker-derived materialization from Module_2A_TRACKER.md and Module_2B_TRACKER.md'
  FROM _m2_paper_map WHERE tracker_id = 'M2A-P004'
  RETURNING paradigm_id
)
INSERT INTO _m2_paradigm_map (tracker_id, paradigm_id) SELECT 'M2A-P004', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 2 curated evidence extraction',
    'First-pass Module 2 biomaterials/scaffold curation for M2A-P005',
    'Tracker-derived materialization from Module_2A_TRACKER.md and Module_2B_TRACKER.md'
  FROM _m2_paper_map WHERE tracker_id = 'M2A-P005'
  RETURNING paradigm_id
)
INSERT INTO _m2_paradigm_map (tracker_id, paradigm_id) SELECT 'M2A-P005', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 2 curated evidence extraction',
    'First-pass Module 2 biomaterials/scaffold curation for M2A-P006',
    'Tracker-derived materialization from Module_2A_TRACKER.md and Module_2B_TRACKER.md'
  FROM _m2_paper_map WHERE tracker_id = 'M2A-P006'
  RETURNING paradigm_id
)
INSERT INTO _m2_paradigm_map (tracker_id, paradigm_id) SELECT 'M2A-P006', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 2 curated evidence extraction',
    'First-pass Module 2 biomaterials/scaffold curation for M2A-P007',
    'Tracker-derived materialization from Module_2A_TRACKER.md and Module_2B_TRACKER.md'
  FROM _m2_paper_map WHERE tracker_id = 'M2A-P007'
  RETURNING paradigm_id
)
INSERT INTO _m2_paradigm_map (tracker_id, paradigm_id) SELECT 'M2A-P007', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 2 curated evidence extraction',
    'First-pass Module 2 biomaterials/scaffold curation for M2A-P008',
    'Tracker-derived materialization from Module_2A_TRACKER.md and Module_2B_TRACKER.md'
  FROM _m2_paper_map WHERE tracker_id = 'M2A-P008'
  RETURNING paradigm_id
)
INSERT INTO _m2_paradigm_map (tracker_id, paradigm_id) SELECT 'M2A-P008', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 2 curated evidence extraction',
    'First-pass Module 2 biomaterials/scaffold curation for M2A-P009',
    'Tracker-derived materialization from Module_2A_TRACKER.md and Module_2B_TRACKER.md'
  FROM _m2_paper_map WHERE tracker_id = 'M2A-P009'
  RETURNING paradigm_id
)
INSERT INTO _m2_paradigm_map (tracker_id, paradigm_id) SELECT 'M2A-P009', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 2 curated evidence extraction',
    'First-pass Module 2 biomaterials/scaffold curation for M2A-P010',
    'Tracker-derived materialization from Module_2A_TRACKER.md and Module_2B_TRACKER.md'
  FROM _m2_paper_map WHERE tracker_id = 'M2A-P010'
  RETURNING paradigm_id
)
INSERT INTO _m2_paradigm_map (tracker_id, paradigm_id) SELECT 'M2A-P010', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 2 curated evidence extraction',
    'First-pass Module 2 biomaterials/scaffold curation for M2A-P011',
    'Tracker-derived materialization from Module_2A_TRACKER.md and Module_2B_TRACKER.md'
  FROM _m2_paper_map WHERE tracker_id = 'M2A-P011'
  RETURNING paradigm_id
)
INSERT INTO _m2_paradigm_map (tracker_id, paradigm_id) SELECT 'M2A-P011', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 2 curated evidence extraction',
    'First-pass Module 2 biomaterials/scaffold curation for M2A-P012',
    'Tracker-derived materialization from Module_2A_TRACKER.md and Module_2B_TRACKER.md'
  FROM _m2_paper_map WHERE tracker_id = 'M2A-P012'
  RETURNING paradigm_id
)
INSERT INTO _m2_paradigm_map (tracker_id, paradigm_id) SELECT 'M2A-P012', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 2 curated evidence extraction',
    'First-pass Module 2 biomaterials/scaffold curation for M2A-P013',
    'Tracker-derived materialization from Module_2A_TRACKER.md and Module_2B_TRACKER.md'
  FROM _m2_paper_map WHERE tracker_id = 'M2A-P013'
  RETURNING paradigm_id
)
INSERT INTO _m2_paradigm_map (tracker_id, paradigm_id) SELECT 'M2A-P013', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 2 curated evidence extraction',
    'First-pass Module 2 biomaterials/scaffold curation for M2A-P014',
    'Tracker-derived materialization from Module_2A_TRACKER.md and Module_2B_TRACKER.md'
  FROM _m2_paper_map WHERE tracker_id = 'M2A-P014'
  RETURNING paradigm_id
)
INSERT INTO _m2_paradigm_map (tracker_id, paradigm_id) SELECT 'M2A-P014', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 2 curated evidence extraction',
    'First-pass Module 2 biomaterials/scaffold curation for M2A-P015',
    'Tracker-derived materialization from Module_2A_TRACKER.md and Module_2B_TRACKER.md'
  FROM _m2_paper_map WHERE tracker_id = 'M2A-P015'
  RETURNING paradigm_id
)
INSERT INTO _m2_paradigm_map (tracker_id, paradigm_id) SELECT 'M2A-P015', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 2 curated evidence extraction',
    'First-pass Module 2 biomaterials/scaffold curation for M2A-P016',
    'Tracker-derived materialization from Module_2A_TRACKER.md and Module_2B_TRACKER.md'
  FROM _m2_paper_map WHERE tracker_id = 'M2A-P016'
  RETURNING paradigm_id
)
INSERT INTO _m2_paradigm_map (tracker_id, paradigm_id) SELECT 'M2A-P016', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 2 curated evidence extraction',
    'First-pass Module 2 biomaterials/scaffold curation for M2A-P017',
    'Tracker-derived materialization from Module_2A_TRACKER.md and Module_2B_TRACKER.md'
  FROM _m2_paper_map WHERE tracker_id = 'M2A-P017'
  RETURNING paradigm_id
)
INSERT INTO _m2_paradigm_map (tracker_id, paradigm_id) SELECT 'M2A-P017', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 2 curated evidence extraction',
    'First-pass Module 2 biomaterials/scaffold curation for M2A-P018',
    'Tracker-derived materialization from Module_2A_TRACKER.md and Module_2B_TRACKER.md'
  FROM _m2_paper_map WHERE tracker_id = 'M2A-P018'
  RETURNING paradigm_id
)
INSERT INTO _m2_paradigm_map (tracker_id, paradigm_id) SELECT 'M2A-P018', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 2 curated evidence extraction',
    'First-pass Module 2 biomaterials/scaffold curation for M2A-P019',
    'Tracker-derived materialization from Module_2A_TRACKER.md and Module_2B_TRACKER.md'
  FROM _m2_paper_map WHERE tracker_id = 'M2A-P019'
  RETURNING paradigm_id
)
INSERT INTO _m2_paradigm_map (tracker_id, paradigm_id) SELECT 'M2A-P019', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 2 curated evidence extraction',
    'First-pass Module 2 biomaterials/scaffold curation for M2A-P020',
    'Tracker-derived materialization from Module_2A_TRACKER.md and Module_2B_TRACKER.md'
  FROM _m2_paper_map WHERE tracker_id = 'M2A-P020'
  RETURNING paradigm_id
)
INSERT INTO _m2_paradigm_map (tracker_id, paradigm_id) SELECT 'M2A-P020', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 2 curated evidence extraction',
    'First-pass Module 2 biomaterials/scaffold curation for M2A-P021',
    'Tracker-derived materialization from Module_2A_TRACKER.md and Module_2B_TRACKER.md'
  FROM _m2_paper_map WHERE tracker_id = 'M2A-P021'
  RETURNING paradigm_id
)
INSERT INTO _m2_paradigm_map (tracker_id, paradigm_id) SELECT 'M2A-P021', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 2 curated evidence extraction',
    'First-pass Module 2 biomaterials/scaffold curation for M2A-P022',
    'Tracker-derived materialization from Module_2A_TRACKER.md and Module_2B_TRACKER.md'
  FROM _m2_paper_map WHERE tracker_id = 'M2A-P022'
  RETURNING paradigm_id
)
INSERT INTO _m2_paradigm_map (tracker_id, paradigm_id) SELECT 'M2A-P022', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 2 curated evidence extraction',
    'First-pass Module 2 biomaterials/scaffold curation for M2A-P023',
    'Tracker-derived materialization from Module_2A_TRACKER.md and Module_2B_TRACKER.md'
  FROM _m2_paper_map WHERE tracker_id = 'M2A-P023'
  RETURNING paradigm_id
)
INSERT INTO _m2_paradigm_map (tracker_id, paradigm_id) SELECT 'M2A-P023', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 2 curated evidence extraction',
    'First-pass Module 2 biomaterials/scaffold curation for M2A-P024',
    'Tracker-derived materialization from Module_2A_TRACKER.md and Module_2B_TRACKER.md'
  FROM _m2_paper_map WHERE tracker_id = 'M2A-P024'
  RETURNING paradigm_id
)
INSERT INTO _m2_paradigm_map (tracker_id, paradigm_id) SELECT 'M2A-P024', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 2 curated evidence extraction',
    'First-pass Module 2 biomaterials/scaffold curation for M2A-P025',
    'Tracker-derived materialization from Module_2A_TRACKER.md and Module_2B_TRACKER.md'
  FROM _m2_paper_map WHERE tracker_id = 'M2A-P025'
  RETURNING paradigm_id
)
INSERT INTO _m2_paradigm_map (tracker_id, paradigm_id) SELECT 'M2A-P025', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 2 curated evidence extraction',
    'First-pass Module 2 biomaterials/scaffold curation for M2A-P026',
    'Tracker-derived materialization from Module_2A_TRACKER.md and Module_2B_TRACKER.md'
  FROM _m2_paper_map WHERE tracker_id = 'M2A-P026'
  RETURNING paradigm_id
)
INSERT INTO _m2_paradigm_map (tracker_id, paradigm_id) SELECT 'M2A-P026', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 2 curated evidence extraction',
    'First-pass Module 2 biomaterials/scaffold curation for M2A-P027',
    'Tracker-derived materialization from Module_2A_TRACKER.md and Module_2B_TRACKER.md'
  FROM _m2_paper_map WHERE tracker_id = 'M2A-P027'
  RETURNING paradigm_id
)
INSERT INTO _m2_paradigm_map (tracker_id, paradigm_id) SELECT 'M2A-P027', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 2 curated evidence extraction',
    'First-pass Module 2 biomaterials/scaffold curation for M2A-P028',
    'Tracker-derived materialization from Module_2A_TRACKER.md and Module_2B_TRACKER.md'
  FROM _m2_paper_map WHERE tracker_id = 'M2A-P028'
  RETURNING paradigm_id
)
INSERT INTO _m2_paradigm_map (tracker_id, paradigm_id) SELECT 'M2A-P028', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 2 curated evidence extraction',
    'First-pass Module 2 biomaterials/scaffold curation for M2A-P029',
    'Tracker-derived materialization from Module_2A_TRACKER.md and Module_2B_TRACKER.md'
  FROM _m2_paper_map WHERE tracker_id = 'M2A-P029'
  RETURNING paradigm_id
)
INSERT INTO _m2_paradigm_map (tracker_id, paradigm_id) SELECT 'M2A-P029', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 2 curated evidence extraction',
    'First-pass Module 2 biomaterials/scaffold curation for M2A-P030',
    'Tracker-derived materialization from Module_2A_TRACKER.md and Module_2B_TRACKER.md'
  FROM _m2_paper_map WHERE tracker_id = 'M2A-P030'
  RETURNING paradigm_id
)
INSERT INTO _m2_paradigm_map (tracker_id, paradigm_id) SELECT 'M2A-P030', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 2 curated evidence extraction',
    'First-pass Module 2 biomaterials/scaffold curation for M2A-P031',
    'Tracker-derived materialization from Module_2A_TRACKER.md and Module_2B_TRACKER.md'
  FROM _m2_paper_map WHERE tracker_id = 'M2A-P031'
  RETURNING paradigm_id
)
INSERT INTO _m2_paradigm_map (tracker_id, paradigm_id) SELECT 'M2A-P031', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 2 curated evidence extraction',
    'First-pass Module 2 biomaterials/scaffold curation for M2A-P032',
    'Tracker-derived materialization from Module_2A_TRACKER.md and Module_2B_TRACKER.md'
  FROM _m2_paper_map WHERE tracker_id = 'M2A-P032'
  RETURNING paradigm_id
)
INSERT INTO _m2_paradigm_map (tracker_id, paradigm_id) SELECT 'M2A-P032', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 2 curated evidence extraction',
    'First-pass Module 2 biomaterials/scaffold curation for M2A-P033',
    'Tracker-derived materialization from Module_2A_TRACKER.md and Module_2B_TRACKER.md'
  FROM _m2_paper_map WHERE tracker_id = 'M2A-P033'
  RETURNING paradigm_id
)
INSERT INTO _m2_paradigm_map (tracker_id, paradigm_id) SELECT 'M2A-P033', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 2 curated evidence extraction',
    'First-pass Module 2 biomaterials/scaffold curation for M2A-P034',
    'Tracker-derived materialization from Module_2A_TRACKER.md and Module_2B_TRACKER.md'
  FROM _m2_paper_map WHERE tracker_id = 'M2A-P034'
  RETURNING paradigm_id
)
INSERT INTO _m2_paradigm_map (tracker_id, paradigm_id) SELECT 'M2A-P034', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 2 curated evidence extraction',
    'First-pass Module 2 biomaterials/scaffold curation for M2A-P035',
    'Tracker-derived materialization from Module_2A_TRACKER.md and Module_2B_TRACKER.md'
  FROM _m2_paper_map WHERE tracker_id = 'M2A-P035'
  RETURNING paradigm_id
)
INSERT INTO _m2_paradigm_map (tracker_id, paradigm_id) SELECT 'M2A-P035', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 2 curated evidence extraction',
    'First-pass Module 2 biomaterials/scaffold curation for M2A-P036',
    'Tracker-derived materialization from Module_2A_TRACKER.md and Module_2B_TRACKER.md'
  FROM _m2_paper_map WHERE tracker_id = 'M2A-P036'
  RETURNING paradigm_id
)
INSERT INTO _m2_paradigm_map (tracker_id, paradigm_id) SELECT 'M2A-P036', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 2 curated evidence extraction',
    'First-pass Module 2 biomaterials/scaffold curation for M2A-P037',
    'Tracker-derived materialization from Module_2A_TRACKER.md and Module_2B_TRACKER.md'
  FROM _m2_paper_map WHERE tracker_id = 'M2A-P037'
  RETURNING paradigm_id
)
INSERT INTO _m2_paradigm_map (tracker_id, paradigm_id) SELECT 'M2A-P037', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 2 curated evidence extraction',
    'First-pass Module 2 biomaterials/scaffold curation for M2A-P038',
    'Tracker-derived materialization from Module_2A_TRACKER.md and Module_2B_TRACKER.md'
  FROM _m2_paper_map WHERE tracker_id = 'M2A-P038'
  RETURNING paradigm_id
)
INSERT INTO _m2_paradigm_map (tracker_id, paradigm_id) SELECT 'M2A-P038', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 2 curated evidence extraction',
    'First-pass Module 2 biomaterials/scaffold curation for M2A-P039',
    'Tracker-derived materialization from Module_2A_TRACKER.md and Module_2B_TRACKER.md'
  FROM _m2_paper_map WHERE tracker_id = 'M2A-P039'
  RETURNING paradigm_id
)
INSERT INTO _m2_paradigm_map (tracker_id, paradigm_id) SELECT 'M2A-P039', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 2 curated evidence extraction',
    'First-pass Module 2 biomaterials/scaffold curation for M2A-P040',
    'Tracker-derived materialization from Module_2A_TRACKER.md and Module_2B_TRACKER.md'
  FROM _m2_paper_map WHERE tracker_id = 'M2A-P040'
  RETURNING paradigm_id
)
INSERT INTO _m2_paradigm_map (tracker_id, paradigm_id) SELECT 'M2A-P040', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 2 curated evidence extraction',
    'First-pass Module 2 biomaterials/scaffold curation for M2A-P041',
    'Tracker-derived materialization from Module_2A_TRACKER.md and Module_2B_TRACKER.md'
  FROM _m2_paper_map WHERE tracker_id = 'M2A-P041'
  RETURNING paradigm_id
)
INSERT INTO _m2_paradigm_map (tracker_id, paradigm_id) SELECT 'M2A-P041', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 2 curated evidence extraction',
    'First-pass Module 2 biomaterials/scaffold curation for M2A-P042',
    'Tracker-derived materialization from Module_2A_TRACKER.md and Module_2B_TRACKER.md'
  FROM _m2_paper_map WHERE tracker_id = 'M2A-P042'
  RETURNING paradigm_id
)
INSERT INTO _m2_paradigm_map (tracker_id, paradigm_id) SELECT 'M2A-P042', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 2 curated evidence extraction',
    'First-pass Module 2 biomaterials/scaffold curation for M2A-P043',
    'Tracker-derived materialization from Module_2A_TRACKER.md and Module_2B_TRACKER.md'
  FROM _m2_paper_map WHERE tracker_id = 'M2A-P043'
  RETURNING paradigm_id
)
INSERT INTO _m2_paradigm_map (tracker_id, paradigm_id) SELECT 'M2A-P043', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 2 curated evidence extraction',
    'First-pass Module 2 biomaterials/scaffold curation for M2A-R001',
    'Tracker-derived materialization from Module_2A_TRACKER.md and Module_2B_TRACKER.md'
  FROM _m2_paper_map WHERE tracker_id = 'M2A-R001'
  RETURNING paradigm_id
)
INSERT INTO _m2_paradigm_map (tracker_id, paradigm_id) SELECT 'M2A-R001', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 2 curated evidence extraction',
    'First-pass Module 2 biomaterials/scaffold curation for M2A-R002',
    'Tracker-derived materialization from Module_2A_TRACKER.md and Module_2B_TRACKER.md'
  FROM _m2_paper_map WHERE tracker_id = 'M2A-R002'
  RETURNING paradigm_id
)
INSERT INTO _m2_paradigm_map (tracker_id, paradigm_id) SELECT 'M2A-R002', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 2 curated evidence extraction',
    'First-pass Module 2 biomaterials/scaffold curation for M2A-R003',
    'Tracker-derived materialization from Module_2A_TRACKER.md and Module_2B_TRACKER.md'
  FROM _m2_paper_map WHERE tracker_id = 'M2A-R003'
  RETURNING paradigm_id
)
INSERT INTO _m2_paradigm_map (tracker_id, paradigm_id) SELECT 'M2A-R003', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 2 curated evidence extraction',
    'First-pass Module 2 biomaterials/scaffold curation for M2A-R004',
    'Tracker-derived materialization from Module_2A_TRACKER.md and Module_2B_TRACKER.md'
  FROM _m2_paper_map WHERE tracker_id = 'M2A-R004'
  RETURNING paradigm_id
)
INSERT INTO _m2_paradigm_map (tracker_id, paradigm_id) SELECT 'M2A-R004', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 2 curated evidence extraction',
    'First-pass Module 2 biomaterials/scaffold curation for M2A-R005',
    'Tracker-derived materialization from Module_2A_TRACKER.md and Module_2B_TRACKER.md'
  FROM _m2_paper_map WHERE tracker_id = 'M2A-R005'
  RETURNING paradigm_id
)
INSERT INTO _m2_paradigm_map (tracker_id, paradigm_id) SELECT 'M2A-R005', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 2 curated evidence extraction',
    'First-pass Module 2 biomaterials/scaffold curation for M2A-R006',
    'Tracker-derived materialization from Module_2A_TRACKER.md and Module_2B_TRACKER.md'
  FROM _m2_paper_map WHERE tracker_id = 'M2A-R006'
  RETURNING paradigm_id
)
INSERT INTO _m2_paradigm_map (tracker_id, paradigm_id) SELECT 'M2A-R006', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 2 curated evidence extraction',
    'First-pass Module 2 biomaterials/scaffold curation for M2A-R007',
    'Tracker-derived materialization from Module_2A_TRACKER.md and Module_2B_TRACKER.md'
  FROM _m2_paper_map WHERE tracker_id = 'M2A-R007'
  RETURNING paradigm_id
)
INSERT INTO _m2_paradigm_map (tracker_id, paradigm_id) SELECT 'M2A-R007', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 2 curated evidence extraction',
    'First-pass Module 2 biomaterials/scaffold curation for M2A-R008',
    'Tracker-derived materialization from Module_2A_TRACKER.md and Module_2B_TRACKER.md'
  FROM _m2_paper_map WHERE tracker_id = 'M2A-R008'
  RETURNING paradigm_id
)
INSERT INTO _m2_paradigm_map (tracker_id, paradigm_id) SELECT 'M2A-R008', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Clinical source page / M1A carried',
    'Tracker experiment M2A-P001-E001',
    'Five patients underwent MRI localization, intraoperative SSEP/MEP-guided scar excision, BMMC-loaded NeuroRegen scaffold implantation, and 12-month safety/electrophysiology follow-up.',
    'Preoperative baseline / intraoperative electrophysiology',
    'Scar resection + NeuroRegen scaffold + autologous BMMC',
    '{"observation_tracker_ids": ["M2B-O001"], "source_experiment": {"chronicity_dpi_wpi": "Chronic; 12-month follow-up", "control_type": "Preoperative baseline / intraoperative electrophysiology", "experiment_extracted": "YES", "experiment_id": "M2A-P001-E001", "figure_ref": "Clinical source page / M1A carried", "injury_device": "Clinical SCI / surgical scar resection", "injury_model": "Complete chronic traumatic SCI", "injury_severity": "Complete chronic SCI", "intervention_type": "Scar resection + NeuroRegen scaffold + autologous BMMC", "methods_summary": "Five patients underwent MRI localization, intraoperative SSEP/MEP-guided scar excision, BMMC-loaded NeuroRegen scaffold implantation, and 12-month safety/electrophysiology follow-up.", "paper_id": "M2A-P001", "sex": "Mixed", "species": "Homo sapiens", "strain": "N/A", "vertebral_level": "Variable"}, "source_experiment_tracker_id": "M2A-P001-E001", "source_paper_tracker_id": "M2A-P001", "tracker_key": "M2A-P001::M2A-P001-E001"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P001'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P001::M2A-P001-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Clinical source page / M1A carried',
    'Tracker experiment M2A-P001-E002',
    'Resected human scar tissue was immunostained for CSPGs, vimentin, NF, nestin, Tuj-1, and S100 to verify scar identity.',
    'Preserved neural tissue marker comparison',
    'Scar tissue histology',
    '{"observation_tracker_ids": ["M2B-O046"], "source_experiment": {"chronicity_dpi_wpi": "Chronic", "control_type": "Preserved neural tissue marker comparison", "experiment_extracted": "YES", "experiment_id": "M2A-P001-E002", "figure_ref": "Clinical source page / M1A carried", "injury_device": "Surgical scar resection", "injury_model": "Complete chronic traumatic SCI", "injury_severity": "Resected scar tissue", "intervention_type": "Scar tissue histology", "methods_summary": "Resected human scar tissue was immunostained for CSPGs, vimentin, NF, nestin, Tuj-1, and S100 to verify scar identity.", "paper_id": "M2A-P001", "sex": "Mixed", "species": "Homo sapiens", "strain": "N/A", "vertebral_level": "Variable"}, "source_experiment_tracker_id": "M2A-P001-E002", "source_paper_tracker_id": "M2A-P001", "tracker_key": "M2A-P001::M2A-P001-E002"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P001'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P001::M2A-P001-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract',
    'Tracker experiment M2A-P002-E001',
    'Locomotor function after surgical scar resection was assessed to evaluate safety.',
    'Chronic SCI before implantation',
    'Scar resection',
    '{"observation_tracker_ids": ["M2B-O030"], "source_experiment": {"chronicity_dpi_wpi": "12 WPI scar resection", "control_type": "Chronic SCI before implantation", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P002-E001", "figure_ref": "Abstract", "injury_device": "Surgical resection", "injury_model": "Chronic SCI with scar resection", "injury_severity": "12-week chronic SCI", "intervention_type": "Scar resection", "methods_summary": "Locomotor function after surgical scar resection was assessed to evaluate safety.", "paper_id": "M2A-P002", "sex": "UNKNOWN", "species": "Rattus norvegicus", "strain": "Adult rats", "vertebral_level": "UNKNOWN"}, "source_experiment_tracker_id": "M2A-P002-E001", "source_paper_tracker_id": "M2A-P002", "tracker_key": "M2A-P002::M2A-P002-E001"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P002'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P002::M2A-P002-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract',
    'Tracker experiment M2A-P002-E002',
    'NeuroRegen collagen scaffold and hUC-MSCs implanted into the resected cavity were assessed by locomotion, motor/somatosensory evoked potentials, and histological repair outcomes.',
    'Resection/scaffold comparison',
    'Collagen scaffold plus hUC-MSC implantation',
    '{"observation_tracker_ids": ["M2B-O051"], "source_experiment": {"chronicity_dpi_wpi": "Chronic post-resection implantation", "control_type": "Resection/scaffold comparison", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P002-E002", "figure_ref": "Abstract", "injury_device": "Surgical resection + NeuroRegen scaffold", "injury_model": "Chronic SCI with scar resection and scaffold/cell implantation", "injury_severity": "12-week chronic SCI", "intervention_type": "Collagen scaffold plus hUC-MSC implantation", "methods_summary": "NeuroRegen collagen scaffold and hUC-MSCs implanted into the resected cavity were assessed by locomotion, motor/somatosensory evoked potentials, and histological repair outcomes.", "paper_id": "M2A-P002", "sex": "UNKNOWN", "species": "Rattus norvegicus", "strain": "Adult rats", "vertebral_level": "UNKNOWN"}, "source_experiment_tracker_id": "M2A-P002-E002", "source_paper_tracker_id": "M2A-P002", "tracker_key": "M2A-P002::M2A-P002-E002"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P002'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P002::M2A-P002-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M2A-P003-E001',
    'The 8 mg/mL dECM formulation produced the longest DRG neurites (1107.40 +/- 39.96 micrometers vs 883.93 +/- 61.01 for collagen I and 963.80 +/- 29.99 for 16 mg/mL; p = 0.047). In vivo, scar resection shifted Arg1/Iba1 ratio from 0.39% +/- 0.09% to 8.00% +/- 1.47% and scaffold addition increased CD31-positive area to 0.114 +/- 0.011 mm2 versus 0.077 +/- 0.009 with resection alone.',
    'Collagen I and scar-resection-only comparisons',
    'Kidney-derived dECM hydrogel scaffold',
    '{"observation_tracker_ids": ["M2B-O031", "M2B-O043"], "source_experiment": {"chronicity_dpi_wpi": "DRG screening and chronic post-resection interval", "control_type": "Collagen I and scar-resection-only comparisons", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P003-E001", "figure_ref": "PMC11682313; DRG assay, qPCR, and vascular/immune histology", "injury_device": "Three-month chronic SCI scar resection followed by 8 microL kidney-derived dECM hydrogel; 8 and 16 mg/mL formulations pre-screened in DRG assay", "injury_model": "Chronic complete SCI with cavitary lesion conditioning", "injury_severity": "Complete chronic lesion", "intervention_type": "Kidney-derived dECM hydrogel scaffold", "methods_summary": "The 8 mg/mL dECM formulation produced the longest DRG neurites (1107.40 +/- 39.96 micrometers vs 883.93 +/- 61.01 for collagen I and 963.80 +/- 29.99 for 16 mg/mL; p = 0.047). In vivo, scar resection shifted Arg1/Iba1 ratio from 0.39% +/- 0.09% to 8.00% +/- 1.47% and scaffold addition increased CD31-positive area to 0.114 +/- 0.011 mm2 versus 0.077 +/- 0.009 with resection alone.", "paper_id": "M2A-P003", "sex": "UNKNOWN", "species": "Rattus norvegicus / DRG explant plus chronic SCI model", "strain": "Adult rat host plus rat DRG explants", "vertebral_level": "UNKNOWN"}, "source_experiment_tracker_id": "M2A-P003-E001", "source_paper_tracker_id": "M2A-P003", "tracker_key": "M2A-P003::M2A-P003-E001"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P003'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P003::M2A-P003-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract/source page / M1A carried',
    'Tracker experiment M2A-P003-E002',
    'Without scar resection, transplanted cells did not survive in the lesion epicenter. TP plus scaffold increased grafted-cell volume and raised NF-H-positive area to 0.0186 +/- 0.0026 mm2 versus 0.0098 +/- 0.0027 with TP alone and 0.0073 +/- 0.0009 in controls, but the paper explicitly reports histologic improvement without functional recovery.',
    'TP-only, scar-resection-only, and scaffold-only comparisons',
    'hNS/PC transplantation with dECM scaffold support',
    '{"observation_tracker_ids": ["M2B-O052"], "source_experiment": {"chronicity_dpi_wpi": "Chronic transplantation endpoint after 3 months SCI", "control_type": "TP-only, scar-resection-only, and scaffold-only comparisons", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P003-E002", "figure_ref": "PMC11682313; graft-volume and NF-H histology", "injury_device": "Scar resection plus scaffold-conditioned lesion followed by three-point hNS/PC transplantation", "injury_model": "Chronic complete SCI with scar resection and transplantation", "injury_severity": "Complete chronic lesion", "intervention_type": "hNS/PC transplantation with dECM scaffold support", "methods_summary": "Without scar resection, transplanted cells did not survive in the lesion epicenter. TP plus scaffold increased grafted-cell volume and raised NF-H-positive area to 0.0186 +/- 0.0026 mm2 versus 0.0098 +/- 0.0027 with TP alone and 0.0073 +/- 0.0009 in controls, but the paper explicitly reports histologic improvement without functional recovery.", "paper_id": "M2A-P003", "sex": "UNKNOWN", "species": "Rattus norvegicus / human iPSC-NS/PC xenograft", "strain": "Adult rat host plus human iPSC-derived NS/PCs", "vertebral_level": "UNKNOWN"}, "source_experiment_tracker_id": "M2A-P003-E002", "source_paper_tracker_id": "M2A-P003", "tracker_key": "M2A-P003::M2A-P003-E002"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P003'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P003::M2A-P003-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Figs. 1-2',
    'Tracker experiment M2A-P004-E001',
    'The scaffold retained architecture, reduced reactive-cell layer thickness by 35% versus agarose, reduced GFAP-defined glial scarring, vascularized, and supported 97 +/- 8 NF200-positive axons per channel and 11 +/- 5 serotonergic axons reaching the caudal end; empty scaffolds did not produce distal host-axon extension.',
    'Empty 3D-printed versus agarose, lesion-only controls',
    '3D-printed PEGDA-GelMA biomimetic scaffold with 200-micrometer channels and 260-300 kPa elastic modulus',
    '{"observation_tracker_ids": ["M2B-O004"], "source_experiment": {"chronicity_dpi_wpi": "4 weeks", "control_type": "Empty 3D-printed versus agarose, lesion-only controls", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P004-E001", "figure_ref": "Figs. 1-2; scaffold mechanics, histology, immunostaining", "injury_device": "2-mm PEGDA-GelMA scaffold; agarose, lesion-only, and no-scaffold controls", "injury_model": "Complete SCI geometry and empty-scaffold compatibility", "injury_severity": "1.8-mm tissue gap; 2-mm implant", "intervention_type": "3D-printed PEGDA-GelMA biomimetic scaffold with 200-micrometer channels and 260-300 kPa elastic modulus", "methods_summary": "The scaffold retained architecture, reduced reactive-cell layer thickness by 35% versus agarose, reduced GFAP-defined glial scarring, vascularized, and supported 97 +/- 8 NF200-positive axons per channel and 11 +/- 5 serotonergic axons reaching the caudal end; empty scaffolds did not produce distal host-axon extension.", "paper_id": "M2A-P004", "sex": "N/A", "species": "Fischer rats; T3 complete transection", "strain": "N/A", "vertebral_level": "T3"}, "source_experiment_tracker_id": "M2A-P004-E001", "source_paper_tracker_id": "M2A-P004", "tracker_key": "M2A-P004::M2A-P004-E001"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P004'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P004::M2A-P004-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Figs. 3-4',
    'Tracker experiment M2A-P004-E002',
    'NPCs filled channels and differentiated into Hu1-positive neurons (47 +/- 2%), NeuN-positive cells (20 +/- 3%), GFAP-positive astrocytes (21 +/- 3%), and Olig2-positive oligodendrocytes (11 +/- 2%). At 6 months, NPC-loaded scaffolds supported 87 +/- 5 serotonergic axons beyond the scaffold, BBB 6.6 +/- 0.5 versus 0.3 +/- 0.2 empty scaffold and 1.6 +/- 0.8 NPC-only, MEP 270 +/- 5 versus 25.1 +/- 5.7 microV, and loss of MEPs after rostral retransection, supporting a scaffold-dependent relay rather than scaffold-only efficacy.',
    'Empty scaffold and NPC graft without scaffold',
    'NPC-loaded 3D-printed biomimetic scaffold',
    '{"observation_tracker_ids": ["M2B-O053"], "source_experiment": {"chronicity_dpi_wpi": "4 weeks and 6 months", "control_type": "Empty scaffold and NPC graft without scaffold", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P004-E002", "figure_ref": "Figs. 3-4; NPC fate, synapses, BBB, MEP, retransection", "injury_device": "2-mm PEGDA-GelMA scaffold loaded with E14 rat spinal NPCs; empty scaffold and NPC-without-scaffold controls", "injury_model": "Acute complete SCI with 1.8-mm tissue removal", "injury_severity": "Complete transection", "intervention_type": "NPC-loaded 3D-printed biomimetic scaffold", "methods_summary": "NPCs filled channels and differentiated into Hu1-positive neurons (47 +/- 2%), NeuN-positive cells (20 +/- 3%), GFAP-positive astrocytes (21 +/- 3%), and Olig2-positive oligodendrocytes (11 +/- 2%). At 6 months, NPC-loaded scaffolds supported 87 +/- 5 serotonergic axons beyond the scaffold, BBB 6.6 +/- 0.5 versus 0.3 +/- 0.2 empty scaffold and 1.6 +/- 0.8 NPC-only, MEP 270 +/- 5 versus 25.1 +/- 5.7 microV, and loss of MEPs after rostral retransection, supporting a scaffold-dependent relay rather than scaffold-only efficacy.", "paper_id": "M2A-P004", "sex": "N/A", "species": "Fischer rats; T3 complete transection", "strain": "N/A", "vertebral_level": "T3"}, "source_experiment_tracker_id": "M2A-P004-E002", "source_paper_tracker_id": "M2A-P004", "tracker_key": "M2A-P004::M2A-P004-E002"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P004'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P004::M2A-P004-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Figs. 2-4',
    'Tracker experiment M2A-P005-E001',
    'Porous PEG hydrogel tubes had 66.5% porosity with 250-micrometer inner and 450-micrometer outer diameter. One-week implants showed transient CD11c+ dendritic-cell and F4/80+ macrophage increases without increased bulk GFAP or CD45; by two weeks macrophage density differences resolved. Tube and bridge implants reduced glial scar thickness at two weeks to 127 +/- 73 and 124 +/- 44 micrometers versus 337 +/- 169 with gelfoam.',
    'Gelfoam-only injury; 5-tube composite and bridge controls',
    'PEG-MAL/YKND two-step tubes or bridges',
    '{"observation_tracker_ids": ["M2B-O005"], "source_experiment": {"chronicity_dpi_wpi": "1, 2, and 8 weeks", "control_type": "Gelfoam-only injury; 5-tube composite and bridge controls", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P005-E001", "figure_ref": "Figs. 2-4; porosity, flow cytometry, histology", "injury_device": "T9-T10 lateral hemisection with 2.25-mm defect", "injury_model": "Lateral hemisection SCI", "injury_severity": "2.25-mm lateral hemisection defect", "intervention_type": "PEG-MAL/YKND two-step tubes or bridges", "methods_summary": "Porous PEG hydrogel tubes had 66.5% porosity with 250-micrometer inner and 450-micrometer outer diameter. One-week implants showed transient CD11c+ dendritic-cell and F4/80+ macrophage increases without increased bulk GFAP or CD45; by two weeks macrophage density differences resolved. Tube and bridge implants reduced glial scar thickness at two weeks to 127 +/- 73 and 124 +/- 44 micrometers versus 337 +/- 169 with gelfoam.", "paper_id": "M2A-P005", "sex": "Female", "species": "Mus musculus", "strain": "C57BL/6J", "vertebral_level": "T9-T10"}, "source_experiment_tracker_id": "M2A-P005-E001", "source_paper_tracker_id": "M2A-P005", "tracker_key": "M2A-P005::M2A-P005-E001"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P005'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P005::M2A-P005-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Figs. 5-7',
    'Tracker experiment M2A-P005-E002',
    'Axon density in tubes reached 1744 +/- 920 axons/mm2 rostrally and 1436 +/- 567 caudally versus 456 +/- 113 axons/mm2 with gelfoam; approximately 30% of tube axons were myelinated, with a higher oligodendrocyte-derived fraction than gelfoam. PEG bridges and tubes improved BMS, reaching approximately 6 versus 3 with gelfoam; tube-versus-bridge superiority was not established.',
    'Gelfoam and bridge comparisons',
    'Aligned PEG hydrogel tube composite',
    '{"observation_tracker_ids": ["M2B-O054"], "source_experiment": {"chronicity_dpi_wpi": "8 weeks", "control_type": "Gelfoam and bridge comparisons", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P005-E002", "figure_ref": "Figs. 5-7; axon/myelin quantification and BMS", "injury_device": "T9-T10 lateral hemisection with 2.25-mm defect", "injury_model": "Lateral hemisection SCI", "injury_severity": "2.25-mm lateral hemisection defect", "intervention_type": "Aligned PEG hydrogel tube composite", "methods_summary": "Axon density in tubes reached 1744 +/- 920 axons/mm2 rostrally and 1436 +/- 567 caudally versus 456 +/- 113 axons/mm2 with gelfoam; approximately 30% of tube axons were myelinated, with a higher oligodendrocyte-derived fraction than gelfoam. PEG bridges and tubes improved BMS, reaching approximately 6 versus 3 with gelfoam; tube-versus-bridge superiority was not established.", "paper_id": "M2A-P005", "sex": "Female", "species": "Mus musculus", "strain": "C57BL/6J", "vertebral_level": "T9-T10"}, "source_experiment_tracker_id": "M2A-P005-E002", "source_paper_tracker_id": "M2A-P005", "tracker_key": "M2A-P005::M2A-P005-E002"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P005'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P005::M2A-P005-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract',
    'Tracker experiment M2A-P006-E001',
    'Fifty-seven rats were assigned to lesion-only, lesion+scar resection, or lesion+scar resection plus alginate hydrogel groups. The 2 x 2 x 3 mm scaffold restored sublesional electrophysiologic responses and improved BBB scores at 14-16 weeks post-injury relative to lesion and scar-resection controls.',
    'Lesion-only and scar-resection-only controls',
    'Anisotropic alginate hydrogel engraftment',
    '{"observation_tracker_ids": ["M2B-O017"], "source_experiment": {"chronicity_dpi_wpi": "4-week chronic scar resection; 12 weeks after engraftment", "control_type": "Lesion-only and scar-resection-only controls", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P006-E001", "figure_ref": "Publisher full-text snapshot", "injury_device": "T5 complete transection with 1-1.5 mm tissue removal followed by scar resection at 4 WPI", "injury_model": "Chronic complete thoracic transection SCI", "injury_severity": "Complete chronic transection", "intervention_type": "Anisotropic alginate hydrogel engraftment", "methods_summary": "Fifty-seven rats were assigned to lesion-only, lesion+scar resection, or lesion+scar resection plus alginate hydrogel groups. The 2 x 2 x 3 mm scaffold restored sublesional electrophysiologic responses and improved BBB scores at 14-16 weeks post-injury relative to lesion and scar-resection controls.", "paper_id": "M2A-P006", "sex": "Female", "species": "Rattus norvegicus", "strain": "Adult female Fischer 344, 140-160 g, n=19/group", "vertebral_level": "T5"}, "source_experiment_tracker_id": "M2A-P006-E001", "source_paper_tracker_id": "M2A-P006", "tracker_key": "M2A-P006::M2A-P006-E001"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P006'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P006::M2A-P006-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract',
    'Tracker experiment M2A-P006-E002',
    'Histology showed numerous host cells within scaffold channels, reduced fibroglial scarring, and regeneration of raphaespinal, propriospinal, and ascending sensory axons into distal host tissue, whereas corticospinal axons did not traverse the graft.',
    'Lesion-only and scar-resection controls',
    'Anisotropic alginate hydrogel channels',
    '{"observation_tracker_ids": ["M2B-O055"], "source_experiment": {"chronicity_dpi_wpi": "Tract tracing 11-12 weeks after grafting", "control_type": "Lesion-only and scar-resection controls", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P006-E002", "figure_ref": "Publisher full-text snapshot", "injury_device": "T5 transection with delayed scar resection and scaffold placement", "injury_model": "Chronic complete thoracic transection SCI", "injury_severity": "Complete chronic transection", "intervention_type": "Anisotropic alginate hydrogel channels", "methods_summary": "Histology showed numerous host cells within scaffold channels, reduced fibroglial scarring, and regeneration of raphaespinal, propriospinal, and ascending sensory axons into distal host tissue, whereas corticospinal axons did not traverse the graft.", "paper_id": "M2A-P006", "sex": "Female", "species": "Rattus norvegicus", "strain": "Adult female Fischer 344", "vertebral_level": "T5"}, "source_experiment_tracker_id": "M2A-P006-E002", "source_paper_tracker_id": "M2A-P006", "tracker_key": "M2A-P006::M2A-P006-E002"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P006'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P006::M2A-P006-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract',
    'Tracker experiment M2A-P007-E001',
    'Genetically engineered CBD-Lamp2b miR21-loaded exosomes were enriched into collagen-I scaffolds, where they showed stronger scaffold retention and sustained release than control exosomes while reducing apoptosis-related signaling in recipient cells.',
    'CT-EXO, CBD-LP-EXO, and free-miR21 comparisons',
    'CBD-LP-miR21 exosome collagen tethering',
    '{"observation_tracker_ids": ["M2B-O037"], "source_experiment": {"chronicity_dpi_wpi": "In vitro plus 6-day release testing", "control_type": "CT-EXO, CBD-LP-EXO, and free-miR21 comparisons", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P007-E001", "figure_ref": "Publisher full-text snapshot", "injury_device": "Exosome engineering, collagen scaffold loading, and cell-challenge assays", "injury_model": "In vitro scaffold delivery model", "injury_severity": "N/A", "intervention_type": "CBD-LP-miR21 exosome collagen tethering", "methods_summary": "Genetically engineered CBD-Lamp2b miR21-loaded exosomes were enriched into collagen-I scaffolds, where they showed stronger scaffold retention and sustained release than control exosomes while reducing apoptosis-related signaling in recipient cells.", "paper_id": "M2A-P007", "sex": "N/A", "species": "HEK293T cells / scaffold system", "strain": "HEK293T, NSCs, PC12, and U118 cell assays", "vertebral_level": "N/A"}, "source_experiment_tracker_id": "M2A-P007-E001", "source_paper_tracker_id": "M2A-P007", "tracker_key": "M2A-P007::M2A-P007-E001"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P007'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P007::M2A-P007-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract',
    'Tracker experiment M2A-P007-E002',
    'Eighty-five rats underwent complete transection and collagen-scaffold implantation. The CBD-LP-miR21-EXO-Col group improved BBB scores, reduced TUNEL and cleaved caspase-3, decreased CS56-positive scar burden, and increased MAP2, TUJ1, 5-HT, and ChAT-associated repair readouts versus comparator scaffolds.',
    'SCI alone, collagen alone, CT-EXO-Col, and CBD-LP-EXO-Col controls',
    'Functionalized collagen-I scaffold with CBD-LP-miR21 exosomes',
    '{"observation_tracker_ids": ["M2B-O056"], "source_experiment": {"chronicity_dpi_wpi": "3 days, 1 week, 14 days, and 8 weeks", "control_type": "SCI alone, collagen alone, CT-EXO-Col, and CBD-LP-EXO-Col controls", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P007-E002", "figure_ref": "Publisher full-text snapshot", "injury_device": "T10 complete transection with 4 mm gap and immediate scaffold implantation", "injury_model": "Complete transection SCI", "injury_severity": "Complete transection", "intervention_type": "Functionalized collagen-I scaffold with CBD-LP-miR21 exosomes", "methods_summary": "Eighty-five rats underwent complete transection and collagen-scaffold implantation. The CBD-LP-miR21-EXO-Col group improved BBB scores, reduced TUNEL and cleaved caspase-3, decreased CS56-positive scar burden, and increased MAP2, TUJ1, 5-HT, and ChAT-associated repair readouts versus comparator scaffolds.", "paper_id": "M2A-P007", "sex": "Female", "species": "Rattus norvegicus", "strain": "Adult female Sprague-Dawley, 180-200 g", "vertebral_level": "T10"}, "source_experiment_tracker_id": "M2A-P007-E002", "source_paper_tracker_id": "M2A-P007", "tracker_key": "M2A-P007::M2A-P007-E002"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P007'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P007::M2A-P007-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Figs. 1-5',
    'Tracker experiment M2A-P008-E001',
    'Scaffold mass loss was approximately 24.8%, 33.4%, and 51.6% at 1, 2, and 3 months in vitro. NT-3 loading was 54.6 ng/mg with 90.1% released in week 1 and 99.7 +/- 0.07% by 3 months. Aligned NF-positive axons were present at 1 week and MAG-positive structures co-localized with axons at 4 weeks; scaffold integration and no cyst formation were reported through 12 weeks.',
    'Plain scaffold, negative-miR scaffold',
    '1-mm PCLEEP nanofiber-collagen scaffold aligned longitudinally in cervical cord',
    '{"observation_tracker_ids": ["M2B-O024"], "source_experiment": {"chronicity_dpi_wpi": "1, 2, and 4 weeks; release followed 3 months", "control_type": "Plain scaffold, negative-miR scaffold", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P008-E001", "figure_ref": "Figs. 1-5; release, degradation, axon and myelin assays", "injury_device": "Aligned PCLEEP nanofibers in 6 mg/mL collagen hydrogel; NT-3/heparin or miR-222 loading", "injury_model": "C5 right-sided one-third hemi-incision SCI", "injury_severity": "One-third hemi-incision cervical lesion", "intervention_type": "1-mm PCLEEP nanofiber-collagen scaffold aligned longitudinally in cervical cord", "methods_summary": "Scaffold mass loss was approximately 24.8%, 33.4%, and 51.6% at 1, 2, and 3 months in vitro. NT-3 loading was 54.6 ng/mg with 90.1% released in week 1 and 99.7 +/- 0.07% by 3 months. Aligned NF-positive axons were present at 1 week and MAG-positive structures co-localized with axons at 4 weeks; scaffold integration and no cyst formation were reported through 12 weeks.", "paper_id": "M2A-P008", "sex": "N/A", "species": "Rattus norvegicus", "strain": "Adult rats", "vertebral_level": "C5"}, "source_experiment_tracker_id": "M2A-P008-E001", "source_paper_tracker_id": "M2A-P008", "tracker_key": "M2A-P008::M2A-P008-E001"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P008'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P008::M2A-P008-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Fig. 6 and Supplementary Fig. 1',
    'Tracker experiment M2A-P008-E002',
    'miRNA loading was 0.5 microgram/mg with approximately 16% loading efficiency; 27.1 +/- 3.38% released during the first month and release remained detectable for at least two more months. miR-222 increased neurite ingrowth at 10 days without changing microglial or astrocyte reactions; Cy5-ODN spread approximately 300 micrometers from the scaffold edge at 14 days.',
    'Plain and negative-miR scaffold controls',
    'miR-222-loaded aligned nanofiber-hydrogel scaffold',
    '{"observation_tracker_ids": ["M2B-O057"], "source_experiment": {"chronicity_dpi_wpi": "10 and 14 days; miRNA release followed 3 months", "control_type": "Plain and negative-miR scaffold controls", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P008-E002", "figure_ref": "Fig. 6 and Supplementary Fig. 1; miRNA delivery, neurite and glial response", "injury_device": "miR-222- or negative-miR-loaded PCLEEP-collagen scaffold; Cy5-ODN tracing", "injury_model": "C5 right-sided one-third hemi-incision SCI", "injury_severity": "One-third hemi-incision cervical lesion", "intervention_type": "miR-222-loaded aligned nanofiber-hydrogel scaffold", "methods_summary": "miRNA loading was 0.5 microgram/mg with approximately 16% loading efficiency; 27.1 +/- 3.38% released during the first month and release remained detectable for at least two more months. miR-222 increased neurite ingrowth at 10 days without changing microglial or astrocyte reactions; Cy5-ODN spread approximately 300 micrometers from the scaffold edge at 14 days.", "paper_id": "M2A-P008", "sex": "N/A", "species": "Rattus norvegicus", "strain": "Adult rats", "vertebral_level": "C5"}, "source_experiment_tracker_id": "M2A-P008-E002", "source_paper_tracker_id": "M2A-P008", "tracker_key": "M2A-P008::M2A-P008-E002"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P008'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P008::M2A-P008-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Figs. 1-2; Tables 1-2',
    'Tracker experiment M2A-P009-E001',
    'Eight patients received scar resection and hUCB-MSC-loaded NeuroRegen. No infection, fever, allergic reaction, shock, perioperative complication, neurological aggravation, or cancer occurred over 1 year; sensation expanded in 5/8, MEP-responsive area expanded in 7/8, finger flexibility increased in 3 cervical patients, but no ASIA classification improved.',
    'Preoperative baseline / safety monitoring',
    'NeuroRegen scaffold + 4 x 10^7 hUCB-MSC implantation',
    '{"observation_tracker_ids": ["M2B-O002", "M2B-O047"], "source_experiment": {"chronicity_dpi_wpi": "1, 3, 6, and 12 months", "control_type": "Preoperative baseline / safety monitoring", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P009-E001", "figure_ref": "Figs. 1-2; Tables 1-2", "injury_device": "Clinical SCI + SSEP/MEP-guided scar resection", "injury_model": "Chronic complete SCI", "injury_severity": "ASIA A; cervical/thoracic C5-T12; 2-36 months post-injury", "intervention_type": "NeuroRegen scaffold + 4 x 10^7 hUCB-MSC implantation", "methods_summary": "Eight patients received scar resection and hUCB-MSC-loaded NeuroRegen. No infection, fever, allergic reaction, shock, perioperative complication, neurological aggravation, or cancer occurred over 1 year; sensation expanded in 5/8, MEP-responsive area expanded in 7/8, finger flexibility increased in 3 cervical patients, but no ASIA classification improved.", "paper_id": "M2A-P009", "sex": "7 male, 1 female", "species": "Homo sapiens", "strain": "N/A", "vertebral_level": "Variable"}, "source_experiment_tracker_id": "M2A-P009-E001", "source_paper_tracker_id": "M2A-P009", "tracker_key": "M2A-P009::M2A-P009-E001"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P009'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P009::M2A-P009-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract',
    'Tracker experiment M2A-P010-E001',
    'PLGA 85:15 scaffolds were molded as 3.0 mm-diameter, 15.0 mm-high cylinders using seven 0.50 mm wires, giving a void volume of 85.4 mm3 within a 106 mm3 mold. Across 30-70% w/v polymer conditions, wall void fraction reached 89% and accessible void fraction 90% through >=220 micrometer interconnections; molecular weight declined to 5% by 26 weeks, mass loss accelerated after 20 weeks, and FITC-dextran release showed a 48-hour burst followed by 4 weeks steady and 8 weeks slower sustained release.',
    'Channel-geometry and polymer-concentration comparison',
    'PLGA multi-channel scaffold',
    '{"observation_tracker_ids": ["M2B-O006"], "source_experiment": {"chronicity_dpi_wpi": "In vitro degradation through 30 weeks; release through 12 weeks", "control_type": "Channel-geometry and polymer-concentration comparison", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P010-E001", "figure_ref": "Publisher full-text snapshot; fabrication, porosity, degradation, and release assays", "injury_device": "PLGA 85:15 injection-molded multi-channel scaffold fabrication", "injury_model": "SCI repair scaffold design", "injury_severity": "N/A", "intervention_type": "PLGA multi-channel scaffold", "methods_summary": "PLGA 85:15 scaffolds were molded as 3.0 mm-diameter, 15.0 mm-high cylinders using seven 0.50 mm wires, giving a void volume of 85.4 mm3 within a 106 mm3 mold. Across 30-70% w/v polymer conditions, wall void fraction reached 89% and accessible void fraction 90% through >=220 micrometer interconnections; molecular weight declined to 5% by 26 weeks, mass loss accelerated after 20 weeks, and FITC-dextran release showed a 48-hour burst followed by 4 weeks steady and 8 weeks slower sustained release.", "paper_id": "M2A-P010", "sex": "N/A", "species": "Scaffold system / rat SCI platform", "strain": "N/A", "vertebral_level": "N/A"}, "source_experiment_tracker_id": "M2A-P010-E001", "source_paper_tracker_id": "M2A-P010", "tracker_key": "M2A-P010::M2A-P010-E001"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P010'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P010::M2A-P010-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract',
    'Tracker experiment M2A-P010-E002',
    'Primary neonatal Schwann-cell cultures were approximately 90% pure and populated all seven channels of the scaffold while remaining viable for at least 48 hours. After implantation into transected adult rat spinal cord, Schwann-cell-containing scaffolds contained regenerating axons at 1 month, supporting the scaffold as a platform for separating architectural, cellular, and molecular intervention effects.',
    'Scaffold-only / cell-seeded platform feasibility',
    'Multi-channel biodegradable scaffold platform',
    '{"observation_tracker_ids": ["M2B-O058"], "source_experiment": {"chronicity_dpi_wpi": "Schwann-cell viability 48 hours in culture; 1 month post-implant in vivo", "control_type": "Scaffold-only / cell-seeded platform feasibility", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P010-E002", "figure_ref": "Publisher full-text snapshot; Schwann-cell culture and transection implantation feasibility", "injury_device": "Experimental transection with scaffold implantation", "injury_model": "Transected spinal cord SCI", "injury_severity": "Transection", "intervention_type": "Multi-channel biodegradable scaffold platform", "methods_summary": "Primary neonatal Schwann-cell cultures were approximately 90% pure and populated all seven channels of the scaffold while remaining viable for at least 48 hours. After implantation into transected adult rat spinal cord, Schwann-cell-containing scaffolds contained regenerating axons at 1 month, supporting the scaffold as a platform for separating architectural, cellular, and molecular intervention effects.", "paper_id": "M2A-P010", "sex": "UNKNOWN", "species": "Rattus norvegicus", "strain": "Adult rat host; primary neonatal Schwann-cell coculture", "vertebral_level": "UNKNOWN"}, "source_experiment_tracker_id": "M2A-P010-E002", "source_paper_tracker_id": "M2A-P010", "tracker_key": "M2A-P010::M2A-P010-E002"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P010'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P010::M2A-P010-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract',
    'Tracker experiment M2A-P011-E001',
    'Neural progenitor cells and Schwann cells isolated from GFP-transgenic rats were cultured within self-assembling peptide nanofiber scaffold and transplanted into transected rat dorsal column lesions to test whether the scaffold could bridge a cystic injury gap.',
    'Injury/graft comparison',
    'SAPNS + neural progenitor and Schwann cell graft',
    '{"observation_tracker_ids": ["M2B-O007"], "source_experiment": {"chronicity_dpi_wpi": "Post-transplant interval not clearly reported in captured text", "control_type": "Injury/graft comparison", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P011-E001", "figure_ref": "Publisher full-text snapshot; donor-cell loading into SAPNS bridge", "injury_device": "Dorsal column transection", "injury_model": "Transected dorsal column SCI", "injury_severity": "Transection", "intervention_type": "SAPNS + neural progenitor and Schwann cell graft", "methods_summary": "Neural progenitor cells and Schwann cells isolated from GFP-transgenic rats were cultured within self-assembling peptide nanofiber scaffold and transplanted into transected rat dorsal column lesions to test whether the scaffold could bridge a cystic injury gap.", "paper_id": "M2A-P011", "sex": "UNKNOWN", "species": "Rattus norvegicus", "strain": "GFP-transgenic donor neural progenitors and Schwann cells / rat host", "vertebral_level": "UNKNOWN"}, "source_experiment_tracker_id": "M2A-P011-E001", "source_paper_tracker_id": "M2A-P011", "tracker_key": "M2A-P011::M2A-P011-E001"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P011'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P011::M2A-P011-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract',
    'Tracker experiment M2A-P011-E002',
    'The implanted SAPNS supported robust host-cell migration, blood-vessel growth, and axonal ingrowth into the scaffold, consistent with a true three-dimensional environment for living-cell migration and lesion bridging. Because the accessible capture is thinner than most other papers, this row should be read as verified histology-focused evidence rather than a deeply parameterized extraction.',
    'Scaffold/graft histology comparison',
    'SAPNS lesion bridge',
    '{"observation_tracker_ids": ["M2B-O059"], "source_experiment": {"chronicity_dpi_wpi": "Post-transplant interval not clearly reported in captured text", "control_type": "Scaffold/graft histology comparison", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P011-E002", "figure_ref": "Publisher full-text snapshot; host ingrowth histology", "injury_device": "Dorsal column transection", "injury_model": "Transected dorsal column SCI", "injury_severity": "Transection", "intervention_type": "SAPNS lesion bridge", "methods_summary": "The implanted SAPNS supported robust host-cell migration, blood-vessel growth, and axonal ingrowth into the scaffold, consistent with a true three-dimensional environment for living-cell migration and lesion bridging. Because the accessible capture is thinner than most other papers, this row should be read as verified histology-focused evidence rather than a deeply parameterized extraction.", "paper_id": "M2A-P011", "sex": "UNKNOWN", "species": "Rattus norvegicus", "strain": "Rat host", "vertebral_level": "UNKNOWN"}, "source_experiment_tracker_id": "M2A-P011-E002", "source_paper_tracker_id": "M2A-P011", "tracker_key": "M2A-P011::M2A-P011-E002"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P011'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P011::M2A-P011-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract',
    'Tracker experiment M2A-P012-E001',
    'Rats underwent complete T8-T9 transection with removal of a 2-mm cord segment and received scaffold-only control or PLGA scaffolds loaded with 1 x 10^5, 2 x 10^4, or 4 x 10^3 hMSCs. Control BBB reached 3 at 2 weeks but fell to about 2 by 6-8 weeks, whereas hMSC groups improved gradually to approximately 4.5-6 by 8 weeks; sham MEP amplitudes were 1757 +/- 333 microV at 4 weeks and 2076 +/- 622 microV at 8 weeks, versus 135 +/- 117 and 100 +/- 25 microV in scaffold-only controls.',
    'PLGA scaffold without hMSC',
    'PLGA scaffold + hMSC',
    '{"observation_tracker_ids": ["M2B-O009"], "source_experiment": {"chronicity_dpi_wpi": "2, 4, 6, and 8 weeks", "control_type": "PLGA scaffold without hMSC", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P012-E001", "figure_ref": "Publisher full-text snapshot; complete transection repair groups and functional readouts", "injury_device": "Surgical complete transection/removal with scaffold implantation", "injury_model": "Complete transection SCI with 2-mm cord removal", "injury_severity": "Complete transection", "intervention_type": "PLGA scaffold + hMSC", "methods_summary": "Rats underwent complete T8-T9 transection with removal of a 2-mm cord segment and received scaffold-only control or PLGA scaffolds loaded with 1 x 10^5, 2 x 10^4, or 4 x 10^3 hMSCs. Control BBB reached 3 at 2 weeks but fell to about 2 by 6-8 weeks, whereas hMSC groups improved gradually to approximately 4.5-6 by 8 weeks; sham MEP amplitudes were 1757 +/- 333 microV at 4 weeks and 2076 +/- 622 microV at 8 weeks, versus 135 +/- 117 and 100 +/- 25 microV in scaffold-only controls.", "paper_id": "M2A-P012", "sex": "UNKNOWN", "species": "Rattus norvegicus", "strain": "Rat", "vertebral_level": "T8-T9"}, "source_experiment_tracker_id": "M2A-P012-E001", "source_paper_tracker_id": "M2A-P012", "tracker_key": "M2A-P012::M2A-P012-E001"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P012'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P012::M2A-P012-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract',
    'Tracker experiment M2A-P012-E002',
    'PKH-labeled hMSCs remained detectable at approximately 8% at 4 weeks and 7% at 8 weeks; NSE-positive donor cells were approximately 11% at 4 weeks and 10% at 8 weeks. NF-positive cells were about 1% in scaffold-only controls but rose to approximately 5% at 4 weeks and 8% at 8 weeks in hMSC groups, supporting donor persistence with partial neural differentiation and enhanced repair.',
    'Scaffold-only / hMSC dose groups',
    'hMSC-seeded PLGA scaffold',
    '{"observation_tracker_ids": ["M2B-O060"], "source_experiment": {"chronicity_dpi_wpi": "4 and 8 weeks", "control_type": "Scaffold-only / hMSC dose groups", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P012-E002", "figure_ref": "Publisher full-text snapshot; donor persistence, differentiation, and axonal-marker outcomes", "injury_device": "Surgical complete transection/removal", "injury_model": "Complete transection SCI", "injury_severity": "Complete transection", "intervention_type": "hMSC-seeded PLGA scaffold", "methods_summary": "PKH-labeled hMSCs remained detectable at approximately 8% at 4 weeks and 7% at 8 weeks; NSE-positive donor cells were approximately 11% at 4 weeks and 10% at 8 weeks. NF-positive cells were about 1% in scaffold-only controls but rose to approximately 5% at 4 weeks and 8% at 8 weeks in hMSC groups, supporting donor persistence with partial neural differentiation and enhanced repair.", "paper_id": "M2A-P012", "sex": "UNKNOWN", "species": "Rattus norvegicus", "strain": "Rat with implanted hMSCs", "vertebral_level": "T8-T9"}, "source_experiment_tracker_id": "M2A-P012-E002", "source_paper_tracker_id": "M2A-P012", "tracker_key": "M2A-P012::M2A-P012-E002"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P012'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P012::M2A-P012-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract',
    'Tracker experiment M2A-P013-E001',
    'Adult rats received a 2-2.5 mm right-sided gap between T8 and T9 bridged with a chitosan conduit containing methacrylamide chitosan hydrogel and encapsulated NSPCs, sealed with fibrin glue. All conduit treatments reduced lesion area to about 0.39 +/- 0.08 mm2 versus 1.30 +/- 0.42 mm2 in untreated controls, and the iIFN-gamma + cells group had the smallest lesion at 0.33 +/- 0.06 mm2.',
    'Untreated injury and conduit-condition comparisons',
    'MAC hydrogel + chitosan conduit + NSPCs',
    '{"observation_tracker_ids": ["M2B-O032"], "source_experiment": {"chronicity_dpi_wpi": "8 weeks", "control_type": "Untreated injury and conduit-condition comparisons", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P013-E001", "figure_ref": "Publisher full-text snapshot; hemisection bridge construction and lesion-size effect", "injury_device": "Right lateral hemisection with conduit bridge implantation", "injury_model": "Hemisection SCI", "injury_severity": "Hemisection", "intervention_type": "MAC hydrogel + chitosan conduit + NSPCs", "methods_summary": "Adult rats received a 2-2.5 mm right-sided gap between T8 and T9 bridged with a chitosan conduit containing methacrylamide chitosan hydrogel and encapsulated NSPCs, sealed with fibrin glue. All conduit treatments reduced lesion area to about 0.39 +/- 0.08 mm2 versus 1.30 +/- 0.42 mm2 in untreated controls, and the iIFN-gamma + cells group had the smallest lesion at 0.33 +/- 0.06 mm2.", "paper_id": "M2A-P013", "sex": "UNKNOWN", "species": "Rattus norvegicus", "strain": "Rat", "vertebral_level": "T8-T9"}, "source_experiment_tracker_id": "M2A-P013-E001", "source_paper_tracker_id": "M2A-P013", "tracker_key": "M2A-P013::M2A-P013-E001"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P013'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P013::M2A-P013-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract',
    'Tracker experiment M2A-P013-E002',
    'Immobilized IFN-gamma or PDGF-AA roughly doubled Fluoro-Gold-traced neurons crossing the lesion in cue-plus-cell groups (n = 3). iIFN-gamma favored betaIII-tubulin-positive neuronal differentiation and iPDGF-AA + cells favored RIP-positive oligodendrocytic outcomes, while ED-1-positive macrophages remained sparse at the lesion edge and BBB scores stabilized around 13-15 without significant treatment differences.',
    'Uncued MAC and MAC+cells bridge comparisons',
    'Immobilized IFN-gamma or PDGF-AA lineage cues',
    '{"observation_tracker_ids": ["M2B-O061"], "source_experiment": {"chronicity_dpi_wpi": "8 weeks", "control_type": "Uncued MAC and MAC+cells bridge comparisons", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P013-E002", "figure_ref": "Publisher full-text snapshot; lineage-cue, tracing, and functional outcomes", "injury_device": "Right lateral hemisection with lineage-cued bridge", "injury_model": "Hemisection SCI", "injury_severity": "Hemisection", "intervention_type": "Immobilized IFN-gamma or PDGF-AA lineage cues", "methods_summary": "Immobilized IFN-gamma or PDGF-AA roughly doubled Fluoro-Gold-traced neurons crossing the lesion in cue-plus-cell groups (n = 3). iIFN-gamma favored betaIII-tubulin-positive neuronal differentiation and iPDGF-AA + cells favored RIP-positive oligodendrocytic outcomes, while ED-1-positive macrophages remained sparse at the lesion edge and BBB scores stabilized around 13-15 without significant treatment differences.", "paper_id": "M2A-P013", "sex": "UNKNOWN", "species": "Rattus norvegicus / NSPC bridge", "strain": "Rat", "vertebral_level": "T8-T9"}, "source_experiment_tracker_id": "M2A-P013-E002", "source_paper_tracker_id": "M2A-P013", "tracker_key": "M2A-P013::M2A-P013-E002"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P013'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P013::M2A-P013-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Figs. 2-7',
    'Tracker experiment M2A-P014-E002',
    'Both ECM hydrogels filled and integrated into lesions, increased NF160 axon ingrowth and RECA vascularization versus saline, and organized ingrowing axons longitudinally, but hydrogels mostly degraded by 2 weeks and fully by 8 weeks with progressive small cysts and massive macrophage infiltration. SC- versus UB-ECM did not differ; hWJ-MSCs did not further increase axon or vessel ingrowth, with few surviving cells at 4 weeks.',
    'Saline lesion; SC-ECM versus UB-ECM; cell-seeded versus empty with immunosuppression',
    'Injectable decellularized ECM hydrogel',
    '{"observation_tracker_ids": ["M2B-O015", "M2B-O062"], "source_experiment": {"chronicity_dpi_wpi": "2, 4, and 8 weeks; BBB weeks 1-4", "control_type": "Saline lesion; SC-ECM versus UB-ECM; cell-seeded versus empty with immunosuppression", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P014-E002", "figure_ref": "Figs. 2-7; H&E, NF160, RECA, macrophage markers, qPCR", "injury_device": "8 mg/mL porcine SC-ECM or UB-ECM hydrogel injected in situ; saline control; SC-ECM plus approximately 15,000 hWJ-MSCs with immunosuppression", "injury_model": "Th8 hemisection with 2-mm segment removed", "injury_severity": "Acute 6 mm3 hemisection cavity", "intervention_type": "Injectable decellularized ECM hydrogel", "methods_summary": "Both ECM hydrogels filled and integrated into lesions, increased NF160 axon ingrowth and RECA vascularization versus saline, and organized ingrowing axons longitudinally, but hydrogels mostly degraded by 2 weeks and fully by 8 weeks with progressive small cysts and massive macrophage infiltration. SC- versus UB-ECM did not differ; hWJ-MSCs did not further increase axon or vessel ingrowth, with few surviving cells at 4 weeks.", "paper_id": "M2A-P014", "sex": "Male", "species": "Rattus norvegicus", "strain": "Male Wistar rats, 250-300 g", "vertebral_level": "Th8"}, "source_experiment_tracker_id": "M2A-P014-E002", "source_paper_tracker_id": "M2A-P014", "tracker_key": "M2A-P014::M2A-P014-E002"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P014'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P014::M2A-P014-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Figs. 1-7',
    'Tracker experiment M2A-P015-E001',
    'Eighteen beagles underwent complete T8 resection, then delayed scar removal and implantation. Scar removal did not reduce Olby scores; functionalized scaffolds reached approximately 6 versus 2-4.5 in controls/scaffold-only.',
    'Control (n=6), scaffold-only (n=6), functionalized scaffold (n=6)',
    'NeuroRegen scaffold +/- 10^7 hUC-MSCs',
    '{"observation_tracker_ids": ["M2B-O018"], "source_experiment": {"chronicity_dpi_wpi": "2 months post-injury scar removal; 12 months post-treatment", "control_type": "Control (n=6), scaffold-only (n=6), functionalized scaffold (n=6)", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P015-E001", "figure_ref": "Fig. 1; Olby time course", "injury_device": "Complete T8 spinal cord segment removal + delayed scar resection", "injury_model": "Chronic complete SCI", "injury_severity": "Complete transection; 5-mm cord removal", "intervention_type": "NeuroRegen scaffold +/- 10^7 hUC-MSCs", "methods_summary": "Eighteen beagles underwent complete T8 resection, then delayed scar removal and implantation. Scar removal did not reduce Olby scores; functionalized scaffolds reached approximately 6 versus 2-4.5 in controls/scaffold-only.", "paper_id": "M2A-P015", "sex": "Female", "species": "Canis familiaris", "strain": "Adult female Beagle", "vertebral_level": "T8"}, "source_experiment_tracker_id": "M2A-P015-E001", "source_paper_tracker_id": "M2A-P015", "tracker_key": "M2A-P015::M2A-P015-E001"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P015'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P015::M2A-P015-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Figs. 2-7',
    'Tracker experiment M2A-P015-E002',
    'Functionalized scaffolds increased Tuj-1/Map2 and 5-HT-positive neurons, remyelinated axons, and lesion-site synaptophysin while reducing CS-56/CSPG signal; human MSCs were absent at 6 months, leaving endogenous-cell mediation unresolved.',
    'Control and non-functionalized NeuroRegen scaffold',
    'Functionalized NeuroRegen scaffold + hUC-MSCs',
    '{"observation_tracker_ids": ["M2B-O063"], "source_experiment": {"chronicity_dpi_wpi": "1 year post-implantation", "control_type": "Control and non-functionalized NeuroRegen scaffold", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P015-E002", "figure_ref": "Figs. 2-7; immunofluorescence/TEM", "injury_device": "Complete transection + scaffold/cell implantation", "injury_model": "Chronic complete SCI", "injury_severity": "Complete transection; chronic cavity", "intervention_type": "Functionalized NeuroRegen scaffold + hUC-MSCs", "methods_summary": "Functionalized scaffolds increased Tuj-1/Map2 and 5-HT-positive neurons, remyelinated axons, and lesion-site synaptophysin while reducing CS-56/CSPG signal; human MSCs were absent at 6 months, leaving endogenous-cell mediation unresolved.", "paper_id": "M2A-P015", "sex": "Female", "species": "Canis familiaris", "strain": "Adult female Beagle", "vertebral_level": "T8"}, "source_experiment_tracker_id": "M2A-P015-E002", "source_paper_tracker_id": "M2A-P015", "tracker_key": "M2A-P015::M2A-P015-E002"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P015'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P015::M2A-P015-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Figs. 3-8',
    'Tracker experiment M2A-P016-E001',
    'iPN groups had immune-cell numbers similar to injury-only at 14 days; Matrigel groups trended toward approximately 3-fold more leukocytes/T cells. SC grafts in iPN contained approximately 3-fold more SCs at 14 days.',
    'Injury-only; Matrigel +/- SC',
    'Schwann cells in injectable decellularized peripheral nerve matrix',
    '{"observation_tracker_ids": ["M2B-O010"], "source_experiment": {"chronicity_dpi_wpi": "3 and 14 days post-transplantation", "control_type": "Injury-only; Matrigel +/- SC", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P016-E001", "figure_ref": "Figs. 3-5; flow cytometry/histology", "injury_device": "Thoracic contusion", "injury_model": "Contusion SCI", "injury_severity": "Moderate contusion; BBB 0.9 +/- 0.5 at 1 day and 5.5 +/- 0.7 at 7 days", "intervention_type": "Schwann cells in injectable decellularized peripheral nerve matrix", "methods_summary": "iPN groups had immune-cell numbers similar to injury-only at 14 days; Matrigel groups trended toward approximately 3-fold more leukocytes/T cells. SC grafts in iPN contained approximately 3-fold more SCs at 14 days.", "paper_id": "M2A-P016", "sex": "Female", "species": "Rattus norvegicus", "strain": "Adult Fischer", "vertebral_level": "Thoracic; T7-T9 sampling"}, "source_experiment_tracker_id": "M2A-P016-E001", "source_paper_tracker_id": "M2A-P016", "tracker_key": "M2A-P016::M2A-P016-E001"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P016'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P016::M2A-P016-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Figs. 6-8',
    'Tracker experiment M2A-P016-E002',
    'At 8 weeks iPN graft volume was 0.95 +/- 0.28 versus 0.48 +/- 0.17 mm3 in Matrigel, SC-myelinated axons 6927 +/- 2429 versus 3259 +/- 475, and BBB was comparable. Grid-walk errors favored iPN at 4 weeks (6.1 +/- 1.1% vs 8.6 +/- 1.8%) but equalized by 8 weeks (3.5 +/- 1.6% vs 5.0 +/- 1.7%).',
    'SC/Matrigel comparison',
    'SC/iPN matrix graft',
    '{"observation_tracker_ids": ["M2B-O064"], "source_experiment": {"chronicity_dpi_wpi": "4 and 8 weeks post-transplantation", "control_type": "SC/Matrigel comparison", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P016-E002", "figure_ref": "Figs. 6-8; graft, axon, BBB/grid-walk", "injury_device": "Thoracic contusion", "injury_model": "Contusion SCI", "injury_severity": "Moderate contusion", "intervention_type": "SC/iPN matrix graft", "methods_summary": "At 8 weeks iPN graft volume was 0.95 +/- 0.28 versus 0.48 +/- 0.17 mm3 in Matrigel, SC-myelinated axons 6927 +/- 2429 versus 3259 +/- 475, and BBB was comparable. Grid-walk errors favored iPN at 4 weeks (6.1 +/- 1.1% vs 8.6 +/- 1.8%) but equalized by 8 weeks (3.5 +/- 1.6% vs 5.0 +/- 1.7%).", "paper_id": "M2A-P016", "sex": "Female", "species": "Rattus norvegicus", "strain": "Adult Fischer", "vertebral_level": "Thoracic; T7-T9 sampling"}, "source_experiment_tracker_id": "M2A-P016-E002", "source_paper_tracker_id": "M2A-P016", "tracker_key": "M2A-P016::M2A-P016-E002"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P016'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P016::M2A-P016-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Figs. 1-5',
    'Tracker experiment M2A-P017-E001',
    'Two acute complete patients received 1.5-cm or 1.1-cm NeuroRegen implants. Both improved to ASIA C with sensory and motor recovery and recovered SSEP/MEP; thoracic WISCI rose 0 to 7 by 12 months. No obvious treatment-related adverse symptoms were reported.',
    'Preoperative baseline / no-treatment comparator',
    'NeuroRegen scaffold + approximately 4 x 10^7 umbilical-cord MSCs',
    '{"observation_tracker_ids": ["M2B-O022"], "source_experiment": {"chronicity_dpi_wpi": "24 hours or 8 days post-injury; 1-24 months reported for thoracic follow-up", "control_type": "Preoperative baseline / no-treatment comparator", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P017-E001", "figure_ref": "Figs. 1-5; ASIA/SSEP/MEP follow-up", "injury_device": "Clinical traumatic SCI + scaffold implantation", "injury_model": "Acute complete SCI", "injury_severity": "ASIA A by combined ASIA/MRI/electrophysiology; T11 and C4", "intervention_type": "NeuroRegen scaffold + approximately 4 x 10^7 umbilical-cord MSCs", "methods_summary": "Two acute complete patients received 1.5-cm or 1.1-cm NeuroRegen implants. Both improved to ASIA C with sensory and motor recovery and recovered SSEP/MEP; thoracic WISCI rose 0 to 7 by 12 months. No obvious treatment-related adverse symptoms were reported.", "paper_id": "M2A-P017", "sex": "Male", "species": "Homo sapiens", "strain": "N/A", "vertebral_level": "T11 and C4"}, "source_experiment_tracker_id": "M2A-P017-E001", "source_paper_tracker_id": "M2A-P017", "tracker_key": "M2A-P017::M2A-P017-E001"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P017'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P017::M2A-P017-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract',
    'Tracker experiment M2A-P018-E001',
    'The ACSS had 60 +/- 10 micrometer oriented pores in a 2 mm-thick, 3 mm-diameter scaffold. hSC-NSPC survival exceeded hbNSPC survival at 1, 4, and 8 weeks (69.0 +/- 4.1, 43.2 +/- 8.8, and 12.0 +/- 2.0 vs 22.0 +/- 6.7, 12.0 +/- 2.7, and 5.4 +/- 1.1 cells/field) and hSC-NSPCs distributed closer to the rostral and caudal host borders.',
    'SCI control, ACSS-only, hbNSPC+ACSS, hSC-NSPC+ACSS (n = 24/group)',
    'Aligned collagen sponge scaffold plus hbNSPC or hSC-NSPC',
    '{"observation_tracker_ids": ["M2B-O025"], "source_experiment": {"chronicity_dpi_wpi": "1, 4, and 8 weeks", "control_type": "SCI control, ACSS-only, hbNSPC+ACSS, hSC-NSPC+ACSS (n = 24/group)", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P018-E001", "figure_ref": "Publisher full-text snapshot; group design and donor-cell tracking", "injury_device": "T9 transection with 2 mm cord removal followed by ACSS implantation seeded with GFP-labeled hbNSPCs or hSC-NSPCs at 2 x 10^6 cells/scaffold in 20 microL", "injury_model": "Complete transection SCI", "injury_severity": "Complete transection; 2 mm gap", "intervention_type": "Aligned collagen sponge scaffold plus hbNSPC or hSC-NSPC", "methods_summary": "The ACSS had 60 +/- 10 micrometer oriented pores in a 2 mm-thick, 3 mm-diameter scaffold. hSC-NSPC survival exceeded hbNSPC survival at 1, 4, and 8 weeks (69.0 +/- 4.1, 43.2 +/- 8.8, and 12.0 +/- 2.0 vs 22.0 +/- 6.7, 12.0 +/- 2.7, and 5.4 +/- 1.1 cells/field) and hSC-NSPCs distributed closer to the rostral and caudal host borders.", "paper_id": "M2A-P018", "sex": "Female", "species": "Rattus norvegicus", "strain": "Female Sprague-Dawley, 6-8 weeks", "vertebral_level": "T9"}, "source_experiment_tracker_id": "M2A-P018-E001", "source_paper_tracker_id": "M2A-P018", "tracker_key": "M2A-P018::M2A-P018-E001"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P018'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P018::M2A-P018-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract',
    'Tracker experiment M2A-P018-E002',
    'Relative to hbNSPC-loaded or scaffold-only controls, hSC-NSPC constructs showed better migration into host tissue, stronger neuronal differentiation/maturation, reduced inflammatory response and glial scar, and improved locomotor recovery, making the benefit partly cell-source dependent rather than a scaffold-only effect.',
    'hbNSPC+ACSS and ACSS-only comparisons',
    'hSC-NSPC-loaded aligned collagen scaffold',
    '{"observation_tracker_ids": ["M2B-O065"], "source_experiment": {"chronicity_dpi_wpi": "Up to 8 weeks after transplantation", "control_type": "hbNSPC+ACSS and ACSS-only comparisons", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P018-E002", "figure_ref": "Publisher full-text snapshot; host-response and recovery outcomes", "injury_device": "T9 complete transection with ACSS-supported donor-cell implantation", "injury_model": "Complete transection SCI", "injury_severity": "Complete transection; 2 mm gap", "intervention_type": "hSC-NSPC-loaded aligned collagen scaffold", "methods_summary": "Relative to hbNSPC-loaded or scaffold-only controls, hSC-NSPC constructs showed better migration into host tissue, stronger neuronal differentiation/maturation, reduced inflammatory response and glial scar, and improved locomotor recovery, making the benefit partly cell-source dependent rather than a scaffold-only effect.", "paper_id": "M2A-P018", "sex": "Female", "species": "Rattus norvegicus", "strain": "Female Sprague-Dawley, 6-8 weeks", "vertebral_level": "T9"}, "source_experiment_tracker_id": "M2A-P018-E002", "source_paper_tracker_id": "M2A-P018", "tracker_key": "M2A-P018::M2A-P018-E002"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P018'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P018::M2A-P018-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract',
    'Tracker experiment M2A-P019-E001',
    'AFG was electrospun into a 2 mm bundle and soaked with RAD:KLT:RGI peptides at 2:1:1 before transglutaminase crosslinking to create AFG/fSAP. The composite Young''s modulus was 2.72 +/- 0.29 kPa versus 3.11 +/- 0.34 kPa for AFG, and female 6-week SD rats (54 total) were assigned to saline, AFG, or AFG/fSAP after 5 mm right T9-T10 lateral hemisection.',
    'AFG vs AFG/fSAP construction comparison',
    'Aligned fibrin hydrogel + functionalized self-assembling peptide composite',
    '{"observation_tracker_ids": ["M2B-O048"], "source_experiment": {"chronicity_dpi_wpi": "In vitro mechanics plus 12-week in vivo timeline", "control_type": "AFG vs AFG/fSAP construction comparison", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P019-E001", "figure_ref": "Publisher full-text snapshot; scaffold fabrication and animal-model design", "injury_device": "AFG fabricated by electrospinning and crosslinked with RAD/KLT/RGI peptides", "injury_model": "SCI repair scaffold design", "injury_severity": "N/A", "intervention_type": "Aligned fibrin hydrogel + functionalized self-assembling peptide composite", "methods_summary": "AFG was electrospun into a 2 mm bundle and soaked with RAD:KLT:RGI peptides at 2:1:1 before transglutaminase crosslinking to create AFG/fSAP. The composite Young''s modulus was 2.72 +/- 0.29 kPa versus 3.11 +/- 0.34 kPa for AFG, and female 6-week SD rats (54 total) were assigned to saline, AFG, or AFG/fSAP after 5 mm right T9-T10 lateral hemisection.", "paper_id": "M2A-P019", "sex": "N/A", "species": "Scaffold system / rat SCI context", "strain": "N/A", "vertebral_level": "N/A"}, "source_experiment_tracker_id": "M2A-P019-E001", "source_paper_tracker_id": "M2A-P019", "tracker_key": "M2A-P019::M2A-P019-E001"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P019'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P019::M2A-P019-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract',
    'Tracker experiment M2A-P019-E002',
    'AFG/fSAP improved CatWalk regulatory index to 73.79 +/- 6.06% versus 61.13 +/- 10.74% for AFG and 22.43 +/- 12.70% for control, and reduced non-paw contact duration to 0.63 +/- 0.97% versus 16.75 +/- 9.65% and 92.21 +/- 10.07%. It also raised rostral and middle axon density, increased CD34 microvessel density to 3.55 +/- 0.55% versus 2.61 +/- 0.37% AFG and 1.50 +/- 0.47% control, promoted remyelination, and reduced syringomyelia through 12 weeks.',
    'Saline and AFG scaffold controls',
    'AFG/fSAP multifunctional aligned fibrin-peptide hydrogel',
    '{"observation_tracker_ids": ["M2B-O066"], "source_experiment": {"chronicity_dpi_wpi": "1, 8, and 12 weeks; BBB weekly; CatWalk/MEP/MRI at 12 weeks", "control_type": "Saline and AFG scaffold controls", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P019-E002", "figure_ref": "Publisher full-text snapshot; multimodal repair outcomes after lateral hemisection", "injury_device": "T9-T10 laminectomy with 5 mm right hemisection bridged by saline, AFG, or AFG/fSAP", "injury_model": "Right lateral hemisection SCI", "injury_severity": "Hemisection; Brown-Sequard-type defect", "intervention_type": "AFG/fSAP multifunctional aligned fibrin-peptide hydrogel", "methods_summary": "AFG/fSAP improved CatWalk regulatory index to 73.79 +/- 6.06% versus 61.13 +/- 10.74% for AFG and 22.43 +/- 12.70% for control, and reduced non-paw contact duration to 0.63 +/- 0.97% versus 16.75 +/- 9.65% and 92.21 +/- 10.07%. It also raised rostral and middle axon density, increased CD34 microvessel density to 3.55 +/- 0.55% versus 2.61 +/- 0.37% AFG and 1.50 +/- 0.47% control, promoted remyelination, and reduced syringomyelia through 12 weeks.", "paper_id": "M2A-P019", "sex": "Female", "species": "Rattus norvegicus", "strain": "Female Sprague-Dawley, 6 weeks, 200-230 g", "vertebral_level": "T9-T10"}, "source_experiment_tracker_id": "M2A-P019-E002", "source_paper_tracker_id": "M2A-P019", "tracker_key": "M2A-P019::M2A-P019-E002"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P019'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P019::M2A-P019-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract',
    'Tracker experiment M2A-P020-E001',
    'Decellularization reduced residual DNA to 46.78 +/- 6.33 ng/mg, a 96.42% reduction versus normal spinal cord. 4D6G failed to polymerize; 1D9G, 2D8G, and 3D7G had compression moduli of 6.04 +/- 0.68, 4.9 +/- 0.14, and 4.01 +/- 0.32 Pa, and MenSC viability after 3 days reached 85.96% +/- 2.7%, 87.17% +/- 1.79%, and 93.74% +/- 1.74%, supporting 3D7G as the preferred scaffold.',
    'Ratio-comparison series',
    'dSCM/GelMA composite scaffold',
    '{"observation_tracker_ids": ["M2B-O033", "M2B-O044"], "source_experiment": {"chronicity_dpi_wpi": "In vitro material and 3-day cell assays", "control_type": "Ratio-comparison series", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P020-E001", "figure_ref": "Publisher full-text snapshot; scaffold optimization and MenSC viability", "injury_device": "dSCM/GelMA fabrication with 1D9G, 2D8G, 3D7G, and 4D6G ratios", "injury_model": "SCI repair scaffold design", "injury_severity": "N/A", "intervention_type": "dSCM/GelMA composite scaffold", "methods_summary": "Decellularization reduced residual DNA to 46.78 +/- 6.33 ng/mg, a 96.42% reduction versus normal spinal cord. 4D6G failed to polymerize; 1D9G, 2D8G, and 3D7G had compression moduli of 6.04 +/- 0.68, 4.9 +/- 0.14, and 4.01 +/- 0.32 Pa, and MenSC viability after 3 days reached 85.96% +/- 2.7%, 87.17% +/- 1.79%, and 93.74% +/- 1.74%, supporting 3D7G as the preferred scaffold.", "paper_id": "M2A-P020", "sex": "N/A", "species": "Scaffold system / human MenSC culture", "strain": "Rat dSCM source plus human menstrual blood-derived stem cells", "vertebral_level": "N/A"}, "source_experiment_tracker_id": "M2A-P020-E001", "source_paper_tracker_id": "M2A-P020", "tracker_key": "M2A-P020::M2A-P020-E001"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P020'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P020::M2A-P020-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract',
    'Tracker experiment M2A-P020-E002',
    'All five treatment groups improved relative to injury, but the MenSC-loaded DSCG/GelMA scaffold produced the strongest functional recovery, with significant group differences at 4 and 6 weeks and concurrent histologic evidence of enhanced repair versus scaffold-only or MenSC-only conditions.',
    'GelMA, DSCG, DSCG-GelMA, MenSC, and MenSC-loaded DSCG/GelMA comparisons',
    'MenSC-encapsulated dSCM/GelMA scaffold',
    '{"observation_tracker_ids": ["M2B-O067"], "source_experiment": {"chronicity_dpi_wpi": "BBB weeks 1-8", "control_type": "GelMA, DSCG, DSCG-GelMA, MenSC, and MenSC-loaded DSCG/GelMA comparisons", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P020-E002", "figure_ref": "Publisher full-text snapshot; transection repair comparison", "injury_device": "T10 complete transection with 2 mm cord removal followed by material or cell implantation", "injury_model": "Complete transection SCI", "injury_severity": "Complete transection; 2 mm gap", "intervention_type": "MenSC-encapsulated dSCM/GelMA scaffold", "methods_summary": "All five treatment groups improved relative to injury, but the MenSC-loaded DSCG/GelMA scaffold produced the strongest functional recovery, with significant group differences at 4 and 6 weeks and concurrent histologic evidence of enhanced repair versus scaffold-only or MenSC-only conditions.", "paper_id": "M2A-P020", "sex": "UNKNOWN", "species": "Rattus norvegicus", "strain": "Rat", "vertebral_level": "T10"}, "source_experiment_tracker_id": "M2A-P020-E002", "source_paper_tracker_id": "M2A-P020", "tracker_key": "M2A-P020::M2A-P020-E002"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P020'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P020::M2A-P020-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract',
    'Tracker experiment M2A-P021-E001',
    'A 100-G field aligned hydrogel fibers, with 0.10 wt% magnetic particles sufficient for consistent orientation. NPCs cultured on aligned hMSC-seeded hydrogels showed greater axon orientation and elongation after 4 days than on unaligned controls.',
    'Unaligned and magnetic-particle dose comparisons',
    'Magnetically aligned self-assembling peptide hydrogel',
    '{"observation_tracker_ids": ["M2B-O026"], "source_experiment": {"chronicity_dpi_wpi": "Four-day in vitro neurite assay", "control_type": "Unaligned and magnetic-particle dose comparisons", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P021-E001", "figure_ref": "Publisher full-text snapshot; magnetic alignment and neurite-guidance assays", "injury_device": "RADA16I hydrogels in 2 x 2 x 2 mm chambers with 0.01, 0.05, or 0.10 wt% magnetic particles polymerized under a 100-G field; hMSCs at 7.5 x 10^6 cells/mL", "injury_model": "Axon-infiltration model", "injury_severity": "N/A", "intervention_type": "Magnetically aligned self-assembling peptide hydrogel", "methods_summary": "A 100-G field aligned hydrogel fibers, with 0.10 wt% magnetic particles sufficient for consistent orientation. NPCs cultured on aligned hMSC-seeded hydrogels showed greater axon orientation and elongation after 4 days than on unaligned controls.", "paper_id": "M2A-P021", "sex": "N/A", "species": "In vitro hydrogel/hMSC/NPC system", "strain": "hMSCs embedded in RADA16I plus surface NPCs", "vertebral_level": "N/A"}, "source_experiment_tracker_id": "M2A-P021-E001", "source_paper_tracker_id": "M2A-P021", "tracker_key": "M2A-P021::M2A-P021-E001"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P021'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P021::M2A-P021-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract',
    'Tracker experiment M2A-P021-E002',
    'The aligned hMSC-seeded group increased Tuj-positive alignment, CGRP-positive regeneration, and GAP43 signal relative to comparison groups, while 5-HT differences were not significant. ED-1, GFAP, and injury-area measures were also quantified, so this is an early histology-focused rather than long-term functional endpoint.',
    'Acellular aligned, hMSC unaligned, and hMSC aligned comparisons',
    'Magnetically aligned hMSC-seeded injectable peptide hydrogel',
    '{"observation_tracker_ids": ["M2B-O068"], "source_experiment": {"chronicity_dpi_wpi": "Two weeks post-injection", "control_type": "Acellular aligned, hMSC unaligned, and hMSC aligned comparisons", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P021-E002", "figure_ref": "Publisher full-text snapshot; cervical contusion histology", "injury_device": "Two weeks after cervical contusion, injectable hydrogel was delivered under rostral-caudal 100-G alignment as acellular plus field, hMSC without field, or hMSC plus field", "injury_model": "Cervical contusion SCI", "injury_severity": "Contusion SCI", "intervention_type": "Magnetically aligned hMSC-seeded injectable peptide hydrogel", "methods_summary": "The aligned hMSC-seeded group increased Tuj-positive alignment, CGRP-positive regeneration, and GAP43 signal relative to comparison groups, while 5-HT differences were not significant. ED-1, GFAP, and injury-area measures were also quantified, so this is an early histology-focused rather than long-term functional endpoint.", "paper_id": "M2A-P021", "sex": "UNKNOWN", "species": "Rattus norvegicus", "strain": "Rat", "vertebral_level": "Cervical"}, "source_experiment_tracker_id": "M2A-P021-E002", "source_paper_tracker_id": "M2A-P021", "tracker_key": "M2A-P021::M2A-P021-E002"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P021'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P021::M2A-P021-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract',
    'Tracker experiment M2A-P022-E001',
    'DBM decellularization reduced residual DNA to 17.501 ng/g, indicating 99.25% removal of cellular material. The optimized hydrogel used 5 mg DBM, 200 microgram PDRN, and 1 x 10^8 TI-EV particles with NPCs, and the full DBM/PDRN/TI-EV@Gel combination increased NPC neurite length by 203.1% over gel alone while increasing TUJ1/MAP2 double-positive differentiation.',
    'Component-combination comparison',
    'DBM/PDRN/TI-EV/NPC@Gel composite scaffold',
    '{"observation_tracker_ids": ["M2B-O034", "M2B-O045"], "source_experiment": {"chronicity_dpi_wpi": "In vitro viability and differentiation; 28-day in vivo design", "control_type": "Component-combination comparison", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P022-E001", "figure_ref": "Publisher full-text snapshot; hydrogel bioactive-component optimization", "injury_device": "HA hydrogel with DBM, PDRN, TI-EVs, and NPCs", "injury_model": "SCI repair scaffold design", "injury_severity": "N/A", "intervention_type": "DBM/PDRN/TI-EV/NPC@Gel composite scaffold", "methods_summary": "DBM decellularization reduced residual DNA to 17.501 ng/g, indicating 99.25% removal of cellular material. The optimized hydrogel used 5 mg DBM, 200 microgram PDRN, and 1 x 10^8 TI-EV particles with NPCs, and the full DBM/PDRN/TI-EV@Gel combination increased NPC neurite length by 203.1% over gel alone while increasing TUJ1/MAP2 double-positive differentiation.", "paper_id": "M2A-P022", "sex": "N/A", "species": "Scaffold system / rat SCI context", "strain": "H9 hESC-derived NPCs in vitro", "vertebral_level": "N/A"}, "source_experiment_tracker_id": "M2A-P022-E001", "source_paper_tracker_id": "M2A-P022", "tracker_key": "M2A-P022::M2A-P022-E001"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P022'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P022::M2A-P022-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract',
    'Tracker experiment M2A-P022-E002',
    'Rats were assigned to sham (n=6), SCI (n=22), DBM@Gel (n=15), DBM/PDRN@Gel (n=17), DBM/PDRN/TI-EV@Gel (n=14), and DBM/PDRN/TI-EV/NPC@Gel (n=12). The full combination most strongly reduced CD68, HMGB1, Iba-1, IL-1beta, and cleaved caspase-3, increased GDNF and NGF, and raised TUJ1, VGAT, NF, NeuN, NG2, MBP, and myelination at 28 days while producing the strongest BBB recovery.',
    'SCI, DBM@Gel, DBM/PDRN@Gel, and DBM/PDRN/TI-EV@Gel comparisons',
    'DBM/PDRN/TI-EV/NPC@Gel injectable bioactive hydrogel',
    '{"observation_tracker_ids": ["M2B-O069"], "source_experiment": {"chronicity_dpi_wpi": "Days 1, 4, 7, 10, 14, 21, and 28", "control_type": "SCI, DBM@Gel, DBM/PDRN@Gel, and DBM/PDRN/TI-EV@Gel comparisons", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P022-E002", "figure_ref": "Publisher full-text snapshot; complete-transection multimodal repair outcomes", "injury_device": "1 mm T10 transection followed by 10 microL lesion injection plus 10 microL rostral and caudal support gel", "injury_model": "Complete transection SCI", "injury_severity": "Complete transection; 1 mm gap", "intervention_type": "DBM/PDRN/TI-EV/NPC@Gel injectable bioactive hydrogel", "methods_summary": "Rats were assigned to sham (n=6), SCI (n=22), DBM@Gel (n=15), DBM/PDRN@Gel (n=17), DBM/PDRN/TI-EV@Gel (n=14), and DBM/PDRN/TI-EV/NPC@Gel (n=12). The full combination most strongly reduced CD68, HMGB1, Iba-1, IL-1beta, and cleaved caspase-3, increased GDNF and NGF, and raised TUJ1, VGAT, NF, NeuN, NG2, MBP, and myelination at 28 days while producing the strongest BBB recovery.", "paper_id": "M2A-P022", "sex": "Female", "species": "Rattus norvegicus", "strain": "Female Sprague-Dawley, 10 weeks, 220-260 g", "vertebral_level": "T10"}, "source_experiment_tracker_id": "M2A-P022-E002", "source_paper_tracker_id": "M2A-P022", "tracker_key": "M2A-P022::M2A-P022-E002"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P022'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P022::M2A-P022-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract',
    'Tracker experiment M2A-P023-E001',
    'Curcumin-loaded PLGA nanoparticles achieved 80.3 +/- 4.2% encapsulation efficiency and 19.6 +/- 2.5% drug loading, with sustained release through 192 hours. Gelatin/alginate scaffolds showed slower degradation than gelatin after day 12, supported hEnSC adhesion, and nanocurcumin hydrogel increased hEnSC proliferation more than free-curcumin hydrogel by days 3 and 7.',
    'Curcumin-loaded vs blank scaffold comparison',
    'Gelatin/alginate hydrogel + hEnSC + curcumin-loaded PLGA nanoparticles',
    '{"observation_tracker_ids": ["M2B-O035"], "source_experiment": {"chronicity_dpi_wpi": "In vitro release through 192 hours; scaffold degradation through 28 days", "control_type": "Curcumin-loaded vs blank scaffold comparison", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P023-E001", "figure_ref": "Publisher full-text snapshot; nanoparticle and scaffold characterization with hEnSC viability", "injury_device": "Gelatin/alginate hydrogel with curcumin-loaded PLGA nanoparticles", "injury_model": "SCI repair scaffold design", "injury_severity": "N/A", "intervention_type": "Gelatin/alginate hydrogel + hEnSC + curcumin-loaded PLGA nanoparticles", "methods_summary": "Curcumin-loaded PLGA nanoparticles achieved 80.3 +/- 4.2% encapsulation efficiency and 19.6 +/- 2.5% drug loading, with sustained release through 192 hours. Gelatin/alginate scaffolds showed slower degradation than gelatin after day 12, supported hEnSC adhesion, and nanocurcumin hydrogel increased hEnSC proliferation more than free-curcumin hydrogel by days 3 and 7.", "paper_id": "M2A-P023", "sex": "N/A", "species": "Scaffold system / rat SCI context", "strain": "Human endometrial stem cells", "vertebral_level": "N/A"}, "source_experiment_tracker_id": "M2A-P023-E001", "source_paper_tracker_id": "M2A-P023", "tracker_key": "M2A-P023::M2A-P023-E001"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P023'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P023::M2A-P023-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract',
    'Tracker experiment M2A-P023-E002',
    'Six groups were studied: sham, SCI, hydrogel, hEnSC/hydrogel, nanocurcumin/hydrogel, and hEnSC plus nanocurcumin/hydrogel. The combination group reached BBB 15.5 +/- 1.05 at week 7 versus 14.16 +/- 0.75 for nanocurcumin alone and remained highest through week 10, while also showing the best H&E white/gray matter preservation, Luxol fast blue myelinated-fiber recovery, and NF200-positive nerve-fiber regeneration.',
    'SCI, hydrogel-only, hEnSC/hydrogel, and nanocurcumin/hydrogel controls',
    'hEnSC plus nanocurcumin gelatin/alginate hydrogel',
    '{"observation_tracker_ids": ["M2B-O070"], "source_experiment": {"chronicity_dpi_wpi": "Weekly BBB through 10 weeks; histology after terminal perfusion", "control_type": "SCI, hydrogel-only, hEnSC/hydrogel, and nanocurcumin/hydrogel controls", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P023-E002", "figure_ref": "Publisher full-text snapshot; delayed post-contusion hydrogel repair comparison", "injury_device": "10 g, 12.5 mm weight-drop contusion at T8-T9 followed by delayed 50 microL injection at 1 week", "injury_model": "Moderate contusion SCI", "injury_severity": "Contusion", "intervention_type": "hEnSC plus nanocurcumin gelatin/alginate hydrogel", "methods_summary": "Six groups were studied: sham, SCI, hydrogel, hEnSC/hydrogel, nanocurcumin/hydrogel, and hEnSC plus nanocurcumin/hydrogel. The combination group reached BBB 15.5 +/- 1.05 at week 7 versus 14.16 +/- 0.75 for nanocurcumin alone and remained highest through week 10, while also showing the best H&E white/gray matter preservation, Luxol fast blue myelinated-fiber recovery, and NF200-positive nerve-fiber regeneration.", "paper_id": "M2A-P023", "sex": "Male", "species": "Rattus norvegicus", "strain": "Adult male Wistar, 220-250 g, n=6/group", "vertebral_level": "T8-T9"}, "source_experiment_tracker_id": "M2A-P023-E002", "source_paper_tracker_id": "M2A-P023", "tracker_key": "M2A-P023::M2A-P023-E002"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P023'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P023::M2A-P023-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Figs. 3-6',
    'Tracker experiment M2A-P024-E001',
    'hAECs attached uniformly; scaffold and/or Noggin increased FOX3, Calca, and MBP expression, while scaffold increased GFAP. Chitosan loaded 22.6% Noggin with 75.3% entrapment efficiency; 28.5% of incorporated Noggin released over 12 days.',
    'Scaffold/cue comparison',
    'Noggin-loaded nanochitosan/polypyrrole-alginate conductive scaffold + hAEC',
    '{"observation_tracker_ids": ["M2B-O036"], "source_experiment": {"chronicity_dpi_wpi": "1 and 3 weeks", "control_type": "Scaffold/cue comparison", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P024-E001", "figure_ref": "Figs. 3-6; SEM/qPCR/release", "injury_device": "Conductive scaffold fabrication", "injury_model": "In vitro scaffold-cell differentiation model", "injury_severity": "N/A", "intervention_type": "Noggin-loaded nanochitosan/polypyrrole-alginate conductive scaffold + hAEC", "methods_summary": "hAECs attached uniformly; scaffold and/or Noggin increased FOX3, Calca, and MBP expression, while scaffold increased GFAP. Chitosan loaded 22.6% Noggin with 75.3% entrapment efficiency; 28.5% of incorporated Noggin released over 12 days.", "paper_id": "M2A-P024", "sex": "N/A", "species": "hAEC culture / scaffold system", "strain": "Human amniotic epithelial cells", "vertebral_level": "N/A"}, "source_experiment_tracker_id": "M2A-P024-E001", "source_paper_tracker_id": "M2A-P024", "tracker_key": "M2A-P024::M2A-P024-E001"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P024'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P024::M2A-P024-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Figs. 7-10',
    'Tracker experiment M2A-P024-E002',
    'Six groups (n=6) were followed for 4 weeks. Noggin+hAEC scaffold achieved BBB 14.0 +/- 1.43 versus 9.5 +/- 1.52 lesion control; scaffold+hAEC 13.5 +/- 0.7 and Noggin scaffold 12.5 +/- 0.51. hAEC-containing groups reduced Iba1/GFAP and increased beta-tubulin/MBP; DII-hAECs remained alive at 4 weeks.',
    'Empty lesion; scaffold; hAEC; Noggin scaffold',
    'Noggin-loaded conductive scaffold +/- DII-hAECs',
    '{"observation_tracker_ids": ["M2B-O071"], "source_experiment": {"chronicity_dpi_wpi": "1 and 4 weeks", "control_type": "Empty lesion; scaffold; hAEC; Noggin scaffold", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P024-E002", "figure_ref": "Figs. 7-10; BBB/qPCR/IHC", "injury_device": "Surgical hemisection", "injury_model": "Right T10-T11 hemisection, 2 x 4 mm cavity", "injury_severity": "Right hemisection", "intervention_type": "Noggin-loaded conductive scaffold +/- DII-hAECs", "methods_summary": "Six groups (n=6) were followed for 4 weeks. Noggin+hAEC scaffold achieved BBB 14.0 +/- 1.43 versus 9.5 +/- 1.52 lesion control; scaffold+hAEC 13.5 +/- 0.7 and Noggin scaffold 12.5 +/- 0.51. hAEC-containing groups reduced Iba1/GFAP and increased beta-tubulin/MBP; DII-hAECs remained alive at 4 weeks.", "paper_id": "M2A-P024", "sex": "Male", "species": "Rattus norvegicus", "strain": "Wistar", "vertebral_level": "T10-T11"}, "source_experiment_tracker_id": "M2A-P024-E002", "source_paper_tracker_id": "M2A-P024", "tracker_key": "M2A-P024::M2A-P024-E002"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P024'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P024::M2A-P024-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Figs. 1-3',
    'Tracker experiment M2A-P025-E001',
    'Adult female rats received fibrin beads containing heparin-binding delivery system and NT-3. F-DS-NT3 1000 ng/mL produced 10.4% overall Tuj1 fiber density versus 3% saline and approximately 6-7% fibrin controls; white-matter-border GFAP was reduced by fibrin scaffolds.',
    'Saline, fibrin-only, delivery-system-only, unmodified NT-3 fibrin',
    'Fibrin scaffold + controlled NT-3 delivery',
    '{"observation_tracker_ids": ["M2B-O012"], "source_experiment": {"chronicity_dpi_wpi": "Immediate implantation; 9-day histology", "control_type": "Saline, fibrin-only, delivery-system-only, unmodified NT-3 fibrin", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P025-E001", "figure_ref": "Figs. 1-3; Tuj1/GFAP quantification", "injury_device": "Surgical T9 ablation", "injury_model": "2-mm spinal cord ablation lesion", "injury_severity": "Complete 2-mm gap", "intervention_type": "Fibrin scaffold + controlled NT-3 delivery", "methods_summary": "Adult female rats received fibrin beads containing heparin-binding delivery system and NT-3. F-DS-NT3 1000 ng/mL produced 10.4% overall Tuj1 fiber density versus 3% saline and approximately 6-7% fibrin controls; white-matter-border GFAP was reduced by fibrin scaffolds.", "paper_id": "M2A-P025", "sex": "Female", "species": "Rattus norvegicus", "strain": "Long Evans", "vertebral_level": "T9"}, "source_experiment_tracker_id": "M2A-P025-E001", "source_paper_tracker_id": "M2A-P025", "tracker_key": "M2A-P025::M2A-P025-E001"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P025'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P025::M2A-P025-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Figs. 5-7',
    'Tracker experiment M2A-P025-E002',
    'Controlled NT-3 enhanced early fiber sprouting and cell migration, but hindlimb BBB scores did not improve versus controls at 12 weeks; no treatment differences in macrophage/microglia density were observed.',
    'TBS, fibrin+NT-3, fibrin+delivery system+NT-3',
    'Fibrin/NT-3 scaffold',
    '{"observation_tracker_ids": ["M2B-O072"], "source_experiment": {"chronicity_dpi_wpi": "12 weeks post-injury", "control_type": "TBS, fibrin+NT-3, fibrin+delivery system+NT-3", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P025-E002", "figure_ref": "Figs. 5-7; BBB/ED-1/subtype staining", "injury_device": "Surgical T9 ablation", "injury_model": "2-mm spinal cord ablation lesion", "injury_severity": "Complete 2-mm gap", "intervention_type": "Fibrin/NT-3 scaffold", "methods_summary": "Controlled NT-3 enhanced early fiber sprouting and cell migration, but hindlimb BBB scores did not improve versus controls at 12 weeks; no treatment differences in macrophage/microglia density were observed.", "paper_id": "M2A-P025", "sex": "Female", "species": "Rattus norvegicus", "strain": "Long Evans", "vertebral_level": "T9"}, "source_experiment_tracker_id": "M2A-P025-E002", "source_paper_tracker_id": "M2A-P025", "tracker_key": "M2A-P025::M2A-P025-E002"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P025'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P025::M2A-P025-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Figs. 1-7',
    'Tracker experiment M2A-P026-E001',
    'Forty rats received delayed implantation after T9 transection; HEMA-MOETACL had communicating 80-micrometer pores and was surrounded by decellularized vascular matrix.',
    'Lesion control (n=8), bFGF alone (n=10), hydrogel alone (n=10), combined (n=12)',
    'bFGF/HEMA-MOETACL hydrogel + acellular vascular matrix',
    '{"observation_tracker_ids": ["M2B-O038"], "source_experiment": {"chronicity_dpi_wpi": "Implantation 5 DPI; 8-week outcome", "control_type": "Lesion control (n=8), bFGF alone (n=10), hydrogel alone (n=10), combined (n=12)", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P026-E001", "figure_ref": "Figs. 1-2; group design", "injury_device": "T9 complete transection with 2-mm removal", "injury_model": "Complete transection SCI", "injury_severity": "Complete transection", "intervention_type": "bFGF/HEMA-MOETACL hydrogel + acellular vascular matrix", "methods_summary": "Forty rats received delayed implantation after T9 transection; HEMA-MOETACL had communicating 80-micrometer pores and was surrounded by decellularized vascular matrix.", "paper_id": "M2A-P026", "sex": "Mixed/UNKNOWN", "species": "Rattus norvegicus", "strain": "Sprague-Dawley", "vertebral_level": "T9"}, "source_experiment_tracker_id": "M2A-P026-E001", "source_paper_tracker_id": "M2A-P026", "tracker_key": "M2A-P026::M2A-P026-E001"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P026'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P026::M2A-P026-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Figs. 3-7',
    'Tracker experiment M2A-P026-E002',
    'Combined hydrogel reduced cavitation to 2.41 +/- 0.80 mm3 and 1.28% versus 25.00 +/- 3.33 mm3 and 16.00% lesion control; it increased axon and vessel ingrowth and SSEP/MEP amplitude while shortening latency. Hydrogel alone reduced cavitation but did not show clear behavioral recovery.',
    'Lesion, bFGF-only, hydrogel-only',
    'bFGF/HEMA-MOETACL hydrogel',
    '{"observation_tracker_ids": ["M2B-O073"], "source_experiment": {"chronicity_dpi_wpi": "8 weeks post-implantation", "control_type": "Lesion, bFGF-only, hydrogel-only", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P026-E002", "figure_ref": "Figs. 3-7; BBB/SSEP/MEP/histology", "injury_device": "T9 complete transection", "injury_model": "Complete transection SCI", "injury_severity": "Complete transection", "intervention_type": "bFGF/HEMA-MOETACL hydrogel", "methods_summary": "Combined hydrogel reduced cavitation to 2.41 +/- 0.80 mm3 and 1.28% versus 25.00 +/- 3.33 mm3 and 16.00% lesion control; it increased axon and vessel ingrowth and SSEP/MEP amplitude while shortening latency. Hydrogel alone reduced cavitation but did not show clear behavioral recovery.", "paper_id": "M2A-P026", "sex": "Mixed/UNKNOWN", "species": "Rattus norvegicus", "strain": "Sprague-Dawley", "vertebral_level": "T9"}, "source_experiment_tracker_id": "M2A-P026-E002", "source_paper_tracker_id": "M2A-P026", "tracker_key": "M2A-P026::M2A-P026-E002"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P026'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P026::M2A-P026-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract',
    'Tracker experiment M2A-P027-E001',
    'Structured HA scaffolds had an outer diameter of about 3 mm and multiple long axially oriented channels about 50 micrometers wide. PLGA microspheres measuring 0.5-1.0 micrometers released BDNF or VEGF for at least 14 days, with peak levels of about 900 pg/mL BDNF and 500 pg/mL VEGF; day-14 in vivo factor levels were approximately 2-fold higher in scaffold+microsphere implants than in HA scaffold alone (P < 0.001, n = 6).',
    'Material/cargo comparison',
    'Structured HA hydrogel + anti-NgR + BDNF/VEGF PLGA microspheres',
    '{"observation_tracker_ids": ["M2B-O013"], "source_experiment": {"chronicity_dpi_wpi": "At least 14 days release; day-14 in vivo factor assay", "control_type": "Material/cargo comparison", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P027-E001", "figure_ref": "Publisher full-text snapshot; scaffold geometry and microsphere release characterization", "injury_device": "HA scaffold fabrication", "injury_model": "SCI repair scaffold design", "injury_severity": "N/A", "intervention_type": "Structured HA hydrogel + anti-NgR + BDNF/VEGF PLGA microspheres", "methods_summary": "Structured HA scaffolds had an outer diameter of about 3 mm and multiple long axially oriented channels about 50 micrometers wide. PLGA microspheres measuring 0.5-1.0 micrometers released BDNF or VEGF for at least 14 days, with peak levels of about 900 pg/mL BDNF and 500 pg/mL VEGF; day-14 in vivo factor levels were approximately 2-fold higher in scaffold+microsphere implants than in HA scaffold alone (P < 0.001, n = 6).", "paper_id": "M2A-P027", "sex": "N/A", "species": "Scaffold system / rat SCI context", "strain": "N/A", "vertebral_level": "N/A"}, "source_experiment_tracker_id": "M2A-P027-E001", "source_paper_tracker_id": "M2A-P027", "tracker_key": "M2A-P027::M2A-P027-E001"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P027'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P027::M2A-P027-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract',
    'Tracker experiment M2A-P027-E002',
    'The HA+PLGA scaffold integrated without cyst formation, preserved longitudinal channels, and improved BBB scores from 2 weeks onward to about 13 by 10 weeks. At 8 weeks it reduced Iba1, GFAP, and CSPG burden while increasing vWF-positive vessel counts and NF-160-positive longitudinal axons relative to untreated injury, with CatWalk weight-distribution measures also shifting toward normal.',
    'Untreated injury and HA-alone scaffold comparisons',
    'HA+PLGA multi-cargo scaffold',
    '{"observation_tracker_ids": ["M2B-O074"], "source_experiment": {"chronicity_dpi_wpi": "2, 4, 8, and 10 weeks", "control_type": "Untreated injury and HA-alone scaffold comparisons", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P027-E002", "figure_ref": "Publisher full-text snapshot; dorsal hemisection repair outcomes", "injury_device": "Dorsal hemisection with scaffold implantation", "injury_model": "Dorsal hemisection SCI", "injury_severity": "Hemisection; 3.0 mm length and 1.5 mm depth removed", "intervention_type": "HA+PLGA multi-cargo scaffold", "methods_summary": "The HA+PLGA scaffold integrated without cyst formation, preserved longitudinal channels, and improved BBB scores from 2 weeks onward to about 13 by 10 weeks. At 8 weeks it reduced Iba1, GFAP, and CSPG burden while increasing vWF-positive vessel counts and NF-160-positive longitudinal axons relative to untreated injury, with CatWalk weight-distribution measures also shifting toward normal.", "paper_id": "M2A-P027", "sex": "UNKNOWN", "species": "Rattus norvegicus", "strain": "Rat", "vertebral_level": "T9-T10"}, "source_experiment_tracker_id": "M2A-P027-E002", "source_paper_tracker_id": "M2A-P027", "tracker_key": "M2A-P027::M2A-P027-E002"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P027'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P027::M2A-P027-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract',
    'Tracker experiment M2A-P028-E001',
    'Rats with postoperative day-1 BBB scores below 5 were assigned to hemisection alone, hydrogel + empty spheres, or hydrogel + NT-3 spheres. Both hydrogel groups showed significantly higher BBB scores than hemisection alone at 4 and 6 weeks (n = 9-10), but NT-3 did not clearly outperform hydrogel alone on locomotor recovery.',
    'SCI alone and hydrogel-only comparison',
    'Injectable collagen hydrogel +/- NT-3',
    '{"observation_tracker_ids": ["M2B-O039"], "source_experiment": {"chronicity_dpi_wpi": "Postoperative day 1 screen; 4 and 6 weeks BBB", "control_type": "SCI alone and hydrogel-only comparison", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P028-E001", "figure_ref": "Publisher full-text snapshot; hemisection treatment groups and BBB outcome", "injury_device": "Hemisection with immediate in situ hydrogel delivery", "injury_model": "Hemisection SCI", "injury_severity": "Hemisection", "intervention_type": "Injectable collagen hydrogel +/- NT-3", "methods_summary": "Rats with postoperative day-1 BBB scores below 5 were assigned to hemisection alone, hydrogel + empty spheres, or hydrogel + NT-3 spheres. Both hydrogel groups showed significantly higher BBB scores than hemisection alone at 4 and 6 weeks (n = 9-10), but NT-3 did not clearly outperform hydrogel alone on locomotor recovery.", "paper_id": "M2A-P028", "sex": "UNKNOWN", "species": "Rattus norvegicus", "strain": "Rat", "vertebral_level": "UNKNOWN"}, "source_experiment_tracker_id": "M2A-P028-E001", "source_paper_tracker_id": "M2A-P028", "tracker_key": "M2A-P028::M2A-P028-E001"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P028'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P028::M2A-P028-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract',
    'Tracker experiment M2A-P028-E002',
    'Both hydrogel groups reduced NG2-positive scar area at 1 and 6 weeks and lowered early Iba-1 burden, whereas GFAP differences were not significant. The NT-3-loaded group specifically increased betaIII-tubulin-positive axonal or neuronal staining and further reduced collagen deposition, indicating added local repair effects without a clear extra BBB benefit.',
    'NT-3 scaffold versus hydrogel-only comparison',
    'NT-3 collagen scaffold',
    '{"observation_tracker_ids": ["M2B-O075"], "source_experiment": {"chronicity_dpi_wpi": "1 and 6 weeks; early inflammatory window around 7 days", "control_type": "NT-3 scaffold versus hydrogel-only comparison", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P028-E002", "figure_ref": "Publisher full-text snapshot; scar, inflammation, and axonal-marker outcomes", "injury_device": "Hemisection with immediate hydrogel treatment", "injury_model": "Hemisection SCI", "injury_severity": "Hemisection", "intervention_type": "NT-3 collagen scaffold", "methods_summary": "Both hydrogel groups reduced NG2-positive scar area at 1 and 6 weeks and lowered early Iba-1 burden, whereas GFAP differences were not significant. The NT-3-loaded group specifically increased betaIII-tubulin-positive axonal or neuronal staining and further reduced collagen deposition, indicating added local repair effects without a clear extra BBB benefit.", "paper_id": "M2A-P028", "sex": "UNKNOWN", "species": "Rattus norvegicus", "strain": "Rat", "vertebral_level": "UNKNOWN"}, "source_experiment_tracker_id": "M2A-P028-E002", "source_paper_tracker_id": "M2A-P028", "tracker_key": "M2A-P028::M2A-P028-E002"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P028'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P028::M2A-P028-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract',
    'Tracker experiment M2A-P029-E001',
    'Two primate studies compared 12 scaffold-implanted and 12 non-implanted monkeys after lateral hemisection. Porous PLGA-PLL scaffolds were engineered to resorb over 12 weeks and were inserted to fill the 8-10 mm lesion gap immediately after hemisection.',
    'Non-implanted control',
    'Porous PLGA/poly-L-lysine biodegradable scaffold',
    '{"observation_tracker_ids": ["M2B-O003"], "source_experiment": {"chronicity_dpi_wpi": "Two studies with weekly follow-up to 12 WPI", "control_type": "Non-implanted control", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P029-E001", "figure_ref": "Publisher full-text snapshot", "injury_device": "T9-T10 lateral hemisection with immediate scaffold implantation", "injury_model": "Partial or complete lateral thoracic hemisection SCI", "injury_severity": "Partial/complete hemisection", "intervention_type": "Porous PLGA/poly-L-lysine biodegradable scaffold", "methods_summary": "Two primate studies compared 12 scaffold-implanted and 12 non-implanted monkeys after lateral hemisection. Porous PLGA-PLL scaffolds were engineered to resorb over 12 weeks and were inserted to fill the 8-10 mm lesion gap immediately after hemisection.", "paper_id": "M2A-P029", "sex": "Male", "species": "Chlorocebus sabaeus", "strain": "Adult male African green monkeys, 5-10 years, 4.5-7.0 kg", "vertebral_level": "T9-T10"}, "source_experiment_tracker_id": "M2A-P029-E001", "source_paper_tracker_id": "M2A-P029", "tracker_key": "M2A-P029::M2A-P029-E001"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P029'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P029::M2A-P029-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract',
    'Tracker experiment M2A-P029-E002',
    'In the complete hemisection subgroup, scaffold-implanted monkeys showed significantly better kinematics recovery at 12 weeks together with appositional remodeling tissue, fewer inner-layer GFAP-positive astrocytes, and neurofilament, GAP43, and MBP-positive elements within the remodeled zone.',
    'Scaffold vs non-implanted control',
    'Porous biodegradable scaffold',
    '{"observation_tracker_ids": ["M2B-O076"], "source_experiment": {"chronicity_dpi_wpi": "Weekly locomotor assessment through 12 WPI with terminal histology", "control_type": "Scaffold vs non-implanted control", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P029-E002", "figure_ref": "Publisher full-text snapshot", "injury_device": "T9-T10 lateral hemisection with treadmill kinematics and EMG follow-up", "injury_model": "Thoracic lateral hemisection SCI", "injury_severity": "Complete hemisection subgroup emphasized", "intervention_type": "Porous biodegradable scaffold", "methods_summary": "In the complete hemisection subgroup, scaffold-implanted monkeys showed significantly better kinematics recovery at 12 weeks together with appositional remodeling tissue, fewer inner-layer GFAP-positive astrocytes, and neurofilament, GAP43, and MBP-positive elements within the remodeled zone.", "paper_id": "M2A-P029", "sex": "Male", "species": "Chlorocebus sabaeus", "strain": "Adult male African green monkeys", "vertebral_level": "T9-T10"}, "source_experiment_tracker_id": "M2A-P029-E002", "source_paper_tracker_id": "M2A-P029", "tracker_key": "M2A-P029::M2A-P029-E002"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P029'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P029::M2A-P029-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Full text',
    'Tracker experiment M2A-P030-E002',
    'NF-GS improved Olby (11.85 +/- 0.64 vs 9.29 +/- 1.48), CMEP amplitude/latency, IBA1 burden, NF-fiber density, host-cell migration, vessel profiles, synapse-like structures, and occasional MBP+ fibers; GFAP scar density was not significantly different.',
    'NF-GS vs F-GS',
    'NT-3/fibroin gelatin scaffold',
    '{"observation_tracker_ids": ["M2B-O040", "M2B-O077"], "source_experiment": {"chronicity_dpi_wpi": "Four weeks after graft", "control_type": "NF-GS vs F-GS", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P030-E002", "figure_ref": "Full text (PMC6055812)", "injury_device": "Hemisection", "injury_model": "Hemisection SCI", "injury_severity": "Hemisection", "intervention_type": "NT-3/fibroin gelatin scaffold", "methods_summary": "NF-GS improved Olby (11.85 +/- 0.64 vs 9.29 +/- 1.48), CMEP amplitude/latency, IBA1 burden, NF-fiber density, host-cell migration, vessel profiles, synapse-like structures, and occasional MBP+ fibers; GFAP scar density was not significantly different.", "paper_id": "M2A-P030", "sex": "Right T10 hemisection, 4 mm removed", "species": "Canis familiaris", "strain": "Female Beagle, 7 months, n=7/group", "vertebral_level": "Acute"}, "source_experiment_tracker_id": "M2A-P030-E002", "source_paper_tracker_id": "M2A-P030", "tracker_key": "M2A-P030::M2A-P030-E002"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P030'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P030::M2A-P030-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract',
    'Tracker experiment M2A-P031-E001',
    'Electrospun PCL/PSA/MP nanofibers combined PCL structural support, PSA surface chemistry, and methylprednisolone cargo; SEM and FTIR confirmed nanofiber morphology and incorporation of both PSA and drug-associated peaks.',
    'Material/drug characterization',
    'PCL/PSA/MP nanofiber scaffold',
    '{"observation_tracker_ids": ["M2B-O041"], "source_experiment": {"chronicity_dpi_wpi": "Material characterization before implantation", "control_type": "Material/drug characterization", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P031-E001", "figure_ref": "Publisher full-text snapshot", "injury_device": "Electrospun PCL/PSA nanofiber scaffold fabrication with methylprednisolone loading", "injury_model": "SCI repair scaffold design", "injury_severity": "N/A", "intervention_type": "PCL/PSA/MP nanofiber scaffold", "methods_summary": "Electrospun PCL/PSA/MP nanofibers combined PCL structural support, PSA surface chemistry, and methylprednisolone cargo; SEM and FTIR confirmed nanofiber morphology and incorporation of both PSA and drug-associated peaks.", "paper_id": "M2A-P031", "sex": "N/A", "species": "Scaffold system / rat SCI context", "strain": "N/A", "vertebral_level": "N/A"}, "source_experiment_tracker_id": "M2A-P031-E001", "source_paper_tracker_id": "M2A-P031", "tracker_key": "M2A-P031::M2A-P031-E001"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P031'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P031::M2A-P031-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract',
    'Tracker experiment M2A-P031-E002',
    'In rat transection SCI, the PCL/PSA/MP scaffold reduced TNF-alpha, IL-6, Iba1-positive microglia/macrophage activation, caspase-3-associated apoptosis, demyelination, and GFAP while increasing NF-200 staining and BBB locomotor recovery relative to comparator groups.',
    'Scaffold/drug comparison',
    'PCL/PSA/MP nanofiber scaffold',
    '{"observation_tracker_ids": ["M2B-O078"], "source_experiment": {"chronicity_dpi_wpi": "Post-implant interval in full text not yet normalized", "control_type": "Scaffold/drug comparison", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P031-E002", "figure_ref": "Publisher full-text snapshot", "injury_device": "Transection with lesion-area scaffold transplantation", "injury_model": "Spinal cord transection SCI", "injury_severity": "Transection", "intervention_type": "PCL/PSA/MP nanofiber scaffold", "methods_summary": "In rat transection SCI, the PCL/PSA/MP scaffold reduced TNF-alpha, IL-6, Iba1-positive microglia/macrophage activation, caspase-3-associated apoptosis, demyelination, and GFAP while increasing NF-200 staining and BBB locomotor recovery relative to comparator groups.", "paper_id": "M2A-P031", "sex": "UNKNOWN", "species": "Rattus norvegicus", "strain": "Rat", "vertebral_level": "UNKNOWN"}, "source_experiment_tracker_id": "M2A-P031-E002", "source_paper_tracker_id": "M2A-P031", "tracker_key": "M2A-P031::M2A-P031-E002"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P031'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P031::M2A-P031-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Full text',
    'Tracker experiment M2A-P032-E001',
    'P-ECM:HA reduced CD11b, ED1, GFAP, and CSPG staining and increased Tuj1 area; F-ECM did not reproduce the benefit. V2a aggregates survived in HA and P-ECM:HA, but this histology study did not test locomotion or functional integration.',
    'HA, F-ECM, P-ECM, V2a-cell combinations',
    'HA hydrogel + astrocyte ECM and/or V2a interneurons',
    '{"observation_tracker_ids": ["M2B-O016"], "source_experiment": {"chronicity_dpi_wpi": "Two weeks after implantation (four weeks after injury)", "control_type": "HA, F-ECM, P-ECM, V2a-cell combinations", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P032-E001", "figure_ref": "Full text (PMC5851469)", "injury_device": "Experimental SCI", "injury_model": "SCI", "injury_severity": "Dorsal hemisection", "intervention_type": "HA hydrogel + astrocyte ECM and/or V2a interneurons", "methods_summary": "P-ECM:HA reduced CD11b, ED1, GFAP, and CSPG staining and increased Tuj1 area; F-ECM did not reproduce the benefit. V2a aggregates survived in HA and P-ECM:HA, but this histology study did not test locomotion or functional integration.", "paper_id": "M2A-P032", "sex": "T8 dorsal hemisection; treatment 2 weeks later", "species": "Rattus norvegicus", "strain": "Adult rats, acellular groups n=7-8; cell groups n=7-8", "vertebral_level": "Subacute"}, "source_experiment_tracker_id": "M2A-P032-E001", "source_paper_tracker_id": "M2A-P032", "tracker_key": "M2A-P032::M2A-P032-E001"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P032'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P032::M2A-P032-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Full text',
    'Tracker experiment M2A-P032-E002',
    'P-ECM reduced scar and immune burden and increased neuronal-process staining; P-ECM+V2a cells increased lesion and peri-lesion Tuj1 staining, with TdTomato+ cell area 6.4 +/- 1.3% vs 3.7 +/- 0.36% P-ECM alone. Functional integration was not established.',
    'ECM subtype / cell comparison',
    'HA/astrocyte ECM hydrogel',
    '{"observation_tracker_ids": ["M2B-O079"], "source_experiment": {"chronicity_dpi_wpi": "Two weeks after implantation", "control_type": "ECM subtype / cell comparison", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P032-E002", "figure_ref": "Full text (PMC5851469)", "injury_device": "Experimental SCI", "injury_model": "SCI", "injury_severity": "Dorsal hemisection", "intervention_type": "HA/astrocyte ECM hydrogel", "methods_summary": "P-ECM reduced scar and immune burden and increased neuronal-process staining; P-ECM+V2a cells increased lesion and peri-lesion Tuj1 staining, with TdTomato+ cell area 6.4 +/- 1.3% vs 3.7 +/- 0.36% P-ECM alone. Functional integration was not established.", "paper_id": "M2A-P032", "sex": "T8 dorsal hemisection; treatment 2 weeks later", "species": "Rattus norvegicus", "strain": "Adult rats, n=7-8/group", "vertebral_level": "Subacute"}, "source_experiment_tracker_id": "M2A-P032-E002", "source_paper_tracker_id": "M2A-P032", "tracker_key": "M2A-P032::M2A-P032-E002"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P032'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P032::M2A-P032-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Figs. 1-5',
    'Tracker experiment M2A-P033-E001',
    'Rats (n=10/group) and dogs (n=5/group) received scaffold with or without hUC-MSCs. Rat BBB was higher in the cell group at 4-8 weeks; rat MEP amplitude/latency improved versus scaffold alone; canine Olby scores improved in both scaffold groups versus SCI and further with cells at 3-6 months; canine MEP also improved with cells.',
    'Sham, SCI, collagen scaffold',
    'Collagen scaffold + hUC-MSC',
    '{"observation_tracker_ids": ["M2B-O023"], "source_experiment": {"chronicity_dpi_wpi": "1 week to 8 weeks rats; 0.5-6 months dogs", "control_type": "Sham, SCI, collagen scaffold", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P033-E001", "figure_ref": "Figs. 1-5; BBB/Olby/MEP/MRI", "injury_device": "Rat T10 1.5-mm removal; canine T8-T11 3-mm removal", "injury_model": "Complete transection SCI", "injury_severity": "Complete transection", "intervention_type": "Collagen scaffold + hUC-MSC", "methods_summary": "Rats (n=10/group) and dogs (n=5/group) received scaffold with or without hUC-MSCs. Rat BBB was higher in the cell group at 4-8 weeks; rat MEP amplitude/latency improved versus scaffold alone; canine Olby scores improved in both scaffold groups versus SCI and further with cells at 3-6 months; canine MEP also improved with cells.", "paper_id": "M2A-P033", "sex": "Female", "species": "Rattus norvegicus and Canis familiaris", "strain": "Sprague-Dawley rats; Beagles", "vertebral_level": "T10 rats; T8-T11 dogs"}, "source_experiment_tracker_id": "M2A-P033-E001", "source_paper_tracker_id": "M2A-P033", "tracker_key": "M2A-P033::M2A-P033-E001"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P033'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P033::M2A-P033-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Tables 1-4; Figs. 6-8',
    'Tracker experiment M2A-P033-E002',
    'Forty patients were assigned to treatment (n=20) or control (n=20). Nine treatment patients improved ASIA A-to-B and two A-to-C; no controls improved ASIA grade. Two treatment patients gained MEP from absent baseline, 9/18 with baseline MEP improved latency/amplitude, 2/10 improved SSEP, residual urine decreased, MRI/DTI showed lesion filling/fiber continuity, and no serious treatment-associated adverse event was reported.',
    'No-implant control (n=20)',
    'Collagen scaffold + 4 x 10^7 hUC-MSC',
    '{"observation_tracker_ids": ["M2B-O080"], "source_experiment": {"chronicity_dpi_wpi": "12-month follow-up", "control_type": "No-implant control (n=20)", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P033-E002", "figure_ref": "Tables 1-4; ASIA/ADL/MEP/SSEP/MRI/DTI", "injury_device": "Clinical acute complete SCI + implantation", "injury_model": "Acute complete cervical SCI", "injury_severity": "ASIA A; C4-C7; within 21 days", "intervention_type": "Collagen scaffold + 4 x 10^7 hUC-MSC", "methods_summary": "Forty patients were assigned to treatment (n=20) or control (n=20). Nine treatment patients improved ASIA A-to-B and two A-to-C; no controls improved ASIA grade. Two treatment patients gained MEP from absent baseline, 9/18 with baseline MEP improved latency/amplitude, 2/10 improved SSEP, residual urine decreased, MRI/DTI showed lesion filling/fiber continuity, and no serious treatment-associated adverse event was reported.", "paper_id": "M2A-P033", "sex": "Mixed", "species": "Homo sapiens", "strain": "N/A", "vertebral_level": "C4-C7"}, "source_experiment_tracker_id": "M2A-P033-E002", "source_paper_tracker_id": "M2A-P033", "tracker_key": "M2A-P033::M2A-P033-E002"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P033'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P033::M2A-P033-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Full text',
    'Tracker experiment M2A-P034-E002',
    'Fully functionalized HA/PPY/PM-CURC-iNPC cap preserved beta-III-tubulin fibers, reduced GFAP-negative lesion area and PDGF expression, but iNPCs preferentially showed GFAP rather than neuronal colocalization and no treatment reduced Iba1/ED1 neuroinflammation at one week.',
    'Injury/scaffold comparison',
    'HA demilune surface-capping scaffold',
    '{"observation_tracker_ids": ["M2B-O019", "M2B-O081"], "source_experiment": {"chronicity_dpi_wpi": "One week after implantation, two weeks after injury", "control_type": "Injury/scaffold comparison", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P034-E002", "figure_ref": "Full text (PMC8698735)", "injury_device": "Experimental SCI", "injury_model": "Subacute SCI", "injury_severity": "Moderate contusion", "intervention_type": "HA demilune surface-capping scaffold", "methods_summary": "Fully functionalized HA/PPY/PM-CURC-iNPC cap preserved beta-III-tubulin fibers, reduced GFAP-negative lesion area and PDGF expression, but iNPCs preferentially showed GFAP rather than neuronal colocalization and no treatment reduced Iba1/ED1 neuroinflammation at one week.", "paper_id": "M2A-P034", "sex": "T8 moderate contusion, 200 kdyn", "species": "Rat model context", "strain": "Female Sprague-Dawley rats, n=3/group", "vertebral_level": "Subacute, 1 week post-injury"}, "source_experiment_tracker_id": "M2A-P034-E002", "source_paper_tracker_id": "M2A-P034", "tracker_key": "M2A-P034::M2A-P034-E002"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P034'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P034::M2A-P034-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Full text',
    'Tracker experiment M2A-P035-E002',
    'Cell-loaded scaffold BBB 5.667 vs empty scaffold 2.333 vs transection control 0.667; MEP amplitude reached 29.57% of normal; NF-H axons projected along channels, but inflammatory signal did not differ and mortality reduced key sample sizes.',
    'Transection control vs empty scaffold vs cell-loaded scaffold',
    'GelMA scaffold + hAEC-derived neural-like cells',
    '{"observation_tracker_ids": ["M2B-O027", "M2B-O082"], "source_experiment": {"chronicity_dpi_wpi": "Eight weeks after implantation", "control_type": "Transection control vs empty scaffold vs cell-loaded scaffold", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P035-E002", "figure_ref": "Full text (PMC9598945)", "injury_device": "Complete transection", "injury_model": "Full transection SCI", "injury_severity": "Full transection", "intervention_type": "GelMA scaffold + hAEC-derived neural-like cells", "methods_summary": "Cell-loaded scaffold BBB 5.667 vs empty scaffold 2.333 vs transection control 0.667; MEP amplitude reached 29.57% of normal; NF-H axons projected along channels, but inflammatory signal did not differ and mortality reduced key sample sizes.", "paper_id": "M2A-P035", "sex": "T10 full transection with 2 mm segment removed", "species": "Rattus norvegicus", "strain": "SCI groups n=3 for BBB analyses; n=5 for MEP groups", "vertebral_level": "Acute"}, "source_experiment_tracker_id": "M2A-P035-E002", "source_paper_tracker_id": "M2A-P035", "tracker_key": "M2A-P035::M2A-P035-E002"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P035'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P035::M2A-P035-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Full text',
    'Tracker experiment M2A-P036-E001',
    'Eight-percent SilMA with PLGA NT-3 microspheres and Ang-(1-7) was UV-crosslinked; Ang-(1-7) released >40% by day 3 and nearly all by day 7, while NT-3 release persisted through days 28-56.',
    'Release/component comparison',
    'Dual-phase SilMA hydrogel + NT-3/Ang-(1-7) PLGA microspheres',
    '{"observation_tracker_ids": ["M2B-O014"], "source_experiment": {"chronicity_dpi_wpi": "In vitro release days 1-56", "control_type": "Release/component comparison", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P036-E001", "figure_ref": "Full text (PMC11617199)", "injury_device": "SilMA hydrogel fabrication", "injury_model": "SCI repair scaffold design", "injury_severity": "N/A", "intervention_type": "Dual-phase SilMA hydrogel + NT-3/Ang-(1-7) PLGA microspheres", "methods_summary": "Eight-percent SilMA with PLGA NT-3 microspheres and Ang-(1-7) was UV-crosslinked; Ang-(1-7) released >40% by day 3 and nearly all by day 7, while NT-3 release persisted through days 28-56.", "paper_id": "M2A-P036", "sex": "N/A", "species": "Scaffold system / rodent SCI context", "strain": "N/A", "vertebral_level": "N/A"}, "source_experiment_tracker_id": "M2A-P036-E001", "source_paper_tracker_id": "M2A-P036", "tracker_key": "M2A-P036::M2A-P036-E001"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P036'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P036::M2A-P036-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Full text',
    'Tracker experiment M2A-P036-E002',
    '4D-SilMA increased Arg-1 and Tuj1, reduced iNOS and GFAP, improved cavity/tissue structure, and reached BMS 6 versus SCI/SilMA; in-vitro Ang-(1-7) and NT-3 assays used LPS-stimulated BV2 cells and mouse NSCs, so combined in-vivo component attribution remains limited.',
    'Sham vs SCI vs SilMA vs 4D-SilMA',
    'Sequential release SilMA scaffold',
    '{"observation_tracker_ids": ["M2B-O083"], "source_experiment": {"chronicity_dpi_wpi": "Eight weeks post-SCI", "control_type": "Sham vs SCI vs SilMA vs 4D-SilMA", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P036-E002", "figure_ref": "Full text (PMC11617199)", "injury_device": "Complete transection", "injury_model": "SCI", "injury_severity": "Complete transection", "intervention_type": "Sequential release SilMA scaffold", "methods_summary": "4D-SilMA increased Arg-1 and Tuj1, reduced iNOS and GFAP, improved cavity/tissue structure, and reached BMS 6 versus SCI/SilMA; in-vitro Ang-(1-7) and NT-3 assays used LPS-stimulated BV2 cells and mouse NSCs, so combined in-vivo component attribution remains limited.", "paper_id": "M2A-P036", "sex": "T10 complete 2 mm transection", "species": "Rodent model context", "strain": "Mice, n=6/group", "vertebral_level": "Acute"}, "source_experiment_tracker_id": "M2A-P036-E002", "source_paper_tracker_id": "M2A-P036", "tracker_key": "M2A-P036::M2A-P036-E002"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P036'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P036::M2A-P036-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract',
    'Tracker experiment M2A-P037-E001',
    'The coaxial scaffold used a fast-degrading gelatin/cellulose nanofiber shell for rapid MnTBAP release and a slower dual-network HA/N-Cad-Alg core that supported NSC survival, migration, and neuronal differentiation with aligned topography.',
    'Scaffold/cue comparison',
    'Hierarchical HA/alginate/gelatin-cellulose hydrogel scaffold',
    '{"observation_tracker_ids": ["M2B-O028"], "source_experiment": {"chronicity_dpi_wpi": "In vitro characterization and 60-day degradation testing", "control_type": "Scaffold/cue comparison", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P037-E001", "figure_ref": "Publisher full-text snapshot", "injury_device": "Coaxial 3D printing of Gel/CNF-MnTBAP shell and HA/N-Cad-Alg core", "injury_model": "SCI repair scaffold design", "injury_severity": "N/A", "intervention_type": "Hierarchical HA/alginate/gelatin-cellulose hydrogel scaffold", "methods_summary": "The coaxial scaffold used a fast-degrading gelatin/cellulose nanofiber shell for rapid MnTBAP release and a slower dual-network HA/N-Cad-Alg core that supported NSC survival, migration, and neuronal differentiation with aligned topography.", "paper_id": "M2A-P037", "sex": "N/A", "species": "Scaffold system / rodent SCI context", "strain": "Postnatal rat NSCs and scaffold system", "vertebral_level": "N/A"}, "source_experiment_tracker_id": "M2A-P037-E001", "source_paper_tracker_id": "M2A-P037", "tracker_key": "M2A-P037::M2A-P037-E001"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P037'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P037::M2A-P037-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract',
    'Tracker experiment M2A-P037-E002',
    'The implanted scaffold rapidly reduced oxidative stress while later supporting endogenous NSC recruitment and neuronal differentiation, leading to improved motor functional restoration in SCI rats together with favorable histologic repair outcomes.',
    'Scaffold/cue comparison',
    'On-demand hierarchical hydrogel scaffold',
    '{"observation_tracker_ids": ["M2B-O084"], "source_experiment": {"chronicity_dpi_wpi": "Post-implant interval in full text not yet normalized", "control_type": "Scaffold/cue comparison", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P037-E002", "figure_ref": "Publisher full-text snapshot", "injury_device": "Experimental SCI with scaffold implantation", "injury_model": "SCI", "injury_severity": "UNKNOWN in tracker pending deeper normalization", "intervention_type": "On-demand hierarchical hydrogel scaffold", "methods_summary": "The implanted scaffold rapidly reduced oxidative stress while later supporting endogenous NSC recruitment and neuronal differentiation, leading to improved motor functional restoration in SCI rats together with favorable histologic repair outcomes.", "paper_id": "M2A-P037", "sex": "Female", "species": "Rattus norvegicus", "strain": "Female Sprague-Dawley, 200-220 g", "vertebral_level": "UNKNOWN"}, "source_experiment_tracker_id": "M2A-P037-E002", "source_paper_tracker_id": "M2A-P037", "tracker_key": "M2A-P037::M2A-P037-E002"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P037'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P037::M2A-P037-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract',
    'Tracker experiment M2A-P038-E001',
    'Nanofibers were 500-700 nm in diameter and released more than 90% of exosomes over 14 days while preserving exosome markers. In LPS-treated cultures, NFs@MP-HAh@Exo most strongly reduced iNOS, cleaved caspase-3, and Bax while increasing Arg-1 and Bcl-2, indicating combined anti-inflammatory and anti-apoptotic activity.',
    'NFs-HAh, NFs@MP-HAh, and NFs@MP-HAh@Exo comparisons',
    'Schwann exosome and methylprednisolone hydrogel patch',
    '{"observation_tracker_ids": ["M2B-O020"], "source_experiment": {"chronicity_dpi_wpi": "Exosome release 14 days; cell assays at 1, 3, 7, and 14 days; macrophage/neuron challenge 24 hours", "control_type": "NFs-HAh, NFs@MP-HAh, and NFs@MP-HAh@Exo comparisons", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P038-E001", "figure_ref": "Publisher full-text snapshot; patch release, biocompatibility, macrophage-polarization, and neuron-apoptosis assays", "injury_device": "PLGA-PEO methylprednisolone nanofiber plus HA hydrogel with Schwann-cell exosomes", "injury_model": "Patch compatibility model", "injury_severity": "N/A", "intervention_type": "Schwann exosome and methylprednisolone hydrogel patch", "methods_summary": "Nanofibers were 500-700 nm in diameter and released more than 90% of exosomes over 14 days while preserving exosome markers. In LPS-treated cultures, NFs@MP-HAh@Exo most strongly reduced iNOS, cleaved caspase-3, and Bax while increasing Arg-1 and Bcl-2, indicating combined anti-inflammatory and anti-apoptotic activity.", "paper_id": "M2A-P038", "sex": "N/A", "species": "In vitro / scaffold system", "strain": "Primary cortical neurons and primary macrophages", "vertebral_level": "N/A"}, "source_experiment_tracker_id": "M2A-P038-E001", "source_paper_tracker_id": "M2A-P038", "tracker_key": "M2A-P038::M2A-P038-E001"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P038'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P038::M2A-P038-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract',
    'Tracker experiment M2A-P038-E002',
    'The dual-cargo patch most strongly reduced day-3 CD68-positive infiltration, iNOS, and neuronal apoptosis while increasing Arg-1. By day 28 it produced the smallest cavitation, better NF200 and neuron survival, improved MEP latency and amplitude, enhanced CatWalk coordination and hindlimb support, and increased spinal-cord electrical activity relative to SCI and NFs@MP-HAh controls.',
    'SCI and methylprednisolone-only patch controls',
    'Exosome plus methylprednisolone composite surface patch',
    '{"observation_tracker_ids": ["M2B-O085"], "source_experiment": {"chronicity_dpi_wpi": "Day 3 inflammation/apoptosis; days 3, 7, 14, 21, and 28 BBB; day 28 MEP/CatWalk/MEA/histology", "control_type": "SCI and methylprednisolone-only patch controls", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P038-E002", "figure_ref": "Publisher full-text snapshot; acute contusion surface-patch repair outcomes", "injury_device": "Immediate surface coverage of hematoma by SCI-only, NFs@MP-HAh, or NFs@MP-HAh@Exo patch", "injury_model": "T10 spinal cord contusion SCI with hematoma", "injury_severity": "Contusion", "intervention_type": "Exosome plus methylprednisolone composite surface patch", "methods_summary": "The dual-cargo patch most strongly reduced day-3 CD68-positive infiltration, iNOS, and neuronal apoptosis while increasing Arg-1. By day 28 it produced the smallest cavitation, better NF200 and neuron survival, improved MEP latency and amplitude, enhanced CatWalk coordination and hindlimb support, and increased spinal-cord electrical activity relative to SCI and NFs@MP-HAh controls.", "paper_id": "M2A-P038", "sex": "Female", "species": "Rattus norvegicus", "strain": "Female Wistar rats; figure analyses n=3/group", "vertebral_level": "T10"}, "source_experiment_tracker_id": "M2A-P038-E002", "source_paper_tracker_id": "M2A-P038", "tracker_key": "M2A-P038::M2A-P038-E002"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P038'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P038::M2A-P038-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Full text',
    'Tracker experiment M2A-P039-E002',
    '2CNT/GelMA+ES reduced Iba1/CS56, increased NF and beta-tubulin III fibers crossing the lesion and remyelination, reached tissue conductivity 1.50 x 10^-3 S/cm vs normal 2.13 x 10^-3, and produced the strongest BBB, pain, and MEP recovery; CNTs remained at lesion without detected rostral/caudal diffusion.',
    'SCI vs GelMA vs 2CNT/GelMA vs 2CNT/GelMA+ES',
    'CNT/GelMA fibers + electrical stimulation',
    '{"observation_tracker_ids": ["M2B-O008", "M2B-O086"], "source_experiment": {"chronicity_dpi_wpi": "Eight weeks post-surgery", "control_type": "SCI vs GelMA vs 2CNT/GelMA vs 2CNT/GelMA+ES", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P039-E002", "figure_ref": "Full text (PMC10897856)", "injury_device": "Complete transection", "injury_model": "SCI", "injury_severity": "Complete transection", "intervention_type": "CNT/GelMA fibers + electrical stimulation", "methods_summary": "2CNT/GelMA+ES reduced Iba1/CS56, increased NF and beta-tubulin III fibers crossing the lesion and remyelination, reached tissue conductivity 1.50 x 10^-3 S/cm vs normal 2.13 x 10^-3, and produced the strongest BBB, pain, and MEP recovery; CNTs remained at lesion without detected rostral/caudal diffusion.", "paper_id": "M2A-P039", "sex": "T9 complete transection; 4 mm removed", "species": "Rat SCI model context", "strain": "Adult female Sprague-Dawley rats, 200-230 g", "vertebral_level": "Acute"}, "source_experiment_tracker_id": "M2A-P039-E002", "source_paper_tracker_id": "M2A-P039", "tracker_key": "M2A-P039::M2A-P039-E002"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P039'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P039::M2A-P039-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Full text',
    'Tracker experiment M2A-P040-E001',
    'LbL PEG/PAA/protein films were assembled at pH <=3 and tested with lysozyme; film composition, agarose concentration/porosity, and H-bonding controlled release. Released lysozyme remained active at early time points.',
    'Release chemistry comparison',
    'PEG/PAA layer-by-layer agarose hydrogel',
    '{"observation_tracker_ids": ["M2B-O042"], "source_experiment": {"chronicity_dpi_wpi": "In vitro PBS/cell-medium release at 37 C", "control_type": "Release chemistry comparison", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P040-E001", "figure_ref": "Full text (PMC2830720)", "injury_device": "Agarose functionalization", "injury_model": "In vitro release model for SCI bridge", "injury_severity": "N/A", "intervention_type": "PEG/PAA layer-by-layer agarose hydrogel", "methods_summary": "LbL PEG/PAA/protein films were assembled at pH <=3 and tested with lysozyme; film composition, agarose concentration/porosity, and H-bonding controlled release. Released lysozyme remained active at early time points.", "paper_id": "M2A-P040", "sex": "N/A", "species": "Scaffold system", "strain": "N/A", "vertebral_level": "N/A"}, "source_experiment_tracker_id": "M2A-P040-E001", "source_paper_tracker_id": "M2A-P040", "tracker_key": "M2A-P040::M2A-P040-E001"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P040'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P040::M2A-P040-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Full text',
    'Tracker experiment M2A-P040-E002',
    'The method demonstrated pH-triggered protein release for more than four weeks in vitro and was proposed for BDNF release from templated agarose scaffolds; it did not test SCI animals.',
    'Cell-based BDNF delivery alternative',
    'Functionalized agarose channel bridge',
    '{"observation_tracker_ids": ["M2B-O087"], "source_experiment": {"chronicity_dpi_wpi": "In vitro; more than four weeks in selected configurations", "control_type": "Cell-based BDNF delivery alternative", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P040-E002", "figure_ref": "Full text (PMC2830720)", "injury_device": "Agarose channel scaffold", "injury_model": "SCI channel bridge model", "injury_severity": "N/A", "intervention_type": "Functionalized agarose channel bridge", "methods_summary": "The method demonstrated pH-triggered protein release for more than four weeks in vitro and was proposed for BDNF release from templated agarose scaffolds; it did not test SCI animals.", "paper_id": "M2A-P040", "sex": "N/A", "species": "Scaffold system / SCI bridge context", "strain": "N/A", "vertebral_level": "N/A"}, "source_experiment_tracker_id": "M2A-P040-E002", "source_paper_tracker_id": "M2A-P040", "tracker_key": "M2A-P040::M2A-P040-E002"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P040'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P040::M2A-P040-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Full text',
    'Tracker experiment M2A-P041-E002',
    'Grafted NT-3-SCs+TrkC-NSCs survived in the injury area; GFP-positive NSC-derived and host NF+ axons were ensheathed by MBP+ myelin from NSC-derived myelinating cells and NT-3-SCs. Functional recovery was not the primary endpoint.',
    'Scaffold/cell comparison',
    'Tissue-engineered gelatin sponge neural scaffold',
    '{"observation_tracker_ids": ["M2B-O011", "M2B-O088"], "source_experiment": {"chronicity_dpi_wpi": "Eight weeks post-graft", "control_type": "Scaffold/cell comparison", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P041-E002", "figure_ref": "Full text (PMC3992004)", "injury_device": "Complete transection", "injury_model": "Complete transection SCI", "injury_severity": "Complete transection", "intervention_type": "Tissue-engineered gelatin sponge neural scaffold", "methods_summary": "Grafted NT-3-SCs+TrkC-NSCs survived in the injury area; GFP-positive NSC-derived and host NF+ axons were ensheathed by MBP+ myelin from NSC-derived myelinating cells and NT-3-SCs. Functional recovery was not the primary endpoint.", "paper_id": "M2A-P041", "sex": "T10 complete transection; 2 mm removed", "species": "Rattus norvegicus", "strain": "Adult female SD rats, histology n=3/group", "vertebral_level": "T10"}, "source_experiment_tracker_id": "M2A-P041-E002", "source_paper_tracker_id": "M2A-P041", "tracker_key": "M2A-P041::M2A-P041-E002"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P041'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P041::M2A-P041-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Full text',
    'Tracker experiment M2A-P042-E002',
    '3D-CF plus NSCs increased NF-H and reduced GFAP versus SCI/scaffold-only groups and improved reported limb function, but NSCs were not labeled/traced and the authors note objective neurological assessments were lacking.',
    'Scaffold/cell comparison',
    '3D-bioprinted collagen/silk scaffold + NSCs',
    '{"observation_tracker_ids": ["M2B-O029", "M2B-O089"], "source_experiment": {"chronicity_dpi_wpi": "Post-implantation endpoint in Results", "control_type": "Scaffold/cell comparison", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P042-E002", "figure_ref": "Full text (PMC6990792)", "injury_device": "Experimental SCI", "injury_model": "SCI", "injury_severity": "SCI", "intervention_type": "3D-bioprinted collagen/silk scaffold + NSCs", "methods_summary": "3D-CF plus NSCs increased NF-H and reduced GFAP versus SCI/scaffold-only groups and improved reported limb function, but NSCs were not labeled/traced and the authors note objective neurological assessments were lacking.", "paper_id": "M2A-P042", "sex": "SCI model; scaffold/cell implantation", "species": "Rat SCI model context", "strain": "Rats, n=10/group", "vertebral_level": "Acute"}, "source_experiment_tracker_id": "M2A-P042-E002", "source_paper_tracker_id": "M2A-P042", "tracker_key": "M2A-P042::M2A-P042-E002"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P042'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P042::M2A-P042-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Full text',
    'Tracker experiment M2A-P043-E002',
    'NF+ axons followed OEC/host-cell trajectories, but only trended above non-seeded/untreated controls; seeded and non-seeded scaffolds both produced significant skilled forelimb recovery, not correlated with scaffold axon extent.',
    'Functional recovery vs axon regeneration relationship',
    'OEC-seeded collagen scaffold',
    '{"observation_tracker_ids": ["M2B-O021", "M2B-O090"], "source_experiment": {"chronicity_dpi_wpi": "Functional follow-up with skilled forelimb test", "control_type": "Functional recovery vs axon regeneration relationship", "experiment_extracted": "YES (full-text)", "experiment_id": "M2A-P043-E002", "figure_ref": "Full text (PMC6170848)", "injury_device": "Mid-cervical unilateral resection model", "injury_model": "Acute SCI", "injury_severity": "Acute lesion-induced gap", "intervention_type": "OEC-seeded collagen scaffold", "methods_summary": "NF+ axons followed OEC/host-cell trajectories, but only trended above non-seeded/untreated controls; seeded and non-seeded scaffolds both produced significant skilled forelimb recovery, not correlated with scaffold axon extent.", "paper_id": "M2A-P043", "sex": "Unilateral mid-cervical spinal cord resection producing lesion gap", "species": "Rattus norvegicus", "strain": "Adult Lewis rats", "vertebral_level": "Mid-cervical"}, "source_experiment_tracker_id": "M2A-P043-E002", "source_paper_tracker_id": "M2A-P043", "tracker_key": "M2A-P043::M2A-P043-E002"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P043'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P043::M2A-P043-E002', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    NULL,
    'Review synthesis',
    'Tracker experiment Review anchors',
    'Module 2 tracker-derived experiment placeholder.',
    NULL,
    NULL,
    '{"observation_tracker_ids": ["M2B-O049"], "source_experiment": {}, "source_experiment_tracker_id": "Review anchors", "source_paper_tracker_id": "M2A-R002-M2A-R004", "tracker_key": "M2A-R002-M2A-R004::Review anchors"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-R002'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-R002-M2A-R004::Review anchors', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    NULL,
    'Review synthesis',
    'Tracker experiment Review anchors',
    'Module 2 tracker-derived experiment placeholder.',
    NULL,
    NULL,
    '{"observation_tracker_ids": ["M2B-O050"], "source_experiment": {}, "source_experiment_tracker_id": "Review anchors", "source_paper_tracker_id": "M2A-R005-M2A-R008", "tracker_key": "M2A-R005-M2A-R008::Review anchors"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-R005'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-R005-M2A-R008::Review anchors', experiment_id FROM inserted;

INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('3D printing / NPC graft scaffold', 'Module 2 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('3D printing / empty scaffold', 'Module 2 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('3D-bioprinted collagen/silk scaffold', 'Module 2 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('3D-printed GelMA microchannel scaffold', 'Module 2 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('AFG/fSAP composite hydrogel', 'Module 2 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Acute human clinical intervention', 'Module 2 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Aligned collagen scaffold plus NSPCs', 'Module 2 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Aligned hydrogel scaffold', 'Module 2 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Aligned nanofiber-hydrogel scaffold', 'Module 2 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Animal-to-clinical translation', 'Module 2 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Cell therapy / chronic translation', 'Module 2 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Chitosan bridge plus NSPC and immobilized cues', 'Module 2 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Chronic canine scar removal plus NeuroRegen/hUC-MSC', 'Module 2 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Chronic human scar resection plus scaffold/cell', 'Module 2 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Chronic scar removal plus anisotropic hydrogel', 'Module 2 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Chronic scar resection plus collagen/hUC-MSC scaffold', 'Module 2 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Clinical intervention', 'Module 2 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Coaxial 3D-printed hierarchical hydrogel', 'Module 2 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Collagen-I scaffold plus miR21 exosomes', 'Module 2 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Conductive aligned hydrogel / electrical stimulation', 'Module 2 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Conductive chitosan/alginate + hAEC + Noggin', 'Module 2 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Conductive surface scaffold', 'Module 2 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('DBM/PDRN/TI-EV/NPC hydrogel', 'Module 2 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Fibrin scaffold controlled release', 'Module 2 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Functionalized agarose hydrogel', 'Module 2 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Gelatin scaffold plus engineered cells', 'Module 2 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Gelatin/alginate + hEnSC + curcumin PLGA', 'Module 2 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('HA hydrogel plus astrocyte ECM', 'Module 2 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('HA scaffold plus PLGA cargo', 'Module 2 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Human resected scar histology', 'Module 2 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Injectable ECM hydrogel', 'Module 2 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Magnetically aligned injectable peptide hydrogel', 'Module 2 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Material taxonomy / translation', 'Module 2 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('NT-3 collagen hydrogel', 'Module 2 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('NT-3/fibroin gelatin scaffold', 'Module 2 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Nanofiber/HA hydrogel patch', 'Module 2 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Non-human primate intervention', 'Module 2 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('OEC-seeded scaffold', 'Module 2 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('PCL/PSA/MP nanofiber scaffold', 'Module 2 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('PLGA scaffold plus hMSC', 'Module 2 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Peptide nanofiber scaffold', 'Module 2 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Scaffold fabrication / platform', 'Module 2 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Sequential-release SilMA scaffold', 'Module 2 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('bFGF hydrogel', 'Module 2 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('dECM scaffold after chronic scar resection', 'Module 2 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('dECM scaffold plus hNS/PC', 'Module 2 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('dPN matrix plus Schwann cells', 'Module 2 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('dSCM/GelMA plus MenSC', 'Module 2 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('decellularized brain matrix hydrogel', 'Module 2 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('spinal cord dECM/GelMA scaffold', 'Module 2 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;

INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('A collagen-I scaffold enriched with CBD-LP-miR21 exosomes was applied to SCI repair to improve exosome retention, sustained release, and repair outcomes.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Angiogenesis / histology', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Axon density, myelination, and locomotion', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Axon guidance, delivery, and remyelination', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Axon infiltration', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Axon regeneration / recovery', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Axonal sprouting / function', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('BBB locomotion, neuronal growth, glial scar formation, inflammation, and collagen deposition were assessed.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Bioactive microenvironment', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Biophysical and biochemical cues', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Biotin-tagged IFN-gamma and PDGF-AA were immobilized to MAC hydrogel to cue neuronal or oligodendrocytic lineages within the bridge.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Boundary condition', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Canine locomotion, conduction, immune burden, and tissue regeneration', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Cell retention / axon guidance', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Cell support / functional reconstruction', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Cell survival / repair response', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Channel architecture', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Circuit repair / function', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Compatibility, architecture, and axon guidance', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Conduction / inflammation / regeneration', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Conduction / locomotion / tract regrowth', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Different hMSC doses were compared for BBB locomotor scores, MEP amplitudes, cell survival, differentiation, and neurological repair.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Drug timing / scaffold characterization', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Early surface-cap repair and inflammation boundary', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Endogenous NSC recruitment / repair', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Endogenous neurons, remyelination, synapses, and secondary scar were assessed after functionalized NeuroRegen implantation.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Function / local healing', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Functional recovery versus scaffold axon regeneration', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Histological repair / function boundary', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Histology assessed host-cell migration, fibroglial scarring, and regeneration of corticospinal, raphaespinal, propriospinal, and ascending sensory axons through and beyond hydrogel channels.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Host ingrowth', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Host integration, inflammation, gliosis, vascularization, regenerated nerve fibers, and locomotor recovery were assessed after implantation.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Host-cell migration, blood-vessel growth, and axonal ingrowth into SAPNS were assessed as evidence of a 3D permissive environment.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Human iPSC-derived NS/PC transplantation was combined with scaffold-supported scar resection to assess graft survival, host axon regeneration, histological repair, and lack of functional recovery.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Hydrogel and biomaterial reviews frame SCI scaffolds as bridges, delivery reservoirs, and cell carriers, but emphasize that material class, lesion geometry, and combination therapy determine interpretability.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Immune integration and glial scar', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Implant size, immune infiltration, Schwann-cell myelinated axons, axon growth, and BBB locomotor performance were assessed.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('In vitro and in vivo experiments evaluated whether the composite scaffold supported human menstrual blood-derived stem cells and improved functional reconstruction after SCI.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('In vivo motor, neural-marker, inflammatory, and scar response were assessed after right T10-T11 hemisection.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('In vivo rat SCI experiments evaluated regeneration and anti-inflammatory repair effects of the combined scaffold strategy.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('In vivo validation assessed whether aligned injectable hydrogel promoted and oriented axon infiltration at the SCI site.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('In-vivo immunomodulation, neural differentiation, tissue repair, and locomotion', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Inflammation / apoptosis / recovery', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Inflammation / electrophysiology / function', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Inflammation, microglia/macrophage activation, apoptosis, axonal regeneration, and functional recovery were assessed after transplantation into transection lesions.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Integration, angiogenesis, axon ingrowth, and host response', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Lineage organization', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Locomotor / electrophysiology', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Locomotor / electrophysiology / histology', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Locomotor / scar response', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Locomotor kinematics, muscle activity, appositional healing, and spinal cord tissue remodeling were compared.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Locomotor recovery / tissue remodeling', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Multimodal regeneration', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Multimodal repair', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Myelinated axons / locomotion', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Myelination / regeneration', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Myelination and graft-cell survival', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('NPC survival, neural relay, and function', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Nerve regeneration', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Nerve regeneration and scar response', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Neural differentiation / repair', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('NeuroRegen collagen scaffold and hUC-MSCs implanted into the resected cavity were assessed by locomotion, motor/somatosensory evoked potentials, and histological repair outcomes.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Neuronal fiber growth, glial scar formation, and hindlimb motor function were compared across NT-3 scaffold, control scaffold, and saline groups.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcomes addressed cell retention, axonal guidance, neuronal regeneration microenvironment, and functional recovery according to abstract.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Patch covering the hematoma surface was assessed for functional, electrophysiological, inflammatory, and neuronal survival outcomes.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Phase I clinical testing evaluated safety, neurological recovery, electrophysiology, and imaging after collagen scaffold plus hUC-MSC transplantation.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Protein-release agarose strategy', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Rat SCI testing assessed angiogenesis, anti-inflammatory and anti-apoptotic effects, neural differentiation, regeneration, and functional recovery.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Rat conduction, axon, remyelination, and function', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Rat full-transection locomotion and conduction', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Regeneration / inflammation', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Regeneration outcomes were assessed to test whether combined guidance and biochemical cues improved spinal cord repair.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Retention / sustained release', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('SCI testing evaluated oxidative stress control, endogenous NSC migration/differentiation, and repair.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Safety / feasibility', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Safety / neurological monitoring', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Safety / neurological outcome', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Safety / repair', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Safety / sensory recovery', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Scaffold-supported cell transplantation reviews emphasize that cells, scaffolds, growth factors, timing, and chronic lesion state interact, limiting simple causal claims.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Scar / immune response / axon penetration', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Scar identity', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Scar, immune response, and neuronal processes', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('The scaffold was framed as a platform to test architecture, transplanted cells, and local molecular agents for axon regeneration.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Timed protein release', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Tissue bridging and material limitation', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Tissue ingrowth / function', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Tissue ingrowth, nerve regeneration, electrophysiology, and functional recovery were assessed after hydrogel implantation.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Vascularization / axon growth / locomotion', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('miRNA delivery and inflammatory boundary', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Five complete chronic traumatic SCI patients underwent SSEP/MEP-guided scar excision, autologous BMMC-loaded NeuroRegen scaffold implantation, and 12-month follow-up.',
    'patients / months',
    'Five complete chronic traumatic SCI patients underwent SSEP/MEP-guided scar excision, autologous BMMC-loaded NeuroRegen scaffold implantation, and 12-month follow-up.',
    'chronic complete human scaffold implantation feasible in small cohort',
    'Abstract + source page',
    'Clinical source page / M1A carried',
    'medium',
    '{"curator_notes": "Feasibility signal only; not efficacy proof.", "experiment_tracker_id": "M2A-P001-E001", "paper_tracker_id": "M2A-P001", "quantitative": "YES", "statistics_reported": "small cohort; adverse-event detail requires full source review", "topic_id": "M2B-T006", "tracker_id": "M2B-O001"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P001::M2A-P001-E001'
    AND et.evidence_type_name = 'Clinical intervention'
    AND ot.outcome_type_name = 'Safety / feasibility'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O001', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Eight chronic complete ASIA A SCI patients received 4 x 10^7 hUCB-MSCs on NeuroRegen after SSEP/MEP-guided scar resection. No treatment-related adverse events occurred over 1 year; sensation expanded in 5/8 and MEP-responsive area in 7/8, while ASIA grade did not improve.',
    'patients / year; percent',
    'Eight chronic complete ASIA A SCI patients received 4 x 10^7 hUCB-MSCs on NeuroRegen after SSEP/MEP-guided scar resection. No treatment-related adverse events occurred over 1 year; sensation expanded in 5/8 and MEP-responsive area in 7/8, while ASIA grade did not improve.',
    'chronic complete human NeuroRegen/hUCB-MSC feasibility cohort with partial neurological signals',
    'Full text Figs. 1-2 and Tables 1-2',
    'Figs. 1-2; Tables 1-2',
    'high',
    '{"curator_notes": "Similar intervention family as M2A-P001 but different cell source; rehabilitation and uncontrolled baseline limit efficacy inference.", "experiment_tracker_id": "M2A-P009-E001", "paper_tracker_id": "M2A-P009", "quantitative": "YES", "statistics_reported": "5/8 sensation expansion; 7/8 MEP-area expansion; no ASIA grade improvement", "topic_id": "M2B-T006", "tracker_id": "M2B-O002"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P009::M2A-P009-E001'
    AND et.evidence_type_name = 'Clinical intervention'
    AND ot.outcome_type_name = 'Safety / neurological outcome'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O002', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Porous PLGA/poly-l-lysine scaffolds implanted after thoracic lateral hemisection improved locomotor recovery in fully hemisected monkeys compared with non-implanted controls and showed appositional healing/tissue remodeling at 12 weeks.',
    'weeks post injury',
    'Porous PLGA/poly-l-lysine scaffolds implanted after thoracic lateral hemisection improved locomotor recovery in fully hemisected monkeys compared with non-implanted controls and showed appositional healing/tissue remodeling at 12 weeks.',
    'primate scaffold implantation improved locomotion and remodeling',
    'Abstract',
    'Abstract',
    'medium',
    '{"curator_notes": "Strong translational bridge but still abstract-level here.", "experiment_tracker_id": "M2A-P029-E001", "paper_tracker_id": "M2A-P029", "quantitative": "YES", "statistics_reported": "significant improvement reported in abstract", "topic_id": "M2B-T006", "tracker_id": "M2B-O003"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P029::M2A-P029-E001'
    AND et.evidence_type_name = 'Non-human primate intervention'
    AND ot.outcome_type_name = 'Locomotor recovery / tissue remodeling'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O003', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'A 2-mm PEGDA-GelMA scaffold with 200-micrometer channels retained its structure for 4 weeks, reduced reactive-cell layer thickness by 35% versus agarose, reduced GFAP scarring, vascularized, and supported 97 +/- 8 NF200-positive axons per channel; empty scaffolds did not produce distal host-axon extension.',
    'axons/channel; percent',
    'A 2-mm PEGDA-GelMA scaffold with 200-micrometer channels retained its structure for 4 weeks, reduced reactive-cell layer thickness by 35% versus agarose, reduced GFAP scarring, vascularized, and supported 97 +/- 8 NF200-positive axons per channel; empty scaffolds did not produce distal host-axon extension.',
    '3D architecture supports integration and host axon entry, but not complete relay by itself',
    'Full text Figs. 1-2',
    'Figs. 1-2',
    'high',
    '{"curator_notes": "Empty-scaffold result is separated from NPC-dependent functional relay.", "experiment_tracker_id": "M2A-P004-E001", "paper_tracker_id": "M2A-P004", "quantitative": "YES", "statistics_reported": "P < 0.0019 for reactive layer; P < 0.0001 for GFAP; n = 11-12", "topic_id": "M2B-T001", "tracker_id": "M2B-O004"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P004::M2A-P004-E001'
    AND et.evidence_type_name = '3D printing / empty scaffold'
    AND ot.outcome_type_name = 'Compatibility, architecture, and axon guidance'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O004', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'In adult female C57BL/6J T9-10 lateral hemisection, porous PEG tubes showed transient dendritic-cell/macrophage enrichment at 1 week that resolved by 2 weeks and reduced glial scar thickness to 127 +/- 73 micrometers versus 337 +/- 169 micrometers with gelfoam.',
    'micrometers',
    'In adult female C57BL/6J T9-10 lateral hemisection, porous PEG tubes showed transient dendritic-cell/macrophage enrichment at 1 week that resolved by 2 weeks and reduced glial scar thickness to 127 +/- 73 micrometers versus 337 +/- 169 micrometers with gelfoam.',
    'modular PEG tubes integrate without prolonged inflammatory amplification and reduce peripheral scar thickness',
    'Full text Figs. 2-4',
    'Figs. 2-4',
    'high',
    '{"curator_notes": "Immune resolution and scar outcomes are distinct from later axon density.", "experiment_tracker_id": "M2A-P005-E001", "paper_tracker_id": "M2A-P005", "quantitative": "YES", "statistics_reported": "n = 3-5/timepoint; tube scar reduction reported in Fig. 4", "topic_id": "M2B-T001", "tracker_id": "M2B-O005"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P005::M2A-P005-E001'
    AND et.evidence_type_name = 'Aligned hydrogel scaffold'
    AND ot.outcome_type_name = 'Immune integration and glial scar'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O005', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'PLGA 85:15 scaffolds were fabricated with parallel channels to enable testing of scaffold architecture, transplanted cells, and local molecular agents for axon regeneration.',
    'qualitative',
    'PLGA 85:15 scaffolds were fabricated with parallel channels to enable testing of scaffold architecture, transplanted cells, and local molecular agents for axon regeneration.',
    'multi-channel PLGA scaffold as combinatorial repair platform',
    'Abstract',
    'Abstract',
    'medium',
    '{"curator_notes": "Primarily platform/architecture evidence, not direct functional outcome.", "experiment_tracker_id": "M2A-P010-E001", "paper_tracker_id": "M2A-P010", "quantitative": "NO", "statistics_reported": "not applicable", "topic_id": "M2B-T001", "tracker_id": "M2B-O006"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P010::M2A-P010-E001'
    AND et.evidence_type_name = 'Scaffold fabrication / platform'
    AND ot.outcome_type_name = 'Channel architecture'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O006', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Self-assembling peptide nanofiber scaffold with neural progenitor and Schwann cells supported host-cell migration, blood-vessel growth, and axonal ingrowth into rat dorsal-column transection sites.',
    'qualitative',
    'Self-assembling peptide nanofiber scaffold with neural progenitor and Schwann cells supported host-cell migration, blood-vessel growth, and axonal ingrowth into rat dorsal-column transection sites.',
    'SAPNS creates permissive 3D ingrowth environment',
    'Abstract',
    'Abstract',
    'medium',
    '{"curator_notes": "Early peptide scaffold bridge anchor.", "experiment_tracker_id": "M2A-P011-E001", "paper_tracker_id": "M2A-P011", "quantitative": "YES", "statistics_reported": "exact values not extracted", "topic_id": "M2B-T001", "tracker_id": "M2B-O007"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P011::M2A-P011-E001'
    AND et.evidence_type_name = 'Peptide nanofiber scaffold'
    AND ot.outcome_type_name = 'Host ingrowth'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O007', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'In T9 complete transection rats, aligned CNT/GelMA fibers plus ES reduced Iba1/CS56, increased NF/beta-tubulin III fibers and remyelination across the lesion, restored tissue conductivity to 1.50 x 10^-3 S/cm versus normal 2.13 x 10^-3, and produced the strongest BBB, pain, and MEP recovery.',
    'quantitative',
    'In T9 complete transection rats, aligned CNT/GelMA fibers plus ES reduced Iba1/CS56, increased NF/beta-tubulin III fibers and remyelination across the lesion, restored tissue conductivity to 1.50 x 10^-3 S/cm versus normal 2.13 x 10^-3, and produced the strongest BBB, pain, and MEP recovery.',
    'conductive aligned scaffold plus ES promotes neural alignment, conduction, and repair',
    'PMC10897856',
    'Full text',
    'high',
    '{"curator_notes": "CNTs remained at the lesion; scaffold and ES effects are bundled.", "experiment_tracker_id": "M2A-P039-E002", "paper_tracker_id": "M2A-P039", "quantitative": "YES", "statistics_reported": "Exact conductivity and 8-week endpoint direction extracted; MEP n=3/group", "topic_id": "M2B-T001", "tracker_id": "M2B-O008"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P039::M2A-P039-E002'
    AND et.evidence_type_name = 'Conductive aligned hydrogel / electrical stimulation'
    AND ot.outcome_type_name = 'Axon regeneration / recovery'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O008', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'hMSC-seeded PLGA scaffolds implanted into 2-mm complete rat spinal cord defects improved BBB scores and MEP amplitudes relative to scaffold-only controls.',
    'BBB / MEP',
    'hMSC-seeded PLGA scaffolds implanted into 2-mm complete rat spinal cord defects improved BBB scores and MEP amplitudes relative to scaffold-only controls.',
    'PLGA+hMSC improved function/electrophysiology vs scaffold-only',
    'Abstract',
    'Abstract',
    'medium',
    '{"curator_notes": "Useful because scaffold-only comparator is present.", "experiment_tracker_id": "M2A-P012-E001", "paper_tracker_id": "M2A-P012", "quantitative": "YES", "statistics_reported": "abstract reports approximate BBB 5 vs 2 and MEP 200-300 uV", "topic_id": "M2B-T002", "tracker_id": "M2B-O009"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P012::M2A-P012-E001'
    AND et.evidence_type_name = 'PLGA scaffold plus hMSC'
    AND ot.outcome_type_name = 'Locomotor / electrophysiology'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O009', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'In adult female Fischer rat thoracic contusion, iPN supported approximately 3-fold more transplanted SCs at 14 days and twice as many SC-myelinated axons at 8 weeks versus Matrigel, with comparable BBB performance; grid-walk errors favored iPN at 4 weeks but equalized by 8 weeks.',
    'relative cell/axon count; BBB; grid-walk error',
    'In adult female Fischer rat thoracic contusion, iPN supported approximately 3-fold more transplanted SCs at 14 days and twice as many SC-myelinated axons at 8 weeks versus Matrigel, with comparable BBB performance; grid-walk errors favored iPN at 4 weeks but equalized by 8 weeks.',
    'iPN improves graft survival and axon histology versus Matrigel without durable locomotor superiority',
    'Full text Figs. 3-8',
    'Figs. 3-8',
    'high',
    '{"curator_notes": "iPN immune-cell numbers resembled injury-only controls at 14 days; matrix was not visible at 8 weeks, consistent with degradation.", "experiment_tracker_id": "M2A-P016-E001", "paper_tracker_id": "M2A-P016", "quantitative": "YES", "statistics_reported": "iPN graft volume 0.95 +/- 0.28 vs 0.48 +/- 0.17 mm3; SC-myelinated axons 6927 +/- 2429 vs 3259 +/- 475", "topic_id": "M2B-T002", "tracker_id": "M2B-O010"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P016::M2A-P016-E001'
    AND et.evidence_type_name = 'dPN matrix plus Schwann cells'
    AND ot.outcome_type_name = 'Myelinated axons / locomotion'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O010', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'In adult rat T10 complete transection, an NT-3-Schwann-cell/TrkC-NSC gelatin scaffold supported graft survival and MBP-positive myelin around GFP-positive graft-derived and host NF+ axons at 8 weeks; in vitro APC+ oligodendrocytic differentiation reached 12.98 +/- 5.33% in the dual-engineered group.',
    'quantitative',
    'In adult rat T10 complete transection, an NT-3-Schwann-cell/TrkC-NSC gelatin scaffold supported graft survival and MBP-positive myelin around GFP-positive graft-derived and host NF+ axons at 8 weeks; in vitro APC+ oligodendrocytic differentiation reached 12.98 +/- 5.33% in the dual-engineered group.',
    'engineered cell/scaffold network promotes myelination',
    'PMC3992004',
    'Full text',
    'high',
    '{"curator_notes": "Scaffold, engineered cells, NT-3, TrkC, and immunosuppression are bundled.", "experiment_tracker_id": "M2A-P041-E002", "paper_tracker_id": "M2A-P041", "quantitative": "YES", "statistics_reported": "MBP histology and APC value extracted; functional recovery was not the primary endpoint", "topic_id": "M2B-T002", "tracker_id": "M2B-O011"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P041::M2A-P041-E002'
    AND et.evidence_type_name = 'Gelatin scaffold plus engineered cells'
    AND ot.outcome_type_name = 'Myelination / regeneration'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O011', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'In adult female Long Evans rats with complete 2-mm T9 ablation, fibrin with a heparin-binding delivery system and NT-3 (1000 ng/mL) increased overall Tuj1 fiber density to 10.4% versus 3% saline and approximately 6-7% fibrin controls, while fibrin reduced white-matter-border GFAP.',
    'percent fiber density; GFAP',
    'In adult female Long Evans rats with complete 2-mm T9 ablation, fibrin with a heparin-binding delivery system and NT-3 (1000 ng/mL) increased overall Tuj1 fiber density to 10.4% versus 3% saline and approximately 6-7% fibrin controls, while fibrin reduced white-matter-border GFAP.',
    'NT-3 fibrin scaffold improved early histology without later functional improvement',
    'Full text Figs. 1-3',
    'Figs. 1-3',
    'high',
    '{"curator_notes": "Key positive-histology/negative-function boundary; no neuronal cell bodies were observed in the lesion.", "experiment_tracker_id": "M2A-P025-E001", "paper_tracker_id": "M2A-P025", "quantitative": "YES", "statistics_reported": "F-DS-NT3 1000 ng/mL; 9-day endpoint", "topic_id": "M2B-T003", "tracker_id": "M2B-O012"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P025::M2A-P025-E001'
    AND et.evidence_type_name = 'Fibrin scaffold controlled release'
    AND ot.outcome_type_name = 'Axonal sprouting / function'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O012', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Structured HA hydrogel with anti-NgR and BDNF/VEGF-loaded PLGA microspheres integrated with host tissue, inhibited inflammation/gliosis, increased vessels and regenerated fibers, and improved locomotor recovery after rat dorsal hemisection.',
    'qualitative',
    'Structured HA hydrogel with anti-NgR and BDNF/VEGF-loaded PLGA microspheres integrated with host tissue, inhibited inflammation/gliosis, increased vessels and regenerated fibers, and improved locomotor recovery after rat dorsal hemisection.',
    'HA+PLGA multi-cargo scaffold improved repair profile',
    'Abstract',
    'Abstract',
    'medium',
    '{"curator_notes": "Multiple active components make attribution difficult.", "experiment_tracker_id": "M2A-P027-E001", "paper_tracker_id": "M2A-P027", "quantitative": "YES", "statistics_reported": "exact values not extracted", "topic_id": "M2B-T003", "tracker_id": "M2B-O013"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P027::M2A-P027-E001'
    AND et.evidence_type_name = 'HA scaffold plus PLGA cargo'
    AND ot.outcome_type_name = 'Vascularization / axon growth / locomotion'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O013', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Eight-percent SilMA with PLGA microspheres released >40% of Ang-(1-7) within 3 days and nearly all by 7 days, while NT-3 release persisted through days 28-56 in PBS release testing.',
    'quantitative',
    'Eight-percent SilMA with PLGA microspheres released >40% of Ang-(1-7) within 3 days and nearly all by 7 days, while NT-3 release persisted through days 28-56 in PBS release testing.',
    'staged release scaffold targets early inflammation then later neuroregeneration',
    'PMC11617199',
    'Full text',
    'high',
    '{"curator_notes": "In-vitro PBS release does not establish the same in-vivo kinetics.", "experiment_tracker_id": "M2A-P036-E001", "paper_tracker_id": "M2A-P036", "quantitative": "YES", "statistics_reported": "Ang-(1-7) >40% by day 3 and nearly complete by day 7; NT-3 remained in delayed release through days 28-56", "topic_id": "M2B-T003", "tracker_id": "M2B-O014"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P036::M2A-P036-E001'
    AND et.evidence_type_name = 'Sequential-release SilMA scaffold'
    AND ot.outcome_type_name = 'Drug timing / scaffold characterization'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O014', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'In male Wistar Th8 hemisection, 8 mg/mL porcine spinal-cord or urinary-bladder ECM hydrogels integrated into the lesion, increased NF160 axon ingrowth and RECA vascularization versus saline, and modulated early inflammatory gene expression, but massive macrophage infiltration, rapid degradation, and progressive small cysts limited reconstruction.',
    'weeks',
    'In male Wistar Th8 hemisection, 8 mg/mL porcine spinal-cord or urinary-bladder ECM hydrogels integrated into the lesion, increased NF160 axon ingrowth and RECA vascularization versus saline, and modulated early inflammatory gene expression, but massive macrophage infiltration, rapid degradation, and progressive small cysts limited reconstruction.',
    'injectable ECM supports tissue bridging and ingrowth but rapid degradation and macrophage response limit durable repair',
    'Full text Figs. 2-7',
    'Figs. 2-7',
    'high',
    '{"curator_notes": "SC-ECM and UB-ECM were not significantly different; functional recovery was not established.", "experiment_tracker_id": "M2A-P014-E002", "paper_tracker_id": "M2A-P014", "quantitative": "YES", "statistics_reported": "n = 5/group/timepoint; qPCR at 2, 4, 8 weeks", "topic_id": "M2B-T004", "tracker_id": "M2B-O015"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P014::M2A-P014-E002'
    AND et.evidence_type_name = 'Injectable ECM hydrogel'
    AND ot.outcome_type_name = 'Integration, angiogenesis, axon ingrowth, and host response'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O015', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'In adult rat T8 dorsal hemisection, protoplasmic astrocyte ECM in HA reduced GFAP area around the lesion (9.7 +/- 1.1% vs sham 16 +/- 3.3%), ED1 area around the lesion (5.5 +/- 0.97% vs sham 9.7 +/- 1.6%), and increased Tuj1 area in the lesion (14 +/- 1.0% vs sham 9.2 +/- 1.9%); fibrous ECM did not reproduce the benefit.',
    'quantitative',
    'In adult rat T8 dorsal hemisection, protoplasmic astrocyte ECM in HA reduced GFAP area around the lesion (9.7 +/- 1.1% vs sham 16 +/- 3.3%), ED1 area around the lesion (5.5 +/- 0.97% vs sham 9.7 +/- 1.6%), and increased Tuj1 area in the lesion (14 +/- 1.0% vs sham 9.2 +/- 1.9%); fibrous ECM did not reproduce the benefit.',
    'astrocyte ECM subtype changes HA hydrogel histology and immune response',
    'PMC5851469',
    'Full text',
    'high',
    '{"curator_notes": "No functional locomotor test; ECM source and cell-loading effects remain separate boundaries.", "experiment_tracker_id": "M2A-P032-E001", "paper_tracker_id": "M2A-P032", "quantitative": "YES", "statistics_reported": "Exact values extracted; 2 weeks after implantation, 4 weeks after injury", "topic_id": "M2B-T004", "tracker_id": "M2B-O016"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P032::M2A-P032-E001'
    AND et.evidence_type_name = 'HA hydrogel plus astrocyte ECM'
    AND ot.outcome_type_name = 'Scar / immune response / axon penetration'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O016', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Anisotropic alginate hydrogels implanted after scar removal at 4 WPI in chronic complete thoracic transection supported electrophysiological conductivity, locomotor improvement, host-cell migration, reduced scarring, and multiple tract classes growing through/beyond channels.',
    'months post engraftment',
    'Anisotropic alginate hydrogels implanted after scar removal at 4 WPI in chronic complete thoracic transection supported electrophysiological conductivity, locomotor improvement, host-cell migration, reduced scarring, and multiple tract classes growing through/beyond channels.',
    'chronic scar-removal alginate scaffold supports structural and functional repair',
    'Abstract',
    'Abstract',
    'medium',
    '{"curator_notes": "Strong chronic bridge to Module 1, but abstract-level here.", "experiment_tracker_id": "M2A-P006-E001", "paper_tracker_id": "M2A-P006", "quantitative": "YES", "statistics_reported": "outcomes up to 3 months; exact stats not extracted", "topic_id": "M2B-T005", "tracker_id": "M2B-O017"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P006::M2A-P006-E001'
    AND et.evidence_type_name = 'Chronic scar removal plus anisotropic hydrogel'
    AND ot.outcome_type_name = 'Conduction / locomotion / tract regrowth'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O017', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'In 18 adult female beagles with complete T8 resection, delayed scar removal and functionalized NeuroRegen implantation (n=6) produced Olby scores of approximately 6 versus 2-4.5 in control or scaffold-only groups by 12 months, with reduced CS-56/CSPG signal in both scaffold groups.',
    'Olby score; histology',
    'In 18 adult female beagles with complete T8 resection, delayed scar removal and functionalized NeuroRegen implantation (n=6) produced Olby scores of approximately 6 versus 2-4.5 in control or scaffold-only groups by 12 months, with reduced CS-56/CSPG signal in both scaffold groups.',
    'large-animal chronic NeuroRegen+hUC-MSC repair signal with scaffold and cell contributions separated',
    'Full text Figs. 1-7',
    'Figs. 1-7',
    'high',
    '{"curator_notes": "Scar removal did not worsen locomotion; functional benefit is confounded by surgery, scaffold, cells, and rehabilitation.", "experiment_tracker_id": "M2A-P015-E001", "paper_tracker_id": "M2A-P015", "quantitative": "YES", "statistics_reported": "Functionalized scaffold reached approximately Olby 6; scaffold-only groups plateaued at 2-4.5; n=6/group", "topic_id": "M2B-T005", "tracker_id": "M2B-O018"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P015::M2A-P015-E001'
    AND et.evidence_type_name = 'Chronic canine scar removal plus NeuroRegen/hUC-MSC'
    AND ot.outcome_type_name = 'Locomotor / scar response'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O018', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'In female SD rats with 200 kdyn T8 contusion, one-week post-injury surface capping with HA/PPY/PM-CURC-iNPC preserved beta-III-tubulin fibers, reduced GFAP-negative lesion area and PDGF expression, and did not worsen gross tissue structure; iNPCs mainly showed astroglial rather than neuronal colocalization and Iba1/ED1 inflammation did not differ at one week.',
    'mixed qualitative/quantitative',
    'In female SD rats with 200 kdyn T8 contusion, one-week post-injury surface capping with HA/PPY/PM-CURC-iNPC preserved beta-III-tubulin fibers, reduced GFAP-negative lesion area and PDGF expression, and did not worsen gross tissue structure; iNPCs mainly showed astroglial rather than neuronal colocalization and Iba1/ED1 inflammation did not differ at one week.',
    'surface-capping conductive scaffold supports cells and early repair-associated responses',
    'PMC8698735',
    'Full text',
    'high',
    '{"curator_notes": "Early small-N study; no long-term function and no early anti-inflammatory benefit.", "experiment_tracker_id": "M2A-P034-E002", "paper_tracker_id": "M2A-P034", "quantitative": "YES", "statistics_reported": "n=3/group; one-week post-implant endpoint", "topic_id": "M2B-T007", "tracker_id": "M2B-O019"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P034::M2A-P034-E002'
    AND et.evidence_type_name = 'Conductive surface scaffold'
    AND ot.outcome_type_name = 'Cell survival / repair response'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O019', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Schwann-cell exosome and methylprednisolone composite patch improved rat SCI functional and electrophysiological performance, shifted macrophages toward M2-type response, reduced inflammatory response, and increased neuronal survival.',
    'qualitative',
    'Schwann-cell exosome and methylprednisolone composite patch improved rat SCI functional and electrophysiological performance, shifted macrophages toward M2-type response, reduced inflammatory response, and increased neuronal survival.',
    'exosome/steroid surface patch modulates inflammation and repair',
    'Abstract',
    'Abstract',
    'medium',
    '{"curator_notes": "Patch covers hematoma surface rather than filling cavity.", "experiment_tracker_id": "M2A-P038-E001", "paper_tracker_id": "M2A-P038", "quantitative": "YES", "statistics_reported": "exact values not extracted", "topic_id": "M2B-T007", "tracker_id": "M2B-O020"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P038::M2A-P038-E001'
    AND et.evidence_type_name = 'Nanofiber/HA hydrogel patch'
    AND ot.outcome_type_name = 'Inflammation / electrophysiology / function'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O020', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'In acute unilateral cervical resection rats, NF+ axons followed OEC/host-cell trajectories but increased only as a trend over non-seeded or untreated lesions; both seeded and non-seeded microstructured collagen scaffolds improved skilled forelimb function, and function was not correlated with scaffold axon extent.',
    'qualitative',
    'In acute unilateral cervical resection rats, NF+ axons followed OEC/host-cell trajectories but increased only as a trend over non-seeded or untreated lesions; both seeded and non-seeded microstructured collagen scaffolds improved skilled forelimb function, and function was not correlated with scaffold axon extent.',
    'functional recovery can dissociate from scaffold-traversing axon regeneration',
    'PMC6170848',
    'Full text',
    'high',
    '{"curator_notes": "Strong negative-mechanism boundary; no single biomaterial/cell component explains recovery.", "experiment_tracker_id": "M2A-P043-E002", "paper_tracker_id": "M2A-P043", "quantitative": "YES", "statistics_reported": "Exact mechanistic direction extracted; source does not establish a simple bridge-mediated recovery mechanism", "topic_id": "M2B-T008", "tracker_id": "M2B-O021"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P043::M2A-P043-E002'
    AND et.evidence_type_name = 'OEC-seeded scaffold'
    AND ot.outcome_type_name = 'Boundary condition'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O021', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Two acute complete patients (T11 treated at approximately 24 hours; C4 at 8 days) received approximately 4 x 10^7 umbilical-cord MSCs on 1.5-cm or 1.1-cm NeuroRegen implants. Both improved from ASIA A to C with sensory/motor gains and recovered SSEP/MEP; the thoracic patient''s WISCI rose from 0 to 7 at 12 months.',
    'ASIA; SSEP/MEP; WISCI',
    'Two acute complete patients (T11 treated at approximately 24 hours; C4 at 8 days) received approximately 4 x 10^7 umbilical-cord MSCs on 1.5-cm or 1.1-cm NeuroRegen implants. Both improved from ASIA A to C with sensory/motor gains and recovered SSEP/MEP; the thoracic patient''s WISCI rose from 0 to 7 at 12 months.',
    'acute complete human scaffold/MSC feasibility signal',
    'Full text Figs. 1-5',
    'Figs. 1-5',
    'high',
    '{"curator_notes": "Supports feasibility and hypothesis generation only; not efficacy-grade evidence.", "experiment_tracker_id": "M2A-P017-E001", "paper_tracker_id": "M2A-P017", "quantitative": "YES", "statistics_reported": "n=2; uncontrolled; no obvious treatment-related adverse symptoms", "topic_id": "M2B-T006", "tracker_id": "M2B-O022"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P017::M2A-P017-E001'
    AND et.evidence_type_name = 'Acute human clinical intervention'
    AND ot.outcome_type_name = 'Safety / neurological monitoring'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O022', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'In rat and canine complete transection models, hUC-MSC-loaded collagen scaffolds improved locomotor and electrophysiological outcomes over SCI or scaffold-only groups: rat BBB improved at 4-8 weeks, while canine Olby scores and MEP improved more with cells at 3-6 months.',
    'BBB; Olby; MEP',
    'In rat and canine complete transection models, hUC-MSC-loaded collagen scaffolds improved locomotor and electrophysiological outcomes over SCI or scaffold-only groups: rat BBB improved at 4-8 weeks, while canine Olby scores and MEP improved more with cells at 3-6 months.',
    'collagen+hUC-MSC preclinical scaffold/cell strategy shows species-spanning functional and conduction signals',
    'Full text Figs. 1-5',
    'Figs. 1-5',
    'high',
    '{"curator_notes": "Animal findings support translation but do not isolate scaffold, cell, and rehabilitation effects completely.", "experiment_tracker_id": "M2A-P033-E001", "paper_tracker_id": "M2A-P033", "quantitative": "YES", "statistics_reported": "Rat n=10/group; canine n=5/group", "topic_id": "M2B-T006", "tracker_id": "M2B-O023"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P033::M2A-P033-E001'
    AND et.evidence_type_name = 'Animal-to-clinical translation'
    AND ot.outcome_type_name = 'Safety / repair'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O023', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'In adult rat C5 hemi-incision, a 1-mm PCLEEP-collagen scaffold aligned to the cord supported axon ingrowth by 1 week, sustained alignment through 4 weeks, and MAG-positive axon-associated structures at 4 weeks. NT-3 loading was 54.6 ng/mg with 90.1% released in week 1 and 99.7% by 3 months; scaffold degradation was 24.8%, 33.4%, and 51.6% at 1, 2, and 3 months in vitro.',
    'ng/mg; percent',
    'In adult rat C5 hemi-incision, a 1-mm PCLEEP-collagen scaffold aligned to the cord supported axon ingrowth by 1 week, sustained alignment through 4 weeks, and MAG-positive axon-associated structures at 4 weeks. NT-3 loading was 54.6 ng/mg with 90.1% released in week 1 and 99.7% by 3 months; scaffold degradation was 24.8%, 33.4%, and 51.6% at 1, 2, and 3 months in vitro.',
    'aligned nanofibers combine contact guidance with prolonged local trophic delivery',
    'Full text Figs. 1-5',
    'Figs. 1-5',
    'high',
    '{"curator_notes": "Functional recovery was not tested in this paper; later work is needed for neuronal reconnection.", "experiment_tracker_id": "M2A-P008-E001", "paper_tracker_id": "M2A-P008", "quantitative": "YES", "statistics_reported": "release and degradation values reported in Results", "topic_id": "M2B-T001", "tracker_id": "M2B-O024"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P008::M2A-P008-E001'
    AND et.evidence_type_name = 'Aligned nanofiber-hydrogel scaffold'
    AND ot.outcome_type_name = 'Axon guidance, delivery, and remyelination'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O024', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Aligned collagen sponge scaffold supported human spinal cord-derived NSPC transplantation after complete transection SCI and was used to compare hSC-NSPCs with brain-derived NSPCs.',
    'qualitative',
    'Aligned collagen sponge scaffold supported human spinal cord-derived NSPC transplantation after complete transection SCI and was used to compare hSC-NSPCs with brain-derived NSPCs.',
    'aligned collagen scaffold supports human NSPC repair platform',
    'Abstract',
    'Abstract',
    'medium',
    '{"curator_notes": "Cell-source comparison is central, but scaffold provides retention/guidance platform.", "experiment_tracker_id": "M2A-P018-E001", "paper_tracker_id": "M2A-P018", "quantitative": "YES", "statistics_reported": "exact values not extracted", "topic_id": "M2B-T001", "tracker_id": "M2B-O025"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P018::M2A-P018-E001'
    AND et.evidence_type_name = 'Aligned collagen scaffold plus NSPCs'
    AND ot.outcome_type_name = 'Cell retention / axon guidance'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O025', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Magnetically responsive self-assembling peptide hydrogels aligned under a 100-Gauss field and were validated for promoting/aliging axon infiltration at SCI sites.',
    'Gauss / qualitative',
    'Magnetically responsive self-assembling peptide hydrogels aligned under a 100-Gauss field and were validated for promoting/aliging axon infiltration at SCI sites.',
    'injectable hydrogel topology can be externally aligned',
    'Abstract',
    'Abstract',
    'medium',
    '{"curator_notes": "Distinct injectable alignment strategy.", "experiment_tracker_id": "M2A-P021-E001", "paper_tracker_id": "M2A-P021", "quantitative": "YES", "statistics_reported": "100-Gauss alignment condition reported", "topic_id": "M2B-T001", "tracker_id": "M2B-O026"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P021::M2A-P021-E001'
    AND et.evidence_type_name = 'Magnetically aligned injectable peptide hydrogel'
    AND ot.outcome_type_name = 'Axon infiltration'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O026', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'After acute 2 mm T10 full transection, hAEC-derived neural-like cell scaffolds improved 8-week BBB to 5.667 versus 2.333 for empty scaffold and 0.667 for transection control; MEP amplitude reached 29.57% of normal and NF-H axons projected along channels.',
    'quantitative',
    'After acute 2 mm T10 full transection, hAEC-derived neural-like cell scaffolds improved 8-week BBB to 5.667 versus 2.333 for empty scaffold and 0.667 for transection control; MEP amplitude reached 29.57% of normal and NF-H axons projected along channels.',
    'microchannel GelMA scaffold plus hAEC neural-like cells supports partial circuit repair',
    'PMC9598945',
    'Full text',
    'high',
    '{"curator_notes": "The paper reports postoperative deaths, severe neuroinflammation, and neural-like rather than mature neuronal identity.", "experiment_tracker_id": "M2A-P035-E002", "paper_tracker_id": "M2A-P035", "quantitative": "YES", "statistics_reported": "BBB n=3/group; MEP n=5 for SCI groups; exact 8-week values extracted", "topic_id": "M2B-T001", "tracker_id": "M2B-O027"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P035::M2A-P035-E002'
    AND et.evidence_type_name = '3D-printed GelMA microchannel scaffold'
    AND ot.outcome_type_name = 'Circuit repair / function'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O027', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Coaxial 3D-printed HA/alginate/gelatin-cellulose scaffold delivered timed cues for oxidative-stress control, endogenous NSC migration, neuronal differentiation, and SCI repair.',
    'qualitative',
    'Coaxial 3D-printed HA/alginate/gelatin-cellulose scaffold delivered timed cues for oxidative-stress control, endogenous NSC migration, neuronal differentiation, and SCI repair.',
    'printed hydrogel can program time-sequenced repair cues',
    'Abstract',
    'Abstract',
    'medium',
    '{"curator_notes": "Also belongs to cargo/release topic.", "experiment_tracker_id": "M2A-P037-E001", "paper_tracker_id": "M2A-P037", "quantitative": "YES", "statistics_reported": "exact values not extracted", "topic_id": "M2B-T001", "tracker_id": "M2B-O028"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P037::M2A-P037-E001'
    AND et.evidence_type_name = 'Coaxial 3D-printed hierarchical hydrogel'
    AND ot.outcome_type_name = 'Endogenous NSC recruitment / repair'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O028', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    '3D-CF plus NSCs increased NF-H-positive fibers and reduced GFAP versus SCI and scaffold-only groups in rat SCI (n=10/group), with reported limb-function improvement; authors noted lack of NSC tracing and limited objective neurological assessment.',
    'quantitative direction',
    '3D-CF plus NSCs increased NF-H-positive fibers and reduced GFAP versus SCI and scaffold-only groups in rat SCI (n=10/group), with reported limb-function improvement; authors noted lack of NSC tracing and limited objective neurological assessment.',
    'bioprinted silk/collagen scaffold plus NSCs supports regeneration',
    'PMC6990792',
    'Full text',
    'high',
    '{"curator_notes": "Architecture and NSC effects remain bundled; the paper''s own tracing/function limitations are retained.", "experiment_tracker_id": "M2A-P042-E002", "paper_tracker_id": "M2A-P042", "quantitative": "YES", "statistics_reported": "n=10/group; exact figure values not transcribed", "topic_id": "M2B-T001", "tracker_id": "M2B-O029"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P042::M2A-P042-E002'
    AND et.evidence_type_name = '3D-bioprinted collagen/silk scaffold'
    AND ot.outcome_type_name = 'Nerve regeneration'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O029', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'NeuroRegen collagen scaffold plus hUC-MSCs after 12-week chronic rat scar resection was assessed by locomotion, motor/somatosensory evoked potentials, and histological repair.',
    '12 WPI scar resection',
    'NeuroRegen collagen scaffold plus hUC-MSCs after 12-week chronic rat scar resection was assessed by locomotion, motor/somatosensory evoked potentials, and histological repair.',
    'chronic rat scaffold/cell repair after scar resection',
    'Abstract',
    'Abstract',
    'medium',
    '{"curator_notes": "Chronic repair bridge; full text unavailable in tracker.", "experiment_tracker_id": "M2A-P002-E001", "paper_tracker_id": "M2A-P002", "quantitative": "YES", "statistics_reported": "exact values not extracted", "topic_id": "M2B-T002", "tracker_id": "M2B-O030"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P002::M2A-P002-E001'
    AND et.evidence_type_name = 'Chronic scar resection plus collagen/hUC-MSC scaffold'
    AND ot.outcome_type_name = 'Locomotor / electrophysiology / histology'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O030', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Chronic complete SCI scar resection plus dECM hydrogel and hNS/PC transplantation improved histological repair signals but did not show functional recovery in the Module 2A extraction.',
    'qualitative',
    'Chronic complete SCI scar resection plus dECM hydrogel and hNS/PC transplantation improved histological repair signals but did not show functional recovery in the Module 2A extraction.',
    'histological repair without functional recovery after dECM+hNS/PC chronic repair',
    'Abstract / source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Important chronic histology-function boundary.", "experiment_tracker_id": "M2A-P003-E001", "paper_tracker_id": "M2A-P003", "quantitative": "YES", "statistics_reported": "exact values not extracted", "topic_id": "M2B-T002", "tracker_id": "M2B-O031"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P003::M2A-P003-E001'
    AND et.evidence_type_name = 'dECM scaffold plus hNS/PC'
    AND ot.outcome_type_name = 'Histological repair / function boundary'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O031', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Methacrylamide chitosan hydrogel and conduit bridge delivered adult NSPCs with immobilized IFN-gamma or PDGF-AA to bias neuronal or oligodendrocytic lineages after rat hemisection SCI.',
    'qualitative',
    'Methacrylamide chitosan hydrogel and conduit bridge delivered adult NSPCs with immobilized IFN-gamma or PDGF-AA to bias neuronal or oligodendrocytic lineages after rat hemisection SCI.',
    'chitosan bridge couples cell delivery with lineage cues',
    'Abstract',
    'Abstract',
    'medium',
    '{"curator_notes": "A clear example of scaffold/cell/cue confounding by design.", "experiment_tracker_id": "M2A-P013-E001", "paper_tracker_id": "M2A-P013", "quantitative": "YES", "statistics_reported": "exact values not extracted", "topic_id": "M2B-T002", "tracker_id": "M2B-O032"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P013::M2A-P013-E001'
    AND et.evidence_type_name = 'Chitosan bridge plus NSPC and immobilized cues'
    AND ot.outcome_type_name = 'Lineage organization'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O032', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'dSCM/GelMA composite scaffold provided a bioactive microenvironment for human menstrual blood-derived stem cells and improved SCI functional reconstruction in rat in vivo testing.',
    'qualitative',
    'dSCM/GelMA composite scaffold provided a bioactive microenvironment for human menstrual blood-derived stem cells and improved SCI functional reconstruction in rat in vivo testing.',
    'spinal cord dECM/GelMA supports stem-cell repair',
    'Abstract',
    'Abstract',
    'medium',
    '{"curator_notes": "ECM and cell effects bundled.", "experiment_tracker_id": "M2A-P020-E001", "paper_tracker_id": "M2A-P020", "quantitative": "YES", "statistics_reported": "exact values not extracted", "topic_id": "M2B-T002", "tracker_id": "M2B-O033"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P020::M2A-P020-E001'
    AND et.evidence_type_name = 'dSCM/GelMA plus MenSC'
    AND ot.outcome_type_name = 'Cell support / functional reconstruction'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O033', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'HA hydrogel with decellularized brain matrix, PDRN, primed MSC EVs, and NPCs induced angiogenesis, anti-inflammatory/anti-apoptotic effects, neural differentiation, regeneration, and functional recovery in rat SCI.',
    'qualitative',
    'HA hydrogel with decellularized brain matrix, PDRN, primed MSC EVs, and NPCs induced angiogenesis, anti-inflammatory/anti-apoptotic effects, neural differentiation, regeneration, and functional recovery in rat SCI.',
    'multimodal hydrogel scaffold supports multi-process repair',
    'Abstract',
    'Abstract',
    'medium',
    '{"curator_notes": "Highly combinatorial; cannot attribute effect to one component.", "experiment_tracker_id": "M2A-P022-E001", "paper_tracker_id": "M2A-P022", "quantitative": "YES", "statistics_reported": "exact values not extracted", "topic_id": "M2B-T002", "tracker_id": "M2B-O034"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P022::M2A-P022-E001'
    AND et.evidence_type_name = 'DBM/PDRN/TI-EV/NPC hydrogel'
    AND ot.outcome_type_name = 'Multimodal regeneration'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O034', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Gelatin/alginate hydrogel seeded with hEnSCs and curcumin-loaded PLGA nanoparticles improved regeneration and anti-inflammatory repair effects in rat SCI.',
    'qualitative',
    'Gelatin/alginate hydrogel seeded with hEnSCs and curcumin-loaded PLGA nanoparticles improved regeneration and anti-inflammatory repair effects in rat SCI.',
    'hydrogel+cell+drug nanoparticle strategy improves repair profile',
    'Abstract',
    'Abstract',
    'medium',
    '{"curator_notes": "Triple combination limits causal attribution.", "experiment_tracker_id": "M2A-P023-E001", "paper_tracker_id": "M2A-P023", "quantitative": "YES", "statistics_reported": "exact values not extracted", "topic_id": "M2B-T002", "tracker_id": "M2B-O035"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P023::M2A-P023-E001'
    AND et.evidence_type_name = 'Gelatin/alginate + hEnSC + curcumin PLGA'
    AND ot.outcome_type_name = 'Regeneration / inflammation'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O035', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'hAECs attached uniformly to nanochitosan/polypyrrole-alginate; scaffold and/or Noggin increased FOX3, Calca, and MBP expression, while scaffold increased GFAP. Noggin loading was 22.6% with 75.3% entrapment efficiency, and 28.5% of incorporated Noggin was released over 12 days.',
    'percent; gene expression',
    'hAECs attached uniformly to nanochitosan/polypyrrole-alginate; scaffold and/or Noggin increased FOX3, Calca, and MBP expression, while scaffold increased GFAP. Noggin loading was 22.6% with 75.3% entrapment efficiency, and 28.5% of incorporated Noggin was released over 12 days.',
    'conductive chitosan scaffold supports hAEC attachment and mixed neural/glial marker induction with measurable Noggin release',
    'Full text Figs. 3-6',
    'Figs. 3-6',
    'high',
    '{"curator_notes": "Marker induction is not equivalent to mature functional neural differentiation.", "experiment_tracker_id": "M2A-P024-E001", "paper_tracker_id": "M2A-P024", "quantitative": "YES", "statistics_reported": "In vitro 21-day differentiation and 12-day release assays", "topic_id": "M2B-T002", "tracker_id": "M2B-O036"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P024::M2A-P024-E001'
    AND et.evidence_type_name = 'Conductive chitosan/alginate + hAEC + Noggin'
    AND ot.outcome_type_name = 'Neural differentiation / repair'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O036', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'CBD-modified miR21-loaded exosomes tethered to collagen-I scaffold improved local exosome retention, sustained release, and SCI repair logic.',
    'qualitative',
    'CBD-modified miR21-loaded exosomes tethered to collagen-I scaffold improved local exosome retention, sustained release, and SCI repair logic.',
    'collagen scaffold tethers engineered exosomes for sustained delivery',
    'Abstract',
    'Abstract',
    'medium',
    '{"curator_notes": "Cargo-delivery exemplar.", "experiment_tracker_id": "M2A-P007-E001", "paper_tracker_id": "M2A-P007", "quantitative": "YES", "statistics_reported": "exact values not extracted", "topic_id": "M2B-T003", "tracker_id": "M2B-O037"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P007::M2A-P007-E001'
    AND et.evidence_type_name = 'Collagen-I scaffold plus miR21 exosomes'
    AND ot.outcome_type_name = 'Retention / sustained release'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O037', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'After delayed implantation 5 days after T9 complete transection, bFGF/HEMA-MOETACL with acellular vascular matrix formed a bridge and reduced cavitation, supported axon and vessel ingrowth, and increased SSEP/MEP amplitude while shortening latency versus lesion, bFGF-only, and hydrogel-only groups.',
    'mm3; percent; SSEP/MEP',
    'After delayed implantation 5 days after T9 complete transection, bFGF/HEMA-MOETACL with acellular vascular matrix formed a bridge and reduced cavitation, supported axon and vessel ingrowth, and increased SSEP/MEP amplitude while shortening latency versus lesion, bFGF-only, and hydrogel-only groups.',
    'delayed bFGF hydrogel supports tissue, electrophysiological, and functional repair',
    'Full text Figs. 1-7',
    'Figs. 1-7',
    'high',
    '{"curator_notes": "bFGF and material effects remain partly inseparable; no clear astrocytic scar reduction versus lesion control.", "experiment_tracker_id": "M2A-P026-E001", "paper_tracker_id": "M2A-P026", "quantitative": "YES", "statistics_reported": "Combined cavity volume 2.41 +/- 0.80 versus 25.00 +/- 3.33 mm3 lesion control; hydrogel-alone did not show clear behavioral recovery", "topic_id": "M2B-T003", "tracker_id": "M2B-O038"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P026::M2A-P026-E001'
    AND et.evidence_type_name = 'bFGF hydrogel'
    AND ot.outcome_type_name = 'Tissue ingrowth / function'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O038', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Injectable collagen hydrogel and NT-3-loaded hydrogel increased functional recovery and altered neuronal growth, scar formation, inflammation, and collagen deposition after hemisection SCI.',
    '1 and 6 WPI',
    'Injectable collagen hydrogel and NT-3-loaded hydrogel increased functional recovery and altered neuronal growth, scar formation, inflammation, and collagen deposition after hemisection SCI.',
    'injectable NT-3 collagen scaffold supports local healing and function',
    'Abstract',
    'Abstract',
    'medium',
    '{"curator_notes": "Complements fibrin/NT-3 boundary.", "experiment_tracker_id": "M2A-P028-E001", "paper_tracker_id": "M2A-P028", "quantitative": "YES", "statistics_reported": "exact values not extracted", "topic_id": "M2B-T003", "tracker_id": "M2B-O039"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P028::M2A-P028-E001'
    AND et.evidence_type_name = 'NT-3 collagen hydrogel'
    AND ot.outcome_type_name = 'Function / local healing'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O039', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'In 14 female Beagles with right T10 4 mm hemisection, NT-3/fibroin gelatin sponge (n=7) improved 4-week Olby score to 11.85 +/- 0.64 versus 9.29 +/- 1.48 fibroin-only control, produced detectable CMEP versus negligible control signal, reduced IBA1+ cells at the graft (74.11 +/- 5.85 vs 98.41 +/- 15.43 cells/0.09 mm2), and increased NF+ fiber density; GFAP scar density was not different. EM also showed host-cell migration, vessels, synapse-like structures, and occasional MBP+ fibers in the NF-GS graft.',
    'quantitative',
    'In 14 female Beagles with right T10 4 mm hemisection, NT-3/fibroin gelatin sponge (n=7) improved 4-week Olby score to 11.85 +/- 0.64 versus 9.29 +/- 1.48 fibroin-only control, produced detectable CMEP versus negligible control signal, reduced IBA1+ cells at the graft (74.11 +/- 5.85 vs 98.41 +/- 15.43 cells/0.09 mm2), and increased NF+ fiber density; GFAP scar density was not different. EM also showed host-cell migration, vessels, synapse-like structures, and occasional MBP+ fibers in the NF-GS graft.',
    'large-animal NT-3/fibroin scaffold improves conduction and repair profile',
    'PMC6055812',
    'Full text',
    'high',
    '{"curator_notes": "Large-animal, short-follow-up evidence; GFAP scar did not improve and CMEP did not prove a fully reconstructed pathway.", "experiment_tracker_id": "M2A-P030-E002", "paper_tracker_id": "M2A-P030", "quantitative": "YES", "statistics_reported": "Exact Olby, IBA1, and NF/GFAP values extracted at 4 weeks", "topic_id": "M2B-T003", "tracker_id": "M2B-O040"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P030::M2A-P030-E002'
    AND et.evidence_type_name = 'NT-3/fibroin gelatin scaffold'
    AND ot.outcome_type_name = 'Conduction / inflammation / regeneration'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O040', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'PCL/polysialic-acid nanofiber scaffold with methylprednisolone reduced inflammatory cytokines, microglia/macrophage activation, and caspase-3 while supporting axonal regeneration and functional recovery after rat transection.',
    'qualitative',
    'PCL/polysialic-acid nanofiber scaffold with methylprednisolone reduced inflammatory cytokines, microglia/macrophage activation, and caspase-3 while supporting axonal regeneration and functional recovery after rat transection.',
    'drug-loaded nanofiber scaffold reduces inflammation and supports regeneration',
    'Abstract',
    'Abstract',
    'medium',
    '{"curator_notes": "Anti-inflammatory scaffold/cargo anchor.", "experiment_tracker_id": "M2A-P031-E001", "paper_tracker_id": "M2A-P031", "quantitative": "YES", "statistics_reported": "exact values not extracted", "topic_id": "M2B-T003", "tracker_id": "M2B-O041"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P031::M2A-P031-E001'
    AND et.evidence_type_name = 'PCL/PSA/MP nanofiber scaffold'
    AND ot.outcome_type_name = 'Inflammation / apoptosis / recovery'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O041', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'PEG/PAA/protein layer-by-layer films over agarose provided pH-triggered sustained protein release for more than four weeks in vitro; release rate depended on agarose concentration/porosity, polymer/protein assembly, and film degradation, and released lysozyme remained active early.',
    'quantitative direction',
    'PEG/PAA/protein layer-by-layer films over agarose provided pH-triggered sustained protein release for more than four weeks in vitro; release rate depended on agarose concentration/porosity, polymer/protein assembly, and film degradation, and released lysozyme remained active early.',
    'agarose channel scaffold can support controlled protein release',
    'PMC2830720',
    'Full text',
    'high',
    '{"curator_notes": "Protein-release method is translationally relevant but not an in-vivo SCI experiment.", "experiment_tracker_id": "M2A-P040-E001", "paper_tracker_id": "M2A-P040", "quantitative": "NO", "statistics_reported": "Full-text methods anchor; no SCI-animal efficacy test", "topic_id": "M2B-T003", "tracker_id": "M2B-O042"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P040::M2A-P040-E001'
    AND et.evidence_type_name = 'Functionalized agarose hydrogel'
    AND ot.outcome_type_name = 'Timed protein release'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O042', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'dECM hydrogel scaffold after chronic complete SCI scar resection supported cavitary lesion filling, vascular endothelial migration, microenvironment changes, and tissue repair signals.',
    'qualitative',
    'dECM hydrogel scaffold after chronic complete SCI scar resection supported cavitary lesion filling, vascular endothelial migration, microenvironment changes, and tissue repair signals.',
    'chronic dECM scaffold supports histological repair after scar resection',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Chronic ECM scaffold anchor.", "experiment_tracker_id": "M2A-P003-E001", "paper_tracker_id": "M2A-P003", "quantitative": "YES", "statistics_reported": "exact values not extracted", "topic_id": "M2B-T004", "tracker_id": "M2B-O043"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P003::M2A-P003-E001'
    AND et.evidence_type_name = 'dECM scaffold after chronic scar resection'
    AND ot.outcome_type_name = 'Angiogenesis / histology'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O043', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'dSCM/GelMA composite scaffold retained bioactive spinal cord matrix components and favorable microstructure/mechanics for stem-cell support.',
    'qualitative',
    'dSCM/GelMA composite scaffold retained bioactive spinal cord matrix components and favorable microstructure/mechanics for stem-cell support.',
    'spinal-cord-derived ECM/GelMA recreates local matrix niche',
    'Abstract',
    'Abstract',
    'medium',
    '{"curator_notes": "Material microenvironment observation.", "experiment_tracker_id": "M2A-P020-E001", "paper_tracker_id": "M2A-P020", "quantitative": "YES", "statistics_reported": "exact values not extracted", "topic_id": "M2B-T004", "tracker_id": "M2B-O044"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P020::M2A-P020-E001'
    AND et.evidence_type_name = 'spinal cord dECM/GelMA scaffold'
    AND ot.outcome_type_name = 'Bioactive microenvironment'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O044', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Decellularized brain matrix within HA hydrogel contributed to a composite scaffold designed to support angiogenesis, anti-inflammation, anti-apoptosis, and neural differentiation.',
    'qualitative',
    'Decellularized brain matrix within HA hydrogel contributed to a composite scaffold designed to support angiogenesis, anti-inflammation, anti-apoptosis, and neural differentiation.',
    'brain-derived ECM is used as bioactive component in multimodal scaffold',
    'Abstract',
    'Abstract',
    'medium',
    '{"curator_notes": "ECM component cannot be isolated from other cargos.", "experiment_tracker_id": "M2A-P022-E001", "paper_tracker_id": "M2A-P022", "quantitative": "YES", "statistics_reported": "exact values not extracted", "topic_id": "M2B-T004", "tracker_id": "M2B-O045"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P022::M2A-P022-E001'
    AND et.evidence_type_name = 'decellularized brain matrix hydrogel'
    AND ot.outcome_type_name = 'Multimodal repair'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O045', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Resected chronic human scar tissue was immunostained for CSPGs, vimentin, NF, nestin, Tuj-1, and S100 to verify scar identity before interpreting scaffold implantation.',
    'qualitative',
    'Resected chronic human scar tissue was immunostained for CSPGs, vimentin, NF, nestin, Tuj-1, and S100 to verify scar identity before interpreting scaffold implantation.',
    'chronic human resection target can be scar-marker rich and neural-marker poor',
    'Source page / M1A carried',
    'Clinical source page / M1A carried',
    'medium',
    '{"curator_notes": "Cross-links Module 1 lesion anatomy with scaffold targeting.", "experiment_tracker_id": "M2A-P001-E002", "paper_tracker_id": "M2A-P001", "quantitative": "YES", "statistics_reported": "exact marker values not extracted", "topic_id": "M2B-T005", "tracker_id": "M2B-O046"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P001::M2A-P001-E002'
    AND et.evidence_type_name = 'Human resected scar histology'
    AND ot.outcome_type_name = 'Scar identity'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O046', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'The chronic human cohort had no reported treatment-related adverse events over 1 year; 62.5% showed expanded sensation, 87.5% expanded MEP-responsive area, 3 cervical patients had increased finger flexibility, and 2 reported defecation sensation without sphincter control.',
    'percent; patients / year',
    'The chronic human cohort had no reported treatment-related adverse events over 1 year; 62.5% showed expanded sensation, 87.5% expanded MEP-responsive area, 3 cervical patients had increased finger flexibility, and 2 reported defecation sensation without sphincter control.',
    'chronic human scar-resection scaffold strategy feasible with partial neurological signals',
    'Full text Figs. 1-2 and Tables 1-2',
    'Figs. 1-2; Tables 1-2',
    'high',
    '{"curator_notes": "Human chronic strategy remains a feasibility signal rather than controlled efficacy evidence.", "experiment_tracker_id": "M2A-P009-E001", "paper_tracker_id": "M2A-P009", "quantitative": "YES", "statistics_reported": "No ASIA classification improved; rehabilitation and no-treatment control limit efficacy inference", "topic_id": "M2B-T005", "tracker_id": "M2B-O047"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P009::M2A-P009-E001'
    AND et.evidence_type_name = 'Chronic human scar resection plus scaffold/cell'
    AND ot.outcome_type_name = 'Safety / sensory recovery'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O047', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Aligned fibrin hydrogel plus functionalized self-assembling peptide formed an interpenetrating composite presenting structural and biochemical cues to enhance SCI regeneration.',
    'qualitative',
    'Aligned fibrin hydrogel plus functionalized self-assembling peptide formed an interpenetrating composite presenting structural and biochemical cues to enhance SCI regeneration.',
    'composite hydrogel combines guidance and regulatory cues',
    'Abstract',
    'Abstract',
    'medium',
    '{"curator_notes": "Connects passive guidance to active cue delivery.", "experiment_tracker_id": "M2A-P019-E001", "paper_tracker_id": "M2A-P019", "quantitative": "YES", "statistics_reported": "exact values not extracted", "topic_id": "M2B-T007", "tracker_id": "M2B-O048"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P019::M2A-P019-E001'
    AND et.evidence_type_name = 'AFG/fSAP composite hydrogel'
    AND ot.outcome_type_name = 'Biophysical and biochemical cues'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O048', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'review-map supports material- and model-specific interpretation',
    'qualitative',
    'review-map supports material- and model-specific interpretation',
    NULL,
    'Review map',
    'Review synthesis',
    'medium',
    '{"curator_notes": "Prevents one-size-fits-all scaffold conclusions.", "experiment_tracker_id": "Review anchors", "paper_tracker_id": "M2A-R002-M2A-R004", "quantitative": "NO", "statistics_reported": "review-level", "topic_id": "M2B-T008", "tracker_id": "M2B-O049"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-R002-M2A-R004::Review anchors'
    AND et.evidence_type_name = 'Material taxonomy / translation'
    AND ot.outcome_type_name = 'Hydrogel and biomaterial reviews frame SCI scaffolds as bridges, delivery reservoirs, and cell carriers, but emphasize that material class, lesion geometry, and combination therapy determine interpretability.'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O049', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'review-map supports combination-therapy caution',
    'qualitative',
    'review-map supports combination-therapy caution',
    NULL,
    'Review map',
    'Review synthesis',
    'medium',
    '{"curator_notes": "Supports boundary records B002 and B005.", "experiment_tracker_id": "Review anchors", "paper_tracker_id": "M2A-R005-M2A-R008", "quantitative": "NO", "statistics_reported": "review-level", "topic_id": "M2B-T008", "tracker_id": "M2B-O050"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-R005-M2A-R008::Review anchors'
    AND et.evidence_type_name = 'Cell therapy / chronic translation'
    AND ot.outcome_type_name = 'Scaffold-supported cell transplantation reviews emphasize that cells, scaffolds, growth factors, timing, and chronic lesion state interact, limiting simple causal claims.'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O050', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Wang N 2018 M2A-P002-E002 preserves a distinct Rattus norvegicus experiment testing Collagen scaffold plus hUC-MSC implantation with endpoint/readout: NeuroRegen collagen scaffold and hUC-MSCs implanted into the resected cavity were assessed by locomotion, motor/somatosensory evoked potentials, and histological repair outcomes..',
    'qualitative',
    'Wang N 2018 M2A-P002-E002 preserves a distinct Rattus norvegicus experiment testing Collagen scaffold plus hUC-MSC implantation with endpoint/readout: NeuroRegen collagen scaffold and hUC-MSCs implanted into the resected cavity were assessed by locomotion, motor/somatosensory evoked potentials, and histological repair outcomes..',
    'M2A-P002-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Collagen scaffold combined with human umbilical cord-derived mesenchymal stem cells promote functional recovery after scar resection in rats with chronic spinal cord injury. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M2A-P002-E002", "paper_tracker_id": "M2A-P002", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M2B-T002", "tracker_id": "M2B-O051"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P002::M2A-P002-E002'
    AND et.evidence_type_name = 'Chronic scar resection plus collagen/hUC-MSC scaffold'
    AND ot.outcome_type_name = 'NeuroRegen collagen scaffold and hUC-MSCs implanted into the resected cavity were assessed by locomotion, motor/somatosensory evoked potentials, and histological repair outcomes.'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O051', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Ito K 2024 M2A-P003-E002 preserves a distinct Rodent chronic complete SCI model experiment testing hNS/PC transplantation with scaffold support with endpoint/readout: Human iPSC-derived NS/PC transplantation was combined with scaffold-supported scar resection to assess graft survival, host axon regeneration, histological repair, and lack of functional recovery..',
    'qualitative',
    'Ito K 2024 M2A-P003-E002 preserves a distinct Rodent chronic complete SCI model experiment testing hNS/PC transplantation with scaffold support with endpoint/readout: Human iPSC-derived NS/PC transplantation was combined with scaffold-supported scar resection to assess graft survival, host axon regeneration, histological repair, and lack of functional recovery..',
    'M2A-P003-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract/source page / M1A carried',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Histological effects of combined therapy involving scar resection, decellularized scaffolds, and human iPSC-NS/PCs transplantation in chronic complete spinal cord injury. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M2A-P003-E002", "paper_tracker_id": "M2A-P003", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M2B-T002", "tracker_id": "M2B-O052"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P003::M2A-P003-E002'
    AND et.evidence_type_name = 'dECM scaffold plus hNS/PC'
    AND ot.outcome_type_name = 'Human iPSC-derived NS/PC transplantation was combined with scaffold-supported scar resection to assess graft survival, host axon regeneration, histological repair, and lack of functional recovery.'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O052', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'In acute T3 complete transection, NPC-loaded scaffolds supported NPC differentiation, 87 +/- 5 serotonergic axons beyond the scaffold at 6 months, BBB 6.6 +/- 0.5 versus 0.3 +/- 0.2 empty scaffold and 1.6 +/- 0.8 NPC-only, and MEP 270 +/- 5 versus 25.1 +/- 5.7 microV. Retransection abolished MEPs, supporting a scaffold-dependent relay.',
    'BBB; microV',
    'In acute T3 complete transection, NPC-loaded scaffolds supported NPC differentiation, 87 +/- 5 serotonergic axons beyond the scaffold at 6 months, BBB 6.6 +/- 0.5 versus 0.3 +/- 0.2 empty scaffold and 1.6 +/- 0.8 NPC-only, and MEP 270 +/- 5 versus 25.1 +/- 5.7 microV. Retransection abolished MEPs, supporting a scaffold-dependent relay.',
    'NPC-loaded architecture supports relay-associated functional recovery; NPCs without scaffold were insufficient',
    'Full text Figs. 3-4',
    'Figs. 3-4',
    'high',
    '{"curator_notes": "Combination therapy; scaffold-only functional effect is not claimed.", "experiment_tracker_id": "M2A-P004-E002", "paper_tracker_id": "M2A-P004", "quantitative": "YES", "statistics_reported": "P < 0.0001 for BBB/MEP comparisons; n = 10", "topic_id": "M2B-T001", "tracker_id": "M2B-O053"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P004::M2A-P004-E002'
    AND et.evidence_type_name = '3D printing / NPC graft scaffold'
    AND ot.outcome_type_name = 'NPC survival, neural relay, and function'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O053', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'At 8 weeks, 5-tube composites reached 1744 +/- 920 axons/mm2 rostrally and 1436 +/- 567 caudally versus 456 +/- 113 with gelfoam; approximately 30% of tube axons were myelinated, and PEG tubes/bridges reached approximately BMS 6 versus 3 with gelfoam. Tube-versus-bridge superiority was not established.',
    'axons/mm2; BMS',
    'At 8 weeks, 5-tube composites reached 1744 +/- 920 axons/mm2 rostrally and 1436 +/- 567 caudally versus 456 +/- 113 with gelfoam; approximately 30% of tube axons were myelinated, and PEG tubes/bridges reached approximately BMS 6 versus 3 with gelfoam. Tube-versus-bridge superiority was not established.',
    'aligned tubes improve axon density and locomotion in this hemisection model, with incomplete and comparator-limited myelination evidence',
    'Full text Figs. 5-7',
    'Figs. 5-7',
    'high',
    '{"curator_notes": "This is a proof-of-concept penetrating injury, not a contusion model.", "experiment_tracker_id": "M2A-P005-E002", "paper_tracker_id": "M2A-P005", "quantitative": "YES", "statistics_reported": "n = 6; P < 0.01 for key axon comparisons", "topic_id": "M2B-T001", "tracker_id": "M2B-O054"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P005::M2A-P005-E002'
    AND et.evidence_type_name = 'Aligned hydrogel scaffold'
    AND ot.outcome_type_name = 'Axon density, myelination, and locomotion'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O054', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Huang L 2020 M2A-P006-E002 preserves a distinct Rattus norvegicus experiment testing Anisotropic alginate hydrogel channels with endpoint/readout: Histology assessed host-cell migration, fibroglial scarring, and regeneration of corticospinal, raphaespinal, propriospinal, and ascending sensory axons through and beyond hydrogel channels..',
    'qualitative',
    'Huang L 2020 M2A-P006-E002 preserves a distinct Rattus norvegicus experiment testing Anisotropic alginate hydrogel channels with endpoint/readout: Histology assessed host-cell migration, fibroglial scarring, and regeneration of corticospinal, raphaespinal, propriospinal, and ascending sensory axons through and beyond hydrogel channels..',
    'M2A-P006-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Anisotropic Alginate Hydrogels Promote Axonal Growth across Chronic Spinal Cord Transections after Scar Removal. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M2A-P006-E002", "paper_tracker_id": "M2A-P006", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M2B-T005", "tracker_id": "M2B-O055"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P006::M2A-P006-E002'
    AND et.evidence_type_name = 'Chronic scar removal plus anisotropic hydrogel'
    AND ot.outcome_type_name = 'Histology assessed host-cell migration, fibroglial scarring, and regeneration of corticospinal, raphaespinal, propriospinal, and ascending sensory axons through and beyond hydrogel channels.'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O055', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Liu X 2022 M2A-P007-E002 preserves a distinct SCI model context experiment testing Functionalized collagen-I scaffold with miR21-loaded exosomes with endpoint/readout: A collagen-I scaffold enriched with CBD-LP-miR21 exosomes was applied to SCI repair to improve exosome retention, sustained release, and repair outcomes..',
    'qualitative',
    'Liu X 2022 M2A-P007-E002 preserves a distinct SCI model context experiment testing Functionalized collagen-I scaffold with miR21-loaded exosomes with endpoint/readout: A collagen-I scaffold enriched with CBD-LP-miR21 exosomes was applied to SCI repair to improve exosome retention, sustained release, and repair outcomes..',
    'M2A-P007-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: A functionalized collagen-I scaffold delivers microRNA 21-loaded exosomes for spinal cord injury repair. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M2A-P007-E002", "paper_tracker_id": "M2A-P007", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M2B-T003", "tracker_id": "M2B-O056"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P007::M2A-P007-E002'
    AND et.evidence_type_name = 'Collagen-I scaffold plus miR21 exosomes'
    AND ot.outcome_type_name = 'A collagen-I scaffold enriched with CBD-LP-miR21 exosomes was applied to SCI repair to improve exosome retention, sustained release, and repair outcomes.'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O056', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'miR-222-loaded scaffolds achieved 0.5 microgram/mg loading with approximately 16% efficiency; 27.1 +/- 3.38% released in the first month and release remained detectable for at least two more months. miR-222 increased neurite ingrowth at 10 days without changing microglial or astrocyte reactions; Cy5-ODN spread approximately 300 micrometers from the scaffold edge at 14 days.',
    'microgram/mg; percent; micrometers',
    'miR-222-loaded scaffolds achieved 0.5 microgram/mg loading with approximately 16% efficiency; 27.1 +/- 3.38% released in the first month and release remained detectable for at least two more months. miR-222 increased neurite ingrowth at 10 days without changing microglial or astrocyte reactions; Cy5-ODN spread approximately 300 micrometers from the scaffold edge at 14 days.',
    'localized nonviral miRNA delivery enhances early neurite ingrowth without detectable glial reaction increase',
    'Full text Fig. 6 and Supplementary Fig. 1',
    'Fig. 6 and Supplementary Fig. 1',
    'high',
    '{"curator_notes": "This does not establish long-term functional recovery.", "experiment_tracker_id": "M2A-P008-E002", "paper_tracker_id": "M2A-P008", "quantitative": "YES", "statistics_reported": "values reported in Results", "topic_id": "M2B-T001", "tracker_id": "M2B-O057"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P008::M2A-P008-E002'
    AND et.evidence_type_name = 'Aligned nanofiber-hydrogel scaffold'
    AND ot.outcome_type_name = 'miRNA delivery and inflammatory boundary'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O057', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Moore MJ 2006 M2A-P010-E002 preserves a distinct Rodent SCI model context experiment testing Multi-channel biodegradable scaffold platform with endpoint/readout: The scaffold was framed as a platform to test architecture, transplanted cells, and local molecular agents for axon regeneration..',
    'qualitative',
    'Moore MJ 2006 M2A-P010-E002 preserves a distinct Rodent SCI model context experiment testing Multi-channel biodegradable scaffold platform with endpoint/readout: The scaffold was framed as a platform to test architecture, transplanted cells, and local molecular agents for axon regeneration..',
    'M2A-P010-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Multiple-channel scaffolds to promote spinal cord axon regeneration. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M2A-P010-E002", "paper_tracker_id": "M2A-P010", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M2B-T001", "tracker_id": "M2B-O058"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P010::M2A-P010-E002'
    AND et.evidence_type_name = 'Scaffold fabrication / platform'
    AND ot.outcome_type_name = 'The scaffold was framed as a platform to test architecture, transplanted cells, and local molecular agents for axon regeneration.'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O058', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Guo J 2007 M2A-P011-E002 preserves a distinct Rattus norvegicus experiment testing SAPNS lesion bridge with endpoint/readout: Host-cell migration, blood-vessel growth, and axonal ingrowth into SAPNS were assessed as evidence of a 3D permissive environment..',
    'qualitative',
    'Guo J 2007 M2A-P011-E002 preserves a distinct Rattus norvegicus experiment testing SAPNS lesion bridge with endpoint/readout: Host-cell migration, blood-vessel growth, and axonal ingrowth into SAPNS were assessed as evidence of a 3D permissive environment..',
    'M2A-P011-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Reknitting the injured spinal cord by self-assembling peptide nanofiber scaffold. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M2A-P011-E002", "paper_tracker_id": "M2A-P011", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M2B-T001", "tracker_id": "M2B-O059"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P011::M2A-P011-E002'
    AND et.evidence_type_name = 'Peptide nanofiber scaffold'
    AND ot.outcome_type_name = 'Host-cell migration, blood-vessel growth, and axonal ingrowth into SAPNS were assessed as evidence of a 3D permissive environment.'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O059', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Kang KN 2012 M2A-P012-E002 preserves a distinct Rattus norvegicus experiment testing hMSC-seeded PLGA scaffold with endpoint/readout: Different hMSC doses were compared for BBB locomotor scores, MEP amplitudes, cell survival, differentiation, and neurological repair..',
    'qualitative',
    'Kang KN 2012 M2A-P012-E002 preserves a distinct Rattus norvegicus experiment testing hMSC-seeded PLGA scaffold with endpoint/readout: Different hMSC doses were compared for BBB locomotor scores, MEP amplitudes, cell survival, differentiation, and neurological repair..',
    'M2A-P012-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Tissue engineered regeneration of completely transected spinal cord using human mesenchymal stem cells. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M2A-P012-E002", "paper_tracker_id": "M2A-P012", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M2B-T002", "tracker_id": "M2B-O060"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P012::M2A-P012-E002'
    AND et.evidence_type_name = 'PLGA scaffold plus hMSC'
    AND ot.outcome_type_name = 'Different hMSC doses were compared for BBB locomotor scores, MEP amplitudes, cell survival, differentiation, and neurological repair.'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O060', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Li H 2016 M2A-P013-E002 preserves a distinct Rattus norvegicus / NSPC bridge experiment testing Immobilized IFN-gamma or PDGF-AA lineage cues with endpoint/readout: Biotin-tagged IFN-gamma and PDGF-AA were immobilized to MAC hydrogel to cue neuronal or oligodendrocytic lineages within the bridge..',
    'qualitative',
    'Li H 2016 M2A-P013-E002 preserves a distinct Rattus norvegicus / NSPC bridge experiment testing Immobilized IFN-gamma or PDGF-AA lineage cues with endpoint/readout: Biotin-tagged IFN-gamma and PDGF-AA were immobilized to MAC hydrogel to cue neuronal or oligodendrocytic lineages within the bridge..',
    'M2A-P013-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: A Hydrogel Bridge Incorporating Immobilized Growth Factors and Neural Stem/Progenitor Cells to Treat Spinal Cord Injury. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M2A-P013-E002", "paper_tracker_id": "M2A-P013", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M2B-T002", "tracker_id": "M2B-O061"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P013::M2A-P013-E002'
    AND et.evidence_type_name = 'Chitosan bridge plus NSPC and immobilized cues'
    AND ot.outcome_type_name = 'Biotin-tagged IFN-gamma and PDGF-AA were immobilized to MAC hydrogel to cue neuronal or oligodendrocytic lineages within the bridge.'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O061', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'In male Wistar Th8 hemisection, both 8 mg/mL porcine SC-ECM and UB-ECM hydrogels increased NF160 axon ingrowth and RECA vascularization versus saline, but macrophage infiltration, rapid degradation, progressive cysts, and absent demonstrated functional recovery constrained interpretation.',
    'weeks',
    'In male Wistar Th8 hemisection, both 8 mg/mL porcine SC-ECM and UB-ECM hydrogels increased NF160 axon ingrowth and RECA vascularization versus saline, but macrophage infiltration, rapid degradation, progressive cysts, and absent demonstrated functional recovery constrained interpretation.',
    'ECM hydrogel provides a transient ingrowth/vascular substrate but is not yet a durable functional bridge',
    'Full text Figs. 2-7',
    'Figs. 2-7',
    'high',
    '{"curator_notes": "No significant SC- versus UB-ECM differences; cell-seeded SC-ECM did not improve axon/vessel ingrowth.", "experiment_tracker_id": "M2A-P014-E002", "paper_tracker_id": "M2A-P014", "quantitative": "YES", "statistics_reported": "n = 5/group/timepoint; qPCR at 2, 4, 8 weeks", "topic_id": "M2B-T004", "tracker_id": "M2B-O062"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P014::M2A-P014-E002'
    AND et.evidence_type_name = 'Injectable ECM hydrogel'
    AND ot.outcome_type_name = 'Tissue bridging and material limitation'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O062', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Functionalized NeuroRegen increased Tuj-1/Map2 and 5-HT-positive neurons, remyelinated axons, and lesion-site synaptophysin while reducing CS-56/CSPG signal at 1 year; human MSCs were not detected at 6 months.',
    'neurons; myelin; synaptophysin; CSPG',
    'Functionalized NeuroRegen increased Tuj-1/Map2 and 5-HT-positive neurons, remyelinated axons, and lesion-site synaptophysin while reducing CS-56/CSPG signal at 1 year; human MSCs were not detected at 6 months.',
    'M2A-P015-E002 preserves distinct histological mechanism and source-cell boundary',
    'Full text Figs. 2-7',
    'Figs. 2-7',
    'high',
    '{"curator_notes": "New neurons were not proven to derive from transplanted MSCs; scaffold and scar-resection effects remain separable boundaries.", "experiment_tracker_id": "M2A-P015-E002", "paper_tracker_id": "M2A-P015", "quantitative": "YES", "statistics_reported": "Full text Figs. 2-7", "topic_id": "M2B-T005", "tracker_id": "M2B-O063"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P015::M2A-P015-E002'
    AND et.evidence_type_name = 'Chronic canine scar removal plus NeuroRegen/hUC-MSC'
    AND ot.outcome_type_name = 'Endogenous neurons, remyelination, synapses, and secondary scar were assessed after functionalized NeuroRegen implantation.'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O063', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'At 8 weeks, SC/iPN grafts were larger and contained about twice as many SC-myelinated axons as SC/Matrigel grafts, while BBB scores were comparable and early grid-walk benefit did not persist.',
    'graft volume; axon count; BBB; grid walk',
    'At 8 weeks, SC/iPN grafts were larger and contained about twice as many SC-myelinated axons as SC/Matrigel grafts, while BBB scores were comparable and early grid-walk benefit did not persist.',
    'iPN provides a histological/graft-survival advantage without durable behavioral superiority',
    'Full text Figs. 6-8',
    'Figs. 6-8',
    'high',
    '{"curator_notes": "Matrix degraded or was not visible by 8 weeks; immune response was not aggravated by iPN.", "experiment_tracker_id": "M2A-P016-E002", "paper_tracker_id": "M2A-P016", "quantitative": "YES", "statistics_reported": "Full text Figs. 6-8", "topic_id": "M2B-T002", "tracker_id": "M2B-O064"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P016::M2A-P016-E002'
    AND et.evidence_type_name = 'dPN matrix plus Schwann cells'
    AND ot.outcome_type_name = 'Implant size, immune infiltration, Schwann-cell myelinated axons, axon growth, and BBB locomotor performance were assessed.'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O064', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Zou Y 2020 M2A-P018-E002 preserves a distinct Rattus norvegicus experiment testing Aligned collagen scaffold-guided NSPC repair with endpoint/readout: Outcomes addressed cell retention, axonal guidance, neuronal regeneration microenvironment, and functional recovery according to abstract..',
    'qualitative',
    'Zou Y 2020 M2A-P018-E002 preserves a distinct Rattus norvegicus experiment testing Aligned collagen scaffold-guided NSPC repair with endpoint/readout: Outcomes addressed cell retention, axonal guidance, neuronal regeneration microenvironment, and functional recovery according to abstract..',
    'M2A-P018-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Aligned collagen scaffold combination with human spinal cord-derived neural stem cells to improve spinal cord injury repair. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M2A-P018-E002", "paper_tracker_id": "M2A-P018", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M2B-T001", "tracker_id": "M2B-O065"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P018::M2A-P018-E002'
    AND et.evidence_type_name = 'Aligned collagen scaffold plus NSPCs'
    AND ot.outcome_type_name = 'Outcomes addressed cell retention, axonal guidance, neuronal regeneration microenvironment, and functional recovery according to abstract.'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O065', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Man W 2021 M2A-P019-E002 preserves a distinct Rodent model context experiment testing Multimodal composite hydrogel with endpoint/readout: Regeneration outcomes were assessed to test whether combined guidance and biochemical cues improved spinal cord repair..',
    'qualitative',
    'Man W 2021 M2A-P019-E002 preserves a distinct Rodent model context experiment testing Multimodal composite hydrogel with endpoint/readout: Regeneration outcomes were assessed to test whether combined guidance and biochemical cues improved spinal cord repair..',
    'M2A-P019-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: A multi-modal delivery strategy for spinal cord regeneration using a composite hydrogel presenting biophysical and biochemical cues synergistically. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M2A-P019-E002", "paper_tracker_id": "M2A-P019", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M2B-T007", "tracker_id": "M2B-O066"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P019::M2A-P019-E002'
    AND et.evidence_type_name = 'AFG/fSAP composite hydrogel'
    AND ot.outcome_type_name = 'Regeneration outcomes were assessed to test whether combined guidance and biochemical cues improved spinal cord repair.'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O066', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'He W 2022 M2A-P020-E002 preserves a distinct Rattus norvegicus experiment testing dSCM/GelMA scaffold + MenSC with endpoint/readout: In vitro and in vivo experiments evaluated whether the composite scaffold supported human menstrual blood-derived stem cells and improved functional reconstruction after SCI..',
    'qualitative',
    'He W 2022 M2A-P020-E002 preserves a distinct Rattus norvegicus experiment testing dSCM/GelMA scaffold + MenSC with endpoint/readout: In vitro and in vivo experiments evaluated whether the composite scaffold supported human menstrual blood-derived stem cells and improved functional reconstruction after SCI..',
    'M2A-P020-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: A decellularized spinal cord extracellular matrix-gel/GelMA hydrogel three-dimensional composite scaffold promotes recovery from spinal cord injury via synergism with human menstrual blood-derived stem cells. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M2A-P020-E002", "paper_tracker_id": "M2A-P020", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M2B-T002", "tracker_id": "M2B-O067"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P020::M2A-P020-E002'
    AND et.evidence_type_name = 'dSCM/GelMA plus MenSC'
    AND ot.outcome_type_name = 'In vitro and in vivo experiments evaluated whether the composite scaffold supported human menstrual blood-derived stem cells and improved functional reconstruction after SCI.'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O067', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Tran KA 2022 M2A-P021-E002 preserves a distinct Rat SCI model context experiment testing Injectable aligned peptide hydrogel scaffold with endpoint/readout: In vivo validation assessed whether aligned injectable hydrogel promoted and oriented axon infiltration at the SCI site..',
    'qualitative',
    'Tran KA 2022 M2A-P021-E002 preserves a distinct Rat SCI model context experiment testing Injectable aligned peptide hydrogel scaffold with endpoint/readout: In vivo validation assessed whether aligned injectable hydrogel promoted and oriented axon infiltration at the SCI site..',
    'M2A-P021-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Magnetic alignment of injectable hydrogel scaffolds for spinal cord injury repair. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M2A-P021-E002", "paper_tracker_id": "M2A-P021", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M2B-T001", "tracker_id": "M2B-O068"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P021::M2A-P021-E002'
    AND et.evidence_type_name = 'Magnetically aligned injectable peptide hydrogel'
    AND ot.outcome_type_name = 'In vivo validation assessed whether aligned injectable hydrogel promoted and oriented axon infiltration at the SCI site.'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O068', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Roh EJ 2023 M2A-P022-E002 preserves a distinct Rattus norvegicus experiment testing Bioactive multimodal hydrogel with endpoint/readout: Rat SCI testing assessed angiogenesis, anti-inflammatory and anti-apoptotic effects, neural differentiation, regeneration, and functional recovery..',
    'qualitative',
    'Roh EJ 2023 M2A-P022-E002 preserves a distinct Rattus norvegicus experiment testing Bioactive multimodal hydrogel with endpoint/readout: Rat SCI testing assessed angiogenesis, anti-inflammatory and anti-apoptotic effects, neural differentiation, regeneration, and functional recovery..',
    'M2A-P022-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Multimodal therapy strategy based on a bioactive hydrogel for repair of spinal cord injury. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M2A-P022-E002", "paper_tracker_id": "M2A-P022", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M2B-T002", "tracker_id": "M2B-O069"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P022::M2A-P022-E002'
    AND et.evidence_type_name = 'DBM/PDRN/TI-EV/NPC hydrogel'
    AND ot.outcome_type_name = 'Rat SCI testing assessed angiogenesis, anti-inflammatory and anti-apoptotic effects, neural differentiation, regeneration, and functional recovery.'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O069', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Ai A 2023 M2A-P023-E002 preserves a distinct Rattus norvegicus experiment testing hEnSC and curcumin-PLGA hydrogel scaffold with endpoint/readout: In vivo rat SCI experiments evaluated regeneration and anti-inflammatory repair effects of the combined scaffold strategy..',
    'qualitative',
    'Ai A 2023 M2A-P023-E002 preserves a distinct Rattus norvegicus experiment testing hEnSC and curcumin-PLGA hydrogel scaffold with endpoint/readout: In vivo rat SCI experiments evaluated regeneration and anti-inflammatory repair effects of the combined scaffold strategy..',
    'M2A-P023-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Enhanced spinal cord regeneration by gelatin/alginate hydrogel scaffolds containing human endometrial stem cells and curcumin-loaded PLGA nanoparticles in rat. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M2A-P023-E002", "paper_tracker_id": "M2A-P023", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M2B-T002", "tracker_id": "M2B-O070"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P023::M2A-P023-E002'
    AND et.evidence_type_name = 'Gelatin/alginate + hEnSC + curcumin PLGA'
    AND ot.outcome_type_name = 'In vivo rat SCI experiments evaluated regeneration and anti-inflammatory repair effects of the combined scaffold strategy.'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O070', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Noggin+hAEC scaffold reached BBB 14.0 +/- 1.43 versus 9.5 +/- 1.52 lesion control at 4 weeks; scaffold+hAEC reached 13.5 +/- 0.7 and Noggin scaffold 12.5 +/- 0.51. hAEC groups reduced Iba1/GFAP and increased beta-tubulin/MBP, with labeled cells surviving at 4 weeks.',
    'BBB; Iba1; GFAP; beta-tubulin; MBP',
    'Noggin+hAEC scaffold reached BBB 14.0 +/- 1.43 versus 9.5 +/- 1.52 lesion control at 4 weeks; scaffold+hAEC reached 13.5 +/- 0.7 and Noggin scaffold 12.5 +/- 0.51. hAEC groups reduced Iba1/GFAP and increased beta-tubulin/MBP, with labeled cells surviving at 4 weeks.',
    'M2A-P024-E002 preserves distinct in vivo combination-therapy evidence and marker/behavior boundary',
    'Full text Figs. 7-10',
    'Figs. 7-10',
    'high',
    '{"curator_notes": "Combined scaffold, hAEC, and Noggin performed best; marker and BBB results do not establish long-term functional connectivity.", "experiment_tracker_id": "M2A-P024-E002", "paper_tracker_id": "M2A-P024", "quantitative": "YES", "statistics_reported": "n=6/group; 4-week endpoint", "topic_id": "M2B-T002", "tracker_id": "M2B-O071"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P024::M2A-P024-E002'
    AND et.evidence_type_name = 'Conductive chitosan/alginate + hAEC + Noggin'
    AND ot.outcome_type_name = 'In vivo motor, neural-marker, inflammatory, and scar response were assessed after right T10-T11 hemisection.'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O071', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Controlled NT-3 release increased early neuronal fiber sprouting and fibrin reduced white-matter-border GFAP, but BBB hindlimb function did not improve relative to controls at 12 weeks and macrophage/microglia density did not differ.',
    'BBB; Tuj1; GFAP; ED-1',
    'Controlled NT-3 release increased early neuronal fiber sprouting and fibrin reduced white-matter-border GFAP, but BBB hindlimb function did not improve relative to controls at 12 weeks and macrophage/microglia density did not differ.',
    'histology-positive/function-negative controlled-release boundary',
    'Full text Figs. 5-7',
    'Figs. 5-7',
    'high',
    '{"curator_notes": "Functional recovery was not observed despite early sprouting.", "experiment_tracker_id": "M2A-P025-E002", "paper_tracker_id": "M2A-P025", "quantitative": "YES", "statistics_reported": "9-day histology; 12-week BBB", "topic_id": "M2B-T003", "tracker_id": "M2B-O072"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P025::M2A-P025-E002'
    AND et.evidence_type_name = 'Fibrin scaffold controlled release'
    AND ot.outcome_type_name = 'Neuronal fiber growth, glial scar formation, and hindlimb motor function were compared across NT-3 scaffold, control scaffold, and saline groups.'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O072', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Combined bFGF/HEMA-MOETACL reduced cavitation to 2.41 +/- 0.80 mm3 and 1.28% versus 25.00 +/- 3.33 mm3 and 16.00% in lesion controls, increased axon and vessel ingrowth, and improved SSEP/MEP amplitude and latency; hydrogel alone reduced cavitation without clear behavioral recovery.',
    'mm3; percent; SSEP/MEP',
    'Combined bFGF/HEMA-MOETACL reduced cavitation to 2.41 +/- 0.80 mm3 and 1.28% versus 25.00 +/- 3.33 mm3 and 16.00% in lesion controls, increased axon and vessel ingrowth, and improved SSEP/MEP amplitude and latency; hydrogel alone reduced cavitation without clear behavioral recovery.',
    'M2A-P026-E002 preserves distinct material-plus-cargo evidence and cavitation/electrophysiology boundary',
    'Full text Figs. 3-7',
    'Figs. 3-7',
    'high',
    '{"curator_notes": "Material effect is evident in cavitation; bFGF adds axon/vessel/electrophysiological signal.", "experiment_tracker_id": "M2A-P026-E002", "paper_tracker_id": "M2A-P026", "quantitative": "YES", "statistics_reported": "8-week endpoint; no foreign-body reaction observed", "topic_id": "M2B-T003", "tracker_id": "M2B-O073"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P026::M2A-P026-E002'
    AND et.evidence_type_name = 'bFGF hydrogel'
    AND ot.outcome_type_name = 'Tissue ingrowth, nerve regeneration, electrophysiology, and functional recovery were assessed after hydrogel implantation.'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O073', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Wen Y 2016 M2A-P027-E002 preserves a distinct Rattus norvegicus experiment testing HA+PLGA multi-cargo scaffold with endpoint/readout: Host integration, inflammation, gliosis, vascularization, regenerated nerve fibers, and locomotor recovery were assessed after implantation..',
    'qualitative',
    'Wen Y 2016 M2A-P027-E002 preserves a distinct Rattus norvegicus experiment testing HA+PLGA multi-cargo scaffold with endpoint/readout: Host integration, inflammation, gliosis, vascularization, regenerated nerve fibers, and locomotor recovery were assessed after implantation..',
    'M2A-P027-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Spinal cord injury repair by implantation of structured hyaluronic acid scaffold with PLGA microspheres in the rat. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M2A-P027-E002", "paper_tracker_id": "M2A-P027", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M2B-T003", "tracker_id": "M2B-O074"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P027::M2A-P027-E002'
    AND et.evidence_type_name = 'HA scaffold plus PLGA cargo'
    AND ot.outcome_type_name = 'Host integration, inflammation, gliosis, vascularization, regenerated nerve fibers, and locomotor recovery were assessed after implantation.'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O074', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Breen BA 2017 M2A-P028-E002 preserves a distinct Rattus norvegicus experiment testing NT-3 collagen scaffold with endpoint/readout: BBB locomotion, neuronal growth, glial scar formation, inflammation, and collagen deposition were assessed..',
    'qualitative',
    'Breen BA 2017 M2A-P028-E002 preserves a distinct Rattus norvegicus experiment testing NT-3 collagen scaffold with endpoint/readout: BBB locomotion, neuronal growth, glial scar formation, inflammation, and collagen deposition were assessed..',
    'M2A-P028-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Therapeutic Effect of Neurotrophin-3 Treatment in an Injectable Collagen Scaffold Following Rat Spinal Cord Hemisection Injury. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M2A-P028-E002", "paper_tracker_id": "M2A-P028", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M2B-T003", "tracker_id": "M2B-O075"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P028::M2A-P028-E002'
    AND et.evidence_type_name = 'NT-3 collagen hydrogel'
    AND ot.outcome_type_name = 'BBB locomotion, neuronal growth, glial scar formation, inflammation, and collagen deposition were assessed.'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O075', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Slotkin JR 2017 M2A-P029-E002 preserves a distinct Chlorocebus sabaeus experiment testing Porous biodegradable scaffold with endpoint/readout: Locomotor kinematics, muscle activity, appositional healing, and spinal cord tissue remodeling were compared..',
    'qualitative',
    'Slotkin JR 2017 M2A-P029-E002 preserves a distinct Chlorocebus sabaeus experiment testing Porous biodegradable scaffold with endpoint/readout: Locomotor kinematics, muscle activity, appositional healing, and spinal cord tissue remodeling were compared..',
    'M2A-P029-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Biodegradable scaffolds promote tissue remodeling and functional improvement in non-human primates with acute spinal cord injury. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M2A-P029-E002", "paper_tracker_id": "M2A-P029", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M2B-T006", "tracker_id": "M2B-O076"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P029::M2A-P029-E002'
    AND et.evidence_type_name = 'Non-human primate intervention'
    AND ot.outcome_type_name = 'Locomotor kinematics, muscle activity, appositional healing, and spinal cord tissue remodeling were compared.'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O076', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Li G 2018 M2A-P030-E002: 14 female Beagles underwent right T10 4 mm hemisection; n=7/group. At 4 weeks NF-GS improved Olby (11.85 +/- 0.64 vs 9.29 +/- 1.48), produced stronger/shorter-latency CMEP, reduced IBA1+ cells at graft (74.11 +/- 5.85 vs 98.41 +/- 15.43 cells/0.09 mm2), and increased NF+ fiber density; GFAP scar density remained similar.',
    'quantitative',
    'Li G 2018 M2A-P030-E002: 14 female Beagles underwent right T10 4 mm hemisection; n=7/group. At 4 weeks NF-GS improved Olby (11.85 +/- 0.64 vs 9.29 +/- 1.48), produced stronger/shorter-latency CMEP, reduced IBA1+ cells at graft (74.11 +/- 5.85 vs 98.41 +/- 15.43 cells/0.09 mm2), and increased NF+ fiber density; GFAP scar density remained similar.',
    'M2A-P030-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'PMC6055812',
    'Full text',
    'high',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; no independent consensus link added.", "experiment_tracker_id": "M2A-P030-E002", "paper_tracker_id": "M2A-P030", "quantitative": "NO", "statistics_reported": "Full-text duplicate/backfill now reconciled to exact values", "topic_id": "M2B-T003", "tracker_id": "M2B-O077"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P030::M2A-P030-E002'
    AND et.evidence_type_name = 'NT-3/fibroin gelatin scaffold'
    AND ot.outcome_type_name = 'Canine locomotion, conduction, immune burden, and tissue regeneration'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O077', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Zhang S 2018 M2A-P031-E002 preserves a distinct Rattus norvegicus experiment testing PCL/PSA/MP nanofiber scaffold with endpoint/readout: Inflammation, microglia/macrophage activation, apoptosis, axonal regeneration, and functional recovery were assessed after transplantation into transection lesions..',
    'qualitative',
    'Zhang S 2018 M2A-P031-E002 preserves a distinct Rattus norvegicus experiment testing PCL/PSA/MP nanofiber scaffold with endpoint/readout: Inflammation, microglia/macrophage activation, apoptosis, axonal regeneration, and functional recovery were assessed after transplantation into transection lesions..',
    'M2A-P031-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Polycaprolactone/polysialic acid hybrid, multifunctional nanofiber scaffolds for treatment of spinal cord injury. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M2A-P031-E002", "paper_tracker_id": "M2A-P031", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M2B-T003", "tracker_id": "M2B-O078"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P031::M2A-P031-E002'
    AND et.evidence_type_name = 'PCL/PSA/MP nanofiber scaffold'
    AND ot.outcome_type_name = 'Inflammation, microglia/macrophage activation, apoptosis, axonal regeneration, and functional recovery were assessed after transplantation into transection lesions.'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O078', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Thompson RE 2018 M2A-P032-E002: P-ECM:HA reduced GFAP area around lesion (9.7 +/- 1.1% vs sham 16 +/- 3.3%), ED1 around lesion (5.5 +/- 0.97% vs sham 9.7 +/- 1.6%), and increased Tuj1 area in lesion (14 +/- 1.0% vs sham 9.2 +/- 1.9%); V2a-cell groups showed persistence and increased neuronal-process staining, without a locomotor/integration endpoint.',
    'quantitative',
    'Thompson RE 2018 M2A-P032-E002: P-ECM:HA reduced GFAP area around lesion (9.7 +/- 1.1% vs sham 16 +/- 3.3%), ED1 around lesion (5.5 +/- 0.97% vs sham 9.7 +/- 1.6%), and increased Tuj1 area in lesion (14 +/- 1.0% vs sham 9.2 +/- 1.9%); V2a-cell groups showed persistence and increased neuronal-process staining, without a locomotor/integration endpoint.',
    'M2A-P032-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'PMC5851469',
    'Full text',
    'high',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; fibrous ECM was not equivalent to protoplasmic ECM.", "experiment_tracker_id": "M2A-P032-E002", "paper_tracker_id": "M2A-P032", "quantitative": "NO", "statistics_reported": "Full-text duplicate/backfill now reconciled to exact values", "topic_id": "M2B-T004", "tracker_id": "M2B-O079"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P032::M2A-P032-E002'
    AND et.evidence_type_name = 'HA hydrogel plus astrocyte ECM'
    AND ot.outcome_type_name = 'Scar, immune response, and neuronal processes'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O079', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'In 20 treatment versus 20 no-implant controls followed 12 months, 9 treatment patients improved ASIA A-to-B and 2 A-to-C while no controls improved ASIA grade; treatment also improved MEP/SSEP in subsets, reduced residual urine, and showed MRI/DTI fiber continuity without serious treatment-associated adverse events.',
    'ASIA; MEP/SSEP; residual urine; DTI',
    'In 20 treatment versus 20 no-implant controls followed 12 months, 9 treatment patients improved ASIA A-to-B and 2 A-to-C while no controls improved ASIA grade; treatment also improved MEP/SSEP in subsets, reduced residual urine, and showed MRI/DTI fiber continuity without serious treatment-associated adverse events.',
    'M2A-P033-E002 preserves a controlled clinical boundary with stronger extraction than the earlier abstract row',
    'Full text Tables 1-4 and Figs. 6-8',
    'Tables 1-4; Figs. 6-8',
    'high',
    '{"curator_notes": "Phase I, non-randomized/limited sample; mild adverse events occurred and causality is uncertain.", "experiment_tracker_id": "M2A-P033-E002", "paper_tracker_id": "M2A-P033", "quantitative": "YES", "statistics_reported": "Forty acute complete cervical SCI patients; treatment n=20, control n=20", "topic_id": "M2B-T006", "tracker_id": "M2B-O080"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P033::M2A-P033-E002'
    AND et.evidence_type_name = 'Animal-to-clinical translation'
    AND ot.outcome_type_name = 'Phase I clinical testing evaluated safety, neurological recovery, electrophysiology, and imaging after collagen scaffold plus hUC-MSC transplantation.'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O080', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Elkhenany H 2021 M2A-P034-E002: n=3/group female SD rats received one-week post-injury T8 contusion surface caps; fully functionalized HA/PPY/PM-CURC-iNPC preserved beta-III-tubulin fibers and reduced GFAP-negative area/PDGF, but Iba1/ED1 inflammation was unchanged and iNPCs mainly showed astroglial identity.',
    'quantitative direction',
    'Elkhenany H 2021 M2A-P034-E002: n=3/group female SD rats received one-week post-injury T8 contusion surface caps; fully functionalized HA/PPY/PM-CURC-iNPC preserved beta-III-tubulin fibers and reduced GFAP-negative area/PDGF, but Iba1/ED1 inflammation was unchanged and iNPCs mainly showed astroglial identity.',
    'M2A-P034-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'PMC8698735',
    'Full text',
    'high',
    '{"curator_notes": "Per-experiment atomization backfill; early endpoint and bundled intervention retained.", "experiment_tracker_id": "M2A-P034-E002", "paper_tracker_id": "M2A-P034", "quantitative": "NO", "statistics_reported": "Full-text duplicate/backfill now reconciled", "topic_id": "M2B-T007", "tracker_id": "M2B-O081"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P034::M2A-P034-E002'
    AND et.evidence_type_name = 'Conductive surface scaffold'
    AND ot.outcome_type_name = 'Early surface-cap repair and inflammation boundary'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O081', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Qiu C 2022 M2A-P035-E002: acute T10 full transection with 2 mm segment removed; at 8 weeks cell-loaded scaffold BBB was 5.667 versus 2.333 empty scaffold and 0.667 transection control, with MEP amplitude 29.57% of normal and robust NF-H projection along channels.',
    'quantitative',
    'Qiu C 2022 M2A-P035-E002: acute T10 full transection with 2 mm segment removed; at 8 weeks cell-loaded scaffold BBB was 5.667 versus 2.333 empty scaffold and 0.667 transection control, with MEP amplitude 29.57% of normal and robust NF-H projection along channels.',
    'M2A-P035-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'PMC9598945',
    'Full text',
    'high',
    '{"curator_notes": "Per-experiment atomization backfill; key BBB analyses n=3 because of postoperative deaths.", "experiment_tracker_id": "M2A-P035-E002", "paper_tracker_id": "M2A-P035", "quantitative": "NO", "statistics_reported": "Full-text duplicate/backfill now reconciled to exact values", "topic_id": "M2B-T001", "tracker_id": "M2B-O082"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P035::M2A-P035-E002'
    AND et.evidence_type_name = '3D-printed GelMA microchannel scaffold'
    AND ot.outcome_type_name = 'Rat full-transection locomotion and conduction'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O082', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Zhang R 2024 M2A-P036-E002: mice received sham, SCI, SilMA, or 4D-SilMA after 2 mm T10 complete transection (n=6/group). At 8 weeks 4D-SilMA reached BMS 6, increased Arg-1 and Tuj1, reduced iNOS and GFAP, and produced fewer cavities/inflammatory cells; in-vitro LPS/BV2 and NSC assays supported separate Ang-(1-7) and NT-3 effects.',
    'quantitative',
    'Zhang R 2024 M2A-P036-E002: mice received sham, SCI, SilMA, or 4D-SilMA after 2 mm T10 complete transection (n=6/group). At 8 weeks 4D-SilMA reached BMS 6, increased Arg-1 and Tuj1, reduced iNOS and GFAP, and produced fewer cavities/inflammatory cells; in-vitro LPS/BV2 and NSC assays supported separate Ang-(1-7) and NT-3 effects.',
    'M2A-P036-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'PMC11617199',
    'Full text',
    'high',
    '{"curator_notes": "In-vivo combined treatment does not isolate each cargo; release was measured in PBS.", "experiment_tracker_id": "M2A-P036-E002", "paper_tracker_id": "M2A-P036", "quantitative": "NO", "statistics_reported": "Full-text duplicate/backfill now reconciled to exact values", "topic_id": "M2B-T003", "tracker_id": "M2B-O083"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P036::M2A-P036-E002'
    AND et.evidence_type_name = 'Sequential-release SilMA scaffold'
    AND ot.outcome_type_name = 'In-vivo immunomodulation, neural differentiation, tissue repair, and locomotion'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O083', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Li Y 2023 M2A-P037-E002 preserves a distinct Rodent model context experiment testing On-demand hierarchical hydrogel scaffold with endpoint/readout: SCI testing evaluated oxidative stress control, endogenous NSC migration/differentiation, and repair..',
    'qualitative',
    'Li Y 2023 M2A-P037-E002 preserves a distinct Rodent model context experiment testing On-demand hierarchical hydrogel scaffold with endpoint/readout: SCI testing evaluated oxidative stress control, endogenous NSC migration/differentiation, and repair..',
    'M2A-P037-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Coaxial 3D printing of hierarchical structured hydrogel scaffolds for on-demand repair of spinal cord injury. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M2A-P037-E002", "paper_tracker_id": "M2A-P037", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M2B-T001", "tracker_id": "M2B-O084"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P037::M2A-P037-E002'
    AND et.evidence_type_name = 'Coaxial 3D-printed hierarchical hydrogel'
    AND ot.outcome_type_name = 'SCI testing evaluated oxidative stress control, endogenous NSC migration/differentiation, and repair.'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O084', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Zhu B 2023 M2A-P038-E002 preserves a distinct Rattus norvegicus experiment testing Exosome/steroid nanofiber hydrogel patch with endpoint/readout: Patch covering the hematoma surface was assessed for functional, electrophysiological, inflammatory, and neuronal survival outcomes..',
    'qualitative',
    'Zhu B 2023 M2A-P038-E002 preserves a distinct Rattus norvegicus experiment testing Exosome/steroid nanofiber hydrogel patch with endpoint/readout: Patch covering the hematoma surface was assessed for functional, electrophysiological, inflammatory, and neuronal survival outcomes..',
    'M2A-P038-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Schwann Cell-Derived Exosomes and Methylprednisolone Composite Patch for Spinal Cord Injury Repair. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M2A-P038-E002", "paper_tracker_id": "M2A-P038", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M2B-T007", "tracker_id": "M2B-O085"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P038::M2A-P038-E002'
    AND et.evidence_type_name = 'Nanofiber/HA hydrogel patch'
    AND ot.outcome_type_name = 'Patch covering the hematoma surface was assessed for functional, electrophysiological, inflammatory, and neuronal survival outcomes.'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O085', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Yao S 2024 M2A-P039-E002: T9 4 mm complete transection rats received GelMA, 2CNT/GelMA, or 2CNT/GelMA+ES; at 8 weeks the combined group had tissue conductivity 1.50 x 10^-3 S/cm versus normal 2.13 x 10^-3, abundant NF/beta-tubulin III fibers, high remyelination, lower Iba1/CS56, and strongest BBB/MEP/pain recovery.',
    'quantitative direction',
    'Yao S 2024 M2A-P039-E002: T9 4 mm complete transection rats received GelMA, 2CNT/GelMA, or 2CNT/GelMA+ES; at 8 weeks the combined group had tissue conductivity 1.50 x 10^-3 S/cm versus normal 2.13 x 10^-3, abundant NF/beta-tubulin III fibers, high remyelination, lower Iba1/CS56, and strongest BBB/MEP/pain recovery.',
    'M2A-P039-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'PMC10897856',
    'Full text',
    'high',
    '{"curator_notes": "Per-experiment atomization backfill; scaffold and ES effects remain bundled.", "experiment_tracker_id": "M2A-P039-E002", "paper_tracker_id": "M2A-P039", "quantitative": "NO", "statistics_reported": "Full-text duplicate/backfill now reconciled", "topic_id": "M2B-T001", "tracker_id": "M2B-O086"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P039::M2A-P039-E002'
    AND et.evidence_type_name = 'Conductive aligned hydrogel / electrical stimulation'
    AND ot.outcome_type_name = 'Rat conduction, axon, remyelination, and function'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O086', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Mehrotra S 2010 M2A-P040-E002: pH-triggered PEG/PAA/protein LbL films over agarose released active model protein for more than four weeks in vitro; no SCI animal was tested.',
    'quantitative direction',
    'Mehrotra S 2010 M2A-P040-E002: pH-triggered PEG/PAA/protein LbL films over agarose released active model protein for more than four weeks in vitro; no SCI animal was tested.',
    'M2A-P040-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'PMC2830720',
    'Full text',
    'high',
    '{"curator_notes": "Per-experiment atomization backfill; methods-only evidence.", "experiment_tracker_id": "M2A-P040-E002", "paper_tracker_id": "M2A-P040", "quantitative": "NO", "statistics_reported": "Full-text duplicate/backfill now reconciled", "topic_id": "M2B-T003", "tracker_id": "M2B-O087"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P040::M2A-P040-E002'
    AND et.evidence_type_name = 'Functionalized agarose hydrogel'
    AND ot.outcome_type_name = 'Protein-release agarose strategy'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O087', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Lai BQ 2014 M2A-P041-E002: after T10 2 mm complete transection, NT-3-SCs+TrkC-NSCs in gelatin sponge survived to 8 weeks and MBP+ myelin ensheathed GFP-positive graft-derived and host NF+ axons; dual-engineered in-vitro cultures showed APC+ oligodendrocytic differentiation 12.98 +/- 5.33%.',
    'quantitative',
    'Lai BQ 2014 M2A-P041-E002: after T10 2 mm complete transection, NT-3-SCs+TrkC-NSCs in gelatin sponge survived to 8 weeks and MBP+ myelin ensheathed GFP-positive graft-derived and host NF+ axons; dual-engineered in-vitro cultures showed APC+ oligodendrocytic differentiation 12.98 +/- 5.33%.',
    'M2A-P041-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'PMC3992004',
    'Full text',
    'high',
    '{"curator_notes": "Per-experiment atomization backfill; no primary locomotor efficacy endpoint.", "experiment_tracker_id": "M2A-P041-E002", "paper_tracker_id": "M2A-P041", "quantitative": "NO", "statistics_reported": "Full-text duplicate/backfill now reconciled", "topic_id": "M2B-T002", "tracker_id": "M2B-O088"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P041::M2A-P041-E002'
    AND et.evidence_type_name = 'Gelatin scaffold plus engineered cells'
    AND ot.outcome_type_name = 'Myelination and graft-cell survival'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O088', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Sun Y 2020 M2A-P042-E002: in rats (n=10/group), 3D-CF plus NSCs increased NF-H and reduced GFAP relative to SCI and scaffold-only groups and improved reported limb function; NSC tracing and objective neurological assessment were not completed.',
    'quantitative direction',
    'Sun Y 2020 M2A-P042-E002: in rats (n=10/group), 3D-CF plus NSCs increased NF-H and reduced GFAP relative to SCI and scaffold-only groups and improved reported limb function; NSC tracing and objective neurological assessment were not completed.',
    'M2A-P042-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'PMC6990792',
    'Full text',
    'high',
    '{"curator_notes": "Per-experiment atomization backfill; architecture and NSC effects remain bundled.", "experiment_tracker_id": "M2A-P042-E002", "paper_tracker_id": "M2A-P042", "quantitative": "NO", "statistics_reported": "Full-text duplicate/backfill now reconciled", "topic_id": "M2B-T001", "tracker_id": "M2B-O089"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P042::M2A-P042-E002'
    AND et.evidence_type_name = '3D-bioprinted collagen/silk scaffold'
    AND ot.outcome_type_name = 'Nerve regeneration and scar response'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O089', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Führmann T 2016 M2A-P043-E002: NF+ axons followed OEC and host-cell trajectories but only trended above non-seeded/untreated lesions; seeded and non-seeded scaffolds both improved skilled forelimb function, and function was not correlated with scaffold axon extent.',
    'qualitative',
    'Führmann T 2016 M2A-P043-E002: NF+ axons followed OEC and host-cell trajectories but only trended above non-seeded/untreated lesions; seeded and non-seeded scaffolds both improved skilled forelimb function, and function was not correlated with scaffold axon extent.',
    'M2A-P043-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'PMC6170848',
    'Full text',
    'high',
    '{"curator_notes": "Per-experiment atomization backfill; direct negative-mechanism boundary.", "experiment_tracker_id": "M2A-P043-E002", "paper_tracker_id": "M2A-P043", "quantitative": "NO", "statistics_reported": "Full-text duplicate/backfill now reconciled", "topic_id": "M2B-T008", "tracker_id": "M2B-O090"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P043::M2A-P043-E002'
    AND et.evidence_type_name = 'OEC-seeded scaffold'
    AND ot.outcome_type_name = 'Functional recovery versus scaffold axon regeneration'
  RETURNING observation_id
)
INSERT INTO _m2_observation_map (tracker_id, observation_id) SELECT 'M2B-O090', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Electrophysiology-guided chronic scar resection followed by NeuroRegen scaffold plus autologous BMMC implantation is feasible in a very small complete chronic human SCI cohort.',
    'conclusion',
    'medium',
    'Abstract / source page',
    'medium',
    '{"curator_notes": "Feasibility only; efficacy remains unproven.", "source_paper_tracker_id": "M2A-P001", "topic_id": "M2B-T006", "tracker_id": "M2B-C001"}'
  FROM _m2_paper_map p
  WHERE p.tracker_id = 'M2A-P001'
  RETURNING claim_id
)
INSERT INTO _m2_claim_map (tracker_id, claim_id) SELECT 'M2B-C001', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'NeuroRegen scaffold plus hUCB-MSC implantation after scar resection was safe in this small chronic complete human cohort and was associated with partial sensory/electrophysiological gains, but not ASIA grade improvement.',
    'conclusion / boundary condition',
    'high',
    'Full text Figs. 1-2 and Tables 1-2',
    'high',
    '{"curator_notes": "Uncontrolled cohort with concurrent rehabilitation; no causal efficacy claim.", "source_paper_tracker_id": "M2A-P009", "topic_id": "M2B-T006", "tracker_id": "M2B-C002"}'
  FROM _m2_paper_map p
  WHERE p.tracker_id = 'M2A-P009'
  RETURNING claim_id
)
INSERT INTO _m2_claim_map (tracker_id, claim_id) SELECT 'M2B-C002', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Porous biodegradable scaffolds can promote tissue remodeling and functional improvement in non-human primate acute SCI.',
    'conclusion',
    'medium',
    'Abstract',
    'medium',
    '{"curator_notes": "Strong translational species, abstract-level extraction.", "source_paper_tracker_id": "M2A-P029", "topic_id": "M2B-T006", "tracker_id": "M2B-C003"}'
  FROM _m2_paper_map p
  WHERE p.tracker_id = 'M2A-P029'
  RETURNING claim_id
)
INSERT INTO _m2_claim_map (tracker_id, claim_id) SELECT 'M2B-C003', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Aligned PEG hydrogel tubes provide modular physical guidance, transiently limit scar formation, support axon growth and partial myelination, and improve locomotion in a mouse lateral-hemisection model; tube-specific superiority over a PEG bridge was not established.',
    'conclusion',
    'high',
    'Full text Figs. 2-7',
    'high',
    '{"curator_notes": "Scaffold-only gelfoam comparator and tube-versus-bridge boundary are now explicit.", "source_paper_tracker_id": "M2A-P005", "topic_id": "M2B-T001", "tracker_id": "M2B-C004"}'
  FROM _m2_paper_map p
  WHERE p.tracker_id = 'M2A-P005'
  RETURNING claim_id
)
INSERT INTO _m2_claim_map (tracker_id, claim_id) SELECT 'M2B-C004', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Conductive aligned GelMA/CNT hydrogel fibers can combine regenerative scaffold guidance with electrical stimulation: in T9 transection rats the combined treatment improved inflammatory markers, axon density/remyelination, tissue conductivity, BBB, pain response, and MEP, but scaffold and stimulation contributions remain bundled.',
    'conclusion / implication',
    'high',
    'Full text Figs. 7-9',
    'high',
    '{"curator_notes": "ES protocol was 2 V for 1 h at 1, 4, and 7 days in vitro; in-vivo functional effects were measured at 8 weeks.", "source_paper_tracker_id": "M2A-P039", "topic_id": "M2B-T001", "tracker_id": "M2B-C005"}'
  FROM _m2_paper_map p
  WHERE p.tracker_id = 'M2A-P039'
  RETURNING claim_id
)
INSERT INTO _m2_claim_map (tracker_id, claim_id) SELECT 'M2B-C005', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Cell-seeded PLGA scaffolds can outperform scaffold-only controls after complete transection SCI.',
    'conclusion',
    'medium',
    'Abstract',
    'medium',
    '{"curator_notes": "One of the clearer scaffold-only comparator claims.", "source_paper_tracker_id": "M2A-P012", "topic_id": "M2B-T002", "tracker_id": "M2B-C006"}'
  FROM _m2_paper_map p
  WHERE p.tracker_id = 'M2A-P012'
  RETURNING claim_id
)
INSERT INTO _m2_claim_map (tracker_id, claim_id) SELECT 'M2B-C006', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Injectable decellularized peripheral nerve matrix is a clinically oriented Schwann-cell carrier that improves graft survival and myelinated-axon counts relative to Matrigel, without durable BBB superiority.',
    'implication / boundary condition',
    'high',
    'Full text Figs. 3-8',
    'high',
    '{"curator_notes": "Histology benefit is stronger than locomotor superiority; iPN did not aggravate early immune infiltration.", "source_paper_tracker_id": "M2A-P016", "topic_id": "M2B-T002", "tracker_id": "M2B-C007"}'
  FROM _m2_paper_map p
  WHERE p.tracker_id = 'M2A-P016'
  RETURNING claim_id
)
INSERT INTO _m2_claim_map (tracker_id, claim_id) SELECT 'M2B-C007', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Scaffold-delivered NT-3 can improve early axonal sprouting and reduce white-matter-border astroglial scar without improving motor function at 12 weeks in this ablation model.',
    'boundary condition',
    'high',
    'Full text Figs. 1-7',
    'high',
    '{"curator_notes": "Important histology-function dissociation; no treatment difference in macrophage/microglia density.", "source_paper_tracker_id": "M2A-P025", "topic_id": "M2B-T003", "tracker_id": "M2B-C008"}'
  FROM _m2_paper_map p
  WHERE p.tracker_id = 'M2A-P025'
  RETURNING claim_id
)
INSERT INTO _m2_claim_map (tracker_id, claim_id) SELECT 'M2B-C008', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Sequential release scaffolds can align an early anti-inflammatory cue with a later neurogenic cue: Ang-(1-7) was released rapidly (>40% by day 3; nearly complete by day 7), whereas NT-3 release persisted through days 28-56, and the combined scaffold improved inflammation, neuronal markers, tissue structure, and BMS after mouse complete transection.',
    'mechanistic / conclusion',
    'high',
    'Full text, release assay and Figs. 3-6',
    'high',
    '{"curator_notes": "Timing is supported in vitro; combined in-vivo cargo attribution remains unresolved.", "source_paper_tracker_id": "M2A-P036", "topic_id": "M2B-T003", "tracker_id": "M2B-C009"}'
  FROM _m2_paper_map p
  WHERE p.tracker_id = 'M2A-P036'
  RETURNING claim_id
)
INSERT INTO _m2_claim_map (tracker_id, claim_id) SELECT 'M2B-C009', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Injectable ECM-derived hydrogels can integrate into acute hemisection lesions and support axon and vessel ingrowth, but rapid degradation, cyst formation, macrophage infiltration, and poor cell survival constrain durable repair; spinal-cord and urinary-bladder ECM performed similarly.',
    'boundary condition',
    'high',
    'Full text Figs. 2-7',
    'high',
    '{"curator_notes": "Avoids treating ECM source as uniformly pro-regenerative or interchangeable with durable bridges.", "source_paper_tracker_id": "M2A-P014", "topic_id": "M2B-T004", "tracker_id": "M2B-C010"}'
  FROM _m2_paper_map p
  WHERE p.tracker_id = 'M2A-P014'
  RETURNING claim_id
)
INSERT INTO _m2_claim_map (tracker_id, claim_id) SELECT 'M2B-C010', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Chronic scar removal followed by anisotropic alginate hydrogel implantation can support conduction, tract growth, and locomotor recovery in chronic complete transection SCI.',
    'conclusion',
    'medium',
    'Abstract',
    'medium',
    '{"curator_notes": "Strong chronic repair signal, but abstract-level.", "source_paper_tracker_id": "M2A-P006", "topic_id": "M2B-T005", "tracker_id": "M2B-C011"}'
  FROM _m2_paper_map p
  WHERE p.tracker_id = 'M2A-P006'
  RETURNING claim_id
)
INSERT INTO _m2_claim_map (tracker_id, claim_id) SELECT 'M2B-C011', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'In a controlled chronic canine transection model, scar removal plus NeuroRegen/hUC-MSC implantation improved locomotor score and lesion-site neurogenesis, remyelination, synapse signal, and secondary CSPG burden relative to controls, but the intervention is multi-component.',
    'conclusion / implication',
    'high',
    'Full text Figs. 1-7',
    'high',
    '{"curator_notes": "n=6/group; human MSC persistence was not demonstrated; rehabilitation and scar removal remain confounders.", "source_paper_tracker_id": "M2A-P015", "topic_id": "M2B-T005", "tracker_id": "M2B-C012"}'
  FROM _m2_paper_map p
  WHERE p.tracker_id = 'M2A-P015'
  RETURNING claim_id
)
INSERT INTO _m2_claim_map (tracker_id, claim_id) SELECT 'M2B-C012', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Surface-applied HA demilune caps can combine conductive fibers, hydrogel cell support, and curcumin to preserve early neuronal fibers and reduce fibrotic/scar-associated signals after subacute contusion, but the one-week n=3 study did not reduce Iba1/ED1 inflammation or establish function.',
    'implication / boundary condition',
    'high',
    'Full text Figs. 5-9',
    'high',
    '{"curator_notes": "Distinct intervention geometry; early endpoint and bundled components limit efficacy attribution.", "source_paper_tracker_id": "M2A-P034", "topic_id": "M2B-T007", "tracker_id": "M2B-C013"}'
  FROM _m2_paper_map p
  WHERE p.tracker_id = 'M2A-P034'
  RETURNING claim_id
)
INSERT INTO _m2_claim_map (tracker_id, claim_id) SELECT 'M2B-C013', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Functional improvement after scaffold/cell treatment should not be assumed to reflect axons regenerating through the scaffold: seeded and non-seeded longitudinal collagen scaffolds both improved skilled forelimb function despite only a trend in axon counts and no correlation between function and scaffold axon extent.',
    'boundary condition',
    'high',
    'Full text source Results',
    'high',
    '{"curator_notes": "Direct mechanistic boundary from the acute cervical OEC-seeded scaffold experiment.", "source_paper_tracker_id": "M2A-P043", "topic_id": "M2B-T008", "tracker_id": "M2B-C014"}'
  FROM _m2_paper_map p
  WHERE p.tracker_id = 'M2A-P043'
  RETURNING claim_id
)
INSERT INTO _m2_claim_map (tracker_id, claim_id) SELECT 'M2B-C014', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Acute complete human NeuroRegen scaffold plus MSC implantation was feasible in two strictly diagnosed patients and coincided with ASIA A-to-C, sensory/motor, and SSEP/MEP recovery, but n = 2 and the uncontrolled design preclude efficacy attribution.',
    'boundary condition',
    'high',
    'Full text Figs. 1-5',
    'high',
    '{"curator_notes": "Keeps the acute clinical signal appropriately constrained.", "source_paper_tracker_id": "M2A-P017", "topic_id": "M2B-T006", "tracker_id": "M2B-C015"}'
  FROM _m2_paper_map p
  WHERE p.tracker_id = 'M2A-P017'
  RETURNING claim_id
)
INSERT INTO _m2_claim_map (tracker_id, claim_id) SELECT 'M2B-C015', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Collagen scaffold plus hUC-MSC repair shows a continuous preclinical-to-clinical signal across rat, canine, and acute complete human contexts, including control-separated clinical neurological gains, but remains a bundled multi-component strategy.',
    'implication / translational boundary',
    'high',
    'Full text Figs. 1-8 and Tables 1-4',
    'high',
    '{"curator_notes": "Strong translational path, weaker as isolated scaffold or cell efficacy proof.", "source_paper_tracker_id": "M2A-P033", "topic_id": "M2B-T006", "tracker_id": "M2B-C016"}'
  FROM _m2_paper_map p
  WHERE p.tracker_id = 'M2A-P033'
  RETURNING claim_id
)
INSERT INTO _m2_claim_map (tracker_id, claim_id) SELECT 'M2B-C016', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Biomimetic 3D-printed PEGDA-GelMA scaffolds can impose lesion-scale architecture that supports host-graft axonal relay formation and functional recovery when loaded with NPCs; empty scaffolds support host axon entry but not distal host-axon extension or MEP recovery.',
    'conclusion',
    'high',
    'Full text Figs. 1-4',
    'high',
    '{"curator_notes": "NPC and scaffold contributions are separated by empty-scaffold, NPC-only, and retransection controls.", "source_paper_tracker_id": "M2A-P004", "topic_id": "M2B-T001", "tracker_id": "M2B-C017"}'
  FROM _m2_paper_map p
  WHERE p.tracker_id = 'M2A-P004'
  RETURNING claim_id
)
INSERT INTO _m2_claim_map (tracker_id, claim_id) SELECT 'M2B-C017', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Multi-channel scaffold architecture is a reusable experimental platform for separating geometry, cell, and molecule effects.',
    'implication',
    'medium',
    'Abstract',
    'medium',
    '{"curator_notes": "Platform claim rather than outcome claim.", "source_paper_tracker_id": "M2A-P010", "topic_id": "M2B-T001", "tracker_id": "M2B-C018"}'
  FROM _m2_paper_map p
  WHERE p.tracker_id = 'M2A-P010'
  RETURNING claim_id
)
INSERT INTO _m2_claim_map (tracker_id, claim_id) SELECT 'M2B-C018', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Injectable scaffolds can be given tunable alignment after delivery, expanding guidance strategies beyond prefabricated implants.',
    'implication',
    'medium',
    'Abstract',
    'medium',
    '{"curator_notes": "Based on magnetic peptide hydrogel design.", "source_paper_tracker_id": "M2A-P021", "topic_id": "M2B-T001", "tracker_id": "M2B-C019"}'
  FROM _m2_paper_map p
  WHERE p.tracker_id = 'M2A-P021'
  RETURNING claim_id
)
INSERT INTO _m2_claim_map (tracker_id, claim_id) SELECT 'M2B-C019', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Microchannel GelMA scaffolds can pair geometry with hAEC-derived neural-like cell placement to support partial repair after complete transection, with 8-week BBB 5.667 versus 2.333 for empty scaffold and 0.667 for transection control and MEP 29.57% of normal.',
    'conclusion / boundary condition',
    'high',
    'Full text Figs. 5-6',
    'high',
    '{"curator_notes": "Architecture and cell effects remain bundled; BBB analyses were small and mortality-limited, and cells were not shown to be mature neurons.", "source_paper_tracker_id": "M2A-P035", "topic_id": "M2B-T001", "tracker_id": "M2B-C020"}'
  FROM _m2_paper_map p
  WHERE p.tracker_id = 'M2A-P035'
  RETURNING claim_id
)
INSERT INTO _m2_claim_map (tracker_id, claim_id) SELECT 'M2B-C020', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Chronic rat scar resection plus collagen/hUC-MSC scaffold repair improves enough outcome domains to justify chronic scaffold/cell testing.',
    'conclusion',
    'low',
    'Abstract',
    'medium',
    '{"curator_notes": "Full-text unavailable, so claim is cautious.", "source_paper_tracker_id": "M2A-P002", "topic_id": "M2B-T002", "tracker_id": "M2B-C021"}'
  FROM _m2_paper_map p
  WHERE p.tracker_id = 'M2A-P002'
  RETURNING claim_id
)
INSERT INTO _m2_claim_map (tracker_id, claim_id) SELECT 'M2B-C021', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'dECM scaffold plus hNS/PC transplantation can improve chronic lesion histology even when functional recovery remains absent.',
    'boundary condition',
    'high',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Useful histology-function boundary in chronic complete SCI.", "source_paper_tracker_id": "M2A-P003", "topic_id": "M2B-T002", "tracker_id": "M2B-C022"}'
  FROM _m2_paper_map p
  WHERE p.tracker_id = 'M2A-P003'
  RETURNING claim_id
)
INSERT INTO _m2_claim_map (tracker_id, claim_id) SELECT 'M2B-C022', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Chitosan bridges with immobilized factors are best interpreted as combined scaffold-cell-cue systems rather than scaffold-only interventions.',
    'boundary condition',
    'high',
    'Abstract',
    'medium',
    '{"curator_notes": "Directly designed as combination therapy.", "source_paper_tracker_id": "M2A-P013", "topic_id": "M2B-T002", "tracker_id": "M2B-C023"}'
  FROM _m2_paper_map p
  WHERE p.tracker_id = 'M2A-P013'
  RETURNING claim_id
)
INSERT INTO _m2_claim_map (tracker_id, claim_id) SELECT 'M2B-C023', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Spinal cord-derived dECM/GelMA scaffolds are used to recreate a lesion-local matrix niche for stem-cell survival and repair.',
    'mechanistic',
    'medium',
    'Abstract',
    'medium',
    '{"curator_notes": "Matrix-niche claim; effect attribution remains bundled.", "source_paper_tracker_id": "M2A-P020", "topic_id": "M2B-T002", "tracker_id": "M2B-C024"}'
  FROM _m2_paper_map p
  WHERE p.tracker_id = 'M2A-P020'
  RETURNING claim_id
)
INSERT INTO _m2_claim_map (tracker_id, claim_id) SELECT 'M2B-C024', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Collagen scaffold tethering can convert exosome delivery from diffuse bolus logic into a local sustained-release strategy.',
    'mechanistic',
    'medium',
    'Abstract',
    'medium',
    '{"curator_notes": "Based on collagen-binding exosome design.", "source_paper_tracker_id": "M2A-P007", "topic_id": "M2B-T003", "tracker_id": "M2B-C025"}'
  FROM _m2_paper_map p
  WHERE p.tracker_id = 'M2A-P007'
  RETURNING claim_id
)
INSERT INTO _m2_claim_map (tracker_id, claim_id) SELECT 'M2B-C025', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Delayed bFGF/HEMA-MOETACL implantation can reduce cavitation, support axon and vessel ingrowth, and improve SSEP/MEP recovery after complete transection, while hydrogel-only effects show that material and trophic contributions are partly separable but not fully independent.',
    'conclusion / boundary condition',
    'high',
    'Full text Figs. 1-7',
    'high',
    '{"curator_notes": "Combined group had the strongest axon, vessel, and electrophysiology outcomes; hydrogel alone reduced cavitation without clear behavioral recovery.", "source_paper_tracker_id": "M2A-P026", "topic_id": "M2B-T003", "tracker_id": "M2B-C026"}'
  FROM _m2_paper_map p
  WHERE p.tracker_id = 'M2A-P026'
  RETURNING claim_id
)
INSERT INTO _m2_claim_map (tracker_id, claim_id) SELECT 'M2B-C026', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Drug-loaded nanofiber scaffolds can combine physical support with anti-inflammatory treatment after SCI.',
    'conclusion',
    'medium',
    'Abstract',
    'medium',
    '{"curator_notes": "Methylprednisolone/PCL/PSA anchor.", "source_paper_tracker_id": "M2A-P031", "topic_id": "M2B-T003", "tracker_id": "M2B-C027"}'
  FROM _m2_paper_map p
  WHERE p.tracker_id = 'M2A-P031'
  RETURNING claim_id
)
INSERT INTO _m2_claim_map (tracker_id, claim_id) SELECT 'M2B-C027', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Layer-by-layer PEG/PAA/protein films over agarose can provide active, pH-triggered protein release for more than four weeks in vitro, supporting a non-cell-based trophic-delivery method for future channel bridges but not proving SCI efficacy.',
    'implication / methods boundary',
    'high',
    'Full text release experiments',
    'high',
    '{"curator_notes": "Lysozyme model protein; BDNF was proposed for subsequent scaffold testing.", "source_paper_tracker_id": "M2A-P040", "topic_id": "M2B-T003", "tracker_id": "M2B-C028"}'
  FROM _m2_paper_map p
  WHERE p.tracker_id = 'M2A-P040'
  RETURNING claim_id
)
INSERT INTO _m2_claim_map (tracker_id, claim_id) SELECT 'M2B-C028', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'HA hydrogel permissiveness is conditional on astrocyte-ECM identity: protoplasmic ECM reduced GFAP, ED1, and CSPG burden and increased Tuj1 penetration, whereas fibrous ECM did not reproduce the benefit and could negate HA-associated CSPG reduction; V2a aggregates increased neuronal-process staining but were not tested for functional integration.',
    'conclusion / boundary condition',
    'high',
    'Full text Figs. 3-7',
    'high',
    '{"curator_notes": "No locomotor endpoint; this is a histology and cell-persistence study.", "source_paper_tracker_id": "M2A-P032", "topic_id": "M2B-T004", "tracker_id": "M2B-C029"}'
  FROM _m2_paper_map p
  WHERE p.tracker_id = 'M2A-P032'
  RETURNING claim_id
)
INSERT INTO _m2_claim_map (tracker_id, claim_id) SELECT 'M2B-C029', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Decellularized matrix components in multimodal hydrogels are usually one part of a larger regenerative cocktail.',
    'boundary condition',
    'medium',
    'Abstract',
    'medium',
    '{"curator_notes": "Avoids assigning all benefit to DBM alone.", "source_paper_tracker_id": "M2A-P022", "topic_id": "M2B-T004", "tracker_id": "M2B-C030"}'
  FROM _m2_paper_map p
  WHERE p.tracker_id = 'M2A-P022'
  RETURNING claim_id
)
INSERT INTO _m2_claim_map (tracker_id, claim_id) SELECT 'M2B-C030', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Chronic human scar-resection scaffold strategies depend on correctly distinguishing scar-rich target tissue from functionally important spared cord.',
    'boundary condition',
    'high',
    'Source page / M1A carried',
    'medium',
    '{"curator_notes": "Cross-module alignment with Module 1B.", "source_paper_tracker_id": "M2A-P001", "topic_id": "M2B-T005", "tracker_id": "M2B-C031"}'
  FROM _m2_paper_map p
  WHERE p.tracker_id = 'M2A-P001'
  RETURNING claim_id
)
INSERT INTO _m2_claim_map (tracker_id, claim_id) SELECT 'M2B-C031', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Chronic scar removal plus anisotropic scaffold channels can turn a chronic transection cavity into a guided repair substrate in rodents.',
    'conclusion',
    'medium',
    'Abstract',
    'medium',
    '{"curator_notes": "Strong chronic animal model claim.", "source_paper_tracker_id": "M2A-P006", "topic_id": "M2B-T005", "tracker_id": "M2B-C032"}'
  FROM _m2_paper_map p
  WHERE p.tracker_id = 'M2A-P006'
  RETURNING claim_id
)
INSERT INTO _m2_claim_map (tracker_id, claim_id) SELECT 'M2B-C032', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Composite hydrogels can intentionally combine structural guidance with biochemical regulation, blurring scaffold and cargo categories.',
    'implication',
    'medium',
    'Abstract',
    'medium',
    '{"curator_notes": "AFG/fSAP anchor.", "source_paper_tracker_id": "M2A-P019", "topic_id": "M2B-T007", "tracker_id": "M2B-C033"}'
  FROM _m2_paper_map p
  WHERE p.tracker_id = 'M2A-P019'
  RETURNING claim_id
)
INSERT INTO _m2_claim_map (tracker_id, claim_id) SELECT 'M2B-C033', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Surface-capping scaffolds are a distinct repair geometry from implanted lesion bridges and can preserve early neuronal fibers while reducing scar/fibrotic signals in a bundled HA/PPY/PM-CURC-iNPC strategy.',
    'implication / boundary condition',
    'high',
    'Full text Figs. 5-9',
    'high',
    '{"curator_notes": "HA demilune cap; one-week n=3 study did not reduce Iba1/ED1 inflammation or establish function.", "source_paper_tracker_id": "M2A-P034", "topic_id": "M2B-T007", "tracker_id": "M2B-C034"}'
  FROM _m2_paper_map p
  WHERE p.tracker_id = 'M2A-P034'
  RETURNING claim_id
)
INSERT INTO _m2_claim_map (tracker_id, claim_id) SELECT 'M2B-C034', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'The scaffold literature should be synthesized by material, cargo, cell source, injury model, chronicity, and outcome class rather than by a single global pro-repair claim.',
    'synthesis',
    'high',
    'Review map',
    'medium',
    '{"curator_notes": "Central synthesis caution.", "source_paper_tracker_id": "M2A-R001-R008", "topic_id": "M2B-T008", "tracker_id": "M2B-C035"}'
  FROM _m2_paper_map p
  WHERE p.tracker_id = 'M2A-R001'
  RETURNING claim_id
)
INSERT INTO _m2_claim_map (tracker_id, claim_id) SELECT 'M2B-C035', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Chronic translation requires anatomical compatibility between scaffold strategy and lesion architecture, not just a positive acute rodent repair signal.',
    'synthesis',
    'high',
    'Review map / Module 1B bridge',
    'medium',
    '{"curator_notes": "Cross-module synthesis statement.", "source_paper_tracker_id": "M2A-R005-R008", "topic_id": "M2B-T008", "tracker_id": "M2B-C036"}'
  FROM _m2_paper_map p
  WHERE p.tracker_id = 'M2A-R005'
  RETURNING claim_id
)
INSERT INTO _m2_claim_map (tracker_id, claim_id) SELECT 'M2B-C036', claim_id FROM inserted;

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Small human chronic cohort; feasibility only", "strength": "medium", "tracker_id": "M2B-L001"}'
FROM _m2_claim_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O001'
WHERE c.tracker_id = 'M2B-C001';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Full-text chronic human clinical support with no ASIA-grade improvement", "strength": "high", "tracker_id": "M2B-L002"}'
FROM _m2_claim_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O002'
WHERE c.tracker_id = 'M2B-C002';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Non-human primate bridge evidence", "strength": "medium", "tracker_id": "M2B-L003"}'
FROM _m2_claim_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O003'
WHERE c.tracker_id = 'M2B-C003';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Aligned tube observation supports guidance claim", "strength": "medium", "tracker_id": "M2B-L004"}'
FROM _m2_claim_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O005'
WHERE c.tracker_id = 'M2B-C004';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Conductive/electrical scaffold observation", "strength": "medium", "tracker_id": "M2B-L005"}'
FROM _m2_claim_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O008'
WHERE c.tracker_id = 'M2B-C005';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Scaffold-only comparator present", "strength": "medium", "tracker_id": "M2B-L006"}'
FROM _m2_claim_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O009'
WHERE c.tracker_id = 'M2B-C006';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Full-text histological superiority vs Matrigel; BBB similar", "strength": "high", "tracker_id": "M2B-L007"}'
FROM _m2_claim_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O010'
WHERE c.tracker_id = 'M2B-C007';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Direct histology-positive/function-negative observation", "strength": "high", "tracker_id": "M2B-L008"}'
FROM _m2_claim_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O012'
WHERE c.tracker_id = 'M2B-C008';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Sequential release design and outcomes", "strength": "medium", "tracker_id": "M2B-L009"}'
FROM _m2_claim_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O014'
WHERE c.tracker_id = 'M2B-C009';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "ECM ingrowth plus immune/material boundary", "strength": "medium", "tracker_id": "M2B-L010"}'
FROM _m2_claim_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O015'
WHERE c.tracker_id = 'M2B-C010';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Chronic scar-removal alginate observation", "strength": "medium", "tracker_id": "M2B-L011"}'
FROM _m2_claim_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O017'
WHERE c.tracker_id = 'M2B-C011';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Full-text canine chronic scaffold/cell evidence", "strength": "high", "tracker_id": "M2B-L012"}'
FROM _m2_claim_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O018'
WHERE c.tracker_id = 'M2B-C012';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Surface-patch inflammatory modulation", "strength": "medium", "tracker_id": "M2B-L013"}'
FROM _m2_claim_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O020'
WHERE c.tracker_id = 'M2B-C013';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Boundary condition explicitly reported", "strength": "high", "tracker_id": "M2B-L014"}'
FROM _m2_claim_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O021'
WHERE c.tracker_id = 'M2B-C014';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "3D-printed NPC scaffold also supports guidance but is cell-confounded", "strength": "low", "tracker_id": "M2B-L015"}'
FROM _m2_claim_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O004'
WHERE c.tracker_id = 'M2B-C004';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Supports scaffold-cell carrier idea but with different cells/material", "strength": "low", "tracker_id": "M2B-L016"}'
FROM _m2_claim_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O010'
WHERE c.tracker_id = 'M2B-C006';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Full-text n = 2 clinical boundary", "strength": "high", "tracker_id": "M2B-L017"}'
FROM _m2_claim_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O022'
WHERE c.tracker_id = 'M2B-C015';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Full-text multi-species translational continuity", "strength": "high", "tracker_id": "M2B-L018"}'
FROM _m2_claim_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O023'
WHERE c.tracker_id = 'M2B-C016';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "3D printed NPC scaffold relay observation", "strength": "medium", "tracker_id": "M2B-L019"}'
FROM _m2_claim_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O004'
WHERE c.tracker_id = 'M2B-C017';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Multi-channel PLGA platform observation", "strength": "medium", "tracker_id": "M2B-L020"}'
FROM _m2_claim_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O006'
WHERE c.tracker_id = 'M2B-C018';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Magnetic alignment observation", "strength": "medium", "tracker_id": "M2B-L021"}'
FROM _m2_claim_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O026'
WHERE c.tracker_id = 'M2B-C019';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "GelMA microchannel + hAEC neural-like cells", "strength": "medium", "tracker_id": "M2B-L022"}'
FROM _m2_claim_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O027'
WHERE c.tracker_id = 'M2B-C020';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Abstract-only chronic rat scaffold/cell support", "strength": "low", "tracker_id": "M2B-L023"}'
FROM _m2_claim_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O030'
WHERE c.tracker_id = 'M2B-C021';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Chronic histology-positive/function-negative boundary", "strength": "high", "tracker_id": "M2B-L024"}'
FROM _m2_claim_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O031'
WHERE c.tracker_id = 'M2B-C022';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Designed scaffold-cell-cue combination", "strength": "high", "tracker_id": "M2B-L025"}'
FROM _m2_claim_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O032'
WHERE c.tracker_id = 'M2B-C023';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "dSCM/GelMA stem-cell support observation", "strength": "medium", "tracker_id": "M2B-L026"}'
FROM _m2_claim_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O033'
WHERE c.tracker_id = 'M2B-C024';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Material niche observation", "strength": "medium", "tracker_id": "M2B-L027"}'
FROM _m2_claim_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O044'
WHERE c.tracker_id = 'M2B-C024';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Collagen-tethered exosome delivery", "strength": "medium", "tracker_id": "M2B-L028"}'
FROM _m2_claim_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O037'
WHERE c.tracker_id = 'M2B-C025';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Full-text bFGF hydrogel complete transection observation", "strength": "high", "tracker_id": "M2B-L029"}'
FROM _m2_claim_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O038'
WHERE c.tracker_id = 'M2B-C026';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "PCL/PSA/MP anti-inflammatory nanofiber observation", "strength": "medium", "tracker_id": "M2B-L030"}'
FROM _m2_claim_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O041'
WHERE c.tracker_id = 'M2B-C027';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Agarose protein-release methods anchor", "strength": "medium", "tracker_id": "M2B-L031"}'
FROM _m2_claim_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O042'
WHERE c.tracker_id = 'M2B-C028';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Astrocyte ECM subtype observation", "strength": "medium", "tracker_id": "M2B-L032"}'
FROM _m2_claim_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O016'
WHERE c.tracker_id = 'M2B-C029';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "DBM/PDRN/TI-EV/NPC multimodal hydrogel observation", "strength": "medium", "tracker_id": "M2B-L033"}'
FROM _m2_claim_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O034'
WHERE c.tracker_id = 'M2B-C030';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "DBM component boundary", "strength": "medium", "tracker_id": "M2B-L034"}'
FROM _m2_claim_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O045'
WHERE c.tracker_id = 'M2B-C030';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Resected human scar marker observation", "strength": "high", "tracker_id": "M2B-L035"}'
FROM _m2_claim_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O046'
WHERE c.tracker_id = 'M2B-C031';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Human scar resection feasibility context", "strength": "medium", "tracker_id": "M2B-L036"}'
FROM _m2_claim_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O001'
WHERE c.tracker_id = 'M2B-C031';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Chronic anisotropic alginate observation", "strength": "medium", "tracker_id": "M2B-L037"}'
FROM _m2_claim_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O017'
WHERE c.tracker_id = 'M2B-C032';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "AFG/fSAP combined cue observation", "strength": "medium", "tracker_id": "M2B-L038"}'
FROM _m2_claim_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O048'
WHERE c.tracker_id = 'M2B-C033';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "HA demilune surface capping observation", "strength": "medium", "tracker_id": "M2B-L039"}'
FROM _m2_claim_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O019'
WHERE c.tracker_id = 'M2B-C034';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Review-map material taxonomy caution", "strength": "high", "tracker_id": "M2B-L040"}'
FROM _m2_claim_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O049'
WHERE c.tracker_id = 'M2B-C035';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Review-map combination therapy caution", "strength": "high", "tracker_id": "M2B-L041"}'
FROM _m2_claim_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O050'
WHERE c.tracker_id = 'M2B-C035';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Review-map chronic translation caution", "strength": "high", "tracker_id": "M2B-L042"}'
FROM _m2_claim_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O050'
WHERE c.tracker_id = 'M2B-C036';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Human scar/neural boundary context", "strength": "medium", "tracker_id": "M2B-L043"}'
FROM _m2_claim_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O046'
WHERE c.tracker_id = 'M2B-C036';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Aligned nanofiber guidance/delivery support", "strength": "medium", "tracker_id": "M2B-L044"}'
FROM _m2_claim_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O024'
WHERE c.tracker_id = 'M2B-C004';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Aligned collagen scaffold guidance/cell-retention support", "strength": "medium", "tracker_id": "M2B-L045"}'
FROM _m2_claim_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O025'
WHERE c.tracker_id = 'M2B-C004';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Injectable alignment support", "strength": "medium", "tracker_id": "M2B-L046"}'
FROM _m2_claim_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O026'
WHERE c.tracker_id = 'M2B-C004';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Composite structural/biochemical guidance support", "strength": "medium", "tracker_id": "M2B-L047"}'
FROM _m2_claim_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O048'
WHERE c.tracker_id = 'M2B-C005';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Another scaffold/cell translation context", "strength": "low", "tracker_id": "M2B-L048"}'
FROM _m2_claim_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O023'
WHERE c.tracker_id = 'M2B-C006';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "ECM/cell-carrier contextual support", "strength": "low", "tracker_id": "M2B-L049"}'
FROM _m2_claim_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O034'
WHERE c.tracker_id = 'M2B-C007';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Another histology-positive/function-negative example", "strength": "high", "tracker_id": "M2B-L050"}'
FROM _m2_claim_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O031'
WHERE c.tracker_id = 'M2B-C008';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Timed cue scaffold supports temporal-design concept", "strength": "medium", "tracker_id": "M2B-L051"}'
FROM _m2_claim_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O028'
WHERE c.tracker_id = 'M2B-C009';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "dECM chronic scaffold context", "strength": "medium", "tracker_id": "M2B-L052"}'
FROM _m2_claim_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O043'
WHERE c.tracker_id = 'M2B-C010';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Chronic scar-resection scaffold/cell context", "strength": "low", "tracker_id": "M2B-L053"}'
FROM _m2_claim_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O030'
WHERE c.tracker_id = 'M2B-C011';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Human chronic NeuroRegen/hUC-MSC context", "strength": "medium", "tracker_id": "M2B-L054"}'
FROM _m2_claim_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O047'
WHERE c.tracker_id = 'M2B-C012';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Surface-capping scaffold context", "strength": "medium", "tracker_id": "M2B-L055"}'
FROM _m2_claim_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O019'
WHERE c.tracker_id = 'M2B-C013';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Functional dissociation also seen with NT-3 fibrin", "strength": "medium", "tracker_id": "M2B-L056"}'
FROM _m2_claim_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O012'
WHERE c.tracker_id = 'M2B-C014';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Scaffold architecture is best treated as a lesion-topology intervention: aligned fibers, channels, pores, conduits, and printed geometry can organize axon, cell, and tissue growth, but the relevant claim depends on matching the scaffold format to lesion shape, gap size, and endpoint.',
    'M2B-T001',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": [], "consensus_draft_id": "M2B-S001", "evidence_status": "CONSENSUS-READY FIRST PASS", "observation_tracker_ids": ["M2B-O004", "M2B-O005", "M2B-O006", "M2B-O007", "M2B-O008", "M2B-O024", "M2B-O025", "M2B-O026", "M2B-O027", "M2B-O028", "M2B-O029"], "supporting_evidence_notes": "Supported by O004-O008 and O024-O029; partly confounded by cells/cargo", "topic_id": "M2B-T001"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m2_consensus_map (tracker_id, consensus_id) SELECT 'M2B-S001', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m2_consensus_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O004'
WHERE c.tracker_id = 'M2B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m2_consensus_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O005'
WHERE c.tracker_id = 'M2B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m2_consensus_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O006'
WHERE c.tracker_id = 'M2B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m2_consensus_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O007'
WHERE c.tracker_id = 'M2B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m2_consensus_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O008'
WHERE c.tracker_id = 'M2B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m2_consensus_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O024'
WHERE c.tracker_id = 'M2B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m2_consensus_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O025'
WHERE c.tracker_id = 'M2B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m2_consensus_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O026'
WHERE c.tracker_id = 'M2B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m2_consensus_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O027'
WHERE c.tracker_id = 'M2B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m2_consensus_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O028'
WHERE c.tracker_id = 'M2B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m2_consensus_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O029'
WHERE c.tracker_id = 'M2B-S001';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Scaffold-cell combinations repeatedly improve retention, survival, bridging, or repair-associated signals after SCI, but first-pass consensus should assign causality jointly unless experiments isolate scaffold-only, cell-only, and combined arms.',
    'M2B-T002',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": [], "consensus_draft_id": "M2B-S002", "evidence_status": "CONSENSUS-READY FIRST PASS", "observation_tracker_ids": ["M2B-O009", "M2B-O010", "M2B-O011", "M2B-O030", "M2B-O031", "M2B-O032", "M2B-O033", "M2B-O034", "M2B-O035", "M2B-O036"], "supporting_evidence_notes": "Supported by O009-O011 and O030-O036; central Module 2B causality caution", "topic_id": "M2B-T002"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m2_consensus_map (tracker_id, consensus_id) SELECT 'M2B-S002', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m2_consensus_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O009'
WHERE c.tracker_id = 'M2B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m2_consensus_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O010'
WHERE c.tracker_id = 'M2B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m2_consensus_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O011'
WHERE c.tracker_id = 'M2B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m2_consensus_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O030'
WHERE c.tracker_id = 'M2B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m2_consensus_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O031'
WHERE c.tracker_id = 'M2B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m2_consensus_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O032'
WHERE c.tracker_id = 'M2B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m2_consensus_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O033'
WHERE c.tracker_id = 'M2B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m2_consensus_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O034'
WHERE c.tracker_id = 'M2B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m2_consensus_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O035'
WHERE c.tracker_id = 'M2B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m2_consensus_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O036'
WHERE c.tracker_id = 'M2B-S002';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Scaffold cargo delivery can reshape trophic, inflammatory, angiogenic, and regenerative conditions at the lesion, yet histological improvement and motor recovery must remain separate endpoints because release success does not guarantee functional benefit.',
    'M2B-T003',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": [], "consensus_draft_id": "M2B-S003", "evidence_status": "CONSENSUS-READY FIRST PASS", "observation_tracker_ids": ["M2B-O012", "M2B-O013", "M2B-O014", "M2B-O037", "M2B-O038", "M2B-O039", "M2B-O040", "M2B-O041", "M2B-O042"], "supporting_evidence_notes": "Supported by O012-O014 and O037-O042; NT-3 fibrin gives boundary condition", "topic_id": "M2B-T003"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m2_consensus_map (tracker_id, consensus_id) SELECT 'M2B-S003', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m2_consensus_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O012'
WHERE c.tracker_id = 'M2B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m2_consensus_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O013'
WHERE c.tracker_id = 'M2B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m2_consensus_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O014'
WHERE c.tracker_id = 'M2B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m2_consensus_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O037'
WHERE c.tracker_id = 'M2B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m2_consensus_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O038'
WHERE c.tracker_id = 'M2B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m2_consensus_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O039'
WHERE c.tracker_id = 'M2B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m2_consensus_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O040'
WHERE c.tracker_id = 'M2B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m2_consensus_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O041'
WHERE c.tracker_id = 'M2B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m2_consensus_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O042'
WHERE c.tracker_id = 'M2B-S003';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Natural ECM, decellularized matrix, and hydrogel scaffolds provide tissue-like repair environments, but their effects are conditional on ECM source, stiffness/degradation, immune response, vascular integration, lesion model, and whether added cells or factors are present.',
    'M2B-T004',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": [], "consensus_draft_id": "M2B-S004", "evidence_status": "CONSENSUS-READY FIRST PASS", "observation_tracker_ids": ["M2B-O015", "M2B-O016", "M2B-O043", "M2B-O044", "M2B-O045"], "supporting_evidence_notes": "Supported by O015-O016 and O043-O045", "topic_id": "M2B-T004"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m2_consensus_map (tracker_id, consensus_id) SELECT 'M2B-S004', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m2_consensus_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O015'
WHERE c.tracker_id = 'M2B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m2_consensus_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O016'
WHERE c.tracker_id = 'M2B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m2_consensus_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O043'
WHERE c.tracker_id = 'M2B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m2_consensus_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O044'
WHERE c.tracker_id = 'M2B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m2_consensus_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O045'
WHERE c.tracker_id = 'M2B-S004';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Chronic scar or cavity scaffold repair is a reconstruction strategy only when lesion anatomy permits safe resection, boundary identification, and gap filling; these rows should be interpreted through Module 1 lesion architecture rather than as generic scaffold efficacy.',
    'M2B-T005',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": [], "consensus_draft_id": "M2B-S005", "evidence_status": "CONSENSUS-READY FIRST PASS", "observation_tracker_ids": ["M2B-O001", "M2B-O002", "M2B-O017", "M2B-O018", "M2B-O046", "M2B-O047"], "supporting_evidence_notes": "Supported by O001-O002, O017-O018, and O046-O047", "topic_id": "M2B-T005"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m2_consensus_map (tracker_id, consensus_id) SELECT 'M2B-S005', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m2_consensus_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O001'
WHERE c.tracker_id = 'M2B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m2_consensus_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O002'
WHERE c.tracker_id = 'M2B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m2_consensus_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O017'
WHERE c.tracker_id = 'M2B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m2_consensus_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O018'
WHERE c.tracker_id = 'M2B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m2_consensus_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O046'
WHERE c.tracker_id = 'M2B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m2_consensus_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O047'
WHERE c.tracker_id = 'M2B-S005';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Large-animal, primate, and early human scaffold studies establish feasibility, surgical handling, safety monitoring, and translational plausibility more strongly than definitive efficacy, so species, lesion completeness, follow-up, and clinical endpoint class must be retained.',
    'M2B-T006',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": [], "consensus_draft_id": "M2B-S006", "evidence_status": "CONSENSUS-READY FIRST PASS", "observation_tracker_ids": ["M2B-O001", "M2B-O002", "M2B-O003", "M2B-O018", "M2B-O022", "M2B-O023", "M2B-O040"], "supporting_evidence_notes": "Supported by O001-O003, O018, O022-O023, and O040", "topic_id": "M2B-T006"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m2_consensus_map (tracker_id, consensus_id) SELECT 'M2B-S006', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m2_consensus_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O001'
WHERE c.tracker_id = 'M2B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m2_consensus_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O002'
WHERE c.tracker_id = 'M2B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m2_consensus_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O003'
WHERE c.tracker_id = 'M2B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m2_consensus_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O018'
WHERE c.tracker_id = 'M2B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m2_consensus_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O022'
WHERE c.tracker_id = 'M2B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m2_consensus_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O023'
WHERE c.tracker_id = 'M2B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m2_consensus_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O040'
WHERE c.tracker_id = 'M2B-S006';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Conductive, electrically active, multimodal, and surface-patch scaffolds extend the module beyond passive bridging by adding stimulation interfaces, inflammatory modulation, or lesion capping, but each active component needs its own attribution boundary.',
    'M2B-T007',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": [], "consensus_draft_id": "M2B-S007", "evidence_status": "CONSENSUS-READY FIRST PASS", "observation_tracker_ids": ["M2B-O008", "M2B-O019", "M2B-O020", "M2B-O048"], "supporting_evidence_notes": "Supported by O008, O019-O020, and O048", "topic_id": "M2B-T007"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m2_consensus_map (tracker_id, consensus_id) SELECT 'M2B-S007', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m2_consensus_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O008'
WHERE c.tracker_id = 'M2B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m2_consensus_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O019'
WHERE c.tracker_id = 'M2B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m2_consensus_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O020'
WHERE c.tracker_id = 'M2B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m2_consensus_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O048'
WHERE c.tracker_id = 'M2B-S007';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Module 2 should synthesize scaffold repair by material class, architecture, cargo, cell combination, lesion chronicity, species, and endpoint family; a pooled pro-regenerative scaffold claim would erase the main design and attribution boundaries.',
    'M2B-T008',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": [], "consensus_draft_id": "M2B-S008", "evidence_status": "CONSENSUS-READY FIRST PASS", "observation_tracker_ids": ["M2B-O049", "M2B-O050"], "supporting_evidence_notes": "Supported by O049-O050 and all boundary records", "topic_id": "M2B-T008"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m2_consensus_map (tracker_id, consensus_id) SELECT 'M2B-S008', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m2_consensus_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O049'
WHERE c.tracker_id = 'M2B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m2_consensus_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O050'
WHERE c.tracker_id = 'M2B-S008';

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
  SELECT COUNT(*) INTO paper_count FROM _m2_paper_map;
  SELECT COUNT(*) INTO experiment_count FROM _m2_experiment_map;
  SELECT COUNT(*) INTO observation_count FROM _m2_observation_map;
  SELECT COUNT(*) INTO claim_count FROM _m2_claim_map;
  SELECT COUNT(*) INTO link_count FROM EvidenceLink;
  SELECT COUNT(*) INTO consensus_count FROM _m2_consensus_map;
  SELECT COUNT(*) INTO consensus_observation_count FROM Consensus_Observation;
  IF paper_count <> 51 THEN RAISE EXCEPTION 'Expected 51 papers, found %', paper_count; END IF;
  IF experiment_count <> 78 THEN RAISE EXCEPTION 'Unexpected experiment count %', experiment_count; END IF;
  IF observation_count <> 90 THEN RAISE EXCEPTION 'Expected 90 observations, found %', observation_count; END IF;
  IF claim_count <> 36 THEN RAISE EXCEPTION 'Expected 36 claims, found %', claim_count; END IF;
  IF link_count <> 56 THEN RAISE EXCEPTION 'Expected 56 evidence links, found %', link_count; END IF;
  IF consensus_count <> 8 THEN RAISE EXCEPTION 'Expected 8 consensus rows, found %', consensus_count; END IF;
  IF consensus_observation_count <> 54 THEN RAISE EXCEPTION 'Unexpected consensus-observation count %', consensus_observation_count; END IF;
END $$;

COMMIT;
