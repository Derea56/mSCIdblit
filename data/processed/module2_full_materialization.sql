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
    NULL, '{"curator_notes": "Chronic complete SCI scaffold/cell anchor", "module": "Module 2", "tracker_id": "M2A-P003"}'
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
    NULL, '{"curator_notes": "High-yield scaffold architecture anchor", "module": "Module 2", "tracker_id": "M2A-P004"}'
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
    NULL, '{"curator_notes": "Alignment/guidance scaffold anchor", "module": "Module 2", "tracker_id": "M2A-P005"}'
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
    NULL, '{"curator_notes": "Chronic scar-removal scaffold bridge", "module": "Module 2", "tracker_id": "M2A-P006"}'
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
    NULL, '{"curator_notes": "Scaffold cargo-delivery anchor", "module": "Module 2", "tracker_id": "M2A-P007"}'
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
    NULL, '{"curator_notes": "Early synthetic channel-architecture scaffold anchor", "module": "Module 2", "tracker_id": "M2A-P010"}'
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
    NULL, '{"curator_notes": "Peptide nanofiber bridge anchor", "module": "Module 2", "tracker_id": "M2A-P011"}'
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
    NULL, '{"curator_notes": "Complete-transection PLGA/cell bridge anchor", "module": "Module 2", "tracker_id": "M2A-P012"}'
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
    NULL, '{"curator_notes": "Patterned growth-factor/cell bridge anchor", "module": "Module 2", "tracker_id": "M2A-P013"}'
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
    NULL, '{"curator_notes": "Human spinal cord-derived NSPC plus aligned collagen anchor", "module": "Module 2", "tracker_id": "M2A-P018"}'
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
    NULL, '{"curator_notes": "Multimodal biophysical/biochemical hydrogel anchor", "module": "Module 2", "tracker_id": "M2A-P019"}'
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
    NULL, '{"curator_notes": "Spinal cord dECM/GelMA plus stem-cell anchor", "module": "Module 2", "tracker_id": "M2A-P020"}'
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
    NULL, '{"curator_notes": "Injectable alignment strategy anchor", "module": "Module 2", "tracker_id": "M2A-P021"}'
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
    NULL, '{"curator_notes": "Complex multimodal hydrogel/cell/EV strategy anchor", "module": "Module 2", "tracker_id": "M2A-P022"}'
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
    NULL, '{"curator_notes": "Hydrogel plus stem cell plus anti-inflammatory nanoparticle anchor", "module": "Module 2", "tracker_id": "M2A-P023"}'
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
    NULL, '{"curator_notes": "Longitudinal HA hydrogel plus multi-cargo microsphere anchor", "module": "Module 2", "tracker_id": "M2A-P027"}'
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
    NULL, '{"curator_notes": "Injectable collagen/NT-3 repair and scar-response anchor", "module": "Module 2", "tracker_id": "M2A-P028"}'
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
    NULL, '{"curator_notes": "Non-human primate translational scaffold anchor", "module": "Module 2", "tracker_id": "M2A-P029"}'
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
    NULL, '{"curator_notes": "Large-animal sustained NT-3/fibroin scaffold anchor", "module": "Module 2", "tracker_id": "M2A-P030"}'
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
    NULL, '{"curator_notes": "Electrospun drug-loaded nanofiber scaffold anchor", "module": "Module 2", "tracker_id": "M2A-P031"}'
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
    NULL, '{"curator_notes": "Astrocyte-ECM and interneuron-supporting HA hydrogel anchor", "module": "Module 2", "tracker_id": "M2A-P032"}'
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
    NULL, '{"curator_notes": "Surface-capping conductive/combinatorial scaffold anchor", "module": "Module 2", "tracker_id": "M2A-P034"}'
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
    NULL, '{"curator_notes": "GelMA microchannel scaffold plus hAEC-derived neural cells anchor", "module": "Module 2", "tracker_id": "M2A-P035"}'
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
    NULL, '{"curator_notes": "Sequential release silk methacryloyl hydrogel anchor", "module": "Module 2", "tracker_id": "M2A-P036"}'
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
    NULL, '{"curator_notes": "Time-programmed 3D-printed hydrogel scaffold anchor", "module": "Module 2", "tracker_id": "M2A-P037"}'
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
    NULL, '{"curator_notes": "Surface patch/exosome/steroid hydrogel scaffold anchor", "module": "Module 2", "tracker_id": "M2A-P038"}'
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
    NULL, '{"curator_notes": "Conductive aligned scaffold plus electrical stimulation anchor", "module": "Module 2", "tracker_id": "M2A-P039"}'
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
    NULL, '{"curator_notes": "Agarose channel/protein-release scaffold methods anchor", "module": "Module 2", "tracker_id": "M2A-P040"}'
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
    NULL, '{"curator_notes": "Myelination-focused NT-3/TrkC neural scaffold anchor", "module": "Module 2", "tracker_id": "M2A-P041"}'
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
    NULL, '{"curator_notes": "3D-bioprinted silk/collagen cell scaffold anchor", "module": "Module 2", "tracker_id": "M2A-P042"}'
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
    NULL, '{"curator_notes": "OEC-seeded scaffold boundary/negative-mechanism anchor", "module": "Module 2", "tracker_id": "M2A-P043"}'
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
    'Histology assessed cavitary lesion filling, vascular endothelial cell migration, microenvironment changes, and tissue repair after scar resection plus kidney-derived dECM hydrogel scaffold.',
    'Scar resection/scaffold comparisons',
    'dECM scaffold after scar resection',
    '{"observation_tracker_ids": ["M2B-O031", "M2B-O043"], "source_experiment": {"chronicity_dpi_wpi": "Chronic phase", "control_type": "Scar resection/scaffold comparisons", "experiment_extracted": "YES", "experiment_id": "M2A-P003-E001", "figure_ref": "Abstract/source page / M1A carried", "injury_device": "Surgical scar resection", "injury_model": "Chronic complete SCI with cavitary lesion", "injury_severity": "Complete chronic lesion", "intervention_type": "dECM scaffold after scar resection", "methods_summary": "Histology assessed cavitary lesion filling, vascular endothelial cell migration, microenvironment changes, and tissue repair after scar resection plus kidney-derived dECM hydrogel scaffold.", "paper_id": "M2A-P003", "sex": "UNKNOWN", "species": "Rodent chronic complete SCI model", "strain": "UNKNOWN", "vertebral_level": "UNKNOWN"}, "source_experiment_tracker_id": "M2A-P003-E001", "source_paper_tracker_id": "M2A-P003", "tracker_key": "M2A-P003::M2A-P003-E001"}'
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
    'Human iPSC-derived NS/PC transplantation was combined with scaffold-supported scar resection to assess graft survival, host axon regeneration, histological repair, and lack of functional recovery.',
    'Scaffold/no-cell comparisons',
    'hNS/PC transplantation with scaffold support',
    '{"observation_tracker_ids": ["M2B-O052"], "source_experiment": {"chronicity_dpi_wpi": "Chronic phase", "control_type": "Scaffold/no-cell comparisons", "experiment_extracted": "YES", "experiment_id": "M2A-P003-E002", "figure_ref": "Abstract/source page / M1A carried", "injury_device": "Surgical scar resection + transplantation", "injury_model": "Chronic complete SCI with cavitary lesion", "injury_severity": "Complete chronic lesion", "intervention_type": "hNS/PC transplantation with scaffold support", "methods_summary": "Human iPSC-derived NS/PC transplantation was combined with scaffold-supported scar resection to assess graft survival, host axon regeneration, histological repair, and lack of functional recovery.", "paper_id": "M2A-P003", "sex": "UNKNOWN", "species": "Rodent chronic complete SCI model", "strain": "UNKNOWN", "vertebral_level": "UNKNOWN"}, "source_experiment_tracker_id": "M2A-P003-E002", "source_paper_tracker_id": "M2A-P003", "tracker_key": "M2A-P003::M2A-P003-E002"}'
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
    'Abstract',
    'Tracker experiment M2A-P004-E001',
    'Microscale continuous projection printing produced biomimetic CNS hydrogel scaffolds tailored to rodent spinal cord dimensions and scalable to human lesion geometries.',
    'Native spinal cord geometry',
    '3D-printed biomimetic hydrogel scaffold',
    '{"observation_tracker_ids": ["M2B-O004"], "source_experiment": {"chronicity_dpi_wpi": "N/A", "control_type": "Native spinal cord geometry", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P004-E001", "figure_ref": "Abstract", "injury_device": "uCPP scaffold fabrication", "injury_model": "Complete SCI geometry modeling", "injury_severity": "Complete SCI scaffold design", "intervention_type": "3D-printed biomimetic hydrogel scaffold", "methods_summary": "Microscale continuous projection printing produced biomimetic CNS hydrogel scaffolds tailored to rodent spinal cord dimensions and scalable to human lesion geometries.", "paper_id": "M2A-P004", "sex": "N/A", "species": "Rodent model / scalable human geometry", "strain": "N/A", "vertebral_level": "Spinal cord"}, "source_experiment_tracker_id": "M2A-P004-E001", "source_paper_tracker_id": "M2A-P004", "tracker_key": "M2A-P004::M2A-P004-E001"}'
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
    'Abstract',
    'Tracker experiment M2A-P004-E002',
    'NPC-loaded biomimetic scaffolds were implanted into complete SCI sites to assess host axon regeneration into the device, NPC axon extension into host cord, synaptic relay formation, synaptic transmission, and functional improvement.',
    'Injured scaffold/graft comparisons',
    'NPC-loaded 3D-printed scaffold implantation',
    '{"observation_tracker_ids": ["M2B-O053"], "source_experiment": {"chronicity_dpi_wpi": "Post-implant repair interval UNKNOWN", "control_type": "Injured scaffold/graft comparisons", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P004-E002", "figure_ref": "Abstract", "injury_device": "Complete spinal cord injury", "injury_model": "Complete SCI", "injury_severity": "Complete SCI", "intervention_type": "NPC-loaded 3D-printed scaffold implantation", "methods_summary": "NPC-loaded biomimetic scaffolds were implanted into complete SCI sites to assess host axon regeneration into the device, NPC axon extension into host cord, synaptic relay formation, synaptic transmission, and functional improvement.", "paper_id": "M2A-P004", "sex": "UNKNOWN", "species": "Rodent", "strain": "UNKNOWN", "vertebral_level": "UNKNOWN"}, "source_experiment_tracker_id": "M2A-P004-E002", "source_paper_tracker_id": "M2A-P004", "tracker_key": "M2A-P004::M2A-P004-E002"}'
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
    'Abstract',
    'Tracker experiment M2A-P005-E001',
    'Modular porous hydrogel tubes were assembled to fill the injury, integrate with host tissue by cell infiltration, and compare immune infiltration and glial scar response against gelfoam.',
    'Gelfoam control',
    'Porous aligned hydrogel tube implantation',
    '{"observation_tracker_ids": ["M2B-O005"], "source_experiment": {"chronicity_dpi_wpi": "1-2 WPI immune/scar assessment", "control_type": "Gelfoam control", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P005-E001", "figure_ref": "Abstract", "injury_device": "Experimental SCI", "injury_model": "SCI defect", "injury_severity": "Lesion defect filled with tubes", "intervention_type": "Porous aligned hydrogel tube implantation", "methods_summary": "Modular porous hydrogel tubes were assembled to fill the injury, integrate with host tissue by cell infiltration, and compare immune infiltration and glial scar response against gelfoam.", "paper_id": "M2A-P005", "sex": "UNKNOWN", "species": "Rodent model context", "strain": "UNKNOWN", "vertebral_level": "UNKNOWN"}, "source_experiment_tracker_id": "M2A-P005-E001", "source_paper_tracker_id": "M2A-P005", "tracker_key": "M2A-P005::M2A-P005-E001"}'
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
    'Abstract',
    'Tracker experiment M2A-P005-E002',
    'Hydrogel tubes guided robust axon growth along inner and outer tube surfaces, increased axon density within tubes, supported myelination of a subset of axons, and enhanced functional recovery.',
    'Gelfoam control',
    'Hydrogel tube axon-guidance scaffold',
    '{"observation_tracker_ids": ["M2B-O054"], "source_experiment": {"chronicity_dpi_wpi": "Recovery phase UNKNOWN", "control_type": "Gelfoam control", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P005-E002", "figure_ref": "Abstract", "injury_device": "Experimental SCI", "injury_model": "SCI defect", "injury_severity": "Lesion defect filled with tubes", "intervention_type": "Hydrogel tube axon-guidance scaffold", "methods_summary": "Hydrogel tubes guided robust axon growth along inner and outer tube surfaces, increased axon density within tubes, supported myelination of a subset of axons, and enhanced functional recovery.", "paper_id": "M2A-P005", "sex": "UNKNOWN", "species": "Rodent model context", "strain": "UNKNOWN", "vertebral_level": "UNKNOWN"}, "source_experiment_tracker_id": "M2A-P005-E002", "source_paper_tracker_id": "M2A-P005", "tracker_key": "M2A-P005::M2A-P005-E002"}'
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
    'After scar resection, anisotropic alginate hydrogels were implanted into the chronic transection cavity and assessed for electrophysiological conductivity and locomotor function.',
    'Scar resection without hydrogel / pre-engraftment baseline',
    'Anisotropic alginate hydrogel engraftment',
    '{"observation_tracker_ids": ["M2B-O017"], "source_experiment": {"chronicity_dpi_wpi": "Scar resection 4 WPI; outcomes up to 3 months after engraftment", "control_type": "Scar resection without hydrogel / pre-engraftment baseline", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P006-E001", "figure_ref": "Abstract", "injury_device": "Thoracic transection + scar resection", "injury_model": "Chronic complete thoracic transection SCI", "injury_severity": "Complete chronic transection", "intervention_type": "Anisotropic alginate hydrogel engraftment", "methods_summary": "After scar resection, anisotropic alginate hydrogels were implanted into the chronic transection cavity and assessed for electrophysiological conductivity and locomotor function.", "paper_id": "M2A-P006", "sex": "UNKNOWN", "species": "Rattus norvegicus", "strain": "UNKNOWN", "vertebral_level": "Thoracic"}, "source_experiment_tracker_id": "M2A-P006-E001", "source_paper_tracker_id": "M2A-P006", "tracker_key": "M2A-P006::M2A-P006-E001"}'
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
    'Histology assessed host-cell migration, fibroglial scarring, and regeneration of corticospinal, raphaespinal, propriospinal, and ascending sensory axons through and beyond hydrogel channels.',
    'Scar resection comparison',
    'Anisotropic alginate hydrogel channels',
    '{"observation_tracker_ids": ["M2B-O055"], "source_experiment": {"chronicity_dpi_wpi": "Up to 3 months after engraftment", "control_type": "Scar resection comparison", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P006-E002", "figure_ref": "Abstract", "injury_device": "Thoracic transection + scar resection", "injury_model": "Chronic complete thoracic transection SCI", "injury_severity": "Complete chronic transection", "intervention_type": "Anisotropic alginate hydrogel channels", "methods_summary": "Histology assessed host-cell migration, fibroglial scarring, and regeneration of corticospinal, raphaespinal, propriospinal, and ascending sensory axons through and beyond hydrogel channels.", "paper_id": "M2A-P006", "sex": "UNKNOWN", "species": "Rattus norvegicus", "strain": "UNKNOWN", "vertebral_level": "Thoracic"}, "source_experiment_tracker_id": "M2A-P006-E002", "source_paper_tracker_id": "M2A-P006", "tracker_key": "M2A-P006::M2A-P006-E002"}'
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
    'CBD-Lamp2b and miR21 were overexpressed in HEK293T cells to produce engineered exosomes that tether to collagen-I scaffold and support sustained miR21 release.',
    'Untethered exosome/scaffold logic',
    'CBD-LP-miR21 exosome collagen tethering',
    '{"observation_tracker_ids": ["M2B-O037"], "source_experiment": {"chronicity_dpi_wpi": "In vitro", "control_type": "Untethered exosome/scaffold logic", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P007-E001", "figure_ref": "Abstract", "injury_device": "N/A", "injury_model": "In vitro scaffold delivery model", "injury_severity": "N/A", "intervention_type": "CBD-LP-miR21 exosome collagen tethering", "methods_summary": "CBD-Lamp2b and miR21 were overexpressed in HEK293T cells to produce engineered exosomes that tether to collagen-I scaffold and support sustained miR21 release.", "paper_id": "M2A-P007", "sex": "N/A", "species": "HEK293T cells / scaffold system", "strain": "HEK293T", "vertebral_level": "N/A"}, "source_experiment_tracker_id": "M2A-P007-E001", "source_paper_tracker_id": "M2A-P007", "tracker_key": "M2A-P007::M2A-P007-E001"}'
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
    'A collagen-I scaffold enriched with CBD-LP-miR21 exosomes was applied to SCI repair to improve exosome retention, sustained release, and repair outcomes.',
    'Nonfunctionalized scaffold/exosome comparisons',
    'Functionalized collagen-I scaffold with miR21-loaded exosomes',
    '{"observation_tracker_ids": ["M2B-O056"], "source_experiment": {"chronicity_dpi_wpi": "Post-injury repair interval UNKNOWN", "control_type": "Nonfunctionalized scaffold/exosome comparisons", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P007-E002", "figure_ref": "Abstract", "injury_device": "Experimental SCI", "injury_model": "SCI", "injury_severity": "UNKNOWN", "intervention_type": "Functionalized collagen-I scaffold with miR21-loaded exosomes", "methods_summary": "A collagen-I scaffold enriched with CBD-LP-miR21 exosomes was applied to SCI repair to improve exosome retention, sustained release, and repair outcomes.", "paper_id": "M2A-P007", "sex": "UNKNOWN", "species": "SCI model context", "strain": "UNKNOWN", "vertebral_level": "UNKNOWN"}, "source_experiment_tracker_id": "M2A-P007-E002", "source_paper_tracker_id": "M2A-P007", "tracker_key": "M2A-P007::M2A-P007-E002"}'
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
    'Abstract',
    'Tracker experiment M2A-P008-E001',
    'A 3D aligned nanofiber-hydrogel scaffold provided sustained nonviral delivery of proteins and small noncoding RNAs plus contact guidance after C5 hemi-incision, with aligned axon regeneration observed by 1 WPI.',
    'Injury/scaffold comparison',
    '3D aligned nanofiber-hydrogel scaffold with nonviral delivery',
    '{"observation_tracker_ids": ["M2B-O024"], "source_experiment": {"chronicity_dpi_wpi": "1 WPI early axon assessment", "control_type": "Injury/scaffold comparison", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P008-E001", "figure_ref": "Abstract", "injury_device": "Hemi-incision", "injury_model": "Cervical hemi-incision SCI", "injury_severity": "C5 hemi-incision", "intervention_type": "3D aligned nanofiber-hydrogel scaffold with nonviral delivery", "methods_summary": "A 3D aligned nanofiber-hydrogel scaffold provided sustained nonviral delivery of proteins and small noncoding RNAs plus contact guidance after C5 hemi-incision, with aligned axon regeneration observed by 1 WPI.", "paper_id": "M2A-P008", "sex": "UNKNOWN", "species": "Rattus norvegicus", "strain": "UNKNOWN", "vertebral_level": "C5"}, "source_experiment_tracker_id": "M2A-P008-E001", "source_paper_tracker_id": "M2A-P008", "tracker_key": "M2A-P008::M2A-P008-E001"}'
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
    'Abstract',
    'Tracker experiment M2A-P008-E002',
    'Inflammatory response and scar tissue formation were assessed after scaffold implantation, with no excessive inflammatory response or scar formation reported in the abstract.',
    'Injury/scaffold comparison',
    '3D aligned nanofiber-hydrogel scaffold',
    '{"observation_tracker_ids": ["M2B-O057"], "source_experiment": {"chronicity_dpi_wpi": "Post-implant response interval UNKNOWN", "control_type": "Injury/scaffold comparison", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P008-E002", "figure_ref": "Abstract", "injury_device": "Hemi-incision", "injury_model": "Cervical hemi-incision SCI", "injury_severity": "C5 hemi-incision", "intervention_type": "3D aligned nanofiber-hydrogel scaffold", "methods_summary": "Inflammatory response and scar tissue formation were assessed after scaffold implantation, with no excessive inflammatory response or scar formation reported in the abstract.", "paper_id": "M2A-P008", "sex": "UNKNOWN", "species": "Rattus norvegicus", "strain": "UNKNOWN", "vertebral_level": "C5"}, "source_experiment_tracker_id": "M2A-P008-E002", "source_paper_tracker_id": "M2A-P008", "tracker_key": "M2A-P008::M2A-P008-E002"}'
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
    'Abstract',
    'Tracker experiment M2A-P009-E001',
    'Eight chronic complete SCI patients underwent neurophysiology-guided scar resection and implantation of hUCB-MSC-loaded NeuroRegen scaffold, with adverse events and neurological/electrophysiological outcomes tracked for 1 year.',
    'Preoperative baseline / safety monitoring',
    'NeuroRegen scaffold + hUCB-MSC implantation',
    '{"observation_tracker_ids": ["M2B-O002", "M2B-O047"], "source_experiment": {"chronicity_dpi_wpi": "Chronic; 1-year follow-up", "control_type": "Preoperative baseline / safety monitoring", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P009-E001", "figure_ref": "Abstract", "injury_device": "Clinical SCI + surgical scar resection", "injury_model": "Chronic complete SCI", "injury_severity": "Chronic complete SCI", "intervention_type": "NeuroRegen scaffold + hUCB-MSC implantation", "methods_summary": "Eight chronic complete SCI patients underwent neurophysiology-guided scar resection and implantation of hUCB-MSC-loaded NeuroRegen scaffold, with adverse events and neurological/electrophysiological outcomes tracked for 1 year.", "paper_id": "M2A-P009", "sex": "Mixed/UNKNOWN", "species": "Homo sapiens", "strain": "N/A", "vertebral_level": "Variable"}, "source_experiment_tracker_id": "M2A-P009-E001", "source_paper_tracker_id": "M2A-P009", "tracker_key": "M2A-P009::M2A-P009-E001"}'
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
    'PLGA 85:15 was injection molded with rapid solvent evaporation to generate parallel-channel scaffolds for SCI repair experiments.',
    'Architecture comparison',
    'PLGA multi-channel scaffold',
    '{"observation_tracker_ids": ["M2B-O006"], "source_experiment": {"chronicity_dpi_wpi": "N/A", "control_type": "Architecture comparison", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P010-E001", "figure_ref": "Abstract", "injury_device": "PLGA scaffold fabrication", "injury_model": "SCI repair scaffold design", "injury_severity": "N/A", "intervention_type": "PLGA multi-channel scaffold", "methods_summary": "PLGA 85:15 was injection molded with rapid solvent evaporation to generate parallel-channel scaffolds for SCI repair experiments.", "paper_id": "M2A-P010", "sex": "N/A", "species": "Scaffold system / rat SCI platform", "strain": "N/A", "vertebral_level": "N/A"}, "source_experiment_tracker_id": "M2A-P010-E001", "source_paper_tracker_id": "M2A-P010", "tracker_key": "M2A-P010::M2A-P010-E001"}'
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
    'The scaffold was framed as a platform to test architecture, transplanted cells, and local molecular agents for axon regeneration.',
    'Scaffold architecture/cell/molecule comparison',
    'Multi-channel biodegradable scaffold platform',
    '{"observation_tracker_ids": ["M2B-O058"], "source_experiment": {"chronicity_dpi_wpi": "Post-implant interval UNKNOWN", "control_type": "Scaffold architecture/cell/molecule comparison", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P010-E002", "figure_ref": "Abstract", "injury_device": "Experimental SCI", "injury_model": "SCI", "injury_severity": "UNKNOWN", "intervention_type": "Multi-channel biodegradable scaffold platform", "methods_summary": "The scaffold was framed as a platform to test architecture, transplanted cells, and local molecular agents for axon regeneration.", "paper_id": "M2A-P010", "sex": "UNKNOWN", "species": "Rodent SCI model context", "strain": "UNKNOWN", "vertebral_level": "UNKNOWN"}, "source_experiment_tracker_id": "M2A-P010-E002", "source_paper_tracker_id": "M2A-P010", "tracker_key": "M2A-P010::M2A-P010-E002"}'
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
    'Neural progenitor cells and Schwann cells were cultured within self-assembling peptide nanofiber scaffold and transplanted into rat transected dorsal column injury.',
    'Injury/graft comparison',
    'SAPNS + neural progenitor and Schwann cell graft',
    '{"observation_tracker_ids": ["M2B-O007"], "source_experiment": {"chronicity_dpi_wpi": "Post-transplant interval UNKNOWN", "control_type": "Injury/graft comparison", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P011-E001", "figure_ref": "Abstract", "injury_device": "Dorsal column transection", "injury_model": "Transected dorsal column SCI", "injury_severity": "Transection", "intervention_type": "SAPNS + neural progenitor and Schwann cell graft", "methods_summary": "Neural progenitor cells and Schwann cells were cultured within self-assembling peptide nanofiber scaffold and transplanted into rat transected dorsal column injury.", "paper_id": "M2A-P011", "sex": "UNKNOWN", "species": "Rattus norvegicus", "strain": "GFP-transgenic donor cells / rat host", "vertebral_level": "UNKNOWN"}, "source_experiment_tracker_id": "M2A-P011-E001", "source_paper_tracker_id": "M2A-P011", "tracker_key": "M2A-P011::M2A-P011-E001"}'
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
    'Host-cell migration, blood-vessel growth, and axonal ingrowth into SAPNS were assessed as evidence of a 3D permissive environment.',
    'Scaffold/graft histology comparison',
    'SAPNS lesion bridge',
    '{"observation_tracker_ids": ["M2B-O059"], "source_experiment": {"chronicity_dpi_wpi": "Post-transplant interval UNKNOWN", "control_type": "Scaffold/graft histology comparison", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P011-E002", "figure_ref": "Abstract", "injury_device": "Dorsal column transection", "injury_model": "Transected dorsal column SCI", "injury_severity": "Transection", "intervention_type": "SAPNS lesion bridge", "methods_summary": "Host-cell migration, blood-vessel growth, and axonal ingrowth into SAPNS were assessed as evidence of a 3D permissive environment.", "paper_id": "M2A-P011", "sex": "UNKNOWN", "species": "Rattus norvegicus", "strain": "UNKNOWN", "vertebral_level": "UNKNOWN"}, "source_experiment_tracker_id": "M2A-P011-E002", "source_paper_tracker_id": "M2A-P011", "tracker_key": "M2A-P011::M2A-P011-E002"}'
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
    'PLGA scaffolds with or without hMSCs were fitted into a 2-mm complete spinal cord defect.',
    'PLGA scaffold without hMSC',
    'PLGA scaffold + hMSC',
    '{"observation_tracker_ids": ["M2B-O009"], "source_experiment": {"chronicity_dpi_wpi": "Post-implant interval UNKNOWN", "control_type": "PLGA scaffold without hMSC", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P012-E001", "figure_ref": "Abstract", "injury_device": "Surgical complete transection/removal", "injury_model": "Complete transection SCI with 2-mm cord removal", "injury_severity": "Complete transection", "intervention_type": "PLGA scaffold + hMSC", "methods_summary": "PLGA scaffolds with or without hMSCs were fitted into a 2-mm complete spinal cord defect.", "paper_id": "M2A-P012", "sex": "UNKNOWN", "species": "Rattus norvegicus", "strain": "UNKNOWN", "vertebral_level": "T8-T9"}, "source_experiment_tracker_id": "M2A-P012-E001", "source_paper_tracker_id": "M2A-P012", "tracker_key": "M2A-P012::M2A-P012-E001"}'
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
    'Different hMSC doses were compared for BBB locomotor scores, MEP amplitudes, cell survival, differentiation, and neurological repair.',
    'Scaffold-only / hMSC dose groups',
    'hMSC-seeded PLGA scaffold',
    '{"observation_tracker_ids": ["M2B-O060"], "source_experiment": {"chronicity_dpi_wpi": "Post-implant interval UNKNOWN", "control_type": "Scaffold-only / hMSC dose groups", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P012-E002", "figure_ref": "Abstract", "injury_device": "Surgical complete transection/removal", "injury_model": "Complete transection SCI", "injury_severity": "Complete transection", "intervention_type": "hMSC-seeded PLGA scaffold", "methods_summary": "Different hMSC doses were compared for BBB locomotor scores, MEP amplitudes, cell survival, differentiation, and neurological repair.", "paper_id": "M2A-P012", "sex": "UNKNOWN", "species": "Rattus norvegicus", "strain": "UNKNOWN", "vertebral_level": "T8-T9"}, "source_experiment_tracker_id": "M2A-P012-E002", "source_paper_tracker_id": "M2A-P012", "tracker_key": "M2A-P012::M2A-P012-E002"}'
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
    'Adult NSPCs were placed in methacrylamide chitosan hydrogel and protected by a chitosan conduit to create a spinal cord bridge.',
    'Bridge/cue comparisons',
    'MAC hydrogel + chitosan conduit + NSPCs',
    '{"observation_tracker_ids": ["M2B-O032"], "source_experiment": {"chronicity_dpi_wpi": "Post-implant interval UNKNOWN", "control_type": "Bridge/cue comparisons", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P013-E001", "figure_ref": "Abstract", "injury_device": "Surgical hemisection", "injury_model": "Hemisection SCI", "injury_severity": "Hemisection", "intervention_type": "MAC hydrogel + chitosan conduit + NSPCs", "methods_summary": "Adult NSPCs were placed in methacrylamide chitosan hydrogel and protected by a chitosan conduit to create a spinal cord bridge.", "paper_id": "M2A-P013", "sex": "UNKNOWN", "species": "Rattus norvegicus", "strain": "UNKNOWN", "vertebral_level": "T8-T9 region"}, "source_experiment_tracker_id": "M2A-P013-E001", "source_paper_tracker_id": "M2A-P013", "tracker_key": "M2A-P013::M2A-P013-E001"}'
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
    'Biotin-tagged IFN-gamma and PDGF-AA were immobilized to MAC hydrogel to cue neuronal or oligodendrocytic lineages within the bridge.',
    'Uncued bridge comparison',
    'Immobilized IFN-gamma or PDGF-AA lineage cues',
    '{"observation_tracker_ids": ["M2B-O061"], "source_experiment": {"chronicity_dpi_wpi": "Post-implant interval UNKNOWN", "control_type": "Uncued bridge comparison", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P013-E002", "figure_ref": "Abstract", "injury_device": "Surgical hemisection", "injury_model": "Hemisection SCI", "injury_severity": "Hemisection", "intervention_type": "Immobilized IFN-gamma or PDGF-AA lineage cues", "methods_summary": "Biotin-tagged IFN-gamma and PDGF-AA were immobilized to MAC hydrogel to cue neuronal or oligodendrocytic lineages within the bridge.", "paper_id": "M2A-P013", "sex": "UNKNOWN", "species": "Rattus norvegicus / NSPC bridge", "strain": "UNKNOWN", "vertebral_level": "T8-T9 region"}, "source_experiment_tracker_id": "M2A-P013-E002", "source_paper_tracker_id": "M2A-P013", "tracker_key": "M2A-P013::M2A-P013-E002"}'
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
    1,
    'Abstract',
    'Tracker experiment M2A-P014-E001',
    'Decellularized porcine spinal cord or urinary bladder ECM hydrogels were injected into hemisection cavities and assessed over 2-8 weeks.',
    'Lesion/injection comparison',
    'Spinal cord ECM hydrogel or urinary bladder ECM hydrogel injection',
    '{"observation_tracker_ids": ["M2B-O015"], "source_experiment": {"chronicity_dpi_wpi": "2, 4, and 8 WPI", "control_type": "Lesion/injection comparison", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P014-E001", "figure_ref": "Abstract", "injury_device": "Hemisection cavity", "injury_model": "Acute hemisection SCI", "injury_severity": "Hemisection", "intervention_type": "Spinal cord ECM hydrogel or urinary bladder ECM hydrogel injection", "methods_summary": "Decellularized porcine spinal cord or urinary bladder ECM hydrogels were injected into hemisection cavities and assessed over 2-8 weeks.", "paper_id": "M2A-P014", "sex": "UNKNOWN", "species": "Rattus norvegicus", "strain": "UNKNOWN", "vertebral_level": "UNKNOWN"}, "source_experiment_tracker_id": "M2A-P014-E001", "source_paper_tracker_id": "M2A-P014", "tracker_key": "M2A-P014::M2A-P014-E001"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P014'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P014::M2A-P014-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract',
    'Tracker experiment M2A-P014-E002',
    'Histology and qPCR assessed scaffold integration, neovascularization, axonal ingrowth, tissue response, and macrophage-related limitations.',
    'ECM source comparison',
    'Injectable ECM hydrogel lesion scaffold',
    '{"observation_tracker_ids": ["M2B-O062"], "source_experiment": {"chronicity_dpi_wpi": "2, 4, and 8 WPI", "control_type": "ECM source comparison", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P014-E002", "figure_ref": "Abstract", "injury_device": "Hemisection cavity", "injury_model": "Acute hemisection SCI", "injury_severity": "Hemisection", "intervention_type": "Injectable ECM hydrogel lesion scaffold", "methods_summary": "Histology and qPCR assessed scaffold integration, neovascularization, axonal ingrowth, tissue response, and macrophage-related limitations.", "paper_id": "M2A-P014", "sex": "UNKNOWN", "species": "Rattus norvegicus", "strain": "UNKNOWN", "vertebral_level": "UNKNOWN"}, "source_experiment_tracker_id": "M2A-P014-E002", "source_paper_tracker_id": "M2A-P014", "tracker_key": "M2A-P014::M2A-P014-E002"}'
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
    'Abstract',
    'Tracker experiment M2A-P015-E001',
    'Dogs underwent complete T8 transection, delayed scar removal, and implantation of hUC-MSC-loaded NeuroRegen scaffold into the chronic lesion.',
    'Chronic scar resection baseline/control',
    'NeuroRegen scaffold + hUC-MSC implantation',
    '{"observation_tracker_ids": ["M2B-O018"], "source_experiment": {"chronicity_dpi_wpi": "2 months post-injury scar removal", "control_type": "Chronic scar resection baseline/control", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P015-E001", "figure_ref": "Abstract", "injury_device": "Complete T8 spinal cord segment removal + scar resection", "injury_model": "Chronic complete SCI", "injury_severity": "Complete transection", "intervention_type": "NeuroRegen scaffold + hUC-MSC implantation", "methods_summary": "Dogs underwent complete T8 transection, delayed scar removal, and implantation of hUC-MSC-loaded NeuroRegen scaffold into the chronic lesion.", "paper_id": "M2A-P015", "sex": "UNKNOWN", "species": "Canis familiaris", "strain": "UNKNOWN", "vertebral_level": "T8"}, "source_experiment_tracker_id": "M2A-P015-E001", "source_paper_tracker_id": "M2A-P015", "tracker_key": "M2A-P015::M2A-P015-E001"}'
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
    'Abstract',
    'Tracker experiment M2A-P015-E002',
    'Locomotor recovery, endogenous neurogenesis, and scar response were assessed after functionalized NeuroRegen implantation.',
    'Scaffold/cell comparison',
    'Functionalized NeuroRegen scaffold',
    '{"observation_tracker_ids": ["M2B-O063"], "source_experiment": {"chronicity_dpi_wpi": "Chronic 2-month post-injury implantation", "control_type": "Scaffold/cell comparison", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P015-E002", "figure_ref": "Abstract", "injury_device": "Complete transection + scaffold/cell implantation", "injury_model": "Chronic complete SCI", "injury_severity": "Complete transection", "intervention_type": "Functionalized NeuroRegen scaffold", "methods_summary": "Locomotor recovery, endogenous neurogenesis, and scar response were assessed after functionalized NeuroRegen implantation.", "paper_id": "M2A-P015", "sex": "UNKNOWN", "species": "Canis familiaris", "strain": "UNKNOWN", "vertebral_level": "T8"}, "source_experiment_tracker_id": "M2A-P015-E002", "source_paper_tracker_id": "M2A-P015", "tracker_key": "M2A-P015::M2A-P015-E002"}'
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
    'Abstract',
    'Tracker experiment M2A-P016-E001',
    'Schwann cells were transplanted in acellular injectable peripheral nerve matrix into contusion lesions and compared with Matrigel and injury-only controls.',
    'Injury-only and Matrigel graft comparisons',
    'Schwann cells in injectable decellularized peripheral nerve matrix',
    '{"observation_tracker_ids": ["M2B-O010"], "source_experiment": {"chronicity_dpi_wpi": "Post-implant interval UNKNOWN", "control_type": "Injury-only and Matrigel graft comparisons", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P016-E001", "figure_ref": "Abstract", "injury_device": "Contusion", "injury_model": "Contusion SCI", "injury_severity": "Contusion", "intervention_type": "Schwann cells in injectable decellularized peripheral nerve matrix", "methods_summary": "Schwann cells were transplanted in acellular injectable peripheral nerve matrix into contusion lesions and compared with Matrigel and injury-only controls.", "paper_id": "M2A-P016", "sex": "UNKNOWN", "species": "Rattus norvegicus", "strain": "UNKNOWN", "vertebral_level": "UNKNOWN"}, "source_experiment_tracker_id": "M2A-P016-E001", "source_paper_tracker_id": "M2A-P016", "tracker_key": "M2A-P016::M2A-P016-E001"}'
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
    'Abstract',
    'Tracker experiment M2A-P016-E002',
    'Implant size, immune infiltration, Schwann-cell myelinated axons, axon growth, and BBB locomotor performance were assessed.',
    'SC/Matrigel comparison',
    'SC/iPN matrix graft',
    '{"observation_tracker_ids": ["M2B-O064"], "source_experiment": {"chronicity_dpi_wpi": "Post-implant interval UNKNOWN", "control_type": "SC/Matrigel comparison", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P016-E002", "figure_ref": "Abstract", "injury_device": "Contusion", "injury_model": "Contusion SCI", "injury_severity": "Contusion", "intervention_type": "SC/iPN matrix graft", "methods_summary": "Implant size, immune infiltration, Schwann-cell myelinated axons, axon growth, and BBB locomotor performance were assessed.", "paper_id": "M2A-P016", "sex": "UNKNOWN", "species": "Rattus norvegicus", "strain": "UNKNOWN", "vertebral_level": "UNKNOWN"}, "source_experiment_tracker_id": "M2A-P016-E002", "source_paper_tracker_id": "M2A-P016", "tracker_key": "M2A-P016::M2A-P016-E002"}'
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
    'Abstract',
    'Tracker experiment M2A-P017-E001',
    'Two acute complete SCI patients received NeuroRegen scaffold plus MSC transplantation and were followed for adverse events and neurological/electrophysiological change.',
    'Preoperative baseline / safety monitoring',
    'NeuroRegen scaffold + MSC implantation',
    '{"observation_tracker_ids": ["M2B-O022"], "source_experiment": {"chronicity_dpi_wpi": "1-year follow-up", "control_type": "Preoperative baseline / safety monitoring", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P017-E001", "figure_ref": "Abstract", "injury_device": "Clinical traumatic SCI + scaffold implantation", "injury_model": "Acute complete SCI", "injury_severity": "Complete injury by ASIA/MRI/electrophysiology", "intervention_type": "NeuroRegen scaffold + MSC implantation", "methods_summary": "Two acute complete SCI patients received NeuroRegen scaffold plus MSC transplantation and were followed for adverse events and neurological/electrophysiological change.", "paper_id": "M2A-P017", "sex": "UNKNOWN", "species": "Homo sapiens", "strain": "N/A", "vertebral_level": "T11 and C4"}, "source_experiment_tracker_id": "M2A-P017-E001", "source_paper_tracker_id": "M2A-P017", "tracker_key": "M2A-P017::M2A-P017-E001"}'
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
    'Human spinal cord-derived NSPCs or human brain-derived NSPCs were transplanted into complete transection SCI with aligned collagen scaffold support.',
    'hbNSPC/scaffold comparison',
    'hSC-NSPCs + aligned collagen sponge scaffold',
    '{"observation_tracker_ids": ["M2B-O025"], "source_experiment": {"chronicity_dpi_wpi": "Post-transplant interval UNKNOWN", "control_type": "hbNSPC/scaffold comparison", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P018-E001", "figure_ref": "Abstract", "injury_device": "Complete transection", "injury_model": "Complete transection SCI", "injury_severity": "Complete transection", "intervention_type": "hSC-NSPCs + aligned collagen sponge scaffold", "methods_summary": "Human spinal cord-derived NSPCs or human brain-derived NSPCs were transplanted into complete transection SCI with aligned collagen scaffold support.", "paper_id": "M2A-P018", "sex": "UNKNOWN", "species": "Rattus norvegicus", "strain": "UNKNOWN", "vertebral_level": "UNKNOWN"}, "source_experiment_tracker_id": "M2A-P018-E001", "source_paper_tracker_id": "M2A-P018", "tracker_key": "M2A-P018::M2A-P018-E001"}'
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
    'Outcomes addressed cell retention, axonal guidance, neuronal regeneration microenvironment, and functional recovery according to abstract.',
    'Cell-source/scaffold comparison',
    'Aligned collagen scaffold-guided NSPC repair',
    '{"observation_tracker_ids": ["M2B-O065"], "source_experiment": {"chronicity_dpi_wpi": "Post-transplant interval UNKNOWN", "control_type": "Cell-source/scaffold comparison", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P018-E002", "figure_ref": "Abstract", "injury_device": "Complete transection", "injury_model": "Complete transection SCI", "injury_severity": "Complete transection", "intervention_type": "Aligned collagen scaffold-guided NSPC repair", "methods_summary": "Outcomes addressed cell retention, axonal guidance, neuronal regeneration microenvironment, and functional recovery according to abstract.", "paper_id": "M2A-P018", "sex": "UNKNOWN", "species": "Rattus norvegicus", "strain": "UNKNOWN", "vertebral_level": "UNKNOWN"}, "source_experiment_tracker_id": "M2A-P018-E002", "source_paper_tracker_id": "M2A-P018", "tracker_key": "M2A-P018::M2A-P018-E002"}'
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
    'AFG/fSAP composite hydrogel was constructed to present interpenetrating biophysical and biochemical cues.',
    'Single-cue scaffold logic',
    'Aligned fibrin hydrogel + functionalized self-assembling peptide composite',
    '{"observation_tracker_ids": ["M2B-O048"], "source_experiment": {"chronicity_dpi_wpi": "N/A", "control_type": "Single-cue scaffold logic", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P019-E001", "figure_ref": "Abstract", "injury_device": "Hydrogel fabrication", "injury_model": "SCI repair scaffold design", "injury_severity": "N/A", "intervention_type": "Aligned fibrin hydrogel + functionalized self-assembling peptide composite", "methods_summary": "AFG/fSAP composite hydrogel was constructed to present interpenetrating biophysical and biochemical cues.", "paper_id": "M2A-P019", "sex": "N/A", "species": "Scaffold system / rodent SCI context", "strain": "N/A", "vertebral_level": "N/A"}, "source_experiment_tracker_id": "M2A-P019-E001", "source_paper_tracker_id": "M2A-P019", "tracker_key": "M2A-P019::M2A-P019-E001"}'
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
    'Regeneration outcomes were assessed to test whether combined guidance and biochemical cues improved spinal cord repair.',
    'Single-cue / scaffold comparisons',
    'Multimodal composite hydrogel',
    '{"observation_tracker_ids": ["M2B-O066"], "source_experiment": {"chronicity_dpi_wpi": "Post-implant interval UNKNOWN", "control_type": "Single-cue / scaffold comparisons", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P019-E002", "figure_ref": "Abstract", "injury_device": "Experimental SCI", "injury_model": "SCI", "injury_severity": "UNKNOWN", "intervention_type": "Multimodal composite hydrogel", "methods_summary": "Regeneration outcomes were assessed to test whether combined guidance and biochemical cues improved spinal cord repair.", "paper_id": "M2A-P019", "sex": "UNKNOWN", "species": "Rodent model context", "strain": "UNKNOWN", "vertebral_level": "UNKNOWN"}, "source_experiment_tracker_id": "M2A-P019-E002", "source_paper_tracker_id": "M2A-P019", "tracker_key": "M2A-P019::M2A-P019-E002"}'
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
    'Decellularized spinal cord matrix-gel and GelMA were combined and assessed for water retention, wettability, degradation, soft mechanics, bioactivity, and microstructure.',
    'Material characterization',
    'dSCM/GelMA composite scaffold',
    '{"observation_tracker_ids": ["M2B-O033", "M2B-O044"], "source_experiment": {"chronicity_dpi_wpi": "N/A", "control_type": "Material characterization", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P020-E001", "figure_ref": "Abstract", "injury_device": "dSCM/GelMA fabrication", "injury_model": "SCI repair scaffold design", "injury_severity": "N/A", "intervention_type": "dSCM/GelMA composite scaffold", "methods_summary": "Decellularized spinal cord matrix-gel and GelMA were combined and assessed for water retention, wettability, degradation, soft mechanics, bioactivity, and microstructure.", "paper_id": "M2A-P020", "sex": "N/A", "species": "Scaffold system / rat SCI context", "strain": "N/A", "vertebral_level": "N/A"}, "source_experiment_tracker_id": "M2A-P020-E001", "source_paper_tracker_id": "M2A-P020", "tracker_key": "M2A-P020::M2A-P020-E001"}'
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
    'In vitro and in vivo experiments evaluated whether the composite scaffold supported human menstrual blood-derived stem cells and improved functional reconstruction after SCI.',
    'Scaffold/cell comparison',
    'dSCM/GelMA scaffold + MenSC',
    '{"observation_tracker_ids": ["M2B-O067"], "source_experiment": {"chronicity_dpi_wpi": "Post-implant interval UNKNOWN", "control_type": "Scaffold/cell comparison", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P020-E002", "figure_ref": "Abstract", "injury_device": "Experimental SCI", "injury_model": "SCI", "injury_severity": "UNKNOWN", "intervention_type": "dSCM/GelMA scaffold + MenSC", "methods_summary": "In vitro and in vivo experiments evaluated whether the composite scaffold supported human menstrual blood-derived stem cells and improved functional reconstruction after SCI.", "paper_id": "M2A-P020", "sex": "UNKNOWN", "species": "Rattus norvegicus", "strain": "UNKNOWN", "vertebral_level": "UNKNOWN"}, "source_experiment_tracker_id": "M2A-P020-E002", "source_paper_tracker_id": "M2A-P020", "tracker_key": "M2A-P020::M2A-P020-E002"}'
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
    'A 100-Gauss external magnetic field during polymerization aligned peptide hydrogel fibers, including in the presence of cells.',
    'Unaligned hydrogel comparison',
    'Magnetically responsive self-assembling peptide hydrogel',
    '{"observation_tracker_ids": ["M2B-O026"], "source_experiment": {"chronicity_dpi_wpi": "In vitro", "control_type": "Unaligned hydrogel comparison", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P021-E001", "figure_ref": "Abstract", "injury_device": "Magnetic hydrogel alignment", "injury_model": "Axon-infiltration model", "injury_severity": "N/A", "intervention_type": "Magnetically responsive self-assembling peptide hydrogel", "methods_summary": "A 100-Gauss external magnetic field during polymerization aligned peptide hydrogel fibers, including in the presence of cells.", "paper_id": "M2A-P021", "sex": "N/A", "species": "In vitro scaffold/NPC system", "strain": "NPC culture", "vertebral_level": "N/A"}, "source_experiment_tracker_id": "M2A-P021-E001", "source_paper_tracker_id": "M2A-P021", "tracker_key": "M2A-P021::M2A-P021-E001"}'
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
    'In vivo validation assessed whether aligned injectable hydrogel promoted and oriented axon infiltration at the SCI site.',
    'Unaligned/injury comparison',
    'Injectable aligned peptide hydrogel scaffold',
    '{"observation_tracker_ids": ["M2B-O068"], "source_experiment": {"chronicity_dpi_wpi": "Post-implant interval UNKNOWN", "control_type": "Unaligned/injury comparison", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P021-E002", "figure_ref": "Abstract", "injury_device": "Experimental SCI", "injury_model": "SCI", "injury_severity": "UNKNOWN", "intervention_type": "Injectable aligned peptide hydrogel scaffold", "methods_summary": "In vivo validation assessed whether aligned injectable hydrogel promoted and oriented axon infiltration at the SCI site.", "paper_id": "M2A-P021", "sex": "UNKNOWN", "species": "Rat SCI model context", "strain": "UNKNOWN", "vertebral_level": "UNKNOWN"}, "source_experiment_tracker_id": "M2A-P021-E002", "source_paper_tracker_id": "M2A-P021", "tracker_key": "M2A-P021::M2A-P021-E002"}'
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
    'Hyaluronic-acid hydrogel, decellularized brain matrix, PDRN, primed MSC EVs, and NPCs were combined into a multimodal scaffold.',
    'Component comparison',
    'DBM/PDRN/TI-EV/NPC@Gel composite scaffold',
    '{"observation_tracker_ids": ["M2B-O034", "M2B-O045"], "source_experiment": {"chronicity_dpi_wpi": "N/A", "control_type": "Component comparison", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P022-E001", "figure_ref": "Abstract", "injury_device": "Hydrogel fabrication", "injury_model": "SCI repair scaffold design", "injury_severity": "N/A", "intervention_type": "DBM/PDRN/TI-EV/NPC@Gel composite scaffold", "methods_summary": "Hyaluronic-acid hydrogel, decellularized brain matrix, PDRN, primed MSC EVs, and NPCs were combined into a multimodal scaffold.", "paper_id": "M2A-P022", "sex": "N/A", "species": "Scaffold system / rat SCI context", "strain": "N/A", "vertebral_level": "N/A"}, "source_experiment_tracker_id": "M2A-P022-E001", "source_paper_tracker_id": "M2A-P022", "tracker_key": "M2A-P022::M2A-P022-E001"}'
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
    'Rat SCI testing assessed angiogenesis, anti-inflammatory and anti-apoptotic effects, neural differentiation, regeneration, and functional recovery.',
    'Component/scaffold comparison',
    'Bioactive multimodal hydrogel',
    '{"observation_tracker_ids": ["M2B-O069"], "source_experiment": {"chronicity_dpi_wpi": "Post-implant interval UNKNOWN", "control_type": "Component/scaffold comparison", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P022-E002", "figure_ref": "Abstract", "injury_device": "Experimental SCI", "injury_model": "SCI", "injury_severity": "UNKNOWN", "intervention_type": "Bioactive multimodal hydrogel", "methods_summary": "Rat SCI testing assessed angiogenesis, anti-inflammatory and anti-apoptotic effects, neural differentiation, regeneration, and functional recovery.", "paper_id": "M2A-P022", "sex": "UNKNOWN", "species": "Rattus norvegicus", "strain": "UNKNOWN", "vertebral_level": "UNKNOWN"}, "source_experiment_tracker_id": "M2A-P022-E002", "source_paper_tracker_id": "M2A-P022", "tracker_key": "M2A-P022::M2A-P022-E002"}'
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
    'Curcumin-loaded PLGA nanoparticles were characterized and encapsulated in gelatin/alginate hydrogel scaffolds seeded with human endometrial stem cells.',
    'Material/cell characterization',
    'Gelatin/alginate hydrogel + hEnSC + curcumin-loaded PLGA nanoparticles',
    '{"observation_tracker_ids": ["M2B-O035"], "source_experiment": {"chronicity_dpi_wpi": "N/A", "control_type": "Material/cell characterization", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P023-E001", "figure_ref": "Abstract", "injury_device": "Hydrogel and nanoparticle fabrication", "injury_model": "SCI repair scaffold design", "injury_severity": "N/A", "intervention_type": "Gelatin/alginate hydrogel + hEnSC + curcumin-loaded PLGA nanoparticles", "methods_summary": "Curcumin-loaded PLGA nanoparticles were characterized and encapsulated in gelatin/alginate hydrogel scaffolds seeded with human endometrial stem cells.", "paper_id": "M2A-P023", "sex": "N/A", "species": "Scaffold system / rat SCI context", "strain": "N/A", "vertebral_level": "N/A"}, "source_experiment_tracker_id": "M2A-P023-E001", "source_paper_tracker_id": "M2A-P023", "tracker_key": "M2A-P023::M2A-P023-E001"}'
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
    'In vivo rat SCI experiments evaluated regeneration and anti-inflammatory repair effects of the combined scaffold strategy.',
    'Scaffold/cell/drug comparison',
    'hEnSC and curcumin-PLGA hydrogel scaffold',
    '{"observation_tracker_ids": ["M2B-O070"], "source_experiment": {"chronicity_dpi_wpi": "Post-implant interval UNKNOWN", "control_type": "Scaffold/cell/drug comparison", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P023-E002", "figure_ref": "Abstract", "injury_device": "Experimental SCI", "injury_model": "SCI", "injury_severity": "UNKNOWN", "intervention_type": "hEnSC and curcumin-PLGA hydrogel scaffold", "methods_summary": "In vivo rat SCI experiments evaluated regeneration and anti-inflammatory repair effects of the combined scaffold strategy.", "paper_id": "M2A-P023", "sex": "UNKNOWN", "species": "Rattus norvegicus", "strain": "UNKNOWN", "vertebral_level": "UNKNOWN"}, "source_experiment_tracker_id": "M2A-P023-E002", "source_paper_tracker_id": "M2A-P023", "tracker_key": "M2A-P023::M2A-P023-E002"}'
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
    'Abstract',
    'Tracker experiment M2A-P024-E001',
    'SEM and neural-marker analyses assessed hAEC attachment, distribution, and neural differentiation on the conductive scaffold.',
    'Scaffold/cue comparison',
    'Noggin-loaded nanochitosan/polypyrrole-alginate conductive scaffold + hAEC',
    '{"observation_tracker_ids": ["M2B-O036"], "source_experiment": {"chronicity_dpi_wpi": "In vitro", "control_type": "Scaffold/cue comparison", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P024-E001", "figure_ref": "Abstract", "injury_device": "Conductive scaffold fabrication", "injury_model": "In vitro scaffold-cell differentiation model", "injury_severity": "N/A", "intervention_type": "Noggin-loaded nanochitosan/polypyrrole-alginate conductive scaffold + hAEC", "methods_summary": "SEM and neural-marker analyses assessed hAEC attachment, distribution, and neural differentiation on the conductive scaffold.", "paper_id": "M2A-P024", "sex": "N/A", "species": "hAEC culture / scaffold system", "strain": "Human amniotic epithelial cells", "vertebral_level": "N/A"}, "source_experiment_tracker_id": "M2A-P024-E001", "source_paper_tracker_id": "M2A-P024", "tracker_key": "M2A-P024::M2A-P024-E001"}'
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
    'Abstract',
    'Tracker experiment M2A-P024-E002',
    'Animal-model testing assessed repair potential of hAECs on Noggin-loaded conductive nanochitosan/polypyrrole-alginate scaffold.',
    'Scaffold/cell comparison',
    'hAEC-loaded conductive chitosan scaffold',
    '{"observation_tracker_ids": ["M2B-O071"], "source_experiment": {"chronicity_dpi_wpi": "Post-implant interval UNKNOWN", "control_type": "Scaffold/cell comparison", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P024-E002", "figure_ref": "Abstract", "injury_device": "Experimental SCI", "injury_model": "SCI", "injury_severity": "UNKNOWN", "intervention_type": "hAEC-loaded conductive chitosan scaffold", "methods_summary": "Animal-model testing assessed repair potential of hAECs on Noggin-loaded conductive nanochitosan/polypyrrole-alginate scaffold.", "paper_id": "M2A-P024", "sex": "UNKNOWN", "species": "Animal SCI model context", "strain": "UNKNOWN", "vertebral_level": "UNKNOWN"}, "source_experiment_tracker_id": "M2A-P024-E002", "source_paper_tracker_id": "M2A-P024", "tracker_key": "M2A-P024::M2A-P024-E002"}'
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
    'Abstract',
    'Tracker experiment M2A-P025-E001',
    'Fibrin scaffolds containing a controlled NT-3 delivery system were implanted in adult rat spinal cord lesions to assess short-term fiber sprouting.',
    'Saline / control scaffold',
    'Fibrin scaffold + controlled NT-3 delivery',
    '{"observation_tracker_ids": ["M2B-O012"], "source_experiment": {"chronicity_dpi_wpi": "Immediate implantation; 9-day histology", "control_type": "Saline / control scaffold", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P025-E001", "figure_ref": "Abstract", "injury_device": "Surgical ablation", "injury_model": "2-mm spinal cord ablation lesion", "injury_severity": "2-mm ablation injury", "intervention_type": "Fibrin scaffold + controlled NT-3 delivery", "methods_summary": "Fibrin scaffolds containing a controlled NT-3 delivery system were implanted in adult rat spinal cord lesions to assess short-term fiber sprouting.", "paper_id": "M2A-P025", "sex": "UNKNOWN", "species": "Rattus norvegicus", "strain": "Adult rats", "vertebral_level": "UNKNOWN"}, "source_experiment_tracker_id": "M2A-P025-E001", "source_paper_tracker_id": "M2A-P025", "tracker_key": "M2A-P025::M2A-P025-E001"}'
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
    'Abstract',
    'Tracker experiment M2A-P025-E002',
    'Neuronal fiber growth, glial scar formation, and hindlimb motor function were compared across NT-3 scaffold, control scaffold, and saline groups.',
    'NT-3 scaffold vs control scaffold/saline',
    'Fibrin/NT-3 scaffold',
    '{"observation_tracker_ids": ["M2B-O072"], "source_experiment": {"chronicity_dpi_wpi": "9 days and functional follow-up UNKNOWN", "control_type": "NT-3 scaffold vs control scaffold/saline", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P025-E002", "figure_ref": "Abstract", "injury_device": "Surgical ablation", "injury_model": "2-mm spinal cord ablation lesion", "injury_severity": "2-mm ablation injury", "intervention_type": "Fibrin/NT-3 scaffold", "methods_summary": "Neuronal fiber growth, glial scar formation, and hindlimb motor function were compared across NT-3 scaffold, control scaffold, and saline groups.", "paper_id": "M2A-P025", "sex": "UNKNOWN", "species": "Rattus norvegicus", "strain": "Adult rats", "vertebral_level": "UNKNOWN"}, "source_experiment_tracker_id": "M2A-P025-E002", "source_paper_tracker_id": "M2A-P025", "tracker_key": "M2A-P025::M2A-P025-E002"}'
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
    'Abstract',
    'Tracker experiment M2A-P026-E001',
    'Rats underwent T9 complete transection followed by delayed implantation of bFGF-incorporated hydrogel surrounded by acellular vascular matrix.',
    'Transection/scaffold comparison',
    'bFGF/HEMA-MOETACL hydrogel + acellular vascular matrix',
    '{"observation_tracker_ids": ["M2B-O038"], "source_experiment": {"chronicity_dpi_wpi": "Implantation 5 DPI; 8-week outcome", "control_type": "Transection/scaffold comparison", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P026-E001", "figure_ref": "Abstract", "injury_device": "T9 complete transection", "injury_model": "Complete transection SCI", "injury_severity": "Complete transection", "intervention_type": "bFGF/HEMA-MOETACL hydrogel + acellular vascular matrix", "methods_summary": "Rats underwent T9 complete transection followed by delayed implantation of bFGF-incorporated hydrogel surrounded by acellular vascular matrix.", "paper_id": "M2A-P026", "sex": "UNKNOWN", "species": "Rattus norvegicus", "strain": "Sprague-Dawley", "vertebral_level": "T9"}, "source_experiment_tracker_id": "M2A-P026-E001", "source_paper_tracker_id": "M2A-P026", "tracker_key": "M2A-P026::M2A-P026-E001"}'
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
    'Abstract',
    'Tracker experiment M2A-P026-E002',
    'Tissue ingrowth, nerve regeneration, and functional recovery were assessed after hydrogel implantation.',
    'Hydrogel/control comparison',
    'bFGF hydrogel scaffold',
    '{"observation_tracker_ids": ["M2B-O073"], "source_experiment": {"chronicity_dpi_wpi": "8 WPI", "control_type": "Hydrogel/control comparison", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P026-E002", "figure_ref": "Abstract", "injury_device": "T9 complete transection", "injury_model": "Complete transection SCI", "injury_severity": "Complete transection", "intervention_type": "bFGF hydrogel scaffold", "methods_summary": "Tissue ingrowth, nerve regeneration, and functional recovery were assessed after hydrogel implantation.", "paper_id": "M2A-P026", "sex": "UNKNOWN", "species": "Rattus norvegicus", "strain": "Sprague-Dawley", "vertebral_level": "T9"}, "source_experiment_tracker_id": "M2A-P026-E002", "source_paper_tracker_id": "M2A-P026", "tracker_key": "M2A-P026::M2A-P026-E002"}'
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
    'Longitudinal multi-tubular HA scaffold was combined with anti-NgR and PLGA microspheres containing BDNF and VEGF.',
    'Material/cargo comparison',
    'Structured HA hydrogel + anti-NgR + BDNF/VEGF PLGA microspheres',
    '{"observation_tracker_ids": ["M2B-O013"], "source_experiment": {"chronicity_dpi_wpi": "N/A", "control_type": "Material/cargo comparison", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P027-E001", "figure_ref": "Abstract", "injury_device": "HA scaffold fabrication", "injury_model": "SCI repair scaffold design", "injury_severity": "N/A", "intervention_type": "Structured HA hydrogel + anti-NgR + BDNF/VEGF PLGA microspheres", "methods_summary": "Longitudinal multi-tubular HA scaffold was combined with anti-NgR and PLGA microspheres containing BDNF and VEGF.", "paper_id": "M2A-P027", "sex": "N/A", "species": "Scaffold system / rat SCI context", "strain": "N/A", "vertebral_level": "N/A"}, "source_experiment_tracker_id": "M2A-P027-E001", "source_paper_tracker_id": "M2A-P027", "tracker_key": "M2A-P027::M2A-P027-E001"}'
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
    'Host integration, inflammation, gliosis, vascularization, regenerated nerve fibers, and locomotor recovery were assessed after implantation.',
    'Injury/scaffold comparison',
    'HA+PLGA multi-cargo scaffold',
    '{"observation_tracker_ids": ["M2B-O074"], "source_experiment": {"chronicity_dpi_wpi": "Post-implant interval UNKNOWN", "control_type": "Injury/scaffold comparison", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P027-E002", "figure_ref": "Abstract", "injury_device": "Dorsal hemisection", "injury_model": "Dorsal hemisection SCI", "injury_severity": "Hemisection", "intervention_type": "HA+PLGA multi-cargo scaffold", "methods_summary": "Host integration, inflammation, gliosis, vascularization, regenerated nerve fibers, and locomotor recovery were assessed after implantation.", "paper_id": "M2A-P027", "sex": "UNKNOWN", "species": "Rattus norvegicus", "strain": "UNKNOWN", "vertebral_level": "T9-T10"}, "source_experiment_tracker_id": "M2A-P027-E002", "source_paper_tracker_id": "M2A-P027", "tracker_key": "M2A-P027::M2A-P027-E002"}'
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
    'Hydrogel-only and NT-3-loaded in situ forming collagen hydrogel were delivered after rat hemisection SCI.',
    'Hydrogel-only / SCI comparison',
    'Injectable collagen hydrogel + NT-3',
    '{"observation_tracker_ids": ["M2B-O039"], "source_experiment": {"chronicity_dpi_wpi": "Immediate treatment; 1 and 6 WPI", "control_type": "Hydrogel-only / SCI comparison", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P028-E001", "figure_ref": "Abstract", "injury_device": "Hemisection", "injury_model": "Hemisection SCI", "injury_severity": "Hemisection", "intervention_type": "Injectable collagen hydrogel + NT-3", "methods_summary": "Hydrogel-only and NT-3-loaded in situ forming collagen hydrogel were delivered after rat hemisection SCI.", "paper_id": "M2A-P028", "sex": "UNKNOWN", "species": "Rattus norvegicus", "strain": "UNKNOWN", "vertebral_level": "UNKNOWN"}, "source_experiment_tracker_id": "M2A-P028-E001", "source_paper_tracker_id": "M2A-P028", "tracker_key": "M2A-P028::M2A-P028-E001"}'
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
    'BBB locomotion, neuronal growth, glial scar formation, inflammation, and collagen deposition were assessed.',
    'NT-3 vs hydrogel-only comparison',
    'NT-3 collagen scaffold',
    '{"observation_tracker_ids": ["M2B-O075"], "source_experiment": {"chronicity_dpi_wpi": "1 and 6 WPI", "control_type": "NT-3 vs hydrogel-only comparison", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P028-E002", "figure_ref": "Abstract", "injury_device": "Hemisection", "injury_model": "Hemisection SCI", "injury_severity": "Hemisection", "intervention_type": "NT-3 collagen scaffold", "methods_summary": "BBB locomotion, neuronal growth, glial scar formation, inflammation, and collagen deposition were assessed.", "paper_id": "M2A-P028", "sex": "UNKNOWN", "species": "Rattus norvegicus", "strain": "UNKNOWN", "vertebral_level": "UNKNOWN"}, "source_experiment_tracker_id": "M2A-P028-E002", "source_paper_tracker_id": "M2A-P028", "tracker_key": "M2A-P028::M2A-P028-E002"}'
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
    'Porous biodegradable scaffolds were implanted after partial or complete thoracic lateral hemisection in non-human primates.',
    'Non-implanted control',
    'PLGA/poly-l-lysine porous scaffold',
    '{"observation_tracker_ids": ["M2B-O003"], "source_experiment": {"chronicity_dpi_wpi": "12 WPI", "control_type": "Non-implanted control", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P029-E001", "figure_ref": "Abstract", "injury_device": "Thoracic lateral hemisection", "injury_model": "Partial or complete lateral hemisection SCI", "injury_severity": "Partial/complete hemisection", "intervention_type": "PLGA/poly-l-lysine porous scaffold", "methods_summary": "Porous biodegradable scaffolds were implanted after partial or complete thoracic lateral hemisection in non-human primates.", "paper_id": "M2A-P029", "sex": "UNKNOWN", "species": "Chlorocebus sabaeus", "strain": "Old-World primate", "vertebral_level": "Thoracic"}, "source_experiment_tracker_id": "M2A-P029-E001", "source_paper_tracker_id": "M2A-P029", "tracker_key": "M2A-P029::M2A-P029-E001"}'
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
    'Locomotor kinematics, muscle activity, appositional healing, and spinal cord tissue remodeling were compared.',
    'Scaffold vs non-implanted control',
    'Porous biodegradable scaffold',
    '{"observation_tracker_ids": ["M2B-O076"], "source_experiment": {"chronicity_dpi_wpi": "12 WPI", "control_type": "Scaffold vs non-implanted control", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P029-E002", "figure_ref": "Abstract", "injury_device": "Thoracic lateral hemisection", "injury_model": "Thoracic hemisection SCI", "injury_severity": "Complete hemisection subgroup emphasized", "intervention_type": "Porous biodegradable scaffold", "methods_summary": "Locomotor kinematics, muscle activity, appositional healing, and spinal cord tissue remodeling were compared.", "paper_id": "M2A-P029", "sex": "UNKNOWN", "species": "Chlorocebus sabaeus", "strain": "Old-World primate", "vertebral_level": "Thoracic"}, "source_experiment_tracker_id": "M2A-P029-E002", "source_paper_tracker_id": "M2A-P029", "tracker_key": "M2A-P029::M2A-P029-E002"}'
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
    1,
    'Abstract',
    'Tracker experiment M2A-P030-E001',
    'Porous gelatin sponge scaffold was modified with NT-3/fibroin complex and assessed for sustained release.',
    'Scaffold characterization',
    'NT-3/fibroin-modified gelatin sponge scaffold',
    '{"observation_tracker_ids": ["M2B-O040"], "source_experiment": {"chronicity_dpi_wpi": "In vitro release before implantation", "control_type": "Scaffold characterization", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P030-E001", "figure_ref": "Abstract", "injury_device": "Gelatin/fibroin scaffold fabrication", "injury_model": "SCI repair scaffold design", "injury_severity": "N/A", "intervention_type": "NT-3/fibroin-modified gelatin sponge scaffold", "methods_summary": "Porous gelatin sponge scaffold was modified with NT-3/fibroin complex and assessed for sustained release.", "paper_id": "M2A-P030", "sex": "N/A", "species": "Scaffold system / canine SCI context", "strain": "N/A", "vertebral_level": "N/A"}, "source_experiment_tracker_id": "M2A-P030-E001", "source_paper_tracker_id": "M2A-P030", "tracker_key": "M2A-P030::M2A-P030-E001"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P030'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P030::M2A-P030-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract',
    'Tracker experiment M2A-P030-E002',
    'Hindlimb movement, neural conduction, inflammation, new neurons, synaptic structures, vessels, and nerve fiber regeneration were assessed.',
    'Injury/scaffold comparison',
    'NT-3/fibroin gelatin scaffold',
    '{"observation_tracker_ids": ["M2B-O077"], "source_experiment": {"chronicity_dpi_wpi": "Post-implant interval UNKNOWN", "control_type": "Injury/scaffold comparison", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P030-E002", "figure_ref": "Abstract", "injury_device": "Hemisection", "injury_model": "Hemisection SCI", "injury_severity": "Hemisection", "intervention_type": "NT-3/fibroin gelatin scaffold", "methods_summary": "Hindlimb movement, neural conduction, inflammation, new neurons, synaptic structures, vessels, and nerve fiber regeneration were assessed.", "paper_id": "M2A-P030", "sex": "UNKNOWN", "species": "Canis familiaris", "strain": "UNKNOWN", "vertebral_level": "UNKNOWN"}, "source_experiment_tracker_id": "M2A-P030-E002", "source_paper_tracker_id": "M2A-P030", "tracker_key": "M2A-P030::M2A-P030-E002"}'
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
    'Polycaprolactone/polysialic acid hybrid nanofiber scaffold encapsulating methylprednisolone was developed.',
    'Material/drug characterization',
    'PCL/PSA/MP nanofiber scaffold',
    '{"observation_tracker_ids": ["M2B-O041"], "source_experiment": {"chronicity_dpi_wpi": "N/A", "control_type": "Material/drug characterization", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P031-E001", "figure_ref": "Abstract", "injury_device": "Nanofiber scaffold fabrication", "injury_model": "SCI repair scaffold design", "injury_severity": "N/A", "intervention_type": "PCL/PSA/MP nanofiber scaffold", "methods_summary": "Polycaprolactone/polysialic acid hybrid nanofiber scaffold encapsulating methylprednisolone was developed.", "paper_id": "M2A-P031", "sex": "N/A", "species": "Scaffold system / rat SCI context", "strain": "N/A", "vertebral_level": "N/A"}, "source_experiment_tracker_id": "M2A-P031-E001", "source_paper_tracker_id": "M2A-P031", "tracker_key": "M2A-P031::M2A-P031-E001"}'
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
    'Inflammation, microglia/macrophage activation, apoptosis, axonal regeneration, and functional recovery were assessed after transplantation into transection lesions.',
    'Scaffold/drug comparison',
    'PCL/PSA/MP nanofiber scaffold',
    '{"observation_tracker_ids": ["M2B-O078"], "source_experiment": {"chronicity_dpi_wpi": "Post-implant interval UNKNOWN", "control_type": "Scaffold/drug comparison", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P031-E002", "figure_ref": "Abstract", "injury_device": "Transection", "injury_model": "Transection SCI", "injury_severity": "Transection", "intervention_type": "PCL/PSA/MP nanofiber scaffold", "methods_summary": "Inflammation, microglia/macrophage activation, apoptosis, axonal regeneration, and functional recovery were assessed after transplantation into transection lesions.", "paper_id": "M2A-P031", "sex": "UNKNOWN", "species": "Rattus norvegicus", "strain": "UNKNOWN", "vertebral_level": "UNKNOWN"}, "source_experiment_tracker_id": "M2A-P031-E002", "source_paper_tracker_id": "M2A-P031", "tracker_key": "M2A-P031::M2A-P031-E002"}'
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
    'Abstract',
    'Tracker experiment M2A-P032-E001',
    'HA hydrogels containing protoplasmic or fibrous astrocyte-derived ECM, with or without V2a interneurons, were implanted after SCI.',
    'HA hydrogel component comparison',
    'HA hydrogel + astrocyte ECM and/or V2a interneurons',
    '{"observation_tracker_ids": ["M2B-O016"], "source_experiment": {"chronicity_dpi_wpi": "Post-implant interval UNKNOWN", "control_type": "HA hydrogel component comparison", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P032-E001", "figure_ref": "Abstract", "injury_device": "Experimental SCI", "injury_model": "SCI", "injury_severity": "UNKNOWN", "intervention_type": "HA hydrogel + astrocyte ECM and/or V2a interneurons", "methods_summary": "HA hydrogels containing protoplasmic or fibrous astrocyte-derived ECM, with or without V2a interneurons, were implanted after SCI.", "paper_id": "M2A-P032", "sex": "UNKNOWN", "species": "Rattus norvegicus", "strain": "UNKNOWN", "vertebral_level": "UNKNOWN"}, "source_experiment_tracker_id": "M2A-P032-E001", "source_paper_tracker_id": "M2A-P032", "tracker_key": "M2A-P032::M2A-P032-E001"}'
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
    'Abstract',
    'Tracker experiment M2A-P032-E002',
    'Glial scar size, axon penetration, and histological response were assessed, with protoplasmic astrocyte ECM showing favorable effects in the abstract.',
    'ECM subtype / cell comparison',
    'HA/astrocyte ECM hydrogel',
    '{"observation_tracker_ids": ["M2B-O079"], "source_experiment": {"chronicity_dpi_wpi": "Post-implant interval UNKNOWN", "control_type": "ECM subtype / cell comparison", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P032-E002", "figure_ref": "Abstract", "injury_device": "Experimental SCI", "injury_model": "SCI", "injury_severity": "UNKNOWN", "intervention_type": "HA/astrocyte ECM hydrogel", "methods_summary": "Glial scar size, axon penetration, and histological response were assessed, with protoplasmic astrocyte ECM showing favorable effects in the abstract.", "paper_id": "M2A-P032", "sex": "UNKNOWN", "species": "Rattus norvegicus", "strain": "UNKNOWN", "vertebral_level": "UNKNOWN"}, "source_experiment_tracker_id": "M2A-P032-E002", "source_paper_tracker_id": "M2A-P032", "tracker_key": "M2A-P032::M2A-P032-E002"}'
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
    'Abstract',
    'Tracker experiment M2A-P033-E001',
    'hUC-MSCs were adsorbed onto collagen scaffolds and implanted into rat and canine complete SCI models.',
    'Scaffold/cell comparison',
    'Collagen scaffold + hUC-MSC',
    '{"observation_tracker_ids": ["M2B-O023"], "source_experiment": {"chronicity_dpi_wpi": "1 week to 6 months", "control_type": "Scaffold/cell comparison", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P033-E001", "figure_ref": "Abstract", "injury_device": "Microsurgical complete transection", "injury_model": "Complete transection SCI", "injury_severity": "Complete SCI", "intervention_type": "Collagen scaffold + hUC-MSC", "methods_summary": "hUC-MSCs were adsorbed onto collagen scaffolds and implanted into rat and canine complete SCI models.", "paper_id": "M2A-P033", "sex": "UNKNOWN", "species": "Rat and canine", "strain": "UNKNOWN", "vertebral_level": "UNKNOWN"}, "source_experiment_tracker_id": "M2A-P033-E001", "source_paper_tracker_id": "M2A-P033", "tracker_key": "M2A-P033::M2A-P033-E001"}'
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
    'Abstract',
    'Tracker experiment M2A-P033-E002',
    'Phase I clinical testing evaluated safety and possible repair after collagen scaffold plus hUC-MSC transplantation.',
    'Phase I safety baseline',
    'Collagen scaffold + hUC-MSC',
    '{"observation_tracker_ids": ["M2B-O080"], "source_experiment": {"chronicity_dpi_wpi": "Clinical follow-up interval UNKNOWN", "control_type": "Phase I safety baseline", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P033-E002", "figure_ref": "Abstract", "injury_device": "Clinical acute complete SCI + implantation", "injury_model": "Acute complete SCI", "injury_severity": "Acute complete SCI", "intervention_type": "Collagen scaffold + hUC-MSC", "methods_summary": "Phase I clinical testing evaluated safety and possible repair after collagen scaffold plus hUC-MSC transplantation.", "paper_id": "M2A-P033", "sex": "UNKNOWN", "species": "Homo sapiens", "strain": "N/A", "vertebral_level": "UNKNOWN"}, "source_experiment_tracker_id": "M2A-P033-E002", "source_paper_tracker_id": "M2A-P033", "tracker_key": "M2A-P033::M2A-P033-E002"}'
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
    1,
    'Abstract',
    'Tracker experiment M2A-P034-E001',
    'In vitro and organotypic cultures assessed iNPC viability, neurite outgrowth, migration, and neuron-like morphology in the scaffold.',
    'Component comparison',
    'HA/PPY/RAD16/iNPC/curcumin scaffold',
    '{"observation_tracker_ids": ["M2B-O019"], "source_experiment": {"chronicity_dpi_wpi": "In vitro", "control_type": "Component comparison", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P034-E001", "figure_ref": "Abstract", "injury_device": "Surface-capping scaffold fabrication", "injury_model": "Scaffold/cell compatibility model", "injury_severity": "N/A", "intervention_type": "HA/PPY/RAD16/iNPC/curcumin scaffold", "methods_summary": "In vitro and organotypic cultures assessed iNPC viability, neurite outgrowth, migration, and neuron-like morphology in the scaffold.", "paper_id": "M2A-P034", "sex": "N/A", "species": "In vitro / organotypic SCI culture", "strain": "Human induced neural progenitor cells", "vertebral_level": "N/A"}, "source_experiment_tracker_id": "M2A-P034-E001", "source_paper_tracker_id": "M2A-P034", "tracker_key": "M2A-P034::M2A-P034-E001"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P034'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P034::M2A-P034-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract',
    'Tracker experiment M2A-P034-E002',
    'Surface-capping scaffold was applied after subacute SCI and assessed for repair-associated outcomes.',
    'Injury/scaffold comparison',
    'HA demilune surface-capping scaffold',
    '{"observation_tracker_ids": ["M2B-O081"], "source_experiment": {"chronicity_dpi_wpi": "Subacute treatment interval", "control_type": "Injury/scaffold comparison", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P034-E002", "figure_ref": "Abstract", "injury_device": "Experimental SCI", "injury_model": "Subacute SCI", "injury_severity": "Subacute SCI", "intervention_type": "HA demilune surface-capping scaffold", "methods_summary": "Surface-capping scaffold was applied after subacute SCI and assessed for repair-associated outcomes.", "paper_id": "M2A-P034", "sex": "UNKNOWN", "species": "Rat model context", "strain": "UNKNOWN", "vertebral_level": "UNKNOWN"}, "source_experiment_tracker_id": "M2A-P034-E002", "source_paper_tracker_id": "M2A-P034", "tracker_key": "M2A-P034::M2A-P034-E002"}'
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
    1,
    'Abstract',
    'Tracker experiment M2A-P035-E001',
    'hAECs were induced into neural-like cells and grown in 3D-printed GelMA biomimetic spinal cord microchannel scaffold.',
    'Induction/scaffold comparison',
    '3D-printed GelMA microchannel scaffold + hAEC-neural-like cells',
    '{"observation_tracker_ids": ["M2B-O027"], "source_experiment": {"chronicity_dpi_wpi": "In vitro", "control_type": "Induction/scaffold comparison", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P035-E001", "figure_ref": "Abstract", "injury_device": "GelMA scaffold fabrication", "injury_model": "In vitro scaffold-cell induction model", "injury_severity": "N/A", "intervention_type": "3D-printed GelMA microchannel scaffold + hAEC-neural-like cells", "methods_summary": "hAECs were induced into neural-like cells and grown in 3D-printed GelMA biomimetic spinal cord microchannel scaffold.", "paper_id": "M2A-P035", "sex": "N/A", "species": "hAEC culture / scaffold system", "strain": "Human amniotic epithelial cells", "vertebral_level": "N/A"}, "source_experiment_tracker_id": "M2A-P035-E001", "source_paper_tracker_id": "M2A-P035", "tracker_key": "M2A-P035::M2A-P035-E001"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P035'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P035::M2A-P035-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract',
    'Tracker experiment M2A-P035-E002',
    'hAEC-neural-like cell scaffold was implanted into rat full transection SCI to assess neural circuit and hindlimb recovery.',
    'Injury/scaffold/cell comparison',
    'GelMA scaffold + hAEC-derived neural-like cells',
    '{"observation_tracker_ids": ["M2B-O082"], "source_experiment": {"chronicity_dpi_wpi": "Post-implant interval UNKNOWN", "control_type": "Injury/scaffold/cell comparison", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P035-E002", "figure_ref": "Abstract", "injury_device": "Complete transection", "injury_model": "Full transection SCI", "injury_severity": "Full transection", "intervention_type": "GelMA scaffold + hAEC-derived neural-like cells", "methods_summary": "hAEC-neural-like cell scaffold was implanted into rat full transection SCI to assess neural circuit and hindlimb recovery.", "paper_id": "M2A-P035", "sex": "UNKNOWN", "species": "Rattus norvegicus", "strain": "UNKNOWN", "vertebral_level": "UNKNOWN"}, "source_experiment_tracker_id": "M2A-P035-E002", "source_paper_tracker_id": "M2A-P035", "tracker_key": "M2A-P035::M2A-P035-E002"}'
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
    'Abstract',
    'Tracker experiment M2A-P036-E001',
    'Dual-phase SilMA hydrogel was characterized for porosity, mechanics, stability, and sequential release behavior.',
    'Release/component comparison',
    'Dual-phase SilMA hydrogel + NT-3/Ang-(1-7) PLGA microspheres',
    '{"observation_tracker_ids": ["M2B-O014"], "source_experiment": {"chronicity_dpi_wpi": "In vitro characterization", "control_type": "Release/component comparison", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P036-E001", "figure_ref": "Abstract", "injury_device": "SilMA hydrogel fabrication", "injury_model": "SCI repair scaffold design", "injury_severity": "N/A", "intervention_type": "Dual-phase SilMA hydrogel + NT-3/Ang-(1-7) PLGA microspheres", "methods_summary": "Dual-phase SilMA hydrogel was characterized for porosity, mechanics, stability, and sequential release behavior.", "paper_id": "M2A-P036", "sex": "N/A", "species": "Scaffold system / rodent SCI context", "strain": "N/A", "vertebral_level": "N/A"}, "source_experiment_tracker_id": "M2A-P036-E001", "source_paper_tracker_id": "M2A-P036", "tracker_key": "M2A-P036::M2A-P036-E001"}'
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
    'Abstract',
    'Tracker experiment M2A-P036-E002',
    'In vitro and in vivo outcomes assessed inflammation reduction, neuronal differentiation, axonal regeneration, and spinal cord repair.',
    'Scaffold/drug comparison',
    'Sequential release SilMA scaffold',
    '{"observation_tracker_ids": ["M2B-O083"], "source_experiment": {"chronicity_dpi_wpi": "Post-implant interval UNKNOWN", "control_type": "Scaffold/drug comparison", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P036-E002", "figure_ref": "Abstract", "injury_device": "Experimental SCI", "injury_model": "SCI", "injury_severity": "UNKNOWN", "intervention_type": "Sequential release SilMA scaffold", "methods_summary": "In vitro and in vivo outcomes assessed inflammation reduction, neuronal differentiation, axonal regeneration, and spinal cord repair.", "paper_id": "M2A-P036", "sex": "UNKNOWN", "species": "Rodent model context", "strain": "UNKNOWN", "vertebral_level": "UNKNOWN"}, "source_experiment_tracker_id": "M2A-P036-E002", "source_paper_tracker_id": "M2A-P036", "tracker_key": "M2A-P036::M2A-P036-E002"}'
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
    'Coaxial 3D printing generated time-programmed scaffold layers carrying antioxidant, migration, and differentiation cues.',
    'Scaffold/cue comparison',
    'Hierarchical HA/alginate/gelatin-cellulose hydrogel scaffold',
    '{"observation_tracker_ids": ["M2B-O028"], "source_experiment": {"chronicity_dpi_wpi": "In vitro characterization", "control_type": "Scaffold/cue comparison", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P037-E001", "figure_ref": "Abstract", "injury_device": "Coaxial 3D printing", "injury_model": "SCI repair scaffold design", "injury_severity": "N/A", "intervention_type": "Hierarchical HA/alginate/gelatin-cellulose hydrogel scaffold", "methods_summary": "Coaxial 3D printing generated time-programmed scaffold layers carrying antioxidant, migration, and differentiation cues.", "paper_id": "M2A-P037", "sex": "N/A", "species": "Scaffold system / rodent SCI context", "strain": "N/A", "vertebral_level": "N/A"}, "source_experiment_tracker_id": "M2A-P037-E001", "source_paper_tracker_id": "M2A-P037", "tracker_key": "M2A-P037::M2A-P037-E001"}'
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
    'SCI testing evaluated oxidative stress control, endogenous NSC migration/differentiation, and repair.',
    'Scaffold/cue comparison',
    'On-demand hierarchical hydrogel scaffold',
    '{"observation_tracker_ids": ["M2B-O084"], "source_experiment": {"chronicity_dpi_wpi": "Post-implant interval UNKNOWN", "control_type": "Scaffold/cue comparison", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P037-E002", "figure_ref": "Abstract", "injury_device": "Experimental SCI", "injury_model": "SCI", "injury_severity": "UNKNOWN", "intervention_type": "On-demand hierarchical hydrogel scaffold", "methods_summary": "SCI testing evaluated oxidative stress control, endogenous NSC migration/differentiation, and repair.", "paper_id": "M2A-P037", "sex": "UNKNOWN", "species": "Rodent model context", "strain": "UNKNOWN", "vertebral_level": "UNKNOWN"}, "source_experiment_tracker_id": "M2A-P037-E002", "source_paper_tracker_id": "M2A-P037", "tracker_key": "M2A-P037::M2A-P037-E002"}'
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
    'Composite patch was tested for exosome stability, neural toxicity, macrophage polarization, and neuronal apoptosis in vitro.',
    'Patch component comparison',
    'Schwann exosome and methylprednisolone hydrogel patch',
    '{"observation_tracker_ids": ["M2B-O020"], "source_experiment": {"chronicity_dpi_wpi": "In vitro", "control_type": "Patch component comparison", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P038-E001", "figure_ref": "Abstract", "injury_device": "Nanofiber/HA patch fabrication", "injury_model": "Patch compatibility model", "injury_severity": "N/A", "intervention_type": "Schwann exosome and methylprednisolone hydrogel patch", "methods_summary": "Composite patch was tested for exosome stability, neural toxicity, macrophage polarization, and neuronal apoptosis in vitro.", "paper_id": "M2A-P038", "sex": "N/A", "species": "In vitro / scaffold system", "strain": "Neural cells / macrophage model", "vertebral_level": "N/A"}, "source_experiment_tracker_id": "M2A-P038-E001", "source_paper_tracker_id": "M2A-P038", "tracker_key": "M2A-P038::M2A-P038-E001"}'
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
    'Patch covering the hematoma surface was assessed for functional, electrophysiological, inflammatory, and neuronal survival outcomes.',
    'Injury/patch comparison',
    'Exosome/steroid nanofiber hydrogel patch',
    '{"observation_tracker_ids": ["M2B-O085"], "source_experiment": {"chronicity_dpi_wpi": "Post-injury patch interval UNKNOWN", "control_type": "Injury/patch comparison", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P038-E002", "figure_ref": "Abstract", "injury_device": "Experimental SCI", "injury_model": "SCI with hematoma surface target", "injury_severity": "UNKNOWN", "intervention_type": "Exosome/steroid nanofiber hydrogel patch", "methods_summary": "Patch covering the hematoma surface was assessed for functional, electrophysiological, inflammatory, and neuronal survival outcomes.", "paper_id": "M2A-P038", "sex": "UNKNOWN", "species": "Rattus norvegicus", "strain": "UNKNOWN", "vertebral_level": "UNKNOWN"}, "source_experiment_tracker_id": "M2A-P038-E002", "source_paper_tracker_id": "M2A-P038", "tracker_key": "M2A-P038::M2A-P038-E002"}'
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
    1,
    'Abstract',
    'Tracker experiment M2A-P039-E001',
    'Conductive aligned fibers were tested with electrical stimulation for PC12 and NSC alignment, differentiation, and neurite sprouting.',
    'Electrical stimulation / scaffold comparison',
    'Aligned conductive CNT/GelMA hydrogel fibers',
    '{"observation_tracker_ids": ["M2B-O008"], "source_experiment": {"chronicity_dpi_wpi": "In vitro", "control_type": "Electrical stimulation / scaffold comparison", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P039-E001", "figure_ref": "Abstract", "injury_device": "CNT/GelMA fiber fabrication", "injury_model": "Neural differentiation model", "injury_severity": "N/A", "intervention_type": "Aligned conductive CNT/GelMA hydrogel fibers", "methods_summary": "Conductive aligned fibers were tested with electrical stimulation for PC12 and NSC alignment, differentiation, and neurite sprouting.", "paper_id": "M2A-P039", "sex": "N/A", "species": "In vitro scaffold/cell system", "strain": "PC12 cells / NSCs", "vertebral_level": "N/A"}, "source_experiment_tracker_id": "M2A-P039-E001", "source_paper_tracker_id": "M2A-P039", "tracker_key": "M2A-P039::M2A-P039-E001"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P039'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P039::M2A-P039-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract',
    'Tracker experiment M2A-P039-E002',
    'In vivo SCI testing assessed aligned conductive scaffold with electrical stimulation for axon regeneration and recovery.',
    'Scaffold/electrical stimulation comparison',
    'CNT/GelMA fibers + electrical stimulation',
    '{"observation_tracker_ids": ["M2B-O086"], "source_experiment": {"chronicity_dpi_wpi": "Post-implant interval UNKNOWN", "control_type": "Scaffold/electrical stimulation comparison", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P039-E002", "figure_ref": "Abstract", "injury_device": "Experimental SCI", "injury_model": "SCI", "injury_severity": "UNKNOWN", "intervention_type": "CNT/GelMA fibers + electrical stimulation", "methods_summary": "In vivo SCI testing assessed aligned conductive scaffold with electrical stimulation for axon regeneration and recovery.", "paper_id": "M2A-P039", "sex": "UNKNOWN", "species": "Rat SCI model context", "strain": "UNKNOWN", "vertebral_level": "UNKNOWN"}, "source_experiment_tracker_id": "M2A-P039-E002", "source_paper_tracker_id": "M2A-P039", "tracker_key": "M2A-P039::M2A-P039-E002"}'
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
    'Abstract',
    'Tracker experiment M2A-P040-E001',
    'Layer-by-layer PEG/PAA/protein films over agarose were tested for timed protein release.',
    'Release chemistry comparison',
    'PEG/PAA layer-by-layer agarose hydrogel',
    '{"observation_tracker_ids": ["M2B-O042"], "source_experiment": {"chronicity_dpi_wpi": "In vitro", "control_type": "Release chemistry comparison", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P040-E001", "figure_ref": "Abstract", "injury_device": "Agarose functionalization", "injury_model": "In vitro release model for SCI bridge", "injury_severity": "N/A", "intervention_type": "PEG/PAA layer-by-layer agarose hydrogel", "methods_summary": "Layer-by-layer PEG/PAA/protein films over agarose were tested for timed protein release.", "paper_id": "M2A-P040", "sex": "N/A", "species": "Scaffold system", "strain": "N/A", "vertebral_level": "N/A"}, "source_experiment_tracker_id": "M2A-P040-E001", "source_paper_tracker_id": "M2A-P040", "tracker_key": "M2A-P040::M2A-P040-E001"}'
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
    'Abstract',
    'Tracker experiment M2A-P040-E002',
    'Protein-release agarose strategy was framed as an alternative to genetically engineered BDNF-secreting cells in templated channel bridges.',
    'Cell-based BDNF delivery alternative',
    'Functionalized agarose channel bridge',
    '{"observation_tracker_ids": ["M2B-O087"], "source_experiment": {"chronicity_dpi_wpi": "In vitro / bridge design context", "control_type": "Cell-based BDNF delivery alternative", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P040-E002", "figure_ref": "Abstract", "injury_device": "Agarose channel scaffold", "injury_model": "SCI channel bridge model", "injury_severity": "N/A", "intervention_type": "Functionalized agarose channel bridge", "methods_summary": "Protein-release agarose strategy was framed as an alternative to genetically engineered BDNF-secreting cells in templated channel bridges.", "paper_id": "M2A-P040", "sex": "N/A", "species": "Scaffold system / SCI bridge context", "strain": "N/A", "vertebral_level": "N/A"}, "source_experiment_tracker_id": "M2A-P040-E002", "source_paper_tracker_id": "M2A-P040", "tracker_key": "M2A-P040::M2A-P040-E002"}'
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
    1,
    'Abstract',
    'Tracker experiment M2A-P041-E001',
    'NT-3-overexpressing Schwann cells and TrkC-overexpressing NSCs were co-cultured in gelatin sponge scaffold to generate a neural scaffold.',
    'Cell/scaffold construction',
    'NT-3-SC + TrkC-NSC gelatin sponge scaffold',
    '{"observation_tracker_ids": ["M2B-O011"], "source_experiment": {"chronicity_dpi_wpi": "In vitro before transplantation", "control_type": "Cell/scaffold construction", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P041-E001", "figure_ref": "Abstract", "injury_device": "Gelatin sponge scaffold", "injury_model": "Neural scaffold construction", "injury_severity": "N/A", "intervention_type": "NT-3-SC + TrkC-NSC gelatin sponge scaffold", "methods_summary": "NT-3-overexpressing Schwann cells and TrkC-overexpressing NSCs were co-cultured in gelatin sponge scaffold to generate a neural scaffold.", "paper_id": "M2A-P041", "sex": "N/A", "species": "Scaffold/cell system", "strain": "NSCs / Schwann cells", "vertebral_level": "N/A"}, "source_experiment_tracker_id": "M2A-P041-E001", "source_paper_tracker_id": "M2A-P041", "tracker_key": "M2A-P041::M2A-P041-E001"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P041'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P041::M2A-P041-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract',
    'Tracker experiment M2A-P041-E002',
    'Graft effects on myelination, NSC differentiation, axon regeneration, and functional recovery were assessed after complete transection.',
    'Scaffold/cell comparison',
    'Tissue-engineered gelatin sponge neural scaffold',
    '{"observation_tracker_ids": ["M2B-O088"], "source_experiment": {"chronicity_dpi_wpi": "Post-graft interval UNKNOWN", "control_type": "Scaffold/cell comparison", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P041-E002", "figure_ref": "Abstract", "injury_device": "T10 complete transection", "injury_model": "Complete transection SCI", "injury_severity": "Complete transection", "intervention_type": "Tissue-engineered gelatin sponge neural scaffold", "methods_summary": "Graft effects on myelination, NSC differentiation, axon regeneration, and functional recovery were assessed after complete transection.", "paper_id": "M2A-P041", "sex": "UNKNOWN", "species": "Rattus norvegicus", "strain": "Adult rats", "vertebral_level": "T10"}, "source_experiment_tracker_id": "M2A-P041-E002", "source_paper_tracker_id": "M2A-P041", "tracker_key": "M2A-P041::M2A-P041-E002"}'
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
    1,
    'Abstract',
    'Tracker experiment M2A-P042-E001',
    'Collagen/silk fibroin scaffold with spinal-cord-like cavities was fabricated by 3D bioprinting and combined with NSCs.',
    'Scaffold/cell construction',
    '3D collagen/silk fibroin scaffold + NSCs',
    '{"observation_tracker_ids": ["M2B-O029"], "source_experiment": {"chronicity_dpi_wpi": "In vitro / fabrication", "control_type": "Scaffold/cell construction", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P042-E001", "figure_ref": "Abstract", "injury_device": "3D bioprinting", "injury_model": "Scaffold fabrication model", "injury_severity": "N/A", "intervention_type": "3D collagen/silk fibroin scaffold + NSCs", "methods_summary": "Collagen/silk fibroin scaffold with spinal-cord-like cavities was fabricated by 3D bioprinting and combined with NSCs.", "paper_id": "M2A-P042", "sex": "N/A", "species": "Scaffold/cell system", "strain": "Neural stem cells", "vertebral_level": "N/A"}, "source_experiment_tracker_id": "M2A-P042-E001", "source_paper_tracker_id": "M2A-P042", "tracker_key": "M2A-P042::M2A-P042-E001"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P042'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P042::M2A-P042-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract',
    'Tracker experiment M2A-P042-E002',
    'In vivo testing assessed nerve regeneration and functional repair after scaffold/cell implantation.',
    'Scaffold/cell comparison',
    '3D-bioprinted collagen/silk scaffold + NSCs',
    '{"observation_tracker_ids": ["M2B-O089"], "source_experiment": {"chronicity_dpi_wpi": "Post-implant interval UNKNOWN", "control_type": "Scaffold/cell comparison", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P042-E002", "figure_ref": "Abstract", "injury_device": "Experimental SCI", "injury_model": "SCI", "injury_severity": "UNKNOWN", "intervention_type": "3D-bioprinted collagen/silk scaffold + NSCs", "methods_summary": "In vivo testing assessed nerve regeneration and functional repair after scaffold/cell implantation.", "paper_id": "M2A-P042", "sex": "UNKNOWN", "species": "Rat SCI model context", "strain": "UNKNOWN", "vertebral_level": "UNKNOWN"}, "source_experiment_tracker_id": "M2A-P042-E002", "source_paper_tracker_id": "M2A-P042", "tracker_key": "M2A-P042::M2A-P042-E002"}'
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
    1,
    'Abstract',
    'Tracker experiment M2A-P043-E001',
    'OEC-seeded scaffolds were implanted into lesion-induced gaps after acute SCI.',
    'Scaffold without OEC / injury comparison',
    'Longitudinal microstructured collagen scaffold + OECs',
    '{"observation_tracker_ids": ["M2B-O021"], "source_experiment": {"chronicity_dpi_wpi": "Post-implant interval UNKNOWN", "control_type": "Scaffold without OEC / injury comparison", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P043-E001", "figure_ref": "Abstract", "injury_device": "Mid-cervical unilateral resection model", "injury_model": "Acute spinal cord resection/gap injury", "injury_severity": "Acute lesion-induced gap", "intervention_type": "Longitudinal microstructured collagen scaffold + OECs", "methods_summary": "OEC-seeded scaffolds were implanted into lesion-induced gaps after acute SCI.", "paper_id": "M2A-P043", "sex": "UNKNOWN", "species": "Rattus norvegicus", "strain": "Adult Lewis rats", "vertebral_level": "Mid-cervical"}, "source_experiment_tracker_id": "M2A-P043-E001", "source_paper_tracker_id": "M2A-P043", "tracker_key": "M2A-P043::M2A-P043-E001"}'
  FROM _m2_paper_map p
  JOIN _m2_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M2A-P043'
  RETURNING experiment_id
)
INSERT INTO _m2_experiment_map (tracker_id, experiment_id) SELECT 'M2A-P043::M2A-P043-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description,
    control_type, intervention_type, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    2,
    'Abstract',
    'Tracker experiment M2A-P043-E002',
    'Functional improvement was evaluated against axon regeneration through the scaffold, with the abstract reporting lack of correlation.',
    'Functional recovery vs axon regeneration relationship',
    'OEC-seeded collagen scaffold',
    '{"observation_tracker_ids": ["M2B-O090"], "source_experiment": {"chronicity_dpi_wpi": "Post-implant interval UNKNOWN", "control_type": "Functional recovery vs axon regeneration relationship", "experiment_extracted": "YES (abstract-level)", "experiment_id": "M2A-P043-E002", "figure_ref": "Abstract", "injury_device": "Mid-cervical unilateral resection model", "injury_model": "Acute SCI", "injury_severity": "Acute lesion-induced gap", "intervention_type": "OEC-seeded collagen scaffold", "methods_summary": "Functional improvement was evaluated against axon regeneration through the scaffold, with the abstract reporting lack of correlation.", "paper_id": "M2A-P043", "sex": "UNKNOWN", "species": "Rattus norvegicus", "strain": "Adult Lewis rats", "vertebral_level": "Mid-cervical"}, "source_experiment_tracker_id": "M2A-P043-E002", "source_paper_tracker_id": "M2A-P043", "tracker_key": "M2A-P043::M2A-P043-E002"}'
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

INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('3D printing / graft scaffold', 'Module 2 tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
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
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Animal-model testing assessed repair potential of hAECs on Noggin-loaded conductive nanochitosan/polypyrrole-alginate scaffold.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Axon growth / integration', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Axon guidance / relay formation', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Axon guidance / scar response', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Axon infiltration', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Axon regeneration / recovery', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Axonal sprouting / function', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('BBB locomotion, neuronal growth, glial scar formation, inflammation, and collagen deposition were assessed.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Bioactive microenvironment', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Biophysical and biochemical cues', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Biotin-tagged IFN-gamma and PDGF-AA were immobilized to MAC hydrogel to cue neuronal or oligodendrocytic lineages within the bridge.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Boundary condition', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Cell retention / axon guidance', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Cell support / functional reconstruction', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Cell survival / repair response', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Channel architecture', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Circuit repair / function', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Conduction / inflammation / regeneration', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Conduction / locomotion / tract regrowth', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Different hMSC doses were compared for BBB locomotor scores, MEP amplitudes, cell survival, differentiation, and neurological repair.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Endogenous NSC recruitment / repair', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Function / local healing', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Functional improvement was evaluated against axon regeneration through the scaffold, with the abstract reporting lack of correlation.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Glial scar size, axon penetration, and histological response were assessed, with protoplasmic astrocyte ECM showing favorable effects in the abstract.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Graft effects on myelination, NSC differentiation, axon regeneration, and functional recovery were assessed after complete transection.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Hindlimb movement, neural conduction, inflammation, new neurons, synaptic structures, vessels, and nerve fiber regeneration were assessed.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Histological repair / function boundary', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Histology and qPCR assessed scaffold integration, neovascularization, axonal ingrowth, tissue response, and macrophage-related limitations.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Histology assessed host-cell migration, fibroglial scarring, and regeneration of corticospinal, raphaespinal, propriospinal, and ascending sensory axons through and beyond hydrogel channels.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Host ingrowth', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Host integration, inflammation, gliosis, vascularization, regenerated nerve fibers, and locomotor recovery were assessed after implantation.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Host-cell migration, blood-vessel growth, and axonal ingrowth into SAPNS were assessed as evidence of a 3D permissive environment.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Human iPSC-derived NS/PC transplantation was combined with scaffold-supported scar resection to assess graft survival, host axon regeneration, histological repair, and lack of functional recovery.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Hydrogel and biomaterial reviews frame SCI scaffolds as bridges, delivery reservoirs, and cell carriers, but emphasize that material class, lesion geometry, and combination therapy determine interpretability.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Hydrogel tubes guided robust axon growth along inner and outer tube surfaces, increased axon density within tubes, supported myelination of a subset of axons, and enhanced functional recovery.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Immunomodulation / neural differentiation', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Implant size, immune infiltration, Schwann-cell myelinated axons, axon growth, and BBB locomotor performance were assessed.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('In vitro and in vivo experiments evaluated whether the composite scaffold supported human menstrual blood-derived stem cells and improved functional reconstruction after SCI.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('In vitro and in vivo outcomes assessed inflammation reduction, neuronal differentiation, axonal regeneration, and spinal cord repair.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('In vivo SCI testing assessed aligned conductive scaffold with electrical stimulation for axon regeneration and recovery.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('In vivo rat SCI experiments evaluated regeneration and anti-inflammatory repair effects of the combined scaffold strategy.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('In vivo testing assessed nerve regeneration and functional repair after scaffold/cell implantation.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('In vivo validation assessed whether aligned injectable hydrogel promoted and oriented axon infiltration at the SCI site.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Inflammation / apoptosis / recovery', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Inflammation / electrophysiology / function', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Inflammation, microglia/macrophage activation, apoptosis, axonal regeneration, and functional recovery were assessed after transplantation into transection lesions.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Inflammatory response and scar tissue formation were assessed after scaffold implantation, with no excessive inflammatory response or scar formation reported in the abstract.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Integration / angiogenesis / axon ingrowth', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Lineage organization', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Locomotor / electrophysiology', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Locomotor / electrophysiology / histology', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Locomotor / scar response', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Locomotor kinematics, muscle activity, appositional healing, and spinal cord tissue remodeling were compared.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Locomotor recovery / tissue remodeling', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Locomotor recovery, endogenous neurogenesis, and scar response were assessed after functionalized NeuroRegen implantation.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Multimodal regeneration', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Multimodal repair', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Myelinated axons / locomotion', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Myelination / regeneration', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('NPC-loaded biomimetic scaffolds were implanted into complete SCI sites to assess host axon regeneration into the device, NPC axon extension into host cord, synaptic relay formation, synaptic transmission, and functional improvement.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Nerve regeneration', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Neural differentiation / repair', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('NeuroRegen collagen scaffold and hUC-MSCs implanted into the resected cavity were assessed by locomotion, motor/somatosensory evoked potentials, and histological repair outcomes.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Neuronal fiber growth, glial scar formation, and hindlimb motor function were compared across NT-3 scaffold, control scaffold, and saline groups.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Outcomes addressed cell retention, axonal guidance, neuronal regeneration microenvironment, and functional recovery according to abstract.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Patch covering the hematoma surface was assessed for functional, electrophysiological, inflammatory, and neuronal survival outcomes.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Phase I clinical testing evaluated safety and possible repair after collagen scaffold plus hUC-MSC transplantation.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Protein-release agarose strategy was framed as an alternative to genetically engineered BDNF-secreting cells in templated channel bridges.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Rat SCI testing assessed angiogenesis, anti-inflammatory and anti-apoptotic effects, neural differentiation, regeneration, and functional recovery.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
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
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Scar / axon penetration', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Scar identity', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Surface-capping scaffold was applied after subacute SCI and assessed for repair-associated outcomes.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('The scaffold was framed as a platform to test architecture, transplanted cells, and local molecular agents for axon regeneration.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Timed protein release', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Tissue ingrowth / function', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Tissue ingrowth, nerve regeneration, and functional recovery were assessed after hydrogel implantation.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Vascularization / axon growth / locomotion', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('hAEC-neural-like cell scaffold was implanted into rat full transection SCI to assess neural circuit and hindlimb recovery.', 'Module 2 tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;

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
    'Eight chronic complete SCI patients received hUCB-MSC-loaded NeuroRegen scaffold after neurophysiology-guided scar resection and were followed for one year.',
    'patients / year',
    'Eight chronic complete SCI patients received hUCB-MSC-loaded NeuroRegen scaffold after neurophysiology-guided scar resection and were followed for one year.',
    'chronic complete human NeuroRegen/hUCB-MSC feasibility cohort',
    'Abstract',
    'Abstract',
    'medium',
    '{"curator_notes": "Similar intervention family as M2A-P001 but different cell source.", "experiment_tracker_id": "M2A-P009-E001", "paper_tracker_id": "M2A-P009", "quantitative": "YES", "statistics_reported": "abstract-level; exact outcome statistics not yet extracted", "topic_id": "M2B-T006", "tracker_id": "M2B-O002"}'
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
    'Biomimetic 3D-printed scaffolds loaded with neural progenitor cells supported host axon entry, graft axon extension into host cord, synaptic relay formation, synaptic transmission, and functional improvement after complete SCI.',
    'qualitative',
    'Biomimetic 3D-printed scaffolds loaded with neural progenitor cells supported host axon entry, graft axon extension into host cord, synaptic relay formation, synaptic transmission, and functional improvement after complete SCI.',
    '3D printed architecture plus NPCs supports bridge/relay repair',
    'Abstract',
    'Abstract',
    'medium',
    '{"curator_notes": "Architecture and cell effects are bundled.", "experiment_tracker_id": "M2A-P004-E001", "paper_tracker_id": "M2A-P004", "quantitative": "YES", "statistics_reported": "statistics not extracted from abstract", "topic_id": "M2B-T001", "tracker_id": "M2B-O004"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P004::M2A-P004-E001'
    AND et.evidence_type_name = '3D printing / graft scaffold'
    AND ot.outcome_type_name = 'Axon guidance / relay formation'
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
    'Porous aligned hydrogel tubes integrated with host tissue, reduced scarring relative to gelfoam, guided axon growth along tube surfaces, supported myelination of some axons, and enhanced functional recovery.',
    'qualitative',
    'Porous aligned hydrogel tubes integrated with host tissue, reduced scarring relative to gelfoam, guided axon growth along tube surfaces, supported myelination of some axons, and enhanced functional recovery.',
    'aligned hydrogel tubes support tissue integration and axon guidance',
    'Abstract',
    'Abstract',
    'medium',
    '{"curator_notes": "Important scaffold-only guidance anchor.", "experiment_tracker_id": "M2A-P005-E001", "paper_tracker_id": "M2A-P005", "quantitative": "YES", "statistics_reported": "abstract-level; exact values not extracted", "topic_id": "M2B-T001", "tracker_id": "M2B-O005"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P005::M2A-P005-E001'
    AND et.evidence_type_name = 'Aligned hydrogel scaffold'
    AND ot.outcome_type_name = 'Axon growth / integration'
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
    'Aligned CNT/GelMA hydrogel fibers mimicked axon-like conductive aligned structure; combined with electrical stimulation they promoted neural-cell alignment/differentiation in vitro and were tested for SCI recovery in vivo.',
    'qualitative',
    'Aligned CNT/GelMA hydrogel fibers mimicked axon-like conductive aligned structure; combined with electrical stimulation they promoted neural-cell alignment/differentiation in vitro and were tested for SCI recovery in vivo.',
    'conductive aligned scaffold plus ES promotes neural alignment and repair',
    'Abstract',
    'Abstract',
    'medium',
    '{"curator_notes": "Advanced guidance/electrical interface anchor.", "experiment_tracker_id": "M2A-P039-E001", "paper_tracker_id": "M2A-P039", "quantitative": "YES", "statistics_reported": "exact values not extracted", "topic_id": "M2B-T001", "tracker_id": "M2B-O008"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P039::M2A-P039-E001'
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
    'Schwann cells in injectable decellularized peripheral nerve matrix produced larger implants and about twice as many Schwann-cell-myelinated axons as Matrigel grafts while performing similarly in BBB locomotor testing.',
    'relative axon count / BBB',
    'Schwann cells in injectable decellularized peripheral nerve matrix produced larger implants and about twice as many Schwann-cell-myelinated axons as Matrigel grafts while performing similarly in BBB locomotor testing.',
    'iPN improves graft/axon histology vs Matrigel without clear BBB superiority',
    'Abstract',
    'Abstract',
    'medium',
    '{"curator_notes": "Separates histological benefit from locomotor equivalence.", "experiment_tracker_id": "M2A-P016-E001", "paper_tracker_id": "M2A-P016", "quantitative": "YES", "statistics_reported": "\"twice as many\" reported in abstract", "topic_id": "M2B-T002", "tracker_id": "M2B-O010"}'
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
    'Gelatin sponge scaffold with NT-3-overexpressing Schwann cells and TrkC-overexpressing NSCs enhanced myelination and repair after rat T10 complete transection.',
    'qualitative',
    'Gelatin sponge scaffold with NT-3-overexpressing Schwann cells and TrkC-overexpressing NSCs enhanced myelination and repair after rat T10 complete transection.',
    'engineered cell/scaffold network promotes myelination',
    'Abstract',
    'Abstract',
    'medium',
    '{"curator_notes": "Combination mechanism is highly bundled.", "experiment_tracker_id": "M2A-P041-E001", "paper_tracker_id": "M2A-P041", "quantitative": "YES", "statistics_reported": "exact values not extracted", "topic_id": "M2B-T002", "tracker_id": "M2B-O011"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P041::M2A-P041-E001'
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
    'NT-3 released from fibrin scaffolds increased neuronal fiber growth into adult rat spinal cord lesions by about 1.5- to 3-fold and reduced glial scar formation, but hindlimb motor function did not improve relative to controls.',
    'fold-change',
    'NT-3 released from fibrin scaffolds increased neuronal fiber growth into adult rat spinal cord lesions by about 1.5- to 3-fold and reduced glial scar formation, but hindlimb motor function did not improve relative to controls.',
    'NT-3 fibrin scaffold improved histology without functional improvement',
    'Abstract',
    'Abstract',
    'medium',
    '{"curator_notes": "Key positive-histology/negative-function boundary.", "experiment_tracker_id": "M2A-P025-E001", "paper_tracker_id": "M2A-P025", "quantitative": "YES", "statistics_reported": "1.5- to 3-fold fiber growth; function not improved", "topic_id": "M2B-T003", "tracker_id": "M2B-O012"}'
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
    'Dual-phase SilMA hydrogel with PLGA microspheres was designed to release Ang-(1-7) early and NT-3 later, reducing inflammation and promoting neural differentiation/axonal regeneration in SCI repair assays.',
    'qualitative',
    'Dual-phase SilMA hydrogel with PLGA microspheres was designed to release Ang-(1-7) early and NT-3 later, reducing inflammation and promoting neural differentiation/axonal regeneration in SCI repair assays.',
    'staged release scaffold targets inflammation then regeneration',
    'Abstract',
    'Abstract',
    'medium',
    '{"curator_notes": "Strong design logic; needs full text for timing and effect sizes.", "experiment_tracker_id": "M2A-P036-E001", "paper_tracker_id": "M2A-P036", "quantitative": "YES", "statistics_reported": "exact values not extracted", "topic_id": "M2B-T003", "tracker_id": "M2B-O014"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P036::M2A-P036-E001'
    AND et.evidence_type_name = 'Sequential-release SilMA scaffold'
    AND ot.outcome_type_name = 'Immunomodulation / neural differentiation'
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
    'Porcine spinal cord and urinary bladder ECM hydrogels integrated into rat hemisection lesions and stimulated neovascularization and axonal ingrowth, while macrophage/mass response created limitations.',
    'qualitative',
    'Porcine spinal cord and urinary bladder ECM hydrogels integrated into rat hemisection lesions and stimulated neovascularization and axonal ingrowth, while macrophage/mass response created limitations.',
    'injectable ECM supports ingrowth but immune/material response matters',
    'Abstract',
    'Abstract',
    'medium',
    '{"curator_notes": "Important ECM benefit/boundary observation.", "experiment_tracker_id": "M2A-P014-E001", "paper_tracker_id": "M2A-P014", "quantitative": "YES", "statistics_reported": "qPCR/histology reported; exact values not extracted", "topic_id": "M2B-T004", "tracker_id": "M2B-O015"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P014::M2A-P014-E001'
    AND et.evidence_type_name = 'Injectable ECM hydrogel'
    AND ot.outcome_type_name = 'Integration / angiogenesis / axon ingrowth'
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
    'HA hydrogels containing protoplasmic astrocyte-derived ECM reduced glial scar size and increased axon penetration after SCI compared with other ECM conditions.',
    'qualitative',
    'HA hydrogels containing protoplasmic astrocyte-derived ECM reduced glial scar size and increased axon penetration after SCI compared with other ECM conditions.',
    'astrocyte ECM subtype changes HA hydrogel histology',
    'Abstract',
    'Abstract',
    'medium',
    '{"curator_notes": "ECM source/subtype is a material boundary condition.", "experiment_tracker_id": "M2A-P032-E001", "paper_tracker_id": "M2A-P032", "quantitative": "YES", "statistics_reported": "exact values not extracted", "topic_id": "M2B-T004", "tracker_id": "M2B-O016"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P032::M2A-P032-E001'
    AND et.evidence_type_name = 'HA hydrogel plus astrocyte ECM'
    AND ot.outcome_type_name = 'Scar / axon penetration'
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
    'In chronic canine complete T8 transection, delayed scar removal followed by hUC-MSC-loaded NeuroRegen scaffold promoted locomotor recovery, endogenous neurogenesis, and reduced scar response.',
    'months post injury',
    'In chronic canine complete T8 transection, delayed scar removal followed by hUC-MSC-loaded NeuroRegen scaffold promoted locomotor recovery, endogenous neurogenesis, and reduced scar response.',
    'large-animal chronic NeuroRegen+hUC-MSC repair signal',
    'Abstract',
    'Abstract',
    'medium',
    '{"curator_notes": "Translational large-animal chronic anchor.", "experiment_tracker_id": "M2A-P015-E001", "paper_tracker_id": "M2A-P015", "quantitative": "YES", "statistics_reported": "exact values not extracted", "topic_id": "M2B-T005", "tracker_id": "M2B-O018"}'
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
    'HA demilune scaffold with PPY-coated fibers, RAD16 hydrogel, iNPCs, and curcumin preserved iNPC viability, increased neurite outgrowth/migration in vitro/organotypic culture, and was applied as a minimally invasive surface cap after subacute SCI.',
    'qualitative',
    'HA demilune scaffold with PPY-coated fibers, RAD16 hydrogel, iNPCs, and curcumin preserved iNPC viability, increased neurite outgrowth/migration in vitro/organotypic culture, and was applied as a minimally invasive surface cap after subacute SCI.',
    'surface-capping conductive scaffold supports cells and repair-associated responses',
    'Abstract',
    'Abstract',
    'medium',
    '{"curator_notes": "Surface-capping strategy differs from lesion-filling bridges.", "experiment_tracker_id": "M2A-P034-E001", "paper_tracker_id": "M2A-P034", "quantitative": "YES", "statistics_reported": "exact values not extracted", "topic_id": "M2B-T007", "tracker_id": "M2B-O019"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P034::M2A-P034-E001'
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
    'OEC-seeded longitudinal collagen scaffold produced functional improvement in acute SCI, but recovery was not correlated with axon regeneration through the scaffold.',
    'qualitative',
    'OEC-seeded longitudinal collagen scaffold produced functional improvement in acute SCI, but recovery was not correlated with axon regeneration through the scaffold.',
    'functional recovery can dissociate from scaffold-traversing axon regeneration',
    'Abstract',
    'Abstract',
    'medium',
    '{"curator_notes": "Prevents overinterpreting all recovery as bridge-mediated axon regeneration.", "experiment_tracker_id": "M2A-P043-E001", "paper_tracker_id": "M2A-P043", "quantitative": "YES", "statistics_reported": "abstract-level; exact correlation metrics not extracted", "topic_id": "M2B-T008", "tracker_id": "M2B-O021"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P043::M2A-P043-E001'
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
    'Two strictly diagnosed acute complete SCI patients received NeuroRegen scaffold plus MSC transplantation and one-year monitoring.',
    'patients / year',
    'Two strictly diagnosed acute complete SCI patients received NeuroRegen scaffold plus MSC transplantation and one-year monitoring.',
    'acute complete human scaffold/MSC feasibility signal',
    'Abstract',
    'Abstract',
    'medium',
    '{"curator_notes": "Supports feasibility only because cohort is extremely small.", "experiment_tracker_id": "M2A-P017-E001", "paper_tracker_id": "M2A-P017", "quantitative": "YES", "statistics_reported": "n = 2; exact endpoints not extracted", "topic_id": "M2B-T006", "tracker_id": "M2B-O022"}'
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
    'Collagen scaffold plus hUC-MSC strategy was tested in rat/canine complete transection models and a phase I acute complete human SCI trial.',
    'multi-species',
    'Collagen scaffold plus hUC-MSC strategy was tested in rat/canine complete transection models and a phase I acute complete human SCI trial.',
    'collagen+hUC-MSC tested across animal and human phase I settings',
    'Abstract',
    'Abstract',
    'medium',
    '{"curator_notes": "Important translational bridge but cell/scaffold effects are bundled.", "experiment_tracker_id": "M2A-P033-E001", "paper_tracker_id": "M2A-P033", "quantitative": "YES", "statistics_reported": "exact human outcome values not extracted", "topic_id": "M2B-T006", "tracker_id": "M2B-O023"}'
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
    'Aligned nanofiber-hydrogel scaffold after rat C5 hemi-incision provided nonviral delivery, contact guidance, early aligned axon regeneration, and no excessive inflammatory or scar response.',
    '1 WPI early axon assessment',
    'Aligned nanofiber-hydrogel scaffold after rat C5 hemi-incision provided nonviral delivery, contact guidance, early aligned axon regeneration, and no excessive inflammatory or scar response.',
    'aligned nanofiber scaffold supports delivery/guidance without excessive scar',
    'Abstract',
    'Abstract',
    'medium',
    '{"curator_notes": "Combines scaffold guidance with molecular delivery.", "experiment_tracker_id": "M2A-P008-E001", "paper_tracker_id": "M2A-P008", "quantitative": "YES", "statistics_reported": "exact values not extracted", "topic_id": "M2B-T001", "tracker_id": "M2B-O024"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P008::M2A-P008-E001'
    AND et.evidence_type_name = 'Aligned nanofiber-hydrogel scaffold'
    AND ot.outcome_type_name = 'Axon guidance / scar response'
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
    'GelMA microchannel scaffold loaded with hAEC-derived neural-like cells improved neural circuit and hindlimb recovery after rat full transection SCI.',
    'qualitative',
    'GelMA microchannel scaffold loaded with hAEC-derived neural-like cells improved neural circuit and hindlimb recovery after rat full transection SCI.',
    'microchannel GelMA scaffold plus hAEC neural-like cells supports circuit repair',
    'Abstract',
    'Abstract',
    'medium',
    '{"curator_notes": "Architecture and cell effects are bundled.", "experiment_tracker_id": "M2A-P035-E001", "paper_tracker_id": "M2A-P035", "quantitative": "YES", "statistics_reported": "exact values not extracted", "topic_id": "M2B-T001", "tracker_id": "M2B-O027"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P035::M2A-P035-E001'
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
    '3D-bioprinted collagen/silk fibroin scaffold with spinal-cord-like cavities plus NSCs promoted nerve regeneration after SCI.',
    'qualitative',
    '3D-bioprinted collagen/silk fibroin scaffold with spinal-cord-like cavities plus NSCs promoted nerve regeneration after SCI.',
    'bioprinted silk/collagen scaffold plus NSCs supports regeneration',
    'Abstract',
    'Abstract',
    'medium',
    '{"curator_notes": "Printed architecture and cell effect bundled.", "experiment_tracker_id": "M2A-P042-E001", "paper_tracker_id": "M2A-P042", "quantitative": "YES", "statistics_reported": "exact values not extracted", "topic_id": "M2B-T001", "tracker_id": "M2B-O029"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P042::M2A-P042-E001'
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
    'Noggin-loaded nanochitosan/polypyrrole-alginate conductive scaffold supported hAEC attachment/neural differentiation and SCI repair-marker testing in an animal model.',
    'qualitative',
    'Noggin-loaded nanochitosan/polypyrrole-alginate conductive scaffold supported hAEC attachment/neural differentiation and SCI repair-marker testing in an animal model.',
    'conductive chitosan scaffold supports hAEC differentiation and repair testing',
    'Abstract',
    'Abstract',
    'medium',
    '{"curator_notes": "Conductive/cell/growth-factor combination.", "experiment_tracker_id": "M2A-P024-E001", "paper_tracker_id": "M2A-P024", "quantitative": "YES", "statistics_reported": "exact values not extracted", "topic_id": "M2B-T002", "tracker_id": "M2B-O036"}'
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
    'bFGF-incorporated HEMA-MOETACL hydrogel implanted 5 days after T9 complete transection supported regenerating tissue ingrowth and functional recovery by 8 weeks.',
    'weeks post injury',
    'bFGF-incorporated HEMA-MOETACL hydrogel implanted 5 days after T9 complete transection supported regenerating tissue ingrowth and functional recovery by 8 weeks.',
    'delayed bFGF hydrogel supports tissue and functional repair',
    'Abstract',
    'Abstract',
    'medium',
    '{"curator_notes": "Growth-factor hydrogel anchor.", "experiment_tracker_id": "M2A-P026-E001", "paper_tracker_id": "M2A-P026", "quantitative": "YES", "statistics_reported": "exact values not extracted", "topic_id": "M2B-T003", "tracker_id": "M2B-O038"}'
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
    'NT-3/fibroin-modified gelatin sponge scaffold improved canine hindlimb movement, neural conduction, inflammation, vessel formation, synaptic structures, and nerve fiber regeneration.',
    'qualitative',
    'NT-3/fibroin-modified gelatin sponge scaffold improved canine hindlimb movement, neural conduction, inflammation, vessel formation, synaptic structures, and nerve fiber regeneration.',
    'large-animal NT-3/fibroin scaffold improves conduction and repair profile',
    'Abstract',
    'Abstract',
    'medium',
    '{"curator_notes": "Large-animal cargo-release anchor.", "experiment_tracker_id": "M2A-P030-E001", "paper_tracker_id": "M2A-P030", "quantitative": "YES", "statistics_reported": "exact values not extracted", "topic_id": "M2B-T003", "tracker_id": "M2B-O040"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P030::M2A-P030-E001'
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
    'PEG/PAA/protein layer-by-layer films over agarose hydrogels provided a strategy for sustained BDNF release from templated SCI channel bridges.',
    'qualitative',
    'PEG/PAA/protein layer-by-layer films over agarose hydrogels provided a strategy for sustained BDNF release from templated SCI channel bridges.',
    'agarose channel scaffold can support controlled protein release',
    'Abstract',
    'Abstract',
    'medium',
    '{"curator_notes": "Methods anchor for release rather than in vivo efficacy.", "experiment_tracker_id": "M2A-P040-E001", "paper_tracker_id": "M2A-P040", "quantitative": "NO", "statistics_reported": "release details not extracted", "topic_id": "M2B-T003", "tracker_id": "M2B-O042"}'
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
    'Chronic complete SCI patients underwent scar resection and NeuroRegen/hUCB-MSC implantation with safety and neurological/electrophysiological follow-up.',
    'patients / year',
    'Chronic complete SCI patients underwent scar resection and NeuroRegen/hUCB-MSC implantation with safety and neurological/electrophysiological follow-up.',
    'chronic human scar-resection scaffold strategy feasible',
    'Abstract',
    'Abstract',
    'medium',
    '{"curator_notes": "Human chronic strategy but efficacy remains cautious.", "experiment_tracker_id": "M2A-P009-E001", "paper_tracker_id": "M2A-P009", "quantitative": "YES", "statistics_reported": "exact values not extracted", "topic_id": "M2B-T005", "tracker_id": "M2B-O047"}'
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
    'Koffler J 2019 M2A-P004-E002 preserves a distinct Rodent experiment testing NPC-loaded 3D-printed scaffold implantation with endpoint/readout: NPC-loaded biomimetic scaffolds were implanted into complete SCI sites to assess host axon regeneration into the device, NPC axon extension into host cord, synaptic relay formation, synaptic transmission, and functional improvement..',
    'qualitative',
    'Koffler J 2019 M2A-P004-E002 preserves a distinct Rodent experiment testing NPC-loaded 3D-printed scaffold implantation with endpoint/readout: NPC-loaded biomimetic scaffolds were implanted into complete SCI sites to assess host axon regeneration into the device, NPC axon extension into host cord, synaptic relay formation, synaptic transmission, and functional improvement..',
    'M2A-P004-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Biomimetic 3D-printed scaffolds for spinal cord injury repair. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M2A-P004-E002", "paper_tracker_id": "M2A-P004", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M2B-T001", "tracker_id": "M2B-O053"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P004::M2A-P004-E002'
    AND et.evidence_type_name = '3D printing / graft scaffold'
    AND ot.outcome_type_name = 'NPC-loaded biomimetic scaffolds were implanted into complete SCI sites to assess host axon regeneration into the device, NPC axon extension into host cord, synaptic relay formation, synaptic transmission, and functional improvement.'
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
    'Dumont CM 2019 M2A-P005-E002 preserves a distinct Rodent model context experiment testing Hydrogel tube axon-guidance scaffold with endpoint/readout: Hydrogel tubes guided robust axon growth along inner and outer tube surfaces, increased axon density within tubes, supported myelination of a subset of axons, and enhanced functional recovery..',
    'qualitative',
    'Dumont CM 2019 M2A-P005-E002 preserves a distinct Rodent model context experiment testing Hydrogel tube axon-guidance scaffold with endpoint/readout: Hydrogel tubes guided robust axon growth along inner and outer tube surfaces, increased axon density within tubes, supported myelination of a subset of axons, and enhanced functional recovery..',
    'M2A-P005-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Aligned hydrogel tubes guide regeneration following spinal cord injury. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M2A-P005-E002", "paper_tracker_id": "M2A-P005", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M2B-T001", "tracker_id": "M2B-O054"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P005::M2A-P005-E002'
    AND et.evidence_type_name = 'Aligned hydrogel scaffold'
    AND ot.outcome_type_name = 'Hydrogel tubes guided robust axon growth along inner and outer tube surfaces, increased axon density within tubes, supported myelination of a subset of axons, and enhanced functional recovery.'
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
    'Nguyen LH 2017 M2A-P008-E002 preserves a distinct Rattus norvegicus experiment testing 3D aligned nanofiber-hydrogel scaffold with endpoint/readout: Inflammatory response and scar tissue formation were assessed after scaffold implantation, with no excessive inflammatory response or scar formation reported in the abstract..',
    'qualitative',
    'Nguyen LH 2017 M2A-P008-E002 preserves a distinct Rattus norvegicus experiment testing 3D aligned nanofiber-hydrogel scaffold with endpoint/readout: Inflammatory response and scar tissue formation were assessed after scaffold implantation, with no excessive inflammatory response or scar formation reported in the abstract..',
    'M2A-P008-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Three-dimensional aligned nanofibers-hydrogel scaffold for controlled non-viral drug/gene delivery to direct axon regeneration in spinal cord injury treatment. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M2A-P008-E002", "paper_tracker_id": "M2A-P008", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M2B-T001", "tracker_id": "M2B-O057"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P008::M2A-P008-E002'
    AND et.evidence_type_name = 'Aligned nanofiber-hydrogel scaffold'
    AND ot.outcome_type_name = 'Inflammatory response and scar tissue formation were assessed after scaffold implantation, with no excessive inflammatory response or scar formation reported in the abstract.'
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
    'Tukmachev D 2016 M2A-P014-E002 preserves a distinct Rattus norvegicus experiment testing Injectable ECM hydrogel lesion scaffold with endpoint/readout: Histology and qPCR assessed scaffold integration, neovascularization, axonal ingrowth, tissue response, and macrophage-related limitations..',
    'qualitative',
    'Tukmachev D 2016 M2A-P014-E002 preserves a distinct Rattus norvegicus experiment testing Injectable ECM hydrogel lesion scaffold with endpoint/readout: Histology and qPCR assessed scaffold integration, neovascularization, axonal ingrowth, tissue response, and macrophage-related limitations..',
    'M2A-P014-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Injectable Extracellular Matrix Hydrogels as Scaffolds for Spinal Cord Injury Repair. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M2A-P014-E002", "paper_tracker_id": "M2A-P014", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M2B-T004", "tracker_id": "M2B-O062"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P014::M2A-P014-E002'
    AND et.evidence_type_name = 'Injectable ECM hydrogel'
    AND ot.outcome_type_name = 'Histology and qPCR assessed scaffold integration, neovascularization, axonal ingrowth, tissue response, and macrophage-related limitations.'
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
    'Li X 2017 M2A-P015-E002 preserves a distinct Canis familiaris experiment testing Functionalized NeuroRegen scaffold with endpoint/readout: Locomotor recovery, endogenous neurogenesis, and scar response were assessed after functionalized NeuroRegen implantation..',
    'qualitative',
    'Li X 2017 M2A-P015-E002 preserves a distinct Canis familiaris experiment testing Functionalized NeuroRegen scaffold with endpoint/readout: Locomotor recovery, endogenous neurogenesis, and scar response were assessed after functionalized NeuroRegen implantation..',
    'M2A-P015-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Transplantation of hUC-MSCs seeded collagen scaffolds reduces scar formation and promotes functional recovery in canines with chronic spinal cord injury. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M2A-P015-E002", "paper_tracker_id": "M2A-P015", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M2B-T005", "tracker_id": "M2B-O063"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P015::M2A-P015-E002'
    AND et.evidence_type_name = 'Chronic canine scar removal plus NeuroRegen/hUC-MSC'
    AND ot.outcome_type_name = 'Locomotor recovery, endogenous neurogenesis, and scar response were assessed after functionalized NeuroRegen implantation.'
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
    'Cerqueira SR 2018 M2A-P016-E002 preserves a distinct Rattus norvegicus experiment testing SC/iPN matrix graft with endpoint/readout: Implant size, immune infiltration, Schwann-cell myelinated axons, axon growth, and BBB locomotor performance were assessed..',
    'qualitative',
    'Cerqueira SR 2018 M2A-P016-E002 preserves a distinct Rattus norvegicus experiment testing SC/iPN matrix graft with endpoint/readout: Implant size, immune infiltration, Schwann-cell myelinated axons, axon growth, and BBB locomotor performance were assessed..',
    'M2A-P016-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Decellularized peripheral nerve supports Schwann cell transplants and axon growth following spinal cord injury. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M2A-P016-E002", "paper_tracker_id": "M2A-P016", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M2B-T002", "tracker_id": "M2B-O064"}'
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
    'Manzari-Tavakoli A 2024 M2A-P024-E002 preserves a distinct Animal SCI model context experiment testing hAEC-loaded conductive chitosan scaffold with endpoint/readout: Animal-model testing assessed repair potential of hAECs on Noggin-loaded conductive nanochitosan/polypyrrole-alginate scaffold..',
    'qualitative',
    'Manzari-Tavakoli A 2024 M2A-P024-E002 preserves a distinct Animal SCI model context experiment testing hAEC-loaded conductive chitosan scaffold with endpoint/readout: Animal-model testing assessed repair potential of hAECs on Noggin-loaded conductive nanochitosan/polypyrrole-alginate scaffold..',
    'M2A-P024-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Therapeutic potential of placenta-derived stem cells cultivated on noggin-loaded nanochitosan/polypyrrole-alginate conductive scaffold to restore spinal cord injury. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M2A-P024-E002", "paper_tracker_id": "M2A-P024", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M2B-T002", "tracker_id": "M2B-O071"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P024::M2A-P024-E002'
    AND et.evidence_type_name = 'Conductive chitosan/alginate + hAEC + Noggin'
    AND ot.outcome_type_name = 'Animal-model testing assessed repair potential of hAECs on Noggin-loaded conductive nanochitosan/polypyrrole-alginate scaffold.'
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
    'Taylor SJ 2006 M2A-P025-E002 preserves a distinct Rattus norvegicus experiment testing Fibrin/NT-3 scaffold with endpoint/readout: Neuronal fiber growth, glial scar formation, and hindlimb motor function were compared across NT-3 scaffold, control scaffold, and saline groups..',
    'qualitative',
    'Taylor SJ 2006 M2A-P025-E002 preserves a distinct Rattus norvegicus experiment testing Fibrin/NT-3 scaffold with endpoint/readout: Neuronal fiber growth, glial scar formation, and hindlimb motor function were compared across NT-3 scaffold, control scaffold, and saline groups..',
    'M2A-P025-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Delivery of neurotrophin-3 from fibrin enhances neuronal fiber sprouting after spinal cord injury. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M2A-P025-E002", "paper_tracker_id": "M2A-P025", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M2B-T003", "tracker_id": "M2B-O072"}'
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
    'Chen B 2015 M2A-P026-E002 preserves a distinct Rattus norvegicus experiment testing bFGF hydrogel scaffold with endpoint/readout: Tissue ingrowth, nerve regeneration, and functional recovery were assessed after hydrogel implantation..',
    'qualitative',
    'Chen B 2015 M2A-P026-E002 preserves a distinct Rattus norvegicus experiment testing bFGF hydrogel scaffold with endpoint/readout: Tissue ingrowth, nerve regeneration, and functional recovery were assessed after hydrogel implantation..',
    'M2A-P026-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Repair of spinal cord injury by implantation of bFGF-incorporated HEMA-MOETACL hydrogel in rats. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M2A-P026-E002", "paper_tracker_id": "M2A-P026", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M2B-T003", "tracker_id": "M2B-O073"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P026::M2A-P026-E002'
    AND et.evidence_type_name = 'bFGF hydrogel'
    AND ot.outcome_type_name = 'Tissue ingrowth, nerve regeneration, and functional recovery were assessed after hydrogel implantation.'
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
    'Li G 2018 M2A-P030-E002 preserves a distinct Canis familiaris experiment testing NT-3/fibroin gelatin scaffold with endpoint/readout: Hindlimb movement, neural conduction, inflammation, new neurons, synaptic structures, vessels, and nerve fiber regeneration were assessed..',
    'qualitative',
    'Li G 2018 M2A-P030-E002 preserves a distinct Canis familiaris experiment testing NT-3/fibroin gelatin scaffold with endpoint/readout: Hindlimb movement, neural conduction, inflammation, new neurons, synaptic structures, vessels, and nerve fiber regeneration were assessed..',
    'M2A-P030-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Neurotrophin-3 released from implant of tissue-engineered fibroin scaffolds inhibits inflammation, enhances nerve fiber regeneration, and improves motor function in canine spinal cord injury. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M2A-P030-E002", "paper_tracker_id": "M2A-P030", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M2B-T003", "tracker_id": "M2B-O077"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P030::M2A-P030-E002'
    AND et.evidence_type_name = 'NT-3/fibroin gelatin scaffold'
    AND ot.outcome_type_name = 'Hindlimb movement, neural conduction, inflammation, new neurons, synaptic structures, vessels, and nerve fiber regeneration were assessed.'
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
    'Thompson RE 2018 M2A-P032-E002 preserves a distinct Rattus norvegicus experiment testing HA/astrocyte ECM hydrogel with endpoint/readout: Glial scar size, axon penetration, and histological response were assessed, with protoplasmic astrocyte ECM showing favorable effects in the abstract..',
    'qualitative',
    'Thompson RE 2018 M2A-P032-E002 preserves a distinct Rattus norvegicus experiment testing HA/astrocyte ECM hydrogel with endpoint/readout: Glial scar size, axon penetration, and histological response were assessed, with protoplasmic astrocyte ECM showing favorable effects in the abstract..',
    'M2A-P032-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Effect of hyaluronic acid hydrogels containing astrocyte-derived extracellular matrix and/or V2a interneurons on histologic outcomes following spinal cord injury. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M2A-P032-E002", "paper_tracker_id": "M2A-P032", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M2B-T004", "tracker_id": "M2B-O079"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P032::M2A-P032-E002'
    AND et.evidence_type_name = 'HA hydrogel plus astrocyte ECM'
    AND ot.outcome_type_name = 'Glial scar size, axon penetration, and histological response were assessed, with protoplasmic astrocyte ECM showing favorable effects in the abstract.'
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
    'Deng WS 2020 M2A-P033-E002 preserves a distinct Homo sapiens experiment testing Collagen scaffold + hUC-MSC with endpoint/readout: Phase I clinical testing evaluated safety and possible repair after collagen scaffold plus hUC-MSC transplantation..',
    'qualitative',
    'Deng WS 2020 M2A-P033-E002 preserves a distinct Homo sapiens experiment testing Collagen scaffold + hUC-MSC with endpoint/readout: Phase I clinical testing evaluated safety and possible repair after collagen scaffold plus hUC-MSC transplantation..',
    'M2A-P033-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Collagen scaffold combined with human umbilical cord-mesenchymal stem cells transplantation for acute complete spinal cord injury. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M2A-P033-E002", "paper_tracker_id": "M2A-P033", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M2B-T006", "tracker_id": "M2B-O080"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P033::M2A-P033-E002'
    AND et.evidence_type_name = 'Animal-to-clinical translation'
    AND ot.outcome_type_name = 'Phase I clinical testing evaluated safety and possible repair after collagen scaffold plus hUC-MSC transplantation.'
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
    'Elkhenany H 2021 M2A-P034-E002 preserves a distinct Rat model context experiment testing HA demilune surface-capping scaffold with endpoint/readout: Surface-capping scaffold was applied after subacute SCI and assessed for repair-associated outcomes..',
    'qualitative',
    'Elkhenany H 2021 M2A-P034-E002 preserves a distinct Rat model context experiment testing HA demilune surface-capping scaffold with endpoint/readout: Surface-capping scaffold was applied after subacute SCI and assessed for repair-associated outcomes..',
    'M2A-P034-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: A Hyaluronic Acid Demilune Scaffold and Polypyrrole-Coated Fibers Carrying Embedded Human Neural Precursor Cells and Curcumin for Surface Capping of Spinal Cord Injuries. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M2A-P034-E002", "paper_tracker_id": "M2A-P034", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M2B-T007", "tracker_id": "M2B-O081"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P034::M2A-P034-E002'
    AND et.evidence_type_name = 'Conductive surface scaffold'
    AND ot.outcome_type_name = 'Surface-capping scaffold was applied after subacute SCI and assessed for repair-associated outcomes.'
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
    'Qiu C 2022 M2A-P035-E002 preserves a distinct Rattus norvegicus experiment testing GelMA scaffold + hAEC-derived neural-like cells with endpoint/readout: hAEC-neural-like cell scaffold was implanted into rat full transection SCI to assess neural circuit and hindlimb recovery..',
    'qualitative',
    'Qiu C 2022 M2A-P035-E002 preserves a distinct Rattus norvegicus experiment testing GelMA scaffold + hAEC-derived neural-like cells with endpoint/readout: hAEC-neural-like cell scaffold was implanted into rat full transection SCI to assess neural circuit and hindlimb recovery..',
    'M2A-P035-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Therapeutic Effect of Biomimetic Scaffold Loaded with Human Amniotic Epithelial Cell-Derived Neural-like Cells for Spinal Cord Injury. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M2A-P035-E002", "paper_tracker_id": "M2A-P035", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M2B-T001", "tracker_id": "M2B-O082"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P035::M2A-P035-E002'
    AND et.evidence_type_name = '3D-printed GelMA microchannel scaffold'
    AND ot.outcome_type_name = 'hAEC-neural-like cell scaffold was implanted into rat full transection SCI to assess neural circuit and hindlimb recovery.'
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
    'Zhang R 2024 M2A-P036-E002 preserves a distinct Rodent model context experiment testing Sequential release SilMA scaffold with endpoint/readout: In vitro and in vivo outcomes assessed inflammation reduction, neuronal differentiation, axonal regeneration, and spinal cord repair..',
    'qualitative',
    'Zhang R 2024 M2A-P036-E002 preserves a distinct Rodent model context experiment testing Sequential release SilMA scaffold with endpoint/readout: In vitro and in vivo outcomes assessed inflammation reduction, neuronal differentiation, axonal regeneration, and spinal cord repair..',
    'M2A-P036-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Dual-phase SilMA hydrogel: a dynamic scaffold for sequential drug release and enhanced spinal cord repair via neural differentiation and immunomodulation. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M2A-P036-E002", "paper_tracker_id": "M2A-P036", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M2B-T003", "tracker_id": "M2B-O083"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P036::M2A-P036-E002'
    AND et.evidence_type_name = 'Sequential-release SilMA scaffold'
    AND ot.outcome_type_name = 'In vitro and in vivo outcomes assessed inflammation reduction, neuronal differentiation, axonal regeneration, and spinal cord repair.'
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
    'Yao S 2024 M2A-P039-E002 preserves a distinct Rat SCI model context experiment testing CNT/GelMA fibers + electrical stimulation with endpoint/readout: In vivo SCI testing assessed aligned conductive scaffold with electrical stimulation for axon regeneration and recovery..',
    'qualitative',
    'Yao S 2024 M2A-P039-E002 preserves a distinct Rat SCI model context experiment testing CNT/GelMA fibers + electrical stimulation with endpoint/readout: In vivo SCI testing assessed aligned conductive scaffold with electrical stimulation for axon regeneration and recovery..',
    'M2A-P039-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Axon-like aligned conductive CNT/GelMA hydrogel fibers combined with electrical stimulation for spinal cord injury recovery. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M2A-P039-E002", "paper_tracker_id": "M2A-P039", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M2B-T001", "tracker_id": "M2B-O086"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P039::M2A-P039-E002'
    AND et.evidence_type_name = 'Conductive aligned hydrogel / electrical stimulation'
    AND ot.outcome_type_name = 'In vivo SCI testing assessed aligned conductive scaffold with electrical stimulation for axon regeneration and recovery.'
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
    'Mehrotra S 2010 M2A-P040-E002 preserves a distinct Scaffold system / SCI bridge context experiment testing Functionalized agarose channel bridge with endpoint/readout: Protein-release agarose strategy was framed as an alternative to genetically engineered BDNF-secreting cells in templated channel bridges..',
    'qualitative',
    'Mehrotra S 2010 M2A-P040-E002 preserves a distinct Scaffold system / SCI bridge context experiment testing Functionalized agarose channel bridge with endpoint/readout: Protein-release agarose strategy was framed as an alternative to genetically engineered BDNF-secreting cells in templated channel bridges..',
    'M2A-P040-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Time Controlled Protein Release from Layer-by-Layer Assembled Multilayer Functionalized Agarose Hydrogels. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M2A-P040-E002", "paper_tracker_id": "M2A-P040", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M2B-T003", "tracker_id": "M2B-O087"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P040::M2A-P040-E002'
    AND et.evidence_type_name = 'Functionalized agarose hydrogel'
    AND ot.outcome_type_name = 'Protein-release agarose strategy was framed as an alternative to genetically engineered BDNF-secreting cells in templated channel bridges.'
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
    'Lai BQ 2014 M2A-P041-E002 preserves a distinct Rattus norvegicus experiment testing Tissue-engineered gelatin sponge neural scaffold with endpoint/readout: Graft effects on myelination, NSC differentiation, axon regeneration, and functional recovery were assessed after complete transection..',
    'qualitative',
    'Lai BQ 2014 M2A-P041-E002 preserves a distinct Rattus norvegicus experiment testing Tissue-engineered gelatin sponge neural scaffold with endpoint/readout: Graft effects on myelination, NSC differentiation, axon regeneration, and functional recovery were assessed after complete transection..',
    'M2A-P041-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Graft of a tissue-engineered neural scaffold serves as a promising strategy to restore myelination after rat spinal cord transection. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M2A-P041-E002", "paper_tracker_id": "M2A-P041", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M2B-T002", "tracker_id": "M2B-O088"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P041::M2A-P041-E002'
    AND et.evidence_type_name = 'Gelatin scaffold plus engineered cells'
    AND ot.outcome_type_name = 'Graft effects on myelination, NSC differentiation, axon regeneration, and functional recovery were assessed after complete transection.'
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
    'Sun Y 2020 M2A-P042-E002 preserves a distinct Rat SCI model context experiment testing 3D-bioprinted collagen/silk scaffold + NSCs with endpoint/readout: In vivo testing assessed nerve regeneration and functional repair after scaffold/cell implantation..',
    'qualitative',
    'Sun Y 2020 M2A-P042-E002 preserves a distinct Rat SCI model context experiment testing 3D-bioprinted collagen/silk scaffold + NSCs with endpoint/readout: In vivo testing assessed nerve regeneration and functional repair after scaffold/cell implantation..',
    'M2A-P042-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Three-dimensional bioprinting collagen/silk fibroin scaffold combined with neural stem cells promotes nerve regeneration after spinal cord injury. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M2A-P042-E002", "paper_tracker_id": "M2A-P042", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M2B-T001", "tracker_id": "M2B-O089"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P042::M2A-P042-E002'
    AND et.evidence_type_name = '3D-bioprinted collagen/silk scaffold'
    AND ot.outcome_type_name = 'In vivo testing assessed nerve regeneration and functional repair after scaffold/cell implantation.'
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
    'Führmann T 2016 M2A-P043-E002 preserves a distinct Rattus norvegicus experiment testing OEC-seeded collagen scaffold with endpoint/readout: Functional improvement was evaluated against axon regeneration through the scaffold, with the abstract reporting lack of correlation..',
    'qualitative',
    'Führmann T 2016 M2A-P043-E002 preserves a distinct Rattus norvegicus experiment testing OEC-seeded collagen scaffold with endpoint/readout: Functional improvement was evaluated against axon regeneration through the scaffold, with the abstract reporting lack of correlation..',
    'M2A-P043-E002 preserves distinct model/timing/intervention/endpoint boundary',
    'Module A tracker',
    'Abstract',
    'medium',
    '{"curator_notes": "Per-experiment atomization backfill from A-layer row; source title: Functional recovery not correlated with axon regeneration through olfactory ensheathing cell-seeded scaffolds in a model of acute spinal cord injury. Existing consensus links remain on original curated observations.", "experiment_tracker_id": "M2A-P043-E002", "paper_tracker_id": "M2A-P043", "quantitative": "NO", "statistics_reported": "Not separately extracted; row added to ensure exact observation-per-experiment coverage.", "topic_id": "M2B-T008", "tracker_id": "M2B-O090"}'
  FROM _m2_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M2A-P043::M2A-P043-E002'
    AND et.evidence_type_name = 'OEC-seeded scaffold'
    AND ot.outcome_type_name = 'Functional improvement was evaluated against axon regeneration through the scaffold, with the abstract reporting lack of correlation.'
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
    'NeuroRegen scaffold plus hUCB-MSC implantation after scar resection is safe and potentially beneficial in chronic complete human SCI.',
    'conclusion',
    'medium',
    'Abstract',
    'medium',
    '{"curator_notes": "\"Potentially beneficial\" should be kept cautious until full clinical endpoints are extracted.", "source_paper_tracker_id": "M2A-P009", "topic_id": "M2B-T006", "tracker_id": "M2B-C002"}'
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
    'Aligned hydrogel tubes provide physical guidance that can integrate with SCI lesions, reduce scarring, guide axons, support some myelination, and improve function.',
    'conclusion',
    'medium',
    'Abstract',
    'medium',
    '{"curator_notes": "Scaffold-only comparator to gelfoam makes this high-value for architecture topic.", "source_paper_tracker_id": "M2A-P005", "topic_id": "M2B-T001", "tracker_id": "M2B-C004"}'
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
    'Conductive aligned GelMA/CNT hydrogel fibers can combine regenerative scaffold guidance with electrical stimulation.',
    'implication',
    'medium',
    'Abstract',
    'medium',
    '{"curator_notes": "Needs full-text extraction for in vivo effect sizes and ES protocol.", "source_paper_tracker_id": "M2A-P039", "topic_id": "M2B-T001", "tracker_id": "M2B-C005"}'
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
    'Decellularized peripheral nerve matrix is a clinically oriented alternative to Matrigel for Schwann-cell transplantation after SCI.',
    'implication',
    'medium',
    'Abstract',
    'medium',
    '{"curator_notes": "Histology benefit stronger than locomotor superiority.", "source_paper_tracker_id": "M2A-P016", "topic_id": "M2B-T002", "tracker_id": "M2B-C007"}'
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
    'Scaffold-delivered NT-3 can improve axonal sprouting and scar histology without necessarily improving motor function.',
    'boundary condition',
    'high',
    'Abstract',
    'medium',
    '{"curator_notes": "Important histology-function dissociation.", "source_paper_tracker_id": "M2A-P025", "topic_id": "M2B-T003", "tracker_id": "M2B-C008"}'
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
    'Sequential release scaffolds are designed to match SCI temporal biology by reducing early inflammation and promoting later neuronal differentiation/regeneration.',
    'mechanistic',
    'medium',
    'Abstract',
    'medium',
    '{"curator_notes": "Plausible design claim; full-text timing needed.", "source_paper_tracker_id": "M2A-P036", "topic_id": "M2B-T003", "tracker_id": "M2B-C009"}'
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
    'Injectable ECM-derived hydrogels can integrate into lesions and support ingrowth, but ECM source and host macrophage/material response are important constraints.',
    'boundary condition',
    'medium',
    'Abstract',
    'medium',
    '{"curator_notes": "Useful for avoiding \"ECM is uniformly pro-regenerative\" overclaim.", "source_paper_tracker_id": "M2A-P014", "topic_id": "M2B-T004", "tracker_id": "M2B-C010"}'
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
    'Large-animal chronic NeuroRegen scaffold plus hUC-MSC implantation after scar removal supports translational feasibility of chronic cavity/scar scaffold repair.',
    'implication',
    'medium',
    'Abstract',
    'medium',
    '{"curator_notes": "Needs full text for functional magnitude and scar-removal details.", "source_paper_tracker_id": "M2A-P015", "topic_id": "M2B-T005", "tracker_id": "M2B-C012"}'
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
    'Surface-applied scaffold patches can modulate the post-SCI inflammatory environment without requiring deep lesion-filling implantation.',
    'implication',
    'medium',
    'Abstract',
    'medium',
    '{"curator_notes": "Distinct intervention geometry.", "source_paper_tracker_id": "M2A-P038", "topic_id": "M2B-T007", "tracker_id": "M2B-C013"}'
  FROM _m2_paper_map p
  WHERE p.tracker_id = 'M2A-P038'
  RETURNING claim_id
)
INSERT INTO _m2_claim_map (tracker_id, claim_id) SELECT 'M2B-C013', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Functional improvement after scaffold/cell treatment should not be assumed to reflect axons regenerating through the scaffold.',
    'boundary condition',
    'high',
    'Abstract',
    'medium',
    '{"curator_notes": "Directly based on negative correlation claim.", "source_paper_tracker_id": "M2A-P043", "topic_id": "M2B-T008", "tracker_id": "M2B-C014"}'
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
    'Acute complete human NeuroRegen scaffold plus MSC implantation is feasible to test in carefully diagnosed complete SCI, but n = 2 is not efficacy-grade evidence.',
    'boundary condition',
    'high',
    'Abstract',
    'medium',
    '{"curator_notes": "Keeps acute clinical signal appropriately constrained.", "source_paper_tracker_id": "M2A-P017", "topic_id": "M2B-T006", "tracker_id": "M2B-C015"}'
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
    'Collagen scaffold plus hUC-MSC repair has translational continuity across rodent, canine, and phase I human contexts.',
    'implication',
    'medium',
    'Abstract',
    'medium',
    '{"curator_notes": "Strong as translational path, weaker as efficacy proof.", "source_paper_tracker_id": "M2A-P033", "topic_id": "M2B-T006", "tracker_id": "M2B-C016"}'
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
    'Biomimetic 3D-printed spinal cord scaffolds can impose lesion-scale architecture that supports host-graft axonal relay formation.',
    'conclusion',
    'medium',
    'Abstract',
    'medium',
    '{"curator_notes": "Confounded by NPC graft but central to architecture topic.", "source_paper_tracker_id": "M2A-P004", "topic_id": "M2B-T001", "tracker_id": "M2B-C017"}'
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
    'Microchannel GelMA scaffolds can pair geometry with neural-like cell placement to improve repair after complete transection.',
    'conclusion',
    'medium',
    'Abstract',
    'medium',
    '{"curator_notes": "Cell and architecture effects not separable.", "source_paper_tracker_id": "M2A-P035", "topic_id": "M2B-T001", "tracker_id": "M2B-C020"}'
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
    'Growth-factor-loaded hydrogels can support tissue ingrowth and functional recovery after complete transection, but material and trophic effects are inseparable.',
    'conclusion',
    'medium',
    'Abstract',
    'medium',
    '{"curator_notes": "Applies to bFGF/HEMA-MOETACL system.", "source_paper_tracker_id": "M2A-P026", "topic_id": "M2B-T003", "tracker_id": "M2B-C026"}'
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
    'Protein-release scaffold methods matter because they can replace cell-based trophic delivery in channel-bridge strategies.',
    'implication',
    'medium',
    'Abstract',
    'medium',
    '{"curator_notes": "Methods anchor, not efficacy anchor.", "source_paper_tracker_id": "M2A-P040", "topic_id": "M2B-T003", "tracker_id": "M2B-C028"}'
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
    'HA hydrogels can be made more or less permissive by the biological identity of incorporated ECM.',
    'conclusion',
    'medium',
    'Abstract',
    'medium',
    '{"curator_notes": "Protoplasmic versus fibrous astrocyte ECM distinction.", "source_paper_tracker_id": "M2A-P032", "topic_id": "M2B-T004", "tracker_id": "M2B-C029"}'
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
    'Surface-capping scaffolds are a distinct repair geometry from implanted lesion bridges and may be useful for modulating exposed injury environments.',
    'implication',
    'medium',
    'Abstract',
    'medium',
    '{"curator_notes": "HA demilune scaffold anchor.", "source_paper_tracker_id": "M2A-P034", "topic_id": "M2B-T007", "tracker_id": "M2B-C034"}'
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
  '{"notes": "Abstract-level clinical support", "strength": "medium", "tracker_id": "M2B-L002"}'
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
  '{"notes": "Histological superiority vs Matrigel; BBB similar", "strength": "medium", "tracker_id": "M2B-L007"}'
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
  '{"notes": "Canine chronic scaffold/cell evidence", "strength": "medium", "tracker_id": "M2B-L012"}'
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
  '{"notes": "n = 2 clinical boundary", "strength": "high", "tracker_id": "M2B-L017"}'
FROM _m2_claim_map c
JOIN _m2_observation_map o ON o.tracker_id = 'M2B-O022'
WHERE c.tracker_id = 'M2B-C015';

INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Multi-species translational continuity", "strength": "medium", "tracker_id": "M2B-L018"}'
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
  '{"notes": "bFGF hydrogel complete transection observation", "strength": "medium", "tracker_id": "M2B-L029"}'
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
  IF experiment_count <> 86 THEN RAISE EXCEPTION 'Unexpected experiment count %', experiment_count; END IF;
  IF observation_count <> 50 THEN RAISE EXCEPTION 'Expected 50 observations, found %', observation_count; END IF;
  IF claim_count <> 36 THEN RAISE EXCEPTION 'Expected 36 claims, found %', claim_count; END IF;
  IF link_count <> 56 THEN RAISE EXCEPTION 'Expected 56 evidence links, found %', link_count; END IF;
  IF consensus_count <> 8 THEN RAISE EXCEPTION 'Expected 8 consensus rows, found %', consensus_count; END IF;
  IF consensus_observation_count <> 54 THEN RAISE EXCEPTION 'Unexpected consensus-observation count %', consensus_observation_count; END IF;
END $$;

COMMIT;
