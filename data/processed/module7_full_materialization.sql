-- Module 7B full first-pass materialization generated from tracker-derived JSON.
-- This script is intended for a fresh database loaded with schema/schema.sql and scripts/seed_controlled_vocab.sql.
BEGIN;

CREATE TEMP TABLE _m7_paper_map (tracker_id TEXT PRIMARY KEY, paper_id INTEGER NOT NULL);
CREATE TEMP TABLE _m7_paradigm_map (tracker_id TEXT PRIMARY KEY, paradigm_id INTEGER NOT NULL);
CREATE TEMP TABLE _m7_experiment_map (tracker_id TEXT PRIMARY KEY, experiment_id INTEGER NOT NULL);
CREATE TEMP TABLE _m7_observation_map (tracker_id TEXT PRIMARY KEY, observation_id INTEGER NOT NULL);
CREATE TEMP TABLE _m7_claim_map (tracker_id TEXT PRIMARY KEY, claim_id INTEGER NOT NULL);
CREATE TEMP TABLE _m7_link_map (tracker_id TEXT PRIMARY KEY, link_id INTEGER NOT NULL);
CREATE TEMP TABLE _m7_consensus_map (tracker_id TEXT PRIMARY KEY, consensus_id INTEGER NOT NULL);

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'The effects of zafirlukast on capsular contracture: preliminary report', 'Scuderi N', 2006,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Clinical breast implant precedent", "module": "Module 7B", "tracker_id": "M7A-P001"}'
  )
  RETURNING paper_id
)
INSERT INTO _m7_paper_map (tracker_id, paper_id) SELECT 'M7A-P001', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Pirfenidone prevents capsular contracture after mammary implantation', 'Gancedo M', 2008,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Capsule fibrosis prevention anchor", "module": "Module 7B", "tracker_id": "M7A-P002"}'
  )
  RETURNING paper_id
)
INSERT INTO _m7_paper_map (tracker_id, paper_id) SELECT 'M7A-P002', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Controlled clinical trial with pirfenidone in the treatment of breast capsular contracture: association of TGF-beta polymorphisms', 'Veras-Castillo ER', 2013,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Human clinical pirfenidone anchor", "module": "Module 7B", "tracker_id": "M7A-P003"}'
  )
  RETURNING paper_id
)
INSERT INTO _m7_paper_map (tracker_id, paper_id) SELECT 'M7A-P003', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Comparison of Cromolyn Sodium, Montelukast, and Zafirlukast Prophylaxis for Capsular Contracture', 'Menku Ozdemir FD', 2022,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Prophylaxis framing directly matches module", "module": "Module 7B", "tracker_id": "M7A-P004"}'
  )
  RETURNING paper_id
)
INSERT INTO _m7_paper_map (tracker_id, paper_id) SELECT 'M7A-P004', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Comparison of Cromolyn Sodium, Montelukast, and Zafirlukast Prophylaxis for Capsular Contracture', 'Bresnick SD', 2023,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Companion/commentary or follow-up source-page row", "module": "Module 7B", "tracker_id": "M7A-P005"}'
  )
  RETURNING paper_id
)
INSERT INTO _m7_paper_map (tracker_id, paper_id) SELECT 'M7A-P005', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Leukotriene Inhibitors in the Prevention of Recurring Capsular Contracture in Secondary Breast Augmentation', 'Procikieviez IO', 2024,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Recurrence-prevention clinical anchor", "module": "Module 7B", "tracker_id": "M7A-P006"}'
  )
  RETURNING paper_id
)
INSERT INTO _m7_paper_map (tracker_id, paper_id) SELECT 'M7A-P006', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Montelukast vs Tranilast Administration in the Prevention of Capsular Contracture in Alloplastic Breast Surgeries: An Experimental Mice Model', 'Xu Y', 2025,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Direct prophylactic host-conditioning comparison", "module": "Module 7B", "tracker_id": "M7A-P007"}'
  )
  RETURNING paper_id
)
INSERT INTO _m7_paper_map (tracker_id, paper_id) SELECT 'M7A-P007', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Tamoxifen reduces silicone implant capsule formation in a mouse model', 'Blum KM', 2022,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Capsule formation reduced in mouse implant model", "module": "Module 7B", "tracker_id": "M7A-P008"}'
  )
  RETURNING paper_id
)
INSERT INTO _m7_paper_map (tracker_id, paper_id) SELECT 'M7A-P008', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Beneficial effects of transdermal administration of tamoxifen on capsular contracture after breast implantation in murine models', 'Okazaki M', 2022,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Boundary: local/transdermal route but recipient-directed", "module": "Module 7B", "tracker_id": "M7A-P009"}'
  )
  RETURNING paper_id
)
INSERT INTO _m7_paper_map (tracker_id, paper_id) SELECT 'M7A-P009', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Preconditioning with monophosphoryl lipid A improves survival of critically ischemic tissue', 'Harder Y', 2005,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Vascular survival rather than fibrosis endpoint", "module": "Module 7B", "tracker_id": "M7A-P010"}'
  )
  RETURNING paper_id
)
INSERT INTO _m7_paper_map (tracker_id, paper_id) SELECT 'M7A-P010', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Remote ischemic preconditioning modulates p38 MAP kinase in rat adipocutaneous flaps', 'Claytor RB', 2007,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Recipient systemic/remote conditioning", "module": "Module 7B", "tracker_id": "M7A-P011"}'
  )
  RETURNING paper_id
)
INSERT INTO _m7_paper_map (tracker_id, paper_id) SELECT 'M7A-P011', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Systemic preconditioning by a prolyl hydroxylase inhibitor promotes prevention of skin flap necrosis via HIF-1-induced bone marrow-derived cells', 'Takaku M', 2012,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Angiogenic host-cell mobilization anchor", "module": "Module 7B", "tracker_id": "M7A-P012"}'
  )
  RETURNING paper_id
)
INSERT INTO _m7_paper_map (tracker_id, paper_id) SELECT 'M7A-P012', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Value of remote ischaemic preconditioning in rat dorsal skin flaps and clamping time', 'Masaoka K', 2016,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Timing/clamping boundary", "module": "Module 7B", "tracker_id": "M7A-P013"}'
  )
  RETURNING paper_id
)
INSERT INTO _m7_paper_map (tracker_id, paper_id) SELECT 'M7A-P013', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Remote ischemic preconditioning in head and neck cancer reconstruction - a randomized controlled trial', 'Krag AE', 2016,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Human reconstructive trial anchor", "module": "Module 7B", "tracker_id": "M7A-P014"}'
  )
  RETURNING paper_id
)
INSERT INTO _m7_paper_map (tracker_id, paper_id) SELECT 'M7A-P014', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Alpha-1 Antitrypsin Enhances Islet Engraftment by Suppression of Instant Blood-Mediated Inflammatory Reaction', 'Wang J', 2017,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "IBMIR/engraftment anchor", "module": "Module 7B", "tracker_id": "M7A-P015"}'
  )
  RETURNING paper_id
)
INSERT INTO _m7_paper_map (tracker_id, paper_id) SELECT 'M7A-P015', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Alpha 1-antitrypsin reduces inflammation and enhances mouse pancreatic islet transplant survival', 'Koulmanda M', 2012,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Mouse graft survival anchor", "module": "Module 7B", "tracker_id": "M7A-P016"}'
  )
  RETURNING paper_id
)
INSERT INTO _m7_paper_map (tracker_id, paper_id) SELECT 'M7A-P016', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Alpha-1 antitrypsin suppresses macrophage activation and promotes islet graft survival after intrahepatic islet transplantation', 'Gou W', 2021,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Macrophage-host response link", "module": "Module 7B", "tracker_id": "M7A-P017"}'
  )
  RETURNING paper_id
)
INSERT INTO _m7_paper_map (tracker_id, paper_id) SELECT 'M7A-P017', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'A randomized controlled pilot trial of etanercept and alpha-1 antitrypsin to improve autologous islet engraftment', 'Abdel-Karim TR', 2023,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Human autologous islet clinical anchor", "module": "Module 7B", "tracker_id": "M7A-P018"}'
  )
  RETURNING paper_id
)
INSERT INTO _m7_paper_map (tracker_id, paper_id) SELECT 'M7A-P018', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Alpha-1 Antitrypsin Augmentation Therapy in Chronic Pancreatitis Patients Undergoing Total Pancreatectomy and Islet Autotransplantation: A Randomized, Controlled Study', 'Wang H', 2024,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Human RCT anchor", "module": "Module 7B", "tracker_id": "M7A-P019"}'
  )
  RETURNING paper_id
)
INSERT INTO _m7_paper_map (tracker_id, paper_id) SELECT 'M7A-P019', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Peri-Transplant Inflammation and Long-Term Diabetes Outcomes Were Not Impacted by Either Etanercept or Alpha-1-Antitrypsin Treatment in Islet Autotransplant Recipients', 'Abdel-Karim TR', 2024,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Important contradiction/limit", "module": "Module 7B", "tracker_id": "M7A-P020"}'
  )
  RETURNING paper_id
)
INSERT INTO _m7_paper_map (tracker_id, paper_id) SELECT 'M7A-P020', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Open Randomized Multicenter Study to Evaluate Safety and Efficacy of Low Molecular Weight Sulfated Dextran in Islet Transplantation', 'von Zur-Muhlen B', 2019,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Clinical complement/coagulation-adjacent host conditioning", "module": "Module 7B", "tracker_id": "M7A-P021"}'
  )
  RETURNING paper_id
)
INSERT INTO _m7_paper_map (tracker_id, paper_id) SELECT 'M7A-P021', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'A precise analysis of C5a inhibitory peptide on inflammatory mediators induced after islet transplantation', 'Nakanishi W', 2011,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Complement phase 1 anchor", "module": "Module 7B", "tracker_id": "M7A-P022"}'
  )
  RETURNING paper_id
)
INSERT INTO _m7_paper_map (tracker_id, paper_id) SELECT 'M7A-P022', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'CCL2/MCP-1 and CXCL12/SDF-1 blockade by L-aptamers improve pancreatic islet engraftment and survival in mouse', 'Citro A', 2019,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Monocyte/chemokine recruitment anchor", "module": "Module 7B", "tracker_id": "M7A-P023"}'
  )
  RETURNING paper_id
)
INSERT INTO _m7_paper_map (tracker_id, paper_id) SELECT 'M7A-P023', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Transplantation of allogeneic islets of Langerhans in the rat liver: effects of macrophage depletion on graft survival and microenvironment activation', 'Bottino R', 1998,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Early microenvironment activation anchor", "module": "Module 7B", "tracker_id": "M7A-P024"}'
  )
  RETURNING paper_id
)
INSERT INTO _m7_paper_map (tracker_id, paper_id) SELECT 'M7A-P024', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Apoptotic cell administration enhances pancreatic islet engraftment by induction of regulatory T cells and tolerogenic dendritic cells', 'Wu C', 2013,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Host immune transition anchor", "module": "Module 7B", "tracker_id": "M7A-P025"}'
  )
  RETURNING paper_id
)
INSERT INTO _m7_paper_map (tracker_id, paper_id) SELECT 'M7A-P025', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Endogenous expansion of regulatory T cells leads to long-term islet graft survival in diabetic NOD mice', 'Shi Q', 2012,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Regulatory host conditioning anchor", "module": "Module 7B", "tracker_id": "M7A-P026"}'
  )
  RETURNING paper_id
)
INSERT INTO _m7_paper_map (tracker_id, paper_id) SELECT 'M7A-P026', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Improvement of Islet Engrafts via Treg Induction Using Immunomodulating Polymeric Tolerogenic Microparticles', 'Neshat SY', 2023,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Boundary: biomaterial immunomodulation but host-directed", "module": "Module 7B", "tracker_id": "M7A-P027"}'
  )
  RETURNING paper_id
)
INSERT INTO _m7_paper_map (tracker_id, paper_id) SELECT 'M7A-P027', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Preventing alloimmune rejection using circular RNA FSCN1-silenced dendritic cells in heart transplantation', 'Wang B', 2021,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Organ tolerance bridge; rejection-heavy", "module": "Module 7B", "tracker_id": "M7A-P028"}'
  )
  RETURNING paper_id
)
INSERT INTO _m7_paper_map (tracker_id, paper_id) SELECT 'M7A-P028', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Mechanisms of tolerance induction in second renal allografts of a chronic rejection model', 'Reutzel-Selke A', 2000,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Chronic rejection/fibrosis-adjacent boundary", "module": "Module 7B", "tracker_id": "M7A-P029"}'
  )
  RETURNING paper_id
)
INSERT INTO _m7_paper_map (tracker_id, paper_id) SELECT 'M7A-P029', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Effects of zileuton and montelukast in mouse experimental spinal cord injury', 'Genovese T', 2008,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "SCI leukotriene conditioning anchor", "module": "Module 7B", "tracker_id": "M7A-P030"}'
  )
  RETURNING paper_id
)
INSERT INTO _m7_paper_map (tracker_id, paper_id) SELECT 'M7A-P030', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'The LTB4-BLT1 axis mediates neutrophil infiltration and secondary injury in experimental spinal cord injury', 'Saiwai H', 2010,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Mechanistic leukotriene/neutrophil anchor", "module": "Module 7B", "tracker_id": "M7A-P031"}'
  )
  RETURNING paper_id
)
INSERT INTO _m7_paper_map (tracker_id, paper_id) SELECT 'M7A-P031', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Zafirlukast in combination with pseudohypericin attenuates spinal cord injury and motor function in experimental mice', 'Chen XG', 2018,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Combination therapy boundary", "module": "Module 7B", "tracker_id": "M7A-P032"}'
  )
  RETURNING paper_id
)
INSERT INTO _m7_paper_map (tracker_id, paper_id) SELECT 'M7A-P032', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Zileuton Ameliorates Neuronal Ferroptosis and Functional Recovery After Spinal Cord Injury', 'Sun P', 2023,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Recent SCI zileuton anchor", "module": "Module 7B", "tracker_id": "M7A-P033"}'
  )
  RETURNING paper_id
)
INSERT INTO _m7_paper_map (tracker_id, paper_id) SELECT 'M7A-P033', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Resolvin D3 Promotes Inflammatory Resolution, Neuroprotection, and Functional Recovery After Spinal Cord Injury', 'Kim J', 2021,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Resolution biology anchor", "module": "Module 7B", "tracker_id": "M7A-P034"}'
  )
  RETURNING paper_id
)
INSERT INTO _m7_paper_map (tracker_id, paper_id) SELECT 'M7A-P034', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Co-Administration of Resolvin D1 and Peripheral Nerve-Derived Stem Cell Spheroids as a Therapeutic Strategy in a Rat Model of Spinal Cord Injury', 'Jeong SY', 2023,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Boundary: co-therapy, not pure host conditioning", "module": "Module 7B", "tracker_id": "M7A-P035"}'
  )
  RETURNING paper_id
)
INSERT INTO _m7_paper_map (tracker_id, paper_id) SELECT 'M7A-P035', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'The Effect of Tranilast 8% Liposomal Gel Versus Placebo on Post-Cesarean Surgical Scars: A Prospective Double-Blind Split-Scar Study', 'Nobata K', 2017,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Boundary: topical scar evidence, not reconstruction implantation", "module": "Module 7B", "tracker_id": "M7A-P036"}'
  )
  RETURNING paper_id
)
INSERT INTO _m7_paper_map (tracker_id, paper_id) SELECT 'M7A-P036', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Nanomicelle-generating Microneedles Loaded With Tranilast for Treatment of Hypertrophic Scars in a Rabbit Model', 'Gao X', 2022,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Boundary: local delivery; useful scar-matrix bridge", "module": "Module 7B", "tracker_id": "M7A-P037"}'
  )
  RETURNING paper_id
)
INSERT INTO _m7_paper_map (tracker_id, paper_id) SELECT 'M7A-P037', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Non-surgical Treatment and Prophylaxis of Capsular Contracture in Mammary Implants: A Systematic Review of Literature', 'Daronch OT', 2025,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Review anchor for implant prophylaxis", "module": "Module 7B", "tracker_id": "M7A-P038"}'
  )
  RETURNING paper_id
)
INSERT INTO _m7_paper_map (tracker_id, paper_id) SELECT 'M7A-P038', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Leukotriene Receptor Antagonists for the Prevention and Treatment of Capsular Contracture: A Systematic Review and Meta-analysis', 'Bin Abdul Aziz O', 2025,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Review anchor for LTRA evidence", "module": "Module 7B", "tracker_id": "M7A-P039"}'
  )
  RETURNING paper_id
)
INSERT INTO _m7_paper_map (tracker_id, paper_id) SELECT 'M7A-P039', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Treatment and Prevention of Periprosthetic Capsular Contracture in Breast Surgery With Prosthesis Using Leukotriene Receptor Antagonists: A Meta-Analysis', 'Pasca A', 2022,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Review anchor for capsule-prevention boundary", "module": "Module 7B", "tracker_id": "M7A-P040"}'
  )
  RETURNING paper_id
)
INSERT INTO _m7_paper_map (tracker_id, paper_id) SELECT 'M7A-P040', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Non-surgical Treatment and Prophylaxis of Capsular Contracture in Mammary Implants', 'Daronch OT', 2025,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Overlaps P038 as review/map source", "module": "Module 7B", "tracker_id": "M7A-R001"}'
  )
  RETURNING paper_id
)
INSERT INTO _m7_paper_map (tracker_id, paper_id) SELECT 'M7A-R001', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Leukotriene Receptor Antagonists for the Prevention and Treatment of Capsular Contracture', 'Bin Abdul Aziz O', 2025,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Capsule prevention and treatment synthesis", "module": "Module 7B", "tracker_id": "M7A-R002"}'
  )
  RETURNING paper_id
)
INSERT INTO _m7_paper_map (tracker_id, paper_id) SELECT 'M7A-R002', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Treatment and Prevention of Periprosthetic Capsular Contracture Using Leukotriene Receptor Antagonists', 'Pasca A', 2022,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Clinical evidence strength boundary", "module": "Module 7B", "tracker_id": "M7A-R003"}'
  )
  RETURNING paper_id
)
INSERT INTO _m7_paper_map (tracker_id, paper_id) SELECT 'M7A-R003', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'An old dream revitalised: preconditioning strategies to protect surgical flaps from critical ischaemia and ischaemia-reperfusion injury', 'Harder Y', 2008,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Vascular conditioning map", "module": "Module 7B", "tracker_id": "M7A-R004"}'
  )
  RETURNING paper_id
)
INSERT INTO _m7_paper_map (tracker_id, paper_id) SELECT 'M7A-R004', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Early inflammatory loss and engraftment barriers in islet transplantation', 'Shapiro AMJ / islet transplant review set', 2020,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "IBMIR and engraftment framing", "module": "Module 7B", "tracker_id": "M7A-R005"}'
  )
  RETURNING paper_id
)
INSERT INTO _m7_paper_map (tracker_id, paper_id) SELECT 'M7A-R005', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Improving diagnostic workup following traumatic spinal cord injury', 'Hupp M / SCI biomarker and lesion-bed review set', 2021,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Bridges Module 6 and Module 7", "module": "Module 7B", "tracker_id": "M7A-R006"}'
  )
  RETURNING paper_id
)
INSERT INTO _m7_paper_map (tracker_id, paper_id) SELECT 'M7A-R006', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Pro-resolving lipid mediators in tissue repair and inflammation resolution', 'Serhan CN / resolution biology review set', 2014,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Mechanistic frame for resolvin rows", "module": "Module 7B", "tracker_id": "M7A-R007"}'
  )
  RETURNING paper_id
)
INSERT INTO _m7_paper_map (tracker_id, paper_id) SELECT 'M7A-R007', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO Paper (title, authors, publication_year, journal, volume, issue, pages, doi, pmid, url, abstract)
  VALUES (
    'Macrophage-fibroblast interactions in repair and fibrosis', 'Wynn TA / fibrosis repair review set', 2016,
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    NULL, '{"curator_notes": "Cross-field conceptual anchor", "module": "Module 7B", "tracker_id": "M7A-R008"}'
  )
  RETURNING paper_id
)
INSERT INTO _m7_paper_map (tracker_id, paper_id) SELECT 'M7A-R008', paper_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 7B curated evidence extraction',
    'First-pass Module 7B host fibroinflammatory conditioning curation for M7A-P001',
    'Tracker-derived materialization from Module_7B_TRACKER.md'
  FROM _m7_paper_map WHERE tracker_id = 'M7A-P001'
  RETURNING paradigm_id
)
INSERT INTO _m7_paradigm_map (tracker_id, paradigm_id) SELECT 'M7A-P001', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 7B curated evidence extraction',
    'First-pass Module 7B host fibroinflammatory conditioning curation for M7A-P002',
    'Tracker-derived materialization from Module_7B_TRACKER.md'
  FROM _m7_paper_map WHERE tracker_id = 'M7A-P002'
  RETURNING paradigm_id
)
INSERT INTO _m7_paradigm_map (tracker_id, paradigm_id) SELECT 'M7A-P002', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 7B curated evidence extraction',
    'First-pass Module 7B host fibroinflammatory conditioning curation for M7A-P003',
    'Tracker-derived materialization from Module_7B_TRACKER.md'
  FROM _m7_paper_map WHERE tracker_id = 'M7A-P003'
  RETURNING paradigm_id
)
INSERT INTO _m7_paradigm_map (tracker_id, paradigm_id) SELECT 'M7A-P003', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 7B curated evidence extraction',
    'First-pass Module 7B host fibroinflammatory conditioning curation for M7A-P004',
    'Tracker-derived materialization from Module_7B_TRACKER.md'
  FROM _m7_paper_map WHERE tracker_id = 'M7A-P004'
  RETURNING paradigm_id
)
INSERT INTO _m7_paradigm_map (tracker_id, paradigm_id) SELECT 'M7A-P004', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 7B curated evidence extraction',
    'First-pass Module 7B host fibroinflammatory conditioning curation for M7A-P005',
    'Tracker-derived materialization from Module_7B_TRACKER.md'
  FROM _m7_paper_map WHERE tracker_id = 'M7A-P005'
  RETURNING paradigm_id
)
INSERT INTO _m7_paradigm_map (tracker_id, paradigm_id) SELECT 'M7A-P005', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 7B curated evidence extraction',
    'First-pass Module 7B host fibroinflammatory conditioning curation for M7A-P006',
    'Tracker-derived materialization from Module_7B_TRACKER.md'
  FROM _m7_paper_map WHERE tracker_id = 'M7A-P006'
  RETURNING paradigm_id
)
INSERT INTO _m7_paradigm_map (tracker_id, paradigm_id) SELECT 'M7A-P006', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 7B curated evidence extraction',
    'First-pass Module 7B host fibroinflammatory conditioning curation for M7A-P007',
    'Tracker-derived materialization from Module_7B_TRACKER.md'
  FROM _m7_paper_map WHERE tracker_id = 'M7A-P007'
  RETURNING paradigm_id
)
INSERT INTO _m7_paradigm_map (tracker_id, paradigm_id) SELECT 'M7A-P007', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 7B curated evidence extraction',
    'First-pass Module 7B host fibroinflammatory conditioning curation for M7A-P008',
    'Tracker-derived materialization from Module_7B_TRACKER.md'
  FROM _m7_paper_map WHERE tracker_id = 'M7A-P008'
  RETURNING paradigm_id
)
INSERT INTO _m7_paradigm_map (tracker_id, paradigm_id) SELECT 'M7A-P008', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 7B curated evidence extraction',
    'First-pass Module 7B host fibroinflammatory conditioning curation for M7A-P009',
    'Tracker-derived materialization from Module_7B_TRACKER.md'
  FROM _m7_paper_map WHERE tracker_id = 'M7A-P009'
  RETURNING paradigm_id
)
INSERT INTO _m7_paradigm_map (tracker_id, paradigm_id) SELECT 'M7A-P009', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 7B curated evidence extraction',
    'First-pass Module 7B host fibroinflammatory conditioning curation for M7A-P010',
    'Tracker-derived materialization from Module_7B_TRACKER.md'
  FROM _m7_paper_map WHERE tracker_id = 'M7A-P010'
  RETURNING paradigm_id
)
INSERT INTO _m7_paradigm_map (tracker_id, paradigm_id) SELECT 'M7A-P010', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 7B curated evidence extraction',
    'First-pass Module 7B host fibroinflammatory conditioning curation for M7A-P011',
    'Tracker-derived materialization from Module_7B_TRACKER.md'
  FROM _m7_paper_map WHERE tracker_id = 'M7A-P011'
  RETURNING paradigm_id
)
INSERT INTO _m7_paradigm_map (tracker_id, paradigm_id) SELECT 'M7A-P011', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 7B curated evidence extraction',
    'First-pass Module 7B host fibroinflammatory conditioning curation for M7A-P012',
    'Tracker-derived materialization from Module_7B_TRACKER.md'
  FROM _m7_paper_map WHERE tracker_id = 'M7A-P012'
  RETURNING paradigm_id
)
INSERT INTO _m7_paradigm_map (tracker_id, paradigm_id) SELECT 'M7A-P012', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 7B curated evidence extraction',
    'First-pass Module 7B host fibroinflammatory conditioning curation for M7A-P013',
    'Tracker-derived materialization from Module_7B_TRACKER.md'
  FROM _m7_paper_map WHERE tracker_id = 'M7A-P013'
  RETURNING paradigm_id
)
INSERT INTO _m7_paradigm_map (tracker_id, paradigm_id) SELECT 'M7A-P013', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 7B curated evidence extraction',
    'First-pass Module 7B host fibroinflammatory conditioning curation for M7A-P014',
    'Tracker-derived materialization from Module_7B_TRACKER.md'
  FROM _m7_paper_map WHERE tracker_id = 'M7A-P014'
  RETURNING paradigm_id
)
INSERT INTO _m7_paradigm_map (tracker_id, paradigm_id) SELECT 'M7A-P014', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 7B curated evidence extraction',
    'First-pass Module 7B host fibroinflammatory conditioning curation for M7A-P015',
    'Tracker-derived materialization from Module_7B_TRACKER.md'
  FROM _m7_paper_map WHERE tracker_id = 'M7A-P015'
  RETURNING paradigm_id
)
INSERT INTO _m7_paradigm_map (tracker_id, paradigm_id) SELECT 'M7A-P015', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 7B curated evidence extraction',
    'First-pass Module 7B host fibroinflammatory conditioning curation for M7A-P016',
    'Tracker-derived materialization from Module_7B_TRACKER.md'
  FROM _m7_paper_map WHERE tracker_id = 'M7A-P016'
  RETURNING paradigm_id
)
INSERT INTO _m7_paradigm_map (tracker_id, paradigm_id) SELECT 'M7A-P016', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 7B curated evidence extraction',
    'First-pass Module 7B host fibroinflammatory conditioning curation for M7A-P017',
    'Tracker-derived materialization from Module_7B_TRACKER.md'
  FROM _m7_paper_map WHERE tracker_id = 'M7A-P017'
  RETURNING paradigm_id
)
INSERT INTO _m7_paradigm_map (tracker_id, paradigm_id) SELECT 'M7A-P017', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 7B curated evidence extraction',
    'First-pass Module 7B host fibroinflammatory conditioning curation for M7A-P018',
    'Tracker-derived materialization from Module_7B_TRACKER.md'
  FROM _m7_paper_map WHERE tracker_id = 'M7A-P018'
  RETURNING paradigm_id
)
INSERT INTO _m7_paradigm_map (tracker_id, paradigm_id) SELECT 'M7A-P018', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 7B curated evidence extraction',
    'First-pass Module 7B host fibroinflammatory conditioning curation for M7A-P019',
    'Tracker-derived materialization from Module_7B_TRACKER.md'
  FROM _m7_paper_map WHERE tracker_id = 'M7A-P019'
  RETURNING paradigm_id
)
INSERT INTO _m7_paradigm_map (tracker_id, paradigm_id) SELECT 'M7A-P019', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 7B curated evidence extraction',
    'First-pass Module 7B host fibroinflammatory conditioning curation for M7A-P020',
    'Tracker-derived materialization from Module_7B_TRACKER.md'
  FROM _m7_paper_map WHERE tracker_id = 'M7A-P020'
  RETURNING paradigm_id
)
INSERT INTO _m7_paradigm_map (tracker_id, paradigm_id) SELECT 'M7A-P020', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 7B curated evidence extraction',
    'First-pass Module 7B host fibroinflammatory conditioning curation for M7A-P021',
    'Tracker-derived materialization from Module_7B_TRACKER.md'
  FROM _m7_paper_map WHERE tracker_id = 'M7A-P021'
  RETURNING paradigm_id
)
INSERT INTO _m7_paradigm_map (tracker_id, paradigm_id) SELECT 'M7A-P021', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 7B curated evidence extraction',
    'First-pass Module 7B host fibroinflammatory conditioning curation for M7A-P022',
    'Tracker-derived materialization from Module_7B_TRACKER.md'
  FROM _m7_paper_map WHERE tracker_id = 'M7A-P022'
  RETURNING paradigm_id
)
INSERT INTO _m7_paradigm_map (tracker_id, paradigm_id) SELECT 'M7A-P022', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 7B curated evidence extraction',
    'First-pass Module 7B host fibroinflammatory conditioning curation for M7A-P023',
    'Tracker-derived materialization from Module_7B_TRACKER.md'
  FROM _m7_paper_map WHERE tracker_id = 'M7A-P023'
  RETURNING paradigm_id
)
INSERT INTO _m7_paradigm_map (tracker_id, paradigm_id) SELECT 'M7A-P023', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 7B curated evidence extraction',
    'First-pass Module 7B host fibroinflammatory conditioning curation for M7A-P024',
    'Tracker-derived materialization from Module_7B_TRACKER.md'
  FROM _m7_paper_map WHERE tracker_id = 'M7A-P024'
  RETURNING paradigm_id
)
INSERT INTO _m7_paradigm_map (tracker_id, paradigm_id) SELECT 'M7A-P024', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 7B curated evidence extraction',
    'First-pass Module 7B host fibroinflammatory conditioning curation for M7A-P025',
    'Tracker-derived materialization from Module_7B_TRACKER.md'
  FROM _m7_paper_map WHERE tracker_id = 'M7A-P025'
  RETURNING paradigm_id
)
INSERT INTO _m7_paradigm_map (tracker_id, paradigm_id) SELECT 'M7A-P025', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 7B curated evidence extraction',
    'First-pass Module 7B host fibroinflammatory conditioning curation for M7A-P026',
    'Tracker-derived materialization from Module_7B_TRACKER.md'
  FROM _m7_paper_map WHERE tracker_id = 'M7A-P026'
  RETURNING paradigm_id
)
INSERT INTO _m7_paradigm_map (tracker_id, paradigm_id) SELECT 'M7A-P026', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 7B curated evidence extraction',
    'First-pass Module 7B host fibroinflammatory conditioning curation for M7A-P027',
    'Tracker-derived materialization from Module_7B_TRACKER.md'
  FROM _m7_paper_map WHERE tracker_id = 'M7A-P027'
  RETURNING paradigm_id
)
INSERT INTO _m7_paradigm_map (tracker_id, paradigm_id) SELECT 'M7A-P027', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 7B curated evidence extraction',
    'First-pass Module 7B host fibroinflammatory conditioning curation for M7A-P028',
    'Tracker-derived materialization from Module_7B_TRACKER.md'
  FROM _m7_paper_map WHERE tracker_id = 'M7A-P028'
  RETURNING paradigm_id
)
INSERT INTO _m7_paradigm_map (tracker_id, paradigm_id) SELECT 'M7A-P028', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 7B curated evidence extraction',
    'First-pass Module 7B host fibroinflammatory conditioning curation for M7A-P029',
    'Tracker-derived materialization from Module_7B_TRACKER.md'
  FROM _m7_paper_map WHERE tracker_id = 'M7A-P029'
  RETURNING paradigm_id
)
INSERT INTO _m7_paradigm_map (tracker_id, paradigm_id) SELECT 'M7A-P029', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 7B curated evidence extraction',
    'First-pass Module 7B host fibroinflammatory conditioning curation for M7A-P030',
    'Tracker-derived materialization from Module_7B_TRACKER.md'
  FROM _m7_paper_map WHERE tracker_id = 'M7A-P030'
  RETURNING paradigm_id
)
INSERT INTO _m7_paradigm_map (tracker_id, paradigm_id) SELECT 'M7A-P030', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 7B curated evidence extraction',
    'First-pass Module 7B host fibroinflammatory conditioning curation for M7A-P031',
    'Tracker-derived materialization from Module_7B_TRACKER.md'
  FROM _m7_paper_map WHERE tracker_id = 'M7A-P031'
  RETURNING paradigm_id
)
INSERT INTO _m7_paradigm_map (tracker_id, paradigm_id) SELECT 'M7A-P031', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 7B curated evidence extraction',
    'First-pass Module 7B host fibroinflammatory conditioning curation for M7A-P032',
    'Tracker-derived materialization from Module_7B_TRACKER.md'
  FROM _m7_paper_map WHERE tracker_id = 'M7A-P032'
  RETURNING paradigm_id
)
INSERT INTO _m7_paradigm_map (tracker_id, paradigm_id) SELECT 'M7A-P032', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 7B curated evidence extraction',
    'First-pass Module 7B host fibroinflammatory conditioning curation for M7A-P033',
    'Tracker-derived materialization from Module_7B_TRACKER.md'
  FROM _m7_paper_map WHERE tracker_id = 'M7A-P033'
  RETURNING paradigm_id
)
INSERT INTO _m7_paradigm_map (tracker_id, paradigm_id) SELECT 'M7A-P033', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 7B curated evidence extraction',
    'First-pass Module 7B host fibroinflammatory conditioning curation for M7A-P034',
    'Tracker-derived materialization from Module_7B_TRACKER.md'
  FROM _m7_paper_map WHERE tracker_id = 'M7A-P034'
  RETURNING paradigm_id
)
INSERT INTO _m7_paradigm_map (tracker_id, paradigm_id) SELECT 'M7A-P034', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 7B curated evidence extraction',
    'First-pass Module 7B host fibroinflammatory conditioning curation for M7A-P035',
    'Tracker-derived materialization from Module_7B_TRACKER.md'
  FROM _m7_paper_map WHERE tracker_id = 'M7A-P035'
  RETURNING paradigm_id
)
INSERT INTO _m7_paradigm_map (tracker_id, paradigm_id) SELECT 'M7A-P035', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 7B curated evidence extraction',
    'First-pass Module 7B host fibroinflammatory conditioning curation for M7A-P036',
    'Tracker-derived materialization from Module_7B_TRACKER.md'
  FROM _m7_paper_map WHERE tracker_id = 'M7A-P036'
  RETURNING paradigm_id
)
INSERT INTO _m7_paradigm_map (tracker_id, paradigm_id) SELECT 'M7A-P036', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 7B curated evidence extraction',
    'First-pass Module 7B host fibroinflammatory conditioning curation for M7A-P037',
    'Tracker-derived materialization from Module_7B_TRACKER.md'
  FROM _m7_paper_map WHERE tracker_id = 'M7A-P037'
  RETURNING paradigm_id
)
INSERT INTO _m7_paradigm_map (tracker_id, paradigm_id) SELECT 'M7A-P037', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 7B curated evidence extraction',
    'First-pass Module 7B host fibroinflammatory conditioning curation for M7A-P038',
    'Tracker-derived materialization from Module_7B_TRACKER.md'
  FROM _m7_paper_map WHERE tracker_id = 'M7A-P038'
  RETURNING paradigm_id
)
INSERT INTO _m7_paradigm_map (tracker_id, paradigm_id) SELECT 'M7A-P038', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 7B curated evidence extraction',
    'First-pass Module 7B host fibroinflammatory conditioning curation for M7A-P039',
    'Tracker-derived materialization from Module_7B_TRACKER.md'
  FROM _m7_paper_map WHERE tracker_id = 'M7A-P039'
  RETURNING paradigm_id
)
INSERT INTO _m7_paradigm_map (tracker_id, paradigm_id) SELECT 'M7A-P039', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 7B curated evidence extraction',
    'First-pass Module 7B host fibroinflammatory conditioning curation for M7A-P040',
    'Tracker-derived materialization from Module_7B_TRACKER.md'
  FROM _m7_paper_map WHERE tracker_id = 'M7A-P040'
  RETURNING paradigm_id
)
INSERT INTO _m7_paradigm_map (tracker_id, paradigm_id) SELECT 'M7A-P040', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 7B curated evidence extraction',
    'First-pass Module 7B host fibroinflammatory conditioning curation for M7A-R001',
    'Tracker-derived materialization from Module_7B_TRACKER.md'
  FROM _m7_paper_map WHERE tracker_id = 'M7A-R001'
  RETURNING paradigm_id
)
INSERT INTO _m7_paradigm_map (tracker_id, paradigm_id) SELECT 'M7A-R001', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 7B curated evidence extraction',
    'First-pass Module 7B host fibroinflammatory conditioning curation for M7A-R002',
    'Tracker-derived materialization from Module_7B_TRACKER.md'
  FROM _m7_paper_map WHERE tracker_id = 'M7A-R002'
  RETURNING paradigm_id
)
INSERT INTO _m7_paradigm_map (tracker_id, paradigm_id) SELECT 'M7A-R002', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 7B curated evidence extraction',
    'First-pass Module 7B host fibroinflammatory conditioning curation for M7A-R003',
    'Tracker-derived materialization from Module_7B_TRACKER.md'
  FROM _m7_paper_map WHERE tracker_id = 'M7A-R003'
  RETURNING paradigm_id
)
INSERT INTO _m7_paradigm_map (tracker_id, paradigm_id) SELECT 'M7A-R003', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 7B curated evidence extraction',
    'First-pass Module 7B host fibroinflammatory conditioning curation for M7A-R004',
    'Tracker-derived materialization from Module_7B_TRACKER.md'
  FROM _m7_paper_map WHERE tracker_id = 'M7A-R004'
  RETURNING paradigm_id
)
INSERT INTO _m7_paradigm_map (tracker_id, paradigm_id) SELECT 'M7A-R004', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 7B curated evidence extraction',
    'First-pass Module 7B host fibroinflammatory conditioning curation for M7A-R005',
    'Tracker-derived materialization from Module_7B_TRACKER.md'
  FROM _m7_paper_map WHERE tracker_id = 'M7A-R005'
  RETURNING paradigm_id
)
INSERT INTO _m7_paradigm_map (tracker_id, paradigm_id) SELECT 'M7A-R005', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 7B curated evidence extraction',
    'First-pass Module 7B host fibroinflammatory conditioning curation for M7A-R006',
    'Tracker-derived materialization from Module_7B_TRACKER.md'
  FROM _m7_paper_map WHERE tracker_id = 'M7A-R006'
  RETURNING paradigm_id
)
INSERT INTO _m7_paradigm_map (tracker_id, paradigm_id) SELECT 'M7A-R006', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 7B curated evidence extraction',
    'First-pass Module 7B host fibroinflammatory conditioning curation for M7A-R007',
    'Tracker-derived materialization from Module_7B_TRACKER.md'
  FROM _m7_paper_map WHERE tracker_id = 'M7A-R007'
  RETURNING paradigm_id
)
INSERT INTO _m7_paradigm_map (tracker_id, paradigm_id) SELECT 'M7A-R007', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO ExperimentalParadigm (paper_id, paradigm_name, description, methodology)
  SELECT paper_id, 'Module 7B curated evidence extraction',
    'First-pass Module 7B host fibroinflammatory conditioning curation for M7A-R008',
    'Tracker-derived materialization from Module_7B_TRACKER.md'
  FROM _m7_paper_map WHERE tracker_id = 'M7A-R008'
  RETURNING paradigm_id
)
INSERT INTO _m7_paradigm_map (tracker_id, paradigm_id) SELECT 'M7A-R008', paradigm_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract',
    'Tracker experiment M7A-P001-E001',
    'Module 7B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M7B-O001"], "source_experiment_tracker_id": "M7A-P001-E001", "source_paper_tracker_id": "M7A-P001", "tracker_key": "M7A-P001::M7A-P001-E001"}'
  FROM _m7_paper_map p
  JOIN _m7_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M7A-P001'
  RETURNING experiment_id
)
INSERT INTO _m7_experiment_map (tracker_id, experiment_id) SELECT 'M7A-P001::M7A-P001-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract',
    'Tracker experiment M7A-P002-E001',
    'Module 7B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M7B-O002"], "source_experiment_tracker_id": "M7A-P002-E001", "source_paper_tracker_id": "M7A-P002", "tracker_key": "M7A-P002::M7A-P002-E001"}'
  FROM _m7_paper_map p
  JOIN _m7_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M7A-P002'
  RETURNING experiment_id
)
INSERT INTO _m7_experiment_map (tracker_id, experiment_id) SELECT 'M7A-P002::M7A-P002-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract',
    'Tracker experiment M7A-P003-E001',
    'Module 7B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M7B-O003"], "source_experiment_tracker_id": "M7A-P003-E001", "source_paper_tracker_id": "M7A-P003", "tracker_key": "M7A-P003::M7A-P003-E001"}'
  FROM _m7_paper_map p
  JOIN _m7_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M7A-P003'
  RETURNING experiment_id
)
INSERT INTO _m7_experiment_map (tracker_id, experiment_id) SELECT 'M7A-P003::M7A-P003-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M7A-P004-E001',
    'Module 7B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M7B-O004"], "source_experiment_tracker_id": "M7A-P004-E001", "source_paper_tracker_id": "M7A-P004", "tracker_key": "M7A-P004::M7A-P004-E001"}'
  FROM _m7_paper_map p
  JOIN _m7_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M7A-P004'
  RETURNING experiment_id
)
INSERT INTO _m7_experiment_map (tracker_id, experiment_id) SELECT 'M7A-P004::M7A-P004-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Source page',
    'Tracker experiment M7A-P005-E001',
    'Module 7B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M7B-O005"], "source_experiment_tracker_id": "M7A-P005-E001", "source_paper_tracker_id": "M7A-P005", "tracker_key": "M7A-P005::M7A-P005-E001"}'
  FROM _m7_paper_map p
  JOIN _m7_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M7A-P005'
  RETURNING experiment_id
)
INSERT INTO _m7_experiment_map (tracker_id, experiment_id) SELECT 'M7A-P005::M7A-P005-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M7A-P006-E001',
    'Module 7B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M7B-O006"], "source_experiment_tracker_id": "M7A-P006-E001", "source_paper_tracker_id": "M7A-P006", "tracker_key": "M7A-P006::M7A-P006-E001"}'
  FROM _m7_paper_map p
  JOIN _m7_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M7A-P006'
  RETURNING experiment_id
)
INSERT INTO _m7_experiment_map (tracker_id, experiment_id) SELECT 'M7A-P006::M7A-P006-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M7A-P007-E001',
    'Module 7B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M7B-O007"], "source_experiment_tracker_id": "M7A-P007-E001", "source_paper_tracker_id": "M7A-P007", "tracker_key": "M7A-P007::M7A-P007-E001"}'
  FROM _m7_paper_map p
  JOIN _m7_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M7A-P007'
  RETURNING experiment_id
)
INSERT INTO _m7_experiment_map (tracker_id, experiment_id) SELECT 'M7A-P007::M7A-P007-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M7A-P008-E001',
    'Module 7B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M7B-O008"], "source_experiment_tracker_id": "M7A-P008-E001", "source_paper_tracker_id": "M7A-P008", "tracker_key": "M7A-P008::M7A-P008-E001"}'
  FROM _m7_paper_map p
  JOIN _m7_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M7A-P008'
  RETURNING experiment_id
)
INSERT INTO _m7_experiment_map (tracker_id, experiment_id) SELECT 'M7A-P008::M7A-P008-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M7A-P009-E001',
    'Module 7B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M7B-O009"], "source_experiment_tracker_id": "M7A-P009-E001", "source_paper_tracker_id": "M7A-P009", "tracker_key": "M7A-P009::M7A-P009-E001"}'
  FROM _m7_paper_map p
  JOIN _m7_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M7A-P009'
  RETURNING experiment_id
)
INSERT INTO _m7_experiment_map (tracker_id, experiment_id) SELECT 'M7A-P009::M7A-P009-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract',
    'Tracker experiment M7A-P010-E001',
    'Module 7B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M7B-O010"], "source_experiment_tracker_id": "M7A-P010-E001", "source_paper_tracker_id": "M7A-P010", "tracker_key": "M7A-P010::M7A-P010-E001"}'
  FROM _m7_paper_map p
  JOIN _m7_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M7A-P010'
  RETURNING experiment_id
)
INSERT INTO _m7_experiment_map (tracker_id, experiment_id) SELECT 'M7A-P010::M7A-P010-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract',
    'Tracker experiment M7A-P011-E001',
    'Module 7B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M7B-O011"], "source_experiment_tracker_id": "M7A-P011-E001", "source_paper_tracker_id": "M7A-P011", "tracker_key": "M7A-P011::M7A-P011-E001"}'
  FROM _m7_paper_map p
  JOIN _m7_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M7A-P011'
  RETURNING experiment_id
)
INSERT INTO _m7_experiment_map (tracker_id, experiment_id) SELECT 'M7A-P011::M7A-P011-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M7A-P012-E001',
    'Module 7B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M7B-O012"], "source_experiment_tracker_id": "M7A-P012-E001", "source_paper_tracker_id": "M7A-P012", "tracker_key": "M7A-P012::M7A-P012-E001"}'
  FROM _m7_paper_map p
  JOIN _m7_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M7A-P012'
  RETURNING experiment_id
)
INSERT INTO _m7_experiment_map (tracker_id, experiment_id) SELECT 'M7A-P012::M7A-P012-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract',
    'Tracker experiment M7A-P013-E001',
    'Module 7B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M7B-O013"], "source_experiment_tracker_id": "M7A-P013-E001", "source_paper_tracker_id": "M7A-P013", "tracker_key": "M7A-P013::M7A-P013-E001"}'
  FROM _m7_paper_map p
  JOIN _m7_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M7A-P013'
  RETURNING experiment_id
)
INSERT INTO _m7_experiment_map (tracker_id, experiment_id) SELECT 'M7A-P013::M7A-P013-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract',
    'Tracker experiment M7A-P014-E001',
    'Module 7B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M7B-O014"], "source_experiment_tracker_id": "M7A-P014-E001", "source_paper_tracker_id": "M7A-P014", "tracker_key": "M7A-P014::M7A-P014-E001"}'
  FROM _m7_paper_map p
  JOIN _m7_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M7A-P014'
  RETURNING experiment_id
)
INSERT INTO _m7_experiment_map (tracker_id, experiment_id) SELECT 'M7A-P014::M7A-P014-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M7A-P015-E001',
    'Module 7B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M7B-O015"], "source_experiment_tracker_id": "M7A-P015-E001", "source_paper_tracker_id": "M7A-P015", "tracker_key": "M7A-P015::M7A-P015-E001"}'
  FROM _m7_paper_map p
  JOIN _m7_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M7A-P015'
  RETURNING experiment_id
)
INSERT INTO _m7_experiment_map (tracker_id, experiment_id) SELECT 'M7A-P015::M7A-P015-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract',
    'Tracker experiment M7A-P016-E001',
    'Module 7B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M7B-O016"], "source_experiment_tracker_id": "M7A-P016-E001", "source_paper_tracker_id": "M7A-P016", "tracker_key": "M7A-P016::M7A-P016-E001"}'
  FROM _m7_paper_map p
  JOIN _m7_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M7A-P016'
  RETURNING experiment_id
)
INSERT INTO _m7_experiment_map (tracker_id, experiment_id) SELECT 'M7A-P016::M7A-P016-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M7A-P017-E001',
    'Module 7B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M7B-O017"], "source_experiment_tracker_id": "M7A-P017-E001", "source_paper_tracker_id": "M7A-P017", "tracker_key": "M7A-P017::M7A-P017-E001"}'
  FROM _m7_paper_map p
  JOIN _m7_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M7A-P017'
  RETURNING experiment_id
)
INSERT INTO _m7_experiment_map (tracker_id, experiment_id) SELECT 'M7A-P017::M7A-P017-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M7A-P018-E001',
    'Module 7B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M7B-O018"], "source_experiment_tracker_id": "M7A-P018-E001", "source_paper_tracker_id": "M7A-P018", "tracker_key": "M7A-P018::M7A-P018-E001"}'
  FROM _m7_paper_map p
  JOIN _m7_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M7A-P018'
  RETURNING experiment_id
)
INSERT INTO _m7_experiment_map (tracker_id, experiment_id) SELECT 'M7A-P018::M7A-P018-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M7A-P019-E001',
    'Module 7B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M7B-O019"], "source_experiment_tracker_id": "M7A-P019-E001", "source_paper_tracker_id": "M7A-P019", "tracker_key": "M7A-P019::M7A-P019-E001"}'
  FROM _m7_paper_map p
  JOIN _m7_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M7A-P019'
  RETURNING experiment_id
)
INSERT INTO _m7_experiment_map (tracker_id, experiment_id) SELECT 'M7A-P019::M7A-P019-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M7A-P020-E001',
    'Module 7B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M7B-O020"], "source_experiment_tracker_id": "M7A-P020-E001", "source_paper_tracker_id": "M7A-P020", "tracker_key": "M7A-P020::M7A-P020-E001"}'
  FROM _m7_paper_map p
  JOIN _m7_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M7A-P020'
  RETURNING experiment_id
)
INSERT INTO _m7_experiment_map (tracker_id, experiment_id) SELECT 'M7A-P020::M7A-P020-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M7A-P021-E001',
    'Module 7B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M7B-O021"], "source_experiment_tracker_id": "M7A-P021-E001", "source_paper_tracker_id": "M7A-P021", "tracker_key": "M7A-P021::M7A-P021-E001"}'
  FROM _m7_paper_map p
  JOIN _m7_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M7A-P021'
  RETURNING experiment_id
)
INSERT INTO _m7_experiment_map (tracker_id, experiment_id) SELECT 'M7A-P021::M7A-P021-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract',
    'Tracker experiment M7A-P022-E001',
    'Module 7B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M7B-O022"], "source_experiment_tracker_id": "M7A-P022-E001", "source_paper_tracker_id": "M7A-P022", "tracker_key": "M7A-P022::M7A-P022-E001"}'
  FROM _m7_paper_map p
  JOIN _m7_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M7A-P022'
  RETURNING experiment_id
)
INSERT INTO _m7_experiment_map (tracker_id, experiment_id) SELECT 'M7A-P022::M7A-P022-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M7A-P023-E001',
    'Module 7B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M7B-O023"], "source_experiment_tracker_id": "M7A-P023-E001", "source_paper_tracker_id": "M7A-P023", "tracker_key": "M7A-P023::M7A-P023-E001"}'
  FROM _m7_paper_map p
  JOIN _m7_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M7A-P023'
  RETURNING experiment_id
)
INSERT INTO _m7_experiment_map (tracker_id, experiment_id) SELECT 'M7A-P023::M7A-P023-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract',
    'Tracker experiment M7A-P024-E001',
    'Module 7B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M7B-O024"], "source_experiment_tracker_id": "M7A-P024-E001", "source_paper_tracker_id": "M7A-P024", "tracker_key": "M7A-P024::M7A-P024-E001"}'
  FROM _m7_paper_map p
  JOIN _m7_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M7A-P024'
  RETURNING experiment_id
)
INSERT INTO _m7_experiment_map (tracker_id, experiment_id) SELECT 'M7A-P024::M7A-P024-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M7A-P025-E001',
    'Module 7B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M7B-O025"], "source_experiment_tracker_id": "M7A-P025-E001", "source_paper_tracker_id": "M7A-P025", "tracker_key": "M7A-P025::M7A-P025-E001"}'
  FROM _m7_paper_map p
  JOIN _m7_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M7A-P025'
  RETURNING experiment_id
)
INSERT INTO _m7_experiment_map (tracker_id, experiment_id) SELECT 'M7A-P025::M7A-P025-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract',
    'Tracker experiment M7A-P026-E001',
    'Module 7B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M7B-O026"], "source_experiment_tracker_id": "M7A-P026-E001", "source_paper_tracker_id": "M7A-P026", "tracker_key": "M7A-P026::M7A-P026-E001"}'
  FROM _m7_paper_map p
  JOIN _m7_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M7A-P026'
  RETURNING experiment_id
)
INSERT INTO _m7_experiment_map (tracker_id, experiment_id) SELECT 'M7A-P026::M7A-P026-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M7A-P027-E001',
    'Module 7B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M7B-O027"], "source_experiment_tracker_id": "M7A-P027-E001", "source_paper_tracker_id": "M7A-P027", "tracker_key": "M7A-P027::M7A-P027-E001"}'
  FROM _m7_paper_map p
  JOIN _m7_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M7A-P027'
  RETURNING experiment_id
)
INSERT INTO _m7_experiment_map (tracker_id, experiment_id) SELECT 'M7A-P027::M7A-P027-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M7A-P028-E001',
    'Module 7B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M7B-O028"], "source_experiment_tracker_id": "M7A-P028-E001", "source_paper_tracker_id": "M7A-P028", "tracker_key": "M7A-P028::M7A-P028-E001"}'
  FROM _m7_paper_map p
  JOIN _m7_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M7A-P028'
  RETURNING experiment_id
)
INSERT INTO _m7_experiment_map (tracker_id, experiment_id) SELECT 'M7A-P028::M7A-P028-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract',
    'Tracker experiment M7A-P029-E001',
    'Module 7B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M7B-O029"], "source_experiment_tracker_id": "M7A-P029-E001", "source_paper_tracker_id": "M7A-P029", "tracker_key": "M7A-P029::M7A-P029-E001"}'
  FROM _m7_paper_map p
  JOIN _m7_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M7A-P029'
  RETURNING experiment_id
)
INSERT INTO _m7_experiment_map (tracker_id, experiment_id) SELECT 'M7A-P029::M7A-P029-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M7A-P030-E001',
    'Module 7B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M7B-O030"], "source_experiment_tracker_id": "M7A-P030-E001", "source_paper_tracker_id": "M7A-P030", "tracker_key": "M7A-P030::M7A-P030-E001"}'
  FROM _m7_paper_map p
  JOIN _m7_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M7A-P030'
  RETURNING experiment_id
)
INSERT INTO _m7_experiment_map (tracker_id, experiment_id) SELECT 'M7A-P030::M7A-P030-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M7A-P031-E001',
    'Module 7B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M7B-O031"], "source_experiment_tracker_id": "M7A-P031-E001", "source_paper_tracker_id": "M7A-P031", "tracker_key": "M7A-P031::M7A-P031-E001"}'
  FROM _m7_paper_map p
  JOIN _m7_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M7A-P031'
  RETURNING experiment_id
)
INSERT INTO _m7_experiment_map (tracker_id, experiment_id) SELECT 'M7A-P031::M7A-P031-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M7A-P032-E001',
    'Module 7B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M7B-O032"], "source_experiment_tracker_id": "M7A-P032-E001", "source_paper_tracker_id": "M7A-P032", "tracker_key": "M7A-P032::M7A-P032-E001"}'
  FROM _m7_paper_map p
  JOIN _m7_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M7A-P032'
  RETURNING experiment_id
)
INSERT INTO _m7_experiment_map (tracker_id, experiment_id) SELECT 'M7A-P032::M7A-P032-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract',
    'Tracker experiment M7A-P033-E001',
    'Module 7B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M7B-O033"], "source_experiment_tracker_id": "M7A-P033-E001", "source_paper_tracker_id": "M7A-P033", "tracker_key": "M7A-P033::M7A-P033-E001"}'
  FROM _m7_paper_map p
  JOIN _m7_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M7A-P033'
  RETURNING experiment_id
)
INSERT INTO _m7_experiment_map (tracker_id, experiment_id) SELECT 'M7A-P033::M7A-P033-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M7A-P034-E001',
    'Module 7B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M7B-O034"], "source_experiment_tracker_id": "M7A-P034-E001", "source_paper_tracker_id": "M7A-P034", "tracker_key": "M7A-P034::M7A-P034-E001"}'
  FROM _m7_paper_map p
  JOIN _m7_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M7A-P034'
  RETURNING experiment_id
)
INSERT INTO _m7_experiment_map (tracker_id, experiment_id) SELECT 'M7A-P034::M7A-P034-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract/source page',
    'Tracker experiment M7A-P035-E001',
    'Module 7B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M7B-O035"], "source_experiment_tracker_id": "M7A-P035-E001", "source_paper_tracker_id": "M7A-P035", "tracker_key": "M7A-P035::M7A-P035-E001"}'
  FROM _m7_paper_map p
  JOIN _m7_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M7A-P035'
  RETURNING experiment_id
)
INSERT INTO _m7_experiment_map (tracker_id, experiment_id) SELECT 'M7A-P035::M7A-P035-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract',
    'Tracker experiment M7A-P036-E001',
    'Module 7B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M7B-O036"], "source_experiment_tracker_id": "M7A-P036-E001", "source_paper_tracker_id": "M7A-P036", "tracker_key": "M7A-P036::M7A-P036-E001"}'
  FROM _m7_paper_map p
  JOIN _m7_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M7A-P036'
  RETURNING experiment_id
)
INSERT INTO _m7_experiment_map (tracker_id, experiment_id) SELECT 'M7A-P036::M7A-P036-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Abstract',
    'Tracker experiment M7A-P037-E001',
    'Module 7B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M7B-O037"], "source_experiment_tracker_id": "M7A-P037-E001", "source_paper_tracker_id": "M7A-P037", "tracker_key": "M7A-P037::M7A-P037-E001"}'
  FROM _m7_paper_map p
  JOIN _m7_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M7A-P037'
  RETURNING experiment_id
)
INSERT INTO _m7_experiment_map (tracker_id, experiment_id) SELECT 'M7A-P037::M7A-P037-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Review/source',
    'Tracker experiment M7A-P038-E001',
    'Module 7B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M7B-O038"], "source_experiment_tracker_id": "M7A-P038-E001", "source_paper_tracker_id": "M7A-P038", "tracker_key": "M7A-P038::M7A-P038-E001"}'
  FROM _m7_paper_map p
  JOIN _m7_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M7A-P038'
  RETURNING experiment_id
)
INSERT INTO _m7_experiment_map (tracker_id, experiment_id) SELECT 'M7A-P038::M7A-P038-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Review/source',
    'Tracker experiment M7A-P039-E001',
    'Module 7B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M7B-O039"], "source_experiment_tracker_id": "M7A-P039-E001", "source_paper_tracker_id": "M7A-P039", "tracker_key": "M7A-P039::M7A-P039-E001"}'
  FROM _m7_paper_map p
  JOIN _m7_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M7A-P039'
  RETURNING experiment_id
)
INSERT INTO _m7_experiment_map (tracker_id, experiment_id) SELECT 'M7A-P039::M7A-P039-E001', experiment_id FROM inserted;

WITH inserted AS (
  INSERT INTO Experiment (
    paper_id, paradigm_id, experiment_number, figure_table_reference, title, description, notes
  )
  SELECT p.paper_id, ep.paradigm_id,
    1,
    'Review/source',
    'Tracker experiment M7A-P040-E001',
    'Module 7B tracker-derived experiment placeholder for SQL materialization.',
    '{"observation_tracker_ids": ["M7B-O040"], "source_experiment_tracker_id": "M7A-P040-E001", "source_paper_tracker_id": "M7A-P040", "tracker_key": "M7A-P040::M7A-P040-E001"}'
  FROM _m7_paper_map p
  JOIN _m7_paradigm_map ep ON ep.tracker_id = p.tracker_id
  WHERE p.tracker_id = 'M7A-P040'
  RETURNING experiment_id
)
INSERT INTO _m7_experiment_map (tracker_id, experiment_id) SELECT 'M7A-P040::M7A-P040-E001', experiment_id FROM inserted;

INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Anti-estrogen implant model', 'Module 7B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Anti-fibrotic implant intervention', 'Module 7B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Chemokine blockade', 'Module 7B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Chronic rejection model', 'Module 7B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Clinical anti-fibrotic trial', 'Module 7B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Clinical implant treatment', 'Module 7B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Complement inhibition', 'Module 7B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Human TPIAT trial', 'Module 7B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Human islet autotransplant follow-up', 'Module 7B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Human islet autotransplant trial', 'Module 7B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Human reconstructive trial', 'Module 7B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Human scar treatment', 'Module 7B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Hypertrophic scar model', 'Module 7B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Implant capsule synthesis', 'Module 7B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Innate immune preconditioning', 'Module 7B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Islet peri-transplant conditioning', 'Module 7B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Islet transplant IBMIR modulation', 'Module 7B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Leukotriene antagonist synthesis', 'Module 7B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Macrophage depletion', 'Module 7B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Macrophage modulation', 'Module 7B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Organ tolerance', 'Module 7B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Prophylactic implant conditioning', 'Module 7B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Prophylactic implant model', 'Module 7B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Recurrence prevention', 'Module 7B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Regulatory immune induction', 'Module 7B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Remote ischemic preconditioning', 'Module 7B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('SCI co-therapy', 'Module 7B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('SCI combination therapy', 'Module 7B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('SCI leukotriene axis', 'Module 7B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('SCI leukotriene inhibition', 'Module 7B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('SCI resolution biology', 'Module 7B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('SCI zileuton treatment', 'Module 7B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Systemic pharmacologic preconditioning', 'Module 7B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Tolerogenic microparticles', 'Module 7B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Transdermal implant model', 'Module 7B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_EvidenceType (evidence_type_name, description) VALUES ('Treg expansion', 'Module 7B tracker-derived evidence type') ON CONFLICT (evidence_type_name) DO NOTHING;

INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Alloimmune rejection', 'Module 7B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Autologous islet engraftment', 'Module 7B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Capsular contracture', 'Module 7B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Capsule contracture outcomes', 'Module 7B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Capsule fibrosis', 'Module 7B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Capsule formation', 'Module 7B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Capsule formation/fibrosis', 'Module 7B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Capsule thickness/fibrosis', 'Module 7B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Engraftment and graft survival', 'Module 7B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Established capsular contracture', 'Module 7B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Ferroptosis and functional recovery', 'Module 7B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Flap necrosis and angiogenic host cells', 'Module 7B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Flap stress signaling', 'Module 7B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Flap survival/clamping', 'Module 7B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Free flap reconstruction', 'Module 7B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Graft survival and microenvironment activation', 'Module 7B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Hypertrophic scar/fibrosis', 'Module 7B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('IBMIR and engraftment', 'Module 7B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Inflammation and functional outcome', 'Module 7B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Inflammation and graft survival', 'Module 7B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Inflammatory mediator induction', 'Module 7B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Injury attenuation and motor function', 'Module 7B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Ischemic tissue survival', 'Module 7B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Islet autotransplant outcomes', 'Module 7B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Islet engraftment', 'Module 7B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Long-term diabetes outcomes', 'Module 7B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Long-term islet graft survival', 'Module 7B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Macrophage activation and graft survival', 'Module 7B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Neutrophil infiltration and secondary injury', 'Module 7B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Recurrent capsular contracture', 'Module 7B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Repair and functional outcome', 'Module 7B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Resolution, neuroprotection, functional recovery', 'Module 7B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Safety/efficacy and IBMIR-related outcomes', 'Module 7B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Scar cosmesis', 'Module 7B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Tolerance induction', 'Module 7B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;
INSERT INTO ControlledVocabulary_OutcomeType (outcome_type_name, description) VALUES ('Tregs, tolerogenic dendritic cells, engraftment', 'Module 7B tracker-derived outcome type') ON CONFLICT (outcome_type_name) DO NOTHING;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Zafirlukast was reported to reduce capsular contracture in a preliminary breast implant clinical report.',
    'Baker grade/contracture',
    'Zafirlukast was reported to reduce capsular contracture in a preliminary breast implant clinical report.',
    'zafirlukast may reduce implant capsule contracture',
    'Abstract',
    'Abstract',
    'low',
    '{"curator_notes": "Preliminary clinical precedent.", "experiment_tracker_id": "M7A-P001-E001", "paper_tracker_id": "M7A-P001", "quantitative": "YES", "statistics_reported": "abstract-level", "topic_id": "M7B-T001", "tracker_id": "M7B-O001"}'
  FROM _m7_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M7A-P001::M7A-P001-E001'
    AND et.evidence_type_name = 'Clinical implant treatment'
    AND ot.outcome_type_name = 'Capsular contracture'
  RETURNING observation_id
)
INSERT INTO _m7_observation_map (tracker_id, observation_id) SELECT 'M7B-O001', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Pirfenidone prevented capsular contracture after mammary implantation.',
    'capsule/contracture',
    'Pirfenidone prevented capsular contracture after mammary implantation.',
    'pirfenidone reduces mammary implant capsule fibrosis',
    'Abstract',
    'Abstract',
    'low',
    '{"curator_notes": "Anti-fibrotic anchor.", "experiment_tracker_id": "M7A-P002-E001", "paper_tracker_id": "M7A-P002", "quantitative": "YES", "statistics_reported": "abstract-level", "topic_id": "M7B-T001", "tracker_id": "M7B-O002"}'
  FROM _m7_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M7A-P002::M7A-P002-E001'
    AND et.evidence_type_name = 'Anti-fibrotic implant intervention'
    AND ot.outcome_type_name = 'Capsule fibrosis'
  RETURNING observation_id
)
INSERT INTO _m7_observation_map (tracker_id, observation_id) SELECT 'M7B-O002', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Pirfenidone was tested clinically for capsular contracture with TGF-beta polymorphism association analysis.',
    'contracture/TGF-beta context',
    'Pirfenidone was tested clinically for capsular contracture with TGF-beta polymorphism association analysis.',
    'pirfenidone clinical capsule treatment tested',
    'Abstract',
    'Abstract',
    'low',
    '{"curator_notes": "Treatment rather than prophylaxis.", "experiment_tracker_id": "M7A-P003-E001", "paper_tracker_id": "M7A-P003", "quantitative": "YES", "statistics_reported": "abstract-level", "topic_id": "M7B-T001", "tracker_id": "M7B-O003"}'
  FROM _m7_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M7A-P003::M7A-P003-E001'
    AND et.evidence_type_name = 'Clinical anti-fibrotic trial'
    AND ot.outcome_type_name = 'Established capsular contracture'
  RETURNING observation_id
)
INSERT INTO _m7_observation_map (tracker_id, observation_id) SELECT 'M7B-O003', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Cromolyn, montelukast, and zafirlukast prophylaxis were compared for capsular contracture prevention.',
    'capsule thickness/fibrosis',
    'Cromolyn, montelukast, and zafirlukast prophylaxis were compared for capsular contracture prevention.',
    'leukotriene/mast-cell prophylaxis tested for capsule prevention',
    'Abstract/source page',
    'Abstract/source page',
    'low',
    '{"curator_notes": "Direct prophylaxis framing.", "experiment_tracker_id": "M7A-P004-E001", "paper_tracker_id": "M7A-P004", "quantitative": "YES", "statistics_reported": "source-page level", "topic_id": "M7B-T001", "tracker_id": "M7B-O004"}'
  FROM _m7_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M7A-P004::M7A-P004-E001'
    AND et.evidence_type_name = 'Prophylactic implant conditioning'
    AND ot.outcome_type_name = 'Capsule thickness/fibrosis'
  RETURNING observation_id
)
INSERT INTO _m7_observation_map (tracker_id, observation_id) SELECT 'M7B-O004', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Follow-up literature supported capsule prophylaxis as a recurring construct for cromolyn, montelukast, and zafirlukast.',
    'contracture',
    'Follow-up literature supported capsule prophylaxis as a recurring construct for cromolyn, montelukast, and zafirlukast.',
    'capsule prophylaxis construct repeated in implant literature',
    'Source page',
    'Source page',
    'low',
    '{"curator_notes": "Commentary/follow-up row.", "experiment_tracker_id": "M7A-P005-E001", "paper_tracker_id": "M7A-P005", "quantitative": "YES", "statistics_reported": "source-page level", "topic_id": "M7B-T001", "tracker_id": "M7B-O005"}'
  FROM _m7_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M7A-P005::M7A-P005-E001'
    AND et.evidence_type_name = 'Prophylactic implant conditioning'
    AND ot.outcome_type_name = 'Capsular contracture'
  RETURNING observation_id
)
INSERT INTO _m7_observation_map (tracker_id, observation_id) SELECT 'M7B-O005', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Leukotriene inhibitors were studied for prevention of recurrent capsular contracture in secondary breast augmentation.',
    'recurrence',
    'Leukotriene inhibitors were studied for prevention of recurrent capsular contracture in secondary breast augmentation.',
    'leukotriene inhibitors studied for recurrent capsule prevention',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Clinical recurrence anchor.", "experiment_tracker_id": "M7A-P006-E001", "paper_tracker_id": "M7A-P006", "quantitative": "YES", "statistics_reported": "source-page level", "topic_id": "M7B-T001", "tracker_id": "M7B-O006"}'
  FROM _m7_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M7A-P006::M7A-P006-E001'
    AND et.evidence_type_name = 'Recurrence prevention'
    AND ot.outcome_type_name = 'Recurrent capsular contracture'
  RETURNING observation_id
)
INSERT INTO _m7_observation_map (tracker_id, observation_id) SELECT 'M7B-O006', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Montelukast and tranilast were compared as prophylactic capsule-modifying agents in an alloplastic breast surgery mouse model.',
    'capsule formation',
    'Montelukast and tranilast were compared as prophylactic capsule-modifying agents in an alloplastic breast surgery mouse model.',
    'montelukast/tranilast prophylaxis modifies implant capsule biology',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Direct host-conditioning comparison.", "experiment_tracker_id": "M7A-P007-E001", "paper_tracker_id": "M7A-P007", "quantitative": "YES", "statistics_reported": "source-page level", "topic_id": "M7B-T001", "tracker_id": "M7B-O007"}'
  FROM _m7_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M7A-P007::M7A-P007-E001'
    AND et.evidence_type_name = 'Prophylactic implant model'
    AND ot.outcome_type_name = 'Capsule formation/fibrosis'
  RETURNING observation_id
)
INSERT INTO _m7_observation_map (tracker_id, observation_id) SELECT 'M7B-O007', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Tamoxifen reduced silicone implant capsule formation in a mouse model.',
    'capsule formation',
    'Tamoxifen reduced silicone implant capsule formation in a mouse model.',
    'tamoxifen reduces silicone implant capsule formation',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Systemic/host endocrine boundary.", "experiment_tracker_id": "M7A-P008-E001", "paper_tracker_id": "M7A-P008", "quantitative": "YES", "statistics_reported": "source-page level", "topic_id": "M7B-T001", "tracker_id": "M7B-O008"}'
  FROM _m7_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M7A-P008::M7A-P008-E001'
    AND et.evidence_type_name = 'Anti-estrogen implant model'
    AND ot.outcome_type_name = 'Capsule formation'
  RETURNING observation_id
)
INSERT INTO _m7_observation_map (tracker_id, observation_id) SELECT 'M7B-O008', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Transdermal tamoxifen improved capsular contracture outcomes in murine breast implantation.',
    'capsular contracture',
    'Transdermal tamoxifen improved capsular contracture outcomes in murine breast implantation.',
    'transdermal tamoxifen improves capsule outcome',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Recipient-directed but route-limited.", "experiment_tracker_id": "M7A-P009-E001", "paper_tracker_id": "M7A-P009", "quantitative": "YES", "statistics_reported": "source-page level", "topic_id": "M7B-T001", "tracker_id": "M7B-O009"}'
  FROM _m7_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M7A-P009::M7A-P009-E001'
    AND et.evidence_type_name = 'Transdermal implant model'
    AND ot.outcome_type_name = 'Capsular contracture'
  RETURNING observation_id
)
INSERT INTO _m7_observation_map (tracker_id, observation_id) SELECT 'M7B-O009', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Monophosphoryl lipid A preconditioning improved survival of critically ischemic tissue.',
    'survival',
    'Monophosphoryl lipid A preconditioning improved survival of critically ischemic tissue.',
    'innate preconditioning improves ischemic tissue survival',
    'Abstract',
    'Abstract',
    'low',
    '{"curator_notes": "Flap survival analog.", "experiment_tracker_id": "M7A-P010-E001", "paper_tracker_id": "M7A-P010", "quantitative": "YES", "statistics_reported": "abstract-level", "topic_id": "M7B-T002", "tracker_id": "M7B-O010"}'
  FROM _m7_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M7A-P010::M7A-P010-E001'
    AND et.evidence_type_name = 'Innate immune preconditioning'
    AND ot.outcome_type_name = 'Ischemic tissue survival'
  RETURNING observation_id
)
INSERT INTO _m7_observation_map (tracker_id, observation_id) SELECT 'M7B-O010', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Remote ischemic preconditioning modulated p38 MAP kinase in rat adipocutaneous flaps.',
    'p38 signaling',
    'Remote ischemic preconditioning modulated p38 MAP kinase in rat adipocutaneous flaps.',
    'remote preconditioning alters flap stress signaling',
    'Abstract',
    'Abstract',
    'low',
    '{"curator_notes": "Mechanistic vascular row.", "experiment_tracker_id": "M7A-P011-E001", "paper_tracker_id": "M7A-P011", "quantitative": "YES", "statistics_reported": "abstract-level", "topic_id": "M7B-T002", "tracker_id": "M7B-O011"}'
  FROM _m7_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M7A-P011::M7A-P011-E001'
    AND et.evidence_type_name = 'Remote ischemic preconditioning'
    AND ot.outcome_type_name = 'Flap stress signaling'
  RETURNING observation_id
)
INSERT INTO _m7_observation_map (tracker_id, observation_id) SELECT 'M7B-O011', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Systemic prolyl hydroxylase inhibitor preconditioning prevented skin flap necrosis via HIF-1-induced bone marrow-derived cells.',
    'necrosis/host cells',
    'Systemic prolyl hydroxylase inhibitor preconditioning prevented skin flap necrosis via HIF-1-induced bone marrow-derived cells.',
    'systemic HIF preconditioning reduces flap necrosis',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Strong host-cell mobilization anchor.", "experiment_tracker_id": "M7A-P012-E001", "paper_tracker_id": "M7A-P012", "quantitative": "YES", "statistics_reported": "source-page level", "topic_id": "M7B-T002", "tracker_id": "M7B-O012"}'
  FROM _m7_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M7A-P012::M7A-P012-E001'
    AND et.evidence_type_name = 'Systemic pharmacologic preconditioning'
    AND ot.outcome_type_name = 'Flap necrosis and angiogenic host cells'
  RETURNING observation_id
)
INSERT INTO _m7_observation_map (tracker_id, observation_id) SELECT 'M7B-O012', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Remote ischemic preconditioning was tested for rat dorsal skin flap value across clamping time.',
    'flap survival',
    'Remote ischemic preconditioning was tested for rat dorsal skin flap value across clamping time.',
    'remote preconditioning tested for flap survival timing',
    'Abstract',
    'Abstract',
    'low',
    '{"curator_notes": "Timing boundary.", "experiment_tracker_id": "M7A-P013-E001", "paper_tracker_id": "M7A-P013", "quantitative": "YES", "statistics_reported": "abstract-level", "topic_id": "M7B-T002", "tracker_id": "M7B-O013"}'
  FROM _m7_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M7A-P013::M7A-P013-E001'
    AND et.evidence_type_name = 'Remote ischemic preconditioning'
    AND ot.outcome_type_name = 'Flap survival/clamping'
  RETURNING observation_id
)
INSERT INTO _m7_observation_map (tracker_id, observation_id) SELECT 'M7B-O013', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'A randomized trial tested remote ischemic preconditioning in head and neck cancer reconstruction.',
    'trial endpoint',
    'A randomized trial tested remote ischemic preconditioning in head and neck cancer reconstruction.',
    'remote preconditioning tested in human free-flap reconstruction',
    'Abstract',
    'Abstract',
    'low',
    '{"curator_notes": "Human reconstruction anchor.", "experiment_tracker_id": "M7A-P014-E001", "paper_tracker_id": "M7A-P014", "quantitative": "YES", "statistics_reported": "abstract-level", "topic_id": "M7B-T002", "tracker_id": "M7B-O014"}'
  FROM _m7_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M7A-P014::M7A-P014-E001'
    AND et.evidence_type_name = 'Human reconstructive trial'
    AND ot.outcome_type_name = 'Free flap reconstruction'
  RETURNING observation_id
)
INSERT INTO _m7_observation_map (tracker_id, observation_id) SELECT 'M7B-O014', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Alpha-1 antitrypsin enhanced islet engraftment by suppressing instant blood-mediated inflammatory reaction.',
    'IBMIR/engraftment',
    'Alpha-1 antitrypsin enhanced islet engraftment by suppressing instant blood-mediated inflammatory reaction.',
    'A1AT suppresses IBMIR and improves islet engraftment',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Strong cell-transplant anchor.", "experiment_tracker_id": "M7A-P015-E001", "paper_tracker_id": "M7A-P015", "quantitative": "YES", "statistics_reported": "source-page level", "topic_id": "M7B-T003", "tracker_id": "M7B-O015"}'
  FROM _m7_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M7A-P015::M7A-P015-E001'
    AND et.evidence_type_name = 'Islet peri-transplant conditioning'
    AND ot.outcome_type_name = 'IBMIR and engraftment'
  RETURNING observation_id
)
INSERT INTO _m7_observation_map (tracker_id, observation_id) SELECT 'M7B-O015', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Alpha-1 antitrypsin reduced inflammation and enhanced mouse pancreatic islet transplant survival.',
    'graft survival',
    'Alpha-1 antitrypsin reduced inflammation and enhanced mouse pancreatic islet transplant survival.',
    'A1AT improves islet survival through inflammation reduction',
    'Abstract',
    'Abstract',
    'low',
    '{"curator_notes": "Mouse graft survival.", "experiment_tracker_id": "M7A-P016-E001", "paper_tracker_id": "M7A-P016", "quantitative": "YES", "statistics_reported": "abstract-level", "topic_id": "M7B-T003", "tracker_id": "M7B-O016"}'
  FROM _m7_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M7A-P016::M7A-P016-E001'
    AND et.evidence_type_name = 'Islet peri-transplant conditioning'
    AND ot.outcome_type_name = 'Inflammation and graft survival'
  RETURNING observation_id
)
INSERT INTO _m7_observation_map (tracker_id, observation_id) SELECT 'M7B-O016', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Alpha-1 antitrypsin suppressed macrophage activation and promoted islet graft survival after intrahepatic transplantation.',
    'macrophage/graft survival',
    'Alpha-1 antitrypsin suppressed macrophage activation and promoted islet graft survival after intrahepatic transplantation.',
    'A1AT suppresses macrophage activation and promotes islet survival',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Immune-stromal transition anchor.", "experiment_tracker_id": "M7A-P017-E001", "paper_tracker_id": "M7A-P017", "quantitative": "YES", "statistics_reported": "source-page level", "topic_id": "M7B-T003", "tracker_id": "M7B-O017"}'
  FROM _m7_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M7A-P017::M7A-P017-E001'
    AND et.evidence_type_name = 'Macrophage modulation'
    AND ot.outcome_type_name = 'Macrophage activation and graft survival'
  RETURNING observation_id
)
INSERT INTO _m7_observation_map (tracker_id, observation_id) SELECT 'M7B-O017', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'A randomized pilot trial tested etanercept and alpha-1 antitrypsin to improve autologous islet engraftment.',
    'engraftment',
    'A randomized pilot trial tested etanercept and alpha-1 antitrypsin to improve autologous islet engraftment.',
    'anti-inflammatory peri-transplant trial tested in human islet autotransplant',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Human trial anchor.", "experiment_tracker_id": "M7A-P018-E001", "paper_tracker_id": "M7A-P018", "quantitative": "YES", "statistics_reported": "source-page level", "topic_id": "M7B-T003", "tracker_id": "M7B-O018"}'
  FROM _m7_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M7A-P018::M7A-P018-E001'
    AND et.evidence_type_name = 'Human islet autotransplant trial'
    AND ot.outcome_type_name = 'Autologous islet engraftment'
  RETURNING observation_id
)
INSERT INTO _m7_observation_map (tracker_id, observation_id) SELECT 'M7B-O018', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Alpha-1 antitrypsin augmentation therapy was tested in chronic pancreatitis patients undergoing total pancreatectomy and islet autotransplantation.',
    'islet autotransplant outcome',
    'Alpha-1 antitrypsin augmentation therapy was tested in chronic pancreatitis patients undergoing total pancreatectomy and islet autotransplantation.',
    'A1AT augmentation tested in TPIAT',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Human RCT anchor.", "experiment_tracker_id": "M7A-P019-E001", "paper_tracker_id": "M7A-P019", "quantitative": "YES", "statistics_reported": "source-page level", "topic_id": "M7B-T003", "tracker_id": "M7B-O019"}'
  FROM _m7_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M7A-P019::M7A-P019-E001'
    AND et.evidence_type_name = 'Human TPIAT trial'
    AND ot.outcome_type_name = 'Islet autotransplant outcomes'
  RETURNING observation_id
)
INSERT INTO _m7_observation_map (tracker_id, observation_id) SELECT 'M7B-O019', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Peri-transplant inflammation and long-term diabetes outcomes were not improved by etanercept or alpha-1 antitrypsin in a follow-up analysis.',
    'diabetes outcome/inflammation',
    'Peri-transplant inflammation and long-term diabetes outcomes were not improved by etanercept or alpha-1 antitrypsin in a follow-up analysis.',
    'A1AT/etanercept benefit not confirmed in long-term islet autotransplant outcomes',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Contradiction boundary.", "experiment_tracker_id": "M7A-P020-E001", "paper_tracker_id": "M7A-P020", "quantitative": "YES", "statistics_reported": "source-page level", "topic_id": "M7B-T003", "tracker_id": "M7B-O020"}'
  FROM _m7_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M7A-P020::M7A-P020-E001'
    AND et.evidence_type_name = 'Human islet autotransplant follow-up'
    AND ot.outcome_type_name = 'Long-term diabetes outcomes'
  RETURNING observation_id
)
INSERT INTO _m7_observation_map (tracker_id, observation_id) SELECT 'M7B-O020', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Low molecular weight sulfated dextran was evaluated for safety and efficacy in islet transplantation.',
    'safety/efficacy',
    'Low molecular weight sulfated dextran was evaluated for safety and efficacy in islet transplantation.',
    'sulfated dextran tested as IBMIR-related islet conditioning',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Complement/coagulation-adjacent.", "experiment_tracker_id": "M7A-P021-E001", "paper_tracker_id": "M7A-P021", "quantitative": "YES", "statistics_reported": "source-page level", "topic_id": "M7B-T003", "tracker_id": "M7B-O021"}'
  FROM _m7_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M7A-P021::M7A-P021-E001'
    AND et.evidence_type_name = 'Islet transplant IBMIR modulation'
    AND ot.outcome_type_name = 'Safety/efficacy and IBMIR-related outcomes'
  RETURNING observation_id
)
INSERT INTO _m7_observation_map (tracker_id, observation_id) SELECT 'M7B-O021', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'C5a inhibitory peptide was analyzed for inflammatory mediators induced after islet transplantation.',
    'inflammatory mediators',
    'C5a inhibitory peptide was analyzed for inflammatory mediators induced after islet transplantation.',
    'C5a inhibition targets early islet inflammatory mediators',
    'Abstract',
    'Abstract',
    'low',
    '{"curator_notes": "Complement phase 1.", "experiment_tracker_id": "M7A-P022-E001", "paper_tracker_id": "M7A-P022", "quantitative": "YES", "statistics_reported": "abstract-level", "topic_id": "M7B-T003", "tracker_id": "M7B-O022"}'
  FROM _m7_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M7A-P022::M7A-P022-E001'
    AND et.evidence_type_name = 'Complement inhibition'
    AND ot.outcome_type_name = 'Inflammatory mediator induction'
  RETURNING observation_id
)
INSERT INTO _m7_observation_map (tracker_id, observation_id) SELECT 'M7B-O022', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'CCL2/MCP-1 and CXCL12/SDF-1 blockade improved pancreatic islet engraftment and survival in mouse.',
    'engraftment/survival',
    'CCL2/MCP-1 and CXCL12/SDF-1 blockade improved pancreatic islet engraftment and survival in mouse.',
    'chemokine blockade improves islet engraftment/survival',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Monocyte recruitment axis.", "experiment_tracker_id": "M7A-P023-E001", "paper_tracker_id": "M7A-P023", "quantitative": "YES", "statistics_reported": "source-page level", "topic_id": "M7B-T003", "tracker_id": "M7B-O023"}'
  FROM _m7_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M7A-P023::M7A-P023-E001'
    AND et.evidence_type_name = 'Chemokine blockade'
    AND ot.outcome_type_name = 'Engraftment and graft survival'
  RETURNING observation_id
)
INSERT INTO _m7_observation_map (tracker_id, observation_id) SELECT 'M7B-O023', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Macrophage depletion altered graft survival and microenvironment activation after allogeneic islet transplantation.',
    'graft survival/microenvironment',
    'Macrophage depletion altered graft survival and microenvironment activation after allogeneic islet transplantation.',
    'macrophages shape islet graft microenvironment and survival',
    'Abstract',
    'Abstract',
    'low',
    '{"curator_notes": "Direction needs full text.", "experiment_tracker_id": "M7A-P024-E001", "paper_tracker_id": "M7A-P024", "quantitative": "YES", "statistics_reported": "abstract-level", "topic_id": "M7B-T003", "tracker_id": "M7B-O024"}'
  FROM _m7_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M7A-P024::M7A-P024-E001'
    AND et.evidence_type_name = 'Macrophage depletion'
    AND ot.outcome_type_name = 'Graft survival and microenvironment activation'
  RETURNING observation_id
)
INSERT INTO _m7_observation_map (tracker_id, observation_id) SELECT 'M7B-O024', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Apoptotic cell administration enhanced islet engraftment by inducing Tregs and tolerogenic dendritic cells.',
    'Tregs/DCs/engraftment',
    'Apoptotic cell administration enhanced islet engraftment by inducing Tregs and tolerogenic dendritic cells.',
    'apoptotic cell host conditioning induces Tregs/DCs and improves engraftment',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Immune transition anchor.", "experiment_tracker_id": "M7A-P025-E001", "paper_tracker_id": "M7A-P025", "quantitative": "YES", "statistics_reported": "source-page level", "topic_id": "M7B-T003", "tracker_id": "M7B-O025"}'
  FROM _m7_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M7A-P025::M7A-P025-E001'
    AND et.evidence_type_name = 'Regulatory immune induction'
    AND ot.outcome_type_name = 'Tregs, tolerogenic dendritic cells, engraftment'
  RETURNING observation_id
)
INSERT INTO _m7_observation_map (tracker_id, observation_id) SELECT 'M7B-O025', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Endogenous expansion of regulatory T cells led to long-term islet graft survival in diabetic NOD mice.',
    'graft survival',
    'Endogenous expansion of regulatory T cells led to long-term islet graft survival in diabetic NOD mice.',
    'Treg expansion supports long-term islet graft survival',
    'Abstract',
    'Abstract',
    'low',
    '{"curator_notes": "Regulatory host state.", "experiment_tracker_id": "M7A-P026-E001", "paper_tracker_id": "M7A-P026", "quantitative": "YES", "statistics_reported": "abstract-level", "topic_id": "M7B-T003", "tracker_id": "M7B-O026"}'
  FROM _m7_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M7A-P026::M7A-P026-E001'
    AND et.evidence_type_name = 'Treg expansion'
    AND ot.outcome_type_name = 'Long-term islet graft survival'
  RETURNING observation_id
)
INSERT INTO _m7_observation_map (tracker_id, observation_id) SELECT 'M7B-O026', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Immunomodulating tolerogenic microparticles improved islet engrafts via Treg induction.',
    'engraftment',
    'Immunomodulating tolerogenic microparticles improved islet engrafts via Treg induction.',
    'tolerogenic microparticles induce Tregs and improve islet engraftment',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Biomaterial but host-directed.", "experiment_tracker_id": "M7A-P027-E001", "paper_tracker_id": "M7A-P027", "quantitative": "YES", "statistics_reported": "source-page level", "topic_id": "M7B-T003", "tracker_id": "M7B-O027"}'
  FROM _m7_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M7A-P027::M7A-P027-E001'
    AND et.evidence_type_name = 'Tolerogenic microparticles'
    AND ot.outcome_type_name = 'Islet engraftment'
  RETURNING observation_id
)
INSERT INTO _m7_observation_map (tracker_id, observation_id) SELECT 'M7B-O027', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Circular RNA FSCN1-silenced dendritic cells prevented alloimmune rejection in heart transplantation.',
    'rejection',
    'Circular RNA FSCN1-silenced dendritic cells prevented alloimmune rejection in heart transplantation.',
    'tolerogenic dendritic cell strategy prevents rejection',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Remodeling endpoint unclear.", "experiment_tracker_id": "M7A-P028-E001", "paper_tracker_id": "M7A-P028", "quantitative": "YES", "statistics_reported": "source-page level", "topic_id": "M7B-T004", "tracker_id": "M7B-O028"}'
  FROM _m7_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M7A-P028::M7A-P028-E001'
    AND et.evidence_type_name = 'Organ tolerance'
    AND ot.outcome_type_name = 'Alloimmune rejection'
  RETURNING observation_id
)
INSERT INTO _m7_observation_map (tracker_id, observation_id) SELECT 'M7B-O028', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'A second renal allograft model analyzed mechanisms of tolerance induction in chronic rejection.',
    'tolerance/rejection',
    'A second renal allograft model analyzed mechanisms of tolerance induction in chronic rejection.',
    'renal allograft tolerance model informs chronic rejection boundary',
    'Abstract',
    'Abstract',
    'low',
    '{"curator_notes": "Rejection-heavy boundary.", "experiment_tracker_id": "M7A-P029-E001", "paper_tracker_id": "M7A-P029", "quantitative": "YES", "statistics_reported": "abstract-level", "topic_id": "M7B-T004", "tracker_id": "M7B-O029"}'
  FROM _m7_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M7A-P029::M7A-P029-E001'
    AND et.evidence_type_name = 'Chronic rejection model'
    AND ot.outcome_type_name = 'Tolerance induction'
  RETURNING observation_id
)
INSERT INTO _m7_observation_map (tracker_id, observation_id) SELECT 'M7B-O029', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Zileuton and montelukast were tested for effects in mouse experimental SCI.',
    'inflammation/function',
    'Zileuton and montelukast were tested for effects in mouse experimental SCI.',
    'leukotriene inhibitors tested after SCI',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "SCI lesion-bed analog.", "experiment_tracker_id": "M7A-P030-E001", "paper_tracker_id": "M7A-P030", "quantitative": "YES", "statistics_reported": "source-page level", "topic_id": "M7B-T005", "tracker_id": "M7B-O030"}'
  FROM _m7_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M7A-P030::M7A-P030-E001'
    AND et.evidence_type_name = 'SCI leukotriene inhibition'
    AND ot.outcome_type_name = 'Inflammation and functional outcome'
  RETURNING observation_id
)
INSERT INTO _m7_observation_map (tracker_id, observation_id) SELECT 'M7B-O030', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'LTB4-BLT1 mediated neutrophil infiltration and secondary injury after experimental SCI.',
    'neutrophil/secondary injury',
    'LTB4-BLT1 mediated neutrophil infiltration and secondary injury after experimental SCI.',
    'LTB4-BLT1 drives neutrophil-linked secondary SCI injury',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Phase 1 inflammatory amplification.", "experiment_tracker_id": "M7A-P031-E001", "paper_tracker_id": "M7A-P031", "quantitative": "YES", "statistics_reported": "source-page level", "topic_id": "M7B-T005", "tracker_id": "M7B-O031"}'
  FROM _m7_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M7A-P031::M7A-P031-E001'
    AND et.evidence_type_name = 'SCI leukotriene axis'
    AND ot.outcome_type_name = 'Neutrophil infiltration and secondary injury'
  RETURNING observation_id
)
INSERT INTO _m7_observation_map (tracker_id, observation_id) SELECT 'M7B-O031', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Zafirlukast plus pseudohypericin attenuated SCI and motor dysfunction in mice.',
    'motor function',
    'Zafirlukast plus pseudohypericin attenuated SCI and motor dysfunction in mice.',
    'zafirlukast combination attenuates SCI motor dysfunction',
    'Abstract/source page',
    'Abstract/source page',
    'low',
    '{"curator_notes": "Combination boundary.", "experiment_tracker_id": "M7A-P032-E001", "paper_tracker_id": "M7A-P032", "quantitative": "YES", "statistics_reported": "source-page level", "topic_id": "M7B-T005", "tracker_id": "M7B-O032"}'
  FROM _m7_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M7A-P032::M7A-P032-E001'
    AND et.evidence_type_name = 'SCI combination therapy'
    AND ot.outcome_type_name = 'Injury attenuation and motor function'
  RETURNING observation_id
)
INSERT INTO _m7_observation_map (tracker_id, observation_id) SELECT 'M7B-O032', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Zileuton ameliorated neuronal ferroptosis and functional recovery after SCI.',
    'ferroptosis/function',
    'Zileuton ameliorated neuronal ferroptosis and functional recovery after SCI.',
    'zileuton improves ferroptosis/recovery endpoints after SCI',
    'Abstract',
    'Abstract',
    'low',
    '{"curator_notes": "Recent low-confidence row.", "experiment_tracker_id": "M7A-P033-E001", "paper_tracker_id": "M7A-P033", "quantitative": "YES", "statistics_reported": "abstract-level", "topic_id": "M7B-T005", "tracker_id": "M7B-O033"}'
  FROM _m7_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M7A-P033::M7A-P033-E001'
    AND et.evidence_type_name = 'SCI zileuton treatment'
    AND ot.outcome_type_name = 'Ferroptosis and functional recovery'
  RETURNING observation_id
)
INSERT INTO _m7_observation_map (tracker_id, observation_id) SELECT 'M7B-O033', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Resolvin D3 promoted inflammatory resolution, neuroprotection, and functional recovery after SCI.',
    'resolution/function',
    'Resolvin D3 promoted inflammatory resolution, neuroprotection, and functional recovery after SCI.',
    'resolvin D3 promotes resolution and recovery after SCI',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Pro-resolving anchor.", "experiment_tracker_id": "M7A-P034-E001", "paper_tracker_id": "M7A-P034", "quantitative": "YES", "statistics_reported": "source-page level", "topic_id": "M7B-T005", "tracker_id": "M7B-O034"}'
  FROM _m7_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M7A-P034::M7A-P034-E001'
    AND et.evidence_type_name = 'SCI resolution biology'
    AND ot.outcome_type_name = 'Resolution, neuroprotection, functional recovery'
  RETURNING observation_id
)
INSERT INTO _m7_observation_map (tracker_id, observation_id) SELECT 'M7B-O034', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Resolvin D1 co-administered with peripheral nerve-derived stem cell spheroids was tested as SCI therapy.',
    'repair/function',
    'Resolvin D1 co-administered with peripheral nerve-derived stem cell spheroids was tested as SCI therapy.',
    'resolvin D1 co-therapy tested with cell spheroids',
    'Abstract/source page',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Not pure host conditioning.", "experiment_tracker_id": "M7A-P035-E001", "paper_tracker_id": "M7A-P035", "quantitative": "YES", "statistics_reported": "source-page level", "topic_id": "M7B-T005", "tracker_id": "M7B-O035"}'
  FROM _m7_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M7A-P035::M7A-P035-E001'
    AND et.evidence_type_name = 'SCI co-therapy'
    AND ot.outcome_type_name = 'Repair and functional outcome'
  RETURNING observation_id
)
INSERT INTO _m7_observation_map (tracker_id, observation_id) SELECT 'M7B-O035', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Tranilast liposomal gel was tested against placebo for post-cesarean scar outcome.',
    'scar cosmesis',
    'Tranilast liposomal gel was tested against placebo for post-cesarean scar outcome.',
    'topical tranilast affects surgical scar outcome',
    'Abstract',
    'Abstract',
    'low',
    '{"curator_notes": "Local-route boundary.", "experiment_tracker_id": "M7A-P036-E001", "paper_tracker_id": "M7A-P036", "quantitative": "YES", "statistics_reported": "abstract-level", "topic_id": "M7B-T006", "tracker_id": "M7B-O036"}'
  FROM _m7_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M7A-P036::M7A-P036-E001'
    AND et.evidence_type_name = 'Human scar treatment'
    AND ot.outcome_type_name = 'Scar cosmesis'
  RETURNING observation_id
)
INSERT INTO _m7_observation_map (tracker_id, observation_id) SELECT 'M7B-O036', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'Tranilast-loaded microneedles were tested for hypertrophic scar treatment in rabbits.',
    'scar/fibrosis',
    'Tranilast-loaded microneedles were tested for hypertrophic scar treatment in rabbits.',
    'local tranilast delivery targets hypertrophic scar fibrosis',
    'Abstract',
    'Abstract',
    'low',
    '{"curator_notes": "Local delivery, not systemic.", "experiment_tracker_id": "M7A-P037-E001", "paper_tracker_id": "M7A-P037", "quantitative": "YES", "statistics_reported": "abstract-level", "topic_id": "M7B-T006", "tracker_id": "M7B-O037"}'
  FROM _m7_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M7A-P037::M7A-P037-E001'
    AND et.evidence_type_name = 'Hypertrophic scar model'
    AND ot.outcome_type_name = 'Hypertrophic scar/fibrosis'
  RETURNING observation_id
)
INSERT INTO _m7_observation_map (tracker_id, observation_id) SELECT 'M7B-O037', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'A systematic review mapped non-surgical treatment and prophylaxis of mammary implant capsular contracture.',
    'review synthesis',
    'A systematic review mapped non-surgical treatment and prophylaxis of mammary implant capsular contracture.',
    'implant capsule prophylaxis/treatment literature exists as synthesis base',
    'Review/source',
    'Review/source',
    'medium',
    '{"curator_notes": "Review anchor.", "experiment_tracker_id": "M7A-P038-E001", "paper_tracker_id": "M7A-P038", "quantitative": "YES", "statistics_reported": "review-level", "topic_id": "M7B-T001", "tracker_id": "M7B-O038"}'
  FROM _m7_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M7A-P038::M7A-P038-E001'
    AND et.evidence_type_name = 'Implant capsule synthesis'
    AND ot.outcome_type_name = 'Capsule contracture outcomes'
  RETURNING observation_id
)
INSERT INTO _m7_observation_map (tracker_id, observation_id) SELECT 'M7B-O038', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'A systematic review/meta-analysis evaluated leukotriene receptor antagonists for capsular contracture prevention/treatment.',
    'meta-analysis',
    'A systematic review/meta-analysis evaluated leukotriene receptor antagonists for capsular contracture prevention/treatment.',
    'LTRA capsule evidence has meta-analytic synthesis',
    'Review/source',
    'Review/source',
    'medium',
    '{"curator_notes": "Review anchor.", "experiment_tracker_id": "M7A-P039-E001", "paper_tracker_id": "M7A-P039", "quantitative": "YES", "statistics_reported": "review-level", "topic_id": "M7B-T001", "tracker_id": "M7B-O039"}'
  FROM _m7_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M7A-P039::M7A-P039-E001'
    AND et.evidence_type_name = 'Leukotriene antagonist synthesis'
    AND ot.outcome_type_name = 'Capsule contracture outcomes'
  RETURNING observation_id
)
INSERT INTO _m7_observation_map (tracker_id, observation_id) SELECT 'M7B-O039', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO Observation (
    experiment_id, evidence_type_id, outcome_type_id, observation_value,
    unit, raw_observation_text, normalized_observation_value, source_section,
    figure_panel_reference, extraction_confidence, notes
  )
  SELECT e.experiment_id, et.evidence_type_id, ot.outcome_type_id,
    'A meta-analysis evaluated leukotriene receptor antagonists for periprosthetic capsular contracture treatment and prevention.',
    'meta-analysis',
    'A meta-analysis evaluated leukotriene receptor antagonists for periprosthetic capsular contracture treatment and prevention.',
    'LTRA capsule prevention/treatment has prior meta-analysis',
    'Review/source',
    'Review/source',
    'medium',
    '{"curator_notes": "Review anchor.", "experiment_tracker_id": "M7A-P040-E001", "paper_tracker_id": "M7A-P040", "quantitative": "YES", "statistics_reported": "review-level", "topic_id": "M7B-T001", "tracker_id": "M7B-O040"}'
  FROM _m7_experiment_map e
  CROSS JOIN ControlledVocabulary_EvidenceType et
  CROSS JOIN ControlledVocabulary_OutcomeType ot
  WHERE e.tracker_id = 'M7A-P040::M7A-P040-E001'
    AND et.evidence_type_name = 'Leukotriene antagonist synthesis'
    AND ot.outcome_type_name = 'Capsule contracture outcomes'
  RETURNING observation_id
)
INSERT INTO _m7_observation_map (tracker_id, observation_id) SELECT 'M7B-O040', observation_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Leukotriene receptor antagonism is a recurring host-conditioning strategy for breast implant capsular contracture prevention or treatment.',
    'synthesis',
    'high',
    'Tracker/review map',
    'medium',
    '{"curator_notes": "Strongest Module 7 precedent.", "source_paper_tracker_id": "M7A-P001, P004-P007, P038-P040", "topic_id": "M7B-T001", "tracker_id": "M7B-C001"}'
  FROM _m7_paper_map p
  WHERE p.tracker_id = 'M7A-P001'
  RETURNING claim_id
)
INSERT INTO _m7_claim_map (tracker_id, claim_id) SELECT 'M7B-C001', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Pirfenidone provides anti-fibrotic capsule evidence in mammary implant models and clinical capsular contracture treatment.',
    'conclusion',
    'medium',
    'Abstract',
    'low',
    '{"curator_notes": "Treatment/prophylaxis distinction needed.", "source_paper_tracker_id": "M7A-P002-P003", "topic_id": "M7B-T001", "tracker_id": "M7B-C002"}'
  FROM _m7_paper_map p
  WHERE p.tracker_id = 'M7A-P002'
  RETURNING claim_id
)
INSERT INTO _m7_claim_map (tracker_id, claim_id) SELECT 'M7B-C002', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Tranilast is represented as a prophylactic capsule-modifying comparator in implant models.',
    'conclusion',
    'medium',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Mostly preclinical in tracker.", "source_paper_tracker_id": "M7A-P007", "topic_id": "M7B-T001", "tracker_id": "M7B-C003"}'
  FROM _m7_paper_map p
  WHERE p.tracker_id = 'M7A-P007'
  RETURNING claim_id
)
INSERT INTO _m7_claim_map (tracker_id, claim_id) SELECT 'M7B-C003', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Tamoxifen can reduce silicone implant capsule formation or capsular contracture outcomes in mouse/murine models.',
    'conclusion',
    'medium',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Route differs across rows.", "source_paper_tracker_id": "M7A-P008-P009", "topic_id": "M7B-T001", "tracker_id": "M7B-C004"}'
  FROM _m7_paper_map p
  WHERE p.tracker_id = 'M7A-P008'
  RETURNING claim_id
)
INSERT INTO _m7_claim_map (tracker_id, claim_id) SELECT 'M7B-C004', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Breast implant capsule evidence should distinguish prophylaxis, recurrence prevention, and treatment of established contracture.',
    'boundary condition',
    'high',
    'Module 7A tracker',
    'high',
    '{"curator_notes": "Timing boundary.", "source_paper_tracker_id": "M7A-P001-P009", "topic_id": "M7B-T001", "tracker_id": "M7B-C005"}'
  FROM _m7_paper_map p
  WHERE p.tracker_id = 'M7A-P001'
  RETURNING claim_id
)
INSERT INTO _m7_claim_map (tracker_id, claim_id) SELECT 'M7B-C005', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Flap preconditioning evidence supports the idea that recipient/systemic state can be modified before tissue transfer.',
    'conclusion',
    'medium',
    'Abstract/source page',
    'low',
    '{"curator_notes": "Vascular endpoints dominate.", "source_paper_tracker_id": "M7A-P010-P014", "topic_id": "M7B-T002", "tracker_id": "M7B-C006"}'
  FROM _m7_paper_map p
  WHERE p.tracker_id = 'M7A-P010'
  RETURNING claim_id
)
INSERT INTO _m7_claim_map (tracker_id, claim_id) SELECT 'M7B-C006', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Systemic hypoxia-pathway preconditioning can mobilize host bone marrow-derived mechanisms and reduce skin flap necrosis.',
    'conclusion',
    'medium',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Strongest flap host-cell row.", "source_paper_tracker_id": "M7A-P012", "topic_id": "M7B-T002", "tracker_id": "M7B-C007"}'
  FROM _m7_paper_map p
  WHERE p.tracker_id = 'M7A-P012'
  RETURNING claim_id
)
INSERT INTO _m7_claim_map (tracker_id, claim_id) SELECT 'M7B-C007', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Flap preconditioning should not be overread as anti-fibrotic conditioning unless remodeling endpoints are measured.',
    'boundary condition',
    'high',
    'Module 7A tracker',
    'high',
    '{"curator_notes": "Endpoint boundary.", "source_paper_tracker_id": "M7A-P010-P014", "topic_id": "M7B-T002", "tracker_id": "M7B-C008"}'
  FROM _m7_paper_map p
  WHERE p.tracker_id = 'M7A-P010'
  RETURNING claim_id
)
INSERT INTO _m7_claim_map (tracker_id, claim_id) SELECT 'M7B-C008', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Alpha-1 antitrypsin and related peri-transplant anti-inflammatory strategies can target early islet engraftment barriers, but human follow-up evidence is mixed.',
    'synthesis',
    'high',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Includes neutral follow-up.", "source_paper_tracker_id": "M7A-P015-P020", "topic_id": "M7B-T003", "tracker_id": "M7B-C009"}'
  FROM _m7_paper_map p
  WHERE p.tracker_id = 'M7A-P015'
  RETURNING claim_id
)
INSERT INTO _m7_claim_map (tracker_id, claim_id) SELECT 'M7B-C009', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'IBMIR/complement/coagulation-adjacent pathways are early host-response targets in islet transplantation.',
    'conclusion',
    'medium',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Phase 1 transplant analog.", "source_paper_tracker_id": "M7A-P015, P021-P022", "topic_id": "M7B-T003", "tracker_id": "M7B-C010"}'
  FROM _m7_paper_map p
  WHERE p.tracker_id = 'M7A-P015'
  RETURNING claim_id
)
INSERT INTO _m7_claim_map (tracker_id, claim_id) SELECT 'M7B-C010', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Macrophage and chemokine recruitment pathways shape islet graft survival and microenvironment activation.',
    'conclusion',
    'medium',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Immune-stromal transition.", "source_paper_tracker_id": "M7A-P017, P023-P024", "topic_id": "M7B-T003", "tracker_id": "M7B-C011"}'
  FROM _m7_paper_map p
  WHERE p.tracker_id = 'M7A-P017'
  RETURNING claim_id
)
INSERT INTO _m7_claim_map (tracker_id, claim_id) SELECT 'M7B-C011', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Regulatory immune conditioning through Tregs and tolerogenic dendritic-cell programs can improve islet engraftment or survival in preclinical settings.',
    'conclusion',
    'medium',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Biomaterial-host boundary for P027.", "source_paper_tracker_id": "M7A-P025-P027", "topic_id": "M7B-T003", "tracker_id": "M7B-C012"}'
  FROM _m7_paper_map p
  WHERE p.tracker_id = 'M7A-P025'
  RETURNING claim_id
)
INSERT INTO _m7_claim_map (tracker_id, claim_id) SELECT 'M7B-C012', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Islet evidence is primarily engraftment/survival evidence and should not be treated as direct anti-fibrotic reconstruction evidence.',
    'boundary condition',
    'high',
    'Module 7A tracker',
    'high',
    '{"curator_notes": "Endpoint boundary.", "source_paper_tracker_id": "M7A-P015-P027", "topic_id": "M7B-T003", "tracker_id": "M7B-C013"}'
  FROM _m7_paper_map p
  WHERE p.tracker_id = 'M7A-P015'
  RETURNING claim_id
)
INSERT INTO _m7_claim_map (tracker_id, claim_id) SELECT 'M7B-C013', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Organ-tolerance studies can inform host immune conditioning but are often rejection-centered rather than remodeling-centered.',
    'boundary condition',
    'high',
    'Module 7A tracker',
    'high',
    '{"curator_notes": "Rejection-only caution.", "source_paper_tracker_id": "M7A-P028-P029", "topic_id": "M7B-T004", "tracker_id": "M7B-C014"}'
  FROM _m7_paper_map p
  WHERE p.tracker_id = 'M7A-P028'
  RETURNING claim_id
)
INSERT INTO _m7_claim_map (tracker_id, claim_id) SELECT 'M7B-C014', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Leukotriene pathway inhibition after SCI can reduce secondary injury-associated processes and improve functional endpoints in animal models.',
    'conclusion',
    'medium',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Lesion-bed analog.", "source_paper_tracker_id": "M7A-P030-P033", "topic_id": "M7B-T005", "tracker_id": "M7B-C015"}'
  FROM _m7_paper_map p
  WHERE p.tracker_id = 'M7A-P030'
  RETURNING claim_id
)
INSERT INTO _m7_claim_map (tracker_id, claim_id) SELECT 'M7B-C015', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'LTB4-BLT1 signaling links leukotriene biology to neutrophil infiltration and secondary SCI injury.',
    'mechanistic',
    'medium',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Phase 1 amplification.", "source_paper_tracker_id": "M7A-P031", "topic_id": "M7B-T005", "tracker_id": "M7B-C016"}'
  FROM _m7_paper_map p
  WHERE p.tracker_id = 'M7A-P031'
  RETURNING claim_id
)
INSERT INTO _m7_claim_map (tracker_id, claim_id) SELECT 'M7B-C016', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Pro-resolving lipid mediator strategies can improve inflammatory resolution and recovery-associated endpoints after SCI, but co-therapy rows need attribution boundaries.',
    'synthesis',
    'medium',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "D1 spheroid co-therapy boundary.", "source_paper_tracker_id": "M7A-P034-P035", "topic_id": "M7B-T005", "tracker_id": "M7B-C017"}'
  FROM _m7_paper_map p
  WHERE p.tracker_id = 'M7A-P034'
  RETURNING claim_id
)
INSERT INTO _m7_claim_map (tracker_id, claim_id) SELECT 'M7B-C017', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'SCI leukotriene/resolution evidence should be treated as lesion-bed conditioning analogy rather than direct preoperative reconstruction evidence.',
    'boundary condition',
    'high',
    'Module 7A tracker',
    'high',
    '{"curator_notes": "Translation boundary.", "source_paper_tracker_id": "M7A-P030-P035", "topic_id": "M7B-T005", "tracker_id": "M7B-C018"}'
  FROM _m7_paper_map p
  WHERE p.tracker_id = 'M7A-P030'
  RETURNING claim_id
)
INSERT INTO _m7_claim_map (tracker_id, claim_id) SELECT 'M7B-C018', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Tranilast scar studies support matrix-maturation biology but are mainly local/topical route evidence in this corpus.',
    'boundary condition',
    'high',
    'Abstract',
    'low',
    '{"curator_notes": "Not systemic host conditioning.", "source_paper_tracker_id": "M7A-P036-P037", "topic_id": "M7B-T006", "tracker_id": "M7B-C019"}'
  FROM _m7_paper_map p
  WHERE p.tracker_id = 'M7A-P036'
  RETURNING claim_id
)
INSERT INTO _m7_claim_map (tracker_id, claim_id) SELECT 'M7B-C019', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Module 7 synthesis must preserve whether the intervention targets the recipient host, graft/donor, scaffold/local depot, or transplanted cells.',
    'synthesis',
    'high',
    'Module 7A tracker',
    'high',
    '{"curator_notes": "Central ontology claim.", "source_paper_tracker_id": "M7A-P001-P040", "topic_id": "M7B-T007", "tracker_id": "M7B-C020"}'
  FROM _m7_paper_map p
  WHERE p.tracker_id = 'M7A-P001'
  RETURNING claim_id
)
INSERT INTO _m7_claim_map (tracker_id, claim_id) SELECT 'M7B-C020', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Route is a first-class variable because oral/systemic, transdermal, remote ischemic, biologic, local depot, and co-therapy interventions imply different host-conditioning strength.',
    'synthesis',
    'high',
    'Module 7A tracker',
    'high',
    '{"curator_notes": "Route ontology.", "source_paper_tracker_id": "M7A-P001-P040", "topic_id": "M7B-T007", "tracker_id": "M7B-C021"}'
  FROM _m7_paper_map p
  WHERE p.tracker_id = 'M7A-P001'
  RETURNING claim_id
)
INSERT INTO _m7_claim_map (tracker_id, claim_id) SELECT 'M7B-C021', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Timing is a first-class variable because prophylaxis, perioperative conditioning, post-injury treatment, chronic treatment, and recurrence prevention are not interchangeable.',
    'synthesis',
    'high',
    'Module 7A tracker',
    'high',
    '{"curator_notes": "Timing ontology.", "source_paper_tracker_id": "M7A-P001-P040", "topic_id": "M7B-T007", "tracker_id": "M7B-C022"}'
  FROM _m7_paper_map p
  WHERE p.tracker_id = 'M7A-P001'
  RETURNING claim_id
)
INSERT INTO _m7_claim_map (tracker_id, claim_id) SELECT 'M7B-C022', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Remodeling endpoints must be kept separate from survival, rejection, function, and engraftment endpoints.',
    'synthesis',
    'high',
    'Module 7A tracker',
    'high',
    '{"curator_notes": "Endpoint ontology.", "source_paper_tracker_id": "M7A-P001-P040", "topic_id": "M7B-T007", "tracker_id": "M7B-C023"}'
  FROM _m7_paper_map p
  WHERE p.tracker_id = 'M7A-P001'
  RETURNING claim_id
)
INSERT INTO _m7_claim_map (tracker_id, claim_id) SELECT 'M7B-C023', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Most Module 7B rows are abstract/source-page level and should remain confidence-limited until full text confirms dose, route, timing, and endpoint details.',
    'boundary condition',
    'high',
    'Module 7A tracker',
    'high',
    '{"curator_notes": "Evidence-quality boundary.", "source_paper_tracker_id": "M7A-P001-P040", "topic_id": "M7B-T008", "tracker_id": "M7B-C024"}'
  FROM _m7_paper_map p
  WHERE p.tracker_id = 'M7A-P001'
  RETURNING claim_id
)
INSERT INTO _m7_claim_map (tracker_id, claim_id) SELECT 'M7B-C024', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Cross-field evidence is hypothesis-generating for SCI reconstruction unless direct SCI reconstructive conditioning studies are available.',
    'synthesis',
    'high',
    'Review map',
    'medium',
    '{"curator_notes": "Translation boundary.", "source_paper_tracker_id": "M7A-R001-R008", "topic_id": "M7B-T008", "tracker_id": "M7B-C025"}'
  FROM _m7_paper_map p
  WHERE p.tracker_id = 'M7A-R001'
  RETURNING claim_id
)
INSERT INTO _m7_claim_map (tracker_id, claim_id) SELECT 'M7B-C025', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Review/meta-analysis rows support the existence of an implant prophylaxis literature but should not replace extraction from primary intervention studies.',
    'boundary condition',
    'high',
    'Review/source',
    'medium',
    '{"curator_notes": "Review boundary.", "source_paper_tracker_id": "M7A-P038-P040", "topic_id": "M7B-T001", "tracker_id": "M7B-C026"}'
  FROM _m7_paper_map p
  WHERE p.tracker_id = 'M7A-P038'
  RETURNING claim_id
)
INSERT INTO _m7_claim_map (tracker_id, claim_id) SELECT 'M7B-C026', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Neutral or negative islet autotransplant follow-up data should be retained as a contradiction to simple anti-inflammatory benefit claims.',
    'boundary condition',
    'high',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Important contradiction.", "source_paper_tracker_id": "M7A-P020", "topic_id": "M7B-T003", "tracker_id": "M7B-C027"}'
  FROM _m7_paper_map p
  WHERE p.tracker_id = 'M7A-P020'
  RETURNING claim_id
)
INSERT INTO _m7_claim_map (tracker_id, claim_id) SELECT 'M7B-C027', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Human reconstructive preconditioning evidence exists but is thin in this first-pass corpus.',
    'boundary condition',
    'medium',
    'Abstract',
    'low',
    '{"curator_notes": "Human flap RCT anchor.", "source_paper_tracker_id": "M7A-P014", "topic_id": "M7B-T002", "tracker_id": "M7B-C028"}'
  FROM _m7_paper_map p
  WHERE p.tracker_id = 'M7A-P014'
  RETURNING claim_id
)
INSERT INTO _m7_claim_map (tracker_id, claim_id) SELECT 'M7B-C028', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Recurrence-prevention studies are closest to perioperative reconstruction conditioning but still may involve patients with prior capsule biology.',
    'boundary condition',
    'medium',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Recurrence boundary.", "source_paper_tracker_id": "M7A-P006", "topic_id": "M7B-T001", "tracker_id": "M7B-C029"}'
  FROM _m7_paper_map p
  WHERE p.tracker_id = 'M7A-P006'
  RETURNING claim_id
)
INSERT INTO _m7_claim_map (tracker_id, claim_id) SELECT 'M7B-C029', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Early SCI anti-inflammatory or pro-resolving treatment may be relevant to future graft-bed preparation hypotheses.',
    'implication',
    'medium',
    'Module 7A tracker',
    'medium',
    '{"curator_notes": "Not direct reconstruction.", "source_paper_tracker_id": "M7A-P030-P035", "topic_id": "M7B-T005", "tracker_id": "M7B-C030"}'
  FROM _m7_paper_map p
  WHERE p.tracker_id = 'M7A-P030'
  RETURNING claim_id
)
INSERT INTO _m7_claim_map (tracker_id, claim_id) SELECT 'M7B-C030', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Biomaterial-delivered tolerogenic microparticles should be classified as host-directed immunomodulation only when the recipient immune response is the target endpoint.',
    'boundary condition',
    'high',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Local/scaffold nuance.", "source_paper_tracker_id": "M7A-P027", "topic_id": "M7B-T003", "tracker_id": "M7B-C031"}'
  FROM _m7_paper_map p
  WHERE p.tracker_id = 'M7A-P027'
  RETURNING claim_id
)
INSERT INTO _m7_claim_map (tracker_id, claim_id) SELECT 'M7B-C031', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Local scar studies are useful for Phase 4 matrix maturation but should be excluded from systemic-host-conditioning consensus claims.',
    'boundary condition',
    'high',
    'Module 7A tracker',
    'high',
    '{"curator_notes": "Local route.", "source_paper_tracker_id": "M7A-P036-P037", "topic_id": "M7B-T006", "tracker_id": "M7B-C032"}'
  FROM _m7_paper_map p
  WHERE p.tracker_id = 'M7A-P036'
  RETURNING claim_id
)
INSERT INTO _m7_claim_map (tracker_id, claim_id) SELECT 'M7B-C032', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Leukotriene antagonist implant evidence is triangulated across clinical reports, recurrence-prevention studies, and reviews, but agent, dose, indication, and evidence-quality boundaries remain important.',
    'synthesis',
    'high',
    'Abstract/source page and review map',
    'medium',
    '{"curator_notes": "Keeps LTRA claim strong but bounded.", "source_paper_tracker_id": "M7A-P001, P006, P039-P040", "topic_id": "M7B-T001", "tracker_id": "M7B-C033"}'
  FROM _m7_paper_map p
  WHERE p.tracker_id = 'M7A-P001'
  RETURNING claim_id
)
INSERT INTO _m7_claim_map (tracker_id, claim_id) SELECT 'M7B-C033', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Flap preconditioning includes a mechanistic host-cell mobilization signal and at least one human reconstruction trial, but the corpus remains thin for remodeling-specific endpoints.',
    'synthesis',
    'medium',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Completes human/flap boundary.", "source_paper_tracker_id": "M7A-P012, P014", "topic_id": "M7B-T002", "tracker_id": "M7B-C034"}'
  FROM _m7_paper_map p
  WHERE p.tracker_id = 'M7A-P012'
  RETURNING claim_id
)
INSERT INTO _m7_claim_map (tracker_id, claim_id) SELECT 'M7B-C034', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Human islet autotransplant studies show that peri-transplant anti-inflammatory conditioning can be tested clinically, but early engraftment rationale may not translate into durable diabetes-outcome benefit.',
    'boundary condition',
    'high',
    'Abstract/source page',
    'medium',
    '{"curator_notes": "Strengthens contradiction handling.", "source_paper_tracker_id": "M7A-P018-P020", "topic_id": "M7B-T003", "tracker_id": "M7B-C035"}'
  FROM _m7_paper_map p
  WHERE p.tracker_id = 'M7A-P018'
  RETURNING claim_id
)
INSERT INTO _m7_claim_map (tracker_id, claim_id) SELECT 'M7B-C035', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO AuthorClaim (
    paper_id, claim_text, claim_type, confidence_level, source_section, extraction_confidence, notes
  )
  SELECT p.paper_id,
    'Module 7 evidence should be graded by directness for SCI reconstruction: direct reconstructive/implant conditioning, transplant engraftment conditioning, SCI lesion-bed analogs, and local scar biology are different evidence tiers.',
    'synthesis',
    'high',
    'Module 7A tracker',
    'high',
    '{"curator_notes": "Evidence-tier ontology.", "source_paper_tracker_id": "M7A-P001-P040", "topic_id": "M7B-T007", "tracker_id": "M7B-C036"}'
  FROM _m7_paper_map p
  WHERE p.tracker_id = 'M7A-P001'
  RETURNING claim_id
)
INSERT INTO _m7_claim_map (tracker_id, claim_id) SELECT 'M7B-C036', claim_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Zafirlukast clinical row", "strength": "low", "tracker_id": "M7B-L001"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O001'
  WHERE c.tracker_id = 'M7B-C001'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L001', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "LTRA prophylaxis comparison", "strength": "low", "tracker_id": "M7B-L002"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O004'
  WHERE c.tracker_id = 'M7B-C001'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L002', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Recurrence prevention", "strength": "medium", "tracker_id": "M7B-L003"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O006'
  WHERE c.tracker_id = 'M7B-C001'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L003', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "LTRA review/meta-analysis", "strength": "medium", "tracker_id": "M7B-L004"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O039'
  WHERE c.tracker_id = 'M7B-C001'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L004', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "LTRA meta-analysis", "strength": "medium", "tracker_id": "M7B-L005"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O040'
  WHERE c.tracker_id = 'M7B-C001'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L005', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Pirfenidone prevention", "strength": "low", "tracker_id": "M7B-L006"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O002'
  WHERE c.tracker_id = 'M7B-C002'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L006', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Pirfenidone clinical treatment", "strength": "low", "tracker_id": "M7B-L007"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O003'
  WHERE c.tracker_id = 'M7B-C002'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L007', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Tranilast comparator", "strength": "medium", "tracker_id": "M7B-L008"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O007'
  WHERE c.tracker_id = 'M7B-C003'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L008', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Tamoxifen mouse implant", "strength": "medium", "tracker_id": "M7B-L009"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O008'
  WHERE c.tracker_id = 'M7B-C004'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L009', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Transdermal tamoxifen", "strength": "medium", "tracker_id": "M7B-L010"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O009'
  WHERE c.tracker_id = 'M7B-C004'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L010', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Treatment/prevention ambiguity", "strength": "low", "tracker_id": "M7B-L011"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O001'
  WHERE c.tracker_id = 'M7B-C005'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L011', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Established contracture treatment", "strength": "low", "tracker_id": "M7B-L012"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O003'
  WHERE c.tracker_id = 'M7B-C005'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L012', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Prophylaxis", "strength": "low", "tracker_id": "M7B-L013"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O004'
  WHERE c.tracker_id = 'M7B-C005'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L013', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Recurrence prevention", "strength": "medium", "tracker_id": "M7B-L014"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O006'
  WHERE c.tracker_id = 'M7B-C005'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L014', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Innate preconditioning", "strength": "low", "tracker_id": "M7B-L015"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O010'
  WHERE c.tracker_id = 'M7B-C006'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L015', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Remote ischemic signaling", "strength": "low", "tracker_id": "M7B-L016"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O011'
  WHERE c.tracker_id = 'M7B-C006'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L016', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Systemic HIF preconditioning", "strength": "medium", "tracker_id": "M7B-L017"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O012'
  WHERE c.tracker_id = 'M7B-C006'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L017', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Human free-flap RCT", "strength": "low", "tracker_id": "M7B-L018"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O014'
  WHERE c.tracker_id = 'M7B-C006'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L018', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Host-cell mobilization", "strength": "medium", "tracker_id": "M7B-L019"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O012'
  WHERE c.tracker_id = 'M7B-C007'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L019', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Survival endpoint", "strength": "low", "tracker_id": "M7B-L020"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O010'
  WHERE c.tracker_id = 'M7B-C008'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L020', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Flap timing/survival", "strength": "low", "tracker_id": "M7B-L021"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O013'
  WHERE c.tracker_id = 'M7B-C008'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L021', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Reconstruction trial endpoint unspecified", "strength": "low", "tracker_id": "M7B-L022"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O014'
  WHERE c.tracker_id = 'M7B-C008'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L022', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "A1AT IBMIR", "strength": "medium", "tracker_id": "M7B-L023"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O015'
  WHERE c.tracker_id = 'M7B-C009'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L023', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Mouse survival", "strength": "low", "tracker_id": "M7B-L024"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O016'
  WHERE c.tracker_id = 'M7B-C009'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L024', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Macrophage activation", "strength": "medium", "tracker_id": "M7B-L025"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O017'
  WHERE c.tracker_id = 'M7B-C009'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L025', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Human pilot trial", "strength": "medium", "tracker_id": "M7B-L026"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O018'
  WHERE c.tracker_id = 'M7B-C009'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L026', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Human RCT test", "strength": "medium", "tracker_id": "M7B-L027"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O019'
  WHERE c.tracker_id = 'M7B-C009'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L027', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contradicts',
  '{"notes": "Follow-up neutral outcome", "strength": "medium", "tracker_id": "M7B-L028"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O020'
  WHERE c.tracker_id = 'M7B-C009'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L028', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "IBMIR A1AT", "strength": "medium", "tracker_id": "M7B-L029"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O015'
  WHERE c.tracker_id = 'M7B-C010'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L029', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Sulfated dextran", "strength": "medium", "tracker_id": "M7B-L030"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O021'
  WHERE c.tracker_id = 'M7B-C010'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L030', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "C5a inhibition", "strength": "low", "tracker_id": "M7B-L031"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O022'
  WHERE c.tracker_id = 'M7B-C010'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L031', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Macrophage activation", "strength": "medium", "tracker_id": "M7B-L032"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O017'
  WHERE c.tracker_id = 'M7B-C011'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L032', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Chemokine blockade", "strength": "medium", "tracker_id": "M7B-L033"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O023'
  WHERE c.tracker_id = 'M7B-C011'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L033', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Macrophage depletion", "strength": "low", "tracker_id": "M7B-L034"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O024'
  WHERE c.tracker_id = 'M7B-C011'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L034', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Apoptotic cell/Treg/DC", "strength": "medium", "tracker_id": "M7B-L035"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O025'
  WHERE c.tracker_id = 'M7B-C012'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L035', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Treg expansion", "strength": "low", "tracker_id": "M7B-L036"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O026'
  WHERE c.tracker_id = 'M7B-C012'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L036', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Tolerogenic microparticles", "strength": "medium", "tracker_id": "M7B-L037"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O027'
  WHERE c.tracker_id = 'M7B-C012'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L037', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Engraftment endpoint", "strength": "medium", "tracker_id": "M7B-L038"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O015'
  WHERE c.tracker_id = 'M7B-C013'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L038', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Diabetes outcome endpoint", "strength": "medium", "tracker_id": "M7B-L039"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O020'
  WHERE c.tracker_id = 'M7B-C013'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L039', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Survival endpoint", "strength": "medium", "tracker_id": "M7B-L040"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O023'
  WHERE c.tracker_id = 'M7B-C013'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L040', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Rejection-centered heart transplant", "strength": "medium", "tracker_id": "M7B-L041"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O028'
  WHERE c.tracker_id = 'M7B-C014'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L041', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Chronic rejection/tolerance", "strength": "low", "tracker_id": "M7B-L042"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O029'
  WHERE c.tracker_id = 'M7B-C014'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L042', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Zileuton/montelukast SCI", "strength": "medium", "tracker_id": "M7B-L043"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O030'
  WHERE c.tracker_id = 'M7B-C015'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L043', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Zafirlukast combo SCI", "strength": "low", "tracker_id": "M7B-L044"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O032'
  WHERE c.tracker_id = 'M7B-C015'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L044', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Zileuton ferroptosis", "strength": "low", "tracker_id": "M7B-L045"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O033'
  WHERE c.tracker_id = 'M7B-C015'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L045', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "LTB4-BLT1 neutrophils", "strength": "medium", "tracker_id": "M7B-L046"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O031'
  WHERE c.tracker_id = 'M7B-C016'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L046', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Resolvin D3", "strength": "medium", "tracker_id": "M7B-L047"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O034'
  WHERE c.tracker_id = 'M7B-C017'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L047', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Resolvin D1 co-therapy", "strength": "medium", "tracker_id": "M7B-L048"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O035'
  WHERE c.tracker_id = 'M7B-C017'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L048', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "SCI not reconstruction", "strength": "high", "tracker_id": "M7B-L049"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O030'
  WHERE c.tracker_id = 'M7B-C018'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L049', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Co-therapy/SCI boundary", "strength": "high", "tracker_id": "M7B-L050"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O035'
  WHERE c.tracker_id = 'M7B-C018'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L050', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Topical tranilast", "strength": "low", "tracker_id": "M7B-L051"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O036'
  WHERE c.tracker_id = 'M7B-C019'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L051', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Microneedle tranilast", "strength": "low", "tracker_id": "M7B-L052"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O037'
  WHERE c.tracker_id = 'M7B-C019'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L052', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Biomaterial but host-directed", "strength": "medium", "tracker_id": "M7B-L053"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O027'
  WHERE c.tracker_id = 'M7B-C020'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L053', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Cell co-therapy", "strength": "medium", "tracker_id": "M7B-L054"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O035'
  WHERE c.tracker_id = 'M7B-C020'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L054', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Transdermal route", "strength": "medium", "tracker_id": "M7B-L055"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O009'
  WHERE c.tracker_id = 'M7B-C021'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L055', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Systemic route", "strength": "medium", "tracker_id": "M7B-L056"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O012'
  WHERE c.tracker_id = 'M7B-C021'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L056', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Local route", "strength": "low", "tracker_id": "M7B-L057"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O036'
  WHERE c.tracker_id = 'M7B-C021'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L057', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Prophylaxis", "strength": "low", "tracker_id": "M7B-L058"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O004'
  WHERE c.tracker_id = 'M7B-C022'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L058', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Recurrence prevention", "strength": "medium", "tracker_id": "M7B-L059"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O006'
  WHERE c.tracker_id = 'M7B-C022'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L059', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Post-injury treatment", "strength": "medium", "tracker_id": "M7B-L060"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O030'
  WHERE c.tracker_id = 'M7B-C022'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L060', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Survival endpoint", "strength": "low", "tracker_id": "M7B-L061"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O010'
  WHERE c.tracker_id = 'M7B-C023'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L061', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Engraftment endpoint", "strength": "medium", "tracker_id": "M7B-L062"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O015'
  WHERE c.tracker_id = 'M7B-C023'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L062', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Rejection endpoint", "strength": "medium", "tracker_id": "M7B-L063"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O028'
  WHERE c.tracker_id = 'M7B-C023'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L063', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Low-confidence example", "strength": "high", "tracker_id": "M7B-L064"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O001'
  WHERE c.tracker_id = 'M7B-C024'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L064', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Abstract-level recent row", "strength": "high", "tracker_id": "M7B-L065"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O033'
  WHERE c.tracker_id = 'M7B-C024'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L065', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Human reconstruction but vascular", "strength": "low", "tracker_id": "M7B-L066"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O014'
  WHERE c.tracker_id = 'M7B-C025'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L066', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "SCI analogy", "strength": "medium", "tracker_id": "M7B-L067"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O030'
  WHERE c.tracker_id = 'M7B-C025'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L067', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Review synthesis", "strength": "medium", "tracker_id": "M7B-L068"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O038'
  WHERE c.tracker_id = 'M7B-C026'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L068', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Review/meta-analysis", "strength": "medium", "tracker_id": "M7B-L069"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O039'
  WHERE c.tracker_id = 'M7B-C026'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L069', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Review/meta-analysis", "strength": "medium", "tracker_id": "M7B-L070"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O040'
  WHERE c.tracker_id = 'M7B-C026'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L070', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Neutral/negative follow-up", "strength": "medium", "tracker_id": "M7B-L071"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O020'
  WHERE c.tracker_id = 'M7B-C027'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L071', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Human flap RCT", "strength": "low", "tracker_id": "M7B-L072"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O014'
  WHERE c.tracker_id = 'M7B-C028'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L072', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Recurrence prevention", "strength": "medium", "tracker_id": "M7B-L073"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O006'
  WHERE c.tracker_id = 'M7B-C029'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L073', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Leukotriene SCI", "strength": "medium", "tracker_id": "M7B-L074"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O030'
  WHERE c.tracker_id = 'M7B-C030'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L074', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Resolvin SCI", "strength": "medium", "tracker_id": "M7B-L075"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O034'
  WHERE c.tracker_id = 'M7B-C030'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L075', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Tolerogenic microparticle endpoint", "strength": "medium", "tracker_id": "M7B-L076"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O027'
  WHERE c.tracker_id = 'M7B-C031'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L076', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Local scar gel", "strength": "low", "tracker_id": "M7B-L077"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O036'
  WHERE c.tracker_id = 'M7B-C032'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L077', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Local scar microneedle", "strength": "low", "tracker_id": "M7B-L078"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O037'
  WHERE c.tracker_id = 'M7B-C032'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L078', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Clinical zafirlukast evidence", "strength": "low", "tracker_id": "M7B-L079"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O001'
  WHERE c.tracker_id = 'M7B-C033'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L079', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Recurrence prevention evidence", "strength": "medium", "tracker_id": "M7B-L080"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O006'
  WHERE c.tracker_id = 'M7B-C033'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L080', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Review/meta-analysis evidence", "strength": "medium", "tracker_id": "M7B-L081"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O039'
  WHERE c.tracker_id = 'M7B-C033'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L081', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Host-cell mobilization signal", "strength": "medium", "tracker_id": "M7B-L082"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O012'
  WHERE c.tracker_id = 'M7B-C034'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L082', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'supports',
  '{"notes": "Human reconstruction trial anchor", "strength": "low", "tracker_id": "M7B-L083"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O014'
  WHERE c.tracker_id = 'M7B-C034'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L083', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Human anti-inflammatory trial", "strength": "medium", "tracker_id": "M7B-L084"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O018'
  WHERE c.tracker_id = 'M7B-C035'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L084', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contradicts_simple_benefit',
  '{"notes": "Neutral/negative long-term outcome", "strength": "medium", "tracker_id": "M7B-L085"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O020'
  WHERE c.tracker_id = 'M7B-C035'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L085', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Direct implant reconstruction tier", "strength": "medium", "tracker_id": "M7B-L086"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O038'
  WHERE c.tracker_id = 'M7B-C036'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L086', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "Transplant engraftment tier", "strength": "medium", "tracker_id": "M7B-L087"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O015'
  WHERE c.tracker_id = 'M7B-C036'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L087', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO EvidenceLink (claim_id, observation_id, link_type, notes)
  SELECT c.claim_id, o.observation_id,
  'contextual_support',
  '{"notes": "SCI lesion-bed analog tier", "strength": "medium", "tracker_id": "M7B-L088"}'
  FROM _m7_claim_map c
  JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O030'
  WHERE c.tracker_id = 'M7B-C036'
  RETURNING link_id
)
INSERT INTO _m7_link_map (tracker_id, link_id) SELECT 'M7B-L088', link_id FROM inserted;

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Breast implant capsular contracture provides the strongest direct precedent that recipient-directed pharmacologic conditioning can alter fibrotic capsule outcomes, especially through leukotriene antagonists and anti-fibrotic or anti-estrogen strategies.',
    'M7B-T001',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M7B-B001", "M7B-B002", "M7B-B007", "M7B-B008"], "claim_tracker_ids": ["M7B-C001", "M7B-C002", "M7B-C003", "M7B-C004", "M7B-C005", "M7B-C026", "M7B-C029", "M7B-C033"], "consensus_draft_id": "M7B-S001", "observation_tracker_ids": ["M7B-O001", "M7B-O002", "M7B-O003", "M7B-O004", "M7B-O005", "M7B-O006", "M7B-O007", "M7B-O008", "M7B-O009", "M7B-O038", "M7B-O039", "M7B-O040"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": "moderate", "supporting_evidence_notes": null, "topic_id": "M7B-T001"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m7_consensus_map (tracker_id, consensus_id) SELECT 'M7B-S001', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O001'
WHERE c.tracker_id = 'M7B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O002'
WHERE c.tracker_id = 'M7B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O003'
WHERE c.tracker_id = 'M7B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O004'
WHERE c.tracker_id = 'M7B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O005'
WHERE c.tracker_id = 'M7B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O006'
WHERE c.tracker_id = 'M7B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O007'
WHERE c.tracker_id = 'M7B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O008'
WHERE c.tracker_id = 'M7B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O009'
WHERE c.tracker_id = 'M7B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O038'
WHERE c.tracker_id = 'M7B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O039'
WHERE c.tracker_id = 'M7B-S001';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O040'
WHERE c.tracker_id = 'M7B-S001';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Flap and ischemic-tissue studies show that recipient or remote systemic preconditioning can improve vascular survival biology before tissue transfer, but this is not yet equivalent to anti-fibrotic recipient-bed conditioning.',
    'M7B-T002',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M7B-B003", "M7B-B008"], "claim_tracker_ids": ["M7B-C006", "M7B-C007", "M7B-C008", "M7B-C028", "M7B-C034"], "consensus_draft_id": "M7B-S002", "observation_tracker_ids": ["M7B-O010", "M7B-O011", "M7B-O012", "M7B-O013", "M7B-O014"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": "mixed", "supporting_evidence_notes": null, "topic_id": "M7B-T002"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m7_consensus_map (tracker_id, consensus_id) SELECT 'M7B-S002', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O010'
WHERE c.tracker_id = 'M7B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O011'
WHERE c.tracker_id = 'M7B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O012'
WHERE c.tracker_id = 'M7B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O013'
WHERE c.tracker_id = 'M7B-S002';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O014'
WHERE c.tracker_id = 'M7B-S002';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Islet transplantation supports peri-transplant host conditioning as a strategy to reduce early inflammatory engraftment barriers, including IBMIR, complement/coagulation signaling, macrophage activation, chemokine recruitment, and regulatory immune balance.',
    'M7B-T003',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M7B-B004", "M7B-B007", "M7B-B008"], "claim_tracker_ids": ["M7B-C009", "M7B-C010", "M7B-C011", "M7B-C012", "M7B-C013", "M7B-C027", "M7B-C031", "M7B-C035"], "consensus_draft_id": "M7B-S003", "observation_tracker_ids": ["M7B-O015", "M7B-O016", "M7B-O017", "M7B-O018", "M7B-O019", "M7B-O020", "M7B-O021", "M7B-O022", "M7B-O023", "M7B-O024", "M7B-O025", "M7B-O026", "M7B-O027"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": "mixed", "supporting_evidence_notes": null, "topic_id": "M7B-T003"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m7_consensus_map (tracker_id, consensus_id) SELECT 'M7B-S003', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O015'
WHERE c.tracker_id = 'M7B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O016'
WHERE c.tracker_id = 'M7B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O017'
WHERE c.tracker_id = 'M7B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O018'
WHERE c.tracker_id = 'M7B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O019'
WHERE c.tracker_id = 'M7B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O020'
WHERE c.tracker_id = 'M7B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O021'
WHERE c.tracker_id = 'M7B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O022'
WHERE c.tracker_id = 'M7B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O023'
WHERE c.tracker_id = 'M7B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O024'
WHERE c.tracker_id = 'M7B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O025'
WHERE c.tracker_id = 'M7B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O026'
WHERE c.tracker_id = 'M7B-S003';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O027'
WHERE c.tracker_id = 'M7B-S003';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Organ tolerance studies are useful for the host-conditioning concept but should remain boundary evidence unless rejection control is linked to remodeling, vascular integration, fibrosis, or functional graft integration.',
    'M7B-T004',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M7B-B005"], "claim_tracker_ids": ["M7B-C014"], "consensus_draft_id": "M7B-S004", "observation_tracker_ids": ["M7B-O028", "M7B-O029"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": "low/mixed", "supporting_evidence_notes": null, "topic_id": "M7B-T004"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m7_consensus_map (tracker_id, consensus_id) SELECT 'M7B-S004', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O028'
WHERE c.tracker_id = 'M7B-S004';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O029'
WHERE c.tracker_id = 'M7B-S004';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'SCI leukotriene and pro-resolving mediator studies support the plausibility that early fibroinflammatory lesion-bed state can be modified, but they are analogs rather than direct preoperative reconstruction studies.',
    'M7B-T005',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M7B-B006", "M7B-B008"], "claim_tracker_ids": ["M7B-C015", "M7B-C016", "M7B-C017", "M7B-C018", "M7B-C030"], "consensus_draft_id": "M7B-S005", "observation_tracker_ids": ["M7B-O030", "M7B-O031", "M7B-O032", "M7B-O033", "M7B-O034", "M7B-O035"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": "moderate", "supporting_evidence_notes": null, "topic_id": "M7B-T005"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m7_consensus_map (tracker_id, consensus_id) SELECT 'M7B-S005', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O030'
WHERE c.tracker_id = 'M7B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O031'
WHERE c.tracker_id = 'M7B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O032'
WHERE c.tracker_id = 'M7B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O033'
WHERE c.tracker_id = 'M7B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O034'
WHERE c.tracker_id = 'M7B-S005';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O035'
WHERE c.tracker_id = 'M7B-S005';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Tranilast scar and hypertrophic-scar studies inform matrix-maturation biology, but local or topical delivery rows should not be used as evidence for systemic host conditioning.',
    'M7B-T006',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M7B-B007"], "claim_tracker_ids": ["M7B-C019", "M7B-C032"], "consensus_draft_id": "M7B-S006", "observation_tracker_ids": ["M7B-O036", "M7B-O037"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": "low", "supporting_evidence_notes": null, "topic_id": "M7B-T006"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m7_consensus_map (tracker_id, consensus_id) SELECT 'M7B-S006', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O036'
WHERE c.tracker_id = 'M7B-S006';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O037'
WHERE c.tracker_id = 'M7B-S006';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Module 7 host-conditioning synthesis requires an explicit ontology for intervention target, route, timing, procedure class, endpoint, and evidence directness, because the corpus spans systemic drugs, remote ischemic conditioning, local delivery, immune-cell modulation, and co-therapy.',
    'M7B-T007',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M7B-B001", "M7B-B002", "M7B-B003", "M7B-B004", "M7B-B005", "M7B-B006", "M7B-B007", "M7B-B008"], "claim_tracker_ids": ["M7B-C020", "M7B-C021", "M7B-C022", "M7B-C023", "M7B-C031", "M7B-C032", "M7B-C036"], "consensus_draft_id": "M7B-S007", "observation_tracker_ids": ["M7B-O001", "M7B-O002", "M7B-O003", "M7B-O004", "M7B-O005", "M7B-O006", "M7B-O007", "M7B-O008", "M7B-O009", "M7B-O010", "M7B-O011", "M7B-O012", "M7B-O013", "M7B-O014", "M7B-O015", "M7B-O016", "M7B-O017", "M7B-O018", "M7B-O019", "M7B-O020", "M7B-O021", "M7B-O022", "M7B-O023", "M7B-O024", "M7B-O025", "M7B-O026", "M7B-O027", "M7B-O028", "M7B-O029", "M7B-O030", "M7B-O031", "M7B-O032", "M7B-O033", "M7B-O034", "M7B-O035", "M7B-O036", "M7B-O037", "M7B-O038", "M7B-O039", "M7B-O040"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": "high on method, mixed on biology", "supporting_evidence_notes": null, "topic_id": "M7B-T007"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m7_consensus_map (tracker_id, consensus_id) SELECT 'M7B-S007', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O001'
WHERE c.tracker_id = 'M7B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O002'
WHERE c.tracker_id = 'M7B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O003'
WHERE c.tracker_id = 'M7B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O004'
WHERE c.tracker_id = 'M7B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O005'
WHERE c.tracker_id = 'M7B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O006'
WHERE c.tracker_id = 'M7B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O007'
WHERE c.tracker_id = 'M7B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O008'
WHERE c.tracker_id = 'M7B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O009'
WHERE c.tracker_id = 'M7B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O010'
WHERE c.tracker_id = 'M7B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O011'
WHERE c.tracker_id = 'M7B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O012'
WHERE c.tracker_id = 'M7B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O013'
WHERE c.tracker_id = 'M7B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O014'
WHERE c.tracker_id = 'M7B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O015'
WHERE c.tracker_id = 'M7B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O016'
WHERE c.tracker_id = 'M7B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O017'
WHERE c.tracker_id = 'M7B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O018'
WHERE c.tracker_id = 'M7B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O019'
WHERE c.tracker_id = 'M7B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O020'
WHERE c.tracker_id = 'M7B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O021'
WHERE c.tracker_id = 'M7B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O022'
WHERE c.tracker_id = 'M7B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O023'
WHERE c.tracker_id = 'M7B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O024'
WHERE c.tracker_id = 'M7B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O025'
WHERE c.tracker_id = 'M7B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O026'
WHERE c.tracker_id = 'M7B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O027'
WHERE c.tracker_id = 'M7B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O028'
WHERE c.tracker_id = 'M7B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O029'
WHERE c.tracker_id = 'M7B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O030'
WHERE c.tracker_id = 'M7B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O031'
WHERE c.tracker_id = 'M7B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O032'
WHERE c.tracker_id = 'M7B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O033'
WHERE c.tracker_id = 'M7B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O034'
WHERE c.tracker_id = 'M7B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O035'
WHERE c.tracker_id = 'M7B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O036'
WHERE c.tracker_id = 'M7B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O037'
WHERE c.tracker_id = 'M7B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O038'
WHERE c.tracker_id = 'M7B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O039'
WHERE c.tracker_id = 'M7B-S007';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O040'
WHERE c.tracker_id = 'M7B-S007';

WITH inserted AS (
  INSERT INTO Consensus (consensus_statement, topic, version, agreement_level, notes)
  VALUES (
    'Cross-field host-conditioning evidence is hypothesis-generating for SCI reconstruction and should remain confidence-stratified until full-text extraction confirms dose, route, timing, host target, and remodeling endpoint.',
    'M7B-T008',
    1,
    'consensus-ready first pass',
    '{"boundary_tracker_ids": ["M7B-B001", "M7B-B002", "M7B-B003", "M7B-B004", "M7B-B005", "M7B-B006", "M7B-B007", "M7B-B008"], "claim_tracker_ids": ["M7B-C024", "M7B-C025"], "consensus_draft_id": "M7B-S008", "observation_tracker_ids": ["M7B-O001", "M7B-O002", "M7B-O003", "M7B-O004", "M7B-O005", "M7B-O006", "M7B-O007", "M7B-O008", "M7B-O009", "M7B-O010", "M7B-O011", "M7B-O012", "M7B-O013", "M7B-O014", "M7B-O015", "M7B-O016", "M7B-O017", "M7B-O018", "M7B-O019", "M7B-O020", "M7B-O021", "M7B-O022", "M7B-O023", "M7B-O024", "M7B-O025", "M7B-O026", "M7B-O027", "M7B-O028", "M7B-O029", "M7B-O030", "M7B-O031", "M7B-O032", "M7B-O033", "M7B-O034", "M7B-O035", "M7B-O036", "M7B-O037", "M7B-O038", "M7B-O039", "M7B-O040"], "readiness_status": "CONSENSUS-READY FIRST PASS", "source_agreement_label": "high on method, mixed on biology", "supporting_evidence_notes": null, "topic_id": "M7B-T008"}'
  )
  RETURNING consensus_id
)
INSERT INTO _m7_consensus_map (tracker_id, consensus_id) SELECT 'M7B-S008', consensus_id FROM inserted;

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O001'
WHERE c.tracker_id = 'M7B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O002'
WHERE c.tracker_id = 'M7B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O003'
WHERE c.tracker_id = 'M7B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O004'
WHERE c.tracker_id = 'M7B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O005'
WHERE c.tracker_id = 'M7B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O006'
WHERE c.tracker_id = 'M7B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O007'
WHERE c.tracker_id = 'M7B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O008'
WHERE c.tracker_id = 'M7B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O009'
WHERE c.tracker_id = 'M7B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O010'
WHERE c.tracker_id = 'M7B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O011'
WHERE c.tracker_id = 'M7B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O012'
WHERE c.tracker_id = 'M7B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O013'
WHERE c.tracker_id = 'M7B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O014'
WHERE c.tracker_id = 'M7B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O015'
WHERE c.tracker_id = 'M7B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O016'
WHERE c.tracker_id = 'M7B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O017'
WHERE c.tracker_id = 'M7B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O018'
WHERE c.tracker_id = 'M7B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O019'
WHERE c.tracker_id = 'M7B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O020'
WHERE c.tracker_id = 'M7B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O021'
WHERE c.tracker_id = 'M7B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O022'
WHERE c.tracker_id = 'M7B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O023'
WHERE c.tracker_id = 'M7B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O024'
WHERE c.tracker_id = 'M7B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O025'
WHERE c.tracker_id = 'M7B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O026'
WHERE c.tracker_id = 'M7B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O027'
WHERE c.tracker_id = 'M7B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O028'
WHERE c.tracker_id = 'M7B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O029'
WHERE c.tracker_id = 'M7B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O030'
WHERE c.tracker_id = 'M7B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O031'
WHERE c.tracker_id = 'M7B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O032'
WHERE c.tracker_id = 'M7B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O033'
WHERE c.tracker_id = 'M7B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O034'
WHERE c.tracker_id = 'M7B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O035'
WHERE c.tracker_id = 'M7B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O036'
WHERE c.tracker_id = 'M7B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O037'
WHERE c.tracker_id = 'M7B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O038'
WHERE c.tracker_id = 'M7B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O039'
WHERE c.tracker_id = 'M7B-S008';

INSERT INTO Consensus_Observation (consensus_id, observation_id, support_type)
SELECT c.consensus_id, o.observation_id, 'supporting'
FROM _m7_consensus_map c
JOIN _m7_observation_map o ON o.tracker_id = 'M7B-O040'
WHERE c.tracker_id = 'M7B-S008';

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
  SELECT COUNT(*) INTO paper_count FROM _m7_paper_map;
  SELECT COUNT(*) INTO experiment_count FROM _m7_experiment_map;
  SELECT COUNT(*) INTO observation_count FROM _m7_observation_map;
  SELECT COUNT(*) INTO claim_count FROM _m7_claim_map;
  SELECT COUNT(*) INTO link_count FROM _m7_link_map;
  SELECT COUNT(*) INTO consensus_count FROM _m7_consensus_map;
  SELECT COUNT(*) INTO consensus_observation_count
  FROM Consensus_Observation co
  JOIN _m7_consensus_map cm ON cm.consensus_id = co.consensus_id;
  IF paper_count <> 48 THEN RAISE EXCEPTION 'Expected 48 papers, found %', paper_count; END IF;
  IF experiment_count <> 40 THEN RAISE EXCEPTION 'Unexpected experiment count %', experiment_count; END IF;
  IF observation_count <> 40 THEN RAISE EXCEPTION 'Expected 40 observations, found %', observation_count; END IF;
  IF claim_count <> 36 THEN RAISE EXCEPTION 'Expected 36 claims, found %', claim_count; END IF;
  IF link_count <> 88 THEN RAISE EXCEPTION 'Expected 88 evidence links, found %', link_count; END IF;
  IF consensus_count <> 8 THEN RAISE EXCEPTION 'Expected 8 consensus rows, found %', consensus_count; END IF;
  IF consensus_observation_count <> 120 THEN RAISE EXCEPTION 'Unexpected consensus-observation count %', consensus_observation_count; END IF;
END $$;

COMMIT;
